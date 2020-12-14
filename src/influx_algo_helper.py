import datetime
import time

from influxdb import InfluxDBClient


class influx_algo_helper(object):

    def __init__(self, exchange, symbol_1, symbol_2):
        self.exchange = exchange
        self.symbol_1 = symbol_1
        self.symbol_2 = symbol_2
        self.label = '{}-{}-{}'.format(exchange, symbol_1, symbol_2)

        self.influx = InfluxDBClient('influxdb', 8086, 'root', 'root', 'crypto_trader_bot')
        self.fee = None
        self.price = None
        self.prev_price = None
        self.prev_macd = self.macd
        self.last_trade_time = None
        self.last_trade_session = None
        self.last_trade_action = None
        self.last_trade_price = None

    def write(self, data):
        self.influx.write_points(data)

    def ma_last_prev(self, period):
        query_ma =  "SELECT moving_average(mean(price), {}) as ma FROM price_volume WHERE exchange = '{}' and symbol_1 = '{}' and symbol_2 = '{}' and time > now() - 1h GROUP BY time(1m) fill(previous) ORDER BY time DESC limit 2".format(period, self.exchange, self.symbol_1, self.symbol_2)
        if period == 1:
            query_ma =  "SELECT mean(price) as ma FROM price_volume WHERE exchange = '{}' and symbol_1 = '{}' and symbol_2 = '{}' and time > now() - 1h GROUP BY time(1m) fill(previous) ORDER BY time DESC limit 2".format(self.exchange, self.symbol_1, self.symbol_2)
        result = self.influx.query(query_ma)
        results = list(result.get_points())
        ma_last = results[0]['ma'] if results and len(results) == 2 and results[0]['ma'] is not None else 0
        ma_prev = results[1]['ma'] if results and len(results) == 2 and results[1]['ma'] is not None else 0
        return float(ma_last), float(ma_prev)

    def ma_minutes_ago(self, period, minutes):
        query_ma =  "SELECT moving_average(mean(price), {}) as ma FROM price_volume WHERE exchange = '{}' and symbol_1 = '{}' and symbol_2 = '{}' and time > now() - 1h GROUP BY time(1m) fill(previous) ORDER BY time DESC limit {}".format(period, self.exchange, self.symbol_1, self.symbol_2, minutes + 1)
        if period == 1:
            query_ma =  "SELECT mean(price) as ma FROM price_volume WHERE exchange = '{}' and symbol_1 = '{}' and symbol_2 = '{}' and time > now() - 1h GROUP BY time(1m) fill(previous) ORDER BY time DESC limit 2".format(self.exchange, self.symbol_1, self.symbol_2)
        result = self.influx.query(query_ma)
        results = list(result.get_points())
        ma = results[minutes]['ma'] if results and len(results) == minutes + 1 and results[minutes]['ma'] is not None else 0
        return float(ma)

    @property
    def rsi_trend_up(self):
        rsi_trend_up = self.price - self.prev_price if self.prev_price and self.price > self.prev_price else 0
        self.log('rsi trend up {}'.format(rsi_trend_up))
        return rsi_trend_up

    @property
    def rsi_trend_down(self):
        rsi_trend_down = self.prev_price - self.price if self.prev_price and self.price < self.prev_price else 0
        self.log('rsi trend down {}'.format(rsi_trend_down))
        return rsi_trend_down

    @property
    def rsi(self):
        # RSI 14
        query_rsi =  "SELECT 100 - 100 / ((moving_average(mean(trend_up), 14) / moving_average(mean(trend_down), 14)) + 1) as rsi FROM price_volume WHERE exchange = '{}' and symbol_1 = '{}' and symbol_2 = '{}' and time > now() - 1h GROUP BY time(1m) fill(linear)".format(self.exchange, self.symbol_1, self.symbol_2)
        result = self.influx.query(query_rsi)
        results = list(result.get_points())
        rsi = results[-1]['rsi'] if results else 50
        self.log('rsi {}'.format(rsi))
        return rsi

    @property
    def macd(self):
        # MACD 12, 26, 9
        query_macd =  "SELECT mean(proper) - moving_average(mean(proper), 9) as macd FROM (SELECT moving_average(mean(price), 12) - moving_average(mean(price), 26) as proper FROM price_volume WHERE exchange = '{}' and symbol_1 = '{}' and symbol_2 = '{}' and time > now() - 5h GROUP BY time(1m) fill(previous)) WHERE time > now() - 1d GROUP BY time(1m) fill(previous)".format(self.exchange, self.symbol_1, self.symbol_2)
        result = self.influx.query(query_macd)
        results = list(result.get_points())
        macd = results[-1]['macd'] if results else 0
        self.log('macd {}'.format(macd))
        return macd

    def macd_minutes_ago(self, minutes):
        # MACD 12, 26, 9
        query_macd =  "SELECT mean(proper) - moving_average(mean(proper), 9) as macd FROM (SELECT moving_average(mean(price), 12) - moving_average(mean(price), 26) as proper FROM price_volume WHERE exchange = '{}' and symbol_1 = '{}' and symbol_2 = '{}' and time > now() - 5h GROUP BY time(1m) fill(previous)) WHERE time > now() - 1d GROUP BY time(1m) fill(previous)".format(self.exchange, self.symbol_1, self.symbol_2)
        result = self.influx.query(query_macd)
        results = list(result.get_points())
        macd = results[-minutes]['macd'] if results else 0
        self.log('macd {} minutes ago {}'.format(minutes, macd))
        return macd

    @property
    def macd_trend(self):
        macd_last = self.macd
        macd_trend = None
        if self.prev_macd < macd_last:
            macd_trend = 'up'
            if self.prev_macd <= 0 and macd_last > 0:
                macd_trend = 'breakup'
        elif self.prev_macd > macd_last:
            macd_trend = 'down'
            if self.prev_macd > 0 and macd_last <= 0:
                macd_trend = 'breakdown'
        self.prev_macd = macd_last
        self.log('macd trend {}'.format(macd_trend))
        return macd_trend


    def min_mean_max(self, period1, period2):
        # HOURLY, DAILY, WEEKLY and MONTHLY AVERAGES
        query_min_mean_max = "SELECT min(price), mean(price), max(price) FROM price_volume WHERE exchange = '{}' and symbol_1 = '{}' and symbol_2 = '{}' and time >= now() - {} GROUP BY time({}) fill(previous) ORDER BY time DESC LIMIT 1"
        query = query_min_mean_max.format(self.exchange, self.symbol_1, self.symbol_2, period1, period2)
        result = self.influx.query(query)
        results = list(result.get_points())
        min = results[0]['min'] if results else 0
        mean = results[0]['mean'] if results else 0
        max = results[0]['max'] if results else 0
        return float(min), float(mean), float(max)

    def hour_min_mean_max(self):
        return self.min_mean_max('2h', '1h')

    def day_min_mean_max(self):
        return self.min_mean_max('48h', '24h')

    def week_min_mean_max(self):
        return self.min_mean_max('14d', '7d')

    def month_min_mean_max(self):
        return self.min_mean_max('60d', '30d')

    def set_price(self, price):
        if self.price:
            self.prev_price = self.price
        else:
            self.prev_price = self.last_price
        self.price = price

    def set_fee(self, fee):
        self.fee = fee

    @property
    def last_price(self):
        result = self.influx.query("SELECT price FROM price_volume WHERE exchange = '{}' and symbol_1 = '{}' and symbol_2 = '{}' ORDER BY time DESC limit 1".format(self.exchange, self.symbol_1, self.symbol_2))
        results = list(result.get_points())
        price = results[0]['price'] if results else 0
        self.log('last price {}'.format(price))
        return price

    def highest_price_minutes_ago(self, minutes):
        result = self.influx.query("SELECT max(price) FROM price_volume WHERE exchange = '{}' and symbol_1 = '{}' and symbol_2 = '{}' and time >= now() - {}m GROUP BY time({}m) fill(previous) ORDER BY time DESC LIMIT 1".format(self.exchange, self.symbol_1, self.symbol_2, minutes * 3, minutes))
        results = list(result.get_points())
        max = results[0]['max'] if results else 0
        self.log('max price {} minutes ago {}'.format(minutes, max))
        return float(max)

    def update_last_trade(self):
        self.last_trade_time, self.last_trade_session, self.last_trade_action, self.last_trade_price = self.last_trade()

    def last_trade(self):
        result = self.influx.query("SELECT price, type, session FROM trade WHERE exchange = '{}' and symbol_1 = '{}' and symbol_2 = '{}' ORDER BY time DESC limit 1 tz('Europe/Amsterdam')".format(self.exchange, self.symbol_1, self.symbol_2))
        results = list(result.get_points())
        date_time = results[0]['time'] if results else None
        session = results[0]['session'] if results else 0
        action = results[0]['type'] if results else None
        price = results[0]['price'] if results else 0
        self.log('last trade date: {} session: {} action: {} price: {}'.format(date_time, session, action, price))
        return date_time, int(session), action, float(price)

    def log(self, message):
        string_date = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        print('{} {}: {}'.format(string_date, self.label, message))
