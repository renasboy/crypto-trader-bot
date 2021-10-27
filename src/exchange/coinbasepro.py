import base64
import hashlib
import hmac
import json
import time
import urllib

import requests
import websocket


class coinbasepro:

    # NOTE this FEE is until 10K
    FEE = 0.005

    def __init__(
        self, symbol_1, symbol_2, public_key, private_key, passphrase, *args, **kwargs
    ):
        self.symbol_1 = symbol_1.upper()
        self.symbol_2 = symbol_2.upper()
        self.symbol = self.symbol_1 + "-" + self.symbol_2
        self.public_key = public_key
        self.private_key = private_key
        self.passphrase = passphrase
        self.url = "https://api.pro.coinbase.com"
        self.websocket = "wss://ws-feed.pro.coinbase.com/"

    def start_listener(self, on_msg, on_err, on_open, on_close):
        def subscribe():
            message = (
                '{ "type": "subscribe", "product_ids" [ "'
                + self.symbol
                + '" ], "channels": [ "level2" ] }'
            )
            ws.send(message)

        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(
            self.websocket, on_message=on_msg, on_error=on_err, on_close=on_close
        )
        ws.on_open = subscribe
        ws.run_forever()

    def parse_ws_msg(self, message):
        msg = json.loads(message)
        price = msg["price_int"]
        volume = msg["amount_int"]
        fee = price * self.FEE
        return msg["date"], msg["type"], float(price), float(volume), float(fee)

    def ticker(self):
        ticker = self.call("GET", "/products/" + self.symbol + "/ticker", {})
        price = float(ticker["price"])
        fee = price * self.FEE
        return float(price), float(fee)

    def balances(self):
        return self.call("GET", "/accounts", {})

    def balance(self, symbol):
        return (next(float(b["available"]) for b in self.balances() if b["currency"] == symbol))

    def orders(self):
        return self.call("GET", "/orders", {})

    def active_order_id(self):
        orders = self.orders()
        if orders:
            for order in orders:
                if order["status"] == "open":
                    return order["id"]

    def orderbook(self):
        return self.call("GET", "/products/" + self.symbol + "/book", {})

    def highest_bid(self):
        orderbook = self.orderbook()
        return float(orderbook["bids"][0][0])

    def lowest_ask(self):
        orderbook = self.orderbook()
        return float(orderbook["asks"][0][0])

    def closed_order(self, id):
        order = self.call("GET", "/orders/" + str(id), {})
        if order and order["status"] == "done" and order["done_reason"] == "filled":
            type = order["side"]
            volume = float(order["filled_size"])
            price = float(order["executed_value"]) / volume
            fee = float(order["fill_fees"])
            return type, price, volume, fee
        return None, None, None, None

    def delete_order(self, id):
        return self.call("DELETE", "/orders/" + str(id), {})

    def market_order(self, type, amount):
        data = dict(type="market", side=type, product_id=self.symbol)
        # size or funds is required
        if type == "buy":
            data["funds"] = amount
        elif type == "sell":
            data["size"] = amount
        print(data)
        order = self.call('POST', '/orders/', data)
        print(order)
        if order:
            return order["id"]

    def limit_order(self, type, volume, price):
        # default type=limit
        data = dict(side=type, size=volume, price=price, product_id=self.symbol)
        print(data)
        order = self.call('POST', '/orders/', data)
        print(order)
        if order:
            return order["id"]

    def call(self, method, path, data):
        if data:
            data = json.dumps(data)
        full_path = "%s%s" % (self.url, path)
        timestamp = str(time.time())
        signature = base64.b64encode(
            hmac.new(
                base64.b64decode(self.private_key),
                (timestamp + method + path + (data or "")).encode("ascii"),
                hashlib.sha256,
            ).digest()
        ).decode("utf-8")
        headers = {
            "CB-ACCESS-SIGN": signature,
            "CB-ACCESS-TIMESTAMP": timestamp,
            "CB-ACCESS-KEY": self.public_key,
            "CB-ACCESS-PASSPHRASE": self.passphrase,
            "Content-Type": "application/json",
        }
        try:
            if method == "GET":
                response = requests.get(full_path, data={}, headers=headers)
            elif method == "POST":
                response = requests.post(full_path, data=data, headers=headers)
            elif method == "DELETE":
                response = requests.delete(full_path, data={}, headers=headers)
            if response.status_code != 200:
                raise Exception(
                    "API failure: {} {}".format(response.status_code, response.content)
                )
            return json.loads(response.content)
        except:
            pass


#if __name__ == '__main__':
#exchange = coinbasepro('BTC', 'EUR', coinbasepro.PUBLIC_KEY, coinbasepro.PRIVATE_KEY, coinbasepro.PASSPHRASE)
#print(exchange.ticker())
#print(exchange.balance('BTC'))
#print(exchange.balance('EUR'))
#print(exchange.orders())
#print(exchange.orderbook())
#print(exchange.highest_bid())
#print(exchange.lowest_ask())
#print(exchange.closed_order('949f38ca-8494-4ce2-b5c7-fb2782114d66'))
#print(exchange.closed_order('dd426289-29f6-406a-9a9f-0775a58c3fb8'))
#print(exchange.active_order_id())
#print(exchange.delete_order('6eb75320-de55-44dd-8af8-8d16880b8ffb'))
#print(exchange.limit_order('buy', 1, 1))
#print(exchange.market_order('buy', 70))
#print(exchange.market_order('sell', 0.0001))
#print(exchange.limit_order('sell', 0.0001, 50380))
#print(exchange.closed_order('dbc39ae4-039a-4351-9121-6abd8e19e0b1'))
