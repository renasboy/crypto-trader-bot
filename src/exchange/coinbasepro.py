import time
import base64
import hashlib
import hmac
import json
import requests
import urllib
import websocket


class coinbasepro(object):

    # NOTE this FEE is until 10K
    FEE = 0.005

    def __init__(self, symbol_1, symbol_2, public_key, private_key, passphrase, *args, **kwargs):
        self.symbol_1 = symbol_1.upper()
        self.symbol_2 = symbol_2.upper()
        self.symbol = self.symbol_1 + '-' + self.symbol_2
        self.public_key = public_key
        self.private_key = private_key
        self.passphrase = passphrase
        self.url = 'https://api.pro.coinbase.com/'
        self.websocket = 'wss://ws-feed.pro.coinbase.com/'

    def start_listener(self, on_msg, on_err, on_open, on_close):
        def subscribe():
            message = '{ "type": "subscribe", "product_ids" [ "' + self.symbol + '" ], "channels": [ "level2" ] }'
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
        price = msg['price_int']
        volume = msg['amount_int']
        fee = price * self.FEE
        return msg['date'], msg['type'], float(price), float(volume), float(fee)

    def ticker(self):
        ticker = self.call('GET', '/products/' + self.symbol + '/ticker', {})
        price = float(ticker['price'])
        fee = price * self.FEE
        return float(price), float(fee)

    def balances(self):
        return self.call('GET', '/accounts', {})

    def balance(self, symbol):
        balances = self.balances()
        for balance in balances:
            if balance['currency'] == symbol:
                return float(balance['available'])

    def orders(self):
        orders = self.call('GET', '/orders', {})
        return orders

    def active_order_id(self):
        orders = self.orders()
        if orders:
            return orders[0]['id']

    def orderbook(self):
        return self.call('GET', '/products/' + self.symbol + '/book', {})

    def highest_bid(self):
        orderbook = self.orderbook()
        return float(orderbook['bids'][0][0])

    def lowest_ask(self):
        orderbook = self.orderbook()
        return float(orderbook['asks'][0][0])

    def closed_order(self, id):
        order = self.call('GET', '/orders/' + str(id), {})
        if order and order['status'] == 'done' and order['done_reason'] == 'filled':
            price = float(order['executed_value'])
            volume = float(order['size'])
            fee = float(order['fill_fees'])
            type = order['side']
            return type, price, volume, fee
        return None, None, None, None

    def add_order(self, type, volume, price):
        data = dict(
            side=type,
            size=volume,
            price=price,
            product_id=self.symbol
        )
        print(data)
        add_order = {'id':1}
        #add_order = self.call('POST', '/orders', data)
        if add_order:
            return add_order['id']

    def call(self, method, path, data):
        post_data = urllib.parse.urlencode(data)
        #post_data = urllib.urlencode(data)
        body = '%s%c%s' % (path, 0x00, post_data)
        full_path = '%s%s' % (self.url, path)
        timestamp = str(time.time())
        signature = base64.b64encode(hmac.new(base64.b64decode(self.private_key), (timestamp + method + path + (data or '')).encode('ascii'), hashlib.sha256).digest()).decode('utf-8')
        headers = {
            'CB-ACCESS-SIGN': signature,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.public_key,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        }
        if method == 'GET':
            response = requests.get(full_path, data=post_data, headers=headers)
        else:
            response = requests.post(full_path, data=post_data, headers=headers)
        if response.status_code != 200:
            print('API failure: {} {}'.format(response.status_code, response.content))
            return False
        return json.loads(response.content)

#if __name__ == '__main__':
    #exchange = coinbasepro('BTC', 'EUR', coinbasepro.PUBLIC_KEY, coinbasepro.PRIVATE_KEY, coinbasepro.PASSPHRASE)
    #print(exchange.ticker())
    #print(exchange.balance('BTC'))
    #print(exchange.balance('EUR'))
    #print(exchange.orders())
    #print(exchange.orderbook())
    #print(exchange.highest_bid())
    #print(exchange.lowest_ask())
    #print(exchange.closed_order(25293373))
    #print(exchange.active_order_id())
    #print(exchange.add_order('sell', 1, 1))
