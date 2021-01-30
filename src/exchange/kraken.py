import base64
import hashlib
import hmac
import json
import time
import urllib

import requests
import websocket


class kraken(object):

    PRICE_MULTIPLIER = 0.00001
    VOLUME_MULTIPLIER =  0.00000001
    FEE = 0.0025
    ANTISPAM_FEE = 0.01

    public_key = None
    private_key = None
    url = None
    websocket = None

    def __init__(self, *args, **kwargs):
        self.public_key = 'CHAVES_CHAVES_CHAVES'
        self.private_key = 'CHAVES_CHAVES_CHAVES'
        self.url = 'https://api.kraken.com'
        self.websocket = 'wss://api.bl3p.eu/1/BTCEUR/trades'

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

    def balances(self):
        return self.call('/0/private/Balance', {})

    def balance_btc(self):
        balances = self.balances()
        return float(balances['results']['XXBT'])

    def balance_eur(self):
        balances = self.balances()
        return float(balances['results']['ZEUR'])

    def fee(self):
        if not self.trade_fee:
            balances = self.balances()
            self.trade_fee = float(balances['data']['trade_fee']) / 100
        return self.trade_fee

    def orders(self):
        orders = self.call('/0/private/OpenOrders', {})
        return orders['result']['open']

    def active_order_id(self):
        orders = self.orders()
        if orders:
            return orders[0]['order_id']

    def orderbook(self):
        return self.call('/0/public/Depth', { 'pair': 'XXBTZEUR' })

    def highest_bid(self):
        orderbook = self.orderbook()
        return float(orderbook['result']['XXBTZEUR']['bids'][1][0])

    def lowest_ask(self):
        orderbook = self.orderbook()
        return float(orderbook['result']['XXBTZEUR']['asks'][1][0])

    def closed_order(self, id):
        types = dict(bid='buy', ask='sell')
        order = self.call('/0/private/QueryOrders', {'txid': id})
        if order['result'] and order['result'][id] and order['result'][id]['status'] == 'closed':
            price = float(order['result'][id]['price'])
            volume = float(order['result'][id]['vol'])
            fee = float(order['result'][id]['fee'])
            type = types[order['data']['type']]
            return type, price, volume, fee
        return None, None, None, None

    def add_order(self, type, volume, price):
        types = dict(buy='buy', sell='sell')
        data = dict(
            pair='XXBTZEUR',
            type=types[type],
            ordertype='limit', # market (no price)
            price=price,
            volume=volume
        )
        print(data)
        add_order = {'result':{'txid': [1]}}
        #add_order = self.call('/0/private/AddOrder', data)
        if add_order:
            return add_order['result']['txid'][0]

    def call(self, path, data):
        #post_data = urllib.parse.urlencode(data)
        post_data = urllib.urlencode(data)
        full_path = '%s%s' % (self.url, path)
        headers = {}
        if 'private' in path:
            message = '%s%s' % (int(1000 * time.time()), post_data)
            body = '%s%s' % (path.encode(), hashlib.sha256(message.encode()).digest())
            signature = base64.b64encode(hmac.new(base64.b64decode(self.private_key), body, hashlib.sha512).digest())
            headers = {
                'API-Key': self.public_key,
                'API-Sign': signature,
                'User-Agent': 'Python Kraken API',
            }

        print(full_path)
        print(post_data)
        print(headers)

        response = requests.post(full_path, data=post_data, headers=headers)
        if response.status_code not in (200, 201, 202):
            print('API failure: {} {}'.format(response.status_code, response.content))
            return False
        print(response.content)
        return json.loads(response.content)

if __name__ == '__main__':
    exchange = kraken()
    #print(exchange.fee() / 100)
    print(exchange.balance_btc())
    #print(exchange.balance_eur())
    #print(exchange.orders())
    #print(exchange.orderbook())
    #print(exchange.highest_bid())
    #print(exchange.lowest_ask())
    #print(exchange.closed_order('07120101'))
    #print(exchange.add_order('sell', PRICE_INT, VOLUME_INT))
