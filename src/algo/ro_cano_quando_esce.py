from datetime import datetime


class ro_cano_quando_esce:
    def __init__(self, helper, buy_percentage, sell_percentage):
        self.algo_helper = helper
        self.buy_percentage = buy_percentage
        self.sell_percentage = sell_percentage
        self.session = 0
        self.open = False

    @property
    def action(self):

        # MACD
        macd = self.algo_helper.macd

        # tempo del MACD ( da tanti minuti passati (3 minuti ))
        macd_2_min_ago = self.algo_helper.macd_minutes_ago(2)
        macd_3_min_ago = self.algo_helper.macd_minutes_ago(3)
        macd_4_min_ago = self.algo_helper.macd_minutes_ago(4)

        # ( medie mobili utilizzate ) MAs
        ma1_last, ma1_prev = self.algo_helper.ma_last_prev(1)
        ma2_last, ma2_prev = self.algo_helper.ma_last_prev(2)
        ma5_last, ma5_prev = self.algo_helper.ma_last_prev(5)
        ma7_last, ma7_prev = self.algo_helper.ma_last_prev(7)
        ma8_last, ma8_prev = self.algo_helper.ma_last_prev(8)
        ma9_last, ma9_prev = self.algo_helper.ma_last_prev(9)
        ma10_last, ma10_prev = self.algo_helper.ma_last_prev(10)
        ma14_last, ma14_prev = self.algo_helper.ma_last_prev(14)
        ma20_last, ma20_prev = self.algo_helper.ma_last_prev(20)
        ma25_last, ma25_prev = self.algo_helper.ma_last_prev(25)
        ma34_last, ma34_prev = self.algo_helper.ma_last_prev(34)
        ma43_last, ma43_prev = self.algo_helper.ma_last_prev(43)
        ma100_last, ma100_prev = self.algo_helper.ma_last_prev(100)

        # tempo delle medie mobili (MA da tanti minuti passati (per es. ma43 2 minuti))
        ma43_2_min_ago = self.algo_helper.ma_minutes_ago(43, 2)
        ma43_5_min_ago = self.algo_helper.ma_minutes_ago(43, 5)
        ma8_3_min_ago = self.algo_helper.ma_minutes_ago(8, 3)
        ma8_2_min_ago = self.algo_helper.ma_minutes_ago(8, 2)
        ma5_3_min_ago = self.algo_helper.ma_minutes_ago(5, 3)
        ma100_2_min_ago = self.algo_helper.ma_minutes_ago(100, 2)
        ma100_3_min_ago = self.algo_helper.ma_minutes_ago(100, 3)
        ma34_2_min_ago = self.algo_helper.ma_minutes_ago(34, 2)

        # LAST TRADE
        last_trade_action = self.algo_helper.last_trade_action
        last_trade_price = self.algo_helper.last_trade_price
        last_trade_time = self.algo_helper.last_trade_time

        seconds_since_last_trade = 0
        if last_trade_time:
            seconds_since_last_trade = (
                datetime.now()
                - datetime.strptime(
                    last_trade_time[: last_trade_time.index(".")], "%Y-%m-%dT%H:%M:%S"
                )
            ).seconds
            self.algo_helper.info(
                "last trade time {}: seconds since last trade: {}".format(
                    last_trade_time, seconds_since_last_trade
                )
            )

        # HIGHER PRICE MIN AGO (10)
        highest_price_10_min_ago = self.algo_helper.highest_price_minutes_ago(10)

        # CURRENT PRICE
        price = self.algo_helper.price

        action = None
        percentage = 0

        # apre la gabbia, se subito dopo l'incrocio della ma8 X ma34 la ma8 >= ma34
        if ma34_prev and ma34_last and ma8_prev < ma34_prev and ma8_last >= ma34_last:
            if not self.session or not self.open:
                self.session = 1
            self.open = True
            self.algo_helper.info("session {}: open segment".format(self.session))
        # se chiude la gabbia, vende subito
        # subito dopo l'incrocio della ma8 X ma34 la m8 < ma34
        elif ma34_prev and ma34_last and ma8_prev >= ma34_prev and ma8_last < ma34_last:
            self.open = False
            self.algo_helper.info("session {}: closed segment".format(self.session))
        # se chiude la gabbia, vende subito se la perdita > -1,20
        # perdita > -1.20%
        elif (
            price - last_trade_price <= 0
            and last_trade_price - price >= last_trade_price * 0.0120
        ):
            self.open = False
            self.algo_helper.info("session {}: closed segment".format(self.session))

        # compra o vende solo se ma8 >= ma34 ed anche (macd proper <= 6.0 oppure se ((ma8 / ma34 - 1) * 100 > 0.37) and macd < -2.0)
        # speciale: macd > macd_4_min_ago e ma8_last > ma8_10_min_ago
        # macd <= 6.0 a macd < -2.0
        # and (macd < 6.0 or ((ma7_last / ma34_last - 1) * 100 > 0.37) and macd < -30)
        if (
            self.open
            and self.session
            and last_trade_action != "buy"
            and ma1_last > ma34_last
            and ma8_last >= ma34_last
            and ma8_last > ma100_last
            and ma34_last > ma43_last
            and ma5_last >= ma5_3_min_ago
            and ma8_last > ma8_2_min_ago
            and ma8_last > ma8_3_min_ago
            and ma34_last > ma34_2_min_ago
            and ma43_last > ma43_2_min_ago
            and ma43_last >= ma43_5_min_ago
            and ma100_last >= ma100_2_min_ago
            and ma100_last >= ma100_3_min_ago
            and macd >= macd_2_min_ago
            and macd >= macd_3_min_ago
            and macd <= 6.0
            or ((ma7_last / ma34_last - 1) * 100 > 0.37)
            and macd < -30.0
        ):

            percentage = self.buy_percentage

            # TODO: separare la condizione speciale

            # compra sessione UNO solo se
            # subito
            if self.session == 1:
                action = "buy"

            # compra sessione DUE solo se
            # subito dopo l'incrocio del ma5 X ma14 il ma5 > ma14
            # ma8 > ma34 e macd < 1
            # macd_now > macd_2_min_ago
            # TODO: Se subito dopo l'incrocio del ma5 X ma14 il ma5 > ma14 e il prezzo (del BUY) e' > di 0,15% del prezzo piu' alto registrato nella fascia degli ultimi 10 minuti (highest_price_10_min_ago) dal punto di incrocio 5-14

            elif (
                self.session == 2
                and ma5_prev < ma14_prev
                and ma5_last > ma14_last
                and ma8_last > ma43_last
                and macd < 1
                and macd > macd_2_min_ago
                and price
                > (highest_price_10_min_ago + highest_price_10_min_ago * 0.0015)
            ):
                action = "buy"

            # compra sessione X solo se
            # subito dopo l'incrocio ma5 X ma14 la ma5 > ma14
            elif self.session > 2 and ma5_prev < ma14_prev and ma5_last > ma14_last:
                action = "buy"

            # fascia di non compra
            if action == "buy":
                # ma anche solo se ma43_last < ma43_2_min_ago
                if ma43_last < ma43_2_min_ago:
                    action = None

        ###############################################################################################################################################
        ###############################################################################################################################################
        ###############################################################################################################################################

        # vende
        elif last_trade_action == "buy":

            percentage = self.sell_percentage

            # vende subito (rispetando la fascia di non vendita) se la gabbia e' chiusa
            # "condizione corona" se MACD >25 vendi subito
            if not self.open or macd > 25:
                action = "sell"
            # vende subito se ma1<ma8 e ma8 < ma34 e ma34 < ma43 e (( ultimo prezzo / prezzo ultimo buy ) -1 * 100 < -0.75
            elif (
                ma1_last < ma8_last
                and ma8_last < ma34_last
                and ma34_last < ma43_last
                and (float(price) / float(last_trade_price) - 1) * 100 <= -0.75
            ):
                action = "sell"
            # vende subito se dopo 60 minuti ma8<ma34 e ma34<ma43
            elif (
                seconds_since_last_trade > 60 * 60
                and ma8_last < ma34_last
                and ma34_last < ma43_last
            ):
                action = "sell"

            ############################################################################################################################################
            ############################################################################################################################################
            ############################################################################################################################################

            # vende sessione UNO solo se
            elif self.session == 1:
                # da  1 a 30 minuti dal buy 1 se subito dopo l'incrocio della ma1 X ma5 la ma1 < ma5
                if (
                    ma1_prev > ma5_prev
                    and ma1_last < ma5_last
                    and seconds_since_last_trade >= 60
                    and seconds_since_last_trade < 60 * 30
                ):
                    action = "sell"
                # da 30 a 45 minuti dal buy 1 se subito dopo l'incrocio della ma1 X ma10 la ma1 < ma10
                elif (
                    ma1_prev > ma10_prev
                    and ma1_last < ma10_last
                    and seconds_since_last_trade >= 60 * 30
                    and seconds_since_last_trade < 60 * 45
                ):
                    action = "sell"
                # dopo a 45 minuti dal buy 1 se subito dopo l'incrocio della ma1 X ma20 la ma1 < ma20
                elif (
                    ma1_prev > ma20_prev
                    and ma1_last < ma20_last
                    and seconds_since_last_trade >= 60 * 45
                ):
                    action = "sell"

            # vende sessione DUE solo se
            # subito dopo l'incrocio prezzo X ma7 il prezzo < ma8
            # e dopo passato 60 secondi dal last trade
            elif (
                self.session == 2
                and ma1_prev > ma8_prev
                and ma1_last < ma8_last
                and seconds_since_last_trade > 60
            ):
                action = "sell"

            # vende session X solo se
            # subito dopo l'incrocio prezzo X ma7 il prezzo < ma7
            # e dopo passato 60 secondi dal last trade
            elif (
                self.session > 2
                and ma1_prev > ma7_prev
                and ma1_last < ma7_last
                and seconds_since_last_trade > 60
            ):
                action = "sell"

            # fascia di non vendita
            if action == "sell":
                # da 1 a 30 minuti  non vendere se il guadagno e' < 0,08% o se la perdita e' > -1,20 %
                if (
                    seconds_since_last_trade >= 60
                    and seconds_since_last_trade < 60 * 30
                ):
                    if (
                        price - last_trade_price >= 0
                        and price - last_trade_price < last_trade_price * 0.0008
                    ):
                        action = None
                    # perdita < -1.20%
                    elif (
                        price - last_trade_price <= 0
                        and last_trade_price - price > last_trade_price * 0.0120
                    ):
                        action = None
                # da 30 a 45 minuti  non vendere se il guadagno e' < 0,15% o se la perdita e' > -1,20 %
                elif (
                    seconds_since_last_trade >= 60 * 30
                    and seconds_since_last_trade < 60 * 45
                ):
                    # ma anche solo se guadagno > 0.15%
                    if (
                        price - last_trade_price >= 0
                        and price - last_trade_price < last_trade_price * 0.0015
                    ):
                        action = None
                    # perdita < -1.20%
                    elif (
                        price - last_trade_price <= 0
                        and last_trade_price - price > last_trade_price * 0.0120
                    ):
                        action = None
                # da 45 a 60 minuti  non vendere se il guadagno e' < 0,30% o se la perdita e' > -1,20 %
                elif seconds_since_last_trade >= 60 * 45:
                    # ma anche solo se guadagno > 0.30%
                    if (
                        price - last_trade_price >= 0
                        and price - last_trade_price < last_trade_price * 0.0030
                    ):
                        action = None
                    # perdita < -1.20%
                    elif (
                        price - last_trade_price <= 0
                        and last_trade_price - price > last_trade_price * 0.0120
                    ):
                        action = None

        self.algo_helper.info("session {}: action {}".format(self.session, action))

        if action == "sell":
            self.algo_helper.info("session {}: closed session".format(self.session))
            self.session = self.session + 1
            if not self.open:
                self.algo_helper.info(
                    "session {}: restart segment".format(self.session)
                )
                self.session = 0
                self.algo_helper.info(
                    "session {}: restart segment".format(self.session)
                )

        return action, percentage
