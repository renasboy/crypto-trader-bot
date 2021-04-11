

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
        ma6_last, ma6_prev = self.algo_helper.ma_last_prev(6)
        ma7_last, ma7_prev = self.algo_helper.ma_last_prev(7)
        ma8_last, ma8_prev = self.algo_helper.ma_last_prev(8)
        ma13_last, ma13_prev = self.algo_helper.ma_last_prev(13)
        ma15_last, ma15_prev = self.algo_helper.ma_last_prev(15)
        ma17_last, ma17_prev = self.algo_helper.ma_last_prev(17)
        ma20_last, ma20_prev = self.algo_helper.ma_last_prev(20)
        ma36_last, ma36_prev = self.algo_helper.ma_last_prev(36)
        ma38_last, ma38_prev = self.algo_helper.ma_last_prev(38)
        ma39_last, ma39_prev = self.algo_helper.ma_last_prev(39)
        ma40_last, ma40_prev = self.algo_helper.ma_last_prev(40)
        ma50_last, ma50_prev = self.algo_helper.ma_last_prev(50)
        ma60_last, ma60_prev = self.algo_helper.ma_last_prev(60)
        ma78_last, ma78_prev = self.algo_helper.ma_last_prev(78)
        ma82_last, ma82_prev = self.algo_helper.ma_last_prev(82)
        
 
        # moving average (2-3-4-5-7-8-20-43-100) di x minuti prima
        
        ma2_2_min_ago = self.algo_helper.ma_minutes_ago(2, 2)
        ma2_3_min_ago = self.algo_helper.ma_minutes_ago(2, 3)
        ma3_2_min_ago = self.algo_helper.ma_minutes_ago(3, 2)
        ma6_2_min_ago = self.algo_helper.ma_minutes_ago(6, 2)
        ma39_2_min_ago = self.algo_helper.ma_minutes_ago(39, 2)
        ma50_2_min_ago = self.algo_helper.ma_minutes_ago(50, 2)
        
        # LAST TRADE
        last_trade_action = self.algo_helper.last_trade_action
        last_trade_price = self.algo_helper.last_trade_price
        seconds_since_last_trade = self.algo_helper.seconds_since_last_trade
       

        # PREV TRADE
        prev_trade_action = self.algo_helper.prev_trade_action
        prev_trade_time = self.algo_helper.prev_trade_time
        prev_trade_price = self.algo_helper.prev_trade_price
        seconds_since_prev_trade = self.algo_helper.seconds_since_prev_trade
        
       
        #########################################################################################################################################################
        
        # PREZZO DI ADESSO (di mercato) - CURRENT PRICE
        price = self.algo_helper.price
       
        ##########################################################################################################################################################
        
        
        # PREZZO di X MINUTI FA (di mercato) - PREV PRICE
        price_1_min_ago = self.algo_helper.price_minutes_ago(1)
        price_2_min_ago = self.algo_helper.price_minutes_ago(2)
        price_3_min_ago = self.algo_helper.price_minutes_ago(3)
        price_5_min_ago = self.algo_helper.price_minutes_ago(5)
        
        
        #############################################################################################################################################################
        
        

        # VENDE DOPO 7200 secondi = 120 minuti ("e se") ro cano torna a casa
        max_hold_time_in_seconds = 7200

        # VENDE DOPO 600 secondi = 10 minuti ("e se") - ro cano perde la forza - riga 323
        max_hold_without_force_time_in_seconds = 600
        
        
        #############################################################################################################################################################
        
        
        # TEMPO in cui (PER COMPRARE) (a tutte le condizioni gia' attive) SI AGGIUNGE una condizione aggiuntiva LA DEVIATION !

        # dall' ULTIMO trade ( 15 minuti = 15 * 60 = 900 secondi )
        min_buy_delay_in_seconds = 900

        # dal PENULTIMO trade ( 20 minuti = 20 * 60 = 1800 secondi )
        min_prev_buy_delay_in_seconds = 1200

       ##############################################################################################################################################################
    
        # formula DEVIATION_gabbia 
        deviation_gabbia = (ma6_last / ma38_last - 1) * 100 if ma38_last else 0
        self.algo_helper.log("deviation_gabbia: {}".format(deviation_gabbia))
        
        # formula DEVIATION_buy1 per comprare durante il TREND RIBASSISTA 
        deviation_buy1 = (ma8_last / ma78_last - 1) * 100 if ma78_last else 0
        self.algo_helper.log("deviation_buy1: {}".format(deviation_buy1))
        
        
        # formula DEVIATION_buy2 per la compra 2 
        deviation_buy2 = (ma8_last / ma78_last - 1) * 100 if ma78_last else 0
        self.algo_helper.log("deviation_buy2: {}".format(deviation_buy2))
        
        
        # formula DEVIATION_buy3 per la compra 3
        deviation_buy3 = (ma8_last / ma78_last - 1) * 100 if ma78_last else 0
        self.algo_helper.log("deviation_buy3: {}".format(deviation_buy3))
        
        ########################################################################################################################
        
        
        # formula DEVIATION_buy per comprare UN PO' PIU' SOPRA DEL LAST TRADE ( di solito l' ultimo SELL ) 
        deviation_buy = (ma2_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.log("deviation_buy: {}".format(deviation_buy))
        
        # formula DEVIATION_prev per comprare UN PO' PIU' SOPRA DEL PREV TRADE ( di solito l' ultimo BUY )
        deviation_prev = (price / prev_trade_price - 1) * 100 if prev_trade_price else 0
        self.algo_helper.log("deviation_prev: {}".format(deviation_prev))

        # formula DEVIATION_sell per vendere
        deviation_sell = (ma2_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.log("deviation_sell: {}".format(deviation_sell))
        
        
        # formula DEVIATION_ma50 per vendere a una certa distanza da ma50
        deviation_ma50 = (ma2_last / ma50_last - 1) * 100 if ma50_last else 0
        self.algo_helper.log("deviation_ma50: {}".format(deviation_ma50))
        
        
        
        ###################################################################################################################################
        
        

        # DEFAULT ACTION DICE DI NON FARE NIENTE (=None, NON TOCCARE)
        action = None

        
        
        ##########################################################################################################################################

        # APRE E CHIUDE GABBIA

        if ma50_last >= ma50_2_min_ago and deviation_gabbia > -0.15:
            #ti ricordo che deviation_gabbia = (ma6_last / ma38_last)
           
            
            # NON TOCCARE QUESTA CONDIZIONE SERVE PER APERTURA DI GABBIA !
            if not self.session or not self.open:
                self.session = 1
                self.open = True
                self.algo_helper.log("session {}: open segment".format(self.session))

        # SI CHIUDE LA GABBIA SE
        elif self.open:
            self.open = False
            self.algo_helper.log("session {}: closed segment".format(self.session))

        #############################################################################################################################################

        ############################################################################################################################################
        
        # COMPRA
        # NON TOCCARE QUESTA CONDIZIONE (QUESTA DICE CHE STA IN MODO BUY, DEVO COMPRARE)
        if self.open and self.session and last_trade_action != "buy":

        ###################################################################################
            
            
            
            # COMPRA UN PO' PIU' SOPRA DELL' ULTIMO TRADE SE deviation_buy > x nei 540 secondi  ( quasi sempre IL SELL )
            if (
            
                (
                    seconds_since_last_trade > 0
                    and seconds_since_last_trade <= min_buy_delay_in_seconds
                    and deviation_buy > 0.01
                )
                
                # COMPRA UN PO' PIU' SOPRA DEL PENULTIMO TRADE SE deviation_prev > x nei 300 secondi ( qualche volta IL BUY)
                
                or (
                    seconds_since_prev_trade > 0
                    and seconds_since_prev_trade <= min_prev_buy_delay_in_seconds
                    and deviation_prev > 0.01
                )
                
                
                or (
                    seconds_since_last_trade == 0
                    or seconds_since_last_trade > min_buy_delay_in_seconds
                )
              
                
            ):

###################################################################################################################################################


                # COMPRA sessione 1
          
                if self.session == 1:
               
                    if (
                       
                        #se va su all' improvviso prende la deviation.
                        #se ci ripensa prima di salire prende l' incrocio
                        #GRAZIE COMPA
                        
                        price > price_2_min_ago
                        and price > price_3_min_ago
                        and ma2_last > ma2_2_min_ago
                        and ma39_prev < ma78_prev and ma39_last > ma78_last or deviation_buy1 > 0.50
                        
                        #roma 2 aprile 2021 - BUY 1
          
                    
                    ):
                        action = "buy"
                       

              
                    elif (
                         
                          price > price_2_min_ago
                          and price > price_3_min_ago
                          and ma2_last > ma2_2_min_ago
                   
                          and ma50_prev < ma82_prev and ma50_last > ma82_last or deviation_buy1 > 0.50
                        
                          #roma 2 aprile 2021 - BUY 1
                     
                    ):

                        action = "buy"
                    
                    
##############################################################################################################################
                
    
                # COMPRA sessione 2
        
                elif self.session == 2:
              
                    if (
                     
                        ma4_prev < ma8_prev and ma4_last > ma8_last or (deviation_buy2 > 0.16 and deviation_buy > 0.18 and deviation_prev > 0.15)
                        
                        
                        #ma8>ma78
                        #punto verde dall' ultimo punto rosso (ma3-last trade)
                        #punto verde dall' ultimo punto verde
                        
                        
                       
                        and ma2_last > ma2_2_min_ago
                        and price > price_1_min_ago
                        and price > price_2_min_ago
                        
                        
                        and ma3_last > ma40_last
                        #incredibile ma vero E' NECESSARIA quando deve ricomprare dopo la correzione al ribasso
                
                    ):

                        action = "buy"

                        
                        
                    elif (
                          ma4_prev < ma8_prev and ma4_last > ma8_last or (deviation_buy2 > 0.16 and deviation_buy > 0.18 and deviation_prev > 0.15)
                          
                          
                          
                          
                          
                          
                         
                          and ma2_last > ma2_2_min_ago
                          and price > price_1_min_ago
                          and price > price_2_min_ago
                        
                          and ma3_last > ma40_last
                          #incredibile ma vero E' NECESSARIA quando deve ricomprare dopo la correzione al ribasso
                    
                    ):

                        action = "buy"
                    
#############################################################################################################################################



                # COMPRA sessione 3 in poi
    
                elif self.session == 3:
           
                    if (
                        
                        
                        ma2_prev < ma8_prev and ma2_last > ma8_last or (deviation_buy3 > 0.155 and deviation_buy > 0.175 and deviation_prev > 0.145)
                        and ma39_last > ma39_2_min_ago
                        
                        and price > price_2_min_ago
                        and price > price_3_min_ago
                        and ma2_last > ma2_2_min_ago
                        and ma2_last >= ma4_last
                        
                        
                        and ma6_last > ma6_2_min_ago
                        and ma3_last > ma40_last
                        
                        #incredibile ma vero E' NECESSARIA quando deve ricomprare dopo la correzione al ribasso
                        and ma3_last > ma6_last
                        
                        #deve essere anche questo
                        and ma2_last > ma50_last
                        and ma2_last > ma78_last
                        
                        #deviation_buy3 = ma8_last / ma78_last
                        #deviation_buy = ma2_last / last_trade_price
                        #deviation_prev = price / prev_trade_price  
                    
                    ):

                        action = "buy"

                        
                        
                    elif (
                          

                          ma3_prev < ma8_prev and ma3_last > ma8_last or (deviation_buy3 > 0.16 and deviation_buy > 0.18 and deviation_prev > 0.15)
                          and ma39_last < ma39_2_min_ago
                        
                          and price > price_2_min_ago
                          and price > price_3_min_ago
                          and ma2_last > ma2_2_min_ago
                          and ma2_last >= ma4_last
                        
                        
                          and ma6_last > ma6_2_min_ago
                          and ma3_last > ma40_last
                        
                          #incredibile ma vero E' NECESSARIA quando deve ricomprare dopo la correzione al ribasso
                          and ma3_last > ma6_last
                        
                          #deve essere anche questo
                          and ma2_last > ma50_last
                          and ma2_last > ma78_last
                        
                          #deviation_buy3 = ma8_last / ma78_last
                          #deviation_buy = ma2_last / last_trade_price
                          #deviation_prev = price / prev_trade_price
                          
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
            self.algo_helper.log("deviation_sell: {}".format(deviation_sell))
            self.algo_helper.log("session: {}".format(self.session))

            ##################################################################################

            # VENDITA 1 - con fasce di tempo !

            #    minuti
            #   0 -  3 ---------- c'e' vita su marte !
            #   3 -  5 -----------
            #   5 - 12 -----------
            
            #  12 - 18 ----------- 
            #  18 - 30 -----------
            #   > 30   -----------

           
            ###########################################################################################################################          0 -3 min

            # VENDITA - da 0 a 3 minuti = da 0 a 180 secondi

            if seconds_since_last_trade > 0 and seconds_since_last_trade <= 180:
                
                
                if (
                    
                    ma2_last < ma39_last 
                    and deviation_sell > 0.10
                    #deviation_sell = ma2_last / last_trade_price
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                ):
                   
                    action = "sell"
                    
                   
                
              
                elif (
                   
                    ma13_last >= ma39_last
                    
                    and deviation_sell < -0.75 or (ma50_last < ma50_2_min_ago and deviation_gabbia < -0.25) or (ma2_last < ma50_last and deviation_ma50 < -0.15)
                    #deviation_sell = ma2_last / last_trade_price
                  
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                    
                ):
                   
                    action = "sell"
                    
                    
                    
                    
                elif (
                    
                    ma13_last < ma39_last
                    
                    and deviation_sell < -0.60 or (ma50_last < ma50_2_min_ago and deviation_gabbia < -0.25)
                    #deviation_sell = ma2_last / last_trade_price
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                   
                ):
                   
                    action = "sell"
                    
                    
         #########################################################################################################################          3-5 min           

            # VENDITA - da 3 a 5 minuti = da 180 a 300 secondi

            elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 300:

                
                if (
                    
                    ma2_last < ma20_last 
                    and deviation_sell > 0.10
                    #deviation_sell = ma2_last / last_trade_price
                    
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                ):
                    action = "sell"

                    
                elif (
                    
                    ma13_last >= ma39_last
                    
                    and deviation_sell < -0.75 or (ma50_last < ma50_2_min_ago and deviation_gabbia < -0.25)
                    #deviation_sell = ma2_last / last_trade_price
                   
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                ):
                    action = "sell"
                    
                    
                    
                elif (
                    
                    ma13_last < ma39_last 
                    and deviation_sell < -0.60 or (ma50_last < ma50_2_min_ago and deviation_gabbia < -0.25) or (ma2_last < ma50_last and deviation_ma50 < -0.15)
                    
                    #deviation_sell = ma2_last / last_trade_price
                   
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                ):
                    action = "sell"
          
            ########################################################################################################################          5-12 min         
                
            # VENDITA - da 5 a 12 minuti = da 300 a 720 secondi

            elif seconds_since_last_trade > 300 and seconds_since_last_trade <= 720:
                

                if (
                    
                    ma2_last < ma20_last
                    and deviation_sell > 0.10
                    #deviation_sell = ma2_last / last_trade_price
                   
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_3_min_ago
                    
                ):
                    action = "sell"
                    
             
                    
                elif (
                    
                    ma13_last >= ma39_last
                    and deviation_sell < -0.75 or (ma50_last < ma50_2_min_ago and deviation_gabbia < -0.25)
                    #deviation_sell = ma2_last / last_trade_price
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_3_min_ago
                    
                ):
                    action = "sell"
                    
                    
                    
                elif (
                    
                    ma13_last < ma39_last
                    and deviation_sell < -0.60 or (ma50_last < ma50_2_min_ago and deviation_gabbia < -0.25) or (ma2_last < ma50_last and deviation_ma50 < -0.15)
                    #deviation_sell = ma2_last / last_trade_price
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_3_min_ago
                    
                ):
                    action = "sell"
                        
                    
                    
                    
                    
                    
            
            #######################################################################################################          12-18 min        

            # VENDITA - da 12 a 18 minuti = da 720 a 1080 secondi

            elif seconds_since_last_trade > 720 and seconds_since_last_trade <= 1080:

                if (
                    
                    ma3_last < ma17_last 
                    and deviation_sell > 0.12
                    #deviation_sell = ma2_last / last_trade_price
                    
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                ):
                    action = "sell"
                    
                  
                elif (
                    
                    ma13_last >= ma39_last
                    and deviation_sell < -0.75 or (ma50_last < ma50_2_min_ago and deviation_gabbia < -0.20)
                    #deviation_sell = ma2_last / last_trade_price
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                ):
                    action = "sell"
                    
                    
                elif (
                    
                    ma13_last < ma39_last
                    and deviation_sell < -0.60 or (ma50_last < ma50_2_min_ago and deviation_gabbia < -0.25) or (ma2_last < ma50_last and deviation_ma50 < -0.15)
                    #deviation_sell = ma2_last / last_trade_price
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                ):
                    action = "sell"   
                    
          
            ################################################################################################################################          18-30 min
            
            
            # VENDITA - da 18 a 30 minuti = da 1080 a 1800 secondi

            elif seconds_since_last_trade > 1080 and seconds_since_last_trade <= 1800:
            
                if (
                    
                    ma3_last < ma17_last 
                    and deviation_sell > 0.12
                    #deviation_sell = ma2_last / last_trade_price
                    
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                ):
                    action = "sell"
                
                    
                elif (
                    
                    ma13_last >= ma39_last
                    and deviation_sell < -0.75 or (ma50_last < ma50_2_min_ago and deviation_gabbia < -0.25)
                    #deviation_sell = ma2_last / last_trade_price
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                ):
                    action = "sell"
                    
                    
                elif (
                    
                    ma13_last < ma39_last
                    and deviation_sell < -0.60 or (ma50_last < ma50_2_min_ago and deviation_gabbia < -0.25) or (ma2_last < ma50_last and deviation_ma50 < -0.15)
                    #deviation_sell = ma2_last / last_trade_price
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                ):
                    action = "sell"   
                    
                    
              
            ########################################################################################################################          >30 min
            # VENDITA - da 30 minuti in poi = da 1800 secondi in poi

            elif seconds_since_last_trade > 1800:
               
                
                if (
                    
                    ma3_last < ma17_last 
                    and deviation_sell > 0.12
                    #deviation_sell = ma2_last / last_trade_price
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                ):
                  
                    action = "sell"
                    
                
                    
                elif (
                    
                    ma13_last >= ma39_last
                    and deviation_sell < -0.75 or (ma50_last < ma50_2_min_ago and deviation_gabbia < -0.25)
                    #deviation_sell = ma2_last / last_trade_price
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                ):
                    action = "sell"
                    
                    
                elif (
                    
                    ma13_last < ma39_last
                    and deviation_sell < -0.60 or (ma50_last < ma50_2_min_ago and deviation_gabbia < -0.25) or (ma2_last < ma50_last and deviation_ma50 < -0.15)
                    #deviation_sell = ma2_last / last_trade_price
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                ):
                    action = "sell"   
                    
                    
            ################################################################################################################################## 


            # 1) (STOP LOSS) (salvagente)  
            # se ma100_last >= ma100_13_min_ago vende in un modo 
            # se ma100_last < ma100_13_min_ago vende in un altro modo
            
            if (
                ma2_last < ma36_last and deviation_sell < -0.65 or (ma2_last < ma36_last and deviation_sell < -0.70)
                
                
              
            ):
                action = "sell"
            
            
            #elif (
                
                #ma2_last < ma36_last 
                #and deviation_sell < -0.50
            #):    
                #action = "sell"
            
            
            
           

            #2) ro cano VENDE " DOPO 120 MINUTI " "max hold time" riga 128
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and ma2_last < ma78_last and deviation_sell < -0.10
                #deviation_sell = ma2_last / last_trade_price
            ):
                action = "sell"

        ############### FINE ALGORITH #################
        
        

        self.algo_helper.log("action {}".format(action))

        if action == "sell":
            self.session += 1

        return action

        #ave comparo meo ! ###### #####
        
