#import inspect
#inspect.getframeinfo(inspect.currentframe()).lineno

#self.algo_helper.log("SELL @ LINE {}".format(__line__))



class ro_cano_che_ritorna:
    def __init__(self, helper):
        self.algo_helper = helper
        self.session = 0
        self.open = False

    @property
    def action(self):

        # moving average (2-3-4-5-x)
        ma2_last, ma2_prev = self.algo_helper.ma_last_prev(2)
        ma3_last, ma3_prev = self.algo_helper.ma_last_prev(3)
        ma4_last, ma4_prev = self.algo_helper.ma_last_prev(4)
        ma5_last, ma5_prev = self.algo_helper.ma_last_prev(5)
        ma7_last, ma7_prev = self.algo_helper.ma_last_prev(7)
        ma8_last, ma8_prev = self.algo_helper.ma_last_prev(8)
        ma9_last, ma9_prev = self.algo_helper.ma_last_prev(9)
        ma10_last, ma10_prev = self.algo_helper.ma_last_prev(10)
        ma11_last, ma11_prev = self.algo_helper.ma_last_prev(11)
        ma12_last, ma12_prev = self.algo_helper.ma_last_prev(12)
        ma13_last, ma13_prev = self.algo_helper.ma_last_prev(13)
        ma14_last, ma14_prev = self.algo_helper.ma_last_prev(14)
        ma15_last, ma15_prev = self.algo_helper.ma_last_prev(15)
        ma16_last, ma16_prev = self.algo_helper.ma_last_prev(16)
        ma18_last, ma18_prev = self.algo_helper.ma_last_prev(18)
        ma20_last, ma20_prev = self.algo_helper.ma_last_prev(20)
        ma21_last, ma21_prev = self.algo_helper.ma_last_prev(21)
        ma22_last, ma22_prev = self.algo_helper.ma_last_prev(22)
        ma24_last, ma24_prev = self.algo_helper.ma_last_prev(24)
        ma25_last, ma25_prev = self.algo_helper.ma_last_prev(25)
        ma28_last, ma28_prev = self.algo_helper.ma_last_prev(28)
        ma32_last, ma32_prev = self.algo_helper.ma_last_prev(32)
        ma36_last, ma36_prev = self.algo_helper.ma_last_prev(36)
        ma50_last, ma50_prev = self.algo_helper.ma_last_prev(50)
        ma85_last, ma85_prev = self.algo_helper.ma_last_prev(85)
        ma100_last, ma100_prev = self.algo_helper.ma_last_prev(100)

        # moving average (2-3-4-5-7-8-20-43-100) di x minuti prima
        ma2_2_min_ago = self.algo_helper.ma_minutes_ago(2, 2)
        ma2_3_min_ago = self.algo_helper.ma_minutes_ago(2, 3)
        ma2_15_min_ago = self.algo_helper.ma_minutes_ago(2, 15)
        ma2_17_min_ago = self.algo_helper.ma_minutes_ago(2, 17)
        ma2_22_min_ago = self.algo_helper.ma_minutes_ago(2, 22)
        ma2_24_min_ago = self.algo_helper.ma_minutes_ago(2, 24)
        ma4_2_min_ago = self.algo_helper.ma_minutes_ago(4, 2)
        ma8_5_min_ago = self.algo_helper.ma_minutes_ago(8, 5)
        ma10_2_min_ago = self.algo_helper.ma_minutes_ago(10, 2)
        ma32_3_min_ago = self.algo_helper.ma_minutes_ago(32, 3)
        ma33_3_min_ago = self.algo_helper.ma_minutes_ago(33, 3)
        ma36_2_min_ago = self.algo_helper.ma_minutes_ago(36, 2)
        ma50_2_min_ago = self.algo_helper.ma_minutes_ago(50, 2)
        ma50_5_min_ago = self.algo_helper.ma_minutes_ago(50, 5)
        ma100_2_min_ago = self.algo_helper.ma_minutes_ago(100, 2)
        ma100_13_min_ago = self.algo_helper.ma_minutes_ago(100, 13)
        
        
        # LAST TRADE
        last_trade_action = self.algo_helper.last_trade_action
        last_trade_price = self.algo_helper.last_trade_price
        seconds_since_last_trade = self.algo_helper.seconds_since_last_trade

        # PREV TRADE
        # prev_trade_action = self.algo_helper.prev_trade_action
        # prev_trade_time = self.algo_helper.prev_trade_time
        prev_trade_price = self.algo_helper.prev_trade_price
        seconds_since_prev_trade = self.algo_helper.seconds_since_prev_trade

        # PREZZO DI ADESSO (di mercato) - CURRENT PRICE
        price = self.algo_helper.price

        # PREZZO PRECEDENTE (di mercato) - PREV PRICE
        price_1_min_ago = self.algo_helper.price_minutes_ago(1)
        price_2_min_ago = self.algo_helper.price_minutes_ago(2)
        price_3_min_ago = self.algo_helper.price_minutes_ago(3)

        # VENDE DOPO 6000 secondi = 100 minuti ("e se") ro cano torna a casa riga 331
        max_hold_time_in_seconds = 6000

        # VENDE DOPO 600 secondi = 10 minuti ("e se") - ro cano perde la forza - riga 323
        max_hold_without_force_time_in_seconds = 600

        # TEMPO in cui (PER COMPRARE) (a tutte le condizioni gia' attive) SI AGGIUNGE una condizione aggiuntiva LA DEVIATION !

        # per ULTIMO trade ( 10 minuti = 10 * 60 = 600 secondi )
        min_buy_delay_in_seconds = 600

        # per PENULTIMO trade ( 15 minuti = 15 * 60 = 900 secondi )
        min_prev_buy_delay_in_seconds = 900

        # formula DEVIATION last_trade (di solito l' ultimo SELL) per comprare UN PO' PIU' SOPRA DEL LAST TRADE
        deviation = (ma2_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.log("deviation: {}".format(deviation))

        # formula DEVIATION prev_trade (qualche volta l' ultimo BUY ) per comprare UN PO' PIU' SOPRA DEL PREV TRADE
        deviation_prev = (price / prev_trade_price - 1) * 100 if prev_trade_price else 0
        self.algo_helper.log("deviation_prev: {}".format(deviation_prev))

        # formula DEVIATION_ma (per comprare durante il TREND RIBASSISTA)
        # pronto a sostituire ma2_last con ma3_last
        deviation_ma = (ma2_last / ma18_last - 1) * 100 if ma18_last else 0
        self.algo_helper.log("deviation_ma: {}".format(deviation_ma))

        # DEFAULT ACTION DICE DI NON FARE NIENTE (=None, NON TOCCARE)
        action = None

        #######################################################################

        # APRE E CHIUDE GABBIA

        # SI APRE LA GABBIA SE
        if ma50_last >= ma50_2_min_ago:
            # NON TOCCARE QUESTA CONDIZIONE SERVE PER APERTURA DI GABBIA
            if not self.session or not self.open:
                self.session = 1
                self.open = True
                self.algo_helper.log("session {}: open segment".format(self.session))

        # SI CHIUDE LA GABBIA SE
        elif self.open:
            self.open = False
            self.algo_helper.log("session {}: closed segment".format(self.session))

        #######################################################################

        # COMPRA
        # NON TOCCARE QUESTA CONDIZIONE (QUESTA DICE CHE STA IN MODO BUY, DEVO COMPRARE)
        if self.open and self.session and last_trade_action != "buy":

            # COMPRA UN PO' PIU' SOPRA DELL' ULTIMO TRADE SE DEVIATION > 0.23 nei 540 secondi  ( quasi sempre IL SELL )
            # COMPRA UN PO' PIU' SOPRA DEL PENULTIMO TRADE SE DEVIATION > 0.15 nei 300 secondi ( qualche volta IL BUY)

            if (
                (
                    seconds_since_last_trade > 0
                    and seconds_since_last_trade <= min_buy_delay_in_seconds
                    and deviation > 0.18
                )
                or (
                    seconds_since_prev_trade > 0
                    and seconds_since_prev_trade <= min_prev_buy_delay_in_seconds
                    and deviation_prev > 0.15
                )
                or (
                    seconds_since_last_trade == 0
                    or seconds_since_last_trade > min_buy_delay_in_seconds
                )
            ):

  
###################################################################################################################################################

                # COMPRA sessione 1   ( qua rompo, compa caro, )
          
                if self.session == 1:
               
                    if (
                    
                        ma50_last >= ma50_2_min_ago
                        and ma36_last >= ma36_2_min_ago
                        and ma8_last >= ma14_last
                        and deviation_ma >= 0.13
                        
                        
                        
                        #and ma85_last >= ma100_last
                        #and ma50_last >= ma50_2_min_ago
                        #and ma8_last >= ma8_5_min_ago
                        
                        #and ma18_last > ma22_last 
                        # per non comprare con breve andamento laterale ( ma il trend e' ribassista )
                        
                        and ma2_last > ma2_2_min_ago
                        and ma2_last > ma2_3_min_ago
                        
                        and ma2_last >= ma7_last
                        and ma4_last > ma4_2_min_ago
                        #and ma7_last >= ma15_last
                        #and ma10_last >= ma10_2_min_ago
                        #and ma11_last > ma15_last
                        
                        and price > price_1_min_ago
                        and price > price_2_min_ago
                        and price > price_3_min_ago
                 
                    ):

                        action = "buy"

                        
                        
                    elif (
                    
                          ma50_last < ma50_2_min_ago
                          and ma36_last < ma36_2_min_ago
                          and ma9_last >= ma15_last
                        
                        
                          #and ma85_last < ma100_last
                          #and ma50_last < ma50_5_min_ago
                          #and ma8_last < ma8_5_min_ago
                          
                          
                          #and ma16_last >= ma24_last
                          
                          
                          
                          #and ma2_last > ma2_15_min_ago
                          #and ma2_last > ma2_17_min_ago
                          #and ma2_last > ma2_22_min_ago
                          #and ma2_last > ma2_24_min_ago ( ultima speranza ) 
                          
                          
                          and ma2_last > ma2_2_min_ago
                          and ma2_last > ma7_last
                          and ma4_last > ma4_2_min_ago
                          #and ma7_last >= ma15_last
                          #and ma10_last >= ma10_2_min_ago
                          #and ma11_last >= ma15_last
                        
                          #and ma18_last > ma22_last 
                          # per non comprare durante il ribasso ( prezzo e ma2 gia' sono andati giu' ! )
                        
                          and price > price_1_min_ago
                          and price > price_2_min_ago
                          and price > price_3_min_ago
                 
                    ):

                        action = "buy"
                    
                    
                    
                    
                    elif (
                    
                          ma50_last < ma50_2_min_ago
                          and ma36_last > ma36_2_min_ago
                          and ma9_last >= ma15_last
                        
                        
                          #and ma85_last < ma100_last
                          #and ma50_last < ma50_5_min_ago
                          #and ma8_last < ma8_5_min_ago
                          
                          
                          #and ma16_last >= ma24_last
                          
                          
                          
                          #and ma2_last > ma2_15_min_ago
                          #and ma2_last > ma2_17_min_ago
                          #and ma2_last > ma2_22_min_ago
                          #and ma2_last > ma2_24_min_ago ( ultima speranza ) 
                          
                          
                          and ma2_last > ma2_2_min_ago
                          and ma2_last > ma7_last
                          and ma4_last > ma4_2_min_ago
                          #and ma7_last >= ma15_last
                          #and ma10_last >= ma10_2_min_ago
                          #and ma11_last >= ma15_last
                        
                          #and ma18_last > ma22_last 
                          # per non comprare durante il ribasso ( prezzo e ma2 gia' sono andati giu' ! )
                        
                          and price > price_1_min_ago
                          and price > price_2_min_ago
                          and price > price_3_min_ago
                 
                    ):

                        action = "buy"
                        
                        
                        
                        
                        
                    elif (
                    
                          ma50_last > ma50_2_min_ago
                          and ma36_last < ma36_2_min_ago
                          and ma8_last >= ma14_last
                        
                        
                          #and ma85_last < ma100_last
                          #and ma50_last < ma50_5_min_ago
                          #and ma8_last < ma8_5_min_ago
                          
                          
                          #and ma16_last >= ma24_last
                          
                          
                          
                          #and ma2_last > ma2_15_min_ago
                          #and ma2_last > ma2_17_min_ago
                          #and ma2_last > ma2_22_min_ago
                          #and ma2_last > ma2_24_min_ago ( ultima speranza ) 
                          
                          
                          and ma2_last > ma2_2_min_ago
                          and ma2_last > ma7_last
                          and ma4_last > ma4_2_min_ago
                          #and ma7_last >= ma15_last
                          #and ma10_last >= ma10_2_min_ago
                          #and ma11_last >= ma15_last
                        
                          #and ma18_last > ma22_last 
                          # per non comprare durante il ribasso ( prezzo e ma2 gia' sono andati giu' ! )
                        
                          and price > price_1_min_ago
                          and price > price_2_min_ago
                          and price > price_3_min_ago
                 
                    ):

                        action = "buy"
                    
                    
                    
                    
                    
                    
                    
                  
##############################################################################################################################
                        
    

                # COMPRA sessione 2
        
                elif self.session == 2:
              
                    if (
                    
                        ma50_last >= ma50_2_min_ago
                        and ma36_last >= ma36_2_min_ago
                        and ma8_last >= ma14_last
                        and deviation > 0.13
                        
                        
                        #and ma85_last >= ma100_last
                        #and ma50_last >= ma50_5_min_ago
                        #and ma8_last >= ma8_5_min_ago
                        
                        #and ma2_last > ma2_15_min_ago
                        #and ma2_last > ma2_17_min_ago
                        
                        and ma2_last > ma7_last
                        and ma2_last > ma2_2_min_ago
                        and ma4_last > ma4_2_min_ago
                        #and ma7_last >= ma15_last
                        #and ma10_last >= ma10_2_min_ago
                        #and ma11_last > ma15_last
                        
                        and price > price_1_min_ago
                        and price > price_2_min_ago
                        #and price > price_3_min_ago
                 
                    ):

                        action = "buy"

                        
                        
                    elif (
                    
                          ma50_last < ma50_2_min_ago
                          and ma36_last < ma36_2_min_ago
                          and ma9_last >= ma15_last
                          and deviation_ma >= 0.18
                        
                          #and ma85_last < ma100_last
                          #and ma50_last < ma50_5_min_ago
                          #and ma8_last < ma8_5_min_ago
                        
                          #and ma2_last > ma2_15_min_ago
                          #and ma2_last > ma2_17_min_ago
                        
                        
                          
                          and ma2_last > ma7_last
                          and ma2_last > ma2_2_min_ago
                          and ma4_last > ma4_2_min_ago
                          #and ma7_last >= ma15_last
                          #and ma10_last >= ma10_2_min_ago
                          #and ma11_last > ma15_last
                        
                          and price > price_1_min_ago
                          and price > price_2_min_ago
                          #and price > price_3_min_ago
                 
                    ):

                        action = "buy"
                    
                    
                    
                    elif (
                    
                          ma50_last < ma50_2_min_ago
                          and ma36_last > ma36_2_min_ago
                          and ma9_last >= ma15_last
                          and deviation_ma > 0.18
                          
                        
                        
                          #and ma85_last < ma100_last
                          #and ma50_last < ma50_5_min_ago
                          #and ma8_last < ma8_5_min_ago
                          
                          
                          #and ma16_last >= ma24_last
                          
                          
                          
                          #and ma2_last > ma2_15_min_ago
                          #and ma2_last > ma2_17_min_ago
                          #and ma2_last > ma2_22_min_ago
                          #and ma2_last > ma2_24_min_ago ( ultima speranza ) 
                          
                          
                          and ma2_last > ma2_2_min_ago
                          and ma2_last > ma7_last
                          and ma4_last > ma4_2_min_ago
                          #and ma7_last >= ma15_last
                          #and ma10_last >= ma10_2_min_ago
                          #and ma11_last >= ma15_last
                        
                          #and ma18_last > ma22_last 
                          # per non comprare durante il ribasso ( prezzo e ma2 gia' sono andati giu' ! )
                        
                          and price > price_1_min_ago
                          and price > price_2_min_ago
                          and price > price_3_min_ago
                 
                    ):

                        action = "buy"
                        
                        
                        
                        
                        
                    elif (
                    
                          ma50_last > ma50_2_min_ago
                          and ma36_last < ma36_2_min_ago
                          and ma8_last >= ma14_last
                        
                        
                          #and ma85_last < ma100_last
                          #and ma50_last < ma50_5_min_ago
                          #and ma8_last < ma8_5_min_ago
                          
                          
                          #and ma16_last >= ma24_last
                          #and deviation_ma > 0.40
                          # vedi riga 100 !
                          
                          #and ma2_last > ma2_15_min_ago
                          #and ma2_last > ma2_17_min_ago
                          #and ma2_last > ma2_22_min_ago
                          #and ma2_last > ma2_24_min_ago ( ultima speranza ) 
                          
                          
                          and ma2_last > ma2_2_min_ago
                          and ma2_last > ma7_last
                          and ma4_last > ma4_2_min_ago
                          #and ma7_last >= ma15_last
                          #and ma10_last >= ma10_2_min_ago
                          #and ma11_last >= ma15_last
                        
                          #and ma18_last > ma22_last 
                          # per non comprare durante il ribasso ( prezzo e ma2 gia' sono andati giu' ! )
                        
                          and price > price_1_min_ago
                          and price > price_2_min_ago
                          and price > price_3_min_ago
                 
                    ):

                        action = "buy"
                
                   
#############################################################################################################################################



                # COMPRA sessione 3 in poi
    
                elif self.session == 3:
            
            
            
                    if (
                    
                        ma50_last >= ma50_2_min_ago
                        and ma36_last >= ma36_2_min_ago
                        and ma8_last >= ma12_last
                        and deviation_ma >= 0.15
                        
                        #and ma85_last >= ma100_last
                        #and ma50_last >= ma50_5_min_ago
                        #and ma8_last >= ma8_5_min_ago
                        
                        #and ma2_last > ma2_15_min_ago
                        #and ma2_last > ma2_17_min_ago
                        
                        and ma2_last > ma7_last
                        and ma2_last > ma2_2_min_ago
                        and ma4_last > ma4_2_min_ago
                        #and ma7_last >= ma15_last
                        #and ma10_last >= ma10_2_min_ago
                        #and ma11_last > ma15_last
                        
                        
                        and price > price_1_min_ago
                        and price > price_2_min_ago
                        #and price > price_3_min_ago
                 
                    ):

                        action = "buy"

                        
                        
                    elif (
                    
                          ma50_last < ma50_2_min_ago
                          and ma36_last < ma36_2_min_ago
                          and ma9_last >= ma15_last
                          and deviation_ma >= 0.15
                        
                          #and ma85_last < ma100_last
                          #and ma50_last < ma50_5_min_ago
                          #and ma8_last < ma8_5_min_ago
                     
                        
                          
                          #and ma2_last > ma2_15_min_ago
                          #and ma2_last > ma2_17_min_ago
                        
                        
                          and ma2_last > ma7_last
                          and ma2_last > ma2_2_min_ago
                          and ma4_last > ma4_2_min_ago
                          #and ma7_last >= ma15_last
                          #and ma10_last >= ma10_2_min_ago
                          #and ma11_last > ma15_last
                        
                          and price > price_1_min_ago
                          and price > price_2_min_ago
                          #and price > price_3_min_ago
                 
                    ):

                        action = "buy"
                        
                        
                        
                        
                   
                    elif (
                    
                          ma50_last < ma50_2_min_ago
                          and ma36_last > ma36_2_min_ago
                          and ma8_last >= ma14_last
                        
                        
                          #and ma85_last < ma100_last
                          #and ma50_last < ma50_5_min_ago
                          #and ma8_last < ma8_5_min_ago
                          
                          
                          #and ma16_last >= ma24_last
                          #and deviation_ma > 0.40
                          # vedi riga 100 !
                          
                          #and ma2_last > ma2_15_min_ago
                          #and ma2_last > ma2_17_min_ago
                          #and ma2_last > ma2_22_min_ago
                          #and ma2_last > ma2_24_min_ago ( ultima speranza ) 
                          
                          
                          and ma2_last > ma2_2_min_ago
                          and ma2_last > ma7_last
                          and ma4_last > ma4_2_min_ago
                          #and ma7_last >= ma15_last
                          #and ma10_last >= ma10_2_min_ago
                          #and ma11_last >= ma15_last
                        
                          #and ma18_last > ma22_last 
                          # per non comprare durante il ribasso ( prezzo e ma2 gia' sono andati giu' ! )
                        
                          and price > price_1_min_ago
                          and price > price_2_min_ago
                          and price > price_3_min_ago
                 
                    ):

                        action = "buy"
                        
                        
                        
                        
                        
                    elif (
                    
                          ma50_last > ma50_2_min_ago
                          and ma36_last < ma36_2_min_ago
                          and ma9_last >= ma14_last
                        
                        
                          #and ma85_last < ma100_last
                          #and ma50_last < ma50_5_min_ago
                          #and ma8_last < ma8_5_min_ago
                          
                          
                          #and ma16_last >= ma24_last
                          #and deviation_ma > 0.40
                          # vedi riga 100 !
                          
                          #and ma2_last > ma2_15_min_ago
                          #and ma2_last > ma2_17_min_ago
                          #and ma2_last > ma2_22_min_ago
                          #and ma2_last > ma2_24_min_ago ( ultima speranza ) 
                          
                          
                          and ma2_last > ma2_2_min_ago
                          and ma2_last > ma7_last
                          and ma4_last > ma4_2_min_ago
                          #and ma7_last >= ma15_last
                          #and ma10_last >= ma10_2_min_ago
                          #and ma11_last >= ma15_last
                        
                          #and ma18_last > ma22_last 
                          # per non comprare durante il ribasso ( prezzo e ma2 gia' sono andati giu' ! )
                        
                          and price > price_1_min_ago
                          and price > price_2_min_ago
                          and price > price_3_min_ago
                 
                    ):

                        action = "buy"
                
                   
                    
                    
        #####################################################################

        # VENDITA
        # NON TOCCARE QUESTA CONDIZIONE (QUESTA DICE CHE STA IN MODO SELL, DEVO VENDERE)
        elif last_trade_action == "buy":

            self.algo_helper.log("ma2_prev: {}".format(ma2_prev))
            self.algo_helper.log("ma7_prev: {}".format(ma7_prev))
            self.algo_helper.log("ma2_last: {}".format(ma2_last))
            self.algo_helper.log("ma7_last: {}".format(ma7_last))
            self.algo_helper.log("deviation: {}".format(deviation))
            self.algo_helper.log("session: {}".format(self.session))

            ##################################################################################

            # VENDITA 1 - con fasce di tempo !

            #    minuti
            #   0 -  3 -----------
            #   3 -  5 -----------
            #   5 - 12 -----------
            #  12 - 20 ----------- + cuscino
            #  20 - 30 -----------
            #   > 30   -----------

            ##################################################################################

            # VENDITA 1 - da 0 a 3 minuti = da 0 a 180 secondi

            if seconds_since_last_trade > 0 and seconds_since_last_trade <= 180:
                
                
                if (
                    ma50_last > ma50_2_min_ago
                    and ma36_last > ma36_2_min_ago
                    and ma2_last < ma13_last
                    and deviation > 0.08
                ):
                   
                    action = "sell"
                    
                   
                
              
                if (
                    ma50_last > ma50_2_min_ago
                    and ma36_last > ma36_2_min_ago
                    and ma2_last < ma13_last
                    and deviation < -0.70
                ):
                   
                    action = "sell"
                    
                    
                    
                    
                    
                    
                    
                if (
                    ma50_last > ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma13_last
                    and deviation > 0.01
                ):
                   
                    action = "sell"

                    
                    
                elif (
                    ma50_last > ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma11_last
                    and deviation < -0.60
                ):
                    action = "sell"
                    
                    
                    
                    
                    
                    
                    
                if (
                    ma50_last < ma50_2_min_ago
                    and ma36_last > ma36_2_min_ago
                    and ma2_last < ma13_last
                    and deviation > 0.01
                ):
                   
                    action = "sell"

                    
                    
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma36_last > ma36_2_min_ago
                    and ma2_last < ma11_last
                    and deviation < -0.50
                ):
                    action = "sell"       
                    
                    
              
                    
                
                    
                    
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma11_last
                    and deviation > 0.01
                ):
                    action = "sell"

                
                

                elif (
                    ma50_last < ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma7_last
                    and deviation < -0.40
                ):
                    action = "sell"
                    
                    
                    
                    
                    

            # VENDITA 1 - da 3 a 5 minuti = da 180 a 300 secondi

            elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 300:

                
                if (
                    ma50_last > ma50_2_min_ago
                    and ma36_last > ma36_2_min_ago
                    and ma2_last < ma13_last
                    and deviation > 0.08
                ):
                    action = "sell"

                    
                elif (
                    ma50_last >= ma50_2_min_ago
                    and ma36_last >= ma36_2_min_ago
                    and ma2_last < ma13_last
                    and deviation < -0.70
                ):
                    action = "sell"
                    
                    
                    
                    
                    
                    
                if (
                    ma50_last > ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma13_last
                    and deviation > 0.01
                ):
                    action = "sell"

                    
                    
                elif (
                    ma50_last > ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma13_last
                    and deviation < -0.60
                ):
                    action = "sell"
                    
                    
                    
                    
                    
                    
                    
                if (
                    ma50_last < ma50_2_min_ago
                    and ma36_last > ma36_2_min_ago
                    and ma2_last < ma13_last
                    and deviation > 0.01
                ):
                    action = "sell"

                    
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma36_last > ma36_2_min_ago
                    and ma2_last < ma13_last
                    and deviation < -0.50
                ):
                    action = "sell"     
                    
                    
                    
                    
                    
                    
                    
                    
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma11_last
                    and deviation > 0.01
                ):
                    action = "sell"

                
                    
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma7_last
                    and deviation < -0.40
                ):
                    action = "sell"

                    
                  
                
                
                    
                    
            # VENDITA 1 - da 5 a 12 minuti = da 300 a 720 secondi

            elif seconds_since_last_trade > 300 and seconds_since_last_trade <= 720:
                
                
                

                if (
                    ma50_last >= ma50_2_min_ago
                    and ma36_last >= ma36_2_min_ago
                    and ma2_last < ma11_last
                    and deviation > 0.12
                ):
                    action = "sell"
                    
                    
                    #cuscino#
                elif (
                    ma50_last >= ma50_2_min_ago
                    and ma36_last >= ma36_2_min_ago
                    and ma3_last < ma20_last
                    
                ):
                    action = "sell"
                    
                    
                    
                    
                    
                    
                elif (
                    ma50_last >= ma50_2_min_ago
                    and ma36_last >= ma36_2_min_ago
                    and ma2_last < ma11_last
                    and deviation < -0.70
                ):
                    action = "sell"
                    
                    
                    
                    
                    
                    
                elif (
                    ma50_last > ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma11_last
                    and deviation > 0.01
                ):
                    action = "sell"
                    
                

                elif (
                    ma50_last > ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma7_last
                    and deviation < -0.60
                ):
                    action = "sell"
                    
                    
                    
                    
                    
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma36_last > ma36_2_min_ago
                    and ma2_last < ma11_last
                    and deviation > 0.01
                ):
                    action = "sell"
                    
                    
                    
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma36_last > ma36_2_min_ago
                    and ma2_last < ma7_last
                    and deviation < -0.50
                ):
                    action = "sell"
                    
                    
                    
                    
                    
                    
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma7_last
                    and deviation > 0.01
                ):
                    action = "sell"
                    
                    
                    
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma7_last
                    and deviation < -0.40
                ):
                    action = "sell"
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    

            # VENDITA 1 - da 12 a 20 minuti = da 720 a 1200 secondi

            elif seconds_since_last_trade > 720 and seconds_since_last_trade <= 1200:

                if (
                    ma50_last >= ma50_2_min_ago
                    and ma36_last >= ma36_2_min_ago
                    and ma2_last < ma13_last
                    and deviation > 0.15
                ):
                    action = "sell"
                    
                    
                    # cuscino della madonna #
                elif (
                    ma50_last >= ma50_2_min_ago
                    and ma36_last >= ma36_2_min_ago
                    and ma3_last < ma28_last
                    
                ):
                    action = "sell"
                    
                  
                    
                elif (
                    ma50_last >= ma50_2_min_ago
                    and ma36_last >= ma36_2_min_ago
                    and ma2_last < ma11_last
                    and deviation < -0.70
                ):
                    action = "sell"
                    
                    
                    
                
                   
                   
                    
                    
                    
                    
                    
                    
                elif (
                    ma50_last >= ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma13_last
                    and deviation > 0.09
                ):
                    action = "sell"
                    
                    
                elif (
                    ma50_last >= ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma13_last
                    and deviation < -0.50
                ):
                    action = "sell"   
                    
                  
                
                
                
                    
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma36_last > ma36_2_min_ago
                    and ma2_last < ma11_last
                    and deviation > 0.01
                ):
                    action = "sell"
                    
                    
                    
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma36_last > ma36_2_min_ago
                    and ma2_last < ma11_last
                    and deviation < -0.50
                ):
                    action = "sell"   
                    
                    
                    
                    
                    

                elif (
                    ma50_last < ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma11_last
                    and deviation > 0.01
                ):
                    action = "sell"
                    
                    
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma11_last
                    and deviation < -0.40
                ):
                    action = "sell"    
                    
                    
                    
                    
                    
                    
                    

            # VENDITA 1 - da 20 a 30 minuti = da 1200 a 1800 secondi

            elif seconds_since_last_trade > 1200 and seconds_since_last_trade <= 1800:
                
                

                if (
                    ma50_last > ma50_2_min_ago
                    and ma36_last > ma36_2_min_ago
                    and ma2_last < ma13_last
                    and deviation > 0.12
                ):
                    action = "sell"
                    
                    
                    # cuscino della madonna #
                elif (
                    ma50_last > ma50_2_min_ago
                    and ma36_last > ma36_2_min_ago
                    and ma3_last < ma25_last
                    
                ):
                    action = "sell"
                    
                    
                elif (
                    ma50_last > ma50_2_min_ago
                    and ma36_last > ma36_2_min_ago
                    and ma2_last < ma16_last
                    and deviation < -0.70
                ):
                    action = "sell"
                    
                    
                    
                    
                    
                    
                elif (
                    ma50_last > ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma10_last
                    and deviation > 0.07
                ):
                    action = "sell"
                    
       

                elif (
                    ma50_last > ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma10_last
                    and deviation < -0.50
                ):
                    action = "sell"
                
                
                
                
                
                
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma36_last > ma36_2_min_ago
                    and ma2_last < ma10_last
                    and deviation > 0.01
                ):
                    action = "sell"
                    
       

                elif (
                    ma50_last < ma50_2_min_ago
                    and ma36_last > ma36_2_min_ago
                    and ma2_last < ma10_last
                    and deviation < -0.50
                ):
                    action = "sell"
                
                
                
                
                
                
                
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma10_last
                    and deviation > 0.01
                ):
                    action = "sell"
                    
       

                elif (
                    ma50_last < ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma10_last
                    and deviation < -0.40
                ):
                    action = "sell"
                
                
                
                
                
                
                
                
                
                
                
                
                    
                    
                    

            # VENDITA 1 - da 30 minuti in poi = da 1800 secondi in poi

            elif seconds_since_last_trade > 1800:
                
                
                
                if (
                    ma50_last > ma50_2_min_ago
                    and ma36_last > ma36_2_min_ago
                    and ma2_last < ma13_last
                    and deviation > 0.15
                ):
                    action = "sell"
                    
                    
                # cuscino della madonna #    
                elif (
                    ma50_last > ma50_2_min_ago
                    and ma36_last > ma36_2_min_ago
                    and ma2_last < ma16_last
                    
                ):
                    action = "sell"
                    
                    
                    
                    
                    
                elif (
                    ma50_last > ma50_2_min_ago
                    and ma36_last > ma36_2_min_ago
                    and ma2_last < ma16_last
                    and deviation < -0.70
                ):
                    action = "sell"
                    
                    
                    
                    
                    
                elif (
                    ma50_last > ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma11_last
                    and deviation > 0.07
                ):
                    action = "sell"
                    
                 

                elif (
                    ma50_last > ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma11_last
                    and deviation < -0.50
                ):
                    action = "sell"
                    
                    
                    
                    
                    
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma36_last > ma36_2_min_ago
                    and ma2_last < ma13_last
                    and deviation > 0.01
                ):
                    action = "sell"
                    
                    
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma36_last > ma36_2_min_ago
                    and ma2_last < ma11_last
                    and deviation < -0.50
                ):
                    action = "sell"
                    
                    
                    
                    
                    
                    
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma11_last
                    and deviation > 0.01
                ):
                    action = "sell"
                    
                    
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma36_last < ma36_2_min_ago
                    and ma2_last < ma11_last
                    and deviation < -0.40
                ):
                    action = "sell"
                    
                    
                    
                    
                    
                    

            #########################################################################################

            # 1) (STOP LOSS) (salvagente)  
            # se ma100_last >= ma100_13_min_ago vende in un modo 
            # se ma100_last < ma100_13_min_ago vende in un altro modo
            
            if (
                ma50_last >= ma50_2_min_ago
                and ma4_last < ma50_last 
                and deviation < -0.80
            ):
                action = "sell"
            
            
            elif (
                ma50_last < ma50_2_min_ago
                and ma2_last < ma20_last 
                and deviation < -0.80
            ):    
                action = "sell"
            
            
            
            # 2) ro cano VENDE SE DIMINUISCE LA FORZA ! ( vende se perdita  < -0.50 e se etc.)
            if (
                seconds_since_last_trade > max_hold_without_force_time_in_seconds
                and deviation < -0.90
                and ma2_last < ma18_last
                and ma7_last < ma11_last
                and ma11_last < ma15_last
            ):
                action = "sell"

            # 3) ro cano VENDE " DOPO 100 MINUTI " "max hold time" ( vende dopo 100 MINUTI "e se" ma7_last < ma7_2_min_ago "e se" ma2 < ma11 )
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and ma2_last < ma20_last
            ):
                action = "sell"

        ############### FINE ALGORITH #################

        self.algo_helper.log("action {}".format(action))

        if action == "sell":
            self.session += 1

        return action

        # ave comparo meo ! ########## #

