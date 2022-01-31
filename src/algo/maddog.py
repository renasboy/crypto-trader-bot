class maddog:
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
        ma69_last, ma69_prev = self.algo_helper.ma_last_prev(69)
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
        
        ma30_10_min_ago = self.algo_helper.ma_minutes_ago(30, 10)
        ma30_20_min_ago = self.algo_helper.ma_minutes_ago(30, 20)
        ma30_30_min_ago = self.algo_helper.ma_minutes_ago(30, 30)
        ma30_40_min_ago = self.algo_helper.ma_minutes_ago(30, 40)
        
        ma33_5_min_ago = self.algo_helper.ma_minutes_ago(33, 5)
        ma39_2_min_ago = self.algo_helper.ma_minutes_ago(39, 2)
        ma39_3_min_ago = self.algo_helper.ma_minutes_ago(39, 3)
        ma50_2_min_ago = self.algo_helper.ma_minutes_ago(50, 2)
        ma69_2_min_ago = self.algo_helper.ma_minutes_ago(69, 2)
        ma72_2_min_ago = self.algo_helper.ma_minutes_ago(72, 2)
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

        # PREZZO di X MINUTI FA (di mercato)
        price_2_min_ago = self.algo_helper.price_minutes_ago(2)
        price_10_min_ago = self.algo_helper.price_minutes_ago(10)
        price_15_min_ago = self.algo_helper.price_minutes_ago(15)
        price_20_min_ago = self.algo_helper.price_minutes_ago(20)

        ###################################################################################################################################################### TEMPO
        ######################################################################################################################################################

        # importante : dolce attesa

        # VENDE DOPO x SECONDI - ro cano torna a casa - (ma c'e' anche un "e se")
        max_hold_time_in_seconds = 300
        #  5 minuti * 60 = 300

        #########################################################################################################################################################
        #########################################################################################################################################################

        #                                                         T U T T E    L E   D E V I A T I O N  !

        ##############################################################################################################

        # formula DEVIATION_1_gabbia
        deviation_1_gabbia = (ma8_last / ma50_last - 1) * 100 if ma50_last else 0
        self.algo_helper.info("deviation_1_gabbia: {}".format(deviation_1_gabbia))

        ##################################################################################################################

        # formula deviation
        deviation = (ma4_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.info("deviation: {}".format(deviation))

        # formula DEVIATION_ma13_sopra_ma25
        deviation_ma13_sopra_ma25 = (
            (ma13_last / ma25_last - 1) * 100 if ma25_last else 0
        )
        self.algo_helper.info(
            "deviation_ma13_sopra_ma25: {}".format(deviation_ma13_sopra_ma25)
        )

        # formula DEVIATION_bellissima
        deviation_bellissima = (ma6_last / ma30_last - 1) * 100 if ma30_last else 0
        self.algo_helper.info("deviation_bellissima: {}".format(deviation_bellissima))

        
        ############# deviation per comprare con un RIALZO IMPROVVISO DOPO UN PERIODO LATERALE
        
        
        # 12 gennaio 2022 la ma2 arriva tardi ! DEVIATION RIALZO IMPROVVISO per adesso solo su RCCR
        
        
        # formula DEVIATION_RIALZO_IMPROVVISO (per 40 min si muove in un range +0.25 -0.25 sintetizzato dalla ma30
        deviation_rialzo_improvviso_1 = (price / ma30_last - 1) * 100 if ma30_last else 0
        self.algo_helper.info("deviation_rialzo_improvviso_1: {}".format(deviation_rialzo_improvviso_1))
        
        deviation_rialzo_improvviso_2 = (price / ma30_10_min_ago - 1) * 100 if ma30_10_min_ago else 0
        self.algo_helper.info("deviation_rialzo_improvviso_2: {}".format(deviation_rialzo_improvviso_2))
        
        deviation_rialzo_improvviso_3 = (price / ma30_20_min_ago - 1) * 100 if ma30_20_min_ago else 0
        self.algo_helper.info("deviation_rialzo_improvviso_3: {}".format(deviation_rialzo_improvviso_3))
        
        deviation_rialzo_improvviso_4 = (price / ma30_30_min_ago - 1) * 100 if ma30_30_min_ago else 0
        self.algo_helper.info("deviation_rialzo_improvviso_4: {}".format(deviation_rialzo_improvviso_4))
        
        
        
        
        deviation_range_1 = (ma30_last / ma30_10_min_ago - 1) * 100 if ma30_10_min_ago else 0
        self.algo_helper.info("deviation_range_1: {}".format(deviation_range_1))
        
        deviation_range_2 = (ma30_10_min_ago / ma30_20_min_ago - 1) * 100 if ma30_20_min_ago else 0
        self.algo_helper.info("deviation_range_2: {}".format(deviation_range_2))
        
        deviation_range_3 = (ma30_20_min_ago / ma30_30_min_ago - 1) * 100 if ma30_30_min_ago else 0
        self.algo_helper.info("deviation_range_3: {}".format(deviation_range_3))
        
        deviation_range_4 = (ma30_30_min_ago / ma30_40_min_ago - 1) * 100 if ma30_40_min_ago else 0
        self.algo_helper.info("deviation_range_4: {}".format(deviation_range_4))
        
        
        deviation_range_x = (ma30_last / ma30_20_min_ago - 1) * 100 if ma30_20_min_ago else 0
        self.algo_helper.info("deviation_range_x: {}".format(deviation_range_x))
        
        
       
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

        # formula delta_buy3_incrocio_ma3_ma8 > 0.10 per la compra 3
        delta_buy3_incrocio_ma3_ma8 = (ma3_last / ma8_last - 1) * 100 if ma8_last else 0
        self.algo_helper.info(
            "delta_buy3_incrocio_ma3_ma8: {}".format(delta_buy3_incrocio_ma3_ma8)
        )

        # formula DEVIATION_buy per comprare UN PO' PIU' SOPRA DEL LAST TRADE ( di solito l' ultimo SELL )
        deviation_buy = (
            (ma2_last / last_trade_price - 1) * 100 if last_trade_price else 0
        )
        self.algo_helper.info("deviation_buy: {}".format(deviation_buy))

        ############################################################################################     DEVIATION_buy_crollo

        # formula DEVIATION_buy_crollo_1 per comprare a una certa distanza da ma78
        deviation_buy_crollo_1 = (ma8_last / ma78_last - 1) * 100 if ma78_last else 0
        self.algo_helper.info(
            "deviation_buy_crollo_1: {}".format(deviation_buy_crollo_1)
        )

        # formula DEVIATION_buy_crollo_2 per comprare a una certa distanza da ma13
        deviation_buy_crollo_2 = (ma3_last / ma13_last - 1) * 100 if ma13_last else 0
        self.algo_helper.info(
            "deviation_buy_crollo_2: {}".format(deviation_buy_crollo_2)
        )

        ############################################################################################################################
        # formula DEVIATION_buy_ma2_sopra_ma13 per comprare a una certa distanza da ma13
        deviation_buy_ma2_sopra_ma13 = (ma2_last / ma13_last - 1) * 100 if ma13_last else 0
        self.algo_helper.info("deviation_buy_ma2_sopra_ma13: {}".format(deviation_buy_ma2_sopra_ma13))
        
        # formula DEVIATION_buy_ma3_sopra_ma13 per comprare a una certa distanza da ma13
        deviation_buy_ma3_sopra_ma13 = (
            (ma3_last / ma13_last - 1) * 100 if ma13_last else 0
        )
        self.algo_helper.info(
            "deviation_buy_ma3_sopra_ma13: {}".format(deviation_buy_ma3_sopra_ma13)
        )

        # formula DEVIATION_ma4_sopra_ma30
        deviation_ma4_sopra_ma30 = (ma4_last / ma30_last - 1) * 100 if ma30_last else 0
        self.algo_helper.info(
            "deviation_ma4_sopra_ma30: {}".format(deviation_ma4_sopra_ma30)
        )

        # formula deviation_ma7_sopra_ma40
        deviation_ma7_sopra_ma40 = (ma7_last / ma40_last - 1) * 100 if ma40_last else 0
        self.algo_helper.info(
            "deviation_ma7_sopra_ma40: {}".format(deviation_ma7_sopra_ma40)
        )

        # formula deviation_ma3_sopra_ma7 (solo per il BUY1)
        deviation_ma3_sopra_ma7 = (ma3_last / ma7_last - 1) * 100 if ma7_last else 0
        self.algo_helper.info(
            "deviation_ma3_sopra_ma7: {}".format(deviation_ma3_sopra_ma7)
        )

        ########################################################################################################################## deviation per vendere

        # formula DEVIATION_sell
        deviation_sell = (
            (ma4_last / last_trade_price - 1) * 100 if last_trade_price else 0
        )
        self.algo_helper.info("deviation_sell: {}".format(deviation_sell))

        # formula DEVIATION_sell_ma78
        deviation_sell_ma78 = (ma4_last / ma78_last - 1) * 100 if ma78_last else 0
        self.algo_helper.info("deviation_sell_ma78: {}".format(deviation_sell_ma78))

        # formula deviation_ma39 per vendere un po' piu' giu' di ma39
        deviation_ma39 = (ma4_last / ma39_last - 1) * 100 if ma39_last else 0
        self.algo_helper.info("deviation_ma39: {}".format(deviation_ma39))
        
        
        # formula deviation_ma25 per vendere un po' piu' giu' di ma25 (per il buy 3-4-5 con ma 39 ha fatto -0.89 !)
        deviation_ma25 = (ma3_last / ma25_last - 1) * 100 if ma25_last else 0
        self.algo_helper.info("deviation_ma25: {}".format(deviation_ma25))
        

        ######################################################################################################## TUTTO COMINCIA DA QUA !
        # dal non fare niente !

        # DEFAULT ACTION DICE DI NON FARE NIENTE (= None, NON TOCCARE )
        action = None
        percentage = 0

        ######################################################################################################## APRE E CHIUDE LA GABBIA !

        # SE LA GABBIA E' TROPPO APERTA IMPAZZISCE NEI MOVIMENTI LATERALI !
        # entrano in azione buy 2-3-4-5 che sono piu' reattivi del BUY 1 !

        # APRE E CHIUDE GABBIA

        if deviation_1_gabbia > -0.29 or deviation_buy_crollo_1 < -1.50:
        #if deviation_1_gabbia > -0.29 or deviation_buy_crollo_1 < -1.50 or (-1.50 < deviation_buy_crollo_1 < -0.60):     CHIEDERE AL COMPARE 1
        
        
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
            ###########################################################################################################################################
            #   B U Y
           
            ###########################################################################################################################################
            percentage = self.buy_percentage
            # NON TOCCARE  ! DI DEFAULT E' IL 2%
            
            ###########################################################################################################################################
            ###########################################################################################################################################
            
            # in futuro
         
            # MACD sempre con aggiunta di ma 13-25 (come studio) (III° cane)
            # TOGLIERE TUTTI GLI INCROCI AL BUY ! se 13 > 100 NON INCROCERA' MAI ! INCROCIO 13-100 DIVENTA 13>100 !
            # analisi dei dati !
          
            ######################################################################################################## COMPRA sessione 1
            # BUY 1 con "percentage" 20
            if self.session == 1:

                # ------------------------------------------------------------ BUY 1 DURANTE IL RIALZO con INCROCIO CLASSICO 69-100

                if (
                    ma69_last > ma100_last
                    and ma13_last > ma78_last
                    and deviation_bellissima > 0.18
                    and ma2_last > ma2_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                    and ma6_last > ma100_last
                    and ma6_last > ma39_last
                    and ma6_last > ma13_last
                    
                    # deviation_bellissima = ma6_last / ma30_last
                    # and deviation_ma13_sopra_ma25 > 0.07 TOLTA PROVVISORIAMENTE vedi BUY ore 10:47 del 23 nov 2021 (E' ARRIVATA MOLTO TARDI)
                ):

                    buy = "BUY 1 con 69 > 100 and deviation_bellissima > 0.163 riga 345"
                    action = "buy"
                    percentage = 20

                ####################################################################  BUY 1 con incrocio 13-69 and ma72_last >= ma72_2_min_ago  "MI PIACE!"

                elif (
                    ma13_last > ma69_last
                    and ma69_last >= ma69_2_min_ago
                    and deviation_bellissima > 0.17
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma3_3_min_ago
                    and ma4_last > ma4_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                    and deviation_ma13_sopra_ma25 > 0.07
                    # quando 13-100 si incrociano price ma2 e ma4 sono gia' in ribasso
                ):
                    buy = "BUY 1 con 13>69 e ma69> 2 min ago (!) riga 363"
                    action = "buy"
                    percentage = 20
                elif (
                    deviation_buy1 > 0.25
                    and ma13_last > ma50_last
                    and ma78_last > ma78_2_min_ago
                    and deviation_bellissima > 0.18
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma4_last > ma4_2_min_ago
                ):
                    buy = "BUY 1 con 13>50 and DEVIATION BUY 1 ALTA e ma78> - riga 378"
                    action = "buy"
                    percentage = 20
                elif (
                    ma78_last < ma78_2_min_ago
                    and ma39_last > ma78_last
                    and deviation_buy1 > 0.14
                    and deviation_bellissima > 0.17
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma4_last > ma4_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                ):
                    buy = "BUY 1 con ma78< and 39>78 and DEVIATION BUY 1 BASSA riga 431"
                    action = "buy"
                    percentage = 10
                elif (
                    ma78_last < ma78_2_min_ago
                    and ma39_last > ma78_last
                    and deviation_bellissima > 0.17
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma4_last > ma4_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                    and deviation_ma13_sopra_ma25 > 0.05
                ):

                    buy = "se ma78< - BUY 1 con incrocio 39>78 - riga 448"
                    action = "buy"
                    percentage = 10
                    # deviation_buy1 = ma13_last/ma39_last
                    # and deviation_ma13_sopra_ma25 > 0.05 FONDAMENTALE
                
                
                ##############################################################################################################################
                # IMPORTANTISSIMO ! - PER COMPRARE DURANTE IL CROLLO - compa prega per me - ( cruise - david gilmour )
                ##############################################################################################################################

                # entriamo nell' area dell' ipervenduto, compa !
                # QUI LASCIO GLI INCROCI !
                # BUY  PRIMO MODO DURANTE IL CROLLO
                

                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -2.30
                    and ma3_last > ma7_last
                ):
                    buy = "BUY DURANTE IL CROLLO - modo 1 riga 469"
                    action = "buy"
                    percentage = 20
                    # deviation_buy_crollo_1 = ma8_last / ma78_last

                # BUY SECONDO MODO - DURANTE IL CROLLO - questa condizione e' entrata in azione ! ( e mi e' sembrata ben fatta !)

                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -1.70
                    and deviation_buy_crollo_2 > 0.11
                ):
                    buy = "BUY DURANTE IL CROLLO - modo 2 riga 481"
                    action = "buy"
                    percentage = 20
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_buy_crollo_2 = ma3_last / ma13_last
                    
                    
                    
                ########################################################################################################### compra durante un rialzo improvviso ! 
                ########################################################################################################### con ma30 che ha 40 min di andamento laterale
                ########################################################################################################### PER ADESSO SOLO SUL BUY 1
                elif (    
                    deviation_rialzo_improvviso_1 > 0.32
                    and deviation_rialzo_improvviso_2 > 0.20
                    and deviation_rialzo_improvviso_3 > 0.20
                    and deviation_rialzo_improvviso_4 > 0.20
                    
                    
                    and deviation_range_1 < 0.20
                    and deviation_range_1 > -0.20
                    and deviation_range_2 < 0.20
                    and deviation_range_2 > -0.20
                    and deviation_range_3 < 0.20
                    and deviation_range_3 > -0.20
                    and deviation_range_4 < 0.20
                    and deviation_range_4 > -0.20
                    and deviation_range_x < 0.20
                    and deviation_range_x > -0.20
                   
                    # deviation_range_x va da 0 a -20 min
                    # teoricamente potresti usare solo la deviation_range !
                    # con deviation_rialzo_improvviso_5 > 0.20 non parte il BUY se trend leggermente ribassista
                ):

                    buy = "BUY 1 RIALZO IMPROVVISO con 0.32 da 0.20 per evitare falsi acquisti guardando anche il 6-30 - riga 411"
                    action = "buy"
                    percentage = 10
                    # deviation_buy1 = ma13_last/ma39_last
                
                ######################################################################################################## per comprare durante un ribasso che non e' un crollo
                """                
                #BUY DURANTE UN RIBASSO CHE NON E' UN CROLLO ! (compare stammi vicino!)                                 CHIEDERE AL COMPARE 3
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -0.60
                    and deviation_buy_crollo_1 > -1.50
                    and deviation_bellissima > 0.17
                ):
                    buy = "BUY DURANTE UN RIBASSO che non e' un crollo ! and deviation_bellissima > 0.17 -  riga 495"
                    action = "buy"
                    percentage = 20
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                """

            #############################################################################################################      COMPRA sessione 2 
            elif self.session == 2:

                if (
                    ma78_last > ma78_2_min_ago
                    and deviation_buy2 > 0.05
                    and deviation_bellissima > 0.12
                    and deviation_buy_ma3_sopra_ma13 > 0.09
                    and deviation_ma7_sopra_ma40 > 0.075
                    and ma2_last > ma2_2_min_ago
                    and price > price_2_min_ago
                    and ma3_last > ma40_last
                ):
                    buy = "BUY 2A riga 514"
                    action = "buy"
                    percentage = 70

                    # deviation_buy_ma3_sopra_ma13 > x e' fondamentale !
                    # deviation_buy2 = ma8_last/ma50_last
                
                
                elif (
                    ma78_last < ma78_2_min_ago
                    and deviation_buy2 > 0.07
                    and deviation_bellissima > 0.12
                    and deviation_ma13_sopra_ma25 > 0.06
                    and deviation_buy_ma3_sopra_ma13 > 0.09
                    and deviation_ma7_sopra_ma40 > 0.10
                    and ma2_last > ma2_2_min_ago
                    and price > price_2_min_ago
                    and ma3_last > ma40_last
                ):
                    buy = "BUY 2B riga 533"
                    action = "buy"
                    percentage = 50
                    # deviation_buy_ma3_sopra_ma13 > x e' fondamentale !
                    # deviation_buy2 = ma8_last/ma50_last

                    
                    
                elif (
                    deviation_buy2 > 0.13
                    and deviation_bellissima > 0.12
                    and deviation_buy_ma3_sopra_ma13 > 0.10
                    and deviation_ma7_sopra_ma40 > 0.14
                    and ma4_last > ma9_last
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma40_last
                    and ma4_last > ma78_last
                ):
                    buy = "BUY 2C riga 551"
                    action = "buy"
                    percentage = 50
                    # deviation_buy2 = ma8_last / ma50
                    
                    
                ############################################################################################################ BUY 2 DURANTE IL CROLLO CHE CONTINUA    
                # se il crollo continua dopo che ha venduto sell 1 durante il crollo - ro cano CI RIPROVA !     
                
                # BUY  PRIMO MODO DURANTE IL CROLLO

                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -2.30
                    and ma3_last > ma7_last
                ):
                    buy = "BUY DURANTE IL CROLLO - modo 1 riga 469"
                    action = "buy"
                    percentage = 20
                    # deviation_buy_crollo_1 = ma8_last / ma78_last

                # BUY SECONDO MODO - DURANTE IL CROLLO - questa condizione e' entrata in azione ! ( e mi e' sembrata ben fatta !)

                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -1.70
                    and deviation_buy_crollo_2 > 0.11
                ):
                    buy = "BUY DURANTE IL CROLLO - modo 2 riga 481"
                    action = "buy"
                    percentage = 20
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_buy_crollo_2 = ma3_last / ma13_last
                
                
                ######################################################################################################## per comprare durante un ribasso che non e' un crollo
                """                
                #BUY DURANTE UN RIBASSO CHE NON E' UN CROLLO ! (compare stammi vicino!)                                 CHIEDERE AL COMPARE 3
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -0.60
                    and deviation_buy_crollo_1 > -1.50
                    and deviation_bellissima > 0.17
                ):
                    buy = "BUY DURANTE UN RIBASSO che non e' un crollo ! and deviation_bellissima > 0.17 -  riga 495"
                    action = "buy"
                    percentage = 20
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                """
            
            
            
            ############################################################################################################ COMPRA sessione 3

            elif self.session == 3:

                if (
                    ma78_last >= ma78_2_min_ago
                    and deviation_buy3 > 0.12
                    and deviation_buy_ma2_sopra_ma13 > 0.16
                    and ma3_last > ma13_last
                    and deviation_ma4_sopra_ma30 > 0.15
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                ):
                    buy = "BUY 3A con ma78 > riga 570"
                    action = "buy"
                    percentage = 50

                    # deviation_buy3 = ma4_last/ma30_last
              
                elif (
                    deviation_buy3 > 0.02
                    and ma39_last > ma78_last
                    and deviation_buy3 > 0.02
                    and delta_buy3_incrocio_ma3_ma8 > 0.06
                    and deviation_ma4_sopra_ma30 > 0.15
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                ):
                    buy = "BUY 3B RIVOLUZIONARIO se ma39 > ma78- riga 588"
                    action = "buy"
                    percentage = 50
                    # deviation_buy3 = ma4_last/ma30_last
                    # riga 462 potrebbe esserci un problema perche' ho tolto ma78_last >= ma78_2_min_ago. vediamo

                elif (
                    ma78_last < ma78_2_min_ago
                    and deviation_buy3 > 0.03
                    and deviation_ma13_sopra_ma25 > 0.040
                    and delta_buy3_incrocio_ma3_ma8 > 0.07
                    and deviation_ma4_sopra_ma30 > 0.15
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                ):
                    buy = "BUY 3C RIVOLUZIONARIO se ma78 < - riga 606"
                    action = "buy"
                    percentage = 40
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
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                ):
                    buy = "BUY 4A con ma 78 > riga 626"
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
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                ):
                    buy = "BUY 4B RIVOLUZIONARIO con ma78 > - riga 641"
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
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                ):
                    buy = "BUY 4C RIVOLUZIONARIO con ma78 < - riga 657"
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
                    and deviation_ma7_sopra_ma40 > 0.11
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                    and ma6_last > ma15_last
                    and ma7_last > ma25_last
                    and deviation_bellissima > 0.12
                    
                    # deviation_bellissima = 6/30
                    # spezzare la catena dei buy - effetti laterali !
                    # se e' arrivato il buy 5 e' molto probabile che il trend sia consolidato
                    # e, a questo punto, non importa se compra con un + 0.10 piu' in alto. NON FA UNA GRANDE DIFFERENZA !
                ):
                    buy = "BUY 5A con ma78 > and deviation_bellissima > 0.163 (PER SPEZZARE LA CATENA -effetti laterali) riga 685"
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
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                    and deviation_bellissima > 0.163
                ):
                    buy = "BUY 5B RIVOLUZIONARIO con ma78 > and deviation_bellissima > 0.163 (PER SPEZZARE LA CATENA -effetti laterali) - riga 701"
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
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                    and deviation_bellissima > 0.163
                ):
                    buy = "BUY 5C RIVOLUZIONARIO con ma78 < and deviation_bellissima > 0.163 - riga 719"
                    action = "buy"
                    percentage = 50
                    # deviation_buy3 = ma4_last/ma30_last

        ############################################################################################

        #  V E N D I T A !                                                                           nota per il compa : la vendita e' fatta con 3 sessioni e 5 eccezioni

        ############################################################################################

        # NON TOCCARE QUESTE RIGHE (DICE CHE STA IN MODO SELL, DEVO VENDERE !)

        elif last_trade_action == "buy":

            percentage = self.sell_percentage
            # E' 100 DI DEFAULT !

            ###################################################################################################################################
            ###################################################################################################################################

            # VENDITA CON SESSIONE 1-2-3-x

            # LA PRIMA VENDITA DOPO IL BUY 1 E' COMPLETAMENTE DIVERSA E PIU' REATTIVA !
            # LA SECONDA VENDITA "PIU' TRANQUILLA"
            # DALLA TERZA VENDITA IN POI COME PER LA PRIMA SI VENDE EVITANDO, SE POSSIBILE, UNA GRANDE PERDITA

            ###################################################################################################################################
            ###################################################################################################################################

            # sell sessione 1 .................... righe  706 - 1593 
            # sell sessione 2 .................... righe 1604 - 2489
            # sell sessione 3-4-x ................ righe 2500 - 3386

            # VENDITA - con fasce di tempo ! minuti

            #   0 -  3
            #   3 -  5
            #   5 - 12
            #  12 - 21
            #  21 - 40
            #  40   60
            #  60   90
            #   > 90

            # < -0.10  ma78 che mi salva (nel movimento laterale mi fa perdere la meta')
            # < -0.20
            # 0.25 - 0.59
            # 0.60 - 0.79
            # 0.80 - 1.20
            # > 1.21

            ####################################################################################################################### SESSIONE 1
            
            # al SELL 1 PUOI AUMENTARE LA PERDITA TOLLERATA POICHE' HAI SOLO IL 10%-20% DEL CAPITALE - eviterai un po' di sell e buy nel movimenti laterali !
            # la perdita tollerata ovviamente va aumentata anche alle 5 vendite eccezonali del SELL 1 sperando che la nuova indentazione ha funzionato
            # fino a questo momento vendevano SOLO le ULTIME 5 condizioni eccezionali 
            
            ####################################################################################################################### sessione 1 ( 0 - 3 min )

            if self.session == 1:

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
                        sell = "sessione 1 SELL (0-3 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.23 - riga 789"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.25
                        and deviation_sell < 0.60
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 1 SELL (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.25 - 0.60 - riga 799"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.61
                        and deviation_sell < 0.79
                    ):
                        sell = "sessione 1 SELL (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.61 - 0.79 - riga 808"
                        action = "sell"

                    # attenzione : tacco di allah e dribbling alla ronaldo SOLO con ma50> (altrimenti si attivano in "sell durante il crollo" che ha le sue dinamiche.)

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 0.80
                        and deviation_sell < 1.20
                    ):

                        sell = "sessione 1 SELL (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell 0.80 - 1.20 ( TACCO DI ALLAH !) - riga 820"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 1.21
                    ):

                        sell = "sessione 1 SELL (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell > 1.21 (DRIBBLING ALLA RONALDO !)- riga 829"
                        action = "sell"

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                    ):
                        sell = "sessione 1 SELL (0-3 min) con ma50 < and incrocio 3-28- riga 839"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                    ):
                        sell = "sessione 1 SELL (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 - riga 849"
                        action = "sell"

                    # ---------------------------------------------------------------------------------------------------------------------- crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell < -0.50
                    ):
                        sell = "sessione 1 SELL CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - riga 859"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                    ):
                        sell = "sessione 1 SELL CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 869"
                        action = "sell"

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                        and deviation_sell > 0.60
                    ):

                        sell = "sessione 1 SELL CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - riga 878"
                        action = "sell"

                ################################################################################################################################ sessione 1 ( 3-5 min )

                # VENDITA - da 3 a 5 minuti = da 180 a 300 secondi

                elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 300:

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell < -0.24
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 1 SELL (3-5 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.24 - riga 893"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma9_last
                        and deviation_sell > 0.25
                        and deviation_sell < 0.90
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 1 SELL (3-5 min) con ma50 > and 3<9 (no incrocio 3-9) and deviation_sell 0.25 - 0.90 - DRIBBLING ALLA RONALDO - riga 903"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                    ):
                        sell = "sessione 1 SELL (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 912"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                    ):
                        sell = "sessione 1 SELL (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - riga 920"
                        action = "sell"

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        # deviation_sell_ma78 = ma3_last / ma78_last
                    ):
                        sell = "sessione 1 SELL (3-5 min) con ma50 < and incrocio 3-28 - riga 931"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                    ):
                        sell = "sessione 1 SELL (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.23 - riga 941"
                        action = "sell"

                    # ---------------------------------------------------------------------------------------------------------------------- guadagno con crollo
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                    ):
                        sell = "sessione 1 SELL GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 950"
                        action = "sell"

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                    ):
                        sell = "sessione 1 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 958"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE

                ################################################################################################################################### sessione 1 ( 5-12 min )

                # VENDITA - da 5 a 12 minuti = da 300 a 720 secondi

                elif seconds_since_last_trade > 300 and seconds_since_last_trade <= 720:

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.41
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 1 SELL (5-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - riga 975"
                        action = "sell"

                    # guardare la stella (guardare da una stella!)
                    # QUESTO E' IL RISCHIO PIU' GRANDE CHE PRENDO ! ( ma con ma50 > ma50 2 min ago DOPO 5 min (+2))

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.25
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 1 SELL (5-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - riga 987"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma9_last
                        and deviation_sell > 0.25
                        and deviation_sell < 0.90
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 1 SELL (5-12 min) con ma50 >  3<9 and deviation_sell 0.25 - 0.90 - DRIBBLING ALLA RONALDO - riga 997"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 1 SELL (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 1007"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                    ):
                        sell = "sessione 1 SELL (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - riga 1015"
                        action = "sell"

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                    ):
                        sell = "sessione 1 SELL 12 (5-12 min) con ma50 < and incrocio 3-28 - riga 1025"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.36
                    ):
                        sell = "sessione 1 SELL 12 (5-12 min) con ma50 < and incrocio 3-100 (cuscino di sant' antonio) - riga 1035"
                        action = "sell"

                    # ------------------------------------------------------------------------------- guadagno con crollo
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                    ):
                        sell = "sessione 1 SELL guadagno con crollo (5-12 min) con ma50 < and incrocio 3-23 - riga 1044"
                        action = "sell"

                    # ------------------------------------------------------------------------------------------------------------ PARACADUTE crollo
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                    ):
                        sell = "sessione 1 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 1053"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE

                ############################################################################################################################  SESSIONE 1 ( 12-21 min )

                # VENDITA - da 12 a 21 minuti = da 720 a 1260 secondi

                elif (
                    seconds_since_last_trade > 720 and seconds_since_last_trade <= 1260
                ):

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma72_prev and ma3_last < ma72_last)
                        and deviation_sell < -0.65
                        # and deviation_ma39 < -0.29 vendeva troppo presto
                        # ATTENZIONE "and (ma3_prev > ma39_prev and ma3_last < ma39_last)" con ma39 NON HA INCROCIATO
                        # and deviation_sell < -0.30
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 1 SELL (12-21 min) con ma50 > and incrocio 3-72 and deviation sell -0.65 e vaffanculo ! - riga 1075"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma100_prev and ma3_last < ma100_last)
                        and deviation_sell < -0.36
                        # viva sant' antonio !
                    ):
                        sell = "sessione 1 SELL (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.36 - riga 1084"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma13_last
                        and deviation_sell > 0.25
                        and deviation_sell < 0.90
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 1 SELL (12-21 min) con ma50> and 3<13 (NO INCROCIO 3-13) and deviation_sell 0.25-0.90 -DOPPIO PASSO ALLA RONALDO - riga 1094"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 1 SELL (12-21 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 1104"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell > 1.21
                    ):
                        sell = "sessione 1 SELL (12-21 min) con ma50 > and incrocio 3-39 and deviation_sell > 1.21 - riga 1112"
                        action = "sell"

                    ##########################################################################################
                    # NON TOCCARE ! CUSCINO DI SANT' ANTONIO !
                    # L' INCROCIO 5-100 MI SALVA ! MA 5<100 VENDE DURANTE IL RIBASSO !
                    ##################################################################### con trend discendente

                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.15
                        # and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        # and deviation_sell < -0.25
                    ):
                        sell = "sessione 1 SELL (12-21 min) con ma50 < and deviation_ma39 < -0.15 - riga 1126"
                        action = "sell"

                        # ATTENZIONE QUESTA aveva FATTO -0.61% !
                        # QUINDI ho abbassato da 0.17 a 0.16 a 0.15
                        # HO NOTATO CHE ANCHE INCROCIO 5-100 SAREBBE ARRIVATO TARDI
                        # ALLORA METTO incrocio 3-78 e deviation <0.10

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.45
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50< !
                    ):
                        sell = "sessione 1 SELL (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - riga 1140"
                        action = "sell"

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        # viva sant' antonio !
                        # incrocio 5-100 no 5<100 altrimenti vende durante il crollo !
                    ):
                        sell = "sessione 1 SELL (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - riga 1150"
                        action = "sell"

                    # --------------------------------------------------------------------------------- PARACADUTE crollo
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                    ):
                        sell = "sessione 1 PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 1159"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE

                    # ----------------------------------------------------------------------------- guadagno con crollo
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.23
                    ):
                        sell = "sessione 1 SELL eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3 - 18 and deviation_sell > 0.23 - riga 1170"
                        action = "sell"

                ################################################################################################################################## SESSIONE 1 ( 21-60 min )

                # VENDITA - da 21 a 60 minuti = da 1261 a 3600 secondi

                elif (
                    seconds_since_last_trade > 1261 and seconds_since_last_trade <= 3600
                ):

                    if (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.65
                        or (deviation_sell < -0.19 and ma3_last < ma50_last)
                        and ma2_last < ma2_2_min_ago
                        # and (ma3_prev > ma78_prev and ma3_last < ma78_last) and deviation_sell < -0.65 or (deviation_sell < 0.10 and ma3_last < ma50_last)
                        # and deviation_ma39 < -0.16 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        # and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        # and deviation_sell < -0.26
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 1 SELL (21-60 min) con ma50> and incrocio 3-78 and deviation_sell<-0.65 or (deviation_sell <-0.19 and ma3_last < ma50_last) - riga 1193"
                        action = "sell"

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.26
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 1 SELL (21-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.26 - riga 1202"
                        action = "sell"

                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma15_last
                        and deviation_sell > 0.32
                        and deviation_sell < 0.90
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 1 SELL (21-60 min) con ma50 > and 4 < 15 (no incrocio 3-13) and deviation_sell 0.32 - 0.90 ELASTICO ALLA RONALDO - riga 1212"
                        action = "sell"
                        # dopo 26 minuti non c'e' piu' quello scatto in avanti - dribbling- che si verifica nei primi minuti

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 1 SELL (21-60 min) con ma50 > and incrocio 3-13 and deviation_sell 0.91 - 1.20 - riga 1223"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 1.21
                        and deviation_sell < 2.70
                    ):
                        sell = "sessione 1 SELL (21-60 min) con ma50 > and incrocio 3-11 and deviation_sell 1.21 - 2.70 - riga 1233"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma9_prev and ma3_last < ma9_last)
                        and deviation_sell > 2.71
                    ):
                        sell = "sessione 1 SELL (21-60 min) con ma50 > and incrocio 3-9 and deviation_sell > 2.71 - riga 1242"
                        action = "sell"

                    ##################################################################### con trend discendente
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.24
                        or deviation_sell < -0.25
                        # and deviation_ma39 < -0.15 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                       
                    ):
                        sell = "sessione 1 SELL (21-60 min) con ma50 < and deviation_ma39 < -0.24 or deviation_sell < -0.25 - riga 1253"
                        action = "sell"

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.37
                    ):
                        sell = "sessione 1 SELL (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - riga 1261"
                        action = "sell"

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                       
                    ):
                        sell = "sessione 1 SELL (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - riga 1270"
                        action = "sell"

                    # -------------------------------------------------------------------------------------- guadagno durante il crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.23
                    ):
                        sell = "sessione 1 SELL eventuale guadagno durante il crollo (21-60 min) con ma50 < incrocio 3 - 18 and deviation_sell > 0.23 - riga 1280"
                        action = "sell"
                
                ##############################################################################################################################  SESSIONE 1 ( da 60 a 90 min )

                # VENDITA - da 60 a 90 min - da 3600 a 5400 secondi in poi
                elif (
                    seconds_since_last_trade > 3600 and seconds_since_last_trade <= 5400
                ):

                    if (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        or (deviation_sell < -0.18 and ma3_last < ma50_last)
                    ):
                        sell = "sessione 1 SELL da 60 a 90 min con ma50 > and deviation_ma39 <-0.18 or (deviation_sell < -0.18 and ma3_last < ma50_last)  - riga 1295"
                        action = "sell"
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # cuscino dell' angelo custode

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.35
                        and deviation_sell < 0.80
                    ):
                        sell = "sessione 1 SELL dopo 60 min con ma50> and incrocio 3-13 and deviation_sell 0.35-0.80 RABONA ALLA RONALDO (ma15 invece di ma13) - riga 1306"
                        action = "sell"

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell > 0.81
                        and deviation_sell < 1.49
                    ):

                        sell = "sessione 1 SELL da 60 a 90 min con ma50 > and incrocio 3-39 and deviation_sell 0.81 - 1.49 - riga 1316"
                        action = "sell"

                        # ma ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 1.50
                        and deviation_sell < 2.70
                    ):

                        sell = "sessione 1 SELL da 60 a 90 min con ma50 > incrocio 3-33 and deviation_sell > 1.50 - riga 1329"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                    ):

                        sell = "sessione 1 SELL da 60 a 90 min con ma50 > incrocio 3-11 and deviation_sell > 2.71 - riga 1339"
                        action = "sell"

                    ######################################################################################## con trend discendente
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.18
                      
                    ):
                        sell = "sessione 1 SELL da 60 a 90 min con ma50 < con deviation_ma39 <-0.18 and deviation_sell < 0.10 (no ma3<ma33) (NO INCROCIO!) - riga 1330"
                        action = "sell"
                   
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.15
                    ):
                        sell = "sessione 1 SELL da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < -0.10 - riga 1341"
                        action = "sell"

                ################################################################################################################################# SESSIONE 1 ( > 90 min )

                # VENDITA - da 90 minuti in poi = da 5400 secondi in poi

                elif seconds_since_last_trade > 5400:

                    if (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        or (deviation_sell < 0.10 and ma3_last < ma50_last)
                        # and ma3_last < ma39_last
                        # and deviation_ma39 < -0.18
                        # and deviation_sell < 0.10
                    ):
                        sell = "sessione 1 SELL dopo 90 min con ma50 > and deviation_ma39 <-0.18 (no ma3<ma39) or (deviation_sell < 0.10 and ma3_last < ma50_last) - riga 1358"
                        action = "sell"

                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # dopo 90 min se il prezzo non ha forza puoi anche prendere qualcosa (solo > 90 min)
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma15_last
                        and deviation_sell > 0.35
                        and deviation_sell < 0.69
                    ):
                        sell = "sessione 1 SELL >90 min con ma50 > con 3-15 (NO INCROCIO) and deviation_sell 0.35 - 0.69 RABONA ALLA RONALDO (ma15 invece di ma13) - riga 1371"
                        action = "sell"

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell > 0.70
                        and deviation_sell < 1.49
                    ):

                        sell = "sessione 1 SELL dopo 90 min con ma50 > incrocio 3-39 (!) and deviation_sell 0.70 - 1.49 - riga 1396"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 1.50
                        and deviation_sell < 2.70
                    ):

                        sell = "sessione 1 SELL dopo 90 min con ma50 > incrocio 3-33 and deviation_sell  1.50 - 2.70 - riga 1407"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                    ):

                        sell = "sessione 1 SELL dopo 90 min con ma50 > incrocio 3-11 (!) and deviation_sell > 2.71 - riga 1417"
                        action = "sell"

                    ######################################################################################## con trend discendente

                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        # and ma3_last < ma33_last
                        # and deviation_ma39 < -0.18
                        # and deviation_sell < 0.10
                    ):
                        sell = "sessione 1 SELL dopo 90 min con ma50 < con deviation_ma39 <-0.18 or (deviation_sell < 0.10 and ma3_last < ma39_last) - riga 1430"
                        action = "sell"
                       
            ################################################################################################# SESSIONE 1 ( vendita con questi 5 altri modi )
           
            # MA ATTENZIONE al conflitto durante il crollo - SELL SOVRAPPOSTO AL BUY
            # NO 3<78 !
            # NO deviation 78 !
            # QUALCHE VOLTA ma3-ma39 NON HANNO INCROCIATO allora per la vendita con il DRIBBLING e il DOPPIO PASSO ALLA RONALDO ho risolto con 3<39
            # il CUSCINO DELL' ANGELO CUSTODE e di SANT' ANTONIO mi proteggono ! (vendita con medie lunghe)
            
            
            # ATTENZIONE sposto di 4 posti in avanti le 5 condizioni eccezionali. - COMPARE PREGA PER ME !                  CHIEDERE AL COMPARE 4
            # adesso prende solo le ultime 5 condizioni eccezionali anche per la sessione 1
            # che si puo' aumentare la perdita tollerata poiche' lavora solo con il 10%-20% del capitale
            
                # 1 - ro cano VENDE CON UN SALVAGENTE
                elif deviation_ma39 < -0.25 and ma50_last > ma50_2_min_ago:

                    sell = "sessione 1 SELL SALVAGENTE 3-39 con ma50 < riga 1444"
                    action = "sell"

                # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!

                # 2 - ro cano VENDE DURANTE UN CROLLO IMPROVVISO !
                elif deviation < -0.62:
                    sell = "sessione 1 SELL CROLLO IMPROVVISO - riga 1451"
                    action = "sell"

                    # deviation = ma4_last / last_trade_price
                    # FORSE E' L' UNICA DEVIATION CHE MI POTRA' SALVARE DA UN CROLLO IMPROVVISO COME QUELLO DEL 3 NOVEMBRE 2021
                    # -0.90 ha fatto fare una perdita di -1.46% il 19 dic 2021

                # 3 - ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma13 >
                elif (
                    seconds_since_last_trade > max_hold_time_in_seconds
                    and ma2_last < last_trade_price
                    and deviation < -0.40
                    and ma13_last > ma13_2_min_ago
                ):

                    sell = "sessione 1 SELL DOLCE ATTESA con ma13 > and deviation < -0.40 - riga 1449"
                    action = "sell"

                    # il fattore tempo - la dolce attesa - solo con trend ribassista
                    # deviation = ma2_last / last_trade_price
                    # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)

                # 4 - ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma13 <
                elif (
                    seconds_since_last_trade > max_hold_time_in_seconds
                    and ma13_last < ma13_2_min_ago
                    and deviation < -0.35
                    and ma2_last < last_trade_price
                ):

                    sell = "sessione 1 SELL DOLCE ATTESA con ma13 < and deviation < -0.35 - riga 1464"
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

                    sell = "sessione 1 SELL TEMPO e se ma8 < ma50 and deviation_sell < -0.49 - riga 1478"
                    action = "sell"
                    # ma13 troppo lenta !
                    # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)

            ########################################################################################################################### SESSIONE 2
            # ALLA SESSIONE 2 MANCA UN ACQUISTO DURANTE IL CROLLO SE PER ES SESSIONE 1 HA GIA' VENDUTO MA IL TITOLO RESTA IN IPERVENDUTO
            elif self.session == 2:

                ############################################################################################################# sessione 2 ( 0-3 min )
                if seconds_since_last_trade > 0 and seconds_since_last_trade <= 180:

                    # con ma50 >

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell < -0.23
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 2 SELL (0-3 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.23 - riga 1515"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.25
                        and deviation_sell < 0.60
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 2 SELL (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.25 - 0.60 - riga 1525"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.61
                        and deviation_sell < 0.79
                    ):
                        sell = "sessione 2 SELL (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.61 - 0.79 - riga 1534"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 0.80
                        and deviation_sell < 1.20
                    ):

                        sell = "sessione 2 SELL (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell 0.80 - 1.20 - riga 1544"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 1.21
                    ):

                        sell = "sessione 2 SELL (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell > 1.21 (che sarebbe come IL DRIBBLING ALLA RONALDO !)- riga 1553"
                        action = "sell"

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                    ):
                        sell = "sessione 2 SELL (0-3 min) con ma50 < and incrocio 3-28- riga 1563"
                        action = "sell"
                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                      
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                    ):
                        sell = "sessione 2 SELL (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 - riga 1572"
                        action = "sell"

                    # ---------------------------------------------------------------------------------------------------------------------- crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell < -0.50
                    ):
                        sell = "sessione 2 SELL CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - riga 1582"
                        action = "sell"
                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                    ):
                        sell = "sessione 2 SELL CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 1591"
                        action = "sell"

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                        and deviation_sell > 0.60
                    ):

                        sell = "sessione 2 SELL CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - riga 1600"
                        action = "sell"

                ################################################################################################################################ SESSIONE 2 ( 3-5 min )

                # VENDITA - da 3 a 5 minuti = da 180 a 300 secondi

                elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 300:

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell < -0.25
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 2 SELL (3-5 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.25 - riga 1615"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma9_last
                        and deviation_sell > 0.25
                        and deviation_sell < 0.90
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 2 SELL (3-5 min) con ma50 > and 3<9 (no incrocio 3-9) and deviation_sell 0.25 - 0.90 - DRIBBLING ALLA RONALDO - riga 1625"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                    ):
                        sell = "sessione 2 SELL (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 1634"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                    ):
                        sell = "sessione 2 SELL (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - riga 1642"
                        action = "sell"

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        # deviation_sell_ma78 = ma3_last / ma78_last
                    ):
                        sell = "sessione 2 SELL (3-5 min) con ma50 < and incrocio 3-28 - riga 1653"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                    ):
                        sell = "sessione 2 SELL (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.23 - riga 1663"
                        action = "sell"

                    # ---------------------------------------------------------------------------------------------------------------------- guadagno con crollo
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                    ):
                        sell = "sessione 2 SELL GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 1660"
                        action = "sell"

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                    ):
                        sell = "sessione 2 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 1668"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE

                ################################################################################################################################### SESSIONE 2  ( 5-12 min )

                # VENDITA - da 5 a 12 minuti = da 300 a 720 secondi

                elif seconds_since_last_trade > 300 and seconds_since_last_trade <= 720:

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.41
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 2 SELL (5-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - riga 1685"
                        action = "sell"

                    # guardare la stella (guardare da una stella!)
                    # QUESTO E' IL RISCHIO PIU' GRANDE CHE PRENDO ! ( ma con ma50 > ma50 2 min ago DOPO 5 min (+2))

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.25
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 2 SELL (5-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - riga 1697"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma9_last
                        and deviation_sell > 0.25
                        and deviation_sell < 0.90
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 2 SELL (5-12 min) con ma50 >  3<9 and deviation_sell 0.25 - 0.90 - DRIBBLING ALLA RONALDO - riga 1707"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 2 SELL (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 1717"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                    ):
                        sell = "sessione 2 SELL (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - riga 1725"
                        action = "sell"

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.31
                    ):
                        sell = "sessione 2 SELL 12 (5-12 min) con ma50 < and incrocio 3-28 and deviation_sell < -0.31 - riga 1735"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.36
                    ):
                        sell = "sessione 2 SELL 12 (5-12 min) con ma50 < and incrocio 3-100 (cuscino di sant' antonio) - riga 1745"
                        action = "sell"

                    # ------------------------------------------------------------------------------- guadagno con crollo
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                    ):
                        sell = "sessione 2 SELL guadagno con crollo (5-12 min) con ma50 < and incrocio 3-23 - riga 1754"
                        action = "sell"

                    # ------------------------------------------------------------------------------------------------------------ PARACADUTE crollo
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                    ):
                        sell = "sessione 2 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 1763"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE

                ############################################################################################################################ SESSIONE 2 ( 12-21 min )

                # VENDITA - da 12 a 21 minuti = da 720 a 1260 secondi

                elif (
                    seconds_since_last_trade > 720 and seconds_since_last_trade <= 1260
                ):

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma72_prev and ma3_last < ma72_last)
                        and deviation_sell < -0.65
                        # and deviation_ma39 < -0.29 vendeva troppo presto
                        # ATTENZIONE "and (ma3_prev > ma39_prev and ma3_last < ma39_last)" con ma39 NON HA INCROCIATO
                        # and deviation_sell < -0.30
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 2 SELL (12-21 min) con ma50 > and incrocio 3-72 and deviation sell -0.65 e vaffanculo ! - riga 1785"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma100_prev and ma3_last < ma100_last)
                        and deviation_sell < -0.36
                        # viva sant' antonio !
                    ):
                        sell = "sessione 2 SELL (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.36 - riga 1794"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma15_last
                        and deviation_sell > 0.25
                        and deviation_sell < 0.90
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 2 SELL (12-21 min) con ma50 > and 3<15 and deviation_sell 0.25-0.90 - DOPPIO PASSO ALLA RONALDO fino a +0.50 - riga 1804"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 2 SELL (12-21 min) con ma50 > and incrocio 3-15 and deviation_sell 0.91 - 1.20 - riga 1814"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 1.21
                    ):
                        sell = "sessione 2 SELL (12-21 min) con ma50 > and incrocio 3-13 and deviation_sell > 1.21 - riga 1822"
                        action = "sell"

                    ##########################################################################################
                    # NON TOCCARE ! CUSCINO DI SANT' ANTONIO !
                    # L' INCROCIO 5-100 MI SALVA ! MA, attenzione, 5<100 VENDE DURANTE IL RIBASSO !
                    ########################################################################################### con trend discendente

                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.15
                        # and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        # and deviation_sell < -0.25
                    ):
                        sell = "sessione 2 SELL (12-21 min) con ma50 < and deviation_ma39 < -0.15 - riga 1836"
                        action = "sell"

                        # ATTENZIONE QUESTA aveva FATTO -0.61% !
                        # QUINDI ho abbassato da 0.17 a 0.16 a 0.15
                        # HO NOTATO CHE ANCHE INCROCIO 5-100 SAREBBE ARRIVATO TARDI
                        # ALLORA METTO incrocio 3-78 e deviation <0.10

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.45
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50< !
                    ):
                        sell = "sessione 2 SELL (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - riga 1850"
                        action = "sell"

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        # viva sant' antonio !
                        # incrocio 5-100 no 5<100 altrimenti vende durante il crollo !
                    ):
                        sell = "sessione 2 SELL (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - riga 1860"
                        action = "sell"

                    # --------------------------------------------------------------------------------- PARACADUTE crollo
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                    ):
                        sell = "sessione 2 PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 1869"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE

                    # ----------------------------------------------------------------------------- guadagno con crollo
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.23
                    ):
                        sell = "sessione 2 SELL eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3 - 18 and deviation_sell > 0.23 - riga 1880"
                        action = "sell"

                ################################################################################################################################## SESSIONE 2 ( 21-60 min )

                # VENDITA - da 21 a 60 minuti = da 1261 a 3600 secondi

                elif (
                    seconds_since_last_trade > 1261 and seconds_since_last_trade <= 3600
                ):

                    if (
                        ma50_last > ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                        and deviation_ma39 < -0.18
                        or (deviation_sell < -0.17 and ma3_last < ma50_last)
                        # and deviation_ma39 < -0.16 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        # and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        # and deviation_sell < -0.26
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 2 SELL (21-60 min) con ma50 > and deviation_ma39 < -0.18 or (deviation_sell < -0.17 and ma3_last < ma50_last) - riga 1901"
                        action = "sell"

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.26
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 2 SELL (21-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.26 - riga 1910"
                        action = "sell"

                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma15_last
                        and deviation_sell > 0.30
                        and deviation_sell < 0.90
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 2 SELL (21-60 min) con ma50 > and 3<15 (no incrocio 3-13) and deviation_sell 0.30 - 0.90 ELASTICO ALLA RONALDO - riga 1920"
                        action = "sell"

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "sessione 2 SELL (21-60 min) con ma50 > and incrocio 3-16 and deviation_sell 0.91 - 1.20 - riga 1930"
                        action = "sell"
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 1.21
                        and deviation_sell < 2.70
                    ):
                        sell = "sessione 2 SELL (21-60 min) con ma50 > and incrocio 3-15 and deviation_sell 1.21 - 2.70 - riga 1938"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                    ):
                        sell = "sessione 2 SELL (21-60 min) con ma50 > and incrocio 3-11 and deviation_sell > 2.71 - riga 1938"
                        action = "sell"

                    ##################################################################### con trend discendente
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.24
                        or deviation_sell < -0.24
                        # NELLA SESSIONE 2 TI PUOI RILASSARE UN POCHINO !
                        # and deviation_ma39 < -0.15 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        # and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    ):
                        sell = "sessione 2 SELL (21-60 min) con ma50 < and deviation_ma39 < -0.24 or deviation_sell < -0.24 - riga 1950"
                        action = "sell"

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.37
                    ):
                        sell = "sessione 2 SELL (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - riga 1958"
                        action = "sell"

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        # viva sant' antonio !
                        # NON INCROCERANNO MAI DURANTE IL CROLLO !
                        # non toccare ! INCROCIO 3-100 CUSCINO DI SANT' ANTONIO !
                    ):
                        sell = "sessione 2 SELL (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - riga 1969"
                        action = "sell"

                    # -------------------------------------------------------------------------------------- guadagno durante il crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.23
                    ):
                        sell = "sessione 2 SELL eventuale guadagno durante il crollo (21-60 min) con ma50 < incrocio 3 - 18 and deviation_sell > 0.23 - riga 1979"
                        action = "sell"

                ############################################################################################################################## SESSIONE 2 ( da 60 a 90 min )

                # VENDITA - da 60 a 90 min - da 3600 a 5400 secondi in poi
                elif (
                    seconds_since_last_trade > 3600 and seconds_since_last_trade <= 5400
                ):

                    if (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        or (deviation_sell < -0.18 and ma3_last < ma50_last)
                    ):
                        sell = "sessione 2 SELL da 60 a 90 min con ma50 > and deviation_ma39 <-0.18 or (deviation_sell < -0.18 and ma3_last < ma50_last)  - riga 1994"
                        action = "sell"
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # cuscino dell' angelo custode

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.35
                        and deviation_sell < 0.80
                    ):
                        sell = "sessione 2 SELL >60 min con ma50> and incrocio 3-13 and deviation_sell 0.35-0.80 RABONA ALLA RONALDO (ma15 invece di ma13)-riga 2005"
                        action = "sell"

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.81
                        and deviation_sell < 1.49
                    ):

                        sell = "sessione 2 SELL da 60 a 90 min con ma50 > and incrocio 3-15 and deviation_sell 0.81 - 1.49 - riga 2015"
                        action = "sell"

                        # ma ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 1.50
                        and deviation_sell < 2.70
                    ):

                        sell = "sessione 2 SELL da 60 a 90 min con ma50 > incrocio 3-13 and deviation_sell 1.50 - 2.70 - riga 2050"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                    ):

                        sell = "sessione 2 SELL da 60 a 90 min con ma50 > incrocio 3-11 and deviation_sell > 2.71 - riga 2060"
                        action = "sell"

                    ######################################################################################## con trend discendente
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        # and ma3_last < ma33_last
                        # and deviation_sell < 0.10
                    ):
                        sell = "sessione 2 SELL da 60 a 90 min con ma50 < con deviation_ma39 <-0.18 and deviation_sell < 0.10 (no ma3<ma33) (NO INCROCIO!) - riga 2036"
                        action = "sell"
                    # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                    # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                    # cuscino dell' angelo custode

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < 0.10
                    ):
                        sell = "sessione 2 SELL da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < 0.10 - riga 2047"
                        action = "sell"

                ################################################################################################################################# SESSIONE 2 ( > 90 min )

                # VENDITA - da 90 minuti in poi = da 5400 secondi in poi

                elif seconds_since_last_trade > 5400:

                    if (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        or (deviation_sell < 0.10 and ma3_last < ma50_last)
                        # and ma3_last < ma39_last
                        # and deviation_ma39 < -0.18
                        # and deviation_sell < 0.10
                    ):
                        sell = "sessione 2 SELL dopo 90 min con ma50 > and deviation_ma39 <-0.18 (no ma3<ma39) or (deviation_sell < 0.10 and ma3_last < ma50_last) - riga 2064"
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
                        sell = "sessione 2 SELL >90 min con ma50 > con 3-15 and deviation_sell 0.35 - 0.69 RABONA ALLA RONALDO (fatto con ma15 invece che con ma13) - riga 2077"
                        action = "sell"

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.70
                        and deviation_sell < 1.49
                    ):

                        sell = "sessione 2 SELL dopo 90 min con ma50 > incrocio 3-15 and deviation_sell 0.70 - 1.49 - riga 2087"
                        action = "sell"

                        # ma 3-48 mi evita la ricompra e la rivendita con perdita !
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 1.50
                        and deviation_sell < 2.70
                    ):

                        sell = "sessione 2 SELL dopo 90 min con ma50 > incrocio 3-13 and deviation_sell 1.50 - 2.70 - riga 2134"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                    ):

                        sell = "sessione 2 SELL dopo 90 min con ma50 > incrocio 3-11 (!) and deviation_sell > 2.71 - riga 2144"
                        action = "sell"

                    ######################################################################################## con trend discendente

                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        # and ma3_last < ma33_last
                        # and deviation_ma39 < -0.18
                        # and deviation_sell < 0.10
                    ):
                        sell = "sessione 2 SELL dopo 90 min con ma50 < con deviation_ma39 <-0.18 or (deviation_sell < 0.10 and ma3_last < ma39_last) - riga 2111"
                        action = "sell"
                    # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                    # dopo 90 min se il prezzo non ha forza puoi anche prendere qualcosa (solo > 90 min
                    # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                    # ATTENZIONE non c'e' l' incrocio 3-33 ( PERCHE' NON HANNO INCROCIATO !) ma 3 < 33 !
                    # cuscino dell' angelo custode
                    #####################################################################################################################

            ################################################################################################ sessione 2  (vendita con questi 5 altri modi)
            ################################################################################################
            ################################################################################################
            # MA ATTENZIONE al conflitto durante il crollo - SELL SOVRAPPOSTO AL BUY

            # NO 3<78 !
            # NO deviation 78 !
            # QUALCHE VOLTA ma3-ma39 NON HANNO INCROCIATO allora per la vendita con il DRIBBLING e il DOPPIO PASSO ALLA RONALDO ho risolto con 3<39
            # il CUSCINO DELL' ANGELO CUSTODE e di SANT' ANTONIO mi proteggono ! (vendita con medie lunghe)

            # 1 - ro cano VENDE CON UN SALVAGENTE
            if deviation_ma39 < -0.25 and ma50_last > ma50_2_min_ago:

                sell = "sessione 2 SELL SALVAGENTE 3-39 con ma50 < riga 2133"
                action = "sell"

                # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!

            # 2 - ro cano VENDE DURANTE UN CROLLO IMPROVVISO !
            elif deviation < -0.62:
                sell = "sessione 2 SELL CROLLO IMPROVVISO - riga 2140"
                action = "sell"

                # deviation = ma4_last / last_trade_price
                # FORSE E' L' UNICA DEVIATION CHE MI POTRA' SALVARE DA UN CROLLO IMPROVVISO COME QUELLO DEL 3 NOVEMBRE 2021
                # -0.90 ha fatto fare una perdita di -1.46% il 19 dic 2021

            # 3 - ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma13 >
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and ma2_last < last_trade_price
                and deviation < -0.40
                and ma13_last > ma13_2_min_ago
            ):

                sell = "sessione 2 SELL DOLCE ATTESA con ma13 > and deviation < -0.40 - riga 2155"
                action = "sell"

                # il fattore tempo - la dolce attesa - solo con trend ribassista
                # deviation = ma2_last / last_trade_price
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)

            # 4 - ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma13 <
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and ma13_last < ma13_2_min_ago
                and deviation < -0.35
                and ma2_last < last_trade_price
            ):

                sell = "sessione 2 SELL DOLCE ATTESA con ma13 < and deviation < -0.35 - riga 2170"
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

                sell = "sessione 2 SELL TEMPO e se ma8 < ma50 and deviation_sell < -0.49 - riga 2184"
                action = "sell"
                # ma13 troppo lenta !
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)

            ##################################################################################################################################
            ###################################################################################################
            ###################################################################################################
            ################################################################################################### SESSIONE 3-4-x

            elif self.session > 2:

                ################################################################################################### sessione 3-4-x ( 0-3 min ) ok
                if seconds_since_last_trade > 0 and seconds_since_last_trade <= 180:

                    # con ma50 >

                    if (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma18_last
                        and deviation_sell < -0.33
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "session 3-4-x SELL (0-3 min) con ma50 > and 3<18 and deviation_sell < -0.33 - riga 2207"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.25
                        and deviation_sell < 0.60
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "session 3-4-x SELL (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.25 - 0.60 - riga 2217"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.61
                        and deviation_sell < 0.79
                    ):
                        sell = "session 3-4-x SELL (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.61 - 0.79 - riga 2226"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 0.80
                        and deviation_sell < 1.20
                    ):

                        sell = "session 3-4-x SELL (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell 0.80 - 1.20 - riga 2236"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 1.21
                    ):

                        sell = "session 3-4-x SELL (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell > 1.21 (che sarebbe come IL DRIBBLING ALLA RONALDO !)- riga 2245"
                        action = "sell"

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                    ):
                        sell = "session 3-4-x SELL (0-3 min) con ma50 < and incrocio 3-28- riga 2255"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                    ):
                        sell = "SELL (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 - riga 2265"
                        action = "sell"

                    # ---------------------------------------------------------------------------------------------------------------------- crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell < -0.50
                    ):
                        sell = "session 3-4-x SELL CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - riga 2275"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                    ):
                        sell = "session 3-4-x SELL CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 2285"
                        action = "sell"

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                        and deviation_sell > 0.60
                    ):

                        sell = "session 3-4-x SELL CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - riga 2294"
                        action = "sell"

                ############################################################################################################## sessione 3-4-x ( 3-5 min  cambiata con 3-7 min )

                # VENDITA - da 3 a 7 minuti = da 180 a 420 secondi

                elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 420:

                    if (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.33
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "session 3-4-x SELL (3-5 min) con ma50 > and 3<16 and deviation_sell < -0.33 - riga 2309"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma9_last
                        and deviation_sell > 0.25
                        and deviation_sell < 0.90
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "session 3-4-x SELL (3-5 min) con ma50 > and 3<9 (no incrocio 3-9) and deviation_sell 0.25 - 0.90 - DRIBBLING ALLA RONALDO - riga 2319"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                    ):
                        sell = "session 3-4-x SELL (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 2328"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                    ):
                        sell = "session 3-4-x SELL (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - riga 2336"
                        action = "sell"

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        # deviation_sell_ma78 = ma3_last / ma78_last
                    ):
                        sell = "session 3-4-x SELL (3-5 min) con ma50 < and incrocio 3-28 - riga 2347"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                    ):
                        sell = "session 3-4-x SELL (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.23 - riga 2357"
                        action = "sell"

                    # ---------------------------------------------------------------------------------------------------------------------- guadagno con crollo
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                    ):
                        sell = "session 3-4-x SELL GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 2366"
                        action = "sell"

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                    ):
                        sell = "session 3-4-x PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 2374"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE

                ####################################################################################################### sessione 3-4-x  (5-12 min) ( cambiata con 7-12 min ! )

                # VENDITA - da 7 a 12 minuti = da 4200 a 720 secondi

                elif seconds_since_last_trade > 420 and seconds_since_last_trade <= 720:

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.41
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "session 3-4-x SELL (5-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - riga 2391"
                        action = "sell"

                    # guardare la stella (guardare da una stella!)
                    # QUESTO E' IL RISCHIO PIU' GRANDE CHE PRENDO ! ( ma con ma50 > ma50 2 min ago DOPO 5 min (+2))
                    # e qua mi ha fottuto con la vendita -1.46 al min 6 del 19 dic 2021 - cambiato crollo improvviso ! e cambiato condizioni e anche fascia da 5-12

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.25
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "session 3-4-x SELL (5-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - riga 2404"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma9_last
                        and deviation_sell > 0.27
                        and deviation_sell < 0.90
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "SELL (5-12 min) con ma50 >  3<9 and deviation_sell 0.27 - 0.90 - DRIBBLING ALLA RONALDO - riga 2414"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "session 3-4-x SELL (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 2424"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                    ):
                        sell = "session 3-4-x SELL (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - riga 2432"
                        action = "sell"

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                    ):
                        sell = "session 3-4-x SELL 12 (5-12 min) con ma50 < and incrocio 3-28 - riga 2442"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.36
                    ):
                        sell = "session 3-4-x SELL 12 (5-12 min) con ma50 < and incrocio 3-100 (cuscino di sant' antonio) - riga 2452"
                        action = "sell"

                    # ------------------------------------------------------------------------------- guadagno con crollo
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                    ):
                        sell = "session 3-4-x SELL guadagno con crollo (5-12 min) con ma50 < and incrocio 3-23 - riga 2461"
                        action = "sell"

                    # ------------------------------------------------------------------------------------------------------------ PARACADUTE crollo
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                    ):
                        sell = "session 3-4-x PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 2470"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE

                ######################################################################################################################### sessione 3-4-x ( 12-21 min )

                # VENDITA - da 12 a 21 minuti = da 720 a 1260 secondi

                elif (
                    seconds_since_last_trade > 720 and seconds_since_last_trade <= 1260
                ):

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma72_prev and ma3_last < ma72_last)
                        and deviation_sell < -0.65
                        # and deviation_ma39 < -0.29 vendeva troppo presto
                        # ATTENZIONE "and (ma3_prev > ma39_prev and ma3_last < ma39_last)" con ma39 NON HA INCROCIATO
                        # and deviation_sell < -0.30
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "session 3-4-x SELL (12-21 min) con ma50 > and incrocio 3-72 and deviation sell -0.65 e vaffanculo ! - riga 2492"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma100_prev and ma3_last < ma100_last)
                        and deviation_sell < -0.36
                        # viva sant' antonio !
                    ):
                        sell = "session 3-4-x SELL (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.36 - riga 2501"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma13_last
                        and deviation_sell > 0.25
                        and deviation_sell < 0.90
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "session 3-4-x SELL (12-21 min) con ma50 > and 3-13 (NO INCROCIO 3-13) and deviation_sell 0.25-0.90 - DOPPIO PASSO ALLA RONALDO - riga 2511"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "session 3-4-x SELL (12-21 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 2521"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell > 1.21
                    ):
                        sell = "session 3-4-x SELL (12-21 min) con ma50 > and incrocio 3-39 and deviation_sell > 1.21 - riga 2529"
                        action = "sell"

                    ##########################################################################################
                    # NON TOCCARE ! CUSCINO DI SANT' ANTONIO !
                    # L' INCROCIO 5-100 MI SALVA ! MA 5<100 VENDE DURANTE IL RIBASSO !
                    ##################################################################### con trend discendente

                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.15
                        # and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        # and deviation_sell < -0.25
                    ):
                        sell = "session 3-4-x SELL (12-21 min) con ma50 < and deviation_ma39 < -0.15 - riga 2543"
                        action = "sell"

                        # ATTENZIONE QUESTA aveva FATTO -0.61% !
                        # QUINDI ho abbassato da 0.17 a 0.16 a 0.15
                        # HO NOTATO CHE ANCHE INCROCIO 5-100 SAREBBE ARRIVATO TARDI
                        # ALLORA METTO incrocio 3-78 e deviation <0.10

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.45
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50< !
                    ):
                        sell = "session 3-4-x SELL (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - riga 2557"
                        action = "sell"

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        # viva sant' antonio !
                        # incrocio 5-100 no 5<100 altrimenti vende durante il crollo !
                    ):
                        sell = "session 3-4-x SELL (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - riga 2567"
                        action = "sell"

                    # --------------------------------------------------------------------------------- PARACADUTE crollo
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                    ):
                        sell = "session 3-4-x PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 2576"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE

                    # ----------------------------------------------------------------------------- guadagno con crollo
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.23
                    ):
                        sell = "session 3-4-x SELL eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3 - 18 and deviation_sell > 0.23 - riga 2587"
                        action = "sell"

                ############################################################################################################################# sessione 3-4-x ( 21-60 min )

                # VENDITA - da 21 a 60 minuti = da 1261 a 3600 secondi

                elif (
                    seconds_since_last_trade > 1261 and seconds_since_last_trade <= 3600
                ):

                    if (
                        ma50_last > ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                        and deviation_ma25 < -0.19
                        or (deviation_sell < -0.23 and ma3_last < ma50_last)
                        # and deviation_ma39 < -0.16 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        # and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        # and deviation_sell < -0.26
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "session 3-4-x SELL (21-60 min) con ma50 > and deviation_ma25 < -0.19 or (deviation_sell < -0.23 and ma3_last < ma50_last) - riga 2608"
                        action = "sell"

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.26
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "session 3-4-x SELL (21-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.26 - riga 2617"
                        action = "sell"

                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma15_last
                        and deviation_sell > 0.30
                        and deviation_sell < 0.90
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "session 3-4-x SELL (21-60 min) con ma50 > and 3<15 (no incrocio 3-15) and deviation_sell 0.30 - 0.90 ELASTICO ALLA RONALDO - riga 2627"
                        action = "sell"

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "session 3-4-x SELL (21-60 min) con ma50 > and incrocio 3-39 and deviation_sell 0.91 - 1.20 - riga 2637"
                        action = "sell"
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 1.21
                        and deviation_sell < 2.70
                    ):
                        sell = "session 3-4-x SELL (21-60 min) con ma50 > and incrocio 3-33 and deviation_sell 1.21 -2.70 - riga 2645"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                    ):
                        sell = "session 3-4-x SELL (21-60 min) con ma50 > and incrocio 3-11 and deviation_sell > 2.71 - riga 2703"
                        action = "sell"
                    
                    
                    
                    
                    ##################################################################### con trend discendente
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.22
                        or deviation_sell < -0.22
                        # and deviation_ma39 < -0.15 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        # nella sessione 3-4-x ti puoi rilassare una ndecchia.
                        # and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                    ):
                        sell = "session 3-4-x SELL (21-60 min) con ma50 < and deviation_ma39 < -0.22 or deviation_sell < 0.22 - riga 2657"
                        action = "sell"

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.37
                    ):
                        sell = "session 3-4-x SELL (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - riga 2665"
                        action = "sell"

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        # viva sant' antonio !
                        # NON INCROCERANNO MAI DURANTE IL CROLLO !
                        # non toccare ! INCROCIO 3-100 CUSCINO DI SANT' ANTONIO !
                    ):
                        sell = "session 3-4-x SELL (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - riga 2676"
                        action = "sell"

                    # -------------------------------------------------------------------------------------- guadagno durante il crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.23
                    ):
                        sell = "session 3-4-x SELL eventuale guadagno durante il crollo (21-60 min) con ma50 < incrocio 3 - 18 and deviation_sell > 0.23 - riga 2686"
                        action = "sell"

                ########################################################################################################################## sessione 3-4-x ( da 60 a 90 min )

                # VENDITA - da 60 a 90 min - da 3600 a 5400 secondi in poi
                elif (
                    seconds_since_last_trade > 3600 and seconds_since_last_trade <= 5400
                ):

                    if (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma25 < -0.19
                        or (deviation_sell < -0.19 and ma3_last < ma50_last)
                    ):
                        sell = "session 3-4-x SELL da 60 a 90 min con ma50 > and deviation_ma25 < -0.19 or (deviation_sell < -0.19 and ma3_last < ma50_last) - riga 2701"
                        action = "sell"
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # cuscino dell' angelo custode

                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma15_last
                        and deviation_sell > 0.35
                        and deviation_sell < 0.80
                    ):
                        sell = "session 3-4-x SELL dopo 60 min con ma50> and incrocio 3<15 and deviation_sell 0.35-0.80 RABONA ALLA RONALDO ( ma15 invece di ma13) - riga 2712"
                        action = "sell"

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.81
                        and deviation_sell < 1.49
                    ):

                        sell = "session 3-4-x SELL da 60 a 90 min con ma50 > and incrocio 3-33 and deviation_sell 0.81 - 1.49 - riga 2722"
                        action = "sell"

                        # ma ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 1.50
                        and deviation_sell < 2.70
                    ):

                        sell = "session 3-4-x SELL da 60 a 90 min con ma50 > incrocio 3-33 and deviation_sell 1.50 - 2.70 - riga 2797"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                    ):

                        sell = "session 3-4-x SELL da 60 a 90 min con ma50 > incrocio 3-11 and deviation_sell > 2.71 - riga 2733"
                        action = "sell"

                    ######################################################################################## con trend discendente
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        # and ma3_last < ma33_last
                        # and deviation_sell < 0.10
                    ):
                        sell = "session 3-4-x SELL da 60 a 90 min con ma50 < con deviation_ma39 <-0.18 and deviation_sell < 0.10 (no ma3<ma33) (NO INCROCIO!) - riga 2743"
                        action = "sell"
                    # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                    # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                    # cuscino dell' angelo custode

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < 0.10
                    ):
                        sell = "session 3-4-x SELL da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < 0.10 - riga 2754"
                        action = "sell"

                ##################################################################################################################### sessione 3-4-x ( > 90 min )

                # VENDITA - da 90 minuti in poi = da 5400 secondi in poi

                elif seconds_since_last_trade > 5400:

                    if (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma25 < -0.18
                        or (deviation_sell < 0.10 and ma3_last < ma50_last)
                        # and ma3_last < ma39_last
                        # and deviation_ma39 < -0.18
                        # and deviation_sell < 0.10
                    ):
                        sell = "session 3-4-x SELL dopo 90 min con ma50> and deviation_ma25 <-0.18 (no ma3<ma39) or (deviation_sell < 0.10 and ma3_last < ma50_last)- riga 2771"
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
                        sell = "session 3-4-x SELL >90 min con ma50 > con 3<15 and deviation_sell 0.35 - 0.69 RABONA ALLA RONALDO (ma15 invece di ma13 !) - riga 2784"
                        action = "sell"

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.70
                        and deviation_sell < 1.49
                    ):

                        sell = "session 3-4-x SELL dopo 90 min con ma50 > incrocio 3-33 (!) and deviation_sell 0.70 - 1.49 - riga 2794"
                        action = "sell"

                        # ma 3-48 mi evita la ricompra e la rivendita con perdita !
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 1.50
                        and deviation_sell < 2.70
                    ):

                        sell = "session 3-4-x SELL dopo 90 min con ma50 > incrocio 3-33 (!) and deviation_sell 1.50 - 2.70 - riga 2805"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                    ):

                        sell = "session 3-4-x SELL dopo 90 min con ma50 > incrocio 3-11 (!) and deviation_sell > 2.71 - riga 2892"
                        action = "sell"

                    ######################################################################################## con trend discendente

                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        # and ma3_last < ma33_last
                        # and deviation_ma39 < -0.18
                        # and deviation_sell < 0.10
                    ):
                        sell = "session 3-4-x SELL dopo 90 min con ma50 < con deviation_ma39 <-0.18 or (deviation_sell < 0.10 and ma3_last < ma39_last) - riga 2818"
                        action = "sell"
                    # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                    # dopo 90 min se il prezzo non ha forza puoi anche prendere qualcosa (solo > 90 min
                    # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                    # ATTENZIONE non c'e' l' incrocio 3-33 ( PERCHE' NON HANNO INCROCIATO !) ma 3 < 33 !
                    # cuscino dell' angelo custode
                #####################################################################################################################

            ################################################################################################ sessione 3-4-x (vendita con questi 5 altri modi)
            ################################################################################################
            ################################################################################################
            # MA ATTENZIONE al conflitto durante il crollo - SELL SOVRAPPOSTO AL BUY

            # NO 3<78 !
            # NO deviation 78 !
            # QUALCHE VOLTA ma3-ma39 NON HANNO INCROCIATO allora per la vendita con il DRIBBLING e il DOPPIO PASSO ALLA RONALDO ho risolto con 3<39
            # il CUSCINO DELL' ANGELO CUSTODE e di SANT' ANTONIO mi proteggono ! (vendita con medie lunghe)

            # 1 - ro cano VENDE CON UN SALVAGENTE
            if deviation_ma39 < -0.24 and ma50_last > ma50_2_min_ago:

                sell = "session 3-4-x SELL SALVAGENTE 3-39 con ma50 < riga 2840"
                action = "sell"

                # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!

            # 2 - ro cano VENDE DURANTE UN CROLLO IMPROVVISO !
            elif deviation < -0.62:
                sell = "session 3-4-x SELL CROLLO IMPROVVISO - riga 2847"
                action = "sell"

                # deviation = ma4_last / last_trade_price

                # FORSE E' L' UNICA DEVIATION CHE MI POTRA' SALVARE DA UN CROLLO IMPROVVISO COME QUELLO DEL 3 NOVEMBRE 2021

            # 3 - ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma13 >
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and ma2_last < last_trade_price
                and deviation < -0.42
                and ma13_last > ma13_2_min_ago
            ):

                sell = "session 3-4-x SELL DOLCE ATTESA con ma13 > and deviation < -0.40 - riga 2862"
                action = "sell"

                # il fattore tempo - la dolce attesa - solo con trend ribassista
                # deviation = ma2_last / last_trade_price
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                # max_hold_time_in_seconds = 300 = 5 min (con 6 min perdita di 0.90 %)
                
            # 4 - ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma25 <
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and ma13_last < ma13_2_min_ago
                and deviation < -0.36
                and ma2_last < last_trade_price
            ):

                sell = "session 3-4-x SELL DOLCE ATTESA con ma13 < and deviation < -0.36 - riga 2877"
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

                sell = "session 3-4-x SELL TEMPO e se ma8 < ma50 and deviation_sell < -0.49 - riga 2891"
                action = "sell"
                # ma13 troppo lenta !
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)

        self.algo_helper.info("action {}".format(action))
        self.algo_helper.info("percentage {}".format(percentage))

        if action == "sell":
            self.algo_helper.info("action sell {}".format(sell))
            self.session += 1

        elif action == "buy":
            self.algo_helper.info("action buy {}".format(buy))

        return action, percentage

        ############### FINE ALGORITH ###################
