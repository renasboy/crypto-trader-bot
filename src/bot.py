import json
import websocket
from influxdb import InfluxDBClient

def on_message(ws, message):
    global prev_price
    global last_trade_session
    global last_trade_price
    global last_trade_action 

    print('websocket message {}'.format(message))
    msg = json.loads(message)

    price = msg['price_int'] * 0.00001
    volume = msg['amount_int'] * 0.000000001
    fee = price * 0.0025 * 2

    trend_up = price - prev_price if prev_price and price > prev_price else 0
    trend_down = prev_price - price if prev_price and price < prev_price else 0

    influx.write_points([dict(
        measurement='price_volume',
        tags=dict(
            type=msg['type']
        ),
        fields=dict(
            timestamp=msg['date'],
            price_src=msg['price_int'],
            volume_src=msg['amount_int'],
            price=float(price),
            volume=float(volume),
            trend_up=float(trend_up),
            trend_down=float(trend_down)
        )
    )])

    # RSI 14
    query_rsi =  'SELECT 100 - 100 / ((moving_average(mean(trend_up), 14) / moving_average(mean(trend_down), 14)) + 1) as rsi FROM price_volume WHERE time > now() - 1h GROUP BY time(1m) fill(linear)'
    result = influx.query(query_rsi)
    results = list(result.get_points())
    rsi = results[-1]['rsi'] if results else 50

    # MACD 12, 26, 9
    query_macd =  'SELECT mean(proper) - moving_average(mean(proper), 9) as macd FROM (SELECT moving_average(mean(price), 12) - moving_average(mean(price), 26) as proper FROM price_volume WHERE time > now() - 5h GROUP BY time(1m) fill(linear)) WHERE time > now() - 1d GROUP BY time(1m) fill(linear)'
    result = influx.query(query_macd)
    results = list(result.get_points())
    macd_last = results[-1]['macd'] if results else 0
    macd_prev = results[-2]['macd'] if results and len(results) > 1 else 0
    macd_trend = None
    if macd_prev < macd_last:
        macd_trend = 'up'
        if macd_prev <= 0 and macd_last > 0:
            macd_trend = 'breakup'
    elif macd_prev > macd_last:
        macd_trend = 'down'
        if macd_prev > 0 and macd_last <= 0:
            macd_trend = 'breakdown'

    print('macd trend {} macd {} rsi {} trend up {} trend down {}'.format(macd_trend, macd_last, rsi, trend_up, trend_down))

    # HOURLY, DAILY, WEEKLY and MONTHLY AVERAGES
    query_min_mean_max = 'SELECT min(price), mean(price), max(price) FROM price_volume WHERE time >= now() - {} GROUP BY time({}) fill(linear) ORDER BY time DESC LIMIT 1'

    query_hour = query_min_mean_max.format('2h', '1h')
    query_day = query_min_mean_max.format('48h', '24h')
    query_week = query_min_mean_max.format('14d', '7d')
    query_month = query_min_mean_max.format('60d', '30d')

    result = influx.query(query_hour)
    results = list(result.get_points())
    hour_avg = results[0]['mean'] if results else 0
    hour_min = results[0]['min'] if results else 0
    hour_max = results[0]['max'] if results else 0

    result = influx.query(query_day)
    results = list(result.get_points())
    day_avg = results[0]['mean'] if results else 0
    day_min = results[0]['min'] if results else 0
    day_max = results[0]['max'] if results else 0

    result = influx.query(query_week)
    results = list(result.get_points())
    week_avg = results[0]['mean'] if results else 0
    week_min = results[0]['min'] if results else 0
    week_max = results[0]['max'] if results else 0

    result = influx.query(query_month)
    results = list(result.get_points())
    month_avg = results[0]['mean'] if results else 0
    month_min = results[0]['min'] if results else 0
    month_max = results[0]['max'] if results else 0

    # TAKE ACTION
    action = None
    if last_trade_action != 'buy' and macd_trend == 'breakup' and rsi < 80 and price == min([price, hour_avg, day_avg]):
        action = 'buy'
        last_trade_session += 1
    elif last_trade_action == 'buy' and macd_trend == 'breakdown' and rsi > 20 and price > last_trade_price + fee:
        action = 'sell'

    if action != None:
        volume = 1.0
        print('action {} price {} session {}'.format(action, price, last_trade_session))
        influx.write_points([dict(
            measurement='trade',
            tags=dict(
                type=action,
                session=str(last_trade_session).rjust(30, '0')
            ),
            fields=dict(
                price=float(price),
                volume=float(volume),
                fee=float(fee),
            )
        )])
        last_trade_action = action
        last_trade_price = float(price)

    prev_price = price 

def on_error(ws, error):
    print('websocket error {}'.format(error))

def on_close(ws):
    print('websocket closed')

def on_open(ws):
    print('websocket open')

if __name__ == '__main__':
    influx = InfluxDBClient('influxdb', 8086, 'root', 'root', 'crypto_trader_bot')

    result = influx.query('SELECT price FROM price_volume ORDER BY time DESC limit 1')
    results = list(result.get_points())
    prev_price = results[0]['price'] if results else 0

    result = influx.query('SELECT price, type, session FROM trade ORDER BY time DESC limit 1')
    results = list(result.get_points())
    last_trade_session = int(results[0]['session']) if results else 0
    last_trade_action = str(results[0]['type']) if results else None
    last_trade_price = float(results[0]['price']) if results else 0
    print('started session {} action {} price {}'.format(last_trade_session, last_trade_action, last_trade_price))

    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        'wss://api.bl3p.eu/1/BTCEUR/trades',
        on_message = on_message,
        on_error = on_error,
        on_close = on_close
    )
    ws.on_open = on_open
    ws.run_forever()
