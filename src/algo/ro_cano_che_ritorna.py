                                                     
                #compa, compa caro !                                          
                #

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
        ma9_last, ma9_prev = self.algo_helper.ma_last_prev(9)
        ma10_last, ma10_prev = self.algo_helper.ma_last_prev(10)
        ma13_last, ma13_prev = self.algo_helper.ma_last_prev(13)
        ma16_last, ma16_prev = self.algo_helper.ma_last_prev(16)
        ma18_last, ma18_prev = self.algo_helper.ma_last_prev(18)
        ma25_last, ma25_prev = self.algo_helper.ma_last_prev(25)
        ma30_last, ma30_prev = self.algo_helper.ma_last_prev(30)
        ma33_last, ma33_prev = self.algo_helper.ma_last_prev(33)
        ma36_last, ma36_prev = self.algo_helper.ma_last_prev(36)
        ma39_last, ma39_prev = self.algo_helper.ma_last_prev(39)
        ma40_last, ma40_prev = self.algo_helper.ma_last_prev(40)
        ma50_last, ma50_prev = self.algo_helper.ma_last_prev(50)
        ma78_last, ma78_prev = self.algo_helper.ma_last_prev(78)
        
        
        
        
        # moving average (2-3-4-5-7-8-20-43-100) di x minuti prima

        ma2_2_min_ago = self.algo_helper.ma_minutes_ago(2, 2)
        ma2_3_min_ago = self.algo_helper.ma_minutes_ago(2, 3)
        ma3_2_min_ago = self.algo_helper.ma_minutes_ago(3, 2)
        ma3_9_min_ago = self.algo_helper.ma_minutes_ago(3, 9)
        ma4_2_min_ago = self.algo_helper.ma_minutes_ago(4, 2)
        ma4_5_min_ago = self.algo_helper.ma_minutes_ago(4, 5)
        ma6_2_min_ago = self.algo_helper.ma_minutes_ago(6, 2)
        ma8_4_min_ago = self.algo_helper.ma_minutes_ago(8, 4)
        ma13_2_min_ago = self.algo_helper.ma_minutes_ago(13, 2)
        ma33_5_min_ago = self.algo_helper.ma_minutes_ago(33, 5)
        ma39_2_min_ago = self.algo_helper.ma_minutes_ago(39, 2)
        ma50_2_min_ago = self.algo_helper.ma_minutes_ago(50, 2)
        ma78_2_min_ago = self.algo_helper.ma_minutes_ago(78, 2)
        ma78_10_min_ago = self.algo_helper.ma_minutes_ago(78, 10)
        
       
    
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


        # PREZZO di X MINUTI FA (di mercato) - 
        
        price_2_min_ago = self.algo_helper.price_minutes_ago(2)
        price_20_min_ago = self.algo_helper.price_minutes_ago(20)
        
        
        

        #############################################################################################################################################################
        
        # VENDE DOPO x SECONDI - ro cano torna a casa - (ma c'e' anche un "e se")
        max_hold_time_in_seconds = 2400
        # 2400 / 60 = 40 minuti
        
       

        #########################################################################################################################################################
        #########################################################################################################################################################
        
        
        
        #                                                         T U T T E    L E   D E V I A T I O N  !
        
        # deviation per comprare
        
        
        
        # formula deviation
        deviation = (ma2_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.log("deviation: {}".format(deviation))
        # da maddog per ATTESA INUTILE !
        
        
        
        # formula DEVIATION_gabbia
        deviation_gabbia = (ma8_last/ma78_last - 1) *100 if ma78_last else 0
        self.algo_helper.log("deviation_gabbia: {}".format(deviation_gabbia))
        
        
       
        # formula DEVIATION_buy1 per la compra 1
        deviation_buy1 = (ma8_last/ma78_last - 1) * 100 if ma78_last else 0
        self.algo_helper.log("deviation_buy1: {}".format(deviation_buy1))

        # formula DEVIATION_buy2 per la compra 2
        deviation_buy2 = (ma8_last/ma78_last - 1) * 100 if ma78_last else 0
        self.algo_helper.log("deviation_buy2: {}".format(deviation_buy2))

        # formula DEVIATION_buy3 per la compra 3
        deviation_buy3 = (ma6_last/ma78_last - 1) * 100 if ma78_last else 0
        self.algo_helper.log("deviation_buy3: {}".format(deviation_buy3))
        

        
        
        # formula DEVIATION_buy per comprare UN PO' PIU' SOPRA DEL LAST TRADE ( di solito l' ultimo SELL )
        deviation_buy=(ma2_last/last_trade_price - 1) *100 if last_trade_price else 0
        self.algo_helper.log("deviation_buy: {}".format(deviation_buy))   
       
      
        # formula DEVIATION_buy_crollo per comprare a una certa distanza da ma13
        deviation_buy_crollo = (ma3_last/ma13_last - 1) *100 if ma13_last else 0
        self.algo_helper.log("deviation_buy_crollo: {}".format(deviation_buy_crollo))
        
       
        # formula DEVIATION_ma7_sopra_ma40
        deviation_ma7_sopra_ma40 = (ma7_last/ma40_last - 1) *100 if ma40_last else 0
        self.algo_helper.log("deviation_ma7_sopra_ma40: {}".format(deviation_ma7_sopra_ma40))
        
       
      
        # formula DEVIATION_SPAZIO_TEMPO ( per comprare se c'e' una velocita' nel rialzo del prezzo )
        deviation_spazio_tempo = (ma3_last/ma3_9_min_ago - 1) *100 if ma3_9_min_ago else 0
        self.algo_helper.log( "deviation_spazio_tempo: {}".format(deviation_spazio_tempo))  
        
        
        ########################################################################################
        
        # deviation per vendere
        
        
        # formula DEVIATION_sell 
        deviation_sell = (ma3_last/last_trade_price - 1) *100 if last_trade_price else 0
        self.algo_helper.log("deviation_sell: {}".format(deviation_sell))   
        
        # formula DEVIATION_sell_ma78
        deviation_sell_ma78 = (ma2_last/ma78_last - 1) *100 if ma78_last else 0
        self.algo_helper.log("deviation_sell_ma78: {}".format(deviation_sell_ma78))
        
        # formula deviation_ma39 per vendere un po' piu' giu' di ma39
        deviation_ma39 = (ma3_last / ma39_last - 1) * 100 if ma39_last else 0
        self.algo_helper.log("deviation_ma39: {}".format(deviation_ma39))
        
        
        
        
        
        # formula vendi se dopo 20 minuti il prezzo non aumenta - attesa inutile
        # PREZZO DI ADESSO / PREZZO DI 20 MINUTI FA < 0,10
        condizione_attesa_inutile = ((ma2_last/price_20_min_ago)-1)*100 if price_20_min_ago else 0
        
        
        #######################################################################################
        
        
        
        
        
        ####################################################################################################################################################

        # DEFAULT ACTION DICE DI NON FARE NIENTE (= None, NON TOCCARE )
        action = None

        ##########################################################################################################################################
        
        
        # APRE E CHIUDE GABBIA

        
        if deviation_gabbia > -0.60 or deviation_buy1 < -1.90:

            # ti ricordo che deviation_gabbia = (ma8_last / ma78_last)

            # NON TOCCARE QUESTA CONDIZIONE ! SERVE PER APERTURA DI GABBIA !
            if not self.session or not self.open:
                self.session = 1
                self.open = True
                self.algo_helper.log("session {}: open segment".format(self.session))

        
        # SI CHIUDE LA GABBIA SE
        else:    
            self.open = False
            self.algo_helper.log("session {}: closed segment".format(self.session))
            
            
            

        #############################################################################################################################################

        # COMPRA
        # NON TOCCARE QUESTA RIGA ( DICE CHE STA IN MODO BUY, vuole COMPRARE ! )
        
        if self.open and self.session and last_trade_action != "buy":

         
            ###########################################################################################################################################
                                                              #   B U Y 
            ###########################################################################################################################################
            
            
            
            ######################################################################################################## COMPRA sessione 1

            if self.session == 1:
              
                # BUY 1 DURANTE IL RIALZO con INCROCIO CLASSICO
                
                if (
                    deviation_buy1 > 0.10 
                    and (ma8_prev < ma50_prev and ma8_last > ma50_last)
                    
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma4_last > ma8_last
                  
                ):

                    buy="BUY 1 con INCROCIO CLASSICO"
                    action="buy"
                
                
               
                ############################################################################## QUESTA FUNZIONA
                
                # BUY 1 DURANTE IL RIALZO con LA DEVIATION BUY 1
                # deviation_buy1 = ma8_last/ma78_last
                
                elif (
                    
                    deviation_buy1 > 0.09
                    and ma8_last > ma50_last
                    
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma4_last > ma4_2_min_ago
                  
                ):

                    buy = "BUY 1 con LA DEVIATION"
                    action = "buy"
                
                
                ##############################################################################
                
                
                # BUY 1 DURANTE IL RIALZO con DEVIATION_SPAZIO_TEMPO
                if (
                    deviation_spazio_tempo > 0.65
                    and ma4_last > ma4_5_min_ago
                    and ma3_last > ma78_last
                    # QUESTA CONDIZIONE SPAZIO-TEMPO ERA UNA TUA IDEA !
                    
                ):

                    buy = "BUY 1 con DEVIATION_SPAZIO_TEMPO"
                    action = "buy"
                    
                   
                
                
                
                ##############################################################################################################################
                # IMPORTANTISSIMO ! SOLO PER IL BUY 1 - PER COMPRARE DURANTE IL CROLLO - compa prega per me - ( cruise - david gilmour )
                ##############################################################################################################################
                
                
                
                # BUY  PRIMO MODO DURANTE IL CROLLO
                elif (    
                    ma2_last > ma2_2_min_ago
                    and (deviation_buy1 < -2.30 and (ma8_prev < ma25_prev and ma8_last > ma25_last))
                  
                ):
                    buy = "BUY DURANTE IL CROLLO - modo 1"
                    action = "buy"
                
                
                
                
                
                # BUY  SECONDO MODO - DURANTE IL CROLLO
                elif (    
                    ma2_last > ma2_2_min_ago
                    and (deviation_buy1 < -2.40 and deviation_buy_crollo > 0.39)
                ):
                    buy = "BUY DURANTE IL CROLLO - modo 2"
                    action = "buy"
            
            
            
            
            ############################################################################################################

            #############################################################################################################      COMPRA sessione 2

            elif self.session == 2:
              
                if (
                    
                    deviation_ma7_sopra_ma40 > 0.12
                    and (ma4_prev < ma9_prev and ma4_last > ma9_last) 
                    and deviation_buy2 > 0.12
                    and ma2_last > ma2_2_min_ago
                    and price > price_2_min_ago
                    and ma4_last > ma78_last
                    and ma3_last > ma40_last
                ):
                    buy = "BUY 2A"
                    action = "buy"   
                        
                    
                    
                ####################################################### MIRACOLO QUESTA HA FUNZIONATO !
                
                
                elif (
                    deviation_buy2 > 0.13
                    and deviation_ma7_sopra_ma40 > 0.13
                    and (ma4_prev < ma9_prev and ma4_last > ma9_last) 
                  
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma40_last
                    and ma4_last > ma78_last
                    
                ):
                    buy = "BUY 2B"
                    action = "buy"
                    
            
            
            ###############################################################################################################

            # ###############################################################################################################     COMPRA sessione 3 in poi

            # elif self.session == 3:
            # CON " elif self.session == 3: " NON COMPRAVA PIU' ALLORA HO PRESO ELSE DA MADDOG CHE INVECE ANDAVA BENE

            
            else: 
                if (
                    deviation_buy3 > 0.10
                    and deviation_ma7_sopra_ma40 > 0.10
                    and (ma4_prev < ma9_prev and ma4_last > ma9_last) 
                   
                    and ma2_last >= ma4_last
                    and ma2_last > ma50_last
                    and ma4_last > ma78_last
                ):
                    buy = "BUY 3A"
                    action = "buy"    
                        
                    
                    

                elif (
                    deviation_buy3 > 0.16
                    and deviation_ma7_sopra_ma40 > 0.12
                    
                   # deviation_buy3 = ma6_last/ma78
                  
                    and ma2_last > ma8_last
                    and ma2_last > ma78_last
                    and ma4_last > ma78_last
                ):
                    buy = "BUY 3B"
                    action = "buy"
                
                
                
        
        ###########################################################################################################################
                                                     #                                  V E N D I T A ....ma non vende proprio !!!!
        ############################################################################################################################

        
        

        # NON TOCCARE QUESTA RIGA (DICE CHE STA IN MODO SELL, DEVO VENDERE)
      
        elif last_trade_action == "buy":
          
          
            
            #####################################################################################################################
            
            # VENDITA CON QUESTE 2 ECCEZIONI !
            
            
            # 1) ro cano VENDE CON UN SALVAGENTE
          
            if (
                deviation_ma39 < -0.34
                
                # deviation_ma39 = ma3_last / ma39_last
            ):
                sell = "SELL SALVAGENTE FUNZIONANTE riga 409"
                action = "sell"
                
                
                
             
            # 2) ro cano VENDE " DOPO x MINUTI " "max hold time"

            
                
                
            

             
                
                
                
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds 
                and ma2_last < last_trade_price 
                and deviation < 0.10
               
                # condizione_attesa_inutile = ma2_last < last_trade_price 
                # deviation = ma2_last / last_trade_price
                
            ):

                sell = "SELL TEMPO"
                action = "sell"

          ###########################################################################################################################################
          
          
          
           ###################################################################################################################################

            # VENDITA 1 - con fasce di tempo ! c'e' vita su marte !

            #    minuti
            #   0 -  3 -
            #   3 -  5 -
            #   5 - 12 -

            #  12 - 18 -
            #  18 - 40 -
            #   > 40   -

            ###################################################################################################################################
            
          
            ####################################################################################################################### 0 - 3 min

            # VENDITA - da 0 a 3 minuti = da 0 a 180 secondi
            if seconds_since_last_trade > 0 and seconds_since_last_trade <= 180:

                if (
                    ma50_last > ma50_2_min_ago 
                    and (ma3_prev > ma30_prev and ma3_last < ma30_last) 
                    and deviation_sell>0.18
                ):
                
                    sell = "SELL 1 (0-3 min) con ma50 >"
                    action = "sell"
                    
                
            
                
                elif (
                    ma50_last > ma50_2_min_ago 
                    and (ma3_prev > ma16_prev and ma3_last < ma16_last) 
                    and deviation_sell>0.65
                 
                ):

                    sell ="SELL 2 (0-3 min) con ma50 >"
                    action ="sell"
                
                
                
                
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last) 
                    and deviation_sell > 0.80
               
                ):

                    sell = "SELL 3 (0-3 min) con ma50 >"
                    action = "sell"
                
                
                
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma78_prev and ma3_last < ma78_last) 
                    and deviation_sell < -0.20
                   
                ):

                    sell = "SELL 4 (0-3 min) con ma50 >"
                    action = "sell"
                    

                    
                    
                # --------------------------------------------------------------------------------------VENDITA ECCEZIONALE DURANTE IL CROLLO
                #################################################################################################################################
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma16_prev and ma3_last < ma16_last) 
                    and deviation_sell > 0.23
                 
                ):

                    sell = "SELL 5 (0-3 min) con ma50 <"
                    action = "sell"

                # ---------------------------------------------------------------------------------------------------------------------
                #################################################################################################################################
                
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma8_prev and ma3_last < ma8_last) 
                    and deviation_sell > 0.60
                   
                ):

                    sell = "SELL 6 ( 0-3 min ) con ma50 <"
                    action = "sell"
                
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma78_prev and ma3_last < ma78_last) 
                    and deviation_sell < -0.20
                   
                ):

                    sell = "SELL 7 (0-3 min) con ma50 <"
                    action = "sell"
                
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma16_prev and ma3_last < ma16_last) 
                    and deviation_sell < -0.75
                   
                ):

                    sell = "SELL 8 (0-3 min) con ma50 <"
                    action = "sell"
            
               
            
            ################################################################################################################################         3-5 min
            ################################################################################################################################
            
            
            # VENDITA - da 3 a 5 minuti = da 180 a 300 secondi

            if seconds_since_last_trade > 180 and seconds_since_last_trade <= 300:

                if (
                    ma50_last > ma50_2_min_ago 
                    and (ma3_prev > ma25_prev and ma3_last < ma25_last) 
                    and deviation_sell > 0.18
                   
                ):
                  
                    sell = "SELL 9 (3-5 min) con ma50 >"
                    action = "sell"
                
                
                
                elif (
                    ma50_last > ma50_2_min_ago 
                    and (ma3_prev > ma16_prev and ma3_last < ma16_last) 
                    and deviation_sell > 0.66
                 
                ):

                    sell = "SELL 10 (3-5 min) con ma50 >"
                    action = "sell"
                
                
                
                
                elif (
                    ma50_last > ma50_2_min_ago 
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last) 
                    and deviation_sell > 0.80
                  
                ):

                    sell = "SELL 11 (3-5 min) con ma50 >"
                    action = "sell"

                    
                # -------------------------------------------------------------------------------------------------------------------------crollo
                ############################################################################################################################
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last) 
                    and deviation_sell > 0.23
                 
                ):

                    sell = "SELL 12 (3-5 min) con ma50 <"
                    action = "sell"

                # --------------------------------------------------------------------------------------------------------------------------------
                ###############################################################################################################################
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma78_prev and ma3_last < ma78_last) 
                    and deviation_sell < -0.20
                  
                ):

                    sell = "SELL 13 (3-5 min) con ma50 <"
                    action = "sell"

                    
                    
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma16_prev and ma3_last < ma16_last) 
                    and deviation_sell < -0.75
                  
                ):

                    sell = "SELL 14 (3-5 min) con ma50 <"
                    action = "sell"

               
                
                
            ################################################################################################################################### 5-12 min

            
            # VENDITA - da 5 a 12 minuti = da 300 a 720 secondi

            
            elif seconds_since_last_trade > 300 and seconds_since_last_trade <= 720:

                
                if (
                    ma50_last > ma50_2_min_ago 
                    and (ma3_prev > ma25_prev and ma3_last < ma25_last) 
                    and deviation_sell > 0.18
                   
                ):
                    sell = "SELL 15 (5-12 min) con ma50 >"
                    action = "sell"

                    
                    
               
                
                
                elif (
                    ma50_last > ma50_2_min_ago 
                    and (ma3_prev > ma16_prev and ma3_last < ma16_last) 
                    and deviation_sell > 0.67
                  
                ):
                    sell = "SELL 16 (5-12 min) con ma50 >"
                    action = "sell"

                    
                    
                    
                elif (
                    ma50_last > ma50_2_min_ago 
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last) 
                    and deviation_sell > 0.80
                   
                ):
                    sell = "SELL 17 (5-12 min) con ma50 >"
                    action = "sell"

                    
                # ---------------------------------------------------------------------------------------------------------------------- crollo
                #########################################################################################################################
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last) 
                    and deviation_sell > 0.23
                   
                ):
                    sell = "SELL 18 (5-12 min) con ma50 <"
                    action = "sell"

                    
                # --------------------------------------------------------------------------------------------------------------------------------
                 ###################################################################################################################################
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma78_prev and ma3_last < ma78_last) 
                    and deviation_sell < -0.20
                 
                ):
                    sell = "SELL 19 (5-12 min) con ma50 <"
                    action = "sell"

                    
                    
                    
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last) 
                    and deviation_sell < -0.75
                   
                ):

                    sell = "SELL 20 (5-12 min) con ma50 <"
                    action = "sell"

                  
             
                
            ############################################################################################################################    12-24 min

            
            # VENDITA - da 12 a 24 minuti = da 720 a 1440 secondi

           
        
            elif seconds_since_last_trade > 720 and seconds_since_last_trade <= 1440:
                
                

                if (
                    ma50_last > ma50_2_min_ago 
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last) 
                    and deviation_sell > 0.18
                
                ):
                    sell = "SELL 21 (12-24 min) con ma50 >"
                    action = "sell"

                    
                    
               
                
                
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                   
                ):
                    sell = "SELL 22 (12-24 min) con ma50 >"
                    action = "sell"

                    
                    
                    
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last) 
                    and deviation_sell > 0.80
                 
                ):
                    sell = "SELL 23 (12-24 min) con ma50 >"
                    action = "sell"

                    
                    
                # ------------------------------------------------------------------------------------------------------------- crollo
                ##############################################################################################################à
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last) 
                    and deviation_sell > 0.23
                  
                ):
                    sell = "SELL 24 (12-24 min) con ma50 <"
                    action = "sell"

                    
                    
                # ---------------------------------------------------------------------------------------------------------------
                  ###############################################################################################################
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma78_prev and ma3_last < ma78_last) 
                    and deviation_sell < -0.20
                  
                ):
                    sell = "SELL 25 (12-24 min) con ma50 <"
                    action = "sell"

                    
                    
                    
                    
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last) 
                    and deviation_sell < -0.75
                 
                ):

                    sell = "SELL 26 (12-24 min) con ma50 <"
                    action = "sell"

                  
                    
            ################################################################################################################################## 24-40 min

            # VENDITA - da 24 a 40 minuti = da 1080 a 1800 secondi

            elif seconds_since_last_trade > 1440 and seconds_since_last_trade <= 2400:

                
               
                if (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma25_prev and ma3_last < ma25_last) 
                    and deviation_sell > 0.18
                  
                ):
                    sell = "SELL 27 (24-40 min) con ma50 >"
                    action = "sell"

                    
               
                    
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                  
                ):
                    sell = "SELL 28 (24-40 min) con ma50 >"
                    action = "sell"

                    
                    
                    
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last) 
                    and deviation_sell > 0.80
                 
                ):
                    sell = "SELL 29 (24-40 min) con ma50 >"
                    action = "sell"

                    
                    
                    
                elif (
                    ma50_last > ma50_2_min_ago 
                    and (ma3_prev > ma78_prev and ma3_last < ma78_last) 
                    and deviation_sell < -0.20
                 
                ):
                    sell = "SELL 30  (24-40 min) con ma50 <"
                    action = "sell"

                    
                    
                # ----------------------------------------------------------------------------------------------------------------------crollo
                #########################################################################################################################
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last) 
                    and deviation_sell > 0.23
                   
                ):
                    sell = "SELL 31  (24-40 min) con ma50 <"
                    action = "sell"

                    
                    
                # --------------------------------------------------------------------------------------------------------------------------
                #############################################################################################################################
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma78_prev and ma3_last < ma78_last) 
                    and deviation_sell < -0.20
                  
                ):
                    sell = "SELL 32  (24-40 min) con ma50 <"
                    action = "sell"

                    
                    
                    
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last) 
                    and deviation_sell < -0.75
                   
                ):

                    sell = "SELL 33 (24-40 min) con ma50 <"
                    action = "sell"
                    
                    
                    
             
                    
                    
            ##############################################################################################################################     > 40 min

            
            
            
            # VENDITA - da 40 minuti in poi = da 2400 secondi in poi

            elif seconds_since_last_trade > 2400:

                
                
                
                if (
                    ma50_last > ma50_2_min_ago 
                    and (ma3_prev > ma25_prev and ma3_last < ma25_last) 
                    and deviation_sell > 0.18
                
                ):

                    sell = "SELL 34 ( dopo 40 min ) con ma50 >"
                    action = "sell"

                
                    
                    
                    
                elif (
                    ma50_last > ma50_2_min_ago 
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last) 
                    and deviation_sell > 0.60
                 
                ):

                    sell = "SELL 35 ( dopo 40 min ) con ma50 >"
                    action = "sell"

                    
                    
                  
                    
                elif (
                    ma50_last > ma50_2_min_ago 
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                 
                ):
                    sell = "SELL 36 ( dopo 40 min ) con ma50 >"
                    action = "sell"

                    
                    
                    
                    
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last) 
                    and deviation_sell > 0.23
                   
                ):
                    sell = "SELL 37 ( dopo 40 min ) con ma50 <"
                    action = "sell"

                    
                  
            ##################################################################################################################################

            
           # VEDI 399 LE HO GIA' MESSE LI LE VENDITE ECCEZIONALI
            
            # salvagente SOLO mentre sale ! altrimenti va in conflitto con il buy durante il crollo

            # 1) STOP LOSS (salvagente)

            
            if (
                ma50_last >= ma50_2_min_ago 
                and (ma3_prev > ma18_prev and ma3_last < ma18_last) 
                and deviation_sell < -0.68
             
            ):
                sell = "SALVAGENTE 1"
                action = "sell"

                
                
                
            elif (
                ma50_last >= ma50_2_min_ago 
                and (ma3_prev > ma36_prev and ma3_last < ma36_last) 
                and deviation_sell < -0.63
               
            ):
                sell = "SALVAGENTE 2"
                action = "sell"

           
            
                
            ##########################################################################################################################

            
          
            
            # 2) ro cano VENDE " DOPO x MINUTI " "max hold time"

            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds 
                and (ma2_prev > ma78_prev and ma2_last < ma78_last) 
                and deviation_sell < -0.50
              
            ):

                sell = "SELL TEMPO 1"
                action = "sell"

                
            
           

                                                     ############### FINE ALGORITH ###################
            
            

        self.algo_helper.log("action {}".format(action))

        if action == "sell":
            self.algo_helper.log("action sell {}".format(sell))
            self.session += 1
            
        elif action == "buy":
            self.algo_helper.log("action buy {}".format(buy))

        return action
      
      
        #compa, compa caro !
