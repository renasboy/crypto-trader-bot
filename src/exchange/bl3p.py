import base64
import hashlib
import hmac
import json
import requests
import urllib
import websocket


class bl3p(object):

    PRICE_MULTIPLIER = 0.00001
    VOLUME_MULTIPLIER =  0.00000001
    FEE = 0.0025
    ANTISPAM_FEE = 0.01

    def __init__(self, symbol_1, symbol_2, public_key, private_key, *args, **kwargs):
        self.symbol_1 = symbol_1.upper()
        self.symbol_2 = symbol_2.upper()
        self.symbol = self.symbol_1 + self.symbol_2
        self.public_key = public_key
        self.private_key = private_key
        self.url = 'https://api.bl3p.eu/1/'
        self.websocket = 'wss://api.bl3p.eu/1/' + self.symbol + '/trades'

    def start_listener(self, on_msg, on_err, on_open, on_close):
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(
            self.websocket,
            on_message = on_msg,
            on_error = on_err,
            on_close = on_close
        )
        ws.on_open = on_open
        ws.run_forever()

    def parse_ws_msg(self, message):
        msg = json.loads(message)
        price = int(msg['price_int']) * self.PRICE_MULTIPLIER
        volume = int(msg['amount_int']) * self.VOLUME_MULTIPLIER
        fee = price * self.FEE + self.ANTISPAM_FEE
        return msg['date'], msg['type'], float(price), float(volume), float(fee)

    def ticker(self):
        ticker = self.call(self.symbol + '/ticker', {})
        price = float(ticker['last'])
        fee = price * self.FEE + self.ANTISPAM_FEE
        return float(price), float(fee)

    def balances(self):
        return self.call('GENMKT/money/info', {})

    def balance(self, symbol):
        balances = self.balances()
        multiplier = self.PRICE_MULTIPLIER
        if symbol == self.symbol_1:
            multiplier = self.VOLUME_MULTIPLIER
        return float(int(balances['data']['wallets'][symbol]['available']['value_int']) * multiplier)

    def orders(self):
        orders = self.call(self.symbol + '/money/orders', {})
        return orders['data']['orders']

    def active_order_id(self):
        orders = self.orders()
        if orders:
            return orders[0]['order_id']

    def orderbook(self):
        return self.call(self.symbol + '/money/depth/full', {})

    def highest_bid(self):
        orderbook = self.orderbook()
        return int(orderbook['data']['bids'][1]['price_int']) * self.PRICE_MULTIPLIER

    def lowest_ask(self):
        orderbook = self.orderbook()
        return int(orderbook['data']['asks'][1]['price_int']) * self.PRICE_MULTIPLIER

    def closed_order(self, id):
        types = dict(bid='buy', ask='sell')
        order = self.call(self.symbol + '/money/order/result', {'order_id': id})
        if order['result'] == 'success' and order['data']['status'] == 'closed':
            price = float(int(order['data']['price']['value_int']) * self.PRICE_MULTIPLIER)
            volume = float(int(order['data']['total_amount']['value_int']) * self.VOLUME_MULTIPLIER)
            fee = float(int(order['data']['total_fee']['value_int']) * self.PRICE_MULTIPLIER)
            type = types[order['data']['type']]
            return type, price, volume, fee
        return None, None, None, None

    def add_order(self, type, volume, price):
        types = dict(buy='bid', sell='ask')
        data = dict(
            type=types[type],
            amount_int=int(volume / self.VOLUME_MULTIPLIER),
            price_int=int(price / self.PRICE_MULTIPLIER),
            fee_currency='EUR'
        )
        print(data)
        add_order = {'data':{'order_id':1}}
        #add_order = self.call(self.symbol + '/money/order/add', data)
        if add_order:
            return add_order['data']['order_id']

    def call(self, path, data):
        post_data = urllib.parse.urlencode(data)
        #post_data = urllib.urlencode(data)
        body = '%s%c%s' % (path, 0x00, post_data)
        signature = base64.b64encode(hmac.new(base64.b64decode(self.private_key), body.encode('utf-8'), hashlib.sha512).digest())
        full_path = '%s%s' % (self.url, path)
        headers = { 'Rest-Key': self.public_key, 'Rest-Sign': signature }

        response = requests.post(full_path, data=post_data, headers=headers)
        if response.status_code != 200:
            print('API failure: {} {}'.format(response.status_code, response.content))
            return False
        print(response.content)
        return json.loads(response.content)

#if __name__ == '__main__':
    #exchange = bl3p('BTC', 'EUR')
    #print(exchange.ticker())
    #print(exchange.balance('BTC'))
    #print(exchange.balance('EUR'))
    #print(exchange.orders())
    #print(exchange.orderbook())
    #print(exchange.highest_bid())
    #print(exchange.lowest_ask())
    #print(exchange.closed_order(25293373))
    #print(exchange.active_order_id())
    #print(exchange.add_order('sell', PRICE_INT, VOLUME_INT))
