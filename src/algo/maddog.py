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
        ma22_last, ma22_prev = self.algo_helper.ma_last_prev(22)
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
        ma125_last, ma125_prev = self.algo_helper.ma_last_prev(125)
        ma150_last, ma150_prev = self.algo_helper.ma_last_prev(150)
        ma200_last, ma200_prev = self.algo_helper.ma_last_prev(200)
        ma300_last, ma300_prev = self.algo_helper.ma_last_prev(300)

        
        # moving average (2-3-4-5-7-8-20-43-100) di x minuti prima
        
        ma2_2_min_ago = self.algo_helper.ma_minutes_ago(2, 2)
        ma2_3_min_ago = self.algo_helper.ma_minutes_ago(2, 3)
        ma2_4_min_ago = self.algo_helper.ma_minutes_ago(2, 4)
        ma3_2_min_ago = self.algo_helper.ma_minutes_ago(3, 2)
        ma3_3_min_ago = self.algo_helper.ma_minutes_ago(3, 3)
        ma3_9_min_ago = self.algo_helper.ma_minutes_ago(3, 9)
        ma3_20_min_ago = self.algo_helper.ma_minutes_ago(3, 20)
        ma4_2_min_ago = self.algo_helper.ma_minutes_ago(4, 2)
        
        ma4_4_min_ago = self.algo_helper.ma_minutes_ago(4, 4)
        ma5_2_min_ago = self.algo_helper.ma_minutes_ago(5, 2)
        ma6_2_min_ago = self.algo_helper.ma_minutes_ago(6, 2)
        ma8_2_min_ago = self.algo_helper.ma_minutes_ago(8, 2)
        ma8_4_min_ago = self.algo_helper.ma_minutes_ago(8, 4)
        ma10_2_min_ago = self.algo_helper.ma_minutes_ago(10, 2)
        ma13_2_min_ago = self.algo_helper.ma_minutes_ago(13, 2)
        ma13_10_min_ago = self.algo_helper.ma_minutes_ago(13, 10)
        ma20_2_min_ago = self.algo_helper.ma_minutes_ago(20, 2)
        ma20_22_min_ago = self.algo_helper.ma_minutes_ago(20, 22)
        ma20_60_min_ago = self.algo_helper.ma_minutes_ago(20, 60)
        ma25_2_min_ago = self.algo_helper.ma_minutes_ago(25, 2)
        ma30_10_min_ago = self.algo_helper.ma_minutes_ago(30, 10)
        ma30_20_min_ago = self.algo_helper.ma_minutes_ago(30, 20)
        ma30_30_min_ago = self.algo_helper.ma_minutes_ago(30, 30)
        ma30_40_min_ago = self.algo_helper.ma_minutes_ago(30, 40)
      
        ma33_5_min_ago = self.algo_helper.ma_minutes_ago(33, 5)
        ma36_2_min_ago = self.algo_helper.ma_minutes_ago(36, 2)
        ma39_2_min_ago = self.algo_helper.ma_minutes_ago(39, 2)
        ma39_3_min_ago = self.algo_helper.ma_minutes_ago(39, 3)
        ma39_15_min_ago = self.algo_helper.ma_minutes_ago(39, 15)
        
        ma50_2_min_ago = self.algo_helper.ma_minutes_ago(50, 2)
        ma69_2_min_ago = self.algo_helper.ma_minutes_ago(69, 2)
        ma69_15_min_ago = self.algo_helper.ma_minutes_ago(69, 15)
        
        ma69_45_min_ago = self.algo_helper.ma_minutes_ago(69, 45)
        ma72_2_min_ago = self.algo_helper.ma_minutes_ago(72, 2)
        ma78_2_min_ago = self.algo_helper.ma_minutes_ago(78, 2)
        ma78_4_min_ago = self.algo_helper.ma_minutes_ago(78, 4)
        ma78_5_min_ago = self.algo_helper.ma_minutes_ago(78, 5)
        ma78_7_min_ago = self.algo_helper.ma_minutes_ago(78, 7)
        ma78_30_min_ago = self.algo_helper.ma_minutes_ago(78, 30)
        ma100_2_min_ago = self.algo_helper.ma_minutes_ago(100, 2)
        ma100_10_min_ago = self.algo_helper.ma_minutes_ago(100, 10)
        ma100_60_min_ago = self.algo_helper.ma_minutes_ago(100, 60)
        ma100_120_min_ago = self.algo_helper.ma_minutes_ago(100, 120)
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

        ###################################################################################################################### TEMPO
        
        # SELL dolce atttesa
        # BUY con il passare del tempo
        
        # SELL 1 FIAT
        # SELL 1 AUDI
        # SELL 1 MASERATI
        # SELL 1 FERRARI
        
        # VENDE DOPO x SECONDI - ro cano torna a casa - (ma c'e' anche un "e se")
        # esempio : 4 minuti * 60 = 240 + 30 secondi = 270 secondi
        
        #####################################################################################################################
        
        # vedi SELL dolce attesa
        
        max_hold_time_in_seconds = 255
        
       
        # vedi BUY 2 con il passare del tempo
        
        max_hold_time_in_seconds_nuova = 7200
        
        
        ###########################################################################################################################
        
        # vedi SELL 1 FIAT - 20 minuti = 1200 secondi
        
        max_hold_time_in_seconds_fiat = 1200
        
       
        # vedi SELL 1 AUDI - 20 minuti = 1200 secondi
        
        max_hold_time_in_seconds_audi = 1200
        
      
        # vedi SELL 1 MASERATI - 20 minuti = 1200 secondi
        
        max_hold_time_in_seconds_maserati = 1200
        
        
        # vedi SELL 1 FERRARI - 20 minuti = 1200 secondi
        
        max_hold_time_in_seconds_ferrari = 1200
        
        
        ###############################################################################################################################
        
        # vedi DELTA BUY 2 DAL SELL 1  > 2 minuti = 120 secondi
        
        max_hold_time_in_seconds_delta_buy2_sell1 = 120
        
        ###############################################################################################################################
       
        #########################################################################################################################################################
        #########################################################################################################################################################

        #                                                         T U T T E    L E   D E V I A T I O N  !

        ##############################################################################################################

        # formula DEVIATION_1_gabbia
        
        deviation_1_gabbia = (ma8_last / ma50_last - 1) * 100 if ma50_last else 0
        self.algo_helper.info("deviation_1_gabbia: {}".format(deviation_1_gabbia))

        

        # formula deviation
        
        deviation = (ma4_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.info("deviation: {}".format(deviation))
        
        
        
        # formula DEVIATION_ma5_sopra_ma28 - FORMULA AUREA !
        
        deviation_ma5_sopra_ma28 = (ma5_last / ma28_last - 1) * 100 if ma28_last else 0
        self.algo_helper.info("deviation_ma5_sopra_ma28: {}".format(deviation_ma5_sopra_ma28))
        
        
        #################################################################################################################
        
        
        # formula delta_1
        
        delta_1 = (ma200_last / ma100_last - 1) * 100 if ma100_last else 0
        self.algo_helper.info("delta_1: {}".format(delta_1))
        
        
        # formula delta_2
        
        delta_2 = (ma200_60_min_ago / ma100_60_min_ago - 1) * 100 if ma100_60_min_ago else 0
        self.algo_helper.info("delta_2: {}".format(delta_2))
        
        
        # formula rapporto_delta_1_delta_2
        
        rapporto_delta_1_delta_2 = (delta_1 / delta_2 - 1) * 100 if delta_2 else 0
        self.algo_helper.info("rapporto_delta_1_delta_2: {}".format(rapporto_delta_1_delta_2))
        
        
        
        # formula delta_1_69_39
        
        delta_1_69_39 = (ma69_last / ma39_last - 1) * 100 if ma39_last else 0
        self.algo_helper.info("delta_1_69_39: {}".format(delta_1_69_39))
        
        
        # formula delta_2_69_39
        
        delta_2_69_39 = (ma69_15_min_ago / ma39_15_min_ago - 1) * 100 if ma39_15_min_ago else 0
        self.algo_helper.info("delta_2_69_39: {}".format(delta_2_69_39))
        
        
        # formula rapporto_delta_1_delta_2_69_39
        
        rapporto_delta_1_delta_2_69_39 = (delta_1_69_39 / delta_2_69_39 - 1) * 100 if delta_2_69_39 else 0
        self.algo_helper.info("rapporto_delta_1_delta_2_69_39: {}".format(rapporto_delta_1_delta_2_69_39))
        
        
        
     
        # formula deviation_ma3
        
        deviation_ma3 = (ma3_last / ma3_20_min_ago - 1) * 100 if ma3_20_min_ago else 0
        self.algo_helper.info("deviation_ma3: {}".format(deviation_ma3))
     
        
        # formula deviation trend ma200
        
        deviation_trend_ma200 = (ma200_last / ma200_120_min_ago - 1) * 100 if ma200_120_min_ago else 0
        self.algo_helper.info("deviation_trend_ma200: {}".format(deviation_trend_ma200))
        
        
        
        # formula deviation trend ma100 - se dopo 60 min cresce > 1%  NON FA PARTIRE LA VENDITA POCHI MALEDETTI E SUBITO !
        # diversamente succederebbero punti sovrapposti !
        
        deviation_trend_ma100 = (ma100_last / ma100_60_min_ago - 1) * 100 if ma100_60_min_ago else 0
        self.algo_helper.info("deviation_trend_ma100: {}".format(deviation_trend_ma100))
        
        
        
        # deviation pochi maledetti
        
        deviation_pochi_maledetti = (ma13_last / ma13_10_min_ago - 1) * 100 if ma13_10_min_ago else 0
        self.algo_helper.info("deviation_pochi_maledetti: {}".format(deviation_pochi_maledetti))
        
      
        ######################################################################
        
        # ESPERIMENTO !
        
        # formula DEVIATION_ma200_sotto_ma300 per comprare
        
        deviation_ma200_sotto_ma300 = (ma200_last / ma300_last - 1) * 100 if ma300_last else 0
        self.algo_helper.info("deviation_ma200_sotto_ma300: {}".format(deviation_ma200_sotto_ma300))
        
        
        # formula DEVIATION_ma5_sotto_ma200 per comprare FINO a una certa distanza da ma200
        
        deviation_ma5_sotto_ma200 = (ma5_last / ma200_last - 1) * 100 if ma200_last else 0
        self.algo_helper.info("deviation_ma5_sotto_ma200: {}".format(deviation_ma5_sotto_ma200))
        
        
        # formula DEVIATION_ma4_sopra_ma100 - BUY 4 (parliamo del BUY 4 !) DEVE STARE a una certa distanza da ma100
        
        deviation_ma4_sopra_ma100 = (ma4_last / ma100_last - 1) * 100 if ma100_last else 0
        self.algo_helper.info("deviation_ma4_sopra_ma100: {}".format(deviation_ma4_sopra_ma100)) 
        
       
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
        
        
        # formula DEVIATION_ma50_sotto_ma300
        
        deviation_ma50_sotto_ma300 = (ma50_last / ma300_last - 1) * 100 if ma300_last else 0
        self.algo_helper.info("deviation_ma50_sotto_ma300: {}".format(deviation_ma50_sotto_ma300))
     
        
        # formula DEVIATION_ma100_sopra_ma300
        
        deviation_ma100_sopra_ma300 = (ma100_last / ma300_last - 1) * 100 if ma300_last else 0
        self.algo_helper.info("deviation_ma100_sopra_ma300: {}".format(deviation_ma100_sopra_ma300))
       
        
        # formula DEVIATION_ma100_sopra_ma200
        
        deviation_ma100_sopra_ma200 = (ma100_last / ma200_last - 1) * 100 if ma200_last else 0
        self.algo_helper.info("deviation_ma100_sopra_ma200: {}".format(deviation_ma100_sopra_ma200))
     
        
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
        
        # formula deviation_ma20_laterale
        
        deviation_ma20_laterale = (ma20_last / ma20_60_min_ago - 1) * 100 if ma20_60_min_ago else 0
        self.algo_helper.info("deviation_ma20_laterale: {}".format(deviation_ma20_laterale))
        
       
        # formula DEVIATION_RIBASSO_IMPROVVISO
        
        deviation_ribasso_improvviso = (price / ma30_last - 1) * 100 if ma30_last else 0
        self.algo_helper.info("deviation_ribasso_improvviso: {}".format(deviation_ribasso_improvviso))
      
        
        # formula DEVIATION_crollo_24_aprile - che va nella vendita speciale
        
        deviation_crollo_24_aprile = (ma2_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.info("deviation_crollo_24_aprile: {}".format(deviation_crollo_24_aprile))
        
       
        ################################################################################################################## deviation per comprare

        # formula DEVIATION_buy1 per la compra 1
        
        deviation_buy1 = (ma13_last / ma39_last - 1) * 100 if ma39_last else 0
        self.algo_helper.info("deviation_buy1: {}".format(deviation_buy1))
        
        

        # formula DEVIATION_buy2 per la compra 2
        
        deviation_buy2 = (ma8_last / ma50_last - 1) * 100 if ma50_last else 0
        self.algo_helper.info("deviation_buy2: {}".format(deviation_buy2))
        
        
        # formula DELTA_buy2 per la compra 2
        
        delta_buy2_dal_sell1 = (ma3_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.info("delta_buy2_dal_sell1: {}".format(delta_buy2_dal_sell1))
    
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
        
        deviation_ma5_sopra_ma25 = (ma5_last / ma25_last - 1) * 100 if ma25_last else 0
        self.algo_helper.info("deviation_ma5_sopra_ma25: {}".format(deviation_ma5_sopra_ma25))
        
        
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
            #   B U Y
            ###########################################################################################################################################
            
            percentage = self.buy_percentage
            
            # NON TOCCARE  ! DI DEFAULT E' IL 2%
            
            ########################################################################################################
            
            # in futuro
            # MACD e RSI
            # TOGLIERE TUTTI GLI INCROCI AL BUY ! se 13 > 100 NON INCROCERA' MAI ! INCROCIO 13-100 DIVENTA 13>100 !
            # analisi dei dati !
           
        
        
            ######################################################################################################## COMPRA sessione 1
            
            # BUY 1 con "percentage" 20
            
            if self.session == 1:
                
            
                # ------------------------------------------------------------ BUY 1 DURANTE IL RIALZO con INCROCIO CLASSICO 69-100
                
                if (    
                    ma20_last > ma200_last
                    and ma69_last > ma100_last
                    and ma3_last > ma8_last
                    and deviation_bellissima > 0.14
                    and ma6_last > ma39_last
                ):    
              
                    buy = "BUY 1 con 20>200 and 69 > 100 and deviation_bellissima > 0.14 r 667"
                    action = "buy"
                    percentage = 20
                    
                    
                 
                # ------------------------------------------------------------ BUY 1 quando incomincia il ribasso MA 300>
                  
                elif (     
                    ma300_last > ma300_120_min_ago
                    and ma8_last > ma100_last
                    and deviation_ma5_sopra_ma28 > 0.16
                    
                    and ma200_last < ma200_60_min_ago
                    and ma100_last < ma100_60_min_ago
                    
                    and deviation_bellissima > 0.14
                    and ma2_last > ma2_2_min_ago
                ):     
                  
                    buy = "BUY 1 quando incomincia il ribasso MA 300> - r 687"
                    action = "buy"
                    percentage = 20
                    
                
                
                # ------------------------------------------------------------ BUY 1 se ma200> and ma300> and 8>50   
                
                elif (    
                    ma20_last > ma200_last
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    and ma8_last > ma50_last
                ):  
                
                    buy = "BUY 1 con 20>200 and 69 > 100 and deviation_bellissima > 0.14 r 702"
                    action = "buy"
                    percentage = 20
                    
                    
                
                
                # ------------------------------------------------------------ BUY 1 tempo ESTATE che considera il passare del TEMPO  CON ma30 > 
                
                elif (     
                    ma69_last > ma69_45_min_ago
                    and ma100_last > ma200_last
                    
                    and ma30_last > ma30_40_min_ago
                
                    and deviation_ma5_sopra_ma28 > 0.15
                    and deviation_bellissima > 0.06
                    and ma20_last > ma20_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma2_last > ma20_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 tempo ESTATE che considera il passare del tempo con deviation_bellissima > 0.06 - r 724"
                    action = "buy"
                    percentage = 20
                    
                    
              
                # ------------------------------------------------------------ BUY 1 tempo PRIMAVERA che considera il passare del tempo con ma30 < 
                
                elif (     
                    ma69_last > ma69_45_min_ago
                    and ma100_last > ma200_last
                    
                    and ma30_last < ma30_40_min_ago
                 
                    and deviation_ma5_sopra_ma28 > 0.175
                    and deviation_bellissima > 0.06
                    and ma2_last > ma20_last
                    and ma5_last >= ma5_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    
                ):    
                    buy = "BUY 1 tempo PRIMAVERA che considera il passare del tempo con deviation_bellissima > 0.06 and deviation_ma5_sopra_ma28 > 0.18 - r 745"
                    action = "buy"
                    percentage = 20
                    
                    
                
                    
                    
                # ------------------------------------------------------------ BUY 1 tempo AUTUNNO che considera il passare del tempo con ma30 > MA 100 > 200
                
                elif (     
                    ma69_last > ma69_45_min_ago
                    and ma100_last < ma200_last
                    
                    and ma30_last > ma30_40_min_ago
                    
                    and ma20_last > ma200_last
                    and deviation_ma5_sopra_ma28 > 0.15
                    and deviation_bellissima > 0.06
                    and ma20_last > ma20_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma2_last > ma20_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 tempo AUTUNNO che considera il passare del tempo con deviation_bellissima > 0.06 - r 769"
                    action = "buy"
                    percentage = 20
                    
              
                
                
                # ------------------------------------------------------------ BUY 1 tempo INVERNO che considera il passare del tempo con ma30 < MA 100 > 200
                
                elif (     
                    ma69_last > ma69_45_min_ago
                    and ma100_last < ma200_last
                    
                    and ma30_last < ma30_40_min_ago
                    
                    and ma20_last > ma200_last
                    and deviation_ma5_sopra_ma28 > 0.175
                    and deviation_bellissima > 0.06
                    and ma2_last > ma20_last
                    and ma5_last >= ma5_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    
                ):    
                    buy = "BUY 1 tempo INVERNO che considera il passare del tempo con deviation_bellissima > 0.06 and deviation_ma5_sopra_ma28 > 0.18 - r 792"
                    action = "buy"
                    percentage = 20
                    
                    
                
                    
                    
                # ------------------------------------- BUY 1 con ma200 < 300< MA ma100> 100 60 min ago e doppio delta < STA RISALENDO !
            
                elif (       
                    ma200_last < ma200_20_min_ago
                    and ma11_last > ma150_last
                    and ma2_last > ma2_2_min_ago
                    
                    and rapporto_delta_1_delta_2 < 1
                    
                    and ma100_last > ma100_60_min_ago
                    and ma200_last < ma200_60_min_ago
                    and ma300_last < ma300_60_min_ago
                ):    
        
                    buy = "BUY 1 11-150 con ma200< 300< MA ma100> 100 60 min ago e doppio delta < STA RISALENDO !- riga 814"
                    action = "buy"
                    percentage = 10
                    
                    # 11-150 perche' doppio delta sta risalendo !
                    
                    
                    
                    
                # BUY 1 copiata e modificata da RCCR che e' arrivata una ndecchia prima del passare del tempo.
                
                elif (
                    
                    ma8_last > ma150_last
                    and deviation_ma100_sopra_ma200 > -0.30
                    
                    and ma100_last > ma100_2_min_ago
                    and ma300_last < ma300_60_min_ago
                    and ma200_last < ma200_60_min_ago
                    
                    and ma72_last >= ma72_2_min_ago
                    and ma13_last > ma69_last
                    and deviation_bellissima > 0.17
                    and deviation_ma13_sopra_ma25 > 0.07
                    and deviation_ma3_sopra_ma7 > 0.05
                    and ma3_last > ma3_3_min_ago
                    and ma2_last > ma2_2_min_ago
              
                ):
                    buy = "BUY 1 8-150 copiata e modificata da RCCR che e' arrivata una ndecchia prima del passare del tempo - riga 843"
                    action = "buy"
                    percentage = 20
                    
                    # importante : ma100 sta sotto la ma200 non le e' troppo lontana cioe' NON ci troviamo in una situazione drammatica! (anche se ma200< e ma300<)
                    
                
                
                
                
                
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
                    buy = "BUY 1 con ma20_last > ma200_last e con 11 > 69 e ma69> 2 min ago (!) r 869"
                    action = "buy"
                    percentage = 20
                    
           
        
        
                
                # BUY 1 con 11-69 SE ma200 SALE DA 2 ORE !
                    
                elif (
                    ma200_last > ma200_120_min_ago
                    and ma20_last > ma200_last
                    and ma11_last > ma69_last
                    and deviation_ma5_sopra_ma28 > 0.15
                    and deviation_bellissima > 0.17
                    and price > price_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma3_3_min_ago
                    and ma4_last > ma4_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                    and deviation_ma13_sopra_ma25 > 0.07
                 
                ):
                    buy = "BUY 1 con 11-69 SE ma200 SALE DA 2 ORE ! - r 893"
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
                    buy = "BUY 1 con 13>50 and DEVIATION BUY 1 ALTA e ma78> - r 910"
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
                    buy = "BUY 1 con ma78< and 39>78 and DEVIATION BUY 1 BASSA r 928"
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

                    buy = "BUY 1 se ma78< - BUY 1 con incrocio 39>78 - r 948"
                    action = "buy"
                    percentage = 10
                    
                    
                
                
                ############################################################################### compra durante un rialzo improvviso ! PER ADESSO SOLO SUL BUY 1
                ############################################################################### con ma30 che ha 30 min di andamento laterale
                
                elif (
                    ma200_last > ma200_20_min_ago
                    and deviation_rialzo_improvviso_sopra > 0.48
                    and deviation_rialzo_improvviso_1 > 0.48
                    and deviation_rialzo_improvviso_2 > 0.19
                    and deviation_rialzo_improvviso_3 > 0.19
                    and deviation_range_1 < 0.20
                    and deviation_range_1 > -0.20
                    and deviation_range_2 < 0.20
                    and deviation_range_2 > -0.20
                    and deviation_range_x < 0.20
                    and deviation_range_x > -0.20
                ):
             
                    buy = "BUY 1 RIALZO IMPROVVISO con ma200 > - r 972"
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
              
                    buy = "BUY 1 variazione 1 RIALZO con 20-69 - r 997"
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

                    buy = "BUY 1 variazione 2 RIALZO con 20-100 - r 1020"
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

                    buy = "BUY 1 variazione 3 RIALZO con 20-200 - r 1043"
                    action = "buy"
                    percentage = 10
                    
                    # deviation_rialzo_improvviso_1 = price / ma30_last
                    # deviation_range_1 = ma30_last / ma30_10_min_ago
                
                
                
                
                
                # rialzo improvviso trend ribassista
                
                elif (    
                   
                    ma200_last < ma200_20_min_ago
                    
                    and deviation_rialzo_improvviso_1 > 1.10
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

                    buy = "BUY 1 RIALZO IMPROVVISO con 78 < ( da 1.20 a 1.1 !) sempre tentando di evitare falsi acquisti - r 1077"
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
                
                # BUY piccola CORREZIONE FIAT
                # BUY grande CORREZIONE AUDI
                # BUY RIBASSO MASERATI
                # BUY CROLLO FERRARI
                
                ########################################################################################################################### ATTENZIONE !
              
            
            
                
                # BUY 1 con ma200> piccola CORREZIONE FIAT che NON E' un forte ribasso e NON E' un crollo ! (compare stammi vicino!)
               
                elif (
                    ma2_last > ma2_2_min_ago
                    and ma200_last > ma200_120_min_ago
                    and deviation_buy_crollo_1 < -0.33
                    and deviation_buy_crollo_1 > -0.59
                    and ma3_last > ma28_last
                    and ma5_last > ma100_last
                ):    
                    
                    buy = "BUY 1A con ma200> piccola CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo - r 1118"
                    action = "buy"
                    percentage = 10
                    
                    # and ma3_last > ma100_last PERCHE' in questa circostanza 3-28 arriva tardi e mi proteggo
                    # dovrei fare 2-5 MA SAREBBE TROPPO RISCHIOSO perche' ma100 gia' e' in ribasso !
                    
                    
                    
                
                # BUY 1 con ma300 > piccola CORREZIONE FIAT che NON E' AUDI e non e' MASERATI e NON E' FERRARI ! (compare stammi vicino!)
              
                elif (

                    ma2_last > ma2_2_min_ago
                    and ma300_last > ma300_120_min_ago
                    and deviation_buy_crollo_1 < -0.33
                    and deviation_buy_crollo_1 > -0.59
                    and deviation_correzione > 0.012
                    and ma5_last > ma72_last
                ):

                    buy = "BUY 1 con ma300 > piccola CORREZIONE FIAT che NON E' una grande correzione AUDI e non e' MASERATI e NON E' FERRARI ! - r 1140"
                    action = "buy"
                    percentage = 10

                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    # ma5 non deve allontanarsi troppo dalla ma200 !
                    # compare prega per me !
                    # and ma3_last > ma69_last SOLTANTO con ma300> va bene anche senza ma sembra che STATISTICAMENTE produce una alta % di piccole perdite
                    
              
                
                # ATTENZIONE !
                # questa condizione che e' una condizione NECESSARIA FUNZIONALE E BUONA compra un po' troppo presto.
                # allora la divido in 3 !
                
                # la prima e' proprio uguale all' originaria ma aumento solo la ma da 5-39 a 5-100 
                # la seconda e' proprio uguale all' originaria ma aumento solo la ma da 5-39 a 5-50
                # la terza e' uguale proprio ma le dico che deve stare a una certa distanza da ma200 ( cioe' tenta di prendere solo il secondo tentativo )
                
                
              
                
                
                # BUY 1 piccola CORREZIONE FIAT = r 995 RCCR medie mobili lunghe TUTE IN RIALZO ! ma si verifica una correzione fiat !
                
                elif (
                    ma3_last > ma25_last
                    and ma100_last > ma100_120_min_ago
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    
                    and ma100_last > ma200_last
                    and ma200_last > ma300_last
                    
                    and deviation_buy_crollo_1 < -0.33
                    and deviation_buy_crollo_1 > -0.59
                    and ma2_last > ma2_2_min_ago
                    
                ):    
                    
                    buy = "BUY 1 piccola CORREZIONE FIAT = r 995 RCCR medie mobili lunghe TUTTE IN RIALZO ! ma si verifica una correzione fiat ! - r 1181"
                    action = "buy"
                    percentage = 10
                    
                    
                
               
                
                ################################################################################################### ecco le 2 CONDIZIONI PIU' PERICOLOSE !
                
                
                
                # BUY 1 DURANTE UNA CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo ! (MA ma3 > ma150 mi protegge un po')
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    and deviation_correzione > 0.03
                    and ma5_last > ma125_last
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 DURANTE UNA CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo ! ma5 > ma125 - riga 1203"
                    action = "buy"
                    percentage = 20
                    
                    
                
                
                    
                # BUY 1 piccola CORREZIONE FIAT = r 701 RCCR CHE FA PAURA ! ( ma la ma100 E' ANCORA VICINA alla ma300 !)
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    and deviation_correzione > 0.03
                    
                    and deviation_ma100_sopra_ma300 > -0.30
                    
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 DURANTE UNA CORREZIONE FIAT = r 701 RCCR CHE FA PAURA ! (ma la ma100 E' ANCORA VICINA alla ma300)! - riga 1223"
                    action = "buy"
                    percentage = 10
                    
                    # deviation_ma100_sopra_ma300 significa 100/300 ( ma100 ancora NON SI E' ALLONTANATA TROPPO DALLA ma300 )
                    
                    
                    
               
                ############################################################################################################################################## 
                
                
                
                # BUY 1 piccola CORREZIONE FIAT = r 701 RCCR ma con rischio ridotto !
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    and ma13_last > ma50_last
                    and ma20_last > ma20_22_min_ago
                    and ma2_last > ma2_2_min_ago
                ):    
                
                    buy = "BUY 1 piccola CORREZIONE FIAT = r 701 RCCR ma con rischio ridotto ! - r 1247"
                    action = "buy"
                    percentage = 20
                    
                   
                
                    
                # BUY 1 piccola CORREZIONE FIAT che non e' una grande correzione AUDI e non e' un forte ribasso MASERATI e non e' un crollo FERRARI !
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    and deviation_correzione > 0.02
                    and ma5_last > ma100_last
                    and deviation_ma20_laterale > -0.15
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 piccola CORREZIONE FIAT che non e' una grande correzione AUDI e non e' un forte ribasso MASERATI e non e' FERRARI ! - r 1265"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    # deviation_ma20_laterale > -0.15 cioe' ma20 ( una ma di breve termine) da ben 60 minuti non perde !
                    
                    # compare prega per me !
                    
                    
                    
                 
                # BUY 1 piccola CORREZIONE FIAT 5-50 che NON E' una grande correzione e non e' un grande ribasso e NON E' un crollo !
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and ma8_last > ma50_last
                    
                    and deviation_ma8_sotto_ma100 < -0.50
                    and deviation_buy_crollo_1 > -0.59
                ): 
            
                    buy = "BUY 1 piccola CORREZIONE FIAT 8-50 che NON E' una grande correzione e non e' un grande ribasso e NON E' un crollo ! - r 1288"
                    action = "buy"
                    percentage = 10
                    
                    
                    
                    
                
                # BUY 1 con ma200> piccola CORREZIONE FIAT che NON E' un forte ribasso e NON E' un crollo ! ALTRA RIGA RCCR che e' andata bene.
                
                elif (    
                    
                    ma200_last > ma200_20_min_ago
                    and ma3_last > ma28_last
                    and ma2_last > ma2_2_min_ago
                    
                    and ma100_last > ma200_last
                    and ma200_last > ma300_last
                    
                    and ma100_last > ma100_60_min_ago
                    and ma200_last > ma200_60_min_ago
                    and ma300_last > ma300_60_min_ago
               
                ):    
                    
                    buy = "BUY 1 con 200 > - riga 1313"
                    action = "buy"
                    percentage = 10
                    
                    
                 
                
                # BUY 1 piccola CORREZIONE FIAT 5-39 ma con ma5 piu' distante da ma200 che NON E' un grande ribasso e NON E' un crollo !
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and ma5_last > ma39_last
                    and deviation_ma5_sopra_ma28 > 0.10
                    and deviation_ma5_sotto_ma200 < -0.85
                    and rapporto_delta_1_delta_2_69_39 < 1
                    and deviation_ma8_sotto_ma100 < -0.50
                    and deviation_buy_crollo_1 > -0.59
                ): 
            
                    buy = "BUY 1 piccola CORREZIONE FIAT 5-39 ma con ma5 piu' distante da ma200 che NON E' un grande ribasso e NON E' un crollo ! - r 1332"
                    action = "buy"
                    percentage = 10
                    
                    # 5-28 se non c'e' un minimo di accelerazione che cazzo mi compri !

                    
                
                
                
                # BUY 1 con ma200< e ma300< piccola CORREZIONE FIAT che NON E' un forte ribasso e NON E' un crollo !
                
                elif (

                    ma2_last > ma2_2_min_ago
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    and ma11_last > ma69_last
                    
                    and deviation_buy_crollo_1 < -0.33
                    and deviation_buy_crollo_1 > -0.59
                    
                ):

                    buy = "BUY 1 con ma200< e ma300< piccola CORREZIONE FIAT che NON E'una grande correzione e NON E' un grande ribasso e NON E' un crollo - r 1356"
                    action = "buy"
                    percentage = 10
                    
                    
                    
                
                # BUY 1 con RIBASSO VELOCE MA la distanza tra ma100 e ma200 si sta riducendo - la ma100 sta risalendo ! USANDO UN DOPPIO DELTA ! 
                
                elif (
                    deviation_ma3 < -1.30
                    
                    
                    and rapporto_delta_1_delta_2 < 1
                    and ma3_last > ma9_last
                ):
                
                    buy = "BUY 1 con RIBASSO VELOCE mentre la distanza tra ma100 e ma200 si sta riducendo - la ma100 sta risalendo ! USANDO UN DOPPIO DELTA ! - r 1373"
                    action = "buy"
                    percentage = 10
                    
                    # and delta_1 < 0.25
                    # and delta_2 > 0.40
                    # STUDIARE MEGLIO DELTA 1 E DELTA 2
                    
                    # compare grazie. altre parole io non ho.
                    
                    
                  
                
                # BUY 1 grande CORREZIONE AUDI che NON E' una piccola CORREZIONE FIAT che NON E' un grande ribasso MASERATI e NON E' un crollo FERRARI !)
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and (ma20_prev < ma200_prev and ma20_last > ma200_last)
                    and deviation_correzione_1 > 0.03
                    
                    and deviation_buy_crollo_1 < -0.60
                    and deviation_buy_crollo_1 > -0.90
                  
                ):
                    buy = "BUY 1 grande CORREZIONE AUDI che NON E' FIAT e NON E' MASERATI e NON E' FERRARI ! + deviation_correzione> 0.02 - r 1397"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma5_last / ma30_last
                    
              
              
                # BUY 1 grande CORREZIONE AUDI che NON E' FIAT e NON E' MASERATI e NON E' FERRARI ! con deviation trend ma200 
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_trend_ma200 > -0.30
                    and deviation_correzione_1 > 0.01
                    
                    and deviation_buy_crollo_1 < -0.60
                    and deviation_buy_crollo_1 > -0.90
                  
                ):
                    buy = "BUY 1 grande CORREZIONE AUDI che NON E' un grande ribasso MASERATI e NON E' un crollo FERRARI ! con deviation trend ma200 - r 1417"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma5_last / ma30_last
                    # deviation_trend_ma200 = ma200_last / ma200_120_min_ago
                    # compare prega per me !
                    
                    
                    
                ######################################################################################################
                ###################################################################################################### attenzione qui applico il doppio delta !
                
                # quando la ma100 si avvicina risalendo verso la ma200 ok cosi'
                # quando la ma100 si allontana verso il basso dalla ma 200 metto 8-50 altrimenti e' una perdita continua !
                
            
                # BUY 1 FIAT che non funzionava MA CHE HA FUNZIONATO ! ( DOPPIO DELTA in risalita !)
                
                elif (    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    and ma3_last > ma9_last
                    
                    and ma200_last < ma300_last
                    and ma20_last < ma100_last
                    and ma100_last < ma100_10_min_ago
                    and deviation_ma200_sotto_ma300 < -0.27
                  
                    and rapporto_delta_1_delta_2 < 1
                    and rapporto_delta_1_delta_2_69_39 < 1
                    
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 FIAT che non funzionava MA CHE HA FUNZIONATO ! ( DOPPIO DELTA 200-100 e DOPPIO DELTA 69-39 in risalita !) - r 1452"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    # and deviation_correzione > 0.10
                    
                    # and delta_1 < 0.25 la puoi aggiungere in un secondo momento
                    # and delta_2 > 0.40 la puoi aggiungere in un secondo momento
                    
                    # compare prega per me !
                    
                    
                    
                    
                # BUY 1 OK FIAT ( DOPPIO DELTA in risalita !)
                
                elif (    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    and deviation_correzione > 0.10
                    
                    and ma200_last < ma300_last
                    and ma20_last < ma100_last
                    and ma100_last < ma100_10_min_ago
                    and deviation_ma200_sotto_ma300 < -0.27
                    
                    
                    
                    and rapporto_delta_1_delta_2 < 1
                    
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 FIAT OK ( DOPPIO DELTA in risalita !) - r 1486"
                    action = "buy"
                    percentage = 20
                    
                    # and delta_1 < 0.50
                    # and delta_2 > 0.69
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    
                    # compare prega per me !
                    
                    
                
                
                
                
                
                
                #  BUY 1 FIAT copia BIS della r701 del RCCR che non funzionava e che invece HA FUNZIONATO ! ( CON DOPPIO DELTA in RIBASSO !) 8-39
                
                elif (    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    and deviation_ma5_sopra_ma28 > 0.10
                    and ma8_last > ma39_last
                    and ma200_last < ma300_last
                    and ma20_last < ma100_last
                    and ma100_last < ma100_10_min_ago
                    and deviation_ma200_sotto_ma300 < -0.27
             
                    and rapporto_delta_1_delta_2 > 1
                    
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 FIAT copia BIS della r701 del RCCR che non funzionava e che invece HA FUNZIONATO ! ( CON DOPPIO DELTA in RIBASSO !) 8-39 - r 1520"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    
                    # and delta_1 > 0.40 la puoi aggiungere in un secondo momento
                    # and delta_2 < 0.25 la puoi aggiungere in un secondo momento
                    
                    # compare prega per me !
                    
                    
                   
                    
                # BUY 1 FIAT OK ( con doppio delta in ribasso !) 8-39
                
                elif (    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    and ma8_last > ma39_last
                    
                    and ma200_last < ma300_last
                    and ma20_last < ma100_last
                    and ma100_last < ma100_10_min_ago
                    and deviation_ma200_sotto_ma300 < -0.27
                    
                 
                    and rapporto_delta_1_delta_2 > 1
                    
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 FIAT OK ( CON DOPPIO DELTA in RIBASSO !) 8-39 - r 1552"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    
                    # and delta_1 > 0.69
                    # and delta_2 > 0.50
                    
                    # compare prega per me !
                    
                    
                    
                    
                #####################################################################################################################
             
                # BUY DURANTE UN RIBASSO AUDI copiata da RCCR CHE E' ANDATA BENISSIMO CHE NON E' UN CROLLO ! (compare stammi vicino!)   
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.60
                    and deviation_buy_crollo_1 > -1.50
                    and deviation_bellissima > 0.02
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 DURANTE UN RIBASSO AUDI copiata da RCCR CHE E' ANDATA BENISSIMO CHE NON E' UN CROLLO ! con deviation_bellissima > 0.02 - riga 1578"
                    action = "buy"
                    percentage = 20
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    
                    
                    
                    
                # copia della riga 530 del RCCR CHE FUNZIONA BENISSIMO ma solo un po' piu' prudente ! - BUY grande ribasso MASERATI CHE NON E' UN CROLLO !
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -0.60
                    and deviation_buy_crollo_1 > -1.50
                    and deviation_bellissima > 0.02
                    and deviation_correzione_1 > 0.03
                    and ma13_last > ma50_last
                ):
                    buy = "copia della riga 530 del RCCR ma piu' prudente ! - BUY GRANDE RIBASSO MASERATI CHE NON E' UN CROLLO ! - r 1596"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                
                
                
                
                # QUA DEVI VEDERE - vanno in sovrapposizione - vedi prima come vanno poi correggi
                
                # BUY 1 GRANDE RIBASSO MASERATI CHE NON E' UN CROLLO ! (compare stammi vicino!) HA FUNZIONATO ! viva ro combaro meo !
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -0.91
                    and deviation_buy_crollo_1 > -1.50
                    and ma3_last > ma28_last
                ):
                    buy = "BUY 1 GRANDE RIBASSO MASERATI CHE NON E' UN CROLLO ! and deviation_bellissima > 0.012- r 1615"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    
                
                
                
                ##############################################################################################################################
                # IMPORTANTISSIMO ! - PER COMPRARE DURANTE IL CROLLO - FERRARI - compa prega per me - ( cruise - david gilmour )
                ##############################################################################################################################

                # entriamo nell' area dell' ipervenduto, compa !
                # QUI LASCIO GLI INCROCI !
                
                # BUY 1 CROLLO FERRARI - modo 1
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -2.30
                    and ma3_last > ma7_last
                ):
                    buy = "BUY 1 CROLLO FERRARI - modo 1 - r 1638"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    
             
            
            
                
                # BUY 1 CROLLO FERRARI - modo 2 questa condizione e' entrata in azione ! ( e mi e' sembrata ben fatta !)

                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -1.61
                    and deviation_buy_crollo_2 > 0.11
                ):
                    buy = "BUY 1 CROLLO FERRARI - modo 2 - r 1655"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_buy_crollo_2 = ma3_last / ma13_last
                    
            
            
            
                ##################################################################################################### CONDIZIONI ESPERIMENTALI !
                
                
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
                    buy = "BUY 1 ECCEZIONALE - se ma200 sale da 15 min e 69> COMPRA con deviation 4-25 e un po' piu' su della ma100 ! - r 1683"
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

                    buy = "BUY 1 DOCCIA se ma200 > da 120 min ! COMPRA - r 1706"
                    action = "buy"
                    percentage = 20   
                    
                
                
                
                ############################################################################################################################
                
                # condizione RCCR - BUY 1 DURANTE UNA CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo !
                # ATTENZIONE ! QUESTA E' UNA CONDIZIONE CHE ANDAVA BENE IN RCCR e non prendeva proprio in maddog !
                # questa condizione considera anche le ipotesi in cui ma100< ma200< ma300<  - da aggiungere in un secondo momento
                # e non e' ancora una situazione cosi' drammatica - distanza di ma8 da last trade
                
                elif (    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    and ma8_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                
                ):
                    buy = "condizione RCCR - BUY 1 DURANTE UNA CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo !  - r 1727"
                    action = "buy"
                    percentage = 20
                    
                    # DA AGGIUNGERE
                    # and ma100_last > ma100_120_min_ago
                    # and ma200_last > ma200_120_min_ago
                    # and ma300_last > ma300_60_min_ago
                    # and deviation_ma8_sotto_last_trade_price > -1.50
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    
                    
             
                
                # BUY 1 con con 200 > 200 20 min ago (100 < and 200 < MA 300 >)    
                
                elif (    
               
                    ma3_last > ma28_last
                    
                    and ma100_last < ma100_60_min_ago
                    and ma200_last < ma200_60_min_ago
                    and ma300_last > ma300_60_min_ago
                    
                    and ma200_last > ma200_20_min_ago
                    and ma13_last > ma200_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    
                    buy = "BUY 1 con 200 > 200 20 min ago (100 < and 200 < MA 300 >) and 13-200 !  - riga 1758"
                    action = "buy"
                    percentage = 10
                    
                    
                    
             
                # BUY 1 forever young 1 PIU' PRUDENTE se ma200 > e se ma200 > ma300 - che si preoccupa degli effetti laterali
             
                elif (  
                    ma200_last > ma300_last
                    and deviation_ma100_laterale > 0.18
                    and ma200_last > ma200_15_min_ago
                    and ma3_last > ma11_last
                    and ma5_last > ma200_last
                    and ma10_last > ma10_2_min_ago
                    and ma2_last > ma2_2_min_ago
                ):

                    buy = "BUY 1 forever young 1 PIU' PRUDENTE se ma 200 > e se ma200 > ma300 - che si preoccupa degli effetti laterali - r 1777"
                    action = "buy"
                    percentage = 20
                    
                    # la troppa prudenza qualche volta genera perdite
                    
                    
                
                ################################################################################################
                
                
                # BUY 1 FOREVER YOUNG PIU' AGGRESSIVO con doppio delta < 1 (rialzo) se ma 200 > e se ma200 > ma300  and deviation_ma5_sopra_ma28 > 0.10
                
                elif (  
                    ma100_last > ma200_last
                    and ma200_last > ma300_last
                    
                    and ma200_last > ma200_15_min_ago
                    and rapporto_delta_1_delta_2 < 1
                    and deviation_ma5_sopra_ma28 > 0.01
                 
                    and ma6_last > ma6_2_min_ago
                    and ma13_last > ma69_last
                    and ma13_last > ma13_2_min_ago
                    and ma2_last > ma2_2_min_ago
                ):
                    
                    buy = "BUY 1 FOREVER YOUNG PIU' AGGRESSIVO (doppio delta < 1) (rialzo) se ma 200 > e se ma200 > ma300 questa sarebbe DOPO DOPPIO MINIMO - r 1804"
                    action = "buy"
                    percentage = 20
                    
                    # SITUAZIONE : dopo crollo e dopo primo grande ribalzo 
                    # riprende a scendere 
                    # MA ma100 e' intanto andata > ma200 !
                    # e anche ma200 sta sopra ma300
                    
              
                
                # BUY 1 FOREVER YOUNG PRUDENTE se ma 200 > e se ma200 > ma300 con doppio delta > 1 (ribasso) and deviation_ma5_sopra_ma28 > 0.30
                
                elif (  
                    ma200_last > ma300_last
                    and ma200_last > ma200_15_min_ago
                    and rapporto_delta_1_delta_2 > 1
                    and deviation_ma5_sopra_ma28 > 0.30
                
                    and ma6_last > ma6_2_min_ago
                    and ma13_last > ma69_last
                    and ma13_last > ma13_2_min_ago
                    and ma2_last > ma2_2_min_ago
                ):
                    
                    buy = "BUY 1 FOREVER YOUNG PRUDENTE con doppio delta > 1 (ribasso) and deviation_ma5_sopra_ma28 > 0.30 se ma 200 > e se ma200 > ma300 - r 1829"
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
                    buy = "BUY 1 con DEVIATION ASSURDA se ma200 > da 120 min COMPRA con INCROCIO ma8 ma200 (ma5>ma300 evita gli EFFETTI LATERALI) - r 1851"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_assurda = price / ma200_last
                    
                    
                    
               
            
            #############################################################################################################      COMPRA sessione 2
            
            elif self.session == 2:
                
                
                if (
                    ma69_last > ma69_2_min_ago
                    and deviation_ma100_sopra_ma300 > 0.20
                    
                    and deviation_buy2 > 0.04
                    and deviation_bellissima > 0.151
                    and deviation_buy_ma3_sopra_ma13 > 0.09
                    and deviation_ma7_sopra_ma40 > 0.07
                    and ma2_last > ma2_2_min_ago
                    and price > price_2_min_ago
                    and ma3_last > ma40_last
                ):
                    buy = "BUY 2A rialzo o laterale - r 1875"
                    action = "buy"
                    percentage = 70

                    # deviation_buy_ma3_sopra_ma13 > x e' fondamentale !
                    # deviation_buy2 = ma8_last/ma50_last
                    
                    
                    
                elif (
                    ma69_last > ma69_2_min_ago
                    and deviation_ma100_sopra_ma300 < 0.20
                    
                    and deviation_buy2 > 0.03
                    and deviation_bellissima > 0.14
                    and deviation_buy_ma3_sopra_ma13 > 0.08
                    and deviation_ma7_sopra_ma40 > 0.06
                    and ma2_last > ma2_2_min_ago
                    and price > price_2_min_ago
                    and ma3_last > ma40_last
                ):
                    buy = "BUY 2A ribasso o laterale - r 1875"
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
                    buy = "BUY 2B - r 1895"
                    action = "buy"
                    percentage = 50
                    
                    # deviation_buy_ma3_sopra_ma13 > x e' fondamentale !
                    # deviation_buy2 = ma8_last/ma50_last
            
                ##################################################################################
                
                
                # BUY 2 con doppio delta < 1 trend crescita and deviation_ma5_sopra_ma28 > 0.14
                
                elif (
                    deviation_buy2 > 0.10
                    and ma100_last > ma100_60_min_ago
                    and rapporto_delta_1_delta_2 < 1
                    and deviation_ma5_sopra_ma28 > 0.14
                    
                    and deviation_bellissima > 0.12
                    
                    and deviation_buy_ma3_sopra_ma13 > 0.10
                    and deviation_ma7_sopra_ma40 > 0.10
                    and ma4_last > ma9_last
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma40_last
                    and ma4_last > ma78_last
                ):
                    buy = "BUY 2C - r 1922"
                    action = "buy"
                    percentage = 50
                    
                    # deviation_buy2 = ma8_last / ma50
                    
                    
            
                # BUY 2 con doppio delta > 1 trend ribasso and deviation_ma5_sopra_ma28 > 0.16
                
                elif (
                    deviation_buy2 > 0.10
                    and ma100_last > ma100_60_min_ago
                    and rapporto_delta_1_delta_2 > 1
                    and deviation_ma5_sopra_ma28 > 0.16
                    
                    and deviation_bellissima > 0.12
                    
                    and deviation_buy_ma3_sopra_ma13 > 0.10
                    and deviation_ma7_sopra_ma40 > 0.10
                    and ma4_last > ma9_last
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma40_last
                    and ma4_last > ma78_last
                ):
                    buy = "BUY 2C - r 1947"
                    action = "buy"
                    percentage = 50
                    
                    # deviation_buy2 = ma8_last / ma50
                    
                    
             
                # BUY 2C se ma100 <
                
                elif (
                    deviation_buy2 > 0.10
                    and ma100_last < ma100_60_min_ago
                    and deviation_bellissima > 0.17
                    
                    and deviation_buy_ma3_sopra_ma13 > 0.10
                    and deviation_ma7_sopra_ma40 > 0.10
                    and ma4_last > ma9_last
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma40_last
                    and ma4_last > ma78_last
                ):
                    buy = "BUY 2C - r 1969"
                    action = "buy"
                    percentage = 50
                    
                    # deviation_buy2 = ma8_last / ma50
                    
               
                ####################################################################################################### BUY 2 DURANTE IL CROLLO CHE CONTINUA !    
                # se il crollo continua dopo che ha venduto sell 1 durante il crollo - ro cano CI RIPROVA !     
                
                # BUY 2  primo modo DURANTE IL CROLLO

                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -2.30
                    and ma3_last > ma7_last
                ):
                    buy = "BUY 2 DURANTE IL CROLLO - modo 1 - r 1986"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    
               
                # BUY 2 secondo modo - DURANTE IL CROLLO - questa condizione e' entrata in azione ! ( e mi e' sembrata ben fatta !)

                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -1.70
                    and deviation_buy_crollo_2 > 0.11
                ):
                    buy = "BUY 2 DURANTE IL CROLLO - modo 2 - r 2000"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_buy_crollo_2 = ma3_last / ma13_last
                    
              
                ################################################### per comprare durante UNA piccola CORREZIONE che NON E' un forte ribasso e NON E' un crollo
                
                # BUY 2A PAZZA DURANTE UNA piccola CORREZIONE che NON E' un forte ribasso e NON E' un crollo ! (compare stammi vicino!)
             
                elif (
                    deviation_ma5_sopra_ma28 > 0.23
             
                    and deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
               
                    and deviation_correzione > 0.015
                    and deviation_buy_ma5_sopra_ma20 > 0.10
                    and ma2_last > ma2_2_min_ago
                ):

                    buy = "BUY 2A PAZZA piccola CORREZIONE che non e' un forte ribasso e non e' un crollo ! deviation 5-28 > 0.05 - r 2023"
                    action = "buy"
                    percentage = 10

                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    # ma5 non deve allontanarsi troppo dalla ma200 !
                    # compare prega per me !
                    
                    
                    
                    
                # BUY 2 CORREZIONE che NON E' un forte ribasso e NON E' un crollo ! con deviation_correzione > 0.02
                 
                elif (

                    ma2_last > ma2_2_min_ago
                    and (ma20_prev < ma200_prev and ma20_last > ma200_last)
                    and deviation_correzione_2 > 0.03
                    and deviation_buy_crollo_1 < -0.60
                    and deviation_buy_crollo_1 > -0.90

                ):

                    buy = "BUY 2 CORREZIONE che NON E' un forte ribasso e NON E' un crollo ! con deviation_correzione > 0.02 - r 2047"
                    action = "buy"
                    percentage = 20
                  
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma5_last / ma30_last
                    # compare prega per me !

                    

                
                # BUY 2 FORTE RIBASSO che NON E' UN CROLLO ! (compare stammi vicino!) 
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -0.60
                    and deviation_buy_crollo_1 > -1.50
                    and deviation_bellissima > 0.17
                ):
                    buy = "BUY 2 FORTE RIBASSO che NON E' UN CROLLO ! and deviation_bellissima > 0.17 - r 2066"
                    action = "buy"
                    percentage = 20
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    
                    
                    
                    
                # BUY 2 esperimentali # CON INCROCIO 3-200 HO RISOLTO IL PROBLEMA DEL BUY 2 ECCEZIONALE CHE COINCIDEVA QUASI CON IL SELL 1 ! 
                
                # BUY 2 nuovo TREND LATERALE !

                elif (
                    ma100_last > ma300_last
                    and ma100_last > ma200_last
                    and ma8_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                        
                    and deviation_ma100_sopra_ma300 < 0.04
                    and deviation_ma100_sopra_ma200 < 0.05
                    
                ):
                    buy = "BUY 2 nuovo TREND LATERALE !  - r 2089"
                    action = "buy"
                    percentage = 40
                    
                    # SE ma100 E' cosi' VICINA A ma200 E ma300 vuo dire che non c'e' un grande rialzo in atto ma un TREND LATERALE !
                    
                    
                    
                    
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
                    buy = "BUY 2 andamento laterale se ma200> da 20 min compra con 4-30 (SUL BUY 2 0.50 e 20-69 vs EFFETTI LATERALI !) - r 2115"
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
                    buy = "BUY 2 andamento laterale se ma200> da 20 min compra con 4-30 (SUL BUY 2 0.50 e 20-69 vs EFFETTI LATERALI !) - r 2140"
                    action = "buy"
                    percentage = 40
                    
                    
                    
                 
                # BUY 2 DOCCIA
                
                elif (    

                    ma200_last > ma200_90_min_ago
                    and ma20_last > ma200_last
                    and deviation_ma5_sopra_ma30 > 0.05
                    and ma11_last > ma69_last
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma69_last
                    and (ma4_prev < ma25_prev and ma4_last > ma25_last)
                    and deviation_buy_ma3_sopra_ma25 > 0.05
                ): 
                    buy = "BUY 2 DOCCIA se ma200 > da 90 min ! - r 2160"
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
                    buy = "BUY 2 con DEVIATION ASSURDA se ma200 sale da 120 min BUY con ma2-ma200 (ma5 > ma300 evita GLI EFFETTI LATERALI !) - r 2179"
                    action = "buy"
                    percentage = 20    
          
                    # deviation_assurda = ma2 / ma200
            
            
            
            
            
                # BUY 2 che ci riprova TORNANDO ALLE ORIGINI con ma200< and ma300 < (compare stammi vicino !)
                
                elif (
                    deviation_buy2 > 0.10
                    and deviation_bellissima > 0.16
                    and ma8_last > ma8_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma7_last
                    and ma3_last > ma13_last
                    and deviation_buy_ma3_sopra_ma20 > 0.05
                    and deviation_ma4_sopra_ma25 > 0.05
                    and deviation_ma5_sopra_ma30 > 0.173
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                ):
               
                    buy = "BUY 2 che ci riprova TORNANDO ALLE ORIGINI con ma200< and ma300< - r 2205"
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

                    buy = "BUY 2 con ma200> e ma300> DURANTE UNA piccola CORREZIONE che non e' un forte ribasso e non e' un crollo - r 2231"
                    action = "buy"
                    percentage = 10
                    
                    
                  
                    
                 
                # --------------------------------------- BUY 2 che considera il passare del tempo con TREND IN RIALZO ! sempre 20 > 200
                
                elif (     
                    seconds_since_last_trade > max_hold_time_in_seconds_nuova
                    and deviation_ma5_sopra_ma28 > 0.10
                    and ma30_last > ma30_40_min_ago
                    
                    and ma20_last > ma200_last
                    and ma20_last > ma100_last
                    
                    and ma4_last > ma100_last
                    
                    and ma100_last < ma300_last
                    and deviation_bellissima > 0.07
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 2 che considera il passare del tempo (SE > 120 min) and 5-28 > 0.10 and ma30 > ma 30 40 min ago (TREND IN RIALZO) - r 2255"
                    action = "buy"
                    percentage = 50
                    
                    
                    
                    
                    
                # --------------------------------------- BUY 2 che considera il passare del tempo con TREND IN RIBASSO ! sempre 20 > 200
                
                elif (     
                    seconds_since_last_trade > max_hold_time_in_seconds_nuova
                    and deviation_ma5_sopra_ma28 > 0.17
                    and ma30_last < ma30_40_min_ago
                    
                    and ma20_last > ma200_last
                    and ma20_last > ma100_last
                    
                    and ma4_last > ma100_last
                    
                    and ma100_last < ma300_last
                    and deviation_bellissima > 0.07
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 2 che considera il passare del tempo (SE > 120 min) and 5-28 > 0.17 and ma30 < ma30 40 min ago (TREND IN RIBASSO) - r 2279"
                    action = "buy"
                    percentage = 50
                    
                    
                    
                
                # BUY 2 FIAT che non funzionava MA CHE HA FUNZIONATO BENISSIMO ! ( DOPPIO DELTA in risalita !) copiato da BUY 1 perche' PERFETTO
                
                elif (    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    and ma3_last > ma9_last
                    
                    and ma200_last < ma300_last
                    and ma20_last < ma100_last
                    and ma100_last < ma100_10_min_ago
                    and deviation_ma200_sotto_ma300 < -0.27
                  
                    and rapporto_delta_1_delta_2 < 1
                    
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 2 FIAT che non funzionava MA CHE HA FUNZIONATO BENISSIMO ! ( DOPPIO DELTA in risalita !) copiato da BUY 1 perche' PERFETTO - r 2302"
                    action = "buy"
                    percentage = 20
                    
                    
                    
                    
                    
                # BUY 2 RIALZO IMPROVVISO ! con ma200 > and ma100_last > ma200_last
                
                elif (
                    ma200_last > ma200_20_min_ago
                    and ma100_last > ma200_last
                    and deviation_rialzo_improvviso_sopra > 0.48
                    and deviation_rialzo_improvviso_1 > 0.48
                    and deviation_rialzo_improvviso_2 > 0.19
                    and deviation_rialzo_improvviso_3 > 0.19
                    and deviation_range_1 < 0.20
                    and deviation_range_1 > -0.20
                    and deviation_range_2 < 0.20
                    and deviation_range_2 > -0.20
                    and deviation_range_x < 0.20
                    and deviation_range_x > -0.20
                ):
             
                    buy = "BUY 2 RIALZO IMPROVVISO ! con ma200 > and 100>200 (solo per il buy 2 e per il buy 3) - r 2327"
                    action = "buy"
                    percentage = 10
                    
                    
                    
                    
                # --------------------------------------- BUY 2 che entra in azione se ma2 va sopra SELL 1 di almeno 0.45 !
                
                elif (     
                    seconds_since_last_trade > max_hold_time_in_seconds_delta_buy2_sell1
                    and delta_buy2_dal_sell1 > 0.45
                    and deviation_ma5_sopra_ma28 > 0.15
                    
                    and ma100_last > ma100_60_min_ago
                    and ma200_last > ma200_120_min_ago
                    and ma100_last > ma200_last
                    and ma3_last > ma8_last
                    and ma5_last > ma18_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 2 che entra in azione se DOPO 2 MINUTI ma2 va sopra SELL 1 > 0.45 ! - r 2348"
                    action = "buy"
                    percentage = 40
                    
                    # il BUY 2 con deviation buy2 (8-50) ma anche con (6-30) ARRIVA IN RITARDO !
                    
                    # vedi r107
                    # vedi r180
                    # vedi r409
                    # vedi r1829
                    # compa prega per me !
                    
                    
                    
                 
            ############################################################################################################ COMPRA sessione 3
            
            # forse dal BUY 3 in poi (o dal BUY 4 in poi) DEVE ESSERE ma100 > E ma2 > ma100 !
            # deviation_buy3 = ma4_last/ma30_last 
                    

            elif self.session == 3:

                if (
                    ma10_last > ma10_2_min_ago
                    and ma200_last > ma200_60_min_ago
                    and deviation > -0.30
                    and deviation_ma5_sopra_ma28 > 0.12
                    
                    and deviation_ma4_sopra_ma30 > 0.11
                    and ma3_last > ma13_last
                    and ma4_last > ma9_last
                    and deviation_ma7_sopra_ma40 > 0.08
                    and ma7_last > ma25_last
                    
                    and deviation_buy_ma2_sopra_ma13 > 0.10
                    and ma4_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                    
                ):  
                
                    buy = "BUY 3A con ma200 che sale da 60 min etc. - r 2389"
                    action = "buy"
                    percentage = 50

                    # deviation_buy3 = ma4_last/ma30_last
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    
                
                
                
                elif (
                    ma69_last >= ma69_2_min_ago
                    and ma200_last < ma200_60_min_ago
                    and deviation_bellissima > 0.37
                    and deviation > -0.30
                    
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
                
                    buy = "BUY 3A con ma69 > MA ma200 scende da 60 min ! - r 2417"
                    action = "buy"
                    percentage = 50
            
               
                
                
                elif (
                    deviation_ma4_sopra_ma30 > 0.15
                    and deviation > -0.30
                    and deviation_bellissima > 0.07
                    and ma39_last > ma69_last
                    and delta_buy3_incrocio_ma3_ma8 >= 0.06
                    and ma3_last > ma8_last
                    and ma3_last >= ma69_last
                    and ma4_last >= ma4_2_min_ago
                    and ma2_last >= ma2_2_min_ago
                    and ma5_last >= ma15_last
                    and ma5_last >= ma25_last
                ):    
                    buy = "BUY 3B RIVOLUZIONARIO se ma39 > ma69 - r 2437"
                    action = "buy"
                    percentage = 50
                    
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                
                
                
                
                
                elif (
                    ma78_last < ma78_2_min_ago
                    and deviation > -0.30
                    
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
                    buy = "BUY 3C RIVOLUZIONARIO se ma78 < - r 2461"
                    action = "buy"
                    percentage = 40
                    
                    # deviation_buy3 = ma4_last/ma30_last
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    
                 
                
                
                
                # BUY 3 RIALZO IMPROVVISO ! con ma200 > and ma100_last > ma200_last
                
                elif (
                    ma200_last > ma200_20_min_ago
                    and ma100_last > ma200_last
                    and deviation_rialzo_improvviso_sopra > 0.48
                    and deviation_rialzo_improvviso_1 > 0.48
                    and deviation_rialzo_improvviso_2 > 0.19
                    and deviation_rialzo_improvviso_3 > 0.19
                    and deviation_range_1 < 0.20
                    and deviation_range_1 > -0.20
                    and deviation_range_2 < 0.20
                    and deviation_range_2 > -0.20
                    and deviation_range_x < 0.20
                    and deviation_range_x > -0.20
                ):
             
                    buy = "BUY 3 RIALZO IMPROVVISO ! con ma200 > and 100>200 (solo per il buy 2 e per il buy 3) - r 2489"
                    action = "buy"
                    percentage = 10
                    
               
                    
                
                # BUY 3 CON IL TURBO ! (compare stammi vicino!)   
                
                elif (    
                    ma200_last > ma200_120_min_ago
                    and deviation > -0.30
                    and ma200_last > ma300_last
                    and ma20_last > ma200_last
                    and deviation_bellissima > 0.05
                    and (ma4_prev < ma25_prev and ma4_last > ma25_last)
                    and ma25_last > ma25_2_min_ago
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 3 CON IL TURBO - r 2508"
                    action = "buy"
                    percentage = 50
                    
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    
          
                
                
                
                # BUY 3 PAZZA piccola CORREZIONE FIAT
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation > -0.30
                    
                    and deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    and deviation_correzione > 0.015
                    and deviation_buy_ma5_sopra_ma20 > 0.12
                    and deviation_ma5_sotto_ma200 > -1.00
                    
                ):

                    buy = "BUY 3 PAZZA piccola CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo ! con deviation_correzione > 0.02 - r 2532"
                    action = "buy"
                    percentage = 10

                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    # ma5 non deve allontanarsi troppo dalla ma200 !
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    
                    
            
            
            
            # ###########################################################################################################       COMPRA sessione 4
            # ----------------------------------------------------------------------------------------------------------------- deviation piu' alte se ma 78 < !
            
            # ########################################### se 300 < il buy 4 deve stare sopra ma100

            elif self.session == 4:
                
                if (
                    ma69_last >= ma69_2_min_ago
                    and ma300_last > ma300_60_min_ago
                    and ma100_last > ma200_last
                    and deviation_buy3 > 0.11
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.11
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                    
                    and ma13_last > ma100_last
                    and deviation_ma5_sopra_ma28 > 0.05
                ):
                    buy = "BUY 4A con ma 78> e 300> E ma100>ma200 - r 2567"
                    action = "buy"
                    percentage = 50
                    
                
                
                
                # se al BUY 4 ha ma100 < ma200 evidentemente c'e' qualche cosa di strano 
                # il trend, evidentemente, e' LATERALE.
                # E ALLORA AGGIUNGO UN BEL 6-30 > 0.15 - TREND LATERALE
             
                
                elif (
                    ma69_last >= ma69_2_min_ago
                    and ma300_last > ma300_60_min_ago
                    and ma100_last < ma200_last
                    and deviation_bellissima > 0.15
                    and deviation_buy3 > 0.11
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.11
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                    
                    and ma13_last > ma100_last
                    and deviation_ma5_sopra_ma28 > 0.05
                ):
                    buy = "BUY 4A con ma 78 > TREND LATERALE con 6-30 > 0.15 - r 2595"
                    action = "buy"
                    percentage = 50
                    
                    
                    
                    
                ##############################################################################################
                
                # BUY 4A con ma 78> e 300< ma 100>200
                
                elif (
                    ma78_last >= ma78_2_min_ago
                    and ma300_last < ma300_60_min_ago
                    and ma100_last > ma200_last
                    
                    and deviation_ma4_sopra_ma100 > 0.25
                    
                    and ma300_last < ma300_120_min_ago
                    and deviation_buy3 > 0.11
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.11
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                    
                    and ma13_last > ma100_last
                    and deviation_ma5_sopra_ma28 > 0.05
                ):
                    buy = "BUY 4A con ma 78> e 300< ma 100>200 - r 2625"
                    action = "buy"
                    percentage = 50
                    
                    
                    
                    
                # BUY 4A con ma 78> e 300< e 100<200
                
                elif (
                    ma78_last >= ma78_2_min_ago
                    and ma300_last < ma300_60_min_ago
                    and ma100_last < ma200_last
                    and deviation_bellissima > 0.15
                    
                    and deviation_ma4_sopra_ma100 > 0.25
                    
                    and ma300_last < ma300_120_min_ago
                    and deviation_buy3 > 0.11
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.11
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                    
                    and ma13_last > ma100_last
                    and deviation_ma5_sopra_ma28 > 0.05
                ):
                    buy = "BUY 4A con ma 78> e 300< e 100<200 - r 2654"
                    action = "buy"
                    percentage = 50
                    
                    #####################################################################
                
                
                
                
                elif (
                    ma78_last >= ma78_2_min_ago
                    and ma300_last > ma300_60_min_ago
                    
                    and deviation_buy3 > 0.02
                    and delta_buy3_incrocio_ma3_ma8 > 0.05
                    and deviation_ma4_sopra_ma30 > 0.14
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last >= ma4_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                    
                    and ma13_last > ma100_last
                    and deviation_ma5_sopra_ma28 > 0.05
                ):
                    buy = "BUY 4B RIVOLUZIONARIO con ma78 > - r 2679"
                    action = "buy"
                    percentage = 50
                    
                    # deviation_buy3 = ma4_last/ma30_last
                    # deviation_ma4_sopra_ma100 > 0.25 arrivati al buy 4 DEVE AVERE UNA CERTA FORZA !
                    
              
            
            
            
                elif (
                    ma78_last >= ma78_2_min_ago
                    and ma300_last < ma300_60_min_ago
                    and deviation_ma4_sopra_ma100 > 0.25
                    
                    and deviation_buy3 > 0.02
                    and delta_buy3_incrocio_ma3_ma8 > 0.05
                    and deviation_ma4_sopra_ma30 > 0.14
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last >= ma4_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                    
                    and ma13_last > ma100_last
                    and deviation_ma5_sopra_ma28 > 0.05
                ):
                    buy = "BUY 4B RIVOLUZIONARIO con ma78 > - r 2707"
                    action = "buy"
                    percentage = 50
                    
                    # deviation_buy3 = ma4_last/ma30_last
                    # deviation_ma4_sopra_ma100 > 0.25 arrivati al buy 4 DEVE AVERE UNA CERTA FORZA !
                    
                    
                    
                ###################################################################################################
               
                elif (
                    ma78_last < ma78_2_min_ago
                    and ma300_last > ma300_60_min_ago
                    
                    and deviation_buy3 > 0.04
                    and delta_buy3_incrocio_ma3_ma8 > 0.08
                    and deviation_ma4_sopra_ma30 > 0.20
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                    
                    and ma13_last > ma100_last
                    and deviation_ma5_sopra_ma28 > 0.05
                ):
                    buy = "BUY 4C RIVOLUZIONARIO con ma78 < - r 2734"
                    action = "buy"
                    percentage = 50
                    
                    
             
            
                elif (
                    ma78_last < ma78_2_min_ago
                    and ma300_last < ma300_60_min_ago
                    and deviation_ma4_sopra_ma100 > 0.25
                    
                    and deviation_buy3 > 0.04
                    and delta_buy3_incrocio_ma3_ma8 > 0.08
                    and deviation_ma4_sopra_ma30 > 0.20
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                    
                    and ma13_last > ma100_last
                    and deviation_ma5_sopra_ma28 > 0.05
                ):
                    buy = "BUY 4C RIVOLUZIONARIO con ma78 < - r 2758"
                    action = "buy"
                    percentage = 50
                    
          
                #############################################################################################
             
                # BUY 4A PAZZA DURANTE UNA piccola CORREZIONE che NON E' un forte ribasso e NON E' un crollo ! (compare stammi vicino!)
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    and deviation_ma5_sopra_ma25 > 0.21
                    
                    and deviation_correzione > 0.015
                    and deviation_buy_ma5_sopra_ma20 > 0.14
                    and deviation_ma5_sotto_ma200 > -1.00
                ):    
           
                    buy = "BUY 4A PAZZA DURANTE UNA piccola CORREZIONE che non e' un forte ribasso e non e' un crollo ! con deviation_correzione > 0.02 - r 2778"
                    action = "buy"
                    percentage = 10
                    
                    # capita a volte il buy 4. fai attenzione! (se BUY 4 sta sotto ma78 e' un caso particolare !)

                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    # ma5 non deve allontanarsi troppo dalla ma200 !
                    
                    
            
            
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
                
                ):
                    buy = "BUY 5 con ma69 > and deviation_bellissima > 0.12 (PER SPEZZARE LA CATENA - effetti laterali) riga 2811"
                    action = "buy"
                    percentage = 50
                    
                    # deviation_bellissima = 6/30
                    # spezzare la catena dei buy - effetti laterali.
                    # se e' arrivato il buy 5 e' molto probabile che il trend sia consolidato
                    # e, a questo punto, non importa se compra con un + 0.10 piu' in alto. NON FA UNA GRANDE DIFFERENZA !
                    
                    
                    
                elif (
                    ma78_last >= ma78_2_min_ago
                    and deviation_ma4_sopra_ma100 > 0.25
                    
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
                    buy = "BUY 5A con ma78 > and deviation_bellissima > 0.163 (PER SPEZZARE LA CATENA -effetti laterali) - r 2837"
                    action = "buy"
                    percentage = 50
                    
                    # deviation_bellissima = 6/30
                    # spezzare la catena dei buy - effetti laterali !
                    # se e' arrivato il buy 5 e' molto probabile che il trend sia consolidato
                    # e, a questo punto, non importa se compra con un + 0.10 piu' in alto. NON FA UNA GRANDE DIFFERENZA !
                    
                    
              
                elif (
                    ma200_last >= ma200_120_min_ago
                    and deviation_ma4_sopra_ma100 > 0.25
                    and ma3_last > ma15_last
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                    and ma7_last > ma25_last
                    and ma13_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                ):   
                    buy = "BUY 5B RIVOLUZIONARIO che NON SPEZZA LA CATENA SE ma200> 120 min) - r 2859"
                    action = "buy"
                    percentage = 50
                    
                    # deviation_buy3 = ma4_last/ma30_last
                    # ok tu non voi spezzare la catena.
                    # ma per essere un BUY 5 devi avere almeno ma13>ma50 cazzo !
                    
                    
                
                
                elif (
                    ma78_last >= ma78_2_min_ago
                    and deviation_ma4_sopra_ma100 > 0.25
                    
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
                    buy = "BUY 5C RIVOLUZIONARIO con ma78 > and deviation_bellissima > 0.163 (PER SPEZZARE LA CATENA -effetti laterali) - r 2886"
                    action = "buy"
                    percentage = 50
                    
                    
                    
                # BUY 5 copiata da buy1 r1313 con modifiche
                
                elif (    
                    
                    ma200_last > ma200_20_min_ago
                    and ma3_last > ma28_last
                    
                    and ma100_last > ma200_last
                    and ma200_last > ma300_last
                    
                    and ma100_last > ma100_120_min_ago
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    
                    and ma13_last > ma100_last
                    and deviation_ma100_sopra_ma300 > 0.70
                    
                    and ma2_last > ma2_2_min_ago
                    
                ):    
                    
                    buy = "BUY 5 copiata da BUY 1 r1313 con modifiche - riga 2946"
                    action = "buy"
                    percentage = 10
                    
                    
                    
                    
                # BUY 5D RIVOLUZIONARIO con ma78 < and deviation_bellissima > 0.163
                
                elif (
                    ma78_last < ma78_2_min_ago
                    and deviation_ma4_sopra_ma100 > 0.25
                    
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
                    buy = "BUY 5D RIVOLUZIONARIO con ma78 < and deviation_bellissima > 0.163 - r 2909"
                    action = "buy"
                    percentage = 50
                    
                    
                    
            
                # BUY 5A PAZZA DURANTE UNA piccola CORREZIONE che NON E' un forte ribasso e NON E' un crollo ! (compare stammi vicino!)
              
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    and deviation_correzione > 0.015
                    and deviation_buy_ma5_sopra_ma20 > 0.14
                    and deviation_ma5_sotto_ma200 > -1.00
                ):    
              
                    buy = "BUY 5 PAZZA DURANTE UNA piccola CORREZIONE che non e' un forte ribasso e non e' un crollo ! con deviation_correzione - r 2927"
                    action = "buy"
                    percentage = 10

                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    # ma5 non deve allontanarsi troppo dalla ma200 !
                    
              
        
        
        
        
        
        ############################################################################################

        #  V E N D I T A !                                                                    

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
            # sell sessione 3 .................... righe 2500 - 3386
            # sell sessione 4-5-x ................ righe 2500 - 3386
           
            # VENDITA - con fasce di tempo ! minuti

            #   0 -  3
            #   3 -  5
            #   5 - 12
            #  12 - 21
            #  21 - 50
            #  50 - 90 
            #  90 - 110 solo le prime 2 sessioni  (> 90 min tutte le altre)
            #    > 90
          
            # < -0.10  ma78 che mi salva (nel movimento laterale mi fa perdere la meta')
            # < -0.20
            # 0.25 - 0.59  MARADONA 5-25 CHE DOPO 60 MIN DIVENTA 5-39 che dopo 90 min diventa 5-50
            # 0.60 - 1.20  RONALDO CHE DOPO 60 MIN DIVENTA 4-20
            # 1.21 - 2.50  TACCO DI ALLAH
            #  > 2.50      SI VIVE TRA GLI ANGELI, compa !
            
            # vendite eccezionali
            
            # aumento la perdita tollerata se trend < (ma50<) MA ma200> e ma200 > ma300 !
         
            ####################################################################################################################### SESSIONE 1
            
            # al SELL 1 PUOI AUMENTARE LA PERDITA TOLLERATA POICHE' HAI SOLO IL 10%-20% DEL CAPITALE - eviterai, INOLTRE, un po' di sell e buy nel movimenti laterali !
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
                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.23 - r 3017"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                 
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.27 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.27 - 0.60 LA PRIMA FINTA DI MARADONA - r 3031"
                        action = "sell"
                        
                        
                
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.61 and deviation_sell < 0.79
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.61 - 0.79 IL PRIMO DRIBBLING ALLA RONALDO  - r 3043"
                        action = "sell"

                    # attenzione : tacco di allah e dribbling alla ronaldo SOLO con ma50> (altrimenti si attivano in "sell durante il crollo" che ha le sue leggi.)
                    
                    
                
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 0.80 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell 0.80 - 1.20 ( DOPPIA FINTA ALLA RONALDO ! ) - r 3058"
                        action = "sell"
                        
                        
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 1.21 and deviation_sell < 1.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell 1.21-1.7( TACCO DI ALLAH ! ) - r 3070"
                        action = "sell"
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 1.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell > 1.71 ( SI VA TRA GLI ANGELI, compa ! ) - r 3083"
                        action = "sell"
                        
                   
                
                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 < and incrocio 3-28 - r 3096"
                        action = "sell"

                    # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                    
                    
                   
                    
                    # SELL 1 (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 and rapporto_delta_1_delta_2 < 1
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and rapporto_delta_1_delta_2 < 1
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.29
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.29 and rapporto_delta_1_delta_2 < 1  - r 3113"
                        action = "sell"
                        
                        
                        
                        
                    # SELL 1 (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 and rapporto_delta_1_delta_2 > 1
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and rapporto_delta_1_delta_2 > 1
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 and rapporto_delta_1_delta_2 > 1 - r 3128"
                        action = "sell"
                        
                        
                   
                 
                    # ---------------------------------------------------------------------------------------------------------------------- crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - r 3142"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                   
                
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - r 3156"
                        action = "sell"
                        
                        
                      
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                        and deviation_sell > 0.61 and deviation_sell < 0.80
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - r 3169"
                        action = "sell"
                  
               
            
            
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma2_prev > ma5_prev and ma2_last < ma5_last)
                        and deviation_sell > 0.81
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - r 3182"
                        action = "sell"
             
            
            
                ################################################################################################################## sessione 1 ( 3-5 min )

                # VENDITA - da 3 a 5 minuti = da 180 a 300 secondi

                elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 300:

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell < -0.24
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.24 - r 3200"
                        action = "sell"
                         
                        # deviation_sell = ma3_last/last_trade_price
                        
                
                
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.27 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                       
                        
                    ):
                        sell = "SELL 1 (3-5 min) con ma50> 5-25 and deviation_sell 0.27 - 0.60 - la prima FINTA ALLA MARADONA - r 3216"
                        action = "sell"
                         
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                     

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.61 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 > and incrocio 3-15 and deviation_sell 0.91 - 1.20 DRIBBLING ALLA RONALDO - r 3230"
                        action = "sell"
                        
                        
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 1.21 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 > and incrocio 3-20 and deviation_sell 1.21 -2.70 ( TACCO DI ALLAH ! ) - r 3242"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 > and incrocio 3-11 and deviation_sell > 2.71 ( SI VA TRA GLI ANGELI, comba ! ) - r 3254"
                        action = "sell"
                        
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 < and incrocio 3-28 - r 3269"
                        action = "sell"
                        
                        # deviation_sell_ma78 = ma3_last / ma78_last
                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.25
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.25 - r 3283"
                        action = "sell"

                    
                    
                    
                    # guadagno durante il crollo o il trend discendente
                     
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23 and deviation_sell < 0.80
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-23 and gain > 0.23 - r 3297"
                        action = "sell"
                        
                    
                  
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma2_prev > ma5_prev and ma2_last < ma5_last)
                        and deviation_sell > 0.81 and deviation_sell < 1.70
                        and ma2_last < ma2_2_min_ago

                    ):

                        sell = "SELL 1 CROLLO (3-5 min) con ma50 < and incrocio 2-5 and gain > 0.81-1.70 - r 3310"
                        action = "sell"

                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma9_prev and ma3_last < ma9_last)
                        and deviation_sell > 1.71
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-9 and gain > 1.71 - r 3323"
                        action = "sell"
                        
                        
                     

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 3335"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE !
                        
                        

                ############################################################################################################ sessione 1 ( 5-12 min )

                # VENDITA - da 5 a 12 minuti = da 300 a 720 secondi

                elif seconds_since_last_trade > 300 and seconds_since_last_trade <= 720:

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.41
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - r 3355"
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
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - r 3372"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        
                        and deviation_sell > 0.27 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                    
                    ):
                        sell = "SELL 1 (5-12 min) con ma50> 5-25 and deviation_sell 0.27 - 0.60 - FINTA ALLA MARADONA - r 3388"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                      
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma13_last
                        
                        and deviation_sell > 0.61 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 >  3-13 and deviation_sell 0.61 - 0.90 - DRIBBLING ALLA RONALDO - r 3404"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 3-15 and deviation_sell 0.91 - 1.20 ( DOPPIA FINTA ALLA RONALDO ) - r 3420"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 1.21 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 3-15 and deviation_sell 1.21-2.70 ( TACCO DI ALLAH ! ) - r 3435"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 3-11 and deviation_sell > 2.71 ( SI STA TRA GLI ANGELI, compa! ) - r 3447"
                        action = "sell"
                        
                        
                      
                    
                    
                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.49
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 < and incrocio 3-28 and deviation_sell < -0.49 - r 3462"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 < and incrocio 3-100 (cuscino di sant' antonio) - r 3475"
                        action = "sell"
                        
                        
                    
                    
                    # ------------------------------------------------------------------------------- guadagno con crollo
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23 and deviation_sell < 0.54
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 < GUADAGNO DURANTE IL CROLLO 0.23-0.54 con incrocio 3-23 - r 3491"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 0.55
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 < GUADAGNO DURANTE IL CROLLO > 0.55  and incrocio 3-13 - r 3502"
                        action = "sell"
                        
                        
                        

                    # -------------------------------------------------- PARACADUTE crollo SE SI RIDUCE LA DISTANZA TRA ma 100 E ma 200 quindi sta risalendo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.45
                        and ma2_last < ma2_2_min_ago
                        
               
                        and rapporto_delta_1_delta_2 < 1
                    ):
                        sell = "SELL 1 PARACADUTE CROLLO distanza < tra ma100 e ma200 (5-12 min) con ma50 < and ma3 < ma16 and deviation_sell < -0.35 - r 3519"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE ma sta risalendo
                        # and delta_1 < 0.25
                        # and delta_2 > 0.40
                        
                        
                      
                    
                    # --------------------------------------------------- PARACADUTE crollo SE AUMENTA LA DISTANZA TRA ma 100 E ma 200 quindi grande ribasso
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.35
                        and ma2_last < ma2_2_min_ago
                        
                        
                        
                        and rapporto_delta_1_delta_2 > 1
                    ):
                        sell = "SELL 1 PARACADUTE CROLLO distanza > tra ma100 e ma200 (5-12 min) con ma50 < and ma3 < ma16 and deviation_sell < -0.35 - r 3541"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE ma sta continuando a scendere
                        # and delta_1 > 0.40
                        # and delta_2 < 0.25
                        
                 
                
                
                ###################################################################################################################  SESSIONE 1 ( 12-21 min )

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
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-72 and deviation sell -0.65 e vaffanculo ! - r 3566"
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
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.36 - r 3585"
                        action = "sell"
                        
                        # viva sant' antonio !
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.27 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 1 (12-21 min) con ma50> and 5<25 and deviation_sell 0.27-0.56 - FINTA ALLA MARADONA - r 3600"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma13_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 1 (12-21 min) con ma50> and 3<13 (NO INCROCIO 3-13) and deviation_sell 0.57-0.90 - DOPPIO PASSO ALLA RONALDO - r 3615"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 ( DOPPIA FINTA ALLA RONALDO ) - r 3630"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.21 and deviation_sell < 1.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-30 and deviation_sell 1.21-1.70 ( IL TACCO DI ALLAH ) - r 3645"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 1.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-15 and deviation_sell > 1.71 ( SI STA TRA GLI ANGELI, compa ! ) - r 3657"
                        action = "sell"
                        
                        
                      
                    
                    ##########################################################################################
                    # NON TOCCARE ! CUSCINO DI SANT' ANTONIO !
                    # L' INCROCIO 5-100 MI SALVA ! MA 5<100 VENDE DURANTE IL RIBASSO !
                    ##################################################################### con trend discendente

                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.159
                        and deviation_sell < -0.34
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 < and deviation_ma39 < -0.159 and deviation_sell < -0.34 - r 3674"
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
                        sell = "SELL 1 (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - r 3693"
                        action = "sell"
                        
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50 < !
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - r 3707"
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
                        sell = "SELL 1 PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 3723"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                   
                
                
                    # ----------------------------------------------------------------------------- guadagno con crollo
                   
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell > 0.25 and deviation_sell > 0.54
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3 - 16 and deviation_sell 0.25-0.54 - r 3741"
                        action = "sell"
                        
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 0.55
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3-11 and deviation_sell > 0.55 - r 3753"
                        action = "sell"
                        
                   
                
                    # ----------------------------------------------------------------------------- torna a casa durante il crollo con minor danno 
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma36_prev and ma3_last < ma36_last)
                        and deviation_sell < -0.25
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 torna a casa durante il crollo con minor danno  (12-21 min) con ma50 < and incrocio 3-36 and deviation_sell < -0.25 - r 3766"
                        action = "sell"
                        
                
               
                ################################################################################################################# SESSIONE 1 ( 21-60 min )

                # VENDITA - da 21 a 50 minuti = da 1261 a 3000 secondi

                elif (
                    seconds_since_last_trade > 1261 and seconds_since_last_trade <= 3000
                ):
                    if (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.65
                        and ma2_last < ma2_2_min_ago
                    
                    ):
                        sell = "SELL 1 (21-50 min) con ma50> and incrocio 3-78 and deviation_sell<-0.65 - r 3785"
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
                        sell = "SELL 1 (21-50 min) con ma50> and deviation_sell <-0.32 and ma3_last < ma50_last - r 3804"
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
                        sell = "SELL 1 (21-50 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.26 - r 3822"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma5_last < ma30_last
                        and deviation_sell > 0.34 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and 5-30 and deviation_sell 0.34 - 0.56 la prima FINTA ALLA MARADONA - r 3836"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma5_last < ma22_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and 5-22 (era 4-15) and deviation_sell 0.51 - 0.90 ELASTICO ALLA RONALDO - r 3848"
                        action = "sell"
                        
                        # dopo 26 minuti non c'e' piu' quello scatto in avanti - dribbling- che si verifica nei primi minuti
                        # deviation_sell = ma3_last/last_trade_price
                        
                 

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma4_prev > ma16_prev and ma4_last < ma16_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and incrocio 4-16 and deviation_sell 0.91 - 1.20 (DOPPIA FINTA DI RONALDO) - r 3863"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma4_prev > ma22_prev and ma4_last < ma22_last)
                        and deviation_sell > 1.21 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and incrocio 4-22 and deviation_sell 1.21 - 2.70 (DOPPIO PASSO DI RONALDO)- r 3878"
                        action = "sell"
                        
                  
               
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma9_prev and ma3_last < ma9_last)
                        and deviation_sell > 2.71 and deviation_sell < 5.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and incrocio 3-9 and deviation_sell 2.71 - 5.70 (TACCO DI ALLAH) - r 3890"
                        action = "sell"
                        
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell > 5.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and incrocio 3-39 and deviation_sell > 2.71 (SI STA TRA GLI ANGELI, comba !) - r 3902"
                        action = "sell"
                        
                    
                    
                    ############################################################################## CUSCINO DI SANT' ANTONIO per questo segmento di tempo !
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma5_last < ma100_last
                        and deviation_sell < -0.10
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and 5-100 and deviation_sell < -0.10 CUSCINO DI SANT' ANTONIO - r 3917"
                        action = "sell"
                  
                    
                   
                    ##################################################################### con trend discendente
                    
                  
                    ################################################################################################ con ma100 DISTANTE sopra dalla ma300
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.16
                        and ma2_last < ma2_2_min_ago
                        
                        and deviation_ma100_sopra_ma300 > 0.69
                       
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 < con deviation_ma39 <-0.16 TREND CRESCITA (100 sopra 300 > 0.69) - r 3935"
                        action = "sell"
                        
                        # and ma3_last < ma33_last
                        # and deviation_sell < 0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # cuscino dell' angelo custode
                        
                    
                    
                    
                    # cuscino sant' antonio
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                
                        and deviation_ma100_sopra_ma300 > 0.69
                        and deviation_sell < -0.10
                        and ma5_last < ma100_last
                    ):
                        sell = "SELL 1 (21-50 min)con ma50 < CUSCINO SANT' ANTONIO (5-100) MA SOLO con TREND CRESCITA (100 sopra 300 > 0.69) - r 3957"
                        action = "sell"
                        
                        
                    
                    
                    
                    # TREND LATERALE (100>300 MA <0.69)
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.17
                        and ma2_last < ma2_2_min_ago
                        
                        and deviation_ma100_sopra_ma300 < 0.69
                        and deviation_sell < -0.15
                       
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 < con deviation_ma39 <-0.17 and deviation_sell < 0.10 TREND LATERALE (100>300 MA <0.69) - r 3975"
                        action = "sell"
                        
                        
                    
                    ######################################################################## con ma50 DISTANTE dalla ma300 # queste 2 son un souvenir !
                    
                    # ho considerato, poi, la distanza tra ma100 e ma300 (ma il principio e' lo stesso)
                    # se ma100 sta molto sopra ma300 TREND IN CRESCITA interviene solo ma39
                    # ma se ma100 e' vicina alla ma300 TREND LATERALE interviene la ma39 E la deviation sell !
                    
                    # poi c'e' il cuscino di sant' antonio 5-100
                    
                    ##########################################################################################
                    
                    # SELL 1 maestro parte 1 (21-50 min) con ma50 < and deviation_ma39 < -0.27
                    
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.27
                        and deviation_ma50_sotto_ma300 > 0.50
                    ):
                        sell = "SELL 1 maestro parte 1 (21-50 min) con ma50 < and deviation_ma39 < -0.27 - r 3998"
                        action = "sell"
                        
                        
                        
                    
                    
                    # SELL 1 maestro parte 2 (21-50 min) con ma50 < and deviation_sell < -0.32
                    
                    elif (        
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.32
                        and deviation_ma50_sotto_ma300 < 0.50
                    ):
                        sell = "SELL 1 maestro parte 2 (21-50 min) con ma50 < and deviation_sell < -0.32 - r 4013"
                        action = "sell"
                
                 
                    
                    #####################################################################################
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.37
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - r 4026"
                        action = "sell"
                        
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO and deviation_sell < -0.27 - r 4038"
                        action = "sell"
                        
               
            
                    ############################################################# con ma50 discendente MA ma200 ET ma200>ma300 - PERDITA TOLLERATA AUMENTA
                    # ho diviso il maestro in 2 !
                  
                    elif (
                        
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.28
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 compa (21-50 min) con ma50 < and deviation_ma39 < -0.28 con > PERDITA TOLLERATA - r 4056"
                        action = "sell"
                        
                        # and deviation_ma39 < -0.15 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        
                        # ERRORE GRAVE CORRETTO DAL MAESTRO - VENDEVA MENTRE SALIVA !
                        # ma50_last < ma50_2_min_ago
                        # and ma2_last < ma2_2_min_ago
                        # and deviation_ma39 < -0.25
                        # or deviation_sell < -0.26
                        
                        
                        
              
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.28
                        and deviation_trend_ma200 > -0.03
                        and ma200_last > ma300_last
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 compa (21-50 min) con ma50 < and deviation_sell < -0.28 con > PERDITA TOLLERATA - r 4079"
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
                        sell = "SELL 1 (21-50 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.40 - CON PERDITA TOLLERATA > - r 4102"
                        action = "sell"
                        
                        
                        

                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        
                        and ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 < and INCROCIO 3-100 -0.30 CUSCINO DI SANT' ANTONIO - CON PERDITA TOLLERATA > - r 4117"
                        action = "sell"
                        
                  
                
                    # -------------------------------------------------------------------------------------- guadagno durante il crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell > 0.30 
                        and deviation_sell < 0.54
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 eventuale guadagno durante il crollo (21-50 min) con ma50 < incrocio 3 - 28 and deviation_sell 0.30 - 0.54 - r 4132"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 0.55
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 eventuale guadagno durante il crollo (21-50 min) con ma50 < incrocio 3 - 11 and deviation_sell > 0.55 - r 4143"
                        action = "sell"
                        
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell < -0.24
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 piccola perdita durante il crollo (21-50 min) con ma50 < incrocio 3 - 18 and deviation_sell < -0.24 - r 4155"
                        action = "sell"
                        
                        
              
            
            
                #############################################################################################################  SESSIONE 1 ( da 50 a 90 min )

                # VENDITA - da 50 a 90 min - da 3001 a 5400 secondi in poi
                
                elif (
                    seconds_since_last_trade > 3001 and seconds_since_last_trade <= 5400
                ):
                    
                    
                    if (    
                        ma50_last > ma50_2_min_ago
                        and deviation_ma39 < -0.22
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > and deviation_ma39 <-0.22 - r 4176"
                        action = "sell"
                        
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        
                     
                        
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and deviation_sell < -0.23
                        and ma3_last < ma50_last
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > and deviation_sell < -0.23 and ma3_last < ma50_last  - r 4189"
                        action = "sell"
                        
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        
                   
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma50_prev and ma5_last < ma50_last)
                        and deviation_sell > 0.32 and deviation_sell < 0.52
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > and incrocio 5-50 and deviation_sell 0.31-0.52 la prima FINTA ALLA MARADONA - r 4202"
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
                        sell = "SELL 1 da 50 a 90 min con ma50> and incrocio 4-20 and deviation_sell 0.51-0.90 RONALDO - r 4218"
                        action = "sell"
                        
                        
                        
                    ############################################################################ ronaldo 60-90 min dal buy se ma200 < non perdona
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma200_last < ma200_120_min_ago
                        and (ma4_prev > ma39_prev and ma4_last < ma39_last)
                        and deviation_sell > 0.53 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50> and incrocio 4-39 and deviation_sell 0.51-0.90 RONALDO - r 4232"
                        action = "sell"
                        
                        
                        
                    ##################################################################################################################
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > and incrocio 3-30 and deviation_sell 0.91 - 1.49 RABONA DI RONALDO - r 4246"
                        action = "sell"
                  
                        # ma ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                    
                        
                        
                       
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > incrocio 3-33 and deviation_sell > 1.50 DOPPIO PASSO ALLA RONALDO - r 4260"
                        action = "sell"
                        
                        
                        
                      
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 da 50 a 90 min con ma50 > incrocio 3-11 and deviation_sell > 2.71 TACCO DI ALLAH - r 4273"
                        action = "sell"
                        
                        
                  
                    ######################################################################################## con trend discendente ma50 <
                    
                    ############################################################## ipotesi peggiore e sono cazzi ! and doppio delta ( sempre con ma50 < )
                    
                    # SELL 1 50-90 min IPOTESI PEGGIORE con ma50< con deviation_ma39 <-0.205 and deviation_sell < -0.205 and DOPPIO DELTA RIBASSO
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma300_last
                        and deviation_trend_ma200 < -0.10
                        
                        and deviation_ma39 < -0.19
                        and deviation_sell < -0.195
                        
                        and rapporto_delta_1_delta_2 > 1
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 50-90 min IPOTESI PEGGIORE con ma50 < con deviation_ma39 <-0.19 and deviation_sell < -0.195 E DOPPIO DELTA RIBASSO - r 4296"
                        action = "sell"
                        
                        
                        
                        
                    # SELL 1 50-90 min IPOTESI PEGGIORE con ma50< con deviation_ma39 <-0.205 and deviation_sell < -0.205 MA DOPPIO DELTA RIALZO
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma300_last
                        and deviation_trend_ma200 < -0.10
                        
                        and deviation_ma39 < -0.215
                        and deviation_sell < -0.215
                        
                        and rapporto_delta_1_delta_2 < 1
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 50-90 min IPOTESI PEGGIORE con ma50< con deviation_ma39 < -0.215 and deviation_sell < -0.215 MA DOPPIO DELTA RIALZO - r 4316"
                        action = "sell"
                        
                        
                        
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma300_last
                        and deviation_trend_ma200 < -0.10
                        
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.15
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 50 a 90 min IPOTESI PEGGIORE con ma50 < con incrocio 3-78 and deviation_sell < -0.15 - r 4333"
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
                        sell = "SELL 1 da 50 a 90 min IPOTESI un po' MENO PEGGIO con ma50 < con deviation_ma39 <-0.19 and deviation_sell < -0.195 - r 4351"
                        action = "sell"
                        
                        
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma300_last
                        and deviation_trend_ma200 > -0.10
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.15
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 50 a 90 min IPOTESI un po' MENO PEGGIO con ma50 < con incrocio 3-78 and deviation_sell < -0.15 - r 4366"
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
                        sell = "SELL 1 da 50 a 90 min UN PO' MEGLIO con ma50 < con deviation_ma39 <-0.22 and deviation_sell < -0.23 - r 4383"
                        action = "sell"
                        
                        
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma300_last
                        and deviation_trend_ma200 < -0.10
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.17
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 50 a 90 min UN PO' MEGLIO con ma50 < con incrocio 3-78 and deviation_sell < -0.17 - r 4398"
                        action = "sell"    
                    
                
                    ##################################################### sempre con ma50 discendente MA trend ma200> ET ma200 > ma300 - PERDITA TOLLERATA AUMENTA
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma300_last
                        and deviation_trend_ma200 > -0.10
                        
                        and deviation_ma39 < -0.23
                        and deviation_sell < -0.30
                        
                        and ma2_last <= ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 50-90 min BEST ma sempre con ma50< con deviation_ma39 <-0.23 and deviation_sell <-0.30 - CON PERDITA TOLLERATA> - r 4415"
                        action = "sell"
                        
                        # ha fatto perdita dell' 1% - forse succede tutto in quei 2 minuti se crolla improvvisamente
                        # con deviation_ma39 < -0.27
                        # con deviation_sell < -0.28
                        
                        
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma300_last
                        and deviation_trend_ma200 > -0.10
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.17
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 50-90 min BEST ma sempre con ma50 < con incrocio 3-78 and deviation_sell < -0.17 - CON PERDITA TOLLERATA > - r 4433"
                        action = "sell"
                        
                
                
                
                ########################################################################################################
                ########################################################################################################
                ######################################################################################################## SESSIONE 1 ( da 90 min a 110 min )

                # VENDITA - da 90 minuti a 110 minuti  = da 5400 secondi a 6600 secondi

                
                elif seconds_since_last_trade > 5400 and seconds_since_last_trade <= 6600:
                    
                    if (    
                        ma50_last > ma50_2_min_ago
                        and deviation_ma39 < -0.22 
                        and deviation_sell < -0.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 90-110 min con ma50 > and deviation_ma39 <-0.22 and deviation_sell < -0.21 - r 4454"
                        action = "sell"
                        
                        
                       
                    elif (     
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma50_last 
                        and deviation_sell < -0.22
                        and ma25_last < ma25_2_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 90-110 min con ma50 > and ma3_last < ma50_last and deviation_sell < -0.22 and ma25 < - r 4466"
                        action = "sell"
                        
                    
                    
                    ################################################################################### fare maradona 1 ma3>ma100 (69) e maradona 2 ma3<ma100 (50)
                    
                    # MARADONA 1
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last > ma100_last
                        and ma5_last < ma69_last
                        and deviation_sell > 0.35 and deviation_sell < 0.64
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 90-110 min con ma50 > con 5-69 (!) and deviation_sell 0.35 - 0.64 la prima FINTA DI MARADONA 1 (non toccare) - r 4483"
                        action = "sell"
                        
                        
                        
                    # MARADONA 2
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma100_last
                        and ma5_last < ma50_last
                        and deviation_sell > 0.35 and deviation_sell < 0.64
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 90-110 min con ma50 > con 5-50 (!) and deviation_sell 0.35 - 0.64 la prima FINTA DI MARADONA 1 - r 4498"
                        action = "sell"
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma42_prev and ma5_last < ma42_last)
                        and deviation_sell > 0.65 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 90-110 min con ma50 > incrocio 5-42 (!) and deviation_sell 0.65 - 1.49 RABONA ALLA RONALDO - r 4511"
                        action = "sell"
                        
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 90-110 min con ma50 > incrocio 3-30 and deviation_sell  1.50 - 2.70 DOPPIO PASSO DI RONALDO - r 4523"
                        action = "sell"
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 2.71 and deviation_sell < 5.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 90-110 min con ma50 > incrocio 3-13 (!) and deviation_sell > 2.71 TACCO DI ALLAH - r 4536"
                        action = "sell"
                        
                        
                        
                
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma69_prev and ma3_last < ma69_last)
                        and deviation_sell > 5.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 90-110 min con ma50 > incrocio 3-69 (!) and deviation_sell > 5.71 SI STA TRA GLI ANGELI, compa ! - r 4549"
                        action = "sell"
                        
                    
                    
                    
                    ######################################################################################## con trend discendente
                    
                    # con or IL MAESTRO HA FATTO LA CORREZIONE ! questa che vedi e' stata corretta dal maestro
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.17
                        and deviation_sell > 0.20
                        and ma5_last < ma5_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 90-110 min con ma50 <  and ma100 < con deviation_ma39 <-0.17 - r 4567"
                        action = "sell"
                        
                        # ma39 non deve vendere laterale quindi per farlo vendere in alto ho dato 0.20
                        
                        
                 
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                        and deviation_sell < -0.15
                        and ma3_last < ma39_last
                        and ma100_last < ma100_60_min_ago
                    ):
                        sell = "SELL 1 90-110 min con ma50 < and ma100 < and (deviation_sell < -0.15 and ma3_last < ma39_last) - r 4581"
                        action = "sell"
                        
                        
                    
                    
                    # ma se ma100 >
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.20
                        and deviation_sell > 0.20
                        and ma5_last < ma5_2_min_ago
                        and ma100_last > ma100_60_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 90-110 min con ma50 < MA ma100 > con deviation_ma39 <-0.20 - r 4597"
                        action = "sell"
                        
                        # ma39 NON DEVE VENDERE in fase laterale ma in alto
                        
                        
                    
                    
                    # ma se ma100 > 
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        
                        and deviation_sell < -0.20
                        and ma3_last < ma39_last
                        and ma100_last > ma100_60_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 90-110 min con ma50 < MA ma100 > and (deviation_sell < -0.20 and ma3_last < ma39_last) - r 4615"
                        action = "sell"
                        
                    
                    
                    ############################################################################### aumento della perdita tollerata ! 50< MA 200> e 200>300
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                        and deviation_ma39 < -0.23
                        and deviation_trend_ma200 > -0.12
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 1 compa 90-110 min con ma50 < and deviation_ma39 < -0.23  con > PERDITA TOLLERATA - r 4631"
                        action = "sell"
                        
                    
                    
                    elif (     
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma39_last
                        and deviation_sell < -0.21
                        and ma2_last < ma2_2_min_ago
                        and deviation_trend_ma200 > -0.12
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 compa 90-110 min con ma50 < (deviation_sell < -0.21 and ma3_last < ma39_last) con > PERDITA TOLLERATA - r 4645"
                        action = "sell"
                        
                        
                    
                        
                ############################################################################################################################ SESSIONE 1 ( > 110 min )

                # VENDITA - da 110 minuti in poi = da 6601 secondi in poi

                elif seconds_since_last_trade > 6601:

                    
                    if (    
                        ma50_last > ma50_2_min_ago
                        and deviation_ma39 < -0.22 
                        and deviation_sell < -0.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 > and deviation_ma39 <-0.22 and deviation_sell < -0.21 - r 4664"
                        action = "sell"
                        
                        
                    
                    
                    elif (     
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma50_last 
                        and deviation_sell < -0.22
                        and ma25_last < ma25_2_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 > and ma3_last < ma50_last and deviation_sell < -0.22 and ma25 < - r 4677"
                        action = "sell"
                        
                    
                    
                    
                    ############################################################################# fare maradona 1 e maradona 2
                    
                    # MARADONA 1
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last > ma100_last
                        and ma5_last < ma69_last
                        and deviation_sell > 0.35 and deviation_sell < 0.64
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 > con 5-69 (!) and deviation_sell 0.35 - 0.64 la prima FINTA DI MARADONA 1 (non toccare) - r 4695"
                        action = "sell"
                        
                        
                    
                    # MARADONA 2
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma100_last
                        and ma5_last < ma50_last
                        and deviation_sell > 0.35 and deviation_sell < 0.64
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 > con 5-50 (!) and deviation_sell 0.35 - 0.64 la prima FINTA DI MARADONA 2  - r 4701"
                        action = "sell"
                        
                        
                    
                    
                    #################################################################################################
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma42_prev and ma5_last < ma42_last)
                        and deviation_sell > 0.65 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 > incrocio 5-42 (!) and deviation_sell 0.65 - 1.49 RABONA ALLA RONALDO - r 4725"
                        action = "sell"
                        
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 dopo 110 min con ma50 > incrocio 3-30 and deviation_sell  1.50 - 2.70 DOPPIO PASSO DI RONALDO - r 4737"
                        action = "sell"
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 2.71 and deviation_sell < 5.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 > incrocio 3-13 (!) and deviation_sell > 2.71 TACCO DI ALLAH - r 4749"
                        action = "sell"
                        
                
                
                
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma69_prev and ma3_last < ma69_last)
                        and deviation_sell > 5.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 dopo 110 min con ma50 > incrocio 3-69 (!) and deviation_sell > 5.71 SI STA TRA GLI ANGELI, compa ! - r 4762"
                        action = "sell"
                        
                    
                    
                    ######################################################################################## con trend discendente
                    
                    # con or IL MAESTRO HA FATTO LA CORREZIONE ! questa che vedi e' stata corretta dal maestro
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.17
                        and deviation_sell > 0.20
                        and ma5_last < ma5_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 <  and ma100 < con deviation_ma39 <-0.17 - r 4779"
                        action = "sell"
                        
                        # ma39 non deve vendere laterale (!) quindi per farlo vendere in alto ho dato 0.20
                        
                        
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                        and deviation_sell < -0.15
                        and ma3_last < ma39_last
                        and ma100_last < ma100_60_min_ago
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 < and ma100 < and (deviation_sell < -0.15 and ma3_last < ma39_last) - r 4794"
                        action = "sell"
                        
                        
                        
              
                    # ma se ma100 >
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.195
                        and deviation_sell > 0.20
                        and ma5_last < ma5_2_min_ago
                        and ma100_last > ma100_60_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 < MA ma100 > con deviation_ma39 <-0.195 - r 4810"
                        action = "sell"
                        
                        # ma39 NON DEVE VENDERE in fase laterale ma in alto
                        
                        
                    
                    
                    # ma se ma100 > 
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                        and deviation_sell < -0.18
                        and ma3_last < ma39_last
                        and ma100_last > ma100_60_min_ago
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 < MA ma100 > and (deviation_sell < -0.18 and ma3_last < ma39_last) - r 4827"
                        action = "sell"
                        
                    
                   
                    ############################################################################### aumento della perdita tollerata ! 50< MA 200> e 200>300
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                        and deviation_ma39 < -0.23
                        and deviation_trend_ma200 > -0.12
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 1 compa dopo 110 min con ma50 < and deviation_ma39 < -0.23  con > PERDITA TOLLERATA - r 4843"
                        action = "sell"
                        
                        
                    
                    elif (     
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma39_last
                        and deviation_sell < -0.21
                        and ma2_last < ma2_2_min_ago
                        and deviation_trend_ma200 > -0.12
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 compa dopo 110 min con ma50 < (deviation_sell < -0.21 and ma3_last < ma39_last) con > PERDITA TOLLERATA - r 4857"
                        action = "sell"
                        
                        
                        
                        
                    # ATTENZIONE ! > 110 min FORSE E' NECESSARA SOLO QUESTA !
                    
                    elif (    
                        ma3_last < ma100_last
                        and deviation_sell < -0.05
                        and ma2_last < ma2_2_min_ago
                    ):
                   
                        sell = "SELL 1 > 110 min FORSE E' NECESSARA SOLO QUESTA ! deviation_sell < -0.05 - r 4871"
                        action = "sell"
                        
         
        
            ################################################################################################# SESSIONE 1 ( vendita con questi 13 ALTRI MODI )
           
            
            # 1 - ro cano VENDE CON UN SALVAGENTE
               
            if deviation_ma39 < -0.25 and deviation < -0.36 and ma50_last > ma50_2_min_ago:

                sell = "SELL 1 SALVAGENTE 3-39 con ma50 < r 4883"
                action = "sell"
                        

                # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!
                    
                    
                    
            # 2 - ro cano VENDE DURANTE UN CROLLO IMPROVVISO ! che dava problemi quando il prezzo ! andava molto sopra ma4 durante un trend rialzista !
            # spero di aver risolto aggiungendo per precauzione queste altre 2 righe
                    
                    
            elif (    
                ma2_last < ma4_last
                and ma2_last < ma6_last
                and deviation  < -0.61
            ): 
                
                sell = "SELL 1 CROLLO IMPROVVISO - r 4901"
                action = "sell"
                        
                # deviation = ma4_last / last_trade_price
                # FORSE E' L' UNICA DEVIATION CHE MI POTRA' SALVARE DA UN CROLLO IMPROVVISO COME QUELLO DEL 3 NOVEMBRE 2021
                # -0.90 ha fatto fare una perdita di -1.46% il 19 dic 2021
                        
                        
                    
                    
            # vendita speciale dopo il crollo del 24 aprile
                    
            elif (    
                ma2_last < ma4_last
                and ma2_last < ma6_last
                and deviation_crollo_24_aprile < -0.58
            ): 
                
                sell = "SELL 1 CROLLO IMPROVVISO - r 4919"
                action = "sell"
                        
                # ho aggiunto anche questa vendita speciale dopo il 24 aprile -1%
                # deviation_crollo_24_aprile = ma2_last / last_trade_price - # r400
                        
                        

            # 3 - ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma13 >
                    
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and ma2_last < last_trade_price
                and deviation < -0.40
                and ma13_last > ma13_2_min_ago
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL 1 DOLCE ATTESA con ma13 > and deviation < -0.40 - r 4937"
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

                sell = "SELL 1 DOLCE ATTESA con ma13 < and deviation < -0.35 - r 4957"
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

                sell = "sessione 1 SELL TEMPO e se ma8 < ma50 and deviation_sell < -0.49 - r 4976"
                action = "sell"
                        
                # ma13 troppo lenta !
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                        
                        
                        
                    
            # 6 - RIBASSO IMPROVVISO
                    
            elif (
                ma78_last > ma78_2_min_ago
                and deviation_ribasso_improvviso < -0.61
            ):
                sell = "SELL 1 RIBASSO IMPROVVISO < -0.61 - r 4991"
                action = "sell"
                        
                        
                 
            # 7 - RIBASSO IMPROVVISO
                
            elif (
                ma78_last < ma78_2_min_ago
                and deviation_ribasso_improvviso < -0.59
            ):
                sell = "SELL 1 RIBASSO IMPROVVISO -0.59 - r 5002"
                action = "sell"
                        
                        
                    
                    
            # 8 - POCHI MALEDETTI E SUBITO con ma200 > MA ma100 NON DEVE SALIRE TROPPO ! - dedicated to comparo meo
                
            elif (
                        
                ma3_last < ma9_last
                and ma200_last > ma200_60_min_ago
                and deviation > 0.68
                and ma2_last < ma2_2_min_ago
                 
                and ma2_last > ma100_last
                        
                and deviation_trend_ma100 < 0.50
                and deviation_pochi_maledetti > 0.25
                        
            ):    
                sell = "SELL 1 POCHI MALEDETTI E SUBITO quando ma200 > e con deviation > 0.70 MA ma100 NON DEVE SALIRE TROPPO ! - r 5023"
                action = "sell"
                        
                # attenzione : le prime 4 righe sono uguali a RCCR che ha funzionato. le altre 3 non hanno fatto attivare questa condizione !
                # deviation_trend_ma100 = ma100_last / ma100_60_min_ago
                # deviation_pochi_maledetti = ma13_last / ma13_10_min_ago
                        
                # and ma2_last > ma100_last (altrimenti vende durante il crollo con la ma3-ma9)
                # incredibile questa and deviation_trend_ma100 < 1.00 - se ma100 sale "forte" da 60 min non deve intervenire sell 3-9
                        
                 
                
            # 9 - POCHI MALEDETTI E SUBITO con ma200 < - dedicated to comparo meo
                
            elif (
                ma3_last < ma9_last 
                and ma200_last < ma200_60_min_ago
                and deviation > 0.70
                and deviation_pochi_maledetti > 0.70
                and ma2_last > ma100_last
            ):    
                sell = "SELL 3-4-x POCHI MALEDETTI E SUBITO quando ma200 < e con deviation > 0.70 - dedicated to comparo meo - r 5044"
                action = "sell"
                    
                # and ma2_last > ma100_last (altrimenti vende durante il crollo con la ma3-ma9)
                        
                        
                
            ######################################################################### vendite dedicate al BUY FIAT - AUDI - MASERATI - FERRARI    
                        
            # 10 - SELL 1 FIAT 
                    
            elif (     
                seconds_since_last_trade > max_hold_time_in_seconds_fiat
                and deviation_buy_crollo_1 < -0.15
                and deviation_buy_crollo_1 > -0.59
                        
                and deviation_ma100_sopra_ma300 < -0.70
                and deviation < -0.29
            ):    
                 
                buy = "SELL 1 FIAT se > 20 min dal BUY FIAT la perdita e' < -0.29 ! - r 5064"
                action = "sell"
                        
                # and ma2_last < ma2_2_min_ago
                # and deviation_ma100_sopra_ma300 < -0.70 significa che c'e' un grande ribasso. 100 sta lontana da 300. 
                # EVITO COSI' PROBLEMI AL TREND LATERALE.
                        
                        
                        
                
            # 11 - SELL 1 AUDI 
                    
            elif (     
                seconds_since_last_trade > max_hold_time_in_seconds_audi
                and deviation_buy_crollo_1 < -0.60
                and deviation_buy_crollo_1 > -0.90
                        
                and deviation_ma100_sopra_ma300 < -0.70
                and deviation < -0.31
                        
            ):
                buy = "SELL 1 AUDI se > 20 min dal BUY AUDI la perdita e' < -0.31 - r 5085"
                action = "sell"
                        
                # and ma2_last < ma2_2_min_ago
                        
                        
               
            # 12 - SELL 1 MASERATI 
                    
            elif (     
                seconds_since_last_trade > max_hold_time_in_seconds_maserati
                and deviation_buy_crollo_1 < -0.91
                and deviation_buy_crollo_1 > -1.50
                      
                and deviation_ma100_sopra_ma300 < -0.70
                and deviation < -0.33
                        
            ):
                buy = "SELL 1 MASERATI se > 20 min dal BUY MASERATI la perdita e' < -0.33 - r 5103"
                action = "sell"
                        
                # and ma2_last < ma2_2_min_ago
                        
               
            
            
            # 13 - SELL 1 FERRARI 
                    
            elif (     
                seconds_since_last_trade > max_hold_time_in_seconds_ferrari
                and deviation_buy_crollo_1 < -1.51
                        
                and deviation_ma100_sopra_ma300 < -0.70
                and deviation < -0.37
            ):
                buy = "SELL 1 FERRARI se > 20 min dal BUY FERRARI la perdita e' < -0.37 - r 5120"
                action = "sell"
                        
                # and ma2_last < ma2_2_min_ago
                        
                        
                        
            
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
                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.23 - r 5147"
                        action = "sell"
                      
                    
               
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.25 - 0.60 FINTA DI MARADONA - r 5159"
                        action = "sell"
                        
                 
                
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.61 and deviation_sell < 0.79
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.61 - 0.79 DRIBBLING DI RONALDO - r 5171"
                        action = "sell"
                    
                    
                    
               
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 0.80 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell 0.80 - 1.20 DOPPIO PASSO ALLA RONALDO - r 5183"
                        action = "sell"
                  
                
                
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell > 1.21 (che sarebbe come IL DRIBBLING ALLA RONALDO !) - r 5195"
                        action = "sell"
                        
                        
                    
                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 < and incrocio 3-28 - r 5208"
                        action = "sell"
                        
                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                   
                
                
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 - r 5222"
                        action = "sell"
                        
                        
                        
               
                    # ---------------------------------------------------------------------------------------------------------------------- crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - r 5236"
                        action = "sell"
                        
                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - r 5249"
                        action = "sell"
                   
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                        and deviation_sell > 0.60
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - r 5261"
                        action = "sell"
                        
                        
                        
              
                ##################################################################################################################### SESSIONE 2 ( 3-5 min )

                # VENDITA - da 3 a 5 minuti = da 180 a 300 secondi

                elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 300:

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell < -0.25
                        and ma2_last < ma2_2_min_ago
                    ):  
                        sell = "SELL 2 (3-5 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.25 - r 5279"
                        action = "sell"
                        
                 
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                    ):  
                        sell = "SELL 2 (3-5 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 5290"
                        action = "sell"
                        
                        
                        
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.57 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 > and incrocio 3-15 and deviation_sell 0.57 - 1.20 - r 5302"
                        action = "sell"
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - r 5314"
                        action = "sell"
                        
                    
                    
                    
                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 < and incrocio 3-28 - r 5329"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        # deviation_sell_ma78 = ma3_last / ma78_last
                        
                        
                        
                  
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.23 - r 5344"
                        action = "sell"
                        
                        
                        

                    # ---------------------------------------------------------------------------------------------------------------------- guadagno con crollo
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 5359"
                        action = "sell"
                        
                   
                
                
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 5371"
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
                        sell = "SELL 2 (5-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - r 5391"
                        action = "sell"
                    
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.25
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - r 5403"
                        action = "sell"
                        
                        
                        
                   
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 5416"
                        action = "sell"
                        
                        
                        
                   
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma15_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 >  3 < 15 and deviation_sell 0.57 - 0.90 - DRIBBLING ALLA RONALDO - r 5429"
                        action = "sell"
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - r 5442"
                        action = "sell"
                        
                        
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - r 5454"
                        action = "sell"
                        
                        
                        
                        
                    ###########################################################################     trend in ribasso and ma200_last < ma300_last
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma300_last
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.31
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 < AND 200<300 and incrocio 3-28 and deviation_sell < -0.31 - r 5469"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        
                        
                  
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma300_last
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 < AND 200<300 and incrocio 3-100 (cuscino di sant' antonio) - r 5484"
                        action = "sell"
                        
                 
                
                
                    ###########################################################################     trend in ribasso MA ma200_last > ma300_last
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma300_last
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.35
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 < MA 200>300 and incrocio 3-28 and deviation_sell < -0.35 - r 5499"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                  
                
                
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma300_last
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.40
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 < MA 200>300 and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.40 - r 5514"
                        action = "sell"
                        
                        
                        
                   
                    # ------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 guadagno con crollo (5-12 min) con ma50 < and incrocio 3-23 - r 5528"
                        action = "sell"
                        
                        

                    # ------------------------------------------------------------------------------------------------------------ PARACADUTE crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.48
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.48 - r 5541"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                   
                
                
                ####################################################################################################################### SESSIONE 2 ( 12-21 min )

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
                        sell = "SELL 2 (12-21 min) con ma50 > and incrocio 3-69 and deviation sell -0.34 e vaffanculo ! - r 5564"
                        action = "sell"
                        
                        # and deviation_ma39 < -0.29 vendeva troppo presto
                        # ATTENZIONE "and (ma3_prev > ma39_prev and ma3_last < ma39_last)" con ma39 NON HA INCROCIATO
                        
                        
                        
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma100_prev and ma3_last < ma100_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.36 - r 5579"
                        action = "sell"
                        
                  
                
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and 5<25 and deviation_sell 0.25-0.56 - MARADONA - r 5592"
                        action = "sell"
                        
                       
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma25_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and 3<25 and deviation_sell 0.57-0.90 - DOPPIO PASSO ALLA RONALDO fino a +0.50 - r 5605"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and incrocio 3-15 and deviation_sell 0.91 - 1.20 - r 5620"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and incrocio 3-13 and deviation_sell > 1.21 - r 5634"
                        action = "sell"
                        
                        

                    ##########################################################################################
                    # NON TOCCARE ! CUSCINO DI SANT' ANTONIO !
                    # L' INCROCIO 5-100 MI SALVA ! MA, attenzione, 5<100 VENDE DURANTE IL RIBASSO !
                    ########################################################################################### con trend discendente

                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.195
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 < and deviation_ma39 < -0.195 - r 5650"
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
                        sell = "SELL 2 (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - r 5670"
                        action = "sell"
                        
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50< ! 
                        
                        
                       

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.28
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - r 5684"
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
                        sell = "SELL 2 PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 5701"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                        
                        
                    # ----------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma4_prev > ma20_prev and ma4_last < ma20_last)
                        and deviation_sell > 0.22
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 4 - 20 and deviation_sell > 0.22 - r 5717"
                        action = "sell"
                        
            
            
            
                ############################################################################################################## SESSIONE 2 ( 21-60 min )

                # VENDITA - da 21 a 60 minuti = da 1261 a 3600 secondi
                
                
                elif (
                    seconds_since_last_trade > 1261 and seconds_since_last_trade <= 3600
                ):
                    
                
                    ######################################################################################################## 2 righe compa RADDOPPIATE !
                    
                    if (        
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.25
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and deviation_ma39 < -0.25 - r 5741"
                        action = "sell"
                        
                        
                        
                
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.28 
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and (deviation_sell < -0.28 and ma3_last < ma50_last) - r 5754"
                        action = "sell"
                        
                    
                    
                    
                    elif (        
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.29
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and deviation_ma39 < -0.29 - TOLLERANTE ! - r 5766"
                        action = "sell"
                        
                  
                
                    
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.29 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and (deviation_sell < -0.29 and ma3_last < ma50_last) TOLLERANTE ! - r 5779"
                        action = "sell"
                        
                        
                        
                        
                    ##############################################################################################################################
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.26
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.26 - r 5795"
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
                        sell = "SELL 2 (21-60 min) con ma50 > and 5<39 and deviation_sell 0.25 - 0.56 MARADONA e' piu' stanco e paziente - r 5813"
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
                        sell = "SELL 2 (21-60 min) con ma50 > AND 200>120 min and 5<69 (fidati!) and deviation_sell 0.57 - 0.90 ELASTICO ALLA RONALDO - r 5835"
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
                        sell = "SELL 2 (21-60 min) con ma50 > AND 200>120min and 3<25 and deviation_sell 0.57 - 0.90 ELASTICO ALLA RONALDO - r 5853"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    
                    ##############################################################################################################
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                   
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and incrocio 3-16 and deviation_sell 0.91 - 1.20 - r 5870"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.21 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and incrocio 3-30 (!) SI PROPRIO COSI' ! 3-30 ! and deviation_sell 1.21 - 2.70 - r 5883"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "sessione 2 SELL (21-60 min) con ma50 > and incrocio 3-11 and deviation_sell > 2.71 - r 5894"
                        action = "sell"
                        

                        
                    #################################################################################################### con trend discendente
                    #################################################################################################### 2 righe del compa GIA' CON TOLLERANZA
                    
                    
                    elif (        
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.27
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "sessione 2 SELL (21-60 min) con ma50 < and deviation_ma39 < -0.27 - r 5909"
                        action = "sell"
                        
                  
                    
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.30
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "sessione 2 SELL (21-60 min) con ma50 < and deviation_sell < -0.30 - r 5920"
                        action = "sell"
                        
                        
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_60_min_ago
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.37
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "sessione 2 SELL (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - r 5933"
                        action = "sell"
                        
                        
                   
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_60_min_ago
                        
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "sessione 2 SELL (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - r 5947"
                        action = "sell"
                        
                        
                      
                    
                    ################################################################################################################# con > PERDITA TOLLERATA !
                    
                    # ATTENZIONE ! AUMENTA LA PERDITA TOLLERATA  ! PERCHE' ma200 sale e perche' ma200 > ma300
                    
                    
                    # divido in 2 parti la correzione del maestro !
                    
                    elif (
                        
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.29
                        and ma200_last > ma200_60_min_ago
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                    
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 < and deviation_ma39 < -0.29   con > PERDITA TOLLERATA ! - r 5970"
                        action = "sell"
                        
                        
                 
                    elif (  
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.35
                        and ma200_last > ma200_60_min_ago
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                     
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 < and deviation_sell < -0.35 con > PERDITA TOLLERATA ! - r 5984"
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
                        sell = "SELL 2 (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.40 con > PERDITA TOLLERATA ! - r 5999"
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
                        sell = "SELL 2 (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO con > PERDITA TOLLERATA ! - r 6014"
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
                        sell = "SELL 2 eventuale guadagno durante il crollo (21-60 min) con ma50 < incrocio 3 - 18 and deviation_sell > 0.23 - r 6032"
                        action = "sell"
                        
                
                
                
                
                #################################################################################################################### SESSIONE 2 ( da 60 a 90 min )

                # VENDITA - da 60 a 90 min - da 3600 a 5400 secondi in poi
                
                elif (
                    seconds_since_last_trade > 3600 and seconds_since_last_trade <= 5400
                ):
                    
                  
                    ################################################################### RIGHE DEL COMPA DA RADDOPPIARE PER AUMENTO TOLLERANZA
                    
                    if (    
                        ma50_last > ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 > and deviation_ma39 < -0.18 - r 6055"
                        action = "sell"
                        
                        
               
                    elif (      
                        ma50_last > ma50_2_min_ago
                        and deviation_sell < -0.18
                        and ma3_last < ma50_last
                        and ma2_last < ma2_2_min_ago 
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 > and (deviation_sell < -0.18 and ma3_last < ma50_last)  - r 6066"
                        action = "sell"
                        
                        
                    
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and deviation_ma39 < -0.22
                        and ma2_last < ma2_2_min_ago
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 > and deviation_ma39 <-0.22 - r 6077"
                        action = "sell"
                        
                        
                  
                    elif (      
                        ma50_last > ma50_2_min_ago
                        and deviation_sell < -0.21
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 > and (deviation_sell < -0.21 and ma3_last < ma50_last)  - r 6089"
                        action = "sell"
                        
                       
                    
                    
                        ##################################################################################################################### 
                     
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma50_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and 5-50 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 6105"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma4_prev > ma25_prev and ma4_last < ma25_last)
                        and deviation_sell > 0.57 and deviation_sell < 0.80
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 >60 min con ma50> and incrocio 4-25 and deviation_sell 0.57-0.80 FINTA ALLA RONALDO - r 6119"
                        action = "sell"
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.81 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 da 60 a 90 min con ma50 > and incrocio 3-18 and deviation_sell 0.81 - 1.49 RABONA ALLA RONALDO - r 6132"
                        action = "sell"

                        # ma ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 da 60 a 90 min con ma50 > incrocio 3-13 and deviation_sell 1.50 - 2.70 DOPPIO PASSO ALLA RONALDO - r 6147"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 da 60 a 90 min con ma50 > incrocio 3-11 and deviation_sell > 2.71 STIAMO TRA GLI ANGELI, compa ! - r 6160"
                        action = "sell"
                        
                        
                    
                    ######################################################################################## trend discendente con PERDITA BASE
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        
                        and deviation_ma39 < -0.17
                        and deviation_sell < 0.10
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min TREND < con PERDITA BASE con ma50 < con deviation_ma39 <-0.17 and deviation_sell < 0.10 - r 6176"
                        action = "sell"
                        
                        # and ma3_last < ma39_last
                        # and deviation_sell < 0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare ! POI STIAMO GIA' AL SELL 2 -le ma hanno avuto piu' tempo di salire
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # cuscino dell' angelo custode
                        
                    
                    

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.13
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 TREND < con PERDITA BASE da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < -0.13 - r 6195"
                        action = "sell"
                        
                        
                        
                        
                        
                    ######################################################################################## trend discendente con POCA PERDITA TOLLERATA  
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last > ma100_60_min_ago
                        and deviation_ma39 < -0.18
                        and deviation_sell < 0.05
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min TREND < con POCA PERDITA TOLLERATA con ma50 < con deviation_ma39 <-0.17 and deviation_sell < 0.05 - r 6212"
                        action = "sell"
                        
                        # and ma3_last < ma39_last
                        # and deviation_sell < 0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare ! POI STIAMO GIA' AL SELL 2 -le ma hanno avuto piu' tempo di salire
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # cuscino dell' angelo custode
                        
                    
                    

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last > ma100_60_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.14
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con POCA PERDITA TOLLERATA con ma50 < con incrocio 3-78 and deviation_sell < -0.14 - r 6231"
                        action = "sell"
                        
                        
                     
                    ################################################################################## trend discendente con MOLTA PERDITA TOLLERATA
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.19
                        
                        and deviation_trend_ma200 > -0.12
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con MOLTA PERDITA TOLLERATA con ma50 < con deviation_ma39 < -0.19 - r 6246"
                        action = "sell"
                        
                        # and ma3_last < ma33_last
                        # and deviation_sell < 0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # cuscino dell' angelo custode
                        
                    
                    

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.15
                        
                        and deviation_trend_ma200 > -0.12
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con MOLTA PERDITA TOLLERATA con ma50 < con incrocio 3-78 and deviation_sell < -0.15 - r 6267"
                        action = "sell"
                        
                    
                
                
                ######################################################################################################### SESSIONE 2 ( da 90 min a 110 min )
                
                # VENDITA 2 - da 90 minuti a 110 minuti = da 5400 secondi a 6600 secondi
                
                elif seconds_since_last_trade > 5400 and seconds_since_last_trade <= 6600:    
                    
                    ###################################################################################   RIGHE DEL COMPA raddoppiate PER AUMENTO TOLLERANZA
                    
                    
                    if (  
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.22
                        and ma200_last > ma200_60_min_ago
                    ):    
                        sell = "SELL 2 90-110 min con ma50 > and deviation_ma39 <-0.22 (no ma3<ma39) - r 6288"
                        action = "sell"
                        
                   
                
                    elif (      
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.21 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 2 90-110 min con ma50 > and (deviation_sell < 0.21 and ma3_last < ma50_last) - r 6300"
                        action = "sell"
                        
                        
                        
                        
                    elif (  
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.23
                        and ma200_last < ma200_60_min_ago
                    ):    
                        sell = "SELL 2 90-110 min con ma50 > and deviation_ma39 < -0.23 - r 6312"
                        action = "sell"
                        
                        
                        
                   
                    elif (      
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.22 
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 2 90-110 min con ma50 > and (deviation_sell < -0.22 and ma3_last < ma50_last) - r 6325"
                        action = "sell"
                        
                        
                        
                    #########################################################################################################
                   
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma50_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 90-110 min con ma50 > and 5-50 (!) and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA (non toccare) - r 6340"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                     
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 90-110 min con ma50 > con 4-20 and deviation_sell 0.57-0.90 DRIBBLING ALLA RONALDO - r 6354"
                        action = "sell"
                        
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 90-110 min con ma50 > incrocio 3-15 and deviation_sell 0.91 - 1.49 - r 6367"
                        action = "sell"

                        # ma 3-48 mi evita la ricompra e la rivendita con perdita !
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 90-110 min con ma50 > incrocio 3-13 and deviation_sell 1.50 - 2.70 - r 6382"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 90-110 min con ma50 > incrocio 3-11 (!) and deviation_sell > 2.71 - r 6394"
                        action = "sell"
                        
                        
                        

                    ######################################################################################## con trend discendente
                    
                    
                    elif (  
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.25
                        and deviation_trend_ma100 > 0.10
                    ):
                        sell = "SELL 2 90-110 min con ma50 < MA ma100 > con deviation_ma39 <-0.25 - r 6409"
                        action = "sell"
                        
              
                    
                
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.20 
                        and ma3_last < ma39_last
                        and deviation_trend_ma100 > 0.10
                    ):
                        sell = "SELL 2 90-110 min con ma50 < MA ma100 > and (deviation_sell < -0.20 and ma3_last < ma39_last) - r 6422"
                        action = "sell"
                        
                  
                
                        
                    elif (  
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.22
                        and deviation_trend_ma100 < 0.10
                    ):
                        sell = "SELL 2 90-110 min con ma50 < MA ma100 < con deviation_ma39 <-0.22 - r 6434"
                        action = "sell"
                        
                        
                
                 
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.18 
                        and ma3_last < ma39_last
                        and deviation_trend_ma100 < 0.10
                    ):
                        sell = "SELL 2 90-110 min con ma50 < MA ma100 < and (deviation_sell < -0.18 and ma3_last < ma39_last) - r 6447"
                        action = "sell"
                        
                    
                    
                    
                    ########################################################################################## AUMENTA PERDITA TOLLERATA e divido in 2 il compa
                    
                    
                    elif (  
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.24
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 compa 90-110 min  con ma50 < con deviation_ma39 <-0.24 con > PERDITA TOLLERATA - r 6464"
                        action = "sell"
                        
                        
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.24 
                        and ma3_last < ma39_last
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 compa 90-110 min con ma50 < (deviation_sell < -0.24 and ma3_last < ma39_last) con > PERDITA TOLLERATA - r 6479"
                        action = "sell"
                        
                        
                 
                ##########################################################################################################
                
                # VENDITA 2 - da 110 minuti in poi = da 6601 secondi in poi

                elif seconds_since_last_trade > 6601:
                    
                    
                    ###################################################################################   RIGHE DEL COMPA raddoppiate PER AUMENTO TOLLERANZA
                    
                    
                    if (  
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.22
                        and ma200_last > ma200_60_min_ago
                    ):    
                        sell = "SELL 2 dopo 110 min con ma50 > and deviation_ma39 <-0.22 (no ma3<ma39) - r 6500"
                        action = "sell"
                        
                   
                
                    elif (      
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.21 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "sessione 2 SELL dopo 110 min con ma50 > and (deviation_sell < 0.21 and ma3_last < ma50_last) - r 6512"
                        action = "sell"
                        
                        
                        
                        
                    elif (  
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.23
                        and ma200_last < ma200_60_min_ago
                    ):    
                        sell = "sessione 2 SELL 2 dopo 110 min con ma50 > and deviation_ma39 < -0.23 - r 6524"
                        action = "sell"
                        
                   
                
                
                    elif (      
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.22 
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "sessione 2 SELL dopo 110 min con ma50 > and (deviation_sell < -0.22 and ma3_last < ma50_last) - r 6537"
                        action = "sell"
                        
                        
                        
                        
                    ################################################################################### fare maradona 1 e maradona 2 se ma2 sta sopra ma100
                   
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma50_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 dopo 110 min con ma50 > and 5-50 (!) and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA (non toccare) - r 6553"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                     
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 > 110 min con ma50 > con 4-20 and deviation_sell 0.57-0.90 DRIBBLING ALLA RONALDO - r 6567"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 dopo 110 min con ma50 > incrocio 3-15 and deviation_sell 0.91 - 1.49 - r 6580"
                        action = "sell"

                        # ma 3-48 mi evita la ricompra e la rivendita con perdita !
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 dopo 110 min con ma50 > incrocio 3-13 and deviation_sell 1.50 - 2.70 - r 6595"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 dopo 110 min con ma50 > incrocio 3-11 (!) and deviation_sell > 2.71 - r 6607"
                        action = "sell"
                        
                        

                    ######################################################################################## con trend discendente
                    
                    
                    elif (  
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.25
                        and deviation_trend_ma100 > 0.10
                    ):
                        sell = "SELL 2 dopo 110 min con ma50 < MA ma100 > con deviation_ma39 <-0.25 - r 6621"
                        action = "sell"
                        
              
                    
                
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.20 
                        and ma3_last < ma39_last
                        and deviation_trend_ma100 > 0.10
                    ):
                        sell = "SELL 2 dopo 110 min con ma50 < MA ma100 > and (deviation_sell < -0.20 and ma3_last < ma39_last) - r 6634"
                        action = "sell"
                        
                  
                        
                    
                    elif (  
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.22
                        and deviation_trend_ma100 < 0.10
                    ):
                        sell = "SELL 2 dopo 110 min con ma50 < MA ma100 < con deviation_ma39 <-0.22 - r 6646"
                        action = "sell"
                        
                        
                
                 
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.18 
                        and ma3_last < ma39_last
                        and deviation_trend_ma100 < 0.10
                    ):
                        sell = "SELL 2 dopo 110 min con ma50 < MA ma100 < and (deviation_sell < -0.18 and ma3_last < ma39_last) - r 6659"
                        action = "sell"
                        
                    
                    
                    
                    ########################################################################################## AUMENTA PERDITA TOLLERATA e divido in 2 il compa
                    
                    
                    elif (  
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.24
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 compa dopo 110 min con ma50 < con deviation_ma39 <-0.24 con > PERDITA TOLLERATA - r 6676"
                        action = "sell"
                        
                        
                    
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.24 
                        and ma3_last < ma39_last
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 compa dopo 110 min con ma50 < (deviation_sell < -0.24 and ma3_last < ma39_last) con > PERDITA TOLLERATA - r 6690"
                        action = "sell"
                        
                        
                        
                        
                    # ATTENZIONE : DOPO 110 MIN forse E' NECESSARIA SOLO QUESTA !
                    
                    elif (    
                        ma3_last < ma100_last
                        and deviation_sell < 0.05
                        and ma2_last < ma2_2_min_ago
                    ):
                   
                        sell = "SELL 2 > 110 min forse E' NECESSARA SOLO QUESTA ! - r 6704"
                        action = "sell"
                    
                        
                    
                    

                    ############################################################################################ sessione 2  (vendita con questi 11 altri modi)
                    ############################################################################################
                    ############################################################################################
                    
                    # MA ATTENZIONE al conflitto durante il crollo - SELL SOVRAPPOSTO AL BUY

                    # NO 3<78 !
                    # NO deviation 78 !
                    # QUALCHE VOLTA ma3-ma39 NON HANNO INCROCIATO allora per la vendita con il DRIBBLING e il DOPPIO PASSO ALLA RONALDO ho risolto con 3<39
                    # il CUSCINO DELL' ANGELO CUSTODE e di SANT' ANTONIO mi proteggono ! (vendita con medie lunghe)
                    

                    # 1 - ro cano VENDE CON UN SALVAGENTE
            
                    if deviation_ma39 < -0.25 and deviation < -0.36 and ma50_last > ma50_2_min_ago:

                        sell = "SELL 2 SALVAGENTE 3-39 con ma50 < - r 6727"
                        action = "sell"

                        # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!
                        
                        
                        

                    # 2 - ro cano VENDE DURANTE UN CROLLO IMPROVVISO !
                    
                    elif (
                        ma2_last < ma4_last
                        and ma2_last < ma6_last
                        and deviation < -0.62
                 
                    ):    
                        
                        sell = "SELL 2 CROLLO IMPROVVISO - r 6744"
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

                        sell = "SELL 2 DOLCE ATTESA con ma13 > and deviation < -0.40 - r 6765"
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

                        sell = "SELL 2 DOLCE ATTESA con ma13 < and deviation < -0.36 - r 6785"
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

                        sell = "SELL 2 TEMPO e se ma8 < ma50 and deviation_sell < -0.49 - r 6805"
                        action = "sell"
                        
                        # ma13 troppo lenta !
                        # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                        
                        
                        
                        
                
                    # 6 POCHI MALEDETTI E SUBITO ma solo con 200 > and...
                    
                    elif (
                        
                        ma3_last < ma9_last
                        and ma200_last > ma200_60_min_ago
                        and deviation > 0.68
                        and ma2_last < ma2_2_min_ago
                 
                        and ma2_last > ma100_last
                        
                        and deviation_pochi_maledetti > 0.25
                        and deviation_trend_ma100 < 0.50
                    ):    
                        sell = "SELL 2 POCHI MALEDETTI E SUBITO quando ma200 > e con deviation > 0.70 MA ma100 NON DEVE SALIRE TROPPO ! - r 6829"
                        action = "sell"
                        
                        # attenzione : le prime 4 righe sono uguali a RCCR che ha funzionato. le altre 3 non hanno fatto attivare questa condizione !
                        
                        # and ma2_last > ma100_last (altrimenti vende durante il crollo con la ma3-ma9)
                        # incredibile questa and deviation_trend_ma100 < 1.00 - se ma100 sale "forte" da 60 min non deve intervenire sell 3-9
                        
                        
                        
                        
                    # 6 - RIBASSO IMPROVVISO - attenzione! ma2 arriva tardi !
            
                    elif (
                        ma78_last > ma78_2_min_ago
                        and deviation_ribasso_improvviso < -0.63
                    ):   
                 
                        sell = "SELL 2 RIBASSO IMPROVVISO - r 6847"
                        action = "sell"
                    
            
                    
                
                    # 7 - RIBASSO IMPROVVISO attenzione! ma2 arriva tardi !
            
                    elif (
                        ma78_last < ma78_2_min_ago
                        and deviation_ribasso_improvviso < -0.63
                
                    ):
       
                        sell = "SELL 2 RIBASSO IMPROVVISO - r 6861"
                        action = "sell"
            
            
            
                    ######################################################################### vendite dedicate al BUY FIAT - AUDI - MASERATI - FERRARI    
                        
                    # 8 - SELL 2 FIAT 
                    
                    elif (     
                        seconds_since_last_trade > max_hold_time_in_seconds_fiat
                        and deviation_buy_crollo_1 < -0.33
                        and deviation_buy_crollo_1 > -0.59
                        and deviation < -0.30
                        and ma2_last < ma2_2_min_ago
                    
                    ):    
                        buy = "SELL 2 FIAT se > 20 min dal BUY FIAT la perdita e' < -0.30 - r 6878"
                        action = "sell"
                        
                        
                        
                        
                    # 9 - SELL 2 AUDI 
                    
                    elif (     
                        seconds_since_last_trade > max_hold_time_in_seconds_audi
                        and deviation_buy_crollo_1 < -0.60
                        and deviation_buy_crollo_1 > -0.90
                        and deviation < -0.35
                        and ma2_last < ma2_2_min_ago
                    
                    ):    
                        buy = "SELL 2 AUDI se > 20 min dal BUY AUDI la perdita e' < -0.35 - r 6894"
                        action = "sell"
                        
                        
                        
                        
                    # 10 - SELL 2 
                    
                    elif (     
                        seconds_since_last_trade > max_hold_time_in_seconds_maserati
                        and deviation_buy_crollo_1 < -0.91
                        and deviation_buy_crollo_1 > -1.50
                        and deviation < -0.40
                        and ma2_last < ma2_2_min_ago
                    
                    ):    
                        buy = "SELL 2 MASERATI se > 20 min dal BUY MASERATI la perdita e' < -0.40 - r 6910"
                        action = "sell"
                        
                        
                        
                        
                    # 11 - SELL 2 
                    
                    elif (     
                        seconds_since_last_trade > max_hold_time_in_seconds_ferrari
                        and deviation_buy_crollo_1 < -1.51
                        and deviation < -0.45
                        and ma2_last < ma2_2_min_ago
                    
                    ):    
                        buy = "SELL 2 FERRARI se > 20 min dal BUY FERRARI la perdita e' < -0.45 - r 6925"
                        action = "sell"
                        
                        
                        
                      
                        
                        # OGGI 5 APRILE 2022
                        
            #    
                        
            
            ###################################################################################################
            ################################################################################################### SESSIONE 3
            
            elif self.session == 3:
                
                ################################################################################################### sessione 3 ( 0-3 min )
                
                if seconds_since_last_trade > 0 and seconds_since_last_trade <= 180:

                    # con ma50 >

                    if (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma18_last
                        and deviation_sell < -0.33
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 3 (0-3 min) con ma50 > and 3<18 and deviation_sell < -0.33 - r 6955"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                     
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma25_prev and ma5_last < ma25_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 3 (0-3 min) con ma50 > and incrocio 5-25 and deviation_sell 0.25 - 0.60 MARADONA - r 6969"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.61 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (0-3 min) con ma50 > and incrocio 3-15 and deviation_sell 0.61 - 0.90 RONALDO - r 6983"
                        action = "sell"
                        
                        
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell 0.91 - 1.20 - r 6996"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell > 1.21 (che sarebbe come IL DRIBBLING ALLA RONALDO !) - r 7009"
                        action = "sell"
                        
                        
                        

                    ###########################################################################     trend in ribasso
                    

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (0-3 min) con ma50 < and incrocio 3-28 - r 7024"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 - r 7038"
                        action = "sell"
                        
                        

                    # ---------------------------------------------------------------------------------------------------------------------- crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - r 7051"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - r 7065"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                        and deviation_sell > 0.60
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - r 7078"
                        action = "sell"
                        
               
                ######################################################################################### sessione 3-4-x ( 3-5 min  cambiata con 3-7 min )

                # VENDITA - da 3 a 7 minuti = da 180 a 420 secondi

                elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 420:
                    

                    if (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma18_last
                        and deviation_sell < -0.335
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 > and 3 < 18 and deviation_sell < -0.335 - r 7095"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 7110"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 > and 5<20 (no incrocio 3-9) and deviation_sell 0.57 - 0.90 - DRIBBLING ALLA RONALDO - r 7125"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - r 7139"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - r 7151"
                        action = "sell"
                        
                  
                    ###########################################################################     trend in ribasso
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 < and incrocio 3-28 - r 7164"
                        action = "sell"
                        
                        # deviation_sell_ma78 = ma3_last / ma78_last
                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.23 - r 7178"
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
                        sell = "SELL 3 (3-5 min) con ma50 < and incrocio 3-28 con > PERDITA TOLLERATA - r 7197"
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
                        sell = "SELL 3 (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.23 con > PERDITA TOLLERATA - r 7215"
                        action = "sell"
                        
                       

                    # -------------------------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - r 7228"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 7239"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                        

                ############################################################################### sessione 3-4-x  (5-12 min) ( cambiata con 7-12 min ! )

                # VENDITA - da 7 a 12 minuti = da 4200 a 720 secondi

                elif seconds_since_last_trade > 420 and seconds_since_last_trade <= 720:

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.41
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - r 7259"
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
                        sell = "SELL 3 (5-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - r 7275"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 7290"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                  
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 >  5<20 and deviation_sell 0.57 - 0.90 - DRIBBLING ALLA RONALDO - r 7305"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma20_prev and ma5_last < ma20_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 > and incrocio 5-20 and deviation_sell 0.91 - 1.20 - r 7320"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - r 7334"
                        action = "sell"
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 < and incrocio 3-28 - r 7347"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 < and incrocio 3-100 (cuscino di sant' antonio) - r 7361"
                        action = "sell"
                        
                        
                        

                    # ------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 guadagno con crollo (5-12 min) con ma50 < and incrocio 3-23 - r 7375"
                        action = "sell"
                        
                        

                    # ------------------------------------------------------------------------------------------------------------ PARACADUTE crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.48
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.48 - r 7388"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                        
                
                ####################################################################################################### sessione 3-4-x ( 12-21 min )

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
                        sell = "SELL 3 (12-21 min) con ma50 > and incrocio 3-72 and deviation sell -0.35 e vaffanculo ! - r 7410"
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
                        sell = "SELL 3 (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.36 - r 7427"
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
                        sell = "SELL 3 (12-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.54 - FINTA ALLA MARADONA - r 7446"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma20_last
                        and deviation_sell > 0.55 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and 5-20 and deviation_sell 0.55-0.90 - DOPPIO PASSO ALLA RONALDO - r 7461"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and incrocio 3-20 and deviation_sell 0.91 - 1.20 - r 7476"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                       
                    

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and incrocio 3-30 and deviation_sell > 1.21 - r 7490"
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
                        sell = "SELL 3 (12-21 min) con ma50 < and deviation_ma39 < -0.165 - r 7509"
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
                        sell = "SELL 3 (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - r 7528"
                        action = "sell"
                        
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50< !
                        
                    

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - r 7542"
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
                        sell = "SELL 3 (12-21 min) con ma50 < and deviation_ma39 < -0.185 con > PERDITA TOLLERATA - r 7561"
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
                        sell = "SELL 3 (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.47 con > PERDITA TOLLERATA - r 7583"
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
                        sell = "SELL 3 (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO con > PERDITA TOLLERATA - r 7600"
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
                        sell = "SELL 3 PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 7617"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                    
                    
                    
                    # ----------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3 - 18 and deviation_sell > 0.23 - r 7633"
                        action = "sell"
                        
                        
                        
                        

                ################################################################################################################## sessione 3-4-x ( 21-60 min )

                # VENDITA - da 21 a 60 minuti = da 1261 a 3600 secondi

                elif (
                    seconds_since_last_trade > 1261 and seconds_since_last_trade <= 3600
                ):
                    
                    
                    ################################################################################################ RIGHE DEL COMPA raddoppiate
                    
                    if (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.25
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and deviation_ma25 < -0.25 - r 7657"
                        action = "sell"
                        
                    
                    
                    
                    elif (      
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.25 
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL (21-60 min) con ma50 > and (deviation_sell < -0.25 and ma3_last < ma50_last) - r 7670"
                        action = "sell"
                        
                        
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.28
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and deviation_ma25 < -0.28 - r 7682"
                        action = "sell"
                        
                    
                    
                    
                    elif (      
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.27 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and (deviation_sell < -0.27 and ma3_last < ma50_last) - r 7695"
                        action = "sell"
                        
                       
                    
                    
                        ##################################################################################################################
                        
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.26
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.26 - r 7710"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma30_prev and ma5_last < ma30_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                   
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 5-30 and deviation_sell 0.25 - 0.56 FINTA DI MARADONA - r 7725"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma5_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and 5 < 20 and deviation_sell 0.57 - 0.90 ELASTICO ALLA RONALDO - r 7740"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 3-30 and deviation_sell 0.91 - 1.20 - r 7756"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.21 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 3-30 and deviation_sell 1.21 -2.70 - r 7770"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 3-11 and deviation_sell > 2.71 - r 7782"
                        action = "sell"
                    
                    
                   
                    ##################################################################### con trend discendente
                   
                    
                    elif (     
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.23
                        
                        and deviation_ma100_sopra_ma300 > 0.69
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and deviation_ma39 < -0.23 - r 7797"
                        action = "sell"
                        
                        # attenzione se ma100 sta molto sopra ma 300 basta deviation ma39
                        # ma se trend laterale metto anche una deviation sell ( vedi prossimo elif )
                        
                    
                    
                    elif (     
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.23
                        
                        and deviation_ma100_sopra_ma300 < 0.69
                        and deviation_sell < -0.15
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and deviation_ma39 < -0.23 - r 7813"
                        action = "sell"
                        
                        # attenzione se ma100 sta molto sopra ma 300 basta deviation ma39
                        # ma se trend laterale metto anche una deviation sell
                        
                        
                    
                    
                   
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.28
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and deviation_sell < -0.28 - r 7828"
                        action = "sell"
                        
                     
                    

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.37
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - r 7840"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - r 7853"
                        action = "sell"
                        
                        # viva sant' antonio !
                        # NON INCROCERANNO MAI DURANTE IL CROLLO !
                        # non toccare ! INCROCIO 3-100 CUSCINO DI SANT' ANTONIO !
                        
                    
                        
                        
                        
                    ####################################################################################################  aumento perdita tollerata se....  
                    
                    # divido il maestro in 2
                    
                    
                    elif (  
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.26
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                       
                    ):
                        sell = "SELL 3 compa (21-60 min) con ma50 < and deviation_ma39 < -0.26 con PERDITA TOLLERATA > - r 7877"
                        action = "sell"
                        
                        
                     
                    
                    elif ( 
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.29
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                    ):
                        sell = "SELL 3 compa (21-60 min) con ma50 < and deviation_sell < 0.29 con PERDITA TOLLERATA > - r 7890"
                        action = "sell"
                        
                        
                        
                    
                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.39
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.39 con > perdita tollerata - r 7904"
                        action = "sell"
                        
                        
                        
                        

                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - con > perdita tollerata - r 7920"
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
                        sell = "SELL 3 eventuale guadagno durante il crollo (21-60 min) con ma50 < incrocio 3 - 18 and deviation_sell > 0.23 - r 7937"
                        action = "sell"
                        
                        
                        
                        

                ######################################################################################################## sessione 3-4-x ( da 60 a 90 min )

                # VENDITA - da 60 a 90 min - da 3600 a 5400 secondi in poi
                
                elif (
                    seconds_since_last_trade > 3600 and seconds_since_last_trade <= 5400
                ):
                  
                
                
                ###################################################################### RIGHE DEL COMPA DA RADDOPPIAte PER AUMENTARE LA TOLLERANZA
                    
                    
                    if (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.21
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 > and deviation_ma25 < -0.19 - r 7963"
                        action = "sell"
                        
                        
                        
                    
                    
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.20 
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 > and (deviation_sell < -0.19 and ma3_last < ma50_last) - r 7977"
                        action = "sell"
                        
                        
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago
                        and deviation_ma25 < -0.21
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 > and deviation_ma25 < -0.19 - r 7989"
                        action = "sell"
                        
                        
                        
                    
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.20 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 > and (deviation_sell < -0.19 and ma3_last < ma50_last) - r 8002"
                        action = "sell"
                        
                        
                        
                        ############################################################################################################
                        
                        
                     
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma50_prev and ma5_last < ma50_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 5-50 and deviation_sell 0.25 - 0.56 FINTA DI MARADONA - r 8018"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 >60 min con ma50> and 4-20 and deviation_sell 0.57-0.90 DRIBBLING ALLA RONALDO - r 8032"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 da 60 a 90 min con ma50 > and incrocio 3-30 and deviation_sell 0.91 - 1.49 - r 8045"
                        action = "sell"

                        # ma ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                        
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 da 60 a 90 min con ma50 > incrocio 3-20 and deviation_sell 1.50 - 2.70 - r 8061"
                        action = "sell"
                        
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 da 60 a 90 min con ma50 > incrocio 3-11 and deviation_sell > 2.71 - r 8075"
                        action = "sell"
                        
                        
                       
                    ############################################################################# con trend discendente MA 100 sopra di molto da 300
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.16
                        and ma2_last < ma2_2_min_ago
                        
                        and deviation_ma100_sopra_ma300 > 0.69
                       
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 < con deviation_ma39 <-0.16 TREND CRESCITA (100 sopra 300 > 0.69) - r 8091"
                        action = "sell"
                        
                        # and ma3_last < ma33_last
                        # and deviation_sell < 0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # cuscino dell' angelo custode
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                
                        and deviation_ma100_sopra_ma300 > 0.69
                        and deviation_sell < -0.10
                        and ma5_last < ma100_last
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 < CUSCINO SANT' ANTONIO (5-100) MA SOLO con TREND CRESCITA (100 sopra 300 > 0.69) - r 8110"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.17
                        and ma2_last < ma2_2_min_ago
                        
                        and deviation_ma100_sopra_ma300 < 0.69
                        and deviation_sell < -0.15
                       
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 < con deviation_ma39 <-0.17 and deviation_sell < 0.10 TREND LATERALE (100>300 MA <0.69) - r 8125"
                        action = "sell"
                        
                        
                        
                        
                    ###########################################################################################################

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.10
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < -0.10 - r 8139"
                        action = "sell"
                        
                        
                     
                    # maggiore perdita tollerata
                    
                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.20
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 < con deviation_ma39 <-0.20 and deviation_sell < 0.10 con > perdita tollerata - r 8154"
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
                        sell = "SELL 3 da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < 0.13 con > perdita tollerata - r 8174"
                        action = "sell"
                        
                        
                 

                ############################################################################################################ sessione 3-4-x ( > 90 min )

                # VENDITA - da 90 minuti in poi = da 5400 secondi in poi

                elif seconds_since_last_trade > 5400:
                    
                    
                    ################################################################################### RIGHE DEL COMPA raddoppiate PER AUMENTARE TOLLERANZA
                    
                    
                    if (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.21
                    ):
                        sell = "SELL 3 dopo 90 min con ma50> and deviation_ma25 <-0.18 (no ma3<ma39) - r 8195"
                        action = "sell"
                    
                    
                    
                    
                    elif (     
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.20 
                        and ma3_last < ma50_last
                    ):
                        sell = "SELL 3 dopo 90 min con ma50> and (deviation_sell < 0.10 and ma3_last < ma50_last)- r 8207"
                        action = "sell"
                        
                    
                    
                        
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.23
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 dopo 90 min con ma50> and deviation_ma25 < -0.23 - r 8219"
                        action = "sell"
                        
                
                    
                    
                    elif (     
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.23 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 dopo 90 min con ma50> and (deviation_sell < -0.23 and ma3_last < ma50_last) - r 8232"
                        action = "sell"
                        
                       
                        
                        
                        
                    ############################################################################################################################### 
                    
                  
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma69_last
                        and deviation_sell > 0.25 and deviation_sell < 0.59
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and 5-69 and deviation_sell 0.25-0.59 - FINTA ALLA MARADONA - r 8249"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # al SELL 3 maradona e' ancora piu' stanco di quello che pensavo !
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma25_last
                        and deviation_sell > 0.60 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 >90 min con ma50 > con 4 < 25 and deviation_sell 0.60 - 0.90 DRIBBLING ALLA RONALDO - r 8264"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 dopo 90 min con ma50 > incrocio 3-30 (!) and deviation_sell 0.91 - 1.49 - r 8277"
                        action = "sell"

                        # ma 3-48 mi evita la ricompra e la rivendita con perdita !
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 dopo 90 min con ma50 > incrocio 3-30 (!) and deviation_sell 1.50 - 2.70 - r 8292"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 dopo 90 min con ma50 > incrocio 3-11 (!) and deviation_sell > 2.71 - r 8305"
                        action = "sell"
                        
                 
                
                
                    ######################################################################################## con trend discendente
                    
                    
                    
                    elif (      
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.15
                       
                    ):
                        sell = "SELL 3 dopo 90 min con ma50 < con deviation_ma39 < -0.15 - r 8321"
                        action = "sell"
                        
                     
                    
                     
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.10 
                        and ma3_last < ma39_last
                    ):
                        sell = "SELL 3 dopo 90 min con ma50 < and (deviation_sell < -0.10 and ma3_last < ma39_last) - r 8333"
                        action = "sell"
                        
                    
                    
                    ################################################################################################ sessione 3 (vendita con questi 7 altri modi)
                    
                    ################################################################################################
                    # ATTENZIONE al conflitto durante il crollo - SELL SOVRAPPOSTO AL BUY

                    # NO 3<78 !
                    # NO deviation 78 !
                    # QUALCHE VOLTA ma3-ma39 NON HANNO INCROCIATO allora per la vendita con il DRIBBLING e il DOPPIO PASSO ALLA RONALDO ho risolto con 3<39
                    # il CUSCINO DELL' ANGELO CUSTODE e di SANT' ANTONIO mi proteggono ! (vendita con medie lunghe)
                    
                    

                    # 1 - ro cano VENDE CON UN SALVAGENTE
            
                    if deviation_ma39 < -0.24 and deviation < -0.36 and ma50_last > ma50_2_min_ago:

                        sell = "SELL 3 SALVAGENTE 3-39 con ma50 < r 8354"
                        action = "sell"

                        # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!
                        
                        
                        

                    # 2 - ro cano VENDE DURANTE UN CROLLO IMPROVVISO !
                    
                    elif (
                   
                        ma2_last < ma4_last
                        and ma2_last < ma6_last
                        and deviation < -0.58
                  
                    ):    
                        
                        sell = "SELL 3 CROLLO IMPROVVISO - r 8372"
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

                        sell = "SELL 3 DOLCE ATTESA con ma13 > and deviation < -0.40 - r 8396"
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

                        sell = "SELL 3 DOLCE ATTESA 270 sec con ma13 < and deviation < -0.345 - r 8417"
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

                        sell = "SELL 3 TEMPO e se ma8 < ma50 and deviation_sell < -0.49 - r 8439"
                        action = "sell"
                        
                        # ma13 troppo lenta !
                        # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                        
                        
                
                
                    # 6 POCHI MALEDETTI E SUBITO ma solo con 200 > and...
                    
                    elif (
                        
                        ma3_last < ma9_last
                        and ma200_last > ma200_60_min_ago
                        and deviation > 0.68
                        and ma2_last < ma2_2_min_ago
                 
                        and ma2_last > ma100_last
                        and deviation_pochi_maledetti > 0.25
                        and deviation_trend_ma100 < 0.50
                    ):    
                        sell = "SELL 3 POCHI MALEDETTI E SUBITO quando ma200 > e con deviation > 0.70 MA ma100 NON DEVE SALIRE TROPPO ! - r 8461"
                        action = "sell"
                        
                        # attenzione : le prime 4 righe sono uguali a RCCR che ha funzionato. le altre 3 non hanno fatto attivare questa condizione !
                        
                        # and ma2_last > ma100_last (altrimenti vende durante il crollo con la ma3-ma9)
                        # incredibile questa and deviation_trend_ma100 < 1.00 - se ma100 sale "forte" da 60 min non deve intervenire sell 3-9
                        
                        #POCHI MALEDETTI E SUBITO FINO A BUY 3. STOP. PASSO E CHIUDO.
                        
                        
                        
                    # 6 - RIBASSO IMPROVVISO
            
                    elif (
                        ma78_last > ma78_2_min_ago
                        and deviation_ribasso_improvviso < -0.63
                        and ma2_last < ma2_2_min_ago
                    ):
       
                        sell = "SELL 3 RIBASSO IMPROVVISO - r 8481"
                        action = "sell"
            
            
            
            
            
                    # 7 - RIBASSO IMPROVVISO
            
                    elif (
                        ma78_last < ma78_2_min_ago
                        and deviation_ribasso_improvviso < -0.63
                        and ma2_last < ma2_2_min_ago
                    ):
       
                        sell = "SELL 3 RIBASSO IMPROVVISO - r 8496"
                        action = "sell"
            
            
            
            
            
            ######################################################################################################
            
            
            elif self.session > 3:
                

                ################################################################################################### sessione 4-5-x ( 0-3 min )
                
                if seconds_since_last_trade > 0 and seconds_since_last_trade <= 180:
                    

                    # con ma50 >

                    if (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma18_last
                        and deviation_sell < -0.33
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (0-3 min) con ma50 > and 3<18 and deviation_sell < -0.33 - r 8522"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma25_prev and ma5_last < ma25_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 4-5-x SELL (0-3 min) con ma50 > and incrocio 5-25 and deviation_sell 0.25 - 0.56 MARADONA - r 8537"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma4_prev > ma20_prev and ma4_last < ma20_last)
                        and deviation_sell > 0.57 and deviation_sell < 0.79
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (0-3 min) con ma50 > and incrocio 4-20 and deviation_sell 0.57 - 0.79 RONALDO - r 8551"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 0.80 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell 0.80 - 1.20 - r 8563"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell > 1.21 (che sarebbe come IL DRIBBLING ALLA RONALDO !) - r 8576"
                        action = "sell"
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (0-3 min) con ma50 < and incrocio 3-28 - r 8589"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 - r 8602"
                        action = "sell"
                        
                        

                    # ---------------------------------------------------------------------------------------------------------------------- crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - r 8615"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - r 8629"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                        and deviation_sell > 0.60
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - r 8642"
                        action = "sell"
                        
                        

                ################################################################################################ sessione 3-4-x ( 3-7 min )

                # VENDITA - da 3 a 7 minuti = da 180 a 420 secondi

                elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 420:
                    

                    if (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.32
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 4-5-x (3-7 min) con ma50 > and 3<16 and deviation_sell < -0.32 - r 8661"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (3-7 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 8675"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 4-5-x (3-7 min) con ma50 > and 4<20 and deviation_sell 0.57 - 0.90 - DRIBBLING ALLA RONALDO - r 8690"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.40
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (3-7 min) con ma50 > and incrocio 3-20 and deviation_sell 0.91 - 1.40 - r 8704"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 1.41
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (3-7 min) con ma50 > and incrocio 3-15 and deviation_sell > 1.41 - r 8715"
                        action = "sell"
                        
                        
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 4-5-x (3-7 min) con ma50 < and incrocio 3-28 - r 8731"
                        action = "sell"
                        
                        # deviation_sell_ma78 = ma3_last / ma78_last
                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (3-7 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.23 - r 8746"
                        action = "sell"
                        
                        

                    # --------------------------------------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x GUADAGNO CON CROLLO (3-7 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - r 8759"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x PARACADUTE CROLLO (3-7 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 8770"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                        

                ######################################################################################## sessione 3-4-x  (7-12 min !)

                # VENDITA - da 7 a 12 minuti = da 4200 a 720 secondi

                elif seconds_since_last_trade > 420 and seconds_since_last_trade <= 720:
                    

                    if (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.41
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (7-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - r 8791"
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
                        sell = "SELL 4-5-x (7-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - r 8807"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (7-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 8821"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                  
                    ):
                        sell = "SELL 4-5-x (7-12 min) con ma50 > and 4-20 and deviation_sell 0.57 - 0.90 - DRIBBLING ALLA RONALDO - r 8836"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 4-5-x (7-12 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - r 8851"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (7-12 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - r 8865"
                        action = "sell"
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (7-12 min) con ma50 < and incrocio 3-28 - r 8878"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (7-12 min) con ma50 < and incrocio 3-100 (cuscino di sant' antonio) - r 8891"
                        action = "sell"
                        
                        

                    # ------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x guadagno con crollo (7-12 min) con ma50 < and incrocio 3-23 - r 8904"
                        action = "sell"
                        
                        

                    # --------------------------------------------------------------------------------------------------- PARACADUTE crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x PARACADUTE CROLLO (7-12 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 8917"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        

                        
                ############################################################################################################## sessione 3-4-x ( 12-21 min )

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
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and incrocio 3-72 and deviation sell -0.65 e vaffanculo ! - r 8940"
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
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.36 - r 8957"
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
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 8976"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and 4-20 and deviation_sell 0.57 - 0.90 - DRIBBLING ALLA RONALDO - r 8991"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - r 9006"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and incrocio 3-30 and deviation_sell > 1.21 - r 9020"
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
                        sell = "SELL 4-5-x (12-21 min) con ma50 < and deviation_ma39 < -0.17 - r 9040"
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
                        sell = "SELL 4-5-x (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - r 9060"
                        action = "sell"
                        
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50< !
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - r 9075"
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
                        sell = "SELL 4-5-x PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 9092"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                        
                  
                    # ----------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3 - 18 and deviation_sell > 0.23 - r 9108"
                        action = "sell"
                        
                        

                ########################################################################################################### sessione 3-4-x ( 21-60 min )
                

                # VENDITA - da 21 a 60 minuti = da 1261 a 3600 secondi

                elif (
                    seconds_since_last_trade > 1261 and seconds_since_last_trade <= 3600
                ):
                    
                    
                    ############################################################################## RIGHE DEL COMPA RADDOPPIATE PER AUMENTARE TOLLERANZA
                    
                    if (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.27
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and deviation_ma25 < -0.27 - r 9131"
                        action = "sell"
                        
                     
                    
                    elif ( 
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.24 
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and (deviation_sell < -0.24 and ma3_last < ma50_last) - r 9143"
                        action = "sell"
                        
                     
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.29
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and deviation_ma25 < -0.29 - r 9155"
                        action = "sell"
                        
                       
                    
                    
                    elif (        
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.26 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and (deviation_sell < -0.26 and ma3_last < ma50_last) - r 9168"
                        action = "sell"
                        
                      
                        #############################################################################################################
                    

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.26
                        and ma2_last < ma2_2_min_ago
                  
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.26 - r 9182"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma25_prev and ma5_last < ma25_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                   
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and incrocio 5-25 and deviation_sell 0.25 - 0.56 FINTA DI MARADONA - r 9197"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma28_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and 3-28 (no incrocio 3-15) and deviation_sell 0.57 - 0.90 FINTA ALLA RONALDO - r 9212"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                      
                    

                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma20_last
                        and deviation_sell > 0.91 and deviation_sell < 1.40
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and 3-20 and deviation_sell 0.91 - 1.40 - r 9227"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma25_last
                        and deviation_sell > 1.41 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and 3-25 and deviation_sell 1.41 -2.70 - r 9241"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and incrocio 3-13 and deviation_sell > 2.71 - r 9253"
                        action = "sell"
                    
                    
                    
                    ################################################################################################# con trend discendente
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.24
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and deviation_ma39 < -0.225 - r 9267"
                        action = "sell"
                        
                        
                 
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.23 
                        and ma3_last < ma39_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and deviation_sell < 0.225 - r 9279"
                        action = "sell"
                        
              
            
            
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_60_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.37
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - r 9292"
                        action = "sell"
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_60_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - r 9305"
                        action = "sell"
                        
                        # viva sant' antonio !
                        # NON INCROCERANNO MAI DURANTE IL CROLLO !
                        # non toccare ! INCROCIO 3-100 CUSCINO DI SANT' ANTONIO !
                        
                        
                        
                        
                        
                    ##################################################################################################### aumenta la tolleranza    
                        
                    elif (
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.26
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and deviation_ma39 < -0.26 - r 9324"
                        action = "sell"
                        
                 
                
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.25 
                        and ma3_last < ma39_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and deviation_sell < 0.25 - r 9336"
                        action = "sell"
                        
              
            
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma200_60_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.39
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.39 - r 9348"
                        action = "sell"
                        
                        
                  
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma200_60_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.29
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and INCROCIO 5-100 (no 5<100) and deviation_sell < -0.29  CUSCINO DI SANT' ANTONIO - r 9361"
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
                        sell = "SELL 4-5-x eventuale guadagno durante il crollo (21-60 min) con ma50 < incrocio 3 - 18 and deviation_sell > 0.23 - r 9379"
                        action = "sell"
                        
                        
                    
                    

                ############################################################################################################# sessione 3-4-x ( da 60 a 90 min )

                # VENDITA - da 60 a 90 min - da 3600 a 5400 secondi in poi
                
                elif (
                    seconds_since_last_trade > 3600 and seconds_since_last_trade <= 5400
                ):
                    
                    
                    
                    ######################################################################### RIGHE DEL COMPA raddoppiate PER AUMENTARE LA TOLLERANZA
                    
                    
                    
                    if ( 
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.22
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > and deviation_ma25 < -0.19 - r 9406"
                        action = "sell"
                        
                        
                    
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.21 
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > and (deviation_sell < -0.19 and ma3_last < ma50_last) - r 9418"
                        action = "sell"
                        
                        
                        
                        
                    elif ( 
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.25
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > and deviation_ma25 < -0.25 - r 9430"
                        action = "sell"
                        
                        
                        
                    
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.24 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > and (deviation_sell < -0.24 and ma3_last < ma50_last) - r 9443"
                        action = "sell"
                        
                        
                        
                        
                        #########################################################################################################################
                        
                      
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma25_prev and ma5_last < ma25_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and incrocio 5-25 and deviation_sell 0.25 - 0.56 FINTA DI MARADONA - r 9460"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x >60 min con ma50> and 4-20 and deviation_sell 0.57-0.90 DRIBBLING ALLA RONALDO - r 9474"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > and incrocio 3-30 and deviation_sell 0.91 - 1.49 - r 9487"
                        action = "sell"

                        # ma ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > incrocio 3-25 and deviation_sell 1.50 - 2.70 - r 9502"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > incrocio 3-13 and deviation_sell > 2.71 - r 9515"
                        action = "sell"
                        
                    
                    
                    
                    ######################################################################################## con trend discendente
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 < con deviation_ma39 <-0.18 and deviation_sell < 0.10 (no ma3<ma33) (NO INCROCIO!) - r 9530"
                        action = "sell"
                        
                        # and ma3_last < ma33_last
                        # and deviation_sell < 0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # cuscino dell' angelo custode
                        
                        
                    
                    
                    # sta in alto e stai attento
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 > 0.25
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.05
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < -0.05 meno tollerante (sta in alto) - r 9552"
                        action = "sell"
                        
                        
                        
                        
                    # sta in basso e, PARADOSSALMENTE, sta piu' calmo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 < 0.25
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.19
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < -0.19 piu' tollerante (sta in basso) - r 9568"
                        action = "sell"
                        
                        

                ############################################################################################################ sessione 3-4-x ( > 90 min )

                # VENDITA - da 90 minuti in poi = da 5400 secondi in poi

                elif seconds_since_last_trade > 5400:
                    
                    
                    
                    # ################################################################################ RIGHE DEL COMPA DA RADDOPPIARE PER AUMENTARE TOLLERANZA
                    
                    if (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.22
                    ):
                        sell = "SELL 4-5-x dopo 90 min con ma50> and deviation_ma25 <-0.18 (no ma3<ma39) - r 9588"
                        action = "sell"
                        
                      
                    
                    
                    
                    elif (     
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.21 
                        and ma3_last < ma50_last
                    ):
                        sell = "SELL 4-5-x dopo 90 min con ma50> and (deviation_sell < 0.10 and ma3_last < ma50_last) - r 9601"
                        action = "sell"
                        
                      
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.25
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x dopo 90 min con ma50> and deviation_ma25 < -0.25 TOLLERANTE - r 9613"
                        action = "sell"
                        
                        
                        
                 
                    elif (     
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.24 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x dopo 90 min con ma50> and (deviation_sell < -0.24 and ma3_last < ma50_last) TOLLERANTE - r 9626"
                        action = "sell"
                        
                        
                        
                        #############################################################################################################################
                       
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 9641"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x >90 min con ma50 > con 4 < 20 and deviation_sell 0.35 - 0.90 FINTA ALLA RONALDO - r 9655"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x dopo 90 min con ma50 > incrocio 3-30 (!) and deviation_sell 0.91 - 1.49 - r 9667"
                        action = "sell"

                        # ma 3-48 mi evita la ricompra e la rivendita con perdita !
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x dopo 90 min con ma50 > incrocio 3-25 (!) and deviation_sell 1.50 - 2.70 - r 9682"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x dopo 90 min con ma50 > incrocio 3-13 (!) and deviation_sell > 2.71 - r 9695"
                        action = "sell"
                        
                        

                    ######################################################################################## con trend discendente
                    
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.215
                    ):
                        sell = "SELL 4-5-x dopo 90 min con ma50 < con deviation_ma39 <-0.215 - r 9709"
                        action = "sell"
                        
                        
                        
                    
                     
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.21 
                        and ma3_last < ma39_last
                    ):
                        sell = "SELL 4-5-x dopo 90 min con ma50 < and (deviation_sell < 0.10 and ma3_last < ma39_last) - r 9722"
                        action = "sell"
                        
                    
                    
                    
            #################################################################################### sessione 3-4-x (vendita con questi 9 altri modi)
            ####################################################################################
            ####################################################################################
                    
            # ATTENZIONE al conflitto durante il crollo - SELL SOVRAPPOSTO AL BUY

            # NO 3<78 !
            # NO deviation 78 !
            # QUALCHE VOLTA ma3-ma39 NON HANNO INCROCIATO allora per la vendita con il DRIBBLING e il DOPPIO PASSO ALLA RONALDO ho risolto con 3<39
            # il CUSCINO DELL' ANGELO CUSTODE e di SANT' ANTONIO mi proteggono ! (vendita con medie lunghe)
                    
                    

            # 1 - SELL condizione speciale ro cano VENDE CON UN SALVAGENTE
            
            if deviation_ma39 < -0.24 and deviation < -0.36 and ma50_last > ma50_2_min_ago:
                   

                sell = "SELL condizione speciale SALVAGENTE 3-39 con ma50 < - r 9746"
                action = "sell"

                # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!
                        
                        
                        

            # 2 - SELL condizione speciale ro cano VENDE DURANTE UN CROLLO IMPROVVISO !
                
            elif (
                ma2_last < ma4_last
                and ma2_last < ma6_last
                and deviation < -0.58
            ):
                  
                sell = "SELL condizione speciale CROLLO IMPROVVISO - r 9762"
                action = "sell"
            
                # con -0.59 il 6 feb 2022 ha fatto -0.85
                # con -0.62 il 4 feb 2022 ha fatto -0.89%
                # deviation = ma4_last / last_trade_price

                # FORSE E' L' UNICA DEVIATION CHE MI POTRA' SALVARE DA UN CROLLO IMPROVVISO COME QUELLO DEL 3 NOVEMBRE 2021
                
                
            
            
            # 3 - SELL condizione speciale dopo il crollo improvviso del 24 aprile 2022
                    
            elif (    
                ma2_last < ma4_last
                and ma2_last < ma6_last
                and deviation_crollo_24_aprile < -0.58
            ): 
                
                sell = "SELL condizione speciale DOPO IL CROLLO IMPROVVISO del 24 aprile 2022 - r 9843"
                action = "sell"
                        
                # ho aggiunto anche questa vendita speciale dopo il 24 aprile -1%
                # deviation_crollo_24_aprile = ma2_last / last_trade_price        
                        
                        
                        

            # 4 - SELL condizione speciale ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma13 >
            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and ma2_last < last_trade_price
                and deviation < -0.42
                and ma13_last > ma13_2_min_ago
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL condizione speciale DOLCE ATTESA con ma13 > and deviation < -0.40 - r 9785"
                action = "sell"

                # il fattore tempo - la dolce attesa - solo con trend ribassista
                # deviation = ma2_last / last_trade_price
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                # max_hold_time_in_seconds = 300 = 5 min (con 6 min perdita di 0.90 %)
                        
                        
                        
                
            # 5 - SELL condizione speciale ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma13 <
            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and ma13_last < ma13_2_min_ago
                and deviation < -0.355
                and ma2_last < last_trade_price
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL condizione speciale DOLCE ATTESA 270 sec con ma13 < and deviation < -0.345 - r 9806"
                action = "sell"

                # il fattore tempo - la dolce attesa - solo con trend ribassista
                # deviation = ma2_last / last_trade_price
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                # max_hold_time_in_seconds = 270 sec = 4 min e 1/2  (con 6 min perdita di 0.60 %)
                # 4 feb 2022 con <-0.26 ha fatto -0.88% (dopo +4.29%)
                # 7 feb 2022 con <-0.345 e 270 sec ha fatto -0.38% - aumenta a 0.355 ! - eventualmente ci pensa la condizione CROLLO IMPROVVISO CHE FUNZIONA !
                        
            
            
            
            # 6 - SELL condizione speciale ro cano VENDE " DOPO x MINUTI " and...
            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and ma8_last < ma50_last
                and deviation_sell < -0.49
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL condizione speciale TEMPO e se ma8 < ma50 and deviation_sell < -0.49 - r 9828"
                action = "sell"
                        
                # ma13 troppo lenta !
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                        
                        
               
                
            # 7 - SELL condizione speciale RIBASSO IMPROVVISO
            
            elif (
                ma78_last > ma78_2_min_ago
                and deviation_ribasso_improvviso < -0.63
                    
            ):
                sell = "SELL condizione speciale RIBASSO IMPROVVISO - r 9844"
                action = "sell"
                    
                    
            
            # 8 - SELL condizione speciale RIBASSO IMPROVVISO
            
            elif (
                ma78_last < ma78_2_min_ago
                and deviation_ribasso_improvviso < -0.63
                    
            ):
                sell = "SELL condizione speciale RIBASSO IMPROVVISO - r 9856"
                action = "sell"
                    
                    
              
            
            # 9 - SELL condizione speciale POCHI MALEDETTI E SUBITO QUANDO SALE FORTE ( cerca di inibirlo ) con ma200 > MA ma100 - dedicated to comparo meo
            
            elif (
                ma3_last < ma28_last
                and deviation_ma100_sopra_ma200 > 0.40    
                and ma200_last > ma200_60_min_ago
                    
                and deviation > 0.70
                and deviation_trend_ma100 < 1.00
                and deviation_pochi_maledetti > 0.25
                and ma2_last > ma100_last
            ):    
                sell = "SELL condizione speciale POCHI MALEDETTI E SUBITO QUANDO SALE FORTE 3-28 ( cerca di inibirlo ) quando ma200 > e con deviation > 0.70 MA - dedicated to comparo meo - r 9874"
                action = "sell"
                    
                # and ma2_last > ma100_last (altrimenti vende durante il crollo con la ma3-ma9)
                # incredibile questa and deviation_trend_ma100 < 1.00 - se ma100 sale "forte" da 60 min non deve intervenire sell 3-9
                
                
                
            # 10 - SELL condizione speciale POCHI MALEDETTI E SUBITO QUANDO SALE PIANO con ma200 > MA ma100 NON DEVE SALIRE TROPPO ! - dedicated to comparo meo
            
            elif (
                ma3_last < ma9_last
                and deviation_ma100_sopra_ma200 < 0.40      
                and ma200_last > ma200_60_min_ago
                    
                and deviation > 0.70
                and deviation_trend_ma100 < 1.00
                and deviation_pochi_maledetti > 0.25
                and ma2_last > ma100_last
            ):    
                sell = "SELL condizione speciale POCHI MALEDETTI E SUBITO 3-9 QUANDO SALE PIANO quando ma200 > e con deviation > 0.70 MA - dedicated to comparo meo - r 9874"
                action = "sell"
                    
                # and ma2_last > ma100_last (altrimenti vende durante il crollo con la ma3-ma9)
                # incredibile questa and deviation_trend_ma100 < 1.00 - se ma100 sale "forte" da 60 min non deve intervenire sell 3-9
                    
                
                
            
            # 11 - SELL condizione speciale POCHI MALEDETTI E SUBITO con ma200 < - dedicated to comparo meo
                
            elif (
                ma3_last < ma9_last 
                and ma200_last < ma200_60_min_ago
                and deviation > 0.70
                and deviation_pochi_maledetti > 0.70
                and ma2_last > ma100_last
            ):    
                sell = "SELL condizione speciale POCHI MALEDETTI E SUBITO 3-9 quando ma200 < e con deviation > 0.70 - dedicated to comparo meo - r 9892"
                action = "sell"
                    
                # and ma2_last > ma100_last (altrimenti vende durante il crollo con la ma3-ma9)
                
                
                
                
            ######################################################################### vendite dedicate al BUY FIAT - AUDI - MASERATI - FERRARI 
            
            # 12 - SELL condizione speciale FIAT 
                    
            elif (     
                seconds_since_last_trade > max_hold_time_in_seconds_fiat
                and deviation_buy_crollo_1 < -0.15
                and deviation_buy_crollo_1 > -0.59
                        
                and deviation_ma100_sopra_ma300 < -0.70
                and deviation < -0.29
            ):    
                 
                buy = "SELL condizione speciale FIAT se > 20 min dal BUY FIAT la perdita e' < -0.29 ! - r 9995"
                action = "sell"
                        
                # and ma2_last < ma2_2_min_ago
                # and deviation_ma100_sopra_ma300 < -0.70 significa che c'e' un grande ribasso. 100 sta lontana da 300. 
                # EVITO COSI' PROBLEMI AL TREND LATERALE.
                        
                        
                        
                
            # 13 - SELL condizione speciale AUDI 
                    
            elif (     
                seconds_since_last_trade > max_hold_time_in_seconds_audi
                and deviation_buy_crollo_1 < -0.60
                and deviation_buy_crollo_1 > -0.90
                        
                and deviation_ma100_sopra_ma300 < -0.70
                and deviation < -0.31
                        
            ):
                buy = "SELL condizione speciale AUDI se > 20 min dal BUY AUDI la perdita e' < -0.31 - r 10016"
                action = "sell"
                        
                # and ma2_last < ma2_2_min_ago
                        
                        
               
            # 14 - SELL condizione speciale MASERATI 
                    
            elif (     
                seconds_since_last_trade > max_hold_time_in_seconds_maserati
                and deviation_buy_crollo_1 < -0.91
                and deviation_buy_crollo_1 > -1.50
                      
                and deviation_ma100_sopra_ma300 < -0.70
                and deviation < -0.33
                        
            ):
                buy = "SELL condizione speciale MASERATI se > 20 min dal BUY MASERATI la perdita e' < -0.33 - r 10034"
                action = "sell"
                        
                # and ma2_last < ma2_2_min_ago
                        
               
            
            
            # 15 - SELL condizione speciale FERRARI 
                    
            elif (     
                seconds_since_last_trade > max_hold_time_in_seconds_ferrari
                and deviation_buy_crollo_1 < -1.51
                        
                and deviation_ma100_sopra_ma300 < -0.70
                and deviation < -0.37
            ):
                buy = "SELL condizione speciale FERRARI se > 20 min dal BUY FERRARI la perdita e' < -0.37 - r 10051"
                action = "sell"
                        
                # and ma2_last < ma2_2_min_ago    
                    
                
                
                

        self.algo_helper.info("action {}".format(action))
        self.algo_helper.info("percentage {}".format(percentage))

        if action == "sell":
            self.algo_helper.info("action sell {}".format(sell))
            self.session += 1

        elif action == "buy":
            self.algo_helper.info("action buy {}".format(buy))

        return action, percentage

        ############### FINE ALGORITH ###################
        
        # viva ro combaro meo.
        # questi miei sacrifici io li dedico a te.
        # grazie.
        # niente altro.
        
        # roma 3 maggio 2022
        
        
        
        
        
