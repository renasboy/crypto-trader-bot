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
        ma20_last, ma20_prev = self.algo_helper.ma_last_prev(20)
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
        ma200_last, ma200_prev = self.algo_helper.ma_last_prev(200)
        ma300_last, ma300_prev = self.algo_helper.ma_last_prev(300)
        
        
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
        ma78_40_min_ago = self.algo_helper.ma_minutes_ago(78, 40)
        ma100_60_min_ago = self.algo_helper.ma_minutes_ago(100, 60)
        ma200_20_min_ago = self.algo_helper.ma_minutes_ago(200, 20)
        ma200_60_min_ago = self.algo_helper.ma_minutes_ago(200, 60)
        ma200_120_min_ago = self.algo_helper.ma_minutes_ago(200, 120)
        ma300_120_min_ago = self.algo_helper.ma_minutes_ago(300, 120)
        
        
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
        max_hold_time_in_seconds = 360
        #  6 minuti * 60 = 360
        
        
        
        #########################################################################################################################################################
        #########################################################################################################################################################

        ##                                           T U T T E    L E   D E V I A T I O N  !

        ##############################################################################################################
        ##############################################################################################################
        ##############################################################################################################
        
        # formula DEVIATION_1_gabbia
        deviation_1_gabbia = (ma8_last / ma50_last - 1) * 100 if ma50_last else 0
        self.algo_helper.info("deviation_1_gabbia: {}".format(deviation_1_gabbia))

        ##################################################################################################################

        # formula deviation
        deviation = (ma4_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.info("deviation: {}".format(deviation))
        
        #################################################################################################################
        #################################################################################################################
        
      

        # ESPERIMENTO !
        
        # formula DEVIATION_CORREZIONE
        
        deviation_correzione = (ma3_last / ma25_last - 1) * 100 if ma25_last else 0
        self.algo_helper.info("deviation_correzione: {}".format(deviation_correzione))
        
        # per adesso solo su RCCR !
        
        
        
        
        
        ############# deviation per comprare con un RIALZO IMPROVVISO
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
       
        #################################################################################################################
        ################################################################################################################## deviation per comprare
        
        # formula DEVIATION_ASSURDA (se ma200>ma200 20 min ago compra con incrocio prezzo-ma200 e vende con incrocio ma2-ma5 e deviation > +0.20 % - ASSURDO !
        
        deviation_assurda = (price / ma200_last - 1) * 100 if ma200_last else 0
        self.algo_helper.info("deviation_assurda: {}".format(deviation_assurda))
        
        
        # formula DEVIATION_ma20_sopra_ma100
        
        deviation_ma20_sopra_ma100 = (ma20_last / ma100_last - 1) * 100 if ma100_last else 0
        self.algo_helper.info("deviation_ma20_sopra_ma100: {}".format(deviation_ma20_sopra_ma100))    
        
        
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
            
        
        # formula deviation_buy_ma5_sopra_ma20 
        
        deviation_buy_ma5_sopra_ma20 = (ma5_last / ma20_last - 1) * 100 if ma20_last else 0
        self.algo_helper.info("deviation_buy_ma5_sopra_ma20: {}".format(deviation_buy_ma5_sopra_ma20))
        

        ########################################################################################################################## deviation per vendere

        # formula DEVIATION_sell
        
        deviation_sell = (ma4_last / last_trade_price - 1) * 100 if last_trade_price else 0
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

        # if deviation_1_gabbia > -0.29 or deviation_buy_crollo_1 < -1.50:
        # if deviation_1_gabbia > -0.29 or deviation_buy_crollo_1 < -1.50 or (-1.50 < deviation_buy_crollo_1 < -0.60):    
        # compare non mi abbandonare !
        
        # QUESTE 3 HANNO DATO ERRORE !
        # if deviation_1_gabbia > -0.29 
        # or deviation_buy_crollo_1 < -1.50 
        # or (-1.50 < deviation_buy_crollo_1 < -0.60):
        
        
        # esperimento ! con aggiunta di deviation correzione e nuova apertura gabbia
        
        if deviation_1_gabbia > -0.29 or deviation_buy_crollo_1 < -1.50 or deviation_buy_crollo_1 > -1.50 and deviation_buy_crollo_1 < -0.60 or deviation_buy_crollo_1 > -0.59 and deviation_buy_crollo_1 < -0.33:
            
       
        # if deviation_1_gabbia > -0.29  
        # or deviation_buy_crollo_1 < -1.50:
        # or deviation_buy_crollo_1 > -1.50 and deviation_buy_crollo_1 < -0.60:    
        
        # vediamo se funziona cosi' o se mi da errore
        
        
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
            #######################################################################################################
           
            # in futuro
            # MACD sempre con aggiunta di ma 13-25 (come studio) (III° cane)
            # TOGLIERE TUTTI GLI INCROCI AL BUY ! se 13 > 100 NON INCROCERA' MAI ! INCROCIO 13-100 DIVENTA 13>100 !
            
            ######################################################################################################## COMPRA sessione 1
            
            # BUY 1 con "percentage" 20
            
            if self.session == 1:
                

                # ------------------------------------------------------------ BUY 1 DURANTE IL RIALZO con INCROCIO CLASSICO 69-100

                if (
                    ma69_last > ma100_last
                    
                    and ma13_last > ma78_last
                    and deviation_bellissima > 0.17
                    
                    
                    and ma5_last > ma5_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                    and ma6_last > ma100_last
                    and ma6_last > ma39_last
                    and ma6_last > ma13_last
                    and ma2_last > ma2_2_min_ago
                ):
                
                    buy = "BUY 1 con 69 > 100 and deviation_bellissima > 0.163 riga 405"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_bellissima = ma6_last / ma30_last
                    # and deviation_ma13_sopra_ma25 > 0.07 TOLTA PROVVISORIAMENTE vedi BUY ore 10:47 del 23 nov 2021 (E' ARRIVATA MOLTO TARDI)
                    

                ####################################################################  BUY 1 con incrocio 13-69 and ma72_last >= ma72_2_min_ago  "MI PIACE!"

                elif (
                    ma13_last > ma69_last
                    
                    
                    and ma72_last >= ma72_2_min_ago
                    and deviation_bellissima > 0.17
                    and price > price_2_min_ago
                    
                    and ma3_last > ma3_3_min_ago
                    and ma4_last > ma4_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                    and deviation_ma13_sopra_ma25 > 0.07
                    and ma2_last > ma2_2_min_ago
               
                ):
                    buy = "BUY 1 con 13>69 e ma72> 2 min ago (!) riga 428"
                    action = "buy"
                    percentage = 20
                
                
                # --------------------------------------------------------------    BUY 1 DURANTE IL RIALZO con 13-50 + deviation
                
                elif (
                    deviation_buy1 > 0.25
                    
                    
                    and ma13_last > ma50_last
                    and ma78_last > ma78_2_min_ago
                    and deviation_bellissima > 0.17
                    and price > price_2_min_ago
                    
                    and ma4_last > ma4_2_min_ago
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 con 13>50 and DEVIATION BUY 1 ALTA e ma78> - riga 445"
                    action = "buy"
                    percentage = 20

                    # deviation_buy1 = ma13_last/ma39_last
                
                
                ########################################################################################################### compra durante un rialzo improvviso ! 
                ########################################################################################################### con ma30 che ha 40 min di andamento laterale
                ########################################################################################################### PER ADESSO SOLO SUL BUY 1
                
                # --------------------------------------------------------------    BUY 1 con 200 >
                
                elif (    
                    ma20_last > ma200_last
                    or ma200_last > ma200_20_min_ago
                ):    
                    
                    buy = "BUY 1 con 200 > - riga 481"
                    action = "buy"
                    percentage = 10
                    
                    
             
                # -------------------------------------------------------------- BUY 1 RIALZO IMPROVVISO con 200 >
                
                elif (    
                    ma20_last > ma200_last
                    and deviation_rialzo_improvviso_1 > 1.20
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
                
                ):

                    buy = "BUY 1 RIALZO IMPROVVISO con 200 > - riga 481"
                    action = "buy"
                    percentage = 10
                    
                    # deviation_buy1 = ma13_last/ma39_last
                    # deviation_range_x va da 0 a -20 min
                    # teoricamente potresti usare solo la deviation_range !
                    # con deviation_rialzo_improvviso_5 > 0.20 non parte il BUY se trend leggermente ribassista
                    
                    
                
                
          
                # -------------------------------------------------------------- BUY 1 con ma200 <
            
                elif (       
                    ma200_last < ma200_20_min_ago
                    and ma20_last > ma200_last
                ):    
        
                    buy = "BUY 1 con ma200 < - riga 514"
                    action = "buy"
                    percentage = 10
                    
                    
                    
                    
                # --------------------------------------------------------------  BUY 1 RIALZO IMPROVVISO con ma200 <
                
                elif (     
                    ma200_last < ma200_20_min_ago
                    
                    and deviation_rialzo_improvviso_1 > 1.30
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

                    buy = "BUY 1 RIALZO IMPROVVISO con ma200 < (1.30 per evitare falsi acquisti) - riga 514"
                    action = "buy"
                    percentage = 10
                    
                    # deviation_buy1 = ma13_last/ma39_last
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                ############################################################################################ compra durante CORREZIONE - FIAT
                ############################################################################################ compra durante RIBASSO - AUDI
                ############################################################################################ compra durante CROLLO - FERRARI
                
                
                ########################################################################################################### A
                
                elif (
                    ma78_last < ma78_2_min_ago
                    
                    and ma39_last > ma78_last
                    and deviation_buy1 > 0.14
                    and deviation_bellissima > 0.18
                    and price > price_2_min_ago
                    
                    and ma4_last > ma4_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                    and ma2_last > ma2_2_min_ago
                ):

                    buy = "BUY 1 con ma78< and 39>78 and DEVIATION BUY 1 BASSA riga 539"
                    action = "buy"
                    percentage = 10
                    
                    # deviation_buy1 = ma13_last/ma39_last
                
                ############################################################################################################ B
                
                elif (
                    ma78_last < ma78_2_min_ago
                    
                    and ma39_last > ma78_last
                    and deviation_bellissima > 0.18
                    and price > price_2_min_ago
                    
                    and ma4_last > ma4_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                    and deviation_ma13_sopra_ma25 > 0.05
                    and ma2_last > ma2_2_min_ago
                ):

                    buy = "BUY 1 se ma78< con incrocio 39>78 - riga 559"
                    action = "buy"
                    percentage = 10
                    
                    # deviation_buy1 = ma13_last/ma39_last
                    # and deviation_ma13_sopra_ma25 > 0.05 FONDAMENTALE
                
                
                ##############################################################################################################################
                # IMPORTANTISSIMO ! SOLO PER IL BUY 1 - PER COMPRARE DURANTE IL CROLLO - compa prega per me - ( cruise - david gilmour )
                ##############################################################################################################################

                # entriamo nell' area dell' ipervenduto, compa !
                # QUI LASCIO GLI INCROCI !

                # BUY  PRIMO MODO DURANTE IL CROLLO

                elif (
                    
                    deviation_buy_crollo_1 < -2.30
                    and ma3_last > ma7_last
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 DURANTE IL CROLLO FERRARI - modo 1 riga 582"
                    action = "buy"
                    percentage = 20
                    # deviation_buy_crollo_1 = ma8_last / ma78_last

                # BUY SECONDO MODO - DURANTE IL CROLLO - questa condizione e' entrata in azione ! ( e mi e' sembrata ben fatta !)

                elif (
                    
                    deviation_buy_crollo_1 < -1.70
                    and deviation_buy_crollo_2 > 0.11
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 DURANTE IL CROLLO FERRARI - modo 2 riga 595"
                    action = "buy"
                    percentage = 20
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_buy_crollo_2 = ma3_last / ma13_last
                
                
                # BUY DURANTE UN RIBASSO CHE NON E' UN CROLLO ! (compare stammi vicino!)   
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.60
                    and deviation_buy_crollo_1 > -1.50
                    and deviation_bellissima > 0.02
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 DURANTE UN RIBASSO AUDI CHE NON E' UN CROLLO ! con deviation_bellissima > 0.02 - riga 611"
                    action = "buy"
                    percentage = 20
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    
                    
                # BUY 1 ECCEZIONALE - se ma200 sale da 20 min compra con ma30

                elif (    
                    ma200_last > ma200_20_min_ago
                    
                    and deviation_ma4_sopra_ma30 > 0.11
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 ECCEZIONALE se ma200 sale da 20 min compra con deviation 4-30 - riga 624"
                    action = "buy"
                    percentage = 20
                    
            
                ######################################################################## correzione - CONDIZIONE FIAT 3-20
              
                # BUY 1 con ma200 > DURANTE UNA piccola CORREZIONE - condizione FIAT
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and ma200_last > ma200_120_min_ago
                    and deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    and ma3_last > ma20_last
                 
                ):

                    buy = "BUY 1A con ma200> DURANTE UNA piccola CORREZIONE - condizione FIAT 3-20 - riga 642"
                    action = "buy"
                    percentage = 10

                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    
                   
                    
                 
                # BUY con DEVIATION ASSURDA 1
                
                
                elif (    
                    ma200_last > ma200_20_min_ago
                    
                    and deviation_assurda > -0.10
                    and deviation_buy_ma3_sopra_ma13 > 0.09
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 DEVIATION ASSURDA 1 considera ma200 > - riga 662"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_assurda = price / ma200_last
                    
                
                
                
                # BUY con DEVIATION ASSURDA 2

                elif (    
                    deviation_ma20_sopra_ma100 > 0.10
                    and deviation_buy_ma3_sopra_ma13 > 0.09
                    and ma5_last > ma5_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    
                ):
                    buy = "BUY 1 DEVIATION ASSURDA 2 considera ma100 < - riga 680"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_ma20_sopra_ma100
                    
                    
                    
                    
                    
                    
                    # esperimento
                    # BUY DURANTE UNA CORREZIONE che non e' un ribasso e non e' un crollo ! (compare stammi vicino!)   
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    and deviation_correzione > 0.03
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 DURANTE UNA CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo ! con deviation_correzione > 0.03 - riga 701"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    # and deviation_correzione > 0.02 HA PRODOTTO MOLTISSIME PERDITE quindi ho modificato con 0.03
                    # compare prega per me !
                    
                    
                    
                    
                    
            #############################################################################################################      COMPRA sessione 2

            elif self.session == 2:

                if (
                    ma78_last > ma78_2_min_ago
                    and deviation_buy2 > 0.05
                    and deviation_bellissima > 0.12
                    and deviation_buy_ma3_sopra_ma13 > 0.09
                    and deviation_ma7_sopra_ma40 > 0.075
                    
                    and price > price_2_min_ago
                    and ma3_last > ma40_last
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 2 riga 729"
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
                    
                    and price > price_2_min_ago
                    and ma3_last > ma40_last
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 2 riga 749"
                    action = "buy"
                    percentage = 50
                    # deviation_buy_ma3_sopra_ma13 > x e' fondamentale !
                    # deviation_buy2 = ma8_last/ma50_last
                
                
                
                elif (
                    deviation_buy2 > 0.13
                    and deviation_buy_ma3_sopra_ma13 > 0.10
                    and deviation_bellissima > 0.14
                    and deviation_ma7_sopra_ma40 > 0.14
                    and ma4_last > ma9_last
                    
                    and ma3_last > ma40_last
                    and ma4_last > ma78_last
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 2 riga 768"
                    action = "buy"
                    percentage = 50
                    
                    # deviation_buy2 = ma8_last / ma50
                    # deviation_bellissima > 0.14 
                    
                    
                # BUY 2 ECCEZIONALE - se ma100 sale da 20 min compra con 4-30

                elif (
                    
                    ma200_last > ma200_20_min_ago
                    and deviation_ma4_sopra_ma30 > 0.13
                    and deviation_correzione > 0.11
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 2 ECCEZIONALE se ma200 sale da 20 min compra con deviation 4-30 and deviation 3-25 - riga 783"
                    action = "buy"
                    percentage = 40
                    
                    # deviation_correzione = 3/25
                    
                    
                    
                # BUY 2 DURANTE UN RIBASSO CHE NON E' UN CROLLO ! (compare stammi vicino!)
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.60
                    and deviation_buy_crollo_1 > -1.50
                    and deviation_bellissima > 0.17
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 2 DURANTE UN RIBASSO CHE NON E' UN CROLLO ! and deviation_bellissima > 0.17 -  riga 798"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    
                    
                
                
                
                # BUY 2 con ma200> e ma300> DURANTE UNA piccola CORREZIONE che NON E' un forte ribasso e NON E' un crollo !  
                
                elif (

                    ma2_last > ma2_2_min_ago
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    and ma200_last > ma300_last
                    and deviation_buy_crollo_1 < -0.33
                    and deviation_buy_crollo_1 > -0.59
                    and deviation_correzione > 0.017
                    and deviation_buy_ma5_sopra_ma20 > 0.12
                    
                ):

                    buy = "BUY 2 con ma200> e ma300> DURANTE UNA piccola CORREZIONE che non e' un forte ribasso e non e' un crollo - riga 823"
                    action = "buy"
                    percentage = 10
                    
                    
            ############################################################################################################ COMPRA sessione 3
          
            elif self.session == 3:

                if (
                    ma69_last >= ma69_2_min_ago
                    and deviation > -0.30
                    and deviation_ma4_sopra_ma30 > 0.12
                    and deviation_buy3 > 0.12
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.08
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    
                    and ma7_last > ma25_last
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 3 con ma69 > riga 843"
                    action = "buy"
                    percentage = 50

                    # deviation_buy3 = ma4_last/ma30_last

                elif (
                    deviation_buy3 > 0.02
                    and deviation > -0.30
                    
                    and ma39_last > ma72_last
                    and deviation_buy3 > 0.02
                    and delta_buy3_incrocio_ma3_ma8 > 0.06
                    and deviation_ma4_sopra_ma30 > 0.15
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                    
                    and ma7_last > ma25_last
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 3 RIVOLUZIONARIO se ma39 > ma72 - riga 862"
                    action = "buy"
                    percentage = 50
                    
                    # deviation_buy3 = ma4_last/ma30_last
                    # riga 462 potrebbe esserci un problema perche' ho tolto ma78_last >= ma78_2_min_ago. vediamo
                    
                    

                elif (
                    ma78_last < ma78_2_min_ago
                    and deviation > -0.30
                    
                    and deviation_buy3 > 0.03
                    and deviation_ma13_sopra_ma25 > 0.04
                    and delta_buy3_incrocio_ma3_ma8 > 0.07
                    and deviation_ma4_sopra_ma30 > 0.15
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                    
                    and ma7_last > ma25_last
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 3 RIVOLUZIONARIO se ma78 < - riga 884"
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
                    
                    and ma7_last > ma25_last
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 4 con ma 78 > riga 909"
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
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 4 RIVOLUZIONARIO con ma78 > - riga 925"
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
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 4 RIVOLUZIONARIO con ma78 < - riga 945"
                    action = "buy"
                    percentage = 50
                    
                    # deviation_buy3 = ma4_last/ma30_last
                    
                    
              
                    
           
            ############################################################################################################  compra sessione 5 in poi
            #  piu' alto il BUY - "effetti laterali"

            else:

                if (
                    ma69_last >= ma69_2_min_ago
                    and deviation_buy3 > 0.12
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.09
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    
                    and ma6_last > ma15_last
                    and ma7_last > ma25_last
                    and deviation_bellissima > 0.12
                    and ma2_last > ma2_2_min_ago
                    
                    # deviation_bellissima = 6/30
                    # spezzare la catena dei buy - effetti laterali.
                    # se e' arrivato il buy 5 e' molto probabile che il trend sia consolidato
                    # e, a questo punto, non importa se compra con un + 0.10 piu' in alto. NON FA UNA GRANDE DIFFERENZA !
                ):
                    buy = "BUY 5 con ma69 > and deviation_bellissima > 0.12 (PER SPEZZARE LA CATENA - effetti laterali) riga 978"
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
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 5 RIVOLUZIONARIO con ma78 > and deviation_bellissima > 0.163 (PER SPEZZARE LA CATENA -effetti laterali) - riga 995"
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
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 5 RIVOLUZIONARIO con ma78 < and deviation_bellissima > 0.163 - riga 1017"
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
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.23 - riga 1094"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.25
                        and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.25 - 0.60 - riga 1109"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.61
                        and deviation_sell < 0.79
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.61 - 0.79 - riga 1121"
                        action = "sell"

                    # attenzione : tacco di allah e dribbling alla ronaldo SOLO con ma50> (altrimenti si attivano in "sell durante il crollo" che ha le sue dinamiche.)

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 0.80
                        and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell 0.80 - 1.20 ( TACCO DI ALLAH !) - riga 1134"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell > 1.21 (DRIBBLING ALLA RONALDO !)- riga 1146"
                        action = "sell"

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 < and incrocio 3-28- riga 1157"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 - riga 1168"
                        action = "sell"

                    # ---------------------------------------------------------------------------------------------------------------------- crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - riga 1179"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 1190"
                        action = "sell"
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                        and deviation_sell > 0.60
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - riga 1201"
                        action = "sell"
                        
                        
                    
                    
                    elif (
                        deviation_sell > 0.20
                        and (ma2_prev > ma5_prev and ma2_last < ma5_last)
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 DEVIATION ASSURDA fascia 0-3 min - riga 1213"
                        action = "sell"
                        
                        
                        
                        

                ################################################################################################################################ sessione 1 ( 3-5 min )

                # VENDITA - da 3 a 5 minuti = da 180 a 300 secondi

                elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 300:

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell < -0.24
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.24 - riga 1233"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma9_last
                        and deviation_sell > 0.25
                        and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 > and 3<9 (no incrocio 3-9) and deviation_sell 0.25 - 0.90 - DRIBBLING ALLA RONALDO - riga 1246"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 1258"
                        action = "sell"
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - riga 1268"
                        action = "sell"
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 < and incrocio 3-28 - riga 1281"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        # deviation_sell_ma78 = ma3_last / ma78_last
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.23 - riga 1295"
                        action = "sell"

                    # ---------------------------------------------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 1306"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 1317"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                     
                        
                    elif (
                        deviation_sell > 0.20
                        and (ma2_prev > ma5_prev and ma2_last < ma5_last)
                         
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 DEVIATION ASSURDA fascia 3-5 min - riga 1330"
                        action = "sell"
                        
                        

                ######################################################################################################################### sessione 1 ( 5-12 min )

                # VENDITA - da 5 a 12 minuti = da 300 a 720 secondi

                elif seconds_since_last_trade > 300 and seconds_since_last_trade <= 720:

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.41
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - riga 1348"
                        action = "sell"

                    # guardare la stella (guardare da una stella!)
                    # QUESTO E' IL RISCHIO PIU' GRANDE CHE PRENDO ! ( ma con ma50 > ma50 2 min ago DOPO 5 min (+2))
                    # deviation_sell = ma3_last/last_trade_price
                    
                    

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.25
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - riga 1363"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma9_last
                        and deviation_sell > 0.25
                        and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 >  3<9 and deviation_sell 0.25 - 0.90 - DRIBBLING ALLA RONALDO - riga 1378"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 1394"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - riga 1407"
                        action = "sell"
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 < and incrocio 3-28 - riga 1419"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 < and incrocio 3-100 (cuscino di sant' antonio) - riga 1432"
                        action = "sell"
                        

                    # ------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 guadagno con crollo (5-12 min) con ma50 < and incrocio 3-23 - riga 1444"
                        action = "sell"

                    # ------------------------------------------------------------------------------------------------------------ PARACADUTE crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 1455"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        

                #######################################################################################################################  SESSIONE 1 ( 12-21 min )

                # VENDITA - da 12 a 21 minuti = da 720 a 1260 secondi

                elif (
                    seconds_since_last_trade > 720 and seconds_since_last_trade <= 1260
                ):

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma72_prev and ma3_last < ma72_last)
                        and deviation_sell < -0.65
                        and ma2_last < ma2_2_min_ago
                        
                        # and deviation_ma39 < -0.29 vendeva troppo presto
                        # ATTENZIONE "and (ma3_prev > ma39_prev and ma3_last < ma39_last)" con ma39 NON HA INCROCIATO
                        # and deviation_sell < -0.30
                        # deviation_sell = ma3_last/last_trade_price
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-72 and deviation sell -0.65 e vaffanculo ! - riga 1481"
                        action = "sell"
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma100_prev and ma3_last < ma100_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.36 - riga 1492"
                        action = "sell"
                        
                        # viva sant' antonio !
                        
                        
                    ############################################################## doppio passo se and ma100_last > ma100_60_min_ago
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma100_last > ma100_60_min_ago
                        and ma3_last < ma18_last
                        and deviation_sell > 0.25
                        and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (12-21 min) con ma50> and 100> and 3<18 and deviation_sell 0.25-0.90 - DOPPIO PASSO ALLA RONALDO - riga 1509"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    ############################################################## doppio passo se and ma100_last < ma100_60_min_ago
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and ma3_last < ma15_last
                        and deviation_sell > 0.25
                        and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (12-21 min) con ma50> and 100< and 3<13 and deviation_sell 0.25-0.90 - DOPPIO PASSO ALLA RONALDO - riga 1525"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    #################################################################
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 1540"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-39 and deviation_sell > 1.21 - riga 1552"
                        action = "sell"

                    ##########################################################################################
                    # NON TOCCARE ! CUSCINO DI SANT' ANTONIO !
                    # L' INCROCIO 5-100 MI SALVA ! MA 5<100 VENDE DURANTE IL RIBASSO !
                    ##################################################################### con trend discendente

                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.27
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 < and deviation_ma39 < -0.27 - riga 1566"
                        action = "sell"
                        
                        # and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        # and deviation_sell < -0.25
                        
                        # ATTENZIONE QUESTA aveva FATTO -0.61% !
                        # QUINDI ho abbassato da 0.17 a 0.16 a 0.15
                        # HO NOTATO CHE ANCHE INCROCIO 5-100 SAREBBE ARRIVATO TARDI
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.45
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - riga 1585"
                        action = "sell"
                        
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50< !
                   
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - riga 1597"
                        action = "sell"
                        
                        # viva sant' antonio !
                        # incrocio 5-100 no 5<100 altrimenti vende durante il crollo !

                    # --------------------------------------------------------------------------------- PARACADUTE crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 1611"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE

                    # ----------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3 - 18 and deviation_sell > 0.23 - riga 1624"
                        action = "sell"

                ##################################################################################################################### SESSIONE 1 ( 21-60 min )

                # VENDITA - da 21 a 60 minuti = da 1261 a 3600 secondi

                elif (
                    seconds_since_last_trade > 1261 and seconds_since_last_trade <= 3600
                ):
                    if (
                        ma50_last > ma50_2_min_ago
                        and ma69_last > ma69_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.65
                        or (deviation_sell < -0.23 and ma4_last < ma50_last)
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 (21-60 min) con ma50> and ma69> and 3-78 and deviation_sell<-0.65 or (deviation_sell <-0.23 and 4<50) - riga 1642"
                        action = "sell"
                        
                  
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma69_last < ma69_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.65
                        or (deviation_sell < -0.22 and ma4_last < ma50_last)
                        and ma2_last < ma2_2_min_ago
                    
                    ):
                        sell = "SELL 1 (21-60 min) con ma50> and ma69< and 3-78 and deviation_sell<-0.65 or (deviation_sell <-0.22 and 4<50) - riga 1655"
                        action = "sell"
                   
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.26
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio and deviation_sell < -0.26 - riga 1667"
                        action = "sell"
                
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma30_last
                        and deviation_sell > 0.30
                        and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-60 min) con ma50 > and 4 < 30 and deviation_sell 0.30 - 0.90 ELASTICO ALLA RONALDO - riga 1677"
                        action = "sell"
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-60 min) con ma50 > and incrocio 3-39 and deviation_sell 0.91 - 1.20 - riga 1688"
                        action = "sell"
                     
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma45_prev and ma3_last < ma45_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-60 min) con ma50 > and incrocio 3-45 and deviation_sell > 1.21 - riga 1698"
                        action = "sell"

                    ##################################################################### con trend discendente
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.26
                        or deviation_sell < -0.26
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-60 min) con ma50 < and deviation_ma39 < -0.26 or deviation_sell < -0.26 - riga 1709"
                        action = "sell"
                        
                        # and deviation_ma39 < -0.15 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        # mario, sii un po' piu' paziente.
                        # quel deviation_sell < 0.10 era troppo restrittivo anche se sono passati 29 minuti.
                        # and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                  

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.37
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - riga 1724"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - riga 1736"
                        action = "sell"
                        
                        # viva sant' antonio !
                        # NON INCROCERANNO MAI DURANTE IL CROLLO !
                        # non toccare ! INCROCIO 3-100 CUSCINO DI SANT' ANTONIO !
                        
                        

                    # -------------------------------------------------------------------------------------- guadagno durante il crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 eventuale guadagno durante il crollo (21-60 min) con ma50 < incrocio 3 - 20 and deviation_sell > 0.23 - riga 1753"
                        action = "sell"

                ###################################################################################################################  SESSIONE 1 ( da 60 a 90 min )

                # VENDITA - da 60 a 90 min - da 3600 a 5400 secondi in poi
                
                elif (
                    seconds_since_last_trade > 3600 and seconds_since_last_trade <= 5400
                ):

                    if (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        or (deviation_sell < -0.18 and ma3_last < ma50_last)
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 60 a 90 min con ma50 > and deviation_ma39 <-0.18 or (deviation_sell < -0.18 and ma3_last < ma50_last) - riga 1770"
                        action = "sell"
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # cuscino dell' angelo custode

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.35
                        and deviation_sell < 0.80
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 dopo 60 min con ma50> and incrocio 3-13 and deviation_sell 0.35-0.80 RABONA ALLA RONALDO - riga 1782"
                        action = "sell"

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell > 0.81
                        and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 da 60 a 90 min con ma50 > and incrocio 3-39 and deviation_sell 0.81 - 1.49 - riga 1793"
                        action = "sell"

                        # ma ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 1.50
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 da 60 a 90 min con ma50 > incrocio 3-33 and deviation_sell > 1.50 - riga 1806"
                        action = "sell"

                    ######################################################################################## con trend discendente
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma200_120_min_ago
                        and deviation_ma39 < -0.25
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 da 60 a 90 min con ma50 < con deviation_ma39 <-0.25 - riga 1817"
                        action = "sell"
                        
                        # and ma3_last < ma33_last
                        # and deviation_sell < 0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # cuscino dell' angelo custode
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma200_120_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.10
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < -0.10 - riga 1833"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_120_min_ago
                        and deviation_ma39 < -0.20
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 da 60 a 90 min con ma50 < con deviation_ma39 <-0.20 - riga 1817"
                        action = "sell"
                        
                        # and ma3_last < ma33_last
                        # and deviation_sell < 0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # cuscino dell' angelo custode
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_120_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < 0.01
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < 0.01 - riga 1833"
                        action = "sell"

                ###################################################################################################################SESSIONE 1 ( > 90 min )

                # VENDITA - da 90 minuti in poi = da 5400 secondi in poi

                elif seconds_since_last_trade > 5400:

                    if (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        or (deviation_sell < -0.10 and ma3_last < ma50_last)
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 dopo 90 min con ma50 > and deviation_ma39 <-0.18 or (deviation_sell < -0.10 and ma3_last < ma50_last) - riga 1849"
                        action = "sell"
                        
                        # and ma3_last < ma39_last
                        # and deviation_ma39 < -0.18
                        # and deviation_sell < 0.10

                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # dopo 90 min se il prezzo non ha forza puoi anche prendere qualcosa (solo > 90 min)
                        # cuscino dell' angelo custode
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma15_last
                        and deviation_sell > 0.35
                        and deviation_sell < 0.69
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 >90 min con ma50 > con 3-15 (NO INCROCIO) and deviation_sell 0.35 - 0.69 RABONA ALLA RONALDO - riga 1869"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma48_prev and ma3_last < ma48_last)
                        and deviation_sell > 0.70
                        and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 dopo 90 min con ma50 > incrocio 3-48 (!) and deviation_sell 0.70 - 1.49 - riga 1882"
                        action = "sell"

                        # ma 3-48 mi evita la ricompra e la rivendita con perdita !
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma48_prev and ma3_last < ma48_last)
                        and deviation_sell > 1.50
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 dopo 90 min con ma50 > incrocio 3-48 (!) and deviation_sell > 1.50 - riga 1895"
                        action = "sell"

                    ######################################################################################## con trend discendente

                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        or (deviation_sell < -0.10 and ma3_last < ma39_last)
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 dopo 90 min con ma50 < con deviation_ma39 <-0.18 or (deviation_sell < -0.10 and ma3_last < ma39_last) - riga 1907"
                        action = "sell"
                        
                        # and ma3_last < ma33_last
                        # and deviation_ma39 < -0.18
                        # and deviation_sell < 0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # dopo 90 min se il prezzo non ha forza puoi anche prendere qualcosa (solo > 90 min
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # ATTENZIONE non c'e' l' incrocio 3-33 ( PERCHE' NON HANNO INCROCIATO !) ma 3 < 33 !
                        # cuscino dell' angelo custode
                        
            #####################################################################################################################

            ################################################################################################# SESSIONE 1 ( vendita con questi 5 altri modi )
            ################################################################################################
            ################################################################################################
            
            # MA ATTENZIONE al conflitto durante il crollo - SELL SOVRAPPOSTO AL BUY

            # NO 3<78 !
            # NO deviation 78 !
            # QUALCHE VOLTA ma3-ma39 NON HANNO INCROCIATO allora per la vendita con il DRIBBLING e il DOPPIO PASSO ALLA RONALDO ho risolto con 3<39
            # il CUSCINO DELL' ANGELO CUSTODE e di SANT' ANTONIO mi proteggono ! (vendita con medie lunghe)

            # 1 - ro cano VENDE CON UN SALVAGENTE
            
            elif deviation_ma39 < -0.26 and deviation < -0.30 and ma50_last > ma50_2_min_ago:

                sell = "SELL 1 SALVAGENTE 3-39 con ma50 < riga 1936"
                action = "sell"

            # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!
            
            

            
            # 2 - ro cano VENDE DURANTE UN CROLLO IMPROVVISO !
            
            elif (            
                ma2_last < ma4_last
                and ma2_last < ma6_last
                and deviation < -0.62
                  
            ):    
                sell = "SELL 1 CROLLO IMPROVVISO - riga 2011"        
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
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL 1 DOLCE ATTESA con ma13 > and deviation < -0.40 - riga 1961"
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
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL 1 DOLCE ATTESA con ma13 < and deviation < -0.35 - riga 1980"
                action = "sell"

                # il fattore tempo - la dolce attesa - solo con trend ribassista
                # deviation = ma2_last / last_trade_price
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                

            # 5 - ro cano VENDE " DOPO x MINUTI " and...
            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and ma8_last < ma50_last
                and deviation_sell < -0.49
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL 1 TEMPO e se ma8 < ma50 and deviation_sell < -0.49 - riga 1997"
                action = "sell"
                
                # ma13 troppo lenta !
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                

            ######################################################################################################################################################
            ###########################################################################################################################
            
            ########################################################################################################################### SESSIONE 2

            elif self.session == 2:

                ############################################################################################################# sessione 2 ( 0-3 min )
                
                if seconds_since_last_trade > 0 and seconds_since_last_trade <= 180:

                    # con ma50 >

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell < -0.23
                        
                        
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.23 - riga 2024"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.25
                        and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.25 - 0.60 - riga 2038"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.61
                        and deviation_sell < 0.79
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.61 - 0.79 - riga 2052"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 0.80
                        and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell 0.80 - 1.20 - riga 2065"
                        action = "sell"

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell > 1.21 un bel dribbing - riga 2075"
                        action = "sell"

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 < and incrocio 3-28- riga 2086"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 - riga 2097"
                        action = "sell"

                    # ---------------------------------------------------------------------------------------------------------------------- crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - riga 2108"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 2120"
                        action = "sell"

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                        and deviation_sell > 0.60
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - riga 2130"
                        action = "sell"

                ############################################################################################################ SESSIONE 2 ( 3-5 min )

                # VENDITA - da 3 a 5 minuti = da 180 a 300 secondi

                elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 300:

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell < -0.24
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.24 - riga 2146"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma9_last
                        and deviation_sell > 0.25
                        and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 > and 3<9 and deviation_sell 0.25 - 0.90 - DRIBBLING ALLA RONALDO - riga 2160"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 2174"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - riga 2186"
                        action = "sell"
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 < and incrocio 3-28 - riga 2200"
                        action = "sell"
                       
                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        # deviation_sell_ma78 = ma3_last / ma78_last
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.23 - riga 2214"
                        action = "sell"

                    # ---------------------------------------------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 2225"
                        action = "sell"

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 2234"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        

                ############################################################################################################## SESSIONE 2  ( 5-12 min )

                # VENDITA - da 5 a 12 minuti = da 300 a 720 secondi

                elif seconds_since_last_trade > 300 and seconds_since_last_trade <= 720:

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.41
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - riga 2253"
                        action = "sell"

                    # guardare la stella (guardare da una stella!)
                    # QUESTO E' IL RISCHIO PIU' GRANDE CHE PRENDO ! ( ma con ma50 > ma50 2 min ago DOPO 5 min (+2))
                    # deviation_sell = ma3_last/last_trade_price
                    
                    

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.25
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - riga 2268"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma9_last
                        and deviation_sell > 0.25
                        and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 >  3<9 and deviation_sell 0.25 - 0.90 - DRIBBLING ALLA RONALDO - riga 2282"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 2296"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - riga 2309"
                        action = "sell"
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 < and incrocio 3-28 - riga 2321"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 < and incrocio 3-100 (cuscino di sant' antonio) - riga 2334"
                        action = "sell"

                    # ------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 guadagno con crollo (5-12 min) con ma50 < and incrocio 3-23 - riga 2345"
                        action = "sell"

                    # ------------------------------------------------------------------------------------------------------------ PARACADUTE crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 2356"
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
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and incrocio 3-72 and deviation sell -0.65 e vaffanculo ! - riga 2376"
                        action = "sell"
                        
                        # and deviation_ma39 < -0.29 vendeva troppo presto
                        # ATTENZIONE "and (ma3_prev > ma39_prev and ma3_last < ma39_last)" con ma39 NON HA INCROCIATO
                   
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma100_prev and ma3_last < ma100_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.36 - riga 2388"
                        action = "sell"
                        
                        # viva sant' antonio !
                        
                        
                    ############################################################## doppio passo se and ma100_last > ma100_60_min_ago
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma100_last > ma100_60_min_ago
                        and ma5_last < ma50_last
                        and deviation_sell > 0.25
                        and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and 100>  and 5<50 and deviation_sell 0.25 - 0.90 - DOPPIO PASSO ALLA RONALDO - riga 2404"
                        action = "sell"
                       
                    
                    ############################################################## doppio passo se and ma100_last < ma100_60_min_ago
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and ma3_last < ma15_last
                        and deviation_sell > 0.25
                        and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and 100< and 3<15 and deviation_sell 0.25 - 0.90 - DOPPIO PASSO ALLA RONALDO - riga 2418"
                        action = "sell"
                    
                    ##################################################################################################
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 2430"
                        action = "sell"
                  
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and incrocio 3-39 and deviation_sell > 1.21 - riga 2439"
                        action = "sell"
                   
                    ##########################################################################################
                    # NON TOCCARE ! CUSCINO DI SANT' ANTONIO !
                    # L' INCROCIO 5-100 MI SALVA ! MA, attenzione, 5<100 VENDE DURANTE IL RIBASSO !
                    
                    ########################################################################################### con trend discendente

                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.15
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 < and deviation_ma39 < -0.15 - riga 2454"
                        action = "sell"
                        
                        # and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        # and deviation_sell < -0.25

                        # ATTENZIONE QUESTA aveva FATTO -0.61% !
                        # QUINDI ho abbassato da 0.17 a 0.16 a 0.15
                        # HO NOTATO CHE ANCHE INCROCIO 5-100 SAREBBE ARRIVATO TARDI
                        # ALLORA METTO incrocio 3-78 e deviation <0.10
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.45
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - riga 2473"
                        action = "sell"
                        
                   
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - riga 2483"
                        action = "sell"
                        
                        # viva sant' antonio !
                        # incrocio 5-100 no 5<100 altrimenti vende durante il crollo !
                        

                    # --------------------------------------------------------------------------------- PARACADUTE crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 2498"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                     

                    # ----------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3 - 18 and deviation_sell > 0.23 - riga 2512"
                        action = "sell"
                        
                        

                ################################################################################################################ SESSIONE 2 ( 21-60 min )

                # VENDITA - da 21 a 60 minuti = da 1261 a 3600 secondi

                elif (
                    seconds_since_last_trade > 1261 and seconds_since_last_trade <= 3600
                ):

                    if (
                        ma50_last > ma50_2_min_ago
                        
                        and deviation_ma39 < -0.16
                        or (deviation_sell < -0.15 and ma3_last < ma50_last)
                        and ma2_last < ma2_2_min_ago
                        
                        
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and deviation_ma39 < -0.16 or (deviation_sell < -0.15 and ma3_last < ma50_last) - riga 2534"
                        action = "sell"
                        
                        # and deviation_ma39 < -0.16 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        # and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        # and deviation_sell < -0.26
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.26
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.26 - riga 2550"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma15_last
                        and deviation_sell > 0.30
                        and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and 3<15 (no incrocio 3-13) and deviation_sell 0.30 - 0.90 ELASTICO ALLA RONALDO - riga 2564"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and incrocio 3-39 and deviation_sell 0.91 - 1.20 - riga 2578"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma45_prev and ma3_last < ma45_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and incrocio 3-45 and deviation_sell > 1.21 - riga 2591"
                        action = "sell"
                        
                        

                    ##################################################################### con trend discendente
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.23
                        or deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 < and deviation_ma39 < -0.23 or deviation_sell < -0.23 - riga 2604"
                        action = "sell"
                        
                        # NELLA SESSIONE 2 TI PUOI RILASSARE UN POCHINO !
                        # and deviation_ma39 < -0.15 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        # and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.37
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - riga 2619"
                        action = "sell"
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - riga 2629"
                        action = "sell"
                        
                        # viva sant' antonio !
                        # NON INCROCERANNO MAI DURANTE IL CROLLO !
                        # non toccare ! INCROCIO 3-100 CUSCINO DI SANT' ANTONIO !
                        

                    # -------------------------------------------------------------------------------------- guadagno durante il crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 eventuale guadagno durante il crollo (21-60 min) con ma50 < incrocio 3 - 18 and deviation_sell > 0.23 - riga 2645"
                        action = "sell"
                        
                        

                ################################################################################################################# SESSIONE 2 ( da 60 a 90 min )

                # VENDITA - da 60 a 90 min - da 3600 a 5400 secondi in poi
                
                elif (
                    seconds_since_last_trade > 3600 and seconds_since_last_trade <= 5400
                ):

                    if (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        or (deviation_sell < -0.18 and ma3_last < ma50_last)
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 > and deviation_ma39 <-0.18 or (deviation_sell < -0.18 and ma3_last < ma50_last) - riga 2664"
                        action = "sell"
                        
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # cuscino dell' angelo custode
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.35
                        and deviation_sell < 0.80
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 >60 min con ma50> and incrocio 3-13 and deviation_sell 0.35-0.80 RABONA ALLA RONALDO - riga 2679"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell > 0.81
                        and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 da 60 a 90 min con ma50 > and incrocio 3-39 and deviation_sell 0.81 - 1.49 - riga 2692"
                        action = "sell"

                        # ma ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 1.50
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 da 60 a 90 min con ma50 > incrocio 3-33 and deviation_sell > 1.50 - riga 2706"
                        action = "sell"
                        
                        

                    ######################################################################################## con trend discendente
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma200_120_min_ago
                        and deviation_ma39 < -0.25
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 < con deviation_ma39 <-0.25 - riga 2718"
                        action = "sell"
                        
                        # and ma3_last < ma33_last
                        # and deviation_sell < 0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # cuscino dell' angelo custode
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma200_120_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < 0.01
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < 0.01 - riga 2735"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_120_min_ago
                        and deviation_ma39 < -0.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 < con deviation_ma39 <-0.20 - riga 2718"
                        action = "sell"
                        
                        # and ma3_last < ma33_last
                        # and deviation_sell < 0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # cuscino dell' angelo custode
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_120_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < 0.01
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < 0.01 - riga 2735"
                        action = "sell"
                        
                        

                ######################################################################################################### SESSIONE 2 ( > 90 min )

                # VENDITA - da 90 minuti in poi = da 5400 secondi in poi

                elif seconds_since_last_trade > 5400:

                    if (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        or (deviation_sell < -0.10 and ma3_last < ma50_last)
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 dopo 90 min con ma50 > and deviation_ma39 <-0.18 or (deviation_sell < -0.10 and ma3_last < ma50_last) - riga 2752"
                        action = "sell"
                        
                        # and ma3_last < ma39_last
                        # and deviation_ma39 < -0.18
                        # and deviation_sell < -0.10

                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # dopo 90 min se il prezzo non ha forza puoi anche prendere qualcosa (solo > 90 min)
                        # cuscino dell' angelo custode
                        
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma15_last
                        and deviation_sell > 0.35
                        and deviation_sell < 0.69
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 >90 min con ma50 > con 3-15 and deviation_sell 0.35 - 0.69 RABONA ALLA RONALDO (fatto con ma15 NO ma13!) - riga 2773"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma48_prev and ma3_last < ma48_last)
                        and deviation_sell > 0.70
                        and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 dopo 90 min con ma50 > incrocio 3-48 (!) and deviation_sell 0.70 - 1.49 - riga 2786"
                        action = "sell"

                        # ma 3-48 mi evita la ricompra e la rivendita con perdita !
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma48_prev and ma3_last < ma48_last)
                        and deviation_sell > 1.50
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 dopo 90 min con ma50 > incrocio 3-48 (!) and deviation_sell > 1.50 - riga 2800"
                        action = "sell"
                        
                        
                        

                    ######################################################################################## con trend discendente

                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 dopo 90 min con ma50 < con deviation_ma39 <-0.18 or (deviation_sell < 0.10 and ma3_last < ma39_last) - riga 2814"
                        action = "sell"
                        
                        # and ma3_last < ma33_last
                        # and deviation_ma39 < -0.18
                        # and deviation_sell < 0.10
                        
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
            
            if deviation_ma39 < -0.26 and deviation < -0.30 and ma50_last > ma50_2_min_ago:

                sell = "SELL 2 SALVAGENTE 3-39 con ma50 < riga 2845"
                action = "sell"

                # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!

            
            
            # 2 - ro cano VENDE DURANTE UN CROLLO IMPROVVISO !
            
            elif (            
                ma2_last < ma4_last
                and ma2_last < ma6_last
                and deviation < -0.62
                  
            ):    
                sell = "SELL 1 CROLLO IMPROVVISO - riga 2960"        
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
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL 2 DOLCE ATTESA con ma13 > and deviation < -0.40 - riga 2874"
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
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL 2 DOLCE ATTESA con ma13 < and deviation < -0.35 - riga 2893"
                action = "sell"

                # il fattore tempo - la dolce attesa - solo con trend ribassista
                # deviation = ma2_last / last_trade_price
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                
                

            # 5 - ro cano VENDE " DOPO x MINUTI " and...
            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and ma8_last < ma50_last
                and deviation_sell < -0.49
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL 2 TEMPO e se ma8 < ma50 and deviation_sell < -0.49 - riga 2911"
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
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (0-3 min) con ma50 > and 3<18 and deviation_sell < -0.33 - riga 2938"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.25
                        and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.25 - 0.60 - riga 2952"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.61
                        and deviation_sell < 0.79
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.61 - 0.79 - riga 2967"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 0.80
                        and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3-4-x (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell 0.80 - 1.20 - riga 2980"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3-4-x (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell > 1.21 (IL DRIBBLING ALLA RONALDO !)- riga 2992"
                        action = "sell"
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (0-3 min) con ma50 < and incrocio 3-28- riga 3005"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 - riga 3018"
                        action = "sell"

                    # ---------------------------------------------------------------------------------------------------------------------- crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x  CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - riga 3029"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 3042"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                        and deviation_sell > 0.60
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3-4-x CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - riga 3054"
                        action = "sell"

                #################################################################################### sessione 3-4-x ( 3-5 min  cambiata con 3-7 min )

                # VENDITA - da 3 a 7 minuti = da 180 a 420 secondi

                elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 420:

                    if (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.33
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (3-5 min) con ma50 > and 3<16 and deviation_sell < -0.33 - riga 3069"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma9_last
                        and deviation_sell > 0.25
                        and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (3-5 min) con ma50 > and 3<9 and deviation_sell 0.25 - 0.90 - DRIBBLING ALLA RONALDO - riga 3083"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 3097"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - riga 3108"
                        action = "sell"
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (3-5 min) con ma50 < and incrocio 3-28 - riga 3121"
                        action = "sell"
                        
                        # deviation_sell_ma78 = ma3_last / ma78_last
                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !

                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.23 - riga 3135"
                        action = "sell"

                    # ---------------------------------------------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 3146"
                        action = "sell"

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 3155"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE

                ####################################################################################################### sessione 3-4-x  (5-12 min) ( cambiata con 7-12 min ! )

                # VENDITA - da 7 a 12 minuti = da 4200 a 720 secondi

                elif seconds_since_last_trade > 420 and seconds_since_last_trade <= 720:

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.41
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (5-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - riga 3172"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price

                        # guardare la stella (guardare da una stella!)
                        # QUESTO E' IL RISCHIO PIU' GRANDE CHE PRENDO ! ( ma con ma50 > ma50 2 min ago DOPO 5 min (+2))
                        # e qua mi ha fottuto con la vendita -1.46 al min 6 del 19 dic 2021 - cambiato crollo improvviso !
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.25
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (5-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - riga 3189"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma9_last
                        and deviation_sell > 0.25
                        and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (5-12 min) con ma50 >  3<9 and deviation_sell 0.25 - 0.90 - DRIBBLING ALLA RONALDO - riga 3203"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 3217"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - riga 3230"
                        action = "sell"
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (5-12 min) con ma50 < and incrocio 3-28 - riga 3242"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (5-12 min) con ma50 < and incrocio 3-100 (cuscino di sant' antonio) - riga 3255"
                        action = "sell"
                        
                        

                    # ------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x guadagno con crollo (5-12 min) con ma50 < and incrocio 3-23 - riga 3268"
                        action = "sell"
                        
                        

                    # ------------------------------------------------------------------------------------------------------------ PARACADUTE crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 3281"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                        

                ############################################################################################################### sessione 3-4-x ( 12-21 min )

                # VENDITA - da 12 a 21 minuti = da 720 a 1260 secondi

                elif (
                    seconds_since_last_trade > 720 and seconds_since_last_trade <= 1260
                ):

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma72_prev and ma3_last < ma72_last)
                        and deviation_sell < -0.65
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (12-21 min) con ma50 > and incrocio 3-72 and deviation sell -0.65 e vaffanculo ! - riga 3303"
                        action = "sell"
                        
                        # and deviation_ma39 < -0.29 vendeva troppo presto
                        # ATTENZIONE "and (ma3_prev > ma39_prev and ma3_last < ma39_last)" con ma39 NON HA INCROCIATO
                        # and deviation_sell < -0.30
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma100_prev and ma3_last < ma100_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.36 - riga 3319"
                        action = "sell"
                        
                        # viva sant' antonio !
                        
                    
                    
                    
                    #################################### se ma100>ma100 60 min ago aumenta il doppio passo
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma100_last > ma100_60_min_ago
                        and ma3_last < ma18_last
                        and deviation_sell > 0.25
                        and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (12-21 min) con ma50 > and 100>60 min ago and 3-18 and deviation_sell 0.25-0.90 - DOPPIO PASSO ALLA RONALDO - riga 3337"
                        action = "sell"
                        
                 
                    #################################### se ma100 < ma100 60 min ago diminuisce il doppio passo
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and ma3_last < ma15_last
                        and deviation_sell > 0.25
                        and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (12-21 min) con ma50 > and 100<60 min ago and 3-15 and deviation_sell 0.25-0.90 - DOPPIO PASSO ALLA RONALDO - riga 3351"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                    
                    ###############################################################################################################################
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (12-21 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 3365"
                        action = "sell"
                        
                
                
                
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (12-21 min) con ma50 > and incrocio 3-39 and deviation_sell > 1.21 - riga 3378"
                        action = "sell"
                    
                    ##########################################################################################
                    # NON TOCCARE ! CUSCINO DI SANT' ANTONIO !
                    # L' INCROCIO 5-100 MI SALVA ! MA 5<100 VENDE DURANTE IL RIBASSO !
                    ##################################################################### con trend discendente

                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.15
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (12-21 min) con ma50 < and deviation_ma39 < -0.15 - riga 3391"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.45
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - riga 3401"
                        action = "sell"
                       
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50< !
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x  (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - riga 3412"
                        action = "sell"
                        
                        # viva sant' antonio !
                        # incrocio 5-100 no 5<100 altrimenti vende durante il crollo !
                        

                    # --------------------------------------------------------------------------------- PARACADUTE crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 3427"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                     
                    # ----------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3 - 18 and deviation_sell > 0.23 - riga 3441"
                        action = "sell"
                        
                        

                ############################################################################################################# sessione 3-4-x ( 21-60 min )

                # VENDITA - da 21 a 60 minuti = da 1261 a 3600 secondi

                elif (
                    seconds_since_last_trade > 1261 and seconds_since_last_trade <= 3600
                ):

                    if (
                        ma50_last > ma50_2_min_ago
                        
                        and deviation_ma25 < -0.25
                        or (deviation_sell < -0.27 and ma3_last < ma50_last)
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (21-60 min) con ma50 > and deviation_ma25 < -0.25 or (deviation_sell < -0.27 and ma3_last < ma50_last) - riga 3461"
                        action = "sell"
                        
                        # and deviation_ma39 < -0.16 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        # and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        # and deviation_sell < -0.26
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.26
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (21-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.26 - riga 3478"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma15_last
                        and deviation_sell > 0.30
                        and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (21-60 min) con ma50 > and 3<15 (no incrocio 3-15) and deviation_sell 0.30 - 0.90 ELASTICO ALLA RONALDO - riga 3493"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell > 0.91
                        and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                        
                        
                    ):
                        sell = "SELL 3-4-x (21-60 min) con ma50 > and incrocio 3-39 and deviation_sell 0.91 - 1.20 - riga 3509"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma4_prev > ma25_prev and ma4_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (21-60 min) con ma50 > and incrocio 4-25 and deviation_sell > 1.21 - riga 3522"
                        action = "sell"
                        
                        
                        

                    ##################################################################### con trend discendente
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.23
                        or deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (21-60 min) con ma50 < and deviation_ma39 < -0.23 or deviation_sell < 0.23 - riga 3536"
                        action = "sell"
                        
                        # and deviation_ma39 < -0.15 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        # nella sessione 3-4-x ti puoi rilassare una ndecchia.
                        # and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.37
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x  (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - riga 3552"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - riga 3563"
                        action = "sell"
                        
                        # viva sant' antonio !
                        # NON INCROCERANNO MAI DURANTE IL CROLLO !
                        # non toccare ! INCROCIO 3-100 CUSCINO DI SANT' ANTONIO !
                        
                        

                    # -------------------------------------------------------------------------------------- guadagno durante il crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x eventuale guadagno durante il crollo (21-60 min) con ma50 < incrocio 3 - 18 and deviation_sell > 0.23 - riga 3580"
                        action = "sell"
                        
                        

                ######################################################################################################## sessione 3-4-x ( da 60 a 90 min )

                # VENDITA - da 60 a 90 min - da 3600 a 5400 secondi in poi
                elif (
                    seconds_since_last_trade > 3600 and seconds_since_last_trade <= 5400
                ):

                    if (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma25 < -0.19
                        or (deviation_sell < -0.19 and ma3_last < ma50_last)
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x da 60 a 90 min con ma50 > and deviation_ma25 < -0.18 or (deviation_sell < -0.18 and ma3_last < ma50_last) - riga 3598"
                        action = "sell"
                        
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # cuscino dell' angelo custode
                        
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma15_last
                        and deviation_sell > 0.35
                        and deviation_sell < 0.80
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x dopo 60 min con ma50> and 3<15 and deviation_sell 0.35-0.80 RABONA ALLA RONALDO ( ma15 invece di ma13 !) - riga 3614"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.81
                        and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3-4-x da 60 a 90 min con ma50 > and incrocio 3-33 and deviation_sell 0.81 - 1.49 - riga 3627"
                        action = "sell"
                       
                        # ma ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.50
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3-4-x da 60 a 90 min con ma50 > incrocio 3-30 and deviation_sell > 1.50 - riga 3641"
                        action = "sell"
                        
                        

                    ######################################################################################## con trend discendente
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma25 < -0.18
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x  da 60 a 90 min con ma50 < con deviation_ma25 < -0.18 and deviation_sell < 0.10 - riga 3653"
                        action = "sell"
                        
                        # and ma3_last < ma33_last
                        # and deviation_sell < 0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # cuscino dell' angelo custode
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.10
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < -0.10 - riga 3670"
                        action = "sell"
                        
                    

                ##################################################################################################################### sessione 3-4-x ( > 90 min )

                # VENDITA - da 90 minuti in poi = da 5400 secondi in poi

                elif seconds_since_last_trade > 5400:

                    if (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma25 < -0.21
                        or (deviation_sell < -0.14 and ma3_last < ma50_last)
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x dopo 90 min con ma50> and deviation_ma25 <-0.21 or (deviation_sell < -0.14 and ma3_last < ma50_last)- riga 3687"
                        action = "sell"
                        
                        # and ma3_last < ma39_last
                        # and deviation_ma39 < -0.18
                        # and deviation_sell < 0.10

                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # dopo 90 min se il prezzo non ha forza puoi anche prendere qualcosa (solo > 90 min)
                        # cuscino dell' angelo custode
                        
                   
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma18_last
                        and deviation_sell > 0.35
                        and deviation_sell < 0.69
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x >90 min con ma50 > con 3<18 and deviation_sell 0.35 - 0.69 RABONA ALLA RONALDO - riga 3707"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.70
                        and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3-4-x dopo 90 min con ma50 > incrocio 3-33 (!) and deviation_sell 0.70 - 1.49 - riga 3720"
                        action = "sell"

                        # ma 3-48 mi evita la ricompra e la rivendita con perdita !
                        
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.50
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3-4-x dopo 90 min con ma50 > incrocio 3-48 (!) and deviation_sell > 1.50 - riga 3735"
                        action = "sell"
                        
                        
                        

                    ######################################################################################## con trend discendente

                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        or (deviation_sell < -0.10 and ma3_last < ma39_last)
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 3-4-x dopo 90 min con ma50 < con deviation_ma39 <-0.18 or (deviation_sell < -0.10 and ma3_last < ma39_last) - riga 3750"
                        action = "sell"
                        
                        # and ma3_last < ma33_last
                        # and deviation_ma39 < -0.18
                        # and deviation_sell < 0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # dopo 90 min se il prezzo non ha forza puoi anche prendere qualcosa (solo > 90 min
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # ATTENZIONE non c'e' l' incrocio 3-33 ( PERCHE' NON HANNO INCROCIATO !) ma 3 < 33 !
                        # cuscino dell' angelo custode
                        
                        
                

            ################################################################################################ sessione 3-4-x (vendita con questi 5 altri modi)
            ################################################################################################
            ################################################################################################
            # MA ATTENZIONE al conflitto durante il crollo - SELL SOVRAPPOSTO AL BUY

            # NO 3<78 !
            # NO deviation 78 !
            # QUALCHE VOLTA ma3-ma39 NON HANNO INCROCIATO allora per la vendita con il DRIBBLING e il DOPPIO PASSO ALLA RONALDO ho risolto con 3<39
            # il CUSCINO DELL' ANGELO CUSTODE e di SANT' ANTONIO mi proteggono ! (vendita con medie lunghe)

            # 1 - ro cano VENDE CON UN SALVAGENTE
            
            if deviation_ma39 < -0.27 and deviation < -0.30 and ma50_last > ma50_2_min_ago:

                sell = "SELL 3-4-x SALVAGENTE 3-39 con ma50 < riga 3779"
                action = "sell"

                # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!
                
                

            # 2 - ro cano VENDE DURANTE UN CROLLO IMPROVVISO !
            
            elif (            
                ma2_last < ma4_last
                and ma2_last < ma6_last
                and deviation < -0.62
                  
            ):    
                sell = "SELL 1 CROLLO IMPROVVISO - riga 2011"        
                action = "sell"
            
                # FORSE E' L' UNICA DEVIATION CHE MI POTRA' SALVARE DA UN CROLLO IMPROVVISO COME QUELLO DEL 3 NOVEMBRE 2021
                # deviation = ma4_last / last_trade_price

                
            

            # 3 - ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma25 >
            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and ma2_last < last_trade_price
                and deviation < -0.40
                and ma13_last > ma13_2_min_ago
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL 3-4-x  DOLCE ATTESA con ma13 > and deviation < -0.40 - riga 3808"
                action = "sell"

                # il fattore tempo - la dolce attesa - solo con trend ribassista
                # deviation = ma2_last / last_trade_price
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
            # 4 - ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma25 <
           
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and ma13_last < ma13_2_min_ago
                and deviation < -0.35
                and ma2_last < last_trade_price
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL 3-4-x DOLCE ATTESA con ma13 < and deviation < -0.35 - riga 3824"
                action = "sell"

                # il fattore tempo - la dolce attesa - solo con trend ribassista
                # deviation = ma2_last / last_trade_price
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                
                

            # 5 - ro cano VENDE " DOPO x MINUTI " and...
            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and ma8_last < ma50_last
                and deviation_sell < -0.49
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL 3-4-x TEMPO e se ma8 < ma50 and deviation_sell < -0.49 - riga 3842"
                action = "sell"
                # ma13 troppo lenta !
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
            
            
            ##################################################################################################
            ##################################################################################################
            ##################################################################################################
            ################################################################################################## POCHI MALEDETTI E SUBITO dedicata al compa !
            
            
            elif (
                ma3_last < ma9_last
                and ma200_last > ma200_60_min_ago
                and deviation > 0.68
                and ma2_last < ma2_2_min_ago
            ):
                sell = "SELL 3-4-x POCHI MALEDETTI E SUBITO solo quando ma200 > - riga 3860"
                action = "sell"
                
                
            elif (
                ma3_last < ma9_last 
                and ma200_last < ma200_60_min_ago
                and deviation > 0.70
                and ma2_last < ma2_2_min_ago
            ):
                sell = "SELL 3-4-x POCHI MALEDETTI E SUBITO solo quando ma200 < e con deviation > 0.70 - riga 3870"
                action = "sell"
                
                
              
                
            # dolce attesa applicata a pochi maledetti e subito
            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and deviation > 0.80
                and ma3_last < ma9_last
                and ma2_last < last_trade_price
                
            ):

                sell = "SELL 3-4-x dolce attesa applicata a pochi maledetti e subito - riga 3886"
                action = "sell"

                # il fattore tempo - la dolce attesa - solo con trend ribassista
                # deviation = ma2_last / last_trade_price
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                
                
         
                
            ##################################################################################################

                
        

        self.algo_helper.info("action {}".format(action))
        self.algo_helper.info("percentage {}".format(percentage))

        if action == "sell":
            self.algo_helper.info("action sell {}".format(sell))
            self.session += 1

        elif action == "buy":
            self.algo_helper.info("action buy {}".format(buy))

        return action, percentage

        ############### FINE ALGORITH ################### #
