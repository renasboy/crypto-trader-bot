                # incrocio 39-78 per risolvere il problema trend laterale - MA.per adesso, solo sul buy 1
                # TOGLIERE IL RUMORE, compa !
                
                # ti voglio bene, compa.                                     
                # compa, compa caro !                                          
                # Tom Petty - Something Good Coming
                ###################################                23 ottobre 2021 funziona 0re 18-40

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
        
        ma28_last, ma28_prev = self.algo_helper.ma_last_prev(28)
        
        ma30_last, ma30_prev = self.algo_helper.ma_last_prev(30)
        ma33_last, ma33_prev = self.algo_helper.ma_last_prev(33)
        ma36_last, ma36_prev = self.algo_helper.ma_last_prev(36)
        ma39_last, ma39_prev = self.algo_helper.ma_last_prev(39)
        ma40_last, ma40_prev = self.algo_helper.ma_last_prev(40)
        ma47_last, ma47_prev = self.algo_helper.ma_last_prev(47)
        ma48_last, ma48_prev = self.algo_helper.ma_last_prev(48)
        
        ma50_last, ma50_prev = self.algo_helper.ma_last_prev(50)
        ma78_last, ma78_prev = self.algo_helper.ma_last_prev(78)
        ma100_last, ma100_prev = self.algo_helper.ma_last_prev(100)
        
        
        
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
        # formula DEVIATION_1_gabbia
        deviation_1_gabbia = (ma8_last/ma39_last - 1) * 100 if ma39_last else 0
        self.algo_helper.log("deviation_1_gabbia: {}".format(deviation_1_gabbia))
        
        
        # formula DEVIATION_2_gabbia
        deviation_2_gabbia = (ma8_last/ma50_last - 1) * 100 if ma50_last else 0
        self.algo_helper.log("deviation_2_gabbia: {}".format(deviation_2_gabbia))
        
       
        ##################################################################################################################  
        
        # formula deviation
        deviation = (ma2_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.log("deviation: {}".format(deviation))
        
        ##################################################################################################################
        
        ################################################################ deviation per comprare
        
        # formula DEVIATION_buy1 per la compra 1
        deviation_buy1 = (ma13_last/ma39_last - 1) * 100 if ma39_last else 0
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
        
        
        
        ######################################################################################## deviation per vendere
        
        
        # formula DEVIATION_sell 
        deviation_sell = (ma3_last/last_trade_price - 1) *100 if last_trade_price else 0
        self.algo_helper.log("deviation_sell: {}".format(deviation_sell))   
        
        # formula DEVIATION_sell_ma78
        deviation_sell_ma78 = (ma4_last/ma78_last - 1) *100 if ma78_last else 0
        self.algo_helper.log("deviation_sell_ma78: {}".format(deviation_sell_ma78))
        
        # formula deviation_ma39 per vendere un po' piu' giu' di ma39
        deviation_ma39 = (ma3_last/ma39_last - 1) * 100 if ma39_last else 0
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
        
        if deviation_1_gabbia > -0.50 and deviation_2_gabbia > -0.50 or deviation_buy_crollo_1 < -1.90:
          
            # deviation_1_gabbia = ma8_last / ma39_last
            # deviation_2_gabbia = ma8_last / ma50_last
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
              
                #------------------------------------------------------------ BUY 1 DURANTE IL RIALZO con INCROCIO CLASSICO 78-100 
                
                
                
                if (
                    ma13_last > ma78_last
                    and (ma78_prev < ma100_prev and ma78_last > ma100_last)      
                    
                    and ma2_last > ma2_2_min_ago
                    and ma4_last > ma8_last
                    
                  
                ):

                    buy="BUY 1 con incrocio 39-78 and INCROCIO CLASSICO 39-50 riga 300"
                    action="buy"
                
                    
                
                
                #--------------------------------------------------------------    BUY 1 DURANTE IL RIALZO con LA DEVIATION BUY 1
                
                
                elif (
                    deviation_buy1 > 0.56
                    and (ma39_prev < ma78_prev and ma39_last > ma78_last)
                    
                    and ma78_last > ma78_2_min_ago
                    
                    
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma4_last > ma4_2_min_ago
                  
                ):  
                  
                    buy = "BUY 1 con incrocio 39-78 and DEVIATION BUY 1 e ma78> riga 322"
                    action = "buy"
                    
                
                    # deviation_buy1 = ma13_last/ma39_last
               
               
                ####################################################################
                
                
                elif (
                   
                    ma78_last < ma78_2_min_ago
                    and (ma39_prev < ma78_prev and ma39_last > ma78_last)
                    and deviation_buy1 > 0.14
                    
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma4_last > ma4_2_min_ago
                  
                ):

                    buy = "BUY 1 con incrocio 39-78 and DEVIATION BUY 1 e ma78 < riga 344"
                    action = "buy"
                    
                    #deviation_buy1 = ma13_last/ma39_last
                    
               
                elif (
                   
                    ma78_last < ma78_2_min_ago
                    
                    and (ma39_prev < ma78_prev and ma39_last > ma78_last) 
                    
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma4_last > ma4_2_min_ago
                  
                ):

                    buy = "se ma78 < - BUY 1 con incrocio 39-78 - riga 362"
                    action = "buy"
                    
                    
                    #deviation_buy1 = ma13_last/ma39_last
                    
                    
                
                ##############################################################################
                
               
                
                # BUY 1 DURANTE IL RIALZO con COMPRA_SPAZIO_TEMPO
                if (
                    compra_spazio_tempo > 0.70
                    and ma3_last > ma33_last
                    and (ma39_prev < ma78_prev and ma39_last > ma78_last)
                    
                  
                    # compra_spazio_tempo = ma3_last / ma3_3_min_ago
                    # QUESTA CONDIZIONE SPAZIO-TEMPO ERA UNA TUA IDEA !
                    # questa condizione e' molto molto rischiosa ! vedi un po'
                ):

                    buy = "BUY 1 con incrocio 47-78 and COMPRA_SPAZIO_TEMPO > 0.70 riga 386"
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
                    buy = "BUY DURANTE IL CROLLO - modo 1 riga 404"
                    action = "buy"
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                
                
                
                
                # BUY  SECONDO MODO - DURANTE IL CROLLO
                elif (    
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -2.40
                    and deviation_buy_crollo_2 > 0.39
                         
                ):
                    buy = "BUY DURANTE IL CROLLO - modo 2 riga 419"
                    action = "buy"
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_buy_crollo_2 = ma3_last / ma13_last
            
            
            ############################################################################################################

            #############################################################################################################      COMPRA sessione 2

            elif self.session == 2:
              
                if (
                    deviation_buy2 > 0.07
                    and deviation_buy_ma3_sopra_ma13 > 0.09
                    and deviation_ma7_sopra_ma40 > 0.08
                   
                    and ma2_last > ma2_2_min_ago
                    and price > price_2_min_ago
                    and ma3_last > ma40_last
                    
                ):
                    buy = "BUY 2A riga 442"
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
                    buy = "BUY 2B riga 462"
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
                    buy = "BUY 3A riga 482"
                    action = "buy"    
                        
                    
                    

                elif (
                
                    deviation_buy3 > 0.02
                    and delta_buy3_incrocio_ma3_ma8 > 0.06
                    and deviation_ma4_sopra_ma30 > 0.18
                    
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago 
               
                ):
                    buy = "BUY 3B RIVOLUZIONARIO - riga 499"
                    action = "buy"
                    
                  
                    # deviation_buy3 = ma4_last/ma30_last
                    
                    
                    
                    
        ############################################################################################################
        
                                                     #  V E N D I T A !
          
        ############################################################################################################
        

        # NON TOCCARE QUESTA RIGA (DICE CHE STA IN MODO SELL, DEVO VENDERE !)
      
        elif last_trade_action == "buy":
          
          
            
        #####################################################################################################################
                  
            
            # VENDITA CON QUESTE 3 ECCEZIONI !
            # altre VENDITE ECCEZIONALI LE HO GIA' MESSE SOTTO - verifica e poi cancella !
            # A T T E N Z I O N E ! salvagente SOLO mentre sale ! altrimenti va in conflitto con il buy durante il crollo - RIFLETTI SU QUESTA FRASE...
                  
            # 1) ro cano VENDE CON UN SALVAGENTE
          
            if (
                deviation_ma39 < -0.24
                and ma50_last < ma50_2_min_ago
            ):
              
                sell = "SELL SALVAGENTE 3-39 con ma50 < riga 534"
                action = "sell"
                  
                # deviation_ma39 = ma3_last / ma39_last  
                
                
            
                  
            # 2) ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA

            elif (
                seconds_since_last_trade > max_hold_time_in_seconds 
                and ma2_last < last_trade_price 
                and deviation < -0.37
                and ma78_last < ma78_2_min_ago
            
            ):
                
                sell = "SELL DOLCE ATTESA - riga 553"
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

                    sell = "con VENDI_SPAZIO_TEMPO riga 571"
                    action = "sell"
                
           

          ###################################################################################################################################
          
          ###################################################################################################################################

            # VENDITA - con fasce di tempo ! c'e' vita su marte !

            #    minuti
            #   0 -  3 
            #   3 -  5 -
            #   5 - 12 -
            #  12 - 24 -
            #  24 - 40 -
            #  40   60
            #  > 60

            #############################################################################################################################
            
            ##############################################################################################################################
             
            # Tom Petty - Something Good Coming
            
            
            # < -0.10  ma78 che mi salva (nel movimento laterale mi fa perdere la meta')
            # < -0.20
            # 0.25 - 0.59
            # 0.60 - 0.79
            # 0.80 - 1.20
            # > 1.21
            ####################################################################################################################### 0 - 3 min
            
            
            
            
            # la deviation_sell_ma78 mi protegge - (ogni volta che c'e' stato un rialzo la ma3 non l' ha mai toccata !)
            # e l' incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde ! e mi protegge anche questa quando ma78 sta molto in alto !
            
            
            # VENDITA - da 0 a 3 minuti = da 0 a 180 secondi
                  
            if seconds_since_last_trade > 0 and seconds_since_last_trade <= 180:
                
                # con ma50 >
                if (
                    ma50_last >= ma50_2_min_ago 
                    and deviation_sell_ma78 < -0.10
                    
                    # deviation_sell_ma78 = ma3_last / ma78_last
                    
                ):
                    sell = "SELL (0-3 min) con ma50 > and deviation_sell_ma78 < -0.10 - riga 625"
                    action = "sell"
                    
                    
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell < -0.23
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (0-3 min) con ma50 > incrocio 3-39 and deviation_sell < -0.23 - riga 614"
                    action = "sell"
                
                
                
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    and deviation_sell > 0.25 and deviation_sell < 0.60
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (0-3 min) con ma50 > incrocio 3-33 and deviation_sell 0.25 - 0.60 - riga 649"
                    action = "sell"
                    
                    
              
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last) 
                    and deviation_sell > 0.61 and deviation_sell < 0.79
                 
                ):
                    sell = "SELL (0-3 min) con ma50 > incrocio 3-33 and deviation_sell 0.61 - 0.79 - riga 661"
                    action = "sell"
                    
                    
                    
                    
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma13_prev and ma3_last < ma13_last) 
                    and deviation_sell > 0.80 and deviation_sell < 1.20
                   
                ):

                    sell = "SELL (0-3 min) con ma50 > incrocio 3-13 and deviation_sell 0.80 - 1.20 - riga 674"
                    action = "sell"
                    
                    
                    
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma11_prev and ma3_last < ma11_last) 
                    and deviation_sell > 1.21
               
                ):

                    sell = "SELL (0-3 min) con ma50 > incrocio 3-11 and deviation_sell > 1.21 - riga 686"
                    action = "sell"
                 
                
                
                
                ###########################################################################     trend in ribasso
             
               
                elif (
                    ma50_last < ma50_2_min_ago 
                    and deviation_sell_ma78 < -0.15
                    and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                  
                    # deviation_sell_ma78 = ma4_last / ma78_last
                ):
                    sell = "SELL (0-3 min) con ma50 < and deviation_sell_ma78 < -0.10 and incrocio 3-28- riga 702"
                    action = "sell"
                    
                    # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                    
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last) 
                    and deviation_sell < -0.23
                   
                ):
                    sell = "SELL (0-3 min) con ma50 < incrocio 3-33 and deviation_sell -0.23 - riga 715"
                    action = "sell"
                    
                    
                    
                # ---------------------------------------------------------------------------------------------------------------------- crollo   
                
                
              
              
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma16_prev and ma3_last < ma16_last) 
                    and deviation_sell < -0.50
                   
                ):
                    sell = "SELL CROLLO (0-3 min) con ma50 < incrocio 3-16 and deviation_sell < -0.50 - riga 731"
                    action = "sell"
                    
                    # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                
                
               
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma23_prev and ma3_last < ma23_last) 
                    and deviation_sell > 0.23
                   
                ):
                    sell = "SELL CROLLO (0-3 min) con ma50 < incrocio 3-23 and deviation_sell > 0.23 - riga 744"
                    action = "sell"
                  
              
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma8_prev and ma3_last < ma8_last) 
                    and deviation_sell > 0.60
                   
                ):

                    sell = "SELL CROLLO (0-3 min) con ma50 < incrocio 3-8 and deviation_sell > 0.60 - riga 756"
                    action = "sell"
                
                  
            
            
            
            ################################################################################################################################         3-5 min
            
            
            # VENDITA - da 3 a 5 minuti = da 180 a 300 secondi

            elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 300:
              
              
                if (
                    ma50_last >= ma50_2_min_ago 
                    and deviation_sell_ma78 < -0.10
                    
                    # deviation_sell_ma78 = ma4_last / ma78_last
                
                ):
                    sell = "SELL (3-5 min) con ma50 > and deviation_sell_ma78 < -0.10 - riga 778"
                    action = "sell"
                    
                
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell < -0.24
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (3-5 min) con ma50 > incrocio 3-39 and deviation_sell < -0.24 - riga 790"
                    action = "sell"
                
                
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    and deviation_sell > 0.25 and deviation_sell < 0.60
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (3-5 min) con ma50 > incrocio 3-33 and deviation_sell 0.25 - 0.60 - riga 802"
                    action = "sell"
                    
                    
              
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last) 
                    and deviation_sell > 0.61 and deviation_sell < 1.20
                 
                ):
                    sell = "SELL (3-5 min) con ma50 > incrocio 3-33 and deviation_sell 0.61 - 1.20 - riga 814"
                    action = "sell"
                    
                    
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma25_prev and ma3_last < ma25_last) 
                    and deviation_sell > 1.21
                 
                ):
                    sell = "SELL (3-5 min) con ma50 > incrocio 3-25 and deviation_sell > 1.21 - riga 824"
                    action = "sell"
                    
                    
                ###########################################################################     trend in ribasso
                
               
                elif (
                    ma50_last < ma50_2_min_ago 
                    and deviation_sell_ma78 < -0.15
                    and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                    
                    # deviation_sell_ma78 = ma3_last / ma78_last
                ):
                    sell = "SELL (3-5 min) con ma50 < and deviation_sell_ma78 < -0.10 and incrocio 3-28 - riga 838"
                    action = "sell"
                    
                    # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                    
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last) 
                    and deviation_sell < -0.23
                   
                ):
                    sell = "SELL (3-5 min) con ma50 < incrocio 3 - 33 and deviation_sell < -0.23 - riga 850"
                    action = "sell"
   
         
                # ---------------------------------------------------------------------------------------------------------------------- guadagno con crollo
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma23_prev and ma3_last < ma23_last) 
                    and deviation_sell > 0.23
                   
                ):
                    sell = "SELL GUADAGNO CON CROLLO (3-5 min) con ma50 < incrocio 3- 23 and deviation_sell > 0.23 - riga 863"
                    action = "sell"

             
                

            ################################################################################################################################### 5-12 min
            
                  
            
            # VENDITA - da 5 a 12 minuti = da 300 a 720 secondi

            
            elif seconds_since_last_trade > 300 and seconds_since_last_trade <= 720:
           
                if (
                    ma50_last >= ma50_2_min_ago 
                    and deviation_sell_ma78 < -0.10
                    
                    # deviation_sell_ma78 = ma4_last / ma78_last
                
                ):
                    sell = "SELL (5-12 min) con ma50 > and deviation_sell_ma78 < -0.10 - riga 885"
                    action = "sell"
                  
                  
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell < -0.25
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (5-12 min) con ma50 > incrocio 3 - 39 and deviation_sell < -0.25 - riga 896"
                    action = "sell"
                    
                
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    and deviation_sell > 0.25 and deviation_sell < 0.60
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (5-12 min) con ma50 > incrocio 3 - 33 and deviation_sell 0.25 - 0.60 - riga 908"
                    action = "sell"
                
                
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    and deviation_sell > 0.61 and deviation_sell < 1.20
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (5-12 min) con ma50 > incrocio 3 - 33 and deviation_sell 0.61 - 1.20 - riga 920"
                    action = "sell"
                    
              
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma25_prev and ma3_last < ma25_last) 
                    and deviation_sell > 1.21
                 
                ):
                    sell = "SELL (5-12 min) con ma50 > incrocio 3 - 25 and deviation_sell > 1.21 - riga 931"
                    action = "sell"
                    
                
                ###########################################################################     trend in ribasso
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and deviation_sell_ma78 < -0.15
                    and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                    
                    # deviation_sell_ma78 = ma4_last / ma78_last
                ):
                    sell = "SELL 12 (5-12 min) con ma50 < and deviation_sell_ma78 < -0.10 and incrocio 3-28 - riga 945"
                    action = "sell"
                    
                    # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                    
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last) 
                    and deviation_sell < -0.24
                   
                ):
                    sell = "SELL (5-12 min) con ma50 < incrocio 3- 33 and deviation_sell < -0.24 - riga 956"
                    action = "sell"
   
                
                
                # ------------------------------------------------------------------------------- eventuale guadagno con crollo
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma23_prev and ma3_last < ma23_last) 
                    and deviation_sell > 0.23
                   
                ):
                    sell = "SELL eventuale guadagno con crollo (5-12 min) con ma50 <  incrocio 3 -23 - riga 970"
                    action = "sell"

             
                
            ############################################################################################################################    12-24 min

            
            # VENDITA - da 12 a 24 minuti = da 720 a 1440 secondi

       
            elif seconds_since_last_trade > 720 and seconds_since_last_trade <= 1440:
          
                
                if (
                    ma50_last >= ma50_2_min_ago 
                    and deviation_sell_ma78 < -0.10
                    
                    # deviation_sell_ma78 = ma4_last / ma78_last
                
                ):
                    sell = "SELL (12-24 min) con ma50 > and deviation_sell_ma78 < -0.10 - riga 991"
                    action = "sell"
                  
                  
                  
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell < -0.30
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (12-24 min) con ma50 > incrocio 3 - 39 and deviation_sell < -0.30 - riga 1003"
                    action = "sell"
                
                
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    and deviation_sell > 0.25 and deviation_sell < 0.60
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (12-24 min) con ma50 > incrocio 3 - 33 and deviation_sell 0.25 - 0.60 - riga 1015"
                    action = "sell"
                
                
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    and deviation_sell > 0.61 and deviation_sell < 1.20
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (12-24 min) con ma50 > incrocio 3 - 33 and deviation_sell 0.61 - 1.20 - riga 1027"
                    action = "sell"
                    
                
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last) 
                    and deviation_sell > 1.21
                 
                ):
                    sell = "SELL (12-24 min) con ma50 > incrocio 3 - 39 and deviation_sell > 1.21 - riga 1038"
                    action = "sell"

                
                
                
                
                ##################################################################### con trend discendente
                
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and deviation_sell_ma78 < -0.20
                    # deviation_sell_ma78 = ma4_last / ma78_last
                ):
                    sell = "SELL (5-12 min) con ma50 < and deviation_sell_ma78 < -0.10 - riga 1054"
                    action = "sell"
                
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last) 
                    and deviation_sell < -0.25
                  
                ):
                    sell = "SELL (12-24 min) con ma50 < incrocio 3- 33 and deviation_sell < -0.25 - riga 1065"
                    action = "sell"
                
                
                
                
                
                # -----------------------------------------------------------------------------eventuale guadagno con crollo
                
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last) 
                    and deviation_sell > 0.23
                   
                ):
                    sell = "SELL eventuale guadagno con crollo (12-24 min) con ma50 < incrocio 3 - 18 and deviation_sell > 0.23 - riga 1082"
                    action = "sell"

          
            
            
            
            ################################################################################################################################## 24-60 min
            

            # VENDITA - da 24 a 60 minuti = da 1080 a 3600 secondi

            elif seconds_since_last_trade > 1440 and seconds_since_last_trade <= 3600:
                
                
                if (
                    ma50_last >= ma50_2_min_ago 
                    and deviation_sell_ma78 < -0.15
                    
                    # deviation_sell_ma78 = ma4_last / ma78_last
                
                ):
                    sell = "SELL (24-60 min) con ma50 > and deviation_sell_ma78 < -0.15 - riga 1104"
                    action = "sell"
                    
                
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell < -0.26 
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (24-60 min) con ma50 > incrocio 3- 39 and deviation_sell < -0.26 - riga 1116"
                    action = "sell"
                
                
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell > 0.30 and deviation_sell < 0.60
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (24-60 min) con ma50 > incrocio 3- 39 and deviation_sell 0.30 - 0.60 - riga 1128"
                    action = "sell"
                
                
                
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell > 0.61 and deviation_sell < 1.20
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (24-60 min) con ma50 > incrocio 3- 39 and deviation_sell 0.61 - 1.20 - riga 1140"
                    action = "sell"
                    
                    
                    
                elif (
                    ma50_last >= ma50_2_min_ago 
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last) 
                    and deviation_sell > 1.21
                 
                ):
                    sell = "SELL (24-60 min) con ma50 > incrocio 3- 39 and deviation_sell > 1.21 - riga 1151"
                    action = "sell"

                
                
                
                
                ##################################################################### con trend discendente
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and deviation_sell_ma78 < -0.21
                  
                    # deviation_sell_ma78 = ma4_last / ma78_last
                ):
                    sell = "SELL (24-60 min) con ma50 < and deviation_sell_ma78 < -0.21 - riga 1167"
                    action = "sell"
                    
                    
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last) 
                    and deviation_sell < -0.25
                  
                ):
                    sell = "SELL (24-60 min) con ma50 < incrocio 3- 33 and deviation_sell < -0.25 - riga 1177"
                    action = "sell"
                    
                    
                    
                
                
                # --------------------------------------------------------------------------------------eventuale guadagno durante il crollo
                
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last) 
                    and deviation_sell > 0.23
                   
                ):
                    sell = "SELL eventuale guadagno durante il crollo (24-60 min) con ma50 < incrocio 3 - 18 and deviation_sell > 0.23 - riga 1194"
                    action = "sell"

                    
            
            
            
            
            
            ##############################################################################################################################     > 60 min
            
            
            # VENDITA - da 60 minuti in poi = da 3600 secondi in poi

            elif seconds_since_last_trade > 3600:
                
                
                
                if (
                    ma50_last >= ma50_2_min_ago 
                    and deviation_sell_ma78 < -0.20
                    
                    # deviation_sell_ma78 = ma4_last / ma78_last
                
                ):
                    sell = "SELL dopo 60 min con ma50 > and deviation_sell_ma78 < -0.20 - riga 1219"
                    action = "sell"
                    
                
                
                elif (
                    ma50_last > ma50_2_min_ago 
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell < -0.30
                   
                ):
                    sell = "SELL dopo 60 min con ma50 > incrocio 3 - 39 and deviation_sell < -0.25 - riga 1230"
                    action = "sell"
                
                
                
                elif (
                    ma50_last > ma50_2_min_ago 
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell > 0.35 and deviation_sell < 0.79
                  
                ):
                    sell = "SELL dopo 60 min con ma50 > incrocio 3 - 39 and deviation_sell 0.35 - 0.79 - riga 1019"
                    action = "sell"
                
                
                
                
                elif (
                    ma50_last > ma50_2_min_ago 
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last) 
                    and deviation_sell > 0.80 and deviation_sell < 2.49
                 
                ):

                    sell = "SELL dopo 60 min con ma50 > incrocio 3 - 39 and deviation_sell 0.80 - 2.49 - riga 1254"
                    action = "sell"
                    
                    # ma 3-48 mi evita la ricompra e la rivendita con perdita ! 
                
                
                
                
                elif (
                    ma50_last > ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last) 
                    and deviation_sell > 2.50
                 
                ):

                    sell = "SELL dopo 60 min con ma50 > incrocio 3 - 33 and deviation_sell > 2.50 - riga 1269"
                    action = "sell"
                    
            
            
            
                ######################################################################################## con trend discendente
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and deviation_sell_ma78 < -0.20
                  
                    # deviation_sell_ma78 = ma4_last / ma78_last
                ):
                    sell = "SELL dopo 60 min con ma50 < and deviation_sell_ma78 < -0.17 - riga 1284"
                    action = "sell"
                    
                
                
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last) 
                    and deviation_sell < -0.25
                   
                ):
                    sell = "SELL dopo 60 min con ma50 < con incrocio 3 - 33 and deviation_sell < -0.25 - riga 1295"
                    action = "sell"

                    
                
                
                
                # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
              
            
            ###########################################################################################################################
            
            
           
          
           # A T T E N Z I O N E !     altre  VENDITE ECCEZIONALI 
           
            # ro cano VENDE " DOPO x MINUTI " and...

            
            if (
                seconds_since_last_trade > max_hold_time_in_seconds 
                and (ma2_prev > ma78_prev and ma2_last < ma78_last) 
                and deviation_sell < -0.48
              
            ):

                sell = "SELL TEMPO 1 e con incrocio 2 - 78 and deviation_sell < -0.48 - riga 1322"
                action = "sell"
                
            #############################################################################################
                
                
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds 
                and ma8_last < ma39_last
                and deviation_sell < -0.31
              
            ):

                sell = "SELL TEMPO 2 e se ma8 < ma39 and deviation_sell < -0.31 - riga 1335"
                action = "sell"
            
           
            #################################################################################################
            
           
            
                                                     ############### FINE ALGORITH ###################
            
            

        self.algo_helper.log("action {}".format(action))

        if action == "sell":
            self.algo_helper.log("action sell {}".format(sell))
            self.session += 1
            
        elif action == "buy":
            self.algo_helper.log("action buy {}".format(buy))

        return action
      
      
        # compa, compa caro !
        # ave comparo meo !
        
        
        # AGAINST THE WIND - Bob Seger & Jason Aldean
        
