class boring_but_safe:
    def __init__(self, helper, buy_percentage, sell_percentage):
        self.algo_helper = helper
        self.buy_percentage = buy_percentage
        self.sell_percentage = sell_percentage

    @property
    def action(self):

        # RSI
        rsi = self.algo_helper.rsi
        # MAC TREND
        macd_trend = self.algo_helper.macd_trend
        # WEEK MEAN
        week_min, week_mean, week_max = self.algo_helper.week_min_mean_max()

        # LAST TRADE
        last_trade_action = self.algo_helper.last_trade_action
        last_trade_price = self.algo_helper.last_trade_price

        # CURRENT PRICE + FEE
        price = self.algo_helper.price
        fee = self.algo_helper.fee

        action = None
        percentage = 0
        if (
            last_trade_action != "buy"
            and macd_trend == "breakup"
            and rsi < 80
            and price == min([price, week_mean])
        ):
            percentage = self.buy_percentage
            action = "buy"
        elif (
            last_trade_action == "buy"
            and macd_trend == "breakdown"
            and rsi > 20
            and price > last_trade_price + (fee * 5)
        ):
            percentage = self.sell_percentage
            action = "sell"
        return action, percentage
