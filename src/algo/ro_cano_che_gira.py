

class ro_cano_che_gira(object):

    def __init__(self, helper):
        self.algo_helper = helper

    @property
    def action(self):

        # MAs
        ma1_last, ma1_prev = self.algo_helper.ma_last_prev(1)
        ma2_last, ma2_prev = self.algo_helper.ma_last_prev(2)
        ma8_last, ma8_prev = self.algo_helper.ma_last_prev(8)
        ma11_last, ma11_prev = self.algo_helper.ma_last_prev(11)
        ma31_last, ma31_prev = self.algo_helper.ma_last_prev(31)

        # LAST TRADE
        last_trade_action = self.algo_helper.last_trade_action
        last_trade_price = self.algo_helper.last_trade_price

        # CURRENT PRICE
        price = self.algo_helper.price

        action = None
        # salvagente, prezzo < last_trade_price - 0.16%
        if last_trade_action == 'buy' and price < last_trade_price - last_trade_price * 0.0016:
            action = 'sell'
        # compra solo se
        elif last_trade_action != 'buy':
            # subito dopo l'incrocio prezzo X ma8 il prezzo > ma8
            # compra o vende solo se ma8 => ma31
            if ma8_last >= ma31_last:
                if ma1_prev < ma8_prev and ma1_last > ma8_last:
                    action = 'buy'
        # vende solo se
        elif last_trade_action == 'buy':
            # subito dopo l'incrocio della ma2 X ma11 la ma2 < ma11
            # e vende anche se ma8 < ma31
            if (ma2_prev > ma11_prev and ma2_last < ma11_last) or ma8_last < ma31_last:
                action = 'sell'
                # ma anche solo se guadagno > 0.08%
                if price - last_trade_price >= 0 and price - last_trade_price < last_trade_price * 0.0008:
                    action = None
                # perdita < -0.04%
                if price - last_trade_price <= 0 and last_trade_price - price < last_trade_price * 0.0004:
                    action = None
        return action
