from datetime import datetime

class ro_cano_quando_esce(object):

    def __init__(self, helper):
        self.algo_helper = helper
        self.session = 0

    @property
    def action(self):

        # MAs
        ma1_last, ma1_prev = self.algo_helper.ma_last_prev(1)
        ma2_last, ma2_prev = self.algo_helper.ma_last_prev(2)
        ma5_last, ma5_prev = self.algo_helper.ma_last_prev(5)
        ma8_last, ma8_prev = self.algo_helper.ma_last_prev(8)
        ma10_last, ma10_prev = self.algo_helper.ma_last_prev(10)
        ma11_last, ma11_prev = self.algo_helper.ma_last_prev(11)
        ma30_last, ma30_prev = self.algo_helper.ma_last_prev(30)

        # LAST TRADE
        last_trade_action = self.algo_helper.last_trade_action
        last_trade_price = self.algo_helper.last_trade_price
        last_trade_time = self.algo_helper.last_trade_time

        # CURRENT PRICE
        price = self.algo_helper.price

        action = None

        # apre la gabbia, se subito dopo l'incrocio della ma8 X ma31 la ma8 >= ma30
        if ma30_prev and ma30_last and ma8_prev < ma30_prev and ma8_last >= ma30_last:
            self.session = 1
            self.algo_helper.log('session {}: open segment'.format(self.session))

        # compra o vende solo se ma8 >= ma30
        if self.session and ma8_last >= ma30_last:

            # salvagente, vende subito se il prezzo < last_trade_price - 0.16%
            if last_trade_action == 'buy' and price < last_trade_price - last_trade_price * 0.0016:
                action = 'sell'

            # compra
            elif last_trade_action != 'buy':

                # compra sessione UNO solo se
                # subito dopo l'incrocio del prezzo X ma2 il prezzo > ma2
                if self.session == 1 and ma1_prev < ma2_prev and ma1_last > ma2_last:
                    action = 'buy'

                # compra sessione DUE solo se
                # subito dopo l'incrocio del prezzo X ma5 il prezzo > ma5
                elif self.session == 2 and ma1_prev < ma5_prev and ma1_last > ma5_last:
                    action = 'buy'
                
                # compra sessione X solo se
                # subito dopo l'incrocio ma2 X ma11 la ma2 > ma11
                elif self.session > 2 and ma2_prev < ma11_prev and ma2_last > ma11_last:
                    action = 'buy'

            # vende
            elif last_trade_action == 'buy':

                # vende sessione UNO solo se
                # subito dopo l'incrocio della ma2 X ma10 la ma2 < ma10
                if self.session == 1 and ma2_prev > ma10_prev and ma2_last < ma10_last and (datetime.now() - datetime.strptime(last_trade_time[:-11], '%Y-%m-%dT%H:%M:%S')).seconds > 60:
                    action = 'sell'

                # vende sessione DUE solo se
                # subito dopo l'incrocio prezzo X ma11 il prezzo < ma11
                elif self.session == 2 and ma1_prev > ma11_prev and ma1_last < ma11_last and (datetime.now() - datetime.strptime(last_trade_time[:-11], '%Y-%m-%dT%H:%M:%S')).seconds > 60:
                    action = 'sell'

                # vende session X solo se
                # subito dopo l'incrocio prezzo X ma11 il prezzo < ma11
                elif self.session > 2 and ma1_prev > ma11_prev and ma1_last < ma11_last:
                    action = 'sell'

                # fascia di non vendita
                if action == 'sell':
                    # ma anche solo se guadagno > 0.08%
                    if price - last_trade_price >= 0 and price - last_trade_price < last_trade_price * 0.0008:
                        action = None
                    # perdita < -0.04%
                    elif price - last_trade_price <= 0 and last_trade_price - price < last_trade_price * 0.0004:
                        action = None

            self.algo_helper.log('session {}: action {}'.format(self.session, action))

            if action == 'sell':
                self.algo_helper.log('session {}: closed session'.format(self.session))
                self.session = self.session + 1

        # se chiude la gabbia, vende subito
        # subito dopo l'incrocio della ma8 X ma30 la m8 < ma30 
        elif ma8_prev >= ma30_prev and ma8_last < ma30_last:
            self.algo_helper.log('session {}: closed segment'.format(self.session))
            self.session = 0
            if last_trade_action == 'buy':
                action = 'sell'

        return action
