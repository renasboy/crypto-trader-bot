import time
import os
import datetime
from influx_algo_helper import influx_algo_helper

def cur_date_time():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%dT%H:%M:%S.%fZ')

def log(message):
    string_date = cur_date_time()
    print('{} {}-{}-{}: {}'.format(string_date, EXCHANGE, SYMBOL_1, SYMBOL_2, message))

def run():
    global algo_helper
    global algo
    global exchange
    global active_order_id

    price, fee = exchange.ticker()

    algo_helper.set_fee(fee)
    algo_helper.set_price(price)

    trend_up = algo_helper.rsi_trend_up
    trend_down = algo_helper.rsi_trend_down 

    algo_helper.write([dict(
        measurement='price_volume',
        tags=dict(
            exchange=EXCHANGE,
            symbol_1=SYMBOL_1,
            symbol_2=SYMBOL_2
        ),
        fields=dict(
            price=float(price),
            trend_up=float(trend_up),
            trend_down=float(trend_down)
        )
    )])

if __name__ == '__main__':

    CONF = os.environ['CONF']
    #execfile('conf/{}.conf'.format(CONF))
    exec(compile(open('conf/{}.conf'.format(CONF), "rb").read(), 'conf/{}.conf'.format(CONF), 'exec'))

    algo_helper = influx_algo_helper(EXCHANGE, SYMBOL_1, SYMBOL_2)
    algo_helper.update_last_trade()

    if ALGO in ('ro_cano', 'ro_cano_che_gira', 'ro_cano_quando_esce', 'ro_cano_che_ritorna', 'boring_but_safe'):
        module = __import__('algo.{}'.format(ALGO), fromlist=[ALGO])
        algo = getattr(module, ALGO)(algo_helper)

    if EXCHANGE in ('bl3p', 'binance', 'cobinhood', 'coinbasepro'):
        module = __import__('exchange.{}'.format(EXCHANGE), fromlist=[EXCHANGE])
        exchange = getattr(module, EXCHANGE)(SYMBOL_1, SYMBOL_2, PUBLIC_KEY, PRIVATE_KEY, PASSPHRASE)

    active_order_id = exchange.active_order_id()
    log('started order id {} '.format(active_order_id))
    while True:
        run()
        time.sleep(PING_INTERVAL)
