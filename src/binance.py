import hashlib
import hmac
import json
import requests
import ssl
import time
import urllib
import websocket


class binance(object):

    FEE = 0.001

    def __init__(self, symbol_1, symbol_2, public_key, private_key):
        self.symbol_1 = symbol_1.upper()
        self.symbol_2 = symbol_2.upper()
        self.symbol = self.symbol_2 + self.symbol_1
        self.public_key = public_key
        self.private_key = private_key
        self.private_url = 'https://api.binance.com/api/v3/'
        self.public_url = 'https://api.binance.com/api/v1/'
        self.websocket = 'wss://stream.binance.com:9443/ws/' + self.symbol.lower() + '@trade'

    def start_listener(self, on_msg, on_err, on_open, on_close):
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(
            self.websocket,
            on_message = on_msg,
            on_error = on_err,
            on_close = on_close
        )
        ws.on_open = on_open
        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    def parse_ws_msg(self, message):
        msg = json.loads(message)
        price = float(msg['p'])
        volume = float(msg['q'])
        type = 'buy' if msg['m'] == True else 'sell'
        fee = float(price * self.FEE)
        return msg['T'], type, price, volume, fee

    def balances(self):
        return self.call('get', 'account', {})

    def balance(self, symbol):
        balances = self.balances()
        for balance in balances['balances']:
            if balance['asset'] == symbol:
                return float(balance['free'])
        return 0.0

    def orders(self):
        return self.call('get', 'openOrders', {'symbol': self.symbol})

    def active_order_id(self):
        orders = self.orders()
        if orders:
            return orders[0]['orderId']

    def orderbook(self):
        return self.call('get', 'depth', {'symbol': self.symbol, 'limit': 5})

    def highest_bid(self):
        orderbook = self.orderbook()
        return float(orderbook['bids'][1][0])

    def lowest_ask(self):
        orderbook = self.orderbook()
        return float(orderbook['asks'][1][0])

    def closed_order(self, id):
        types = dict(BUY='buy', SELL='sell')
        order = self.call('get', 'order', {'symbol': self.symbol,'orderId': id})
        if order and order['status'] == 'FILLED':
            price = float(order['price'])
            volume = float(order['origQty'])
            fee = 0
            type = types[order['side']]
            return type, price, volume, fee
        return None, None, None, None

    def add_order(self, type, volume, price):
        types = dict(buy='BUY', sell='SELL')
        data = dict(
            symbol=self.symbol,
            side=types[type],
            type='LIMIT', # MARKET
            timeInForce='GTC',
            quantity=volume,
            price=price,
            newOrderRespType='ACK'
        )
        print(data)
        add_order = {'orderId':1}
        #add_order = self.call('post', 'order', data)
        if add_order:
            return add_order['orderId']

    def call(self, method, path, data):
        data['timestamp'] = int(1000 * time.time())
        post_data = urllib.parse.urlencode(data)
        #post_data = urllib.urlencode(data)
        signature = hmac.new(self.private_key.encode('utf-8'), post_data.encode('utf-8'), hashlib.sha256).hexdigest()
        post_data += '&signature=' + signature
        headers = {
            'User-Agent': 'Python Binance API',
            'Accept': 'application/json',
            'X-MBX-APIKEY': self.public_key,
        }

        full_path = '%s%s' % (self.private_url, path)
        if path in ('depth', ):
            del(data['timestamp'])
            full_path = '%s%s' % (self.public_url, path)
            response = requests.get(full_path, data)
        elif method == 'post':
            response = requests.post(full_path, data=post_data, headers=headers)
        else:
            response = requests.get(full_path, post_data, headers=headers)
        if response.status_code != 200:
            print('API failure: {} {}'.format(response.status_code, response.content))
            return False
        print(response.content)
        return json.loads(response.content)

#if __name__ == '__main__':
    #exchange = binance('ETH', 'TRX')
    #print(exchange.balance('ETH'))
    #print(exchange.balance('TRX'))
    #print(exchange.orders())
    #print(exchange.orderbook())
    #print(exchange.highest_bid())
    #print(exchange.lowest_ask())
    #print(exchange.closed_order('17391295'))
    #print(exchange.active_order_id())
    #print(exchange.add_order('sell', 1, 1))
