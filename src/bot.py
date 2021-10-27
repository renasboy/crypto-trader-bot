import os
import time

from influx_algo_helper import influx_algo_helper


def run():
    global algo_helper
    global algo
    global exchange
    global active_order_id

    algo_helper.set_price()
    price = algo_helper.price
    fee = algo_helper.fee

    # ALGO TAKE ACTION
    action = algo.action

    if action != None:
        if not LIMIT_ORDER:
            if not DRY_RUN:
                if action == "buy":
                    amount = exchange.balance(SYMBOL_2) * (
                        float(MAX_SYMBOL_2_PERCENTAGE) / 100.0
                    )
                elif action == "sell":
                    amount = exchange.balance(SYMBOL_1) * (
                        float(MAX_SYMBOL_1_PERCENTAGE) / 100.0
                    )
                algo_helper.log(
                    "REAL market order action {} amount {}".format(action, amount)
                )
                active_order_id = exchange.market_order(action, amount)
                algo_helper.log("REAL market order id {} ".format(active_order_id))
            else:
                active_order_id = 1
        elif not active_order_id:
            if action == "buy":
                price = exchange.lowest_ask()
                volume = (
                    exchange.balance(SYMBOL_2)
                    * (float(MAX_SYMBOL_2_PERCENTAGE) / 100.0)
                ) / price
            elif action == "sell":
                price = exchange.highest_bid()
                volume = exchange.balance(SYMBOL_1) * (
                    float(MAX_SYMBOL_1_PERCENTAGE) / 100.0
                )

            if not DRY_RUN:
                algo_helper.log(
                    "REAL limit order action {} price {} volume {}".format(
                        action, price, volume
                    )
                )
                active_order_id = exchange.limit_order(action, volume, price)
                algo_helper.log("REAL limit order id {} ".format(active_order_id))
            else:
                active_order_id = 1

    # AFTER CONFIRMATION
    if active_order_id:
        if not LIMIT_ORDER or not exchange.orders():
            if LIMIT_ORDER and not DRY_RUN:
                action, price, volume, fee = exchange.closed_order(active_order_id)
            if action:
                algo_helper.last_trade_session += int(action == "buy")
                algo_helper.write_trade_action(
                    action, active_order_id, price, volume, fee
                )
                if action == "sell":
                    algo_helper.write_trade_session(price)
                algo_helper.update_last_trade()
                active_order_id = None


if __name__ == "__main__":

    CONF = os.environ["CONF"]

    exec(
        compile(
            open("conf/{}.conf".format(CONF), "rb").read(),
            "conf/{}.conf".format(CONF),
            "exec",
        )
    )

    algo_helper = influx_algo_helper(ALGO, EXCHANGE, SYMBOL_1, SYMBOL_2)
    algo_helper.update_last_trade()

    if ALGO in (
        "maddog",
        "ro_cano_quando_esce",
        "ro_cano_che_ritorna",
        "boring_but_safe",
    ):
        module = __import__("algo.{}".format(ALGO), fromlist=[ALGO])
        algo = getattr(module, ALGO)(algo_helper)

    if EXCHANGE in ("bl3p", "binance", "cobinhood", "coinbasepro"):
        module = __import__("exchange.{}".format(EXCHANGE), fromlist=[EXCHANGE])
        exchange = getattr(module, EXCHANGE)(
            SYMBOL_1, SYMBOL_2, PUBLIC_KEY, PRIVATE_KEY, PASSPHRASE
        )

    active_order_id = None
    if LIMIT_ORDER:
        active_order_id = exchange.active_order_id()
        algo_helper.log("started order id {} ".format(active_order_id))

    while True:
        run()
        time.sleep(PING_INTERVAL)
