class maddog:
    def __init__(self, helper):
        self.algo_helper = helper
        self.session = 0
        self.open = False

    @property
    def action(self):

        # ro cano ritorna automaticamente ( per esempio 90 minuti x 60 = 5400 secondi )...............................(ADESSO 60 MINUTI) RIGA 319
        max_hold_time_in_seconds = 3600
        
        # e durata segmento in cui si aggiunge una condizione per il BUY ( per esempio 40 minuti x 60 = 2400 secondi )
        min_buy_delay_in_seconds = 2400

        # MACD di 1-2-3-4 minuti prima
        # macd = self.algo_helper.macd

        # macd_2_min_ago = self.algo_helper.macd_minutes_ago(2)

        # moving average (2-3-4-5-x)
        ma2_last, ma2_prev = self.algo_helper.ma_last_prev(2)
        ma3_last, ma3_prev = self.algo_helper.ma_last_prev(3)
        ma4_last, ma4_prev = self.algo_helper.ma_last_prev(4)
        ma5_last, ma5_prev = self.algo_helper.ma_last_prev(5)
        ma7_last, ma7_prev = self.algo_helper.ma_last_prev(7)
        ma8_last, ma8_prev = self.algo_helper.ma_last_prev(8)
        ma9_last, ma9_prev = self.algo_helper.ma_last_prev(9)
        ma11_last, ma11_prev = self.algo_helper.ma_last_prev(11)
        ma12_last, ma12_prev = self.algo_helper.ma_last_prev(12)
        ma13_last, ma13_prev = self.algo_helper.ma_last_prev(13)
        ma14_last, ma14_prev = self.algo_helper.ma_last_prev(14)
        ma15_last, ma15_prev = self.algo_helper.ma_last_prev(15)
        ma16_last, ma16_prev = self.algo_helper.ma_last_prev(16)
        ma18_last, ma18_prev = self.algo_helper.ma_last_prev(18)
        ma20_last, ma20_prev = self.algo_helper.ma_last_prev(20)
        ma21_last, ma21_prev = self.algo_helper.ma_last_prev(21)
        ma24_last, ma24_prev = self.algo_helper.ma_last_prev(24)
        ma28_last, ma28_prev = self.algo_helper.ma_last_prev(28)
        ma34_last, ma34_prev = self.algo_helper.ma_last_prev(34)
        ma36_last, ma36_prev = self.algo_helper.ma_last_prev(36)
        ma38_last, ma38_prev = self.algo_helper.ma_last_prev(38)
        ma39_last, ma39_prev = self.algo_helper.ma_last_prev(39)
        ma40_last, ma40_prev = self.algo_helper.ma_last_prev(40)
        ma43_last, ma43_prev = self.algo_helper.ma_last_prev(43)
        ma48_last, ma48_prev = self.algo_helper.ma_last_prev(48)
        ma50_last, ma50_prev = self.algo_helper.ma_last_prev(50)
       
        ma20_last, ma20_prev = self.algo_helper.ma_last_prev(20)
        ma60_last, ma60_prev = self.algo_helper.ma_last_prev(60)
        ma78_last, ma78_prev = self.algo_helper.ma_last_prev(78)
        ma85_last, ma85_prev = self.algo_helper.ma_last_prev(85)
        ma100_last, ma100_prev = self.algo_helper.ma_last_prev(100)
        #
        

        # moving average (2-3-4-5-7-8-20-43-100) di x minuti prima (NON METTERE MAI 1 min !)
        ma2_2_min_ago = self.algo_helper.ma_minutes_ago(2, 2)
        ma3_2_min_ago = self.algo_helper.ma_minutes_ago(3, 2)
        ma4_2_min_ago = self.algo_helper.ma_minutes_ago(4, 2)
        ma5_2_min_ago = self.algo_helper.ma_minutes_ago(5, 2)
        ma5_3_min_ago = self.algo_helper.ma_minutes_ago(5, 3)
        ma7_2_min_ago = self.algo_helper.ma_minutes_ago(7, 2)
        ma11_2_min_ago = self.algo_helper.ma_minutes_ago(11, 2)
        ma12_2_min_ago = self.algo_helper.ma_minutes_ago(12, 2)
        ma15_5_min_ago = self.algo_helper.ma_minutes_ago(15, 5)
        ma16_2_min_ago = self.algo_helper.ma_minutes_ago(16, 2)
        ma20_2_min_ago = self.algo_helper.ma_minutes_ago(20, 2)
        ma36_2_min_ago = self.algo_helper.ma_minutes_ago(36, 2)
        ma39_2_min_ago = self.algo_helper.ma_minutes_ago(39, 2)
        ma60_2_min_ago = self.algo_helper.ma_minutes_ago(60, 2)
        ma78_2_min_ago = self.algo_helper.ma_minutes_ago(78, 2)
        ma85_3_min_ago = self.algo_helper.ma_minutes_ago(85, 3)
        
        
        
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
        price_4_min_ago = self.algo_helper.price_minutes_ago(4)
        
        
    
        #######################################################################################################################################################    
        
        

        # formula "deviation_buy1" (per comprare LA PRIMA VOLTA durante il TREND RIBASSISTA)
        deviation_buy1 = (ma8_last / ma78_last - 1) * 100 if ma78_last else 0
        self.algo_helper.log("deviation_buy1: {}".format(deviation_buy1))
        
        
        # formula "deviation_buy2" 
        deviation_buy2 = (ma8_last / ma78_last - 1) * 100 if ma78_last else 0
        self.algo_helper.log("deviation_buy2: {}".format(deviation_buy2))
        
        
        # formula "deviation_buy3"
        deviation_buy3 = (ma8_last / ma78_last - 1) * 100 if ma78_last else 0
        self.algo_helper.log("deviation_buy3: {}".format(deviation_buy3))
        
        
        
        # formula deviation per comprare un po' piu' sopra del SELL
        deviation = (ma2_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.log("deviation: {}".format(deviation))
        
        
        # formula deviation per vendere un po' piu' giu' di ma78
        deviation_sell = (ma2_last / ma78_last - 1) * 100 if ma78_last else 0
        self.algo_helper.log("deviation_sell: {}".format(deviation_sell))
        
        # formula deviation per vendere a una certa distanza da ma50
        deviation_ma50 = (ma2_last / ma50_last - 1) * 100 if ma50_last else 0
        self.algo_helper.log("deviation_ma50: {}".format(deviation_ma50))
        
        

        #
        
        action = None

        ##################################################################################################################################################
        # APRE E CHIUDE GABBIA
        # SI APRE LA GABBIA SE
      
        if ma8_last > ma38_last and deviation_buy1 > -0.10 and price > price_2_min_ago and price > price_3_min_ago:
        # deviation_buy1 = ma8_last / ma78_last 
            
            # NON TOCCARE QUESTA CONDIZIONE SERVE PER APERTURA DI GABBIA
            if not self.session or not self.open:
                self.session = 1
                self.open = True
                self.algo_helper.log("session {}: open segment".format(self.session))
                
                
        # SI CHIUDE LA GABBIA SE
        else:
            self.open = False
            self.algo_helper.log("session {}: closed segment".format(self.session))

        
        
        ###########################################
        
        # COMPRA
        # NON TOCCARE QUESTA CONDIZIONE (QUESTA DICE CHE STA IN MODO BUY, DEVO COMPRARE)
        if self.open and self.session and last_trade_action != "buy":
            
            

            # COMPRA UN PO' PIU' SOPRA DELL' ULTIMO SELL ( aggiungere compra un po' piu' sopra dell' ultimo BUY deviation > 0.20 )
            if (
                seconds_since_last_trade > 0
                and seconds_since_last_trade <= min_buy_delay_in_seconds
                and deviation > 0.15
            ) or (
                seconds_since_last_trade == 0
                or seconds_since_last_trade > min_buy_delay_in_seconds
            ):
                
                
        #######################################################################

                # COMPRA sessione 1
                if self.session == 1:
                    if (
                       
                        #se va su all' improvviso prende la deviation.
                        #se ci ripensa prima di salire prende l' incrocio
                        #GRAZIE COMPA
                      
                        ma13_prev < ma78_prev and ma13_last > ma78_last or deviation_buy1 > 0.17
                        #deviation_buy1 = ma8_last / ma78_last
                       
                        and price > price_2_min_ago
                        and price > price_3_min_ago
                        and price > price_4_min_ago
                       
                    ):
                        action = "buy"
                        
                        

                # COMPRA sessione 2
                elif self.session == 2:
                    if (
                        
                        price > price_2_min_ago
                        and ma2_last > ma2_2_min_ago
                        
                        and ma3_last > ma40_last
                        #incredibile ma vero E' NECESSARIA quando deve ricomprare dopo la correzione al ribasso
                        
                        and deviation > 0.18
                        #deviation = ma2_last / last_trade_price
                        
                        and deviation_buy2 > 0.15
                        #deviation_buy2 = ma8_last / ma78_last
                   
                    ):
                        action = "buy"

                        
                        
                        
                # COMPRA sessione 3 in poi
                else:
                    if (
                        
                        ma2_last >= ma4_last
                        and price > price_2_min_ago
                        
                        #deve essere anche questo
                        and ma2_last > ma50_last
                        and ma2_last > ma78_last
                        
                        and ma3_last > ma40_last
                        #incredibile ma vero E' NECESSARIA quando deve ricomprare dopo la correzione al ribasso
                        
                        and deviation > 0.085
                        
                        
                        and deviation_buy3 > 0.105
                        #deviation_buy3 = ma8_last / ma78_last
                        
                    ):
                        action = "buy"

        ##############################################################################################################
        
        
        # VENDA
        # NON TOCCARE QUESTA CONDIZIONE (QUESTA DICE CHE STA IN MODO SELL, DEVO VENDERE)
        elif last_trade_action == "buy":

            self.algo_helper.log("ma2_prev: {}".format(ma2_prev))
            self.algo_helper.log("ma7_prev: {}".format(ma7_prev))
            self.algo_helper.log("ma2_last: {}".format(ma2_last))
            self.algo_helper.log("ma7_last: {}".format(ma7_last))
            self.algo_helper.log("deviation: {}".format(deviation))
            self.algo_helper.log("session: {}".format(self.session))

       ###############################################################################################################################################     
            
            # VENDE
           
            # VENDE sessione 1
            if self.session == 1:
                
                if (
                    
                    ma2_last < ma15_last and deviation > 0.13
                    
                ):
                   
                    action = "sell"     
                    

                    
                    
                elif (
                   
                    deviation_sell < -0.19 or (ma3_last < ma39_last and deviation_buy1 < -0.20) or (ma2_last < ma50_last and deviation_ma50 < -0.20)
                    #deviation_sell = ma2_last / ma78_last
                    #deviation_buy1 = ma8_last / ma78_last
                ):
                    action = "sell"    
                  
                
                
            # VENDE sessione 2
            elif self.session == 2:
               
                if (
                    
                    ma2_last < ma15_last and deviation > 0.13
                    
                    
                ):
                   
                    action = "sell"     
                    

                    
                    
                elif (
                    
                    ma2_last < ma39_last and deviation_sell < -0.12 or (ma3_last < ma39_last and deviation_buy1 < -0.20) or (ma2_last < ma50_last and deviation_ma50 < -0.20)
                    #deviation_sell = ma2_last / ma78_last
                    #deviation_buy1 = (ma8_last / ma78_last
                    
                    
                ):
                    action = "sell"      
                       
                 

            # VENDE sessione 3 in poi
            else:
                
                if (
                    
                    ma2_last < ma15_last and deviation > 0.01
                    
                    
                ):
                   
                    action = "sell"     
                    

                    
                    
                elif (
                    
                    ma2_last < ma39_last and deviation_sell < -0.10 or (ma2_last < ma39_last and deviation_buy1 < -0.20) or (ma2_last < ma50_last and deviation_ma50 < -0.20)
                    #deviation_sell = ma2_last / ma78_last
                    #deviation_buy1 = ma8_last / ma78_last
                    
                ):
                    action = "sell"        
                        
                        
                        
            ###################################################################################################################################################################
            
                       
            # STOP LOSS (salvagente)
            
            if ma2_last < ma39_last and deviation < -0.69:
                action = "sell"
            
            # 1) vedi riga 11 per es. DI 1 ORA = 3600 SECONDI "max hold time" " DOPO UN' ORA VENDE SUBITO " e se ma8_last < ma39_last and deviation < -0.40:
            
            if seconds_since_last_trade > max_hold_time_in_seconds and ma8_last < ma39_last and deviation < -0.69:
                
                    
                action = "sell"

        self.algo_helper.log("action {}".format(action))

        if action == "sell":
            self.session += 1

        return action


        # grazie compa ### 
        #
        #plinium###
