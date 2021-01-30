import os
import time

from influx_algo_helper import influx_algo_helper


# TICKER POOLING
def run():
    global algo_helper
    global exchange

    price, fee = exchange.ticker()

    algo_helper.log('price: {} fee: {}'.format(price, fee))

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

# WEBSOCKET
def on_message(ws, message):
    log('websocket message {}'.format(message))
    date_time, type, price, volume, fee = exchange.parse_ws_msg(message)

def on_error(ws, error):
    log('websocket error {}'.format(error))

def on_close(ws):
    log('websocket closed')

def on_open(ws):
    log('websocket open')

# MAIN
if __name__ == '__main__':

    CONF = os.environ['CONF']
    exec(compile(open('conf/{}.conf'.format(CONF), "rb").read(), 'conf/{}.conf'.format(CONF), 'exec'))

    algo_helper = influx_algo_helper('listener', EXCHANGE, SYMBOL_1, SYMBOL_2)

    if EXCHANGE in ('bl3p', 'binance', 'cobinhood', 'coinbasepro'):
        module = __import__('exchange.{}'.format(EXCHANGE), fromlist=[EXCHANGE])
        exchange = getattr(module, EXCHANGE)(SYMBOL_1, SYMBOL_2, PUBLIC_KEY, PRIVATE_KEY, PASSPHRASE)

    if DATA_RETRIEVAL in ('ticker', 'websocket'):
        if DATA_RETRIEVAL == 'websocket':
            exchange.start_listener(on_message, on_error, on_open, on_close)
        elif DATA_RETRIEVAL == 'ticker':
            while True:
                run()
                time.sleep(PING_INTERVAL)
