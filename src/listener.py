import time
import os

from influx_algo_helper import influx_algo_helper


def run():
    global algo_helper
    global exchange

    price, fee = exchange.ticker()

    algo_helper.write([dict(
        measurement='price_volume',
        tags=dict(
            exchange=EXCHANGE,
            symbol_1=SYMBOL_1,
            symbol_2=SYMBOL_2
        ),
        fields=dict(
            price=float(price),
            fee=float(fee)
        )
    )])

if __name__ == '__main__':

    CONF = os.environ['CONF']
    exec(compile(open('conf/{}.conf'.format(CONF), "rb").read(), 'conf/{}.conf'.format(CONF), 'exec'))

    algo_helper = influx_algo_helper('listener', EXCHANGE, SYMBOL_1, SYMBOL_2)

    if EXCHANGE in ('bl3p', 'binance', 'cobinhood', 'coinbasepro'):
        module = __import__('exchange.{}'.format(EXCHANGE), fromlist=[EXCHANGE])
        exchange = getattr(module, EXCHANGE)(SYMBOL_1, SYMBOL_2, PUBLIC_KEY, PRIVATE_KEY, PASSPHRASE)

    while True:
        run()
        time.sleep(PING_INTERVAL)
