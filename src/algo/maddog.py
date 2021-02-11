class maddog:
    def __init__(self, helper):
        self.algo_helper = helper
        self.session = 0
        self.open = False

    @property
    def action(self):

        # TIME dopo quanto tempo ro cano ritorna automaticamente ( per esempio 60 minuti x 60 = 3600 secondi ) e durata segmento in cui si aggiunge una condizione per il BUY
        max_hold_time_in_seconds = 3600
        min_buy_delay_in_seconds = 2100

        # MACD di 1-2-3-4 minuti prima
        # macd = self.algo_helper.macd

        # macd_2_min_ago = self.algo_helper.macd_minutes_ago(2)

        # moving average (2-3-4-5-x)
        ma2_last, ma2_prev = self.algo_helper.ma_last_prev(2)
        ma4_last, ma4_prev = self.algo_helper.ma_last_prev(4)
        ma5_last, ma5_prev = self.algo_helper.ma_last_prev(5)
        ma7_last, ma7_prev = self.algo_helper.ma_last_prev(7)
        ma11_last, ma11_prev = self.algo_helper.ma_last_prev(11)
        ma13_last, ma13_prev = self.algo_helper.ma_last_prev(13)
        ma15_last, ma15_prev = self.algo_helper.ma_last_prev(15)
        ma16_last, ma16_prev = self.algo_helper.ma_last_prev(16)
        ma18_last, ma18_prev = self.algo_helper.ma_last_prev(18)
        ma20_last, ma20_prev = self.algo_helper.ma_last_prev(20)
        ma21_last, ma21_prev = self.algo_helper.ma_last_prev(21)
        ma28_last, ma28_prev = self.algo_helper.ma_last_prev(28)
        ma34_last, ma34_prev = self.algo_helper.ma_last_prev(34)
        ma43_last, ma43_prev = self.algo_helper.ma_last_prev(43)
        ma50_last, ma50_prev = self.algo_helper.ma_last_prev(50)
        #
        ma20_last, ma20_prev = self.algo_helper.ma_last_prev(20)
        ma60_last, ma60_prev = self.algo_helper.ma_last_prev(60)
        ma85_last, ma85_prev = self.algo_helper.ma_last_prev(85)
        ma100_last, ma100_prev = self.algo_helper.ma_last_prev(100)
        #
        

        # moving average (2-3-4-5-7-8-20-43-100) di x minuti prima (NON METTERE MAI 1 min !)
        ma2_2_min_ago = self.algo_helper.ma_minutes_ago(2, 2)
        ma4_2_min_ago = self.algo_helper.ma_minutes_ago(4, 2)
        ma5_2_min_ago = self.algo_helper.ma_minutes_ago(5, 2)
        ma5_3_min_ago = self.algo_helper.ma_minutes_ago(5, 3)
        ma7_2_min_ago = self.algo_helper.ma_minutes_ago(7, 2)
        ma11_2_min_ago = self.algo_helper.ma_minutes_ago(11, 2)
        ma15_5_min_ago = self.algo_helper.ma_minutes_ago(15, 5)
        ma16_2_min_ago = self.algo_helper.ma_minutes_ago(16, 2)
        ma20_2_min_ago = self.algo_helper.ma_minutes_ago(20, 2)
        ma60_2_min_ago = self.algo_helper.ma_minutes_ago(60, 2)
        ma85_3_min_ago = self.algo_helper.ma_minutes_ago(85, 3)
        ma100_13_min_ago = self.algo_helper.ma_minutes_ago(100, 13)
        
        
        # LAST TRADE
        last_trade_action = self.algo_helper.last_trade_action
        # last_trade_time = self.algo_helper.last_trade_time
        last_trade_price = self.algo_helper.last_trade_price
        seconds_since_last_trade = self.algo_helper.seconds_since_last_trade

        # PREZZO DI ADESSO (di mercato) - CURRENT PRICE
        price = self.algo_helper.price

        # PREZZO PRECEDENTE (di mercato) - PREV PRICE
        price_1_min_ago = self.algo_helper.price_minutes_ago(1)
        price_2_min_ago = self.algo_helper.price_minutes_ago(2)
        price_3_min_ago = self.algo_helper.price_minutes_ago(3)
        price_7_min_ago = self.algo_helper.price_minutes_ago(7)
    
        # formula deviation per comprare un po' piu' sopra del SELL
        deviation = (ma2_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.log("deviation: {}".format(deviation))

        # formula DEVIATION_ma (per comprare durante il TREND RIBASSISTA)
        deviation_ma = (ma2_last / ma28_last - 1) * 100 if ma28_last else 0
        self.algo_helper.log("deviation_ma: {}".format(deviation_ma))

        action = None

        #######################################################################
        # APRE E CHIUDE GABBIA
        # SI APRE LA GABBIA SE
        if ma100_last > ma100_13_min_ago:
            # NON TOCCARE QUESTA CONDIZIONE SERVE PER APERTURA DI GABBIA
            if not self.session or not self.open:
                self.session = 1
                self.open = True
                self.algo_helper.log("session {}: open segment".format(self.session))
        # SI CHIUDE LA GABBIA SE
        else:
            self.open = False
            self.algo_helper.log("session {}: closed segment".format(self.session))

        #######################################################################
        # COMPRA
        # NON TOCCARE QUESTA CONDIZIONE (QUESTA DICE CHE STA IN MODO BUY, DEVO COMPRARE)
        if self.open and self.session and last_trade_action != "buy":

            # COMPRA UN PO' PIU' SOPRA DELL' ULTIMO SELL ( aggiungere compra un po' piu' sopra dell' ultimo BUY deviation > 0.20 )
            if (
                seconds_since_last_trade > 0
                and seconds_since_last_trade <= min_buy_delay_in_seconds
                and deviation > 0.18
            ) or (
                seconds_since_last_trade == 0
                or seconds_since_last_trade > min_buy_delay_in_seconds
            ):

                # COMPRA sessione 1
                if self.session == 1:
                    if (
                        ma2_last > ma2_2_min_ago
                        and ma4_last > ma4_2_min_ago
                        and ma5_last > ma5_2_min_ago
                        and ma5_2_min_ago > ma5_3_min_ago
                        and ma7_last > ma7_2_min_ago
                        and ma11_last >= ma11_2_min_ago
                        and ma15_last > ma15_5_min_ago
                        and ma16_last >= ma16_2_min_ago
                        and ma18_last >= ma21_last
                        
                        and price > price_1_min_ago
                        and price > price_2_min_ago
                        and price > price_3_min_ago
                        and price > price_7_min_ago
                        
                        and ma20_last >= ma20_2_min_ago
                        #and ma60_last >= ma60_2_min_ago
                        
                        #and ma20_last >= ma60_last
                        
                        and ma85_last >= ma100_last
                        #and ma85_last >= ma85_3_min_ago
                        and ma100_last >= ma100_13_min_ago
                        
                        and ma20_last >= ma60_last
                        
                    ):
                        action = "buy"

                # COMPRA sessione 2
                elif self.session == 2:
                    if (
                        ma2_last > ma2_2_min_ago
                        and ma4_last > ma4_2_min_ago
                        and ma5_last > ma5_2_min_ago
                        and ma5_2_min_ago > ma5_3_min_ago
                        and ma7_last > ma7_2_min_ago
                        and ma11_last >= ma11_2_min_ago
                        and ma15_last > ma15_5_min_ago
                        and ma16_last >= ma16_2_min_ago
                        #and ma18_last >= ma21_last
                       
                        and price > price_1_min_ago
                        and price > price_2_min_ago
                        and price > price_3_min_ago
                        and price > price_7_min_ago
                        
                        and ma20_last >= ma20_2_min_ago
                        and ma60_last >= ma60_2_min_ago
                        
                        and ma20_last >= ma60_last
                        
                        and ma85_last >= ma100_last
                        and ma85_last >= ma85_3_min_ago
                        and ma100_last >= ma100_13_min_ago
                        
                        and ma20_last >= ma60_last
                        
                        
                    ):
                        action = "buy"

                        
                        
                        
                # COMPRA sessione 3 in poi
                else:
                    if (
                        ma2_last > ma2_2_min_ago
                        and ma4_last > ma4_2_min_ago
                        and ma5_last > ma5_2_min_ago
                        and ma5_2_min_ago > ma5_3_min_ago
                        and ma7_last > ma7_2_min_ago
                        and ma11_last >= ma11_2_min_ago
                        and ma15_last >= ma15_5_min_ago
                        
                        and deviation_ma > 0.25
                        # and ma16_last > ma16_2_min_ago
                    
                        and price > price_1_min_ago
                        and price > price_2_min_ago
                        and price > price_3_min_ago
                        and price > price_7_min_ago
                        
                        and ma20_last >= ma20_2_min_ago
                        #and ma60_last >= ma60_2_min_ago
                        
                        and ma20_last >= ma60_last
                        
                        and ma85_last >= ma100_last
                        and ma85_last >= ma85_3_min_ago
                        and ma100_last >= ma100_13_min_ago
                        
                        and ma20_last >= ma60_last
                        
                        
                    ):
                        action = "buy"

        #######################################################################
        # VENDA
        # NON TOCCARE QUESTA CONDIZIONE (QUESTA DICE CHE STA IN MODO SELL, DEVO VENDERE)
        elif last_trade_action == "buy":

            self.algo_helper.log("ma2_prev: {}".format(ma2_prev))
            self.algo_helper.log("ma7_prev: {}".format(ma7_prev))
            self.algo_helper.log("ma2_last: {}".format(ma2_last))
            self.algo_helper.log("ma7_last: {}".format(ma7_last))
            self.algo_helper.log("deviation: {}".format(deviation))
            self.algo_helper.log("session: {}".format(self.session))

            # VENDE
            
            
            

            # VENDE sessione 1
            if self.session == 1:
                
                if (
                    ma100_last > ma100_13_min_ago
                    and ma2_last < ma34_last
                    and deviation > 0.01
                ):
                   
                    action = "sell"     
                    

                    
                    
                elif (
                    ma100_last > ma100_13_min_ago
                    and ma2_last < ma15_last
                    and deviation < -0.82
                ):
                    action = "sell"    
                
                    
                    
                        
                        
                        
                        

            # VENDE sessione 2
            elif self.session == 2:
               
                if (
                    ma100_last > ma100_13_min_ago
                    and ma2_last < ma13_last
                    and deviation > 0.10
                ):
                   
                    action = "sell"     
                    

                    
                    
                elif (
                    ma100_last > ma100_13_min_ago
                    and ma2_last < ma11_last
                    and deviation < -0.82
                ):
                    action = "sell"      
                       
                        
                        
                        
                        

            # VENDE sessione 3 in poi
            else:
                #if ma2_last < ma16_last:
                if (
                    ma100_last > ma100_13_min_ago
                    and ma2_last < ma15_last
                    and deviation > 0.12
                ):
                   
                    action = "sell"     
                    

                    
                    
                elif (
                    ma100_last > ma100_13_min_ago
                    and ma2_last < ma13_last
                    and deviation < -0.82
                ):
                    action = "sell"        
                        #action = "sell"
                        
                        
                        
                  
                        

            # STOP LOSS (salvagente)
            if deviation < -1.20 and ma2_last < ma21_last:
                action = "sell"

            
           
            
            

            
            # 1) ATTESA DI 1 ORA = 3600 SECONDI "max hold time" " DOPO UN' ORA VENDE SUBITO "
            #if seconds_since_last_trade > max_hold_time_in_seconds:
            if seconds_since_last_trade > max_hold_time_in_seconds and ma2_last < ma20_last:
                
                    
                action = "sell"

        self.algo_helper.log("action {}".format(action))

        if action == "sell":
            self.session += 1

        return action


# grazie compa #####
