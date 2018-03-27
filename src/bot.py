import time
import os
import datetime
from influxdb import InfluxDBClient

def ma(period):
    query_ma =  "SELECT moving_average(mean(price), {}) as ma FROM price_volume WHERE exchange = '{}' and symbol_1 = '{}' and symbol_2 = '{}' and time > now() - 1h GROUP BY time(1m) fill(linear) ORDER BY time DESC limit 2".format(period, EXCHANGE, SYMBOL_1, SYMBOL_2)
    if period == 1:
        query_ma =  "SELECT mean(price) as ma FROM price_volume WHERE exchange = '{}' and symbol_1 = '{}' and symbol_2 = '{}' and time > now() - 1h GROUP BY time(1m) fill(linear) ORDER BY time DESC limit 2".format(EXCHANGE, SYMBOL_1, SYMBOL_2)
    result = influx.query(query_ma)
    results = list(result.get_points())
    ma_last = results[0]['ma'] if results and len(results) == 2 and results[0]['ma'] is not None else 0
    ma_prev = results[1]['ma'] if results and len(results) == 2 and results[1]['ma'] is not None else 0
    return float(ma_last), float(ma_prev)

def on_message(ws, message):
    global exchange
    global active_order_id
    global prev_price
    global macd_prev
    global last_trade_time
    global last_trade_session
    global last_trade_action
    global last_trade_price

    print('websocket message {}'.format(message))

    timest, type, price, volume, fee = exchange.parse_ws_msg(message)

    trend_up = price - prev_price if prev_price and price > prev_price else 0
    trend_down = prev_price - price if prev_price and price < prev_price else 0
    prev_price = price

    influx.write_points([dict(
        measurement='price_volume',
        tags=dict(
            exchange=EXCHANGE,
            symbol_1=SYMBOL_1,
            symbol_2=SYMBOL_2,
            type=type
        ),
        fields=dict(
            timestamp=timest,
            price=float(price),
            volume=float(volume),
            trend_up=float(trend_up),
            trend_down=float(trend_down)
        )
    )])

    # TAKE ACTION
    action = None
    if BOT_ALGO == 'ro_cano':

        # MAs
        ma1_last, ma1_prev = ma(1)
        ma8_last, ma8_prev = ma(8)
        ma29_last, ma29_prev = ma(29)
        ma11_last, ma11_prev = ma(11)

        # salvagente, prezzo < last_trade_price - 0.5%
        if last_trade_action == 'buy' and price < last_trade_price - last_trade_price * 0.005:
            action = 'sell'
        # compRa solo se
        elif last_trade_action != 'buy':
            # subito dopo l'incrocio prezzo X ma8 la prezzo > ma8
            # compRa o vendi solo se ma8 => ma29
            if ma8_last >= ma29_last:
                if ma1_prev < ma8_prev and ma1_last > ma8_last:
                    action = 'buy'
        # vendi solo se
        elif last_trade_action == 'buy':
            # SUBITO DOPO L'INCROCIO PREZZO X MA10 IL PREZZO < MA11
            # e vendi anche se ma8 < ma29
            if (ma1_prev > ma11_prev and ma1_last < ma11_last) or ma8_last < ma29_last:
                action = 'sell'
                # ma anche solo se guadagno > 0.12%
                if price - last_trade_price >= 0 and price - last_trade_price < last_trade_price * 0.0012:
                    action = None
                # perdita < -0.13%
                if price - last_trade_price <= 0 and last_trade_price - price < last_trade_price * 0.0013:
                    action = None

    elif BOT_ALGO == 'boring_but_safe':

        # RSI 14
        query_rsi =  "SELECT 100 - 100 / ((moving_average(mean(trend_up), 14) / moving_average(mean(trend_down), 14)) + 1) as rsi FROM price_volume WHERE exchange = '{}' and symbol_1 = '{}' and symbol_2 = '{}' and time > now() - 1h GROUP BY time(1m) fill(linear)".format(EXCHANGE, SYMBOL_1, SYMBOL_2)
        result = influx.query(query_rsi)
        results = list(result.get_points())
        rsi = results[-1]['rsi'] if results else 50

        # MACD 12, 26, 9
        query_macd =  "SELECT mean(proper) - moving_average(mean(proper), 9) as macd FROM (SELECT moving_average(mean(price), 12) - moving_average(mean(price), 26) as proper FROM price_volume WHERE exchange = '{}' and symbol_1 = '{}' and symbol_2 = '{}' and time > now() - 5h GROUP BY time(1m) fill(linear)) WHERE time > now() - 1d GROUP BY time(1m) fill(linear)".format(EXCHANGE, SYMBOL_1, SYMBOL_2)
        result = influx.query(query_macd)
        results = list(result.get_points())
        macd_last = results[-1]['macd'] if results else 0
        macd_trend = None
        if macd_prev < macd_last:
            macd_trend = 'up'
            if macd_prev <= 0 and macd_last > 0:
                macd_trend = 'breakup'
        elif macd_prev > macd_last:
            macd_trend = 'down'
            if macd_prev > 0 and macd_last <= 0:
                macd_trend = 'breakdown'

        macd_prev = macd_last

        print('macd trend {} macd {} rsi {} trend up {} trend down {}'.format(macd_trend, macd_last, rsi, trend_up, trend_down))

        # HOURLY, DAILY, WEEKLY and MONTHLY AVERAGES
        query_min_mean_max = "SELECT min(price), mean(price), max(price) FROM price_volume WHERE exchange = '{}' and symbol_1 = '{}' and symbol_2 = '{}' and time >= now() - {} GROUP BY time({}) fill(linear) ORDER BY time DESC LIMIT 1"

        query_hour = query_min_mean_max.format(EXCHANGE, SYMBOL_1, SYMBOL_2, '2h', '1h')
        query_day = query_min_mean_max.format(EXCHANGE, SYMBOL_1, SYMBOL_2, '48h', '24h')
        query_week = query_min_mean_max.format(EXCHANGE, SYMBOL_1, SYMBOL_2, '14d', '7d')
        query_month = query_min_mean_max.format(EXCHANGE, SYMBOL_1, SYMBOL_2, '60d', '30d')

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

        if last_trade_action != 'buy' and macd_trend == 'breakup' and rsi < 80 and price == min([price, week_avg]):
            action = 'buy'
        elif last_trade_action == 'buy' and macd_trend == 'breakdown' and rsi > 20 and price > last_trade_price + (fee * 5):
            action = 'sell'

    if action != None:
        if not active_order_id:
            if action == 'buy':
                price = exchange.lowest_ask()
                volume = (exchange.balance(SYMBOL_2) * (float(MAX_SYMBOL_2_PERCENTAGE) / 100.0)) / price
            elif action == 'sell':
                price = exchange.highest_bid()
                volume = exchange.balance(SYMBOL_1) * (float(MAX_SYMBOL_1_PERCENTAGE) / 100.0)

            print('order action {} price {} volume {} session {}'.format(action, price, volume, last_trade_session))
            if not DRY_RUN:
                active_order_id = exchange.add_order(action, volume, price)
                print('order id {} '.format(active_order_id))
            else:
                active_order_id = last_trade_session + 1

    # AFTER CONFIRMATION
    if active_order_id and not exchange.orders():
        if not DRY_RUN:
            action, price, volume, fee = exchange.closed_order(active_order_id)
        if action:
            if action == 'buy':
                last_trade_session += 1
            influx.write_points([dict(
                measurement='trade',
                tags=dict(
                    exchange=EXCHANGE,
                    symbol_1=SYMBOL_1,
                    symbol_2=SYMBOL_2,
                    type=action,
                    session=str(last_trade_session).rjust(30, '0'),
                    order_id=active_order_id,
                ),
                fields=dict(
                    price=float(price),
                    volume=float(volume),
                    fee=float(fee),
                )
            )])

            # SAVE SESSION
            if action == 'sell':
                influx.write_points([dict(
                    measurement='session',
                    tags=dict(
                        exchange=EXCHANGE,
                        symbol_1=SYMBOL_1,
                        symbol_2=SYMBOL_2,
                        session=str(last_trade_session).rjust(30, '0'),
                        buy_time=last_trade_time,
                        sell_time=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
                    ),
                    fields=dict(
                        buy_price=float(last_trade_price),
                        sell_price=float(price)
                    )
                )])

            last_trade_action = action
            last_trade_price = float(price)
            last_trade_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        active_order_id = None

def on_error(ws, error):
    print('websocket error {}'.format(error))

def on_close(ws):
    print('websocket closed')

def on_open(ws):
    print('websocket open')

if __name__ == '__main__':
    CONF = os.environ['CONF']
    #execfile(CONF)
    exec(compile(open('conf/{}.conf'.format(CONF), "rb").read(), 'conf/{}.conf'.format(CONF), 'exec'))

    influx = InfluxDBClient('influxdb', 8086, 'root', 'root', 'crypto_trader_bot')

    result = influx.query("SELECT price FROM price_volume WHERE exchange = '{}' and symbol_1 = '{}' and symbol_2 = '{}' ORDER BY time DESC limit 1".format(EXCHANGE, SYMBOL_1, SYMBOL_2))
    results = list(result.get_points())
    prev_price = results[0]['price'] if results else 0

    query_macd =  "SELECT mean(proper) - moving_average(mean(proper), 9) as macd FROM (SELECT moving_average(mean(price), 12) - moving_average(mean(price), 26) as proper FROM price_volume WHERE exchange = '{}' and symbol_1 = '{}' and symbol_2 = '{}' and time > now() - 5h GROUP BY time(1m) fill(linear)) WHERE time > now() - 1d GROUP BY time(1m) fill(linear)".format(EXCHANGE, SYMBOL_1, SYMBOL_2)
    result = influx.query(query_macd)
    results = list(result.get_points())
    macd_prev = results[-1]['macd'] if results else 0

    result = influx.query("SELECT price, type, session FROM trade WHERE exchange = '{}' and symbol_1 = '{}' and symbol_2 = '{}' ORDER BY time DESC limit 1".format(EXCHANGE, SYMBOL_1, SYMBOL_2))
    results = list(result.get_points())
    last_trade_time = results[0]['time'] if results else None
    last_trade_session = int(results[0]['session']) if results else 0
    last_trade_action = str(results[0]['type']) if results else None
    last_trade_price = float(results[0]['price']) if results else 0
    print('started session {} action {} price {}'.format(last_trade_session, last_trade_action, last_trade_price))

    if EXCHANGE == 'bl3p':
        from bl3p import bl3p
        exchange = bl3p(SYMBOL_1, SYMBOL_2, PUBLIC_KEY, PRIVATE_KEY)
    elif EXCHANGE == 'binance':
        from binance import binance
        exchange = binance(SYMBOL_1, SYMBOL_2, PUBLIC_KEY, PRIVATE_KEY)
    elif EXCHANGE == 'cobinhood':
        from cobinhood import cobinhood
        exchange = cobinhood(SYMBOL_1, SYMBOL_2, PUBLIC_KEY, PRIVATE_KEY)

    active_order_id = exchange.active_order_id()
    print('started order id {} '.format(active_order_id))
    exchange.start_listener(on_message, on_error, on_open, on_close)
