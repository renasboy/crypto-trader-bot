                
                
                # ti voglio bene, compa.                                     
                # compa, compa caro !                                          
                # Tom Petty - Something Good Coming
                

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
        
        ma11_last, ma11_prev = self.algo_helper.ma_last_prev(11)
        
        ma13_last, ma13_prev = self.algo_helper.ma_last_prev(13)
        ma16_last, ma16_prev = self.algo_helper.ma_last_prev(16)
        ma18_last, ma18_prev = self.algo_helper.ma_last_prev(18)
        
        ma23_last, ma23_prev = self.algo_helper.ma_last_prev(23)
        
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
        
        ma2_4_min_ago = self.algo_helper.ma_minutes_ago(2, 4)
        
        ma3_2_min_ago = self.algo_helper.ma_minutes_ago(3, 2)
        
        ma3_3_min_ago = self.algo_helper.ma_minutes_ago(3, 3)
        
        ma3_9_min_ago = self.algo_helper.ma_minutes_ago(3, 9)
        ma4_2_min_ago = self.algo_helper.ma_minutes_ago(4, 2)
        ma4_4_min_ago = self.algo_helper.ma_minutes_ago(4, 4)
        ma6_2_min_ago = self.algo_helper.ma_minutes_ago(6, 2)
        ma8_4_min_ago = self.algo_helper.ma_minutes_ago(8, 4)
        ma13_2_min_ago = self.algo_helper.ma_minutes_ago(13, 2)
        ma33_5_min_ago = self.algo_helper.ma_minutes_ago(33, 5)
        ma39_2_min_ago = self.algo_helper.ma_minutes_ago(39, 2)
        ma39_3_min_ago = self.algo_helper.ma_minutes_ago(39, 3)
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
        price_10_min_ago = self.algo_helper.price_minutes_ago(10)
        price_15_min_ago = self.algo_helper.price_minutes_ago(15)
        price_20_min_ago = self.algo_helper.price_minutes_ago(20)
        
        
        ###################################################################################################################################################### TEMPO
        ######################################################################################################################################################
                                                                                                                
        
        # importante : dolce attesa vedi riga 522
        
        # VENDE DOPO x SECONDI - ro cano torna a casa - (ma c'e' anche un "e se")
        max_hold_time_in_seconds = 480
        #  8 minuti * 60 = 480
        
       

        #########################################################################################################################################################
        #########################################################################################################################################################
        
        
        
        #                                                         T U T T E    L E   D E V I A T I O N  !
        
        
        
        
        ##############################################################################################################
        # formula DEVIATION_gabbia
        deviation_gabbia = (ma8_last/ma39_last - 1) *100 if ma39_last else 0
        self.algo_helper.log("deviation_gabbia: {}".format(deviation_gabbia))
        
        ##################################################################################################################  
        
        # formula deviation
        deviation = (ma2_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.log("deviation: {}".format(deviation))
        
        ##################################################################################################################
        
        ################################################################ deviation per comprare
        
        
        
        # formula DEVIATION_buy1 per la compra 1
        deviation_buy1 = (ma11_last/ma39_last - 1) * 100 if ma39_last else 0
        self.algo_helper.log("deviation_buy1: {}".format(deviation_buy1))

        # formula DEVIATION_buy2 per la compra 2
        deviation_buy2 = (ma8_last/ma50_last - 1) * 100 if ma50_last else 0
        self.algo_helper.log("deviation_buy2: {}".format(deviation_buy2))
        
        # formula DEVIATION_buy3 per la compra 3
        deviation_buy3 = (ma4_last/ma30_last - 1) * 100 if ma30_last else 0
        self.algo_helper.log("deviation_buy3: {}".format(deviation_buy3))
        
        #------------------------------------------------------------------------------------------------------------
        
        #formula delta_buy3_incrocio_ma3_ma8 > 0.10 per la compra 3
        delta_buy3_incrocio_ma3_ma8 = (ma3_last/ma8_last - 1) * 100 if ma8_last else 0
        self.algo_helper.log("delta_buy3_incrocio_ma3_ma8: {}".format(delta_buy3_incrocio_ma3_ma8))
       
      
        # formula DEVIATION_buy per comprare UN PO' PIU' SOPRA DEL LAST TRADE ( di solito l' ultimo SELL )
        deviation_buy=(ma2_last/last_trade_price - 1) *100 if last_trade_price else 0
        self.algo_helper.log("deviation_buy: {}".format(deviation_buy))   
       
        
        ############################################################################################     DEVIATION_buy_crollo
        
        # formula DEVIATION_buy_crollo_1 per comprare a una certa distanza da ma78
        deviation_buy_crollo_1 = (ma8_last/ma78_last - 1) *100 if ma78_last else 0
        self.algo_helper.log("deviation_buy_crollo_1: {}".format(deviation_buy_crollo_1))
        
        
        # formula DEVIATION_buy_crollo_2 per comprare a una certa distanza da ma13
        deviation_buy_crollo_2 = (ma3_last/ma13_last - 1) *100 if ma13_last else 0
        self.algo_helper.log("deviation_buy_crollo_2: {}".format(deviation_buy_crollo_2))
        
        ############################################################################################################################
        
        
        
        
        
        # formula DEVIATION_buy_ma3_sopra_ma13 per comprare a una certa distanza da ma13
        deviation_buy_ma3_sopra_ma13 = (ma3_last/ma13_last - 1) *100 if ma13_last else 0
        self.algo_helper.log("deviation_buy_ma3_sopra_ma13: {}".format(deviation_buy_ma3_sopra_ma13))
        
        
        # formula DEVIATION_ma4_sopra_ma30
        deviation_ma4_sopra_ma30 = (ma4_last/ma30_last - 1) *100 if ma30_last else 0
        self.algo_helper.log("deviation_ma4_sopra_ma30: {}".format(deviation_ma4_sopra_ma30))
        
        
        # formula deviation_ma7_sopra_ma40
        deviation_ma7_sopra_ma40 = (ma7_last/ma40_last - 1) *100 if ma40_last else 0
        self.algo_helper.log("deviation_ma7_sopra_ma40: {}".format(deviation_ma7_sopra_ma40))
        
        
        
        
        
        
        ########################################################################################
        
        
        ######################################################################################## deviation per vendere
        
        
        # formula DEVIATION_sell 
        deviation_sell = (ma3_last/last_trade_price - 1) *100 if last_trade_price else 0
        self.algo_helper.log("deviation_sell: {}".format(deviation_sell))   
        
        # formula DEVIATION_sell_ma78
        deviation_sell_ma78 = (ma2_last/ma78_last - 1) *100 if ma78_last else 0
        self.algo_helper.log("deviation_sell_ma78: {}".format(deviation_sell_ma78))
        
        # formula deviation_ma39 per vendere un po' piu' giu' di ma39
        deviation_ma39 = (ma3_last / ma39_last - 1) * 100 if ma39_last else 0
        self.algo_helper.log("deviation_ma39: {}".format(deviation_ma39))
        
        
        ################################################################################################ SPAZIO - TEMPO
        
        
        # formula COMPRA_SPAZIO_TEMPO ( per comprare se c'e' una alta velocita' nel rialzo del prezzo )
        compra_spazio_tempo = (ma3_last/ma3_3_min_ago - 1) *100 if ma3_3_min_ago else 0
        self.algo_helper.log( "compra_spazio_tempo: {}".format(compra_spazio_tempo))  
        
        
        # formula VENDI_SPAZIO_TEMPO ( per vendere se c'e' una alta velocita' nel ribasso del prezzo )
        vendi_spazio_tempo = (ma2_last/ma2_4_min_ago - 1) *100 if ma2_4_min_ago else 0
        self.algo_helper.log( "vendi_spazio_tempo: {}".format(vendi_spazio_tempo))  
        
        
        ####################################################################################################################################################

        # DEFAULT ACTION DICE DI NON FARE NIENTE (= None, NON TOCCARE )
        action = None

        ##########################################################################################################################################
        
        
        # APRE E CHIUDE GABBIA

        
        if deviation_gabbia > -0.50 or deviation_buy_crollo_1 < -1.90:
          
            # deviation_gabbia = ma8_last / ma39_last
            # deviation_buy_crollo_1 = ma8_last / ma78_last
            
            
            
            
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
              
                #------------------------------------------------------------ BUY 1 DURANTE IL RIALZO con INCROCIO CLASSICO 39-78
                
                if (
                    ma13_last > ma78_last
                    and (ma13_prev < ma78_prev and ma13_last > ma78_last)       
                    
                    and ma2_last > ma2_2_min_ago
                    and ma4_last > ma8_last
                  
                ):

                    buy="BUY 1 con INCROCIO CLASSICO 8-48 riga 299"
                    action="buy"
                
                
               
                #--------------------------------------------------------------    BUY 1 DURANTE IL RIALZO con LA DEVIATION BUY 1
                
                
                
               
                elif (
                    
                    deviation_buy1 > 0.08
                    and ma78_last > ma78_2_min_ago
                    
                    
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma4_last > ma4_2_min_ago
                  
                ):

                    buy = "BUY 1 con LA DEVIATION e ma78> riga 321"
                    action = "buy"
                    
                    
                    # deviation_buy1 = ma11_last/ma39_last
                    
                    
                ####################################################################
                
                elif (
                    
                    deviation_buy1 > 0.12
                    
                    and ma78_last < ma78_2_min_ago
                    
                    
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma4_last > ma4_2_min_ago
                  
                ):

                    buy = "BUY 1 con LA DEVIATION e ma78 < riga 343"
                    action = "buy"
                    
                    
                    #deviation_buy1 = ma11_last/ma39_last
                    
                
                ##############################################################################
                
                
                
                # BUY 1 DURANTE IL RIALZO con COMPRA_SPAZIO_TEMPO
                if (
                    compra_spazio_tempo > 0.70
                    and ma3_last > ma78_last
                    
                  
                    # compra_spazio_tempo = ma3_last/ma3_9_min_ago
                    # QUESTA CONDIZIONE SPAZIO-TEMPO ERA UNA TUA IDEA !
                    
                ):

                    buy = "BUY 1 con COMPRA_SPAZIO_TEMPO riga 365"
                    action = "buy"
                    
                   
                
                ##############################################################################################################################
                # IMPORTANTISSIMO ! SOLO PER IL BUY 1 - PER COMPRARE DURANTE IL CROLLO - compa prega per me - ( cruise - david gilmour )
                ##############################################################################################################################
                
                # entriamo nell' area dell' ipervenduto, compa !
                
                # BUY  PRIMO MODO DURANTE IL CROLLO
                
                elif (    
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -2.30 
                    and (ma8_prev < ma25_prev and ma8_last > ma25_last)
                  
                ):
                    buy = "BUY DURANTE IL CROLLO - modo 1 riga 384"
                    action = "buy"
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                
                
                
                
                # BUY  SECONDO MODO - DURANTE IL CROLLO
                elif (    
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -2.40
                    and deviation_buy_crollo_2 > 0.39
                         
                ):
                    buy = "BUY DURANTE IL CROLLO - modo 2 riga 398"
                    action = "buy"
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_buy_crollo_2 = ma3_last / ma13_last
            
            
            ############################################################################################################

            #############################################################################################################      COMPRA sessione 2

            elif self.session == 2:
              
                if (
                    deviation_buy2 > 0.08
                    and deviation_buy_ma3_sopra_ma13 > 0.09
                    and deviation_ma7_sopra_ma40 > 0.08
                    
                    
                    and ma2_last > ma2_2_min_ago
                    and price > price_2_min_ago
                    and ma3_last > ma40_last
                    
                ):
                    buy = "BUY 2A riga 421"
                    action = "buy"   
                        
                    # deviation_buy_ma3_sopra_ma13 > x e' fondamentale !
                    # deviation_buy2 = ma8_last/ma50_last 
                
                
                
                elif (
                    deviation_buy2 > 0.13
                    and deviation_buy_ma3_sopra_ma13 > 0.10
                    and deviation_ma7_sopra_ma40 > 0.14
                    and (ma4_prev < ma9_prev and ma4_last > ma9_last) 
                    
                  
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma40_last
                    and ma4_last > ma78_last
                    
                ):
                    buy = "BUY 2B riga 441"
                    action = "buy"
                    
                    
                    # deviation_buy2 = ma8_last / ma50
           
                  
            # ###############################################################################################################     COMPRA sessione 3 in poi

           
            else: 
                if (
                    deviation_buy3 > 0.10
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.10
                    and (ma4_prev < ma9_prev and ma4_last > ma9_last) 
                    
                    and ma4_last > ma50_last
                    
                ):
                    buy = "BUY 3A riga 461"
                    action = "buy"    
                        
                    
                    

                elif (
                
                    deviation_buy3 > 0.02
                    and delta_buy3_incrocio_ma3_ma8 > 0.06
                    
                    
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago 
               
                ):
                    buy = "BUY 3B RIVOLUZIONARIO - riga 478"
                    action = "buy"
                    
                  
                    # deviation_buy3 = ma4_last/ma30_last
                    
        ############################################################################################################
                                                     #                                                                V E N D I T A !
        ############################################################################################################

        
        

        # NON TOCCARE QUESTA RIGA (DICE CHE STA IN MODO SELL, DEVO VENDERE !)
      
        elif last_trade_action == "buy":
          
          
            
        #####################################################################################################################
                  
            
            # VENDITA CON QUESTE 3 ECCEZIONI !
            
            
                  
            # 1) ro cano VENDE CON UN SALVAGENTE
          
            if (
                deviation_ma39 < -0.24
            
            ):
                sell = "SELL SALVAGENTE 3-39  riga 510"
                action = "sell"
                  
                # deviation_ma39 = ma3_last / ma39_last  
                
                
            
                  
                  
            # 2) ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA

            elif (
                seconds_since_last_trade > max_hold_time_in_seconds 
                and ma2_last < last_trade_price 
                and deviation < -0.37
                and ma78_last < ma78_2_min_ago
            
            ):

                sell = "SELL DOLCE ATTESA - riga 529"
                action = "sell"
                
                # il fattore tempo - la dolce attesa - solo con trend ribassista
                # deviation = ma2_last / last_trade_price
                
                
                  
                  
            # 3) ro cano VENDE DOPO 4 minuti con VENDI_SPAZIO_TEMPO se il ribasso ha una alta velocita' # ha venduto con +0.07 strano !
                if (
                    vendi_spazio_tempo < -0.65
                    and ma4_last < ma4_4_min_ago
                    
                    # QUESTA CONDIZIONE SPAZIO-TEMPO ERA UNA TUA IDEA !
                    # vendi_spazio_tempo = ma2_last/ma2_4_min_ago
                ):

                    sell = "con VENDI_SPAZIO_TEMPO riga 547"
                    action = "sell"
                
           

          ###################################################################################################################################
          
          ###################################################################################################################################

            # VENDITA 1 - con fasce di tempo ! c'e' vita su marte !

            #    minuti
            #   0 -  3 -
            #   3 -  5 -
            #   5 - 12 -

            #  12 - 18 -
            #  18 - 40 -
            #   > 40   -

            #############################################################################################################################
            
            ##############################################################################################################################
             
            # Tom Petty - Something Good Coming
            
            # <-0.20
            # 0.25 -0.59
            # 0.60-0.79
            # > 0.80
            ####################################################################################################################### 0 - 3 min

            
                  
            # VENDITA - da 0 a 3 minuti = da 0 a 180 secondi
                  
            if seconds_since_last_trade > 0 and seconds_since_last_trade <= 180:
                
                # con ma50 >
                if (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell < -0.20 
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL 1 (0-3 min) con ma50 > riga 593"
                    action = "sell"
                    
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    and deviation_sell > 0.25 and deviation_sell < 0.60
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL 2 (0-3 min) con ma50 > riga 604"
                    action = "sell"
                    
                    
              
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last) 
                    and deviation_sell > 0.61 and deviation_sell < 0.79
                 
                ):
                    sell = "SELL 3 (0-3 min) con ma50 > riga 616"
                    action = "sell"
                    
                    
                    
                    
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last) 
                    and deviation_sell > 0.80
               
                ):

                    sell = "SELL 4 (0-3 min) con ma50 > riga 629"
                    action = "sell"
                    
                 
                    
                ###########################################################################     trend in ribasso
             
            
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last) 
                    and deviation_sell < -0.20
                   
                ):
                    sell = "SELL 5 (0-3 min) con ma50 < riga 643"
                    action = "sell"
                    
                    
                    
                # ---------------------------------------------------------------------------------------------------------------------- crollo   
                
                
                # ------------------------------------------------------------- AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma16_prev and ma3_last < ma16_last) 
                    and deviation_sell < -0.50
                   
                ):
                    sell = "SELL 6 (0-3 min) con ma50 < riga 659"
                    action = "sell"
                    
                # ---------------------------------------------------------------- 
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma23_prev and ma3_last < ma23_last) 
                    and deviation_sell > 0.23
                   
                ):
                    sell = "SELL 7 (0-3 min) con ma50 < riga 671"
                    action = "sell"
                  
              
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma8_prev and ma3_last < ma8_last) 
                    and deviation_sell > 0.60
                   
                ):

                    sell = "SELL 8 (0-3 min) con ma50 < riga 683"
                    action = "sell"
                
                  
              
            ################################################################################################################################         3-5 min
           
            # VENDITA - da 3 a 5 minuti = da 180 a 300 secondi

            elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 300:
              
                if (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell < -0.20 
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL 9 (3-5 min) con ma50 > riga 701"
                    action = "sell"
                    
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    and deviation_sell > 0.25 and deviation_sell < 0.60
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL 10 (3-5 min) con ma50 > riga 712"
                    action = "sell"
                    
                    
              
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last) 
                    and deviation_sell > 0.61
                 
                ):
                    sell = "SELL 11 (3-5 min) con ma50 > riga 724"
                    action = "sell"
                    
                    
                    
                ###########################################################################     trend in ribasso
             
            
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last) 
                    and deviation_sell < -0.20
                   
                ):
                    sell = "SELL 12 (3-5 min) con ma50 < riga 738"
                    action = "sell"
   
         
                # ---------------------------------------------------------------------------------------------------------------------- crollo
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma23_prev and ma3_last < ma23_last) 
                    and deviation_sell > 0.23
                   
                ):
                    sell = "SELL 13 (3-5 min) con ma50 < riga 751"
                    action = "sell"

             
                

            ################################################################################################################################### 5-12 min
            
                  
            
            # VENDITA - da 5 a 12 minuti = da 300 a 720 secondi

            
            elif seconds_since_last_trade > 300 and seconds_since_last_trade <= 720:
           
            
                if (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell < -0.20 
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL 14 (5-12 min) con ma50 > riga 774"
                    action = "sell"
                    
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    and deviation_sell > 0.25 and deviation_sell < 0.60
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL 15 (5-12 min) con ma50 > riga 785"
                    action = "sell"
                    
                    
              
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last) 
                    and deviation_sell > 0.61
                 
                ):
                    sell = "SELL 16 (5-12 min) con ma50 > riga 797"
                    action = "sell"
                    
                    
                    
                ###########################################################################     trend in ribasso
             
            
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last) 
                    and deviation_sell < -0.20
                   
                ):
                    sell = "SELL 17 (5-12 min) con ma50 < riga 811"
                    action = "sell"
   
         
                # ------------------------------------------------------------------------------- crollo
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma23_prev and ma3_last < ma23_last) 
                    and deviation_sell > 0.23
                   
                ):
                    sell = "SELL 18 (5-12 min) con ma50 < riga 824"
                    action = "sell"

             
                
            ############################################################################################################################    12-24 min

            
            # VENDITA - da 12 a 24 minuti = da 720 a 1440 secondi

       
            elif seconds_since_last_trade > 720 and seconds_since_last_trade <= 1440:
                
                if (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell < -0.20 
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL 19 (12-24 min) con ma50 > riga 844"
                    action = "sell"
                
                
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    and deviation_sell > 0.25 and deviation_sell < 0.60
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL 20 (12-24 min) con ma50 > riga 856"
                    action = "sell"
                
                
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma23_prev and ma3_last < ma23_last) 
                    and deviation_sell > 0.61
                 
                ):
                    sell = "SELL 21 (12-24 min) con ma50 > riga 867"
                    action = "sell"

                
                
                
                
                ##################################################################### con trend discendente
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last) 
                    and deviation_sell < -0.16
                  
                ):
                    sell = "SELL 22 (12-24 min) con ma50 < riga 882"
                    action = "sell"
                
                
                # -----------------------------------------------------------------------------crollo
                
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last) 
                    and deviation_sell > 0.23
                   
                ):
                    sell = "SELL 23 (12-24 min) con ma50 < riga 896"
                    action = "sell"

          
            
            
            
            ################################################################################################################################## 24-40 min

            # VENDITA - da 24 a 40 minuti = da 1080 a 1800 secondi

            elif seconds_since_last_trade > 1440 and seconds_since_last_trade <= 2400:

            
                if (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell < -0.20 
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL 24 (24-40 min) con ma50 > riga 917"
                    action = "sell"
                
                
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    and deviation_sell > 0.29 and deviation_sell < 0.60
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL 25 (24-40 min) con ma50 > riga 929"
                    action = "sell"
                
                
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma23_prev and ma3_last < ma23_last) 
                    and deviation_sell > 0.61
                 
                ):
                    sell = "SELL 26 (24-40 min) con ma50 > riga 940"
                    action = "sell"

                
                
                
                
                ##################################################################### con trend discendente
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last) 
                    and deviation_sell < -0.16
                  
                ):
                    sell = "SELL 27 (24-40 min) con ma50 < riga 955"
                    action = "sell"
                
                
                # --------------------------------------------------------------------------------------crollo
                
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last) 
                    and deviation_sell > 0.23
                   
                ):
                    sell = "SELL 28 (24-40 min) con ma50 < riga 969"
                    action = "sell"

                    
                    
            ##############################################################################################################################     > 40 min
            
            
            # VENDITA - da 40 minuti in poi = da 2400 secondi in poi

            elif seconds_since_last_trade > 2400:

                if (
                    ma50_last > ma50_2_min_ago 
                    and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                    and deviation_sell < -0.25
                   
                ):
                    sell = "SELL 29 ( dopo 40 min ) con ma50 > ( -0.20 con ma3-ma78 ) - riga 987"
                    action = "sell"
                
                
                
                elif (
                    ma50_last > ma50_2_min_ago 
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell > 0.29 and deviation_sell < 0.59
                  
                ):
                    sell = "SELL 30 ( dopo 40 min ) con ma50 > - ( 0.29 -0.59 con ma3-ma39 ) - riga 998"
                    action = "sell"
                
                
                
                elif (
                    ma50_last > ma50_2_min_ago 
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last) 
                    and deviation_sell > 0.60
                 
                ):

                    sell = "SELL 31 ( dopo 40 min ) con ma50 > ( >0.60 con ma3-ma39 ) - riga 1010"
                    action = "sell"
                    
                    # ma3-39 mi evita la ricompra e la rivendita con perdita !
                   
            
            
            
                ######################################################################################## con trend discendente
              
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last) 
                    and deviation_sell < -0.16
                   
                ):
                    sell = "SELL 32 ( dopo 40 min ) con ma50 < riga 1027"
                    action = "sell"

                    
            
                # qui non ho messo il crollon perche' dopo 40 min o gia' ha venduto o e' gia' risalita
              
            
            ###########################################################################################################################
            
            

            
           # VEDI 399 LE HO GIA' MESSE LI LE VENDITE ECCEZIONALI
            
            # salvagente SOLO mentre sale ! altrimenti va in conflitto con il buy durante il crollo

            # 1) STOP LOSS (salvagente)

            
            if (
                ma50_last >= ma50_2_min_ago 
                and (ma3_prev > ma18_prev and ma3_last < ma18_last) 
                and deviation_sell < -0.68
             
            ):
                sell = "SALVAGENTE 1 riga 1053"
                action = "sell"

                
                
                
            elif (
                ma50_last >= ma50_2_min_ago 
                and (ma3_prev > ma36_prev and ma3_last < ma36_last) 
                and deviation_sell < -0.63
               
            ):
                sell = "SALVAGENTE 2 riga 1065"
                action = "sell"

           
            
                
            ##########################################################################################################################

            
          
            
            # 2) ro cano VENDE " DOPO x MINUTI " and...

            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds 
                and (ma2_prev > ma78_prev and ma2_last < ma78_last) 
                and deviation_sell < -0.50
              
            ):

                sell = "SELL TEMPO 1 riga 1086"
                action = "sell"
                
                
                
                
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds 
                and ma8_last < ma39_last
                and deviation_sell < -0.35
              
            ):

                sell = "SELL TEMPO 2 riga 1099"
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
        ##
        
        # ave comparo meo !
        # attenzione vende dopo 6 min con le condizioni della fascia > 40 min ! vediamo...
        
