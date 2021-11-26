

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
        
        
        

        # moving average (2-3-4-5-7-8-20-43-100) di x minuti prima

        ma2_2_min_ago = self.algo_helper.ma_minutes_ago(2, 2)
        ma2_3_min_ago = self.algo_helper.ma_minutes_ago(2, 3)

        ma2_4_min_ago = self.algo_helper.ma_minutes_ago(2, 4)

        ma3_2_min_ago = self.algo_helper.ma_minutes_ago(3, 2)
        ma3_3_min_ago = self.algo_helper.ma_minutes_ago(3, 3)
        ma3_9_min_ago = self.algo_helper.ma_minutes_ago(3, 9)
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

        # PREZZO di X MINUTI FA (di mercato) -

        price_2_min_ago = self.algo_helper.price_minutes_ago(2)
        price_10_min_ago = self.algo_helper.price_minutes_ago(10)
        price_15_min_ago = self.algo_helper.price_minutes_ago(15)
        price_20_min_ago = self.algo_helper.price_minutes_ago(20)

        ###################################################################################################################################################### TEMPO
        ######################################################################################################################################################

        # importante : dolce attesa 

        # VENDE DOPO x SECONDI - ro cano torna a casa - (ma c'e' anche un "e se")
        max_hold_time_in_seconds = 360
        #  6 minuti * 60 = 360

        #########################################################################################################################################################
        #########################################################################################################################################################

        #                                                         T U T T E    L E   D E V I A T I O N  !

        ##############################################################################################################

        # formula DEVIATION_1_gabbia
        deviation_1_gabbia = (ma8_last / ma50_last - 1) * 100 if ma50_last else 0
        self.algo_helper.info("deviation_1_gabbia: {}".format(deviation_1_gabbia))

        ##################################################################################################################

        # formula deviation
        deviation = (ma3_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.info("deviation: {}".format(deviation))

        ##################################################################################################################

        ################################################################ deviation per comprare

        # formula DEVIATION_buy1 per la compra 1
        deviation_buy1 = (ma13_last / ma39_last - 1) * 100 if ma39_last else 0
        self.algo_helper.info("deviation_buy1: {}".format(deviation_buy1))
        
        
        # formula DEVIATION_bellissima
        deviation_bellissima = (ma6_last / ma30_last - 1) * 100 if ma30_last else 0
        self.algo_helper.info("deviation_bellissima: {}".format(deviation_bellissima))
        

        # formula DEVIATION_buy2 per la compra 2
        deviation_buy2 = (ma8_last / ma50_last - 1) * 100 if ma50_last else 0
        self.algo_helper.info("deviation_buy2: {}".format(deviation_buy2))

        # formula DEVIATION_buy3 per la compra 3
        deviation_buy3 = (ma4_last / ma30_last - 1) * 100 if ma30_last else 0
        self.algo_helper.info("deviation_buy3: {}".format(deviation_buy3))

        # ------------------------------------------------------------------------------------------------------------

        # formula delta_buy3_incrocio_ma3_ma8 > 0.10 per la compra 3
        delta_buy3_incrocio_ma3_ma8 = (ma3_last / ma8_last - 1) * 100 if ma8_last else 0
        self.algo_helper.info("delta_buy3_incrocio_ma3_ma8: {}".format(delta_buy3_incrocio_ma3_ma8))
            
        

        # formula DEVIATION_buy per comprare UN PO' PIU' SOPRA DEL LAST TRADE ( di solito l' ultimo SELL )
        deviation_buy = (ma2_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.info("deviation_buy: {}".format(deviation_buy))    
        
        

        ############################################################################################     DEVIATION_buy_crollo

        # formula DEVIATION_buy_crollo_1 per comprare a una certa distanza da ma78
        deviation_buy_crollo_1 = (ma8_last / ma78_last - 1) * 100 if ma78_last else 0
        self.algo_helper.info("deviation_buy_crollo_1: {}".format(deviation_buy_crollo_1))
            
        

        # formula DEVIATION_buy_crollo_2 per comprare a una certa distanza da ma13
        deviation_buy_crollo_2 = (ma3_last / ma13_last - 1) * 100 if ma13_last else 0
        self.algo_helper.info("deviation_buy_crollo_2: {}".format(deviation_buy_crollo_2))
        
      
        ############################################################################################################################

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
      
        ######################################################################################## deviation per vendere

        # formula DEVIATION_sell
        deviation_sell = (ma4_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.info("deviation_sell: {}".format(deviation_sell))    
       
        # formula DEVIATION_sell_ma78
        deviation_sell_ma78 = (ma4_last / ma78_last - 1) * 100 if ma78_last else 0
        self.algo_helper.info("deviation_sell_ma78: {}".format(deviation_sell_ma78))
        
      
        # formula deviation_ma39 per vendere un po' piu' giu' di ma39
        deviation_ma39 = (ma4_last / ma39_last - 1) * 100 if ma39_last else 0
        self.algo_helper.info("deviation_ma39: {}".format(deviation_ma39))
        
        
        
        ###########################################################################################
      
        # DEFAULT ACTION DICE DI NON FARE NIENTE (= None, NON TOCCARE )
        action = None
        percentage = 0

        ############################################################################################ APRE E CHIUDE LA GABBIA
        
        # SE LA GABBIA E' TROPPO APERTA IMPAZZISCE NEI MOVIMENTI LATERALI ! entrano in azione buy 2-3-4-5 che sono piu' reattivi del BUY 1 !
        
        # APRE E CHIUDE GABBIA

        if deviation_1_gabbia > -0.29 or deviation_buy_crollo_1 < -1.90:

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

        #############################################################################################################################################

        # COMPRA
        # NON TOCCARE QUESTA RIGA ( DICE CHE STA IN MODO BUY, vuole COMPRARE ! )

        if self.open and self.session and last_trade_action != "buy":

            ###########################################################################################################################################
            #   B U Y
            ###########################################################################################################################################

            percentage = self.buy_percentage
            # NON TOCCARE  ! DI DEFAULT E' IL 2%
            
        
            # in futuro
            # buy spazio-tempo ma con aggiunta di ma 13-25
            # MACD sempre con aggiunta di ma 13-25 (come studio) (III° cane)
            
            # TOGLIER TUTTI GLI INCROCI AL BUY ! se 13 > 100 NON INCROCERA' MAI ! INCROCIO 13-100 DIVENTA 13>100 !
            
            
            
            ######################################################################################################## COMPRA sessione 1

            if self.session == 1:

                # ------------------------------------------------------------ BUY 1 DURANTE IL RIALZO con INCROCIO CLASSICO 72-100

                if (
                    ma13_last > ma78_last
                    and ma72_last > ma100_last
                    and ma2_last > ma2_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                    
                    and ma6_last > ma100_last
                    and ma6_last > ma39_last
                    and ma6_last > ma13_last
                    # ho visto anche il BUY durante il crollo
                    
                    and deviation_bellissima > 0.163
                    # deviation_bellissima = ma6_last / ma30_last
                    
                    # and deviation_ma13_sopra_ma25 > 0.07 TOLTA PROVVISORIAMENTE vedi BUY ore 10:47 del 23 nov 2021 (E' ARRIVATA MOLTO TARDI)
                ):

                    buy = "BUY 1 con 72>100 and deviation_bellissima >0.163 riga 294"
                    action = "buy"
                    percentage = 50
                    
                    
                    
                
                # --------------------------------------------------------------    BUY 1 DURANTE IL RIALZO con LA DEVIATION BUY 1

                elif (
                    deviation_buy1 > 0.56
                    and ma13_last > ma39_last
                    and ma78_last > ma78_2_min_ago
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma4_last > ma4_2_min_ago
                ):
                    buy = "BUY 1 con 13>39 and DEVIATION BUY 1 ALTA e ma78 > riga 311"
                    action = "buy"
                    percentage = 50

                    # deviation_buy1 = ma13_last/ma39_last
               
                ####################################################################  BUY 1 con incrocio 13-100 and ma78_last >= ma78_4_min_ago  "MI PIACE!"

                elif (
                    ma13_last > ma100_last
                    and ma78_last >= ma78_4_min_ago
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma3_3_min_ago
                    and ma4_last > ma4_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                    and deviation_ma13_sopra_ma25 > 0.06
                    # quando 13-100 si incrociano price ma2 e ma4 sono gia' in ribasso
                ):
                    buy = "BUY 1 con 13>100 e ma78> 4 min ago riga 330"
                    action = "buy"
                    percentage = 50
                ################################################################################################################## compra durante il ribasso
                
                
                elif (
                    ma78_last < ma78_2_min_ago
                    and ma39_last > ma78_last
                    and deviation_buy1 > 0.14
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma4_last > ma4_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                ):

                    buy = "BUY 1 con ma78< and 39>78 and DEVIATION BUY 1 BASSA riga 346"
                    action = "buy"
                    percentage = 50
                    # deviation_buy1 = ma13_last/ma39_last
                
                
                elif (
                    ma78_last < ma78_2_min_ago
                    and ma39_last > ma78_last
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma4_last > ma4_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                    and deviation_ma13_sopra_ma25 > 0.05
                ):

                    buy = "se ma78< - BUY 1 con incrocio 39>78 - riga 362"
                    action = "buy"
                    percentage = 50
                    # deviation_buy1 = ma13_last/ma39_last
                    # and deviation_ma13_sopra_ma25 > 0.05 FONDAMENTALE
              
                ##############################################################################################################################
                # IMPORTANTISSIMO ! SOLO PER IL BUY 1 - PER COMPRARE DURANTE IL CROLLO - compa prega per me - ( cruise - david gilmour )
                ##############################################################################################################################

                # entriamo nell' area dell' ipervenduto, compa !
                # QUI LASCIO GLI INCROCI !
              
                # BUY  PRIMO MODO DURANTE IL CROLLO

                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -2.30
                    and (ma8_prev < ma25_prev and ma8_last > ma25_last)
                ):
                    buy = "BUY DURANTE IL CROLLO - modo 1 riga 382"
                    action = "buy"
                    percentage = 50
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                
                
              
                # BUY SECONDO MODO - DURANTE IL CROLLO - questa condizione e' entrata in azione ! ( e mi e' sembrata ben fatta !)
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -1.80
                    and deviation_buy_crollo_2 > 0.21
                ):
                    buy = "BUY DURANTE IL CROLLO - modo 2 riga 396"
                    action = "buy"
                    percentage = 50
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_buy_crollo_2 = ma3_last / ma13_last
                    
            ############################################################################################################

            #############################################################################################################      COMPRA sessione 2

            elif self.session == 2:
                if (
                    
                    ma78_last > ma78_4_min_ago
                    and deviation_buy2 > 0.07
                    and deviation_buy_ma3_sopra_ma13 > 0.09
                    and deviation_ma7_sopra_ma40 > 0.09
                    and ma2_last > ma2_2_min_ago
                    and price > price_2_min_ago
                    and ma3_last > ma40_last
                ):
                    buy = "BUY 2A riga 417"
                    action = "buy"
                    percentage = 50
                    # deviation_buy_ma3_sopra_ma13 > x e' fondamentale !
                    # deviation_buy2 = ma8_last/ma50_last
                    
                    
                elif (
                    
                    ma78_last < ma78_4_min_ago
                    and deviation_buy2 > 0.07
                    and deviation_ma13_sopra_ma25 > 0.06
                    
                    and deviation_buy_ma3_sopra_ma13 > 0.09
                    and deviation_ma7_sopra_ma40 > 0.10
                    and ma2_last > ma2_2_min_ago
                    and price > price_2_min_ago
                    and ma3_last > ma40_last
                ):
                    buy = "BUY 2B riga 436"
                    action = "buy"
                    percentage = 50
                    # deviation_buy_ma3_sopra_ma13 > x e' fondamentale !
                    # deviation_buy2 = ma8_last/ma50_last
                
                
                elif (
                    
                    
                    deviation_buy2 > 0.13
                    and deviation_buy_ma3_sopra_ma13 > 0.10
                    and deviation_ma7_sopra_ma40 > 0.14
                    and ma4_last > ma9_last
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma40_last
                    and ma4_last > ma78_last
                ):
                    buy = "BUY 2C riga 454"
                    action = "buy"
                    percentage = 50
                    # deviation_buy2 = ma8_last / ma50

            ############################################################################################################COMPRA sessione 3

            elif self.session == 3:

                if (
                    ma78_last >= ma78_2_min_ago
                    and deviation_buy3 > 0.11
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.10
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    
                    and ma7_last > ma25_last
                ):
                    buy = "BUY 3A con ma78 > riga 473"
                    action = "buy"
                    percentage = 50
            
            
            
                elif (    
                    deviation_buy3 > 0.02
                    and ma39_last > ma78_last
                    and deviation_buy3 > 0.02
                    and delta_buy3_incrocio_ma3_ma8 > 0.06
                    and deviation_ma4_sopra_ma30 > 0.17
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                    
                    and ma7_last > ma25_last
                ):
                    buy = "BUY 3B RIVOLUZIONARIO se ma39 > ma78- riga 491"
                    action = "buy"
                    percentage = 50
                    # deviation_buy3 = ma4_last/ma30_last
                    # riga 462 potrebbe esserci un problema perche' ho tolto ma78_last >= ma78_2_min_ago. vediamo
                
                
                elif (
                    ma78_last < ma78_2_min_ago
                    and deviation_buy3 > 0.03
                    and deviation_ma13_sopra_ma25 > 0.045
                    and delta_buy3_incrocio_ma3_ma8 > 0.07
                    and deviation_ma4_sopra_ma30 > 0.18
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                    
                    and ma7_last > ma25_last
                ):
                    buy = "BUY 3C RIVOLUZIONARIO se ma78 < - riga 510"
                    action = "buy"
                    percentage = 50
                    # deviation_buy3 = ma4_last/ma30_last
                    
                    

            # ###############################################################################################################       COMPRA sessione 4
            # --------------------------------------------------------------------------------------------------------------------- deviation piu' alte se ma 78 < !
            
            elif self.session == 4:
                
                if (
                    ma78_last >= ma78_2_min_ago
                    and deviation_buy3 > 0.11
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.11
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    
                    and ma7_last > ma25_last
                ):
                    buy = "BUY 4A con ma 78 > riga 532"
                    action = "buy"
                    percentage = 50
                    
                   
                elif (
                    ma78_last >= ma78_2_min_ago
                    and deviation_buy3 > 0.02
                    and delta_buy3_incrocio_ma3_ma8 > 0.06
                    and deviation_ma4_sopra_ma30 > 0.15
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                    
                    and ma7_last > ma25_last
                ):
                    buy = "BUY 4B RIVOLUZIONARIO con ma78 > - riga 548"
                    action = "buy"
                    percentage = 50
                    # deviation_buy3 = ma4_last/ma30_last

                
                
                elif (
                    ma78_last < ma78_2_min_ago
                    and deviation_buy3 > 0.04
                    and delta_buy3_incrocio_ma3_ma8 > 0.08
                    and deviation_ma4_sopra_ma30 > 0.20
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                    
                    and ma7_last > ma25_last
                ):
                    buy = "BUY 4C RIVOLUZIONARIO con ma78 < - riga 566"
                    action = "buy"
                    percentage = 50
                    # deviation_buy3 = ma4_last/ma30_last
          
        ############################################################################################################  compra sessione 5 in poi
                                                                                                                   #  piu' alto il BUY - "effetti laterali"
             
            else:

                if (
                    ma78_last >= ma78_2_min_ago
                    and deviation_buy3 > 0.13
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.13
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    
                    and ma6_last > ma15_last
                    and ma7_last > ma25_last
                    
                    and deviation_bellissima > 0.163
                    
                    # deviation_bellissima = 6/30
                    # questa deviation serve a spezzare la catena dei buy - effetti laterali.
                    # se e' arrivato il buy 5 e' molto probabile che il trend sia consolidato 
                    # e, a questo punto, non importa se compra con un + 0.10 piu' in alto. NON FA UNA GRANDE DIFFERENZA !
                ):
                    buy = "BUY 5A con ma78 > and deviation_bellissima > 0.163 (PER SPEZZARE LA CATENA -effetti laterali) riga 594"
                    action = "buy"
                    percentage = 50
                
                
                
                elif (
                    ma78_last >= ma78_2_min_ago
                    and deviation_buy3 > 0.03
                    and delta_buy3_incrocio_ma3_ma8 > 0.06
                    and deviation_ma4_sopra_ma30 > 0.15
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                    
                    and ma7_last > ma25_last
                    and deviation_bellissima > 0.163
                ):
                    buy = "BUY 5B RIVOLUZIONARIO con ma78 > and deviation_bellissima > 0.163 (PER SPEZZARE LA CATENA -effetti laterali) - riga 612"
                    action = "buy"
                    percentage = 50
                    # deviation_buy3 = ma4_last/ma30_last
                
             
                elif (
                    ma78_last < ma78_2_min_ago
                    and deviation_buy3 > 0.04
                    and delta_buy3_incrocio_ma3_ma8 > 0.08
                    and deviation_ma4_sopra_ma30 > 0.20
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                    
                    and ma7_last > ma25_last
                    and deviation_bellissima > 0.163
                ):
                    buy = "BUY 5C RIVOLUZIONARIO con ma78 < and deviation_bellissima > 0.163 - riga 630"
                    action = "buy"
                    percentage = 50
                    # deviation_buy3 = ma4_last/ma30_last
                    
                    

        ############################################################################################################

        #  V E N D I T A !

        ############################################################################################################

        # NON TOCCARE QUESTE RIGHE (DICE CHE STA IN MODO SELL, DEVO VENDERE !)

        elif last_trade_action == "buy":

            percentage = self.sell_percentage
            # E' 100 DI DEFAULT !
            #####################################################################################################################
            
           
            # VENDITA CON QUESTE 5 ECCEZIONI !
            # MA ATTENZIONE al conflitto durante il crollo - SELL SOVRAPPOSTO AL BUY
            
            
            # NO 3<78 !
            # NO deviation 78 !
            # QUALCHE VOLTA ma3-ma39 NON HANNO INCROCIATO allora per la vendita con il DRIBBLING e il DOPPIO PASSO ALLA RONALDO ho risolto con 3<39
            # il CUSCINO DELL' ANGELO CUSTODE e di SANT' ANTONIO mi proteggono ! (vendita con medie lunghe)
            
           
            # 1 - ro cano VENDE CON UN SALVAGENTE
            if deviation_ma39 < -0.25 and ma50_last > ma50_2_min_ago:
             
                sell = "SELL SALVAGENTE 3-39 con ma50 < riga 665"
                action = "sell"
        
                # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!
            
            
            
            # 2 - ro cano VENDE DURANTE UN CROLLO IMPROVVISO !
            elif (
                deviation < -0.60
            ):
                sell = "SELL CROLLO IMPROVVISO - riga 676"
                action = "sell"
                
                # deviation = ma2_last / last_trade_price
                # FORSE E' L' UNICA DEVIATION CHE MI POTRA' SALVARE DA UN CROLLO IMPROVVISO COME QUELLO DEL 3 NOVEMBRE 2021
                
            
            
            # 3 - ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma25 >
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and ma2_last < last_trade_price
                and deviation < -0.45
                and ma25_last > ma25_2_min_ago
            ):

                sell = "SELL DOLCE ATTESA con ma25> and deviation < -0.45 - riga 692"
                action = "sell"

                # il fattore tempo - la dolce attesa - solo con trend ribassista
                # deviation = ma2_last / last_trade_price
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
            
            
            
            # 4 - ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma25 <
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and ma25_last < ma25_2_min_ago
                
                and deviation < -0.40
                and ma2_last < last_trade_price
            ):

                sell = "SELL DOLCE ATTESA con ma25< and deviation < -0.40 - riga 710"
                action = "sell"

                # il fattore tempo - la dolce attesa - solo con trend ribassista
                # deviation = ma2_last / last_trade_price
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
            
            
            
            
            # 5 - ro cano VENDE " DOPO x MINUTI " and...
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and ma8_last < ma50_last
                and deviation_sell < -0.49
            ):

                sell = "SELL TEMPO e se ma8 < ma50 and deviation_sell < -0.49 - riga 727"
                action = "sell"
                # ma13 troppo lenta !
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)

            ###################################################################################################################################
            
            

            # VENDITA - con fasce di tempo ! c'e' vita su marte !

            #    minuti
            #   0 -  3
            #   3 -  5 -
            #   5 - 12 -
            #  12 - 21 - ---------------------------------------------qui comincia un nuovo paradigma !
            #  21 - 40 -
            #  40   60
            #  60   90
            #   > 90
            
            
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
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell < -0.23
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (0-3 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.23 - riga 781"
                    action = "sell"
                
                
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    and deviation_sell > 0.25
                    and deviation_sell < 0.60
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.25 - 0.60 - riga 792"
                    action = "sell"

                    
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    and deviation_sell > 0.61
                    and deviation_sell < 0.79
                ):
                    sell = "SELL (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.61 - 0.79 - riga 802"
                    action = "sell"
                
                
                
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                    and deviation_sell > 0.80
                    and deviation_sell < 1.20
                ):

                    sell = "SELL (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell 0.80 - 1.20 - riga 814"
                    action = "sell"
                
                
                
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                    and deviation_sell > 1.21
                ):

                    sell = "SELL (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell > 1.21 (che sarebbe come IL DRIBBLING ALLA RONALDO !)- riga 825"
                    action = "sell"
                
                
                ###########################################################################     trend in ribasso

                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                    and deviation_sell < -0.30
                ):
                    sell = "SELL (0-3 min) con ma50 < and incrocio 3-28- riga 751"
                    action = "sell"

                    # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                
                
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    and deviation_sell < -0.23
                ):
                    sell = "SELL (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 - riga 847"
                    action = "sell"

                # ---------------------------------------------------------------------------------------------------------------------- crollo

                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                    and deviation_sell < -0.50
                ):
                    sell = "SELL CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - riga 857"
                    action = "sell"

                    # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                
                
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                    and deviation_sell > 0.23
                ):
                    sell = "SELL CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 868"
                    action = "sell"
                
                
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                    and deviation_sell > 0.60
                ):

                    sell = "SELL CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - riga 878"
                    action = "sell"
            
            
            
            ################################################################################################################################         3-5 min

            # VENDITA - da 3 a 5 minuti = da 180 a 300 secondi

            elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 300:

                if (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell < -0.24
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (3-5 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.24 - riga 895"
                    action = "sell"
                
                
                elif (
                    ma50_last >= ma50_2_min_ago
                    and ma3_last < ma9_last
                    and deviation_sell > 0.25
                    and deviation_sell < 0.90
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (3-5 min) con ma50 > and 3<9 (no incrocio 3-9) and deviation_sell 0.25 - 0.90 - DRIBBLING ALLA RONALDO - riga 906"
                    action = "sell"
                
                
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                    and deviation_sell > 0.91
                    and deviation_sell < 1.20
                ):
                    sell = "SELL (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 916"
                    action = "sell"

                    
                    
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                    and deviation_sell > 1.21
                ):
                    sell = "SELL (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - riga 926"
                    action = "sell"
                
                
                ###########################################################################     trend in ribasso

                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                    and deviation_sell < -0.30
                    
                    # deviation_sell_ma78 = ma3_last / ma78_last
                ):
                    sell = "SELL (3-5 min) con ma50 < and incrocio 3-28 - riga 939"
                    action = "sell"

                    # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                
                
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    and deviation_sell < -0.23
                ):
                    sell = "SELL (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.23 - riga 950"
                    action = "sell"

                    
                    
                # ---------------------------------------------------------------------------------------------------------------------- guadagno con crollo
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                    and deviation_sell > 0.23
                ):
                    sell = "SELL GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 961"
                    action = "sell"
                    
                    
                    
                    
                    
                    
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma3_last < ma16_last
                    and deviation_sell < -0.50
                ):
                    sell = "PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 974"
                    action = "sell"
                    
                    # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                    
                    
                    
                

                    
                    
                    
                    
                    
                    
                    
            ################################################################################################################################### 5-12 min

            # VENDITA - da 5 a 12 minuti = da 300 a 720 secondi

            elif seconds_since_last_trade > 300 and seconds_since_last_trade <= 720:

                if (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                    and deviation_sell < -0.41
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (5-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - riga 1002"
                    action = "sell"
                
                # guardare la stella (guardare da una stella!)
                # QUESTO E' IL RISCHIO PIU' GRANDE CHE PRENDO ! ( ma con ma50 > ma50 2 min ago DOPO 5 min (+2))
                
                
                
                
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                    and deviation_sell < -0.25
                    
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (5-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - riga 1018"
                    action = "sell"
                
                
                
                
                elif (
                    ma50_last >= ma50_2_min_ago
                    and ma3_last < ma9_last
                    and deviation_sell > 0.25
                    and deviation_sell < 0.90
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (5-12 min) con ma50 >  3<9 and deviation_sell 0.25 - 0.90 - DRIBBLING ALLA RONALDO - riga 1031"
                    action = "sell"

                    
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                    and deviation_sell > 0.91
                    and deviation_sell < 1.20
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 1042"
                    action = "sell"

                    
                    
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                    and deviation_sell > 1.21
                ):
                    sell = "SELL (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - riga 1052"
                    action = "sell"

                    
                ###########################################################################     trend in ribasso

                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                    and deviation_sell < -0.30
                    
                ):
                    sell = "SELL 12 (5-12 min) con ma50 < and incrocio 3-28 - riga 1064"
                    action = "sell"

                    # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                
              
               
                elif (
                    ma50_last < ma50_2_min_ago 
                    and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                    and deviation_sell < -0.30
                    
                ):
                    sell = "SELL 12 (5-12 min) con ma50 < and incrocio 3-100 (cuscino di sant' antonio) - riga 1077"
                    action = "sell"    
                    
                    
                
                    
                    
                # ------------------------------------------------------------------------------- guadagno con crollo
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                    and deviation_sell > 0.23
                ):
                    sell = "SELL guadagno con crollo (5-12 min) con ma50 < and incrocio 3-23 - riga 1090"
                    action = "sell"
                    
                    
                    
                    
                # ------------------------------------------------------------------------------------------------------------ PARACADUTE crollo   
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma3_last < ma16_last
                    and deviation_sell < -0.50
                ):
                    sell = "PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 1102"
                    action = "sell"
                    
                    # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                    
                
 







            ############################################################################################################################    12-21 min

            # VENDITA - da 12 a 21 minuti = da 720 a 1260 secondi

            elif seconds_since_last_trade > 720 and seconds_since_last_trade <= 1260:

                if (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma72_prev and ma3_last < ma72_last) 
                    and deviation_sell < -0.65
                    
                    #and deviation_ma39 < -0.29 vendeva troppo presto
                    
                    # ATTENZIONE "and (ma3_prev > ma39_prev and ma3_last < ma39_last)" con ma39 NON HA INCROCIATO
                    # and deviation_sell < -0.30
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (12-21 min) con ma50 > and incrocio 3-72 and deviation sell -0.65 e vaffanculo ! - riga 1133"
                    action = "sell"
                
                
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma100_prev and ma3_last < ma100_last)
                    and deviation_sell < -0.30
                    # viva sant' antonio !
                ):
                    sell = "SELL (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.30 - riga 1143"
                    action = "sell"
                
                
                
                elif (
                    ma50_last >= ma50_2_min_ago
                    and ma3_last < ma13_last
                    and deviation_sell > 0.25
                    and deviation_sell < 0.90
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (12-21 min) con ma50 > and 3-13 (NO INCROCIO 3-13) and deviation_sell 0.25 - 0.90 - DOPPIO PASSO ALLA RONALDO fino a +0.50 - riga 1155"
                    action = "sell"

                    
                    
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                    and deviation_sell > 0.91
                    and deviation_sell < 1.20
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (12-21 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 1167"
                    action = "sell"
                
                
                
                elif (
                    ma50_last >= ma50_2_min_ago
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell > 1.21
                ):
                    sell = "SELL (12-21 min) con ma50 > and incrocio 3-39 and deviation_sell > 1.21 - riga 1177"
                    action = "sell"
                
                ##########################################################################################
                # NON TOCCARE ! CUSCINO DI SANT' ANTONIO !
                # L' INCROCIO 5-100 MI SALVA ! MA 5<100 VENDE DURANTE IL RIBASSO !
                ##################################################################### con trend discendente
                
                elif (
                    ma50_last < ma50_2_min_ago
                    and deviation_ma39 < -0.15
                    
                    #and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    #and deviation_sell < -0.25
                ):
                    sell = "SELL (12-21 min) con ma50 < and deviation_ma39 < -0.15 - riga 1192"
                    action = "sell"
                    
                    #ATTENZIONE QUESTA aveva FATTO -0.61% !
                    #QUINDI ho abbassato da 0.17 a 0.16 a 0.15
                    #HO NOTATO CHE ANCHE INCROCIO 5-100 SAREBBE ARRIVATO TARDI
                    #ALLORA METTO incrocio 3-78 e deviation <0.10
             
                
                    
                    
                    
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma78_prev and ma3_last < ma78_last) and deviation_sell < -0.45
                    
                    # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50< !
               
                ):
                    sell = "SELL (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - riga 1211"
                    action = "sell"
                
                
                
                
                
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                    and deviation_sell < -0.27
                    # viva sant' antonio !
                   # incrocio 5-100 no 5<100 altrimenti vende durante il crollo !
                ):
                    sell = "SELL (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - riga 1225"
                    action = "sell"   
                    
                    
                    
                    
                # --------------------------------------------------------------------------------- PARACADUTE crollo   
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma3_last < ma16_last
                    and deviation_sell < -0.50
                ):
                    sell = "PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 1237"
                    action = "sell"
                    
                    # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE  
                    
                    
                    
                # ----------------------------------------------------------------------------- guadagno con crollo
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                    and deviation_sell > 0.23
                ):
                    sell = "SELL eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3 - 18 and deviation_sell > 0.23 - riga 1250"
                    action = "sell"    
                
                    
                    
                

                    
            
            
            
            
            ################################################################################################################################## 21-60 min

            # VENDITA - da 21 a 60 minuti = da 1261 a 3600 secondi

            elif seconds_since_last_trade > 1261 and seconds_since_last_trade <= 3600:

                if (
                    ma50_last > ma50_2_min_ago
                    
                    and (ma3_prev > ma78_prev and ma3_last < ma78_last) and deviation_sell < -0.65 or (deviation_sell < 0.10 and ma3_last < ma50_last)
                    
                    #and deviation_ma39 < -0.16 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                    #and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    #and deviation_sell < -0.26
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (21-60 min) con ma50 > and deviation_ma39 < -0.16 or (deviation_sell < 0.10 and ma3_last < ma50_last) - riga 1278"
                    action = "sell"

                
                
                elif (
                    ma50_last > ma50_2_min_ago
                    and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                    and deviation_sell < -0.26
                   
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (21-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.26 - riga 1290"
                    action = "sell"
                
                
                
                
                elif (
                    ma50_last > ma50_2_min_ago
                    and ma3_last < ma16_last
                    and deviation_sell > 0.30
                    and deviation_sell < 0.90
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (21-60 min) con ma50 > and 3<16 (no incrocio 3-13) and deviation_sell 0.30 - 0.90 ELASTICO ALLA RONALDO - riga 1303"
                    action = "sell"

                    
                elif (
                    ma50_last > ma50_2_min_ago
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell > 0.91
                    and deviation_sell < 1.20
                    # deviation_sell = ma3_last/last_trade_price
                ):
                    sell = "SELL (21-60 min) con ma50 > and incrocio 3-39 and deviation_sell 0.91 - 1.20 - riga 1314"
                    action = "sell"
                
                
                
                
                
                
                elif (
                    ma50_last > ma50_2_min_ago
                    and (ma3_prev > ma45_prev and ma3_last < ma45_last)
                    and deviation_sell > 1.21
                ):
                    sell = "SELL (21-60 min) con ma50 > and incrocio 3-45 and deviation_sell > 1.21 - riga 1327"
                    action = "sell"
                    
                    
                    
                    
                    
                    

                ##################################################################### con trend discendente
                elif (
                    ma50_last < ma50_2_min_ago
                    and deviation_ma39 < -0.15 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                    
                    #and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    
                ):
                    sell = "SELL (21-60 min) con ma50 < and deviation_ma39 < -0.15 or (deviation_sell < 0.10 and ma3_last < ma39_last) - riga 1344"
                    action = "sell"
                
                
                
                
                
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma78_prev and ma3_last < ma78_last) and deviation_sell < -0.37
                  
                ):
                    sell = "SELL (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - riga 1356"
                    action = "sell"
                
                
                
                
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                    and deviation_sell < -0.27
                    # viva sant' antonio !
                    # NON INCROCERANNO MAI DURANTE IL CROLLO !
                    # non toccare ! INCROCIO 3-100 CUSCINO DI SANT' ANTONIO !
                ):
                    sell = "SELL (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - riga 1370"
                    action = "sell"
                
                
                
                
                
                # -------------------------------------------------------------------------------------- guadagno durante il crollo
                
               
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                    and deviation_sell > 0.23
                ):
                    sell = "SELL eventuale guadagno durante il crollo (21-60 min) con ma50 < incrocio 3 - 18 and deviation_sell > 0.23 - riga 1385"
                    action = "sell"

                    
                    
                
                
                
                
                
                    
            ##############################################################################################################################     da 60 a 90 min
            
            
            # VENDITA - da 60 a 90 min - da 3600 a 5400 secondi in poi
            elif seconds_since_last_trade > 3600 and seconds_since_last_trade <= 5400:
            

                if (
                    ma50_last > ma50_2_min_ago
                    and deviation_ma39 < -0.18 or (deviation_sell < 0.10 and ma3_last < ma50_last)
                   
                ):
                    sell = "SELL da 60 a 90 min con ma50 > and deviation_ma39 <-0.18 (no ma3<ma39) (NO INCROCIO!) (NO and deviation_sell < 0.10 (!)) - riga 1408"
                    action = "sell"
                    # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                    # cuscino dell' angelo custode
                   
                
                
                
                
                elif (
                    ma50_last > ma50_2_min_ago
                    and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                    and deviation_sell > 0.35
                    and deviation_sell < 0.80
                ):
                    sell = "SELL dopo 60 min con ma50 > and incrocio 3-13 and deviation_sell 0.35 - 0.80 RABONA ALLA RONALDO (fatto con ma15 invece che con ma13) - riga 1423"
                    action = "sell"

                
                
                
                elif (
                    ma50_last > ma50_2_min_ago
                    and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                    and deviation_sell > 0.81
                    and deviation_sell < 1.49
                ):

                    sell = "SELL da 60 a 90 min con ma50 > and incrocio 3-39 and deviation_sell 0.81 - 1.49 - riga 1436"
                    action = "sell"

                    # ma ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
 

                elif (
                    ma50_last > ma50_2_min_ago
                    and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    and deviation_sell > 1.50
                ):

                    sell = "SELL da 60 a 90 min con ma50 > incrocio 3-33 and deviation_sell > 1.50 - riga 1448"
                    action = "sell"

                
                
                
                
                ######################################################################################## con trend discendente
                elif (
                    ma50_last < ma50_2_min_ago
                    and deviation_ma39 < -0.18
                    #and ma3_last < ma33_last
                    #and deviation_sell < 0.10
                    
                ):
                    sell = "SELL da 60 a 90 min con ma50 < con deviation_ma39 <-0.18 and deviation_sell < 0.10 (no ma3<ma33) (NO INCROCIO!) - riga 1463"
                    action = "sell"
                # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                # cuscino dell' angelo custode
                
                
                
                
                
                elif (
                    ma50_last < ma50_2_min_ago
                    and (ma3_prev > ma78_prev and ma3_last < ma78_last) and deviation_sell < 0.10
                 
                ):
                    sell = "SELL da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < 0.10 - riga 1478"
                    action = "sell"
                
            
            
            
            
            
            
            ################################################################################################################################# > 90 min
            
            # VENDITA - da 90 minuti in poi = da 5400 secondi in poi

            elif seconds_since_last_trade > 5400:

                if (
                    ma50_last > ma50_2_min_ago
                    and deviation_ma39 < -0.18 or (deviation_sell < 0.10 and ma3_last < ma50_last)
                    #and ma3_last < ma39_last
                    #and deviation_ma39 < -0.18
                    #and deviation_sell < 0.10
                ):   
                    sell = "SELL dopo 90 min con ma50 > and deviation_ma39 <-0.18 (no ma3<ma39) or (deviation_sell < 0.10 and ma3_last < ma50_last) - riga 1500"
                    action = "sell"
                    
                    
                    # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                    # dopo 90 min se il prezzo non ha forza puoi anche prendere qualcosa (solo > 90 min)
                    # cuscino dell' angelo custode
                    
                
                
                
                
                elif (
                    ma50_last > ma50_2_min_ago
                    and ma3_last < ma15_last
                    and deviation_sell > 0.35
                    and deviation_sell < 0.69
                ):
                    sell = "SELL >90 min con ma50 > con 3-15 (NO INCROCIO) and deviation_sell 0.35 - 0.69 RABONA ALLA RONALDO (fatto con ma15 invece che con ma13) - riga 1518"
                    action = "sell"

                    
                    
                    
                elif (
                    ma50_last > ma50_2_min_ago
                    and (ma3_prev > ma48_prev and ma3_last < ma48_last)
                    and deviation_sell > 0.70
                    and deviation_sell < 1.49
                ):

                    sell = "SELL dopo 90 min con ma50 > incrocio 3-48 (!) and deviation_sell 0.70 - 1.49 - riga 1531"
                    action = "sell"

                    # ma 3-48 mi evita la ricompra e la rivendita con perdita !

                    
                elif (
                    ma50_last > ma50_2_min_ago
                    and (ma3_prev > ma48_prev and ma3_last < ma48_last)
                    and deviation_sell > 1.50
                ):

                    sell = "SELL dopo 90 min con ma50 > incrocio 3-48 (!) and deviation_sell > 1.50 - riga 1543"
                    action = "sell"

                    
                    
                    
                    
                ######################################################################################## con trend discendente

                elif (
                    ma50_last < ma50_2_min_ago
                    and deviation_ma39 < -0.18 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                    #and ma3_last < ma33_last
                    #and deviation_ma39 < -0.18
                    #and deviation_sell < 0.10
                    
                ):
                    sell = "SELL dopo 90 min con ma50 < con deviation_ma39 <-0.18 or (deviation_sell < 0.10 and ma3_last < ma39_last) - riga 1560"
                    action = "sell"
                # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                # dopo 90 min se il prezzo non ha forza puoi anche prendere qualcosa (solo > 90 min
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
        
        
        # vai compaaaaaaaaaaaa



