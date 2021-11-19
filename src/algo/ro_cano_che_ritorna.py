    # CCR = MADDOG                           # 17 NOVEMBRE 2021 - funziona MA PROBLEMI SUL COINBASE - realizza solo il buy 1 poi si blocca !
             
class ro_cano_che_ritorna:
    def __init__(self, helper, buy_percentage, sell_percentage):
        self.algo_helper = helper
        self.buy_percentage = buy_percentage
        self.sell_percentage = sell_percentage
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
        ma15_last, ma15_prev = self.algo_helper.ma_last_prev(15)
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
        ma45_last, ma45_prev = self.algo_helper.ma_last_prev(45)
        ma47_last, ma47_prev = self.algo_helper.ma_last_prev(47)
        ma48_last, ma48_prev = self.algo_helper.ma_last_prev(48)
        ma50_last, ma50_prev = self.algo_helper.ma_last_prev(50)
        ma72_last, ma72_prev = self.algo_helper.ma_last_prev(72)
        ma78_last, ma78_prev = self.algo_helper.ma_last_prev(78)
        ma100_last, ma100_prev = self.algo_helper.ma_last_prev(100)
        ma200_last, ma100_prev = self.algo_helper.ma_last_prev(200)
         
         
        # moving average (2-3-4-5-7-8-20-43-100) di x minuti prima 
        ma2_2_min_ago = self.algo_helper.ma_minutes_ago(2, 2)
        ma2_3_min_ago = self.algo_helper.ma_minutes_ago(2, 3)
        ma2_4_min_ago = self.algo_helper.ma_minutes_ago(2, 4)
        ma3_2_min_ago = self.algo_helper.ma_minutes_ago(3, 2)
        ma3_3_min_ago = self.algo_helper.ma_minutes_ago(3, 3)
        ma4_2_min_ago = self.algo_helper.ma_minutes_ago(4, 2)
        ma5_2_min_ago = self.algo_helper.ma_minutes_ago(5, 2)
        ma4_4_min_ago = self.algo_helper.ma_minutes_ago(4, 4)
        ma6_2_min_ago = self.algo_helper.ma_minutes_ago(6, 2)
        ma8_4_min_ago = self.algo_helper.ma_minutes_ago(8, 4)
        ma13_2_min_ago = self.algo_helper.ma_minutes_ago(13, 2)
        ma25_2_min_ago = self.algo_helper.ma_minutes_ago(25, 2)
        ma33_5_min_ago = self.algo_helper.ma_minutes_ago(33, 5)
        ma39_2_min_ago = self.algo_helper.ma_minutes_ago(39, 2)
        ma39_3_min_ago = self.algo_helper.ma_minutes_ago(39, 3)
        ma50_2_min_ago = self.algo_helper.ma_minutes_ago(50, 2)
        ma78_2_min_ago = self.algo_helper.ma_minutes_ago(78, 2)
        ma78_4_min_ago = self.algo_helper.ma_minutes_ago(78, 4)
        ma78_5_min_ago = self.algo_helper.ma_minutes_ago(78, 5)
        ma78_7_min_ago = self.algo_helper.ma_minutes_ago(78, 7)
        ma200_3_min_ago = self.algo_helper.ma_minutes_ago(200, 3)
        

        
        # LAST TRADE
        last_trade_action = self.algo_helper.last_trade_action
        last_trade_price = self.algo_helper.last_trade_price
        seconds_since_last_trade = self.algo_helper.seconds_since_last_trade
        
        
        # PREV TRADE
        prev_trade_action = self.algo_helper.prev_trade_action
        prev_trade_time = self.algo_helper.prev_trade_time
        prev_trade_price = self.algo_helper.prev_trade_price
        seconds_since_prev_trade = self.algo_helper.seconds_since_prev_trade
        
        
        # PREZZO DI ADESSO (di mercato) - CURRENT PRICE
        price = self.algo_helper.price

        
        # PREZZO di X MINUTI FA (di mercato)
        price_2_min_ago = self.algo_helper.price_minutes_ago(2)
        price_10_min_ago = self.algo_helper.price_minutes_ago(10)
        price_15_min_ago = self.algo_helper.price_minutes_ago(15)
        price_20_min_ago = self.algo_helper.price_minutes_ago(20)
        
        

        ###########################################################################################################################      TEMPO
        ########################################################################################################################### 

        # importante : dolce attesa 

        # VENDE DOPO x SECONDI - ro cano torna a casa - (ma c'e' anche un "e se")
        max_hold_time_in_seconds = 360
        #  6 minuti * 60 = 360

        ###########################################################################################################################
        ###########################################################################################################################
        
        

        #                                                         T U T T E    L E   D E V I A T I O N  !

        ##############################################################################################################
        ##############################################################################################################
        
        
        # formula DEVIATION_1_gabbia
        deviation_1_gabbia = (ma8_last / ma50_last - 1) * 100 if ma50_last else 0
        self.algo_helper.info("deviation_1_gabbia: {}".format(deviation_1_gabbia))

        

        # formula deviation
        deviation = (ma3_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.info("deviation: {}".format(deviation))
        
        
        
        ##################################################################################################################
        ################################################################################################################## deviation per comprare
        
        # formula DEVIATION_buy1 per la compra 1
        deviation_buy1 = (ma13_last / ma39_last - 1) * 100 if ma39_last else 0
        self.algo_helper.info("deviation_buy1: {}".format(deviation_buy1))

        # formula DEVIATION_buy2 per la compra 2
        deviation_buy2 = (ma8_last / ma50_last - 1) * 100 if ma50_last else 0
        self.algo_helper.info("deviation_buy2: {}".format(deviation_buy2))

        # formula DEVIATION_buy3 per la compra 3
        deviation_buy3 = (ma4_last / ma30_last - 1) * 100 if ma30_last else 0
        self.algo_helper.info("deviation_buy3: {}".format(deviation_buy3))

        # ------------------------------------------------------------------------------------------------------------

        # formula delta_buy3_incrocio_ma3_ma8 > 0.10 ( per la compra 3 )
        delta_buy3_incrocio_ma3_ma8 = (ma3_last / ma8_last - 1) * 100 if ma8_last else 0
        self.algo_helper.info("delta_buy3_incrocio_ma3_ma8: {}".format(delta_buy3_incrocio_ma3_ma8))
       
        # formula DEVIATION_buy per comprare UN PO' PIU' SOPRA DEL LAST TRADE ( di solito l' ultimo SELL )
        deviation_buy = (ma2_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.info("deviation_buy: {}".format(deviation_buy))    
        
        
        
        ###########################################################################################    DEVIATION_buy_crollo
        ###########################################################################################

        # formula DEVIATION_buy_crollo_1 per comprare a una certa distanza da ma78
        deviation_buy_crollo_1 = (ma8_last / ma78_last - 1) * 100 if ma78_last else 0
        self.algo_helper.info("deviation_buy_crollo_1: {}".format(deviation_buy_crollo_1))
            
        

        # formula DEVIATION_buy_crollo_2 per comprare a una certa distanza da ma13
        deviation_buy_crollo_2 = (ma3_last / ma13_last - 1) * 100 if ma13_last else 0
        self.algo_helper.info("deviation_buy_crollo_2: {}".format(deviation_buy_crollo_2))
            
        
        ##############################################################################################
        ##############################################################################################
        

        # formula DEVIATION_buy_ma3_sopra_ma13 per comprare a una certa distanza da ma13
        deviation_buy_ma3_sopra_ma13 = (ma3_last / ma13_last - 1) * 100 if ma13_last else 0
        self.algo_helper.info("deviation_buy_ma3_sopra_ma13: {}".format(deviation_buy_ma3_sopra_ma13))    
        

        # formula DEVIATION_ma4_sopra_ma30
        deviation_ma4_sopra_ma30 = (ma4_last / ma30_last - 1) * 100 if ma30_last else 0
        self.algo_helper.info("deviation_ma4_sopra_ma30: {}".format(deviation_ma4_sopra_ma30))
            
        # formula DEVIATION_ma13_sopra_ma25
        deviation_ma13_sopra_ma25 = (ma13_last / ma25_last - 1) * 100 if ma25_last else 0
        self.algo_helper.info("deviation_ma13_sopra_ma25: {}".format(deviation_ma13_sopra_ma25))

        # formula deviation_ma7_sopra_ma40
        deviation_ma7_sopra_ma40 = (ma7_last / ma40_last - 1) * 100 if ma40_last else 0
        self.algo_helper.info("deviation_ma7_sopra_ma40: {}".format(deviation_ma7_sopra_ma40))
            
        # formula deviation_ma3_sopra_ma7 (solo per il BUY1)
        deviation_ma3_sopra_ma7 = (ma3_last / ma7_last - 1) * 100 if ma7_last else 0
        self.algo_helper.info("deviation_ma3_sopra_ma7: {}".format(deviation_ma3_sopra_ma7))
            
        

        ########################################################################################################################### deviation per vendere
        
        
        # formula DEVIATION_sell
        deviation_sell = (ma4_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.info("deviation_sell: {}".format(deviation_sell))    
        
        

        # formula DEVIATION_sell_ma78
        deviation_sell_ma78 = (ma4_last / ma78_last - 1) * 100 if ma78_last else 0
        self.algo_helper.info("deviation_sell_ma78: {}".format(deviation_sell_ma78))
        
        
        
        # formula deviation_ma39 per vendere un po' piu' giu' di ma39
        deviation_ma39 = (ma4_last / ma39_last - 1) * 100 if ma39_last else 0
        self.algo_helper.info("deviation_ma39: {}".format(deviation_ma39))
        
        
        ############################################################################################################################
        ############################################################################################################################
        ############################################################################################################################ 
        
        # DEFAULT ACTION DICE DI NON FARE NIENTE (= None, NON TOCCARE )
        action = None
        percentage = 0
        
        ##########################################################################################################################################################
        ##########################################################################################################################################################
        ############################################################################################################################      APRE E CHIUDE LA GABBIA !

        # SI APRE LA GABBIA SE

        if deviation_1_gabbia > -0.39 or deviation_buy_crollo_1 < -1.90:
            # se la gabbia si apre troppo facilmente avrai problemi con andamento laterale ! ( prima deviation_1_gabbia > -0.27 ) vediamo con -0.50 come si comporta.
            # deviation_1_gabbia = ma8_last / ma50_last
            # deviation_buy_crollo_1 = ma8_last / ma78_last

            # NON TOCCARE QUESTA CONDIZIONE ! SERVE PER APERTURA DI GABBIA !
            if not self.session or not self.open:
                self.session = 1
                self.open = True
                self.algo_helper.info("session {}: open segment".format(self.session))

        # SI CHIUDE LA GABBIA SE
        else:
            self.open = False
            self.algo_helper.info("session {}: closed segment".format(self.session))
            
            
          
        ############################################################################################
        ############################################################################################
        ############################################################################################ 
        #############################################################################################################################################

        # COMPRA
        # NON TOCCARE QUESTA RIGA ( DICE CHE STA IN MODO BUY, vuole COMPRARE ! )

        if self.open and self.session and last_trade_action != "buy":

            
                                                                    #   B U Y
            ###########################################################################################################################################
           
            # rialzo improvviso che adesso manca (spazio-tempo) - vedi buy2 durante il crollo ! (e considerare l' aggiunta di 13-25)
            ##################################################################################################################################COMPRA 1

            percentage = self.buy_percentage


            if self.session == 1:

                
                # ------------------------------------------------------------ BUY 1 DURANTE IL RIALZO con INCROCIO CLASSICO 72-100
                if (
                    ma13_last > ma78_last
                    and (ma72_prev < ma100_prev and ma72_last > ma100_last)
                    and ma2_last > ma2_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                    and deviation_ma13_sopra_ma25 > 0.07
                ):

                    buy = "BUY 1 con incrocio 72-100 riga 284"
                    action = "buy"
                    percentage = 50
                    # la deviation_ma13_sopra_ma25 puoi portarla > 0.072 SOLO CON 72-100
                    
                    
               
                # --------------------------------------------------------------    BUY 1 DURANTE IL RIALZO con LA DEVIATION BUY 1
                elif (
                    deviation_buy1 > 0.56
                    and (ma13_prev < ma39_prev and ma13_last > ma39_last)
                    and ma78_last > ma78_2_min_ago
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma4_last > ma4_2_min_ago
                ):
                    buy = "BUY 1 con incrocio 13-39 and DEVIATION BUY 1 ALTA e ma78 > riga 301"
                    action = "buy"
                    percentage = 50

                    # deviation_buy1 = ma13_last/ma39_last
              
              
                ####################################################################  BUY 1 con incrocio 13-100 and ma78_last > ma78_5_min_ago  "MI PIACE!"
                elif (
                    (ma13_prev < ma100_prev and ma13_last > ma100_last)
                    and ma78_last > ma78_4_min_ago
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma3_3_min_ago
                    and ma4_last > ma4_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                    and deviation_ma13_sopra_ma25 > 0.06
                    # quando 13-100 si incrociano price ma2 e ma4 sono gia' in ribasso
                ):
                    buy = "BUY 1 con incrocio 13 - 100 e ma78> 4 min (no 5 min ago !) ago riga 320"
                    action = "buy"
                    percentage = 50
                
                
                ################################################################################################################## compra durante il ribasso
                
                
                ###################################################### se ma78< BUY 1 con incrocio 39-78 and DEVIATION BUY 1 BASSA
                elif (
                    ma78_last < ma78_2_min_ago
                    and (ma39_prev < ma78_prev and ma39_last > ma78_last)
                    and deviation_buy1 > 0.14
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma4_last > ma4_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                ):

                    buy = "BUY 1 con incrocio 39-78 and DEVIATION BUY 1 BASSA e ma78 < riga 339"
                    action = "buy"
                    percentage = 50
                    # deviation_buy1 = ma13_last/ma39_last
                    
              
              
                #############################################################se ma78< BUY 1 con incrocio 39-78
                elif (
                    ma78_last < ma78_2_min_ago
                    and (ma39_prev < ma78_prev and ma39_last > ma78_last)
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma4_last > ma4_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                    and deviation_ma13_sopra_ma25 > 0.05
                ):

                    buy = "se ma78 < - BUY 1 con incrocio 39-78 - riga 357"
                    action = "buy"
                    percentage = 50
                    # deviation_buy1 = ma13_last/ma39_last
                    # and deviation_ma13_sopra_ma25 > 0.05 FONDAMENTALE !
                    
                    
                #################################################################################################
                #################################################################################################
                
                # IMPORTANTISSIMO ! SOLO PER IL BUY 1 - PER  - compa prega per me - ( cruise - david gilmour )
                # entriamo nell' area dell' ipervenduto, compa !
                
                ####################################################################################################      COMPRARE DURANTE IL CROLLO
              
              
                
                # BUY  PRIMO MODO DURANTE IL CROLLO
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -2.30
                    and (ma8_prev < ma25_prev and ma8_last > ma25_last)
                ):
                    buy = "BUY DURANTE IL CROLLO - modo 1 riga 380"
                    action = "buy"
                    percentage = 50
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                
                
                
                # BUY SECONDO MODO - DURANTE IL CROLLO - questa condizione e' entrata in azione ! ( e mi e' sembrata addirittura buona !) 
                # MA METTIAMOLO ALLA PROVA CON deviation_buy_crollo_1 < -1.80 ! (non con -2.40)
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -1.80
                    and deviation_buy_crollo_2 > 0.35
                    
                    # PRIMA ERA COSI'
                    #ma2_last > ma2_2_min_ago
                    #and deviation_buy_crollo_1 < -2.40
                    #and deviation_buy_crollo_2 > 0.35
                ):
                    buy = "BUY DURANTE IL CROLLO - modo 2 riga 400"
                    action = "buy"
                    percentage = 50
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_buy_crollo_2 = ma3_last / ma13_last
                    
               
            #############################################################################################################
            #############################################################################################################      COMPRA sessione 2

            elif self.session == 2:
                
                
                ################################################################# BUY 2A con ma78 >
                if (
                    ma78_last > ma78_5_min_ago
                    and deviation_buy2 > 0.07
                    and deviation_buy_ma3_sopra_ma13 > 0.09
                    and deviation_ma7_sopra_ma40 > 0.09
                    and ma2_last > ma2_2_min_ago
                    and price > price_2_min_ago
                    and ma3_last > ma40_last
                ):
                    buy = "BUY 2A con ma78 > riga 423"
                    action = "buy"
                    percentage = 50
                    # deviation_buy_ma3_sopra_ma13 > x e' fondamentale !
                    # deviation_buy2 = ma8_last/ma50_last
                    
                    
                ################################################################# BUY 2B con ma78 <
                elif (
                    ma78_last < ma78_5_min_ago
                    and deviation_buy2 > 0.07
                    and deviation_buy_ma3_sopra_ma13 > 0.09
                    and deviation_ma7_sopra_ma40 > 0.10
                    and ma2_last > ma2_2_min_ago
                    and price > price_2_min_ago
                    and ma3_last > ma40_last
                ):
                    buy = "BUY 2A con ma78 < riga 440"
                    action = "buy"
                    percentage = 50
                    # deviation_buy_ma3_sopra_ma13 > x e' fondamentale !
                    # deviation_buy2 = ma8_last/ma50_last
                    
                    
                
                ################################################################################### BUY 2C
                elif (
                    deviation_buy2 > 0.13
                    and deviation_buy_ma3_sopra_ma13 > 0.10
                    and deviation_ma7_sopra_ma40 > 0.14
                    and (ma4_prev < ma9_prev and ma4_last > ma9_last)
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma40_last
                    and ma4_last > ma78_last
                ):
                    buy = "BUY 2B riga 458"
                    action = "buy"
                    percentage = 50
                    # deviation_buy2 = ma8_last / ma50
                    
           
            ############################################################################################################COMPRA sessione 3

            elif self.session == 3:
                
                
                
                ############################################################################## BUY 3A con ma78 > 
                if (
                    ma78_last >= ma78_2_min_ago
                    and deviation_buy3 > 0.11
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.10
                    and (ma4_prev < ma9_prev and ma4_last > ma9_last)
                    and ma4_last > ma50_last
                ):
                    buy = "BUY 3A con ma78 > riga 479"
                    action = "buy"
                    percentage = 50
               
                ############################################################################## BUY 3B RIVOLUZIONARIO se ma39 > ma78
                elif (    
                    deviation_buy3 > 0.02
                    and (ma39_prev < ma78_prev and ma39_last > ma78_last)
                    and deviation_buy3 > 0.02
                    and delta_buy3_incrocio_ma3_ma8 > 0.06
                    and deviation_ma4_sopra_ma30 > 0.17
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                ):
                    buy = "BUY 3B RIVOLUZIONARIO se ma39 > ma78- riga 494"
                    action = "buy"
                    percentage = 50
                    # deviation_buy3 = ma4_last/ma30_last
                    # riga 462 potrebbe esserci un problema perche' ho tolto ma78_last >= ma78_2_min_ago. vediamo
                    
               
            
                ################################################################################ BUY 3C RIVOLUZIONARIO se ma78 <
                elif (
                    ma78_last < ma78_2_min_ago
                    and deviation_buy3 > 0.03
                    and deviation_ma13_sopra_ma25 > 0.045
                    and delta_buy3_incrocio_ma3_ma8 > 0.07
                    and deviation_ma4_sopra_ma30 > 0.18
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                    
                ):
                    buy = "BUY 3C RIVOLUZIONARIO se ma78 < - riga 514"
                    action = "buy"
                    percentage = 50
                    # deviation_buy3 = ma4_last/ma30_last
                    
                    

            # ###############################################################################################################       COMPRA sessione 4
            # --------------------------------------------------------------------------------------------------------------------- deviation piu' alte se ma 78 < !
            
            elif self.session == 4:
                
                
                ############################################################################### BUY 4A con ma 78 >
                if (
                    ma78_last >= ma78_2_min_ago
                    and deviation_buy3 > 0.11
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.11
                    and (ma4_prev < ma9_prev and ma4_last > ma9_last)
                    and ma4_last > ma50_last
                ):
                    buy = "BUY 4A con ma 78 > riga 536"
                    action = "buy"
                    percentage = 50
                
                
                ############################################################################## BUY 4B RIVOLUZIONARIO con ma78 >
                elif (
                    ma78_last >= ma78_2_min_ago
                    and deviation_buy3 > 0.02
                    and delta_buy3_incrocio_ma3_ma8 > 0.06
                    and deviation_ma4_sopra_ma30 > 0.17
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                ):
                    buy = "BUY 4B RIVOLUZIONARIO con ma78 > - riga 551"
                    action = "buy"
                    percentage = 50
                    # deviation_buy3 = ma4_last/ma30_last

                
                ############################################################################## BUY 4C RIVOLUZIONARIO con ma78 <
                elif (
                    ma78_last < ma78_2_min_ago
                    and deviation_buy3 > 0.04
                    and delta_buy3_incrocio_ma3_ma8 > 0.08
                    and deviation_ma4_sopra_ma30 > 0.20
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                ):
                    buy = "BUY 4C RIVOLUZIONARIO con ma78 < - riga 567"
                    action = "buy"
                    percentage = 50
                    # deviation_buy3 = ma4_last/ma30_last
                    
                    
        
        
        
        ############################################################################################################  compra sessione 5 in poi
                                                                                                                   #  piu' alto il BUY - "effetti laterali"
             
            else:
                
                ############################################################################## BUY 5A con ma 78 >
                if (
                    ma78_last >= ma78_2_min_ago
                    and deviation_buy3 > 0.13
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.13
                    and (ma4_prev < ma9_prev and ma4_last > ma9_last)
                    and ma4_last > ma50_last
                ):
                    buy = "BUY 5A riga 590"
                    action = "buy"
                    percentage = 50
                    
                
                ####################################################################### BUY 5B RIVOLUZIONARIO con ma78 >
                elif (
                    ma78_last >= ma78_2_min_ago
                    and deviation_buy3 > 0.03
                    and delta_buy3_incrocio_ma3_ma8 > 0.06
                    and deviation_ma4_sopra_ma30 > 0.18
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                ):
                    buy = "BUY 5B RIVOLUZIONARIO con ma78 > - riga 605"
                    action = "buy"
                    percentage = 50
                    # deviation_buy3 = ma4_last/ma30_last
                
                
                ########################################################################### BUY 5C RIVOLUZIONARIO con ma78 <
                elif (
                    ma78_last < ma78_2_min_ago
                    and deviation_buy3 > 0.04
                    and delta_buy3_incrocio_ma3_ma8 > 0.08
                    and deviation_ma4_sopra_ma30 > 0.20
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                ):
                    buy = "BUY 5C RIVOLUZIONARIO con ma78 < - riga 621"
                    action = "buy"
                    percentage = 50
                    # deviation_buy3 = ma4_last/ma30_last
                    
                    
                    
                    
                    
                    
        ############################################################################################################            
        ############################################################################################################
        ############################################################################################################

                                                                                                                   #  V E N D I T A !

        ############################################################################################################
        
        # NON TOCCARE QUESTA RIGA (DICE CHE STA IN MODO SELL, DEVO VENDERE !)

        elif last_trade_action == "buy":

            percentage = self.sell_percentage
            

            #####################################################################################################################
            #####################################################################################################################
            #####################################################################################################################
            
         
            # MA ATTENZIONE al conflitto durante il crollo - SELL SOVRAPPOSTO AL BUY
            # NO 3 < 78 !
            # NO deviation 78 !
            # salvagente SOLO mentre sale 
            
            #####################################################################################################################
            
            # A T T E N Z I O N E ! 
            # VENDITA CON QUESTE 5 ECCEZIONI !
            
            
            # 1 - ro cano VENDE CON UN SALVAGENTE
            if deviation_ma39 < -0.25 and ma50_last > ma50_2_min_ago:
             
                sell = "SELL SALVAGENTE 3-39 con ma50 < riga 665"
                action = "sell"
        
                # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!) !
            
            
            
            # 2 - ro cano VENDE DURANTE UN CROLLO IMPROVVISO !
            elif (
                deviation < -0.70
            ):
                sell = "SELL CROLLO IMPROVVISO - riga 676"
                action = "sell"
                
                # deviation = ma2_last / last_trade_price
                # FORSE E' L' UNICA DEVIATION CHE MI POTRA' SALVARE DA UN CROLLO IMPROVVISO COME QUELLO DEL 3 NOVEMBRE 2021
                
            
            
            # 3 - ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA 1 con ma25 >
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and ma2_last < last_trade_price
                and deviation < -0.45
                and ma25_last > ma25_2_min_ago
            ):

                sell = "SELL DOLCE ATTESA 1 con ma25 > and deviation < -0.45 - riga 692"
                action = "sell"

                # il fattore tempo - la dolce attesa - solo con trend ribassista
                # deviation = ma2_last / last_trade_price
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                
                
                
            # 4 - ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA 2 con ma25 <
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and ma25_last < ma25_2_min_ago
                and deviation < -0.41
                and ma2_last < last_trade_price
            ):
          
                sell = "SELL DOLCE ATTESA 2 con ma25 < and deviation < -0.41 - riga 709"
                action = "sell"

                # il fattore tempo - la dolce attesa - solo con trend ribassista
                # deviation = ma2_last / last_trade_price
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
            
            
            
            # 5 - ro cano VENDE " DOPO x MINUTI " and...
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and ma11_last < ma39_last
                and deviation_sell < -0.35
            ):

                sell = "SELL TEMPO e se ma11 < ma39 and deviation_sell < -0.35 - riga 725"
                action = "sell"
                # ma13 troppo lenta !
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                
                

            
            ################################################################################
            ################################################################################
            ################################################################################ VENDITA - con fasce di tempo ! c'e' vita su marte !
                        
            #    minuti
            #   0 -  3
            #   3 -  5 -
            #   5 - 12 -
            #  12 - 24 -
            #  24 - 40 -
            #  40   60
            #  60   90
            #   > 90
            
            
            ##############################################################################################################################
            
            
            # Tom Petty - Something Good Coming

            # < -0.10  ma78 che mi salva (nel movimento laterale mi fa perdere la meta')
            # < -0.20
            # 0.25 - 0.60
            # 0.61 - 0.79
            # 0.80 - 1.20
            # > 1.21
            
            
            ####################################################################################################################### 0 - 3 min
            
            
            
            # la deviation_sell_ma78 mi protegge - (ogni volta che c'e' stato un rialzo la ma3 non l' ha mai toccata !)
            # e l' incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde ! e mi protegge anche questa quando ma78 sta molto in alto !

            # VENDITA - da 0 a 3 minuti = da 0 a 180 secondi

            if seconds_since_last_trade > 0 and seconds_since_last_trade <= 180:

                
                #################################################################################################### 1) con ma50 > 
                if (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell < -0.23
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (0-3 min) con ma50 > incrocio 3-39 and deviation_sell < -0.23 - riga 780"
                    action = "sell"
                
                
                
                #################################################################################################### 2) con ma50 > 
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    and deviation_sell > 0.25
                    and deviation_sell < 0.60
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (0-3 min) con ma50 > incrocio 3-33 and deviation_sell 0.25 - 0.60 - riga 793"
                    action = "sell"

                
                
                #################################################################################################### 3) con ma50 > 
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    and deviation_sell > 0.61
                    and deviation_sell < 0.79
                ):
                    sell = "SELL (0-3 min) con ma50 > incrocio 3-33 and deviation_sell 0.61 - 0.79 - riga 805"
                    action = "sell"
                
                
                
                
                #################################################################################################### 4) con ma50 > 
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                    and deviation_sell > 0.80
                    and deviation_sell < 1.20
                ):

                    sell = "SELL (0-3 min) con ma50 > incrocio 3-13 and deviation_sell 0.80 - 1.20 - riga 819"
                    action = "sell"
                
                
                
                #################################################################################################### 5) con ma50 > 
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                    and deviation_sell > 1.21
                ):

                    sell = "SELL (0-3 min) con ma50 > incrocio 3-11 and deviation_sell > 1.21 - riga 831"
                    action = "sell"
                
                
                
                ##############################################################################################    
                ##############################################################################################  
                ############################################################################################## trend in ribasso
                
                
                ############################################################################################### 1) con ma50 < 
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                    and deviation_sell < -0.30
                ):
                    sell = "SELL (0-3 min) con ma50 < and incrocio 3-28- riga 847"
                    action = "sell"

                    # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                
                
                
                ############################################################################################### 2) con ma50 < 
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    and deviation_sell < -0.23
                ):
                    sell = "SELL (0-3 min) con ma50 < incrocio 3-33 and deviation_sell -0.23 - riga 860"
                    action = "sell"
                
                
                
                # ---------------------------------------------------------------------------------------------------------------------- 
                # ---------------------------------------------------------------------------------------------------------------------- 
                # ---------------------------------------------------------------------------------------------------------------------- SELL crollo
                
                
                
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                    and deviation_sell > 0.23
                ):
                    sell = "SELL CROLLO (0-3 min) con ma50 < incrocio 3-23 and deviation_sell > 0.23 - riga 876"
                    action = "sell"
                
                
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                    and deviation_sell > 0.60
                ):

                    sell = "SELL CROLLO (0-3 min) con ma50 < incrocio 3-8 and deviation_sell > 0.60 - riga 886"
                    action = "sell"
                
                
                
                # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma3_last < ma16_last
                    and deviation_sell < -0.50
                ):
                    sell = "SELL CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 897"
                    action = "sell"

                    
                
                
                
            
            ################################################################################################################################ SELL 3-5 min

            # VENDITA - da 3 a 5 minuti = da 180 a 300 secondi

            elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 300:
              
              
                #################################################################################################### 1) con ma50 > 
                if (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell < -0.24
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (3-5 min) con ma50 > incrocio 3-39 and deviation_sell < -0.24 - riga 919"
                    action = "sell"
                
                
                
                #################################################################################################### 2) con ma50 >
                elif (
                    ma50_last >= ma50_2_min_ago
                    and ma3_last < ma13_last
                    and deviation_sell > 0.25
                    and deviation_sell < 0.60
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (3-5 min) con ma50 > 3<13 (NO INCROCIO 3-13) and deviation_sell 0.25 - 0.60 - DRIBBLING ALLA RONALDO - riga 932"
                    action = "sell"
                
                
                
                #################################################################################################### 3) con ma50 >
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                    and deviation_sell > 0.61
                    and deviation_sell < 1.20
                ):
                    sell = "SELL (3-5 min) con ma50 > incrocio 3-25 and deviation_sell 0.61 - 1.20 - riga 944"
                    action = "sell"

                    
                
                
                #################################################################################################### 4) con ma50 >
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                    and deviation_sell > 1.21
                ):
                    sell = "SELL (3-5 min) con ma50 > incrocio 3-25 and deviation_sell > 1.21 - riga 956"
                    action = "sell"
                  
                
                
                
                ###########################################################################     trend in ribasso
                
                
                #################################################################################################### 1) con ma50 <
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                    and deviation_sell < -0.30
                    
                    # deviation_sell_ma78 = ma3_last / ma78_last
                ):
                    sell = "SELL (3-5 min) con ma50 < and incrocio 3-28 - riga 973"
                    action = "sell"

                    # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                
                
                
                #################################################################################################### 2) con ma50 <
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    and deviation_sell < -0.23
                ):
                    sell = "SELL (3-5 min) con ma50 < incrocio 3-33 and deviation_sell < -0.23 - riga 986"
                    action = "sell"
                
                
                
                
                # --------------------------------------------------------------------------------------------------------------------- guadagno con crollo
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                    and deviation_sell > 0.23
                ):
                    sell = "SELL con GUADAGNO CON CROLLO (3-5 min) con ma50 < incrocio 3-23 and deviation_sell > 0.23 - riga 998"
                    action = "sell"
                
                
                
               
                # ---------------------------------------------------------------------------------------------------------------------- PARACADUTE crollo
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma3_last < ma16_last
                    and deviation_sell < -0.50
                ):
                    sell = "PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 1010"
                    action = "sell"
                    
                    # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                    
                    
            
            
            
            
            ################################################################################################################################### 5-12 min

            # VENDITA - da 5 a 12 minuti = da 300 a 720 secondi

            elif seconds_since_last_trade > 300 and seconds_since_last_trade <= 720:
              
              
                
                #################################################################################################### 1) con ma50 >
                if (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell < -0.25
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (5-12 min) con ma50 > incrocio 3-39 and deviation_sell < -0.25 - riga 1035"
                    action = "sell"
                    
                
                
                #################################################################################################### 2) con ma50 >
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                    and deviation_sell < -0.25
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (5-12 min) con ma50 > incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - riga 1048"
                    action = "sell"

                    
                
                
                #################################################################################################### 3) con ma50 >
                elif (
                    ma50_last >= ma50_2_min_ago
                    and ma3_last < ma13_last
                    and deviation_sell > 0.25
                    and deviation_sell < 0.60
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (5-12 min) con ma50 > ma3 < ma13 (NO INCROCIO 3-13) and deviation_sell 0.25 - 0.60 - DRIBBLING ALLA RONALDO - riga 1062"
                    action = "sell"

                
                
                #################################################################################################### 4) con ma50 >
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                    and deviation_sell > 0.61
                    and deviation_sell < 1.20
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (5-12 min) con ma50 > incrocio 3-25 and deviation_sell 0.61 - 1.20 - riga 1075"
                    action = "sell"

                    
                
                
                #################################################################################################### 5) con ma50 >
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                    and deviation_sell > 1.21
                ):
                    sell = "SELL (5-12 min) con ma50 > incrocio 3-25 and deviation_sell > 1.21 - riga 1087"
                    action = "sell"

                    
                    
                
                
                ###########################################################################     trend in ribasso
                
                
                
                #################################################################################################### 1) con ma50 <
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                    and deviation_sell < -0.30
                    
                ):
                    sell = "SELL 12 (5-12 min) con ma50 < and incrocio 3-28 - riga 1105"
                    action = "sell"
                    
                    
                
                #################################################################################################### 2) con ma50 <
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                    and deviation_sell < -0.30
                    
                ):
                    sell = "SELL 12 (5-12 min) con ma50 < and incrocio 3-100 (cuscino di sant' antonio) - riga 1117"
                    action = "sell"

                    

                    
                #################################################################################################### 3) con ma50 <   
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    and deviation_sell < -0.27
                ):
                    sell = "SELL (5-12 min) con ma50 < incrocio 3-33 and deviation_sell < -0.27 - riga 1129"
                    action = "sell"
                    
                    
                    

                    
                # ---------------------------------------------------------------------------------------------------------- guadagno con crollo
                
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                    and deviation_sell > 0.23
                ):
                    sell = "SELL eventuale guadagno con crollo (5-12 min) con ma50 <  incrocio 3-23 - riga 1143"
                    action = "sell"
                    
                    
                
                
                # ------------------------------------------------------------------------------------------------------------ PARACADUTE crollo   
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma3_last < ma16_last
                    and deviation_sell < -0.50
                ):
                    sell = "PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 1155"
                    action = "sell"
                    
                    # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                    
                
            
            
            
            
            ############################################################################################################################    12-24 min
            ############################################################################################################################
            ############################################################################################################################   
            ############################################################################################################################

            # VENDITA - da 12 a 24 minuti = da 720 a 1440 secondi

            elif seconds_since_last_trade > 720 and seconds_since_last_trade <= 1440:
              
              
              
                #################################################################################################### 1) con ma50 >
                if (
                    ma50_last >= ma50_2_min_ago
                    #and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    # attenzione ma3 NON HA INCROCIATO con ma39 !
                    and deviation_ma39 < -0.16
                    
                    # and deviation_sell < -0.30
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (12-24 min) con ma50 > and deviation_ma39 < -0.16 - riga 1186"
                    action = "sell"
                
                
                
                
                #################################################################################################### 2) con ma50 >
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                    and deviation_sell < -0.30
                    # viva sant' antonio !
                ):
                    sell = "SELL (12-24 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio and deviation_sell < 0.30 - riga 1199"
                    action = "sell"
                
                
                
                
                #################################################################################################### 3) con ma50 >
                elif (
                    ma50_last >= ma50_2_min_ago
                    and ma3_last < ma13_last
                    and deviation_sell > 0.25
                    and deviation_sell < 0.60
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (12-24 min) con ma50 > ma3 < ma13 (NO INCROCIO 3-13) and deviation_sell 0.25 - 0.60 - DRIBBLING ALLA RONALDO fino a +0.60 - riga 1213"
                    action = "sell"

                    
                    
                    
                
                #################################################################################################### 4) con ma50 >
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                    and deviation_sell > 0.61
                    and deviation_sell < 1.20
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (12-24 min) con ma50 > incrocio 3-25 and deviation_sell 0.61 - 1.20 - riga 1228"
                    action = "sell"
                
                
                
                
                
                #################################################################################################### 5) con ma50 >
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell > 1.21
                ):
                    sell = "SELL (12-24 min) con ma50 > incrocio 3-39 and deviation_sell > 1.21 - riga 1241"
                    action = "sell"
                
                
                
                
                
                ############################################################################################# con trend discendente
                
                # NON TOCCARE ! CUSCINO DI SANT' ANTONIO !
                # L' INCROCIO 5-100 MI SALVA ! MA 5<100 VENDE DURANTE IL RIBASSO !
                
                
                #################################################################################################### 1) con ma50 <
                elif (
                    ma50_last < ma50_2_min_ago
                    and deviation_ma39 < -0.15
                    #ATTENZIONE QUESTA HA FATTO -0.61% !
                    #QUINDI ho abbassato da 0.17 a 0.16 a 0.15
                    #HO NOTATO CHE ANCHE INCROCIO 5-100 SAREBBE ARRIVATO TARDI
                    #ALLORA METTO incrocio 3-78 e deviation <0.10
                  
                    #and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    #and deviation_sell < -0.25
                ):
                    sell = "SELL (12-24 min) con ma50 < and deviation_ma39 < -0.15 - riga 1266"
                    action = "sell"
                    
                    
                
                
                
                #################################################################################################### 2) con ma50 <
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                   # incrocio 5-100 no 5<100 altrimenti vende durante il crollo !
                ):
                    sell = "SELL (12-24 min) con ma50 < and CUSCINO DI SANT' ANTONIO - riga 1279"
                    action = "sell"
                  
                
                
                
                
                #################################################################################################### 3) con ma50 <
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma78_prev and ma3_last < ma78_last) and deviation_sell < -0.37
                    
                    # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50< !
               
                ):
                    sell = "SELL (12-24 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - riga 1294"
                    action = "sell"
                
                
                
                
                
                # ----------------------------------------------------------------------------- guadagno con crollo
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                    and deviation_sell > 0.23
                ):
                    sell = "SELL eventuale guadagno con crollo (12-24 min) con ma50 < incrocio 3 - 18 and deviation_sell > 0.23 - riga 1307"
                    action = "sell"
                    
                    
                    
                
                
                
                # --------------------------------------------------------------------------------- PARACADUTE crollo   
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma3_last < ma16_last
                    and deviation_sell < -0.50
                ):
                    sell = "PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 1321"
                    action = "sell"
                    
                    # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                    
                
            
            
            ################################################################################################################################## 24-60 min

            # VENDITA - da 24 a 60 minuti = da 1080 a 3600 secondi

            elif seconds_since_last_trade > 1440 and seconds_since_last_trade <= 3600:
              
              
              
                if (
                    ma50_last > ma50_2_min_ago
                    and deviation_ma39 < -0.16 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                    #and deviation_sell < 0.10
                    #and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    #and deviation_sell < -0.26
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (24-60 min) con ma50 > and deviation_ma39 < -0.16 or (deviation_sell < 0.10 and ma3_last < ma39_last) - riga 1345"
                    action = "sell"
                
                
                
                
                
                
                elif (
                    ma50_last > ma50_2_min_ago
                    and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                    and deviation_sell < -0.26
                   
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (24-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.26 - riga 1360"
                    action = "sell"

                
                
                
                
                
                elif (
                    ma50_last > ma50_2_min_ago
                    and ma3_last < ma13_last
                    and deviation_sell > 0.30
                    and deviation_sell < 0.60
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (24-60 min) con ma50 > ma3 < ma13 (NO INCROCIO 3-13) and deviation_sell 0.30 - 0.60 DRIBBLING ALLA RONALDO - riga 1375"
                    action = "sell"

                
                
                
                
                
                elif (
                    ma50_last > ma50_2_min_ago
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell > 0.61
                    and deviation_sell < 1.20
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (24-60 min) con ma50 > incrocio 3-39 and deviation_sell 0.61 - 1.20 - riga 1390"
                    action = "sell"
                
                
                
                
                
                
                
                elif (
                    ma50_last > ma50_2_min_ago
                    and (ma3_prev > ma45_prev and ma3_last < ma45_last)
                    and deviation_sell > 1.21
                ):
                    sell = "SELL (24-60 min) con ma50 > incrocio 3-45 and deviation_sell > 1.21 - riga 1404"
                    action = "sell"
                
                
                
                
                
                
                ##################################################################### con trend discendente
                elif (
                    ma50_last < ma50_2_min_ago
                    and deviation_ma39 < -0.15 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                    #and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    #and deviation_sell < -0.34
                    
                ):
                    sell = "SELL (24-60 min) con ma50 < and deviation_ma39 < -0.15 or (deviation_sell < 0.10 and ma3_last < ma39_last) - riga 1420"
                    action = "sell"
                    
                    
                
                
                
                
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma78_prev and ma3_last < ma78_last) and deviation_sell < -0.37
                  
                ):
                    sell = "SELL (24-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - riga 1433"
                    action = "sell"
                
                
                
                
                
                
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                    # NON INCROCERANNO MAI DURANTE IL CROLLO !
                    # non toccare ! INCROCIO 3-100 CUSCINO DI SANT' ANTONIO !
                ):
                    sell = "SELL (24-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - riga 1447"
                    action = "sell"
                
                
                
                # --------------------------------------------------------------------------------------eventuale guadagno durante il crollo

                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                    and deviation_sell > 0.23
                ):
                    sell = "SELL eventuale guadagno durante il crollo (24-60 min) con ma50 < incrocio 3 - 18 and deviation_sell > 0.23 - riga 1459"
                    action = "sell"

                    
                    
                    
                   
                  
                  
            ##############################################################################################################################     da 60 a 90 min
            
            
            # VENDITA - da 60 a 90 min - da 3600 a 5400 secondi in poi
            elif seconds_since_last_trade > 3600 and seconds_since_last_trade <= 5400:
            

                if (
                    ma50_last > ma50_2_min_ago
                    #and ma3_last < ma39_last
                    and deviation_ma39 < -0.18
                    #and deviation_sell < 0.10
                    
                ):
                    sell = "SELL da 60 a 90 min con ma50 > and deviation_ma39 <-0.18 (no ma3<ma39) (NO INCROCIO!) (NO and deviation_sell < 0.10 (!)) - riga 1482"
                    action = "sell"
                    # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                    # cuscino dell' angelo custode
                   
                
                elif (
                    ma50_last > ma50_2_min_ago
                    and ma3_last < ma15_last
                    and deviation_sell > 0.35
                    and deviation_sell < 0.69
                ):
                    sell = "SELL dopo 60 min con ma50> ma3<ma15 (NO INCROCIO 3-13) and deviation_sell 0.35 - 0.69 DOPPIO PASSO ALLA RONALDO (ma15 invece dicon ma13) - riga 1494"
                    action = "sell"

                    
                elif (
                    ma50_last > ma50_2_min_ago
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell > 0.70
                    and deviation_sell < 1.49
                ):

                    sell = "SELL da 60 a 90 min con ma50 > incrocio 3-39 and deviation_sell 0.70 - 1.49 - riga 1505"
                    action = "sell"

                    # ma 3-48 mi evita la ricompra e la rivendita con perdita !
 

                elif (
                    ma50_last > ma50_2_min_ago
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    and deviation_sell > 1.50
                ):

                    sell = "SELL da 60 a 90 min con ma50 > incrocio 3-33 and deviation_sell > 1.50 - riga 1517"
                    action = "sell"

        
        
                ######################################################################################## con trend discendente
          
          
          
                elif (
                    ma50_last < ma50_2_min_ago
                    and deviation_ma39 < -0.18
                 
                ):
                    sell = "SELL da 60 a 90 min con ma50 < con deviation_ma39 <-0.18 and deviation_sell < 0.10 (no ma3<ma33) (NO INCROCIO!) - riga 1531"
                    action = "sell"
                # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                # cuscino dell' angelo custode
                
                
                
                
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma78_prev and ma3_last < ma78_last) and deviation_sell < 0.10
                 
                ):
                    sell = "SELL da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < 0.10 - riga 1545"
                    action = "sell"
                
            
            
            ################################################################################################################################# > 90 min
            
            # VENDITA - da 90 minuti in poi = da 5400 secondi in poi

            elif seconds_since_last_trade > 5400:
                
                
                
                if (
                    ma50_last > ma50_2_min_ago
                    #and ma3_last < ma39_last
                    and deviation_ma39 < -0.18 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                    # dopo 90 min se il prezzo non ha forza puoi anche prendere qualcosa (solo > 90 min QUESTA RIGA e' diversa da MADDOG)
                ):   
                    sell = "SELL dopo 90 min con ma50 > and deviation_ma39 <-0.18 (no ma3<ma39) (NO INCROCIO!) or (deviation_sell < 0.10 and ma3 < ma39) - riga 1564"
                    action = "sell"
                    # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                    # cuscino dell' angelo custode
                    
                    
                elif (
                    ma50_last > ma50_2_min_ago
                    and ma3_last < ma15_last
                    and deviation_sell > 0.35
                    and deviation_sell < 0.69
                ):
                    sell = "SELL dopo 90 min con ma50> ma3<ma15 (NO INCROCIO 3-15) and deviation_sell 0.35 - 0.69 DOPPIO PASSO ALLA RONALDO (con ma15 invece di ma13)-riga 1576"
                    action = "sell"

                    
                elif (
                    ma50_last > ma50_2_min_ago
                    and (ma3_prev > ma48_prev and ma3_last < ma48_last)
                    and deviation_sell > 0.70
                    and deviation_sell < 1.49
                ):

                    sell = "SELL dopo 90 min con ma50 > incrocio 3-48 (!) and deviation_sell 0.70 - 1.49 - riga 1587"
                    action = "sell"

                    # ma 3-48 mi evita la ricompra e la rivendita con perdita !

                    
                elif (
                    ma50_last > ma50_2_min_ago
                    and (ma3_prev > ma48_prev and ma3_last < ma48_last)
                    and deviation_sell > 1.50
                ):

                    sell = "SELL dopo 90 min con ma50 > incrocio 3-48 (!) and deviation_sell > 1.50 - riga 1599"
                    action = "sell"

                    
                ######################################################################################## con trend discendente
             
                    
                elif (
                    ma50_last < ma50_2_min_ago
                    #and ma3_last < ma33_last
                    and deviation_ma39 < -0.18 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                    # dopo 90 min se il prezzo non ha forza puoi anche prendere qualcosa (solo > 90 min QUESTA RIGA e' diversa da MADDOG)
                    
                ):
                    sell = "SELL dopo 90 min con ma50 < con deviation_ma39 <-0.18 (no ma3<ma33) (NO INCROCIO!) or (deviation_sell < 0.10 and ma3_last < ma39_last) - riga 1613"
                    action = "sell"
                # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                # ATTENZIONE non c'e' l' incrocio 3-33 ( PERCHE' NON HANNO INCROCIATO !) ma 3 < 33 !
                # cuscino dell' angelo custode
                
                
                ######################################################################################################################################################

           
            

            ############### FINE ALGORITH ###################

        self.algo_helper.info("action {}".format(action))
        self.algo_helper.info("percentage {}".format(percentage))

        if action == "sell":
            self.algo_helper.info("action sell {}".format(sell))
            self.session += 1

        elif action == "buy":
            self.algo_helper.info("action buy {}".format(buy))

        return action, percentage

        # compa, compa caro !
        # ave comparo meo !

        # AGAINST THE WIND - Bob Seger & Jason Aldean
        
        
        # vai compaaaaaaaaaaaaa
        # ave comparo meo !
        
        # ti voglio bene, compa.
        # compa, compa caro ! 
        #



