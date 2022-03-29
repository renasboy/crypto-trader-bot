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
        ma20_last, ma20_prev = self.algo_helper.ma_last_prev(20)
        ma23_last, ma23_prev = self.algo_helper.ma_last_prev(23)
        ma25_last, ma25_prev = self.algo_helper.ma_last_prev(25)
        ma28_last, ma28_prev = self.algo_helper.ma_last_prev(28)
        ma30_last, ma30_prev = self.algo_helper.ma_last_prev(30)
        ma33_last, ma33_prev = self.algo_helper.ma_last_prev(33)
        ma36_last, ma36_prev = self.algo_helper.ma_last_prev(36)
        ma39_last, ma39_prev = self.algo_helper.ma_last_prev(39)
        ma40_last, ma40_prev = self.algo_helper.ma_last_prev(40)
        ma42_last, ma42_prev = self.algo_helper.ma_last_prev(42)
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
        ma10_2_min_ago = self.algo_helper.ma_minutes_ago(10, 2)
        ma13_2_min_ago = self.algo_helper.ma_minutes_ago(13, 2)
        ma13_10_min_ago = self.algo_helper.ma_minutes_ago(13, 10)
        ma20_2_min_ago = self.algo_helper.ma_minutes_ago(20, 2)
        ma25_2_min_ago = self.algo_helper.ma_minutes_ago(25, 2)
        
        ma30_10_min_ago = self.algo_helper.ma_minutes_ago(30, 10)
        ma30_20_min_ago = self.algo_helper.ma_minutes_ago(30, 20)
        ma30_30_min_ago = self.algo_helper.ma_minutes_ago(30, 30)
        ma30_40_min_ago = self.algo_helper.ma_minutes_ago(30, 40)
        
        ma33_5_min_ago = self.algo_helper.ma_minutes_ago(33, 5)
        ma36_2_min_ago = self.algo_helper.ma_minutes_ago(36, 2)
        ma39_2_min_ago = self.algo_helper.ma_minutes_ago(39, 2)
        ma39_3_min_ago = self.algo_helper.ma_minutes_ago(39, 3)
        ma50_2_min_ago = self.algo_helper.ma_minutes_ago(50, 2)
        ma69_2_min_ago = self.algo_helper.ma_minutes_ago(69, 2)
        ma69_45_min_ago = self.algo_helper.ma_minutes_ago(69, 45)
        ma72_2_min_ago = self.algo_helper.ma_minutes_ago(72, 2)
        ma78_2_min_ago = self.algo_helper.ma_minutes_ago(78, 2)
        ma78_4_min_ago = self.algo_helper.ma_minutes_ago(78, 4)
        ma78_5_min_ago = self.algo_helper.ma_minutes_ago(78, 5)
        ma78_7_min_ago = self.algo_helper.ma_minutes_ago(78, 7)
        ma78_30_min_ago = self.algo_helper.ma_minutes_ago(78, 30)
        ma100_60_min_ago = self.algo_helper.ma_minutes_ago(100, 60)
        ma200_15_min_ago = self.algo_helper.ma_minutes_ago(200, 15)
        ma200_20_min_ago = self.algo_helper.ma_minutes_ago(200, 20)
        ma200_60_min_ago = self.algo_helper.ma_minutes_ago(200, 60)
        ma200_90_min_ago = self.algo_helper.ma_minutes_ago(200, 90)
        ma200_120_min_ago = self.algo_helper.ma_minutes_ago(200, 120)
        ma200_120_min_ago = self.algo_helper.ma_minutes_ago(200, 120)
        ma300_60_min_ago = self.algo_helper.ma_minutes_ago(300, 60)
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
        
        # importante : dolce attesa

        # VENDE DOPO x SECONDI - ro cano torna a casa - (ma c'e' anche un "e se")
        
        max_hold_time_in_seconds = 255
        
        #  4 minuti * 60 = 240 + 30 secondi = 270 secondi

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
        
        
        # formula deviation trend ma200
        
        deviation_trend_ma200 = (ma200_last / ma200_120_min_ago - 1) * 100 if ma200_120_min_ago else 0
        self.algo_helper.info("deviation_trend_ma200: {}".format(deviation_trend_ma200))
        
        # deviation pochi maledetti
        
        deviation_pochi_maledetti = (ma13_last / ma13_10_min_ago - 1) * 100 if ma13_10_min_ago else 0
        self.algo_helper.info("deviation_pochi_maledetti: {}".format(deviation_pochi_maledetti))
        
      
        ######################################################################
        
        # ESPERIMENTO !
        
        # formula DEVIATION_ma5_sotto_ma200 per comprare FINO a una certa distanza da ma200
        
        deviation_ma5_sotto_ma200 = (ma5_last / ma200_last - 1) * 100 if ma200_last else 0
        self.algo_helper.info("deviation_ma5_sotto_ma200: {}".format(deviation_ma5_sotto_ma200))   
        
        
        # formula deviation_ma8_sotto_last_trade_price
        
        deviation_ma8_sotto_last_trade_price = (ma8_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.info("deviation_ma8_sotto_last_trade_price: {}".format(deviation_ma8_sotto_last_trade_price))
        
        
        # formule DEVIATION CORREZIONE
        
        deviation_correzione = (ma3_last / ma25_last - 1) * 100 if ma25_last else 0
        self.algo_helper.info("deviation_correzione: {}".format(deviation_correzione))

        
        deviation_correzione_1 = (ma5_last / ma30_last - 1) * 100 if ma30_last else 0
        self.algo_helper.info("deviation_correzione_1: {}".format(deviation_correzione_1))
        
        deviation_correzione_2 = (ma5_last / ma39_last - 1) * 100 if ma39_last else 0
        self.algo_helper.info("deviation_correzione_2: {}".format(deviation_correzione_2))
        
        
        # formula DEVIATION_ASSURDA (se ma200>ma200 20 min ago compra con incrocio ma2-ma200 e vende con incrocio ma2-ma5 e deviation > +0.20 % - ASSURDO !
        
        deviation_assurda = (ma2_last / ma200_last - 1) * 100 if ma200_last else 0
        self.algo_helper.info("deviation_assurda: {}".format(deviation_assurda))
        
        
        
        # formula DEVIATION_MA100_LATERALE evita BUY CONTINUI DEL BUY ECCEZIONALE NELLA FASE LATERALE
        
        deviation_ma100_laterale = (ma5_last / ma100_last - 1) * 100 if ma100_last else 0
        self.algo_helper.info("deviation_ma100_laterale: {}".format(deviation_ma100_laterale))
        
        
        
        # formula DEVIATION_ma8_sotto_ma100
        
        deviation_ma8_sotto_ma100 = (ma8_last / ma100_last - 1) * 100 if ma100_last else 0
        self.algo_helper.info("deviation_ma8_sotto_ma100: {}".format(deviation_ma8_sotto_ma100))
        
       
        
        # formula DEVIATION_ma13_sopra_ma25
        
        deviation_ma13_sopra_ma25 = (ma13_last / ma25_last - 1) * 100 if ma25_last else 0
        self.algo_helper.info("deviation_ma13_sopra_ma25: {}".format(deviation_ma13_sopra_ma25))    
        
        
        # formula DEVIATION_bellissima
        
        deviation_bellissima = (ma6_last / ma30_last - 1) * 100 if ma30_last else 0
        self.algo_helper.info("deviation_bellissima: {}".format(deviation_bellissima))

        
        ############# deviation per comprare con un RIALZO IMPROVVISO DOPO UN PERIODO LATERALE
        
        
        # 12 gennaio 2022 la ma2 arriva tardi ! DEVIATION RIALZO IMPROVVISO per adesso solo su RCCR
        
        # ma deve andare almeno di 0.5% sopra la ma200 ! cosi' eviti molti falsi buy
        
        # formula DEVIATION_RIALZO_IMPROVVISO_SOPRA (deve stare 0.5 sopra la ma200)
        
        deviation_rialzo_improvviso_sopra = (price / ma200_last - 1) * 100 if ma200_last else 0
        self.algo_helper.info("deviation_rialzo_improvviso_sopra: {}".format(deviation_rialzo_improvviso_sopra))
        
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
        
        
        deviation_range_x = (ma30_last / ma30_20_min_ago - 1) * 100 if ma30_20_min_ago else 0
        self.algo_helper.info("deviation_range_x: {}".format(deviation_range_x))
        
        
        
        # formula DEVIATION_RIBASSO_IMPROVVISO
        
        deviation_ribasso_improvviso = (price / ma30_last - 1) * 100 if ma30_last else 0
        self.algo_helper.info("deviation_ribasso_improvviso: {}".format(deviation_ribasso_improvviso))
        
       
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
    
        # formula DEVIATION_buy_ma3_sopra_ma20 per comprare a una certa distanza da ma20
        
        deviation_buy_ma3_sopra_ma20 = (ma3_last / ma20_last - 1) * 100 if ma20_last else 0
        self.algo_helper.info("deviation_buy_ma3_sopra_ma20: {}".format(deviation_buy_ma3_sopra_ma20))
        

        deviation_buy_ma5_sopra_ma20 = (ma5_last / ma20_last - 1) * 100 if ma20_last else 0
        self.algo_helper.info("deviation_buy_ma5_sopra_ma20: {}".format(deviation_buy_ma5_sopra_ma20))

        
        # formula DEVIATION_buy_ma2_sopra_ma13 per comprare a una certa distanza da ma13
        
        deviation_buy_ma2_sopra_ma13 = (ma2_last / ma13_last - 1) * 100 if ma13_last else 0
        self.algo_helper.info("deviation_buy_ma2_sopra_ma13: {}".format(deviation_buy_ma2_sopra_ma13))
        
        # formula DEVIATION_buy_ma3_sopra_ma13 per comprare a una certa distanza da ma13
        
        deviation_buy_ma3_sopra_ma13 = (ma3_last / ma13_last - 1) * 100 if ma13_last else 0
        self.algo_helper.info("deviation_buy_ma3_sopra_ma13: {}".format(deviation_buy_ma3_sopra_ma13))
            
      
        # formula DEVIATION_buy_ma3_sopra_ma25 per comprare a una certa distanza da ma25
        
        deviation_buy_ma3_sopra_ma25 = (ma3_last / ma25_last - 1) * 100 if ma25_last else 0
        self.algo_helper.info("deviation_buy_ma3_sopra_ma25: {}".format(deviation_buy_ma3_sopra_ma25))    
        
      
        # formula DEVIATION_ma4_sopra_ma30
        
        deviation_ma4_sopra_ma30 = (ma4_last / ma30_last - 1) * 100 if ma30_last else 0
        self.algo_helper.info("deviation_ma4_sopra_ma30: {}".format(deviation_ma4_sopra_ma30))
            
        
        
        # formula DEVIATION_ma4_sopra_ma25
        
        deviation_ma4_sopra_ma25 = (ma4_last / ma25_last - 1) * 100 if ma25_last else 0
        self.algo_helper.info("deviation_ma4_sopra_ma25: {}".format(deviation_ma4_sopra_ma25))
            
        
        
        # formula DEVIATION_ma5_sopra_ma30
        
        deviation_ma5_sopra_ma30 = (ma5_last / ma30_last - 1) * 100 if ma30_last else 0
        self.algo_helper.info("deviation_ma5_sopra_ma30: {}".format(deviation_ma5_sopra_ma30))
            
       
        # formula deviation_ma7_sopra_ma40
        
        deviation_ma7_sopra_ma40 = (ma7_last / ma40_last - 1) * 100 if ma40_last else 0
        self.algo_helper.info("deviation_ma7_sopra_ma40: {}".format(deviation_ma7_sopra_ma40))
            
        

        # formula deviation_ma3_sopra_ma7 (solo per il BUY1)
        
        deviation_ma3_sopra_ma7 = (ma3_last / ma7_last - 1) * 100 if ma7_last else 0
        self.algo_helper.info("deviation_ma3_sopra_ma7: {}".format(deviation_ma3_sopra_ma7))
            
        

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
        
        # if deviation_1_gabbia > -0.29 or deviation_buy_crollo_1 < -1.50 or deviation_buy_crollo_1 > -1.50 and deviation_buy_crollo_1 < -0.60:
        
        # ultima evoluzione APERTURA GABBIA
        
        # if deviation_1_gabbia > -0.30 or deviation_buy_crollo_1 < -1.62 or deviation_buy_crollo_1 > -1.59 and deviation_buy_crollo_1 < -0.72 or deviation_buy_crollo_1 > -0.69 and deviation_buy_crollo_1 < -0.36:
        
        if deviation_1_gabbia > -0.27 or deviation_buy_crollo_1 < -1.51 or deviation_buy_crollo_1 > -1.50 and deviation_buy_crollo_1 < -0.60 or deviation_buy_crollo_1 > -0.59 and deviation_buy_crollo_1 < -0.33:
        
        # FATTO GABBIA UGUALE A QUELLA DEL RCCR ! andava meglio !
        
        # HO INTERROTTO LA CONTINUITA' COSI' CHIUDE E PARTE LA SESSION 1
        
        # QUESTE 3 HANNO DATO ERRORE !
        # if deviation_1_gabbia > -0.29 
        # or deviation_buy_crollo_1 < -1.50 
        # or (-1.50 < deviation_buy_crollo_1 < -0.60):
        
        
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
            
            # in futuro
         
            # MACD sempre con aggiunta di ma 13-25 (come studio) (III° cane)
            # TOGLIERE TUTTI GLI INCROCI AL BUY ! se 13 > 100 NON INCROCERA' MAI ! INCROCIO 13-100 DIVENTA 13>100 !
            # analisi dei dati !
      
            ######################################################################################################## COMPRA sessione 1
            
            # BUY 1 con "percentage" 20
            
            
            if self.session == 1:
                
            
                # ------------------------------------------------------------ BUY 1 DURANTE IL RIALZO con INCROCIO CLASSICO 69-100
                
                if (    
                    ma20_last > ma200_last
                    and ma69_last > ma100_last
                    
                    and deviation_bellissima > 0.14
                    and ma6_last > ma39_last
                ):    
              
                    buy = "BUY 1 con 20>200 and 69 > 100 and deviation_bellissima > 0.14 riga 494"
                    action = "buy"
                    percentage = 20
                    
                    
                    
                # ------------------------------------------------------------ BUY 1 se ma200> and ma300> and 13>50   
                
                elif (    
                    ma20_last > ma200_last
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    and ma13_last > ma50_last
                ):  
                
                    buy = "BUY 1 con 20>200 and 69 > 100 and deviation_bellissima > 0.14 riga 509"
                    action = "buy"
                    percentage = 20
              
                # ------------------------------------------------------------ BUY 1 che considera il passare del tempo
                
                elif (     
                    ma69_last > ma69_45_min_ago
                    and deviation_bellissima > 0.14
                    and ma20_last > ma20_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma2_last > ma20_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 BUY 1 che considera il passare del tempo - riga 523"
                    action = "buy"
                    percentage = 20
                    
              
                # ------------------------------------------------------------  BUY 1 con incrocio 11-69 and ma69_last >= ma69_2_min_ago  "MI PIACE!"

                elif (
                    ma20_last > ma200_last
                    and ma11_last > ma69_last
                    and ma69_last >= ma69_2_min_ago
                    and deviation_bellissima > 0.17
                    and price > price_2_min_ago
                    
                    and ma3_last > ma3_3_min_ago
                    and ma4_last > ma4_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                    and deviation_ma13_sopra_ma25 > 0.06
                 
                ):
                    buy = "BUY 1 con ma20_last > ma200_last e con 11 > 69 e ma69> 2 min ago (!) riga 543"
                    action = "buy"
                    percentage = 20
           
                
                # BUY 1 con 11-69 SE ma200 SALE DA 2 ORE !
                    
                elif (
                    ma200_last > ma200_120_min_ago
                    and ma20_last > ma200_last
                    and ma11_last > ma69_last
                    
                    and deviation_bellissima > 0.17
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma3_3_min_ago
                    and ma4_last > ma4_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                    and deviation_ma13_sopra_ma25 > 0.07
                 
                ):
                    buy = "BUY 1 con 11-69 SE ma200 SALE DA 2 ORE ! - riga 564"
                    action = "buy"
                    percentage = 20
                    
           
                elif (
                    ma20_last > ma200_last
                    and deviation_buy1 > 0.24
                    and ma13_last > ma50_last
                    and ma78_last > ma78_2_min_ago
                    and deviation_bellissima > 0.18
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma4_last > ma4_2_min_ago
                ):
                    buy = "BUY 1 con 13>50 and DEVIATION BUY 1 ALTA e ma78> - riga 579"
                    action = "buy"
                    percentage = 20
                    
                    
                elif (
                    ma20_last > ma200_last
                    and ma78_last < ma78_2_min_ago
                    and ma39_last > ma78_last
                    and deviation_buy1 > 0.14
                    and deviation_bellissima > 0.17
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma4_last > ma4_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                ):
                    buy = "BUY 1 con ma78< and 39>78 and DEVIATION BUY 1 BASSA riga 595"
                    action = "buy"
                    percentage = 10
                    
               
                elif (
                    ma20_last > ma200_last
                    and ma78_last < ma78_2_min_ago
                    and ma39_last > ma78_last
                    and deviation_bellissima > 0.17
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma4_last > ma4_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                    and deviation_ma13_sopra_ma25 > 0.05
                ):

                    buy = "BUY 1 se ma78< - BUY 1 con incrocio 39>78 - riga 612"
                    action = "buy"
                    percentage = 10
               
        
                ####################################################################################################### compra durante un rialzo improvviso ! 
                ####################################################################################################### con ma30 che ha 40 min di andamento laterale
                ####################################################################################################### PER ADESSO SOLO SUL BUY 1
                
                elif (
                   
                    ma200_last > ma200_20_min_ago
                    
                    and deviation_rialzo_improvviso_sopra > 0.49
                    
                    and deviation_rialzo_improvviso_1 > 0.49
                    
                    and deviation_rialzo_improvviso_2 > 0.19
                    and deviation_rialzo_improvviso_3 > 0.19
                  
                    and deviation_range_1 < 0.20
                    and deviation_range_1 > -0.20
                    and deviation_range_2 < 0.20
                    and deviation_range_2 > -0.20
                    
                    and deviation_range_x < 0.20
                    and deviation_range_x > -0.20
                   
                ):

                    buy = "BUY 1 RIALZO IMPROVVISO con ma200 > - riga 647"
                    action = "buy"
                    percentage = 10
                 
                    # deviation_rialzo_improvviso_sopra = price / ma200_last
                    # deviation_rialzo_improvviso_1 = price / ma30_last
                    # deviation_rialzo_improvviso_2 = price / ma30_10_min_ago
                    # deviation_rialzo_improvviso_3 = price / ma30_20_min_ago
                    # deviation_range_1 = ma30_last / ma30_10_min_ago
                    # deviation_range_2 = ma30_10_min_ago / ma30_20_min_ago
                    # deviation_range_x = ma30_last / ma30_20_min_ago
                    
                    
           
                # BUY 1 variazione 1 RIALZO con 20-69
                
                elif (
                    
                    ma200_last > ma200_20_min_ago
                    and (ma20_prev < ma69_prev and ma20_last > ma69_last)
                   
                    and deviation_rialzo_improvviso_1 > 0.25
                    and deviation_range_1 > 0.20
                    
                    and ma2_last > ma2_2_min_ago
                ):

                    buy = "BUY 1 variazione 1 RIALZO con 20-69 - riga 674"
                    action = "buy"
                    percentage = 10
                 
                    # deviation_rialzo_improvviso_1 = price / ma30_last
                    # deviation_range_1 = ma30_last / ma30_10_min_ago
                    
                
                
                # BUY 1 variazione 2 RIALZO con 20-100
                
                elif (
                  
                    ma200_last > ma200_20_min_ago
                    and (ma20_prev < ma100_prev and ma20_last > ma100_last)
                   
                    and deviation_rialzo_improvviso_1 > 0.25
                    and deviation_range_1 > 0.20
                    
                    and ma2_last > ma2_2_min_ago
                ):

                    buy = "BUY 1 variazione 2 RIALZO con 20-100 - riga 704"
                    action = "buy"
                    percentage = 10
                    
                    # deviation_rialzo_improvviso_1 = price / ma30_last
                    # deviation_range_1 = ma30_last / ma30_10_min_ago
                    
                    
                    
                # BUY 1 variazione 3 RIALZO con 20-200
                
                elif (
                  
                    ma200_last > ma200_20_min_ago
                    and (ma20_prev < ma200_prev and ma20_last > ma200_last)
                    and deviation_rialzo_improvviso_1 > 0.25
                    and deviation_range_1 > 0.20
                    and ma2_last > ma2_2_min_ago
                
                ):

                    buy = "BUY 1 variazione 3 RIALZO con 20-200 - riga 725"
                    action = "buy"
                    percentage = 10
                    
                    # deviation_rialzo_improvviso_1 = price / ma30_last
                    # deviation_range_1 = ma30_last / ma30_10_min_ago
                
                
             
                # rialzo improvviso trend ribassista
                
                elif (    
                   
                    ma200_last < ma200_20_min_ago
                    
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
             
                    and deviation_range_x < 0.20
                    and deviation_range_x > -0.20
                 
                ):

                    buy = "BUY 1 RIALZO IMPROVVISO con 78 < (1.20 ! per evitare falsi acquisti) - riga 751"
                    action = "buy"
                    percentage = 10
                    
                    # deviation_rialzo_improvviso_sopra = price / ma200_last
                    # deviation_rialzo_improvviso_1 = price / ma30_last
                    # deviation_rialzo_improvviso_2 = price / ma30_10_min_ago
                    # deviation_rialzo_improvviso_3 = price / ma30_20_min_ago
                    # deviation_rialzo_improvviso_4 = price / ma30_30_min_ago
                    # deviation_range_1 = ma30_last / ma30_10_min_ago
                    # deviation_range_2 = ma30_10_min_ago / ma30_20_min_ago
                    # deviation_range_3 = ma30_20_min_ago / ma30_30_min_ago
                    # deviation_range_x = ma30_last / ma30_20_min_ago
          
                ########################################################################################################################### ATTENZIONE !
                
                # piccola CORREZIONE FIAT
                # grande CORREZIONE AUDI
                # RIBASSO MASERATI
                # CROLLO FERRARI
                
                ########################################################################################################################### ATTENZIONE !
                
                
                
                # BUY 1 con ma200> DURANTE UNA piccola CORREZIONE FIAT che NON E' un forte ribasso e NON E' un crollo ! (compare stammi vicino!)
               
                elif (
                    ma2_last > ma2_2_min_ago
                    and ma200_last > ma200_120_min_ago
                    and deviation_buy_crollo_1 < -0.33
                    and deviation_buy_crollo_1 > -0.59
                    and deviation_correzione > 0.017
                    and deviation_buy_ma5_sopra_ma20 > 0.12
                ):    
                    
                    buy = "BUY 1A con ma200> DURANTE UNA piccola CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo - riga 793"
                    action = "buy"
                    percentage = 10
                    
                
                # BUY 1 con ma300 > DURANTE UNA piccola CORREZIONE FIAT che NON E' un forte ribasso e NON E' un crollo ! (compare stammi vicino!)
              
                elif (

                    ma2_last > ma2_2_min_ago
                    and ma300_last > ma300_120_min_ago
                    and deviation_buy_crollo_1 < -0.33
                    and deviation_buy_crollo_1 > -0.59
                    and deviation_correzione > 0.012
                    and ma5_last > ma72_last
                ):

                    buy = "BUY 1 con ma300 > DURANTE UNA piccola CORREZIONE FIAT che NON E' un forte ribasso e NON E' un crollo ! - riga 810"
                    action = "buy"
                    percentage = 10

                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    # ma5 non deve allontanarsi troppo dalla ma200 !
                    # compare prega per me !
                    # and ma3_last > ma69_last SOLTANTO con ma300> va bene anche senza ma sembra che STATISTICAMENTE produce una alta % di piccole perdite
                    
                
                
                
                # BUY 1 DURANTE UNA piccola CORREZIONE FIAT che NON E' un forte ribasso e NON E' un crollo !
             
                elif (
                    ma2_last > ma2_2_min_ago
                    and ma5_last > ma39_last
                    and deviation_ma8_sotto_ma100 < -0.50
                    and deviation_buy_crollo_1 > -0.59
                ): 
            
                    buy = "BUY 1 DURANTE UNA piccola CORREZIONE FIAT che NON E' un forte ribasso e NON E' un crollo ! - riga 832"
                    action = "buy"
                    percentage = 10
                    

               
                # BUY 1 con ma200< e ma300< DURANTE UNA piccola CORREZIONE FIAT che NON E' un forte ribasso e NON E' un crollo !
                
                elif (

                    ma2_last > ma2_2_min_ago
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    and ma11_last > ma69_last
                    
                    and deviation_buy_crollo_1 < -0.33
                    and deviation_buy_crollo_1 > -0.59
                    
                ):

                    buy = "BUY 1 con ma200< e ma300< piccola CORREZIONE FIAT che NON E'una grande correzione e NON E' un grande ribasso e NON E' un crollo -r 852"
                    action = "buy"
                    percentage = 10

                    # compare prega per me !
                    # se ma200< e ma300< si torna alle origini ! 11-69 ! (con ma2 > ma2 2 min ago)
         
              
                
                # BUY 1 durante UNA grande CORREZIONE AUDI che NON E' una piccola CORREZIONE BICICLETTA che NON E' un grande ribasso e NON E' un crollo !)
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and (ma20_prev < ma200_prev and ma20_last > ma200_last)
                    and deviation_correzione_1 > 0.03
                    
                    and deviation_buy_crollo_1 < -0.60
                    and deviation_buy_crollo_1 > -0.90
                  
                ):
                    buy = "BUY 1 durante UNA grande CORREZIONE AUDI che NON E' un grande ribasso e NON E' un crollo ! + deviation_correzione> 0.02 - riga 872"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma5_last / ma30_last
                    
              
              
                # BUY 1 con deviation trend ma200 DURANTE UNA grande CORREZIONE AUDI che NON E' una piccola correzione e NON E' un grande ribasso e NON E' un crollo !)
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_trend_ma200 > -0.30
                    and deviation_correzione_1 > 0.03
                    
                    and deviation_buy_crollo_1 < -0.60
                    and deviation_buy_crollo_1 > -0.90
                  
                ):
                    buy = "BUY 1 con deviation trend ma200 DURANTE UNA grande CORREZIONE AUDI che NON E' un grande ribasso e NON E' un crollo ! - riga 892"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma5_last / ma30_last
                    
                    # compare prega per me !
               
               
                # copia della riga 530 del RCCR CHE FUNZIONA BENISSIMO ma solo un po' piu' prudente ! - BUY DURANTE UN grande ribasso MASERATI CHE NON E' UN CROLLO !
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -0.60
                    and deviation_buy_crollo_1 > -1.50
                    and deviation_bellissima > 0.02
                    and deviation_correzione_1 > 0.03
                    and ma13_last > ma50_last
                ):
                    buy = "copia della riga 530 del RCCR ma piu' prudente ! - BUY DURANTE UN GRANDE RIBASSO MASERATI CHE NON E' UN CROLLO ! - riga 911"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                
                
                
                # QUA DEVI VEDERE vanno in sovrapposizione - vedi prima come vanno poi correggi
                
                # BUY 1 durante un GRANDE RIBASSO MASERATI CHE NON E' UN CROLLO ! (compare stammi vicino!) HA FUNZIONATO ! viva ro combaro meo !
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -0.91
                    and deviation_buy_crollo_1 > -1.50
                    and ma3_last > ma30_last
                ):
                    buy = "BUY 1 durante un GRANDE RIBASSO MASERATI CHE NON E' UN CROLLO ! and deviation_bellissima > 0.012- riga 929"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    
                
                ##############################################################################################################################
                # IMPORTANTISSIMO ! - PER COMPRARE DURANTE IL CROLLO - FERRARI - compa prega per me - ( cruise - david gilmour )
                ##############################################################################################################################

                # entriamo nell' area dell' ipervenduto, compa !
                # QUI LASCIO GLI INCROCI !
                
                # BUY 1 DURANTE IL CROLLO FERRARI - modo 1
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -2.30
                    and ma3_last > ma7_last
                ):
                    buy = "BUY 1 DURANTE IL CROLLO FERRARI - modo 1 riga 950"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    
               
                
                
                # BUY 1 DURANTE IL CROLLO FERRARI - modo 2 questa condizione e' entrata in azione ! ( e mi e' sembrata ben fatta !)

                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -1.61
                    and deviation_buy_crollo_2 > 0.11
                ):
                    buy = "BUY 1 DURANTE IL CROLLO FERRARI - modo 2 riga 966"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_buy_crollo_2 = ma3_last / ma13_last
                    
            
                ##################################################################################################### CONDIZIONI ESPERIMENTALI !
                #####################################################################################################
                
                # BUY 1 ECCEZIONALE - se ma200 sale da 15 min e ma69> COMPRA con 4-25 e un po' piu' su della ma100

                elif (
                    ma200_last > ma200_15_min_ago
                    and ma69_last > ma69_2_min_ago
                    and deviation_ma100_laterale > 0.50
                    
                    and deviation_ma4_sopra_ma25 > 0.10
                    
                    and (ma4_prev < ma25_prev and ma4_last > ma25_last)
                    and ma2_last > ma2_2_min_ago
                    and (ma3_prev < ma8_prev and ma3_last > ma8_last)
                    and ma36_last > ma36_2_min_ago
                  
                ):
                    buy = "BUY 1 ECCEZIONALE - se ma200 sale da 15 min e 69> COMPRA con deviation 4-25 e un po' piu' su della ma100 ! - riga 991"
                    action = "buy"
                    percentage = 20
                    
                    # deviation 4-25 forse, in futuro, da aumentare un pochino.
                    
                    
                # BUY 1 DOCCIA 
                
                elif (    

                    ma200_last > ma200_120_min_ago
                    and ma20_last > ma200_last
                    and ma20_last > ma69_last
                    and ma2_last > ma2_2_min_ago
                    and (ma3_prev < ma8_prev and ma3_last > ma8_last)
                    and ma3_last > ma69_last
                    and (ma4_prev < ma25_prev and ma4_last > ma25_last)
                    and deviation_buy_ma3_sopra_ma25 > 0.05
                  
                ):

                    buy = "BUY 1 DOCCIA se ma200 > da 120 min ! COMPRA riga 1013"
                    action = "buy"
                    percentage = 20   
                    
                
                # condizione RCCR - BUY 1 DURANTE UNA CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo !
                # ATTENZIONE ! QUESTA E' UNA CONDIZIONE CHE ANDAVA BENE IN RCCR e non prendeva proprio in maddog !
                # questa condizione considera anche le ipotesi in cui ma100< ma200< ma300<  - da aggiungere in un secondo momento
                # e non e' ancora una situazione cosi' drammatica - distanza di ma8 da last trade
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    and ma8_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                    
                    # and ma100_last > ma100_120_min_ago
                    # and ma200_last > ma200_120_min_ago
                    # and ma300_last > ma300_60_min_ago
                    # and deviation_ma8_sotto_last_trade_price > -1.50
                    
                ):
                    buy = "condizione RCCR - BUY 1 DURANTE UNA CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo !  - riga 1036"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    
                    # compare prega per me !
                    
                    
                # BUY 1 forever young 1 PIU' PRUDENTE se ma200 > e se ma200 > ma300 - che si preoccupa degli effetti laterali
             
                elif (  
                    ma200_last > ma300_last
                    and deviation_ma100_laterale > 0.18
                    and ma200_last > ma200_15_min_ago
                    and ma3_last > ma11_last
                    and ma5_last > ma200_last
                    and ma2_last > ma2_2_min_ago
                ):

                    buy = "BUY 1 forever young 1 PIU' PRUDENTE se ma 200 > e se ma200 > ma300 - che si preoccupa degli effetti laterali - riga 1057"
                    action = "buy"
                    percentage = 20
                    
                    
                    
                # BUY 1 FOREVER YOUNG 2 PIU' AGGRESSIVO se ma 200 > e se ma200 > ma300
             
                elif (  
                    ma200_last > ma300_last
                    and ma200_last > ma200_15_min_ago
                    and ma13_last > ma69_last
                    and ma2_last > ma2_2_min_ago
                ):
                    
                    buy = "BUY 1 FOREVER YOUNG 2 PIU' AGGRESSIVO se ma 200 > e se ma200 > ma300 - riga 1072"
                    action = "buy"
                    percentage = 20

                    

                # BUY 1 con DEVIATION ASSURDA  se ma200 > da 20 min COMPRA con INCROCIO ma8 - ma200 >

                elif (    
                    ma200_last > ma200_120_min_ago
                    and deviation_assurda > 0.10
                    and ma5_last > ma300_last
                    and (ma8_prev < ma200_prev and ma8_last > ma200_last)
                    and (ma3_prev < ma8_prev and ma3_last > ma8_last)
                    
                    and ma20_last > ma20_2_min_ago
                    and ma39_last > ma39_2_min_ago
                    and ma69_last > ma69_2_min_ago
                    and deviation_buy_ma3_sopra_ma25 > 0.10
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 con DEVIATION ASSURDA se ma200 > da 120 min COMPRA con INCROCIO ma8 ma200 (ma5>ma300 evita gli EFFETTI LATERALI) - riga 1056"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_assurda = price / ma200_last
                    
                
            
            #############################################################################################################      COMPRA sessione 2
            
            elif self.session == 2:

                if (
                    ma69_last > ma69_2_min_ago
                    and deviation_buy2 > 0.04
                    and deviation_bellissima > 0.12
                    and deviation_buy_ma3_sopra_ma13 > 0.09
                    and deviation_ma7_sopra_ma40 > 0.07
                    and ma2_last > ma2_2_min_ago
                    and price > price_2_min_ago
                    and ma3_last > ma40_last
                ):
                    buy = "BUY 2A riga 1078"
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
                    buy = "BUY 2B riga 1097"
                    action = "buy"
                    percentage = 50
                    
                    # deviation_buy_ma3_sopra_ma13 > x e' fondamentale !
                    # deviation_buy2 = ma8_last/ma50_last

                   
                elif (
                    deviation_buy2 > 0.10
                    and deviation_bellissima > 0.12
                    and deviation_buy_ma3_sopra_ma13 > 0.10
                    and deviation_ma7_sopra_ma40 > 0.10
                    and ma4_last > ma9_last
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma40_last
                    and ma4_last > ma78_last
                ):
                    buy = "BUY 2C riga 1115"
                    action = "buy"
                    percentage = 50
                    
                    # deviation_buy2 = ma8_last / ma50
                    
                    
                ############################################################################################################ BUY 2 DURANTE IL CROLLO CHE CONTINUA    
                # se il crollo continua dopo che ha venduto sell 1 durante il crollo - ro cano CI RIPROVA !     
                
                # BUY 2  primo modo DURANTE IL CROLLO

                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -2.30
                    and ma3_last > ma7_last
                ):
                    buy = "BUY 2 DURANTE IL CROLLO - modo 1 riga 1132"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                 

                # BUY 2 secondo modo - DURANTE IL CROLLO - questa condizione e' entrata in azione ! ( e mi e' sembrata ben fatta !)

                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -1.70
                    and deviation_buy_crollo_2 > 0.11
                ):
                    buy = "BUY 2 DURANTE IL CROLLO - modo 2 riga 1146"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_buy_crollo_2 = ma3_last / ma13_last
                    
               
                ################################################### per comprare durante UNA piccola CORREZIONE che NON E' un forte ribasso e NON E' un crollo
                
                # BUY 2A PAZZA DURANTE UNA piccola CORREZIONE che NON E' un forte ribasso e NON E' un crollo ! (compare stammi vicino!)
                
                
                elif (

                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    and deviation_correzione > 0.015
                    and deviation_buy_ma5_sopra_ma20 > 0.10
                    
                    
                ):

                    buy = "BUY 2A PAZZA DURANTE UNA piccola CORREZIONE che non e' un forte ribasso e non e' un crollo ! con deviation_correzione > 0.02 - riga 1170"
                    action = "buy"
                    percentage = 10

                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    # ma5 non deve allontanarsi troppo dalla ma200 !
                    # compare prega per me !
                    
                    
                # BUY 2 DURANTE UNA CORREZIONE che NON E' un forte ribasso e NON E' un crollo ! con deviation_correzione > 0.02  696"
                 
                elif (

                    ma2_last > ma2_2_min_ago
                    and (ma20_prev < ma200_prev and ma20_last > ma200_last)
                    and deviation_correzione_2 > 0.03
                    and deviation_buy_crollo_1 < -0.60
                    and deviation_buy_crollo_1 > -0.90

                ):

                    buy = "BUY 2 DURANTE UNA CORREZIONE che NON E' un forte ribasso e NON E' un crollo ! con deviation_correzione > 0.02 - riga 1192"
                    action = "buy"
                    percentage = 20
                  
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma5_last / ma30_last
                    # compare prega per me !

                    

                
                # BUY 2 DURANTE UN FORTE RIBASSO che NON E' UN CROLLO ! (compare stammi vicino!) 
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -0.60
                    and deviation_buy_crollo_1 > -1.50
                    and deviation_bellissima > 0.17
                ):
                    buy = "BUY 2 DURANTE UN FORTE RIBASSO che NON E' UN CROLLO ! and deviation_bellissima > 0.17 -  riga 1211"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    
                    
                    
                # buy 2 esperimentali # CON INCROCIO 3-200 HO RISOLTO IL PROBLEMA DEL BUY 2 ECCEZIONALE CHE COINCIDEVA QUASI CON IL SELL 1 ! 
                
                
                # BUY 2 andamento laterale - se ma200 sale da 20 min compra con 4-30 ma sul BUY 2 lo 0.50 evita GLI EFFETTI LATERALI !

                elif (
                    ma200_last > ma200_20_min_ago
                    and ma20_last > ma200_last
                    
                    and (ma3_prev < ma200_prev and ma3_last > ma200_last)
                    and (ma20_prev < ma69_prev and ma20_last > ma69_last)
                    
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                    and ma10_last > ma10_2_min_ago
                    
                    and deviation_ma4_sopra_ma30 > 0.17
                    and deviation_ma100_laterale > 0.49
                    
                ):
                    buy = "BUY 2 andamento laterale se ma200> da 20 min compra con 4-30 (SUL BUY 2 0.50 e 20-69 vs EFFETTI LATERALI !) - riga 1239"
                    action = "buy"
                    percentage = 40
                    
                
                
                # BUY 2 andamento laterale - se ma200 sale da 20 min compra con 4-30 ma sul BUY 2 lo 0.50 vs EFFETTI LATERALI !

                elif (
                    
                    ma200_last > ma200_20_min_ago
                    and ma20_last > ma200_last
                    
                    and (ma3_prev < ma100_prev and ma3_last > ma100_last)
                    and (ma20_prev < ma69_prev and ma20_last > ma69_last)
                    
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                    and ma10_last > ma10_2_min_ago
                    
                    and deviation_ma4_sopra_ma30 > 0.17
                    and deviation_ma100_laterale > 0.49
                   
                ):
                    buy = "BUY 2 andamento laterale se ma200> da 20 min compra con 4-30 (SUL BUY 2 0.50 e 20-69 vs EFFETTI LATERALI !) - riga 1263"
                    action = "buy"
                    percentage = 40
                    
                    
                    
                # BUY 2 DOCCIA
                
                elif (    

                    ma200_last > ma200_90_min_ago
                    and ma20_last > ma200_last
                    and ma11_last > ma69_last
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma69_last
                    and (ma4_prev < ma25_prev and ma4_last > ma25_last)
                    and deviation_buy_ma3_sopra_ma25 > 0.05
                ): 
                    buy = "BUY 2 DOCCIA se ma200 > da 90 min ! COMPRA riga 1281"
                    action = "buy"
                    percentage = 20
                    
                
                
                # BUY 2 con DEVIATION ASSURDA = ma2 / ma200_last CON ma200 >

                elif (    
                    ma200_last > ma200_120_min_ago
                    and deviation_assurda > 0.10
                    and ma5_last > ma300_last
                    and ma10_last > ma10_2_min_ago
                    
                    and deviation_ma4_sopra_ma30 > 0.13
                    and deviation_ma100_laterale > 0.10
                    and (ma3_prev < ma200_prev and ma3_last > ma200_last)
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 2 con DEVIATION ASSURDA se ma200 sale da 120 min BUY con ma2-ma200 (ma5 > ma300 evita GLI EFFETTI LATERALI !) - riga 1300"
                    action = "buy"
                    percentage = 20    
          
                    # deviation_assurda = ma2 / ma200
            
              
                
                # BUY 2 che ci riprova TORNANDO ALLE ORIGINI con ma200< and ma300 < (compare stammi vicino !)
                
                elif (
                    deviation_buy2 > 0.10
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma7_last
                    and ma3_last > ma13_last
                    and deviation_buy_ma3_sopra_ma20 > 0.05
                    and deviation_ma4_sopra_ma25 > 0.05
                    and deviation_ma5_sopra_ma30 > 0.173
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                ):
               
                    buy = "BUY 2 che ci riprova TORNANDO ALLE ORIGINI con ma200< and ma300< - riga 1322"
                    action = "buy"
                    percentage = 30

                    # compare prega per me !
                    # se ma200< e ma300< si torna alle origini ! 8-50 ! (con ma2 > ma2 2 min ago)
                    # deviation_buy2 = ma8_last / ma50_last
                    
                    
                    
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

                    buy = "BUY 2 con ma200> e ma300> DURANTE UNA piccola CORREZIONE che non e' un forte ribasso e non e' un crollo - riga 1347"
                    action = "buy"
                    percentage = 10
                    
           
            ############################################################################################################ COMPRA sessione 3
            

            elif self.session == 3:

                if (
                    ma69_last >= ma69_2_min_ago
                    and deviation_buy3 > 0.12
                    and deviation_ma4_sopra_ma30 > 0.12
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.08
                    and ma4_last > ma9_last
                    and deviation_ma4_sopra_ma30 > 0.12
                    and deviation_buy_ma2_sopra_ma13 > 0.10
                    and ma4_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                ):  
                
                    buy = "BUY 3A con ma78 > riga 1370"
                    action = "buy"
                    percentage = 50

                    # deviation_buy3 = ma4_last/ma30_last
               
                elif (
                    deviation_buy3 > 0.02
                    and ma39_last > ma72_last
                    and deviation_buy3 > 0.02
                    and delta_buy3_incrocio_ma3_ma8 > 0.06
                    and deviation_ma4_sopra_ma30 > 0.15
                    and ma3_last > ma8_last
                    and ma3_last > ma72_last
                    and ma4_last > ma4_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma5_last > ma15_last
                    and ma7_last > ma25_last
                ):
                    buy = "BUY 3B RIVOLUZIONARIO se ma39 > ma72- riga 1390"
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
                    buy = "BUY 3C RIVOLUZIONARIO se ma78 < - riga 1410"
                    action = "buy"
                    percentage = 40
                    
                    # deviation_buy3 = ma4_last/ma30_last
                    
            
                # BUY 3 CON IL TURBO ! (compare stammi vicino!)
               
                elif (    
                    ma200_last > ma200_120_min_ago
                    and ma200_last > ma300_last
                    and ma20_last > ma200_last
                    
                    and (ma4_prev < ma25_prev and ma4_last > ma25_last)
                    and ma25_last > ma25_2_min_ago
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 3 CON IL TURBO - riga 1428"
                    action = "buy"
                    percentage = 50

             
                    
                elif (

                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    and deviation_correzione > 0.015
                    and deviation_buy_ma5_sopra_ma20 > 0.12
                    and deviation_ma5_sotto_ma200 > -1.00
                    
                ):

                    buy = "BUY 3A PAZZA DURANTE UNA piccola CORREZIONE che non e' un forte ribasso e non e' un crollo ! con deviation_correzione > 0.02 - riga 1445"
                    action = "buy"
                    percentage = 10

                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    # ma5 non deve allontanarsi troppo dalla ma200 !
            
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
                    buy = "BUY 4A con ma 78 > riga 1468"
                    action = "buy"
                    percentage = 50
                    

                elif (
                    ma78_last >= ma78_2_min_ago
                    and deviation_buy3 > 0.02
                    and delta_buy3_incrocio_ma3_ma8 > 0.05
                    and deviation_ma4_sopra_ma30 > 0.14
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last >= ma4_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                ):
                    buy = "BUY 4B RIVOLUZIONARIO con ma78 > - riga 1484"
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
                    buy = "BUY 4C RIVOLUZIONARIO con ma78 < - riga 1502"
                    action = "buy"
                    percentage = 50
                    
                    # deviation_buy3 = ma4_last/ma30_last
                    
                  
                # BUY 4A PAZZA DURANTE UNA piccola CORREZIONE che NON E' un forte ribasso e NON E' un crollo ! (compare stammi vicino!)
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    and deviation_correzione > 0.015
                    and deviation_buy_ma5_sopra_ma20 > 0.14
                    and deviation_ma5_sotto_ma200 > -1.00
                ):    
           
                    buy = "BUY 4A PAZZA DURANTE UNA piccola CORREZIONE che non e' un forte ribasso e non e' un crollo ! con deviation_correzione > 0.02 - riga 1520"
                    action = "buy"
                    percentage = 10

                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    # ma5 non deve allontanarsi troppo dalla ma200 !
             
            ############################################################################################################  compra sessione 5 in poi
            #  piu' alto il BUY - "effetti laterali"

            else:

                if (
                    ma78_last >= ma78_2_min_ago
                    
                    and deviation_buy3 > 0.12
                    and deviation_bellissima > 0.17
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.10
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    and ma6_last > ma15_last
                    and ma7_last > ma25_last
                    and ma2_last > ma2_2_min_ago
              
                ):
                    buy = "BUY 5A con ma78 > and deviation_bellissima > 0.163 (PER SPEZZARE LA CATENA -effetti laterali) riga 1547"
                    action = "buy"
                    percentage = 50
                    
                    # deviation_bellissima = 6/30
                    # spezzare la catena dei buy - effetti laterali !
                    # se e' arrivato il buy 5 e' molto probabile che il trend sia consolidato
                    # e, a questo punto, non importa se compra con un + 0.10 piu' in alto. NON FA UNA GRANDE DIFFERENZA !
                    
                    
                   
                elif (
                    ma200_last >= ma200_120_min_ago
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                    and ma7_last > ma25_last
                    and ma13_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                ):   
                    buy = "BUY 5B RIVOLUZIONARIO che NON SPEZZA LA CATENA SE ma200> 120 min) - riga 1568"
                    action = "buy"
                    percentage = 50
                    
                    # deviation_buy3 = ma4_last/ma30_last
                    # ok tu non voi spezzare la catena.
                    # ma per essere un BUY 5 devi avere almeno ma13>ma50 cazzo !
                    
                    
                elif (
                    ma78_last >= ma78_2_min_ago
                    and deviation_buy3 > 0.03
                    and deviation_bellissima > 0.17
                    and delta_buy3_incrocio_ma3_ma8 > 0.05
                    and deviation_ma4_sopra_ma30 > 0.13
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                    and ma7_last > ma25_last
                    
                    and ma2_last > ma2_2_min_ago
                    
                ):
                    buy = "BUY 5c RIVOLUZIONARIO con ma78 > and deviation_bellissima > 0.163 (PER SPEZZARE LA CATENA -effetti laterali) - riga 1590"
                    action = "buy"
                    percentage = 50
                    
                    # deviation_buy3 = ma4_last/ma30_last

                    
                elif (
                    ma78_last < ma78_2_min_ago
                    and ma20_last > ma200_last
                    
                    and deviation_buy3 > 0.04
                    and deviation_bellissima > 0.181
                    and delta_buy3_incrocio_ma3_ma8 > 0.075
                    and deviation_ma4_sopra_ma30 > 0.19
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                    and ma7_last > ma25_last
                    
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 5d RIVOLUZIONARIO con ma78 < and deviation_bellissima > 0.163 - riga 1612"
                    action = "buy"
                    percentage = 50
                    
                    # deviation_buy3 = ma4_last/ma30_last
                    
                    
                    
                    
                # BUY 5A PAZZA DURANTE UNA piccola CORREZIONE che NON E' un forte ribasso e NON E' un crollo ! (compare stammi vicino!)
                
                
                elif (

                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    and deviation_correzione > 0.015
                    and deviation_buy_ma5_sopra_ma20 > 0.14
                    and deviation_ma5_sotto_ma200 > -1.00
                    
                ):

                    buy = "BUY 5 PAZZA DURANTE UNA piccola CORREZIONE che non e' un forte ribasso e non e' un crollo ! con deviation_correzione > 0.02 - riga 1635"
                    action = "buy"
                    percentage = 10

                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    # ma5 non deve allontanarsi troppo dalla ma200 !
                    # compare prega per me !
                    
                
                    
                    
        ############################################################################################

        #  V E N D I T A !                                                                           nota per il compa : la vendita e' fatta con 3 sessioni e 7 eccezioni

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
            # 0.25 - 0.59  MARADONA 5-25 CHE DOPO 60 MIN DIVENTA 5-39 che dopo 90 min diventa 5-50
            # 0.60 - 1.20  RONALDO CHE DOPO 60 MIN DIVENTA 4-20
            # 1.21 - 2.50  TACCO DI ALLAH
            #  > 2.50      SI VIVE TRA GLI ANGELI
            
            # aumento la perdita tollerata se trend < (ma50<) MA ma200> e ma200 > ma300 !
            # 7 vendite eccezionali
            

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
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.23 - riga 1724"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.27 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.27 - 0.60 LA PRIMA FINTA DI MARADONA - riga 1737"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.61 and deviation_sell < 0.79
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.61 - 0.79 IL PRIMO DRIBBLING ALLA RONALDO  - riga 1750"
                        action = "sell"

                    # attenzione : tacco di allah e dribbling alla ronaldo SOLO con ma50> (altrimenti si attivano in "sell durante il crollo" che ha le sue dinamiche.)
                    
                    

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 0.80 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell 0.80 - 1.20 ( DOPPIA FINTA ALLA RONALDO ! ) - riga 1764"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 1.21 and deviation_sell < 1.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell 1.21-1.7( TACCO DI ALLAH ! )- riga 1777"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 1.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell > 1.71 ( SI VA TRA GLI ANGELI, compa ! )- riga 1790"
                        action = "sell"
                        
                        
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 < and incrocio 3-28- riga 1805"
                        action = "sell"

                    # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                    
                    

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 - riga 1818"
                        action = "sell"
                    
                    
                    
                    # ---------------------------------------------------------------------------------------------------------------------- crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - riga 1831"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 1844"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                        and deviation_sell > 0.61 and deviation_sell < 0.80
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - riga 1855"
                        action = "sell"
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma2_prev > ma5_prev and ma2_last < ma5_last)
                        and deviation_sell > 0.81
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - riga 1866"
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
                        sell = "SELL 1 (3-5 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.24 - riga 1886"
                        action = "sell"
                         
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.27 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                       
                        
                    ):
                        sell = "SELL 1 (3-5 min) con ma50> 5-25 and deviation_sell 0.27 - 0.60 - la prima FINTA ALLA MARADONA - riga 1901"
                        action = "sell"
                         
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                     

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.61 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 > and incrocio 3-15 and deviation_sell 0.91 - 1.20 DRIBBLING ALLA RONALDO - riga 1915"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 1.21 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 > and incrocio 3-20 and deviation_sell 1.21 -2.70 ( TACCO DI ALLAH ! ) - riga 1926"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 > and incrocio 3-11 and deviation_sell > 2.71 ( SI VA TRA GLI ANGELI, comba ! ) - riga 1937"
                        action = "sell"
                        
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 < and incrocio 3-28 - riga 1951"
                        action = "sell"
                        
                         
                        # deviation_sell_ma78 = ma3_last / ma78_last
                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.25
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.25 - riga 1966"
                        action = "sell"

                    
                    
                    # guadagno durante il crollo o il trend discendente
                     
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23 and deviation_sell < 0.80
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-23 and gain > 0.23 - riga 1979"
                        action = "sell"
                        
                    
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma2_prev > ma5_prev and ma2_last < ma5_last)
                        and deviation_sell > 0.81 and deviation_sell < 1.70
                        and ma2_last < ma2_2_min_ago

                    ):

                        sell = "SELL 1 CROLLO (3-5 min) con ma50 < and incrocio 2-5 and gain > 0.81-1.70 - riga 1994"
                        action = "sell"

                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma9_prev and ma3_last < ma9_last)
                        and deviation_sell > 1.71
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-9 and gain > 1.71 - riga 2007"
                        action = "sell"
                        
                        
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 2021"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE !
                        
                        

                ################################################################################################################################### sessione 1 ( 5-12 min )

                # VENDITA - da 5 a 12 minuti = da 300 a 720 secondi

                elif seconds_since_last_trade > 300 and seconds_since_last_trade <= 720:

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.41
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - riga 2041"
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
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - riga 2056"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        
                        and deviation_sell > 0.27 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                    
                    ):
                        sell = "SELL 1 (5-12 min) con ma50> 5-25 and deviation_sell 0.27 - 0.60 - FINTA ALLA MARADONA - riga 2070"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma13_last
                        
                        and deviation_sell > 0.61 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 >  3-13 and deviation_sell 0.61 - 0.90 - DRIBBLING ALLA RONALDO - riga 2085"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 3-15 and deviation_sell 0.91 - 1.20 ( DOPPIA FINTA ALLA RONALDO ) - riga 2100"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 1.21 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 3-15 and deviation_sell 1.21-2.70 ( TACCO DI ALLAH ! ) - riga 2115"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 3-11 and deviation_sell > 2.71 ( SI STA TRA GLI ANGELI, compa! ) - riga 2126"
                        action = "sell"
                        
                        
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 < and incrocio 3-28 - riga 2141"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 < and incrocio 3-100 (cuscino di sant' antonio) - riga 2154"
                        action = "sell"
                        
                        
                    
                    
                    # ------------------------------------------------------------------------------- guadagno con crollo
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23 and deviation_sell < 0.54
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 < GUADAGNO DURANTE IL CROLLO 0.23-0.54 con incrocio 3-23 - riga 2170"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 0.55
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 < GUADAGNO DURANTE IL CROLLO > 0.55  and incrocio 3-13 - riga 2180"
                        action = "sell"
                        
                        

                    # ------------------------------------------------------------------------------------------------------------ PARACADUTE crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.40
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 PARACADUTE CROLLO (5-12 min) con ma50 < and ma3 < ma16 (no incrocio) and deviation_sell < -0.40 - riga 2193"
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
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-72 and deviation sell -0.65 e vaffanculo ! - riga 2216"
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
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.36 - riga 2233"
                        action = "sell"
                        
                        # viva sant' antonio !
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.27 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 1 (12-21 min) con ma50> and 5<25 and deviation_sell 0.27-0.56 - FINTA ALLA MARADONA - riga 2246"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma13_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 1 (12-21 min) con ma50> and 3<13 (NO INCROCIO 3-13) and deviation_sell 0.57-0.90 - DOPPIO PASSO ALLA RONALDO - riga 2260"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 ( DOPPIA FINTA ALLA RONALDO )- riga 2275"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.21 and deviation_sell < 1.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-30 and deviation_sell 1.21-1.70 ( IL TACCO DI ALLAH ) - riga 2289"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 1.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-15 and deviation_sell > 1.71 ( SI STA TRA GLI ANGELI, compa ! ) - riga 2299"
                        action = "sell"
                        
                        
                      
                    
                    ##########################################################################################
                    # NON TOCCARE ! CUSCINO DI SANT' ANTONIO !
                    # L' INCROCIO 5-100 MI SALVA ! MA 5<100 VENDE DURANTE IL RIBASSO !
                    ##################################################################### con trend discendente

                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.159
                        and deviation_sell < -0.29
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 < and deviation_ma39 < -0.159 and deviation_sell < -0.29 - riga 2316"
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
                        sell = "SELL 1 (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - riga 2335"
                        action = "sell"
                        
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50< !
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - riga 2347"
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
                        sell = "SELL 1 PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 2362"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                        

                    # ----------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell > 0.25 and deviation_sell > 0.54
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3 - 16 and deviation_sell 0.25-0.54 - riga 2379"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 0.55
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3-11 and deviation_sell > 0.55 - riga 2389"
                        action = "sell"
                        
                    
                    # ----------------------------------------------------------------------------- torna a casa durante il crollo con minor danno 
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma36_prev and ma3_last < ma36_last)
                        and deviation_sell < -0.25
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 torna a casa durante il crollo con minor danno  (12-21 min) con ma50 < and incrocio 3-36 and deviation_sell < -0.25 - riga 2401"
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
                        and ma2_last < ma2_2_min_ago
                    
                    ):
                        sell = "SELL 1 (21-60 min) con ma50> and incrocio 3-78 and deviation_sell<-0.65 - riga 2422"
                        action = "sell"
                        
                        # VENDITA IN BASSO 
                        # and deviation_ma39 < -0.16 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        # and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        # and deviation_sell < -0.26
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_sell < -0.32
                        and ma3_last < ma50_last
                        and ma2_last < ma2_2_min_ago
                    
                    ):
                        sell = "SELL 1 (21-60 min) con ma50> and deviation_sell <-0.32 and ma3_last < ma50_last - riga 2441"
                        action = "sell"
                        
                        # VENDITA 1 IN ALTO dopo BUY IN RISALITA
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
                        sell = "SELL 1 (21-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.26 - riga 2459"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma5_last < ma30_last
                        and deviation_sell > 0.31 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (60-90 min) con ma50 > and 5-30 and deviation_sell 0.31-0.56 la prima FINTA ALLA MARADONA - riga 2473"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma5_last < ma15_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-60 min) con ma50 > and 5-15 (era 4-15) and deviation_sell 0.51 - 0.90 ELASTICO ALLA RONALDO - riga 2485"
                        action = "sell"
                        
                        # dopo 26 minuti non c'e' piu' quello scatto in avanti - dribbling- che si verifica nei primi minuti
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma4_prev > ma16_prev and ma4_last < ma16_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-60 min) con ma50 > and incrocio 4-16 and deviation_sell 0.91 - 1.20 (DOPPIA FINTA DI RONALDO)- riga 2500"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma4_prev > ma18_prev and ma4_last < ma18_last)
                        and deviation_sell > 1.21 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-60 min) con ma50 > and incrocio 4-18 and deviation_sell 1.21 - 2.70 (DOPPIO PASSO DI RONALDO)- riga 2514"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma9_prev and ma3_last < ma9_last)
                        and deviation_sell > 2.71 and deviation_sell < 5.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-60 min) con ma50 > and incrocio 3-9 and deviation_sell 2.71 - 5.70 (TACCO DI ALLAH) - riga 2526"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell > 5.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-60 min) con ma50 > and incrocio 3-39 and deviation_sell > 2.71 (SI STA TRA GLI ANGELI, comba !) - riga 2536"
                        action = "sell"
                    
                    
                    
                    ##################################################################### con trend discendente
                    
                    # ho diviso in 2 parti separate la lezione del maestro
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma39 < -0.28)
                        
                    ):
                        sell = "SELL 1 maestro parte 1 (21-60 min) con ma50 < and deviation_ma39 < -0.28  - riga 2550"
                        action = "sell"
                        
                    
                    
                    
                    elif (        
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.26)
                    ):
                        sell = "SELL 1 maestro parte 2 (21-60 min) con ma50 < and deviation_sell < -0.26 - riga 2559"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.37
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - riga 2571"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - riga 2582"
                        action = "sell"
                        
                        
                        
                    ############################################################# con ma50 discendente MA ma200 ET ma200>ma300 - PERDITA TOLLERATA AUMENTA
                    # ho diviso il maestro in 2 !
                    
                    
                    elif (
                        
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma39 < -0.28)
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 compa (21-60 min) con ma50 < and deviation_ma39 < -0.28 con > PERDITA TOLLERATA - riga 2598"
                        action = "sell"
                        
                        # and deviation_ma39 < -0.15 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        
                        # ERRORE GRAVE CORRETTO DAL MAESTRO - VENDEVA MENTRE SALIVA !
                        # ma50_last < ma50_2_min_ago
                        # and ma2_last < ma2_2_min_ago
                        # and deviation_ma39 < -0.25
                        # or deviation_sell < -0.26
                        
                      
                    elif (    
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.29)
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 compa (21-60 min) con ma50 < and deviation_sell < -0.29 con > PERDITA TOLLERATA - riga 2616"
                        action = "sell"
                        
                        # and deviation_ma39 < -0.15 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        
                        # ERRORE GRAVE CORRETTO DAL MAESTRO - VENDEVA MENTRE SALIVA !
                        # ma50_last < ma50_2_min_ago
                        # and ma2_last < ma2_2_min_ago
                        # and deviation_ma39 < -0.25
                        # or deviation_sell < -0.26
                        
                    
                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        
                        and ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.40
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.40 - CON PERDITA TOLLERATA > - riga 2636"
                        action = "sell"
                        
                        

                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        
                        and ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-60 min) con ma50 < and INCROCIO 3-100 -0.30 CUSCINO DI SANT' ANTONIO - CON PERDITA TOLLERATA > - riga 2649"
                        action = "sell"
                        
                  
                    
                    # -------------------------------------------------------------------------------------- guadagno durante il crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.30 and deviation_sell < 0.54
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 eventuale guadagno durante il crollo (21-60 min) con ma50 < incrocio 3 - 18 and deviation_sell 0.30 - 0.54 - riga 2663"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 0.55
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 eventuale guadagno durante il crollo (21-60 min) con ma50 < incrocio 3 - 11 and deviation_sell > 0.55 - riga 2673"
                        action = "sell"
                        
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell < -0.18
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 piccola perdita durante il crollo (21-60 min) con ma50 < incrocio 3 - 18 and deviation_sell < -0.18 - riga 2685"
                        action = "sell"
                        
              
                ##############################################################################################################################  SESSIONE 1 ( da 60 a 90 min )

                # VENDITA - da 60 a 90 min - da 3600 a 5400 secondi in poi
                
                elif (
                    seconds_since_last_trade > 3600 and seconds_since_last_trade <= 5400
                ):
                    
                    
                    if (    
                        ma50_last > ma50_2_min_ago
                        and deviation_ma39 < -0.22
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL da 60 a 90 min con ma50 > and deviation_ma39 <-0.22 - riga 2703"
                        action = "sell"
                        
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                     
                        
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and deviation_sell < -0.23
                        and ma3_last < ma50_last
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL da 60 a 90 min con ma50 > and deviation_sell < -0.23 and ma3_last < ma50_last  - riga 2758"
                        action = "sell"
                        
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        
                   
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma50_prev and ma5_last < ma50_last)
                        and deviation_sell > 0.32 and deviation_sell < 0.52
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 60 a 90 min con ma50 > and incrocio 5-50 and deviation_sell 0.31-0.52 la prima FINTA ALLA MARADONA - riga 2771"
                        action = "sell"
                        
                        # MARADONA accompagna nelle prime fasi di crescita il titolo. poi interviene RONALDO se il rialzo comincia a farsi piu' consistente.
                    
                    
                    ############################################################################ ronaldo 60-90 min dal buy se ma200 > somiglia a maradona
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma200_last > ma200_120_min_ago
                        and (ma4_prev > ma50_prev and ma4_last < ma50_last)
                        and deviation_sell > 0.53 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 60 a 90 min con ma50> and incrocio 4-20 and deviation_sell 0.51-0.90 RONALDO - riga 2786"
                        action = "sell"
                        
                        
                    ############################################################################ ronaldo 60-90 min dal buy se ma200 < non perdona
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma200_last < ma200_120_min_ago
                        and (ma4_prev > ma20_prev and ma4_last < ma20_last)
                        and deviation_sell > 0.53 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 60 a 90 min con ma50> and incrocio 4-20 and deviation_sell 0.51-0.90 RONALDO - riga 2799"
                        action = "sell"
                        
                    ##################################################################################################################
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 60 a 90 min con ma50 > and incrocio 3-30 and deviation_sell 0.91 - 1.49 RABONA DI RONALDO - riga 2810"
                        action = "sell"
                  
                        # ma ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                        
                       
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 60 a 90 min con ma50 > incrocio 3-33 and deviation_sell > 1.50 DOPPIO PASSO ALLA RONALDO - riga 2822"
                        action = "sell"
                        
                        
                      
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 da 60 a 90 min con ma50 > incrocio 3-11 and deviation_sell > 2.71 TACCO DI ALLAH - riga 2834"
                        action = "sell"
                        
                  
                    ######################################################################################## con trend discendente ma50 <
                    
                    ################################################################ ipotesi peggiore e sono cazzi ! ( sempre con ma50 < )
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma300_last
                        and deviation_trend_ma200 < -0.10
                        
                        and deviation_ma39 < -0.19
                        and ma2_last < ma2_2_min_ago
                        and deviation_sell < -0.195
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 60 a 90 min IPOTESI PEGGIORE con ma50 < con deviation_ma39 <-0.19 and deviation_sell < -0.195 - riga 2851"
                        action = "sell"
                        
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma300_last
                        and deviation_trend_ma200 < -0.10
                        
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.15
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 60 a 90 min IPOTESI PEGGIORE con ma50 < con incrocio 3-78 and deviation_sell < -0.15 - riga 2865"
                        action = "sell"
                        
               
                    ############################################################### ipotesi mediana 1 un po' meno peggio ( sempre con ma50 < )
                  
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma300_last
                        and deviation_trend_ma200 > -0.10
                        
                        
                        and deviation_ma39 < -0.19
                        and ma2_last < ma2_2_min_ago
                        and deviation_sell < -0.195
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 60 a 90 min IPOTESI un po' MENO PEGGIO con ma50 < con deviation_ma39 <-0.19 and deviation_sell < -0.195 - riga 2884"
                        action = "sell"
                        
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma300_last
                        and deviation_trend_ma200 > -0.10
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.15
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 60 a 90 min IPOTESI un po' MENO PEGGIO con ma50 < con incrocio 3-78 and deviation_sell < -0.15 - riga 2897"
                        action = "sell"
                        
                
                    #################################################################### # ipotesi mediana 2 un po' meglio ( sempre con ma50 < )
                   
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma300_last
                        and deviation_trend_ma200 < -0.10
                        
                        and deviation_ma39 < -0.22
                        and ma2_last < ma2_2_min_ago
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 60 a 90 min UN PO' MEGLIO con ma50 < con deviation_ma39 <-0.22 and deviation_sell < -0.23 - riga 2863"
                        action = "sell"
                        
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma300_last
                        and deviation_trend_ma200 < -0.10
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.17
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 60 a 90 min UN PO' MEGLIO con ma50 < con incrocio 3-78 and deviation_sell < -0.17 - riga 2876"
                        action = "sell"    
                    
                    
                   
                    
                    ############################################################### con ma50 discendente MA trend ma200> ET ma200 > ma300 - PERDITA TOLLERATA AUMENTA
                    
                    # ipotesi migliore ( sempre con ma50 < ) MA....!
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma300_last
                        and deviation_trend_ma200 > -0.10
                        
                        and deviation_ma39 < -0.24
                        and ma2_last < ma2_2_min_ago
                        and deviation_sell < -0.25
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 60 a 90 min IPOTESI MIGLIORE ma sempre con ma50 < con deviation_ma39 < -0.24 and deviation_sell < -0.25 - CON PERDITA TOLLERATA > - riga 2897"
                        action = "sell"
                        
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma300_last
                        and deviation_trend_ma200 > -0.10
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.17
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 60 a 90 min IPOTESI MIGLIORE ma sempre con ma50 < con incrocio 3-78 and deviation_sell < -0.17 - CON PERDITA TOLLERATA > - riga 2911"
                        action = "sell"
                        
                        
                ###########################################################################################################################
                ###########################################################################################################################
                
                
                ############################################################################################################################ SESSIONE 1 ( > 90 min )

                # VENDITA - da 90 minuti in poi = da 5400 secondi in poi

                elif seconds_since_last_trade > 5400:

                    
                    if (    
                        ma50_last > ma50_2_min_ago
                        and deviation_ma39 < -0.22 
                        and deviation_sell < -0.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 dopo 90 min con ma50 > and deviation_ma39 <-0.22 and deviation_sell < -0.21 - riga 2932"
                        action = "sell"
                        
                        
                       
                    elif (     
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma50_last 
                        and deviation_sell < -0.22
                        and ma25_last < ma25_2_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 dopo 90 min con ma50 > and ma3_last < ma50_last and deviation_sell < -0.22 and ma25 < - riga 2944"
                        action = "sell"
                        
                  
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma5_last < ma50_last
                        and deviation_sell > 0.35 and deviation_sell < 0.64
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 dopo 90 min con ma50 > con 5-50 and deviation_sell 0.35 - 0.64 la prima FINTA DI MARADONA (ma15 invece di ma13) - riga 2956"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma42_prev and ma5_last < ma42_last)
                        and deviation_sell > 0.65 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 dopo 90 min con ma50 > incrocio 5-42 (!) and deviation_sell 0.65 - 1.49 RABONA ALLA RONALDO - riga 2968"
                        action = "sell"
                        
                        
                      
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 dopo 90 min con ma50 > incrocio 3-30 and deviation_sell  1.50 - 2.70 DOPPIO PASSO DI RONALDO - riga 2979"
                        action = "sell"
                        
                        
                    
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 2.71 and deviation_sell < 5.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 dopo 90 min con ma50 > incrocio 3-13 (!) and deviation_sell > 2.71 TACCO DI ALLAH - riga 2992"
                        action = "sell"
                        
                     
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma69_prev and ma3_last < ma69_last)
                        and deviation_sell > 5.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 dopo 90 min con ma50 > incrocio 3-69 (!) and deviation_sell > 5.71 SI STA TRA GLI ANGELI, compa ! - riga 3004"
                        action = "sell"
                        
                     
                    ######################################################################################## con trend discendente
                    
                    # con or IL MAESTRO HA FATTO LA CORREZIONE ! questa che vedi e' stata corretta dal maestro
                    
                    elif (    
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma39 < -0.17)
                        and ma5_last < ma5_2_min_ago
                    ):
                        sell = "SELL 1 dopo 90 min con ma50 < con deviation_ma39 <-0.17 - riga 3016"
                        action = "sell"
                        
                
                    elif (
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.13 and ma3_last < ma39_last )
                       
                    ):
                        sell = "SELL 1 dopo 90 min con ma50 < and (deviation_sell < -0.13 and ma3_last < ma39_last) - riga 3024"
                        action = "sell"
                        
                    
                    ############################################################################### aumento della perdita tollerata ! 50< MA 200> e 200>300
                    # ho diviso il compare in 2 !
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma39 < -0.20)
                        and deviation_trend_ma200 > -0.12
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 1 compa dopo 90 min con ma50 < and deviation_ma39 < -0.20  con > PERDITA TOLLERATA - riga 3039"
                        action = "sell"
                     
                        
                    elif (    
                        
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.21 and ma3_last < ma39_last )
                        and deviation_trend_ma200 > -0.12
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 compa dopo 90 min con ma50 < (deviation_sell < -0.21 and ma3_last < ma39_last) con > PERDITA TOLLERATA - riga 3050"
                        action = "sell"
                        
          
            ################################################################################################# SESSIONE 1 ( vendita con questi 7 altri modi )
           
            
                    # 1 - ro cano VENDE CON UN SALVAGENTE
                
                    elif deviation_ma39 < -0.25 and deviation < -0.36 and ma50_last > ma50_2_min_ago:

                        sell = "SELL 1 SALVAGENTE 3-39 con ma50 < riga 3061"
                        action = "sell"

                    # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!
                    
                    
                    

                    # 2 - ro cano VENDE DURANTE UN CROLLO IMPROVVISO !
                    
                    elif deviation < -0.62:
                        sell = "SELL 1 CROLLO IMPROVVISO - riga 3072"
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

                        sell = "SELL 1 DOLCE ATTESA con ma13 > and deviation < -0.40 - riga 3091"
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

                        sell = "SELL 1 DOLCE ATTESA con ma13 < and deviation < -0.35 - riga 3111"
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

                        sell = "sessione 1 SELL TEMPO e se ma8 < ma50 and deviation_sell < -0.49 - riga 3127"
                        action = "sell"
                        
                        # ma13 troppo lenta !
                        # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                        
                  
                    # 6 - RIBASSO IMPROVVISO
                    
                    elif (
                        ma78_last > ma78_2_min_ago
                        and deviation_ribasso_improvviso < -0.63
                  
                    ):
                        sell = "SELL 1 RIBASSO IMPROVVISO - riga 3141"
                        action = "sell"
                
            
            
                    # 7 - RIBASSO IMPROVVISO
                
                    elif (
                        ma78_last < ma78_2_min_ago
                        and deviation_ribasso_improvviso < -0.63
                    
                    ):
                        sell = "SELL 1 RIBASSO IMPROVVISO - riga 3153"
                        action = "sell"
               
            ########################################################################################################################### SESSIONE 2
            
            # ALLA SESSIONE 2 MANCAva UN ACQUISTO DURANTE IL CROLLO SE PER ES SESSIONE 1 HA GIA' VENDUTO MA IL TITOLO RESTA IN IPERVENDUTO
            
            elif self.session == 2:

                ############################################################################################################# sessione 2 ( 0-3 min )
                
                if seconds_since_last_trade > 0 and seconds_since_last_trade <= 180:

                    # con ma50 >

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.23 - riga 3175"
                        action = "sell"
                  
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.25 - 0.60 FINTA DI MARADONA - riga 3185"
                        action = "sell"
              
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.61 and deviation_sell < 0.79
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.61 - 0.79 DRIBBLING DI RONALDO- riga 3194"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 0.80 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell 0.80 - 1.20 DOPPIO PASSO ALLA RONALDO - riga 3206"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell > 1.21 (che sarebbe come IL DRIBBLING ALLA RONALDO !)- riga 3218"
                        action = "sell"
                
                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 < and incrocio 3-28- riga 3229"
                        action = "sell"
                        
                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                  
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 - riga 3240"
                        action = "sell"
                        

                    # ---------------------------------------------------------------------------------------------------------------------- crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - riga 3252"
                        action = "sell"
                        
                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 3265"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                        and deviation_sell > 0.60
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - riga 3277"
                        action = "sell"
                 
                ################################################################################################################################ SESSIONE 2 ( 3-5 min )

                # VENDITA - da 3 a 5 minuti = da 180 a 300 secondi

                elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 300:

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell < -0.25
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.25 - riga 3293"
                        action = "sell"
                  
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - riga 3303"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.57 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 > and incrocio 3-15 and deviation_sell 0.57 - 1.20 - riga 3316"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - riga 3327"
                        action = "sell"
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 < and incrocio 3-28 - riga 3341"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        # deviation_sell_ma78 = ma3_last / ma78_last
                  
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.23 - riga 3353"
                        action = "sell"
                        

                    # ---------------------------------------------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 3365"
                        action = "sell"
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 3375"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        

                ####################################################################################################################### SESSIONE 2  ( 5-12 min )

                # VENDITA - da 5 a 12 minuti = da 300 a 720 secondi

                elif seconds_since_last_trade > 300 and seconds_since_last_trade <= 720:

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.41
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - riga 3393"
                        action = "sell"
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.25
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - riga 3403"
                        action = "sell"
                   
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL (12-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - riga 3414"
                        action = "sell"
                   
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma15_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 >  3 < 15 and deviation_sell 0.57 - 0.90 - DRIBBLING ALLA RONALDO - riga 3424"
                        action = "sell"
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 3435"
                        action = "sell"
                   
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - riga 3444"
                        action = "sell"
                  
                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.31
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 < and incrocio 3-28 and deviation_sell < -0.31 - riga 3455"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                  
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 < and incrocio 3-100 (cuscino di sant' antonio) - riga 3466"
                        action = "sell"
                 
                    # ------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 guadagno con crollo (5-12 min) con ma50 < and incrocio 3-23 - riga 3477"
                        action = "sell"
                        

                    # ------------------------------------------------------------------------------------------------------------ PARACADUTE crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 3489"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
              
                ############################################################################################################################ SESSIONE 2 ( 12-21 min )

                # VENDITA - da 12 a 21 minuti = da 720 a 1260 secondi

                elif (
                    seconds_since_last_trade > 720 and seconds_since_last_trade <= 1260
                ):

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma69_prev and ma3_last < ma69_last)
                        and deviation_sell < -0.34
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and incrocio 3-69 and deviation sell -0.34 e vaffanculo ! - riga 3508"
                        action = "sell"
                        
                        # and deviation_ma39 < -0.29 vendeva troppo presto
                        # ATTENZIONE "and (ma3_prev > ma39_prev and ma3_last < ma39_last)" con ma39 NON HA INCROCIATO
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma100_prev and ma3_last < ma100_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.36 - riga 3520"
                        action = "sell"
                        
                        # viva sant' antonio !
                        
                      
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma28_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and 5<28 and deviation_sell 0.25-0.56 - MARADONA - riga 3533"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma25_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and 3<25 and deviation_sell 0.57-0.90 - DOPPIO PASSO ALLA RONALDO fino a +0.50 - riga 3547"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and incrocio 3-15 and deviation_sell 0.91 - 1.20 - riga 3561"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and incrocio 3-13 and deviation_sell > 1.21 - riga 3574"
                        action = "sell"
                        
                        

                    ##########################################################################################
                    # NON TOCCARE ! CUSCINO DI SANT' ANTONIO !
                    # L' INCROCIO 5-100 MI SALVA ! MA, attenzione, 5<100 VENDE DURANTE IL RIBASSO !
                    ########################################################################################### con trend discendente

                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.20
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 < and deviation_ma39 < -0.20 - riga 3590"
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
                        sell = "SELL 2 (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - riga 3609"
                        action = "sell"
                        
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50< ! 
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.28
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - riga 3622"
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
                        sell = "SELL 2 PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 3638"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        

                    # ----------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma4_prev > ma20_prev and ma4_last < ma20_last)
                        and deviation_sell > 0.22
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 4 - 20 and deviation_sell > 0.22 - riga 3653"
                        action = "sell"
                        
                        
                        
                        

                ################################################################################################################################## SESSIONE 2 ( 21-60 min )

                # VENDITA - da 21 a 60 minuti = da 1261 a 3600 secondi
                
                
                elif (
                    seconds_since_last_trade > 1261 and seconds_since_last_trade <= 3600
                ):
                    
                    
                    
                    ######################################################################################################## 2 righe compa RADDOPPIATE !
                    
                    if (        
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma39 < -0.25)
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and deviation_ma39 < -0.25 - riga 3676"
                        action = "sell"
                        
                        
                    
                    
                    
                    elif (    
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.28 and ma3_last < ma50_last)
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and (deviation_sell < -0.28 and ma3_last < ma50_last) - riga 3686"
                        action = "sell"
                        
                        
                    
                    
                    
                    elif (        
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma39 < -0.29)
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and deviation_ma39 < -0.29 - TOLLERANTE ! - riga 3697"
                        action = "sell"
                        
                        
                    
                    
                    
                    elif (    
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.30 and ma3_last < ma50_last)
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and (deviation_sell < -0.30 and ma3_last < ma50_last) TOLLERANTE ! - riga 3708"
                        action = "sell"
                        
                    ##############################################################################################################################
                        
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.26
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.26 - riga 3722"
                        action = "sell"
                  
                        # deviation_sell = ma3_last/last_trade_price
                        # IMPORTANTE !   
                        # vai compaaaaaaaaaa
                        # poco guadagno ma piu' alta
                        # molto guadagno ma piu' bassa
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma5_last < ma39_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and 5<39 and deviation_sell 0.25 - 0.56 MARADONA e' piu' stanco e paziente - riga 3740"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    ############################################################################################################################
                    # ATTENZIONE !
                    # ELASTICO ALLA RONALDO SE ma200 > ma200 120 min ago
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma200_last > ma200_120_min_ago
                        and ma5_last < ma69_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > AND 200>120 min and 5<69 (fidati!) and deviation_sell 0.57 - 0.90 ELASTICO ALLA RONALDO - riga 3759"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    # ELASTICO ALLA RONALDO SE ma200 < ma200 120 min ago
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma200_last < ma200_120_min_ago
                        and ma3_last < ma25_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > AND 200>120min and 3<25 and deviation_sell 0.57 - 0.90 ELASTICO ALLA RONALDO - riga 3754"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                    
                    ##############################################################################################################
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                   
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and incrocio 3-16 and deviation_sell 0.91 - 1.20 - riga 3791"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.21 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and incrocio 3-30 (!) SI PROPRIO COSI' ! 3-30 ! and deviation_sell 1.21 - 2.70 - riga 3804"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "sessione 2 SELL (21-60 min) con ma50 > and incrocio 3-11 and deviation_sell > 2.71 - riga 3815"
                        action = "sell"
                        

                    ######################################################################################################## con trend discendente
                    ######################################################################################################## 2 righe del compa GIA' CON TOLLERANZA
                    
                    
                    elif (        
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma39 < -0.25)
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "sessione 2 SELL (21-60 min) con ma50 < and deviation_ma39 < -0.25 - riga 3826"
                        action = "sell"
                  
                    
                    elif (    
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.27)
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "sessione 2 SELL (21-60 min) con ma50 < and deviation_sell < -0.27 - riga 3833"
                        action = "sell"
                        
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_60_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.37
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "sessione 2 SELL (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - riga 3843"
                        action = "sell"
                   
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_60_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "sessione 2 SELL (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - riga 3852"
                        action = "sell"
                      
                    ################################################################################################################# con > PERDITA TOLLERATA !
                    
                    # ATTENZIONE ! AUMENTA LA PERDITA TOLLERATA  ! PERCHE' ma200 sale e perche' ma200 > ma300
                    
                    
                    # divido in 2 parti la correzione del maestro !
                    
                    elif (
                        
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma39 < -0.28)
                        and ma200_last > ma200_60_min_ago
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                    
                    ):
                        sell = "SELL 2 compa (21-60 min) con ma50 < and deviation_ma39 < -0.28   con > PERDITA TOLLERATA ! - riga 3869"
                        action = "sell"
                        
                 
                    elif (  
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.29)
                        and ma200_last > ma200_60_min_ago
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                     
                    ):
                        sell = "SELL 2 compa (21-60 min) con ma50 < and deviation_sell < -0.29 con > PERDITA TOLLERATA ! - riga 3879"
                        action = "sell"
                     
                   
                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma200_60_min_ago
                        and ma200_last > ma300_last
                        and ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.40
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "sessione 2 SELL (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.40 con > PERDITA TOLLERATA ! - riga 3891"
                        action = "sell"
                 
                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma200_60_min_ago
                        and ma200_last > ma300_last
                        and ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "sessione 2 SELL (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO con > PERDITA TOLLERATA ! - riga 3902"
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
                        sell = "sessione 2 SELL eventuale guadagno durante il crollo (21-60 min) con ma50 < incrocio 3 - 18 and deviation_sell > 0.23 - riga 3918"
                        action = "sell"
                        
                        
                        

                ############################################################################################################################## SESSIONE 2 ( da 60 a 90 min )

                # VENDITA - da 60 a 90 min - da 3600 a 5400 secondi in poi
                
                elif (
                    seconds_since_last_trade > 3600 and seconds_since_last_trade <= 5400
                ):
                    
                    ############################################################################################ RIGHE DEL COMPA DA RADDOPPIARE PER AUMENTO TOLLERANZA
                    
                    if (    
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma39 < -0.18)
                    ):
                        sell = "sessione 2 SELL da 60 a 90 min con ma50 > and deviation_ma39 < -0.18 - riga 3937"
                        action = "sell"
                        
                        
                    
                   
                    elif (      
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.18 and ma3_last < ma50_last)
                    ):
                        sell = "sessione 2 SELL da 60 a 90 min con ma50 > and (deviation_sell < -0.18 and ma3_last < ma50_last)  - riga 3946"
                        action = "sell"
                        
                        
                        
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma39 < -0.22)
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "sessione 2 SELL da 60 a 90 min con ma50 > and deviation_ma39 <-0.22 - riga 3957"
                        action = "sell"
                        
                        
                    
                   
                    elif (      
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.21 and ma3_last < ma50_last)
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "sessione 2 SELL da 60 a 90 min con ma50 > and (deviation_sell < -0.21 and ma3_last < ma50_last)  - riga 3967"
                        action = "sell"
                        
                        
                        
                        
                        #####################################################################################################################
                        
                      
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma50_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and 5-50 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - riga 3984"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma4_prev > ma25_prev and ma4_last < ma25_last)
                        and deviation_sell > 0.57 and deviation_sell < 0.80
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 >60 min con ma50> and incrocio 4-25 and deviation_sell 0.57-0.80 FINTA ALLA RONALDO -riga 3996"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.81 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 da 60 a 90 min con ma50 > and incrocio 3-18 and deviation_sell 0.81 - 1.49 RABONA ALLA RONALDO - riga 4008"
                        action = "sell"

                        # ma ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 da 60 a 90 min con ma50 > incrocio 3-13 and deviation_sell 1.50 - 2.70 DOPPIO PASSO ALLA RONALDO - riga 4022"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 da 60 a 90 min con ma50 > incrocio 3-11 and deviation_sell > 2.71 STIAMO TRA GLI ANGELI, compa ! - riga 4034"
                        action = "sell"
                        
                    
                    ######################################################################################## con trend discendente
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.17
                        and deviation_sell < 0.01
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 < con deviation_ma39 <-0.17 and deviation_sell < 0.01 (no ma3<ma33) (NO INCROCIO!) - riga 4046"
                        action = "sell"
                        
                        # and ma3_last < ma33_last
                        # and deviation_sell < 0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # cuscino dell' angelo custode
                        
                    
                    

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.13
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < -0.13 - riga 4064"
                        action = "sell"
                        
                        
                        
                        
                    ################################################################################## aumenta perdita tollerata
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 < con deviation_ma39 < -0.18 AUMENTA PERDITA TOLLERATA - riga 4080"
                        action = "sell"
                        
                        # and ma3_last < ma33_last
                        # and deviation_sell < 0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # cuscino dell' angelo custode
                        
                    
                    

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.13
                        
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < -0.13 AUMENTA PERDITA TOLLERATA - riga 4101"
                        action = "sell"
                        
                        
                        
                        
                        
                       
                
                ################################################################################################################################# SESSIONE 2 ( > 90 min )

                # VENDITA 2 - da 90 minuti in poi = da 5400 secondi in poi

                elif seconds_since_last_trade > 5400:
                    
                    
                    ####################################################################################################   RIGHE DEL COMPA DA RADDOPPIARE PER AUMENTO TOLLERANZA
                    
                    
                    if (  
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma39 < -0.20)
                    ):    
                        sell = "SELL 2 dopo 90 min con ma50 > and deviation_ma39 <-0.18 (no ma3<ma39) - riga 4123"
                        action = "sell"
                        
                   
                    elif (      
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.19 and ma3_last < ma50_last)
                    ):
                        sell = "sessione 2 SELL dopo 90 min con ma50 > and (deviation_sell < 0.10 and ma3_last < ma50_last) - riga 4130"
                        action = "sell"
                        
                        
                        
                    elif (  
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma39 < -0.23)
                        and ma200_last > ma200_60_min_ago
                    ):    
                        sell = "sessione 2 SELL 2 dopo 90 min con ma50 > and deviation_ma39 < -0.23 - riga 4139"
                        action = "sell"
                        
                   
                    elif (      
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.22 and ma3_last < ma50_last)
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "sessione 2 SELL dopo 90 min con ma50 > and (deviation_sell < -0.22 and ma3_last < ma50_last) - riga 4147"
                        action = "sell"
                        
                        
                        ###############################################################################################################################
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma42_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and 5-42 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - riga 4163"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "sessione 2 SELL 2 >90 min con ma50 > con 4-20 and deviation_sell 0.57-0.90 DRIBBLING ALLA RONALDO - riga 4178"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "sessione 2 SELL 2 dopo 90 min con ma50 > incrocio 3-15 and deviation_sell 0.91 - 1.49 - riga 4190"
                        action = "sell"

                        # ma 3-48 mi evita la ricompra e la rivendita con perdita !
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "sessione 2 SELL 2 dopo 90 min con ma50 > incrocio 3-13 and deviation_sell 1.50 - 2.70 - riga 4204"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "sessione 2 SELL 2 dopo 90 min con ma50 > incrocio 3-11 (!) and deviation_sell > 2.71 - riga 4215"
                        action = "sell"
                        
                        

                    ######################################################################################## con trend discendente
                    
                    
                    
                    elif (  
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma39 < -0.22)
                    
                    ):
                        sell = "sessione 2 SELL 2 dopo 90 min con ma50 < con deviation_ma39 <-0.16 - riga 4228"
                        action = "sell"
                        
                        # quello che vedi e' stato discusso con il maestro
                        
                        
                 
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.18 and ma3_last < ma39_last)
                     
                    ):
                        sell = "sessione 2 SELL 2 dopo 90 min con ma50 < and (deviation_sell < -0.18 and ma3_last < ma39_last) - riga 4241"
                        action = "sell"
                        
                        # quello che vedi e' stato discusso con il maestro
                        
                        
                        
                    
                    
                    
                    
                    ########################################################################################## AUMENTA PERDITA TOLLERATA e divido in 2 il compa
                    
                    
                    elif (  
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma39 < -0.24)
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 compa dopo 90 min con ma50 < con deviation_ma39 <-0.24 con > PERDITA TOLLERATA - riga 4261"
                        action = "sell"
                        
                        
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.24 and ma3_last < ma39_last)
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 compa dopo 90 min con ma50 < (deviation_sell < -0.24 and ma3_last < ma39_last) con > PERDITA TOLLERATA - riga 4273"
                        action = "sell"
                        
                        
                    
                    #####################################################################################################################

                    ################################################################################################ sessione 2  (vendita con questi 7 altri modi)
                    ################################################################################################
                    ################################################################################################
                    
                    # MA ATTENZIONE al conflitto durante il crollo - SELL SOVRAPPOSTO AL BUY

                    # NO 3<78 !
                    # NO deviation 78 !
                    # QUALCHE VOLTA ma3-ma39 NON HANNO INCROCIATO allora per la vendita con il DRIBBLING e il DOPPIO PASSO ALLA RONALDO ho risolto con 3<39
                    # il CUSCINO DELL' ANGELO CUSTODE e di SANT' ANTONIO mi proteggono ! (vendita con medie lunghe)
                    

                    # 1 - ro cano VENDE CON UN SALVAGENTE
            
                    if deviation_ma39 < -0.25 and deviation < -0.36 and ma50_last > ma50_2_min_ago:

                        sell = "SELL 2 SALVAGENTE 3-39 con ma50 < riga 4296"
                        action = "sell"

                        # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!
                        
                        

                    # 2 - ro cano VENDE DURANTE UN CROLLO IMPROVVISO !
            
                    elif deviation < -0.62:
                        sell = "SELL 2 CROLLO IMPROVVISO - riga 4306"
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

                        sell = "SELL 2 DOLCE ATTESA con ma13 > and deviation < -0.40 - riga 4325"
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

                        sell = "SELL 2 DOLCE ATTESA con ma13 < and deviation < -0.36 - riga 4345"
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

                        sell = "SELL 2 TEMPO e se ma8 < ma50 and deviation_sell < -0.49 - riga 4364"
                        action = "sell"
                        
                        # ma13 troppo lenta !
                        # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                        
                
                
                    # 6 - RIBASSO IMPROVVISO - attenzione! ma2 arriva tardi !
            
                    elif (
                        ma78_last > ma78_2_min_ago
                        and deviation_ribasso_improvviso < -0.63
                       
                    ):
       
                        sell = "SELL 2 RIBASSO IMPROVVISO - riga 4380"
                        action = "sell"
            
            
            
                    # 7 - RIBASSO IMPROVVISO attenzione! ma2 arriva tardi !
            
                    elif (
                        ma78_last < ma78_2_min_ago
                        and deviation_ribasso_improvviso < -0.63
                        
                
                    ):
       
                        sell = "SELL 2 RIBASSO IMPROVVISO - riga 4394"
                        action = "sell"
                
                

            ##################################################################################################################################
            ###################################################################################################
            ###################################################################################################
            ################################################################################################### SESSIONE 3
            
            elif self.session == 3:
                
                ################################################################################################### sessione 3 ( 0-3 min ) ok
                
                if seconds_since_last_trade > 0 and seconds_since_last_trade <= 180:

                    # con ma50 >

                    if (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma18_last
                        and deviation_sell < -0.33
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 3 (0-3 min) con ma50 > and 3<18 and deviation_sell < -0.33 - riga 4419"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma25_prev and ma5_last < ma25_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 3 (0-3 min) con ma50 > and incrocio 5-25 and deviation_sell 0.25 - 0.60 MARADONA - riga 4433"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.61 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (0-3 min) con ma50 > and incrocio 3-15 and deviation_sell 0.61 - 0.90 RONALDO - riga 4446"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell 0.91 - 1.20 - riga 4458"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell > 1.21 (che sarebbe come IL DRIBBLING ALLA RONALDO !)- riga 4470"
                        action = "sell"
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (0-3 min) con ma50 < and incrocio 3-28- riga 4483"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 - riga 4496"
                        action = "sell"
                        

                    # ---------------------------------------------------------------------------------------------------------------------- crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - riga 4508"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 4521"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                        and deviation_sell > 0.60
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - riga 4533"
                        action = "sell"
                        

                ############################################################################################################## sessione 3-4-x ( 3-5 min  cambiata con 3-7 min )

                # VENDITA - da 3 a 7 minuti = da 180 a 420 secondi

                elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 420:

                    if (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma18_last
                        and deviation_sell < -0.335
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 > and 3 < 18 and deviation_sell < -0.335 - riga 4549"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - riga 4562"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 > and 5<20 (no incrocio 3-9) and deviation_sell 0.57 - 0.90 - DRIBBLING ALLA RONALDO - riga 4575"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 4588"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - riga 4599"
                        action = "sell"
                        

                    ###########################################################################     trend in ribasso
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 < and incrocio 3-28 - riga 4612"
                        action = "sell"
                        
                        # deviation_sell_ma78 = ma3_last / ma78_last
                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.23 - riga 4626"
                        action = "sell"
                        
                        
                        
                    # aumenta perdita tollerata se ma50< MA ma200> et ma200>ma300
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.31
                        
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                        
                      
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 < and incrocio 3-28 con > PERDITA TOLLERATA - riga 4644"
                        action = "sell"
                        
                        # deviation_sell_ma78 = ma3_last / ma78_last
                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.25
                        
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.23 con > PERDITA TOLLERATA - riga 4662"
                        action = "sell"
                        
                       

                    # ---------------------------------------------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 4675"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 4686"
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
                        sell = "SELL 3 (5-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - riga 4705"
                        action = "sell"
                        
                    # deviation_sell = ma3_last/last_trade_price
                    # guardare la stella (guardare da una stella!)
                    # QUESTO E' IL RISCHIO PIU' GRANDE CHE PRENDO ! ( ma con ma50 > ma50 2 min ago DOPO 5 min (+2))
                    # e qua mi ha fottuto con la vendita -1.46 al min 6 del 19 dic 2021 - cambiato crollo improvviso ! e cambiato condizioni e anche fascia da 5-12
                    
                    

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.25
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - riga 4721"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - riga 4735"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                  
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 >  5<20 and deviation_sell 0.57 - 0.90 - DRIBBLING ALLA RONALDO - riga 4749"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma20_prev and ma5_last < ma20_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 > and incrocio 5-20 and deviation_sell 0.91 - 1.20 - riga 4764"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - riga 4778"
                        action = "sell"
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 < and incrocio 3-28 - riga 4791"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 < and incrocio 3-100 (cuscino di sant' antonio) - riga 4804"
                        action = "sell"
                        
                        

                    # ------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 guadagno con crollo (5-12 min) con ma50 < and incrocio 3-23 - riga 4817"
                        action = "sell"
                        
                        

                    # ------------------------------------------------------------------------------------------------------------ PARACADUTE crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.48
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.48 - riga 4830"
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
                        and deviation_sell < -0.35
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and incrocio 3-72 and deviation sell -0.35 e vaffanculo ! - riga 4851"
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
                        sell = "SELL 3 (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.36 - riga 4767"
                        action = "sell"
                    
                        # viva sant' antonio !
                        # IMPORTANTE !   
                        # vai compaaaaaaaaaa
                        # poco guadagno ma piu' alta
                        # molto guadagno ma piu' bassa
                    
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.54
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.54 - FINTA ALLA MARADONA - riga 4886"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma20_last
                        and deviation_sell > 0.55 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and 5-20 and deviation_sell 0.55-0.90 - DOPPIO PASSO ALLA RONALDO - riga 4901"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and incrocio 3-20 and deviation_sell 0.91 - 1.20 - riga 4916"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and incrocio 3-30 and deviation_sell > 1.21 - riga 4929"
                        action = "sell"
                        
                    
                    
                    ##########################################################################################
                    # NON TOCCARE ! CUSCINO DI SANT' ANTONIO !
                    # L' INCROCIO 5-100 MI SALVA ! MA 5<100 VENDE DURANTE IL RIBASSO !
                    
                    
                    ##################################################################### con trend discendente

                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.165
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 < and deviation_ma39 < -0.165 - riga 4947"
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
                        sell = "SELL 3 (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - riga 4966"
                        action = "sell"
                        
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50< !
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - riga 4981"
                        action = "sell"
                        
                        # viva sant' antonio !
                        # incrocio 5-100 no 5<100 altrimenti vende durante il crollo !
                        
                        
                        
                        
                    # aumento della perdita tollerata
                    
                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.185
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 < and deviation_ma39 < -0.185 con > PERDITA TOLLERATA - riga 5000"
                        action = "sell"
                        
                        # and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        # and deviation_sell < -0.25
                        # ATTENZIONE QUESTA aveva FATTO -0.61% !
                        # QUINDI ho abbassato da 0.17 a 0.16 a 0.15
                        # HO NOTATO CHE ANCHE INCROCIO 5-100 SAREBBE ARRIVATO TARDI
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10
                        
                        

                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.47
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.47 con > PERDITA TOLLERATA - riga 5021"
                        action = "sell"
                        
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50< !
                        
                        
                        

                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO con > PERDITA TOLLERATA - riga 5038"
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
                        sell = "SELL 3 PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 5054"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                        

                    # ----------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3 - 18 and deviation_sell > 0.23 - riga 5070"
                        action = "sell"
                        
                        

                ############################################################################################################################# sessione 3-4-x ( 21-60 min )

                # VENDITA - da 21 a 60 minuti = da 1261 a 3600 secondi

                elif (
                    seconds_since_last_trade > 1261 and seconds_since_last_trade <= 3600
                ):
                    
                    
                    ################################################################################################ RIGHE DEL COMPA DA RADDOPPIARE
                    
                    if (    
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma25 < -0.25)
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and deviation_ma25 < -0.25 - riga 5088"
                        action = "sell"
                        
                    
                    
                    elif (      
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.25 and ma3_last < ma50_last)
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL (21-60 min) con ma50 > and (deviation_sell < -0.25 and ma3_last < ma50_last) - riga 5096"
                        action = "sell"
                        
                        
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma25 < -0.28)
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and deviation_ma25 < -0.28 - riga 5107"
                        action = "sell"
                        
                    
                    
                    elif (      
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.27 and ma3_last < ma50_last)
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and (deviation_sell < -0.27 and ma3_last < ma50_last) - riga 5116"
                        action = "sell"
                        
                       
                        ##################################################################################################################
                        
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.26
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.26 - riga 5129"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma30_prev and ma5_last < ma30_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                   
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 5-30 and deviation_sell 0.25 - 0.56 FINTA DI MARADONA - riga 5144"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma5_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and 5 < 20 and deviation_sell 0.57 - 0.90 ELASTICO ALLA RONALDO - riga 5159"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 3-30 and deviation_sell 0.91 - 1.20 - riga 5175"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.21 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 3-30 and deviation_sell 1.21 -2.70 - riga 5189"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 3-11 and deviation_sell > 2.71 - riga 5201"
                        action = "sell"
                    
                    
                    ##################################################################### con trend discendente
                   
                    
                    
                    elif (     
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma39 < -0.23)
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and deviation_ma39 < -0.23 - riga 5212"
                        action = "sell"
                        
                  
                    elif (    
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.28)
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and deviation_sell < -0.28 - riga 5219"
                        action = "sell"
                        
                     

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.37
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - riga 5230"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - riga 5242"
                        action = "sell"
                        
                        # viva sant' antonio !
                        # NON INCROCERANNO MAI DURANTE IL CROLLO !
                        # non toccare ! INCROCIO 3-100 CUSCINO DI SANT' ANTONIO !
                        
                    
                        
                    ##############################################################################################################  aumento perdita tollerata se....  
                    
                    # divido il maestro in 2
                    
                    
                    elif (  
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma39 < -0.25)
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                       
                    ):
                        sell = "SELL 3 compa (21-60 min) con ma50 < and deviation_ma39 < -0.25 con PERDITA TOLLERATA > - riga 5262"
                        action = "sell"
                        
                        
                     
                    
                    elif ( 
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.24)
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                    ):
                        sell = "SELL 3 compa (21-60 min) con ma50 < and deviation_sell < 0.24  con PERDITA TOLLERATA > - riga 5273"
                        action = "sell"
                        
                        
                        
                    
                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.39
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.39 con > perdita tollerata - riga 5287"
                        action = "sell"
                        
                        

                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - con > perdita tollerata - riga 5301"
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
                        sell = "SELL 3 eventuale guadagno durante il crollo (21-60 min) con ma50 < incrocio 3 - 18 and deviation_sell > 0.23 - riga 5318"
                        action = "sell"
                        
                        

                ################################################################################################################## sessione 3-4-x ( da 60 a 90 min )

                # VENDITA - da 60 a 90 min - da 3600 a 5400 secondi in poi
                
                elif (
                    seconds_since_last_trade > 3600 and seconds_since_last_trade <= 5400
                ):
                  
                ################################################################################## RIGHE DEL COMPA DA RADDOPPIARE PER AUMENTARE LA TOLLERANZA
                    
                    
                    if (    
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma25 < -0.21)
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 > and deviation_ma25 < -0.19 - riga 5337"
                        action = "sell"
                        
                        
                        
                    
                    
                    elif (    
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.20 and ma3_last < ma50_last)
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 > and (deviation_sell < -0.19 and ma3_last < ma50_last) - riga 5347"
                        action = "sell"
                        
                        
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma25 < -0.21)
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 > and deviation_ma25 < -0.19 - riga 5357"
                        action = "sell"
                        
                        
                        
                    
                    elif (    
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.20 and ma3_last < ma50_last)
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 > and (deviation_sell < -0.19 and ma3_last < ma50_last) - riga 5367"
                        action = "sell"
                        
                        
                        ############################################################################################################
                     
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma50_prev and ma5_last < ma50_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 5-50 and deviation_sell 0.25 - 0.56 FINTA DI MARADONA - riga 5380"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 >60 min con ma50> and 4-20 and deviation_sell 0.57-0.90 DRIBBLING ALLA RONALDO - riga 5394"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 da 60 a 90 min con ma50 > and incrocio 3-30 and deviation_sell 0.91 - 1.49 - riga 5407"
                        action = "sell"

                        # ma ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 da 60 a 90 min con ma50 > incrocio 3-20 and deviation_sell 1.50 - 2.70 - riga 5422"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 da 60 a 90 min con ma50 > incrocio 3-11 and deviation_sell > 2.71 - riga 5435"
                        action = "sell"
                        
                        
                        

                    ################################################################################################################## con trend discendente
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 < con deviation_ma39 <-0.18 and deviation_sell < 0.10 (no ma3<ma33) (NO INCROCIO!) - riga 5449"
                        action = "sell"
                        
                        # and ma3_last < ma33_last
                        # and deviation_sell < 0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # cuscino dell' angelo custode
                        
                        
                    

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < 0.10
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < 0.10 - riga 5467"
                        action = "sell"
                        
                        
                        
                        
                    # maggiore perdita tollerata
                    
                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.20
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 < con deviation_ma39 <-0.20 and deviation_sell < 0.10 con > perdita tollerata - riga 5483"
                        action = "sell"
                        
                        # and ma3_last < ma33_last
                        # and deviation_sell < 0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # cuscino dell' angelo custode
                        
                        
                    

                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < 0.13
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < 0.13 con > perdita tollerata - riga 5503"
                        action = "sell"
                 

                ##################################################################################################################### sessione 3-4-x ( > 90 min )

                # VENDITA - da 90 minuti in poi = da 5400 secondi in poi

                elif seconds_since_last_trade > 5400:
                    
                    ############################################################################################ RIGHE DEL COMPA DA RADDOPPIARE PER AUMENTARE TOLLERANZA
                    
                    
                    if (    
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma25 < -0.21)
                    ):
                        sell = "SELL 3 dopo 90 min con ma50> and deviation_ma25 <-0.18 (no ma3<ma39) - riga 5519"
                        action = "sell"
                        
                    
                  
                    
                    elif (     
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.20 and ma3_last < ma50_last)
                    ):
                        sell = "SELL 3 dopo 90 min con ma50> and (deviation_sell < 0.10 and ma3_last < ma50_last)- riga 5528"
                        action = "sell"
                        
                        
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma25 < -0.23)
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 dopo 90 min con ma50> and deviation_ma25 < -0.23 - riga 5538"
                        action = "sell"
                        
                    
                  
                    
                    elif (     
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.23 and ma3_last < ma50_last)
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 dopo 90 min con ma50> and (deviation_sell < -0.23 and ma3_last < ma50_last) - riga 5548"
                        action = "sell"
                        
                       
                        
                    ########################################################################################################################################### 
                  
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma50_last
                        and deviation_sell > 0.25 and deviation_sell < 0.59
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and 5-50 and deviation_sell 0.25-0.59 - FINTA ALLA MARADONA - riga 5562"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma25_last
                        and deviation_sell > 0.60 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 >90 min con ma50 > con 4 < 25 and deviation_sell 0.60 - 0.90 DRIBBLING ALLA RONALDO - riga 5575"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 dopo 90 min con ma50 > incrocio 3-30 (!) and deviation_sell 0.91 - 1.49 - riga 5587"
                        action = "sell"

                        # ma 3-48 mi evita la ricompra e la rivendita con perdita !
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 dopo 90 min con ma50 > incrocio 3-30 (!) and deviation_sell 1.50 - 2.70 - riga 5602"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 dopo 90 min con ma50 > incrocio 3-11 (!) and deviation_sell > 2.71 - riga 5615"
                        action = "sell"
                        
                 
                    ######################################################################################## con trend discendente
                    
                    
                    
                    elif (      
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma39 < -0.21)
                    ):
                        sell = "SELL 3 dopo 90 min con ma50 < con deviation_ma39 <-0.18 - riga 5626"
                        action = "sell"
                        
                        
                        
                        
                    
                     
                    elif (    
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.20 and ma3_last < ma39_last)
                    ):
                        sell = "SELL 3 dopo 90 min con ma50 < and (deviation_sell < 0.10 and ma3_last < ma39_last) - riga 5637"
                        action = "sell"
                        
                    
                    ################################################################################################ sessione 3 (vendita con questi 7 altri modi)
                    ################################################################################################
                    ################################################################################################
                    # MA ATTENZIONE al conflitto durante il crollo - SELL SOVRAPPOSTO AL BUY

                    # NO 3<78 !
                    # NO deviation 78 !
                    # QUALCHE VOLTA ma3-ma39 NON HANNO INCROCIATO allora per la vendita con il DRIBBLING e il DOPPIO PASSO ALLA RONALDO ho risolto con 3<39
                    # il CUSCINO DELL' ANGELO CUSTODE e di SANT' ANTONIO mi proteggono ! (vendita con medie lunghe)
                    
                    

                    # 1 - ro cano VENDE CON UN SALVAGENTE
            
                    if deviation_ma39 < -0.24 and deviation < -0.36 and ma50_last > ma50_2_min_ago:

                        sell = "SELL 3 SALVAGENTE 3-39 con ma50 < riga 5657"
                        action = "sell"

                        # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!
                        
                        
                        

                    # 2 - ro cano VENDE DURANTE UN CROLLO IMPROVVISO !
            
                    elif deviation < -0.58:
                    
                        sell = "SELL 3 CROLLO IMPROVVISO < -0.58 - riga 5669"
                        action = "sell"
                
                        # con -0.59 il 6 feb 2022 ha fatto -0.85
                        # con -0.62 il 4 feb 2022 ha fatto -0.89%
                        # deviation = ma4_last / last_trade_price

                        # FORSE E' L' UNICA DEVIATION CHE MI POTRA' SALVARE DA UN CROLLO IMPROVVISO COME QUELLO DEL 3 NOVEMBRE 2021
                        
                        
                        
                        

                    # 3 - ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma13 >
            
                    elif (
                        seconds_since_last_trade > max_hold_time_in_seconds
                        and ma2_last < last_trade_price
                        and deviation < -0.42
                        and ma13_last > ma13_2_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 DOLCE ATTESA con ma13 > and deviation < -0.40 - riga 5692"
                        action = "sell"

                        # il fattore tempo - la dolce attesa - solo con trend ribassista
                        # deviation = ma2_last / last_trade_price
                        # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                        # max_hold_time_in_seconds = 300 = 5 min (con 6 min perdita di 0.90 %)
                        
                        
                        
                
                    # 4 - ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma13 <
            
                    elif (
                        seconds_since_last_trade > max_hold_time_in_seconds
                        and ma13_last < ma13_2_min_ago
                        and deviation < -0.355
                        and ma2_last < last_trade_price
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 DOLCE ATTESA 270 sec con ma13 < and deviation < -0.345 - riga 5713"
                        action = "sell"

                        # il fattore tempo - la dolce attesa - solo con trend ribassista
                        # deviation = ma2_last / last_trade_price
                        # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                        # max_hold_time_in_seconds = 270 sec = 4 min e 1/2  (con 6 min perdita di 0.60 %)
                        # 4 feb 2022 con <-0.26 ha fatto -0.88% (dopo +4.29%)
                        # 7 feb 2022 con <-0.345 e 270 sec ha fatto -0.38% - aumenta a 0.355 ! -eventualmente ci pensa la condizione CROLLO IMPROVVISO CHE FUNZIONA !
                        
            
            
            
                    # 5 - ro cano VENDE " DOPO x MINUTI " and...
            
                    elif (
                        seconds_since_last_trade > max_hold_time_in_seconds
                        and ma8_last < ma50_last
                        and deviation_sell < -0.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 TEMPO e se ma8 < ma50 and deviation_sell < -0.49 - riga 5735"
                        action = "sell"
                        
                        # ma13 troppo lenta !
                        # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                        
                        
                
                
                
                    # 6 - RIBASSO IMPROVVISO
            
                    elif (
                        ma78_last > ma78_2_min_ago
                        and deviation_ribasso_improvviso < -0.63
                        and ma2_last < ma2_2_min_ago
                    ):
       
                        sell = "SELL 3 RIBASSO IMPROVVISO - riga 5753"
                        action = "sell"
            
            
            
            
            
                    # 7 - RIBASSO IMPROVVISO
            
                    elif (
                        ma78_last < ma78_2_min_ago
                        and deviation_ribasso_improvviso < -0.63
                        and ma2_last < ma2_2_min_ago
                    ):
       
                        sell = "SELL 3 RIBASSO IMPROVVISO - riga 5768"
                        action = "sell"
            
            
            
            elif self.session > 3:

                ################################################################################################### sessione 4-5-x ( 0-3 min ) ok
                
                if seconds_since_last_trade > 0 and seconds_since_last_trade <= 180:

                    # con ma50 >

                    if (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma18_last
                        and deviation_sell < -0.33
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (0-3 min) con ma50 > and 3<18 and deviation_sell < -0.33 - riga 5787"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma25_prev and ma5_last < ma25_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 4-5-x SELL (0-3 min) con ma50 > and incrocio 5-25 and deviation_sell 0.25 - 0.56 MARADONA - riga 5801"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma4_prev > ma20_prev and ma4_last < ma20_last)
                        and deviation_sell > 0.57 and deviation_sell < 0.79
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (0-3 min) con ma50 > and incrocio 4-20 and deviation_sell 0.57 - 0.79 RONALDO - riga 5814"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 0.80 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell 0.80 - 1.20 - riga 5826"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell > 1.21 (che sarebbe come IL DRIBBLING ALLA RONALDO !)- riga 5838"
                        action = "sell"
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (0-3 min) con ma50 < and incrocio 3-28- riga 5851"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 - riga 5864"
                        action = "sell"

                    # ---------------------------------------------------------------------------------------------------------------------- crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - riga 5875"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 5888"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                        and deviation_sell > 0.60
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - riga 5900"
                        action = "sell"
                        

                ######################################################################################################## sessione 3-4-x ( 3-5 min  cambiata con 3-7 min )

                # VENDITA - da 3 a 7 minuti = da 180 a 420 secondi

                elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 420:

                    if (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.32
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 4-5-x (3-5 min) con ma50 > and 3<16 and deviation_sell < -0.32 - riga 5917"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - riga 5930"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 4-5-x (3-5 min) con ma50 > and 4<20 and deviation_sell 0.57 - 0.90 - DRIBBLING ALLA RONALDO - riga 5944"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.40
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (3-5 min) con ma50 > and incrocio 3-20 and deviation_sell 0.91 - 1.40 - riga 5957"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 1.41
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (3-5 min) con ma50 > and incrocio 3-15 and deviation_sell > 1.41 - riga 5968"
                        action = "sell"
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 4-5-x (3-5 min) con ma50 < and incrocio 3-28 - riga 5981"
                        action = "sell"
                        
                        # deviation_sell_ma78 = ma3_last / ma78_last
                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.23 - riga 5995"
                        action = "sell"
                        

                    # ---------------------------------------------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 6007"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 6018"
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
                        sell = "SELL 4-5-x (5-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - riga 6037"
                        action = "sell"
                        
                    # deviation_sell = ma3_last/last_trade_price
                    # guardare la stella (guardare da una stella!)
                    # QUESTO E' IL RISCHIO PIU' GRANDE CHE PRENDO ! ( ma con ma50 > ma50 2 min ago DOPO 5 min (+2))
                    # e qua mi ha fottuto con la vendita -1.46 al min 6 del 19 dic 2021 - cambiato crollo improvviso ! e cambiato condizioni e anche fascia da 5-12
                    
                    

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.25
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (5-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - riga 6053"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - riga 6067"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                  
                    ):
                        sell = "SELL 4-5-x (5-12 min) con ma50 > and 4-20 and deviation_sell 0.57 - 0.90 - DRIBBLING ALLA RONALDO - riga 6081"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 4-5-x (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 6096"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - riga 6110"
                        action = "sell"
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (5-12 min) con ma50 < and incrocio 3-28 - riga 6123"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (5-12 min) con ma50 < and incrocio 3-100 (cuscino di sant' antonio) - riga 6136"
                        action = "sell"
                        
                        

                    # ------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x guadagno con crollo (5-12 min) con ma50 < and incrocio 3-23 - riga 6149"
                        action = "sell"
                        
                        

                    # ------------------------------------------------------------------------------------------------------------ PARACADUTE crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 6162"
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
                        and deviation_sell < -0.35
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and incrocio 3-72 and deviation sell -0.65 e vaffanculo ! - riga 6183"
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
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.36 - riga 6199"
                        action = "sell"
                    
                        # viva sant' antonio !
                        # IMPORTANTE !   
                        # vai compaaaaaaaaaa
                        # poco guadagno ma piu' alta
                        # molto guadagno ma piu' bassa
                    
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - riga 6218"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and 4-20 and deviation_sell 0.57 - 0.90 - DRIBBLING ALLA RONALDO - riga 6233"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - riga 6248"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and incrocio 3-30 and deviation_sell > 1.21 - riga 6261"
                        action = "sell"
                        
                    
                    
                    ##########################################################################################
                    # NON TOCCARE ! CUSCINO DI SANT' ANTONIO !
                    # L' INCROCIO 5-100 MI SALVA ! MA 5<100 VENDE DURANTE IL RIBASSO !
                    ##################################################################### con trend discendente

                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.17
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 < and deviation_ma39 < -0.17 - riga 6277"
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
                        sell = "SELL 4-5-x (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - riga 6296"
                        action = "sell"
                        
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50< !
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - riga 6311"
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
                        sell = "SELL 4-5-x PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - riga 6328"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                  
                    # ----------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3 - 18 and deviation_sell > 0.23 - riga 6344"
                        action = "sell"
                        
                        

                #################################################################################################################### sessione 3-4-x ( 21-60 min )
                

                # VENDITA - da 21 a 60 minuti = da 1261 a 3600 secondi

                elif (
                    seconds_since_last_trade > 1261 and seconds_since_last_trade <= 3600
                ):
                    
                    ###################################################################################### RIGHE DEL COMPA DA RADDOPPIATE PER AUMENTARE TOLLERANZA
                    
                    if (    
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma25 < -0.27)
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and deviation_ma25 < -0.27 - riga 6363"
                        action = "sell"
                        
                     
                    
                    elif ( 
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.24 and ma3_last < ma50_last)
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and (deviation_sell < -0.24 and ma3_last < ma50_last) - riga 6371"
                        action = "sell"
                        
                     
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma25 < -0.29)
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and deviation_ma25 < -0.29 - riga 6381"
                        action = "sell"
                        
                        
                        
                        
                     
                    
                    elif (        
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.26 and ma3_last < ma50_last)
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and (deviation_sell < -0.26 and ma3_last < ma50_last) - riga 6393"
                        action = "sell"
                        
                        
                        
                        #############################################################################################################
                        
                     

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.26
                        and ma2_last < ma2_2_min_ago
                  
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.26 - riga 6409"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma25_prev and ma5_last < ma25_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                   
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and incrocio 5-25 and deviation_sell 0.25 - 0.56 FINTA DI MARADONA - riga 6424"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma25_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and 3-25 (no incrocio 3-15) and deviation_sell 0.57 - 0.90 FINTA ALLA RONALDO - riga 6439"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                      

                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma20_last
                        and deviation_sell > 0.91 and deviation_sell < 1.40
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and 3-20 and deviation_sell 0.91 - 1.40 - riga 6453"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma25_last
                        and deviation_sell > 1.41 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and 3-25 and deviation_sell 1.41 -2.70 - riga 6467"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and incrocio 3-13 and deviation_sell > 2.71 - riga 6479"
                        action = "sell"
                    
                    
                    ############################################################################################################## con trend discendente
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma39 < -0.24)
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and deviation_ma39 < -0.225 - riga 6491"
                        action = "sell"
                        
                 
                    elif (    
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.23 and ma3_last < ma39_last)
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and deviation_sell < 0.225 - riga 6500"
                        action = "sell"
              
            
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_60_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.37
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - riga 6512"
                        action = "sell"
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_60_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - riga 6524"
                        action = "sell"
                        
                        # viva sant' antonio !
                        # NON INCROCERANNO MAI DURANTE IL CROLLO !
                        # non toccare ! INCROCIO 3-100 CUSCINO DI SANT' ANTONIO !
                        
                        
                        
                        
                    ##################################################################################################### aumenta la tolleranza    
                        
                    elif (
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma39 < -0.26)
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and deviation_ma39 < -0.26 - riga 6491"
                        action = "sell"
                        
                 
                    elif (    
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.25 and ma3_last < ma39_last)
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and deviation_sell < 0.25 - riga 6500"
                        action = "sell"
              
            
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma200_60_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.39
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.39 - riga 6512"
                        action = "sell"
                        
                  
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma200_60_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.29
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and INCROCIO 5-100 (no 5<100) and deviation_sell < -0.29  CUSCINO DI SANT' ANTONIO - riga 6524"
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
                        sell = "SELL 4-5-x eventuale guadagno durante il crollo (21-60 min) con ma50 < incrocio 3 - 18 and deviation_sell > 0.23 - riga 6540"
                        action = "sell"
                        
                        
                    

                ################################################################################################################# sessione 3-4-x ( da 60 a 90 min )

                # VENDITA - da 60 a 90 min - da 3600 a 5400 secondi in poi
                
                elif (
                    seconds_since_last_trade > 3600 and seconds_since_last_trade <= 5400
                ):
                    
                    
                    ########################################################################################### RIGHE DEL COMPA DA RADDOPPIARE PER AUMENTARE LA TOLLERANZA
                    
                    
                    
                    if ( 
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma25 < -0.22)
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > and deviation_ma25 < -0.19 - riga 6562"
                        action = "sell"
                        
                        
                    
                    elif (    
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.21 and ma3_last < ma50_last)
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > and (deviation_sell < -0.19 and ma3_last < ma50_last) - riga 6570"
                        action = "sell"
                        
                        
                        
                        
                    elif ( 
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma25 < -0.25)
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > and deviation_ma25 < -0.25 - riga 6580"
                        action = "sell"
                        
                        
                    
                    elif (    
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.24 and ma3_last < ma50_last)
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > and (deviation_sell < -0.24 and ma3_last < ma50_last) - riga 6589"
                        action = "sell"
                        
                        
                        #########################################################################################################################
                        
                      
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma25_prev and ma5_last < ma25_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and incrocio 5-25 and deviation_sell 0.25 - 0.56 FINTA DI MARADONA - riga 6604"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x >60 min con ma50> and 4-20 and deviation_sell 0.57-0.90 DRIBBLING ALLA RONALDO - riga 6618"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > and incrocio 3-30 and deviation_sell 0.91 - 1.49 - riga 6631"
                        action = "sell"

                        # ma ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > incrocio 3-25 and deviation_sell 1.50 - 2.70 - riga 6646"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > incrocio 3-13 and deviation_sell > 2.71 - riga 6659"
                        action = "sell"
                        
                    
                    ######################################################################################## con trend discendente
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 < con deviation_ma39 <-0.18 and deviation_sell < 0.10 (no ma3<ma33) (NO INCROCIO!) - riga 6671"
                        action = "sell"
                        
                        # and ma3_last < ma33_last
                        # and deviation_sell < 0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # cuscino dell' angelo custode
                        
                        
                    

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < 0.01
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < 0.01 - riga 6689"
                        action = "sell"
                        
                        

                ##################################################################################################################### sessione 3-4-x ( > 90 min )

                # VENDITA - da 90 minuti in poi = da 5400 secondi in poi

                elif seconds_since_last_trade > 5400:
                    
                    # ########################################################################################### RIGHE DEL COMPA DA RADDOPPIARE PER AUMENTARE TOLLERANZA
                    
                    if (    
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma25 < -0.22)
                    ):
                        sell = "SELL 4-5-x dopo 90 min con ma50> and deviation_ma25 <-0.18 (no ma3<ma39) - riga 6705"
                        action = "sell"
                        
                      
                    
                    elif (     
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.21 and ma3_last < ma50_last)
                    ):
                        sell = "SELL 4-5-x dopo 90 min con ma50> and (deviation_sell < 0.10 and ma3_last < ma50_last)- riga 6713"
                        action = "sell"
                        
                      
                        
                    elif (    
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma25 < -0.25)
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x dopo 90 min con ma50> and deviation_ma25 < -0.25 TOLLERANTE - riga 6722"
                        action = "sell"
                        
                        
                   
                    
                    elif (     
                        ma50_last > ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.24 and ma3_last < ma50_last)
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x dopo 90 min con ma50> and (deviation_sell < -0.24 and ma3_last < ma50_last) TOLLERANTE - riga 6732"
                        action = "sell"
                        
                        
                        #############################################################################################################################
                       
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - riga 6746"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x >90 min con ma50 > con 4 < 20 and deviation_sell 0.35 - 0.90 FINTA ALLA RONALDO - riga 6759"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x dopo 90 min con ma50 > incrocio 3-30 (!) and deviation_sell 0.91 - 1.49 - riga 6771"
                        action = "sell"

                        # ma 3-48 mi evita la ricompra e la rivendita con perdita !
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x dopo 90 min con ma50 > incrocio 3-25 (!) and deviation_sell 1.50 - 2.70 - riga 6786"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x dopo 90 min con ma50 > incrocio 3-13 (!) and deviation_sell > 2.71 - riga 6799"
                        action = "sell"
                        
                        

                    ######################################################################################## con trend discendente
                    
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_ma39 < -0.215)
                    ):
                        sell = "SELL 4-5-x dopo 90 min con ma50 < con deviation_ma39 <-0.215 - riga 6811"
                        action = "sell"
                        
                        
                        
                    
                     
                    elif (    
                        ma50_last < ma50_2_min_ago and (ma2_last < ma2_2_min_ago and deviation_sell < -0.21 and ma3_last < ma39_last)
                    ):
                        sell = "SELL 4-5-x dopo 90 min con ma50 < and (deviation_sell < 0.10 and ma3_last < ma39_last) - riga 6821"
                        action = "sell"
                        
                    
                    ################################################################################################ sessione 3-4-x (vendita con questi 7 altri modi)
                    ################################################################################################
                    ################################################################################################
                    # MA ATTENZIONE al conflitto durante il crollo - SELL SOVRAPPOSTO AL BUY

                    # NO 3<78 !
                    # NO deviation 78 !
                    # QUALCHE VOLTA ma3-ma39 NON HANNO INCROCIATO allora per la vendita con il DRIBBLING e il DOPPIO PASSO ALLA RONALDO ho risolto con 3<39
                    # il CUSCINO DELL' ANGELO CUSTODE e di SANT' ANTONIO mi proteggono ! (vendita con medie lunghe)
                    
                    

                # 1 - ro cano VENDE CON UN SALVAGENTE
            
                if deviation_ma39 < -0.24 and deviation < -0.36 and ma50_last > ma50_2_min_ago:

                    sell = "SELL 4-5-x SALVAGENTE 3-39 con ma50 < riga 6841"
                    action = "sell"

                    # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!
                        
                        
                        

                # 2 - ro cano VENDE DURANTE UN CROLLO IMPROVVISO !
            
                elif deviation < -0.58:
                    
                    sell = "SELL 4-5-x CROLLO IMPROVVISO < -0.58 - riga 6853"
                    action = "sell"
                
                    # con -0.59 il 6 feb 2022 ha fatto -0.85
                    # con -0.62 il 4 feb 2022 ha fatto -0.89%
                    # deviation = ma4_last / last_trade_price

                    # FORSE E' L' UNICA DEVIATION CHE MI POTRA' SALVARE DA UN CROLLO IMPROVVISO COME QUELLO DEL 3 NOVEMBRE 2021
                        
                        
                        
                        

                # 3 - ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma13 >
            
                elif (
                    seconds_since_last_trade > max_hold_time_in_seconds
                    and ma2_last < last_trade_price
                    and deviation < -0.42
                    and ma13_last > ma13_2_min_ago
                    and ma2_last < ma2_2_min_ago
                ):

                    sell = "SELL 4-5-x DOLCE ATTESA con ma13 > and deviation < -0.40 - riga 6876"
                    action = "sell"

                    # il fattore tempo - la dolce attesa - solo con trend ribassista
                    # deviation = ma2_last / last_trade_price
                    # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                    # max_hold_time_in_seconds = 300 = 5 min (con 6 min perdita di 0.90 %)
                        
                        
                        
                
                # 4 - ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma13 <
            
                elif (
                    seconds_since_last_trade > max_hold_time_in_seconds
                    and ma13_last < ma13_2_min_ago
                    and deviation < -0.355
                    and ma2_last < last_trade_price
                    and ma2_last < ma2_2_min_ago
                ):

                    sell = "SELL 4-5-x DOLCE ATTESA 270 sec con ma13 < and deviation < -0.345 - riga 6897"
                    action = "sell"

                    # il fattore tempo - la dolce attesa - solo con trend ribassista
                    # deviation = ma2_last / last_trade_price
                    # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                    # max_hold_time_in_seconds = 270 sec = 4 min e 1/2  (con 6 min perdita di 0.60 %)
                    # 4 feb 2022 con <-0.26 ha fatto -0.88% (dopo +4.29%)
                    # 7 feb 2022 con <-0.345 e 270 sec ha fatto -0.38% - aumenta a 0.355 ! - eventualmente ci pensa la condizione CROLLO IMPROVVISO CHE FUNZIONA !
                        
            
            
            
                # 5 - ro cano VENDE " DOPO x MINUTI " and...
            
                elif (
                    seconds_since_last_trade > max_hold_time_in_seconds
                    and ma8_last < ma50_last
                    and deviation_sell < -0.49
                    and ma2_last < ma2_2_min_ago
                ):

                    sell = "SELL 4-5-x TEMPO e se ma8 < ma50 and deviation_sell < -0.49 - riga 6919"
                    action = "sell"
                        
                    # ma13 troppo lenta !
                    # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                        
                        
                
                
                
                # 6 - RIBASSO IMPROVVISO
            
                elif (
                    ma78_last > ma78_2_min_ago
                    and deviation_ribasso_improvviso < -0.63
                    
                ):
                    sell = "SELL 4-5-x RIBASSO IMPROVVISO - riga 6936"
                    action = "sell"
                    
                    
            
                # 7 - RIBASSO IMPROVVISO
            
                elif (
                    ma78_last < ma78_2_min_ago
                    and deviation_ribasso_improvviso < -0.63
                    
                ):
                    sell = "SELL 4-5-x RIBASSO IMPROVVISO - riga 6948"
                    action = "sell"
                    
                    
                
                
                # POCHI MALEDETTI E SUBITO - dedicated to comparo meo
                
                elif (
                    ma3_last < ma9_last
                    and ma200_last > ma200_60_min_ago
                    and deviation > 0.70
                    and deviation_pochi_maledetti > 0.70
                    and ma2_last > ma100_last
                    and ma2_last < ma2_2_min_ago
                ):
                    sell = "SELL 3-4-x POCHI MALEDETTI E SUBITO quando ma200 > e con deviation > 0.70 - dedicated to comparo meo - riga 7029"
                    action = "sell"
                    
                    # and ma2_last > ma100_last (altrimenti vende durante il crollo con la ma3-ma9)
                
                
                elif (
                    ma3_last < ma9_last 
                    and ma200_last < ma200_60_min_ago
                    and deviation > 0.70
                    and deviation_pochi_maledetti > 0.70
                    and ma2_last > ma100_last
                    and ma2_last < ma2_2_min_ago
                ):
                    sell = "SELL 3-4-x POCHI MALEDETTI E SUBITO quando ma200 < e con deviation > 0.70 - dedicated to comparo meo - riga 7039"
                    action = "sell"
                    
                    # and ma2_last > ma100_last (altrimenti vende durante il crollo con la ma3-ma9)
                    
                    
                
                
                

        self.algo_helper.info("action {}".format(action))
        self.algo_helper.info("percentage {}".format(percentage))

        if action == "sell":
            self.algo_helper.info("action sell {}".format(sell))
            self.session += 1

        elif action == "buy":
            self.algo_helper.info("action buy {}".format(buy))

        return action, percentage

        ############### FINE ALGORITH ###################
        
        
