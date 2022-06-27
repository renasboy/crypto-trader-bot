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
        ma34_last, ma34_prev = self.algo_helper.ma_last_prev(34)
        ma36_last, ma36_prev = self.algo_helper.ma_last_prev(36)
        ma39_last, ma39_prev = self.algo_helper.ma_last_prev(39)
        ma40_last, ma40_prev = self.algo_helper.ma_last_prev(40)
        ma42_last, ma42_prev = self.algo_helper.ma_last_prev(42)
        ma45_last, ma45_prev = self.algo_helper.ma_last_prev(45)
        ma47_last, ma47_prev = self.algo_helper.ma_last_prev(47)
        ma48_last, ma48_prev = self.algo_helper.ma_last_prev(48)
        ma50_last, ma50_prev = self.algo_helper.ma_last_prev(50)
        ma52_last, ma52_prev = self.algo_helper.ma_last_prev(52)
        ma54_last, ma54_prev = self.algo_helper.ma_last_prev(54)
        
        ma59_last, ma59_prev = self.algo_helper.ma_last_prev(59)
        
        ma69_last, ma69_prev = self.algo_helper.ma_last_prev(69)
        ma72_last, ma72_prev = self.algo_helper.ma_last_prev(72)
        ma78_last, ma78_prev = self.algo_helper.ma_last_prev(78)
        ma100_last, ma100_prev = self.algo_helper.ma_last_prev(100)
        ma125_last, ma125_prev = self.algo_helper.ma_last_prev(125)
        ma140_last, ma140_prev = self.algo_helper.ma_last_prev(140)
        ma150_last, ma150_prev = self.algo_helper.ma_last_prev(150)
        ma200_last, ma200_prev = self.algo_helper.ma_last_prev(200)
        ma285_last, ma285_prev = self.algo_helper.ma_last_prev(285)
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
        ma18_30_min_ago = self.algo_helper.ma_minutes_ago(18, 30)
        ma20_2_min_ago = self.algo_helper.ma_minutes_ago(20, 2)
        ma20_22_min_ago = self.algo_helper.ma_minutes_ago(20, 22)
        ma20_60_min_ago = self.algo_helper.ma_minutes_ago(20, 60)
        ma25_2_min_ago = self.algo_helper.ma_minutes_ago(25, 2)
        ma28_2_min_ago = self.algo_helper.ma_minutes_ago(28, 2)
        ma28_30_min_ago = self.algo_helper.ma_minutes_ago(28, 30)
        
        ma30_10_min_ago = self.algo_helper.ma_minutes_ago(30, 10)
        ma30_20_min_ago = self.algo_helper.ma_minutes_ago(30, 20)
        ma30_30_min_ago = self.algo_helper.ma_minutes_ago(30, 30)
        ma30_40_min_ago = self.algo_helper.ma_minutes_ago(30, 40)
      
        ma33_5_min_ago = self.algo_helper.ma_minutes_ago(33, 5)
        ma36_2_min_ago = self.algo_helper.ma_minutes_ago(36, 2)
        ma39_2_min_ago = self.algo_helper.ma_minutes_ago(39, 2)
        ma39_3_min_ago = self.algo_helper.ma_minutes_ago(39, 3)
        ma39_15_min_ago = self.algo_helper.ma_minutes_ago(39, 15)
        ma39_30_min_ago = self.algo_helper.ma_minutes_ago(39, 30)
        ma48_3_min_ago = self.algo_helper.ma_minutes_ago(48, 3)
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
        ma78_60_min_ago = self.algo_helper.ma_minutes_ago(78, 60)
        ma100_2_min_ago = self.algo_helper.ma_minutes_ago(100, 2)
        ma100_3_min_ago = self.algo_helper.ma_minutes_ago(100, 3)
        
        ma100_10_min_ago = self.algo_helper.ma_minutes_ago(100, 10)
        ma100_30_min_ago = self.algo_helper.ma_minutes_ago(100, 30)
        ma100_50_min_ago = self.algo_helper.ma_minutes_ago(100, 50)
        ma100_60_min_ago = self.algo_helper.ma_minutes_ago(100, 60)
        ma100_120_min_ago = self.algo_helper.ma_minutes_ago(100, 120)
        ma150_60_min_ago = self.algo_helper.ma_minutes_ago(150, 60)
        ma200_15_min_ago = self.algo_helper.ma_minutes_ago(200, 15)
        ma200_20_min_ago = self.algo_helper.ma_minutes_ago(200, 20)
        ma200_30_min_ago = self.algo_helper.ma_minutes_ago(200, 30)
        ma200_60_min_ago = self.algo_helper.ma_minutes_ago(200, 60)
        ma200_90_min_ago = self.algo_helper.ma_minutes_ago(200, 90)
        ma200_120_min_ago = self.algo_helper.ma_minutes_ago(200, 120)
        ma200_120_min_ago = self.algo_helper.ma_minutes_ago(200, 120)
        ma300_20_min_ago = self.algo_helper.ma_minutes_ago(300, 20)
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
        
        # vedi SELL 1 FIAT - 2 minuti = 120 secondi
        
        max_hold_time_in_seconds_fiat = 120
        
       
        # vedi SELL 1 AUDI - 2 minuti = 120 secondi
        
        max_hold_time_in_seconds_audi = 120
        
      
        # vedi SELL 1 MASERATI - 2 minuti = 120 secondi
        
        max_hold_time_in_seconds_maserati = 120
        
        
        # vedi SELL 1 FERRARI - 2 minuti = 120 secondi
        
        max_hold_time_in_seconds_ferrari = 120
        
        
        ###############################################################################################################################
        
        # vedi DELTA BUY 2 DAL SELL 1  > 2 minuti = 120 secondi
        
        max_hold_time_in_seconds_delta_buy2_sell1 = 120
        
        
        #########################################################################################################################################################
        #########################################################################################################################################################

        #                                                         T U T T E    L E   D E V I A T I O N  !
        

        # formula DEVIATION_1_gabbia
        
        deviation_1_gabbia = (ma8_last / ma50_last - 1) * 100 if ma50_last else 0
        self.algo_helper.info("deviation_1_gabbia: {}".format(deviation_1_gabbia))

        # formula deviation
        
        deviation = (ma5_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.info("deviation: {}".format(deviation))
        
        
        
        # formula DEVIATION_ma5_sopra_ma28 - FORMULA AUREA !
        
        deviation_ma5_sopra_ma28 = (ma5_last / ma28_last - 1) * 100 if ma28_last else 0
        self.algo_helper.info("deviation_ma5_sopra_ma28: {}".format(deviation_ma5_sopra_ma28))
        
        
        
        # formula DEVIATION_ma3_sopra_ma16
        
        deviation_ma3_sopra_ma16 = (ma3_last / ma16_last - 1) * 100 if ma16_last else 0
        self.algo_helper.info("deviation_ma3_sopra_ma16: {}".format(deviation_ma3_sopra_ma16))
        
        
        #################################################################################################################
        
        # formula delta_1
        
        delta_1 = (ma200_last / ma100_last - 1) * 100 if ma100_last else 0
        self.algo_helper.info("delta_1: {}".format(delta_1))
        
        
        # formula delta_2
        
        delta_2 = (ma200_60_min_ago / ma100_60_min_ago - 1) * 100 if ma100_60_min_ago else 0
        self.algo_helper.info("delta_2: {}".format(delta_2))
        
        
        # formula rapporto_delta_1_delta_2
        
        rapporto_delta_1_delta_2 = (delta_1 / delta_2) if delta_2 else 0
        self.algo_helper.info("rapporto_delta_1_delta_2: {}".format(rapporto_delta_1_delta_2))
        
        
        
        
        
        
        # formula delta_150_100
        
        delta_150_100 = (ma150_last / ma100_last - 1) * 100 if ma100_last else 0
        self.algo_helper.info("delta_150_100: {}".format(delta_150_100))
        
        
        # formula delta_150_100_60_min
        
        delta_150_100_60_min = (ma150_60_min_ago / ma100_60_min_ago - 1) * 100 if ma100_60_min_ago else 0
        self.algo_helper.info("delta_150_100_60_min: {}".format(delta_150_100_60_min))
        
        
        # non serve piu' il rapporto !
        
        
        
        
        
        
        # formula delta_1_200_30
        
        delta_1_200_30 = (ma200_last / ma30_last - 1) * 100 if ma30_last else 0
        self.algo_helper.info("delta_1_200_30: {}".format(delta_1_200_30))
        
        
        # formula delta_2_200_30_30_min
        
        delta_2_200_30_30_min = (ma200_30_min_ago / ma30_30_min_ago - 1) * 100 if ma30_30_min_ago else 0
        self.algo_helper.info("delta_2_200_30_30_min: {}".format(delta_2_200_30_30_min))
        
        
        # non serve piu' il rapporto !
        
        
        
        
        
        # formula delta_1_200_78
        
        delta_1_200_78 = (ma200_last / ma78_last - 1) * 100 if ma78_last else 0
        self.algo_helper.info("delta_1_200_78: {}".format(delta_1_200_78))
        
        
        # formula delta_2_200_78_60_min
        
        delta_2_200_78_60_min = (ma200_60_min_ago / ma78_60_min_ago - 1) * 100 if ma78_60_min_ago else 0
        self.algo_helper.info("delta_2_200_78_60_min: {}".format(delta_2_200_78_60_min))
        
        
        # non serve piu' il rapporto !
        
        
       
        
        
        
        
        
        
        
        
        
        
        # formula delta_1_69_39
        
        delta_1_69_39 = (ma69_last / ma39_last - 1) * 100 if ma39_last else 0
        self.algo_helper.info("delta_1_69_39: {}".format(delta_1_69_39))
        
        
        # formula delta_2_69_39
        
        delta_2_69_39 = (ma69_15_min_ago / ma39_15_min_ago - 1) * 100 if ma39_15_min_ago else 0
        self.algo_helper.info("delta_2_69_39: {}".format(delta_2_69_39))
        
        
        # formula rapporto_delta_1_delta_2_69_39
        
        rapporto_delta_1_delta_2_69_39 = (delta_1_69_39 / delta_2_69_39) if delta_2_69_39 else 0
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
        
    
        # formula DEVIATION_ma200_sotto_ma300 per comprare
        
        deviation_ma200_sotto_ma300 = (ma200_last / ma300_last - 1) * 100 if ma300_last else 0
        self.algo_helper.info("deviation_ma200_sotto_ma300: {}".format(deviation_ma200_sotto_ma300))
        
        
        
        # formula DEVIATION_MA100_LATERALE evita BUY CONTINUI DEL BUY ECCEZIONALE NELLA FASE LATERALE
        
        deviation_ma100_laterale = (ma5_last / ma100_last - 1) * 100 if ma100_last else 0
        self.algo_helper.info("deviation_ma100_laterale: {}".format(deviation_ma100_laterale))
        
        
        
        # formula DEVIATION_ma5_sotto_ma200 per comprare FINO a una certa distanza da ma200
        
        deviation_ma5_sotto_ma200 = (ma5_last / ma200_last - 1) * 100 if ma200_last else 0
        self.algo_helper.info("deviation_ma5_sotto_ma200: {}".format(deviation_ma5_sotto_ma200))
        
        
        # formula DEVIATION_ma4_sopra_ma100 - BUY 4 (parliamo del BUY 4 !) DEVE STARE a una certa distanza da ma100
        
        deviation_ma4_sopra_ma100 = (ma4_last / ma100_last - 1) * 100 if ma100_last else 0
        self.algo_helper.info("deviation_ma4_sopra_ma100: {}".format(deviation_ma4_sopra_ma100)) 
        
       
        # formula deviation_ma8_sotto_last_trade_price
        
        deviation_ma8_sotto_last_trade_price = (ma8_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.info("deviation_ma8_sotto_last_trade_price: {}".format(deviation_ma8_sotto_last_trade_price))
        
      
        # formula DEVIATION_evita_ribasso_improvviso_crollo_ferrari
        
        deviation_evita_ribasso_improvviso_crollo_ferrari = (ma3_last / ma30_last - 1) * 100 if ma30_last else 0
        self.algo_helper.info("deviation_evita_ribasso_improvviso_crollo_ferrari: {}".format(deviation_evita_ribasso_improvviso_crollo_ferrari))
        
        
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
        
      
        
        # formula deviation_ma3_sopra_ma10 (per il buy in risalita)
        
        deviation_ma3_sopra_ma10 = (ma3_last / ma10_last - 1) * 100 if ma10_last else 0
        self.algo_helper.info("deviation_ma3_sopra_ma10: {}".format(deviation_ma3_sopra_ma10))
        
        
        
        # formula DEVIATION_ma8_sotto_ma100
        
        deviation_ma8_sotto_ma100 = (ma8_last / ma100_last - 1) * 100 if ma100_last else 0
        self.algo_helper.info("deviation_ma8_sotto_ma100: {}".format(deviation_ma8_sotto_ma100))
        
        
        
        # formula DEVIATION_ma8_sotto_ma200
        
        deviation_ma8_sotto_ma200 = (ma8_last / ma200_last - 1) * 100 if ma200_last else 0
        self.algo_helper.info("deviation_ma8_sotto_ma200: {}".format(deviation_ma8_sotto_ma200))
        
        
        
        # formula DEVIATION_ma8_sotto_ma300
        
        deviation_ma8_sotto_ma300 = (ma8_last / ma300_last - 1) * 100 if ma300_last else 0
        self.algo_helper.info("deviation_ma8_sotto_ma300: {}".format(deviation_ma8_sotto_ma300))
        
        
        
        
        # formula DEVIATION_ma5_sotto_ma300
        
        deviation_ma5_sotto_ma300 = (ma5_last / ma300_last - 1) * 100 if ma300_last else 0
        self.algo_helper.info("deviation_ma5_sotto_ma300: {}".format(deviation_ma5_sotto_ma300))
        
        
        # formula DEVIATION_ma28_sotto_ma100
        
        deviation_ma28_sotto_ma100 = (ma28_last / ma100_last - 1) * 100 if ma100_last else 0
        self.algo_helper.info("deviation_ma28_sotto_ma100: {}".format(deviation_ma28_sotto_ma100))
        
        
        
        
        
        # formula DEVIATION_ma50_sotto_ma200
        
        deviation_ma50_sotto_ma200 = (ma50_last / ma200_last - 1) * 100 if ma200_last else 0
        self.algo_helper.info("deviation_ma50_sotto_ma200: {}".format(deviation_ma50_sotto_ma200))
        
        
        # formula DEVIATION_ma50_sotto_ma300
        
        deviation_ma50_sotto_ma300 = (ma50_last / ma300_last - 1) * 100 if ma300_last else 0
        self.algo_helper.info("deviation_ma50_sotto_ma300: {}".format(deviation_ma50_sotto_ma300))
        
        
        # formula DEVIATION_ma25_sotto_ma300
        
        deviation_ma25_sotto_ma300 = (ma25_last / ma300_last - 1) * 100 if ma300_last else 0
        self.algo_helper.info("deviation_ma25_sotto_ma300: {}".format(deviation_ma25_sotto_ma300))
        
        
        # formula DEVIATION_ma100_sopra_ma300
        
        deviation_ma100_sopra_ma300 = (ma100_last / ma300_last - 1) * 100 if ma300_last else 0
        self.algo_helper.info("deviation_ma100_sopra_ma300: {}".format(deviation_ma100_sopra_ma300))
       
        
        # formula DEVIATION_ma100_sopra_ma200
        
        deviation_ma100_sopra_ma200 = (ma100_last / ma200_last - 1) * 100 if ma200_last else 0
        self.algo_helper.info("deviation_ma100_sopra_ma200: {}".format(deviation_ma100_sopra_ma200))
        
        
     
        # formula DEVIATION_ma13_sopra_ma25
        
        deviation_ma13_sopra_ma25 = (ma13_last / ma25_last - 1) * 100 if ma25_last else 0
        self.algo_helper.info("deviation_ma13_sopra_ma25: {}".format(deviation_ma13_sopra_ma25))
        
        
        
        # formula DEVIATION_ma5_sopra_ma16
        
        deviation_ma5_sopra_ma16 = (ma5_last / ma16_last - 1) * 100 if ma16_last else 0
        self.algo_helper.info("deviation_ma5_sopra_ma16: {}".format(deviation_ma5_sopra_ma16))
        
        
        
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
        
        
            
        # formula DEVIATION_buy_ma2_sopra_ma5 per comprare a una certa distanza da ma5
        
        deviation_buy_ma2_sopra_ma5 = (ma2_last / ma5_last - 1) * 100 if ma5_last else 0
        self.algo_helper.info("deviation_buy_ma2_sopra_ma5: {}".format(deviation_buy_ma2_sopra_ma5))
        
        
        
        
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
            
            
            
            
            ######################################################################################################## COMPRA sessione 1
            
            # BUY 1 con "percentage" 20 -30 - x
            
            if self.session == 1:
                
            
                # ------------------------------------------------------------ BUY 1 DURANTE IL RIALZO con INCROCIO CLASSICO 69-100 and ma78 >
                
                
                if (    
                    ma20_last > ma200_last
                    and ma10_last > ma100_last
                    and deviation_ma3_sopra_ma10 > 0.13
                    
                    and ma300_last > ma300_120_min_ago
                    and ma78_last > ma78_2_min_ago
                    
                    and ma69_last > ma100_last
                    and ma3_last > ma8_last
                    and deviation_bellissima > 0.14
                    and ma6_last > ma39_last
                ):    
              
                    buy = "BUY 1 con 20>200 AND 10 > 100 AND 3-10 > 0.13 and 69 > 100 and deviation_bellissima > 0.14 and ma78 > - r 771A"
                    action = "buy"
                    percentage = 90
                    
                    
                elif (    
                    ma20_last > ma200_last
                    and ma10_last < ma100_last
                    and deviation_ma3_sopra_ma10 > 0.15
                    
                    and ma300_last > ma300_120_min_ago
                    and ma78_last > ma78_2_min_ago
                    
                    and ma69_last > ma100_last
                    and ma3_last > ma8_last
                    and deviation_bellissima > 0.14
                    and ma6_last > ma39_last
                ):    
              
                    buy = "BUY 1 con 20>200 AND 10 > 100 AND 3-10 > 0.15 and 69 > 100 and deviation_bellissima > 0.14 and ma78 > - r 771B"
                    action = "buy"
                    percentage = 90
                    
                    
                
                
                
                
                
                # BUY 1 piccola CORREZIONE FIAT = r 1226 RCCR medie mobili lunghe TUTTE IN RIALZO ! ma si verifica una correzione fiat !
                
                elif (
                    ma3_last > ma25_last
                    and ma100_last > ma100_10_min_ago
                    and ma33_last > ma78_last
                    
                    and ma100_last > ma100_120_min_ago
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    
                    and ma100_last > ma200_last
                    and ma200_last > ma300_last
                    
                    and deviation_buy_crollo_1 < -0.33
                    and deviation_buy_crollo_1 > -0.59
                    and ma2_last > ma2_2_min_ago
                    
                ):    
                    
                    buy = "BUY 1 piccola CORREZIONE FIAT = r 1226 RCCR medie mobili lunghe TUTTE IN RIALZO ! ma si verifica una correzione fiat ! - r 796 A"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                # BUY 1 piccola CORREZIONE FIAT = r 1226 RCCR medie mobili lunghe TUTTE IN RIALZO ! ma si verifica una correzione fiat !
                
                elif (
                    ma3_last > ma25_last
                    and ma100_last > ma100_10_min_ago
                    and ma33_last < ma78_last
                    
                    and deviation_ma3_sopra_ma10 > 0.12
                    and deviation_ma5_sopra_ma28 > 0.01
                    
                    and ma100_last > ma100_120_min_ago
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    
                    and ma100_last > ma200_last
                    and ma200_last > ma300_last
                    
                    and deviation_buy_crollo_1 < -0.33
                    and deviation_buy_crollo_1 > -0.59
                    and ma2_last > ma2_2_min_ago
                    
                ):    
                    
                    buy = "BUY 1 piccola CORREZIONE FIAT = r 1226 RCCR medie mobili lunghe TUTTE IN RIALZO ! ma si verifica una correzione fiat ! - r 796 B"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                # ------------------------------------------------------------ BUY 1 DURANTE IL RIALZO con INCROCIO CLASSICO 69-100 and ma78 < AND 5-28 > 0.11
                
                elif (    
                    ma20_last > ma200_last
                    and ma300_last > ma300_120_min_ago
                    and ma78_last < ma78_2_min_ago
                    and deviation_ma5_sopra_ma28 > 0.11
                    
                    and ma69_last > ma100_last
                    and ma3_last > ma8_last
                    and deviation_bellissima > 0.14
                    and ma6_last > ma39_last
                ):    
              
                    buy = "BUY 1 con 20>200 and 69 > 100 and deviation_bellissima > 0.14 and ma78 < AND 5-28 > 0.11 - r 819"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                
                
                elif (    
                    ma28_last > ma300_last
                    and ma300_last < ma300_120_min_ago
                    and ma200_last > ma200_60_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.18
                    
                    and ma69_last > ma100_last
                    and ma3_last > ma8_last
                    and deviation_bellissima > 0.12
                    and ma6_last > ma39_last
                ):    
              
                    buy = "BUY 1 con 28>300 and 69 > 100 e 200> and deviation_bellissima > 0.12 and 5-28>0.18 - r 840"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                elif (    
                    ma28_last > ma300_last
                    and ma300_last < ma300_120_min_ago
                    and ma200_last < ma200_60_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.20
                    
                    and ma69_last > ma100_last
                    and ma3_last > ma8_last
                    and deviation_bellissima > 0.14
                    and ma6_last > ma39_last
                ):    
              
                    buy = "BUY 1 con 28>300 and 69 > 100 e 200< and deviation_bellissima > 0.14 - r 859"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                    
                    
              
                # ------------------------------------------------------ BUY 1 MOLTO RISCHIOSO modo 1 ! quando incomincia il ribasso MA ma300 120 > E ma200 120 >
                  
                elif (     
                    ma300_last > ma300_120_min_ago
                    and ma200_last > ma200_120_min_ago
                    
                    and ma200_last < ma200_60_min_ago
                    and ma100_last < ma100_60_min_ago
                    
                    and ma8_last > ma78_last
                    
                    and deviation_ma3_sopra_ma10 > 0.13
                    and deviation_ma5_sopra_ma28 > 0.20
                    and deviation_bellissima > 0.10
               
                    and ma2_last >= ma2_2_min_ago
                ):     
                  
                    buy = "BUY 1 MOLTO RISCHIOSO modo 1 ! quando incomincia il ribasso MA ma300 120 > e ma200 120 > ANCORA IN RIALZO ! 3-10 > 0.13 - r 884 A"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                    
                # ------------------------------------------------------------ BUY 1 MOLTO RISCHIOSO modo 1 ! quando incomincia il ribasso MA ma300 > MA ma200 120 <
                  
                elif (     
                    ma300_last > ma300_120_min_ago
                    and ma200_last < ma200_120_min_ago
                    
                    and ma200_last < ma200_60_min_ago
                    and ma100_last < ma100_60_min_ago
                    
                    and ma8_last > ma69_last
                    
                    and deviation_ma3_sopra_ma10 > 0.12
                    and deviation_ma5_sopra_ma28 > 0.19
                    and deviation_bellissima > 0.12
               
                    and ma2_last > ma2_2_min_ago
                ):     
                  
                    buy = "BUY 1 MOLTO RISCHIOSO modo 1 ! quando incomincia il ribasso MA ma300 ANCORA IN RIALZO MA ma200 120 < con 3-10 > 0.13 - r 884 B"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                    
                    
                # ------------------------------------------------------------ BUY 1 MOLTO RISCHIOSO modo 2 ! quando incomincia il ribasso MA ma300 >
                
                elif (     
                    ma300_last > ma300_120_min_ago
                    and ma8_last > ma100_last
                    and ma28_last > ma125_last
                
                    and ma200_last < ma200_60_min_ago
                    and ma100_last < ma100_60_min_ago
                 
                    and deviation_bellissima > 0.14
                    and ma2_last > ma2_2_min_ago
                ):     
                  
                    buy = "BUY 1 MOLTO RISCHIOSO modo 2 ! quando incomincia il ribasso MA ma300> - r 905"
                    action = "buy"
                    percentage = 90
                    
                
               
                
                
                
                
                
                
                
                # ------------------------------------------------------------ BUY 1 RAFFORZATA se ma200> and ma300 > and 8>50 AND ma78 >
                
                
                elif (    
                    ma20_last > ma200_last
                    and ma50_last > ma78_last
                    and deviation_ma3_sopra_ma10 > 0.01
                    
                    and ma78_last > ma78_2_min_ago
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    and ma8_last > ma50_last
                ):  
                
                    buy = "BUY 1 RAFFORZATA (50>78) con 20>200 and 69 > 100 and deviation_bellissima > 0.14 AND ma78 > - r 931"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                    
                    
                # ------------------------------------------------------------ BUY 1 se ma200> and ma300 > and 8>50 AND ma78 >  
                
                elif (    
                    ma20_last > ma200_last
                    and ma50_last < ma78_last
                    and deviation_ma5_sopra_ma28 > 0.16
                    
                    and ma78_last > ma78_2_min_ago
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    and ma8_last > ma50_last
                ):  
                
                    buy = "BUY 1 (50<78) con 20>200 and 69 > 100 and deviation_bellissima > 0.14 AND ma78 > - r 952"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                    
                    
                    
                    
                    
                    
                # BUY 1 se ma200> and ma300 > and 8>50 AND ma78 < AND 8 > 78 AND 5-28 > 0.11 
                
                elif (    
                    ma20_last > ma125_last
                    and ma8_last > ma78_last
                    and ma78_last < ma78_2_min_ago
                    and deviation_ma5_sopra_ma28 > 0.11
                    
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    and ma8_last > ma50_last
                ):  
                
                    buy = "BUY 1 con 20>125 and 69 > 100 and deviation_bellissima > 0.14 AND ma78 > AND 8 > 78 AND 5-28 > 0.11  - r 977"
                    action = "buy"
                    percentage = 90
                    
                    # 27 giu 2022 20>125 da 20>200
                    
                    
                    
                    
                # BUY 1 se ma200> and ma300 > and 8>50 AND ma78 < AND 8 < 78 AND 5-28 > 0.17 
                
                elif (    
                    ma20_last > ma200_last
                    and ma8_last < ma78_last
                    and ma78_last < ma78_2_min_ago
                    and deviation_ma5_sopra_ma28 > 0.17
                    
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    and ma8_last > ma50_last
                ):  
                
                    buy = "BUY 1 con 20>200 and 69 > 100 and deviation_bellissima > 0.14 AND ma78 > AND 8 < 78 AND 5-28 > 0.17 - r 997"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                # BUY 1 PERICOLOSA derivata dal tardo autunno ! togliendo i 40 minuti della ma30 
                
                elif (     
                    ma8_last > ma54_last
                    and ma78_last > ma200_last
                    
                    and ma39_last > ma39_30_min_ago
                    and ma69_last >= ma69_2_min_ago
                    
                    and deviation_ma100_sopra_ma300 < -0.30
                    and ma100_last < ma200_last
                    and ma200_last < ma200_120_min_ago
                    
                    
                    and deviation_ma5_sopra_ma28 > 0.18
                    and deviation_bellissima > 0.05
                    
                    and ma20_last >= ma20_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma2_last > ma20_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 PERICOLOSA 8-54 derivata dal tardo autunno ! togliendo i 40 minuti della ma30 con 11-59 con 5-28 > 0.19 - r 1032 Aa"
                    action = "buy"
                    percentage = 90
                    
                    # 100 deve stare un po' sotto alla 300 !
                    
                    
                    
                    
                # BUY 1 PERICOLOSA derivata dal tardo autunno ! togliendo i 40 minuti della ma30 
                
                elif (     
                    ma8_last > ma54_last
                    and ma78_last < ma200_last
                    and deviation_ma5_sopra_ma28 > 0.30
                    
                    and ma39_last > ma39_30_min_ago
                    and ma69_last >= ma69_2_min_ago
                    
                    and deviation_ma100_sopra_ma300 < -0.30
                    and ma100_last < ma200_last
                    and ma200_last < ma200_120_min_ago
                    
                    
                    and deviation_ma5_sopra_ma28 > 0.18
                    and deviation_bellissima > 0.05
                    
                    and ma20_last >= ma20_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma2_last > ma20_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 PERICOLOSA 8-54 derivata dal tardo autunno ! togliendo i 40 minuti della ma30 con 11-59 con 5-28 > 0.30 - r 1032 Ab"
                    action = "buy"
                    percentage = 90
                    
                    # 100 deve stare un po' sotto alla 300 !
                    # 22 giu 2022 se 78 >200 5-28 > 0.30
                    
                    
                    
                    
                    
                    
                    
                    
                # BUY 1 PERICOLOSA derivata dal tardo autunno ! togliendo i 40 minuti della ma30 
                
                elif (     
                    ma8_last > ma54_last
                    and ma39_last > ma39_30_min_ago
                    and ma69_last < ma69_2_min_ago
                    
                    and deviation_ma100_sopra_ma300 < -0.25
                    and ma100_last < ma200_last
                    and ma200_last < ma200_120_min_ago
                    
                    
                    and deviation_ma5_sopra_ma28 > 0.19
                    and deviation_bellissima > 0.06
                    
                    and ma20_last > ma20_2_min_ago
                    and ma2_last > ma20_last
                    
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 PERICOLOSA 8-54 derivata dal tardo autunno ! con 11-59 con 5-28 > 0.19 - r 1032 B"
                    action = "buy"
                    percentage = 90
                    
                    # 100 deve stare un po' sotto alla 300 !
                    
                    
                    
                    
                # BUY 1 PERICOLOSA derivata dal tardo autunno ! togliendo i 40 minuti della ma30 
                
                elif (     
                    ma8_last > ma54_last
                    and ma78_last > ma200_last
                    
                    and ma39_last < ma39_30_min_ago
                    and deviation_ma100_sopra_ma300 < -0.27
                    and ma100_last < ma200_last
                    and ma200_last < ma200_120_min_ago
                    
                    and ma11_last > ma59_last
                    and deviation_ma5_sopra_ma28 > 0.21
                    and deviation_bellissima > 0.06
                    
                    and ma20_last > ma20_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma2_last > ma20_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 PERICOLOSA 8-54 and 39< MA 78>200 derivata dal tardo autunno ! con 5-28 > 0.20 - r 1060 A"
                    action = "buy"
                    percentage = 90
                    
                    # 100 deve stare un po' sotto alla 300 !
                    
                    
                    
                # BUY 1 PERICOLOSA derivata dal tardo autunno ! togliendo i 40 minuti della ma30 
                
                elif (     
                    ma8_last > ma54_last
                    and ma78_last < ma200_last
                    and ma39_last < ma39_30_min_ago
                    and deviation_ma100_sopra_ma300 < -0.27
                    and ma100_last < ma200_last
                    and ma200_last < ma200_120_min_ago
                    
                    and ma11_last > ma59_last
                    and deviation_ma5_sopra_ma28 > 0.27
                    and deviation_bellissima > 0.06
                    
                    and ma20_last > ma20_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma2_last > ma20_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 PERICOLOSA 8-54 and 39< AND 78 < 200 derivata dal tardo autunno ! togliendo i 40 minuti della ma30 e con 5-28 > 0.27 - r 1060 B"
                    action = "buy"
                    percentage = 90
                    
                    # 100 deve stare un po' sotto alla 300 !
                    # 22 GIU 2022 5-28 > 0.27 da 0.20
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                #################################################################################################################### ecco le 4 stagioni !  
                
                
                # BUY 1 tempo ESTATE PIU' LENTA 100 < 60 min ago considera il passare del tempo ! ma30 > 
                
                elif (     
                    ma50_last > ma100_last
                    and ma100_last > ma200_last
                    and ma100_last < ma100_60_min_ago
                    
                    and ma30_last > ma30_40_min_ago
                
                    and deviation_ma5_sopra_ma28 > 0.15
                    and deviation_bellissima > 0.06
                    and ma20_last > ma20_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma2_last > ma20_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 tempo ESTATE PIU' LENTA 100 > 60 min ago considera il passare del tempo ! ma30 > - r 1100"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                    
                # BUY 1 tempo ESTATE PIU' VELOCE 100 > 60 min ago (solo l' estate se lo puo' perettere!) considera il passare del TEMPO ! ma30 > 
                
                elif (     
                    ma15_last > ma28_last
                    and ma8_last > ma200_last
                    and ma100_last > ma100_60_min_ago
                    
                    and ma30_last > ma30_40_min_ago
                
                    and deviation_ma5_sopra_ma28 > 0.15
                    and deviation_bellissima > 0.06
                    and ma20_last > ma20_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma2_last > ma20_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 tempo ESTATE PIU' VELOCE 100 > 60 min ago (solo l' estate se lo puo' permettere!) considera il passare del tempo ! ma30 > - r 1123"
                    action = "buy"
                    percentage = 90
                    
                    # 9 giu 2022 15>28 al posto di 50>100 
                    # 9 giu 2022 8>200 al posto di 100>200
                    
                    
                    
                    
                
                
                # BUY 1 tempo PRIMAVERA che considera il passare del tempo con ma30 < 
                
                elif (     
                    ma50_last > ma100_last
                    and ma100_last > ma200_last
                    and deviation_buy_ma2_sopra_ma5 > 0.12
                    
                    and ma30_last < ma30_40_min_ago
                 
                    and deviation_ma5_sopra_ma28 > 0.175
                    and deviation_bellissima > 0.06
                    and ma2_last > ma20_last
                    and ma5_last >= ma5_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    
                ):    
                    buy = "BUY 1 tempo PRIMAVERA che considera il passare del tempo con deviation_bellissima > 0.06 and deviation_ma5_sopra_ma28 > 0.18 - r 1151"
                    action = "buy"
                    percentage = 90
                    
                    
                
                    
                
                
                
                
                # BUY 1 tempo INIZIO AUTUNNO (200 > 200 120 min) che considera il passare del tempo con ma30 > MA 100 < 200
                
                elif (     
                    ma50_last > ma100_last
                    and ma200_last > ma200_120_min_ago
                    and deviation_ma5_sopra_ma28 > 0.17
                    and ma100_last < ma200_last
                    
                    and ma30_last > ma30_40_min_ago
                    
                    and ma11_last > ma125_last
                    
                    
                    and deviation_bellissima > 0.06
                    and ma20_last > ma20_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma2_last > ma20_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 tempo INIZIO AUTUNNO (200 > 200 120 min ago) che considera il passare del tempo con 5-28 > 0.17 - r 1181"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                    
                # BUY 1 tempo FINE AUTUNNO PRECEDENTE(quasi inverno !)
                
                elif (     
                    ma50_last > ma69_last
                    and ma200_last < ma200_120_min_ago
                    and ma100_last < ma200_last
                    
                    and ma30_last > ma30_30_min_ago
                    and ma11_last > ma125_last
                    
                    and deviation_ma5_sopra_ma28 > 0.20
                    and deviation_bellissima > 0.06
               
                    and ma20_last > ma20_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma2_last > ma20_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 PERICOLOSA tempo FINE AUTUNNO LENTO (quasi inverno !) con 50-78 che considera il passare del tempo con 5-28 > 0.20 - r 1206"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                    
                # BUY 1 tempo FINE AUTUNNO (quasi inverno !)
                
                elif (     
                    ma8_last > ma50_last
                    and ma30_last > ma30_40_min_ago
                    
                    and ma8_last < ma100_last
                    and ma8_last < ma200_last
                    and ma8_last < ma300_last
                    
                    and ma200_last < ma200_120_min_ago
                    and ma100_last < ma200_last
                    
                    and deviation_ma50_sotto_ma200 < -0.22
              
                    and deviation_ma5_sopra_ma28 > 0.20
                    
                    
                    and ma11_last > ma125_last
                    
                    
                    and deviation_bellissima > 0.06
                    and ma20_last > ma20_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma2_last > ma20_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 PERICOLOSA tempo FINE AUTUNNO VELOCE (quasi inverno !) con 50-78 che considera il passare del tempo con 5-28 > 0.20 - r 1241"
                    action = "buy"
                    percentage = 80
                    
                    # 50-78 PRIMA ERA 50-100 (arrivava un po' tardi.) (questa era la mia impressione.)
                    # 8>50
                    
                    
                    ################################################################################################ fine autunno
                    
              
                
                
                
                
                
                
                
                
                # BUY 1 tempo INVERNO che considera il passare del tempo con ma30 < MA 100 < 200
                
                elif (     
                    ma50_last > ma100_last
                    and ma100_last < ma200_last
                    
                    and ma30_last < ma30_40_min_ago
                    
                    and ma11_last > ma125_last
                    
                    and deviation_ma3_sopra_ma10 > 0.09
                    and deviation_ma5_sopra_ma28 > 0.175
                    and deviation_bellissima > 0.06
                    and ma2_last > ma20_last
                    and ma5_last >= ma5_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    
                ):    
                    buy = "BUY 1 tempo INVERNO che considera il passare del tempo con dev_bellissima > 0.06 and dev_ma5_sopra_ma28 > 0.18 E 3-10 > 0.09 - r 1276"
                    action = "buy"
                    percentage = 90
                    
                    
                
                    
                    
                # BUY 1 con ma200 < 300< MA ma100> 100 60 min ago e doppio delta < and ma100 >60_min_ago STA RISALENDO !
            
                elif (       
                    ma200_last < ma200_20_min_ago
                    and ma11_last > ma125_last
                    and ma2_last > ma2_2_min_ago
                    and deviation_ma5_sopra_ma28 > 0.15
                    
                    
                    and delta_1 < delta_2
                    and ma100_last > ma100_60_min_ago
                    
                    and ma200_last < ma200_60_min_ago
                    and ma300_last < ma300_60_min_ago
                ):    
        
                    buy = "BUY 1 11-125 con ma200< 300< MA ma100> 100 60 min ago e doppio delta < MA ma100 > - GIORNO ! - riga 1300"
                    action = "buy"
                    percentage = 90
                    
                    # 11-150 perche' doppio delta sta risalendo !
                    # MA HO DOVUTO AGGIUNGERE and deviation_ma5_sopra_ma28 > 0.20
                    
                    # 14 giu 2022 11-125 da 11-150 (giorno!)
                    
                    
                    
                    
                    
                    
                    
                    
                    
                # BUY 1 MISTERO CON 8>50 E 5-28 PIU' ALTO ! per arrivare una ndecchia prima del passare del tempo. prendendo rischio
                
                elif (
                    deviation_ma5_sopra_ma28 > 0.30
                    and ma8_last > ma54_last
                    
                    and deviation_ma100_sopra_ma200 > -0.60
                    and deviation_ma50_sotto_ma200 < -0.15
                    
                    and ma100_last < ma100_60_min_ago
                    and ma200_last < ma200_60_min_ago
                    and ma300_last < ma300_60_min_ago
                    
                    
                    and deviation_ma13_sopra_ma25 > 0.04
                    and deviation_ma3_sopra_ma7 > 0.04
                    
                    and ma2_last >= ma2_2_min_ago
              
                ):
                    buy = "BUY 1 MISTERO CON 8>54 E 5-28 PIU' ALTO ! per arrivare una ndecchia prima del passare del tempo prendendo rischio - riga 1337"
                    action = "buy"
                    percentage = 90
                    
                    # ma100 sta sotto la ma200 MA non le e' troppo lontana cioe' NON ci troviamo in una situazione drammatica! ( anche se ma100< e ma200< e ma300< )
                    # MISTERO !
                    
                    
                    
                    
                    
                # BUY 1 MISTERO con INCROCIO 8-50 E 5-28 PIU' BASSO per arrivare una ndecchia prima del passare del tempo. prendendo rischio
                
                elif (
                    
                    deviation_ma5_sopra_ma28 > 0.24
                    and ma78_last > ma200_last
                    and delta_1_200_78 < delta_2_200_78_60_min
                    
                    and (ma8_prev < ma50_prev and ma8_last > ma50_last)
                    and deviation_ma100_sopra_ma200 > -0.60
                    and deviation_ma50_sotto_ma200 < -0.15
                    
                    and deviation_ma100_sopra_ma300 > -0.80
                    
                    and ma100_last < ma100_60_min_ago
                    and ma200_last < ma200_60_min_ago
                    and ma300_last < ma300_60_min_ago
                    
                    
                    and deviation_ma13_sopra_ma25 > 0.06
                    and deviation_ma3_sopra_ma7 > 0.04
                    
                    and ma2_last >= ma2_2_min_ago
              
                ):
                    buy = "BUY 1 MISTERO con INCROCIO 8-50 e 5-28 > 0.28 prendendo rischio - E CON delta 200-78 - RIALZO - riga 1368 AA"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                    
                    
                    
                    
                # BUY 1 MISTERO con INCROCIO 8-50 E 5-28 PIU' BASSO per arrivare una ndecchia prima del passare del tempo. prendendo rischio
                
                elif (
                    
                    deviation_ma5_sopra_ma28 > 0.24
                    and ma78_last < ma200_last
                    and deviation_ma3_sopra_ma10 > 0.11
                    
                    and delta_1_200_78 < delta_2_200_78_60_min
                    
                    and (ma8_prev < ma50_prev and ma8_last > ma50_last)
                    and deviation_ma100_sopra_ma200 > -0.60
                    and deviation_ma50_sotto_ma200 < -0.15
                    
                    and deviation_ma100_sopra_ma300 > -0.80
                    
                    and ma100_last < ma100_60_min_ago
                    and ma200_last < ma200_60_min_ago
                    and ma300_last < ma300_60_min_ago
                    
                    
                    and deviation_ma13_sopra_ma25 > 0.06
                    and deviation_ma3_sopra_ma7 > 0.04
                    
                    and ma2_last >= ma2_2_min_ago
              
                ):
                    buy = "BUY 1 MISTERO con INCROCIO 8-50 e 5-28 > 0.28 prendendo rischio - E CON delta 200-78 - RIALZO - riga 1368 AB"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                    
                    
                    
                    
                    
                # BUY 1 MISTERO con INCROCIO 8-50 E 5-28 PIU' BASSO per arrivare una ndecchia prima del passare del tempo. prendendo rischio
                
                elif (
                    
                    deviation_ma5_sopra_ma28 > 0.24
                    and delta_1_200_78 > delta_2_200_78_60_min
                    and deviation_ma3_sopra_ma10 > 0.22
                    
                    and (ma8_prev < ma50_prev and ma8_last > ma50_last)
                    and deviation_ma100_sopra_ma200 > -0.60
                    and deviation_ma50_sotto_ma200 < -0.15
                    
                    and deviation_ma100_sopra_ma300 > -0.80
                    
                    and ma100_last < ma100_60_min_ago
                    and ma200_last < ma200_60_min_ago
                    and ma300_last < ma300_60_min_ago
                    
                    
                    and deviation_ma13_sopra_ma25 > 0.06
                    and deviation_ma3_sopra_ma7 > 0.04
                    
                    and ma2_last >= ma2_2_min_ago
              
                ):
                    buy = "BUY 1 MISTERO con INCROCIO 8-50 e 5-28 > 0.28 prendendo rischio - E CON delta 200-78 - RIBASSO - riga 1368 B"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                # BUY 1 MISTERO con INCROCIO 8-50 E 5-28 PIU' BASSO per arrivare una ndecchia prima del passare del tempo. prendendo rischio
                
                elif (
                    
                    deviation_ma5_sopra_ma28 > 0.14
                    and (ma8_prev < ma50_prev and ma8_last > ma50_last)
                    and deviation_ma100_sopra_ma200 > -0.60
                    and deviation_ma50_sotto_ma200 < -0.15
                    
                    and deviation_ma100_sopra_ma300 < -0.80
                    
                    and ma100_last < ma100_60_min_ago
                    and ma200_last < ma200_60_min_ago
                    and ma300_last < ma300_60_min_ago
                    
                    
                    and deviation_ma13_sopra_ma25 > 0.06
                    and deviation_ma3_sopra_ma7 > 0.04
                    
                    and ma2_last >= ma2_2_min_ago
              
                ):
                    buy = "BUY 1 MISTERO (sembra BUY FIAT) con INCROCIO 8-50 e 5-28 > 0.14 arrivare ndecchia prima del passare del tempo - rischiosa - riga 1397"
                    action = "buy"
                    percentage = 80
                    
                    # ma100 sta sotto la ma200 MA non le e' troppo lontana cioe' NON ci troviamo in una situazione drammatica! ( anche se ma100< e ma200< e ma300< )
                    # MISTERO !
                    
                    
                
                
                
                
                
                
                
                
                
                
                
                # BUY 1 copiata e modificata da RCCR che e' arrivata una ndecchia prima del passare del tempo.
                
                elif (
                    
                    ma8_last > ma140_last
                    and deviation_ma100_sopra_ma200 > -0.30
                    and ma20_last > ma200_last
                    
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
                    buy = "BUY 1 8-140 copiata e modificata da RCCR che e' arrivata una ndecchia prima del passare del tempo -20>200 - riga 1437 a"
                    action = "buy"
                    percentage = 80
                    
                    # importante : ma100 sta sotto la ma200 non le e' troppo lontana cioe' NON ci troviamo in una situazione drammatica! (anche se ma200< e ma300<)
                    # 20 maggio 2020 messo ma140 prima era ma150
                    
                    
                    
                # BUY 1 copiata e modificata da RCCR che e' arrivata una ndecchia prima del passare del tempo.
                
                elif (
                    
                    ma8_last > ma140_last
                    and deviation_ma100_sopra_ma200 > -0.30
                    and ma20_last < ma200_last
                    and deviation_ma5_sopra_ma28 > 0.18
                    
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
                    buy = "BUY 1 8-140 copiata e modificata da RCCR che e' arrivata una ndecchia prima del passare del tempo - 20<200 AND 5-28 > 0.18 - riga 1437 b"
                    action = "buy"
                    percentage = 80
                    
                    # importante : ma100 sta sotto la ma200 non le e' troppo lontana cioe' NON ci troviamo in una situazione drammatica! (anche se ma200< e ma300<)
                    # 20 maggio 2020 messo ma140 prima era ma150
                    
                
                
                
                
                
                
                
                
                
                
                
                # ------------------------------------------------------------  BUY 1 con incrocio 11-69 and ma69_last >= ma69_2_min_ago  "MI PIACE!"
                
                elif (
                    ma20_last > ma200_last
                    and ma11_last > ma50_last
                    and ma69_last >= ma69_2_min_ago
                    and ma300_last > ma300_120_min_ago
                    
                    and deviation_bellissima > 0.16
                    and price > price_2_min_ago
                    and ma3_last > ma3_3_min_ago
                    
                    and deviation_ma3_sopra_ma7 > 0.05
                    and deviation_ma13_sopra_ma25 > 0.06
                 
                ):
                    buy = "BUY 1 con ma20_last > ma200_last e con 11 > 59 e ma69> 2 min ago (!) r 1471"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                elif (
                    ma20_last > ma200_last
                    and ma11_last > ma50_last
                    and ma69_last >= ma69_2_min_ago
                    and ma300_last < ma300_120_min_ago
                    and deviation_ma5_sopra_ma28 > 0.24
                    
                    and deviation_bellissima > 0.17
                    and price > price_2_min_ago
                    
                    and ma3_last > ma3_3_min_ago
                    and ma4_last > ma4_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                    and deviation_ma13_sopra_ma25 > 0.06
                 
                ):
                    buy = "BUY 1 con ma20_last > ma200_last e con 11 > 59 e ma69> 2 min ago (!) r 1494"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                # buy1 r913 anticipata e modificata sta risalendo
                
                elif (
                    ma100_last > ma200_last
                    and ma100_last > ma300_last
                    and ma100_last > ma100_120_min_ago
                    
                    
                    and delta_1 < delta_2
                    and ma100_last > ma100_60_min_ago
                    
                    and ma11_last > ma50_last
                    
                    and deviation_bellissima > 0.17
                    and price > price_2_min_ago
                    
                    and ma3_last > ma3_3_min_ago
                    and ma4_last > ma4_2_min_ago
                    and deviation_ma3_sopra_ma7 > 0.05
                    and deviation_ma13_sopra_ma25 > 0.06
                 
                ):
                    buy = "BUY 1 r913 anticipata e modificata e con 11 > 50 - SOPRA RIALZO RIALZO - GIORNO - r 1538"
                    action = "buy"
                    percentage = 80
                    
           
        
        
                
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
                    buy = "BUY 1 con 11-69 SE ma200 SALE DA 2 ORE ! - r 1562"
                    action = "buy"
                    percentage = 80
                    
                    
                    
           
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
                    buy = "BUY 1 con 13>50 and DEVIATION BUY 1 ALTA e ma78> - r 1579"
                    action = "buy"
                    percentage = 80
                    
               
            
            
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
                    buy = "BUY 1 con ma78< and 39>78 and DEVIATION BUY 1 BASSA r 1597"
                    action = "buy"
                    percentage = 80
                    
                    
               
            
            
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

                    buy = "BUY 1 se ma78< - BUY 1 con incrocio 39>78 - r 1617"
                    action = "buy"
                    percentage = 80
                    
                    
                
                
                ############################################################################### compra durante un rialzo improvviso ! PER ADESSO SOLO SUL BUY 1
                ############################################################################### con ma30 che ha 30 min di andamento laterale
                
                
                elif (
                    ma200_last > ma200_20_min_ago
                    and ma300_last > ma300_120_min_ago
                    and deviation_ma100_sopra_ma300 > 0.50
                    
                    and deviation_rialzo_improvviso_sopra > 0.45
                    and deviation_rialzo_improvviso_1 > 0.45
                    and deviation_rialzo_improvviso_2 > 0.19
                    and deviation_rialzo_improvviso_3 > 0.19
                    and deviation_range_1 < 0.22
                    and deviation_range_1 > -0.22
                    and deviation_range_2 < 0.22
                    and deviation_range_2 > -0.22
                    and deviation_range_x < 0.22
                    and deviation_range_x > -0.22
                ):
             
                    buy = "BUY 1 RIALZO IMPROVVISO con ma200 > E 300 > 120 min ago e con > 0.45 SE MA100 MOLTO IN ALTO DA MA300 - r 1641 AA"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                elif (
                    ma200_last > ma200_20_min_ago
                    and ma300_last > ma300_120_min_ago
                    and deviation_ma100_sopra_ma300 < 0.50
                    
                    and deviation_rialzo_improvviso_sopra > 0.46
                    and deviation_rialzo_improvviso_1 > 0.46
                    and deviation_rialzo_improvviso_2 > 0.19
                    and deviation_rialzo_improvviso_3 > 0.19
                    and deviation_range_1 < 0.22
                    and deviation_range_1 > -0.22
                    and deviation_range_2 < 0.22
                    and deviation_range_2 > -0.22
                    and deviation_range_x < 0.22
                    and deviation_range_x > -0.22
                ):
             
                    buy = "BUY 1 RIALZO IMPROVVISO con ma200 > E 300 > 120 min ago e con > 0.46 - r 1641 AB"
                    action = "buy"
                    percentage = 90
                 
                    # deviation_rialzo_improvviso_sopra = price / ma200_last
                    # deviation_rialzo_improvviso_1 = price / ma30_last
                    # deviation_rialzo_improvviso_2 = price / ma30_10_min_ago
                    # deviation_rialzo_improvviso_3 = price / ma30_20_min_ago
                    # deviation_range_1 = ma30_last / ma30_10_min_ago
                    # deviation_range_2 = ma30_10_min_ago / ma30_20_min_ago
                    # deviation_range_x = ma30_last / ma30_20_min_ago
                    
                    
                    
                
                
                
                
                
                
                
                
                
                
                
                elif (
                    ma200_last > ma200_20_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and deviation_rialzo_improvviso_sopra > 0.50
                    and deviation_rialzo_improvviso_1 > 0.50
                    and deviation_rialzo_improvviso_2 > 0.19
                    and deviation_rialzo_improvviso_3 > 0.19
                    and deviation_range_1 < 0.22
                    and deviation_range_1 > -0.22
                    and deviation_range_2 < 0.22
                    and deviation_range_2 > -0.22
                    and deviation_range_x < 0.22
                    and deviation_range_x > -0.22
                ):
             
                    buy = "BUY 1 RIALZO IMPROVVISO con ma200 > E 300 > 120 min ago e con > 0.50 - r 1641 B"
                    action = "buy"
                    percentage = 90
                 
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
              
                    buy = "BUY 1 variazione 1 RIALZO con 20-69 - r 1667"
                    action = "buy"
                    percentage = 80
                 
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

                    buy = "BUY 1 variazione 2 RIALZO con 20-100 - r 1690"
                    action = "buy"
                    percentage = 80
                    
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

                    buy = "BUY 1 variazione 3 RIALZO con 20-200 - r 1713"
                    action = "buy"
                    percentage = 80
                    
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

                    buy = "BUY 1 RIALZO IMPROVVISO con 78 < ( da 1.20 a 1.1 !) sempre tentando di evitare falsi acquisti - r 1747"
                    action = "buy"
                    percentage = 90
                    
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
                    and ma28_last > ma28_30_min_ago
                    
                    and deviation_buy_crollo_1 < -0.33
                    and deviation_buy_crollo_1 > -0.69
                    and ma3_last > ma28_last
                    and ma5_last > ma100_last
                ):    
                    
                    buy = "BUY 1A con ma200> piccola CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo - r 1788 A"
                    action = "buy"
                    percentage = 80
                    
                    # and ma3_last > ma100_last PERCHE' in questa circostanza 3-28 arriva tardi e mi proteggo
                    # dovrei fare 2-5 MA SAREBBE TROPPO RISCHIOSO perche' ma100 gia' e' in ribasso !
                    
                    
                    
                    
                # BUY 1 con ma200> piccola CORREZIONE FIAT che NON E' un forte ribasso e NON E' un crollo ! CON ma28 < E CON 5-28 > 0.13 (compare stammi vicino!)
               
                elif (
                    ma2_last > ma2_2_min_ago
                    and ma200_last > ma200_120_min_ago
                    and ma28_last < ma28_30_min_ago
                    and deviation_ma5_sopra_ma28 > 0.13
                    
                    and deviation_buy_crollo_1 < -0.33
                    and deviation_buy_crollo_1 > -0.69
                    and ma3_last > ma28_last
                    and ma5_last > ma100_last
                ):    
                    
                    buy = "BUY 1A con ma200> piccola CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo CON ma28 < E CON 5-28 > 0.13 - r 1788 B"
                    action = "buy"
                    percentage = 80
                    
                    # and ma3_last > ma100_last PERCHE' in questa circostanza 3-28 arriva tardi e mi proteggo
                    # dovrei fare 2-5 MA SAREBBE TROPPO RISCHIOSO perche' ma100 gia' e' in ribasso !
                    
                    
                    
                    
                    
                    
                
                
                # BUY 1 con ma300 > piccola CORREZIONE FIAT che NON E' AUDI e non e' MASERATI e NON E' FERRARI ! (compare stammi vicino!)
              
                elif (

                    ma2_last > ma2_2_min_ago
                    and ma300_last > ma300_120_min_ago
                    and deviation_buy_crollo_1 < -0.33
                    and deviation_buy_crollo_1 > -0.69
                    and deviation_correzione > 0.012
                    and ma5_last > ma72_last
                ):

                    buy = "BUY 1 con ma300 > piccola CORREZIONE FIAT che NON E' una grande correzione AUDI e non e' MASERATI e NON E' FERRARI ! - r 1811"
                    action = "buy"
                    percentage = 80

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
                    and ma100_last > ma100_10_min_ago
                    
                    and ma100_last > ma100_120_min_ago
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    
                    and ma100_last > ma200_last
                    and ma200_last > ma300_last
                    
                    and deviation_buy_crollo_1 < -0.33
                    and deviation_buy_crollo_1 > -0.69
                    and ma2_last > ma2_2_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.10
                    
                ):    
                    
                    buy = "BUY 1 piccola CORREZIONE FIAT = r 995 RCCR medie mobili lunghe TUTTE IN RIALZO ! ma si verifica una correzione fiat ! - r 1854"
                    action = "buy"
                    percentage = 80
                    
                    
                
                
                # BUY 1 piccola CORREZIONE FIAT = r 995 RCCR medie mobili lunghe TUTTE IN RIALZO MA ma100 COMINCIA A RIPIEGARE ! correzione fiat
                
                elif (
                    ma3_last > ma25_last
                    
                    and ma100_last < ma100_10_min_ago
                    and ma11_last > ma100_last
                    
                    and ma100_last > ma100_120_min_ago
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    
                    and ma100_last > ma200_last
                    and ma200_last > ma300_last
                    
                    and deviation_buy_crollo_1 < -0.33
                    and deviation_buy_crollo_1 > -0.69
                    and ma2_last > ma2_2_min_ago
                    
                ):    
                    
                    buy = "BUY 1 piccola CORREZIONE FIAT = r 995 RCCR medie mobili lunghe TUTTE IN RIALZO MA ma100 COMINCIA A RIPIEGARE ! correzione fiat ! - r 1882"
                    action = "buy"
                    percentage = 80
                    
                    
             
                ################################################################################################### ecco le 2 CONDIZIONI PIU' PERICOLOSE !
                
               
                # BUY 1 DURANTE UNA CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo ! (MA ma3 > ma150 mi protegge un po')
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
                    and deviation_correzione > 0.03
                    and ma100_last > ma300_last
                    and ma5_last > ma100_last
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 DURANTE UNA CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo ! ma100>300 5 > ma100 - riga 1902"
                    action = "buy"
                    percentage = 80
                    
                    
                # BUY 1 DURANTE UNA CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo ! (MA ma3 > ma150 mi protegge un po')
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
                    and deviation_correzione > 0.03
                    
                    and ma100_last < ma300_last
                    and ma5_last > ma125_last
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 DURANTE UNA CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo ! ma100<300 ma5 > ma125 - riga 1919"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                    
                    
                    
                
                
                    
                # BUY 1 FIAT problematica CHE FA PAURA ! ( ma la ma100 E' ANCORA VICINA alla ma300 !) NON TOCCARE 5-28 > 0.10 !
                # ( E ANCHE la ma25 deve stare un po' distante dalla 300 !!! )
                
                elif (
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
                    
                    and ma11_last > ma125_last
                    
                    and deviation_correzione > 0.03
                    and deviation_ma5_sopra_ma28 > 0.05
                    and deviation_ma100_sopra_ma300 > -0.30
                    and deviation_ma25_sotto_ma300 < -0.60
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 FIAT problematica CHE FA PAURA ! 11-125 (MA ma100 E' ANCORA VICINA alla ma300) (E CON ma25 un po' distante dalla ma300) - riga 1947"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_ma100_sopra_ma300 significa 100/300 ( ma100 ancora NON SI E' ALLONTANATA TROPPO DALLA ma300 )
                    # deviation_ma25_sotto_ma300 significa che anche ma25 deve andare almeno un po' sotto ma300 (per evitare piccole schegge rialziste !)
                    # NON TOCCARE 5-28 > 0.05 !
                    # ho dovuto aggiungere 5-125 per inibirla. SOLO PROBLEMI !
               
                ############################################################################################################################################## 
                
                
                # BUY 1 piccola CORREZIONE FIAT = r 701 RCCR ma con rischio ridotto !
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
                    and ma78_last > ma200_last
                    
                    and deviation_ma3_sopra_ma10 > 0.12
                    
                    
                    and ma13_last > ma50_last
                    and ma20_last > ma20_22_min_ago
                    and ma2_last > ma2_2_min_ago
                ):    
                
                    buy = "BUY 1 piccola CORREZIONE FIAT 78>200 = r 701 RCCR ma con rischio ridotto ! 3-10 > 0.12 cazzo ! - r 1971 a"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                # BUY 1 piccola CORREZIONE FIAT = r 701 RCCR ma con rischio ridotto !
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
                    and ma78_last < ma200_last
                    
                    and deviation_ma3_sopra_ma10 > 0.12
                    and deviation_ma5_sopra_ma28 > 0.12
                    
                    and ma13_last > ma50_last
                    and ma20_last > ma20_22_min_ago
                    and ma2_last > ma2_2_min_ago
                ):    
                
                    buy = "BUY 1 piccola CORREZIONE FIAT 78<200 = r 701 RCCR ma con rischio ridotto ! 3-10 > 0.12 cazzo ! AND 5-28>0.12 - r 1971 b"
                    action = "buy"
                    percentage = 80
                    
                   
                
                    
                # BUY 1 piccola CORREZIONE FIAT che non e' una grande correzione AUDI e non e' un forte ribasso MASERATI e non e' un crollo FERRARI !
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
                    
                    and deviation_ma5_sopra_ma28 > 0.07
                    
                    and deviation_correzione > 0.02
                    and ma5_last > ma100_last
                    and deviation_ma20_laterale > -0.15
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 piccola CORREZIONE FIAT che non e' una grande correzione AUDI e non e' un forte ribasso MASERATI e non e' FERRARI ! - r 1989"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    # deviation_ma20_laterale > -0.15 cioe' ma20 ( una ma di breve termine) da ben 60 minuti non perde !
                    
                    # compare prega per me !
                    
                    
                    
                # BUY 1 piccola CORREZIONE FIAT 5-50 che NON E' una grande correzione e non e' un grande ribasso e NON E' un crollo !
                
                elif (
                    ma2_last > ma2_2_min_ago
                    
                    and deviation_ma3_sopra_ma10 > 0.145
                    and ma8_last > ma28_last
                    
                    and deviation_ma100_sopra_ma300 > -0.30
                    
                    and deviation_ma8_sotto_ma100 < -0.50
                    and deviation_buy_crollo_1 > -0.69
                ): 
            
                    buy = "BUY 1 piccola CORREZIONE 100 VICINA 300 FIAT 8-28 che NON E' grande correzione e non e' grande ribasso e NON E' un crollo ! - r 2013"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                # BUY 1 piccola CORREZIONE FIAT 5-50 che NON E' una grande correzione e non e' un grande ribasso e NON E' un crollo !
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and ma8_last > ma50_last
                    and deviation_ma5_sopra_ma28 > 0.20
                    and deviation_ma100_sopra_ma300 < -0.30
                    
                    and deviation_ma8_sotto_ma100 < -0.50
                    and deviation_buy_crollo_1 > -0.69
                    
                    and delta_1 < delta_2
                    and deviation_ma3_sopra_ma10 > 0.05
                ): 
            
                    buy = "BUY 1 FIAT con delta1 < delta2 and 3-10 > 0.05 and 5-28 > 0.20 e con 8-50 e con ma100 LONTANA 300 - r 2030 A"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                # BUY 1 piccola CORREZIONE FIAT 5-50 che NON E' una grande correzione e non e' un grande ribasso e NON E' un crollo !
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and ma8_last > ma50_last
                    and deviation_ma5_sopra_ma28 > 0.20
                    and deviation_ma100_sopra_ma300 < -0.30
                    
                    and deviation_ma8_sotto_ma100 < -0.50
                    and deviation_buy_crollo_1 > -0.69
                    
                    and delta_1 > delta_2
                    and deviation_ma3_sopra_ma10 > 0.17
                ): 
            
                    buy = "BUY 1 FIAT con delta1 > delta2 and 3-10 > 0.17 and 5-28 > 0.20 e con 8-50 e con ma100 LONTANA 300 - r 2030 B"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                
                
                
                
                
                
                # BUY 1 con ma200> piccola CORREZIONE FIAT che NON E' un forte ribasso e NON E' un crollo ! ALTRA RIGA RCCR che e' andata bene.
                
                elif (    
                    
                    ma200_last > ma200_20_min_ago
                    and deviation_ma5_sopra_ma28 > 0.165
                    and ma28_last > ma28_2_min_ago
                    
                    and ma3_last > ma28_last
                    and ma2_last > ma2_2_min_ago
                    
                    and ma100_last > ma200_last
                    and ma200_last > ma300_last
                    
                    and ma100_last > ma100_60_min_ago
                    and ma200_last > ma200_60_min_ago
                    and ma300_last > ma300_60_min_ago
             
                ):    
                    
                    buy = "BUY 1 con 200 > con 5-28> 0.165 and ma28_last > ma28_2_min_ago - riga 2062"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                
                
                
                
                
                # BUY 1 con ma200> piccola CORREZIONE FIAT che NON E' un forte ribasso e NON E' un crollo ! ALTRA RIGA RCCR che e' andata bene.
                
                elif (    
                    
                    ma200_last > ma200_20_min_ago
                    and ma28_last > ma28_30_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.19
                    and ma28_last < ma28_2_min_ago
                    
                    and ma3_last > ma28_last
                    and ma2_last > ma2_2_min_ago
                    
                    and ma100_last > ma200_last
                    and ma200_last > ma300_last
                    
                    and ma100_last > ma100_60_min_ago
                    and ma200_last > ma200_60_min_ago
                    and ma300_last > ma300_60_min_ago
             
                ):    
                    
                    buy = "BUY 1 con 200 > con 5-28> 0.19 and ma28_last < ma28_2_min_ago and ma28_last > ma28_30_min_ago - riga 2095"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                # BUY 1 con ma200> piccola CORREZIONE FIAT che NON E' un forte ribasso e NON E' un crollo ! ALTRA RIGA RCCR che e' andata bene.
                
                elif (    
                    
                    ma200_last > ma200_20_min_ago
                    and ma28_last < ma28_30_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.25
                    and ma28_last < ma28_2_min_ago
                    
                    and ma3_last > ma28_last
                    and ma2_last > ma2_2_min_ago
                    
                    and ma100_last > ma200_last
                    and ma200_last > ma300_last
                    
                    and ma100_last > ma100_60_min_ago
                    and ma200_last > ma200_60_min_ago
                    and ma300_last > ma300_60_min_ago
             
                ):    
                    
                    buy = "BUY 1 con 200 > con 5-28> 0.19 and ma28_last < ma28_2_min_ago and ma28_last < ma28_30_min_ago - riga 2123"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                    
                    
                    
                 
                
                # BUY 1 piccola CORREZIONE FIAT 5-39 ma con ma5 piu' distante da ma200 che NON E' un grande ribasso e NON E' un crollo ! STA RISALENDO
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and ma5_last > ma34_last
                    and deviation_ma5_sopra_ma28 > 0.175
                    and deviation_ma5_sotto_ma200 < -0.85
                    
                    and rapporto_delta_1_delta_2_69_39 < 1
                    and ma39_last > ma39_30_min_ago
                    
                    and ma100_last > ma100_60_min_ago
                    
                    and deviation_ma8_sotto_ma100 < -0.50
                    and deviation_buy_crollo_1 > -0.69
                ): 
            
                    buy = "BUY 1 CORREZIONE FIAT 5-34 ma con ma5 piu' distante da ma200 - SOTTO RIALZO RIALZO - GIORNO ! - r 2152"
                    action = "buy"
                    percentage = 80
                    
                    # 5-28 se non c'e' un minimo di accelerazione che cazzo mi compri !
                    # CORREZIONE FIAT NON E' un grande ribasso e NON E' un crollo 

                    
                
                
                
                # BUY 1 con ma200 < e ma300 < piccola CORREZIONE FIAT che NON E' un forte ribasso e NON E' un crollo !
                
                elif (

                    ma2_last > ma2_2_min_ago
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    and ma11_last > ma69_last
                    
                    and deviation_buy_crollo_1 < -0.33
                    and deviation_buy_crollo_1 > -0.69
                    
                ):

                    buy = "BUY 1 con ma200< e ma300< piccola CORREZIONE FIAT che NON E'una grande correzione e NON E' un grande ribasso e NON E' un crollo - r 2177"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                
                # BUY 1 con RIBASSO VELOCE MA la distanza tra ma100 e ma200 si sta riducendo - USANDO UN DOPPIO DELTA ! STA RISALENDO
                
                elif (
                    deviation_ma3 < -1.30
                  
                    
                    and delta_1 < delta_2
                    and ma100_last > ma100_60_min_ago
                    
                    and ma3_last > ma20_last
                ):
                
                    buy = "BUY 1 con RIBASSO VELOCE mentre la distanza tra ma100 e ma200 si sta riducendo - SOTTO RIALZO RIALZO - GIORNO ! - r 2196"
                    action = "buy"
                    percentage = 80
                    
                    # and delta_1 < 0.25
                    # and delta_2 > 0.40
                    # STUDIARE MEGLIO DELTA 1 E DELTA 2
                    
                    # compare grazie. altre parole io non ho.
                    
                    
                  
                
                # BUY 1 grande CORREZIONE AUDI che NON E' una piccola CORREZIONE FIAT che NON E' un grande ribasso MASERATI e NON E' un crollo FERRARI !)
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and (ma20_prev < ma200_prev and ma20_last > ma200_last)
                    and deviation_correzione_1 > 0.03
                    
                    and deviation_buy_crollo_1 < -0.70
                    and deviation_buy_crollo_1 > -0.90
                  
                ):
                    buy = "BUY 1 grande CORREZIONE AUDI che NON E' FIAT e NON E' MASERATI e NON E' FERRARI ! + deviation_correzione> 0.02 - r 2220"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma5_last / ma30_last
                    
              
                
                
                # BUY 1 grande CORREZIONE AUDI che NON E' FIAT e NON E' MASERATI e NON E' FERRARI ! con deviation trend ma200 
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_trend_ma200 > -0.30
                    and deviation_correzione_1 > -0.01
                    
                    and deviation_buy_crollo_1 < -0.70
                    and deviation_buy_crollo_1 > -0.90
                  
                ):
                    buy = "BUY 1 grande CORREZIONE AUDI che NON E' un grande ribasso MASERATI e NON E' un crollo FERRARI ! con deviation trend ma200 - r 2241"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma5_last / ma30_last
                    # deviation_trend_ma200 = ma200_last / ma200_120_min_ago
                    # compare prega per me !
                    
                    # and deviation_correzione_1 > -0.01 significa una ndecchia prima di 5-30 !
                
                
                ######################################################################################################
                ###################################################################################################### attenzione qui applico il doppio delta !
                
                # quando la ma100 si avvicina risalendo verso la ma200 ok cosi'
                # quando la ma100 si allontana verso il basso dalla ma 200 metto 8-50 altrimenti e' una perdita continua !
                
            
                # BUY 1 FIAT che non funzionava MA CHE HA FUNZIONATO ! ( DOPPIO DELTA 200-100 E DOPPIO DELTA 69-39 !) STA RISALENDO
                
                elif (    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
                    
                    and deviation_ma5_sopra_ma28 > 0.11
                    and ma3_last > ma9_last
                    and deviation_ma5_sopra_ma28 > 0.05
                    and ma200_last < ma300_last
                    and ma20_last < ma100_last
                    and ma100_last < ma100_10_min_ago
                    and deviation_ma200_sotto_ma300 < -0.27
                  
                    
                    and delta_1 < delta_2
                    and ma100_last > ma100_60_min_ago
                    
                    and rapporto_delta_1_delta_2_69_39 < 1
                    and ma39_last > ma39_30_min_ago
                    
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 FIAT che non funzionava MA CHE HA FUNZIONATO ! SOTTO RIALZO RIALZO - GIORNO ! - r 2283"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    # and deviation_correzione > 0.10
                    
                    # and delta_1 < 0.25 la puoi aggiungere in un secondo momento
                    # and delta_2 > 0.40 la puoi aggiungere in un secondo momento
                    
                    # compare prega per me !
                    
                    
                    
                    
                # BUY 1 OK FIAT ( DOPPIO DELTA) STA RISALENDO
                
                elif (    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
                    and deviation_correzione > 0.10
                    and deviation_ma5_sopra_ma28 > 0.07
                    and ma200_last < ma300_last
                    and ma20_last < ma100_last
                    and ma100_last < ma100_10_min_ago
                    and deviation_ma200_sotto_ma300 < -0.27
                   
                    
                    and delta_1 < delta_2
                    and ma100_last > ma100_60_min_ago
                    
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 FIAT OK DOPPIO DELTA STA RISALENDO - SOTTO RIALZO RIALZO - GIORNO !- r 2317"
                    action = "buy"
                    percentage = 80
                    
                    # and delta_1 < 0.50
                    # and delta_2 > 0.69
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    # MA DEVE AVERE UN PO' DI FORZA 5-28 > 0.07 !
                    # compare prega per me !
                    
                    
                
                
                
                
                
                
                #  BUY 1 FIAT copia BIS della r701 del RCCR che non funzionava e che invece HA FUNZIONATO ! ( CON DOPPIO DELTA in RIBASSO !) 8-39
                
                elif (    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
                    
                    and ma300_last > ma300_120_min_ago
                    and deviation_ma5_sopra_ma28 > 0.15
                    and ma8_last > ma39_last
                    and ma200_last < ma300_last
                    and ma20_last < ma100_last
                    and ma100_last < ma100_10_min_ago
                    and deviation_ma200_sotto_ma300 < -0.27
             
                    
                    and delta_1 > delta_2
                    and ma100_last < ma100_60_min_ago
                    
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 FIAT 300 > 120 min agocopia BIS della r701 del RCCR che non funzionava e che invece HA FUNZIONATO ! - NOTTE ! ! 8-39 - r 2355"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                #  BUY 1 FIAT copia BIS della r701 del RCCR che non funzionava e che invece HA FUNZIONATO ! ( CON DOPPIO DELTA in RIBASSO !) 8-39
                
                elif (    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
                    
                    and ma300_last < ma300_120_min_ago
                    and deviation_ma5_sopra_ma28 > 0.285
                    
                    and ma8_last > ma39_last
                    and ma200_last < ma300_last
                    and ma20_last < ma100_last
                    and ma100_last < ma100_10_min_ago
                    and deviation_ma200_sotto_ma300 < -0.27
             
                    
                    and delta_1 > delta_2
                    and ma100_last < ma100_60_min_ago
                    
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 FIAT 300 < 120 min ago copia BIS della r701 del RCCR che non funzionava e che invece HA FUNZIONATO ! - NOTTE ! ! 8-39 - r 2383"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    
                    # and delta_1 > 0.40 la puoi aggiungere in un secondo momento
                    # and delta_2 < 0.25 la puoi aggiungere in un secondo momento
                    
                    # compare prega per me !
                    
                    
                   
                
                
                
                
                
                
                
                # BUY 1 FIAT OK ( con doppio delta in ribasso !) 8-39
                
                elif (    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
                    and ma8_last > ma39_last
                    
                    and ma200_last < ma300_last
                    and ma20_last < ma100_last
                    and ma100_last < ma100_10_min_ago
                    and deviation_ma200_sotto_ma300 < -0.27
                    
                 
                    
                    and delta_1 > delta_2
                    and ma100_last < ma100_60_min_ago
                    and deviation_ma5_sopra_ma28 > 0.25
                    
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 FIAT OK (DOPPIO DELTA) RIBASSO ! 8-39  SOTTO RIBASSO RIBASSO  - NOTTE ! - r 2424"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    
                    # and delta_1 > 0.69
                    # and delta_2 > 0.50
                    
                    # compare prega per me !
                    
                    
                    
                    
                #####################################################################################################################
                
                
                # BUY 1 RIBASSO AUDI A importato dal BUY 2 che e' andato benissimo dopo il blocco
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.70
                    and deviation_buy_crollo_1 > -1.50
                    
                    and deviation_ma8_sotto_ma300 > -1.20
                    
                    and ma5_last > ma16_last
                    and deviation_ma5_sopra_ma16 > 0.11
                    and deviation_ma5_sopra_ma28 > 0.01
                    
                    and ma2_last > ma2_2_min_ago
                    and ma78_last < ma200_last
                    
                ):
                    buy = "BUY 1 RIBASSO AUDI A importato dal BUY 2 CON 8 sotto 300 > -1.20 - 5-16 > 0.11 E 5-28 > 0.01 - riga 2456 A"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # questa cosa che 78 deve essere < 200 ha dell' incredibile. MA NON TOCCARE !
                    
                    
                    
                    
                # BUY 1 RIBASSO AUDI B importato dal BUY 2 CON 8 sotto 300 < -1.20
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.70
                    and deviation_buy_crollo_1 > -1.50
                    
                    and deviation_ma8_sotto_ma300 < -1.20
                    
                    and ma5_last > ma15_last
                    
                    and ma2_last >= ma2_2_min_ago
                    and ma78_last < ma200_last
                    
                ):
                    buy = "BUY 1 RIBASSO AUDI B importato dal BUY 2 CON 8 sotto 300 < -1.20 - 5-15 - riga 2456 B"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # questa cosa che 78 deve essere < 200 ha dell' incredibile. MA NON TOCCARE !
                    # 21 giu 2022 5-18 da 5-20
                    # 21 giu 2022 5-16 da 5-18
                    # 27 giu 2022 5-15 da 5-16
                    
                # BUY 1 ultimo e meraviglioso RIBASSO AUDI con 5-16 copiata da RCCR CHE E' ANDATA BENISSIMO e che non e' un crollo ! (compare dove sei!)   
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.60
                    and deviation_buy_crollo_1 > -1.70
                    and deviation_ma5_sopra_ma16 > 0.11
                    
                    and ma100_last < ma100_120_min_ago
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and ma100_last > ma200_last
                    and ma200_last > ma300_last
                    
                    and deviation_ma100_laterale < -0.50
                    
                    and ma5_last > ma16_last
                    and ma2_last > ma2_2_min_ago
                    and ma78_last < ma200_last
                    
                    
                ):
                    buy = "BUY 1 ultimo e meraviglioso RIBASSO AUDI con 5-16 copiata da RCCR CHE E' ANDATA BENISSIMO e che non e' un crollo !  - riga 2489"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # questa cosa che 78 deve essere < 200 ha dell' incredibile. MA NON TOCCARE !
                    # and deviation_ma100_laterale < -0.50 significa che ma5 sa sotto di almeno 0.50 rispetto alla ma100 - questa e' necessaria
                    
                    
                    
                    
                    
                    
                # BUY 1 RIBASSO AUDI PIU' LENTA copiata da RCCR CHE E' ANDATA BENISSIMO CHE NON E' UN CROLLO ! (compare stammi vicino!)
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.70
                    and deviation_buy_crollo_1 > -1.50
                    and delta_1 < delta_2
                    
                    and deviation_ma5_sopra_ma16 > 0.09
                    and ma5_last > ma16_last
                    
                    and ma2_last > ma2_2_min_ago
                    and ma78_last < ma200_last
                    
                ):
                    buy = "BUY 1 RIBASSO AUDI PIU' LENTA CHE NON E' UN CROLLO ! and delta_1 < delta_2 con dev 5-16 > 0.09 - riga 2515 A"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # questa cosa che 78 deve essere < 200 ha dell' incredibile. MA NON TOCCARE !
                    
                    
                    
                    
                
                
                
                
                
                # BUY 1 DURANTE UN RIBASSO AUDI PIU' LENTA LENTA copiata da RCCR CHE E' ANDATA BENISSIMO CHE NON E' UN CROLLO ! (compare stammi vicino!)
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.70
                    and deviation_buy_crollo_1 > -1.50
                    and delta_1 > delta_2
                    
                    and ma13_last > ma25_last
                    
                    and ma5_last > ma16_last
                    and deviation_ma5_sopra_ma16 > 0.05
                    
                    and ma2_last > ma2_2_min_ago
                    and ma78_last < ma200_last
                    
                ):
                    buy = "BUY 1 DURANTE UN RIBASSO AUDI PIU' LENTA CHE NON E' UN CROLLO ! and delta_1 > delta_2 con dev 5-16 > 0.05 e 13>25 - riga 2515 B1"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # questa cosa che 78 deve essere < 200 ha dell' incredibile. MA NON TOCCARE !
                    # dev 5-16 c'e' perhe' sto riducendo piano piano
                    
                    
                    
                # BUY 1 DURANTE UN RIBASSO AUDI PIU' LENTA LENTA copiata da RCCR CHE E' ANDATA BENISSIMO CHE NON E' UN CROLLO ! (compare stammi vicino!)
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.70
                    and deviation_buy_crollo_1 > -1.50
                    and delta_1 > delta_2
                    
                    and ma13_last < ma25_last
                    and deviation_ma3_sopra_ma10 > 0.35
                    
                    and ma4_last > ma15_last
                    
                    
                    and ma2_last > ma2_2_min_ago
                    and ma78_last < ma200_last
                    
                ):
                    buy = "BUY 1 RIBASSO AUDI PIU' LENTA CHE NON E' UN CROLLO ! and delta_1 > delta_2 con 4-15 > 0.10 e 13<25 E 3-10 > 0.35 ! - riga 2515 B2"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # questa cosa che 78 deve essere < 200 ha dell' incredibile. MA NON TOCCARE !
                    # dev 5-16 c'e' perhe' sto riducendo piano piano
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                # BUY 1 DURANTE UN RIBASSO AUDI PIU' GIU' E PIU' VELOCE LENTA copiata da RCCR CHE E' ANDATA BENISSIMO CHE NON E' UN CROLLO !
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.70
                    and deviation_buy_crollo_1 > -1.50
                    
                    
                    and deviation_ma3_sopra_ma16 > 0.46
                    
                    and ma2_last >= ma2_2_min_ago
                    and ma78_last < ma200_last
                    
                ):
                    buy = "BUY 1 RIBASSO AUDI PIU' GIU' -0.70 E PIU' VELOCE CHE NON E' UN CROLLO ! con deviation 3-16 > 0.46  - riga 2538"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # questa cosa che 78 deve essere < 200 ha dell' incredibile. MA NON TOCCARE !
                    # 1 GIUGNO 2022 3-15 troppo veloce e troppi buy affrettati ! e perdite conseguenti !
                    # 7 giugno 2022 3-16> 0.20
                    
                    
                    
                    
                    
                    
                    
                    
                # copia della riga 530 del RCCR CHE FUNZIONA BENISSIMO ma solo un po' piu' prudente ! - BUY grande ribasso AUDI CHE NON E' UN CROLLO !
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -0.70
                    and deviation_buy_crollo_1 > -1.50
                    and deviation_bellissima > 0.02
                    and deviation_correzione_1 > 0.03
                    and ma13_last > ma50_last
                    and ma78_last < ma200_last
                ):
                    buy = "copia della riga 530 del RCCR ma piu' prudente ! - BUY GRANDE RIBASSO AUDI CHE NON E' UN CROLLO ! - r 2565"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # questa cosa che 78 deve essere < 200 ha dell' incredibile. MA NON TOCCARE !
                
                
                
                # QUA DEVI VEDERE - vanno in sovrapposizione - vedi prima come vanno poi correggi
                
                # BUY 1 GRANDE RIBASSO MASERATI CHE NON E' UN CROLLO ! (compare stammi vicino!) HA FUNZIONATO ! viva ro combaro meo !
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -0.91
                    and deviation_buy_crollo_1 > -1.50
                    and deviation_ma5_sopra_ma28 > 0.03
                    and ma78_last < ma200_last
                ):
                    buy = "BUY 1 GRANDE RIBASSO MASERATI CHE NON E' UN CROLLO ! con 5-28 - r 2585"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # questa cosa che 78 deve essere < 200 ha dell' incredibile. MA NON TOCCARE !
               
                ##############################################################################################################################
                # IMPORTANTISSIMO ! - PER COMPRARE DURANTE IL CROLLO - FERRARI - compa prega per me - ( cruise - david gilmour )
                ##############################################################################################################################

                # entriamo nell' area dell' ipervenduto, compa !
                # QUI LASCIO GLI INCROCI !
                
                
                
                # BUY 1 CROLLO FERRARI - modo 1
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -2.30
                    and ma3_last > ma16_last
                    and ma78_last < ma300_last
                ):
                    buy = "BUY 1 CROLLO FERRARI 3-16 - modo 1 and ma78_last < ma300_last - r 2609"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # era 3-7 ma MI DISPIACE TANTO ma ho dovuto mettere 5-15
                    
                    
                
                
                # BUY 1 CROLLO FERRARI - modo 2 questa condizione e' entrata in azione ! ( e mi e' sembrata ben fatta !)

                elif (
                    ma2_last >= ma2_2_min_ago
                    and deviation_buy_crollo_1 < -1.61
                    and ma5_last > ma18_last
                    and ma78_last < ma300_last
                ):
                    buy = "BUY 1 CROLLO FERRARI - modo 2 and ma78_last < ma300_last - r 2627"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # 14 GIU 2022 5-18
                    
                    
                    
                    
                # BUY 1 crollo MISSILE COMPA !
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -2.60
                    and ma3_last > ma13_last
                    and ma78_last < ma300_last
                ):
                    buy = "BUY 1 crollo MISSILE COMPA 3-13 and ma78_last < ma300_last - r 2645"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    
                    
                    
                    
                    
                    
                    
                    
                    
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -2.30
                    and ma5_last > ma15_last
                    
                    and ma78_last > ma300_last
                    and deviation_ma5_sopra_ma28 > 0.05
                ):
                    buy = "BUY 1 CROLLO FERRARI - modo 1 and ma78_last > ma300_last - r 2667"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # era 3-7 ma MI DISPIACE TANTO ma ho dovuto mettere 5-15
                    
                    
                    
                
                
                # BUY 1 CROLLO FERRARI - modo 2 questa condizione e' entrata in azione ! ( e mi e' sembrata ben fatta !)

                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -1.61
                    and deviation_buy_crollo_2 > 0.01
                    
                    and ma78_last > ma300_last
                    and deviation_ma5_sopra_ma28 > 0.05
                ):
                    buy = "BUY 1 CROLLO FERRARI - modo 2 and ma78_last > ma300_last - r 2688"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_buy_crollo_2 = ma3_last / ma13_last
                    
                    
                    
                    
                # BUY 1 crollo MISSILE COMPA !
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -2.60
                    and ma3_last > ma13_last
                    
                    and ma78_last > ma300_last
                    and deviation_ma5_sopra_ma28 > 0.05
                ):
                    buy = "BUY 1 crollo MISSILE COMPA 3-13 and ma78_last > ma300_last - r 2708"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    
                    
                    
                    
                    
                    
                    
                    
                    
            
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
                    buy = "BUY 1 ECCEZIONALE - se ma200 sale da 15 min e 69> COMPRA con deviation 4-25 e un po' piu' su della ma100 ! - r 2741"
                    action = "buy"
                    percentage = 80
                    
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

                    buy = "BUY 1 DOCCIA se ma200 > da 120 min ! COMPRA - r 2764"
                    action = "buy"
                    percentage = 80   
                    
                
                
                ############################################################################################################################
                
                
                
                # e non e' ancora una situazione cosi' drammatica.
                
                elif (    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
                    
                    and deviation_ma3_sopra_ma10 > 0.125
                    
                    and ma8_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                
                ):
                    buy = "BUY 1 ribasso AUDI o correzione FIAT che non e' un forte ribasso e non e' un crollo !  - r 2783"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
                
                
                # ECCO LA CONDIZIONE FIAT CHE FA PAURA ! MA CERCHIAMO DI FARLA ATTIVARE NEL MOMENTO GIUSTO (SOTTO RIALZO RIBASSO) AURORA
                
                elif (
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
                    
                    
                    and delta_1 < delta_2
                    and ma100_last < ma100_60_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.05
                    
                    and ma300_last < ma300_60_min_ago
                    and ma100_last < ma200_last
                    and deviation_ma200_sotto_ma300 > -0.15
                    and deviation_ma100_sopra_ma300 > -0.30
                    
                    and deviation_correzione > 0.03
                    
                    
                    and deviation_ma25_sotto_ma300 < -0.60
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 CORREZIONE FIAT CHE FA PAURA ! (MA ma100 e ma200 sono ANCORA VICINE alla ma300) (SOTTO cresce diminuisce) AURORA - riga 2830"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                    
                    
                    
                    
                # FIAT SOTTO RIBASSO RIBASSO - NOTTE
                
                elif (
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
                    
                    
                    and delta_1 > delta_2
                    and ma100_last < ma100_60_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.30
                    
                    and ma300_last < ma300_60_min_ago
                    and ma100_last < ma200_last
                    and deviation_ma200_sotto_ma300 > -0.15
                    and deviation_ma100_sopra_ma300 > -0.30
                    
                    and deviation_correzione > 0.03
                    
                    
                    and deviation_ma25_sotto_ma300 < -0.60
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 CORREZIONE FIAT CHE FA PAURA ! (MA ma100 e ma200 sono ANCORA VICINE alla ma300) (SOTTO RIBASSO RIBASSO ) NOTTE ! - riga 2864"
                    action = "buy"
                    percentage = 80
                    
                    # questa e' la condizione che piu' di tutte mi ha fatto soffrire.
                    # ma molte volte ha dato grandi soddisfazioni sul RCCR
                    # io ho cercato di prendere LA PARTE MIGLIORE.
                    # SPERIAMO. sempre.
                    
                    # deviation_ma100_sopra_ma300 significa 100/300 ( ma100 ancora NON SI E' ALLONTANATA TROPPO DALLA ma300 )
                    # deviation_ma25_sotto_ma300 significa che anche ma25 deve andare almeno un po' sotto ma300 (per evitare piccole schegge rialziste !)
                    # NON TOCCARE 5-28 > 0.05 !
                    
                    
                    
                    
                    
                    
                    
              
                
                
                # BUY 1 CROLLO FERRARI ok - RCCR - questa condizione mi e' sembrata ben fatta !

                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -1.61
                    and deviation_buy_crollo_2 > 0.01
                    and deviation_ma3_sopra_ma10 > 0.12
                ):
                    buy = "BUY 1 CROLLO FERRARI ok CON 3-10 necessaria ! - RCCR - r 2912"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_buy_crollo_2 = ma3_last / ma13_last
                    # fondamentale aggiunta 3-10 perche' anche ferrari NE HA BISOGNO ma non 5-28 CHE COMINCIA AD ESSERE INAPPROPRIATA
                    
                    
                    
                # BUY 1 SUL SUPPORTO 300 !
          
                elif (    
                    ma5_last > ma13_last
                    and (ma3_last > ma285_last and ma3_last < ma285_last)
                    and ma100_last > ma100_120_min_ago
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    
                    and ma100_last > ma200_last
                    and ma2_last > ma300_last
                    and ma2_last > ma2_2_min_ago
                
                ):
                    buy = "BUY 1 SUL SUPPORTO 300 ! - r 2913"
                    action = "buy"
                    percentage = 80
                    
                    # madonna compa !
                    
                    
                    
                # BUY 1 dopo ribasso MA CON TUTTE LE MA > e con incrocio al rialzo 8-140 !
                
                elif (    
                    ma50_last > ma100_last
                    and (ma8_last < ma140_last and ma8_last > ma140_last)
                 
                    and ma100_last > ma100_60_min_ago
                   
                    and ma100_last > ma100_120_min_ago
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    
                    and ma100_last > ma200_last
                    and ma200_last > ma300_last
                    
                    and ma2_last > ma300_last
                    and ma2_last > ma2_2_min_ago
                
                ):
                    buy = "BUY 1 dopo ribasso MA CON TUTTE LE MA > e con incrocio al rialzo 8-140 - r 2940"
                    action = "buy"
                    percentage = 80
                    
                    # madonna compa !
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                # BUY 1 CHE MANCAVA ! con incrocio 11-50 AND 5-28 > 0.20 ( CON 100 < AND 200 < AND 300 < ) (!)
                
                elif (
                    deviation_ma5_sopra_ma28 > 0.265
                    and (ma11_last < ma50_last and ma11_last > ma50_last)
                    and deviation_ma8_sotto_ma300 < -0.30
                    
                    and ma100_last < ma100_120_min_ago
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.20
                    and ma2_last > ma2_2_min_ago
                    
            
                ):
                    buy = "BUY 1 CHE MANCAVA ! con incrocio 11-50 AND 5-28 > 0.265 (!) ( CON 100 < AND 200 < AND 300 < ) (!)  - r 2972"
                    action = "buy"
                    percentage = 80
                    
                    # madonna compa !
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                # BUY 1 CHE MANCAVA DOPO BUY-SELL CROLLO ! 150-100 GIORNO ! E 50 > 100
                
                elif (
                    deviation_ma5_sopra_ma28 > 0.10
                    and deviation_ma3_sopra_ma10 > 0.04
                    and ma78_last > ma200_last
                 
                    and ma50_last > ma100_last
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and ma100_last < ma100_120_min_ago
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and delta_150_100 < delta_150_100_60_min
                    
                    
                    and ma2_last > ma2_2_min_ago
                
                ):
                    buy = "BUY 1 78>200 CHE MANCAVA DOPO BUY-SELL CROLLO ! 50 > 100 AND 150-100 GIORNO ! and 3-10 > 0.05 and 5-28 > 0.12 - r 3007 a"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                # BUY 1 CHE MANCAVA DOPO BUY-SELL CROLLO ! 150-100 GIORNO ! E 50 > 100
                
                elif (
                    deviation_ma5_sopra_ma28 > 0.12
                    and deviation_ma3_sopra_ma10 > 0.05
                    and ma78_last < ma200_last
                    
                    and ma50_last > ma100_last
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and ma100_last < ma100_120_min_ago
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and delta_150_100 < delta_150_100_60_min
                    and ma100_last > ma100_3_min_ago
                    
                    and ma2_last > ma2_2_min_ago
                
                ):
                    buy = "BUY 1 78<200 CHE MANCAVA DOPO BUY-SELL CROLLO ! 50 > 100 AND 150-100 GIORNO ! and 3-10 > 0.05 and 5-28 > 0.12 - r 3007 b"
                    action = "buy"
                    percentage = 80
                    
                    # madonna compa ! 
                    # the sound of silence
                    # ASSURDO ! questa 100 > 100 3 min e' incredibile ! si e' verificata dopo il BUY-SELL del crollo ! NON TOCCARE
                    # SI STA RIDUCENDO LA DISTANZA TRA 150 E 100
                    
                    # 10 giu 5-28 0.12 da 0.09 cazzo
                    
                    
                    
                    
                # BUY 1 CHE MANCAVA DOPO BUY-SELL CROLLO ! 150-100 GIORNO ! MA 50 < 100
                
                elif (
                    deviation_ma5_sopra_ma28 > 0.12
                    and deviation_ma3_sopra_ma10 > 0.25
                    
                    and ma50_last < ma100_last
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and ma100_last < ma100_120_min_ago
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and delta_150_100 < delta_150_100_60_min
                    and ma100_last > ma100_3_min_ago
                    
                    and ma2_last > ma2_2_min_ago
                
                ):
                    buy = "BUY 1 CHE MANCAVA DOPO BUY-SELL CROLLO ! 50 < 100 AND 150-100 GIORNO ! and 3-10 > 0.25 and 5-28 > 0.12 - r 3008"
                    action = "buy"
                    percentage = 80
                    
                    # madonna compa ! 
                    # the sound of silence
                    # ASSURDO ! questa 100 > 100 3 min e' incredibile ! si e' verificata dopo il BUY-SELL del crollo ! NON TOCCARE
                    # SI STA RIDUCENDO LA DISTANZA TRA 150 E 100
                    
                    # 10 giu 2022 5-28 0.12 da 0.09 cazzo
                    # 21 giu 2022 3-10 > 0.25 da > 0.05 CAZZO
                    
                    
                
                
                # BUY 1 CHE MANCAVA aggressiva - (SEMBRA pari al BUY DURANTE UN RIBASSO AUDI !)
                
                elif (
                    deviation_ma5_sopra_ma28 > 0.05
                    and deviation_ma3_sopra_ma10 > 0.12
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and ma100_last < ma100_60_min_ago
                    and ma200_last < ma200_60_min_ago
                    and ma300_last < ma300_60_min_ago
                    
                    
                    and deviation_ma8_sotto_ma100 < -0.70
                    and deviation_ma8_sotto_ma200 < -1.10
                    and deviation_ma8_sotto_ma300 < -1.30
                    
                    and ma2_last > ma2_2_min_ago
                
                ):
                    buy = "BUY 1 CHE MANCAVA aggressiva  (SEMBRA pari al BUY DURANTE UN RIBASSO AUDI !) 3-10 > 0.12 AND 5-28 > 0.05 - r 3042"
                    action = "buy"
                    percentage = 80
                    
                    # madonna compa che ti sei dimenticato di me ! 
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
          
                
            
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
                    
                    buy = "BUY 1 con 200 > 200 20 min ago (100 < and 200 < MA 300 >) and 13-200 !  - riga 3075"
                    action = "buy"
                    percentage = 80
                    
                    
                
                # BUY 1 SITUAZIONE TREND LATERALE che mancava con ma300 > - DOPPIO DELTA - RIALZO
                
                elif (    
               
                    ma8_last > ma300_last
                    and ma100_last > ma200_last
                    and ma100_last > ma300_last
                    
                    and ma28_last > ma28_30_min_ago
                    
                    and delta_1 < delta_2
                    and ma100_last > ma100_60_min_ago
                    
                    and ma300_last > ma300_60_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.14
                    and ma2_last > ma2_2_min_ago
                ):    
                    
                    buy = "BUY 1 SITUAZIONE TREND LATERALE che mancava con ma300 > - GIORNO ! and 5-28 > 0.14 con 28>28 30 min ago - riga 3100 A"
                    action = "buy"
                    percentage = 80
                    
                    # ho aggiunto 5-28 > 0.05
                    # cosa curiosa SEMBRA CHE and ma2_last > ma2_2_min_ago abbia fatto ritardare questo BUY.
                    # ho tenuto i 2 minuti e ho ridotto 5-28
                    
                    
                    
                    
                # BUY 1 SITUAZIONE TREND LATERALE che mancava con ma300 > - DOPPIO DELTA - RIALZO
                
                elif (    
               
                    ma8_last > ma300_last
                    and ma100_last > ma200_last
                    and ma100_last > ma300_last
                    
                    and ma28_last < ma28_30_min_ago
                    
                    and delta_1 < delta_2
                    and ma100_last > ma100_60_min_ago
                    
                    and ma300_last > ma300_60_min_ago
                    
                    and deviation_ma3_sopra_ma10 > 0.17
                    and deviation_ma5_sopra_ma28 > 0.14
                    and ma2_last > ma2_2_min_ago
                ):    
                    
                    buy = "BUY 1 SITUAZIONE TREND LATERALE che mancava con ma300 > - GIORNO ! and 5-28 > 0.14 MA 28 < 28 30 min ago AND 3-10 > 0.17 - riga 3100 B"
                    action = "buy"
                    percentage = 80
                    
                    # ho aggiunto 5-28 > 0.05
                    # cosa curiosa SEMBRA CHE and ma2_last > ma2_2_min_ago abbia fatto ritardare questo BUY.
                    # ho tenuto i 2 minuti e ho ridotto 5-28
                    
                    
                    
                # BUY 1 SITUAZIONE TREND LATERALE che mancava con ma300 < - DOPPIO DELTA - RIALZO
                
                elif (    
               
                    ma8_last > ma300_last
                    and ma100_last > ma200_last
                    and ma100_last > ma300_last
                    
                    
                    and delta_1 < delta_2
                    and ma100_last > ma100_60_min_ago
                    
                    and ma300_last < ma300_60_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.16
                    and ma2_last > ma2_2_min_ago
                ):    
                    
                    buy = "BUY 1 SITUAZIONE TREND LATERALE che mancava con ma300 < - SOPRA RIALZO RIALZO - GIORNO ! and 5-28 > 0.16 - riga 3128"
                    action = "buy"
                    percentage = 80
                    
                    # 8 giu 2022 5-28 0.16 da 0.17
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
              
                
                
                # BUY 1 forever young 1 PIU' PRUDENTE se ma200 > e se ma200 > ma300 - che si preoccupa degli effetti laterali
                
                elif (  
                    ma200_last > ma300_last
                    and ma78_last > ma100_last
                    and deviation_ma100_laterale > 0.18
                    and ma200_last > ma200_15_min_ago
                    and deviation_ma5_sopra_ma28 > 0.10
                    
                    and ma3_last > ma11_last
                    and ma5_last > ma200_last
                    and ma10_last > ma10_2_min_ago
                    and ma2_last > ma2_2_min_ago
                ):

                    buy = "BUY 1 forever young 1 PIU' PRUDENTE se ma 200 > e se ma200 > ma300 - che si preoccupa degli effetti laterali - r 3162"
                    action = "buy"
                    percentage = 80
                    
                    # la troppa prudenza qualche volta genera perdite
                    
                    
                    
                    
                    
                # BUY 1 forever young 1 PIU' PRUDENTE se ma 200 > e se ma200 > ma300
                
                elif (  
                    ma200_last > ma300_last
                    and ma78_last < ma100_last
                    and deviation_ma100_laterale > 0.12
                    and ma11_last > ma200_last
                    and ma200_last > ma200_15_min_ago
                    and deviation_ma5_sopra_ma28 > 0.09
                    
                    and ma3_last > ma11_last
                    and ma5_last > ma200_last
                    
                    and ma2_last > ma2_2_min_ago
                ):

                    buy = "BUY 1 forever young 1 PIU' PRUDENTE se ma 200 > e se ma200 > ma300 - r 3188"
                    action = "buy"
                    percentage = 80
                    
                    # la troppa prudenza qualche volta genera perdite
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
               
                ################################################################################################
                
                
                # BUY 1 FOREVER YOUNG PIU' AGGRESSIVO con doppio delta < 1 E MA100> (rialzo) se ma 200 > e se ma200 > ma300  and deviation_ma5_sopra_ma28 > 0.10
                
                elif (  
                    ma100_last > ma200_last
                    and ma200_last > ma300_last
                    
                    and ma200_last > ma200_15_min_ago
                    
                    
                    and delta_1 < delta_2
                    and ma100_last > ma100_60_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.01
                 
                    and ma6_last > ma6_2_min_ago
                    and ma13_last > ma69_last
                    and ma13_last > ma13_2_min_ago
                    and ma2_last > ma2_2_min_ago
                ):
                    
                    buy = "BUY 1 FOREVER YOUNG PIU' AGGRESSIVO (doppio delta < 1 E 100> ) (SOPRA RIALZO RIALZO) - GIORNO - se ma 200 > e se ma200 > ma300 - r 3228"
                    action = "buy"
                    percentage = 80
                    
                    # SITUAZIONE : dopo crollo e dopo primo grande ribalzo riprende a scendere 
                    # MA ma100 e' intanto andata > ma200 !
                    # e anche ma200 sta sopra ma300
                    
                    
                    
              
                
                
                # BUY 1 FOREVER YOUNG PRUDENTE se ma 200 > e se ma200 > ma300 con doppio delta > 1 (ribasso) and deviation_ma5_sopra_ma28 > 0.30
                
                elif (  
                    ma200_last > ma300_last
                    and ma200_last > ma200_15_min_ago
                    
                    
                    and delta_1 > delta_2
                    and ma100_last < ma100_60_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.30
                
                    and ma6_last > ma6_2_min_ago
                    and ma13_last > ma69_last
                    and ma13_last > ma13_2_min_ago
                    and ma2_last > ma2_2_min_ago
                ):
                    
                    buy = "BUY 1 FOREVER YOUNG PRUDENTE SOPRA RIBASSO RIBASSO - NOTTE - and deviation_ma5_sopra_ma28 > 0.30 se ma 200 > e se ma200 > ma300 - r 3259"
                    action = "buy"
                    percentage = 80
                    
                    
                
                
                
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
                    and deviation_correzione > 0.03
                    
                    and ma100_last < ma100_120_min_ago
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and deviation_ma100_sopra_ma300 <-2.30
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 DURANTE UNA CORREZIONE FIAT da r701 RCCE ho dovuto metterla ! con deviation_correzione > 0.03 MA 100 lontana da 300 ! - riga 3281"
                    action = "buy"
                    percentage = 80
                    
                    # 100 sopra 300 MA IN REALTA' STA SOTTO.
                    # 100 lontana da 300
                    # 100< 200< 300< da oltre 120 min
                    
                    # deve essere cosi' altrimenti la r701 RCCR genera molte perdite.
                    # ma il 9 maggio 2022 RCCR ha comprato in situazione DRAMMATICA ed e' andata benissimo mentre MADDOG DORMIVA.
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
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
                    buy = "BUY 1 con DEVIATION ASSURDA se ma200 > da 120 min COMPRA con INCROCIO ma8 ma200 (ma5>ma300 evita gli EFFETTI LATERALI) - r 3316"
                    action = "buy"
                    percentage = 80
                    
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
                    buy = "BUY 2A rialzo o laterale - r 3341"
                    action = "buy"
                    percentage = 80

                    # deviation_buy_ma3_sopra_ma13 > x e' fondamentale !
                    # deviation_buy2 = ma8_last/ma50_last
                    
                    
                    
                elif (
                    ma69_last >= ma69_2_min_ago
                    and deviation_ma100_sopra_ma300 < 0.20
                    
                    and deviation_buy2 > 0.02
                    and deviation_bellissima > 0.12
                    and deviation_buy_ma3_sopra_ma13 > 0.08
                    and deviation_ma7_sopra_ma40 > 0.06
                    and ma2_last >= ma2_2_min_ago
                    and price > price_2_min_ago
                    and ma3_last > ma40_last
                ):
                    buy = "BUY 2A ribasso o laterale - r 3362"
                    action = "buy"
                    percentage = 80

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
                    buy = "BUY 2B - r 3382"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_ma3_sopra_ma13 > x e' fondamentale !
                    # deviation_buy2 = ma8_last/ma50_last
                    
                    
            
                ##################################################################################
                
                
                # BUY 2C ( SOPRA and DOPPIO DELTA < 1 and 100> ) (ribasso-rialzo) - CREPUSCOLO and deviation_ma5_sopra_ma28 > 0.14
                
                elif (
                    deviation_buy2 > 0.10
                    and ma100_last > ma100_60_min_ago
                  
                    
                    and delta_1 > delta_2
                    and ma100_last > ma100_60_min_ago
                    
                    and deviation_ma3_sopra_ma10 > 0.16
                    and deviation_ma5_sopra_ma28 > 0.14
                 
                    and deviation_bellissima > 0.12
                    and deviation_buy_ma3_sopra_ma13 > 0.10
                    and deviation_ma7_sopra_ma40 > 0.10
                    and ma4_last > ma9_last
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma40_last
                    and ma4_last > ma78_last
                ):
                    buy = "BUY 2C (SOPRA) (delta1 > delta2 and 100 > ) - CREPUSCOLO - and dev_ma5_sopra_ma28 > 0.14 AND 3-10 > 0.16 - r 3415"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy2 = ma8_last / ma50
                    
                    
                
                
                
                
                # BUY 2 300 > 120 min ago con doppio delta > 1 trend ribasso and deviation_ma5_sopra_ma28 > 0.16
                
                elif (
                    deviation_buy2 > 0.10
                    and ma300_last > ma300_120_min_ago
                    
                    and delta_1 > delta_2
                    and ma100_last < ma100_60_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.16
                    
                    and deviation_bellissima > 0.12
                    
                    and deviation_buy_ma3_sopra_ma13 > 0.10
                    and deviation_ma7_sopra_ma40 > 0.10
                    and ma4_last > ma9_last
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma40_last
                    and ma4_last > ma78_last
                ):
                    buy = "BUY 2C SOPRA RIBASSO RIBASSO - NOTTE - r 3446"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy2 = ma8_last / ma50
                    
                    
                    
                    
                    
                # BUY 2 300 < 120 min ago con doppio delta > 1 trend ribasso and deviation_ma5_sopra_ma28 > 0.16
                
                elif (
                    deviation_buy2 > 0.10
                    and ma300_last < ma300_120_min_ago
                    and deviation_buy_ma2_sopra_ma5 > 0.27
                    
                    and delta_1 > delta_2
                    and ma100_last < ma100_60_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.01
                    
                    and deviation_bellissima > 0.12
                    
                    and deviation_buy_ma3_sopra_ma13 > 0.10
                    and deviation_ma7_sopra_ma40 > 0.10
                    and ma4_last > ma9_last
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma40_last
                    and ma4_last > ma78_last
                ):
                    buy = "BUY 2C SOPRA RIBASSO RIBASSO - NOTTE - r 3477"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy2 = ma8_last / ma50
                    
                    # incredibile :  anticipa con 300 < 120 min ago
                    
                    
                    
                    
             
                # BUY 2C se ma100 <
                
                elif (
                    deviation_buy2 > 0.09
                    
                    and ma200_last > ma200_120_min_ago
                    
                    and ma5_last > ma18_last
                    
                    and ma100_last < ma100_50_min_ago
                    and deviation_bellissima > 0.165
                    
                    and deviation_buy_ma3_sopra_ma13 > 0.10
                    and deviation_ma7_sopra_ma40 > 0.10
                    and ma4_last > ma9_last
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma40_last
                    and ma4_last > ma78_last
                ):
                    buy = "BUY 2C con 100 < MA 200 > con 5 > 18 ( NON TOCCARE ) - r 3508"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy2 = ma8_last / ma50
                    
                    
                
             
                
                
                # --------------------------------------------------- BUY 2 ORIGINALE CHE CI RIPROVA IMPORTATO DA SELL 1 - NOTTE
                
                elif (
                    ma50_last < ma50_2_min_ago
                    and ma3_last > ma28_last
                        
                    and ma2_last > ma2_2_min_ago
                        
                    and delta_1 > delta_2
                    and ma100_last < ma100_60_min_ago
                        
                    and ma100_last < ma100_120_min_ago
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                        
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                ):
                    buy = "BUY 2 ORIGINALE CHE CI RIPROVA IMPORTATO DA SELL 1  - NOTTE - r 3537"
                    action = "sell"
                    percentage = 80
                    

                        
                # BUY 2 DURANTE UN RIBASSO AUDI CHE NON E' UN CROLLO ! E CHE CI RIPROVA (compare stammi vicino!)
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.70
                    and deviation_buy_crollo_1 > -1.50
                    
                    and ma5_last > ma16_last
                    and ma2_last > ma2_2_min_ago
                    and ma78_last < ma200_last
                    and deviation_ma5_sopra_ma16 > 0.08
                ):
                    buy = "BUY 2 DURANTE UN RIBASSO AUDI CHE NON E' UN CROLLO ! E CHE CI RIPROVA con dev_5-16 > 0.08 - riga 3555"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # questa cosa che 78 deve essere < 200 ha dell' incredibile. MA NON TOCCARE !
                    
                    # 19 giu 2022 dev_5-16 a 0.08 da 0.09
                    
                   
                    
                
                
                # IL BUY 2 CI RIPROVA CON INCROCIO 8-50
                
                elif (
                    deviation_buy2 > 0.005
                    and ma50_last > ma100_last
                    
                    and ma200_last < ma200_120_min_ago
                    
                    and ma100_last < ma100_50_min_ago
                    and (ma7_prev < ma50_prev and ma7_last > ma50_last)
                    and ma2_last > ma2_2_min_ago
                ):
               
                    buy = "BUY 2C con 100< and 200< con INCROCIO 7-50 - r 3580"
                    action = "buy"
                    percentage = 80
                    
                    
               
            
            
            
            
            
            
                # BUY 2C con 100< and 200< con INCROCIO 7-50 PIU' FORTE (SOPRA -CRESCE-DIMINUISCE) aurora
                
                elif (
                    deviation_buy2 > 0.01
                    
                    
                    and delta_1 < delta_2
                    and ma100_last < ma100_60_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.10
                    
                    and ma50_last < ma100_last
                    
                    
                    and ma200_last < ma200_120_min_ago
                    
                    and ma100_last < ma100_50_min_ago
                    and (ma7_prev < ma50_prev and ma7_last > ma50_last)
                    and ma2_last > ma2_2_min_ago
                ):
               
                    buy = "BUY 2C con 100< and 200< con INCROCIO 7-50 and 5-28 >0.10 (SOPRA - aurora - r 3613"
                    action = "buy"
                    percentage = 80
                    
                    # 6 giu 2022 5-28 a 0.10 da 0.07
                    
                    
                    
                    
                # BUY 2C con 100< and 200< con INCROCIO 7-50 PIU' FRAGILE (SOPRA DIMINUISCE DIMINUISCE) notte
                
                elif (
                    deviation_buy2 > 0.01
                    
                    
                    and delta_1 > delta_2
                    and ma100_last < ma100_60_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.29
                    
                    and ma50_last < ma100_last
                    
                    and ma200_last < ma200_120_min_ago
                    
                    and ma100_last < ma100_50_min_ago
                    and (ma7_prev < ma50_prev and ma7_last > ma50_last)
                    and ma2_last > ma2_2_min_ago
                ):
               
                    buy = "BUY 2C con 100< and 200< con INCROCIO 7-50 and 5-28 > 0.29 - NOTTE! - r 3642"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy2 = ma8_last / ma50
                    # incrocio va bene nel trend laterale NON TOCCARLO ! ho messo incrocio per evitare punti sopvrapposti
                    
                    
                    
                    
                
                
                
                # IL BUY 2 CI RIPROVA MA PIU' IN ALTO ! non toccare questa altrimenti fa punti sovrapposti !
                
                elif (
                    deviation_buy2 > 0.01
                    and ma200_last < ma200_120_min_ago
                    
                    and ma100_last < ma100_50_min_ago
                    
                    and deviation_buy > 0.50
                    and deviation_ma5_sopra_ma28 > 0.60
                    and ma2_last > ma2_2_min_ago
                ):
               
                    buy = "BUY 2C con 100 < and 200 < con DEVIATION BUY > 0.50 and 5-28 > 0.60 - r 3668"
                    action = "buy"
                    percentage = 90
                    
                    # deviation_buy2 = ma8_last / ma50
                    # deviation buy e 5-28 cosi' alte per evitare punti sovrapposti NON TOCCARE
                    
                    
                    
                    
                    
                
                ####################################################################################################### BUY 2 DURANTE IL CROLLO CHE CONTINUA !
                
                # se il crollo continua dopo che ha venduto sell 1 durante il crollo - ro cano CI RIPROVA !     
                
                # BUY 2  primo modo DURANTE IL CROLLO

                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -2.30
                    and ma3_last > ma15_last
                ):
                    buy = "BUY 2 DURANTE IL CROLLO - modo 1 2-7 - r 3691"
                    action = "buy"
                    percentage = 90
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # 14 GIU 2022 3-15 PERCHE' COMPRAVA CONTINUAMENTE DURANTE IL CROLLO CON 3-7
                    
                    
                    
                # BUY 2 secondo modo - DURANTE IL CROLLO - questa condizione e' entrata in azione ! ( e mi e' sembrata ben fatta !)

                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -1.70
                    and deviation_buy_crollo_1 > -2.29
                    and deviation_buy_crollo_2 > 0.11
                    and deviation_ma5_sopra_ma28 > 0.03
                ):
                    buy = "BUY 2 DURANTE IL CROLLO - modo 2 - r 3709"
                    action = "buy"
                    percentage = 90
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_buy_crollo_2 = ma3_last / ma13_last
                    
                    
                    
                    
                # BUY 2 CHE MANCAVA DOPO BUY-SELL CROLLO ! 150-100 GIORNO !
                
                elif (
                    deviation_ma5_sopra_ma28 > 0.10
                    and deviation_ma3_sopra_ma10 > 0.20
                    
                    and deviation_ma100_sopra_ma300 < -0.20
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and ma100_last < ma100_120_min_ago
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and delta_150_100 < delta_150_100_60_min
                    and ma100_last > ma100_3_min_ago
                    
                    and ma2_last > ma2_2_min_ago
                
                ):
                    buy = "BUY 2 CHE MANCAVA DOPO BUY-SELL CROLLO ! 150-100 GIORNO ! - r 3738"
                    action = "buy"
                    percentage = 90
                    
                    # madonna compa ! 
                    # the sound of silence
                    # ASSURDO ! questa 100 > 100 3 min e' incredibile ! si e' verificata dopo il BUY-SELL del crollo ! NON TOCCARE
                    # SI STA RIDUCENDO LA DISTANZA TRA 150 E 100
                    # and deviation_ma100_sopra_ma300 < -0.20 significa che stiamo ancora in una situazione di ribasso !
                    
                    
                    
                
                    
                    
              
                ################################################### per comprare durante UNA piccola CORREZIONE che NON E' un forte ribasso e NON E' un crollo
                
                # BUY 2A PAZZA DURANTE UNA piccola CORREZIONE che NON E' un forte ribasso e NON E' un crollo ! (compare stammi vicino!)
             
                elif (
                    deviation_ma5_sopra_ma28 > 0.23
             
                    and deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
               
                    and deviation_correzione > 0.015
                    and deviation_buy_ma5_sopra_ma20 > 0.10
                    and ma2_last > ma2_2_min_ago
                ):

                    buy = "BUY 2A PAZZA piccola CORREZIONE che non e' un forte ribasso e non e' un crollo ! deviation 5-28 > 0.05 - r 3769"
                    action = "buy"
                    percentage = 80

                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    # ma5 non deve allontanarsi troppo dalla ma200 !
                    # compare prega per me !
              
                
                
                # BUY 2 CORREZIONE che NON E' un forte ribasso e NON E' un crollo ! con deviation_correzione > 0.02
                 
                elif (

                    ma2_last > ma2_2_min_ago
                    and (ma20_prev < ma200_prev and ma20_last > ma200_last)
                    and deviation_correzione_2 > 0.03
                    and deviation_buy_crollo_1 < -0.70
                    and deviation_buy_crollo_1 > -0.90

                ):

                    buy = "BUY 2 CORREZIONE che NON E' un forte ribasso e NON E' un crollo ! con deviation_correzione > 0.02 - r 3792"
                    action = "buy"
                    percentage = 80
                  
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma5_last / ma30_last
                    # compare prega per me !
                    
                    
                    

                    

                
                # BUY 2 FORTE RIBASSO che NON E' UN CROLLO ! (compare stammi vicino!) 
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -0.70
                    and deviation_buy_crollo_1 > -1.50
                    and deviation_bellissima > 0.15
                ):
                    buy = "BUY 2 FORTE RIBASSO che NON E' UN CROLLO ! and deviation_bellissima > 0.15 - r 3814"
                    action = "buy"
                    percentage = 80
                    
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
                    and deviation_ma5_sopra_ma28 > 0.10
                ):
                    buy = "BUY 2 nuovo TREND LATERALE ! - r 3837"
                    action = "buy"
                    percentage = 80
                    
                    # SE ma100 E' cosi' VICINA A ma200 E ma300 vuo dire che non c'e' un grande rialzo in atto ma un TREND LATERALE !
                    # 5-28 a 0.10 da 0.07
                    
                    
                    
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
                    buy = "BUY 2 andamento laterale se ma200> da 20 min compra con 4-30 (SUL BUY 2 0.50 e 20-69 vs EFFETTI LATERALI !) - r 3863"
                    action = "buy"
                    percentage = 80
                    
                    
                
                
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
                    buy = "BUY 2 andamento laterale se ma200> da 20 min compra con 4-30 (SUL BUY 2 0.50 e 20-69 vs EFFETTI LATERALI !) - r 3888"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                # BUY 2 DOCCIA
                
                elif (    

                    ma100_last > ma100_60_min_ago
                    and ma200_last > ma200_90_min_ago
                    and ma300_last > ma300_120_min_ago
                    and ma20_last > ma200_last
                    
                    and deviation_ma100_sopra_ma300 > 0.70
                    and deviation_ma3_sopra_ma10 > 0.01
                    
                    and ma3_last > ma59_last
                    
                    
                    and deviation_ma5_sopra_ma30 > 0.02
                    and deviation_buy_ma3_sopra_ma25 > 0.04
                    
                    and (ma4_prev < ma25_prev and ma4_last > ma25_last)
                    and ma2_last >= ma2_2_min_ago
                ): 
                    buy = "BUY 2 DOCCIA se ma200 > da 90 min ! E 3-10 > 0.01 - 100 MOLTO ALTA RISPETTO A 300 - r 3910 A"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                    
                # BUY 2 DOCCIA
                
                elif (    

                    ma100_last > ma100_60_min_ago
                    and ma200_last > ma200_90_min_ago
                    and ma300_last > ma300_120_min_ago
                    and ma20_last > ma200_last
                    and deviation_ma100_sopra_ma300 < 0.70
                    and deviation_ma3_sopra_ma10 > 0.01
                    
                    and ma3_last > ma59_last
                    and ma11_last > ma59_last
                    
                    and deviation_ma5_sopra_ma30 > 0.03
                    and deviation_buy_ma3_sopra_ma25 > 0.05
                    
                    and (ma4_prev < ma25_prev and ma4_last > ma25_last)
                    and ma2_last >= ma2_2_min_ago
                ): 
                    buy = "BUY 2 DOCCIA se ma200 > da 90 min ! E 3-10 > 0.01 -100 NON LONTANA DA 300  r 3910 B"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                    
                
                
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
                    buy = "BUY 2 con DEVIATION ASSURDA se ma200 sale da 120 min BUY con ma2-ma200 (ma5 > ma300 evita GLI EFFETTI LATERALI !) - r 3929"
                    action = "buy"
                    percentage = 70    
          
                    # deviation_assurda = ma2 / ma200
            
            
            
            
            
            
                # BUY 2 che ci riprova TORNANDO ALLE ORIGINI ( TREND LATERALE !) con ma200< and ma300< AND 100 vicina alla 300
                
                elif (
                    deviation_buy2 > 0.05
                    and deviation_ma100_sopra_ma300 > -0.20
                    and deviation_ma5_sopra_ma28 > 0.18
                    
                    and deviation_bellissima > 0.13
                    and ma8_last > ma8_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma7_last
                    and ma3_last > ma13_last
                    and deviation_buy_ma3_sopra_ma20 > 0.05
                    and deviation_ma4_sopra_ma25 > 0.05
                    
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                ):
               
                    buy = "BUY 2 che ci riprova TORNANDO ALLE ORIGINI ( TREND LATERALE !) con ma200< and ma300< AND 100 vicina alla 300 - r 3959"
                    action = "buy"
                    percentage = 70

                    # compare prega per me !
                    # se ma200< e ma300< si torna alle origini ! 8-50 ! (con ma2 > ma2 2 min ago)
                    # deviation_buy2 = ma8_last / ma50_last
                    
                    # SE 100 STA VICINO ALLA 300 TREND LATERALE ! - 5-28 DEVE AVERE UNA SPINTA MAGGIORE !
                    
                    
                    
                    
                    
                    
                # BUY 2 che ci riprova TORNANDO ALLE ORIGINI (TREND RIBASSO !) con ma200< and ma300< AND 100 molto sotto 300
                
                elif (
                    deviation_buy2 > 0.06
                    and deviation_ma100_sopra_ma300 < -0.20
                    and deviation_ma5_sopra_ma28 > 0.15
                    
                    and deviation_bellissima > 0.14
                    and ma8_last > ma8_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma7_last
                    and ma3_last > ma13_last
                    and deviation_buy_ma3_sopra_ma20 > 0.05
                    and deviation_ma4_sopra_ma25 > 0.05
                    
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                ):
               
                    buy = "BUY 2 che ci riprova TORNANDO ALLE ORIGINI (TREND RIBASSO !) con ma200< and ma300< AND 100 molto sotto 300 - r 3993"
                    action = "buy"
                    percentage = 70

                    # compare prega per me !
                    # se ma200< e ma300< si torna alle origini ! 8-50 ! (con ma2 > ma2 2 min ago)
                    # deviation_buy2 = ma8_last / ma50_last
                    
                    # 9 giu 2022 dev_buy2 (8-50) a 0.06 da 0.08
                    # 9 giu 2022 dev_bellissima a 0.15 da 0.16
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
                # BUY 2 con ma200> e ma300> DURANTE UNA piccola CORREZIONE che NON E' un forte ribasso e NON E' un crollo !  
                
                elif (

                    ma2_last > ma2_2_min_ago
                    and ma28_last > ma28_30_min_ago
                    
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    and ma200_last > ma300_last
                    and deviation_buy_crollo_1 < -0.33
                    and deviation_buy_crollo_1 > -0.59
                    and deviation_correzione > 0.017
                    and deviation_buy_ma5_sopra_ma20 > 0.12
                    
                ):

                    buy = "BUY 2 con ma200> e ma300> DURANTE UNA piccola CORREZIONE che non e' un forte ribasso e non e' un crollo - r 4035"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                    
                # BUY 2 con ma200> e ma300> DURANTE UNA piccola CORREZIONE che NON E' un forte ribasso e NON E' un crollo !  
                
                elif (

                    ma2_last > ma2_2_min_ago
                    and ma28_last < ma28_30_min_ago
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    and ma200_last > ma300_last
                    and deviation_buy_crollo_1 < -0.33
                    and deviation_buy_crollo_1 > -0.59
                    and deviation_correzione > 0.017
                    and deviation_buy_ma5_sopra_ma20 > 0.12
                    
                    and deviation_ma5_sopra_ma28 > 0.18
                ):

                    buy = "BUY 2 con ma200> e ma300> DURANTE UNA piccola CORREZIONE che non e' un forte ribasso e non e' un crollo - r 4059"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                  
                    
                 
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
                    buy = "BUY 2 che considera il passare del tempo (SE > 120 min) and 5-28 > 0.10 and ma30 > ma 30 40 min ago (TREND IN RIALZO) - r 4092"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                    
                    
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
                    buy = "BUY 2 che considera il passare del tempo (SE > 120 min) and 5-28 > 0.17 and ma30 < ma30 40 min ago (TREND IN RIBASSO) - r 4116"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                
                # BUY 2 FIAT che non funzionava MA CHE HA FUNZIONATO BENISSIMO ! ( DOPPIO DELTA AND 100> ) risalita ! copiato da BUY 1 perche' PERFETTO
                
                elif (    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
                    and ma3_last > ma9_last
                    
                    and ma200_last < ma300_last
                    and ma20_last < ma100_last
                    and ma100_last < ma100_10_min_ago
                    and deviation_ma200_sotto_ma300 < -0.27
                  
                    
                    and delta_1 < delta_2
                    and ma100_last > ma100_60_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.07
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 2 FIAT che non funzionava MA CHE HA FUNZIONATO BENISSIMO ( SOTTO RIALZO RIALZO ) GIORNO ! copiato da BUY 1 - r 4142"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                    
                # BUY 2 RIALZO IMPROVVISO ! con ma200 > and ma100_last > ma200_last
                
                elif (
                    ma200_last > ma200_20_min_ago
                    and ma100_last > ma200_last
                    and deviation_ma100_sopra_ma300 > 0.40
                    
                    and deviation_rialzo_improvviso_sopra > 0.46
                    and deviation_rialzo_improvviso_1 > 0.46
                    and deviation_rialzo_improvviso_2 > 0.19
                    and deviation_rialzo_improvviso_3 > 0.19
                    and deviation_range_1 < 0.20
                    and deviation_range_1 > -0.20
                    and deviation_range_2 < 0.20
                    and deviation_range_2 > -0.20
                    and deviation_range_x < 0.20
                    and deviation_range_x > -0.20
                ):
             
                    buy = "BUY 2 RIALZO IMPROVVISO ! con ma200 > and 100>200 (solo per il buy 2 e per il buy 3) AND 100 SOPRA 300 > 0.40 - r 4167 a"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                # BUY 2 RIALZO IMPROVVISO ! con ma200 > and ma100_last > ma200_last
                
                elif (
                    ma200_last > ma200_20_min_ago
                    and ma100_last > ma200_last
                    and deviation_ma100_sopra_ma300 < 0.40
                    
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
             
                    buy = "BUY 2 RIALZO IMPROVVISO ! con ma200 > and 100>200 (solo per il buy 2 e per il buy 3) AND 100 SOPRA 300 < 0.40 - r 4167 b"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
                
                # --------------------------------------- BUY 2 che entra in azione se ma2 va sopra SELL 1 di almeno 0.45 !
                
                elif (     
                    seconds_since_last_trade > max_hold_time_in_seconds_delta_buy2_sell1
                    and delta_buy2_dal_sell1 > 0.30
                    and deviation_ma5_sopra_ma28 > 0.29
                    
                    and ma100_last > ma100_60_min_ago
                    and ma200_last > ma200_120_min_ago
                    and ma100_last > ma200_last
                    and ma3_last > ma8_last
                    and ma5_last > ma18_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 2 che entra in azione se DOPO 2 MINUTI ma2 va sopra SELL 1 > 0.30 E 5-28 > 0.29 ! - r 4187"
                    action = "buy"
                    percentage = 70
                    
                    # il BUY 2 con deviation buy2 (8-50) ma anche con (6-30) ARRIVA IN RITARDO !
                    
                    # 16 giu 2022 delta_buy2_dal_sell1 a 0.30 da 0.45
                    # vedi r180
                    # vedi r409
                    # vedi r1829
                    # compa prega per me !
                    
                    
                
                
                
                
                
                
                # BUY 2 ECCEZIONALE - se ma100 sale da 20 min compra con 4-30 IMPORTATA DA RCCR perche' andava molto bene nel trend laterale

                elif (
                    
                    ma200_last > ma200_20_min_ago
                    and deviation_buy_ma2_sopra_ma5 > 0.10
                    
                    and deviation_ma5_sopra_ma28 > 0.27
                    and ma5_last > ma15_last
                    and deviation_ma4_sopra_ma30 > 0.13
                    and deviation_correzione > 0.12
                    
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 2 ECCEZIONALE se ma200 sale da 20 min compra con deviation 4-30 and deviation 3-25 IMPORTATA DA RCCR - riga 4220"
                    action = "buy"
                    percentage = 70
                    
                    # deviation_correzione = 3/25    
                    # non toccare 5 > 15 !
                    # and deviation_buy_ma2_sopra_ma5 > 0.10 FONDAMENTALE
                    
                    
                    
                    
                    
                    
                    
                    
                
                
                # BUY 2 PENULTIMA condizione ! ma tutte negative MA BUY con 8 > 125
                
                elif (     
               
                    ma25_last > ma200_last
                    and ma100_last < ma100_60_min_ago
                    and ma200_last < ma200_60_min_ago
                    and ma300_last < ma300_60_min_ago
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    and deviation_buy_ma5_sopra_ma20 > 0.05
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 2 PENUULTIMA CONDIZIONE ! ma tutte negative MA BUY con 25-200 (ho sostituito 8 > 125) - r 4251"
                    action = "buy"
                    percentage = 70
                    
                    # BUY con 25>200 ha sostituito 8>125 (che un po' mi piaceva ma era troppo rischiosa)
                    
                    
                    
                    
                
                
                
                # BUY 2 con ma200 che sale da 60 min etc. importata dal BUY 3 RCCR
                
                elif (
                    ma10_last >= ma10_2_min_ago
                    and ma200_last > ma200_60_min_ago
                    and deviation > -0.40
                    
                    and ma33_last > ma78_last
                    and deviation_ma5_sopra_ma28 > 0.14
                    
                    and deviation_ma4_sopra_ma30 > 0.11
                    and ma3_last > ma13_last
                    and ma4_last > ma9_last
                    and deviation_ma7_sopra_ma40 > 0.05
                    and ma7_last > ma25_last
                    
                    and deviation_buy_ma2_sopra_ma13 > 0.10
                    and ma4_last > ma50_last
                    and ma2_last >= ma2_2_min_ago
                    
                ):  
                
                    buy = "BUY 2 con ma200 che sale da 60 min 33 > 78 ! - r 4281 A"
                    action = "buy"
                    percentage = 70
                    
                    
                # BUY 2 con ma200 che sale da 60 min etc. importata dal BUY 3 RCCR
                
                elif (
                    ma10_last >= ma10_2_min_ago
                    and ma200_last > ma200_60_min_ago
                    and deviation > -0.40
                    
                    and ma33_last < ma78_last
                    and deviation_ma3_sopra_ma10 > 0.20
                    and deviation_ma5_sopra_ma28 > 0.14
                    
                    and deviation_ma4_sopra_ma30 > 0.11
                    and ma3_last > ma13_last
                    and ma4_last > ma9_last
                    and deviation_ma7_sopra_ma40 > 0.03
                    and ma7_last > ma25_last
                    
                    and deviation_buy_ma2_sopra_ma13 > 0.10
                    and ma4_last > ma50_last
                    and ma2_last >= ma2_2_min_ago
                    
                ):  
                
                    buy = "BUY 2 con ma200 che sale da 60 min 33 < 78 ! - r 4281 B"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                # BUY 2 RIVOLUZIONARIO se ma39 > ma50 - r 3450
                
                elif (
                    deviation_ma4_sopra_ma30 > 0.15
                    and ma200_last > ma200_120_min_ago
                    and deviation > -0.30
                    and deviation_bellissima > 0.07
                    and ma39_last > ma50_last
                    and delta_buy3_incrocio_ma3_ma8 >= 0.06
                    and ma3_last > ma8_last
                    and ma3_last >= ma69_last
                    and ma4_last >= ma4_2_min_ago
                    and ma2_last >= ma2_2_min_ago
                    and ma5_last >= ma15_last
                    and ma5_last >= ma25_last
                ):    
                    buy = "BUY 2 RIVOLUZIONARIO se ma39 > ma50 - r 4307"
                    action = "buy"
                    percentage = 70
                    
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    
                    
                    
                # BUY 2 RIVOLUZIONARIO se ma39 > ma50 - r 3450
                
                elif (
                    deviation_ma4_sopra_ma30 > 0.14
                    and ma200_last < ma200_120_min_ago
                    and deviation > -0.30
                    and deviation_bellissima > 0.06
                    and ma28_last > ma50_last
                    and delta_buy3_incrocio_ma3_ma8 >= 0.06
                    and ma3_last > ma8_last
                    and ma3_last >= ma69_last
                    and ma4_last >= ma4_2_min_ago
                    and ma2_last >= ma2_2_min_ago
                    and ma5_last >= ma15_last
                    and ma5_last >= ma25_last
                ):    
                    buy = "BUY 2 RIVOLUZIONARIO se ma39 > ma50 - r 4331"
                    action = "buy"
                    percentage = 70
                    
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    
                    
                    
                
                
                
                
                
                
                
                
                
                
                
                # BUY 2 ultima condizione ! ma tutte negative MA BUY con 50-100 (integra r2505)
                
                elif (     
               
                    ma50_last > ma100_last
                    and ma100_last < ma100_60_min_ago
                    and ma200_last < ma200_60_min_ago
                    and ma300_last < ma300_60_min_ago
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    and deviation_ma5_sopra_ma28 > 0.12
                    and deviation_buy_ma5_sopra_ma20 > 0.05
                    
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 2 ULTIMA CONDIZIONE ! ma tutte negative MA 50 > 100 (integra r2505) - r 4366"
                    action = "buy"
                    percentage = 70
                    
                    # aggiunta di 5-28 < 0.12
                    
           
            ############################################################################################################ COMPRA sessione 3
            
            # forse dal BUY 3 in poi (o dal BUY 4 in poi) DEVE ESSERE ma100 > E ma2 > ma100 !
            # deviation_buy3 = ma4_last/ma30_last 
                    

            elif self.session == 3:
                
                if (
                    ma10_last > ma10_2_min_ago
                    and ma28_last > ma69_last
                    
                    and ma200_last > ma200_60_min_ago
                    and deviation > -0.30
                    and deviation_ma3_sopra_ma10 > 0.11
                    and deviation_ma5_sopra_ma28 > 0.14
                    
                    and deviation_ma4_sopra_ma30 > 0.11
                    and ma3_last > ma13_last
                    and ma4_last > ma9_last
                    and deviation_ma7_sopra_ma40 > 0.08
                    and ma7_last > ma25_last
                    
                    and deviation_buy_ma2_sopra_ma13 > 0.10
                    and ma4_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                    
                ):  
                
                    buy = "BUY 3A con ma200 che sale da 60 min and ma28_last > ma69_last - r 4401"
                    action = "buy"
                    percentage = 80

                    # deviation_buy3 = ma4_last/ma30_last
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    
                    
                    
                    
                    
                    
                
                
                ######################################################### raddoppiate con 100> o con 100< 
                
                elif (
                    ma10_last > ma10_2_min_ago
                    and ma28_last < ma78_last
                    and ma100_last > ma100_60_min_ago
                    
                    and ma200_last > ma200_60_min_ago
                    and deviation > -0.30
                    and deviation_ma5_sopra_ma28 > 0.155
                    
                    and deviation_ma4_sopra_ma30 > 0.11
                    and ma3_last > ma13_last
                    and ma4_last > ma9_last
                    and deviation_ma7_sopra_ma40 > 0.08
                    and ma7_last > ma25_last
                    
                    and deviation_buy_ma2_sopra_ma13 > 0.10
                    and ma4_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                    
                ):  
                
                    buy = "BUY 3A con ma200 che sale da 60 min and ma28_last < ma78_last MA 100> 60 min ago - r 4438"
                    action = "buy"
                    percentage = 80

                    # deviation_buy3 = ma4_last/ma30_last
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    
                    
                    
                    
                elif (
                    ma10_last > ma10_2_min_ago
                    and ma28_last < ma78_last
                    and ma100_last < ma100_60_min_ago
                    
                    and ma200_last > ma200_60_min_ago
                    and deviation > -0.30
                    and deviation_ma5_sopra_ma28 > 0.22
                    
                    and deviation_ma4_sopra_ma30 > 0.11
                    and ma3_last > ma13_last
                    and ma4_last > ma9_last
                    and deviation_ma7_sopra_ma40 > 0.08
                    and ma7_last > ma25_last
                    
                    and deviation_buy_ma2_sopra_ma13 > 0.10
                    and ma4_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                    
                ):  
                
                    buy = "BUY 3A con ma200 che sale da 60 min and ma28_last < ma78_last - r 4469"
                    action = "buy"
                    percentage = 80

                    # deviation_buy3 = ma4_last/ma30_last
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                # BUY 3A con ma69 > MA ma200 scende da 60 min ! MA CON ma300>60 min ago
                
                elif (
                    ma69_last >= ma69_2_min_ago
                    and ma200_last < ma200_60_min_ago
                    and ma300_last < ma300_60_min_ago
                    
                    and deviation_ma3_sopra_ma10 > 0.14
                    and deviation_bellissima > 0.35
                    and deviation > -0.30
                    
                    and deviation_buy3 > 0.12
                    and deviation_ma4_sopra_ma30 > 0.12
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.08
                    and ma4_last > ma9_last
                    and ma7_last > ma25_last
                    and deviation_buy_ma2_sopra_ma13 > 0.10
                    and ma4_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                ):      
              
                    buy = "BUY 3A con ma69 > MA ma200 scende da 60 min ! e CON ma300 < 60 min ago - r 4510"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                    
                # BUY 3 nuovo TREND LATERALE !
                
                elif (
                    ma100_last > ma300_last
                    and ma100_last > ma200_last
                    and ma8_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                        
                    and deviation_ma100_sopra_ma300 < 0.04
                    and deviation_ma100_sopra_ma200 < 0.05
                    and deviation_ma5_sopra_ma28 > 0.07
                ):
                    buy = "BUY 3 nuovo TREND LATERALE ! - r 4530"
                    action = "buy"
                    percentage = 80
                    
                    # SE ma100 E' cosi' VICINA A ma200 E ma300 vuo dire che non c'e' un grande rialzo in atto ma un TREND LATERALE !
                    
                    
                    
                    
                    
                #  BUY 3A con ma69 > MA ma200 scende da 60 min ! and ma300_last > ma300_60_min_ago
                
                elif (
                    ma3_last > ma300_last
                    and ma200_last < ma200_60_min_ago
                    and ma300_last > ma300_60_min_ago
                    
                    and deviation_bellissima > 0.35
                    and deviation > -0.30
                    
                    and deviation_buy3 > 0.12
                    and deviation_ma4_sopra_ma30 > 0.12
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.08
                    and ma4_last > ma9_last
                    and ma7_last > ma25_last
                    and deviation_buy_ma2_sopra_ma13 > 0.10
                    and ma4_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                ):      
              
                    buy = "BUY 3A con ma69 > MA ma200 scende da 60 min ! and ma300_last > ma300_60_min_ago - r 4561"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                elif (
                    deviation_ma4_sopra_ma30 > 0.15
                    and deviation > -0.30
                    and deviation_bellissima > 0.07
                    and ma39_last > ma50_last
                    and delta_buy3_incrocio_ma3_ma8 >= 0.06
                    and ma3_last > ma8_last
                    and ma3_last >= ma69_last
                    and ma4_last >= ma4_2_min_ago
                    and ma2_last >= ma2_2_min_ago
                    and ma5_last >= ma15_last
                    and ma5_last >= ma25_last
                ):    
                    buy = "BUY 3B da RCCR - se ma39 > ma50 - r 4593"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                elif (
                    deviation_ma4_sopra_ma30 > 0.15
                    and (ma3_prev < ma22_prev and ma3_last > ma22_last)
                    and deviation > -0.30
                    and deviation_bellissima > 0.07
                    and ma39_last > ma50_last
                    and delta_buy3_incrocio_ma3_ma8 >= 0.06
                    and ma3_last > ma8_last
                    and ma3_last >= ma69_last
                    and ma4_last >= ma4_2_min_ago
                    and ma2_last >= ma2_2_min_ago
                    and ma5_last >= ma15_last
                    and ma5_last >= ma25_last
                ):    
                    buy = "BUY 3C RIVOLUZIONARIO se ma39 > ma50 - r 4614"
                    action = "buy"
                    percentage = 80
                    
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    # ho dovuto aggiungere incrocio dal basso!
                    
                    
                    
                    
                    
                
              
                elif (
                    ma69_last < ma69_2_min_ago
                    and deviation > -0.30
                    
                    and deviation_buy3 > 0.02
                    and deviation_ma13_sopra_ma25 > 0.040
                    and delta_buy3_incrocio_ma3_ma8 > 0.07
                    and deviation_ma4_sopra_ma30 > 0.14
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                ):
                    buy = "BUY 3D RIVOLUZIONARIO se ma69 < - r 4641"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy3 = ma4_last/ma30_last
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    
                    
                    
                    
                # BUY 3 importata da RCCR - AUDI CHE NON E' UN CROLLO ! con 5-16
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.60
                    and deviation_buy_crollo_1 > -1.50
                    
                    and deviation_ma5_sopra_ma16 > 0.01
                    and ma5_last > ma16_last
                    
                    and ma2_last > ma2_2_min_ago
                    and ma78_last < ma200_last
                    
                ):
                    buy = "BUY 3 importata da RCCR - AUDI CHE NON E' UN CROLLO ! con 5-16 > 0.01 - riga 4668"
                    action = "buy"
                    percentage = 90
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # questa cosa che 78 deve essere < 200 ha dell' incredibile. MA NON TOCCARE !   
                    
                    
                    
                    
                    
                    
                # BUY 3 FORTE RIBASSO che NON E' UN CROLLO ! (compare stammi vicino!) da BUY2 RCCR
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -0.60
                    and deviation_buy_crollo_1 > -1.50
                    and deviation_bellissima > 0.17
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and ma100_last < ma100_120_min_ago
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
             
                    
                ):
                    buy = "BUY 3 FORTE RIBASSO che NON E' UN CROLLO ! and deviation_bellissima > 0.17  da BUY2 RCCR - r 4669"
                    action = "buy"
                    percentage = 90
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    
                    
                    
                    
                    
                    
                # BUY 3 NUOVO che ci riprova TORNANDO ALLE ORIGINI con ma200< and ma300<
                
                elif (
                    deviation_buy2 > 0.05
                    and deviation_ma5_sopra_ma28 > 0.15
                    
                    and ma8_last > ma8_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma7_last
                    and ma3_last > ma13_last
                    and deviation_buy_ma3_sopra_ma20 > 0.05
                    and deviation_ma4_sopra_ma25 > 0.05
                    
                    
                    and ma100_last > ma200_last
                    and ma200_last < ma200_60_min_ago
                    
                ):
               
                    buy = "BUY 3 NUOVO che ci riprova TORNANDO ALLE ORIGINI con ma200<  MA 100 e' andata sopra 200 ! - r 4699"
                    action = "buy"
                    percentage = 90

                    # compare prega per me !
                    # se ma200< MA 100 e' andata sopra 200 ! si torna alle origini ! 8-50 ! (con ma2 > ma2 2 min ago)
                    # deviation_buy2 = ma8_last / ma50_last
                    
                    
                    
                    
                    
                    
                    
                    
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
             
                    buy = "BUY 3 RIALZO IMPROVVISO ! con ma200 > and 100>200 (solo per il buy 2 e per il buy 3) - r 4731"
                    action = "buy"
                    percentage = 80
                    
                    
                    
            
                # BUY 3 CON IL TURBO ! (compare stammi vicino!)   
                
                elif (    
                    ma200_last > ma200_120_min_ago
                    and deviation > -0.30
                    and ma200_last > ma300_last
                    and ma20_last > ma200_last
                    
                    and deviation_ma3_sopra_ma10 > 0.145
                    and deviation_bellissima > 0.05
                    and (ma4_prev < ma25_prev and ma4_last > ma25_last)
                    and ma25_last > ma25_2_min_ago
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 3 CON IL TURBO - r 4750"
                    action = "buy"
                    percentage = 80
                    
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    
                    
                    
                    
                    
                
                ################################################################### condizioni che mancavano !!!
                
                # BUY 3 primo modo che ci riprova DURANTE IL CROLLO !

                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -2.30
                    and ma2_last > ma7_last
                ):
                    buy = "BUY 3 che ci riprova DURANTE IL CROLLO - modo 1 2-7 - r 4770"
                    action = "buy"
                    percentage = 90
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    
                    
                    
               
                # BUY 3 secondo modo che ci riprova DURANTE IL CROLLO !
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -1.70
                    and deviation_buy_crollo_1 > -2.29
                    and deviation_buy_crollo_2 > 0.11
                    and deviation_ma5_sopra_ma28 > 0.03
                ):
                    buy = "BUY 3 che ci riprova DURANTE IL CROLLO - modo 2 - r 4788"
                    action = "buy"
                    percentage = 90
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_buy_crollo_2 = ma3_last / ma13_last
                    
                    
                    
                    
                # BUY 3 che ci riprova DURANTE IL CROLLO - modo 3
                
                elif (
                    
                    ma5_last > ma20_last
                    
                    and deviation_ma5_sotto_ma300 < -2.40
                    and deviation_ma100_laterale < -1.90
                    and deviation_ma28_sotto_ma100 < -0.80
                    
                    
                    and ma100_last < ma100_120_min_ago
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and ma2_last > ma2_2_min_ago
                    
                ):
                    buy = "BUY 3 che ci riprova DURANTE IL CROLLO - modo 3 - r 4819"
                    action = "buy"
                    percentage = 90
                    
                    # and deviation_ma100_laterale < -1.90 e' 5 sotto 100 (NON TI PREOCCUPARE)
                    # QUESTA CONDIZIONE E' STATA CREATA DOPO AVER VISTO UN CROLLO DOPO IL BUY 2 ma il BUY 3 non entrava in azione !
                    
                    
                    
                    
                    
                    
                
                
                
                # BUY 3 ultima condizione che mancava ! ma tutte negative MA BUY con 8 > 125
                
                elif (     
               
                    ma8_last > ma150_last
                    and ma100_last < ma100_60_min_ago
                    and ma200_last < ma200_60_min_ago
                    and ma300_last < ma300_60_min_ago
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    and deviation_buy_ma5_sopra_ma20 > 0.05
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 3 ULTIMA CONDIZIONE che mancava ! ma tutte negative MA BUY con 8-150 - r 4848"
                    action = "buy"
                    percentage = 80
                    
                    # BUY 3 ULTIMA CONDIZIONE che mancava con 8-150
                    
                    
                    
                    
                    
                    
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

                    buy = "BUY 3 PAZZA piccola CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo ! con deviation_correzione > 0.02 - r 4873"
                    action = "buy"
                    percentage = 80

                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    # ma5 non deve allontanarsi troppo dalla ma200 !
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
         
            # ########################################################################################################## COMPRA sessione 4
            
            # ---------------------------------------------------------------------------------------------------------- deviation piu' alte se ma 78 < !
            
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
                    buy = "BUY 4A con ma 78> e 300> E ma100>ma200 - r 4918"
                    action = "buy"
                    percentage = 70
          
                    # se al BUY 4 ha ma100 < ma200 evidentemente c'e' qualche cosa di strano 
                    # il trend, evidentemente, e' LATERALE.
                    # E ALLORA AGGIUNGO UN BEL 6-30 > 0.15 - TREND LATERALE
             
                
                
                
                
                
                
                
                # BUY 4 di emergenza CROLLO FERRARI - modo 1
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -2.30
                    and ma3_last > ma28_last
                ):
                    buy = "BUY 4 di emergenza CROLLO FERRARI - modo 1 - 3-28 - r 4940"
                    action = "buy"
                    percentage = 70
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # SALTA IL BUY 2 allora ho fatto il BUY 3 di emergenza (se <-2.30 si attiva 8-25)
                    
                    
                    
                
                
                # BUY 4 di emergenza CROLLO FERRARI - modo 2 

                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -1.61
                    and deviation_buy_crollo_1 > -2.29
                    and deviation_buy_crollo_2 > 0.11
                    and ma8_last > ma50_last
                ):
                    buy = "BUY 4 di emergenza CROLLO FERRARI - modo 2 - r 4960"
                    action = "buy"
                    percentage = 70
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_buy_crollo_2 = ma3_last / ma13_last
                    # SALTA IL BUY 2 allora ho fatto il BUY 3 di emergenza (se <-1.61 si attiva 8-50)
                    
                    
                    
                    
                elif (
                    deviation_ma4_sopra_ma30 > 0.14
                    and ma300_last > ma300_120_min_ago
                    
                    and deviation > -0.30
                    and deviation_bellissima >= 0.06
                    and ma39_last >= ma48_last
                    and delta_buy3_incrocio_ma3_ma8 >= 0.06
                    and ma3_last > ma8_last
                    and ma3_last >= ma69_last
                    and ma4_last >= ma4_2_min_ago
                    and ma2_last >= ma2_2_min_ago
                    and ma5_last >= ma15_last
                    and ma5_last >= ma25_last
                ):    
                    buy = "BUY 4B importato da BUY 3 RCCR se ma39 > ma48 con 300 > - r 4961a"
                    action = "buy"
                    percentage = 70  
                    
                    
                elif (
                    deviation_ma4_sopra_ma30 > 0.15
                    and ma300_last < ma300_120_min_ago
                    
                    and deviation > -0.30
                    and deviation_bellissima > 0.07
                    and ma39_last > ma50_last
                    and delta_buy3_incrocio_ma3_ma8 >= 0.06
                    and ma3_last > ma8_last
                    and ma3_last >= ma69_last
                    and ma4_last >= ma4_2_min_ago
                    and ma2_last >= ma2_2_min_ago
                    and ma5_last >= ma15_last
                    and ma5_last >= ma25_last
                ):    
                    buy = "BUY 4B importato da BUY 3 RCCR se ma39 > ma50 con 300 < - r 4961b"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                    
                    
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
                    buy = "BUY 4A con ma 78 > TREND LATERALE con 6-30 > 0.15 - r 4989"
                    action = "buy"
                    percentage = 70
                    
               
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
                    buy = "BUY 4A con ma 78> e 300< ma 100>200 - r 5017"
                    action = "buy"
                    percentage = 70
                    
               
                    
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
                    buy = "BUY 4A con ma 78> e 300< e 100<200 - r 5045"
                    action = "buy"
                    percentage = 70
                    
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
                    buy = "BUY 4B RIVOLUZIONARIO con ma78 > - r 5068"
                    action = "buy"
                    percentage = 70
                    
                    # deviation_buy3 = ma4_last/ma30_last
                    # deviation_ma4_sopra_ma100 > 0.25 arrivati al buy 4 DEVE AVERE UNA CERTA FORZA !
                    
                
                
                
                
                
                
                
                
                
                elif (
                    ma78_last >= ma78_2_min_ago
                    and ma300_last < ma300_60_min_ago
                    and deviation_ma4_sopra_ma100 > 0.24
                    and ma39_last > ma100_last
                    
                    and deviation_buy3 > 0.01
                    and delta_buy3_incrocio_ma3_ma8 > 0.05
                    and deviation_ma4_sopra_ma30 > 0.15
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last >= ma4_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                    
                    and ma13_last > ma100_last
                    and deviation_ma5_sopra_ma28 > 0.10
                ):
                    buy = "BUY 4B RIVOLUZIONARIO con ma78 > and ma39_last > ma100_last - r 5102"
                    action = "buy"
                    percentage = 70
                    
                    # deviation_buy3 = ma4_last/ma30_last
                    # deviation_ma4_sopra_ma100 > 0.25 arrivati al buy 4 DEVE AVERE UNA CERTA FORZA !
                    
                    
                    
                    
                elif (
                    ma78_last >= ma78_2_min_ago
                    and ma300_last < ma300_60_min_ago
                    and deviation_ma4_sopra_ma100 > 0.25
                    and ma39_last < ma100_last
                    
                    and deviation_buy3 > 0.02
                    and delta_buy3_incrocio_ma3_ma8 > 0.05
                    and deviation_ma4_sopra_ma30 > 0.16
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last >= ma4_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                    
                    and ma13_last > ma100_last
                    and deviation_ma5_sopra_ma28 > 0.10
                ):
                    buy = "BUY 4B RIVOLUZIONARIO con ma78 > and ma39_last < ma100_last - r 5130"
                    action = "buy"
                    percentage = 70
                    
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
                    buy = "BUY 4C RIVOLUZIONARIO con ma78 < - r 5164"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                
                # BUY 4C RIVOLUZIONARIO con ma78 <
                
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
                    buy = "BUY 4C RIVOLUZIONARIO con ma78 < - r 5190"
                    action = "buy"
                    percentage = 70
                    
                    
                
                
                
                
                # BUY 4 se 11 > 200 e con ma69 > and deviation_bellissima > 0.12 (PER SPEZZARE LA CATENA - effetti laterali) IMPORTATA DA BUY 5
                
                elif (
                    ma69_last >= ma69_2_min_ago
                    and ma11_last > ma200_last
                    and deviation_bellissima > 0.12
                    and deviation_buy3 > 0.12
                    and deviation_ma7_sopra_ma40 > 0.09
               
                    and ma3_last > ma13_last
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    and ma6_last > ma15_last
                    and ma7_last > ma25_last
                    
                    and ma2_last > ma2_2_min_ago
             
                ):
                    buy = "BUY 4 se 11 > 200 e con ma69 > and deviation_bellissima > 0.12 (PER SPEZZARE LA CATENA - effetti laterali) DA BUY 5 RCCR - riga 5217"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                    
                # BUY 4 NUOVA (trend laterale) con ma8_last > ma100_last AND and ma300_last > ma300_120_min_ago
                
                elif (
                    ma69_last >= ma69_2_min_ago
                    and ma8_last > ma100_last
                    and ma100_last > ma300_last
                    and ma100_last > ma100_60_min_ago
                    and ma300_last > ma300_120_min_ago
                    and deviation_ma5_sopra_ma28 > 0.12
                    
                    and deviation_bellissima > 0.11
                    and deviation_buy3 > 0.12
                    and deviation_ma7_sopra_ma40 > 0.09
               
                    and ma3_last > ma13_last
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    and ma6_last > ma15_last
                    and ma7_last > ma25_last
                    
                    and ma2_last > ma2_2_min_ago
             
                ):
                    buy = "BUY 4 NUOVA (trend laterale) 8 > 100 AND ma300_last > ma300_120_min_ago AND 5-28 > 0.12 e con ma69 > - riga 5247"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                    
                # BUY 4 se 8 > 200 con 5-28 > 0.20 ! e con ma69 > and deviation_bellissima > 0.12 (PER SPEZZARE LA CATENA - effetti laterali) IMPORTATA DA BUY 5
                
                elif (
                    ma69_last >= ma69_2_min_ago
                    and ma8_last > ma200_last
                    and deviation_ma5_sopra_ma28 > 0.20
                    
                    and deviation_bellissima > 0.12
                    and deviation_buy3 > 0.12
                    and deviation_ma7_sopra_ma40 > 0.09
               
                    and ma3_last > ma13_last
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    and ma6_last > ma15_last
                    and ma7_last > ma25_last
                    
                    and ma2_last > ma2_2_min_ago
             
                ):
                    buy = "BUY 4 se 11 > 200 con 5-28 > 0.20 ! e con ma69 > (PER SPEZZARE LA CATENA - effetti laterali) DA BUY 5 RCCR - riga 5274"
                    action = "buy"
                    percentage = 70
                    
                    # deviation_bellissima = 6/30
                    # spezzare la catena dei buy - effetti laterali.
                    # se e' arrivato il buy 5 e' molto probabile che il trend sia consolidato
                    # e, a questo punto, non importa se compra con un + 0.10 piu' in alto. NON FA UNA GRANDE DIFFERENZA !
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
          
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
           
                    buy = "BUY 4A PAZZA DURANTE UNA piccola CORREZIONE che non e' un forte ribasso e non e' un crollo ! con deviation_correzione > 0.02 - r 5309"
                    action = "buy"
                    percentage = 70
                    
                    # capita a volte il buy 4. fai attenzione! (se BUY 4 sta sotto ma78 e' un caso particolare !)

                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    # ma5 non deve allontanarsi troppo dalla ma200 !
                    
                    
                    
              
            ############################################################################################################  compra sessione 5 in poi
            
            #################################################### ATTENZIONE! HO MESSO and ma78_last > ma150_last (50>100 non e' stata sufficiente)
            
            #################################################### STIAMO AL BUY 5 PERDIO !
            
            
            #  piu' alto il BUY - "effetti laterali"

            else:
                
                if (
                    ma50_last >= ma50_2_min_ago
                    and ma28_last > ma28_30_min_ago
                    and ma78_last > ma150_last
                    
                    and deviation_ma5_sopra_ma28 > 0.12
                    
                    and deviation_buy3 > 0.09
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.09
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    
                    and ma6_last > ma15_last
                    and ma7_last > ma25_last
                    
                    and ma2_last > ma2_2_min_ago
                
                ):
                    buy = "BUY 5 con ma50 > AND 50>100 and ma28_last > ma28_30_min_ago and 5-28 > 0.12 - riga 5352"
                    action = "buy"
                    percentage = 70
                    
                    # 6 giu 2022 5-28 a 0.12 da 0.15
                    
                    
                    
                    
                    
                elif (
                    ma50_last >= ma50_2_min_ago
                    and ma28_last < ma28_30_min_ago
                    and ma78_last > ma150_last
                    
                    and deviation_ma5_sopra_ma28 > 0.17
                    
                    and deviation_buy3 > 0.10
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.09
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    
                    and ma6_last > ma15_last
                    and ma7_last > ma25_last
                    
                    and ma2_last > ma2_2_min_ago
                
                ):
                    buy = "BUY 5 con ma50 > AND 50>100 and ma28_last < ma28_30_min_ago and 5-28 > 0.17 - riga 5381"
                    action = "buy"
                    percentage = 70
                    
                    # 6 giu 2022 5-28 a 0.12 da 0.15
                
                
                
                
                
                
                
                
                elif (
                    ma50_last >= ma50_2_min_ago
                    and ma300_last > ma300_120_min_ago
                    
                    and ma78_last < ma150_last
                    and deviation_ma5_sopra_ma28 > 0.27
                    and ma50_last > ma100_last
                    
                    
                    and deviation_buy3 > 0.10
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.09
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    
                    and ma6_last > ma15_last
                    and ma7_last > ma25_last
                    and deviation_bellissima > 0.12
                    and ma2_last > ma2_2_min_ago
                
                ):
                    buy = "BUY 5 con ma50 > AND 50<100 and 300 > 60 min ago and 5-28 > 0.27 (SI !) - riga 5415"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                elif (
                    ma50_last >= ma50_2_min_ago
                    and ma300_last < ma300_120_min_ago
                    and ma78_last < ma150_last
                    and deviation_ma5_sopra_ma28 > 0.29
                    and ma50_last > ma100_last
                    
                    and deviation_ma3_sopra_ma10 > 0.07
                    
                    and deviation_buy3 > 0.10
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.09
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    
                    and ma6_last > ma15_last
                    and ma7_last > ma25_last
                    and deviation_bellissima > 0.12
                    and ma2_last > ma2_2_min_ago
                
                ):
                    buy = "BUY 5 con ma50 > and 300 < 60 min ago AND 50<100 and 5-28 > 0.29 (SI !) - riga 5441"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                    
                    
                    
                 
                    
                # BUY 5 di emergenza CROLLO FERRARI - modo 1
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -2.30
                    and ma3_last > ma28_last
                ):
                    buy = "BUY 5 di emergenza CROLLO FERRARI - modo 1 - 3-28 - r 5459"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # SALTA IL BUY 2 allora ho fatto il BUY 3 di emergenza (se <-2.30 si attiva 8-25)
                    
                    
                    
                    
                    
                    
                    
                elif (
                    ma50_last >= ma50_2_min_ago
                    and ma78_last < ma150_last
                    and deviation_ma5_sopra_ma28 > 0.31
                    and ma50_last < ma100_last
                    
                    
                    and deviation_buy3 > 0.10
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.09
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    
                    and ma6_last > ma15_last
                    and ma7_last > ma25_last
                    and deviation_bellissima > 0.12
                    and ma2_last > ma2_2_min_ago
                
                ):
                    buy = "BUY 5 con ma50 > AND 50<100 and 5-28 > 0.31 (SI !) (PER SPEZZARE LA CATENA un po' di meno - vs effetti laterali) riga 5491"
                    action = "buy"
                    percentage = 70
                    
                    # deviation_bellissima = 6/30
                    # spezzare la catena dei buy - effetti laterali.
                    # se e' arrivato il buy 5 e' molto probabile che il trend sia consolidato
                    # e, a questo punto, non importa se compra con un + 0.10 piu' in alto. NON FA UNA GRANDE DIFFERENZA !
                    
                    
                    
                    
                    
                
                
                
                
                # BUY 5 TUTTE LE ma IN CRESCITA
                
                elif (
                    ma69_last < ma69_2_min_ago
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
                    
                    and ma100_last > ma200_last
                    and ma200_last > ma300_last
                    
                    and ma300_last > ma300_60_min_ago
                ):
                    buy = "BUY 5 CON TUTTE LE ma IN CRESCITA - r 5529"
                    action = "buy"
                    percentage = 70
                    
                    # deviation_buy3 = ma4_last/ma30_last
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    
                    
                    
                    
                    
                # ATTENZIONE ! AL BUY 5 TRANNE CHE IN UNA EVENTUALE CORREZIONE HO MESSO 78>150 STIAMO AL BUY 5 PERDIO !
                # SENZA QUESTA 78>150 HO AVUTO MOLTI PROBLEMI !
                
                
                elif (
                    ma78_last >= ma78_2_min_ago
                    and ma78_last > ma150_last
                    
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
                    buy = "BUY 5A con ma78 > and deviation_bellissima > 0.163 (PER SPEZZARE LA CATENA - effetti laterali) - r 5561"
                    action = "buy"
                    percentage = 70
                    
                    # deviation_bellissima = 6/30
                    # spezzare la catena dei buy - effetti laterali !
                    # se e' arrivato il buy 5 e' molto probabile che il trend sia consolidato
                    # e, a questo punto, non importa se compra con un + 0.10 piu' in alto. NON FA UNA GRANDE DIFFERENZA !
                    
                    
                
                elif (
                    ma200_last >= ma200_120_min_ago
                    and ma78_last > ma150_last
                    
                    and deviation_ma5_sopra_ma28 > 0.10
                    
                    and deviation_ma4_sopra_ma100 > 0.25
                    and ma3_last > ma15_last
                    and ma3_last > ma8_last
                    and ma3_last > ma78_last
                    and ma4_last > ma4_2_min_ago
                    and ma7_last > ma25_last
                    and ma13_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                ):   
                    buy = "BUY 5B RIVOLUZIONARIO che NON SPEZZA LA CATENA SE ma200> 120 min) - r 5587"
                    action = "buy"
                    percentage = 70
                    
                    # deviation_buy3 = ma4_last/ma30_last
                    # ok tu non voi spezzare la catena.
                    # ma per essere un BUY 5 devi avere almeno ma13>ma50 cazzo !
                    
                    
                    
             
                elif (
                    ma78_last >= ma78_2_min_ago
                    and ma78_last > ma150_last
                    
                    and deviation_ma4_sopra_ma100 > 0.25
                    
                    and deviation_ma3_sopra_ma10 > 0.07
                    
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
                    buy = "BUY 5C RIVOLUZIONARIO con ma78 > and deviation_bellissima > 0.163 (PER SPEZZARE LA CATENA -effetti laterali) - r 5616"
                    action = "buy"
                    percentage = 70
                    
                    
                    
              
                # BUY 5 copiata da buy1 r1313 con modifiche
                
                elif (    
                    
                    ma200_last > ma200_20_min_ago
                    and ma78_last > ma150_last
                    and deviation_ma5_sopra_ma28 > 0.10
                    and (ma5_prev < ma28_prev and ma5_last > ma28_last)
                    
                    and ma28_last > ma34_last
                    
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
                    
                    buy = "BUY 5 copiata da BUY 1 r1313 con modifiche - riga 5650"
                    action = "buy"
                    percentage = 70
                    
                    
                    
              
                # BUY 5D RIVOLUZIONARIO con ma78 < and deviation_bellissima > 0.163
                
                elif (
                    ma78_last < ma78_2_min_ago
                    and ma78_last > ma150_last
                    
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
                    buy = "BUY 5D RIVOLUZIONARIO con ma78 < and deviation_bellissima > 0.163 - r 5677"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                    
                    
                
                
                
                
                
                # RIALZO IMPROVVISO 200< DOPO TANTO TEMPO DI TREND LATERALE - POTREBBE SUCCEDERE !
                
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

                    buy = "BUY 5 RIALZO IMPROVVISO con 200 < tentando di evitare falsi acquisti DOPO TANTO TEMPO DI TREND LATERALE - POTREBBE SUCCEDERE ! - r 5713"
                    action = "buy"
                    percentage = 70
                    
                    # da 1.20 a 1.1 !
                    
                    
                    
                    
                # RIALZO IMPROVVISO 200> DOPO TANTO TEMPO DI TREND LATERALE - POTREBBE SUCCEDERE !
                
                elif (
                    ma200_last > ma200_20_min_ago
                    and deviation_rialzo_improvviso_sopra > 0.82
                    and deviation_rialzo_improvviso_1 > 0.46
                    and deviation_rialzo_improvviso_2 > 0.19
                    and deviation_rialzo_improvviso_3 > 0.19
                    and deviation_range_1 < 0.22
                    and deviation_range_1 > -0.22
                    and deviation_range_2 < 0.22
                    and deviation_range_2 > -0.22
                    and deviation_range_x < 0.22
                    and deviation_range_x > -0.22
                ):
             
                    buy = "BUY 5 RIALZO IMPROVVISO con 200 > e con > 0.72 DOPO TANTO TEMPO DI TREND LATERALE - POTREBBE SUCCEDERE ! - r 5738"
                    action = "buy"
                    percentage = 70
                    
                    # 6 giu 2022 deviation rialzo improvviso a 0.82 da 0.62
                    
                    
                    
                    
                # NELLA CORREZIONE EVENTUALE (SIAMO AL BUY 5 !) NON HO MESSO and ma50_last > ma100_last
                
                # BUY 5A PAZZA DURANTE UNA piccola CORREZIONE che NON E' un forte ribasso e NON E' un crollo ! (compare stammi vicino!)
                
                elif (
                    ma2_last >= ma2_2_min_ago
                    and deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
                    and deviation_correzione > 0.014
                    and deviation_buy_ma5_sopra_ma20 > 0.13
                    and deviation_ma5_sotto_ma200 > -1.20
                ):    
              
                    buy = "BUY 5 PAZZA DURANTE UNA piccola CORREZIONE che non e' un forte ribasso e non e' un crollo ! con deviation_correzione - r 5760"
                    action = "buy"
                    percentage = 80

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
           
            # VENDITA - con fasce di tempo ! i minuti sono espressi in secondi

            #   0 -  3
            #   3 -  5
            #   5 - 12
            #  12 - 21
            #  21 - 50
            #  50 - 90 
            #  90 - 110 solo le prime 2 sessioni  (> 90 min tutte le altre)
            #     > 110 solo le prime 2 sessioni
          
             
            # < -0.20
            # < -0.10  cuscino di sant' antonio se trend > e cuscino della madonna se trend <
            # 0.25 - 0.59  MARADONA 5-25 CHE DOPO 60 MIN DIVENTA 5-39 che dopo 90 min diventa 5-50
            # 0.60 - 1.20  RONALDO CHE DOPO 60 MIN DIVENTA 4-20
            # 1.21 - 2.50  TACCO DI ALLAH
            #  > 2.50      SI VIVE TRA GLI ANGELI, compa !
            
            # vendite eccezionali
            
            # aumento della perdita tollerata - trend e doppia deviation
            
            
            ####################################################################################################################### SESSIONE 1
            
            # al SELL 1 PUOI AUMENTARE LA PERDITA TOLLERATA POICHE' HAI SOLO IL 10%-20% DEL CAPITALE - eviterai, INOLTRE, un po' di sell e buy nel movimenti laterali !
            # la perdita tollerata ovviamente va aumentata anche alle 5 vendite eccezonali del SELL 1 sperando che la nuova indentazione ha funzionato
            # fino a questo momento vendevano SOLO le ULTIME 5 condizioni eccezionali
            
            
            
            ####################################################################################################################### sessione 1 ( 0 - 3 min )

            if self.session == 1:
                
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
                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.23 - r 5857"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                 
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.27 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.27 - 0.60 LA PRIMA FINTA DI MARADONA - r 5871"
                        action = "sell"
                        
                        
                
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.61 and deviation_sell < 0.79
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.61 - 0.79 IL PRIMO DRIBBLING ALLA RONALDO  - r 5883"
                        action = "sell"

                    # attenzione : tacco di allah e dribbling alla ronaldo SOLO con ma50> (altrimenti si attivano in "sell durante il crollo" che ha le sue leggi.)
                    
                    
                
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 0.80 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell 0.80 - 1.20 ( DOPPIA FINTA ALLA RONALDO ! ) - r 5898"
                        action = "sell"
                        
                        
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 1.21 and deviation_sell < 1.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell 1.21-1.7( TACCO DI ALLAH ! ) - r 5910"
                        action = "sell"
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 1.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell > 1.71 ( SI VA TRA GLI ANGELI, compa ! ) - r 5923"
                        action = "sell"
                        
                   
                
                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 < and incrocio 3-28 - r 5936"
                        action = "sell"

                    # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                    
                    
                   
                    
                    # SELL 1 (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 and rapporto_delta_1_delta_2 < 1
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        
                        
                        and delta_1 < delta_2
                        and ma100_last > ma100_60_min_ago
                        
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.29
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.29 SOTTO RIALZO RIALZO - GIORNO - r 5957"
                        action = "sell"
                        
                        
                        
                        
                    # SELL 1 (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 and rapporto_delta_1_delta_2 > 1
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        
                        
                        and delta_1 > delta_2
                        and ma100_last < ma100_60_min_ago
                        
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 SOTTO RIBASSO RIBASSO - NOTTE - r 5976"
                        action = "sell"
                        
                        
                   
                 
                    # ---------------------------------------------------------------------------------------------------------------------- crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - r 5990"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                   
                
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - r 6004"
                        action = "sell"
                        
                        
                      
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                        and deviation_sell > 0.61 and deviation_sell < 0.80
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - r 6017"
                        action = "sell"
                  
               
            
            
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma2_prev > ma5_prev and ma2_last < ma5_last)
                        and deviation_sell > 0.81
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - r 6030"
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
                        sell = "SELL 1 (3-5 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.24 - r 6048"
                        action = "sell"
                         
                        # deviation_sell = ma3_last/last_trade_price
                        
                
                
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.27 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                       
                        
                    ):
                        sell = "SELL 1 (3-5 min) con ma50> 5-25 and deviation_sell 0.27 - 0.60 - la prima FINTA ALLA MARADONA - r 6064"
                        action = "sell"
                         
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                     
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.61 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 > and incrocio 3-15 and deviation_sell 0.91 - 1.20 DRIBBLING ALLA RONALDO - r 6079"
                        action = "sell"
                        
                        
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 1.21 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 > and incrocio 3-20 and deviation_sell 1.21 -2.70 ( TACCO DI ALLAH ! ) - r 6091"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 > and incrocio 3-11 and deviation_sell > 2.71 ( SI VA TRA GLI ANGELI, comba ! ) - r 6103"
                        action = "sell"
                        
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 < and incrocio 3-28 - r 6118"
                        action = "sell"
                        
                        # deviation_sell_ma78 = ma3_last / ma78_last
                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.25
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.25 - r 6132"
                        action = "sell"

                    
                    
                    
                    # guadagno durante il crollo o il trend discendente
                     
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23 and deviation_sell < 0.80
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-23 and gain > 0.23 - r 6146"
                        action = "sell"
                        
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma2_prev > ma8_prev and ma2_last < ma8_last)
                        and deviation_sell > 0.81 and deviation_sell < 1.70
                        and ma2_last < ma2_2_min_ago

                    ):

                        sell = "SELL 1 CROLLO (3-5 min) con ma50 < and incrocio 2-8 and gain > 0.81-1.70 - r 6160"
                        action = "sell"

                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma9_prev and ma3_last < ma9_last)
                        and deviation_sell > 1.71
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-9 and gain > 1.71 - r 6173"
                        action = "sell"
                        
                        
                     

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 6185"
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
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - r 6206"
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
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - r 6223"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        
                        and deviation_sell > 0.27 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                    
                    ):
                        sell = "SELL 1 (5-12 min) con ma50> 5-25 and deviation_sell 0.27 - 0.60 - FINTA ALLA MARADONA - r 6239"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                      
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma13_last
                        
                        and deviation_sell > 0.61 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 >  3-13 and deviation_sell 0.61 - 0.90 - DRIBBLING ALLA RONALDO - r 6255"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 3-15 and deviation_sell 0.91 - 1.20 ( DOPPIA FINTA ALLA RONALDO ) - r 6271"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 1.21 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 3-15 and deviation_sell 1.21-2.70 ( TACCO DI ALLAH ! ) - r 6286"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 3-11 and deviation_sell > 2.71 ( SI STA TRA GLI ANGELI, compa! ) - r 6298"
                        action = "sell"
                        
                        
                      
                    
                    
                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.49
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 < and incrocio 3-28 and deviation_sell < -0.49 - r 6313"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 < and incrocio 3-100 (cuscino di sant' antonio) - r 6327"
                        action = "sell"
                        
                        
                    
                    
                    # ------------------------------------------------------------------------------- guadagno con crollo
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23 and deviation_sell < 0.54
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 < GUADAGNO DURANTE IL CROLLO 0.23-0.54 con incrocio 3-23 - r 6343"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 0.55
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 < GUADAGNO DURANTE IL CROLLO > 0.55  and incrocio 3-13 - r 6354"
                        action = "sell"
                        
                        
                        

                    # -------------------------------------------------- PARACADUTE crollo SE SI RIDUCE LA DISTANZA TRA ma 100 E ma 200 quindi sta risalendo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.45
                        and ma2_last < ma2_2_min_ago
                        
                        
                        
                        and delta_1 < delta_2
                        and ma100_last > ma100_60_min_ago
                    ):
                        sell = "SELL 1 PARACADUTE CROLLO distanza< ma100-ma200 (5-12 min) Ema50< E ma3<ma16 and deviation_sell< -0.35 - GIORNO- r 6373"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE ma sta risalendo
                        # and delta_1 < 0.25
                        # and delta_2 > 0.40
                        
                        
                      
                    
                    
                    
                    
                    
                    # --------------------------------------------------- PARACADUTE crollo SE AUMENTA LA DISTANZA TRA ma 100 E ma 200 quindi grande ribasso INFERI
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.35
                        and ma2_last < ma2_2_min_ago
                        and ma300_last > ma300_120_min_ago
                       
                        
                        and delta_1 > delta_2
                        and ma100_last < ma100_60_min_ago
                    ):
                        sell = "SELL 1 PARACADUTE CROLLO 300 > distanza> ma100-ma200 (5-12 min) e ma50< and ma3 < ma16 and dev_sell < -0.35  - NOTTE - r 6400"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE ma sta continuando a scendere
                        
                        
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.47
                        and ma2_last < ma2_2_min_ago
                        
                        and ma300_last < ma300_120_min_ago
                       
                        
                        and delta_1 > delta_2
                        and ma100_last < ma100_60_min_ago
                    ):
                        sell = "SELL 1 PARACADUTE CROLLO 300 < distanza> ma100-ma200 (5-12 min) e ma50< and ma3 < ma16 and dev_sell < -0.47  - NOTTE - r 6421"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE ma sta continuando a scendere
                        
                        
                        
                        
                        
                 
                
                
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
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-72 and deviation sell -0.65 e vaffanculo ! - r 6448"
                        action = "sell"
                         
                        # and deviation_ma39 < -0.29 vendeva troppo presto
                        # ATTENZIONE "and (ma3_prev > ma39_prev and ma3_last < ma39_last)" con ma39 NON HA INCROCIATO
                        # and deviation_sell < -0.30
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                      
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma100_prev and ma3_last < ma100_last)
                        and deviation_sell < -0.39
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.39 - r 6467"
                        action = "sell"
                        
                        # viva sant' antonio !
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.27 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 1 (12-21 min) con ma50> and 5 < 25 and deviation_sell 0.27-0.56 - FINTA ALLA MARADONA - r 6482"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last > ma300_last
                        
                        and ma3_last < ma22_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 1 (12-21 min) con ma50> and 3 < 22 con 3 sopra 300 (NO INCROCIO 3-13) and dev_sell 0.57-0.90 - DOPPIO PASSO RONALDO - r 6497 a"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma300_last
                        
                        and ma3_last < ma13_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 1 (12-21 min) con ma50> and 3<13 con 3 soto 300 (NO INCROCIO 3-13) and dev_sell 0.57-0.90 - DOPPIO PASSO RONALDO - r 6497 b"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 ( DOPPIA FINTA ALLA RONALDO ) - r 6512"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.21 and deviation_sell < 1.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-30 and deviation_sell 1.21-1.70 ( IL TACCO DI ALLAH ) - r 6527"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 1.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-15 and deviation_sell > 1.71 ( SI STA TRA GLI ANGELI, compa ! ) - r 6539"
                        action = "sell"
                        
                        
                      
                    
                    ##########################################################################################
                    
                    # NON TOCCARE ! CUSCINO DI SANT' ANTONIO !
                    # L' INCROCIO 5-100 MI SALVA ! MA 5<100 VENDE DURANTE IL RIBASSO !
                    
                    
                    ##################################################################### con trend discendente
                    
                    
                    # RAFFORZATO DA 100>300
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last > ma300_last
                        
                        and deviation_ma39 < -0.16
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (12-21 min) RAFFORZATO con ma50 < and deviation_ma39 < -0.16 and deviation_sell < -0.36 - r 6564"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last < ma300_last
                        and deviation_ma39 < -0.159
                        and deviation_sell < -0.34
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 < and deviation_ma39 < -0.159 and deviation_sell < -0.34 - r 6577"
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
                        sell = "SELL 1 (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - r 6602"
                        action = "sell"
                        
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50 < !
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - r 6616"
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
                        sell = "SELL 1 PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 6632"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                   
                
                
                    # -------------------------------------------- guadagno con crollo ! fondamentale per uscire, EVENTUALMENTE, con guadagno DURANTE IL CROLLO !
                    
                    # INTANTO TE LI PRENDI E TE LI PORTI A CASA ! 
                    # E' UNA SPECIE DI POCHI MALEDETTI E SUBITO.
                   
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.80
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3-28 and deviation_sell 0.25-0.80 - r 6653"
                        action = "sell"
                        
                        # 15 giu 2022 3-28 da 3-16
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 0.81
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3-11 and deviation_sell > 0.81 - r 6670"
                        action = "sell"
                        
                   
                
                    # ----------------------------------------------------------------------------- torna a casa durante il crollo con minor danno 
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma36_prev and ma3_last < ma36_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 torna a casa durante il crollo con minor danno  (12-21 min) con ma50 < and incrocio 3-36 and deviation_sell < -0.25 - r 6683"
                        action = "sell"
                        
                        # 1 giugno 2022 -0.27 da 0.25
                        
                
                
                
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
                        sell = "SELL 1 (21-50 min) con ma50> and incrocio 3-78 and deviation_sell<-0.65 - r 6705"
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
                        sell = "SELL 1 (21-50 min) con ma50> and deviation_sell <-0.32 and ma3_last < ma50_last - r 6724"
                        action = "sell"
                        
                        # VENDITA 1 IN ALTO dopo BUY IN RISALITA
                        # and deviation_ma39 < -0.16 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        # and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        # and deviation_sell < -0.26
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.29
                        and ma300_last > ma300_120_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.29 - r 6745"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.26
                        and ma300_last < ma300_120_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.26 - r 6761"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    ######################################################################################### doppio delta > 1 TREND CONTINUA AL RIALZO vendi cosi'
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        
                        
                        and delta_1 < delta_2
                        and ma100_last > ma100_60_min_ago
                        
                        and ma5_last < ma39_last
                        and deviation_sell > 0.34 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and 5-39 and deviation_sell 0.34 - 0.56 la prima FINTA ALLA MARADONA  - GIORNO - r 6789"
                        action = "sell"
                        
                        # 31 maggio 2022 5-39 da 5-20
                        
                        
                        
                        
                    ###################################################################### doppio delta < 1 TREND COMINCIA A SCENDERE ! vendi con ma50 !
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        
                        
                        and delta_1 > delta_2
                        and ma100_last > ma100_60_min_ago
                        
                        and deviation_ma100_sopra_ma200 > -0.10
                        and ma3_last < ma50_last
                        and deviation_sell > 0.34 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and 3-50 and deviation_sell 0.34-0.56 FINTA ALLA MARADONA - - CREPUSCOLO - r 6812"
                        action = "sell"
                        
                        # 100 deve stare sopra 200 cosi' non vende con ma 50 durante il crollo o un forte ribasso !
                        
                        ###########################################################################################################
                        
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    ############################################################################## doppio delta > 1 TREND CONTINUA AL RIALZO vendi cosi'
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last > ma300_last
                        
                        and delta_1 < delta_2
                        and ma100_last > ma100_60_min_ago
                        
                        and ma5_last < ma33_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and 5-33 and deviation_sell 0.51 - 0.90 ELASTICO ALLA RONALDO E 100 > 300 - GIORNO - r 6847a"
                        action = "sell"
                        
                        # dopo 26 minuti non c'e' piu' quello scatto in avanti - dribbling- che si verifica nei primi minuti
                        # deviation_sell = ma3_last/last_trade_price
                        # 5-22 (era 4-15)
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma300_last
                        
                        and delta_1 < delta_2
                        and ma100_last > ma100_60_min_ago
                        
                        and ma5_last < ma22_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and 5-22 and deviation_sell 0.51 - 0.90 ELASTICO ALLA RONALDO MA 100 < 300- GIORNO - r 6847b"
                        action = "sell"
                        
                        # dopo 26 minuti non c'e' piu' quello scatto in avanti - dribbling- che si verifica nei primi minuti
                        # deviation_sell = ma3_last/last_trade_price
                        # 5-22 (era 4-15)
                        
                        
                        
                        
                        
                        
                        
                    ########################################################################## doppio delta < 1 TREND COMINCIA A SCENDERE ! vendi con ma50 !
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        
                        
                        and delta_1 > delta_2
                        and ma100_last > ma100_60_min_ago
                        
                        and deviation_ma100_sopra_ma200 > -0.10
                        and ma3_last < ma50_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and 3-50 and deviation_sell 0.51-0.90 ELASTICO ALLA RONALDO - CREPUSCOLO - r 6871"
                        action = "sell"
                        
                        # dopo 26 minuti non c'e' piu' quello scatto in avanti - dribbling- che si verifica nei primi minuti
                        # deviation_sell = ma3_last/last_trade_price
                        # 100 deve stare sopra 200 per non vendere con ma50 durante il crollo o un forte ribasso
                        
                        
                        
                        
                        
                        
                 
                    #######################################################################################################
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last > ma300_last
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and incrocio 3-25 se 3 sopra 300 and deviation_sell 0.91 - 1.20 (DOPPIA FINTA DI RONALDO) - r 6893 A"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma300_last
                        and (ma3_prev > ma42_prev and ma3_last < ma42_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and incrocio 3-42 se 3 sotto 300 and deviation_sell 0.91 - 1.20 (DOPPIA FINTA DI RONALDO) - r 6893 B"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma4_prev > ma28_prev and ma4_last < ma28_last)
                        and deviation_sell > 1.21 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and incrocio 4-28 and deviation_sell 1.21 - 2.70 (DOPPIO PASSO DI RONALDO)- r 6908"
                        action = "sell"
                        
                  
               
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma9_prev and ma3_last < ma9_last)
                        and deviation_sell > 2.71 and deviation_sell < 5.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and incrocio 3-9 and deviation_sell 2.71 - 5.70 (TACCO DI ALLAH) - r 6920"
                        action = "sell"
                        
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell > 5.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and incrocio 3-39 and deviation_sell > 2.71 (SI STA TRA GLI ANGELI, comba !) - r 6932"
                        action = "sell"
                        
                    
                    
                    ############################################################################## CUSCINO DI SANT' ANTONIO per questo segmento di tempo !
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last > ma200_last
                        
                        and ma100_last > ma100_60_min_ago
                        and ma5_last < ma100_last
                        and deviation_sell < -0.26
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and 5-100 and deviation_sell < -0.26 CUSCINO DI SANT' ANTONIO se ma100 > E 100 > 200- r 6947 A"
                        action = "sell"
                        
                        # 19 giu 2022 dev sell a 0.26 da 0.24
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma200_last
                        
                        and ma100_last > ma100_60_min_ago
                        and ma5_last < ma100_last
                        and deviation_sell < -0.24
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and 5-100 and deviation_sell < -0.24 CUSCINO DI SANT' ANTONIO se ma100 > MA 100 < 200 - r 6947 B"
                        action = "sell"
                        
                        
                        
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and ma300_last > ma300_120_min_ago
                        
                        and ma5_last < ma100_last
                        and deviation_sell < -0.25
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and 5-100 and deviation_sell < -0.25 CUSCINO DELLA MADONNA se ma100 < MA 300 >- r 6962"
                        action = "sell"
                        
                        
                    
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and ma300_last < ma300_120_min_ago
                        
                        and ma200_last > ma200_60_min_ago
                        
                        
                        and ma5_last < ma100_last
                        and deviation_sell < -0.26
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50> and 5-100 and dev_sell< -0.26 se ma100< CUSCINO DELLA MADONNA  E DE SANTO RENATO 300 < MA 200> - r 6984"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and ma300_last < ma300_120_min_ago
                        
                        and ma200_last < ma200_60_min_ago
                        
                        and ma5_last < ma100_last
                        and deviation_sell < -0.25
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50> and 5-100 and dev_sell< -0.25 se ma100< CUSCINO DELLA MADONNA E DE SANTO RENATO 300 < CON 200< - r 7002"
                        action = "sell"
                        
                        
               
                    ################################################################################################ con trend discendente 
                    ################################################################################################ con ma100 DISTANTE sopra dalla ma300
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.16
                        and deviation_sell < -0.29
                        and ma2_last < ma2_2_min_ago
                        
                        and deviation_ma100_sopra_ma300 > 0.69
                    ):   
                        sell = "SELL 1 (21-50 min) con ma50 < con deviation_ma39 <-0.16 and dev_sell< -0.29 TREND CRESCITA (100 sopra 300 > 0.69) - r 7017"
                        action = "sell"
                        
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
                        sell = "SELL 1 (21-50 min)con ma50 < CUSCINO SANT' ANTONIO (5-100) MA SOLO con TREND CRESCITA (100 sopra 300 > 0.69) - r 7036"
                        action = "sell"
                        
                        
                  
                    
                    # TREND LATERALE (100/300  <0.69 and >-0.77)
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        
                        and deviation_correzione_2 < -0.20
                        and deviation < -0.27
                        
                        and ma2_last < ma2_2_min_ago
                        
                        and deviation_ma100_sopra_ma300 < 0.69
                        and deviation_ma100_sopra_ma300 > -0.77
                    
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 < e dev_ma39 < -0.20 e deviation_sell < -0.27 TREND LATERALE (100>300 <0.69 and > -0.77) - r 7056"
                        action = "sell"
                        
                        # HO AVUTO UN PROBLEMA GRANDE ! ha venduto con -0.14 ma io avevo -0.20 e -0.27 !!! ore 15:30 25 mag 2022
                        # DEVIATION 3-39 DIVENTA 4-39 (deviation_correzione_2)
                        # DEVIATION SELL DIVENTA 5-last trade price (deviation)
                        
                        # non mi arrendo !
                    
                    
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
                        sell = "SELL 1 maestro parte 1 (21-50 min) con ma50 < and deviation_ma39 < -0.27 - r 7087"
                        action = "sell"
                        
                        
                        
                    
                    
                    
                    # RAFFORZATIVO CON 300 > 300 120 AGO (TREND RIALZO) OPPURE CON 300< 300 120 min ago (CROLLO)
                    
                    # SELL 1 maestro parte 2 (21-50 min) con ma50 < and deviation_sell < -0.33
                    
                    
                    elif (        
                        ma50_last < ma50_2_min_ago
                        and ma300_last > ma300_120_min_ago
                        and ma300_last > ma300_20_min_ago
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.36
                        and deviation_ma50_sotto_ma300 < 0.50
                    ):
                        sell = "SELL 1 maestro parte 2 300>120 e 300>20 (21-50 min) con ma50 < and deviation_sell < -0.36 - r 7109"
                        action = "sell"
                        
                        
                        
                        
                    elif (        
                        ma50_last < ma50_2_min_ago
                        and ma300_last > ma300_120_min_ago
                        and ma300_last < ma300_20_min_ago
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.33
                        and deviation_ma50_sotto_ma300 < 0.50
                    ):
                        sell = "SELL 1 maestro parte 2 300>120 e 300>20 (21-50 min) con ma50 < and deviation_sell < -0.33 - r 7124"
                        action = "sell"
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    # ECCO inequivocabilmente il crollo !    
                    
                    elif (        
                        ma50_last < ma50_2_min_ago
                        and ma300_last < ma300_120_min_ago
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.36
                        and deviation_ma50_sotto_ma300 < 0.50
                    ):
                        sell = "SELL 1 maestro parte 2 (21-50 min) con ma50 < and deviation_sell < -0.36 - r 7147"
                        action = "sell"
                        
                        # da 0.33 a 0.36 perche' durante il crollo ferrari non devi guardare i centesimi.
                        
                        
                        
                        
                
                 
                    
                    
                    #####################################################################################
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.37
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - r 7167"
                        action = "sell"
                        
                    
                    
                    
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last > ma100_60_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.31
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 < e 100> and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO and deviation_sell < -0.31 - r 7183"
                        action = "sell"
                        
                        
                        
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and ma100_last > ma100_30_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.29
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 < e 100< and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO and dev_sell < -0.30 - r 7196 A"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and ma100_last < ma100_30_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.29
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 < e 100< and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO and dev_sell < -0.29 - r 7196 B"
                        action = "sell"
                        
                        
                        
                        
                        
               
                    
                
                    ############################################################# con ma50 discendente MA ma200 ET ma200>ma300 - PERDITA TOLLERATA AUMENTA
                
                    # ho diviso il maestro in 2 !
                    
                    
                    elif (
                        
                        ma50_last < ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 > 0.60
                   
                        and deviation_ma39 < -0.28
                        
                        and ma2_last < ma2_2_min_ago
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 compa (21-50 min) con ma50 < and deviation_ma39 < -0.28 con > PERDITA TOLLERATA 100>300 DI MOLTO - r 4261 A"
                        action = "sell"
                        
                        # and deviation_ma39 < -0.15 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        
                        # ERRORE GRAVE CORRETTO DAL MAESTRO - VENDEVA MENTRE SALIVA !
                        # ma50_last < ma50_2_min_ago
                        # and ma2_last < ma2_2_min_ago
                        # and deviation_ma39 < -0.25
                        # or deviation_sell < -0.26
                        
                        
                    elif (
                        
                        ma50_last < ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 < 0.60
                    
                        and deviation_ma39 < -0.28
                        and deviation_sell < -0.25
                        
                        and ma2_last < ma2_2_min_ago
                        
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 < and dev_ma39 < -0.28 AND DEV SELL<-0.25 con > PERDITA TOLLERATA 100 SOPRA 300 NON DI MOLTO - r 4261 B"
                        action = "sell"
                        
                        # and deviation_ma39 < -0.15 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        
                        # ERRORE GRAVE CORRETTO DAL MAESTRO - VENDEVA MENTRE SALIVA !
                        # ma50_last < ma50_2_min_ago
                        # and ma2_last < ma2_2_min_ago
                        # and deviation_ma39 < -0.25
                        # or deviation_sell < -0.26
                        
                        
                        
                        
                    # rafforzativo alla perdita tollerata
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma200_120_min_ago
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.31
                        and deviation_trend_ma200 > -0.03
                        and ma200_last > ma300_last
                        
                        
                    ):
                        sell = "SELL 1 compa (21-50 min) con ma50 < and deviation_sell < -0.31 con > PERDITA TOLLERATA RAFFORZATA (200> 120 min)  - r 4284"
                        action = "sell"
                        
                        
                        
                        
                    # rafforzativo alla perdita tollerata
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_120_min_ago
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.28
                        and deviation_trend_ma200 > -0.03
                        and ma200_last > ma300_last
                        
                        
                    ):
                        sell = "SELL 1 compa (21-50 min) con ma50 < and deviation_sell < -0.28 con > PERDITA TOLLERATA - r 4285"
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
                        sell = "SELL 1 (21-50 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.40 - CON PERDITA TOLLERATA > - r 4307"
                        action = "sell"
                        
                        
                        

                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        
                        and ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 < and INCROCIO 3-100 -0.30 CUSCINO DI SANT' ANTONIO - CON PERDITA TOLLERATA > - r 4322"
                        action = "sell"
                        
                  
                    
                    
                    # -------------------------------------------------------------------------------------- guadagno durante il crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell > 0.30 
                        and deviation_sell < 0.54
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 eventuale guadagno durante il crollo (21-50 min) con ma50 < incrocio 3 - 28 and deviation_sell 0.30 - 0.54 - r 4338"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 0.55
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 eventuale guadagno durante il crollo (21-50 min) con ma50 < incrocio 3 - 11 and deviation_sell > 0.55 - r 4349"
                        action = "sell"
                        
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell < -0.24
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 piccola perdita durante il crollo (21-50 min) con ma50 < incrocio 3 - 18 and deviation_sell < -0.24 - r 4361"
                        action = "sell"
                        
                        
              
            
            
                #############################################################################################################  SESSIONE 1 ( da 50 a 90 min )

                # VENDITA - da 50 a 90 min - da 3001 a 5400 secondi in poi
                
                elif (
                    seconds_since_last_trade > 3001 and seconds_since_last_trade <= 5400
                ):
                    
                    if (    
                        ma50_last > ma50_2_min_ago
                        and ma100_last > ma200_last
                        and deviation_ma39 < -0.22
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > and deviation_ma39 <-0.22 and deviation_sell < -0.23 - r 4381"
                        action = "sell"
                        
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        
                        
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and ma100_last > ma100_60_min_ago
                        and ma100_last < ma200_last
                        and deviation_ma39 < -0.22
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > and deviation_ma39 < -0.22 - r 4382 a"
                        action = "sell"
                        
                        # se 100 cresce da 60 min il sistema e' piu' rilassato e non ha fretta di portare a casa un guadagno minimo
                        
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and ma100_last < ma200_last
                        and deviation_ma39 < -0.22
                        and deviation_sell < 0.23
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > and deviation_ma39 < -0.22 - r 4382 b"
                        action = "sell"
                        
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # potrebbe essere situazione di crollo che vende con ma39 e senza deviation sell !
                        # cioe' in una situazione di crollo si porta a casa lo 0.23
                        
                        
                        
                        
                        
                        
                     
                    
                    
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and deviation_sell < -0.23
                        and ma3_last < ma50_last
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > and deviation_sell < -0.23 and ma3_last < ma50_last  - r 4396"
                        action = "sell"
                        
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        
                   
                    
                    
                    # la prima FINTA ALLA MARADONA RAFFORZATO DA 100>150
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last > ma150_last
                        and (ma5_prev > ma54_prev and ma5_last < ma54_last)
                        and deviation_sell > 0.32 and deviation_sell < 0.52
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > and incrocio 5-54 and deviation_sell 0.31-0.52 la prima FINTA ALLA MARADONA RAFFORZATO - r 4410"
                        action = "sell"
                        
                        # MARADONA RAFFORZATO accompagna nelle prime fasi di crescita. poi interviene RONALDO se il rialzo comincia a farsi piu' consistente.
                        
                        
                    # la prima FINTA ALLA MARADONA
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma150_last
                        and (ma5_prev > ma52_prev and ma5_last < ma52_last)
                        and deviation_sell > 0.32 and deviation_sell < 0.52
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > and incrocio 5-52 and deviation_sell 0.31-0.52 la prima FINTA ALLA MARADONA - r 4411"
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
                        sell = "SELL 1 da 50 a 90 min con ma50> and incrocio 4-20 and deviation_sell 0.51-0.90 RONALDO - r 4426"
                        action = "sell"
                        
                        
                    
                    
                    ############################################################################ ronaldo 60-90 min dal buy se ma200 < non perdona
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma200_last < ma200_120_min_ago
                        and (ma4_prev > ma39_prev and ma4_last < ma39_last)
                        and deviation_sell > 0.53 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50> and incrocio 4-39 and deviation_sell 0.51-0.90 RONALDO - r 4441"
                        action = "sell"
                        
                        
                        
                    ##################################################################################################################
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > and incrocio 3-30 and deviation_sell 0.91 - 1.49 RABONA DI RONALDO - r 4455"
                        action = "sell"
                  
                        # ma ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                    
                        
                        
                    # SELL 1 da 50 a 90 min DOPPIO PASSO ALLA RONALDO 1 (se 50-200 > 0.30 stai un po' piu' tranquillo)
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma50_sotto_ma200 > 0.30
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > incrocio 3-33 and deviation_sell > 1.50 DOPPIO PASSO ALLA RONALDO se 50-200 > 0.30 - r 4468"
                        action = "sell"
                        
                        # deviation_ma50_sotto_ma200 = 50/200 quindi non farti ingannare dalla parola sotto.
                        # 31 maggio 2022 3-39 da 3-33
                        
                        
                    # SELL 1 da 50 a 90 min DOPPIO PASSO ALLA RONALDO 2 se 50-200 < 0.30 
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma50_sotto_ma200 < 0.30
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > incrocio 3-33 and deviation_sell > 1.50 DOPPIO PASSO ALLA RONALDO se 50-200 < 0.30 - r 4469"
                        action = "sell"
                        
                        
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 > 0.50
                        and (ma3_prev > ma42_prev and ma3_last < ma42_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 da 50 a 90 min con ma50 > incrocio 3-11 and deviation_sell > 2.71 TACCO DI ALLAH - r 4482a"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 < 0.50
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 da 50 a 90 min con ma50 > incrocio 3-13 and deviation_sell > 2.71 TACCO DI ALLAH - r 4482b"
                        action = "sell"
                        
                        
                        
                        
                        
                        
                        
                  
                    ######################################################################################## con trend discendente ma50 <
                    
                    ############################################################## ipotesi peggiore e sono cazzi ! and doppio delta ( sempre con ma50 < )
                    
                    # SELL 1 50-90 min IPOTESI PEGGIORE con ma50< con deviation_ma39 <-0.205 and deviation_sell < -0.205 and DOPPIO DELTA INFERI
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma300_last
                        and deviation_trend_ma200 < -0.10
                        
                        and deviation_ma39 < -0.19
                        and deviation_sell < -0.22
                        
                        
                        and delta_1 > delta_2
                        and ma100_last < ma100_60_min_ago
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 50-90 min IPOTESI PEGGIORE con ma50 < con deviation_ma39 <-0.19 and dev sell < -0.22 SOTTO RIBASSO RIBASSO - NOTTE - r 4505"
                        action = "sell"
                        
                        # 6 giu 2022 deviation sell a -0.22 da -0.195
                        
                        
                        
                    # SELL 1 50-90 min IPOTESI PEGGIORE MA DOPPIO DELTA RISALITA con ma50< con deviation_ma39 <-0.205 and deviation_sell < -0.205
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma300_last
                        and deviation_trend_ma200 < -0.10
                        
                        and deviation_ma39 < -0.215
                        and deviation_sell < -0.30
                        
                        
                        and delta_1 < delta_2
                        and ma100_last > ma100_60_min_ago
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 50-90 min con ma50< e dev ma39 < -0.215 e dev sell <-0.30 SOTTO RIALZO RIALZO - GIORNO ! - r 4525"
                        action = "sell"
                        
                        # IPOTESI PEGGIORE MA GIORNO !
                        
                        
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma300_last
                        and deviation_trend_ma200 < -0.10
                        
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.15
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 50 a 90 min IPOTESI PEGGIORE con ma50 < con incrocio 3-78 and deviation_sell < -0.15 - r 4542"
                        action = "sell"
                        
                        
               
                    ############################################################### ipotesi mediana 1 RAFFORZATA un po' meno peggio ( sempre con ma50 < )
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last > ma300_last
                        
                        and ma200_last < ma300_last
                        and deviation_trend_ma200 > -0.10
                        
                        
                        and deviation_ma39 < -0.20
                        and ma2_last < ma2_2_min_ago
                        and deviation_sell < -0.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 50-90 min IPOTESI mediana 1 RAFFORZATA un po' MENO PEGGIO con ma50< E deviation_ma39 <-0.20 E deviation_sell < -0.21- r 4560"
                        action = "sell"
                        
                        
                        
                        
                    ############################################################### ipotesi mediana 1 un po' meno peggio ( sempre con ma50 < )
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last < ma300_last
                        and ma100_last > ma100_60_min_ago
                        
                        and ma200_last < ma300_last
                        and deviation_trend_ma200 > -0.10
                        
                        
                        and deviation_ma39 < -0.19
                        and deviation_sell < -0.22
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 50 a 90 min IPOTESI un po' MENO PEGGIO con ma50 < con dev_ma39 < -0.19 MA 100> and dev_sell < -0.22 - r 4561"
                        action = "sell"
                        
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last < ma300_last
                        and ma100_last < ma100_60_min_ago
                        
                        and ma200_last < ma300_last
                        and deviation_trend_ma200 > -0.10
                        
                        
                        and deviation_ma39 < -0.19
                        and deviation_sell < -0.21
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 50 a 90 min IPOTESI un po' MENO PEGGIO con ma50 < con deviation_ma39 <-0.19 E 100< and dev_sell < -0.21 - r 4562"
                        action = "sell"
                        
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma300_last
                        and deviation_trend_ma200 > -0.10
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.15
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 50 a 90 min IPOTESI un po' MENO PEGGIO con ma50 < con incrocio 3-78 and deviation_sell < -0.15 - r 4575"
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
                        sell = "SELL 1 da 50 a 90 min UN PO' MEGLIO con ma50 < con deviation_ma39 <-0.22 and deviation_sell < -0.23 - r 4592"
                        action = "sell"
                        
                        
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma300_last
                        and deviation_trend_ma200 < -0.10
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.17
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 50 a 90 min UN PO' MEGLIO con ma50 < con incrocio 3-78 and deviation_sell < -0.17 - r 4607"
                        action = "sell"    
                    
                
                    ##################################################### sempre con ma50 discendente MA trend ma200> ET ma200 > ma300 - PERDITA TOLLERATA AUMENTA
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma300_last
                        and deviation_trend_ma200 > -0.10
                        
                        and ma78_last > ma200_last
                        
                        and deviation_ma39 < -0.23
                        and deviation_sell < -0.30
                        
                        and ma2_last <= ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 50-90 min BEST ma sempre con ma50< E 78 > 200 con dev_ma39 <-0.23 and dev_sell <-0.30 - CON PERDITA TOLLERATA > - r 4624 A"
                        action = "sell"
                        
                        # ha fatto perdita dell' 1% - forse succede tutto in quei 2 minuti se crolla improvvisamente
                        # con deviation_ma39 < -0.27
                        # con deviation_sell < -0.28
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma300_last
                        and deviation_trend_ma200 > -0.10
                        
                        and ma78_last < ma200_last
                        
                        and deviation_ma39 < -0.23
                        and deviation_sell < -0.295
                        
                        and ma2_last <= ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 50-90 min BEST ma sempre con ma50< MA 78 < 200 con dev_ma39 <-0.23 and dev_sell <-0.295 - CON PERDITA TOLLERATA > - r 4624 B"
                        action = "sell"
                        
                        # ha fatto perdita dell' 1% - forse succede tutto in quei 2 minuti se crolla improvvisamente
                        # con deviation_ma39 < -0.27
                        # con deviation_sell < -0.28
                        
                        
                    
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last > ma200_last
                        
                        and ma200_last > ma300_last
                        and deviation_trend_ma200 > -0.10
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.29
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 RAFFORZATA da 50-90 min BEST ma sempre con ma50 < con incrocio 3-78 and deviation_sell < -0.29 - PERDITA TOLLERATA > - r 4642"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last < ma200_last
                        
                        and ma200_last > ma300_last
                        and deviation_trend_ma200 > -0.10
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.25
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 50-90 min BEST ma sempre con ma50 < con incrocio 3-78 and deviation_sell < -0.25 - CON PERDITA TOLLERATA > - r 4643"
                        action = "sell"
                        
                        
                        
                        
                        
                    # AGGIUNTA TARDIVA MA FORSE NECESSARIA !
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        
                        and ma100_last < ma200_last
                        and ma200_last < ma300_last
                        
                        and ma200_last < ma200_120_min_ago
                        and ma300_last < ma300_120_min_ago
                   
                        and deviation_sell < -0.17
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 50-90 min AGGIUNTA TARDIVA MA FORSE NECESSARIA ! - r 4644"
                        action = "sell"
                        
                        
                        
                        
                
                
                
                ########################################################################################################
                ########################################################################################################
                ######################################################################################################## SESSIONE 1 ( da 90 min a 110 min )

                # VENDITA - da 90 minuti a 110 minuti  = da 5400 secondi a 6600 secondi

                
                elif seconds_since_last_trade > 5400 and seconds_since_last_trade <= 6600:
                    
                    
                    if (    
                        ma50_last > ma50_2_min_ago
                        and ma100_last > ma200_last
                        and deviation_ma39 < -0.22 
                        and deviation_sell < -0.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 90-110 min con ma50 > and deviation_ma39 <-0.22 and deviation_sell < -0.21 - r 4662"
                        action = "sell"
                        
                        
                        
                    if (    
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma200_last
                        and deviation_ma39 < -0.22 
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 90-110 min con ma50 > and deviation_ma39 <-0.22 - r 4663"
                        action = "sell"
                        
                        # potrebbe essere una situazione di crollo con 39 senza deviation sell !
                        
                        
                        
                        
                        
                       
                    elif (     
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma50_last 
                        and deviation_sell < -0.22
                        and ma25_last < ma25_2_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 90-110 min con ma50 > and ma3_last < ma50_last and deviation_sell < -0.22 and ma25 < - r 4675"
                        action = "sell"
                        
                    
                    
                    ################################################################################### fare maradona 1 ma3>ma100 (69) e maradona 2 ma3<ma100 (50)
                    
                    # MARADONA 1a
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma200_last > ma300_last
                        and ma3_last > ma100_last
                        and ma5_last < ma69_last
                        and deviation_sell > 0.35 and deviation_sell < 0.64
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1a 90-110 min con ma50 > con 5-69 (!) and deviation_sell 0.35 - 0.64 la prima FINTA DI MARADONA 1 (non toccare) - r 4692"
                        action = "sell"
                        
                    
                    
                    
                    
                    
                    # MARADONA 1b FASE LATERALE
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma200_last < ma300_last
                        and deviation_ma200_sotto_ma300 > -0.30
                        
                        and ma3_last > ma100_last
                        and ma5_last < ma78_last
                        and deviation_sell > 0.35 and deviation_sell < 0.64
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1b FASE LATERALE 90-110 min con ma50 > con 5-78 (!) and deviation_sell 0.35 - 0.64 la prima FINTA DI MARADONA 1 - r 4693"
                        action = "sell"
                        
                        
                        
                    # MARADONA 1b FASE RIBASSO
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma200_last < ma300_last
                        and deviation_ma200_sotto_ma300 < -0.30
                        
                        and ma3_last > ma100_last
                        and ma5_last < ma69_last
                        and deviation_sell > 0.35 and deviation_sell < 0.64
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1b FASE RIBASSO 90-110 min con ma50 > con 5-69 (!) and deviation_sell 0.35 - 0.64 la prima FINTA DI MARADONA 1 - r 4694"
                        action = "sell"
                        
                        
                    
                    
                    
                    
                    
                    
                    # MARADONA 2
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma100_last
                        and ma5_last < ma50_last
                        and deviation_sell > 0.35 and deviation_sell < 0.64
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 90-110 min con ma50 > con 5-50 (!) and deviation_sell 0.35 - 0.64 la prima FINTA DI MARADONA 1 - r 4707"
                        action = "sell"
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma42_prev and ma5_last < ma42_last)
                        and deviation_sell > 0.65 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 90-110 min con ma50 > incrocio 5-42 (!) and deviation_sell 0.65 - 1.49 RABONA ALLA RONALDO - r 4720"
                        action = "sell"
                        
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 90-110 min con ma50 > incrocio 3-30 and deviation_sell  1.50 - 2.70 DOPPIO PASSO DI RONALDO - r 4732"
                        action = "sell"
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 2.71 and deviation_sell < 5.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 90-110 min con ma50 > incrocio 3-13 (!) and deviation_sell > 2.71 TACCO DI ALLAH - r 4745"
                        action = "sell"
                        
                        
                        
                
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma69_prev and ma3_last < ma69_last)
                        and deviation_sell > 5.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 90-110 min con ma50 > incrocio 3-69 (!) and deviation_sell > 5.71 SI STA TRA GLI ANGELI, compa ! - r 4758"
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
                        sell = "SELL 1 90-110 min con ma50 <  and ma100 < con deviation_ma39 <-0.17 - r 4776"
                        action = "sell"
                        
                        # ma39 non deve vendere laterale quindi per farlo vendere in alto ho dato 0.20
                        
                        
                        
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                        and deviation_sell < -0.19
                        and ma3_last < ma39_last
                        and ma100_last < ma100_60_min_ago
                        and ma300_last > ma300_120_min_ago
                    ):
                        sell = "SELL 1 90-110 min con ma50 < and ma100 < and (deviation_sell < -0.15 and ma3_last < ma39_last) MA 300>120min ago - r 4789"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                        and deviation_sell < -0.145
                        and ma3_last < ma39_last
                        and ma100_last < ma100_60_min_ago
                        and ma300_last < ma300_120_min_ago
                    ):
                        sell = "SELL 1 90-110 min con ma50 < and ma100 < and (deviation_sell < -0.145 and ma3_last < ma39_last) 300 < 120 min ago - r 4790"
                        action = "sell"
                        
                        # 27 giu 2022 dev sell 0.145 da 0.15
                        
                        
                        
                        
                        
                        
                        
                    
                    
                    # ma se ma100 >
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.20
                        and deviation_sell > 0.20
                        and ma5_last < ma5_2_min_ago
                        and ma100_last > ma100_60_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 90-110 min con ma50 < MA ma100 > con deviation_ma39 <-0.20 - r 4806"
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
                        sell = "SELL 1 90-110 min con ma50 < MA ma100 > and (deviation_sell < -0.20 and ma3_last < ma39_last) - r 4824"
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
                        sell = "SELL 1 compa 90-110 min con ma50 < and deviation_ma39 < -0.23  con > PERDITA TOLLERATA - r 4840"
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
                        sell = "SELL 1 compa 90-110 min con ma50 < (deviation_sell < -0.21 and ma3_last < ma39_last) con > PERDITA TOLLERATA - r 4854"
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
                        sell = "SELL 1 dopo 110 min con ma50 > and deviation_ma39 <-0.22 and deviation_sell < -0.21 - r 4873"
                        action = "sell"
                        
                        
                    
                    
                    elif (     
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma50_last 
                        and deviation_sell < -0.22
                        and ma25_last < ma25_2_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 > and ma3_last < ma50_last and deviation_sell < -0.22 and ma25 < - r 4886"
                        action = "sell"
                        
                    
                    
                    
                    ############################################################################# fare maradona 1 e maradona 2
                    
                    # MARADONA 1
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last > ma100_last
                        and ma5_last < ma78_last
                        and deviation_sell > 0.35 and deviation_sell < 0.64
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 > con 5-78 (!) and deviation_sell 0.35 - 0.64 la prima FINTA DI MARADONA 1 (non toccare) - r 4904"
                        action = "sell"
                        
                        # 10 GIU 2022 5-78 da 5-69
                        
                    # MARADONA 2
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma100_last
                        and deviation_ma100_sopra_ma300 > 0.30
                        and ma7_last < ma54_last
                        and deviation_sell > 0.35 and deviation_sell < 0.64
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 > con 7-54 (!) and dev_sell 0.35 - 0.64 la prima FINTA DI MARADONA 2 CON 100 sopra 300 > 0.30 - r 4919a"
                        action = "sell"
                        
                        # se 100 sopra 300 >0.30 stai calmo
                        
                        
                        
                        
                    # MARADONA 3
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma100_last
                        and deviation_ma100_sopra_ma300 < 0.30
                        and ma5_last < ma50_last
                        and deviation_sell > 0.35 and deviation_sell < 0.64
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 > con 5-50 (!) and dev_sell 0.35 - 0.64 la prima FINTA DI MARADONA 3 CON 100 sopra 300 < 0.30 - r 4919b"
                        action = "sell"
                        
                        
                    
                    
                    #################################################################################################
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma42_prev and ma5_last < ma42_last)
                        and deviation_sell > 0.65 and deviation_sell < 1.49
                        and deviation_ma100_sopra_ma200 > 0.45
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 > incrocio 5-42 (!) se 100-200 > 0.45 and deviation_sell 0.65 - 1.49 RABONA ALLA RONALDO - r 4934"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma34_prev and ma5_last < ma34_last)
                        and deviation_sell > 0.65 and deviation_sell < 1.49
                        and deviation_ma100_sopra_ma200 < 0.45
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 > incrocio 5-34 se 100-200 < 0.45 and deviation_sell 0.65 - 1.49 RABONA ALLA RONALDO - r 4935"
                        action = "sell"
                        
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 dopo 110 min con ma50 > incrocio 3-30 and deviation_sell  1.50 - 2.70 DOPPIO PASSO DI RONALDO - r 4946"
                        action = "sell"
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 2.71 and deviation_sell < 5.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 > incrocio 3-13 (!) and deviation_sell > 2.71 TACCO DI ALLAH - r 4959"
                        action = "sell"
                        
                
                
                
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma69_prev and ma3_last < ma69_last)
                        and deviation_sell > 5.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 dopo 110 min con ma50 > incrocio 3-69 (!) and deviation_sell > 5.71 SI STA TRA GLI ANGELI, compa ! - r 4972"
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
                        sell = "SELL 1 dopo 110 min con ma50 <  and ma100 < con deviation_ma39 <-0.17 - r 4989"
                        action = "sell"
                        
                        # ma39 non deve vendere laterale (!) quindi per farlo vendere in alto ho dato 0.20
                        
                        
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                        and deviation_sell < -0.15
                        and ma3_last < ma39_last
                        and ma100_last < ma100_60_min_ago
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 < and ma100 < and (deviation_sell < -0.15 and ma3_last < ma39_last) - r 5004"
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
                        sell = "SELL 1 dopo 110 min con ma50 < MA ma100 > con deviation_ma39 <-0.195 - r 5020"
                        action = "sell"
                        
                        # ma39 NON DEVE VENDERE in fase laterale ma in alto
                        
                        
                    
                    
                    # ma se ma100 > 
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                        and deviation_sell < -0.20
                        and ma3_last < ma39_last
                        and ma100_last > ma100_60_min_ago
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 < MA ma100 > and (deviation_sell < -0.20 and ma3_last < ma39_last) - r 5037"
                        action = "sell"
                        
                    
                   
                    ############################################################################### aumento della perdita tollerata ! 50< MA 200> e 200>300
                    
                    
                    
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                        and deviation_ma100_sopra_ma300 > 0.30
                        
                        and deviation_ma39 < -0.23
                        and deviation_trend_ma200 > -0.12
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 1 compa dopo 110 min con ma50 < and deviation_ma39 < -0.23  con > PERDITA TOLLERATA - r 5052"
                        action = "sell"
                        
                        
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                        and deviation_ma100_sopra_ma300 < 0.30
                        and deviation_sell < -0.21
                        
                        and deviation_ma39 < -0.23
                        and deviation_trend_ma200 > -0.12
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 1 compa dopo 110 min con ma50 < and deviation_ma39 < -0.23  and deviation_sell < -0.21 con > PERDITA TOLLERATA - r 5053"
                        action = "sell"
                        
                        # se 100 > 300 di poco metto anche deviation_sell < -0.21
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    
                    elif (     
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma39_last
                        and deviation_sell < -0.21
                        and ma2_last < ma2_2_min_ago
                        and deviation_trend_ma200 > -0.12
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 compa dopo 110 min con ma50 < (deviation_sell < -0.21 and ma3_last < ma39_last) con > PERDITA TOLLERATA - r 5067"
                        action = "sell"
                        
                        
                        
                        
                    # ATTENZIONE 1 ! > 110 min E CON 300 > 120 min FORSE E' NECESSARA SOLO QUESTA !
                    
                    elif (    
                        ma3_last < ma100_last
                        and ma300_last > ma300_120_min_ago
                        and ma100_last > ma200_last
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                    ):
                   
                        sell = "SELL 1 > 110 min FORSE E' NECESSARA SOLO QUESTA 1 ! deviation_sell < -0.27 - r 5081"
                        action = "sell"
                        
                        
                        
                    # ATTENZIONE 2 ! > 110 min E CON 300 > 120 min FORSE E' NECESSARA SOLO QUESTA !
                    
                    elif (    
                        ma3_last < ma100_last
                        and ma300_last > ma300_120_min_ago
                        and ma100_last < ma200_last
                        and deviation_sell < -0.22
                        and ma2_last < ma2_2_min_ago
                    ):
                   
                        sell = "SELL 1 > 110 min FORSE E' NECESSARA SOLO QUESTA 2 ! deviation_sell < -0.22 - r 5082"
                        action = "sell"
                        
                        
                        
                        
                        
                        
                    # ATTENZIONE 3 ! > 110 min E CON 300 < 120 min FORSE E' NECESSARA SOLO QUESTA !
                    
                    elif (    
                        ma3_last < ma100_last
                        and ma300_last < ma300_120_min_ago
                        and ma100_last > ma200_last
                        and deviation_sell < -0.09
                        and ma2_last < ma2_2_min_ago
                    ):
                   
                        sell = "SELL 1 > 110 min FORSE E' NECESSARA SOLO QUESTA 3 ! deviation_sell < -0.09 - r 5083"
                        action = "sell"
                        
                        
                        
                    # ATTENZIONE 4 ! > 110 min E CON 300 < 120 min FORSE E' NECESSARA SOLO QUESTA !
                    
                    elif (    
                        ma3_last < ma100_last
                        and ma300_last < ma300_120_min_ago
                        and ma100_last < ma200_last
                        and deviation_sell < -0.05
                        and ma2_last < ma2_2_min_ago
                    ):
                   
                        sell = "SELL 1 > 110 min FORSE E' NECESSARA SOLO QUESTA 4 ! deviation_sell < -0.05 - r 5084"
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
                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.23 - r 5106"
                        action = "sell"
                      
                    
               
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.25 - 0.60 FINTA DI MARADONA - r 5118"
                        action = "sell"
                        
                 
                
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.61 and deviation_sell < 0.79
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.61 - 0.79 DRIBBLING DI RONALDO - r 5130"
                        action = "sell"
                    
                    
                    
               
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 0.80 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell 0.80 - 1.20 DOPPIO PASSO ALLA RONALDO - r 5142"
                        action = "sell"
                  
                
                
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell > 1.21 (che sarebbe come IL DRIBBLING ALLA RONALDO !) - r 5154"
                        action = "sell"
                        
                        
                    
                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 < and incrocio 3-28 - r 5167"
                        action = "sell"
                        
                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                   
                
                
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 - r 5181"
                        action = "sell"
                        
                        
                        
               
                    # ---------------------------------------------------------------------------------------------------------------------- crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - r 5195"
                        action = "sell"
                        
                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - r 5208"
                        action = "sell"
                   
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                        and deviation_sell > 0.60
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - r 5220"
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
                        sell = "SELL 2 (3-5 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.25 - r 5238"
                        action = "sell"
                        
                 
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                    ):  
                        sell = "SELL 2 (3-5 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 5249"
                        action = "sell"
                        
                        
                        
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.57 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 > and incrocio 3-15 and deviation_sell 0.57 - 1.20 - r 5261"
                        action = "sell"
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - r 5273"
                        action = "sell"
                        
                    
                    
                    
                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 < and incrocio 3-28 - r 5288"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        # deviation_sell_ma78 = ma3_last / ma78_last
                        
                        
                        
                  
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.23 - r 5303"
                        action = "sell"
                        
                        
                        

                    # ---------------------------------------------------------------------------------------------------------------------- guadagno con crollo
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 5318"
                        action = "sell"
                        
                   
                
                
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 5330"
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
                        sell = "SELL 2 (5-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - r 5350"
                        action = "sell"
                    
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.25
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - r 5362"
                        action = "sell"
                        
                        
                        
                   
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 5375"
                        action = "sell"
                        
                        
                        
                   
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma15_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 >  3 < 15 and deviation_sell 0.57 - 0.90 - DRIBBLING ALLA RONALDO - r 5388"
                        action = "sell"
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - r 5401"
                        action = "sell"
                        
                        
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - r 5413"
                        action = "sell"
                        
                        
                        
                        
                    ###########################################################################     trend in ribasso and ma200_last < ma300_last
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma300_last
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.31
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 < AND 200<300 and incrocio 3-28 and deviation_sell < -0.31 - r 5428"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        
                        
                  
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma300_last
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 < AND 200<300 and incrocio 3-100 (cuscino di sant' antonio) - r 5443"
                        action = "sell"
                        
                 
                
                
                    ###########################################################################     trend in ribasso MA ma200_last > ma300_last
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma300_last
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.35
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 < MA 200>300 and incrocio 3-28 and deviation_sell < -0.35 - r 5458"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                  
                
                
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma300_last
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.40
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 < MA 200>300 and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.40 - r 5473"
                        action = "sell"
                        
                        
                        
                   
                    # ------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 guadagno con crollo (5-12 min) con ma50 < and incrocio 3-23 - r 5487"
                        action = "sell"
                        
                        

                    # ------------------------------------------------------------------------------------------------------------ PARACADUTE crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.48
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.48 - r 5500"
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
                        sell = "SELL 2 (12-21 min) con ma50 > and incrocio 3-69 and deviation sell -0.34 e vaffanculo ! - r 5523"
                        action = "sell"
                        
                        # and deviation_ma39 < -0.29 vendeva troppo presto
                        # ATTENZIONE "and (ma3_prev > ma39_prev and ma3_last < ma39_last)" con ma39 NON HA INCROCIATO
                        
                        
                        
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma100_prev and ma3_last < ma100_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.36 - r 5538"
                        action = "sell"
                        
                  
                
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and 5<25 and deviation_sell 0.25-0.56 - MARADONA - r 5551"
                        action = "sell"
                        
                       
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma25_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and 3<25 and deviation_sell 0.57-0.90 - DOPPIO PASSO ALLA RONALDO fino a +0.50 - r 5564"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma100_last > ma300_last
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and incrocio 3-15 and deviation_sell 0.91 - 1.20 CON 100 > 300 RIALZO - r 5579A"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma100_last < ma300_last
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and incrocio 3-20 and deviation_sell 0.91 - 1.20 CON 100 < 300 CROLLO - r 5579B"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                        
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and incrocio 3-13 and deviation_sell > 1.21 - r 5593"
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
                        sell = "SELL 2 (12-21 min) con ma50 < and deviation_ma39 < -0.195 - r 5609"
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
                        sell = "SELL 2 (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - r 5629"
                        action = "sell"
                        
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50< ! 
                        
                        
                       

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.28
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - r 5643"
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
                        sell = "SELL 2 PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 5660"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                        
                        
                    # ----------------------------------------------------------------------------- guadagno con crollo
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma18_last > ma18_30_min_ago
                         
                        and (ma4_prev > ma33_prev and ma4_last < ma33_last)
                        and deviation_sell > 0.22
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 4 - 33 se 18> and deviation_sell > 0.22 - r 5676a"
                        action = "sell"
                        
                        # 19 giu 2022 4-33 da 4-20
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma18_last < ma18_30_min_ago
                        
                        and (ma4_prev > ma20_prev and ma4_last < ma20_last)
                        and deviation_sell > 0.22
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 4 - 20 se 18< and deviation_sell > 0.22 - r 5676b"
                        action = "sell"
                        
                        # 19 giu 2022 4-33 da 4-20
            
            
            
                ############################################################################################################## SESSIONE 2 ( 21-60 min )

                # VENDITA - da 21 a 60 minuti = da 1261 a 3600 secondi
                
                
                elif (
                    seconds_since_last_trade > 1261 and seconds_since_last_trade <= 3600
                ):
                    
                
                    ######################################################################################################## righe compa RADDOPPIATE !
                    
                    # situazione in miglioramento
                    
                    if (        
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.255
                        and ma200_last < ma200_60_min_ago
                        and ma100_last > ma200_last
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and deviation_ma39 < -0.255 situazione in miglioramento - r 5700"
                        action = "sell"
                        
                        
                    
                    
                    
                    
                    
                    # situazione post crollo
                    
                    elif (        
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma200_last
                        and deviation_sell < -0.28
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.26
                        and ma200_last < ma200_60_min_ago
                        
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and deviation_ma39 < -0.26 and deviation_sell < -0.28 - situazione post crollo - r 5701"
                        action = "sell"
                        
                        
                    
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    # situazione in miglioramento
                    
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and ma100_last > ma200_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.32
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                        
                    ):
                        sell = "SELL 2 (21-60 min) RAFFORZATA con ma50 > and (deviation_sell < -0.32 and ma3_last < ma50_last) situazione in miglioramento - r 5703"
                        action = "sell"
                        
                        
                        
                   
                        
                  
                    
                    # situazione post crollo
                    
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.30
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                        and ma100_last < ma200_last
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and (deviation_sell < -0.28 and ma3_last < ma50_last) situazione post crollo - r 5704"
                        action = "sell"
                        
                        
                        
                        #######################################################################################################################
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (        
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.29
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and deviation_ma39 < -0.29 - TOLLERANTE ! - r 5725"
                        action = "sell"
                        
                  
                
                    
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.31
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and (deviation_sell < -0.29 and ma3_last < ma50_last) TOLLERANTE ! - r 5738"
                        action = "sell"
                        
                        # 21 giu 2022 0.31 da 0.29
                        
                        
                        
                    ##############################################################################################################################
                        
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.29
                        and ma300_last > ma300_120_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.29 - r 5754"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.26
                        and ma300_last < ma300_120_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.26 - r 5755"
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
                        sell = "SELL 2 (21-60 min) con ma50 > and 5<39 and deviation_sell 0.25 - 0.56 MARADONA e' piu' stanco e paziente - r 5772"
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
                        sell = "SELL 2 (21-60 min) con ma50 > AND 200>120 min and 5<69 (fidati!) and deviation_sell 0.57 - 0.90 ELASTICO ALLA RONALDO - r 5794"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    # ELASTICO ALLA RONALDO SE ma200 < ma200 120 min ago
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last > ma100_60_min_ago
                        and ma200_last < ma200_120_min_ago
                        
                        and ma3_last < ma48_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > AND 200>120min and 100> and 3<48 and deviation_sell 0.57 - 0.90 ELASTICO ALLA RONALDO - r 5812 a"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    # ELASTICO ALLA RONALDO SE ma200 < ma200 120 min ago
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and ma200_last < ma200_120_min_ago
                        
                        and ma3_last < ma25_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > AND 200>120min and 100< and 3<25 and deviation_sell 0.57 - 0.90 ELASTICO ALLA RONALDO - r 5812 b"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    
                    ##############################################################################################################
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                   
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and incrocio 3-18 and deviation_sell 0.91 - 1.20 - r 5829"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma30_prev and ma5_last < ma30_last)
                        and deviation_sell > 1.21 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and incrocio 5-30 (!) SI PROPRIO COSI' ! 3-30 ! and deviation_sell 1.21 - 2.70 - r 5842"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and incrocio 3-20 and deviation_sell > 2.71 - r 5853"
                        action = "sell"
                        

                        
                    #################################################################################################### con trend discendente
                    #################################################################################################### 2 righe del compa GIA' CON TOLLERANZA
                    
                    
                    
                    elif (        
                        ma50_last < ma50_2_min_ago
                        and ma300_last > ma300_120_min_ago
                        
                        and ma78_last > ma200_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.30
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 < and deviation_ma39 < -0.30 AND 78>200 - r 5867 A"
                        action = "sell"    
                        
                        
                    elif (        
                        ma50_last < ma50_2_min_ago
                        and ma300_last > ma300_120_min_ago
                        
                        and ma78_last < ma200_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.295
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 < and deviation_ma39 < -0.295 AND 78<200 - r 5867 B"
                        action = "sell"
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    # ecco inequivocabilmente il crollo !
                    
                    elif (        
                        ma50_last < ma50_2_min_ago
                        and ma300_last < ma300_120_min_ago
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.31
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 < and deviation_ma39 < -0.31 - r 5868"
                        action = "sell"
                        
                        # durante il crollo non devi pensare ai centesimi !
                        
                  
                    
                    
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.32
                        and ma200_last < ma200_60_min_ago
                        and ma50_last > ma100_last
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 < and deviation_sell < -0.32 - r 5879"
                        action = "sell"
                        
                        # 2 GIUGNO a 0.335 da 0.32
                        
                        
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.335
                        and ma200_last < ma200_60_min_ago
                        and ma50_last < ma100_last
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 < and deviation_sell < -0.335 - r 5880"
                        action = "sell"
                        
                        # 2 GIUGNO a 0.335 da 0.32
                        
                    
                    
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_60_min_ago
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.37
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - r 5893"
                        action = "sell"
                        
                        
                   
                    
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_60_min_ago
                        and ma100_last > ma100_60_min_ago
                        
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.31
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50< 200< e 100> and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO con deviation_sell < -0.31 - r 5906"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_60_min_ago
                        and ma100_last < ma100_60_min_ago
                        
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.29
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50< 200< e 100< and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO con deviation_sell < -0.29 - r 5907"
                        action = "sell"
                        
                        
                        
                        
                        
                        
                      
                    
                    ############################################################################################################## con > PERDITA TOLLERATA !
                    
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
                        sell = "SELL 2 (21-60 min) con ma50 < and deviation_ma39 < -0.29   con > PERDITA TOLLERATA ! - r 5930"
                        action = "sell"
                        
                        
                 
                    elif (  
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.35
                        and ma200_last > ma200_60_min_ago
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                     
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 < and deviation_sell < -0.35 con > PERDITA TOLLERATA ! - r 5944"
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
                        sell = "SELL 2 (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.40 con > PERDITA TOLLERATA ! - r 5959"
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
                        sell = "SELL 2 (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO con > PERDITA TOLLERATA ! - r 5974"
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
                        sell = "SELL 2 (21-60 min) eventuale guadagno durante il crollo (21-60 min) con ma50 < incrocio 3 - 18 and deviation_sell > 0.23 - r 5992"
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
                        and deviation_ma100_sopra_ma300 > 0.70
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 > and deviation_ma39 < -0.18 SE 100 MOLTO ALTA RISPETTO ALLA 300 OK COSI' - r 6015 a"
                        action = "sell"
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        and deviation_ma100_sopra_ma300 < 0.70
                        and deviation_sell < -0.10
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 > and deviation_ma39 < -0.18 SE 100 VICINA ALLA 300 C'E' DEV SELL < -0.10  - r 6015 b"
                        action = "sell"
                        
                        
                        
                        
                        
               
                    elif (      
                        ma50_last > ma50_2_min_ago
                        and deviation_sell < -0.18
                        and ma3_last < ma50_last
                        and ma2_last < ma2_2_min_ago 
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 > and (deviation_sell < -0.18 and ma3_last < ma50_last)  - r 6026"
                        action = "sell"
                        
                        
                    
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and deviation_ma39 < -0.22
                        and ma2_last < ma2_2_min_ago
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 > and deviation_ma39 <-0.22 - r 6037"
                        action = "sell"
                        
                        
                  
                    elif (      
                        ma50_last > ma50_2_min_ago
                        and deviation_sell < -0.21
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 > and (deviation_sell < -0.21 and ma3_last < ma50_last)  - r 6049"
                        action = "sell"
                        
                       
                    
                    
                        ##################################################################################################################### 
                     
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma50_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 > and 5-50 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 6065"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma4_prev > ma25_prev and ma4_last < ma25_last)
                        and deviation_sell > 0.57 and deviation_sell < 0.80
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50> and incrocio 4-25 and deviation_sell 0.57-0.80 FINTA ALLA RONALDO - r 6079"
                        action = "sell"
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.81 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 da 60 a 90 min con ma50 > and incrocio 3-18 and deviation_sell 0.81 - 1.49 RABONA ALLA RONALDO - r 6092"
                        action = "sell"

                        # ma ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma34_prev and ma3_last < ma34_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and deviation_ma100_sopra_ma200 > 0.45
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 da 60 a 90 min con ma50 > CON 100>200 > 0.45 incrocio 3-34 (!) and dev_sell 1.50 - 2.70 DOPPIO PASSO ALLA RONALDO - r 6108"
                        action = "sell"
                        
                        # 6 giu 2022 3-34 da 3-13
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and deviation_ma100_sopra_ma200 < 0.45
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 da 60 a 90 min con ma50 > CON 100>200 < 0.45 incrocio 3-16 and dev_sell 1.50 - 2.70 DOPPIO PASSO ALLA RONALDO - r 6109"
                        action = "sell"
                        
                        # 6 giu 2022 3-16 da 3-13
                        
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 da 60 a 90 min con ma50 > incrocio 3-20 and deviation_sell > 2.71 STIAMO TRA GLI ANGELI, compa ! - r 6121"
                        action = "sell"
                        
                        
                    
                    ######################################################################################## trend discendente con PERDITA BASE
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        
                        and deviation_ma39 < -0.17
                        and deviation_sell < 0.10
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min TREND < con PERDITA BASE con ma50 < con deviation_ma39 <-0.17 and deviation_sell < 0.10 - r 6137"
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
                        sell = "SELL 2 da 60 a 90 min TREND < con PERDITA BASE  con ma50 < con incrocio 3-78 and deviation_sell < -0.13 - r 6156"
                        action = "sell"
                        
                        
                        
                        
                        
                    ######################################################################################## trend discendente con POCA PERDITA TOLLERATA
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last > ma100_60_min_ago
                        and ma100_last > ma200_last
                        
                        and deviation_ma39 < -0.18
                        and deviation_sell < -0.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min TREND < con POCA PERDITA TOLLERATA con ma50 < con deviation_ma39 <-0.17 and deviation_sell < -0.20 - r 6172"
                        action = "sell"
                        
                        # and ma3_last < ma39_last
                        # and deviation_sell < -0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare ! POI STIAMO GIA' AL SELL 2 -le ma hanno avuto piu' tempo di salire
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # cuscino dell' angelo custode
                        
                        
                        
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last > ma100_60_min_ago
                        and ma100_last < ma200_last
                        
                        and deviation_ma39 < -0.18
                        and deviation_sell < -0.15
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min TREND < con POCA PERDITA TOLLERATA con ma50 < con deviation_ma39 <-0.17 and deviation_sell < -0.15 - r 6173"
                        action = "sell"
                        
                        # and ma3_last < ma39_last
                        # and deviation_sell < -0.10
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
                        sell = "SELL 2 da 60 a 90 min con POCA PERDITA TOLLERATA con ma50 < con incrocio 3-78 and deviation_sell < -0.14 - r 6192"
                        action = "sell"
                        
                        
                    
                    
                    ################################################################################## trend discendente con MOLTA PERDITA TOLLERATA
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma59_last
                        and deviation_ma100_sopra_ma300 > 0.50
                        and deviation_trend_ma200 > -0.12
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con MOLTA PERDITA TOLLERATA con ma50 < con 3 < 59 con 100 sopra 300 < 0.50 - r 6207a"
                        action = "sell"
                        
                        # questa anticipa di una ndecchia la prossima
                        
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma59_last
                        and deviation_ma100_sopra_ma300 < 0.50
                        and deviation_sell < -0.25
                        
                        and deviation_trend_ma200 > -0.12
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con MOLTA PERDITA TOLLERATA con ma50 < con 3 < 59 con 100 sopra 300 < 0.50 - r 6207b"
                        action = "sell"
                        
                        # questa anticipa di una ndecchia la prossima
                        
                        
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.19
                        
                        and deviation_trend_ma200 > -0.12
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con MOLTA PERDITA TOLLERATA con ma50 < con deviation_ma39 < -0.19 - r 6208"
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
                        sell = "SELL 2 da 60 a 90 min con MOLTA PERDITA TOLLERATA con ma50 < con incrocio 3-78 and deviation_sell < -0.15 - r 6229"
                        action = "sell"
                        
                        
                        
                        
                        
                    # AGGIUNTA TARDIVA MA FORSE NECESSARIA !
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        
                        and ma100_last < ma200_last
                        and ma200_last < ma300_last
                        
                        and ma200_last < ma200_120_min_ago
                        and ma300_last < ma300_120_min_ago
                   
                        and deviation_sell < -0.10
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min AGGIUNTA TARDIVA MA FORSE NECESSARIA ! - r 6230"
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
                        sell = "SELL 2 90-110 min con ma50 > and deviation_ma39 <-0.22 (no ma3<ma39) - r 6250"
                        action = "sell"
                        
                   
                
                    elif (      
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.21 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 2 90-110 min con ma50 > and (deviation_sell < 0.21 and ma3_last < ma50_last) - r 6262"
                        action = "sell"
                        
                        
                        
                        
                    elif (  
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.23
                        and ma200_last < ma200_60_min_ago
                    ):    
                        sell = "SELL 2 90-110 min con ma50 > and deviation_ma39 < -0.23 - r 6274"
                        action = "sell"
                        
                        
                        
                   
                    elif (      
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.22 
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 2 90-110 min con ma50 > and (deviation_sell < -0.22 and ma3_last < ma50_last) - r 6287"
                        action = "sell"
                        
                        
                        
                    #########################################################################################################
                   
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma50_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 90-110 min con ma50 > and 5-50 (!) and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA (non toccare) - r 6302"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                     
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 90-110 min con ma50 > con 4-20 and deviation_sell 0.57-0.90 DRIBBLING ALLA RONALDO - r 6316"
                        action = "sell"
                        
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma22_prev and ma3_last < ma22_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 90-110 min con ma50 > incrocio 3-22 and deviation_sell 0.91 - 1.49 - r 6329"
                        action = "sell"

                        # ma 3-48 mi evita la ricompra e la rivendita con perdita !
                        # ma 3-15 vendeva troppo presto. guardando il grafico da piu' lontano.
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 90-110 min con ma50 > incrocio 3-13 and deviation_sell 1.50 - 2.70 - r 6344"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 90-110 min con ma50 > incrocio 3-11 (!) and deviation_sell > 2.71 - r 6356"
                        action = "sell"
                        
                        
                        

                    ######################################################################################## con trend discendente
                    
                    
                    elif (  
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.25
                        and deviation_trend_ma100 > 0.10
                    ):
                        sell = "SELL 2 90-110 min con ma50 < MA ma100 > con deviation_ma39 <-0.25 - r 6371"
                        action = "sell"
                        
              
                    
                
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.20 
                        and ma3_last < ma39_last
                        and deviation_trend_ma100 > 0.10
                    ):
                        sell = "SELL 2 90-110 min con ma50 < MA ma100 > and (deviation_sell < -0.20 and ma3_last < ma39_last) - r 6384"
                        action = "sell"
                        
                  
                
                        
                    elif (  
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.22
                        and deviation_trend_ma100 < 0.10
                    ):
                        sell = "SELL 2 90-110 min con ma50 < MA ma100 < con deviation_ma39 <-0.22 - r 6396"
                        action = "sell"
                        
                        
                
                 
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.20
                        and ma3_last < ma39_last
                        and deviation_trend_ma100 < 0.10
                    ):
                        sell = "SELL 2 90-110 min con ma50 < MA ma100 < and (deviation_sell < -0.20 and ma3_last < ma39_last) - r 6409"
                        action = "sell"
                        
                    
                    
                    
                    ########################################################################################## AUMENTA PERDITA TOLLERATA e divido in 2 il compa
                    
                    
                    elif (  
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.235
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 compa 90-110 min  con ma50 < con deviation_ma39 <-0.235 con > PERDITA TOLLERATA - r 6426"
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
                        sell = "SELL 2 compa 90-110 min con ma50 < (deviation_sell < -0.24 and ma3_last < ma39_last) con > PERDITA TOLLERATA - r 6441"
                        action = "sell"
                        
                        
                 
                ##########################################################################################################
                
                # VENDITA 2 - da 110 minuti in poi = da 6601 secondi in poi

                elif seconds_since_last_trade > 6601:
                    
                    
                    ###################################################################################   RIGHE DEL COMPA raddoppiate PER AUMENTO TOLLERANZA
                    
                    if (  
                        ma50_last > ma50_2_min_ago
                        and ma100_last > ma200_last
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.22
                        and deviation_sell < -0.25 
                        and ma200_last > ma200_60_min_ago
                    ):    
                        sell = "SELL 2 dopo 110 min con ma50 > and deviation_ma39 <-0.22 (no ma3<ma39) - r 6461"
                        action = "sell"
                        
                        
                    if (  
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma200_last
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.22
                        and ma200_last > ma200_60_min_ago
                    ):    
                        sell = "SELL 2 dopo 110 min con ma50 > and deviation_ma39 <-0.22 (no ma3<ma39) - r 6462"
                        action = "sell"
                        
                        # POTREBBE ESSERE SITUAZIONE DI CROLLO SOLO CON 39 E SENZA DEVIATION SELL
                        
                        
                        
                   
                
                    elif (      
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.21 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "sessione 2 SELL dopo 110 min con ma50 > and (deviation_sell < 0.21 and ma3_last < ma50_last) - r 6474"
                        action = "sell"
                        
                        
                        
                        
                    elif (  
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.23
                        and ma200_last < ma200_60_min_ago
                    ):    
                        sell = "sessione 2 SELL 2 dopo 110 min con ma50 > and deviation_ma39 < -0.23 - r 6486"
                        action = "sell"
                        
                   
                
                
                    elif (      
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.22 
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "sessione 2 SELL dopo 110 min con ma50 > and (deviation_sell < -0.22 and ma3_last < ma50_last) - r 6499"
                        action = "sell"
                        
                        
                        
                        
                    ################################################################################### fare maradona 1 e maradona 2 se ma2 sta sopra ma100
                   
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma59_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 dopo 110 min con ma50 > and 5-59 (!) and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA (non toccare) - r 6515"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # 9 GIU 2022 5-59 da 5-50
                     
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 > 110 min con ma50 > con 4-20 and deviation_sell 0.57-0.90 DRIBBLING ALLA RONALDO - r 6529"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 dopo 110 min con ma50 > incrocio 3-15 and deviation_sell 0.91 - 1.49 - r 6542"
                        action = "sell"

                        # ma 3-48 mi evita la ricompra e la rivendita con perdita !
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 dopo 110 min con ma50 > incrocio 3-13 and deviation_sell 1.50 - 2.70 - r 6557"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 dopo 110 min con ma50 > incrocio 3-11 (!) and deviation_sell > 2.71 - r 6569"
                        action = "sell"
                        
                        

                    ######################################################################################## con trend discendente
                    
                    
                    elif (  
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.25
                        and deviation_trend_ma100 > 0.10
                    ):
                        sell = "SELL 2 dopo 110 min con ma50 < MA ma100 > con deviation_ma39 <-0.25 - r 6583"
                        action = "sell"
                        
              
                    
                
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.20 
                        and ma3_last < ma39_last
                        and deviation_trend_ma100 > 0.10
                    ):
                        sell = "SELL 2 dopo 110 min con ma50 < MA ma100 > and (deviation_sell < -0.20 and ma3_last < ma39_last) - r 6596"
                        action = "sell"
                        
                  
                        
                    
                    elif (  
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.22
                        and deviation_trend_ma100 < 0.10
                    ):
                        sell = "SELL 2 dopo 110 min con ma50 < MA ma100 < con deviation_ma39 <-0.22 - r 6608"
                        action = "sell"
                        
                        
                
                 
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.18 
                        and ma3_last < ma39_last
                        and deviation_trend_ma100 < 0.10
                    ):
                        sell = "SELL 2 dopo 110 min con ma50 < MA ma100 < and (deviation_sell < -0.18 and ma3_last < ma39_last) - r 6621"
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
                        sell = "SELL 2 compa dopo 110 min con ma50 < con deviation_ma39 <-0.24 con > PERDITA TOLLERATA - r 6638"
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
                        sell = "SELL 2 compa dopo 110 min con ma50 < (deviation_sell < -0.24 and ma3_last < ma39_last) con > PERDITA TOLLERATA - r 6652"
                        action = "sell"
                        
                        
                        
                 
                    # ATTENZIONE : DOPO 110 MIN forse E' NECESSARIA SOLO QUESTA !
                    
                    elif (    
                        ma3_last < ma100_last
                        and deviation_sell < 0.05
                        and ma2_last < ma2_2_min_ago
                    ):
                   
                        sell = "SELL 2 > 110 min forse E' NECESSARA SOLO QUESTA ! - r 6666"
                        action = "sell"
                    
                        
                    
                    
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
                        sell = "SELL 3 (0-3 min) con ma50 > and 3<18 and deviation_sell < -0.33 - r 6689"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                     
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma25_prev and ma5_last < ma25_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 3 (0-3 min) con ma50 > and incrocio 5-25 and deviation_sell 0.25 - 0.60 MARADONA - r 6703"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.61 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (0-3 min) con ma50 > and incrocio 3-15 and deviation_sell 0.61 - 0.90 RONALDO - r 6717"
                        action = "sell"
                        
                        
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell 0.91 - 1.20 - r 6730"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell > 1.21 (che sarebbe come IL DRIBBLING ALLA RONALDO !) - r 6743"
                        action = "sell"
                        
                        
                        

                    ###########################################################################     trend in ribasso
                    

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (0-3 min) con ma50 < and incrocio 3-28 - r 6758"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 - r 6772"
                        action = "sell"
                        
                        

                    # ---------------------------------------------------------------------------------------------------------------------- crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - r 6785"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - r 6799"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                        and deviation_sell > 0.60
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - r 6812"
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
                        sell = "SELL 3 (3-5 min) con ma50 > and 3 < 18 and deviation_sell < -0.335 - r 6829"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 6844"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 > and 5<20 (no incrocio 3-9) and deviation_sell 0.57 - 0.90 - DRIBBLING ALLA RONALDO - r 6859"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - r 6873"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - r 6885"
                        action = "sell"
                        
                  
                    ###########################################################################     trend in ribasso
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 < and incrocio 3-28 - r 6898"
                        action = "sell"
                        
                        # deviation_sell_ma78 = ma3_last / ma78_last
                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.23 - r 6912"
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
                        sell = "SELL 3 (3-5 min) con ma50 < and incrocio 3-28 con > PERDITA TOLLERATA - r 6931"
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
                        sell = "SELL 3 (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.23 con > PERDITA TOLLERATA - r 6949"
                        action = "sell"
                        
                       

                    # -------------------------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - r 6962"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 6974"
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
                        sell = "SELL 3 (5-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - r 6994"
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
                        sell = "SELL 3 (5-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - r 7010"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 7025"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                  
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 >  5<20 and deviation_sell 0.57 - 0.90 - DRIBBLING ALLA RONALDO - r 7040"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma20_prev and ma5_last < ma20_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 > and incrocio 5-20 and deviation_sell 0.91 - 1.20 - r 7055"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - r 7069"
                        action = "sell"
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 < and incrocio 3-28 - r 7082"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last > ma100_60_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.39
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 < and ma100 > 60 min ago and incrocio 3-100 (cuscino di sant' antonio) E deviation_sell < -0.39 - r 7096"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.38
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 < and ma100 < 60 min ago and incrocio 3-100 (cuscino di sant' antonio) E deviation_sell < -0.38  - r 7097"
                        action = "sell"
                        
                        
                        

                    # ------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 guadagno con crollo (5-12 min) con ma50 < and incrocio 3-23 - r 7110"
                        action = "sell"
                        
                        

                    # ------------------------------------------------------------------------------------------------------------ PARACADUTE crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.48
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.48 - r 7123"
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
                        sell = "SELL 3 (12-21 min) con ma50 > and incrocio 3-72 and deviation sell -0.35 e vaffanculo ! - r 7145"
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
                        sell = "SELL 3 (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.36 - r 7162"
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
                        sell = "SELL 3 (12-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.54 - FINTA ALLA MARADONA - r 7181"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma20_last
                        and deviation_sell > 0.55 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and 5-20 and deviation_sell 0.55-0.90 - DOPPIO PASSO ALLA RONALDO - r 7196"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and incrocio 3-20 and deviation_sell 0.91 - 1.20 - r 7211"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                       
                    

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and incrocio 3-30 and deviation_sell > 1.21 - r 7225"
                        action = "sell"
                        
                  
                
                    ##########################################################################################
                    
                    # NON TOCCARE ! CUSCINO DI SANT' ANTONIO !
                    # L' INCROCIO 5-100 MI SALVA ! MA 5<100 VENDE DURANTE IL RIBASSO !
                    
                  
                    ##################################################################### con trend discendente
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.165
                        
                        and deviation_ma100_sopra_ma200 > -0.70
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 < and deviation_ma39 < -0.165 100 spra 200 > -0.70 - r 7244a"
                        action = "sell"
                        
                        # and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        # and deviation_sell < -0.25
                        # ATTENZIONE QUESTA aveva FATTO -0.61% !
                        # QUINDI ho abbassato da 0.17 a 0.16 a 0.15
                        # HO NOTATO CHE ANCHE INCROCIO 5-100 SAREBBE ARRIVATO TARDI
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10
                        
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.165
                        
                        and deviation_ma100_sopra_ma200 < -0.70
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 < and deviation_ma39 < -0.165 100 spra 200 < -0.70 crollo ! - r 7244b"
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
                        sell = "SELL 3 (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - r 7263"
                        action = "sell"
                        
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50< !
                        
                    

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - r 7277"
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
                        sell = "SELL 3 (12-21 min) con ma50 < and deviation_ma39 < -0.185 con > PERDITA TOLLERATA - r 7296"
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
                        sell = "SELL 3 (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.47 con > PERDITA TOLLERATA - r 7318"
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
                        sell = "SELL 3 (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO con > PERDITA TOLLERATA - r 7335"
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
                        sell = "SELL 3 PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 7352"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                    
                    
                    
                    # ----------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                        
                        and ma5_last < ma78_last
                    ):
                        sell = "SELL 3 eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3 - 18 and deviation_sell > 0.23 - r 7368"
                        action = "sell"
                        
                        
                        
                        

                ################################################################################################################## sessione 3-4-x ( 21-60 min )

                # VENDITA - da 21 a 60 minuti = da 1261 a 3600 secondi

                elif (
                    seconds_since_last_trade > 1261 and seconds_since_last_trade <= 3600
                ):
                    
                    
                    ################################################################################################ RIGHE DEL COMPA raddoppiate
                    
                    
                    if (    
                        ma50_last > ma50_2_min_ago
                        and deviation_ma100_sopra_ma200 > 0.30
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.27
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and deviation_ma25 < -0.27 CON 100-200 > 0.30 - r 7392"
                        action = "sell"
                        
                        # in alto senza deviation sell
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and deviation_ma100_sopra_ma200 < 0.30
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.27
                        and deviation_sell < -0.30
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and deviation_ma25 < -0.27 and deviation_sell < -0.30 CON 100-200 < 0.30 - r 7393"
                        action = "sell"
                        
                        # in basso con deviation sell 
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (      
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.25 
                        and ma3_last < ma42_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL (21-60 min) con ma50 > and (deviation_sell < -0.25 and ma3_last < ma42_last) - r 7405"
                        action = "sell"
                        
                        # 16 GIU 2022 3-42 da 3-50
                        
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.31
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and deviation_ma25 < -0.31 - r 7417"
                        action = "sell"
                        
                    
                    
                    
                    elif (      
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.27 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and (deviation_sell < -0.27 and ma3_last < ma50_last) - r 7430"
                        action = "sell"
                        
                       
                    
                    
                        ##################################################################################################################
                        
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.26
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.26 - r 7445"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and (ma5_prev > ma39_prev and ma5_last < ma39_last)
                        
                        and ma39_last > ma100_last
                        
                        and ma2_last < ma2_2_min_ago
                   
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and 39>100 and incrocio 5-39 and deviation_sell 0.25 - 0.56 FINTA DI MARADONA - r 7460"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and (ma5_prev > ma30_prev and ma5_last < ma30_last)
                        
                        and ma39_last < ma100_last
                        
                        and ma2_last < ma2_2_min_ago
                   
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and 39<100 and incrocio 5-39 and deviation_sell 0.25 - 0.56 FINTA DI MARADONA - r 7461"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma5_last < ma39_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and 5 < 39 and deviation_sell 0.57 - 0.90 ELASTICO ALLA RONALDO - r 7475"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # 31 maggio 2022 5-39 da 5-20
                        
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 3-30 and deviation_sell 0.91 - 1.20 - r 7491"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # 14 giu 2022 3-28 da 3-30
                        
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma300_last
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.21 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 3-30 and dev_sell 1.21 -2.70 - ma100 e' ancora sotto ma300 e vende un po' prima - r 7505"
                        action = "sell"
                        
                        # vende un po' prima perche' e' ancora un po' preoccupato perche' ma100 sta sotto ma300
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last > ma300_last
                        and (ma3_prev > ma52_prev and ma3_last < ma52_last)
                        and deviation_sell > 1.21 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 3-52 and dev_sell 1.21 -2.70 - ma100 e' andata sopra ma300 e si distende - r 7506"
                        action = "sell"
                        
                        
                        
                        
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 3-11 and deviation_sell > 2.71 - r 7517"
                        action = "sell"
                    
                    
                   
                    ##################################################################### con trend discendente
                   
                    
                    elif (     
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.23
                        
                        and deviation_ma100_sopra_ma300 > 0.50
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and deviation_ma39 < -0.23 con 50 sopra 300 > 0.50 - r 7532"
                        action = "sell"
                        
                        # attenzione se ma100 sta molto sopra ma 300 basta deviation ma39
                        # ma se trend laterale metto anche una deviation sell ( vedi prossimo elif )
                        
                    
                    
                    
                    elif (     
                        ma50_last < ma50_2_min_ago
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.23
                        
                        and deviation_ma100_sopra_ma300 < 0.50
                        and deviation_sell < -0.25
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and deviation_ma39 < -0.23 and deviation_sell < -0.25 con 50 sopra 300 < 0.50 - r 7550"
                        action = "sell"
                        
                        # attenzione se ma100 sta molto sopra ma 300 basta deviation ma39
                        # ma se trend laterale metto anche una deviation sell
                        
                        
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma300_last > ma300_120_min_ago
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.31
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and ma300> and deviation_sell < -0.31 - r 7565"
                        action = "sell"
                        
                    
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma300_last < ma300_120_min_ago
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.28
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and ma300< and deviation_sell < -0.28 - r 7577"
                        action = "sell"
                        
                     
                    

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.37
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - r 7589"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - r 7602"
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
                        sell = "SELL 3 compa (21-60 min) con ma50 < and deviation_ma39 < -0.26 con PERDITA TOLLERATA > - r 7625"
                        action = "sell"
                        
                        
                     
                    
                    elif ( 
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.29
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                    ):
                        sell = "SELL 3 compa (21-60 min) con ma50 < and deviation_sell < 0.29 con PERDITA TOLLERATA > - r 7638"
                        action = "sell"
                        
                        
                        
                    
                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.39
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.39 con > perdita tollerata - r 7652"
                        action = "sell"
                        
                        
                        
                        

                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - con > perdita tollerata - r 7668"
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
                        sell = "SELL 3 eventuale guadagno durante il crollo (21-60 min) con ma50 < incrocio 3 - 18 and deviation_sell > 0.23 - r 7685"
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
                        sell = "SELL 3 da 60 a 90 min con ma50 > and deviation_ma25 < -0.19 - r 7711"
                        action = "sell"
                        
                        
                        
                    
                    
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.20 
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 > and (deviation_sell < -0.19 and ma3_last < ma50_last) - r 7725"
                        action = "sell"
                        
                        
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago
                        and deviation_ma25 < -0.21
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 > and deviation_ma25 < -0.19 - r 7737"
                        action = "sell"
                        
                        
                        
                    
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.20 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 > and (deviation_sell < -0.19 and ma3_last < ma50_last) - r 7750"
                        action = "sell"
                        
                        
                        
                        ############################################################################################################
                        
                        
                     
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma50_prev and ma5_last < ma50_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 5-50 and deviation_sell 0.25 - 0.56 FINTA DI MARADONA - r 7766"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 >60 min con ma50> and 4-20 and deviation_sell 0.57-0.90 DRIBBLING ALLA RONALDO - r 7780"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 da 60 a 90 min con ma50 > and incrocio 3-30 and deviation_sell 0.91 - 1.49 - r 7793"
                        action = "sell"

                        # ma ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma300_last
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 da 60 a 90 min con ma50 > incrocio 3-20 and dev_sell 1.50 - 2.70 - ma100 ancora sotto ma300 e vende un po' prima - r 7809"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last > ma300_last
                        and (ma3_prev > ma50_prev and ma3_last < ma50_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 da 60 a 90 min con ma50 > incrocio 3-50 and deviation_sell 1.50 - 2.70 - ma100 sopra ma300 e si distende - r 7810"
                        action = "sell"
                        
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 da 60 a 90 min con ma50 > incrocio 3-11 and deviation_sell > 2.71 - r 7823"
                        action = "sell"
                        
                        
                       
                    ############################################################################# con trend discendente MA 100 sopra di molto da 300
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.16
                        and ma2_last < ma2_2_min_ago
                        
                        and deviation_ma100_sopra_ma300 > 0.69
                       
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 < con deviation_ma39 <-0.16 TREND CRESCITA (100 sopra 300 > 0.69) - r 7839"
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
                        sell = "SELL 3 da 60 a 90 min con ma50 < CUSCINO SANT' ANTONIO (5-100) MA SOLO con TREND CRESCITA (100 sopra 300 > 0.69) - r 7859"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.17
                        and ma2_last < ma2_2_min_ago
                        
                        and deviation_ma100_sopra_ma300 < 0.69
                        and deviation_sell < -0.16
                       
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 < con deviation_ma39 <-0.17 and deviation_sell < 0.10 TREND LATERALE (100>300 MA <0.69) - r 7874"
                        action = "sell"
                        
                        # 27 giu 2022 deviation_sell < -0.16 da 0.15
                        
                        
                        
                        
                    ###########################################################################################################

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.10
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < -0.10 - r 7888"
                        action = "sell"
                        
                        
                     
                    # maggiore perdita tollerata
                    
                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.20
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 < con deviation_ma39 <-0.20 and deviation_sell < 0.10 con > perdita tollerata - r 7903"
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
                        sell = "SELL 3 da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < 0.13 con > perdita tollerata - r 7923"
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
                        sell = "SELL 3 dopo 90 min con ma50> and deviation_ma25 <-0.18 (no ma3<ma39) - r 7944"
                        action = "sell"
                    
                    
                    
                    
                    elif (     
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.20 
                        and ma3_last < ma50_last
                    ):
                        sell = "SELL 3 dopo 90 min con ma50> and (deviation_sell < 0.10 and ma3_last < ma50_last)- r 7956"
                        action = "sell"
                        
                    
                    
                        
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.23
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 dopo 90 min con ma50> and deviation_ma25 < -0.23 - r 7968"
                        action = "sell"
                        
                
                    
                    
                    elif (     
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.23 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 dopo 90 min con ma50> and (deviation_sell < -0.23 and ma3_last < ma50_last) - r 7981"
                        action = "sell"
                        
                       
                        
                        
                        
                    ############################################################################################################################### 
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma39_last
                        and deviation_sell > 0.29 and deviation_sell < 0.59
                        and ma2_last < ma2_2_min_ago
                        and deviation_ma100_sopra_ma200 > 0.20
                       
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and 5-39 and deviation_sell 0.29 - 0.59 - FINTA ALLA MARADONA se sale tanto - r 7998"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma150_last
                        and deviation_sell > 0.25 and deviation_sell < 0.59
                        and ma2_last < ma2_2_min_ago
                        and deviation_ma100_sopra_ma200 < 0.20
                       
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and 5-150 (!) and deviation_sell 0.25 - 0.59 - FINTA ALLA MARADONA se sale poco - r 7999"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # al SELL 3 maradona e' ancora piu' stanco di quello che pensavo !
                        
                        
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma30_last
                        and deviation_sell > 0.60 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 >90 min con ma50 > con 4<30 and deviation_sell 0.60 - 0.90 DRIBBLING ALLA RONALDO - r 8013"
                        action = "sell"
                        
                        # 6 giu 2022 4-30 da 4-25
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 dopo 90 min con ma50 > incrocio 3-30 (!) and deviation_sell 0.91 - 1.49 - r 8026"
                        action = "sell"

                        # ma 3-48 mi evita la ricompra e la rivendita con perdita !
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 dopo 90 min con ma50 > incrocio 3-30 (!) and deviation_sell 1.50 - 2.70 - r 8041"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 dopo 90 min con ma50 > incrocio 3-11 (!) and deviation_sell > 2.71 - r 8054"
                        action = "sell"
                        
                 
                
                
                    ######################################################################################## con trend discendente
                    
                    
                    elif (      
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.20
                       
                    ):
                        sell = "SELL 3 dopo 90 min con ma50 < con deviation_ma39 < -0.20 - r 8069"
                        action = "sell"
                        
                        
                    elif (      
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma300_last
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.16
                       
                    ):
                        sell = "SELL 3 dopo 90 min con ma50 < con deviation_ma39 < -0.16 - r 8070"
                        action = "sell"
                        
                     
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 > 0.20
                        and ma2_last < ma2_2_min_ago 
                         
                        and ma3_last < ma39_last
                    ):
                        sell = "SELL 3 dopo 90 min con ma50< MA ma100 > ma300 and ma3_last < ma39_last - r 8082"
                        action = "sell"
                        
                        # se sta in alto NO DEVIATION SELL - la 100 se ne sta andando in alto.
                        
                        
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 < 0.20
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.15 
                        and ma3_last < ma39_last
                    ):
                        sell = "SELL 3 dopo 90 min con ma50 < and ma100 NON DISTANTE dalla ma300 and (deviation_sell < -0.15 and ma3_last < ma39_last) - r 8083"
                        action = "sell"
                        
                        # SE ma100 RESTA VICINA ALLA ma300 - trend laterale - allora tieniti pronto anche con la deviation sell
                        
                        
                        
                    
                    
                    
            #######################################################################################################
            
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
                        sell = "SELL 4-5-x (0-3 min) con ma50 > and 3<18 and deviation_sell < -0.33 - r 8106"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma25_prev and ma5_last < ma25_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 4-5-x SELL (0-3 min) con ma50 > and incrocio 5-25 and deviation_sell 0.25 - 0.56 MARADONA - r 8121"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma4_prev > ma20_prev and ma4_last < ma20_last)
                        and deviation_sell > 0.57 and deviation_sell < 0.79
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (0-3 min) con ma50 > and incrocio 4-20 and deviation_sell 0.57 - 0.79 RONALDO - r 8135"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 0.80 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell 0.80 - 1.20 - r 8147"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell > 1.21 (che sarebbe come IL DRIBBLING ALLA RONALDO !) - r 8160"
                        action = "sell"
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (0-3 min) con ma50 < and incrocio 3-28 - r 8173"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 - r 8186"
                        action = "sell"
                        
                        

                    # ---------------------------------------------------------------------------------------------------------------------- crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - r 8199"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - r 8213"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                        and deviation_sell > 0.60
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - r 8226"
                        action = "sell"
                        
                        

                ################################################################################################ sessione 3-4-x ( 3-7 min )

                # VENDITA - da 3 a 7 minuti = da 180 a 420 secondi

                elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 420:
                    
                    if (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma16_last
                        
                        and ma39_last > ma200_last
                        
                        and deviation_sell < -0.38
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 4-5-x (3-7 min) con ma50 >  and 39 > 200 and 3 < 16 and deviation_sell < -0.38 - r 8245"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma16_last
                        
                        and ma39_last < ma200_last
                        
                        and deviation_sell < -0.32
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 4-5-x (3-7 min) con ma50 > and 39 < 200 and 3 < 16 and deviation_sell < -0.32 - r 8246"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (3-7 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 8259"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 4-5-x (3-7 min) con ma50 > and 4<20 and deviation_sell 0.57 - 0.90 - DRIBBLING ALLA RONALDO - r 8274"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.40
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (3-7 min) con ma50 > and incrocio 3-20 and deviation_sell 0.91 - 1.40 - r 8288"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 1.41
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (3-7 min) con ma50 > and incrocio 3-15 and deviation_sell > 1.41 - r 8299"
                        action = "sell"
                        
                        
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 4-5-x (3-7 min) con ma50 < and incrocio 3-28 - r 8315"
                        action = "sell"
                        
                        # deviation_sell_ma78 = ma3_last / ma78_last
                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (3-7 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.23 - r 8330"
                        action = "sell"
                        
                        

                    # --------------------------------------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x GUADAGNO CON CROLLO (3-7 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - r 8343"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x PARACADUTE CROLLO (3-7 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 8354"
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
                        sell = "SELL 4-5-x (7-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - r 8375"
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
                        sell = "SELL 4-5-x (7-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - r 8392"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (7-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 8406"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                  
                    ):
                        sell = "SELL 4-5-x (7-12 min) con ma50 > and 4-20 and deviation_sell 0.57 - 0.90 - DRIBBLING ALLA RONALDO - r 8421"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 4-5-x (7-12 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - r 8436"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (7-12 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - r 8450"
                        action = "sell"
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (7-12 min) con ma50 < and incrocio 3-28 - r 8463"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (7-12 min) con ma50 < and incrocio 3-100 (cuscino di sant' antonio) - r 8476"
                        action = "sell"
                        
                        

                    # ------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x guadagno con crollo (7-12 min) con ma50 < and incrocio 3-23 - r 8489"
                        action = "sell"
                        
                        

                    # --------------------------------------------------------------------------------------------------- PARACADUTE crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x PARACADUTE CROLLO (7-12 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 8502"
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
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and incrocio 3-72 and deviation sell -0.65 e vaffanculo ! - r 8525"
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
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.36 - r 8542"
                        action = "sell"
                    
                        # viva sant' antonio !
                        # IMPORTANTE !   
                        # vai compaaaaaaaaaa
                        # poco guadagno ma piu' alta
                        # molto guadagno ma piu' bassa
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    #################################################################### and rapporto_delta_1_delta_2 > 1 and ma100_last > ma100_60_min_ago
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        
                        
                        and delta_1 < delta_2
                        and ma100_last > ma100_60_min_ago
                        
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA sopra rialzo rialzo - GIORNO - r 8560"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                        
                        
                    ########################################################################### DOPPIO DELTA<1 AND 100< TRAMONTO
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        
                        
                        and delta_1 > delta_2
                        and ma100_last > ma100_60_min_ago
                        
                        and ma3_last < ma50_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50>and 3-50 and dev_sell 0.25-0.56 - SOPRA RIBASSO RIALZO - CREPUSCOLO - FINTA ALLA MARADONA - r 8561"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        ###################################################################
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    
                    ######################################################## and rapporto_delta_1_delta_2 > 1 AND 100> SORGERE
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        
                        
                        and delta_1 < delta_2
                        and ma100_last > ma100_60_min_ago
                        
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and 4-20 e dev_sell 0.57 - 0.90 - SORGERE DRIBBLING ALLA RONALDO - GIORNO - r 8576"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                        
                        
                    ################################################################## and rapporto_delta_1_delta_2 < 1 TRAMONTO
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        
                        
                        and delta_1 > delta_2
                        and ma100_last > ma100_60_min_ago
                        
                        and deviation_ma100_sopra_ma200 > -0.10
                        and ma3_last < ma50_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and 3-50 and dev_sell 0.57 - 0.90 - DRIBBLING RONALDO sopra ribasso rialzo -CREPUSCOLO - r 8576"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # 100 DEVE STARE SOPRA 200 per non vendere durante il crollo con ma50
                        
                        ###############################################################
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - r 8591"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and incrocio 3-30 and deviation_sell > 1.21 - r 8605"
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
                        sell = "SELL 4-5-x (12-21 min) con ma50 < and deviation_ma39 < -0.17 - r 8625"
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
                        sell = "SELL 4-5-x (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - r 8645"
                        action = "sell"
                        
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50< !
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - r 8660"
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
                        sell = "SELL 4-5-x PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 8677"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                        
                  
                    # ----------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3 - 18 and deviation_sell > 0.23 - r 8693"
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
                        and deviation_ma25 < -0.29
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and deviation_ma25 < -0.29 - r 8716"
                        action = "sell"
                        
                     
                    
                    elif ( 
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.24 
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and (deviation_sell < -0.24 and ma3_last < ma50_last) - r 8728"
                        action = "sell"
                        
                     
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.30
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and deviation_ma25 < -0.30 - r 8740"
                        action = "sell"
                        
                       
                    
                    
                    elif (        
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.26 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and (deviation_sell < -0.26 and ma3_last < ma50_last) - r 8753"
                        action = "sell"
                        
                      
                        #############################################################################################################
                    

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.26
                        and ma2_last < ma2_2_min_ago
                  
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.26 - r 8767"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    #######################################################
                    
                    
                    # FINTA DI MARADONA
                    
                    ###################################################### and rapporto_delta_1_delta_2 > 1 AND 100> SORGERE
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        
                        
                        and delta_1 < delta_2
                        and ma100_last > ma100_60_min_ago
                        
                        and (ma5_prev > ma25_prev and ma5_last < ma25_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                   
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and incrocio 5-25 and deviation_sell 0.25 - 0.56 SOPRA RIALZO RIALZO - GIORNO - FINTA DI MARADONA - r 8781"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    ##################################################################### and rapporto_delta_1_delta_2 < 1 tramonto
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        
                        
                        and delta_1 > delta_2
                        and ma100_last > ma100_60_min_ago
                        
                        and deviation_ma100_sopra_ma200 > -0.10
                        and (ma3_prev > ma50_prev and ma3_last < ma50_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                   
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50> and incrocio 5-25 and dev_sell 0.25-0.56 FINTA MARADONA SOPRA RIBASSO RIALZO-CREPUSCOLO- r 8782"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # 100 deve stare sopra 200 per non vendere con ma50 durante il crollo.
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    # tra MARADONA e RONALDO ho messo POCHI MALEDETTI E SUBITO se alla fine del trend da' una botta rialzista
                    
                    elif (
                        ma3_last < ma13_last
                        and ma200_last > ma200_60_min_ago
                        and deviation > 0.68
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (21-60 min) SOLO QUI tra MARADONA e RONALDO ho messo POCHI MALEDETTI E SUBITO 11-13 ( solo quando ma200 > ) - riga 8931"
                        action = "sell"
                        
                        
                        
                    
                    
                    
                    
                    
                    
                    # FINTA ALLA RONALDO
                    
                    
                    ######################################################################## and rapporto_delta_1_delta_2 > 1 AND 100> SORGERE
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        
                        
                        and delta_1 < delta_2
                        and ma100_last > ma100_60_min_ago
                        
                        and ma3_last < ma28_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and 3-28 (no incrocio 3-15) and deviation_sell 0.57 - 0.90 FINTA ALLA RONALDO - GIORNO - r 8796"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    ######################################################## and rapporto_delta_1_delta_2 < 1 tramonto
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        
                        
                        and delta_1 > delta_2
                        and ma100_last > ma100_60_min_ago
                        
                        and deviation_ma100_sopra_ma200 > -0.10
                        and ma3_last < ma50_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and 3-50 (no incrocio 3-15) e deviation_sell 0.57-0.90 FINTA ALLA RONALDO - CREPUSCOLO - r 8797"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # 100 dee stare sopra 200 per non vendere con ma50 durante il crollo o un grande ribasso
                        
                        
                        
                        ###################################################################################################
                        
                        
                        
                        
                        
                        
                        
                        
                        
                      
                    

                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma20_last
                        and deviation_sell > 0.91 and deviation_sell < 1.40
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and 3-20 and deviation_sell 0.91 - 1.40 - r 8812"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma25_last
                        and deviation_sell > 1.41 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and 3-25 and deviation_sell 1.41 -2.70 - r 8826"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and incrocio 3-13 and deviation_sell > 2.71 - r 8838"
                        action = "sell"
                    
                    
                    
                    ################################################################################################# con trend discendente
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma50_last > ma100_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.29
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x RAFFORZATA (21-60 min) con ma50 < and deviation_ma39 < -0.29 - r 8852"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma50_last < ma100_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.28
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and deviation_ma39 < -0.28 - r 8853"
                        action = "sell"
                        
                        
                    
                    
                    
                    
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma50_last > ma100_last
                        and ma100_last > ma200_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.29
                        and ma3_last < ma39_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x RAFFORZATA (21-60 min) con ma50 < and deviation_sell < 0.32 100>200 !- r 8863"
                        action = "sell"
                        
                        
                        
                        
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma50_last > ma100_last
                        and ma100_last < ma200_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.29
                        and ma3_last < ma39_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x RAFFORZATA (21-60 min) con ma50 < and deviation_sell < 0.29 100<200 - r 8864"
                        action = "sell"
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma50_last < ma100_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.28
                        and ma3_last < ma39_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and deviation_sell < 0.28 - r 8865"
                        action = "sell"
                        
                        
                        
                        
                        
                        
                        
              
            
            
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_60_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.37
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - r 8877"
                        action = "sell"
                    
                    
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_60_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - r 8890"
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
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and deviation_ma39 < -0.26 - r 8909"
                        action = "sell"
                        
                 
                    
                    
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.33
                        and ma3_last < ma39_last
                        and ma200_last > ma200_60_min_ago
                        and ma300_last > ma300_120_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and 200> 60 min and 300 > 120 min and deviation_sell < -0.33 - r 8921"
                        action = "sell"
                        
                        
                        
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.28
                        and ma3_last < ma39_last
                        and ma200_last > ma200_60_min_ago
                        and ma300_last < ma300_120_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and 200> 60 min and 300 < 120 min and deviation_sell < -0.28 - r 8922"
                        action = "sell"
                        
              
                    
                
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma200_60_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.39
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.39 - r 8933"
                        action = "sell"
                        
                        
                  
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma200_60_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.29
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and INCROCIO 5-100 (no 5<100) and deviation_sell < -0.29  CUSCINO DI SANT' ANTONIO - r 8946"
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
                        sell = "SELL 4-5-x eventuale guadagno durante il crollo (21-60 min) con ma50 < incrocio 3 - 18 and deviation_sell > 0.23 - r 8964"
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
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > and deviation_ma25 < -0.19 - r 8991"
                        action = "sell"
                        
                        
                    
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.21 
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > and (deviation_sell < -0.19 and ma3_last < ma50_last) - r 9003"
                        action = "sell"
                        
                        
                        
                        
                    elif ( 
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.25
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > and deviation_ma25 < -0.25 - r 9015"
                        action = "sell"
                        
                        
                        
                    
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.24 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > and (deviation_sell < -0.24 and ma3_last < ma50_last) - r 9028"
                        action = "sell"
                        
                        
                        
                        
                        #########################################################################################################################
                        
                      
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma25_prev and ma5_last < ma25_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and incrocio 5-25 and deviation_sell 0.25 - 0.56 FINTA DI MARADONA - r 9045"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x >60 min con ma50> and 4-20 and deviation_sell 0.57-0.90 DRIBBLING ALLA RONALDO - r 9059"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > and incrocio 3-30 and deviation_sell 0.91 - 1.49 - r 9072"
                        action = "sell"

                        # ma ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > incrocio 3-25 and deviation_sell 1.50 - 2.70 - r 9087"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > incrocio 3-13 and deviation_sell > 2.71 - r 9100"
                        action = "sell"
                        
                    
                    
                    
                    ######################################################################################## con trend discendente
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 < con deviation_ma39 <-0.18 and deviation_sell < 0.10 (no ma3<ma33) (NO INCROCIO!) - r 9115"
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
                        and deviation_sell < -0.07
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < -0.07 meno tollerante (sta in alto) - r 9137"
                        action = "sell"
                        
                        
                        
                        
                    # sta in basso e, PARADOSSALMENTE, sta piu' calmo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 < 0.25
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.19
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < -0.19 piu' tollerante (sta in basso) - r 9153"
                        action = "sell"
                        
                        

                ############################################################################################################ sessione 3-4-x ( > 90 min )

                # VENDITA - da 90 minuti in poi = da 5400 secondi in poi

                elif seconds_since_last_trade > 5400:
                    
                    
                    
                    # ################################################################################ RIGHE DEL COMPA DA RADDOPPIARE PER AUMENTARE TOLLERANZA
                    
                    
                    if (    
                        ma50_last > ma50_2_min_ago
                        and ma50_last > ma100_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.28
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x dopo 90 min con ma50> and deviation_ma25 <-0.28 ( no ma3 < ma39 ) - r 9172"
                        action = "sell"
                        
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and ma50_last < ma100_last
                        
                        and ma2_last < ma2_2_min_ago
                        and deviation_ma25 < -0.29
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x RAFFORZATO dopo 90 min con ma50> and deviation_ma25 <-0.29 ( no ma3 < ma39 ) - r 9173"
                        action = "sell"
                        
                      
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (     
                        ma50_last > ma50_2_min_ago
                        and ma50_last > ma100_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.29
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x RAFFORZATO dopo 90 min con ma50> and (deviation_sell < -0.29 and ma3_last < ma50_last) - r 9186"
                        action = "sell"
                        
                        
                        
                        
                    elif (     
                        ma50_last > ma50_2_min_ago
                        and ma50_last < ma100_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.28
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x dopo 90 min con ma50> and (deviation_sell < -0.28 and ma3_last < ma50_last) - r 9187"
                        action = "sell"
                        
                      
                        
                    
                    
                    
                    
                    
                    
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and ma50_last > ma100_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.31
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x RAFFORZATO dopo 90 min con ma50> and deviation_ma25 < -0.31 TOLLERANTE - r 9198"
                        action = "sell"
                        
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and ma50_last < ma100_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.30
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x dopo 90 min con ma50> and deviation_ma25 < -0.30 TOLLERANTE - r 9199"
                        action = "sell"
                        
                        
                        
                        
                        
                        
                        
                    elif (     
                        ma50_last > ma50_2_min_ago
                        and ma50_last > ma100_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.32
                        
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x RAFFORZATO dopo 90 min con ma50> and (deviation_sell < -0.32 and ma3_last < ma50_last) TOLLERANTE - r 9211"
                        action = "sell"
                        
                        
                        
                    elif (     
                        ma50_last > ma50_2_min_ago
                        and ma50_last < ma100_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.31
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x dopo 90 min con ma50> and (deviation_sell < -0.31 and ma3_last < ma50_last) TOLLERANTE - r 9212"
                        action = "sell"
                        
                        
                        
                        #############################################################################################################################
                       
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 9226"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x >90 min con ma50 > con 4 < 20 and deviation_sell 0.35 - 0.90 FINTA ALLA RONALDO - r 9240"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x dopo 90 min con ma50 > incrocio 3-30 (!) and deviation_sell 0.91 - 1.49 - r 9252"
                        action = "sell"

                        # ma 3-48 mi evita la ricompra e la rivendita con perdita !
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x dopo 90 min con ma50 > incrocio 3-25 (!) and deviation_sell 1.50 - 2.70 - r 9267"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x dopo 90 min con ma50 > incrocio 3-13 (!) and deviation_sell > 2.71 - r 9288"
                        action = "sell"
                        
                        

                    ######################################################################################## con trend discendente
                    
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.215
                    ):
                        sell = "SELL 4-5-x dopo 90 min con ma50 < con deviation_ma39 <-0.215 - r 9294"
                        action = "sell"
                        
                        
                        
                    
                     
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.21 
                        and ma3_last < ma39_last
                    ):
                        sell = "SELL 4-5-x dopo 90 min con ma50 < and (deviation_sell < 0.10 and ma3_last < ma39_last) - r 9307"
                        action = "sell"
                        
                    
                    
                    
            #################################################################################################################### VENDITE SPECIALI !
            ####################################################################################
            ####################################################################################
                    
            # ATTENZIONE al conflitto durante il crollo - SELL SOVRAPPOSTO AL BUY

            # NO 3<78 !
            # NO deviation 78 !
            # QUALCHE VOLTA ma3-ma39 NON HANNO INCROCIATO allora per la vendita con il DRIBBLING e il DOPPIO PASSO ALLA RONALDO ho risolto con 3 < 39
            # il CUSCINO DELL' ANGELO CUSTODE e di SANT' ANTONIO mi proteggono ! (vendita con medie lunghe)
                    
          
            
            
            
            
            
            
            ####################################################################################### SALVAGENTE con deviation_ma5_sotto_ma200 > -1.00
            
            # SENZA and ma2_last < ma2_2_min_ago VENDE mentre ma4 si trova sotto il BUY !
            
            
            # 1 - SELL condizione speciale ro cano VENDE CON UN SALVAGENTE con deviation_ma5_sotto_ma200 > -1.00
            
            if (
                deviation_ma39 < -0.25
                and deviation_sell < -0.32
                and ma2_last < ma2_2_min_ago
                
                and ma50_last > ma50_2_min_ago
                and deviation_ma100_sopra_ma300 > 0.40
                
                and deviation_ma5_sotto_ma200 > -1.00
            ):
                sell = "SELL condizione speciale SALVAGENTE 1 3-39 con ma50 > - con deviation_ma5_sotto_ma200 > -1.00 - r 9335"
                action = "sell"
                
                # 14 giu 2022 deviation_sell -0.32
                

                
                
          
            
            # 2 - SELL condizione speciale ro cano VENDE CON UN SALVAGENTE con deviation_ma5_sotto_ma200 > -1.00   
            
            elif (
                deviation_ma39 < -0.25
                and deviation_sell < -0.34
                and ma2_last < ma2_2_min_ago 
                
                and ma50_last > ma50_2_min_ago
                and deviation_ma100_sopra_ma300 < 0.40
                
                and deviation_ma5_sotto_ma200 > -1.00
            ):
                sell = "SELL condizione speciale SALVAGENTE 2 3-39 con ma50 > - con deviation_ma5_sotto_ma200 > -1.00 and deviation < -0.34 - r 9353"
                action = "sell"   
                

                # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !)
                
                
         
            # 3 - SELL condizione speciale ro cano VENDE CON UN SALVAGENTE con deviation_ma5_sotto_ma200 > -1.00
            
            elif (
                deviation_ma39 < -0.25
                and deviation_sell < -0.305
                and ma2_last < ma2_2_min_ago 
                
                and ma50_last < ma50_2_min_ago
                and deviation_ma100_sopra_ma300 > 0.40
                
                and deviation_ma5_sotto_ma200 > -1.00
            ):
                sell = "SELL condizione speciale SALVAGENTE 3 3-39 < -0.25 e dev < -0.31 and dev_sell < -0.305 con ma50 < - con dev_ma5_sotto_ma200 > -1.00 - r 9372 A"
                action = "sell"
                
                # 27 giu 2022 dev sell a 0.305 da 0.31
                
                
                # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !)
                
                # 21 giugno 2022 RICORDO TREMENDO 9372 ha venduto a -2.23% !!!
                # COME PRIMA COSA HO NOTATO CHE AVEVA DEVIATION INVECE DI DEVIATON SELL 
                # ma non sapendo se era questo il problema ho creato la prossima condizione speciale.
                
                
                
                
            # 4 - SELL ricordo terribile del 21 giugno 2022
            
            elif (
                
                ma3_last < ma100_last
                and deviation_sell < -0.69
                and deviation_ma100_sopra_ma300 > 0.20
                and ma2_last < ma2_2_min_ago 
             
            ):
                sell = "SELL 21 giugno 2022 - deviation_sell < -0.69 - r 9372 Ba"
                action = "sell"   
             
                # 21 giugno 2022 RICORDO TERRIBILE del 21 giugno 2022 !  9372 A ha venduto a -2.23% !!!
                
                
                
            # 4 - SELL ricordo terribile del 21 giugno 2022
            
            elif (
                
                ma3_last < ma100_last
                and deviation_sell < -0.68
                and deviation_ma100_sopra_ma300 < 0.20
                and ma2_last < ma2_2_min_ago 
             
            ):
                sell = "SELL 21 giugno 2022 - deviation_sell < -0.68 - r 9373 Bb"
                action = "sell"   
             
                # 21 giugno 2022 RICORDO TERRIBILE del 21 giugno 2022 !  9372 A ha venduto a -2.23% !!!
                
                
            
                
            # 5 - SELL condizione speciale ro cano VENDE CON UN SALVAGENTE con deviation_ma5_sotto_ma200 > -1.00
            
            elif (
                deviation_ma39 < -0.27
                and deviation_sell < -0.315
                and ma2_last < ma2_2_min_ago 
                
                and ma50_last < ma50_2_min_ago
                and deviation_ma100_sopra_ma300 < 0.40
                
                and deviation_ma5_sotto_ma200 > -1.00
            ):
                sell = "SELL condizione speciale SALVAGENTE 4 deviation 3-39 <-0.27 and deviation <-0.315 - con ma50 < e con ma5 sotto ma200 > -1.00 - r 9390"
                action = "sell"   
                

                # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!
                # modifica solo devation.
                
                
                
                
                #########################################################################################################################
                
                
                
                
                
            
            
            
            ############################################################################## SALVAGENTE con deviation_ma5_sotto_ma200 < -1.00 and > -1.50
            
            
            
            # 6 - SELL condizione speciale ro cano VENDE CON UN SALVAGENTE con deviation_ma5_sotto_ma200 < -1.00 and > -1.50
            
            elif (
                deviation_ma39 < -0.25
                and deviation_sell < -0.40
                
                and ma50_last > ma50_2_min_ago
                and deviation_ma100_sopra_ma300 > 0.40
                
                and deviation_ma5_sotto_ma200 < -1.00
                and deviation_ma5_sotto_ma200 > -1.50
                
                and ma2_last < ma2_2_min_ago 
            ):
                sell = "SELL condizione speciale SALVAGENTE 1 3-39 con ma50 > - con deviation_ma5_sotto_ma200 < -1.00 and > -1.50 - r 9395"
                action = "sell"   
                

                # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!
                
          
            
            # 7 - SELL condizione speciale ro cano VENDE CON UN SALVAGENTE con deviation_ma5_sotto_ma200 < -1.00 and > -1.50   
            
            elif (
                deviation_ma39 < -0.25
                and deviation_sell < -0.40
                
                and ma50_last > ma50_2_min_ago
                and deviation_ma100_sopra_ma300 < 0.40
                
                and deviation_ma5_sotto_ma200 < -1.00
                and deviation_ma5_sotto_ma200 > -1.50
                
                and ma2_last < ma2_2_min_ago 
            ):
                sell = "SELL condizione speciale SALVAGENTE 2 3-39 con ma50 > - con deviation_ma5_sotto_ma200 < -1.00 and > -1.50 - r 9396"
                action = "sell"   
                

                # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!
                
         
            
            # 8 - SELL condizione speciale ro cano VENDE CON UN SALVAGENTE con deviation_ma5_sotto_ma200 < -1.00 and > -1.50
            
            elif (
                deviation_ma39 < -0.25
                and deviation_sell < -0.40
                
                and ma50_last < ma50_2_min_ago
                and deviation_ma100_sopra_ma300 > 0.40
                
                and deviation_ma5_sotto_ma200 < -1.00
                and deviation_ma5_sotto_ma200 > -1.50
                
                and ma2_last < ma2_2_min_ago 
                
            ):
                sell = "SELL condizione speciale SALVAGENTE 3 3-39 con ma50 < - con deviation_ma5_sotto_ma200 < -1.00 and > -1.50 - r 9397"
                action = "sell"   
                

                # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!
                
                
                
                
                
            
            # 9 - SELL condizione speciale ro cano VENDE CON UN SALVAGENTE con deviation_ma5_sotto_ma200 < -1.50 CROLLO !
            
            elif (
                
                deviation_sell < -0.50
                and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                
                and ma50_last < ma50_2_min_ago
                and deviation_ma100_sopra_ma300 < 0.40
                
                and deviation_ma5_sotto_ma200 < -1.50
                
            ):
                sell = "SELL condizione speciale SALVAGENTE 4C 3-39 con ma50 < - con deviation_ma5_sotto_ma200 < -1.50 CROLLO ! - r 9398 A"
                action = "sell"   
                

                # DEVIATION 3-39 FACEVA USCIRE PUNTO ROSSO SOVRAPPOSTO AL PUNTO VERDE PERCHE' NEL CROLLO 3 ERA SOTTO 39 ( E NON POTEVANO NEANCHE INCROCIARE)
                # 
                
                
                
                
            # 10 - SELL condizione speciale ro cano VENDE CON UN SALVAGENTE con deviation_ma5_sotto_ma200 < -1.00 and > -1.50 GRANDE RIBASSO !
            
            elif (
                ma2_last < ma2_2_min_ago
                and deviation_sell < -0.36
                and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                
                and ma50_last < ma50_2_min_ago
                and deviation_ma100_sopra_ma300 < 0.40
                
                and deviation_ma5_sotto_ma200 < -1.00
                and deviation_ma5_sotto_ma200 > -1.50
                
                
                
            ):
                sell = "SELL condizione speciale SALVAGENTE 4 3-13 con ma50 < e con deviation_ma5_sotto_ma200 < -1.00 and > -1.50 GRANDE RIBASSO ! - r 9398 B"
                action = "sell"
                
                # co deviation 3-39 NELLA PRESENTE SITUAZIONE CROLLO 3 SOTTO 39 E PARTIVA IL PUNTO ROSSO SOVRAPPOSTO AL PUNTO VERDE
                

                
                
                
                
                #####################################################################################################################################
                
                
                
                
                
                
                
                
                
                
                
            ##################################################################################### SALVAGENTE con deviation_ma5_sotto_ma200 < -1.50
            
            
            
            # 11 - SELL condizione speciale ro cano VENDE CON UN SALVAGENTE con deviation_ma5_sotto_ma200 < -1.50
            
            elif (
                deviation_ma39 < -0.25
                and deviation_sell < -0.50
                
                and ma50_last > ma50_2_min_ago
                and deviation_ma100_sopra_ma300 > 0.40
                
                and deviation_ma5_sotto_ma200 < -1.50
            ):
                sell = "SELL condizione speciale SALVAGENTE 1C 3-39 con ma50 > - con deviation_ma5_sotto_ma200 < -1.50 - r 9399"
                action = "sell"   
                

                # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!
                
          
            
            # 12 - SELL condizione speciale ro cano VENDE CON UN SALVAGENTE con deviation_ma5_sotto_ma200 < -1.50   
            
            elif (
                deviation_ma39 < -0.25
                and deviation_sell < -0.50
                
                and ma50_last > ma50_2_min_ago
                and deviation_ma100_sopra_ma300 < 0.40
                
                and deviation_ma5_sotto_ma200 < -1.50
                
            ):
                sell = "SELL condizione speciale SALVAGENTE 2C 3-39 con ma50 > - con deviation_ma5_sotto_ma200 < -1.50 - r 9400"
                action = "sell"   
                

                # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!
                
         
            
            
            
            
            
            # 13 - SELL condizione speciale ro cano VENDE CON UN SALVAGENTE con deviation_ma5_sotto_ma200 < -1.50
            
            elif (
                deviation_ma39 < -0.25
                and deviation_sell < -0.53
                and ma100_last > ma100_60_min_ago
                
                and ma50_last < ma50_2_min_ago
                and deviation_ma100_sopra_ma300 > 0.40
                
                and deviation_ma5_sotto_ma200 < -1.50
                
            ):
                sell = "SELL condizione speciale SALVAGENTE 3C 3-39 con ma50 < - con deviation_ma5_sotto_ma200 < -1.50 - r 9401a"
                action = "sell"   
                

                # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!
                # 14 giu 2022 -0.52 da 0.50
                # 15 giu 2022 -0.53 da 0.52
                
                
                
                
            # 14 - SELL condizione speciale ro cano VENDE CON UN SALVAGENTE con deviation_ma5_sotto_ma200 < -1.50
            
            elif (
                deviation_ma39 < -0.25
                and deviation_sell < -0.52
                and ma100_last < ma100_60_min_ago
                
                and ma50_last < ma50_2_min_ago
                and deviation_ma100_sopra_ma300 > 0.40
                
                and deviation_ma5_sotto_ma200 < -1.50
                
            ):
                sell = "SELL condizione speciale SALVAGENTE 3C 3-39 con ma50 < - con deviation_ma5_sotto_ma200 < -1.50 - r 9401b"
                action = "sell"   
                

                # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!
                # 14 giu 2022 -0.52 da 0.50
                
                
                
                
            
                
            
                
                
                
                ##################################################################################################################### fine salvagente
                
                
              
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            ################################################################################################################## CROLLO IMPROVVISO !
            
            
            
            # 15 - SELL condizione speciale ro cano VENDE DURANTE UN CROLLO IMPROVVISO ! and deviation_ma5_sotto_ma200 > -1.00
            
            elif (
                ma2_last < ma4_last
                and ma2_last < ma6_last
                and deviation_sell < -0.58
                
                and deviation_ma5_sotto_ma200 > -1.00
            ):
                  
                sell = "SELL condizione speciale CROLLO IMPROVVISO - and deviation_ma5_sotto_ma200 > -1.00 - r 9399"
                action = "sell"
            
                # con -0.59 il 6 feb 2022 ha fatto -0.85
                # con -0.62 il 4 feb 2022 ha fatto -0.89%
                # deviation = ma4_last / last_trade_price

                # FORSE E' L' UNICA DEVIATION CHE MI POTRA' SALVARE DA UN CROLLO IMPROVVISO COME QUELLO DEL 3 NOVEMBRE 2021
                
                
                
                
                
                
            # 16 - SELL condizione speciale ro cano VENDE DURANTE UN CROLLO IMPROVVISO ! and deviation_ma5_sotto_ma200 < -1.00
            
            elif (
                ma2_last < ma4_last
                and ma2_last < ma6_last
                and deviation_sell < -0.60
                
                and deviation_ma5_sotto_ma200 < -1.00
            ):
                  
                sell = "SELL condizione speciale CROLLO IMPROVVISO - and deviation_ma5_sotto_ma200 < -1.00 - r 9400"
                action = "sell"
            
                # con -0.59 il 6 feb 2022 ha fatto -0.85
                # con -0.62 il 4 feb 2022 ha fatto -0.89%
                # deviation = ma4_last / last_trade_price

                # FORSE E' L' UNICA DEVIATION CHE MI POTRA' SALVARE DA UN CROLLO IMPROVVISO COME QUELLO DEL 3 NOVEMBRE 2021
                
                
                
                
                ##################################################################################################################### fine crollo improvviso
                
                
                
                
                
            
            
            
            
            
            
            
            ################################################################################################ dopo crollo improvviso del 24 aprile 2022
            
            # 17 - SELL condizione speciale dopo crollo improvviso del 24 aprile 2022 ! and deviation_ma5_sotto_ma200 > -1.00
                    
            elif (    
                ma2_last < ma4_last
                and ma2_last < ma6_last
                and ma33_last > ma78_last
                
                and delta_1_200_30 < delta_2_200_30_30_min
                
                and deviation_crollo_24_aprile < -0.56
                
                and deviation_ma5_sotto_ma200 > -1.00
            ): 
                
                sell = "SELL condizione speciale DOPO CROLLO IMPROVVISO del 24 aprile 2022 - and dev_ma5_sotto_ma200 > -1.00 - (-0.57) giorno E 33>78 - r 9401 a1"
                action = "sell"
                        
                # ho aggiunto anche questa vendita speciale dopo il 24 aprile -1%
                # deviation_crollo_24_aprile = ma2_last / last_trade_price        
                # -0.58 ha generato perdita -0.82 il 10 maggio 2022 cosi' ho ridotto a -0.575
                # -0.575 ha generato perdita -1.12 il 10 maggio 2022 cosi' ho ridotto a -0.57
                # -0.57 ha generato perdita -1.37 il 12 maggio 2022 cosi' ho ridotto a -0.56
                # -0.56 ha generato perdita -1.19 il 13 maggio 2022 cosi' ho ridotto a -0.55
                # MA VA BENE !
                # con delta_1_200_30 < delta_2_200_30_30_min ho aumentato a -0.56
                
                # 21 giu 2022 a -0.56 da -0.57
                
                
                
            # 18 - SELL condizione speciale dopo crollo improvviso del 24 aprile 2022 ! and deviation_ma5_sotto_ma200 > -1.00
                    
            elif (    
                ma2_last < ma4_last
                and ma2_last < ma6_last
                and ma33_last < ma78_last
                
                and delta_1_200_30 < delta_2_200_30_30_min
                
                and deviation_crollo_24_aprile < -0.56
                
                and deviation_ma5_sotto_ma200 > -1.00
            ): 
                
                sell = "SELL condizione speciale DOPO CROLLO IMPROVVISO del 24 aprile 2022 - and dev_ma5_sotto_ma200 > -1.00 - (-0.56) giorno MA 33<78 - r 9401 a2"
                action = "sell"
                        
                # ho aggiunto anche questa vendita speciale dopo il 24 aprile -1%
                # deviation_crollo_24_aprile = ma2_last / last_trade_price        
                # -0.58 ha generato perdita -0.82 il 10 maggio 2022 cosi' ho ridotto a -0.575
                # -0.575 ha generato perdita -1.12 il 10 maggio 2022 cosi' ho ridotto a -0.57
                # -0.57 ha generato perdita -1.37 il 12 maggio 2022 cosi' ho ridotto a -0.56
                # -0.56 ha generato perdita -1.19 il 13 maggio 2022 cosi' ho ridotto a -0.55
                # MA VA BENE !
                # con delta_1_200_30 < delta_2_200_30_30_min ho aumentato a -0.56
                
                
                
                
                
            # 19 - SELL condizione speciale dopo il crollo improvviso del 24 aprile 2022 ! and deviation_ma5_sotto_ma200 > -1.00
                    
            elif (    
                ma2_last < ma4_last
                and ma2_last < ma6_last
                and delta_1_200_30 > delta_2_200_30_30_min
                
                and deviation_crollo_24_aprile < -0.55
                
                and deviation_ma5_sotto_ma200 > -1.00
            ): 
                
                sell = "SELL condizione speciale DOPO IL CROLLO IMPROVVISO del 24 aprile 2022 - and deviation_ma5_sotto_ma200 > -1.00 - (-0.56) notte - r 9401 b"
                action = "sell"
                        
                # ho aggiunto anche questa vendita speciale dopo il 24 aprile -1%
                # deviation_crollo_24_aprile = ma2_last / last_trade_price        
                # -0.58 ha generato perdita -0.82 il 10 maggio 2022 cosi' ho ridotto a -0.575
                # -0.575 ha generato perdita -1.12 il 10 maggio 2022 cosi' ho ridotto a -0.57
                # -0.57 ha generato perdita -1.37 il 12 maggio 2022 cosi' ho ridotto a -0.56
                # -0.56 ha generato perdita -1.19 il 13 maggio 2022 cosi' ho ridotto a -0.55
                # MA VA BENE !
                
                
            
            
            
            
            
            
            # 20 - SELL condizione speciale dopo il crollo improvviso del 24 aprile 2022 ! and deviation_ma5_sotto_ma200 < -1.00
                    
            elif (    
                ma2_last < ma4_last
                and ma2_last < ma6_last
                and deviation_crollo_24_aprile < -0.60
                
                and delta_1 < delta_2
                and deviation_ma5_sotto_ma200 < -1.00
            ): 
                
                sell = "SELL condizione speciale DOPO IL CROLLO IMPROVVISO del 24 aprile 2022 - and delta_1 < delta_2 and dev_ma5_sotto_ma200 < -1.00 - r 9402a"
                action = "sell"
                        
                # ho aggiunto anche questa vendita speciale dopo il 24 aprile -1%
                # deviation_crollo_24_aprile = ma2_last / last_trade_price        
                # -0.58 ha generato perdita -0.82 il 10 maggio 2022 cosi' ho ridotto a -0.575
                # -0.575 ha generato perdita -1.12 il 10 maggio 2022 cosi' ho ridotto a -0.57
                
                # -0.60 ha generato perdita -0.84 il 13 maggio 2022 cosi' ho ridotto a -0.59
                # MA VA BENE !
                
                
                
            # 21 - SELL condizione speciale dopo il crollo improvviso del 24 aprile 2022 ! and deviation_ma5_sotto_ma200 < -1.00
                    
            elif (    
                ma2_last < ma4_last
                and ma2_last < ma6_last
                and deviation_crollo_24_aprile < -0.59
                
                and delta_1 > delta_2
                and deviation_ma5_sotto_ma200 < -1.00
            ): 
                
                sell = "SELL condizione speciale DOPO IL CROLLO IMPROVVISO del 24 aprile 2022 - and delta_1 > delta_2 and dev_ma5_sotto_ma200 < -1.00 - r 9402b"
                action = "sell"
                        
                # ho aggiunto anche questa vendita speciale dopo il 24 aprile -1%
                # deviation_crollo_24_aprile = ma2_last / last_trade_price        
                # -0.58 ha generato perdita -0.82 il 10 maggio 2022 cosi' ho ridotto a -0.575
                # -0.575 ha generato perdita -1.12 il 10 maggio 2022 cosi' ho ridotto a -0.57
                
                # -0.60 ha generato perdita -0.84 il 13 maggio 2022 cosi' ho ridotto a -0.59
                # MA VA BENE !
                
                
                
                
                ######################################################################################### fine dopo il crollo improvviso del 24 aprile 2022
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            # 22 - SELL condizione speciale RIBASSO IMPROVVISO con deviation_sell < -0.60
            
            elif (
                ma78_last > ma78_2_min_ago
                and deviation_ribasso_improvviso < -0.63
                and deviation_evita_ribasso_improvviso_crollo_ferrari > -0.62
                and deviation_sell < -0.60
            ):
                sell = "SELL condizione speciale RIBASSO IMPROVVISO - r 9558"
                action = "sell"
                    
                # IMPORTANTISSIMO ! PREZZO / ma30 FACEVA VENDERE IMMEDIATAMENTE DURANTE IL CROLLO FERRARI !
                # perche' il prezzo era OVVIAMENTE molto distante dalla ma30
                # cosi' ho aggiunto la deviation che dice che se ma3 e' piu' giu' della ma30 IL RIBASSO IMPROVVISO NON E' GIA' PIU' !
                # INTERVERRANNO ALTRE CONDIZIONI
                # ho dovuto mettere and deviation_sell < -0.30 (ha fatto vendita strana con -0.20 ore 00:10 del 9 maggio 2022)
                
                
                
            
            
            # 23 - SELL condizione speciale RIBASSO IMPROVVISO con deviation_sell < -0.60
            
            elif (
                ma78_last < ma78_2_min_ago
                and deviation_ribasso_improvviso < -0.63
                and deviation_evita_ribasso_improvviso_crollo_ferrari > -0.62
                and deviation_sell < -0.60
            ):
                sell = "SELL condizione speciale RIBASSO IMPROVVISO - r 9576"
                action = "sell"
                
                # IMPORTANTISSIMO ! PREZZO / ma30 FACEVA VENDERE IMMEDIATAMENTE DURANTE IL CROLLO FERRARI !
                # prezzo molto distante dalla ma30
                # cosi' ho aggiunto la deviation che dice che se ma3 e' piu' giu' della ma30 IL RIBASSO IMPROVVISO NON E' GIA' PIU' !
                # INTERVERRANNO ALTRE CONDIZIONI    
                # anche qua ho dovuto mettere and deviation_sell < -0.18    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            # 24 - SELL condizione speciale ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma100 > e ma13 >
           
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and deviation_sell < -0.39
                and ma2_last < last_trade_price
                
                and ma100_last > ma100_30_min_ago
                and ma13_last > ma13_2_min_ago
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL condizione speciale DOLCE ATTESA con ma100 > e ma13 > and deviation < -0.39 - r 9448"
                action = "sell"
                
            
            
            
            # 25 - SELL condizione speciale ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma100 > e ma13 <
            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and deviation_sell < -0.37
                and ma2_last < last_trade_price
                
                and ma100_last > ma100_30_min_ago
                and ma13_last > ma13_2_min_ago
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL condizione speciale DOLCE ATTESA con ma100 > e ma13 < and deviation < -0.37 - r 9465"
                action = "sell"
                
            
            
            
            # 26 - SELL condizione speciale ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma100 < e con ma13 > 
            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and deviation_sell < -0.41
                and ma2_last < last_trade_price
                
                and ma100_last < ma100_30_min_ago
                and ma13_last > ma13_2_min_ago
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL condizione speciale DOLCE ATTESA con ma100 < e con ma13 > and deviation < -0.41 - r 9482"
                action = "sell"
                
            
            
            
            
            
            
            
            
            
            
            
            
            # 27 - SELL condizione speciale ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma100 < e con ma13 < ( and 20 > 100 )
            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and deviation_sell < -0.355
                
                and ma20_last > ma100_last
                
                and ma100_last < ma100_30_min_ago
                and ma13_last > ma13_2_min_ago
                and ma2_last < last_trade_price
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL condizione speciale DOLCE ATTESA con ma100 < e con ma13 < and dev_sell < -0.355 ( and 20 > 100 )- r 9499"
                action = "sell"
                
            
            
            
            
            
            
            
            
            
            
            # 28 - SELL condizione speciale ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma100 < e con ma13 < ( and 20 < 100 )
            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and deviation_sell < -0.39
                
                and ma20_last < ma100_last
                and ma300_last > ma300_120_min_ago
                
                and ma100_last < ma100_30_min_ago
                and ma13_last > ma13_2_min_ago
                and ma2_last < last_trade_price
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL condizione speciale DOLCE ATTESA 300 > con ma100 < e con ma13 < and deviation < -0.39 ( and 20 < 100 ) - r 9500 a"
                action = "sell"

                # il fattore tempo - la dolce attesa - solo con trend ribassista
                # deviation = ma2_last / last_trade_price
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                # max_hold_time_in_seconds = 300 = 5 min (con 6 min perdita di 0.90 %)
                
                # IMPORTANTE ! HO deviation < -0.355 MA VENDE CON SOLI - 0.25 cosi' ovviamente e' impossibile !
                # allora ho provato con un rafforzativo and ma20_last < ma100_last
                # per distinguerla da quella precedente che aveva dato il problema. ( e che ha and ma20_last < ma100_last )
                
                
                
                
                
            # 29 - SELL condizione speciale ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma100 < e con ma13 < ( and 20 < 100 )
            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and deviation_sell < -0.42
                
                and ma20_last < ma100_last
                and ma300_last < ma300_120_min_ago
                
                and ma100_last < ma100_30_min_ago
                and ma13_last > ma13_2_min_ago
                and ma2_last < last_trade_price
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL condizione speciale DOLCE ATTESA 300 < con ma100 < e con ma13 < and deviation < -0.42 ( and 20 < 100 ) - r 9500 b"
                action = "sell"

                
                
                
                
                
                
                
                        
                        
             
            
            # 30 - SELL condizione speciale ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma13 <
            
            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and deviation_ma100_sopra_ma200 > -0.70
                
                and deviation_sell < -0.43
                and ma13_last < ma13_2_min_ago
                
                and ma2_last < last_trade_price
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL condizione speciale DOLCE ATTESA 270 sec con ma13 < and deviation < -0.43 - r 9520"
                action = "sell"
                
                # il fattore tempo - la dolce attesa - solo con trend ribassista
                # deviation = ma2_last / last_trade_price
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                # max_hold_time_in_seconds = 270 sec = 4 min e 1/2  (con 6 min perdita di 0.60 %)
                # 4 feb 2022 con <-0.26 ha fatto -0.88% (dopo +4.29%)
                # 7 feb 2022 con <-0.345 e 270 sec ha fatto -0.38% - aumenta a 0.355 ! - eventualmente ci pensa la condizione CROLLO IMPROVVISO CHE FUNZIONA !
                
                
                
            # 31 - SELL condizione speciale ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma13 <
            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and deviation_ma100_sopra_ma200 < -0.70
                
                and deviation_sell < -0.50
                and ma13_last < ma13_2_min_ago
                
                and ma2_last < last_trade_price
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL condizione speciale DOLCE ATTESA 270 sec con ma13 < and deviation < -0.50 con 100 sotto di molto 200 durante crollo ! - r 9521"
                action = "sell"
                
                # durante il crollo sono un po' piu' tollerante - paradossalmente ! HO ATTESO MOLTO QUESTO MOMENTO !

                
                        
            
            
            
            
            
            
            
            # 32 - SELL condizione speciale ro cano VENDE " DOPO x MINUTI " and...
            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and deviation_sell < -0.49
                and ma8_last < ma50_last
                
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL condizione speciale TEMPO e se ma8 < ma50 and deviation_sell < -0.49 - r 9542"
                action = "sell"
                        
                # ma13 troppo lenta !
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                        
                        
               
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
              
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            # 33 - SELL condizione speciale POCHI MALEDETTI E SUBITO QUANDO SALE FORTE ( cerca di inibirlo ) con ma200 > MA ma100 - dedicated to comparo meo
            
            elif (
                ma3_last < ma28_last
                and deviation_ma100_sopra_ma200 > 0.40    
                and ma200_last > ma200_60_min_ago
                    
                and deviation_sell > 0.70
                and deviation_trend_ma100 < 1.00
                and deviation_pochi_maledetti > 0.25
                and ma2_last > ma100_last
                and ma2_last < ma2_2_min_ago
            ):    
                sell = "SELL condizione speciale POCHI MALEDETTI E SUBITO QUANDO SALE FORTE 3-28 ( cerca di inibirlo ) con ma200> e con deviation > 0.70 - r 9599"
                action = "sell"
                    
                # and ma2_last > ma100_last (altrimenti vende durante il crollo con la ma3-ma9)
                # incredibile questa and deviation_trend_ma100 < 1.00 - se ma100 sale "forte" da 60 min non deve intervenire sell 3-9
                
                
                
            # 34 - SELL condizione speciale POCHI MALEDETTI E SUBITO QUANDO SALE PIANO con ma200 > MA ma100 NON DEVE SALIRE TROPPO ! - dedicated to comparo meo
            
            elif (
                ma3_last < ma25_last
                and deviation_ma100_sopra_ma200 < 0.40      
                and ma200_last > ma200_60_min_ago
                    
                and deviation_sell > 0.70
                and deviation_sell < 0.99
                and deviation_trend_ma100 < 1.00
                and deviation_pochi_maledetti > 0.25
                and ma2_last > ma100_last
                
            ):    
                sell = "SELL condizione speciale POCHI MALEDETTI E SUBITO 3-25 QUANDO SALE PIANO quando ma200 > e con deviation > 0.70 and < 0.99 - r 9616"
                action = "sell"
                    
                # and ma2_last > ma100_last (altrimenti vende durante il crollo con la ma3-ma9)
                # incredibile questa and deviation_trend_ma100 < 1.00 - se ma100 sale "forte" da 60 min non deve intervenire sell 3-9
                    
                
                
            
            # 35 - SELL condizione speciale POCHI MALEDETTI E SUBITO con ma200 < - dedicated to comparo meo
            
            elif (
                ma3_last < ma20_last 
                and ma200_last < ma200_60_min_ago
                and deviation_sell > 0.90
                and deviation_sell < 1.30
                and deviation_pochi_maledetti > 0.70
                and ma2_last > ma100_last
                and ma2_last < ma2_2_min_ago
            ):    
                sell = "SELL condizione speciale POCHI MALEDETTI E SUBITO 3-20 quando ma200 < e con deviation > 0.90 and < 1.30 - dedicated to comparo meo - r 10201"
                action = "sell"
                    
                # and ma2_last > ma100_last (altrimenti vende durante il crollo con la ma3-ma9)
                
                
            # 36 - SELL condizione speciale POCHI MALEDETTI E SUBITO ma non troppo ! 3-18 quando ma200 < e con deviation > 1.31 and < 2.50
            
            elif (
                ma3_last < ma18_last 
                and ma200_last < ma200_60_min_ago
                and deviation_sell > 1.31
                and deviation_sell < 2.50
                and deviation_pochi_maledetti > 0.70
                and ma2_last > ma100_last
                and ma2_last < ma2_2_min_ago
            ):    
                sell = "SELL condizione speciale POCHI MALEDETTI E SUBITO ma non troppo ! 3-18 quando ma200 < e con deviation > 1.31 and < 2.50 - r 10202"
                action = "sell"
                    
                # and ma2_last > ma100_last (altrimenti vende durante il crollo con la ma3-ma9)
                # 14 giu 2022 3-18 da 3-9
                
                
            
            
            
            
            
            # 37 - POCHI MALEDETTI E SUBITO ma non troppo 3-28 mentre sale
            
            elif (
                ma3_last < ma28_last 
                and ma200_last < ma200_60_min_ago
                and deviation_ma100_sopra_ma300 > 0.30
                
                and deviation_sell > 2.51
                and deviation_pochi_maledetti > 0.70
                and ma2_last > ma100_last
                and ma2_last < ma2_2_min_ago
            ):    
                sell = "SELL condizione speciale POCHI MALEDETTI E SUBITO ma non troppo mentre sale 3-28 quando ma200 < e con deviation > 2.51 - r 10203 a"
                action = "sell"
                    
                # and ma2_last > ma100_last (altrimenti vende durante il crollo con la ma3-ma9)
                
                
                
                
            # 38 - POCHI MALEDETTI E SUBITO ma non troppo mentre scende
            
            elif (
                ma3_last < ma8_last 
                and ma200_last < ma200_60_min_ago
                and deviation_ma100_sopra_ma300 < 0.30
                
                and deviation_sell > 2.51
                and deviation_pochi_maledetti > 0.70
                and ma2_last > ma100_last
                and ma2_last < ma2_2_min_ago
            ):    
                sell = "SELL condizione speciale POCHI MALEDETTI E SUBITO 3-8 quando ma200 < e con deviation > 2.51 - dedicated to comparo meo - r 10203 b"
                action = "sell"
                    
                # and ma2_last > ma100_last (altrimenti vende durante il crollo con la ma3-ma9)
                
                
                
                
                
                
                
                
                
                
            
            ######################################################################### vendite dedicate al BUY FIAT - AUDI - MASERATI - FERRARI 
            
            # 39 - SELL condizione speciale FIAT 
                    
            elif (     
                seconds_since_last_trade > max_hold_time_in_seconds_fiat
                and deviation_buy_crollo_1 < -0.15
                and deviation_buy_crollo_1 > -0.59
                        
                and deviation_ma100_sopra_ma300 < -0.70
                and deviation_sell < -0.30
            ):    
                 
                buy = "SELL condizione speciale FIAT se > 2 min dal BUY FIAT la perdita e' < -0.30 ! - r 9658"
                action = "sell"
                        
                # and ma2_last < ma2_2_min_ago
                # and deviation_ma100_sopra_ma300 < -0.70 significa che c'e' un grande ribasso. 100 sta lontana da 300. 
                # EVITO COSI' PROBLEMI AL TREND LATERALE.
                        
                        
                        
                
            # 40 - SELL condizione speciale AUDI 
                    
            elif (     
                seconds_since_last_trade > max_hold_time_in_seconds_audi
                and deviation_buy_crollo_1 < -0.60
                and deviation_buy_crollo_1 > -0.90
                        
                and deviation_ma100_sopra_ma300 < -0.70
                and deviation_sell < -0.40
                        
            ):
                buy = "SELL condizione speciale AUDI se > 2 min dal BUY AUDI la perdita e' < -0.40 - r 9679"
                action = "sell"
                        
                # and ma2_last < ma2_2_min_ago
                        
                        
            
            
            # 41 - SELL condizione speciale MASERATI 
                    
            elif (     
                seconds_since_last_trade > max_hold_time_in_seconds_maserati
                and deviation_buy_crollo_1 < -0.91
                and deviation_buy_crollo_1 > -1.50
                      
                and deviation_ma100_sopra_ma300 < -0.70
                and deviation_sell < -0.50
                        
            ):
                buy = "SELL condizione speciale MASERATI se > 2 min dal BUY MASERATI la perdita e' < -0.50 - r 9698"
                action = "sell"
                        
                # and ma2_last < ma2_2_min_ago
                        
               
            
            
            # 42 - SELL condizione speciale FERRARI 
                    
            elif (     
                seconds_since_last_trade > max_hold_time_in_seconds_ferrari
                and deviation_buy_crollo_1 < -1.51
                        
                and deviation_ma100_sopra_ma300 < -0.70
                and deviation_sell < -0.58
            ):
                buy = "SELL condizione speciale FERRARI se > 2 min dal BUY FERRARI la perdita e' < -0.70 - r 9715"
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
        
        # roma 5 maggio 2022
        
        # 15 giugno 2022 INGRESSO DELLE 2 SORELLE 3-10 and 5-28
        
        # in futuro
            # MACD e RSI
            # TOGLIERE TUTTI GLI INCROCI AL BUY ! se 13 > 100 NON INCROCERA' MAI ! INCROCIO 13-100 DIVENTA 13>100 !
            # analisi dei dati !
            
           
        
        
        
        
