

class ro_cano(object):

    def __init__(self, helper):
        self.algo_helper = helper

    @property
    def action(self):

        # MAs
        ma1_last, ma1_prev = self.algo_helper.ma_last_prev(1)
        ma8_last, ma8_prev = self.algo_helper.ma_last_prev(8)
        ma29_last, ma29_prev = self.algo_helper.ma_last_prev(29)
        ma11_last, ma11_prev = self.algo_helper.ma_last_prev(11)

        # LAST TRADE
        last_trade_action = self.algo_helper.last_trade_action
        last_trade_price = self.algo_helper.last_trade_price

        # CURRENT PRICE
        price = self.algo_helper.price

        action = None
        # salvagente, prezzo < last_trade_price - 0.5%
        if last_trade_action == 'buy' and price < last_trade_price - last_trade_price * 0.005:
            action = 'sell'
        # compRa solo se
        elif last_trade_action != 'buy':
            # subito dopo l'incrocio prezzo X ma8 la prezzo > ma8
            # compRa o vendi solo se ma8 => ma29
            if ma8_last >= ma29_last:
                if ma1_prev < ma8_prev and ma1_last > ma8_last:
                    action = 'buy'
        # vendi solo se
        elif last_trade_action == 'buy':
            # SUBITO DOPO L'INCROCIO PREZZO X MA10 IL PREZZO < MA11
            # e vendi anche se ma8 < ma29
            if (ma1_prev > ma11_prev and ma1_last < ma11_last) or ma8_last < ma29_last:
                action = 'sell'
                # ma anche solo se guadagno > 0.12%
                if price - last_trade_price >= 0 and price - last_trade_price < last_trade_price * 0.0012:
                    action = None
                # perdita < -0.13%
                if price - last_trade_price <= 0 and last_trade_price - price < last_trade_price * 0.0013:
                    action = None
        return action
