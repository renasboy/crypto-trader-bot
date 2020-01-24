import hashlib
import hmac
import json
import requests
import ssl
import time
import urllib
import websocket


class cobinhood(object):

    def __init__(self, symbol_1, symbol_2, public_key, private_key, *args, **kwargs):
        self.symbol_1 = symbol_1.upper()
        self.symbol_2 = symbol_2.upper()
        self.symbol = self.symbol_2 + '-' + self.symbol_1
        self.public_key = public_key
        self.private_key = private_key
        self.url = 'https://api.cobinhood.com'
        self.websocket = 'wss://ws.cobinhood.com/v2/ws/'

    def start_listener(self, on_msg, on_err, on_open, on_close):
        def subscribe():
            message = '{ "action": "subscribe", "trading_pair_id": "' + self.symbol+ '", "type": "trade" }'
            ws.send(message)
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(
            self.websocket,
            on_message = on_msg,
            on_error = on_err,
            on_close = on_close
        )
        ws.on_open = subscribe
        ws.run_forever()

    def parse_ws_msg(self, message):
        msg = json.loads(message)
        price = float(msg[2])
        volume = float(msg[3])
        type = msg[4]
        fee = 0
        return msg['1'], type, price, volume, fee

    def ticker(self):
        ticker = self.call('get', '/v1/market/tickers/' + self.symbol, {})
        price = float(ticker['result']['ticker']['last_trade_price'])
        fee = 0
        return float(price), float(fee)

    def balances(self):
        return self.call('get', '/v1/wallet/balances', {})

    def balance(self, symbol):
        balances = self.balances()
        for balance in balances['result']['balances']:
            if balance['currency'] == symbol:
                return float(balance['total'])
        return 0.0

    def orders(self):
        orders = self.call('get', '/v1/trading/orders', {'trading_pair_id': self.symbol})
        return [order for order in orders['result']['orders'] if order['state'] in ('open', 'new','partially_filled')]

    def active_order_id(self):
        orders = self.orders()
        if orders:
            return orders[0]['id']

    def orderbook(self):
        return self.call('get', '/v1/market/orderbooks/' + self.symbol, {'limit': 5})

    def highest_bid(self):
        orderbook = self.orderbook()
        return float(orderbook['result']['orderbook']['bids'][1][0])

    def lowest_ask(self):
        orderbook = self.orderbook()
        return float(orderbook['result']['orderbook']['asks'][1][0])

    def closed_order(self, id):
        types = dict(bid='buy', ask='sell')
        order = self.call('get', '/v1/trading/orders/' + id, {})
        if 'order' in order['result'] and order['result']['order']['state'] == 'filled':
            price = float(order['result']['order']['price'])
            volume = float(order['result']['order']['size'])
            fee = 0
            type = types[order['result']['order']['side']]
            return type, price, volume, fee
        return None, None, None, None

    def add_order(self, type, volume, price):
        types = dict(buy='bid', sell='ask')
        data = dict(
            trading_pair_id=self.symbol,
            side=types[type],
            type='limit',  # market
            size=volume,
            price=price,
        )
        print(data)
        add_order = {'result': { 'order': { 'id': 1 } } }
        #add_order = self.call('post', '/v1/trading/orders', data)
        if add_order:
            return add_order['result']['order']['id']

    def call(self, method, path, data):
        post_data = urllib.parse.urlencode(data)
        #post_data = urllib.urlencode(data)
        headers = {
            'User-Agent': 'Python Cobinhood API',
            'Accept': 'application/json',
            'Authorization': self.public_key,
            'nonce': str(int(time.time())),
        }

        full_path = '%s%s' % (self.url, path)
        if method == 'post':
            response = requests.post(full_path, data=post_data, headers=headers)
        else:
            response = requests.get(full_path, post_data, headers=headers)
        if response.status_code != 200:
            print('API failure: {} {}'.format(response.status_code, response.content))
            return False
        print(response.content)
        return json.loads(response.content)

#if __name__ == '__main__':
    #exchange = cobinhood('BTC', 'ETH')
    #print(exchange.ticker())
    #print(exchange.balance('BTC'))
    #print(exchange.balance('ETH'))
    #print(exchange.orders())
    #print(exchange.orderbook())
    #print(exchange.highest_bid())
    #print(exchange.lowest_ask())
    #print(exchange.closed_order('17391295'))
    #print(exchange.active_order_id())
    #print(exchange.add_order('sell', 1, 1))
