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
        ma43_last, ma43_prev = self.algo_helper.ma_last_prev(43)
        ma48_last, ma48_prev = self.algo_helper.ma_last_prev(48)
        ma50_last, ma50_prev = self.algo_helper.ma_last_prev(50)
        #
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
    
    
        #######################################################################################################################################################    
        ###################################################################################################################################################### 
        

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
        
        
        

        #####################################################################################################################################################
        
        
        
        
        action = None

        ##################################################################################################################################################
        # APRE E CHIUDE GABBIA
        # SI APRE LA GABBIA SE
        #if ma2_last > ma38_last:
      
        #ma fai cosi' (che la gabbia resterà aperta come se fosse ma78 > ma78 2 min ago !)
        if ma2_last > ma38_last and deviation_buy1 > -0.40:
            
        #if ma2_last > ma38_last and deviation_buy1 > -0.36: vedi questo valore alle ore 9:43
        # TI RICORDO CHE LA deviation_buy1 prende (ma8_last / ma78_last - 1) * 100
            
            
            
            # NON TOCCARE QUESTA CONDIZIONE SERVE PER APERTURA DI GABBIA
            if not self.session or not self.open:
                self.session = 1
                self.open = True
                self.algo_helper.log("session {}: open segment".format(self.session))
                
                
        # SI CHIUDE LA GABBIA SE
        else:
            self.open = False
            self.algo_helper.log("session {}: closed segment".format(self.session))

        #############################################################################################################################################################
        
        
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
                        
                        
                        
                        #potrai provare- DICO PROVARE- anche un incrocio anticlassico  ma4<ma38 and ma4>ma50
                        
                        
                        #deviation_buy1 > -0.13
                        
                        ma13_prev < ma38_prev and ma13_last > ma38_last
                        #STO PROVANDO L' INCROCIO
                        #ma13_prev < ma38_prev and ma13_last > ma38_last or deviation_buy1 > -0.125 
                        and price > price_2_min_ago
                        and price > price_3_min_ago
                        
                        
                        #deviation_buy1 > -0.145 or (ma24_prev < ma78_prev and ma24_last > ma78_last) 
                        #SARA' COSI' ! con incrocio classico ! MA DEVI PROVARE ANCORA L' INCROCIO CON deviation buy1 che compra molto piu' alto
                        #vedi cano che ritorna
                        
                        
                        #forse dovrai aggiungere eventualmente and (ma3_last > ma39_last and ma12_last > ma12_2_min_ago)
                        
                        
                        
                        
                        #and (ma2_prev < ma3_prev and ma2_last > ma3_last and ma12_last > ma12_2_min_ago)
                        #ma2_last >= ma4_last
                        #and ma2_last >= ma8_last
                        
                        #ma18_last >= ma21_last
                        
                        #and ma2_prev < ma4_prev and ma2_last > ma4_last
                        # attenzione ! vedi che se ci sono grandi rialzi improvvisi la ma2 incrocia MOLTO DIFFICILMENTE la ma4
                        
                        #and ma2_last > ma2_2_min_ago
                        #and ma4_last > ma4_2_min_ago
                        #and ma5_last > ma5_2_min_ago
                        #and ma7_last > ma7_2_min_ago
                       
                     
                    ):
                        action = "buy"
                        
                        

                # COMPRA sessione 2
                elif self.session == 2:
                    if (
                        #ma8_last >= ma14_last
                        #ma2_last >= ma8_last
                        
                        #ma2_last > ma2_2_min_ago
                        #and ma4_last > ma4_2_min_ago
                        #and ma5_last > ma5_2_min_ago
                        
                        
                        #piu' veloce !
                        #and (ma2_prev < ma4_prev and ma2_last > ma4_last)
                        
                        
                        price > price_2_min_ago
                        and ma2_last > ma2_2_min_ago
                        
                        and deviation > 0.18
                        
                        and deviation_buy2 > 0.15
                        #and deviation_buy2 > 0.12 or (ma5_prev < ma36_prev and ma5_last > ma36_last and ma3_last > ma39_last and ma12_last > ma12_2_min_ago)
                        #SARA' COSI' !
                        
                        
                        
                        
                        #and price > price_3_min_ago
                        
                        #and deviation_buy1 > 0.15 and (ma3_prev < ma5_prev and ma3_last > ma5_last
                        #deviation > 0.10 dopo che ha venduto ha comprato nello stesso minuto (puntino verde proprio sopra puntino rosso) con il price che scendeva
                        #allora tolgo la deviation e lascio solo price 1 min ago e price 2 min ago per vedere se funziona ! - FUNZIONA ! vai compaaaaaaaaaaaa
                        
                     
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
                        
                        
                        and deviation > 0.09
                        
                        and deviation_buy3 > 0.11
                        #and deviation_buy3 > 0.12 or (ma5_prev < ma36_prev and ma5_last > ma36_last and ma3_last > ma39_last and ma12_last > ma12_2_min_ago)
                        #SARA' COSI' !
                        
                        

                        #and ma2_last > ma2_2_min_ago
                        #and ma4_last > ma4_2_min_ago
                        #and ma5_last > ma5_2_min_ago
                        #ma8_last >= ma14_last
                        
                        
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
                    
                    ma2_last < ma16_last 
                    and deviation > 0.25
                    #ma78_last > ma78_2_min_ago
                ):
                   
                    action = "sell"     
                    

                    
                    
                elif (
                    
                    #ma78_last < ma78_2_min_ago
                    #and deviation < -0.21 NON FUNZIONA ! rimetto < - 0.65 ! Per adesso soltanto al al buy 1
                    #and deviation < -0.65
                    #RIMETTO DEVIATION <-0.22 MA CON MEDIA PIU' ALTA
                    
                    ma2_last < ma39_last 
                    and deviation < -0.59
                    # ti ricordo che deviation = (ma2_last / last_trade_price - 1) * 100
                    
                    
                ):
                    action = "sell"    
                    
                    
                
                    # cano maddog fa difficilmente un passo falso ! per questo siamo piu' tolleranti sulla perdita dopo il primo acquisto
                    # ciao comba che non mi parli piu'.
                    # ma basta che stai bene tu.
                    
                        
                        
                        
                        

            # VENDE sessione 2
            elif self.session == 2:
               
                if (
                    
                    ma2_last < ma15_last 
                    and deviation > 0.25
                    #ma78_last > ma78_2_min_ago
                ):
                   
                    action = "sell"     
                    

                    
                    
                elif (
                    
                    ma2_last < ma38_last 
                    #ma2_last < ma20_last 
                    #and deviation < -0.59
                    #ma78_last < ma78_2_min_ago
                ):
                    action = "sell"      
                       
                        
                        
                        
                        

            # VENDE sessione 3 in poi
            else:
                
                if (
                    
                    ma2_last < ma15_last 
                    and deviation > 0.01
                    #ma78_last > ma78_2_min_ago
                ):
                   
                    action = "sell"     
                    

                    
                    
                elif (
                    
                    ma3_last < ma36_last 
                    and deviation < -0.17
                    #ma78_last < ma78_2_min_ago
                ):
                    action = "sell"        
                        #action = "sell"
                        
                        
                        
                  
                        

            # STOP LOSS (salvagente)
            if deviation < -0.61 and ma2_last < ma39_last:
                action = "sell"

            
           
            
            

            
            # 1) vedi riga 11 per es. DI 1 ORA = 3600 SECONDI "max hold time" " DOPO UN' ORA VENDE SUBITO " e se ma8_last < ma39_last and deviation < -0.40:
            
            if seconds_since_last_trade > max_hold_time_in_seconds and ma8_last < ma39_last and deviation < -0.62:
                
                    
                action = "sell"

        self.algo_helper.log("action {}".format(action))

        if action == "sell":
            self.session += 1

        return action


        # grazie compa #### # ###
        ####
