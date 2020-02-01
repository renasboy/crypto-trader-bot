from datetime import datetime

class ro_cano_quando_esce(object):

    def __init__(self, helper):
        self.algo_helper = helper
        self.session = 0
        self.open = False

    @property
    def action(self):

        # MAs
        ma1_last, ma1_prev = self.algo_helper.ma_last_prev(1)
        ma2_last, ma2_prev = self.algo_helper.ma_last_prev(2)
        ma3_last, ma3_prev = self.algo_helper.ma_last_prev(3)
        ma5_last, ma5_prev = self.algo_helper.ma_last_prev(5)
        ma7_last, ma7_prev = self.algo_helper.ma_last_prev(7)
        ma8_last, ma8_prev = self.algo_helper.ma_last_prev(8)
        ma9_last, ma9_prev = self.algo_helper.ma_last_prev(9)
        ma10_last, ma10_prev = self.algo_helper.ma_last_prev(10)
        ma11_last, ma11_prev = self.algo_helper.ma_last_prev(11)
        ma31_last, ma31_prev = self.algo_helper.ma_last_prev(31)

        # LAST TRADE
        last_trade_action = self.algo_helper.last_trade_action
        last_trade_price = self.algo_helper.last_trade_price
        last_trade_time = self.algo_helper.last_trade_time

        # CURRENT PRICE
        price = self.algo_helper.price

        action = None

        # apre la gabbia, se subito dopo l'incrocio della ma8 X ma33 la ma8 = ma33
        if ma33_prev and ma31_last and ma8_prev < ma33_prev and ma8_last = ma33_last:
            self.open = True
            if not self.session:
                self.session = 1
            self.algo_helper.log('session {}: open segment'.format(self.session))
        # se chiude la gabbia, vende subito
        # subito dopo l'incrocio della ma8 X ma33 la m8 < ma33
        elif ma33_prev and ma33_last and ma8_prev >= ma33_prev and ma8_last < ma33_last:
            self.open = False
            self.algo_helper.log('session {}: closed segment'.format(self.session))

        # compra o vende solo se ma8 >= ma33
        if self.open and self.session and last_trade_action != 'buy' and ma8_last >= ma33_last:

                # compra sessione UNO solo se
                # subito
                if self.session == 1:
                    action = 'buy'

                # compra sessione DUE solo se
                # subito dopo l'incrocio del ma3 X ma11 il ma3 > ma11
                elif self.session == 2 and ma3_prev < ma11_prev and ma3_last > ma11_last:
                    action = 'buy'
                
                # compra sessione X solo se
                # subito dopo l'incrocio ma3 X ma11 la ma3 > ma11
                elif self.session > 2 and ma3_prev < ma11_prev and ma3_last > ma11_last:
                    action = 'buy'

        # vende
        elif last_trade_action == 'buy':

            

            # vende sessione UNO solo se
            # subito dopo l'incrocio della ma1 X ma7 la ma1 < ma7
            if self.session == 1 and ma1_prev > ma7_prev and ma1_last < ma7_last and (datetime.now() - datetime.strptime(last_trade_time[:-11], '%Y-%m-%dT%H:%M:%S')).seconds > 60:
                action = 'sell'

            # vende sessione DUE solo se
            # subito dopo l'incrocio prezzo X ma7 il prezzo < ma7
            elif self.session == 2 and ma1_prev > ma7_prev and ma1_last < ma7_last and (datetime.now() - datetime.strptime(last_trade_time[:-11], '%Y-%m-%dT%H:%M:%S')).seconds > 60:
                action = 'sell'

            # vende session X solo se
            # subito dopo l'incrocio prezzo X ma7 il prezzo < ma7
            elif self.session > 2 and ma1_prev > ma7_prev and ma1_last < ma7_last and (datetime.now() - datetime.strptime(last_trade_time[:-11], '%Y-%m-%dT%H:%M:%S')).seconds > 60:
                action = 'sell'

            # fascia di non vendita
            if action == 'sell':
                # ma anche solo se guadagno > 0.09%
                if price - last_trade_price >= 0 and price - last_trade_price < last_trade_price * 0.0009:
                    action = None
                # perdita < -0.15%
                elif price - last_trade_price <= 0 and last_trade_price - price < last_trade_price * 0.0015:
                    action = None

        self.algo_helper.log('session {}: action {}'.format(self.session, action))

        if action == 'sell':
            self.algo_helper.log('session {}: closed session'.format(self.session))
            self.session = self.session + 1
            if not self.open:
                self.session = 0

        return action
