import uuid
import hashlib
import hmac
import json
import time

import requests
import websocket


class coinbasepro:

    # NOTE this FEE is until 10K
    FEE = 0.005

    def __init__(
        self, symbol_1, symbol_2, public_key, private_key, *args, **kwargs
    ):
        self.symbol_1 = symbol_1.upper()
        self.symbol_2 = symbol_2.upper()
        self.symbol = self.symbol_1 + "-" + self.symbol_2
        self.public_key = public_key
        self.private_key = private_key
        self.url = "https://api.coinbase.com"
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
        return msg["date"], msg["type"].lower(), float(price), float(volume), float(fee)

    def ticker(self):
        ticker = self.call("GET", "/products/" + self.symbol, {})
        price = float(ticker["price"])
        fee = price * self.FEE
        return float(price), float(fee)

    def balances(self):
        return self.call("GET", "/accounts", {})

    def balance(self, symbol):
        return next(
            float(b["available_balance"]["value"]) for b in self.balances()["accounts"] if b["currency"] == symbol
        )

    def orders(self):
        orders = self.call("GET", "/orders/historical/batch?order_status=OPEN", {})
        return orders["orders"] if orders else []

    def active_order_id(self):
        orders = self.orders()
        for order in orders:
            if order["status"] == "OPEN":
                return order["order_id"]

    def orderbook(self):
        return self.call("GET", "/product_book?product_id=" + self.symbol, {})

    def highest_bid(self):
        orderbook = self.orderbook()
        return float(orderbook["pricebook"]["bids"][0]["price"])

    def lowest_ask(self):
        orderbook = self.orderbook()
        return float(orderbook["pricebook"]["asks"][0]["price"])

    def closed_order(self, id):
        order = self.call("GET", "/orders/historical/" + str(id), {})
        if order:
            print(json.dumps(order))
        if order and "order" in order and order["order"]["status"] == "FILLED":
            type = order["order"]["side"].lower()
            volume = float(order["order"]["filled_size"])
            price = float(order["order"]["average_filled_price"])
            fee = float(order["order"]["total_fees"])
            return type, price, volume, fee
        return None, None, None, None

    def delete_order(self, id):
        return self.call("POST", "/orders/batch_cancel", dict(order_ids=[str(id)]))

    def market_order(self, type, amount):
        data = dict(
            client_order_id=str(uuid.uuid4()),
            product_id=self.symbol,
            side=type.upper(),
            order_configuration=dict(
                market_market_ioc=dict()
            )
        )
        if type == "buy":
            data["order_configuration"]["market_market_ioc"]["quote_size"] = str(round(amount, 2))
        elif type == "sell":
            data["order_configuration"]["market_market_ioc"]["base_size"] = str(int(amount * 100000000) / 100000000)
        print(json.dumps(data))
        order = self.call("POST", "/orders/", data)
        print(order)
        print(json.dumps(order))
        if order and "success" in order and order["success"]:
            return order["success_response"]["order_id"]

    def limit_order(self, type, volume, price):
        data = dict(
            client_order_id=str(uuid.uuid4()),
            product_id=self.symbol,
            side=type.upper(),
            order_configuration=dict(
                limit_limit_gtc=dict(
                    base_size=str(volume),
                    limit_price=str(price)
                )
            )
        )
        print(json.dumps(data))
        order = self.call("POST", "/orders/", data)
        print(json.dumps(order))
        if order and "success" in order and order["success"]:
            return order["success_response"]["order_id"]

    def call(self, method, path, data):
        if data:
            data = json.dumps(data)
        full_path = "%s%s%s" % (self.url, "/api/v3/brokerage",  path)
        timestamp = str(int(time.time()))
        signature = hmac.new(
            self.private_key.encode("utf-8"),
            (timestamp + method + "/api/v3/brokerage" + path.split('?')[0] + str(data or "")).encode("utf-8"),
            digestmod=hashlib.sha256,
        ).digest().hex()
        headers = {
            "CB-ACCESS-SIGN": signature,
            "CB-ACCESS-TIMESTAMP": timestamp,
            "CB-ACCESS-KEY": self.public_key,
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
                print(response.content)
                raise Exception(
                    "API failure: {} {}".format(response.status_code, response.content)
                )
            return json.loads(response.content)
        except:
            pass


#if __name__ == '__main__':
# exchange = coinbasepro('BTC', 'EUR', 'API_KEY', 'PRIVATE_KEY')
# print(exchange.ticker())
# print(json.dumps(exchange.balances()))
# print(exchange.balance('BTC'))
# print(exchange.balance('EUR'))
# print(json.dumps(exchange.orders()))
# print(json.dumps(exchange.orderbook()))
# print(exchange.highest_bid())
# print(exchange.lowest_ask())
# print(exchange.closed_order('3e4695f6-5eec-4d07-b9f1-27fb3c41ef42'))
# print(exchange.active_order_id())
# print(json.dumps(exchange.delete_order('98d6d3aa-58b1-4c24-873c-ce6a7864342c')))
# print(exchange.limit_order('buy', 0.0001, 10000))
# print(exchange.market_order('buy', 30))
# print(exchange.market_order('sell', 0.0008927884609665))
# print(json.dumps(exchange.limit_order('sell', 0.0001, 50380)))
# print(json.dumps(exchange.delete_order('8ed72001-4333-426a-920c-c6c9f3db237f')))
# print(exchange.closed_order('6b6628f4-44df-482f-a7e2-3c0eb9b5b34d'))
