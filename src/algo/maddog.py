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
        ma56_last, ma56_prev = self.algo_helper.ma_last_prev(56)
        ma59_last, ma59_prev = self.algo_helper.ma_last_prev(59)
        
        ma69_last, ma69_prev = self.algo_helper.ma_last_prev(69)
        ma72_last, ma72_prev = self.algo_helper.ma_last_prev(72)
        ma78_last, ma78_prev = self.algo_helper.ma_last_prev(78)
        ma86_last, ma86_prev = self.algo_helper.ma_last_prev(86)
        ma90_last, ma90_prev = self.algo_helper.ma_last_prev(90)
        ma100_last, ma100_prev = self.algo_helper.ma_last_prev(100)
        ma125_last, ma125_prev = self.algo_helper.ma_last_prev(125)
        ma130_last, ma130_prev = self.algo_helper.ma_last_prev(130)
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
        ma28_20_min_ago = self.algo_helper.ma_minutes_ago(28, 20)
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
        ma59_60_min_ago = self.algo_helper.ma_minutes_ago(59, 60)
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
        ma100_180_min_ago = self.algo_helper.ma_minutes_ago(100, 180)
        ma100_301_min_ago = self.algo_helper.ma_minutes_ago(100, 301)
        
        ma150_60_min_ago = self.algo_helper.ma_minutes_ago(150, 60)
        ma200_15_min_ago = self.algo_helper.ma_minutes_ago(200, 15)
        ma200_20_min_ago = self.algo_helper.ma_minutes_ago(200, 20)
        ma200_30_min_ago = self.algo_helper.ma_minutes_ago(200, 30)
        ma200_60_min_ago = self.algo_helper.ma_minutes_ago(200, 60)
        ma200_90_min_ago = self.algo_helper.ma_minutes_ago(200, 90)
        ma200_120_min_ago = self.algo_helper.ma_minutes_ago(200, 120)
        ma200_120_min_ago = self.algo_helper.ma_minutes_ago(200, 120)
        ma200_180_min_ago = self.algo_helper.ma_minutes_ago(200, 180)
        ma200_301_min_ago = self.algo_helper.ma_minutes_ago(200, 301)
        
        ma300_20_min_ago = self.algo_helper.ma_minutes_ago(300, 20)
        ma300_60_min_ago = self.algo_helper.ma_minutes_ago(300, 60)
        ma300_120_min_ago = self.algo_helper.ma_minutes_ago(300, 120)
        ma300_180_min_ago = self.algo_helper.ma_minutes_ago(300, 180)
        
        ma300_300_min_ago = self.algo_helper.ma_minutes_ago(300, 300)
        ma300_301_min_ago = self.algo_helper.ma_minutes_ago(300, 301)
        
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
        price_1_min_ago = self.algo_helper.price_minutes_ago(1)
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
        
        
        
        # SELL DOPO 9000 secondi = 150 min dal BUY con 5-90 cazzo
        
        max_hold_time_in_seconds_sell_5_90 = 9000
        
        
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
        
        
        
        
        
        # formula delta_300_100
        
        delta_300_100 = (ma300_last / ma100_last - 1) * 100 if ma100_last else 0
        self.algo_helper.info("delta_300_100: {}".format(delta_300_100))
        
        
        # formula delta_300_100_60_min
        
        delta_300_100_60_min = (ma300_60_min_ago / ma100_60_min_ago - 1) * 100 if ma100_60_min_ago else 0
        self.algo_helper.info("delta_300_100_60_min: {}".format(delta_300_100_60_min))
        
        
        # non serve piu' il rapporto !
        
        
        
        
        
        
        
        
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
        
        
        
        
        
        # formula deviation trend ma100
        
        deviation_trend_ma100_180_min_ago = (ma100_last / ma100_180_min_ago - 1) * 100 if ma100_180_min_ago else 0
        self.algo_helper.info("deviation_trend_ma100_180_min_ago: {}".format(deviation_trend_ma100_180_min_ago))
        
        
        # formula deviation trend ma200
        
        deviation_trend_ma200 = (ma200_last / ma200_120_min_ago - 1) * 100 if ma200_120_min_ago else 0
        self.algo_helper.info("deviation_trend_ma200: {}".format(deviation_trend_ma200))
        
        
        # formula deviation trend ma300
        
        deviation_trend_ma300_180_min_ago = (ma300_last / ma300_180_min_ago - 1) * 100 if ma300_180_min_ago else 0
        self.algo_helper.info("deviation_trend_ma300_180_min_ago: {}".format(deviation_trend_ma300_180_min_ago))
        
        
        
        # formula deviation_ma100_180_min_ago_sopra_ma300_180_min_ago
        
        deviation_ma100_180_min_ago_sopra_ma300_180_min_ago = (ma100_180_min_ago / ma300_180_min_ago - 1) * 100 if ma300_180_min_ago else 0
        self.algo_helper.info("deviation_ma100_180_min_ago_sopra_ma300_180_min_ago: {}".format(deviation_ma100_180_min_ago_sopra_ma300_180_min_ago))
        
        
        
        
        
        
        
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
        
        
        
        # formula DEVIATION_ma5_sotto_ma300
        
        deviation_ma5_sotto_ma300 = (ma5_last / ma300_last - 1) * 100 if ma300_last else 0
        self.algo_helper.info("deviation_ma5_sotto_ma300: {}".format(deviation_ma5_sotto_ma300))
        
        
        
        
        
        
        
        
        
        
        
        
        
        # formula deviation_ma300_diviso_ma300_5_ore_ago
        
        deviation_ma300__diviso_ma300_5_ore_ago = (ma300_last / ma300_301_min_ago - 1) * 100 if ma300_301_min_ago else 0
        self.algo_helper.info("deviation_ma300__diviso_ma300_5_ore_ago: {}".format(deviation_ma300__diviso_ma300_5_ore_ago))
        
        
        # formula DEVIATION_MA100_LATERALE evita BUY CONTINUI DEL BUY ECCEZIONALE NELLA FASE LATERALE
        
        deviation_ma100_laterale = (ma5_last / ma100_last - 1) * 100 if ma100_last else 0
        self.algo_helper.info("deviation_ma100_laterale: {}".format(deviation_ma100_laterale))
        
        
        
        # formula DEVIATION_ma3_sotto_ma200 per comprare FINO a una certa distanza da ma200
        
        deviation_ma3_sotto_ma200 = (ma3_last / ma200_last - 1) * 100 if ma200_last else 0
        self.algo_helper.info("deviation_ma3_sotto_ma200: {}".format(deviation_ma3_sotto_ma200))
        
        # questa e' stata aggiunta il 13 settembre 2022 dopo che deviation_ma5_sotto_ma200 aveva fatto -3% !!!
        
        
        
        
        
        
        
        # formula DEVIATION_ma78_sotto_ma300
        
        deviation_ma78_sotto_ma300 = (ma78_last / ma300_last - 1) * 100 if ma300_last else 0
        self.algo_helper.info("deviation_ma78_sotto_ma300: {}".format(deviation_ma78_sotto_ma300))
        
        
        # formula DEVIATION_ma78_sotto_ma200
        
        deviation_ma78_sotto_ma200 = (ma78_last / ma200_last - 1) * 100 if ma200_last else 0
        self.algo_helper.info("deviation_ma78_sotto_ma200: {}".format(deviation_ma78_sotto_ma200))
        
        
        
        
        
        # formula DEVIATION_ma3_sotto_ma100 
        
        deviation_ma3_sotto_ma100 = (ma3_last / ma100_last - 1) * 100 if ma100_last else 0
        self.algo_helper.info("deviation_ma3_sotto_ma100: {}".format(deviation_ma3_sotto_ma100))
        
        
    
        # formula DEVIATION_ma3_sotto_ma300
        
        deviation_ma3_sotto_ma300 = (ma3_last / ma300_last - 1) * 100 if ma300_last else 0
        self.algo_helper.info("deviation_ma3_sotto_ma300: {}".format(deviation_ma3_sotto_ma300))
        
        
        
        
        
        
        
        
        
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
        
        
        
        # deviation ribasso e rialzo velocissimo 1 ! 
        
        deviation_ribasso_e_rialzo_velocissimo_1 = ( price / price_10_min_ago - 1) * 100 if price_10_min_ago else 0
        self.algo_helper.info("deviation_ribasso_e_rialzo_velocissimo_1: {}".format(deviation_ribasso_e_rialzo_velocissimo_1))
        
        
        
        # deviation ribasso e rialzo velocissimo 2 ! 
        
        deviation_ribasso_e_rialzo_velocissimo_2 = (price / price_2_min_ago - 1) * 100 if price_2_min_ago else 0
        self.algo_helper.info("deviation_ribasso_e_rialzo_velocissimo_2: {}".format(deviation_ribasso_e_rialzo_velocissimo_2))
        
        
        
      
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        
        
        # formula DEVIATION_ma200_sopra_ma300
        
        deviation_ma200_sopra_ma300 = (ma200_last / ma300_last - 1) * 100 if ma300_last else 0
        self.algo_helper.info("deviation_ma200_sopra_ma300: {}".format(deviation_ma200_sopra_ma300))
        
        
       
        
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
              
                    buy = "BUY 1 con 20>200 AND 10 > 100 AND 3-10 > 0.13 and 69 > 100 and deviation_bellissima > 0.14 and ma78 > - r 916A"
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
              
                    buy = "BUY 1 con 20>200 AND 10 > 100 AND 3-10 > 0.15 and 69 > 100 and deviation_bellissima > 0.14 and ma78 > - r 935B"
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
                    
                    buy = "BUY 1 piccola CORREZIONE FIAT = r 1226 RCCR medie mobili lunghe TUTTE IN RIALZO ! ma si verifica una correzione fiat ! - r 965 A"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                # BUY 1 piccola CORREZIONE FIAT = r 1226 RCCR medie mobili lunghe TUTTE IN RIALZO ! ma si verifica una correzione fiat !
                
                elif (
                    ma3_last > ma25_last
                    and ma100_last > ma100_10_min_ago
                    and ma33_last < ma78_last
                    
                    and deviation_ma3_sopra_ma10 > 0.18
                    and deviation_ma5_sopra_ma28 > 0.20
                    
                    and ma100_last > ma100_120_min_ago
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    
                    and ma100_last > ma200_last
                    and ma200_last > ma300_last
                    
                    and deviation_buy_crollo_1 < -0.33
                    and deviation_buy_crollo_1 > -0.59
                    and ma2_last > ma2_2_min_ago
                    
                ):    
                    
                    buy = "BUY 1 piccola CORREZIONE FIAT = r 1226 RCCR medie mobili lunghe TUTTE IN RIALZO ! ma si verifica una correzione fiat ! - r 994 B"
                    action = "buy"
                    percentage = 80
                    
                    # > estate alzato buy
                    
                    
                    
                    
                    
                    
                    
                    
                    
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
              
                    buy = "BUY 1 con 20>200 and 69 > 100 and deviation_bellissima > 0.14 and ma78 < AND 5-28 > 0.11 - r 1021"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                
                # BUY 1 con 28>300 and 69 > 100 e 200> and deviation_bellissima > 0.12 and 5-28>0.18
                
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
              
                    buy = "BUY 1 con 28>300 and 69 > 100 e 200> and deviation_bellissima > 0.12 and 5-28>0.18 - r 1042"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                    
                # BUY 1 5-300 in alto
                
                elif (
                    
                    ma8_last > ma150_last
                    and deviation_ma100_sopra_ma200 > -0.30
                    
                    and deviation_ma5_sotto_ma300 > 0.33
                    
                    
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
                    buy = "BUY 1 5-300 - riga 1043 A"
                    action = "buy"
                    percentage = 50
                    
                    # importante : ma100 sta sotto la ma200 non le e' troppo lontana
                    
                    
                    
                    
                    
                # BUY 1 5-300 zona mediana
                
                elif (
                    
                    ma8_last > ma150_last
                    and deviation_ma100_sopra_ma200 > -0.30
                    
                    and deviation_ma5_sotto_ma300 < 0.33
                    and deviation_ma5_sotto_ma300 > -0.33
                    
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
                    buy = "BUY 1 5-300 - riga 1043 B"
                    action = "buy"
                    percentage = 50
                    
                    # importante : ma100 sta sotto la ma200 non le e' troppo lontana
                    
                    
                    
                    
                # BUY 1 zona inferiore
                
                elif (
                    
                    ma8_last > ma150_last
                    and deviation_ma100_sopra_ma200 > -0.30
                    
                    and deviation_ma5_sotto_ma300 < -0.33
                    
                    
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
                    buy = "BUY 1 5-300 - riga 1043 C"
                    action = "buy"
                    percentage = 50
                    
                    # importante : ma100 sta sotto la ma200 non le e' troppo lontana
                    
                    
                
                
                
                
                
                
                
                elif (    
                    ma28_last > ma300_last
                    and ma300_last < ma300_120_min_ago
                    and ma200_last < ma200_60_min_ago
                    
                    and deviation_ma3_sopra_ma10 > 0.10
                    and deviation_ma5_sopra_ma28 > 0.16
                    and deviation_bellissima > 0.12
                    
                    and ma69_last > ma100_last
                    and ma3_last > ma8_last
                    
                    and ma6_last > ma39_last
                ):    
              
                    buy = "BUY 1 con 28>300 and 69 > 100 e 200< and deviation_bellissima > 0.12 and 5-28 > 0.16 and 3-10 > 0.10 - r 1061"
                    action = "buy"
                    percentage = 90
                    
                    # > estate dev bellissima 0.12 and 5-28 0.16 and 3-10 > 0.10
                    
                    
                    
                # ------------------------------------------------------ BUY 1 MOLTO RISCHIOSO modo 1 ! quando incomincia il ribasso MA ma300 120 > E ma200 120 >
                  
                elif (     
                    ma300_last > ma300_120_min_ago
                    and ma78_last > ma100_last
                    and ma200_last > ma200_120_min_ago
                    
                    and ma200_last < ma200_60_min_ago
                    and ma100_last < ma100_60_min_ago
                    
                    and ma200_last > ma300_last
                    
                    and ma8_last > ma78_last
                    
                    and deviation_ma3_sopra_ma10 > 0.10
                    and deviation_ma5_sopra_ma28 > 0.18
                    and deviation_bellissima > 0.07
               
                    and ma2_last >= ma2_2_min_ago
                ):     
                  
                    buy = "BUY 1 - 80% - RISCHIOSO ! incomincia il ribasso MA ma300 120 > e ma200 120 > ANCORA IN RIALZO ! E 200 > 300 e 3-10 > 0.10 - r 1088 A1x"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                # ------------------------------------------------------ BUY 1 MOLTO RISCHIOSO modo 1 ! quando incomincia il ribasso MA ma300 120 > E ma200 120 >
                  
                elif (     
                    ma300_last > ma300_120_min_ago
                    and ma78_last < ma100_last
                    and ma200_last > ma200_120_min_ago
                    
                    and ma200_last < ma200_60_min_ago
                    and ma100_last < ma100_60_min_ago
                    
                    and ma200_last > ma300_last
                    
                    and ma8_last > ma78_last
                    
                    and deviation_ma3_sopra_ma10 > 0.10
                    and deviation_ma5_sopra_ma28 > 0.30
                    and deviation_bellissima > 0.07
               
                    and ma2_last >= ma2_2_min_ago
                ):     
                  
                    buy = "BUY 1 - 80% - RISCHIOSO ! incomincia il ribasso MA ma300 120 > e ma200 120 > ANCORA IN RIALZO ! E 200 > 300 e 3-10 > 0.10 - r 1088 A1y"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                    
                    
                    
                    
                    
                # ------------------------------------------------------ BUY 1 MOLTO RISCHIOSO modo 1 ! quando incomincia il ribasso MA ma300 120 > E ma200 120 >
                  
                elif (     
                    ma300_last > ma300_120_min_ago
                    and ma200_last > ma200_120_min_ago
                    
                    and ma200_last < ma200_60_min_ago
                    and ma100_last < ma100_60_min_ago
                    
                    and ma200_last < ma300_last
                    
                    and ma8_last > ma78_last
                    
                    and deviation_ma3_sopra_ma10 > 0.13
                    and deviation_ma5_sopra_ma28 > 0.20
                    and deviation_bellissima > 0.10
               
                    and ma2_last >= ma2_2_min_ago
                ):     
                  
                    buy = "BUY 1 al 70% RISCHIOSO ! incomincia il ribasso MA ma300 120 > e ma200 120 > ANCORA IN RIALZO ! MA 200 < 300 e 3-10 > 0.13 - r 1114 A2"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                    
                    
                
                    
                    
                    
                    
                    
                    
                    
                # ------------------------------------------------------------ BUY 1 MOLTO RISCHIOSO modo 1 ! quando incomincia il ribasso MA ma300 > MA ma200 120 <
                  
                elif (     
                    ma300_last > ma300_120_min_ago
                    and ma200_last < ma200_120_min_ago
                    
                    and ma200_last < ma200_60_min_ago
                    and ma100_last < ma100_60_min_ago
                    
                    and ma8_last > ma48_last
                    
                    and deviation_ma3_sopra_ma10 > 0.12
                    and deviation_ma5_sopra_ma28 > 0.19
                    
                    and ma5_last > ma200_last
                    and ma2_last > ma2_2_min_ago
                ):     
                  
                    buy = "BUY 1 MOLTO RISCHIOSO modo 1 ! quando incomincia il ribasso MA ma300 ANCORA IN RIALZO MA ma200 120 < con 3-10 > 0.13 - r 1139 B1"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                    
                    
                    
                    
                # ------------------------------------------------------------ BUY 1 MOLTO RISCHIOSO modo 1 ! quando incomincia il ribasso MA ma300 > MA ma200 120 <
                  
                elif (     
                    ma300_last > ma300_120_min_ago
                    and deviation_ma5_sotto_ma300 < -0.40
                    
                    and ma200_last < ma200_120_min_ago
                    
                    and ma200_last < ma200_60_min_ago
                    and ma100_last < ma100_60_min_ago
                    
                    and ma5_last > ma48_last
                    
                    and deviation_ma3_sopra_ma10 > 0.10
                    and deviation_ma5_sopra_ma28 > 0.10
                    
                    and ma2_last >= ma2_2_min_ago
                ):     
                  
                    buy = "BUY 1 MOLTO RISCHIOSO modo 1 ! quando incomincia il ribasso MA ma300 ANCORA IN RIALZO MA ma200 120 < con 3-10 > 0.13 - r 1139 B2"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                    
                    
                    
                    
                    
                    
                # ------------------------------------------------------------ BUY 1 MOLTO RISCHIOSO modo 2 ! quando incomincia il ribasso MA ma300 > E MA 200>300
                
                elif (     
                    ma300_last > ma300_120_min_ago
                    and ma200_last > ma300_last
                    and ma78_last > ma100_last
                    and ma8_last > ma100_last
                    
                    and ma200_last < ma200_60_min_ago
                    and ma100_last < ma100_60_min_ago
                    
                    and deviation_ma3_sopra_ma10 > 0.17
                    and deviation_ma5_sopra_ma28 > 0.17
                    and deviation_bellissima > 0.14
                    
                    and ma2_last > ma2_2_min_ago
                ):     
                  
                    buy = "BUY 1 MOLTO RISCHIOSO modo 2 ! quando incomincia il ribasso MA ma300 > E 200>300 con 78>100 - r 1161 A1"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                    
                    
                    
                # ----------------------------------------------------- BUY 1 MOLTO RISCHIOSO modo 2 ! quando incomincia il ribasso MA ma300 > E MA 200>300
                
                elif (     
                    ma300_last > ma300_301_min_ago
                    
                    and ma200_last > ma300_last
                    and ma78_last < ma100_last
                    and ma8_last > ma100_last
                    
                    and ma200_last < ma200_60_min_ago
                    and ma100_last < ma100_60_min_ago
                    and deviation_ma3_sopra_ma10 > 0.11
                    and deviation_ma5_sopra_ma28 > 0.13
                    and deviation_bellissima > 0.10
                    and ma2_last > ma2_2_min_ago
                ):     
                  
                    buy = "BUY 1 MOLTO RISCHIOSO modo 2 ! quando incomincia il ribasso MA ma300 > E 200>300 con 78<100 e 5-28 > 0.19 - r 1161 A2"
                    action = "buy"
                    percentage = 80
                    
                    # 28 set se 300 sale da 5 ore ho anticipato il buy di una ndecchiecella
                    
                    
                
                    
                    
                    
                
                    
                    
                    
                    
                    
                
                
                
                    
                    
                    
                # ------------------------------------------------------------ BUY 1 MOLTO RISCHIOSO modo 2 ! quando incomincia il ribasso MA ma300 > E MA 200<300
                
                
                elif (     
                    ma300_last > ma300_120_min_ago
                    
                    and ma200_last < ma300_last
                    and ma5_last < ma300_last
                    and ma5_last > ma100_last
                    
                    and deviation_ma3_sopra_ma10 > 0.135
                    
                    and ma200_last < ma200_60_min_ago
                    and ma100_last < ma100_60_min_ago
              
                    and ma2_last > ma2_2_min_ago
                ):     
                  
                    buy = "BUY 1 quando incomincia il ribasso MA ma300> MA 200<300 CON 5 SOTTO 300 ! E COMPRA CON 5 SOPRA 100 ! - r 1184 B1"
                    action = "buy"
                    percentage = 90
                    
                    # 20 set 2022 aggiunto 3-10 > 0.11
                    #  1 ott 2022 3-10 > 0.135
                    
                
                    
                    
                    
                
             
                
                # ------------------------------------------------------------ BUY 1 RAFFORZATA se ma200> and ma300 > and 8>50 AND ma78 >
                
                elif (    
                    ma20_last > ma200_last
                    
                    and delta_300_100 < 0.20
                    and delta_300_100 > -0.20
                    
                    and ma50_last > ma78_last
                    
                    and deviation_ma3_sopra_ma10 > 0.07
                    
                    and ma28_last > ma28_20_min_ago
                    
                    and ma59_last > ma59_60_min_ago
                    and ma78_last > ma78_2_min_ago
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    and ma8_last > ma50_last
                  
                ):  
                
                    buy = "BUY 1 (50>78) con 20>200 and 69 > 100 AND ma78 > AND 59 > 59 60 min ago CON 28 > 28 20 min - r 1206 aA"
                    action = "buy"
                    percentage = 80
                    
                    # 19 set 2022 aggiunta 3-10 > 0.07
                    
                    
                    
                    
                    
                    
                    
                    
                # ------------------------------------------------------------ BUY 1 RAFFORZATA se ma200> and ma300 > and 8>50 AND ma78 >
                
                elif (    
                    ma20_last > ma200_last
                    and ma50_last > ma78_last
                    and deviation_ma3_sopra_ma10 > 0.12
                    and ma28_last < ma28_20_min_ago
                    
                    and ma59_last > ma59_60_min_ago
                    and ma78_last > ma78_2_min_ago
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    and ma8_last > ma50_last
                ):  
                
                    buy = "BUY 1 (50>78) con 20>200 and 69 > 100 AND ma78 > AND 59 > 59 60 min ago CON 28 < 28 20 min AND 3-10 > 0.12- r 1227 aB"
                    action = "buy"
                    percentage = 80
                    
             
                    
                # ------------------------------------------------------------ BUY 1 RAFFORZATA se ma200> and ma300 > and 8>50 AND ma78 > CON 3-10 > 0.12
                
                elif (    
                    ma20_last > ma200_last
                    and ma50_last > ma78_last
                    and deviation_ma3_sopra_ma10 > 0.12
                    
                    and ma59_last < ma59_60_min_ago
                    and ma78_last > ma78_2_min_ago
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    and ma8_last > ma50_last
                ):  
                
                    buy = "BUY 1 RAFFORZATA (50>78) con 20>200 and 69 > 100 and dev_bellissima > 0.14 AND ma78 > AND 59 > 59 60 min ago CON 3-10 > 0.12- r 1247 b"
                    action = "buy"
                    percentage = 80
                    
             
                # ------------------------------------------------------------ BUY 1 se ma200> and ma300 > and 8>50 AND ma78 >  
                
                elif (    
                    ma20_last > ma200_last
                    and ma78_last > ma100_last
                    and ma50_last < ma78_last
                    and deviation_ma5_sopra_ma28 > 0.21
                    
                    and ma78_last > ma78_2_min_ago
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    and ma8_last > ma50_last
                ):  
                
                    buy = "BUY 1 (50<78) con 20>200 and 69 > 100 and deviation 5-28 > 0.16 AND ma78 > - r 1266 A"
                    action = "buy"
                    percentage = 90
                    
                    # > estate 5-28 a 0.21 da 0.16
                    
                    
                    
                    
                # ------------------------------------------------------------ BUY 1 se ma200> and ma300 > and 8>50 AND ma78 >  
                
                elif (    
                    ma20_last > ma200_last
                    and ma78_last < ma100_last
                    and ma50_last < ma78_last
                    and deviation_ma5_sopra_ma28 > 0.30
                    
                    and ma78_last > ma78_2_min_ago
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    and ma8_last > ma50_last
                ):  
                
                    buy = "BUY 1 (50<78) con 20>200 and 69 > 100 and deviation_bellissima > 0.14 AND ma78 > - r 1266 B"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                    
                    
                    
                    
                    
                   
                    
                # BUY 1 se ma200> and ma300 > and 8>50 AND ma78 > AND 8 > 78 AND 5-28 > 0.11 
                
                elif (    
                    ma20_last > ma125_last
                    and ma78_last > ma200_last
                    
                    and ma8_last > ma78_last
                    and ma78_last < ma78_2_min_ago
                    
                    and deviation_ma3_sopra_ma10 > 0.15
                    and deviation_ma5_sopra_ma28 > 0.12
                    
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    and ma8_last > ma50_last
                ):  
                
                    buy = "BUY 1 con 20>125 and 69 > 100 AND ma78 > AND 8 > 78 CON 78 > 200 and 5-28 > 0.12 and 3-10 > 0.15  - r 1288 A"
                    action = "buy"
                    percentage = 90
                    
                    # 27 giu 2022 20>125 da 20>200
                    
                    
                    
                    
                # BUY 1 se ma200> and ma300 > and 8>50 AND ma78 < AND 8 > 78 AND 5-28 > 0.11 
                
                elif (    
                    ma20_last > ma125_last
                    and ma78_last < ma200_last
                    
                    and ma8_last > ma78_last
                    and ma78_last < ma78_2_min_ago
                    
                    and deviation_ma3_sopra_ma10 > 0.21
                    and deviation_ma5_sopra_ma28 > 0.22
                    
                    and ma200_last > ma200_120_min_ago
                    and ma300_last > ma300_120_min_ago
                    and ma8_last > ma50_last
                ):  
                
                    buy = "BUY 1 con 20>125 and 69 > 100 and dev_bellissima > 0.14 AND ma78 > AND 8 > 78 AND 5-28 > 0.22 CON 78<200 e 3-10 > 0.21 ! - r 1288 B"
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
                
                    buy = "BUY 1 con 20>200 and 69 > 100 and deviation_bellissima > 0.14 AND ma78 > AND 8 < 78 AND 5-28 > 0.17 - r 1336"
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
                    buy = "BUY 1 PERICOLOSA 8-54 derivata dal tardo autunno ! togliendo i 40 minuti della ma30 con 11-59 con 5-28 > 0.19 - r 1365 Aa"
                    action = "buy"
                    percentage = 80
                    
                    # 100 deve stare un po' sotto alla 300 !
                    
                    
                    
                    
                # BUY 1 PERICOLOSA derivata dal tardo autunno ! togliendo i 40 minuti della ma30 
                
                elif (     
                    ma8_last > ma54_last
                    and ma78_last < ma200_last
                    and deviation_ma3_sopra_ma10 > 0.24
                    and deviation_ma5_sopra_ma28 > 0.30
                    
                    and ma39_last > ma39_30_min_ago
                    and ma69_last >= ma69_2_min_ago
                    
                    and deviation_ma100_sopra_ma300 < -0.30
                    and ma100_last < ma200_last
                    and ma200_last < ma200_120_min_ago
               
                    and deviation_bellissima > 0.05
                    
                    and ma20_last >= ma20_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma2_last > ma20_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 PERICOLOSA 8-54 derivata dal tardo autunno ! togliendo i 40 minuti della ma30 con 11-59 con 5-28 > 0.30 - r 1396 Ab"
                    action = "buy"
                    percentage = 70
                    
                    # 100 deve stare un po' sotto alla 300 !
                    # 22 giu 2022 se 78 >200 5-28 > 0.30
                    
                  
                    
                    
                # BUY 1 PERICOLOSA derivata dal tardo autunno ! togliendo i 40 minuti della ma30 
                
                elif (     
                    ma8_last > ma54_last
                    and ma39_last > ma39_30_min_ago
                    and ma69_last < ma69_2_min_ago
                    
                    and deviation_ma100_sopra_ma300 < -0.25
                    and deviation_ma3_sopra_ma10 > 0.17
                    and deviation_ma5_sopra_ma28 > 0.19
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma200_120_min_ago
                  
                    and deviation_bellissima > 0.06
                    
                    and ma20_last > ma20_2_min_ago
                    and ma2_last > ma20_last
                    
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 PERICOLOSA 8-54 derivata dal tardo autunno ! con 11-59 con 5-28 > 0.19 AND 3-10 > 0.17 cazzo - r 1427 B"
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
                    
                    and deviation_ma3_sopra_ma10 > 0.27
                    and deviation_ma5_sopra_ma28 > 0.21
                    
                    and ma20_last > ma20_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma2_last > ma20_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 PERICOLOSA 8-54 and 39< derivata dal tardo autunno ! CON 78>200 con 5-28 > 0.20 - r 1456 A"
                    action = "buy"
                    percentage = 90
                    
                    # 100 deve stare un po' sotto alla 300 !
                    
                    
                    
                # BUY 1 PERICOLOSA derivata dal tardo autunno ! togliendo i 40 minuti della ma30 
                
                elif (     
                    ma8_last > ma54_last
                    and ma78_last < ma200_last
                    
                    and deviation_ma3_sopra_ma10 > 0.27
                    and deviation_ma5_sopra_ma28 > 0.30
                    
                    
                    and ma39_last < ma39_30_min_ago
                    and deviation_ma100_sopra_ma300 < -0.27
                    and ma100_last < ma200_last
                    and ma200_last < ma200_120_min_ago
                    
                    and ma11_last > ma59_last
                    
                    and ma20_last > ma20_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma2_last > ma20_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 PERICOLOSA 8-54 and 39< derivata dal tardo autunno !  AND 78 < 200 CON 3-10 > 0.24 CON 5-28 > 0.27 - r 1486 B"
                    action = "buy"
                    percentage = 90
                    
                    # 100 deve stare un po' sotto alla 300 !
                    # 22 GIU 2022 5-28 > 0.27 da 0.20
                    
                    # > estate 3-10 0.27 and 5-28 0.30 HO ALZATO IL BUY ! e forse qua un giorno metto incrocio al rialzo 8-54
                    
                    
                    
                    
                    
                    
                    
                    
                    
               
                    
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
                    buy = "BUY 1 tempo ESTATE PIU' LENTA 100 > 60 min ago considera il passare del tempo ! ma30 > - r 1514"
                    action = "buy"
                    percentage = 90
                    
                    
                
                
                
                
                
                    
                    
                    
                    
                    
                    
                    
                    
                    
                # BUY 1 tempo ESTATE PIU' VELOCE 100 > 60 min ago (solo l' estate se lo puo' perettere!) considera il passare del TEMPO ! ma30 > 
                
                elif (     
                    ma15_last > ma28_last
                    and ma78_last > ma100_last
                    
                    and ma8_last > ma200_last
                    and ma100_last > ma100_60_min_ago
                    
                    and ma30_last > ma30_40_min_ago
                    
                    and deviation_ma3_sopra_ma10 > 0.08
                    and deviation_ma5_sopra_ma28 > 0.13
                    and deviation_bellissima > 0.05
                    and ma20_last > ma20_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma2_last > ma20_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 tempo ESTATE PIU' VELOCE 100 > 60 min ago (solo l' estate se lo puo' permettere!) considera il passare del tempo ! ma30 > - r 1537 A"
                    action = "buy"
                    percentage = 90
                    
                    # 9 giu 2022 15>28 al posto di 50>100 
                    # 9 giu 2022 8>200 al posto di 100>200
                    # 4 set 5-28 0.13 da 0.15
                    # 4 set dev bellissima 0.05 da 0.06
                    
                    
                    
                    
                # BUY 1 tempo ESTATE PIU' VELOCE 100 > 60 min ago (solo l' estate se lo puo' perettere!) considera il passare del TEMPO ! ma30 > 
                
                elif (     
                    ma15_last > ma28_last
                    and ma78_last < ma100_last
                    
                    and ma8_last > ma200_last
                    and ma100_last > ma100_60_min_ago
                    
                    and ma30_last > ma30_40_min_ago
                
                    and deviation_ma5_sopra_ma28 > 0.22
                    and deviation_bellissima > 0.06
                    and ma20_last > ma20_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma2_last > ma20_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 tempo ESTATE PIU' VELOCE 100 > 60 min ago (solo l' estate se lo puo' permettere!) considera il passare del tempo ! ma30 > - r 1537 B"
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
                    buy = "BUY 1 tempo PRIMAVERA che considera il passare del tempo con deviation_bellissima > 0.06 and deviation_ma5_sopra_ma28 > 0.18 - r 1562"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                # BUY 1 tempo INIZIO AUTUNNO con 78 > 150 and (200 > 200 120 min) che considera passare del tempo con ma30 > MA 100 < 200
                
                elif (     
                    ma50_last > ma100_last
                    and ma78_last > ma150_last
                    
                    and ma200_last > ma300_last
                    and ma200_last > ma200_120_min_ago
                    and deviation_ma5_sopra_ma28 > 0.05
                    and ma100_last < ma200_last
                    
                    and ma30_last > ma30_40_min_ago
                    
                    and ma11_last > ma125_last
                  
                    and deviation_bellissima > 0.02
                    and ma20_last > ma20_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma2_last > ma20_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 tempo INIZIO AUTUNNO con 78 > 150 and (200 > 200 120 min ago) che considera passare del tempo con 5-28 > 0.05 e 200>300 - r 1586 A1"
                    action = "buy"
                    percentage = 80
                    
                    # > estate ho anticipato buy
                    
                    
                    
                # BUY 1 tempo INIZIO AUTUNNO con 78 < 150 and (200 > 200 120 min) che considera passare del tempo con ma30 > MA 100 < 200
                
                elif (     
                    ma50_last > ma100_last
                    and ma78_last < ma150_last
                    
                    and ma200_last > ma300_last
                    and ma200_last > ma200_120_min_ago
                    and deviation_ma5_sopra_ma28 > 0.25
                    and ma100_last < ma200_last
                    
                    and ma30_last > ma30_40_min_ago
                    
                    and ma11_last > ma125_last
                  
                    and deviation_bellissima > 0.02
                    and ma20_last > ma20_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma2_last > ma20_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 tempo INIZIO AUTUNNO con 78 < 150 and (200 > 200 120 min ago) che considera passare del tempo con 5-28 > 0.25 e 200>300 - r 1586 A2"
                    action = "buy"
                    percentage = 80
                    
                    # > estate ho anticipato buy
                    
                    
                    
                    
                    
                    
                # BUY 1 tempo INIZIO AUTUNNO (200 > 200 120 min) che considera il passare del tempo con ma30 > MA 100 < 200
                
                elif (     
                    ma50_last > ma100_last
                    and ma200_last < ma300_last
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
                    buy = "BUY 1 tempo INIZIO AUTUNNO (200 > 200 120 min ago) che considera il passare del tempo con 5-28 > 0.17 and 200<300 - r 1586 b"
                    action = "buy"
                    percentage = 70
                    
                    
                
                
                # BUY 1 tempo FINE AUTUNNO PRECEDENTE (quasi inverno !)
                
                elif (     
                    ma8_last > ma50_last
                    and ma78_last > ma100_last
                    
                    and ma200_last < ma200_120_min_ago
                    and ma100_last < ma200_last
                    
                    and ma30_last >= ma30_30_min_ago
                
                    and deviation_ma3_sopra_ma10 > 0.10
                    and deviation_ma5_sopra_ma28 > 0.15
                    and deviation_bellissima > 0.05
               
                    and ma20_last > ma20_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma2_last > ma20_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 pericolosa MA 78 > 100 tempo FINE AUTUNNO (quasi inverno) che considera passare tempo E CON 3-10 > 0.10 con 5-28 > 0.15 - r 1614 a"
                    action = "buy"
                    percentage = 80
                    
                    # 28 GIU 2022 HO TOLTO 11-125 e sono tornato alle origini con 8-56 !
                    # 20 set 8-50 da 8-56
                    
                    
                # BUY 1 tempo FINE AUTUNNO PRECEDENTE (quasi inverno !)
                
                elif (     
                    ma8_last > ma56_last
                    and ma78_last < ma100_last
                    
                    and ma200_last < ma200_120_min_ago
                    and ma100_last < ma200_last
                    
                    and ma30_last > ma30_30_min_ago
                    
                    
                    and deviation_ma3_sopra_ma10 > 0.24
                    and deviation_ma5_sopra_ma28 > 0.20
                    and deviation_bellissima > 0.06
               
                    and ma20_last > ma20_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma2_last > ma20_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 PERICOLOSA 78<100 tempo FINE AUTUNNO (quasi inverno) con 50-78 considera passare del tempo CON 3-10>0.24 con 5-28 > 0.20 - r 1614 b"
                    action = "buy"
                    percentage = 80
                    
                    # 28 GIU 2022 HO TOLTO 11-125 e sono tornato alle origini con 8-56 !
                    
                    
                    
                
                
                
                
                # BUY 1 2 sett 2022 ore 5:03 - maria callas casta diva bellini - ma300 che SALE
                
                elif (     
                    ma5_last > ma69_last
                    and deviation_ma50_sotto_ma300 < -0.29
                    and deviation_ma78_sotto_ma300 < -0.20
                    
                    and ma300_last > ma300_301_min_ago
                    and ma300_last > ma300_60_min_ago
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma200_120_min_ago
                    
                    and deviation_ma3_sopra_ma10 > 0.11
                    and deviation_ma5_sopra_ma28 > 0.13
                    
                    and ma2_last > ma20_last
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 1 2 sett 2022 ore 5:03 maria callas casta diva bellini - ma300 5 ore che SALE - r 1615 A"
                    action = "buy"
                    percentage = 80
                    
                    # vedi che c'e' ma 300 5 ore che cresce
                    # 18 set 3-10 a 0.11 da 0.09
                    # se 78 sta lontana dalla 200 3-10 e' ok ! cazzo ! vedi 20 settembre ore 12:26
                    
                
                    
                
                
                
                # BUY 1 maria callas core 'ngrato - 2 sett 2022 ore 5:03 - ma300 che SCENDE
                
                elif (     
                    ma5_last > ma69_last
                    and deviation_ma50_sotto_ma300 < -0.29
                    and deviation_ma78_sotto_ma300 < -0.23
                    and deviation_ma78_sotto_ma200 < -0.30
                    and deviation_ma5_sotto_ma300 < -0.60
                    
                    and ma300_last < ma300_301_min_ago
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma200_120_min_ago
                    
                    and deviation_ma3_sopra_ma10 > 0.07
                    and deviation_ma5_sopra_ma28 > 0.108
                    
                    and ma2_last >= ma20_last
                    and ma2_last >= ma2_2_min_ago
                ):    
                    buy = "BUY 1 maria callas core 'ngrato - 5 sotto 300 < -0.60 - 2 sett 2022 ore 5:03 - ma300 che SCENDE - r 1615 B"
                    action = "buy"
                    percentage = 80
                    
                    # vedi che c'e' ma 300 che scende
                    # 19 set 2022 ho anticipato maria callas core ngrato di una ndecchiecella
                    # se 78 sta vicino alla 200 3-10 piu' alto ! cazzo ! vedi 20 settembre ore 14:47
                    # 24 set 2022 5-28 > 0.11 da 0.12
                    # 26 set 2022 5-28 > 0.108 da 0.11
                    
                
                    
                    
                    
                    
                    
                
                
                
                
                
                
                
                
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
                    buy = "BUY 1 PERICOLOSA tempo FINE AUTUNNO VELOCE (quasi inverno !) con 50-78 che considera il passare del tempo con 5-28 > 0.20 - r 1651"
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
                    buy = "BUY 1 tempo INVERNO che considera il passare del tempo con dev_bellissima > 0.06 and dev_ma5_sopra_ma28 > 0.18 E 3-10 > 0.09 - r 1688"
                    action = "buy"
                    percentage = 90
                    
                    
                
                    
                    
                # BUY 1 con ma200 < 300< MA ma100> 100 60 min ago e doppio delta < and ma100 >60_min_ago STA RISALENDO !
            
                elif (       
                    ma200_last < ma200_20_min_ago
                    and ma8_last > ma125_last
                    and ma2_last >= ma2_2_min_ago
                    
                    and deviation_ma3_sopra_ma10 > 0.07
                    and deviation_ma5_sopra_ma28 > 0.11
                 
                    and delta_1 < delta_2
                    and ma100_last > ma100_60_min_ago
                    
                    and ma200_last < ma200_60_min_ago
                    and ma300_last < ma300_60_min_ago
                ):    
        
                    buy = "BUY 1 11-125 con ma200< 300< MA ma100> 100 60 min ago e doppio delta < MA ma100 > - GIORNO ! - riga 1712"
                    action = "buy"
                    percentage = 90
                    
                    # 11-150 perche' doppio delta sta risalendo !
                    # MA HO DOVUTO AGGIUNGERE and deviation_ma5_sopra_ma28 > 0.20
                    
                    # 14 giu 2022 11-125 da 11-150 (giorno!)
                    # 22 set 2022 aggiunto 3-10 0.07
                    # 22 set 2022 5-28 > 0.12
                    # 30 set 5-28 0.11 da 0.12
                    
                    
                    
                    
                    
                    
                # BUY 1 MISTERO CON 8>50 E 5-28 PIU' ALTO ! per arrivare una ndecchia prima del passare del tempo. prendendo rischio
                
                elif (
                    deviation_ma5_sopra_ma28 > 0.30
                    and ma78_last > ma200_last
                    and deviation_ma3_sopra_ma10 > 0.05
                    
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
                    buy = "BUY 1 MISTERO CON 8>54 E 5-28 PIU' ALTO ! prendendo rischio con 78 > 200 3-10 > 0.05 - riga 1751 a"
                    action = "buy"
                    percentage = 90
                    
                    # ma100 sta sotto la ma200 MA non le e' troppo lontana cioe' NON ci troviamo in una situazione drammatica! ( anche se ma100< e ma200< e ma300< )
                    # MISTERO !
                    
                    
                    
                # BUY 1 MISTERO CON 8>50 E 5-28 PIU' ALTO ! per arrivare una ndecchia prima del passare del tempo. prendendo rischio
                
                elif (
                    deviation_ma5_sopra_ma28 > 0.30
                    and ma78_last < ma200_last
                    and deviation_ma3_sopra_ma10 > 0.24
                    
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
                    buy = "BUY 1 MISTERO CON 8>54 E 5-28 PIU' ALTO ! prendendo rischio con 78 < 200 3-10 > 0.24 - riga 1783 b"
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
                    buy = "BUY 1 MISTERO con INCROCIO 8-50 e 5-28 > 0.28 prendendo rischio - E CON delta 200-78 - RIALZO - riga 1825 AA"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                    
                    
                    
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
                    buy = "BUY 1 MISTERO con INCROCIO 8-50 e 5-28 > 0.28 prendendo rischio - E CON delta 200-78 - RIALZO - riga 1862 AB"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                    
                    
                    
                    
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
                    buy = "BUY 1 MISTERO con INCROCIO 8-50 e 5-28 > 0.28 prendendo rischio - E CON delta 200-78 - RIBASSO - riga 1898 B"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
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
                    buy = "BUY 1 MISTERO (sembra BUY FIAT) con INCROCIO 8-50 e 5-28 > 0.14 arrivare ndecchia prima del passare del tempo - rischiosa - riga 1936"
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
                    and deviation_bellissima > 0.21
                    and deviation_ma13_sopra_ma25 > 0.09
                    and deviation_ma3_sopra_ma7 > 0.05
                    and ma3_last > ma3_3_min_ago
                    and ma2_last > ma2_2_min_ago
              
                ):
                    buy = "BUY 1 8-140 copiata e modificata da RCCR che e' arrivata una ndecchia prima del passare del tempo -20>200 - riga 1976 a"
                    action = "buy"
                    percentage = 80
                    
                    # importante : ma100 sta sotto la ma200 non le e' troppo lontana cioe' NON ci troviamo in una situazione drammatica! (anche se ma200< e ma300<)
                    # 20 maggio 2020 messo ma140 prima era ma150
                    # > estate alzato buy
                    
                    
                
                # BUY 1 copiata e modificata da RCCR che e' arrivata una ndecchia prima del passare del tempo.
                
                elif (    
                    ma8_last > ma140_last
                    and deviation_ma100_sopra_ma200 > -0.30
                    and ma20_last < ma200_last
                    and deviation_ma3_sopra_ma10 > 0.24
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
                    buy = "BUY 1 8-140 copiata e modificata da RCCR - 20<200 AND 3-10>0.24 AND 5-28 > 0.18 - riga 2008 b"
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
                    buy = "BUY 1 con ma20_last > ma200_last e con 11 > 59 e ma69> 2 min ago (!) r 2042"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                elif (
                    ma20_last > ma200_last
                    and ma11_last > ma50_last
                    and ma69_last >= ma69_2_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.15
                    and deviation_ma3_sopra_ma7 > 0.05
                    and deviation_ma13_sopra_ma25 > 0.05
                    
                    and deviation_bellissima > 0.13
                    
                    and price >= price_2_min_ago
                    
                ):
                    buy = "BUY 1 con ma20_last > ma200_last e con 11 > 59 e ma69> 2 min ago (!) r 2065"
                    action = "buy"
                    percentage = 80
                    
                    # > estate anticipato buy di una ndecchia
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
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
                    buy = "BUY 1 r913 anticipata e modificata e con 11 > 50 - SOPRA RIALZO RIALZO - GIORNO - r 2109"
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
                    buy = "BUY 1 con 11-69 SE ma200 SALE DA 2 ORE ! - r 2133"
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
                    buy = "BUY 1 con 13>50 and DEVIATION BUY 1 ALTA e ma78> - r 2150"
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
                    buy = "BUY 1 con ma78< and 39>78 and DEVIATION BUY 1 BASSA r 2168"
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

                    buy = "BUY 1 se ma78< - BUY 1 con incrocio 39>78 - r 2188"
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
             
                    buy = "BUY 1 RIALZO IMPROVVISO con ma200 > E 300 > 120 min ago e con > 0.45 SE MA100 MOLTO IN ALTO DA MA300 - r 2216 AA"
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
             
                    buy = "BUY 1 RIALZO IMPROVVISO con ma200 > E 300 > 120 min ago e con > 0.46 - r 2239 AB"
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
             
                    buy = "BUY 1 RIALZO IMPROVVISO con ma200 > E 300 > 120 min ago e con > 0.50 - r 2280 B"
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
              
                    buy = "BUY 1 variazione 1 RIALZO con 20-69 - r 2312"
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

                    buy = "BUY 1 variazione 2 RIALZO con 20-100 - r 2335"
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

                    buy = "BUY 1 variazione 3 RIALZO con 20-200 - r 2358"
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

                    buy = "BUY 1 RIALZO IMPROVVISO con 78 < ( da 1.20 a 1.1 !) sempre tentando di evitare falsi acquisti - r 2392"
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
                    
                    buy = "BUY 1A con ma200> piccola CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo - r 2434 A"
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
                    
                    buy = "BUY 1A con ma200> piccola CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo CON ma28 < E CON 5-28 > 0.13 - r 2458 B"
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

                    buy = "BUY 1 con ma300 > piccola CORREZIONE FIAT che NON E' una grande correzione AUDI e non e' MASERATI e NON E' FERRARI ! - r 2484"
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
                
                
             
                # BUY 1 piccola CORREZIONE FIAT = r 995 RCCR medie mobili lunghe TUTTE IN RIALZO ! ma si verifica una correzione fiat !
                
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
                    
                    buy = "BUY 1 piccola CORREZIONE FIAT = r 995 RCCR medie mobili lunghe TUTTE IN RIALZO ! ma si verifica una correzione fiat ! - r 2527"
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
                    
                    buy = "BUY 1 piccola CORREZIONE FIAT = r 995 RCCR medie mobili lunghe TUTTE IN RIALZO MA ma100 COMINCIA A RIPIEGARE ! correzione fiat ! - r 2555"
                    action = "buy"
                    percentage = 80
                    
                    
             
                ################################################################################################### ecco le 2 CONDIZIONI PIU' PERICOLOSE !
                
               
                # BUY 1 DURANTE UNA CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo ! (MA ma3 > ma150 mi protegge un po')
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
                    and deviation_ma5_sotto_ma300 < -0.65
                    
                    and deviation_correzione > 0.03
                    and deviation_ma5_sopra_ma28 > 0.05
                    
                    and deviation_ma100_sopra_ma300 > -0.30
                    and deviation_ma25_sotto_ma300 < -0.60
                    
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 FIAT 5 DEVE STARE DISTANTE DALLA 300 ! - riga 2575"
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
                    buy = "BUY 1 DURANTE UNA CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo ! ma100<300 ma5 > ma125 - r 2595"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                    
                    
                    
                
                
                # BUY 1 FIAT 5-300 ( ma la ma100 E' ANCORA VICINA alla ma300 !) 
                # ( E ANCHE la ma25 deve stare un po' distante dalla 300 !!! )
                
                elif (
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
                    
                    and deviation_ma5_sotto_ma300 < -0.40
                    and deviation_ma100_sopra_ma300 > -0.30
                    
                    and deviation_correzione > 0.03
                    and deviation_ma25_sotto_ma300 < -0.60
                    
                    and deviation_ma3_sopra_ma10 > 0.22
                    and deviation_ma5_sopra_ma28 > 0.05
                    
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 FIAT 5-300 (MA ma100 E' ANCORA VICINA alla ma300) (E CON ma25 un po' distante dalla ma300) - r 2623"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_ma100_sopra_ma300 significa 100/300 ( ma100 ancora NON SI E' ALLONTANATA TROPPO DALLA ma300 )
                    # deviation_ma25_sotto_ma300 significa che anche ma25 deve andare almeno un po' sotto ma300 (per evitare piccole schegge rialziste !)
                    # 19 set 2022 aggiunto 3-10 > 0.22
                    
                    
                    
                    
                    
                    
                
                    
                    
                    
               
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
                
                    buy = "BUY 1 piccola CORREZIONE FIAT 78>200 = r 701 RCCR ma con rischio ridotto ! 3-10 > 0.12 cazzo ! - r 2651 a"
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
                
                    buy = "BUY 1 piccola CORREZIONE FIAT 78<200 = r 701 RCCR ma con rischio ridotto ! 3-10 > 0.12 cazzo ! AND 5-28>0.12 - r 2673 b"
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
                    buy = "BUY 1 piccola CORREZIONE FIAT che non e' una grande correzione AUDI e non e' un forte ribasso MASERATI e non e' FERRARI ! - r 2694"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    # deviation_ma20_laterale > -0.15 cioe' ma20 ( una ma di breve termine) da ben 60 minuti non perde !
                    
                    # compare prega per me !
                    
                    
                    
                    
                    
                # BUY 1 piccola CORREZIONE FIAT 5-50 che NON E' una grande correzione e non e' un grande ribasso e NON E' un crollo !
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and ma78_last > ma200_last
                    
                    and deviation_ma3_sopra_ma10 > 0.145
                    and ma8_last > ma28_last
                    
                    and deviation_ma100_sopra_ma300 > -0.30
                    
                    and deviation_ma8_sotto_ma100 < -0.50
                    and deviation_buy_crollo_1 > -0.69
                ): 
            
                    buy = "BUY 1 FIAT piccola CORREZIONE 100 VICINA 300  8-28 NO grande correzione NO grande ribasso NO crollo ! 78 > 200 - r 2723"
                    action = "buy"
                    percentage = 70
                    
                    
                
                
                
                
                
                
                # BUY 1 piccola CORREZIONE FIAT ma300 > 300 5 ore con 5-50 che NON E' una grande correzione e non e' un grande ribasso e NON E' un crollo !
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and ma78_last < ma200_last
                    and ma300_last > ma300_301_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.21
                    and deviation_ma3_sopra_ma10 > 0.10
                    
                    and deviation_ma100_sopra_ma300 > -0.40
                    
                    and deviation_ma8_sotto_ma100 < -0.50
                    and deviation_buy_crollo_1 > -0.69
                ): 
            
                    buy = "BUY 1 FIAT ma300 > 300 5 ore con 100 VICINA 300 NO grande correzione NO grande ribasso NO crollo ! 78 < 200  - r 2745a"
                    action = "buy"
                    percentage = 70
                    
                    # 28 giu 2022 se 78 < 200 ho messo 3-10 > 0.24
                    # 23 lug 2022 5-28 > 0.21 deve essere sicura dopo 5 ore di ribasso !
                    
                    
                    
                    
                    
                # BUY 1 piccola CORREZIONE FIAT 5-50 che NON E' una grande correzione e non e' un grande ribasso e NON E' un crollo !
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and ma78_last < ma200_last
                    and ma300_last < ma300_301_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.22
                    and deviation_ma3_sopra_ma10 > 0.25
                    and ma8_last > ma28_last
                    
                    and deviation_ma100_sopra_ma300 > -0.40
                    
                    and deviation_ma8_sotto_ma100 < -0.50
                    and deviation_buy_crollo_1 > -0.69
                ): 
            
                    buy = "BUY 1 FIAT piccola CORREZIONE 100 VICINA 300  8-28 NO grande correzione NO grande ribasso NO crollo ! 78 < 200  - r 2745b"
                    action = "buy"
                    percentage = 70
                    
                    # 28 giu 2022 se 78 < 200 ho messo 3-10 > 0.24 
                    
                    
                    
                    
                    
                    
                    
                    
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
            
                    buy = "BUY 1 FIAT con delta1 < delta2 and 3-10 > 0.05 and 5-28 > 0.20 e con 8-50 e con ma100 LONTANA 300 - r 2773 A"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                elif (    
                    deviation_buy_crollo_1 < -0.27
                    and deviation_buy_crollo_1 > -0.62
                    and ma8_last > ma50_last
                    and ma125_last > ma300_last
                    and ma2_last > ma2_2_min_ago
                
                ):
                    buy = "BUY 1 DURANTE UNA CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo ! condizione RCCR MA 125 > 300 ! - r 2793"
                    action = "buy"
                    percentage = 60
                    
                    
                    
                    
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
            
                    buy = "BUY 1 FIAT con delta1 > delta2 and 3-10 > 0.17 and 5-28 > 0.20 e con 8-50 e con ma100 LONTANA 300 - r 2795 B"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                
                
                
                
                
                # BUY 1 con ma200> piccola CORREZIONE FIAT che NON E' un forte ribasso e NON E' un crollo ! ALTRA RIGA RCCR che e' andata bene.
                
                elif (    
                    
                    ma200_last > ma200_20_min_ago
                    and ma20_last > ma78_last
                    
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
                    
                    buy = "BUY 1 con 200 > con 5-28> 0.165 and ma28_last > ma28_2_min_ago - 20 > 78 - riga 2828 a"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                # BUY 1 con ma200> piccola CORREZIONE FIAT che NON E' un forte ribasso e NON E' un crollo ! ALTRA RIGA RCCR che e' andata bene.
                
                elif (    
                    
                    ma200_last > ma200_20_min_ago
                    and ma20_last < ma78_last
                    
                    and deviation_ma3_sopra_ma10 > 0.17
                    and deviation_ma5_sopra_ma28 > 0.15
                    
                    and ma28_last > ma28_2_min_ago
                    
                    and ma3_last > ma28_last
                    and ma2_last > ma2_2_min_ago
                    
                    and ma100_last > ma200_last
                    and ma200_last > ma300_last
                    
                    and ma100_last > ma100_60_min_ago
                    and ma200_last > ma200_60_min_ago
                    and ma300_last > ma300_60_min_ago
             
                ):    
                    
                    buy = "BUY 1 con 200 > and ma28_last > ma28_2_min_ago - 20 < 78 and dev_ma3_sopra_ma10 > 0.17 con 5-28> 0.15 - riga 2859 b"
                    action = "buy"
                    percentage = 80
                    
                    # > estate anticipato buy di una ndecchiecella
                    
                    
                    
                    
                    
                    
                    
                    
                    
                # BUY 1 che mancava se dopo 300 min di rialzo c'e' una correzione improvvisa 
                
                elif (    
               
                    ma5_last > ma48_last
                    and ma300_last > ma300_300_min_ago
                    
                    and deviation_ma5_sotto_ma300 < -0.70
                    and deviation_ma3_sopra_ma10 > 0.01
                    and deviation_ma5_sopra_ma28 > 0.04
                    
                    and ma2_last > ma2_2_min_ago
                ):    
                    
                    buy = "BUY 1 che mancava se dopo 300 min di rialzo c'e' una correzione improvvisa - riga 2860"
                    action = "buy"
                    percentage = 80
                    
                    # 3 set 5-48 da 5-50
                    # 3 set dev 5-28 0.04 da 0.05
                    
                    
                    
                    
                    
                    
                    
                    
                
                
                
                
                
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
                    
                    buy = "BUY 1 con 200 > con 5-28> 0.19 and ma28_last < ma28_2_min_ago and ma28_last > ma28_30_min_ago - riga 2894"
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
                    
                    buy = "BUY 1 con 200 > con 5-28> 0.19 and ma28_last < ma28_2_min_ago and ma28_last < ma28_30_min_ago - riga 2925"
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
            
                    buy = "BUY 1 CORREZIONE FIAT 5-34 ma con ma5 piu' distante da ma200 - SOTTO RIALZO RIALZO - GIORNO ! - r 2954"
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

                    buy = "BUY 1 con ma200< e ma300< piccola CORREZIONE FIAT che NON E'una grande correzione e NON E' un grande ribasso e NON E' un crollo - r 2979"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                
                # BUY 1 con RIBASSO VELOCE MA la distanza tra ma100 e ma200 si sta riducendo - USANDO UN DOPPIO DELTA ! STA RISALENDO
                
                elif (
                    deviation_ma3 < -1.30
                  
                    
                    and delta_1 < delta_2
                    and ma100_last > ma100_60_min_ago
                    
                    and ma3_last > ma20_last
                ):
                
                    buy = "BUY 1 con RIBASSO VELOCE mentre la distanza tra ma100 e ma200 si sta riducendo - SOTTO RIALZO RIALZO - GIORNO ! - r 2998"
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
                    buy = "BUY 1 grande CORREZIONE AUDI che NON E' FIAT e NON E' MASERATI e NON E' FERRARI ! + deviation_correzione> 0.02 - r 3022"
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
                    
                    and deviation_ma3_sopra_ma10 > 0.09
                    and deviation_ma5_sopra_ma28 > 0.01
                  
                ):
                    buy = "BUY 1 AUDI che NON E' un grande ribasso MASERATI e NON E' un crollo FERRARI ! con deviation trend ma200 - r 3043"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma5_last / ma30_last
                    # deviation_trend_ma200 = ma200_last / ma200_120_min_ago
                    # compare prega per me !
                    
                    # and deviation_correzione_1 > -0.01 significa una ndecchia prima di 5-30 !
                    # 22 set aggiunte 3-10 e 5-28
                
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
                    buy = "BUY 1 FIAT che non funzionava MA CHE HA FUNZIONATO ! SOTTO RIALZO RIALZO - GIORNO ! - r 3086"
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
                    buy = "BUY 1 FIAT OK DOPPIO DELTA STA RISALENDO - SOTTO RIALZO RIALZO - GIORNO ! - r 3120"
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
                    buy = "BUY 1 FIAT 300 > 120 min agocopia BIS della r701 del RCCR che non funzionava e che invece HA FUNZIONATO ! - NOTTE ! ! 8-39 - r 3158"
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
                    buy = "BUY 1 FIAT 300 < 120 min ago copia BIS della r701 del RCCR che non funzionava e che invece HA FUNZIONATO ! - NOTTE ! ! 8-39 - r 3186"
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
                    buy = "BUY 1 FIAT OK (DOPPIO DELTA) RIBASSO ! 8-39  SOTTO RIBASSO RIBASSO  - NOTTE ! - r 3227"
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
                    
                    and deviation_ma3_sopra_ma10 > 0.10
                    and deviation_ma5_sopra_ma28 > 0.01
                    
                    and ma2_last > ma2_2_min_ago
                    and ma78_last < ma200_last
                    
                ):
                    buy = "BUY 1 RIBASSO AUDI A importato dal BUY 2 CON 8 sotto 300 > -1.20 - 5-16 > 0.11 E 5-28 > 0.01 - riga 3264 A"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # questa cosa che 78 deve essere < 200 ha dell' incredibile. MA NON TOCCARE !
                    
                    
                    
                    
                # BUY 1 RIBASSO AUDI B importato dal BUY 2 CON 8 sotto 300 < -1.20
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.70
                    and deviation_buy_crollo_1 > -1.50
                    
                    and deviation_ma8_sotto_ma300 < -1.20
                    
                    and ma5_last > ma25_last
                    and deviation_ma3_sopra_ma10 > 0.19
                    
                    and ma2_last >= ma2_2_min_ago
                    and ma78_last < ma200_last
                    
                ):
                    buy = "BUY 1 RIBASSO AUDI B importato dal BUY 2 CON 8 sotto 300 < -1.20 - 5-25 and 3-10 > 0.19 - riga 3289 B"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # questa cosa che 78 deve essere < 200 ha dell' incredibile. MA NON TOCCARE !
                    # 21 giu 2022 5-18 da 5-20
                    # 21 giu 2022 5-16 da 5-18
                    # 27 giu 2022 5-15 da 5-16
                    # > vacanza 3-10 > 0.19 da 0.15
                    # roma 5-25
                    
                    
                    
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
                    buy = "BUY 1 ultimo e meraviglioso RIBASSO AUDI con 5-16 copiata da RCCR CHE E' ANDATA BENISSIMO e che non e' un crollo !  - riga 3326"
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
                    and deviation_ma5_sopra_ma28 > 0.18
                    
                    and ma2_last > ma2_2_min_ago
                    and ma78_last < ma200_last
                    
                ):
                    buy = "BUY 1 RIBASSO AUDI PIU' LENTA CHE NON E' UN CROLLO ! and delta_1 < delta_2 con dev 5-16 > 0.09 E 5-28 > 0.18 - riga 3354 A"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # questa cosa che 78 deve essere < 200 ha dell' incredibile. MA NON TOCCARE !
                    # ho dovuto aggiungere 5-28 > 0.18 perche' non riesco a fare modifiche con 5-300>-3.00 e 5-300<-3.00
                    # e il compare non risponde
                    
                    
                    
                
                
                
                
                
                # BUY 1 DURANTE UN RIBASSO AUDI PIU' LENTA LENTA copiata da RCCR CHE E' ANDATA BENISSIMO CHE NON E' UN CROLLO ! (compare stammi vicino!)
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.70
                    and deviation_buy_crollo_1 > -1.50
                    and delta_1 > delta_2
                    
                    and ma13_last > ma25_last
                    
                    and ma5_last > ma16_last
                    and deviation_ma5_sopra_ma16 > 0.10
                    
                    and ma2_last > ma2_2_min_ago
                    and ma78_last < ma200_last
                    
                ):
                    buy = "BUY 1 DURANTE UN RIBASSO AUDI PIU' LENTA CHE NON E' UN CROLLO ! and delta_1 > delta_2 con dev 5-16 > 0.10 e 13>25 - riga 3386 B1"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # questa cosa che 78 deve essere < 200 ha dell' incredibile. MA NON TOCCARE !
                    # dev 5-16 c'e' perhe' sto riducendo piano piano
                    
                    # > estate 5-16 0.10 da 0.05
                    
                    
                    
                    
                    
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
                    buy = "BUY 1 RIBASSO AUDI PIU' LENTA CHE NON E' UN CROLLO ! and delta_1 > delta_2 con 4-15 > 0.10 e 13<25 E 3-10 > 0.35 ! - riga 3417 B2"
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
                    buy = "BUY 1 RIBASSO AUDI PIU' GIU' -0.70 E PIU' VELOCE CHE NON E' UN CROLLO ! con deviation 3-16 > 0.46  - riga 3452"
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
                    buy = "copia della riga 530 del RCCR ma piu' prudente ! - BUY GRANDE RIBASSO AUDI CHE NON E' UN CROLLO ! - r 3479"
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
                    buy = "BUY 1 GRANDE RIBASSO MASERATI CHE NON E' UN CROLLO ! con 5-28 - r 3499"
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
                    ma2_last >= ma2_2_min_ago
                    and deviation_buy_crollo_1 < -2.30
                    and ma3_last > ma16_last
                    and deviation_ma3_sopra_ma10 > 0.31
                    and ma78_last < ma300_last
                ):
                    buy = "BUY 1 CROLLO FERRARI 3-16 - modo 1 and ma78_last < ma300_last - r 3525"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # era 3-7 ma MI DISPIACE TANTO ma ho dovuto mettere 3-16
                    # aggiunto 3-10 0.31
                    
                    
                
                
                # BUY 1 CROLLO FERRARI - modo 2 questa condizione e' entrata in azione ! ( e mi e' sembrata ben fatta !)

                elif (
                    ma2_last >= ma2_2_min_ago
                    and deviation_buy_crollo_1 < -1.61
                    and ma5_last > ma18_last
                    and ma78_last < ma300_last
                ):
                    buy = "BUY 1 CROLLO FERRARI - modo 2 and ma78_last < ma300_last - r 3543"
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
                    buy = "BUY 1 crollo MISSILE COMPA 3-13 and ma78_last < ma300_last - r 3561"
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
                    buy = "BUY 1 CROLLO FERRARI - modo 1 and ma78_last > ma300_last - r 3583"
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
                    buy = "BUY 1 CROLLO FERRARI - modo 2 and ma78_last > ma300_last - r 3604"
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
                    buy = "BUY 1 crollo MISSILE COMPA 3-13 and ma78_last > ma300_last - r 3624"
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
                    buy = "BUY 1 ECCEZIONALE - se ma200 sale da 15 min e 69> COMPRA con deviation 4-25 e un po' piu' su della ma100 ! - r 3657"
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
                    
                    and deviation_buy_ma3_sopra_ma25 > 0.08
                    and deviation_ma3_sopra_ma10 > 0.10
                    and deviation_ma5_sopra_ma28 > 0.01
                  
                ):

                    buy = "BUY 1 DOCCIA se ma200 > da 120 min ! COMPRA - r 3680"
                    action = "buy"
                    percentage = 80
                    
                    # > estate 3-25 0.08 da 0.05
                
                
                ############################################################################################################################
                
                
                
                # e non e' ancora una situazione cosi' drammatica.
                
                elif (    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
                    
                    and deviation_ma3_sopra_ma10 > 0.125
                    
                    and ma8_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                
                ):
                    buy = "BUY 1 ribasso AUDI o correzione FIAT che non e' un forte ribasso e non e' un crollo !  - r 3702"
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
                    buy = "BUY 1 CORREZIONE FIAT CHE FA PAURA ! (MA ma100 e ma200 sono ANCORA VICINE alla ma300) (SOTTO cresce diminuisce) AURORA - riga 3749"
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
                    buy = "BUY 1 CORREZIONE FIAT CHE FA PAURA ! (MA ma100 e ma200 sono ANCORA VICINE alla ma300) (SOTTO RIBASSO RIBASSO ) NOTTE ! - riga 3783"
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
                    and deviation_ma3_sopra_ma10 > 0.155
                ):
                    buy = "BUY 1 CROLLO FERRARI ok CON 3-10 necessaria ! - RCCR - r 3813"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_buy_crollo_2 = ma3_last / ma13_last
                    # fondamentale aggiunta 3-10 perche' anche ferrari NE HA BISOGNO ma non 5-28 CHE COMINCIA AD ESSERE INAPPROPRIATA
                    # 27 giu 2022 3-10 0.155 NON MENO DI QUESTA PERDIO !
                    
                    
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
                    buy = "BUY 1 SUL SUPPORTO 300 ! - r 3837"
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
                    buy = "BUY 1 dopo ribasso MA CON TUTTE LE MA > e con incrocio al rialzo 8-140 - r 3864"
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
                    buy = "BUY 1 CHE MANCAVA ! con incrocio 11-50 AND 5-28 > 0.265 (!) ( CON 100 < AND 200 < AND 300 < ) (!)  - r 3896"
                    action = "buy"
                    percentage = 80
                    
                    # madonna compa !
                    
                    
                    
                    
                    
                    
                    
                    
                    
                # BUY 1 CHE MANCAVA DOPO BUY-SELL CROLLO ! 150-100 GIORNO ! E 50 > 100
                
                elif (
                    
                    deviation_ma5_sotto_ma300 > -0.40
                    
                    and deviation_ma5_sopra_ma28 > 0.18
                    and deviation_ma3_sopra_ma10 > 0.10
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
                    buy = "BUY 1 78>200 che mancava DOPO BUY-SELL e nuovo CROLLO ! 50 > 100 AND 150-100 GIORNO ! and 5-28 > 0.18 and 3-10 > 0.10 - r 3935 A1"
                    action = "buy"
                    percentage = 80
                    
                    # > estate 5-28 > 0.18 da 0.12 and 3-10 > 0.10 da 0.05
                    
                    
                    
                    
                    
                    
                # BUY 1 CHE MANCAVA DOPO BUY-SELL CROLLO ! delta 150-100 GIORNO ! E 50 > 100
                
                elif (
                    deviation_ma5_sotto_ma300 < -0.40
                    and ma8_last > ma50_last
                    
                    and deviation_ma5_sopra_ma28 > 0.15
                    and deviation_ma3_sopra_ma10 > 0.10
                    
                 
                    and ma50_last > ma100_last
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and ma100_last < ma100_120_min_ago
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and delta_150_100 < delta_150_100_60_min
                    
                    and ma2_last >= ma2_2_min_ago
              
                ):
                    buy = "BUY 1 78 > 200 che mancava DOPO BUY-SELL e nuovo CROLLO ! 50 > 100 AND delta 150-100 GIORNO ! and 3-10 > 0.10 and 5-28 > 0.15 - r 3968 A2"
                    action = "buy"
                    percentage = 80
                    
                    # > estate 5-28 0.15 e 3-10 0.10
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                # BUY 1 CHE MANCAVA DOPO BUY-SELL CROLLO ! 150-100 GIORNO ! E 50 > 100
                
                elif (
                    deviation_ma5_sopra_ma28 > 0.18
                    and deviation_ma3_sopra_ma10 > 0.15
                    and ma78_last < ma200_last
                    
                    and ma50_last > ma100_last
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and ma100_last < ma100_120_min_ago
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and delta_150_100 < delta_150_100_60_min
                    and ma100_last > ma100_3_min_ago
                    
                    and ma2_last >= ma2_2_min_ago
                
                ):
                    buy = "BUY 1 78<200 CHE MANCAVA DOPO BUY-SELL CROLLO ! 50 > 100 AND 150-100 GIORNO ! and 3-10 > 0.15 and 5-28 > 0.18 - r 4005 b"
                    action = "buy"
                    percentage = 80
                    
                    # madonna compa ! 
                    # the sound of silence
                    # ASSURDO ! questa 100 > 100 3 min e' incredibile ! si e' verificata dopo il BUY-SELL del crollo ! NON TOCCARE
                    # SI STA RIDUCENDO LA DISTANZA TRA 150 E 100
                    
                    # 10 giu 2022 5-28 0.12 da 0.09 cazzo
                    #  2 lug 2022 3-10 0.15 da 0.05 cazzo
                    # > estate 5-28 0.18 da 0.12 e 3-10 0.15 da 0.05 HO ALZATO IL BUY !
                    
                    
                    
                    
                    
                    
                    
                    
                    
                # BUY 1 CHE MANCAVA DOPO 5 ore di ribasso
                
                elif (
                    deviation_ma5_sopra_ma28 > 0.16
                    and deviation_ma3_sopra_ma10 > 0.07
                    and deviation_ma100_laterale > -0.80
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and ma100_last < ma100_301_min_ago
                    and ma200_last < ma200_301_min_ago
                    and ma300_last < ma300_301_min_ago
                    
                    and deviation_ma300__diviso_ma300_5_ore_ago < -0.25
                    and deviation_ma5_sotto_ma300 < -0.43
                    
                    and ma2_last > ma2_2_min_ago
                
                ):
                    buy = "BUY 1 CHE MANCAVA DOPO 5 ore di ribasso con 5-28 > 0.16 se entra dopo 5 ore deve essere piu' sicuro MA 5 non lontana da 100 - r 4040 A"
                    action = "buy"
                    percentage = 80
                    
                    # > estate anticipata ndecchiecella 5-28 0.17 da 0.20
                    # aggiunta 3-10 > 0.07
                    # 5-28 0.16 da 0.17 (adesso c'e' anche 3-10)
                    
                    
                # BUY 1 CHE MANCAVA DOPO 5 ore di ribasso
                
                elif (
                    deviation_ma5_sopra_ma28 > 0.22
                    and deviation_ma100_laterale < -0.80
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and ma100_last < ma100_301_min_ago
                    and ma200_last < ma200_301_min_ago
                    and ma300_last < ma300_301_min_ago
                    
                    and deviation_ma300__diviso_ma300_5_ore_ago < -0.25
                    and deviation_ma5_sotto_ma300 < -0.43
                    
                    and ma2_last > ma2_2_min_ago
                
                ):
                    buy = "BUY 1 CHE MANCAVA DOPO 5 ore di ribasso con 5-28> 0.22 se entra dopo 5 ore deve essere piu' sicuro CON 5 molto lontana da 100- r 4040 B"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                 
                # BUY 1 CHE MANCAVA DOPO BUY-SELL CROLLO ! 150-100 GIORNO ! MA 50 < 100
                
                elif (
                    deviation_ma5_sopra_ma28 > 0.18
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
                    buy = "BUY 1 CHE MANCAVA DOPO BUY-SELL CROLLO ! 50 < 100 AND 150-100 GIORNO ! and 3-10 > 0.25 and 5-28 > 0.18 - r 4042"
                    action = "buy"
                    percentage = 80
                    
                    # madonna compa ! 
                    # the sound of silence
                    # ASSURDO ! questa 100 > 100 3 min e' incredibile ! si e' verificata dopo il BUY-SELL del crollo ! NON TOCCARE
                    # SI STA RIDUCENDO LA DISTANZA TRA 150 E 100
                    
                    # 10 giu 2022 5-28 0.12 da 0.09 cazzo
                    # 21 giu 2022 3-10 > 0.25 da > 0.05 CAZZO
                    # 29 ago 5-28 0.18
                    
                    
                    
                    
                    
                    
                    
                    
                
                    
                    
                    
                    
                    
                    
                    
                    
                

                    
                    
                    
                    
                    
                    
                    
                # BUY 1 che ci riprova quando se ne va lateralmente dopo il crollo
                
                elif (
                    ma5_last > ma300_last
                    and ma8_last > ma50_last
                    
                    and deviation_ma3_sopra_ma10 > 0.155
                    and deviation_ma5_sopra_ma28 > 0.01
                    
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and delta_300_100 < delta_300_100_60_min
                    
                    and deviation_ma100_sopra_ma300 > -0.40
                    and deviation_ma200_sopra_ma300 > -0.40
                    
                    and ma2_last > ma2_2_min_ago
                
                ):
               
                    buy = "BUY 1 che ci riprova quando se ne va lateralmente dopo il crollo - r 4082 A1"
                    action = "buy"
                    percentage = 80

                    # compare prega per me !
                    
                    
                    
                # BUY 1 che ci riprova quando se ne va lateralmente dopo il crollo
                
                elif (
                    ma28_last > ma300_last
                    and ma20_last < ma50_last
                    
                    and deviation_ma3_sopra_ma10 > 0.155
                    and deviation_ma5_sopra_ma28 > 0.40
                    
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and delta_300_100 < delta_300_100_60_min
                    
                    and deviation_ma100_sopra_ma300 > -0.40
                    and deviation_ma200_sopra_ma300 > -0.40
                    
                    and ma2_last > ma2_2_min_ago
                
                ):
               
                    buy = "BUY 1 che ci riprova quando se ne va lateralmente dopo il crollo - r 4111 A2"
                    action = "buy"
                    percentage = 80

                    # compare prega per me !
                    # 6 luglio 2022 SE 20 < 50 5-28 > 0.40 ! NON TOCCARE
                    
                    
                    
                    
                # BUY 1 che ci riprova quando se ne va lateralmente dopo il crollo
                
                elif (
                    ma28_last < ma300_last
                    and deviation_ma3_sopra_ma10 > 0.17
                    and deviation_ma5_sopra_ma28 > 0.20
                    
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and delta_300_100 < delta_300_100_60_min
                    
                    and deviation_ma100_sopra_ma300 > -0.40
                    and deviation_ma200_sopra_ma300 > -0.40
                    
                    and ma2_last >= ma2_2_min_ago
                
                ):
               
                    buy = "BUY 1 che ci riprova quando se ne va lateralmente dopo il crollo - SE 28 < 300 3-10 > 0.21- r 4138 b"
                    action = "buy"
                    percentage = 80

                    # 2 lug 2022 3-10 0.21 da 0.22
                    
                    # > estate 3-10 0.17 e 5-28 0.20 DOVEVO ALZARE IL BUY quando se ne va lateralmente dopo il crollo
                    
                    
                ##################################################################################### esperimento ! andato male ! avevo messo
                
                # 5-28 piu' alto nella prima condizione ( che mi copriva e mi faceva comprare sicuramente )
                # incrocio al rialzo e ma2 > ma2 2 min ago (che mi faceva comprare al secondo tentativo)
                
                ######################################################################################
                
                # BUY 1 CHE MANCAVA aggressiva - (SEMBRA pari al BUY DURANTE UN RIBASSO AUDI !)
                
                elif (
                    ma5_last < ma33_last
                    
                    and deviation_ma3_sopra_ma10 > 0.085
                    and deviation_ma5_sopra_ma28 > 0.11
                    
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
                    buy = "BUY 1 pari al BUY AUDI CHE MANCAVA ! con 5-33 () 3-10 > 0.085 e 5-28 0.11 - r 4166"
                    action = "buy"
                    percentage = 80
                    
                    # madonna compa che ti sei dimenticato di me !
                    # 18 set 5-33 e 3-10 > 0.085
                    # 20 set 3-10 > 0.085 da 0.09
                    # 22 set ho aggiunto 5-28 > 0.11
                
            
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
                    
                    buy = "BUY 1 con 200 > 200 20 min ago (100 < and 200 < MA 300 >) and 13-200 !  - riga 4190"
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
                    
                    buy = "BUY 1 SITUAZIONE TREND LATERALE che mancava con ma300 > - GIORNO ! and 5-28 > 0.14 con 28>28 30 min ago - riga 4215 A"
                    action = "buy"
                    percentage = 80
                    
                    # ho aggiunto 5-28 > 0.05
                    # cosa curiosa SEMBRA CHE and ma2_last > ma2_2_min_ago abbia fatto ritardare questo BUY.
                    # ho tenuto i 2 minuti e ho ridotto 5-28
                    
                    
                    
                    
                # BUY 1 SITUAZIONE TREND LATERALE che mancava con ma300 > - DOPPIO DELTA - RIALZO
                
                elif (    
               
                    ma8_last > ma300_last
                    and ma78_last > ma100_last
                    and ma300_last > ma300_301_min_ago
                    
                    and ma100_last > ma200_last
                    and ma100_last > ma300_last
                    
                    and ma28_last < ma28_30_min_ago
                    
                    and delta_1 < delta_2
                    and ma100_last > ma100_60_min_ago
                    
                    and ma300_last > ma300_60_min_ago
                    
                    and deviation_ma3_sopra_ma10 > 0.17
                    and deviation_ma5_sopra_ma28 > 0.10
                    and ma2_last >= ma2_2_min_ago
                ):    
                    
                    buy = "BUY 1 SITUAZIONE TREND LATERALE con ma300 > - GIORNO ! and 5-28 > 0.14 MA 28 < 28 30 min ago AND 3-10 > 0.17 e 300 >5 ore! - r 4246 B1x"
                    action = "buy"
                    percentage = 80
                    
                    # ho aggiunto 5-28 > 0.05
                    # cosa curiosa SEMBRA CHE and ma2_last > ma2_2_min_ago abbia fatto ritardare questo BUY.
                    # ho tenuto i 2 minuti e ho ridotto 5-28
                    # > estate 3-10 0.17 da 0.07 e 5-28 0.10 da 0.06
                    
                    
                # BUY 1 SITUAZIONE TREND LATERALE che mancava con ma300 > - DOPPIO DELTA - RIALZO
                
                elif (    
               
                    ma8_last > ma300_last
                    and ma78_last > ma100_last
                    and ma300_last < ma300_301_min_ago
                    
                    and ma100_last > ma200_last
                    and ma100_last > ma300_last
                    
                    and ma28_last < ma28_30_min_ago
                    
                    and delta_1 < delta_2
                    and ma100_last > ma100_60_min_ago
                    
                    and ma300_last > ma300_60_min_ago
                    
                    and deviation_ma3_sopra_ma10 > 0.17
                    and deviation_ma5_sopra_ma28 > 0.10
                    and ma2_last > ma2_2_min_ago
                ):    
                    
                    buy = "BUY 1 SITUAZIONE TREND LATERALE con ma300 > - GIORNO !  MA 28 < 28 30 min ago AND 3-10 > 0.17 and 5-28 > 0.09 e 300 < 5 ore !- r 4246 B1y"
                    action = "buy"
                    percentage = 80
                    
                    # ho aggiunto 5-28 > 0.05
                    # cosa curiosa SEMBRA CHE and ma2_last > ma2_2_min_ago abbia fatto ritardare questo BUY.
                    # ho tenuto i 2 minuti e ho ridotto 5-28
                    
                    # > estate aumentati 3-10 e 5-28
                    
                    
                    
                    
                    
                # BUY 1 SITUAZIONE TREND LATERALE che mancava con ma300 > - DOPPIO DELTA - RIALZO
                
                elif (    
               
                    ma8_last > ma300_last
                    and ma78_last < ma100_last
                    
                    and ma100_last > ma200_last
                    and ma100_last > ma300_last
                    
                    and ma28_last < ma28_30_min_ago
                    
                    and delta_1 < delta_2
                    and ma100_last > ma100_60_min_ago
                    
                    and ma300_last > ma300_60_min_ago
                    
                    and deviation_ma3_sopra_ma10 > 0.17
                    and deviation_ma5_sopra_ma28 > 0.14
                    and ma2_last >= ma2_2_min_ago
                ):    
                    
                    buy = "BUY 1 SITUAZIONE TREND LATERALE con ma300 > - GIORNO ! and 5-28 > 0.14 MA 28 < 28 30 min ago AND 3-10 > 0.17 - riga 4278 B2"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                    
                    
                    
                # BUY 1 SITUAZIONE TREND LATERALE modo A che mancava con ma300 < - DOPPIO DELTA - RIALZO
                
                elif (    
               
                    ma8_last > ma200_last
                    and deviation_ma5_sotto_ma300 > 0.40
                    
                    and ma100_last > ma200_last
                    and ma100_last > ma300_last
                 
                    and delta_1 < delta_2
                    and ma100_last > ma100_60_min_ago
                    and ma300_last < ma300_60_min_ago
           
                    and deviation_ma5_sopra_ma28 > 0.13
                    and ma2_last >= ma2_2_min_ago
                ):    
                    
                    buy = "BUY 1 SITUAZIONE TREND LATERALE modo A che mancava con ma300 < - SOPRA RIALZO RIALZO - GIORNO ! and 5-28 > 0.13 - riga 4301 A"
                    action = "buy"
                    percentage = 80
                    
                    # 3 set modo a
                    
                    
                    
                    
                # BUY 1 SITUAZIONE TREND LATERALE modo B che mancava con ma300 < - DOPPIO DELTA - RIALZO
                
                elif (    
               
                    ma8_last > ma200_last
                    and deviation_ma5_sotto_ma300 < 0.40
                    and deviation_ma5_sotto_ma300 > -0.30
                   
                    and ma100_last > ma200_last
                    and ma100_last > ma300_last
                 
                    and delta_1 < delta_2
                    and ma100_last > ma100_60_min_ago
                    and ma300_last < ma300_60_min_ago
                    
                    and deviation_ma3_sopra_ma10 > 0.08
                    and deviation_ma5_sopra_ma28 > 0.17
                    and ma2_last >= ma2_2_min_ago
                ):    
                    
                    buy = "BUY 1 SITUAZIONE TREND LATERALE modo B che mancava con ma300 < - SOPRA RIALZO RIALZO - GIORNO ! and 5-28 > 0.17 - riga 4301 B"
                    action = "buy"
                    percentage = 80
                    
                    # 3 set modo b
                    # 14 set aggiunta 3-10 > 0.08
                    
                    
                # BUY 1 SITUAZIONE TREND LATERALE modo C che mancava con ma300 < - DOPPIO DELTA - RIALZO
                
                elif (    
               
                    ma8_last > ma200_last
                    and deviation_ma5_sotto_ma300 < -0.30
                    
                    and ma100_last > ma200_last
                    and ma100_last > ma300_last
                 
                    and delta_1 < delta_2
                    and ma100_last > ma100_60_min_ago
                    and ma300_last < ma300_60_min_ago
           
                    and deviation_ma5_sopra_ma28 > 0.12
                    and ma2_last >= ma2_2_min_ago
                ):    
                    
                    buy = "BUY 1 SITUAZIONE TREND LATERALE modo C che mancava con ma300 < - SOPRA RIALZO RIALZO - GIORNO ! and 5-28 > 0.12 - riga 4301 C"
                    action = "buy"
                    percentage = 80
                    
                    # 3 set modo c
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                # BUY 1 forever young 1 PIU' PRUDENTE se ma200 > e se ma200 > ma300 - che si preoccupa degli effetti laterali
                
                elif (  
                    ma200_last > ma300_last
                    and ma300_last > ma300_120_min_ago
                    
                    and ma78_last > ma100_last
                    and deviation_ma100_laterale > 0.18
                    and ma200_last > ma200_15_min_ago
                    and deviation_ma5_sopra_ma28 > 0.08
                    
                    and ma3_last >= ma11_last
                    
                    and ma10_last >= ma10_2_min_ago
                    and ma2_last >= ma2_2_min_ago
                ):

                    buy = "BUY 1 forever young 1 con 300 > 120 min ago PIU' PRUDENTE se ma 200 > e se ma200 > ma300 - si preoccupa degli effetti laterali - r 4325"
                    action = "buy"
                    percentage = 80
                    
                    # la troppa prudenza qualche volta genera perdite
                    
                    
                    
                
                    
                    
                    
                    
                    
              
                # BUY 1 forever young 1 PIU' PRUDENTE se ma 200 > e se ma200 > ma300 AND 78 > 200
                
                elif (  
                    ma200_last > ma300_last
                    and deviation_ma100_laterale > 0.12
                    and ma200_last > ma200_15_min_ago
                    and ma78_last > ma200_last
                    
                    and deviation_ma3_sopra_ma10 > 0.035
                    and deviation_ma5_sopra_ma28 > 0.09
                    
                    and ma78_last < ma100_last
                    
                    and ma11_last > ma200_last
                    
                    
                    
                    and ma3_last > ma11_last
                    and ma5_last > ma200_last
                    
                    and ma2_last > ma2_2_min_ago
                ):

                    buy = "BUY 1 forever young 1 PIU' PRUDENTE se ma 200 > e se ma200 > ma300 AND 78 > 200 - r 4353 A"
                    action = "buy"
                    percentage = 80
                    
                    # 1 ott 2022 3-10 > 0.035
                    
                    
                
                    
                    
                    
                    
                    
                    
                # BUY 1 forever young 1 PIU' PRUDENTE se ma 200 > e se ma200 > ma300 AND 78 < 200 
                
                elif (  
                    ma200_last > ma300_last
                    and ma78_last < ma200_last
                    and ma300_last > ma300_120_min_ago
                    
                    and deviation_ma3_sopra_ma10 > 0.10
                    and deviation_ma5_sopra_ma28 > 0.03
                    
                    and ma78_last < ma100_last
                    and deviation_ma100_laterale > 0.07
                    and ma11_last > ma200_last
                    and ma200_last > ma200_15_min_ago
                    
                    
                    and ma3_last > ma11_last
                    and ma4_last > ma100_last
                    
                    and ma2_last >= ma2_2_min_ago
                ):

                    buy = "BUY 1 forever young 1 USATA MOVIMENTO LATERALE se ma 200 > e se ma200 > ma300 AND 78 < 200 AND 3-10 > 0.10 e 300>120 min ago - r 4379 B1"
                    action = "buy"
                    percentage = 80
                    
                    # la troppa prudenza qualche volta genera perdite !
                    # RCCR r1852 e' arrivata una ndecchia prima. studia le piccole differenze.
                    # 30 set 3-10 a 0.10 da 0.04
                    
                    
                    
                    
                # BUY 1 forever young 1 PIU' PRUDENTE se ma 200 > e se ma200 > ma300 AND 78 < 200 
                
                elif (  
                    ma200_last > ma300_last
                    and ma78_last < ma200_last
                    and ma300_last < ma300_120_min_ago
                    
                    and deviation_ma3_sopra_ma10 > 0.07
                    and deviation_ma5_sopra_ma28 > 0.09
                    
                    and ma78_last < ma100_last
                    and deviation_ma100_laterale > 0.12
                    and ma11_last > ma200_last
                    and ma200_last > ma200_15_min_ago
                    
                    
                    and ma3_last > ma11_last
                    and ma5_last > ma200_last
                    
                    and ma2_last > ma2_2_min_ago
                ):

                    buy = "BUY 1 forever young 1 PIU' PRUDENTE se ma 200 > e se ma200 > ma300 AND 78 < 200 AND 3-10 > 0.07 e 300<120 min ago- r 4379 B2"
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
                    
                    and deviation_ma3_sopra_ma10 > 0.07
                    and deviation_ma5_sopra_ma28 > 0.01
                 
                    and ma6_last > ma6_2_min_ago
                    and ma13_last > ma69_last
                    and ma13_last > ma13_2_min_ago
                    and ma2_last > ma2_2_min_ago
                ):
                    
                    buy = "BUY 1 FOREVER YOUNG PIU' AGGRESSIVO (doppio delta < 1 E 100> ) (SOPRA RIALZO RIALZO) - GIORNO - se ma 200 > e se ma200 > ma300 - r 4410"
                    action = "buy"
                    percentage = 80
                    
                    # SITUAZIONE : dopo crollo e dopo primo grande ribalzo riprende a scendere 
                    # MA ma100 e' intanto andata > ma200 !
                    # e anche ma200 sta sopra ma300
                    
                
                
                # BUY 1 NEW FOREVER YOUNG piccola CORREZIONE FIAT - ALTRA RIGA RCCR che e' andata bene.
                
                elif (    
                    
                    ma200_last > ma200_20_min_ago
                    and ma3_last > ma28_last
                    
                    and deviation_ma3_sopra_ma10 > 0.07
                    
                    and ma100_last > ma200_last
                    and ma200_last > ma300_last
                    
                    and ma100_last > ma100_60_min_ago
                    and ma200_last > ma200_60_min_ago
                    and ma300_last > ma300_60_min_ago
                    
                    and ma2_last > ma2_2_min_ago
                 
                ):    
                    
                    buy = "BUY 1 NEW FOREVER YOUNG piccola CORREZIONE FIAT - ALTRA RIGA RCCR che e' andata bene - riga 4411"
                    action = "buy"
                    percentage = 40
                    
                    # 13 set aggiunte 3-10 and 5-28
                    # se sta molto in alto per comprare 5 deve incrociare dal basso con la 100 ed avere 3-10 > 0.11 vedi ore 12:06 del 26 set 2022
                    # VA IN CONFLITTO. aalora ho lasciato solo 3-10 > 0.11
                    # BUY 1 correzione FIAT con riga 1384 RCCR + 3-10 - altra riga RCCR che e' andata bene.
                    # vedi 30 set ore 18:26 RCCR riga 1384
                    # in MADDOG ho aggiunto 3-10 > 0.07 e lasciato 3-28 
                    
                
                
                    
                
                
                
                    
                    
                    
                    
                
                    
                    
                    
                    
                # BUY 1 FOREVER YOUNG PRUDENTE se ma 200 > e se ma200 > ma300 con doppio delta > 1 (ribasso) and deviation_ma5_sopra_ma28 > 0.30
                
                elif (  
                    ma200_last > ma300_last
                    and ma300_last > ma300_120_min_ago
                    and ma200_last > ma200_15_min_ago
                    and deviation_ma100_laterale < -0.60
                    
                    and delta_1 > delta_2
                    and ma100_last < ma100_60_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.17
                    
                    and ma6_last > ma6_2_min_ago
                    and ma8_last > ma54_last
                    and ma13_last > ma13_2_min_ago
                    and ma2_last > ma2_2_min_ago
             
                ):
                    
                    buy = "BUY 1 FOREVER YOUNG - NOTTE - MA 300 > 120 min ago and dev_ma5_sopra_ma28 > 0.30 se ma 200 > e se ma200 > ma300 - r 4440 A1"
                    action = "buy"
                    percentage = 80
                    
                    # dev 100 laterale significa che 5 deve essere distante dalla 100
                    # 24 set vuoi comprare di notte ? allora dev 5-100 = dev 100 laterale deve essere distante di almeno - 0.60 (distanza della 5 dalla 100 !)
                    
                    
                    
                
                    
                    
                
                    
                    
                    
                    
                    
                # BUY 1 FOREVER YOUNG PRUDENTE se ma 200 > e se ma200 > ma300 con doppio delta > 1 (ribasso) and deviation_ma5_sopra_ma28 > 0.30
                
                elif (  
                    ma200_last > ma300_last
                    and ma300_last < ma300_60_min_ago
                    and deviation_ma3_sopra_ma10 > 0.22
                    
                    and ma200_last > ma200_15_min_ago
                 
                    and delta_1 > delta_2
                    and ma100_last < ma100_60_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.30
                
                    and ma6_last > ma6_2_min_ago
                    and ma13_last > ma69_last
                    and ma13_last > ma13_2_min_ago
                    and ma2_last > ma2_2_min_ago
                ):
                    
                    buy = "BUY 1 FOREVER YOUNG PRUDENTE SOPRA RIBASSO RIBASSO - NOTTE - and dev_ma5_sopra_ma28 > 0.30 se ma 200 > e se ma200 > ma300 - r 4440 B"
                    action = "buy"
                    percentage = 80
                    
            
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
                    and deviation_correzione > 0.03
                    
                    and deviation_ma3_sopra_ma10 > 0.16
                    and deviation_ma5_sopra_ma28 > 0.11
                    
                    and ma100_last < ma100_120_min_ago
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and deviation_ma100_sopra_ma300 <-2.30
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 DURANTE UNA CORREZIONE FIAT da r701 RCCE ho dovuto metterla ! con deviation_correzione > 0.03 MA 100 lontana da 300 ! - riga 4485"
                    action = "buy"
                    percentage = 80
                    
                    # 100 sopra 300 MA IN REALTA' STA SOTTO.
                    # 100 lontana da 300
                    # 100< 200< 300< da oltre 120 min
                    
                    # deve essere cosi' altrimenti la r701 RCCR genera molte perdite.
                    # ma il 9 maggio 2022 RCCR ha comprato in situazione DRAMMATICA ed e' andata benissimo mentre MADDOG DORMIVA.
                    # 14 set 2022 ho aggiunto 3-10 e 5-28
                    
                    
                    
                
                # BUY 1 piccola CORREZIONE FIAT CHE FA PAURA ! ( ma la ma100 E' ANCORA VICINA alla ma300 !) NON TOCCARE 5-28 > 0.10 !
                # ( E ANCHE la ma25 deve stare un po' distante dalla 300 !!! )
                
                elif (
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    
                    and deviation_correzione > 0.03
                    and deviation_ma5_sopra_ma28 > 0.05
                    
                    and ma78_last > ma100_last
                    and ma200_last > ma300_last
                    and deviation_ma100_sopra_ma300 > -0.30
                    and deviation_ma25_sotto_ma300 < -0.60
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 FIAT (MA ma100 ANCORA VICINA alla ma300 e 200 e' ancora sopra 300) (E CON ma25 un po' distante da ma300) 50% 78>100 - riga 4514 A"
                    action = "buy"
                    percentage = 50
                    
                    # deviation_ma100_sopra_ma300 significa 100/300 ( ma100 ancora NON SI E' ALLONTANATA TROPPO DALLA ma300 )
                    # ma200 sta ancora sopra ma300 !
                    # deviation_ma25_sotto_ma300 significa che anche ma25 deve andare almeno un po' sotto ma300 (per evitare piccole schegge rialziste !)
                    # NON TOCCARE 5-28 > 0.05 !
                    
                    
                    
                    
                    
                # BUY 1 piccola CORREZIONE FIAT CHE FA PAURA ! ( ma la ma100 E' ANCORA VICINA alla ma300 !) NON TOCCARE 5-28 > 0.10 !
                # ( E ANCHE la ma25 deve stare un po' distante dalla 300 !!! )
                
                elif (
                    deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    
                    and deviation_correzione > 0.03
                    and deviation_ma5_sopra_ma28 > 0.19
                    
                    and ma78_last < ma100_last
                    and deviation_ma3_sopra_ma10 > 0.12
                    and ma200_last > ma300_last
                    and deviation_ma100_sopra_ma300 > -0.30
                    and deviation_ma25_sotto_ma300 < -0.60
                    and ma2_last > ma2_2_min_ago
                ):
                    buy = "BUY 1 FIAT (MA ma100 ANCORA VICINA alla ma300 e 200 e' ancora >300) (E CON ma25 distante da ma300) 50% E 78<100 E 3-10 > 0.15 - r 4514 B"
                    action = "buy"
                    percentage = 50
                    
                    # deviation_ma100_sopra_ma300 significa 100/300 ( ma100 ancora NON SI E' ALLONTANATA TROPPO DALLA ma300 )
                    # ma200 sta ancora sopra ma300 !
                    # deviation_ma25_sotto_ma300 significa che anche ma25 deve andare almeno un po' sotto ma300 (per evitare piccole schegge rialziste !)
                    # NON TOCCARE 5-28 > 0.05 !
                    
                    # > estate 5-28 0.19 da 0.05 e 3-10 0.15 da 0.10
                
                
                
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
                    buy = "BUY 1 con DEVIATION ASSURDA se ma200 > da 120 min COMPRA con INCROCIO ma8 ma200 (ma5>ma300 evita gli EFFETTI LATERALI) - r 4542"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_assurda = price / ma200_last
                    
                    
                
                
                # BUY 1 5 LUGLIO 2022 ma100 sotto ma300 di almeno -0.90 ! E CON 3-10 > 0.12
                
                elif (
                    
                    deviation_ma100_sopra_ma300 < -0.90
                    and ma8_last > ma50_last
                    and deviation_ma3_sopra_ma10 > 0.16
                    
                    and ma100_last < ma100_120_min_ago
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and ma2_last > ma2_2_min_ago
                    and price > price_2_min_ago
                    
                ):
                    buy = "BUY 1 5 LUGLIO 2022 ma100 sotto ma300 di almeno -0.90 ! 3-10 > 0.12 - r 4570"
                    action = "buy"
                    percentage = 70

                    # 22 lug 2022 3-10 0.16 da 0.12 cazzo
                    
                    
                    
                    
                # BUY 1 DURANTE UN RIBASSO AUDI con 5-16 copiata da RCCR CHE E' ANDATA BENISSIMO ! 22 ago 2022
                
                elif (
                    
                    deviation_ma5_sopra_ma16 > 0.20
                    
                    and deviation_buy_crollo_1 < -0.60
                    and deviation_buy_crollo_1 > -1.60
                    
                    and ma78_last < ma200_last
                    and ma2_last > ma2_2_min_ago
                  
                ):
                    buy = "BUY 1 DURANTE UN RIBASSO AUDI con 5-16 copiata da RCCR CHE E' ANDATA BENISSIMO ! 22 ago 2022 - riga 4571"
                    action = "buy"
                    percentage = 50
                    
                    # 14 sett dev 5-16 ho dovuto purtroppo portarla a 0.20 da 0.10 dopo il crollo del 13 set
                    # non e' partita ferrari
                    # non riesco a fare 5-300 > -3.00 e 5-300 < -3.00 che casino ! il compare non risponde
                    
                    
                
                    
                    
                    
                    
                    
                    
                    
                
                    
                    
                    
                    
                    
                # BUY 1 CROLLO IMPROVVISO e RISALITA SUPERVELOCE - la piu' pericolosa d tutte ! - BUY con il 30% - dovrebbe evitarmi il "buy alto"

                elif (    
                    
                    price >= ma3_last
                    
                    and ma100_last > ma300_last
                    
                    and deviation_ma3_sotto_ma100 < -1.70
                    and deviation_ma3_sotto_ma300 < -1.60
                    
                    and deviation_ribasso_e_rialzo_velocissimo_1 < -1.50
                    and deviation_ribasso_e_rialzo_velocissimo_2 > -0.50
                    
                    and deviation_ma100_sopra_ma300 < 0.40
                    
               
                ):
                    buy = "BUY 1 CROLLO IMPROVVISO e RISALITA SUPERVELOCE - la piu' pericolosa d tutte ! - BUY con il 30% - dovrebbe evitarmi il buy alto - r 4598"
                    action = "buy"
                    percentage = 30
                    
                    
                    # deviation_ribasso_e_rialzo_velocissimo_1 = price / price_10_min_ago
                    # deviation_ribasso_e_rialzo_velocissimo_2 = price / price_2_min_ago
                    
                    # importante : il prezzo puo' essere anche piu' basso del prezzo di 2 min ago ! - fidati - 
                    # in questa circostanza ma2 arriva tardissimo !
                    # se 100 > 300 NON E' UN CROLLO !
                    
                    # and deviation_ma100_sopra_ma300 < 0.40 significa che CON QUESTE CONDIZIONI COSI' AGGRESSIVE 
                    # NON COMPRA mentre scende precipitosamente dopo un grandissimo rialzo !
                    # potra' anche farlo ma considerando il 3-10 e il 5-28
                    
                    # Manchester Orchestra - I Know How To Speak
                  
            
            #############################################################################################################      COMPRA sessione 2
            
            elif self.session == 2:
                
                if (
                    ma69_last > ma69_2_min_ago
                    and deviation_ma100_sopra_ma300 > 0.20
                    and ma78_last > ma200_last
                    
                    and deviation_buy2 > 0.03
                    and deviation_bellissima > 0.151
                    and deviation_buy_ma3_sopra_ma13 > 0.09
                    and deviation_ma7_sopra_ma40 > 0.05
                    and ma2_last > ma2_2_min_ago
                    and price > price_2_min_ago
                    and ma3_last > ma40_last
                ):
                    buy = "BUY 2A rialzo o laterale con 78 > 200 - r 4639 a"
                    action = "buy"
                    percentage = 80

                    # deviation_buy_ma3_sopra_ma13 > x e' fondamentale !
                    # deviation_buy2 = ma8_last/ma50_last
                    
                    
                    
                elif (
                    ma69_last > ma69_2_min_ago
                    and deviation_ma100_sopra_ma300 > 0.20
                    and ma78_last < ma200_last
                    
                    and deviation_buy2 > 0.04
                    and deviation_bellissima > 0.151
                    and deviation_buy_ma3_sopra_ma13 > 0.09
                    and deviation_ma7_sopra_ma40 > 0.07
                    and ma2_last > ma2_2_min_ago
                    and price > price_2_min_ago
                    and ma3_last > ma40_last
                ):
                    buy = "BUY 2A rialzo o laterale con 78 < 200 - r 4661 b"
                    action = "buy"
                    percentage = 80

                    # deviation_buy_ma3_sopra_ma13 > x e' fondamentale !
                    # deviation_buy2 = ma8_last/ma50_last
                    
                    
                    
                    
                    
                elif (
                    ma69_last >= ma69_2_min_ago
                    and deviation_ma100_sopra_ma300 < 0.20
                    and ma78_last > ma200_last
                    
                    and deviation_ma5_sopra_ma28 > 0.15
                    and deviation_buy2 > 0.01
                    and deviation_bellissima > 0.08
                    and deviation_buy_ma3_sopra_ma13 > 0.08
                    and deviation_ma7_sopra_ma40 > 0.05
                    and ma3_last > ma40_last
                    and price > price_2_min_ago
                    
                ):
                    buy = "BUY 2A ribasso o laterale  and ma78_last > ma200_last - r 4685 a"
                    action = "buy"
                    percentage = 80

                    # deviation_buy_ma3_sopra_ma13 > x e' fondamentale !
                    # deviation_buy2 = ma8_last/ma50_last  
                    # tolta and ma2_last >= ma2_2_min_ago !
                    
                    
                    
                    
                elif (
                    ma69_last >= ma69_2_min_ago
                    and deviation_ma100_sopra_ma300 < 0.20
                    and ma78_last < ma200_last
                    
                    and deviation_buy2 > 0.02
                    and deviation_ma3_sopra_ma10 > 0.24
                    and deviation_ma5_sopra_ma28 > 0.18
                    
                    and deviation_bellissima > 0.12
                    and deviation_buy_ma3_sopra_ma13 > 0.08
                    and deviation_ma7_sopra_ma40 > 0.06
                    and ma2_last >= ma2_2_min_ago
                    and price > price_2_min_ago
                    and ma3_last > ma40_last
                ):
                    buy = "BUY 2A ribasso o laterale and ma78_last < ma200_last - r 4709 B"
                    action = "buy"
                    percentage = 80

                    # deviation_buy_ma3_sopra_ma13 > x e' fondamentale !
                    # deviation_buy2 = ma8_last/ma50_last
                    # roma aggiunta 5-28
                    
                    
                
             
                elif (
                    ma78_last < ma78_2_min_ago
                    and deviation_ma5_sotto_ma300 > -0.59
                    
                    and deviation_buy2 > 0.07
                    and deviation_ma3_sopra_ma10 > 0.11
                    
                    and deviation_bellissima > 0.12
                    and deviation_ma13_sopra_ma25 > 0.06
                    and deviation_buy_ma3_sopra_ma13 > 0.09
                    and deviation_ma7_sopra_ma40 > 0.10
                    and ma2_last > ma2_2_min_ago
                    and price > price_2_min_ago
                    and ma3_last > ma40_last
                ):
                    buy = "BUY 2B - r 4732 a"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_ma3_sopra_ma13 > x e' fondamentale !
                    # deviation_buy2 = ma8_last/ma50_last
                    # 18 set aggiunta 3-10 ! 0.11
                    
                
                
                elif (
                    ma78_last < ma78_2_min_ago
                    and deviation_ma5_sotto_ma300 < -0.59
                    and delta_1 < delta_2
                    
                    and ma5_last > ma15_last
                    and deviation_ma3_sopra_ma10 > 0.15
                    
                    and ma2_last > ma2_2_min_ago
                    and price > price_2_min_ago
                    
                ):
                    buy = "BUY 2Ba durante crollo - 5 sotto 300 di molto ! PIU' AGGRESSIVO (delta 1 < delta 2) (ma100 sta risalendo) - r 4732 b1"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_ma3_sopra_ma13 > x e' fondamentale !
                    # deviation_buy2 = ma8_last/ma50_last
                    
                    
                    
                elif (
                    ma78_last < ma78_2_min_ago
                    and deviation_ma5_sotto_ma300 < -0.59
                    and delta_1 > delta_2
                    
                    and ma5_last > ma15_last
                    and deviation_ma3_sopra_ma10 > 0.15
                    
                    and deviation_buy2 > 0.04
                    and deviation_bellissima > 0.06
                    and deviation_ma13_sopra_ma25 > 0.03
                    and deviation_buy_ma3_sopra_ma13 > 0.03
                    and deviation_ma7_sopra_ma40 > 0.04
                    
                    and ma2_last > ma2_2_min_ago
                    and price > price_2_min_ago
                    
                ):
                    buy = "BUY 2Bb  durante crollo - 5 sotto 300 di molto ! PIU' PRUDENTE (delta 1 > delta 2) (ma100 si allontana verso il basso da ma200)- r 4732 b2"
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
                    buy = "BUY 2C (SOPRA) (delta1 > delta2 and 100 > ) - CREPUSCOLO - and dev_ma5_sopra_ma28 > 0.14 AND 3-10 > 0.16 - r 4765"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy2 = ma8_last / ma50
                    
                    
                
                
                
                # BUY 2 300 > 120 min ago e 200> con doppio delta > 1 trend ribasso and deviation_ma5_sopra_ma28 > 0.16
                
                elif (
                    deviation_buy2 > 0.12
                    and ma300_last > ma300_120_min_ago
                    and ma200_last > ma200_120_min_ago
                    
                    and delta_1 > delta_2
                    and ma100_last < ma100_60_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.15
                    
                    and deviation_bellissima > 0.12
                    
                    and deviation_buy_ma3_sopra_ma13 > 0.10
                    and deviation_ma7_sopra_ma40 > 0.10
                    and ma4_last > ma9_last
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma40_last
                    and ma4_last > ma78_last
                ):
                    buy = "BUY 2C SOPRA RIBASSO RIBASSO - NOTTE - r 4796 a"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy2 = ma8_last / ma50
                    # > estate ho alzato buy
                    
                    
                    
                # BUY 2 300 > 120 min ago MA 200< con doppio delta > 1 trend ribasso and deviation_ma5_sopra_ma28 > 0.18
                
                elif (
                    deviation_buy2 > 0.12
                    and ma300_last > ma300_120_min_ago
                    and ma200_last < ma200_120_min_ago
                    
                    and delta_1 > delta_2
                    and ma100_last < ma100_60_min_ago
                    
                    and deviation_ma5_sopra_ma28 > 0.18
                    
                    and deviation_bellissima > 0.15
                    
                    and deviation_buy_ma3_sopra_ma13 > 0.10
                    and deviation_ma7_sopra_ma40 > 0.10
                    and ma4_last > ma9_last
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma40_last
                    and ma4_last > ma78_last
                ):
                    buy = "BUY 2C SOPRA RIBASSO RIBASSO - NOTTE - r 4796 b"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy2 = ma8_last / ma50
                    # > estate ho alzato buy
                    
                    
                 
                    
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
                    buy = "BUY 2C SOPRA RIBASSO RIBASSO - NOTTE - r 4827"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy2 = ma8_last / ma50
                    
                    # incredibile :  anticipa con 300 < 120 min ago
                    
                    
                    
                    
                # BUY 2C dopo grande rialzo e grande ribasso 
                
                elif (
                    deviation_buy2 > 0.09
                    
                    and deviation_ma5_sotto_ma200 > 0.05
                    
                    and deviation_ma3_sopra_ma10 > 0.15
                    and deviation_ma5_sopra_ma28 > 0.30
                    
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
                    buy = "BUY 2C dopo grande rialzo e grande ribasso - r 4858 a"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy2 = ma8_last / ma50
                    
                    
                    
                # BUY 2C dopo grande rialzo e grande ribasso
                
                elif (
                    deviation_buy2 > 0.09
                    
                    and deviation_ma5_sotto_ma200 < 0.05
                    and deviation_ma5_sotto_ma200 > -0.35
                    
                    and deviation_ma3_sopra_ma10 > 0.17
                    and deviation_ma5_sopra_ma28 > 0.32
                    
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
                    buy = "BUY 2C dopo grande rialzo e grande ribasso - r 4858 b"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy2 = ma8_last / ma50
                    
                    
                    
                # BUY 2C dopo grande rialzo e grande ribasso
                
                elif (
                    deviation_buy2 > 0.09
                    
                    and deviation_ma5_sotto_ma200 < -0.35
                    
                    and deviation_ma3_sopra_ma10 > 0.15
                    and deviation_ma5_sopra_ma28 > 0.30
                    
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
                    buy = "BUY 2C dopo grande rialzo e grande ribasso - r 4858 c"
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
                    buy = "BUY 2 ORIGINALE CHE CI RIPROVA IMPORTATO DA SELL 1  - NOTTE - r 4887"
                    action = "sell"
                    percentage = 80
                    

                        
                # BUY 2 DURANTE UN RIBASSO AUDI CHE NON E' UN CROLLO ! E CHE CI RIPROVA (compare stammi vicino!)
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.70
                    and deviation_buy_crollo_1 > -1.50
                    
                    and ma5_last > ma28_last
                    
                    and ma2_last > ma2_2_min_ago
                    and ma78_last < ma200_last
                    
                ):
                    buy = "BUY 2 DURANTE UN RIBASSO AUDI CHE NON E' UN CROLLO ! E CHE CI RIPROVA con 5 > 28 - riga 4905"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # questa cosa che 78 deve essere < 200 ha dell' incredibile. MA NON TOCCARE !
                    
                    # 19 giu 2022 dev_5-16 a 0.08 da 0.09
                    # 9 luglio ho messo 5>22 perche' cosi' e' chiaro chi interviene e comunque 5-16 >0.08 era arrivata molto tardi e 5-16 arriva una ndecchia prima
                    
                    # > estate 5-28 da 5-22
                   
                    
                
                # IL BUY 2 CI RIPROVA CON INCROCIO 8-50
                
                elif (
                    deviation_buy2 > 0.005
                    and ma50_last > ma100_last
                    
                    and deviation_ma100_sopra_ma300 > -0.60
                    and deviation_ma3_sopra_ma10 > 0.01
                    
                    and ma200_last < ma200_120_min_ago
                    
                    and ma100_last < ma100_50_min_ago
                    and (ma7_prev < ma50_prev and ma7_last > ma50_last)
                    and ma2_last > ma2_2_min_ago
                ):
               
                    buy = "BUY 2C con 100< and 200< con INCROCIO 7-50 100 NON DISTANTE DA 300 - r 4934 a"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                # IL BUY 2 CI RIPROVA CON INCROCIO 8-50
                
                elif (
                    deviation_buy2 > 0.005
                    and ma50_last > ma100_last
                    
                    and deviation_ma100_sopra_ma300 < -0.60
                    and deviation_ma3_sopra_ma10 > 0.17
                    
                    and ma200_last < ma200_120_min_ago
                    
                    and ma100_last < ma100_50_min_ago
                    and (ma7_prev < ma50_prev and ma7_last > ma50_last)
                    and ma2_last > ma2_2_min_ago
                ):
               
                    buy = "BUY 2C con 100< and 200< con INCROCIO 7-50 100 MOLTO SOTTO 300 CON 3-10 > 0.17 QUA DEVE DIMOSTRARE UNA CERTA FORZA ! - r 4956 b"
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
               
                    buy = "BUY 2C con 100< and 200< con INCROCIO 7-50 and 5-28 > 0.10 (SOPRA - aurora - r 4989"
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
               
                    buy = "BUY 2C con 100< and 200< con INCROCIO 7-50 and 5-28 > 0.29 - NOTTE! - r 5018"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy2 = ma8_last / ma50
                    # incrocio va bene nel trend laterale NON TOCCARLO ! ho messo incrocio per evitare punti sopvrapposti
                    
                    
                    
                    
                
                
                # BUY 2 DURANTE UN RIBASSO AUDI con 5-16 copiata da RCCR CHE E' ANDATA BENISSIMO ! 22 ago 2022
                
                elif (
                    
                    deviation_buy_crollo_1 < -0.60
                    and deviation_buy_crollo_1 > -1.60
                    
                    and ma5_last > ma16_last
                    and deviation_ma5_sopra_ma16 > 0.10
                    
                    and ma2_last > ma2_2_min_ago
                    and ma78_last < ma200_last
                    
                ):
                    buy = "BUY 2 DURANTE UN RIBASSO AUDI con 5-16 copiata da RCCR CHE E' ANDATA BENISSIMO ! 22 ago 2022 - riga 4571"
                    action = "buy"
                    percentage = 50
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # questa cosa che 78 deve essere < 200 ha dell' incredibile. MA NON TOCCARE !
                    
                    
                    
                    
                    
                # IL BUY 2 CI RIPROVA MA PIU' IN ALTO ! non toccare questa altrimenti fa punti sovrapposti !
                
                elif (
                    deviation_buy2 > 0.01
                    and ma200_last < ma200_120_min_ago
                    
                    and ma100_last < ma100_50_min_ago
                    
                    and deviation_buy > 0.50
                    and deviation_ma5_sopra_ma28 > 0.60
                    and ma2_last > ma2_2_min_ago
                ):
               
                    buy = "BUY 2C con 100 < and 200 < con DEVIATION BUY > 0.50 and 5-28 > 0.60 - r 5044"
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
                    buy = "BUY 2 DURANTE IL CROLLO - modo 1 2-7 - r 5067"
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
                    buy = "BUY 2 DURANTE IL CROLLO - modo 2 - r 5085"
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
                    buy = "BUY 2 CHE MANCAVA DOPO BUY-SELL CROLLO ! 150-100 GIORNO ! - r 5116"
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
                    
                    and deviation_ma100_sopra_ma300 > -1.20
                    
                    and deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
               
                    and deviation_correzione > 0.015
                    and deviation_buy_ma5_sopra_ma20 > 0.10
                    and ma2_last > ma2_2_min_ago
                ):

                    buy = "BUY 2A PAZZA AUDI che non e' un forte ribasso e non e' un crollo ! deviation 5-28 > 0.05 CON 100 non lontana dalla 300 - r 5150 a"
                    action = "buy"
                    percentage = 80

                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    # ma5 non deve allontanarsi troppo dalla ma200 !
                    # compare prega per me !
                    
                    
                    
                    
                # BUY 2A PAZZA DURANTE UNA piccola CORREZIONE che NON E' un forte ribasso e NON E' un crollo ! (compare stammi vicino!)
             
                elif (
                    deviation_ma5_sopra_ma28 > 0.05
                    
                    and deviation_ma3_sopra_ma10 > 0.02
                    and deviation_ma100_sopra_ma300 < -1.20
                    
                    and deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.69
               
                    and deviation_correzione > 0.015
                    and deviation_buy_ma5_sopra_ma20 > 0.10
                    and ma2_last >= ma2_2_min_ago
                ):

                    buy = "BUY 2A PAZZA AUDI che non e' un forte ribasso e non e' un crollo ! deviation 5-28 > 0.05 CON 100 MOLTO SOTTO 300 - r 5178 b"
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

                    buy = "BUY 2 CORREZIONE che NON E' un forte ribasso e NON E' un crollo ! con deviation_correzione > 0.02 - r 5207"
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
                    buy = "BUY 2 FORTE RIBASSO che NON E' UN CROLLO ! and deviation_bellissima > 0.15 - r 5229"
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
                    and deviation_ma5_sopra_ma28 > 0.18
                ):
                    buy = "BUY 2 nuovo TREND LATERALE ! - r 5252"
                    action = "buy"
                    percentage = 80
                    
                    # SE ma100 E' cosi' VICINA A ma200 E ma300 vuo dire che non c'e' un grande rialzo in atto ma un TREND LATERALE !
                    # 5-28 a 0.10 da 0.07
                    # > estate 5-28 0.18 da 0.10
                    
                    
                    
                    
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
                    buy = "BUY 2 andamento laterale se ma200> da 20 min compra con 4-30 (SUL BUY 2 0.50 e 20-69 vs EFFETTI LATERALI !) - r 5279"
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
                    buy = "BUY 2 andamento laterale se ma200> da 20 min compra con 4-30 (SUL BUY 2 0.50 e 20-69 vs EFFETTI LATERALI !) - r 5304"
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
                    buy = "BUY 2 DOCCIA se ma200 > da 90 min ! E 3-10 > 0.01 - 100 MOLTO ALTA RISPETTO A 300 - r 5333 A"
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
                    buy = "BUY 2 DOCCIA se ma200 > da 90 min ! E 3-10 > 0.01 -100 NON LONTANA DA 300  r 5360 B"
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
                    buy = "BUY 2 con DEVIATION ASSURDA se ma200 sale da 120 min BUY con ma2-ma200 (ma5 > ma300 evita GLI EFFETTI LATERALI !) - r 5382"
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
               
                    buy = "BUY 2 che ci riprova TORNANDO ALLE ORIGINI ( TREND LATERALE !) con ma200< and ma300< AND 100 vicina alla 300 - r 5412"
                    action = "buy"
                    percentage = 70

                    # compare prega per me !
                    # se ma200< e ma300< si torna alle origini ! 8-50 ! (con ma2 > ma2 2 min ago)
                    # deviation_buy2 = ma8_last / ma50_last
                    
                    # SE 100 STA VICINO ALLA 300 TREND LATERALE ! - 5-28 DEVE AVERE UNA SPINTA MAGGIORE !
                    
                    
                    
                # BUY 2 che ci riprova quando se ne va LATERALMENTE dopo il crollo
                
                elif (
                    ma78_last > ma200_last
                    and ma28_last > ma28_20_min_ago
                    
                    and deviation_ma3_sopra_ma10 > 0.08
                    and deviation_ma5_sopra_ma28 > -0.02
                    
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and delta_300_100 < delta_300_100_60_min
                    
                    and deviation_ma100_sopra_ma300 > -0.50
                    and deviation_ma200_sopra_ma300 > -0.50
                    
                    and ma2_last > ma2_2_min_ago
                
                ):
               
                    buy = "BUY 2 CON 78 > 200 che ci riprova quando se ne va lateralmente dopo il crollo CON 28>28 30 min ago - r 5445 A1"
                    action = "buy"
                    percentage = 80

                    # compare prega per me !
                    # 29 set 2022 3-10 > 0.08 da 0.10
                    # 29 set 28 20 min ago da 28 30 min ago
                    
                    
                    
                # BUY 2 che ci riprova quando se ne va lateralmente dopo il crollo
                
                elif (
                    ma78_last > ma200_last
                    and ma28_last < ma28_30_min_ago
                    
                    and deviation_ma3_sopra_ma10 > 0.20
                    and deviation_ma5_sopra_ma28 > -0.01
                    
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and delta_300_100 < delta_300_100_60_min
                    
                    and deviation_ma100_sopra_ma300 > -0.50
                    and deviation_ma200_sopra_ma300 > -0.50
                    
                    and ma2_last > ma2_2_min_ago
                
                ):
               
                    buy = "BUY 2 CON 78 > 200 che ci riprova quando se ne va lateralmente dopo il crollo CON 28 < 28 30 min ago E 3-10 > 0.20 - r 5476 a2"
                    action = "buy"
                    percentage = 80

                    # compare prega per me !
                    
                    
                    
                # BUY 2 che ci riprova quando se ne va lateralmente dopo il crollo
                
                elif (
                    ma78_last > ma200_last
                    and deviation_ma3_sopra_ma10 > 0.17
                    and deviation_ma5_sopra_ma28 > 0.20
                    
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and delta_300_100 < delta_300_100_60_min
                    
                    and deviation_ma100_sopra_ma300 > -0.50
                    and deviation_ma200_sopra_ma300 > -0.50
                    
                    and ma2_last > ma2_2_min_ago
                
                ):
               
                    buy = "BUY 2 CON 78 < 200 che ci riprova quando se ne va lateralmente dopo il crollo - r 5503 b"
                    action = "buy"
                    percentage = 80
                    
                    # > estate aumentato buy 3-10 0.17 e 5-28 0.20

                   
                    
                    
                    
                # BUY 2 che ci riprova TORNANDO ALLE ORIGINI (TREND RIBASSO !) con ma200< and ma300< AND 5 NON MOLTO SOTTO 300
                
                elif (
                    deviation_buy2 > 0.05
              
                    and deviation_ma100_sopra_ma300 < -0.20
                    and deviation_ma5_sotto_ma300 > -0.70
                    and deviation_ma5_sopra_ma28 > 0.29
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
               
                    buy = "BUY 2 che ci riprova TORNANDO ALLE ORIGINI (TREND RIBASSO !) con ma200< and ma300< AND 5 NON MOLTO SOTTO 300 - r 5531 A"
                    action = "buy"
                    percentage = 70

                    # compare prega per me !
                    # se ma200< e ma300< si torna alle origini ! 8-50 ! (con ma2 > ma2 2 min ago)
                    # deviation_buy2 = ma8_last / ma50_last
                    
                    # 9 giu 2022 dev_buy2 (8-50) a 0.06 da 0.08
                    # 9 giu 2022 dev_bellissima a 0.15 da 0.16
                    # 16 set 2022 dev buy 2 0.05 da 0.06
                    
                    
                    
                # BUY 2 che ci riprova TORNANDO ALLE ORIGINI (TREND RIBASSO !) con ma200< and ma300< AND 5 molto sotto 300
                
                elif (
                    deviation_buy2 > 0.07
                    
                    
                    
                    and deviation_ma100_sopra_ma300 < -0.20
                    and deviation_ma5_sotto_ma300 < -0.70
                    and deviation_ma5_sopra_ma28 > 0.19
                    and deviation_bellissima > 0.145
                    and ma8_last > ma8_2_min_ago
                    and ma2_last > ma2_2_min_ago
                    and ma3_last > ma7_last
                    and ma3_last > ma13_last
                    and deviation_buy_ma3_sopra_ma20 > 0.05
                    and deviation_ma4_sopra_ma25 > 0.05
                    
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                ):
               
                    buy = "BUY 2 che ci riprova TORNANDO ALLE ORIGINI (TREND RIBASSO !) con ma200< and ma300< AND 5 molto sotto 300 - r 5531 B"
                    action = "buy"
                    percentage = 70

                    # compare prega per me !
                    # se ma200< e ma300< si torna alle origini ! 8-50 ! (con ma2 > ma2 2 min ago)
                    # deviation_buy2 = ma8_last / ma50_last
                    
                    # 9 giu 2022 dev_buy2 (8-50) a 0.06 da 0.08
                    # 9 giu 2022 dev_bellissima a 0.15 da 0.16
                    
                    # > estate aumentato un po' il buy
              
                
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

                    buy = "BUY 2 con ma200> e ma300> DURANTE UNA piccola CORREZIONE che non e' un forte ribasso e non e' un crollo - r 5562"
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

                    buy = "BUY 2 con ma200> e ma300> DURANTE UNA piccola CORREZIONE che non e' un forte ribasso e non e' un crollo - r 5586"
                    action = "buy"
                    percentage = 70
                    
                    
                    
               
                # --------------------------------------- BUY 2 che considera il passare tempo con TREND IN RIALZO ! e 78 > 200 e sempre 20 > 200
                
                elif (     
                    seconds_since_last_trade > max_hold_time_in_seconds_nuova
                    and ma78_last > ma200_last
                    
                    and deviation_ma5_sopra_ma28 > 0.10
                    and deviation_bellissima > 0.07
                    
                    and ma30_last > ma30_40_min_ago
                    
                    and ma20_last > ma200_last
                    and ma20_last > ma100_last
                    
                    and ma4_last > ma100_last
                    
                    and ma100_last < ma300_last
                    
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 2 che considera il passare tempo (SE > 120 min) and 5-28 > 0.10 e ma30 > ma 30 40 min ago (TREND IN RIALZO) con 78>200  - r 5610 A"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                # --------------------------------------- BUY 2 che considera il passare tempo con TREND IN RIALZO ! e 78 < 200 e sempre 20 > 200
                
                elif (     
                    seconds_since_last_trade > max_hold_time_in_seconds_nuova
                    and ma78_last < ma200_last
                    
                    and deviation_ma5_sopra_ma28 > 0.20
                    and deviation_bellissima > 0.07
                    
                    and ma30_last > ma30_40_min_ago
                    
                    and ma20_last > ma200_last
                    and ma20_last > ma100_last
                    
                    and ma4_last > ma100_last
                    
                    and ma100_last < ma300_last
                    
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 2 che considera il passare del tempo (SE > 120 min) and 5-28 > 0.10 e ma30 > ma 30 40 min ago (TREND IN RIALZO) con 78>200 - r 5610 B"
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
                    buy = "BUY 2 che considera il passare del tempo (SE > 120 min) and 5-28 > 0.17 and ma30 < ma30 40 min ago (TREND IN RIBASSO) - r 5634"
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
                    buy = "BUY 2 FIAT che non funzionava MA CHE HA FUNZIONATO BENISSIMO ( SOTTO RIALZO RIALZO ) GIORNO ! copiato da BUY 1 - r 5660"
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
             
                    buy = "BUY 2 RIALZO IMPROVVISO ! con ma200 > and 100>200 (solo per il buy 2 e per il buy 3) AND 100 SOPRA 300 > 0.40 - r 5686 a"
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
             
                    buy = "BUY 2 RIALZO IMPROVVISO ! con ma200 > and 100>200 (solo per il buy 2 e per il buy 3) AND 100 SOPRA 300 < 0.40 - r 5711 b"
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
                    buy = "BUY 2 che entra in azione se DOPO 2 MINUTI ma2 va sopra SELL 1 > 0.30 E 5-28 > 0.29 ! - r 5732"
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
                    buy = "BUY 2 ECCEZIONALE se ma200 sale da 20 min compra con deviation 4-30 and deviation 3-25 IMPORTATA DA RCCR - riga 5762"
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
                    
                    and ma300_last > ma300_60_min_ago
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    and deviation_buy_ma5_sopra_ma20 > 0.05
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 2 PENUULTIMA CONDIZIONE ! ma tutte negative MA BUY con 25-200 (ho sostituito 8 > 125) - r 5794 A"
                    action = "buy"
                    percentage = 70
                    
                    # BUY con 25>200 ha sostituito 8>125 (che un po' mi piaceva ma era troppo rischiosa)
                    
                    
                    
                # BUY 2 PENULTIMA condizione ! ma tutte negative MA BUY con 8 > 125
                
                elif (     
               
                    ma25_last > ma200_last
                    and ma100_last < ma100_60_min_ago
                    and ma200_last < ma200_60_min_ago
                    and ma300_last < ma300_60_min_ago
                    
                    and ma300_last < ma300_60_min_ago
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and deviation_ma3_sopra_ma10 > 0.16
                    and deviation_ma5_sopra_ma28 > 0.14
                    and deviation_buy_ma5_sopra_ma20 > 0.05
                    
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 2 PENUULTIMA CONDIZIONE ! ma tutte negative MA BUY con 25-200 (ho sostituito 8 > 125) - r 5794 B"
                    action = "buy"
                    percentage = 70
                    
                    # BUY con 25>200 ha sostituito 8>125 (che un po' mi piaceva ma era troppo rischiosa)
                    # se 300 < 120 min ago aggiunte 3-10 and 5-28 !
                    
                    
                    
                
                
                
                # BUY 2 con ma200 che sale da 60 min etc. importata dal BUY 3 RCCR
                
                elif (
                    ma10_last >= ma10_2_min_ago
                    and ma200_last > ma200_60_min_ago
                    and deviation > -0.40
                    
                    and deviation_ma3_sopra_ma10 > 0.10
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
                
                    buy = "BUY 2 con ma200 che sale da 60 min 33 > 78 ! and 3-10 > 0.10 - r 5829 A"
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
                
                    buy = "BUY 2 con ma200 che sale da 60 min 33 < 78 ! - r 5860 B"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                # BUY 2 RIVOLUZIONARIO se ma39 > ma50 - r 3450
                
                elif (
                    deviation_ma4_sopra_ma30 > 0.15
                    and ma200_last > ma200_120_min_ago
                    and ma78_last > ma78_30_min_ago
                    
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
                    buy = "BUY 2 RIVOLUZIONARIO se ma39 > ma50 E CON 78 > 78 30 min ago - r 5892 a"
                    action = "buy"
                    percentage = 70
                    
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    
                    
                    
                # BUY 2 RIVOLUZIONARIO se ma39 > ma50 - r 3450
                
                elif (
                    deviation_ma4_sopra_ma30 > 0.15
                    and ma200_last > ma200_120_min_ago
                    and ma78_last < ma78_30_min_ago
                    and deviation_ma3_sopra_ma10 > 0.17
                    
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
                    buy = "BUY 2 RIVOLUZIONARIO se ma39 > ma50 MA 78 < 78 30 min ago E CON 3-10 > 0.17 - r 5919 b"
                    action = "buy"
                    percentage = 70
                    
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    
                    
                    
                    
                # BUY 2 RIVOLUZIONARIO A1 (100 NON E' ATTACCATA ALLA 300 !) deviation_ma100_sopra_ma300 > 0.05 e 39>50 E 8>200
                
                elif (
                    deviation_ma4_sopra_ma30 > 0.14
                    and deviation_bellissima > 0.06
                    
                    and deviation_ma100_sopra_ma300 > 0.05
                    
                    and ma200_last < ma200_120_min_ago
                    and ma8_last > ma200_last
                    
                    and deviation > -0.30
                    
                    and ma28_last > ma50_last
                    and delta_buy3_incrocio_ma3_ma8 >= 0.06
                    and ma3_last > ma8_last
                    and ma3_last >= ma69_last
                    and ma4_last >= ma4_2_min_ago
                    and ma2_last >= ma2_2_min_ago
                    and ma5_last >= ma15_last
                    and ma5_last >= ma25_last
                ):    
                    buy = "BUY 2 RIVOLUZIONARIO A1 (100 CHE NON E' ATTACCATA ALLA 300 !) e ma39 > ma50 E 8>200 - r 5945 A1"
                    action = "buy"
                    percentage = 70
                    
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    # 26 set 100-300 se stanno attaccate e' molto rischioso ! vedi ore 22:48 24 set 2022
                    
                    
                # BUY 2 RIVOLUZIONARIO A2 (100 E' ATTACCATA ALLA 300 !) (pericolo !) (deviation_ma100_sopra_ma300 tra 0.05 e -0.05) e 39>50 E 8>200
                
                elif (
                    deviation_ma4_sopra_ma30 > 0.14
                    and deviation_bellissima > 0.06
                    
                    and deviation_ma100_sopra_ma300 < 0.05
                    and deviation_ma100_sopra_ma300 > -0.05
                    and deviation_ma3_sopra_ma10 > 0.11
                    
                    and ma200_last < ma200_120_min_ago
                    and ma8_last > ma200_last
                    
                    and deviation > -0.30
                    
                    and ma28_last > ma50_last
                    and delta_buy3_incrocio_ma3_ma8 >= 0.06
                    and ma3_last > ma8_last
                    and ma3_last >= ma69_last
                    and ma4_last >= ma4_2_min_ago
                    and ma2_last >= ma2_2_min_ago
                    and ma5_last >= ma15_last
                    and ma5_last >= ma25_last
                ):    
                    buy = "BUY 2 RIVOLUZIONARIO A2 (con 100 CHE E' ATTACCATA ALLA 300 !) (pericolo !) E 3-10 > 0.11 e 39 > 50 and 8 > 200 - r 5945 A2"
                    action = "buy"
                    percentage = 70
                    
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    # 26 set 100-300 se stanno attaccate e' molto rischioso ! vedi ore 22:48 24 set 2022
                    
                    
                    
                # BUY 2 RIVOLUZIONARIO A3 (100 NON E' ATTACCATA ALLA 300 !) e 39>50 E 8>200 and deviation_ma100_sopra_ma300 > 0.05 
                
                elif (
                    deviation_ma4_sopra_ma30 > 0.14
                    and deviation_bellissima > 0.06
                    
                    and deviation_ma100_sopra_ma300 < -0.05
                    
                    and ma200_last < ma200_120_min_ago
                    and ma8_last > ma200_last
                    
                    and deviation > -0.30
                    
                    and ma28_last > ma50_last
                    and delta_buy3_incrocio_ma3_ma8 >= 0.06
                    and ma3_last > ma8_last
                    and ma3_last >= ma69_last
                    and ma4_last >= ma4_2_min_ago
                    and ma2_last >= ma2_2_min_ago
                    and ma5_last >= ma15_last
                    and ma5_last >= ma25_last
                ):    
                    buy = "BUY 2 RIVOLUZIONARIO A3 con 100 CHE NON E' ATTACCATA ALLA 300 ! e ma39 > ma50 and 8 > 200 - r 5945 A3"
                    action = "buy"
                    percentage = 70
                    
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    # 26 set 100-300 se stanno attaccate e' molto rischioso ! vedi ore 22:48 24 set 2022
                    
                    
                    
                    
                    
                    
                    
                    
                # BUY 2 RIVOLUZIONARIO se 39>50 E 8<200 
                
                elif (
                    deviation_ma4_sopra_ma30 > 0.20
                    and deviation_bellissima > 0.10
                    
                    and ma200_last < ma200_120_min_ago
                    and ma8_last < ma200_last
                    
                    and deviation > -0.30
                    
                    and ma28_last > ma50_last
                    and delta_buy3_incrocio_ma3_ma8 >= 0.06
                    and ma3_last > ma8_last
                    and ma3_last >= ma69_last
                    and ma4_last >= ma4_2_min_ago
                    and ma2_last >= ma2_2_min_ago
                    and ma5_last >= ma15_last
                    and ma5_last >= ma25_last
                ):    
                    buy = "BUY 2 RIVOLUZIONARIO se ma39 > ma50 - r 5945 B"
                    action = "buy"
                    percentage = 70
                    
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    # > estate se 8 sta sotto 200 4-30 >0.20 and dev bellissima >0.10
                    
                    
                
                
                
                
                # RIALZO IMPROVVISO 200< DOPO TANTO TEMPO DI TREND LATERALE - POTREBBE SUCCEDERE !
                
                elif (    
                   
                    ma200_last < ma200_20_min_ago
                    
                    and deviation_rialzo_improvviso_1 > 0.92
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

                    buy = "BUY 2 RIALZO IMPROVVISO con 200 < tentando di evitare falsi acquisti DOPO TANTO TEMPO DI TREND LATERALE - POTREBBE SUCCEDERE ! - r 5978"
                    action = "buy"
                    percentage = 70
                    
                    # 8 luglio 2022 ore 3:28 e' capitato rialzo improvviso sul BUY 2 !
                    
                    
                    
                # RIALZO IMPROVVISO 200> DOPO TANTO TEMPO DI TREND LATERALE - POTREBBE SUCCEDERE !
                
                elif (
                    ma200_last > ma200_20_min_ago
                    and deviation_rialzo_improvviso_sopra > 0.78
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
             
                    buy = "BUY 2 RIALZO IMPROVVISO con 200 > e con > 0.72 DOPO TANTO TEMPO DI TREND LATERALE - POTREBBE SUCCEDERE e' successo ! - r 5979"
                    action = "buy"
                    percentage = 70
                    
                    # 1 luglio a 0.72 da 0.82
                    # 8 luglio 2022 ore 3:28 e' capitato rialzo improvviso sul BUY 2
                    # 21 lug 2022 0.78 da 0.22
                    
                    
                    
                    
                    
                    
                # BUY 2 CHE MANCAVA DOPO 5 ore di ribasso
                
                elif (
                    deviation_ma5_sopra_ma28 > 0.30
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and ma100_last < ma100_301_min_ago
                    and ma200_last < ma200_301_min_ago
                    and ma300_last < ma300_301_min_ago
                    
                    and deviation_ma300__diviso_ma300_5_ore_ago < -0.25
                    and deviation_ma5_sotto_ma300 < -0.43
                    
                    and ma2_last > ma2_2_min_ago
                
                ):
                    buy = "BUY 2 CHE MANCAVA DOPO 5 ore di ribasso buy con 5-28>0.30 perdio se entra dopo 5 ore deve essere piu' sicuro ! - r 5979"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                # BUY 2 ultima condizione ! ma tutte negative MA BUY con 50-100 (integra r2505)
                
                elif (     
               
                    ma50_last > ma100_last
                    and ma78_last > ma100_last
                    
                    and ma100_last < ma100_60_min_ago
                    and ma200_last < ma200_60_min_ago
                    and ma300_last < ma300_60_min_ago
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and deviation_ma3_sopra_ma10 > 0.11
                    and deviation_ma5_sopra_ma28 > 0.13
                    and deviation_buy_ma5_sopra_ma20 > 0.01
                    
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 2 ULTIMA CONDIZIONE ! ma tutte negative MA 50 > 100 (integra r2505) con 78>100 - r 5980 A"
                    action = "buy"
                    percentage = 70
                    
                    # aggiunta di 5-28 > 0.12
                    # 22 set aggiunta di 3-10 > 0.11
                    
                    
                # BUY 2 ultima condizione ! ma tutte negative MA BUY con 50-100 (integra r2505)
                
                elif (     
               
                    ma50_last > ma100_last
                    and ma78_last < ma100_last
                    and ma100_last < ma100_60_min_ago
                    and ma200_last < ma200_60_min_ago
                    and ma300_last < ma300_60_min_ago
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    and deviation_ma5_sopra_ma28 > 0.12
                    and deviation_buy_ma5_sopra_ma20 > 0.05
                    
                    and ma2_last > ma2_2_min_ago
                ):    
                    buy = "BUY 2 ULTIMA CONDIZIONE ! ma tutte negative MA 50 > 100 (integra r2505) con 78<100 - r 5980b"
                    action = "buy"
                    percentage = 70
                    
                    # aggiunta di 5-28 < 0.12
                    
                    
                    
                    
                    
           
            ############################################################################################################ COMPRA sessione 3
            
            # forse dal BUY 3 in poi (o dal BUY 4 in poi) DEVE ESSERE ma100 > E ma2 > ma100 !
            # deviation_buy3 = ma4_last/ma30_last 
                    

            elif self.session == 3:
                
                if (
                    ma10_last >= ma10_2_min_ago
                    and ma28_last > ma69_last
                    
                    and ma200_last > ma200_60_min_ago
                    and deviation > -0.30
                    and deviation_ma3_sopra_ma10 > 0.11
                    and deviation_ma5_sopra_ma28 > 0.13
                    
                    and deviation_ma4_sopra_ma30 > 0.10
                    and ma3_last > ma13_last
                    and ma4_last > ma9_last
                    and deviation_ma7_sopra_ma40 > 0.05
                    and ma7_last > ma25_last
                    
                    and deviation_buy_ma2_sopra_ma13 > 0.10
                    and ma4_last > ma50_last
                    and ma2_last >= ma2_2_min_ago
                    
                ):  
                
                    buy = "BUY 3A con ma200 che sale da 60 min and ma28_last > ma69_last - r 6016"
                    action = "buy"
                    percentage = 80

                    # deviation_buy3 = ma4_last/ma30_last
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    
                    
                    
                    
                    
                    
                
                
                ######################################################### raddoppiate con 100> o con 100<
                
                elif (
                    ma10_last > ma10_2_min_ago
                    and ma28_last < ma78_last
                    and ma100_last > ma100_60_min_ago
                    
                    and deviation_ma100_sopra_ma300 > 0.50
                    and deviation_ma3_sopra_ma10 > 0.25
                    and deviation_ma5_sopra_ma28 > 0.155
                    
                    and ma200_last > ma200_60_min_ago
                    and deviation > -0.30
                 
                    and deviation_ma4_sopra_ma30 > 0.11
                    and ma3_last > ma13_last
                    and ma4_last > ma9_last
                    and deviation_ma7_sopra_ma40 > 0.08
                    and ma7_last > ma25_last
                    
                    and deviation_buy_ma2_sopra_ma13 > 0.10
                    and ma4_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                    
                ):  
                
                    buy = "BUY 3A con ma200 che sale da 60 min and ma28_last < ma78_last MA 100> 60 min ago CON 100 MOLTO SOPRA 300 - r 6056 a"
                    action = "buy"
                    percentage = 80

                    # deviation_buy3 = ma4_last/ma30_last
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    
                    
                    
                    
                elif (
                    ma10_last > ma10_2_min_ago
                    and ma28_last < ma78_last
                    and ma100_last > ma100_60_min_ago
                    
                    and deviation_ma100_sopra_ma300 < 0.50
                    and deviation_ma3_sopra_ma10 > 0.10
                    and deviation_ma5_sopra_ma28 > 0.155
                    
                    and ma200_last > ma200_60_min_ago
                    and deviation > -0.30
                   
                    and deviation_ma4_sopra_ma30 > 0.11
                    and ma3_last > ma13_last
                    and ma4_last > ma9_last
                    and deviation_ma7_sopra_ma40 > 0.08
                    and ma7_last > ma25_last
                    
                    and deviation_buy_ma2_sopra_ma13 > 0.10
                    and ma4_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                    
                ):  
                
                    buy = "BUY 3A con ma200 che sale da 60 min and ma28_last < ma78_last MA 100> 60 min ago CON 100 POCO SOPRA 300 - r 6090 b"
                    action = "buy"
                    percentage = 80

                    # deviation_buy3 = ma4_last/ma30_last
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    
                    
                    
                elif (
                    ma10_last > ma10_2_min_ago
                    and ma300_last > ma300_301_min_ago
                    and ma28_last < ma78_last
                    and ma100_last < ma100_60_min_ago
                    
                    and ma200_last > ma200_60_min_ago
                    and deviation > -0.30
                    and deviation_ma5_sopra_ma28 > 0.18
                    
                    and deviation_ma4_sopra_ma30 > 0.11
                    and ma3_last > ma13_last
                    and ma4_last > ma9_last
                    and deviation_ma7_sopra_ma40 > 0.07
                    and ma7_last > ma25_last
                    
                    and deviation_buy_ma2_sopra_ma13 > 0.10
                    and ma4_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                    
                ):  
                
                    buy = "BUY 3A con 300 > 300 301 min ago ! e con ma200 che sale da 60 min and ma28_last < ma78_last - r 6121 A"
                    action = "buy"
                    percentage = 80

                    # deviation_buy3 = ma4_last/ma30_last
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    # 28 set con 300 > 301 min ago anticipa ndecchia
                    
                    
                elif (
                    ma10_last > ma10_2_min_ago
                    and ma300_last < ma300_301_min_ago
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
                
                    buy = "BUY 3A con ma200 che sale da 60 min and ma28_last < ma78_last - r 6121 B"
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
              
                    buy = "BUY 3A con ma69 > MA ma200 scende da 60 min ! e CON ma300 < 60 min ago - r 6163"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                
                
                # BUY 3 nuovo TREND LATERALE !
                
                elif (
                    ma100_last > ma300_last
                    and ma100_last > ma200_last
                    and ma78_last > ma200_last
                    and deviation_ma78_sotto_ma200 > 0.25
                    
                    and deviation_ma3_sopra_ma10 > 0.01
                    and deviation_ma5_sopra_ma28 > 0.07
                    
                    and ma8_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                        
                    and deviation_ma100_sopra_ma300 < 0.04
                    and deviation_ma100_sopra_ma200 < 0.05
                    
                ):
                    buy = "BUY 3 nuovo TREND LATERALE ! dev 78-200 > 0.25 - 78 > 200 con 3-10 > 0.01 - r 6187 A1"
                    action = "buy"
                    percentage = 80
                    
                    # SE ma100 E' cosi' VICINA A ma200 E ma300 vuo dire che non c'e' un grande rialzo in atto ma un TREND LATERALE !
                # BUY 3 nuovo TREND LATERALE !
                
                
                
                elif (
                    ma100_last > ma300_last
                    and ma100_last > ma200_last
                    and ma78_last > ma200_last
                    and deviation_ma78_sotto_ma200 < 0.25
                    and deviation_ma78_sotto_ma200 > -0.25
                    
                    and deviation_ma3_sopra_ma10 > 0.16
                    and deviation_ma5_sopra_ma28 > 0.07
                    
                    and ma8_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                        
                    and deviation_ma100_sopra_ma300 < 0.04
                    and deviation_ma100_sopra_ma200 < 0.05
                    
                ):
                    buy = "BUY 3 nuovo TREND LATERALE ! dev 78-200 > -0.25 - 0.25 - 78 > 200 con 3-10 > 0.16 - r 6187 A2"
                    action = "buy"
                    percentage = 80
                    
                    # SE ma100 E' cosi' VICINA A ma200 E ma300 vuo dire che non c'e' un grande rialzo in atto ma un TREND LATERALE !
                    
                    
                    
                elif (
                    ma100_last > ma300_last
                    and ma100_last > ma200_last
                    and ma78_last > ma200_last
                    and deviation_ma78_sotto_ma200 < -0.25
                    
                    and deviation_ma3_sopra_ma10 > 0.01
                    and deviation_ma5_sopra_ma28 > 0.07
                    
                    and ma8_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                        
                    and deviation_ma100_sopra_ma300 < 0.04
                    and deviation_ma100_sopra_ma200 < 0.05
                    
                ):
                    buy = "BUY 3 nuovo TREND LATERALE ! dev 78-200 < -0.25 - 78 > 200 con 3-10 > 0.01 - r 6187 A3"
                    action = "buy"
                    percentage = 80
                    
                    # SE ma100 E' cosi' VICINA A ma200 E ma300 vuo dire che non c'e' un grande rialzo in atto ma un TREND LATERALE !
                    
                    
                    
                    
                    
                    
                    
                    
                    
                # BUY 3 nuovo TREND LATERALE !
                
                elif (
                    ma100_last > ma300_last
                    and ma100_last > ma200_last
                    and ma78_last < ma200_last
                    
                    and deviation_ma3_sopra_ma10 > 0.07
                    and deviation_ma5_sopra_ma28 > 0.07
                    
                    and ma8_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                        
                    and deviation_ma100_sopra_ma300 < 0.04
                    and deviation_ma100_sopra_ma200 < 0.05
                    
                ):
                    buy = "BUY 3 nuovo TREND LATERALE ! - 78 < 200 con 3-10 > 0.07 - r 6214 b"
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
              
                    buy = "BUY 3A con ma69 > MA ma200 scende da 60 min ! and ma300_last > ma300_60_min_ago - r 6248"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                elif (
                    deviation_ma4_sopra_ma30 > 0.15
                    and deviation_ma3_sopra_ma10 > 0.17
                    and deviation_ma5_sopra_ma28 > 0.10
                    and deviation_bellissima > 0.07
                    
                    and deviation > -0.30
                    
                    and ma39_last > ma50_last
                    and delta_buy3_incrocio_ma3_ma8 >= 0.06
                    and ma3_last > ma8_last
                    and ma3_last >= ma69_last
                    and ma4_last >= ma4_2_min_ago
                    and ma2_last >= ma2_2_min_ago
                    and ma5_last >= ma15_last
                    and ma5_last >= ma25_last
                ):    
                    buy = "BUY 3B da RCCR - se ma39 > ma50 - r 6280"
                    action = "buy"
                    percentage = 80
                    
                    # > estate aggiunti 3-10 and 5-28
                    
                    
                    
                    
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
                    buy = "BUY 3C RIVOLUZIONARIO se ma39 > ma50 - r 6301"
                    action = "buy"
                    percentage = 80
                    
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    # ho dovuto aggiungere incrocio dal basso!
                    
                    
                    
                    
                    
                elif (
                    ma69_last < ma69_2_min_ago
                    and ma300_last > ma300_120_min_ago
                    and deviation > -0.30
                    
                    and ma78_last > ma200_last
                    
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
                    buy = "BUY 3D RIVOLUZIONARIO con 300 > 120 min ago e se ma69 < AND ma78_last > ma200_last - r 6329 a1"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy3 = ma4_last/ma30_last
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    
                    
                elif (
                    ma69_last < ma69_2_min_ago
                    and ma300_last < ma300_120_min_ago
                    and deviation > -0.30
                    
                    and ma78_last > ma200_last
                    
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
                    buy = "BUY 3D RIVOLUZIONARIO con 300 < 120 min ago e se ma69 < AND ma78_last > ma200_last - r 6329 a2"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy3 = ma4_last/ma30_last
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    
                    
                    
                    
                elif (
                    ma69_last < ma69_2_min_ago
                    and deviation > -0.30
                    
                    and ma78_last < ma200_last
                    and deviation_ma3_sopra_ma10 > 0.15
                    
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
                    buy = "BUY 3D RIVOLUZIONARIO se ma69 < AND ma78_last < ma200_last AND deviation_ma3_sopra_ma10 > 0.07- r 6356 b"
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
                    buy = "BUY 3 importata da RCCR - AUDI CHE NON E' UN CROLLO ! con 5-16 > 0.01 - riga 6388"
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
                    buy = "BUY 3 FORTE RIBASSO che NON E' UN CROLLO ! and deviation_bellissima > 0.17  da BUY2 RCCR - r 6417"
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
               
                    buy = "BUY 3 NUOVO che ci riprova TORNANDO ALLE ORIGINI con ma200<  MA 100 e' andata sopra 200 ! - r 6447"
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
             
                    buy = "BUY 3 RIALZO IMPROVVISO ! con ma200 > and 100>200 (solo per il buy 2 e per il buy 3) - r 6479"
                    action = "buy"
                    percentage = 80
                    
                    
                    
                # BUY 3 con ma200> piccola CORREZIONE FIAT che NON E' un forte ribasso e NON E' un crollo ! ALTRA RIGA RCCR che e' andata bene.
                
                elif (    
                    
                    ma200_last > ma200_20_min_ago
                    and ma3_last > ma28_last
                    and ma2_last > ma2_2_min_ago
                    
                    and ma100_last > ma200_last
                    and ma200_last > ma300_last
                    
                    and ma100_last > ma100_60_min_ago
                    and ma200_last > ma200_60_min_ago
                    and ma300_last > ma300_60_min_ago
                    
                    and deviation_ma3_sopra_ma10 > 0.06
                    and deviation_ma5_sopra_ma28 > -0.02
                ):    
                    
                    buy = "BUY 1 con 200 > - riga 1384 RCCR portata nel MADDOG - r 6480"
                    action = "buy"
                    percentage = 80
                    
                    # 30 set importato r 1384 RCCR su BUY 3 MADDOG
                    # 30 set 2022 aggiunta 3-10
                    # 30 set 2022 aggiunta 5.28
                    
                    
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
                    buy = "BUY 3 CON IL TURBO - r 6500"
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
                    buy = "BUY 3 che ci riprova DURANTE IL CROLLO - modo 1 2-7 - r 6520"
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
                    buy = "BUY 3 che ci riprova DURANTE IL CROLLO - modo 2 - r 6538"
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
                    buy = "BUY 3 che ci riprova DURANTE IL CROLLO - modo 3 - r 6569"
                    action = "buy"
                    percentage = 90
                    
                    # and deviation_ma100_laterale < -1.90 e' 5 sotto 100 (NON TI PREOCCUPARE)
                    # QUESTA CONDIZIONE E' STATA CREATA DOPO AVER VISTO UN CROLLO DOPO IL BUY 2 ma il BUY 3 non entrava in azione !
                    
                    
                    
                # BUY 3 29 ago 2022 > 120 min di ribasso
                
                elif (
                    
                    ma18_last > ma78_last
                    
                    and ma100_last < ma100_120_min_ago
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and deviation_ma5_sopra_ma28 > 0.08
                    and ma2_last >= ma2_2_min_ago
                    
                ):
                    buy = "BUY 3 29 ago 2022 > 120 min di ribasso AND 18>78 - r 6570 A"
                    action = "buy"
                    percentage = 90
                    
                    # 14 set 2022 18-78 da 18-100
                    
                    
                    
                    
                # BUY 3 29 ago 2022 > 180 min di ribasso
                
                elif (
                    
                    ma18_last > ma100_last
                    
                    and ma100_last < ma100_180_min_ago
                    and ma200_last < ma200_180_min_ago
                    and ma300_last < ma300_180_min_ago
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and deviation_ma5_sopra_ma28 > 0.02
                    and ma2_last >= ma2_2_min_ago
                    
                ):
                    buy = "BUY 3 29 ago 2022 > 180 min di ribasso - r 6570 B"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                    
                    
                    
                    
                    
                
                
                
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
                    buy = "BUY 3 ULTIMA CONDIZIONE che mancava ! ma tutte negative MA BUY con 8-150 - r 6598"
                    action = "buy"
                    percentage = 80
                    
                    # BUY 3 ULTIMA CONDIZIONE che mancava con 8-150
                    
                    
                    
                    
                # BUY 3 con ma69 > and deviation_bellissima > 0.12 (PER SPEZZARE LA CATENA - effetti laterali) IMPORTATA DA BUY 4 RCCR   
                
                elif (
                    ma69_last >= ma69_2_min_ago
                    and ma78_last > ma100_last
                    and deviation_ma3_sopra_ma10 > 0.05
                    and deviation_ma5_sopra_ma28 > 0.01
                    
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
                    buy = "BUY 3 78>100 E con ma69 > and dev_bellissima > 0.12 (PER SPEZZARE LA CATENA - effetti laterali) IMPORTATA DA BUY 4 RCCR - riga 6599A"
                    action = "buy"
                    percentage = 50
                    
                    # 28 set aggiunta 3-10
                    
                    
                    
                # BUY 3 con ma69 > and deviation_bellissima > 0.12 (PER SPEZZARE LA CATENA - effetti laterali) IMPORTATA DA BUY 4 RCCR   
                
                elif (
                    ma69_last >= ma69_2_min_ago
                    and ma78_last < ma100_last
                    and deviation_ma5_sopra_ma28 > 0.30
                    
                    and deviation_bellissima > 0.12
                    and deviation_buy3 > 0.13
                    and deviation_ma7_sopra_ma40 > 0.09
               
                    and ma3_last > ma13_last
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    and ma6_last > ma15_last
                    and ma7_last > ma25_last
                    
                    and ma2_last > ma2_2_min_ago
             
                ):
                    buy = "BUY 3 78<100 E con ma69 > and deviation_bellissima > 0.12 (PER SPEZZARE LA CATENA - effetti laterali) IMPORTATA DA BUY 4 RCCR - riga 6599B"
                    action = "buy"
                    percentage = 50
                    
                    
                    
                    
                    
                    
                    
                    
                    
                # BUY 3 PAZZA piccola CORREZIONE FIAT
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation > -0.30
                    
                    and deviation_buy_crollo_1 < -0.29
                    and deviation_buy_crollo_1 > -0.59
                    
                    and deviation_correzione > 0.02
                    and deviation_buy_ma5_sopra_ma20 > 0.15
                    and deviation_ma5_sotto_ma200 > -1.00
                    
                ):

                    buy = "BUY 3 PAZZA piccola CORREZIONE FIAT che non e' un forte ribasso e non e' un crollo ! con deviation_correzione > 0.02 - r 6623"
                    action = "buy"
                    percentage = 80

                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_correzione = ma3_last / ma25_last
                    # ma5 non deve allontanarsi troppo dalla ma200 !
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    
                    # > estate 5-20 0.15 da 0.12 e dev correzione  0.02 da 0.015
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
         
            # ########################################################################################################## COMPRA sessione 4
            
            # ---------------------------------------------------------------------------------------------------------- deviation piu' alte se ma 78 < !
            
            # ########################################### se 300 < il buy 4 deve stare sopra ma100

            elif self.session == 4:
                
                
                if (
                    ma69_last >= ma69_2_min_ago
                    and ma300_last > ma300_301_min_ago
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
                    buy = "BUY 4A con ma 78> e 300> E ma100>ma200 - r 6668 A"
                    action = "buy"
                    percentage = 70
          
                    # se al BUY 4 ha ma100 < ma200 evidentemente c'e' qualche cosa di strano 
                    # il trend, evidentemente, e' LATERALE.
                    # E ALLORA AGGIUNGO UN BEL 6-30 > 0.15 - TREND LATERALE
                    
                    
                elif (
                    ma69_last >= ma69_2_min_ago
                    and ma300_last < ma300_301_min_ago
                    and deviation_ma3_sopra_ma10 > 0.10
                    and deviation_ma5_sopra_ma28 > 0.13
                    
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
                    buy = "BUY 4A con ma 78> e 300> E ma100>ma200 - r 6668 B"
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
                    buy = "BUY 4 di emergenza CROLLO FERRARI - modo 1 - 3-28 - r 6690"
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
                    buy = "BUY 4 di emergenza CROLLO FERRARI - modo 2 - r 6710"
                    action = "buy"
                    percentage = 70
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # deviation_buy_crollo_2 = ma3_last / ma13_last
                    # SALTA IL BUY 2 allora ho fatto il BUY 3 di emergenza (se <-1.61 si attiva 8-50)
                    
                    
                    
                elif (
                    deviation_ma4_sopra_ma30 > 0.10
                    and ma300_last > ma300_120_min_ago
                    and ma100_last > ma100_60_min_ago
                    
                    and deviation > -0.30
                    and deviation_bellissima >= 0.03
                    and ma39_last >= ma48_last
                    and delta_buy3_incrocio_ma3_ma8 >= 0.06
                    and ma3_last > ma8_last
                    and ma3_last >= ma69_last
                    and ma4_last >= ma4_2_min_ago
                    and ma2_last >= ma2_2_min_ago
                    and ma5_last >= ma15_last
                    and ma5_last >= ma25_last
                ):    
                    buy = "BUY 4B importato da BUY 3 RCCR se ma39 > ma48 con 300 > e 100> - r 6736 a1"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                    
                elif (
                    deviation_ma4_sopra_ma30 > 0.14
                    and ma300_last > ma300_120_min_ago
                    and ma100_last < ma100_60_min_ago
                    
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
                    buy = "BUY 4B importato da BUY 3 RCCR se ma39 > ma48 con 300 > e 100< - r 6736 2"
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
                    buy = "BUY 4B importato da BUY 3 RCCR se ma39 > ma50 con 300 < - r 6756 b"
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
                    buy = "BUY 4A con ma 78 > TREND LATERALE con 6-30 > 0.15 - r 6780"
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
                    and deviation_ma7_sopra_ma40 > 0.12
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    and ma2_last > ma2_2_min_ago
                    and ma7_last > ma25_last
                    
                    and ma13_last > ma100_last
                    and deviation_ma5_sopra_ma28 > 0.15
                ):
                    buy = "BUY 4A con ma 78> e 300< ma 100>200 - r 6808"
                    action = "buy"
                    percentage = 70
                    
                    # > vacanza 5-28 > 0.15 da 0.05
                    
               
                    
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
                    buy = "BUY 4A con ma 78> e 300< e 100<200 - r 6836"
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
                    buy = "BUY 4B RIVOLUZIONARIO con ma78 > - r 6859"
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
                    buy = "BUY 4B RIVOLUZIONARIO con ma78 > and ma39_last > ma100_last - r 6893"
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
                    buy = "BUY 4B RIVOLUZIONARIO con ma78 > and ma39_last < ma100_last - r 6921"
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
                    buy = "BUY 4C RIVOLUZIONARIO con ma78 < - r 6955"
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
                    buy = "BUY 4C RIVOLUZIONARIO con ma78 < - r 6981"
                    action = "buy"
                    percentage = 70
                    
                    
                
                
                
                
                # BUY 4 se 11 > 200 e con ma69 > and deviation_bellissima > 0.12 (PER SPEZZARE LA CATENA - effetti laterali) IMPORTATA DA BUY 5
                
                elif (
                    ma69_last >= ma69_2_min_ago
                    and ma11_last > ma200_last
                    
                    and deviation_buy3 > 0.12
                    and deviation_bellissima > 0.14
                    and deviation_ma7_sopra_ma40 > 0.12
                    
                    and ma3_last > ma13_last
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    and ma6_last > ma15_last
                    and ma7_last > ma25_last
                    
                    and ma2_last > ma2_2_min_ago
             
                ):
                    buy = "BUY 4 se 11 > 200 e con ma69 > and dev_bellissima > 0.12 (PER SPEZZARE LA CATENA - effetti laterali) DA BUY 5 RCCR - riga 7008"
                    action = "buy"
                    percentage = 70
                    
                    # > estate 7-40 0.12 da 0.09 and dev bellissima 0.14 da 0.12
                    
                    
                    
                    
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
                    buy = "BUY 4 NUOVA (trend laterale) 8 > 100 AND ma300_last > ma300_120_min_ago AND 5-28 > 0.12 e con ma69 > - riga 7038"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                    
                # BUY 4 29 ago 2022 > 120 min di ribasso - PENSIERO LATERALE
                
                elif (
                    
                    ma18_last > ma100_last
                    
                    and ma100_last < ma100_120_min_ago
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and deviation_ma5_sotto_ma300 < -0.35
                    
                    and deviation_ma5_sopra_ma28 > 0.08
                    and ma2_last >= ma2_2_min_ago
                    
                ):
                    buy = "BUY 4 29 ago 2022 > 120 min di ribasso - deviation_ma5_sotto_ma300"
                    action = "buy"
                    percentage = 90
                    
                    # vuoi comprare dopo 120 min di ribasso ? deve essere 5-300 < -0.35 ! voglio uno sconto ulteriore dello 0.35% ! PENSIERO LATERALE
                    
                    
                # BUY 4 29 ago 2022 > 180 min di ribasso
                
                elif (
                    
                    ma18_last > ma100_last
                    
                    and ma100_last < ma100_180_min_ago
                    and ma200_last < ma200_180_min_ago
                    and ma300_last < ma300_180_min_ago
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and deviation_ma5_sopra_ma28 > 0.02
                    and ma2_last >= ma2_2_min_ago
                    
                ):
                    buy = "BUY 4 29 ago 2022 > 180 min di ribasso - r 7039 B"
                    action = "buy"
                    percentage = 90
                    
                    
                    
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
                    buy = "BUY 4 se 11 > 200 con 5-28 > 0.20 ! e con ma69 > (PER SPEZZARE LA CATENA - effetti laterali) DA BUY 5 RCCR - riga 7065"
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
           
                    buy = "BUY 4A PAZZA DURANTE UNA piccola CORREZIONE che non e' un forte ribasso e non e' un crollo ! con deviation_correzione > 0.02 - r 7100"
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
                    and ma100_last > ma300_last
                    and ma28_last > ma28_30_min_ago
                    and ma78_last > ma150_last
                    
                    and deviation_ma5_sopra_ma28 > 0.08
                    
                    and deviation_buy3 > 0.06
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.09
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    
                    and ma6_last > ma15_last
                    and ma7_last > ma25_last
                    
                    and ma2_last > ma2_2_min_ago
                
                ):
                    buy = "BUY 5 con ma50 > AND 50>100 and ma28_last > ma28_30_min_ago and 5-28 > 0.08 CON ma100_last > ma300_last - riga 7144 a"
                    action = "buy"
                    percentage = 70
                    
                    # 6 giu 2022 5-28 a 0.12 da 0.15
                    
                    # > estate anticipo buy 5-28 0.08 da 0.12
                    
                    
                    
                    
                elif (
                    ma50_last >= ma50_2_min_ago
                    and ma100_last < ma300_last
                    and ma28_last > ma28_30_min_ago
                    and ma78_last > ma150_last
                    
                    and deviation_ma3_sopra_ma10 > 0.22
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
                    buy = "BUY 5 con ma50 > AND 50>100 and ma28_last > ma28_30_min_ago and 5-28 > 0.12  CON ma100_last < ma300_last AND 3-10 > 0.22 - riga 7174 b"
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
                    buy = "BUY 5 con ma50 > AND 50>100 and ma28_last < ma28_30_min_ago and 5-28 > 0.17 - riga 7203"
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
                    buy = "BUY 5 con ma50 > AND 50<100 and 300 > 60 min ago and 5-28 > 0.27 (SI !) - riga 7237"
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
                    buy = "BUY 5 con ma50 > and 300 < 60 min ago AND 50<100 and 5-28 > 0.29 (SI !) - riga 7264"
                    action = "buy"
                    percentage = 70
                    
                    
                    
                    
                    
                    
                 
                    
                # BUY 5 di emergenza CROLLO FERRARI - modo 1
                
                elif (
                    ma2_last > ma2_2_min_ago
                    and deviation_buy_crollo_1 < -2.30
                    and ma3_last > ma28_last
                ):
                    buy = "BUY 5 di emergenza CROLLO FERRARI - modo 1 - 3-28 - r 7282"
                    action = "buy"
                    percentage = 80
                    
                    # deviation_buy_crollo_1 = ma8_last / ma78_last
                    # SALTA IL BUY 2 allora ho fatto il BUY 3 di emergenza (se <-2.30 si attiva 8-25)
                    
                    
                    
                    
                    
                    
                elif (
                    ma50_last >= ma50_2_min_ago
                    and ma78_last > ma150_last
                    
                    and deviation_ma5_sotto_ma200 > 0.05
                    
                    and deviation_ma3_sopra_ma10 > 0.17
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
                    buy = "BUY 5 con ma50 > AND 50<100 and 5-28 > 0.31 (SI !) (PER SPEZZARE LA CATENA un po' di meno - vs effetti laterali) - r 7314 a"
                    action = "buy"
                    percentage = 70
                    
                    # deviation_bellissima = 6/30
                    # spezzare la catena dei buy - effetti laterali.
                    # se e' arrivato il buy 5 e' molto probabile che il trend sia consolidato
                    # e, a questo punto, non importa se compra con un + 0.10 piu' in alto. NON FA UNA GRANDE DIFFERENZA !
                    
                elif (
                    ma50_last >= ma50_2_min_ago
                    and ma78_last < ma150_last
                    
                    and deviation_ma5_sotto_ma200 < 0.05
                    and deviation_ma5_sotto_ma200 > -0.35
                    
                    and deviation_ma3_sopra_ma10 > 0.17
                    and deviation_ma5_sopra_ma28 > 0.35
                    
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
                    buy = "BUY 5 con ma50 > AND 50<100 and 5-28 > 0.31 (SI !) (PER SPEZZARE LA CATENA un po' di meno - vs effetti laterali) - r 7314 b"
                    action = "buy"
                    percentage = 70
                    
                    # deviation_bellissima = 6/30
                    # spezzare la catena dei buy - effetti laterali.
                    # se e' arrivato il buy 5 e' molto probabile che il trend sia consolidato
                    # e, a questo punto, non importa se compra con un + 0.10 piu' in alto. NON FA UNA GRANDE DIFFERENZA !
                    
                    
                    
                elif (
                    ma50_last >= ma50_2_min_ago
                    and ma78_last < ma150_last
                    
                    and deviation_ma5_sotto_ma200 < -0.35
                    
                    and deviation_ma3_sopra_ma10 > 0.17
                    and deviation_ma5_sopra_ma28 > 0.33
                    
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
                    buy = "BUY 5 con ma50 > AND 50<100 and 5-28 > 0.31 (SI !) (PER SPEZZARE LA CATENA un po' di meno - vs effetti laterali) - r 7314 c"
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
                    buy = "BUY 5 CON TUTTE LE ma IN CRESCITA - r 7352"
                    action = "buy"
                    percentage = 70
                    
                    # deviation_buy3 = ma4_last/ma30_last
                    # and deviation > -0.30 perche' se va un po' troppo giu' dal SELL 2 (last_trade_price) DEVE RICOMINCIARE dal BUY 1 !
                    
                    
                    
                    
                    
                # ATTENZIONE ! AL BUY 5 TRANNE CHE IN UNA EVENTUALE CORREZIONE HO MESSO 78>150 STIAMO AL BUY 5 PERDIO !
                # SENZA QUESTA 78>150 HO AVUTO MOLTI PROBLEMI !
                
                
                elif (
                    ma78_last >= ma78_2_min_ago
                    and ma78_last > ma150_last
                    
                    and deviation_ma4_sopra_ma100 > 0.10
                    
                    and deviation_buy3 > 0.10
                    and deviation_bellissima > 0.10
                    and ma3_last > ma13_last
                    and deviation_ma7_sopra_ma40 > 0.10
                    and ma4_last > ma9_last
                    and ma4_last > ma50_last
                    and ma6_last > ma15_last
                    and ma7_last > ma25_last
                    and ma2_last >= ma2_2_min_ago
              
                ):
                    buy = "BUY 5A con ma78 > and deviation_bellissima > 0.163 (PER SPEZZARE LA CATENA - effetti laterali) - r 7384"
                    action = "buy"
                    percentage = 70
                    
                    # deviation_bellissima = 6/30
                    # spezzare la catena dei buy - effetti laterali !
                    # se e' arrivato il buy 5 e' molto probabile che il trend sia consolidato
                    # e, a questo punto, non importa se compra con un + 0.10 piu' in alto. NON FA UNA GRANDE DIFFERENZA !
                    
                    # > vacanza anticipato buy
                    
                
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
                    buy = "BUY 5B RIVOLUZIONARIO che NON SPEZZA LA CATENA SE ma200> 120 min) - r 7410"
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
                    buy = "BUY 5C RIVOLUZIONARIO con ma78 > and deviation_bellissima > 0.163 (PER SPEZZARE LA CATENA -effetti laterali) - r 7441"
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
                    
                    buy = "BUY 5 copiata da BUY 1 r1313 con modifiche - riga 7475"
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
                    buy = "BUY 5D RIVOLUZIONARIO con ma78 < and deviation_bellissima > 0.163 - r 7502"
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

                    buy = "BUY 5 RIALZO IMPROVVISO con 200 < tentando di evitare falsi acquisti DOPO TANTO TEMPO DI TREND LATERALE - POTREBBE SUCCEDERE ! - r 7538"
                    action = "buy"
                    percentage = 70
                    
                    # da 1.20 a 1.1 !
                    
                    
                    
                    
                # RIALZO IMPROVVISO 200> DOPO TANTO TEMPO DI TREND LATERALE - POTREBBE SUCCEDERE !
                
                elif (
                    ma200_last > ma200_20_min_ago
                    and deviation_rialzo_improvviso_sopra > 0.69
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
             
                    buy = "BUY 5 RIALZO IMPROVVISO con 200 > e con > 0.72 DOPO TANTO TEMPO DI TREND LATERALE - POTREBBE SUCCEDERE e' successo ! - r 7563"
                    action = "buy"
                    percentage = 70
                    
                    # 6 giu 2022 deviation rialzo improvviso a 0.82 da 0.62
                    # 1 luglio a 0.72 da 0.82
                    # > estate 0.69 da 0.72
                    
                
                # BUY 5 29 ago 2022 > 120 min di ribasso 78>150
                
                elif (
                    
                    ma18_last > ma100_last
                    and ma78_last > ma150_last
                    
                    and ma100_last < ma100_120_min_ago
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and deviation_ma5_sopra_ma28 > 0.08
                    and ma2_last >= ma2_2_min_ago
                    
                ):
                    buy = "BUY 5 29 ago 2022 > 120 min di ribasso 78>150 - r 7564 A1"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                    
                    
                # BUY 5 29 ago 2022 > 120 min di ribasso 78<150
                
                elif (
                    
                    ma18_last > ma100_last
                    and ma78_last < ma150_last
                    
                    and ma100_last < ma100_120_min_ago
                    and ma200_last < ma200_120_min_ago
                    and ma300_last < ma300_120_min_ago
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and deviation_ma3_sopra_ma10 > 0.07
                    and deviation_ma5_sopra_ma28 > 0.12
                    and ma2_last >= ma2_2_min_ago
                    
                ):
                    buy = "BUY 5 29 ago 2022 > 120 min di ribasso 78<150 - r 7564 A2"
                    action = "buy"
                    percentage = 90
                    
                    # 19 set 2022 aggiunta 3-10 0.07 
                    
                    
                    
                    
                # BUY 5 29 ago 2022 > 180 min di ribasso 78>150
                
                elif (
                    
                    ma18_last > ma100_last
                    and ma78_last > ma150_last
                    
                    and ma100_last < ma100_180_min_ago
                    and ma200_last < ma200_180_min_ago
                    and ma300_last < ma300_180_min_ago
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and deviation_ma5_sopra_ma28 > 0.02
                    and ma2_last >= ma2_2_min_ago
                    
                ):
                    buy = "BUY 5 29 ago 2022 > 180 min di ribasso 78>150 - r 7564 B1"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                # BUY 5 29 ago 2022 > 180 min di ribasso 78<150
                
                elif (
                    
                    ma18_last > ma100_last
                    and ma78_last < ma150_last
                    
                    and ma100_last < ma100_180_min_ago
                    and ma200_last < ma200_180_min_ago
                    and ma300_last < ma300_180_min_ago
                    
                    and ma100_last < ma200_last
                    and ma200_last < ma300_last
                    
                    and deviation_ma5_sopra_ma28 > 0.13
                    and ma2_last >= ma2_2_min_ago
                    
                ):
                    buy = "BUY 5 29 ago 2022 > 180 min di ribasso 78<150 - r 7564 B2"
                    action = "buy"
                    percentage = 90
                    
                    
                    
                    
                    
                    
                    
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
              
                    buy = "BUY 5 PAZZA DURANTE UNA piccola CORREZIONE che non e' un forte ribasso e non e' un crollo ! con deviation_correzione - r 7588"
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
                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.23 - r 7685"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                 
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.27 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.27 - 0.60 LA PRIMA FINTA DI MARADONA - r 7699"
                        action = "sell"
                        
                        
                
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.61 and deviation_sell < 0.79
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.61 - 0.79 IL PRIMO DRIBBLING ALLA RONALDO  - r 7711"
                        action = "sell"

                    # attenzione : tacco di allah e dribbling alla ronaldo SOLO con ma50> (altrimenti si attivano in "sell durante il crollo" che ha le sue leggi.)
                    
                    
                
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 0.80 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell 0.80 - 1.20 ( DOPPIA FINTA ALLA RONALDO ! ) - r 7726"
                        action = "sell"
                        
                        
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 1.21 and deviation_sell < 1.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell 1.21-1.7( TACCO DI ALLAH ! ) - r 7738"
                        action = "sell"
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 1.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell > 1.71 ( SI VA TRA GLI ANGELI, compa ! ) - r 7751"
                        action = "sell"
                        
                   
                
                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (0-3 min) con ma50 < and incrocio 3-28 - r 7764"
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
                        sell = "SELL 1 (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.29 SOTTO RIALZO RIALZO - GIORNO - r 7785"
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
                        sell = "SELL 1 (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 SOTTO RIBASSO RIBASSO - NOTTE - r 7804"
                        action = "sell"
                        
                        
                   
                 
                    # ---------------------------------------------------------------------------------------------------------------------- crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - r 7818"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                   
                
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - r 7832"
                        action = "sell"
                        
                        
                      
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                        and deviation_sell > 0.61 and deviation_sell < 0.80
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - r 7845"
                        action = "sell"
                  
               
            
            
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma2_prev > ma5_prev and ma2_last < ma5_last)
                        and deviation_sell > 0.81
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - r 7858"
                        action = "sell"
             
            
            
                ################################################################################################################## sessione 1 ( 3-5 min )

                # VENDITA - da 3 a 5 minuti = da 180 a 300 secondi

                elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 300:
                    
                    if (
                        ma50_last >= ma50_2_min_ago
                        and ma78_last > ma200_last
                        
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.27 CON 78>200 - r 7878 a"
                        action = "sell"
                         
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma78_last < ma200_last
                        
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell < -0.24
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.24 CON 78<200 - r 7894 b"
                        action = "sell"
                         
                        # deviation_sell = ma3_last/last_trade_price
                        
                
                
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.27 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                       
                        
                    ):
                        sell = "SELL 1 (3-5 min) con ma50> 5-25 and deviation_sell 0.27 - 0.60 - la prima FINTA ALLA MARADONA - r 7910"
                        action = "sell"
                         
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                     
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.61 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 > and incrocio 3-15 and deviation_sell 0.91 - 1.20 DRIBBLING ALLA RONALDO - r 7925"
                        action = "sell"
                        
                        
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 1.21 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 > and incrocio 3-20 and deviation_sell 1.21 -2.70 ( TACCO DI ALLAH ! ) - r 7937"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 > and incrocio 3-11 and deviation_sell > 2.71 ( SI VA TRA GLI ANGELI, comba ! ) - r 7949"
                        action = "sell"
                        
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 < and incrocio 3-28 - r 7964"
                        action = "sell"
                        
                        # deviation_sell_ma78 = ma3_last / ma78_last
                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.25
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.25 - r 7978"
                        action = "sell"

                    
                    
                    
                    # guadagno durante il crollo o il trend discendente
                     
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23 and deviation_sell < 0.80
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-23 and gain > 0.23 - r 7992"
                        action = "sell"
                        
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma2_prev > ma8_prev and ma2_last < ma8_last)
                        and deviation_sell > 0.81 and deviation_sell < 1.70
                        and ma2_last < ma2_2_min_ago

                    ):

                        sell = "SELL 1 CROLLO (3-5 min) con ma50 < and incrocio 2-8 and gain > 0.81-1.70 - r 8006"
                        action = "sell"

                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma9_prev and ma3_last < ma9_last)
                        and deviation_sell > 1.71
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-9 and gain > 1.71 - r 8019"
                        action = "sell"
                        
                        
                     

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 8031"
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
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - r 8052"
                        action = "sell"

                    # guardare la stella (guardare da una stella!)
                    # QUESTO E' IL RISCHIO PIU' GRANDE CHE PRENDO ! ( ma con ma50 > ma50 2 min ago DOPO 5 min (+2))
                    # deviation_sell = ma3_last/last_trade_price 
                    
                    
                      
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.28
                        and ma2_last < ma2_2_min_ago
                  
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.28 - r 8069"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        
                        and deviation_sell > 0.27 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                    
                    ):
                        sell = "SELL 1 (5-12 min) con ma50> 5-25 and deviation_sell 0.27 - 0.60 - FINTA ALLA MARADONA - r 8085"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                      
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma13_last
                        
                        and deviation_sell > 0.61 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 >  3-13 and deviation_sell 0.61 - 0.90 - DRIBBLING ALLA RONALDO - r 8101"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 3-15 and deviation_sell 0.91 - 1.20 ( DOPPIA FINTA ALLA RONALDO ) - r 8117"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 1.21 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 3-15 and deviation_sell 1.21-2.70 ( TACCO DI ALLAH ! ) - r 8132"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 > and incrocio 3-11 and deviation_sell > 2.71 ( SI STA TRA GLI ANGELI, compa! ) - r 8144"
                        action = "sell"
                        
                        
                      
                    
                    
                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.49
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 < and incrocio 3-28 and deviation_sell < -0.49 - r 8159"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 < and incrocio 3-100 (cuscino di sant' antonio) - r 8173"
                        action = "sell"
                        
                        
                    
                    
                    # ------------------------------------------------------------------------------- guadagno con crollo
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23 and deviation_sell < 0.54
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 < GUADAGNO DURANTE IL CROLLO 0.23-0.54 con incrocio 3-23 - r 8189"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 0.55
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (5-12 min) con ma50 < GUADAGNO DURANTE IL CROLLO > 0.55  and incrocio 3-13 - r 8200"
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
                        sell = "SELL 1 PARACADUTE CROLLO distanza< ma100-ma200 (5-12 min) Ema50< E ma3<ma16 and deviation_sell< -0.35 - GIORNO- r 8219"
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
                        sell = "SELL 1 PARACADUTE CROLLO 300 > distanza> ma100-ma200 (5-12 min) e ma50< and ma3 < ma16 and dev_sell < -0.35  - NOTTE - r 8246"
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
                        sell = "SELL 1 PARACADUTE CROLLO 300 < distanza> ma100-ma200 (5-12 min) e ma50< and ma3 < ma16 and dev_sell < -0.47  - NOTTE - r 8267"
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
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-72 and deviation sell -0.65 e vaffanculo ! - r 8294"
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
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.39 - r 8313"
                        action = "sell"
                        
                        # viva sant' antonio !
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.27 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 1 (12-21 min) con ma50> and 5 < 25 and deviation_sell 0.27-0.56 - FINTA ALLA MARADONA - r 8328"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last > ma300_last
                        
                        and ma3_last < ma22_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 1 (12-21 min) con ma50> and 3 < 22 con 3 sopra 300 (NO INCROCIO 3-13) and dev_sell 0.57-0.90 - DOPPIO PASSO RONALDO - r 8346 a"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma300_last
                        
                        and ma3_last < ma13_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 1 (12-21 min) con ma50> and 3<13 con 3 soto 300 (NO INCROCIO 3-13) and dev_sell 0.57-0.90 - DOPPIO PASSO RONALDO - r 8362 b"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 ( DOPPIA FINTA ALLA RONALDO ) - r 8379"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.21 and deviation_sell < 1.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-30 and deviation_sell 1.21-1.70 ( IL TACCO DI ALLAH ) - r 8394"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 1.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 > and incrocio 3-15 and deviation_sell > 1.71 ( SI STA TRA GLI ANGELI, compa ! ) - r 8406"
                        action = "sell"
                        
                        
                      
                    
                    ##########################################################################################
                    
                    # NON TOCCARE ! CUSCINO DI SANT' ANTONIO !
                    # L' INCROCIO 5-100 MI SALVA ! MA 5<100 VENDE DURANTE IL RIBASSO !
                    
                    
                    ##################################################################### con trend discendente
                    
                    
                    # RAFFORZATO DA 100>300
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last > ma300_last
                        and ma300_last > ma300_120_min_ago
                        and deviation_ma39 < -0.16
                        and deviation_sell < -0.38
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (12-21 min) RAFFORZATO con 300 > 120 min ago e con ma50 < and deviation_ma39 < -0.16 and deviation_sell < -0.38 - r 8431 A"
                        action = "sell"
                        
                        # 22 set dev sell -0.38 da -0.36
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last > ma300_last
                        and ma300_last < ma300_120_min_ago
                        
                        and deviation_ma39 < -0.16
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (12-21 min) RAFFORZATO ma 300 < 120 min ago e con ma50 < and deviation_ma39 < -0.16 and deviation_sell < -0.36 - r 8431 B"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last < ma300_last
                        and deviation_ma39 < -0.159
                        and deviation_sell < -0.34
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 < and deviation_ma39 < -0.159 and deviation_sell < -0.34 - r 8444"
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
                        sell = "SELL 1 (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - r 8469"
                        action = "sell"
                        
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50 < !
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - r 8483"
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
                        sell = "SELL 1 PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 8499"
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
                        sell = "SELL 1 eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3-28 and deviation_sell 0.25-0.80 - r 8520"
                        action = "sell"
                        
                        # 15 giu 2022 3-28 da 3-16
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 0.81
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3-11 and deviation_sell > 0.81 - r 8538"
                        action = "sell"
                        
                   
                
                    # ----------------------------------------------------------------------------- torna a casa durante il crollo con minor danno 
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 < -0.40
                        and (ma3_prev > ma36_prev and ma3_last < ma36_last)
                        and deviation_sell < -0.335
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 torna a casa durante il crollo con minor danno  (12-21 min) con ma50 < and incrocio 3-36 and dev_sell < -0.335 - r 8551"
                        action = "sell"
                        
                        #  1 giugno 2022 -0.27 da -0.25
                        # 21 lug 2022 -0.30 da -0.27
                        #  3 set 2022 -0.325 da -0.30
                        # 21 set 2022 -0.335 da -0.325
                        
                
                
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
                        sell = "SELL 1 (21-50 min) con ma50> and incrocio 3-78 and deviation_sell<-0.65 - r 8573"
                        action = "sell"
                        
                        # VENDITA IN BASSO 
                        # and deviation_ma39 < -0.16 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        # and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        # and deviation_sell < -0.26
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma8_sotto_ma300 > -1.00
                        
                        and deviation_sell < -0.33
                        and ma3_last < ma50_last
                        and ma2_last < ma2_2_min_ago
                    
                    ):
                        sell = "SELL 1 (21-50 min) con ma50> and deviation_sell <-0.32 and ma3_last < ma50_last - con 8 sotto 300 > -1.00 - r 8595 a"
                        action = "sell"
                        
                        # VENDITA 1 IN ALTO dopo BUY IN RISALITA
                        # and deviation_ma39 < -0.16 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        # and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        # and deviation_sell < -0.26
                        # deviation_sell = ma3_last/last_trade_price
                        # deviation_ma8_sotto_ma300 = ma8_last / ma300_last
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma8_sotto_ma300 < -1.00
                        
                        and deviation_sell < -0.34
                        and ma3_last < ma50_last
                        and ma2_last < ma2_2_min_ago
                    
                    ):
                        sell = "SELL 1 (21-50 min) con ma50> and deviation_sell <-0.34 and ma3_last < ma50_last - con 8 sotto 300 < -1.00 - r 8615 b"
                        action = "sell"
                        
                        # VENDITA 1 IN ALTO dopo BUY IN RISALITA
                        # and deviation_ma39 < -0.16 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        # and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        # and deviation_sell < -0.26
                        # deviation_sell = ma3_last/last_trade_price
                        # deviation_ma8_sotto_ma300 = ma8_last / ma300_last
                        
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.29
                        and ma300_last > ma300_120_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.29 - r 8636"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.26
                        and ma300_last < ma300_120_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.26 - r 8652"
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
                        sell = "SELL 1 (21-50 min) con ma50 > and 5-39 and deviation_sell 0.34 - 0.56 la prima FINTA ALLA MARADONA  - GIORNO - r 8680"
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
                        sell = "SELL 1 (21-50 min) con ma50 > and 3-50 and deviation_sell 0.34-0.56 FINTA ALLA MARADONA - - CREPUSCOLO - r 8703"
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
                        sell = "SELL 1 (21-50 min) con ma50 > and 5-33 and deviation_sell 0.51 - 0.90 ELASTICO ALLA RONALDO E 100 > 300 - GIORNO - r 8740 a"
                        action = "sell"
                        
                        # dopo 26 minuti non c'e' piu' quello scatto in avanti - dribbling- che si verifica nei primi minuti
                        # deviation_sell = ma3_last/last_trade_price
                        # 5-22 (era 4-15)
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma300_last
                        
                        and delta_1 < delta_2
                        and ma100_last > ma100_60_min_ago
                        
                        and ma5_last < ma39_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and 5-39 and deviation_sell 0.51 - 0.90 ELASTICO ALLA RONALDO MA 100 < 300- GIORNO - r 8761 b"
                        action = "sell"
                        
                        # dopo 26 minuti non c'e' piu' quello scatto in avanti - dribbling- che si verifica nei primi minuti
                        # deviation_sell = ma3_last/last_trade_price
                        # 5-22 (era 4-15)
                        # 5-39 da 5-22 dopo le dolomiti !
                        
                        
                        
                        
                        
                        
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
                        sell = "SELL 1 (21-50 min) con ma50 > and 3-50 and deviation_sell 0.51-0.90 ELASTICO ALLA RONALDO - CREPUSCOLO - r 8789"
                        action = "sell"
                        
                        # dopo 26 minuti non c'e' piu' quello scatto in avanti - dribbling- che si verifica nei primi minuti
                        # deviation_sell = ma3_last/last_trade_price
                        # 100 deve stare sopra 200 per non vendere con ma50 durante il crollo o un forte ribasso
                        
                        
                        
                        
                        
                        
                 
                    #######################################################################################################
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last > ma300_last
                        and (ma4_prev > ma50_prev and ma4_last < ma50_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and incrocio 4-50 se 3 sopra 300 and deviation_sell 0.91 - 1.20 (DOPPIA FINTA DI RONALDO) - r 8829 A"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # 28 set 4-50 da 3-25
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma300_last
                        and (ma3_prev > ma42_prev and ma3_last < ma42_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and incrocio 3-42 se 3 sotto 300 and deviation_sell 0.91 - 1.20 (DOPPIA FINTA DI RONALDO) - r 8829 B"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma4_prev > ma28_prev and ma4_last < ma28_last)
                        and deviation_sell > 1.21 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and incrocio 4-28 and deviation_sell 1.21 - 2.70 (DOPPIO PASSO DI RONALDO)- r 8844"
                        action = "sell"
                        
                  
               
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma9_prev and ma3_last < ma9_last)
                        and deviation_sell > 2.71 and deviation_sell < 5.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and incrocio 3-9 and deviation_sell 2.71 - 5.70 (TACCO DI ALLAH) - r 8856"
                        action = "sell"
                        
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell > 5.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and incrocio 3-39 and deviation_sell > 2.71 (SI STA TRA GLI ANGELI, comba !) - r 8868"
                        action = "sell"
                        
                    
                    
                    ############################################################################## CUSCINO DI SANT' ANTONIO per questo segmento di tempo !
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last > ma200_last
                        
                        and ma100_last > ma100_60_min_ago
                        and ma5_last < ma100_last
                        and deviation_sell < -0.29
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and 5-100 and deviation_sell < -0.29 CUSCINO DI SANT' ANTONIO se ma100 > E 100 > 200- r 8886 A"
                        action = "sell"
                        
                        # 19 giu 2022 dev sell a 0.26 da 0.24
                        # 29 giu 2022 dev sell a 0.29 da 0.26
                        
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma200_last
                        and ma300_last > ma300_301_min_ago
                        and ma100_last > ma100_60_min_ago
                        and ma5_last < ma100_last
                        and deviation_sell < -0.25
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and 5-100 and deviation_sell < -0.25 CUSCINO DI SANT' ANTONIO se ma100 > MA 100 < 200 - r 8904 B1"
                        action = "sell"
                        
                        # se 300 > 301 min ago aumenta tolleranza dev sell
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma200_last
                        and ma300_last < ma300_301_min_ago
                        and ma100_last > ma100_60_min_ago
                        and ma5_last < ma100_last
                        and deviation_sell < -0.24
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and 5-100 and deviation_sell < -0.24 CUSCINO DI SANT' ANTONIO se ma100 > MA 100 < 200 - r 8904 B2"
                        action = "sell"
                        
                        
                        
                        
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and ma300_last > ma300_120_min_ago
                        and ma40_last > ma100_last
                        and ma5_last < ma100_last
                        and deviation_sell < -0.35
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and 5-100 and deviation_sell < -0.35 CUSCINO DELLA MADONNA se ma100 < MA 300 > E 40 > 100 - r 8922 A"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and ma300_last > ma300_120_min_ago
                        and ma40_last < ma100_last
                        and ma5_last < ma100_last
                        and deviation_sell < -0.34
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 > and 5-100 and deviation_sell < -0.34 CUSCINO DELLA MADONNA se ma100 < MA 300 > E 40 < 100 - r 8922 B"
                        action = "sell"
                        
                        # > estate -0.34 da -0.27
                        
                        
                    
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and ma300_last < ma300_120_min_ago
                        
                        and ma200_last > ma200_60_min_ago
                        
                        
                        and ma5_last < ma100_last
                        and deviation_sell < -0.26
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50> and 5-100 and dev_sell< -0.26 se ma100< CUSCINO DELLA MADONNA  E DE SANTO RENATO 300 < MA 200> - r 8944"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and ma300_last < ma300_120_min_ago
                        
                        and ma200_last < ma200_60_min_ago
                        
                        and ma5_last < ma100_last
                        and deviation_sell < -0.32
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 (21-50 min) con ma50> and 5-100 and dev_sell< -0.32 se ma100< CUSCINO DELLA MADONNA E DE SANTO RENATO 300 < CON 200< - r 8962"
                        action = "sell"
                        
                        # > estate dev sell -0.32 da -0.25
                        
               
                    ################################################################################################ con trend discendente 
                    ################################################################################################ con ma100 DISTANTE sopra dalla ma300
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.16
                        and deviation_sell < -0.29
                        and ma2_last < ma2_2_min_ago
                        
                        and deviation_ma100_sopra_ma300 > 0.69
                    ):   
                        sell = "SELL 1 (21-50 min) con ma50 < con deviation_ma39 <-0.16 and dev_sell< -0.29 TREND CRESCITA (100 sopra 300 > 0.69) - r 8978"
                        action = "sell"
                        
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # cuscino dell' angelo custode
                        
                        
                        
                    
                    # cuscino sant' antonio
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                        and ma8_last > ma39_last
                        and deviation_ma100_sopra_ma300 > 0.69
                        and deviation_sell < -0.15
                        and ma5_last < ma100_last
                    ):
                        sell = "SELL 1 (21-50 min)con ma50 < CUSCINO SANT' ANTONIO (5-100) MA SOLO con TREND CRESCITA (100 sopra 300 > 0.69) E 8>39 - r 8997 a"
                        action = "sell"
                        
                        
                    # cuscino sant' antonio
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                        and ma8_last < ma39_last
                        and deviation_ma100_sopra_ma300 > 0.69
                        and deviation_sell < -0.12
                        and ma5_last < ma100_last
                    ):
                        sell = "SELL 1 (21-50 min)con ma50 < CUSCINO SANT' ANTONIO (5-100) MA SOLO con TREND CRESCITA (100 sopra 300 > 0.69) E 8<39 - r 8997 b"
                        action = "sell"
                        
                        
                  
                    # TREND LATERALE (100/300  <0.69 and >-0.77) NON TOCCARE 
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.17
                        and ma2_last < ma2_2_min_ago
                        
                        and deviation_ma100_sopra_ma300 < 0.69
                        and deviation_ma100_sopra_ma300 > -0.77
                        and deviation_sell < -0.21
                        
                        and ma3_last < ma300_last
                    ):
                        sell = "SELL 1 NON TOCCARE (21-50 min) con ma50 < con dev_ma39 <-0.17 E dev_sell < -0.21 TREND LATERALE (100>300 <0.69 and >-0.77) - r 9016"
                        action = "sell"
                        
                        # OGGI 22 LUG 2022 QUESTA SU RCCR HA FATTO -0.56 MENTRE MADOG HA FATTO -1.43 !
                        
                        # > estate -0.21 da -0.18
                        
                        
                        
                        
                        
                    # TREND LATERALE (100/300  < 0.69 and > -0.77)
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma300_last > ma300_301_min_ago
                        and deviation_sell  < -0.35
                        
                        and deviation_ma100_sopra_ma300 < 0.69
                        and deviation_ma100_sopra_ma300 > -0.77
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 < e deviation_sell < -0.35 TREND LATERALE (100>300 <0.69 and > -0.77) - r 9017 A"
                        action = "sell"
                        
                        # HO AVUTO UN PROBLEMA GRANDE ! ha venduto con -0.14 ma io avevo -0.20 e -0.27 !!! ore 15:30 25 mag 2022
                        # DEVIATION 3-39 DIVENTA 4-39 (deviation_correzione_2)
                        # DEVIATION SELL DIVENTA 5-last trade price (deviation)
                        
                        # non mi arrendo !
                        # > estate -0.34 da -0.30
                        # con 300 > 301 min ago -0.35 da -0.34
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma300_last < ma300_301_min_ago
                        and deviation_sell  < -0.34
                        
                        and deviation_ma100_sopra_ma300 < 0.69
                        and deviation_ma100_sopra_ma300 > -0.77
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 < e deviation_sell < -0.34 TREND LATERALE (100>300 <0.69 and > -0.77) - r 9017 B"
                        action = "sell"
                        
                        # HO AVUTO UN PROBLEMA GRANDE ! ha venduto con -0.14 ma io avevo -0.20 e -0.27 !!! ore 15:30 25 mag 2022
                        # DEVIATION 3-39 DIVENTA 4-39 (deviation_correzione_2)
                        # DEVIATION SELL DIVENTA 5-last trade price (deviation)
                        
                        # non mi arrendo !
                        # > estate -0.34 da -0.30
                    
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
                        and deviation_ma39 < -0.28
                        and deviation_ma50_sotto_ma300 > 0.50
                    ):
                        sell = "SELL 1 maestro parte 1 (21-50 min) con ma50 < and deviation_ma39 < -0.28 - r 9048"
                        action = "sell"
                        
                        # 27 giu 2022 deviation_ma39 < -0.28 da -0.27
                        
                        
                        
                    
                    
                    
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
                        sell = "SELL 1 maestro parte 2 300>120 e 300>20 (21-50 min) con ma50 < and deviation_sell < -0.36 - r 9072"
                        action = "sell"
                        
                        
                        
                        
                    elif (        
                        ma50_last < ma50_2_min_ago
                        and ma300_last > ma300_120_min_ago
                        and ma300_last < ma300_20_min_ago
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.33
                        and deviation_ma50_sotto_ma300 < 0.50
                    ):
                        sell = "SELL 1 maestro parte 2 300>120 e 300>20 (21-50 min) con ma50 < and deviation_sell < -0.33 - r 9087"
                        action = "sell"
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    # ECCO inequivocabilmente il crollo !    
                    
                    elif (        
                        ma50_last < ma50_2_min_ago
                        and ma300_last < ma300_120_min_ago
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.36
                        and deviation_ma50_sotto_ma300 < 0.50
                    ):
                        sell = "SELL 1 maestro parte 2 (21-50 min) con ma50 < and deviation_sell < -0.36 - r 9110"
                        action = "sell"
                        
                        # da 0.33 a 0.36 perche' durante il crollo ferrari non devi guardare i centesimi.
                        
                        
                        
                        
                
                 
                    
                    
                    #####################################################################################
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.37
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - r 9130"
                        action = "sell"
                        
                    
                    
                    
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last > ma100_60_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.31
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 < e 100> and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO and deviation_sell < -0.31 - r 9146"
                        action = "sell"
                        
                        
                        
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and ma100_last > ma100_30_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.29
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 < e 100< and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO and dev_sell < -0.30 - r 9162 A"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and ma100_last < ma100_30_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.33
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 < e 100< and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO and dev_sell < -0.33 - r 9174 B"
                        action = "sell"
                        
                        # 18 set -0.33 da -0.29
                        
                        
                        
                        
                        
               
                    
                
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
                        sell = "SELL 1 compa (21-50 min) con ma50 < and deviation_ma39 < -0.28 con > PERDITA TOLLERATA 100>300 DI MOLTO - r 9202 A"
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
                        sell = "SELL 1 (21-50 min) con ma50 < and dev_ma39 < -0.28 AND DEV SELL<-0.25 con > PERDITA TOLLERATA 100 SOPRA 300 NON DI MOLTO - r 9229 B"
                        action = "sell"
                        
                        # and deviation_ma39 < -0.15 or (deviation_sell < 0.10 and ma3_last < ma39_last)
                        
                        # ERRORE GRAVE CORRETTO DAL MAESTRO - VENDEVA MENTRE SALIVA !
                        # ma50_last < ma50_2_min_ago
                        # and ma2_last < ma2_2_min_ago
                        # and deviation_ma39 < -0.25
                        # or deviation_sell < -0.26
                        
                        
                        
                    # perdita tollerata DOPPIA
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma125_last > ma300_last
                        and ma200_last > ma200_120_min_ago
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.35
                        and deviation_trend_ma200 > -0.03
                        and ma200_last > ma300_last
                       
                    ):
                        sell = "SELL 1 compa (21-50 min) con ma50 < and dev_sell < -0.35 con > perdita tollerata doppia (200> 120 min)- r 9255 A"
                        action = "sell"
                        
                        
                    # perdita tollerata SEMPLICE
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma125_last < ma300_last
                        and ma200_last > ma200_120_min_ago
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.33
                        and deviation_trend_ma200 > -0.03
                        and ma200_last > ma300_last
                    
                    ):
                        sell = "SELL 1 compa (21-50 min) con ma50 < and deviation_sell < -0.33 con > perdita tollerata semplice (200> 120 min) - r 9255 B"
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
                        sell = "SELL 1 compa (21-50 min) con ma50 < and deviation_sell < -0.28 con > PERDITA TOLLERATA - r 9273"
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
                        sell = "SELL 1 (21-50 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.40 - CON PERDITA TOLLERATA > - r 9296"
                        action = "sell"
                        
                        
                        

                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        
                        and ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 (21-50 min) con ma50 < and INCROCIO 3-100 -0.30 CUSCINO DI SANT' ANTONIO - CON PERDITA TOLLERATA > - r 9311"
                        action = "sell"
                        
                    
                    
                    
                    # SELL 1 eventuale guadagno ANZI NON PERDITA dopo BUY AUDI E crollo SUCCESSIVO (21-50 min) 
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma33_prev and ma5_last < ma33_last)
                        and deviation_sell < -0.10
                        
                        and ma100_last < ma200_last
                        and ma200_last < ma300_last
                        
                        and ma100_last < ma100_120_min_ago
                        and ma200_last < ma200_120_min_ago
                        and ma300_last < ma300_120_min_ago
                        
                        and deviation_ma200_sotto_ma300 < -0.10
                        
                        and deviation_ma100_sopra_ma300 < -0.20
                        and deviation_ma100_sopra_ma300 > -0.80
                        and deviation_ma100_laterale > -1.00
                        
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 eventuale guadagno ANZI NON GRANDE PERDITA dopo BUY AUDI E crollo SUCCESSIVO (21-50 min) - r 9312"
                        action = "sell"
                        
                        # in questa circostanza drammatica di crollo AUDI INTANTO TE LI PRENDI poi, eventualmente, ci pensa BUY 2
                        
                        # deviation 100 laterale =5/100 >-1.00 significa che questa condizione NON non interviene E' UNA SITUAZIONE DI CROLLO !
                        # si interviene solo nella fascia di mezza cottura ! 
                        # 20 set 2022 dev sell -0.10 da 0.01
                        
                        
                        
                        
                    # -------------------------------------------------------------------------------------- guadagno durante il crollo LEGGERO
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 > -1.20
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 0.30 
                        and deviation_sell < 0.54
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 eventuale GAIN nel crollo LEGGERO (21-50 min) con ma50 < incr 3 -30 and dev_sell 0.30 - 0.54 and dev 5-300 > -1.20- r 9327 A"
                        action = "sell"
                        
                        
                        
                    # -------------------------------------------------------------------------------------- guadagno durante il crollo PESANTE
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 < -1.20
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 0.30 
                        and deviation_sell < 0.54
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 eventuale GAIN nel crollo PESANTE (21-50 min) con ma50 < incr 3-30 and dev_sell 0.30 - 0.54 and dev 5-300 < -1.20 - r 9327 B"
                        action = "sell"
                        
                        # 14 set 3-30 da 3-28
                        
                        
                        
                        
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 0.55
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 eventuale guadagno durante il crollo (21-50 min) con ma50 < incrocio 3 - 11 and deviation_sell > 0.55 - r 9338"
                        action = "sell"
                        
                        
                        
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 > -0.90
                        
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 piccola perdita durante il crollo (21-50 min) con ma50 < incrocio 3 - 18 and dev_sell < -0.27 non e' crollo ! - r 9353 A"
                        action = "sell"
                        
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 < -0.90
                        
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 piccola perdita durante il crollo (21-50 min) con ma50 < incrocio 3 - 18 and dev_sell < -0.27 e' crollo ! - r 9353 B"
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
                        sell = "SELL 1 da 50 a 90 min con ma50 > and deviation_ma39 <-0.22 and deviation_sell < -0.23 - r 9388"
                        action = "sell"
                        
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and ma78_last > ma100_last
                        
                        and ma100_last > ma100_60_min_ago
                        and ma100_last < ma200_last
                        and deviation_ma39 < -0.27
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > and deviation_ma39 < -0.27 CON 78 > 100 - r 9404 a1"
                        action = "sell"
                        
                        # se 100 cresce da 60 min il sistema e' piu' rilassato e non ha fretta di portare a casa un guadagno minimo
                        
                        
                        
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and ma78_last < ma100_last
                        
                        and ma100_last > ma100_60_min_ago
                        and ma100_last < ma200_last
                        and deviation_ma39 < -0.25
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > and deviation_ma39 < -0.25 CON 78 < 100- r 9422 a2"
                        action = "sell"
                        
                        # se 100 cresce da 60 min il sistema e' piu' rilassato e non ha fretta di portare a casa un guadagno minimo
                        
                        
                        
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 > 0.50
                        and ma100_last < ma100_60_min_ago
                        and ma100_last < ma200_last
                        and deviation_ma39 < -0.22
                        and deviation_sell < 0.23
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > and deviation_ma39 < -0.22 and deviation_sell < 0.23 con 5 sopra 300 > 0.50 - r 9440 b1"
                        action = "sell"
                        
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # potrebbe essere situazione di crollo che vende con ma39 e senza deviation sell !
                        # cioe' in una situazione di crollo si porta a casa lo 0.23
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 < 0.50
                        and ma100_last < ma100_60_min_ago
                        and ma100_last < ma200_last
                        and deviation_ma39 < -0.22
                        and deviation_sell < -0.15
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > and deviation_ma39 < -0.22 and deviation_sell < -0.15 con 5 sopra 300 < 0.50 - r 9440 b2"
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
                        sell = "SELL 1 da 50 a 90 min con ma50 > and deviation_sell < -0.23 and ma3_last < ma50_last  - r 9461"
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
                        sell = "SELL 1 da 50 a 90 min con ma50 > and incrocio 5-54 and deviation_sell 0.31-0.52 la prima FINTA ALLA MARADONA RAFFORZATO - r 9493 A"
                        action = "sell"
                        
                        # MARADONA RAFFORZATO accompagna nelle prime fasi di crescita. poi interviene RONALDO se il rialzo comincia a farsi piu' consistente.
                        
                        
                    # la prima FINTA ALLA MARADONA
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma150_last
                        and ma300_last > ma300_120_min_ago
                        
                        and (ma5_prev > ma59_prev and ma5_last < ma59_last)
                        and deviation_sell > 0.32 and deviation_sell < 0.52
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > and incrocio 5-59 and deviation_sell 0.31-0.52 la prima FINTA ALLA MARADONA - r 9493 B"
                        action = "sell"
                        
                        # MARADONA accompagna nelle prime fasi di crescita il titolo. poi interviene RONALDO se il rialzo comincia a farsi piu' consistente.
                        # 30 set 5-59 da 5-52 se 300 > 300 120 min ago
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma150_last
                        and ma300_last < ma300_120_min_ago
                        
                        and (ma5_prev > ma52_prev and ma5_last < ma52_last)
                        and deviation_sell > 0.32 and deviation_sell < 0.52
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > and incrocio 5-52 and deviation_sell 0.31-0.52 la prima FINTA ALLA MARADONA - r 9493 B"
                        action = "sell"
                        
                        # MARADONA accompagna nelle prime fasi di crescita il titolo. poi interviene RONALDO se il rialzo comincia a farsi piu' consistente.
                        
                        
                        
                        
                        
                    
                    
                    
                    ############################################################################ ronaldo 60-90 min dal buy se ma200 > somiglia a maradona
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma300_last > ma300_120_min_ago
                        and ma200_last > ma200_120_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell > 0.53 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50> and incrocio 5-78 se 300 > 120 min ago and deviation_sell 0.51-0.90 RONALDO - r 9514a"
                        action = "sell"
                        
                        # 5-125 da 4-50 dopo le dolomiti
                        # 5-78 tornato a roma dopo le vacanze
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma300_last < ma300_120_min_ago
                        and ma200_last > ma200_120_min_ago
                        and (ma4_prev > ma50_prev and ma4_last < ma50_last)
                        and deviation_sell > 0.53 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50> and incrocio 4-20 se 300 < 120 min ago and deviation_sell 0.51-0.90 RONALDO - r 9514b"
                        action = "sell"
                        
                        
                    
                    
                    ############################################################################ ronaldo 60-90 min dal buy se ma200 < non perdona
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 > 0.59
                        and ma200_last < ma200_120_min_ago
                        and (ma4_prev > ma39_prev and ma4_last < ma39_last)
                        and deviation_sell > 0.53 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50> and incrocio 4-39 and deviation_sell 0.51-0.90 RONALDO - r 9529 a"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 < 0.59
                        and ma200_last < ma200_120_min_ago
                        and (ma4_prev > ma100_prev and ma4_last < ma100_last)
                        and deviation_sell > 0.53 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50> and incrocio 4-100 ! GUARDANDO LE COSE DA LONTANO and deviation_sell 0.51-0.90 RONALDO - r 9529 b"
                        action = "sell"
                        
                        # se 5 non e' distante dalla 300 movimento laterale e 4-100 ritornando dalle dolomiti e guardando le cose da lontano !
                        
                        
                    ##################################################################################################################
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 > 0.40
                        and (ma5_prev > ma48_prev and ma5_last < ma48_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > and incrocio 5-48 and deviation_sell 0.91 - 1.49 RABONA DI RONALDO  5-300 > 0.40 - r 9543 A"
                        action = "sell"
                  
                        # ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 < 0.40
                        and deviation_ma5_sotto_ma300 > 0.01
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > and incrocio 3-33 and deviation_sell 0.91 - 1.49 RABONA DI RONALDO  5-300 0.01 - 0.40 - r 9543 B"
                        action = "sell"
                  
                        # ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 < 0.01
                        and deviation_ma5_sotto_ma300 > -2.00
                        and (ma4_prev > ma48_prev and ma4_last < ma48_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > and incrocio 4-48 and deviation_sell 0.91 - 1.49 RABONA DI RONALDO 5-300 -2.00 - 0.01 - r 9543 C"
                        action = "sell"
                  
                        # ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        
                        and deviation_ma5_sotto_ma300 < -2.00
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > and incrocio 3-33 and deviation_sell 0.91 - 1.49 RABONA DI RONALDO 5-300 < -2.00 - r 9543 D"
                        action = "sell"
                  
                        # ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                    
                    
                    
                    
                    
                        
                        
                    
                    
                    
                    
                    
                    
                    
                    # SELL 1 da 50 a 90 min DOPPIO PASSO ALLA RONALDO 1 (se 50-200 > 0.30 stai un po' piu' tranquillo)
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma50_sotto_ma200 > 0.30
                        and (ma3_prev > ma39_prev and ma3_last < ma39_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 da 50 a 90 min con ma50 > incrocio 3-33 and deviation_sell > 1.50 DOPPIO PASSO ALLA RONALDO se 50-200 > 0.30 - r 9559"
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
                        sell = "SELL 1 da 50 a 90 min con ma50 > incrocio 3-33 and deviation_sell > 1.50 DOPPIO PASSO ALLA RONALDO se 50-200 < 0.30 - r 9575"
                        action = "sell"
                        
                        
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 > 0.50
                        and (ma3_prev > ma42_prev and ma3_last < ma42_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 da 50 a 90 min con ma50 > incrocio 3-11 and deviation_sell > 2.71 TACCO DI ALLAH - r 9591 a"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 < 0.50
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 da 50 a 90 min con ma50 > incrocio 3-13 and deviation_sell > 2.71 TACCO DI ALLAH - r 9603 b"
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
                        sell = "SELL 1 50-90 min IPOTESI PEGGIORE con ma50 < con dev_ma39 <-0.19 and dev sell < -0.22 SOTTO RIBASSO RIBASSO - NOTTE - r 9633"
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
                        sell = "SELL 1 50-90 min con ma50< e dev ma39 < -0.215 e dev sell <-0.30 SOTTO RIALZO RIALZO - GIORNO ! - r 9656"
                        action = "sell"
                        
                        # IPOTESI PEGGIORE MA GIORNO !
                        
                        
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma300_last
                        and deviation_trend_ma200 < -0.10
                        
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.24
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 50 a 90 min IPOTESI PEGGIORE con ma50 < con incrocio 5-78 and deviation_sell < -0.24 - r 9674"
                        action = "sell"
                        
                        # > estate 5-78 da 3-78 e dev sell -0.20 da -0.15
                        # 3 set dev sell -0.24 da -0.20
                        
                        
                        
               
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
                        sell = "SELL 1 50-90 min IPOTESI mediana 1 RAFFORZATA un po' MENO PEGGIO con ma50< E dev_ma39 <-0.20 E deviation_sell < -0.21- r 9694"
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
                        sell = "SELL 1 da 50 a 90 min IPOTESI un po' MENO PEGGIO con ma50 < con dev_ma39 < -0.19 MA 100> and dev_sell < -0.22 - r 9717"
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
                        sell = "SELL 1 da 50 a 90 min IPOTESI un po' MENO PEGGIO con ma50 < con deviation_ma39 <-0.19 E 100< and dev_sell < -0.21 - r 9736"
                        action = "sell"
                        
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma300_last
                        and deviation_trend_ma200 > -0.10
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.15
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 50 a 90 min IPOTESI un po' MENO PEGGIO con ma50 < con incrocio 3-78 and deviation_sell < -0.15 - r 9757"
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
                        sell = "SELL 1 da 50 a 90 min UN PO' MEGLIO con ma50 < con deviation_ma39 <-0.22 and deviation_sell < -0.23 - r 9774"
                        action = "sell"
                        
                        
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma300_last
                        and deviation_trend_ma200 < -0.10
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.17
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 50 a 90 min UN PO' MEGLIO con ma50 < con incrocio 3-78 and deviation_sell < -0.17 - r 9789"
                        action = "sell"
                        
                    
                    ##################################################### sempre con ma50 discendente MA trend ma200> ET ma200 > ma300 - PERDITA TOLLERATA AUMENTA
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma300_last > ma300_120_min_ago
                        and ma200_last > ma300_last
                        and deviation_trend_ma200 > -0.10
                        
                        and ma78_last > ma200_last
                        
                        and deviation_ma39 < -0.23
                        and deviation_sell < -0.35
                        
                        and ma2_last <= ma2_2_min_ago
                    ):
                        sell = "SELL 1 50-90 min con ma50 < E 78 > 200 con dev_ma39 <-0.23 and dev_sell <-0.35 - PERDITA TOLLERATA > e 300 > 120 min ago - r 9807 A1"
                        action = "sell"
                        
                        # ha fatto perdita dell' 1% - forse succede tutto in quei 2 minuti se crolla improvvisamente
                        # con deviation_ma39 < -0.27 E CON con deviation_sell < -0.28
                        # 6 luglio 2022 dev_sell a -0.31 da -0.30
                        
                        
                        
                        
                    ##################################################### sempre con ma50 discendente MA trend ma200> ET ma200 > ma300 - PERDITA TOLLERATA AUMENTA
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma300_last < ma300_120_min_ago
                        and ma200_last > ma300_last
                        and deviation_trend_ma200 > -0.10
                        
                        and ma78_last > ma200_last
                        
                        and deviation_ma39 < -0.23
                        and deviation_sell < -0.33
                        
                        and ma2_last <= ma2_2_min_ago
                    ):
                        sell = "SELL 1 50-90 min con ma50 < E 78 > 200 con dev_ma39 <-0.23 and dev_sell <-0.33 - PERDITA TOLLERATA > e 300 < 120 min ago - r 9807 A2"
                        action = "sell"
                        
                        # ha fatto perdita dell' 1% - forse succede tutto in quei 2 minuti se crolla improvvisamente
                        # con deviation_ma39 < -0.27 E CON con deviation_sell < -0.28
                        # 6 luglio 2022 dev_sell a -0.31 da -0.30
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma300_last
                        and deviation_trend_ma200 > -0.10
                        
                        and ma78_last < ma200_last
                        
                        and deviation_ma39 < -0.23
                        and deviation_sell < -0.29
                        
                        and ma2_last <= ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 50-90 min BEST sempre con ma50< MA 78 < 200 con dev_ma39 <-0.23 and dev_sell <-0.29 - CON PERDITA TOLLERATA > - r 9828 B"
                        action = "sell"
                        
                        # ha fatto perdita dell' 1% - forse succede tutto in quei 2 minuti se crolla improvvisamente
                        # con deviation_ma39 < -0.27
                        # con deviation_sell < -0.28
                        # DEV SELL 0.29 DA 0.295 dopo dolomiti
                        
                    
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last > ma200_last
                        
                        and ma200_last > ma300_last
                        and deviation_trend_ma200 > -0.10
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.29
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 RAFFORZATA da 50-90 min BEST ma sempre con ma50 < con incrocio 3-78 and dev_sell < -0.29 - PERDITA TOLLERATA > - r 9851"
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
                        sell = "SELL 1 da 50-90 min BEST ma sempre con ma50 < con incrocio 3-78 and dev_sell < -0.25 - CON PERDITA TOLLERATA > - r 9867"
                        action = "sell"
                        
                        
                        
                    # AGGIUNTA TARDIVA MA FORSE NECESSARIA !
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and delta_1 < delta_2
                        
                        and ma300_last > ma300_301_min_ago
                        and ma100_last < ma200_last
                        and ma200_last < ma300_last
                        
                        and ma200_last < ma200_120_min_ago
                        and ma300_last < ma300_120_min_ago
                   
                        and deviation_sell < -0.19
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 50-90 min AGGIUNTA TARDIVA MA FORSE NECESSARIA ! and delta_1 < delta_2 and deviation_sell < -0.19 e 300>5 ore - r 9888 a1"
                        action = "sell"
                        
                        
                        
                        
                    # AGGIUNTA TARDIVA MA FORSE NECESSARIA !
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and delta_1 < delta_2
                        
                        and ma300_last < ma300_301_min_ago
                        and ma100_last < ma200_last
                        and ma200_last < ma300_last
                        
                        and ma200_last < ma200_120_min_ago
                        and ma300_last < ma300_120_min_ago
                   
                        and deviation_sell < -0.28
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 50-90 min AGGIUNTA TARDIVA MA FORSE NECESSARIA ! and delta_1 < delta_2 and deviation_sell < -0.28 e 300<5 ore - r 9888 a2"
                        action = "sell"
                        
                        # > estate -0.28 da -0.18
                        
                        
                        
                        
                        
                        
                    # AGGIUNTA TARDIVA MA FORSE NECESSARIA !
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and delta_1 > delta_2
                        and ma100_last < ma200_last
                        and ma200_last < ma300_last
                        
                        and ma200_last < ma200_120_min_ago
                        and ma300_last < ma300_120_min_ago
                   
                        and deviation_sell < -0.22
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da 50-90 min AGGIUNTA TARDIVA MA FORSE NECESSARIA ! and delta_1 > delta_2 and deviation_sell < -0.22 - r 9908 b"
                        action = "sell"
                        
                        # 21 lug 2022 0.22 da 0.175
                        
                        
                        
                    # SELL 1 eventuale guadagno con crollo (50-90 min) con ma50 < and incrocio 5-59 and deviation_sell > 0.45
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma59_prev and ma5_last < ma59_last)
                        and deviation_sell > 0.45
                        
                        and ma100_last < ma200_last
                        and ma200_last < ma300_last
                        
                        and ma100_last < ma100_120_min_ago
                        and ma200_last < ma200_120_min_ago
                        and ma300_last < ma300_120_min_ago
                     
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 eventuale guadagno con crollo (50-90 min) con ma50 < and incrocio 5-59 and deviation_sell > 0.45 - r 9930"
                        action = "sell"
                        
                        # in questa circostanza drammatica di crollo INTANTO TE LI PRENDI poi, eventualmente, ci pensa BUY 2
                        
                        
                        
                        
                        
                        
                    
                        
                        
                        
                        
                
                
                
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
                        sell = "SELL 1 90-110 min con ma50 > and deviation_ma39 <-0.22 and deviation_sell < -0.21 - r 9965"
                        action = "sell"
                        
                        
                        
                    if (    
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma200_last
                        and deviation_ma39 < -0.22 
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 90-110 min con ma50 > and deviation_ma39 <-0.22 - r 9977"
                        action = "sell"
                        
                        # potrebbe essere una situazione di crollo con 39 senza deviation sell !
                        
                        
                        
                        
                        
                       
                    elif (     
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma50_last 
                        and deviation_sell < -0.22
                        and ma25_last < ma25_2_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 90-110 min con ma50 > and ma3_last < ma50_last and deviation_sell < -0.22 and ma25 < - r 9994"
                        action = "sell"
                        
                    
                    
                    ################################################################################### fare maradona 1 ma3>ma100 (69) e maradona 2 ma3<ma100 (50)
                    
                    # MARADONA 1a
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 > 0.49
                        
                        and ma200_last > ma300_last
                        and ma3_last > ma100_last
                        and ma5_last < ma69_last
                        and deviation_sell > 0.35 and deviation_sell < 0.64
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1a 90-110 min con ma50 > con 5-69 (!) and deviation_sell 0.35 - 0.64 la prima FINTA DI MARADONA 1 (non toccare) - r 10012 a"
                        action = "sell"
                        
                        # maradona mentre cresce
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 < 0.49
                        
                        and ma200_last > ma300_last
                        and ma3_last > ma100_last
                        and ma5_last < ma100_last
                        and deviation_sell > 0.35 and deviation_sell < 0.64
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1a 90-110 min con ma50 > con 5-100 (!) and deviation_sell 0.35 - 0.64 la prima FINTA DI MARADONA 1 (non toccare) - r 10012 b"
                        action = "sell"
                        
                        # maradona laterale
                        # 5-100 da 5-69 se andamento laterale 
                        
                    
                    
                    
                    
                    
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
                        sell = "SELL 1b FASE LATERALE 90-110 min con ma50 > con 5-78 (!) and deviation_sell 0.35 - 0.64 la prima FINTA DI MARADONA 1 - r 10033"
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
                        sell = "SELL 1b FASE RIBASSO 90-110 min con ma50 > con 5-69 (!) and deviation_sell 0.35 - 0.64 la prima FINTA DI MARADONA 1 - r 10051"
                        action = "sell"
                        
                        
                    
                    
                    
                    
                    
                    
                    # MARADONA 2
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma100_last
                        and ma5_last < ma50_last
                        and deviation_sell > 0.35 and deviation_sell < 0.64
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 90-110 min con ma50 > con 5-50 (!) and deviation_sell 0.35 - 0.64 la prima FINTA DI MARADONA 1 - r 10071"
                        action = "sell"
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell > 0.65 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 90-110 min con ma50 > incrocio 5-78 (!) and deviation_sell 0.65 - 1.49 RABONA ALLA RONALDO - r 10084"
                        action = "sell"
                        
                        # > estate 5-78 da 5-42
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 90-110 min con ma50 > incrocio 3-78 and deviation_sell  1.50 - 2.70 DOPPIO PASSO DI RONALDO - r 10096"
                        action = "sell"
                        
                        # > estate 3-78 da 3-30
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell > 2.71 and deviation_sell < 5.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 90-110 min con ma50 > incrocio 3-78 (!) and deviation_sell > 2.71 TACCO DI ALLAH - r 10109"
                        action = "sell"
                        
                        # > estate 3-78 da 3-13
                        
                        
                
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma69_prev and ma3_last < ma69_last)
                        and deviation_sell > 5.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 90-110 min con ma50 > incrocio 3-69 (!) and deviation_sell > 5.71 SI STA TRA GLI ANGELI, compa ! - r 10122"
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
                        sell = "SELL 1 90-110 min con ma50 <  and ma100 < con deviation_ma39 <-0.17 - r 10140"
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
                        sell = "SELL 1 90-110 min con ma50 < and ma100 < and (deviation_sell < -0.15 and ma3_last < ma39_last) MA 300>120min ago - r 10158"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                        and deviation_sell < -0.14
                        and ma3_last < ma39_last
                        and ma100_last < ma100_60_min_ago
                        and ma300_last < ma300_120_min_ago
                    ):
                        sell = "SELL 1 90-110 min con ma50 < and ma100 < and (deviation_sell < -0.14 and ma3_last < ma39_last) 300 < 120 min ago - r 10170"
                        action = "sell"
                        
                        # 27 giu 2022 dev sell 0.145 da 0.15
                        
                        # > estate -0.14 da -0.145
                        
                        
                        
                        
                        
                    
                    # ma se ma100 >
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.23
                        and deviation_sell > 0.20
                        and ma5_last < ma5_2_min_ago
                        and ma100_last > ma100_60_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 90-110 min con ma50 < MA ma100 > con deviation_ma39 <-0.23 - r 10193 A"
                        action = "sell"
                        
                        # ma39 NON DEVE VENDERE in fase laterale ma in alto
                        # 28 set con 300 > 300 301 min ago !
                        # 28 set dev 39 -0.23 da -0.20
                        
                        
                        
                        
                    # ma se ma100 >
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.20
                        and deviation_sell > 0.20
                        and ma5_last < ma5_2_min_ago
                        and ma100_last > ma100_60_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 90-110 min con ma50 < MA ma100 > con deviation_ma39 <-0.20 - r 10193 B"
                        action = "sell"
                        
                        # ma39 NON DEVE VENDERE in fase laterale ma in alto
                        
                        
                        
                        
                        
                        
                        
                    
                    
                    # ma se ma100 >
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 > -0.50
                        and ma100_last > ma100_60_min_ago
                        and ma300_last > ma300_120_min_ago
                        
                        and deviation_sell < -0.23
                        and ma3_last < ma39_last
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 90-110 min con ma50< MA ma100> E 300> and (dev_sell < -0.23 and ma3_last < ma39_last) con 5-100 > -0.50 - r 10211 A1"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 > -0.50
                        and ma100_last > ma100_60_min_ago
                        and ma300_last < ma300_120_min_ago
                        
                        and deviation_sell < -0.225
                        and ma3_last < ma39_last
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 90-110 min con ma50< MA ma100> E 300< and (dev_sell < -0.225 and ma3_last < ma39_last) con 5-100 > -0.50 - r 10211 A2"
                        action = "sell"
                        
                        # 19 set dev sell -0.225 da -0.23
                        
                        
                        
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 < -0.50
                        and deviation_sell < -0.28
                        and ma3_last < ma39_last
                        and ma100_last > ma100_60_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 90-110 min con ma50 < MA ma100 > and (deviation_sell < -0.28 and ma3_last < ma39_last) con 5-100 < -0.50 - r 10211 b"
                        action = "sell"
                        
                        
                        
                        
                    
                    
                    ############################################################################### aumento della perdita tollerata ! 50< MA 200> e 200>300
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                        and deviation_ma39 < -0.32
                        and deviation_trend_ma200 > -0.12
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 1 compa 90-110 min con ma50 < and deviation_ma39 < -0.32  con > PERDITA TOLLERATA - r 10227"
                        action = "sell"
                        
                        # > estate -0.32 da -0.23
                        
                    
                    
                    elif (     
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma39_last
                        and deviation_sell < -0.21
                        and ma2_last < ma2_2_min_ago
                        and deviation_trend_ma200 > -0.12
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 compa 90-110 min con ma50 < (deviation_sell < -0.21 and ma3_last < ma39_last) con > PERDITA TOLLERATA - r 10241"
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
                        sell = "SELL 1 dopo 110 min con ma50 > and deviation_ma39 <-0.22 and deviation_sell < -0.21 - r 10260"
                        action = "sell"
                        
                        
                    
                    
                    elif (     
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma50_last 
                        and deviation_sell < -0.22
                        and ma25_last < ma25_2_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 > and ma3_last < ma50_last and deviation_sell < -0.22 and ma25 < - r 10273"
                        action = "sell"
                        
                    
                    
                    
                    ############################################################################# fare maradona 1 e maradona 2
                    
                    
                       
                        
                    # MARADONA 1
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last > ma100_last
                        and ma5_last < ma100_last
                        and deviation_sell > 0.35 and deviation_sell < 0.64
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 > con 5-100 (!) and deviation_sell 0.35 - 0.64 la prima FINTA DI MARADONA 1 (non toccare) - r 10291"
                        action = "sell"
                        
                        # 10 GIU 2022 5-78 da 5-69
                        # > estate 100 da 78
                        
                        
                        
                        
                    # MARADONA 2
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma100_last
                        and deviation_ma100_sopra_ma300 > 0.30
                        and ma7_last < ma54_last
                        and deviation_sell > 0.35 and deviation_sell < 0.64
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 > con 7-54 and dev_sell 0.35 - 0.64 la prima FINTA DI MARADONA 2 CON 100 sopra 300 > 0.30 - r 10310 a"
                        action = "sell"
                        
                        # se 100 sopra 300 >0.30 stai calmo
                        
                        
                        
                        
                    # MARADONA 3
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma100_last
                        and ma3_last < ma10_last
                        
                        and deviation_ma100_sopra_ma300 < 0.30
                        and ma5_last < ma50_last
                        and deviation_sell > 0.35 and deviation_sell < 0.64
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 > con 5-50 and dev_sell 0.35 - 0.64 la prima FINTA DI MARADONA 3 CON 100 sopra 300 < 0.30 - r 10329 b"
                        action = "sell"
                        
                        # 3 set ho aggiunto 3<10 incredibile ma vero vendeva mentre saliva !
                        
                    
                    
                    #################################################################################################
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma42_prev and ma5_last < ma42_last)
                        and deviation_sell > 0.65 and deviation_sell < 1.49
                        and deviation_ma100_sopra_ma200 > 0.45
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 > incrocio 5-42 (!) se 100-200 > 0.45 and deviation_sell 0.65 - 1.49 RABONA ALLA RONALDO - r 10346"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma300_last > ma300_301_min_ago
                        
                        and (ma5_prev > ma125_prev and ma5_last < ma125_last)
                        and deviation_sell > 0.65 and deviation_sell < 1.49
                        and deviation_ma100_sopra_ma200 < 0.45
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 >110 min con 300 > 5 ore ago E con ma50 > E incr 5-125 se 100-200 < 0.45 and dev_sell 0.65 - 1.49 RABONA RONALDO - r 10358 A"
                        action = "sell"
                        
                        # > estate 5-78 da 5-34
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma300_last < ma300_301_min_ago
                        
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell > 0.65 and deviation_sell < 1.49
                        and deviation_ma100_sopra_ma200 < 0.45
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 >110 min con 300 < 5 ore ago E con ma50 > E incr 5-78 se 100-200 < 0.45 and dev_sell 0.65 - 1.49 RABONA RONALDO - r 10358 B"
                        action = "sell"
                        
                        # > estate 5-78 da 5-34
                        # 5-125 se 300
                        
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 > 0.40
                        and (ma3_prev > ma100_prev and ma3_last < ma100_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 dopo 110 min con ma50 > incrocio 3-100 CON 100 sopra 300 > 0.40 and deviation_sell  1.50-2.70 DOPPIO PASSO RONALDO - r 10382 A"
                        action = "sell"
                        
                        # 3 set 2022 ma100 da ma48
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 < 0.40
                        and (ma3_prev > ma50_prev and ma3_last < ma50_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):    
                        sell = "SELL 1 dopo 110 min con ma50 > incrocio 3-30 CON 100 sopra 300 <0.40 and deviation_sell  1.50-2.70 DOPPIO PASSO RONALDO - r 10393 B"
                        action = "sell"
                        
                        # 18 set 3-50 da 3-30
                        
                        
                        
                        
                        
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell > 2.71 and deviation_sell < 5.70
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 > incrocio 3-28 and deviation_sell > 2.71 TACCO DI ALLAH - r 10411"
                        action = "sell"
                        
                        # 1 ott 2022 3-28 da 3-13
                        
                
                
                
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma69_prev and ma3_last < ma69_last)
                        and deviation_sell > 5.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 1 dopo 110 min con ma50 > incrocio 3-69 (!) and deviation_sell > 5.71 SI STA TRA GLI ANGELI, compa ! - r 10424"
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
                        sell = "SELL 1 dopo 110 min con ma50 <  and ma100 < con deviation_ma39 <-0.17 - r 10441"
                        action = "sell"
                        
                        # ma39 non deve vendere laterale (!) quindi per farlo vendere in alto ho dato 0.20
                        
                        
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                        and deviation_sell < -0.218
                        and ma3_last < ma39_last
                        and ma100_last < ma100_60_min_ago
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 < and ma100 < and (deviation_sell < -0.218 and ma3_last < ma39_last) - r 10456"
                        action = "sell"
                        
                        # > estate -0.22 da -0.15
                        # 24 set 2022 -0.218 da -0.22
                        
                        
                        
              
                    # ma se ma100 >
                
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.195
                        and deviation_sell > 0.20
                        and ma5_last < ma5_2_min_ago
                        and ma300_last > ma300_120_min_ago
                        and ma100_last > ma100_60_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 < MA ma100 > E ma300 > e con deviation_ma39 <-0.195 - r 10472 A"
                        action = "sell"
                        
                        # ma39 NON DEVE VENDERE in fase laterale ma in alto
                        
                        
                        
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.193
                        and deviation_sell > 0.20
                        and ma5_last < ma5_2_min_ago
                        and ma300_last < ma300_120_min_ago
                        and ma100_last > ma100_60_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 < MA ma100 > E ma300 < e con deviation_ma39 <-0.193 - r 10472 B"
                        action = "sell"
                        
                        # ma39 NON DEVE VENDERE in fase laterale ma in alto
                        # 26 set dev39 a 0.193 da 0.195
                        
                    
                    
                    
                    # ma se ma100 > 
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                        and deviation_sell < -0.27
                        and ma3_last < ma39_last
                        and ma100_last > ma100_60_min_ago
                        and ma78_last > ma200_last
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 < MA ma100 > and (deviation_sell < -0.27 and ma3_last < ma39_last) - r 10489 a"
                        action = "sell"
                        
                        # 3 luglio 2022 a 0.27 da 0.20
                        
                        
                        
                    # ma se ma100 > 
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                        and deviation_sell < -0.23
                        and ma3_last < ma39_last
                        and ma100_last > ma100_60_min_ago
                        and ma78_last < ma200_last
                    ):
                        sell = "SELL 1 dopo 110 min con ma50 < MA ma100 > and (deviation_sell < -0.23 and ma3_last < ma39_last) - r 10506 b"
                        action = "sell"
                        
                        # 3 luglio 2022 a 0.23 da 0.20
                        
                    
                   
                    ############################################################################### aumento della perdita tollerata ! 50< MA 200> e 200>300
                    
                    
                    
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                        and deviation_ma100_sopra_ma300 > 0.30
                        
                        and deviation_ma39 < -0.25
                        and deviation_trend_ma200 > -0.12
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 1 compa dopo 110 min con ma50 < and deviation_ma39 < -0.23  con > PERDITA TOLLERATA - r 10530"
                        action = "sell"
                        
                        # 18 set dev 39 -0.25 da -0.23
                        
                        
                        
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma2_last < ma2_2_min_ago
                        and deviation_ma100_sopra_ma300 < 0.30
                        and deviation_sell < -0.27
                        
                        and deviation_ma39 < -0.23
                        and deviation_trend_ma200 > -0.12
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 1 compa dopo 110 min con ma50 < and deviation_ma39 < -0.23  and deviation_sell < -0.27 con > PERDITA TOLLERATA - r 10546"
                        action = "sell"
                        
                        # se 100 > 300 di poco metto anche deviation_sell < -0.21
                        # > estate -0.27 da -0.21
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    # SELL 1 da RCCR ! IPOTESI PEGGIORE con ma50< con dev_ma39 < -0.22 and deviation_sell < -0.22 MA DOPPIO DELTA RIALZO 
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        
                        and ma3_last < ma300_last
                        and ma200_last < ma300_last
                        and deviation_trend_ma200 < -0.10
                        
                        and deviation_ma39 < -0.22
                        and deviation_sell < -0.22
                        
                        and rapporto_delta_1_delta_2 < 1
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 da RCCR ! IPOTESI PEGGIORE con ma50< con dev_ma39 < -0.22 and deviation_sell < -0.22 MA DOPPIO DELTA RIALZO - r 10571"
                        action = "sell"
                        
                        # 19 SET r 10546 la condizione precedente ha fatto -1.65 ed e' partita insieme ad altre 2 condizioni speciali ! 
                        # quindi ho aggiunto questa importata SIA QUA CHE NELLE CONDIZIONI SPECIALI ( nuova condizione speciale )
                        # 19 set 2022 IMPORTATO DA RCCR > sell 4:18 del 19 set -1.65 % !
                        # 19 set 2022 deviation_ma39 < -0.22 AND and deviation_sell < -0.22
                        
                        
                        
                        
                    elif (     
                        ma50_last < ma50_2_min_ago
                        and ma300_last > ma300_120_min_ago
                        and ma3_last < ma39_last
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                        and deviation_trend_ma200 > -0.12
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 dopo 110 min E 300 > 120 min ago e con ma50 < (dev_sell < -0.23 and ma3_last < ma39_last) con > PERDITA TOLLERATA - r 10572 A"
                        action = "sell"    
                        
                        
                    elif (     
                        ma50_last < ma50_2_min_ago
                        and ma300_last < ma300_120_min_ago
                        and ma3_last < ma39_last
                        and deviation_sell < -0.21
                        and ma2_last < ma2_2_min_ago
                        and deviation_trend_ma200 > -0.12
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 1 dopo 110 min E 300 < 120 min ago e con ma50 < (dev_sell < -0.21 and ma3_last < ma39_last) con > PERDITA TOLLERATA - r 10572 B"
                        action = "sell"
                        
                        
                        
                    
                    
                    
                    
                    
                    # ATTENZIONE 1 ! > 110 min E CON 300 > 120 min FORSE E' NECESSARA SOLO QUESTA !
                    
                    elif (    
                        ma3_last < ma100_last
                        and ma300_last > ma300_120_min_ago
                        and ma100_last > ma200_last
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                    ):
                   
                        sell = "SELL 1 > 110 min FORSE E' NECESSARA SOLO QUESTA 1 ! deviation_sell < -0.27 - r 10588"
                        action = "sell"
                        
                        
                        
                    # ATTENZIONE 2 ! > 110 min E CON 300 > 120 min FORSE E' NECESSARA SOLO QUESTA !
                    
                    elif (    
                        ma3_last < ma100_last
                        and ma300_last > ma300_120_min_ago
                        and ma100_last < ma200_last
                        and deviation_sell < -0.22
                        and ma2_last < ma2_2_min_ago
                    ):
                   
                        sell = "SELL 1 > 110 min FORSE E' NECESSARA SOLO QUESTA 2 ! deviation_sell < -0.22 - r 10603"
                        action = "sell"
                        
                        
                        
                        
                        
                    # ATTENZIONE 3 ! > 110 min E CON 300 < 120 min FORSE E' NECESSARA SOLO QUESTA !
                    
                    elif (    
                        ma3_last < ma100_last
                        and ma78_last > ma300_last
                        and ma300_last < ma300_120_min_ago
                        and ma100_last > ma200_last
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                   
                        sell = "SELL 1 > 110 min FORSE E' NECESSARA SOLO QUESTA 3 ! deviation_sell < -0.23 CON 78 > 300 - r 10621 a"
                        action = "sell"
                        
                        # > estate a -0.19 da 0.09
                        # 17 set a -0.23 da -0.19
                        
                        
                        
                    # ATTENZIONE 3 ! > 110 min E CON 300 < 120 min FORSE E' NECESSARA SOLO QUESTA !
                    
                    elif (    
                        ma3_last < ma100_last
                        and ma78_last < ma300_last
                        and ma300_last < ma300_120_min_ago
                        and ma100_last > ma200_last
                        and deviation_sell < -0.13
                        and ma2_last < ma2_2_min_ago
                    ):
                   
                        sell = "SELL 1 > 110 min FORSE E' NECESSARA SOLO QUESTA 3 ! dev_sell < -0.13 CON 78 < 300 (ancora ribasso !) porta a casa ! - r 10637 b"
                        action = "sell"
                        
                        # 23 lug 2022 dev sell < 0.10 ha fatto fare perdita di -0.26 !
                        # 23 lug 2022 a < 0.09 da < 0.10
                        # > estate -0.10 da 0.09
                        # -0.13 da -0.10
                        
                        
                    # ATTENZIONE 4 ! > 110 min E CON 300 < 120 min FORSE E' NECESSARA SOLO QUESTA !
                    
                    elif (    
                        ma3_last < ma100_last
                        and ma5_last > ma200_last
                        
                        and ma300_last < ma300_120_min_ago
                        and ma100_last < ma200_last
                        and deviation_sell < -0.15
                        and ma2_last < ma2_2_min_ago
                    ):
                   
                        sell = "SELL 1 > 110 min con 5 > 200 ! FORSE E' NECESSARA SOLO QUESTA 4 ! deviation_sell < -0.15 - r 10655 A"
                        action = "sell"
                        
                        
                    # ATTENZIONE 4 ! > 110 min E CON 300 < 120 min FORSE E' NECESSARA SOLO QUESTA !
                    
                    elif (    
                        ma3_last < ma100_last
                        and ma5_last < ma200_last
                        
                        and ma300_last < ma300_120_min_ago
                        and ma100_last < ma200_last
                        and deviation_sell < -0.10
                        and ma2_last < ma2_2_min_ago
                    ):
                   
                        sell = "SELL 1 > 110 min con 5 < 200 ! FORSE E' NECESSARA SOLO QUESTA 4 ! deviation_sell < -0.10 - r 10655 B"
                        action = "sell"
                        
                        #  4 set 2022 dev sell -0.07 da -0.05
                        # 26 set 2022 dev sell -0.10 da -0.07
                        
                        
        
            
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
                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.23 - r 10680"
                        action = "sell"
                      
                    
               
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.25 - 0.60 FINTA DI MARADONA - r 10692"
                        action = "sell"
                        
                 
                
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.61 and deviation_sell < 0.79
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-33 and deviation_sell 0.61 - 0.79 DRIBBLING DI RONALDO - r 10704"
                        action = "sell"
                    
                    
                    
               
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 0.80 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell 0.80 - 1.20 DOPPIO PASSO ALLA RONALDO - r 10716"
                        action = "sell"
                  
                
                
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell > 1.21 (che sarebbe come IL DRIBBLING ALLA RONALDO !) - r 10728"
                        action = "sell"
                        
                        
                    
                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 < and incrocio 3-28 - r 10741"
                        action = "sell"
                        
                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                   
                
                
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 - r 10755"
                        action = "sell"
                        
                        
                        
               
                    # ---------------------------------------------------------------------------------------------------------------------- crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - r 10769"
                        action = "sell"
                        
                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - r 10782"
                        action = "sell"
                   
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                        and deviation_sell > 0.60
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - r 10794"
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
                        sell = "SELL 2 (3-5 min) con ma50 > and incrocio 3-39 and deviation_sell < -0.25 - r 10812"
                        action = "sell"
                        
                 
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                    ):  
                        sell = "SELL 2 (3-5 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 10823"
                        action = "sell"
                        
                        
                        
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.57 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 > and incrocio 3-15 and deviation_sell 0.57 - 1.20 - r 10835"
                        action = "sell"
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - r 10847"
                        action = "sell"
                        
                    
                    
                    
                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 < and incrocio 3-28 - r 10862"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        # deviation_sell_ma78 = ma3_last / ma78_last
                        
                        
                        
                  
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.28
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.28 - r 10877"
                        action = "sell"
                        
                        # 0.28 da 0.23
                        
                        
                        

                    # ---------------------------------------------------------------------------------------------------------------------- guadagno con crollo
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - riga 10892"
                        action = "sell"
                        
                   
                
                
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 10904"
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
                        sell = "SELL 2 (5-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - r 10924"
                        action = "sell"
                    
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.25
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - r 10936"
                        action = "sell"
                        
                        
                        
                   
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 10949"
                        action = "sell"
                        
                        
                        
                   
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma15_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 >  3 < 15 and deviation_sell 0.57 - 0.90 - DRIBBLING ALLA RONALDO - r 10962"
                        action = "sell"
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - r 10975"
                        action = "sell"
                        
                        
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - r 10987"
                        action = "sell"
                        
                        
                        
                        
                    ###########################################################################     trend in ribasso and ma200_last < ma300_last
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma300_last
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.31
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 < AND 200<300 and incrocio 3-28 and deviation_sell < -0.31 - r 11002"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        
                        
                  
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma300_last
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 < AND 200<300 and incrocio 3-100 (cuscino di sant' antonio) - r 11017"
                        action = "sell"
                        
                 
                
                
                    ###########################################################################     trend in ribasso MA ma200_last > ma300_last
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma300_last
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.35
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 < MA 200>300 and incrocio 3-28 and deviation_sell < -0.35 - r 11032"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                  
                
                
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma300_last
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.40
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (5-12 min) con ma50 < MA 200>300 and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.40 - r 11047"
                        action = "sell"
                        
                        
                        
                   
                    # ------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 guadagno con crollo (5-12 min) con ma50 < and incrocio 3-23 - r 11061"
                        action = "sell"
                        
                        

                    # ------------------------------------------------------------------------------------------------------------ PARACADUTE crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.48
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.48 - r 11074"
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
                        sell = "SELL 2 (12-21 min) con ma50 > and incrocio 3-69 and deviation sell -0.34 e vaffanculo ! - r 11097"
                        action = "sell"
                        
                        # and deviation_ma39 < -0.29 vendeva troppo presto
                        # ATTENZIONE "and (ma3_prev > ma39_prev and ma3_last < ma39_last)" con ma39 NON HA INCROCIATO
                        
                        
                        
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma100_prev and ma3_last < ma100_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.36 - r 11112"
                        action = "sell"
                        
                  
                
                
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and 5<25 and deviation_sell 0.25-0.56 - MARADONA - r 11125"
                        action = "sell"
                        
                       
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma25_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and 3<25 and deviation_sell 0.57-0.90 - DOPPIO PASSO ALLA RONALDO fino a +0.50 - r 11138"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma100_last > ma300_last
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and incrocio 3-15 and deviation_sell 0.91 - 1.20 CON 100 > 300 RIALZO - r 11156 A"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma100_last < ma300_last
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and incrocio 3-20 and deviation_sell 0.91 - 1.20 CON 100 < 300 CROLLO - r 11171 B"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                        
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 > and incrocio 3-13 and deviation_sell > 1.21 - r 11190"
                        action = "sell"
                        
                        

                    ##########################################################################################
                    # NON TOCCARE ! CUSCINO DI SANT' ANTONIO !
                    # L' INCROCIO 5-100 MI SALVA ! MA, attenzione, 5<100 VENDE DURANTE IL RIBASSO !
                    ########################################################################################### con trend discendente
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 > 0.50
                        and deviation_ma39 < -0.199
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 < and deviation_ma39 < -0.195 - r 11206 A"
                        action = "sell"
                        
                        # and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        # ATTENZIONE deviation_sell < -0.25 aveva FATTO -0.61% !
                        # HO NOTATO CHE ANCHE INCROCIO 5-100 SAREBBE ARRIVATO TARDI
                        
                        # > estate se 5 molto sopra 300 ma39 -0.199 da -0.19
                        
                        
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 < 0.50
                        and deviation_ma39 < -0.199
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 < and deviation_ma39 < -0.199 and dev sell -0.30 - r 11206 B"
                        action = "sell"
                        
                        
                        # ATTENZIONE deviation_sell < -0.25 aveva FATTO -0.61% !
                        # HO NOTATO CHE ANCHE INCROCIO 5-100 SAREBBE ARRIVATO TARDI
                        
                        # > estate se 5 vicina 300 ma39 -0.199 da -0.19 e dev sell -0.30
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.45
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - r 11226"
                        action = "sell"
                        
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50< ! 
                        
                        
                       

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.28
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - r 11240"
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
                        sell = "SELL 2 PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 11257"
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
                        sell = "SELL 2 eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 4 - 33 se 18> and deviation_sell > 0.22 - r 11276 a"
                        action = "sell"
                        
                        # 19 giu 2022 4-33 da 4-20
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma18_last < ma18_30_min_ago
                        
                        and (ma4_prev > ma20_prev and ma4_last < ma20_last)
                        and deviation_sell > 0.22
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 4 - 20 se 18< and deviation_sell > 0.22 - r 11290 b"
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
                        sell = "SELL 2 (21-60 min) con ma50 > and deviation_ma39 < -0.255 situazione in miglioramento - r 11318"
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
                        sell = "SELL 2 (21-60 min) con ma50 > and deviation_ma39 < -0.26 and deviation_sell < -0.28 - situazione post crollo - r 11338"
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
                        sell = "SELL 2 (21-60 min) RAFFORZATA con ma50 > and (dev_sell < -0.32 and ma3_last < ma50_last) situazione in miglioramento - r 11365"
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
                        sell = "SELL 2 (21-60 min) con ma50 > and (deviation_sell < -0.28 and ma3_last < ma50_last) situazione post crollo - r 11384"
                        action = "sell"
                        
                        
                        
                        #######################################################################################################################
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (        
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.29
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and deviation_ma39 < -0.29 - TOLLERANTE ! - r 11410"
                        action = "sell"
                        
                  
                
                    
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.33
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and (deviation_sell < -0.33 and ma3_last < ma50_last) TOLLERANTE ! - r 11423"
                        action = "sell"
                        
                        # 21 giu 2022 dev sell 0.31 da 0.29
                        # 13 set 2022 dev sell 0.33 da 0.31
                        
                        
                    ##############################################################################################################################
                        
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.29
                        and ma300_last > ma300_120_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.29 - r 11440"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.26
                        and ma300_last < ma300_120_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.26 - r 11452"
                        action = "sell"
                  
                        # deviation_sell = ma3_last/last_trade_price
                        # IMPORTANTE !   
                        # vai compaaaaaaaaaa
                        # poco guadagno ma piu' alta
                        # molto guadagno ma piu' bassa
                        
                        
                        
                        
                        
                        
                        
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 > 0.40
                        and ma5_last < ma69_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and 5 < 69 and deviation_sell 0.25 - 0.56 MARADONA e' piu' stanco e paziente - r 11477 A"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # 5-69 da 5-39 dopo dolomiti
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 < 0.40
                        and deviation_ma5_sotto_ma300 > -0.40
                        and ma5_last < ma39_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and 5 < 39 and deviation_sell 0.25 - 0.56 MARADONA e' piu' stanco e paziente - r 11477 B"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # 5-69 da 5-39 dopo dolomiti
                        # 29 set 5-39 fascia mediana 5-300
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 < -0.40
                        and ma5_last < ma78_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and 5 < 78 and deviation_sell 0.25 - 0.56 MARADONA e' piu' stanco e paziente - r 11477 C"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # > estate 5-78 da 5-48 
                        
                        
                        
                        
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
                        sell = "SELL 2 (21-60 min) con ma50 > AND 200>120 min and 5<69 (fidati!) and deviation_sell 0.57 - 0.90 ELASTICO ALLA RONALDO - r 11499"
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
                        sell = "SELL 2 (21-60 min) con ma50 > AND 200>120min and 100> and 3<48 and deviation_sell 0.57 - 0.90 ELASTICO ALLA RONALDO - r 11518 a"
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
                        sell = "SELL 2 (21-60 min) con ma50 > AND 200>120min and 100< and 3<25 and deviation_sell 0.57 - 0.90 ELASTICO ALLA RONALDO - r 11538 b"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    
                    ##############################################################################################################
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma42_prev and ma3_last < ma42_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                   
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and incrocio 3-42 and deviation_sell 0.91 - 1.20 - r 11555"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # 17 set 3-42 da 3-18
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma30_prev and ma5_last < ma30_last)
                        and deviation_sell > 1.21 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and incrocio 5-30 (!) SI PROPRIO COSI' ! 3-30 ! and deviation_sell 1.21 - 2.70 - r 11568"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 > and incrocio 3-20 and deviation_sell > 2.71 - r 11579"
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
                        sell = "SELL 2 (21-60 min) con ma50 < and deviation_ma39 < -0.30 AND 78>200 - r 11599 A"
                        action = "sell"    
                        
                        
                    elif (        
                        ma50_last < ma50_2_min_ago
                        and ma300_last > ma300_120_min_ago
                        
                        and ma78_last < ma200_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.295
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 < and deviation_ma39 < -0.295 AND 78<200 - r 11613 B"
                        action = "sell"
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    # ecco inequivocabilmente il crollo !
                    
                    elif (        
                        ma50_last < ma50_2_min_ago
                        and ma300_last < ma300_120_min_ago
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.31
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 < and deviation_ma39 < -0.31 - r 11633"
                        action = "sell"
                        
                        # durante il crollo non devi pensare ai centesimi !
                        
                  
                    
                    
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.318
                        and ma200_last < ma200_60_min_ago
                        and ma50_last > ma100_last
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 < and deviation_sell < -0.318 - r 11650"
                        action = "sell"
                        
                        # 26 set -0.318 da -0.32
                        
                    
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.348
                        and ma200_last < ma200_60_min_ago
                        and ma50_last < ma100_last
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 < and deviation_sell < -0.348 - r 11663"
                        action = "sell"
                        
                        # 2 GIUGNO a 0.335 da 0.32
                        # 0.345 da 0.335 dopo le dolomiti
                        # 24 set 2022 -0.348 da -0.345
                    
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_60_min_ago
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.37
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - r 11681"
                        action = "sell"
                        
                        
                   
                    
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_60_min_ago
                        and ma100_last > ma100_60_min_ago
                        
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.31
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50< 200< e 100> and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO con dev_sell < -0.31 - r 11699"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_60_min_ago
                        and ma100_last < ma100_60_min_ago
                        
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.29
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50< 200< e 100< and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO con dev_sell < -0.29 - r 11714"
                        action = "sell"
                        
                        
                        
                        
                        
                        
                      
                    
                    ############################################################################################################## con > PERDITA TOLLERATA !
                    
                    # ATTENZIONE ! AUMENTA LA PERDITA TOLLERATA  ! PERCHE' ma200 sale e perche' ma200 > ma300
                    
                    
                    # divido in 2 parti la correzione del maestro !
                    
                    elif (
                        
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.37
                        and ma200_last > ma200_60_min_ago
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                    
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 < and deviation_ma39 < -0.37 con > PERDITA TOLLERATA ! - r 11741"
                        action = "sell"
                        
                        # > estate -0.37 da -0.29
                        
                        
                        
                        
                    elif (  
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.36
                        and ma300_last > ma300_301_min_ago
                        and ma200_last > ma200_60_min_ago
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                     
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 < and deviation_sell < -0.36 con > PERDITA TOLLERATA ! - r 11755 A"
                        action = "sell"
                        
                        # 28 set se 300 > 300 301 min ago allora dev sell a -0.36 da -0.35
                        
                        
                    elif (  
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.35
                        and ma300_last < ma300_301_min_ago
                        and ma200_last > ma200_60_min_ago
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                     
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 < and deviation_sell < -0.35 con > PERDITA TOLLERATA ! - r 11755 B"
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
                        sell = "SELL 2 (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.40 con > PERDITA TOLLERATA ! - r 11770"
                        action = "sell"
                        
                        
                        
                    elif (
                        deviation_trend_ma200 > -0.10
                        and deviation_ma5_sotto_ma300 > 0.59
                        
                        and ma200_last > ma200_60_min_ago
                        and ma200_last > ma300_last
                        and ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO con > PERDITA TOLLERATA ! - r 11785a"
                        action = "sell"
                        
                        # viva sant' antonio !
                        # NON INCROCERANNO MAI DURANTE IL CROLLO !
                        # non toccare ! INCROCIO 3-100 CUSCINO DI SANT' ANTONIO !
                        
                        
                        
                        
                        
                    elif (
                        deviation_trend_ma200 > -0.10
                        and deviation_ma5_sotto_ma300 < 0.59
                        
                        and ma200_last > ma200_60_min_ago
                        and ma200_last > ma300_last
                        and ma50_last < ma50_2_min_ago
                        and (ma8_prev > ma130_prev and ma8_last < ma130_last)
                        and deviation_sell < -0.38
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) con ma50 < and INCROCIO 8-130 (no 3<100) CUSCINO DI SANT' ANTONIO con > PERDITA TOLLERATA ! - r 11785b"
                        action = "sell"
                        
                        # viva sant' antonio !
                        # NON INCROCERANNO MAI DURANTE IL CROLLO !
                        # non toccare ! INCROCIO 3-100 CUSCINO DI SANT' ANTONIO !
                        # tornando dalle dolomiti se 5 e' vicina a 300 sant' antonio e' piu' delicato ( e' un movimento laterale )
                        # > estate -0.38 da 0.30
                
                
                    # -------------------------------------------------------------------------------------- guadagno durante il crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 (21-60 min) eventuale guadagno durante il crollo (21-60 min) con ma50 < incrocio 3-28 and dev_sell > 0.23 - r 11803"
                        action = "sell"
                        
                        # 14 set 3-28 da 3-18
                        
                
                
                
                
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
                        sell = "SELL 2 da 60 a 90 min con ma50 > and deviation_ma39 < -0.18 SE 100 MOLTO ALTA RISPETTO ALLA 300 OK COSI' - r 11828 a1"
                        action = "sell"
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma39_last
                        and deviation_ma100_sopra_ma300 > 0.70
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 > and 3 < 39 SE 100 MOLTO ALTA RISPETTO ALLA 300 OK COSI' - r 11828 a2"
                        action = "sell"
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and deviation_ma39 < -0.18
                        and deviation_ma100_sopra_ma300 < 0.70
                        and deviation_sell < -0.10
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 > and deviation_ma39 < -0.18 SE 100 VICINA ALLA 300 C'E' DEV SELL < -0.10  - r 11839 b"
                        action = "sell"
                        
                        
                        
                        
                        
               
                    elif (      
                        ma50_last > ma50_2_min_ago
                        and deviation_sell < -0.18
                        and ma3_last < ma50_last
                        and ma2_last < ma2_2_min_ago 
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 > and (deviation_sell < -0.18 and ma3_last < ma50_last)  - r 11853"
                        action = "sell"
                        
                        
                    
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and deviation_ma39 < -0.22
                        and ma2_last < ma2_2_min_ago
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 > and deviation_ma39 <-0.22 - r 11864"
                        action = "sell"
                        
                        
                  
                    elif (      
                        ma50_last > ma50_2_min_ago
                        and deviation_sell < -0.21
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 > and (deviation_sell < -0.21 and ma3_last < ma50_last)  - r 11876"
                        action = "sell"
                        
                       
                    
                    
                        ##################################################################################################################### 
                     
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma78_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50 > and 5-78 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 11892"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # 21 lug 2022 5-69 da 5-50 dopo le dolomiti
                        
                        # > estate 5-78 da 5-69
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma4_prev > ma25_prev and ma4_last < ma25_last)
                        and deviation_sell > 0.57 and deviation_sell < 0.80
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con ma50> and incrocio 4-25 and deviation_sell 0.57-0.80 FINTA ALLA RONALDO - r 11906"
                        action = "sell"
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma28_prev and ma5_last < ma28_last)
                        and deviation_sell > 0.81 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 da 60 a 90 min con ma50 > and incrocio 5-28 and deviation_sell 0.81 - 1.49 RABONA ALLA RONALDO - r 11919"
                        action = "sell"

                        # ma ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                        # 5-28 da 3-18 dopo dolomiti
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma34_prev and ma3_last < ma34_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and deviation_ma100_sopra_ma200 > 0.45
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 da 60 a 90 min con ma50 > CON 100>200 > 0.45 incrocio 3-34 (!) and dev_sell 1.50 - 2.70 DOPPIO PASSO RONALDO - r 11943"
                        action = "sell"
                        
                        # 6 giu 2022 3-34 da 3-13
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma25_prev and ma5_last < ma25_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and deviation_ma100_sopra_ma200 < 0.45
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 da 60 a 90 min con ma50 > CON 100>200 < 0.45 incrocio 3-16 and dev_sell 1.50 - 2.70 DOPPIO PASSO RONALDO - r 11959"
                        action = "sell"
                        
                        # 6 giu 2022 3-16 da 3-13
                        # 5-25 da 3-16 dopo dolomiti
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 da 60 a 90 min con ma50 > incrocio 3-20 and dev_sell > 2.71 STIAMO TRA GLI ANGELI, compa ! - r 11983"
                        action = "sell"
                        
                        
                    
                    ######################################################################################## trend discendente con PERDITA BASE
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        
                        and deviation_ma39 < -0.17
                        and deviation_sell < -0.10
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min TREND < con PERDITA BASE con ma50 < con deviation_ma39 <-0.17 and dev_sell < -0.10 - r 11999"
                        action = "sell"
                        
                        # and ma3_last < ma39_last
                        # and deviation_sell < 0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare ! POI STIAMO GIA' AL SELL 2 -le ma hanno avuto piu' tempo di salire
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # cuscino dell' angelo custode
                        # > estate dev sell -0.10 da 0.10
                        
                    
                    

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.13
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min TREND < con PERDITA BASE  con ma50 < con incrocio 3-78 and dev_sell < -0.13 - r 12018"
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
                        sell = "SELL 2 da 60 a 90 min TREND < con POCA PERDITA TOLLERATA con ma50 < con deviation_ma39 <-0.17 and dev_sell < -0.20 - r 12037"
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
                        sell = "SELL 2 da 60 a 90 min TREND < con POCA PERDITA TOLLERATA con ma50 < con deviation_ma39 <-0.17 and dev_sell < -0.15 - r 12060"
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
                        sell = "SELL 2 da 60 a 90 min con POCA PERDITA TOLLERATA con ma50 < con incrocio 3-78 and deviation_sell < -0.14 - r 12087"
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
                        sell = "SELL 2 da 60 a 90 min con MOLTA PERDITA TOLLERATA con ma50 < con 3 < 59 con 100 sopra 300 < 0.50 - r 12105 a"
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
                        sell = "SELL 2 da 60 a 90 min con MOLTA PERDITA TOLLERATA con ma50 < con 3 < 59 con 100 sopra 300 < 0.50 - r 12123 b"
                        action = "sell"
                        
                        # questa anticipa di una ndecchia la prossima
                        
                        
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.29
                        
                        and deviation_trend_ma200 > -0.12
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con MOLTA PERDITA TOLLERATA con ma50 < con deviation_ma39 < -0.29 - r 12140"
                        action = "sell"
                        
                        # and ma3_last < ma33_last
                        # and deviation_sell < 0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # cuscino dell' angelo custode
                        
                        # > vacanza -0.29 da -0.19
                        
                        
                        
                    
                    
                    
                    
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.15
                        
                        and deviation_trend_ma200 > -0.12
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min con MOLTA PERDITA TOLLERATA con ma50 < con incrocio 3-78 and deviation_sell < -0.15 - r 12169"
                        action = "sell"
                        
                        
                        
                        
                    # AGGIUNTA TARDIVA MA FORSE NECESSARIA !
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        
                        and ma100_last < ma200_last
                        and ma200_last < ma300_last
                        
                        and ma200_last < ma200_120_min_ago
                        and ma300_last < ma300_120_min_ago
                        
                        and delta_300_100 < delta_300_100_60_min
                   
                        and deviation_sell < -0.12
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min AGGIUNTA TARDIVA MA FORSE NECESSARIA ! delta 300-100 < and deviation_sell < -0.12 - r 12191 a"
                        action = "sell"
                        
                        
                        
                    # AGGIUNTA TARDIVA MA FORSE NECESSARIA !
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        
                        and ma100_last < ma200_last
                        and ma200_last < ma300_last
                        
                        and ma200_last < ma200_120_min_ago
                        and ma300_last < ma300_120_min_ago
                        
                        and delta_300_100 > delta_300_100_60_min
                   
                        and deviation_sell < -0.10
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 da 60 a 90 min AGGIUNTA TARDIVA MA FORSE NECESSARIA ! delta 300-100 > and deviation_sell < -0.10 - r 12212 b"
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
                        sell = "SELL 2 90-110 min con ma50 > and deviation_ma39 <-0.22 (no ma3<ma39) - r 12237"
                        action = "sell"
                        
                   
                
                    elif (      
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.21 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 2 90-110 min con ma50 > and (deviation_sell < 0.21 and ma3_last < ma50_last) - r 12249"
                        action = "sell"
                        
                        
                        
                        
                    elif (  
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.23
                        and ma200_last < ma200_60_min_ago
                    ):    
                        sell = "SELL 2 90-110 min con ma50 > and deviation_ma39 < -0.23 - r 12261"
                        action = "sell"
                        
                        
                        
                   
                    elif (      
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.22 
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 2 90-110 min con ma50 > and (deviation_sell < -0.22 and ma3_last < ma50_last) - r 12274"
                        action = "sell"
                        
                        
                        
                    #########################################################################################################
                   
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma50_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 90-110 min con ma50 > and 5-50 (!) and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA (non toccare) - r 12289"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                     
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 > 0.40
                        and ma4_last < ma48_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 90-110 min con ma50 > con 4-48 CON 100 sopra 300 > 0.40 and deviation_sell 0.57-0.90 DRIBBLING ALLA RONALDO - r 12303 a"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 < 0.40
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 90-110 min con ma50 > con 4-20 CON 100 sopra 300 > 0.40 and deviation_sell 0.57-0.90 DRIBBLING ALLA RONALDO - r 12315 b"
                        action = "sell"
                        
                        
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 > 0.40
                        and (ma4_prev > ma50_prev and ma4_last < ma50_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 90-110 min con 5-300 > 0.40 e con ma50 > incrocio 4-50 and deviation_sell 0.91 - 1.49 - r 12328 A"
                        action = "sell"

                        # ma 3-48 mi evita la ricompra e la rivendita con perdita !
                        # ma 3-15 vendeva troppo presto. guardando il grafico da piu' lontano.
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 < 0.40
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 90-110 min con 5-300 < 0.40 e con ma50 > incrocio 3-33 and deviation_sell 0.91 - 1.49 - r 12328 B"
                        action = "sell"

                        # ma 3-48 mi evita la ricompra e la rivendita con perdita !
                        # ma 3-15 vendeva troppo presto. guardando il grafico da piu' lontano.
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 90-110 min con ma50 > incrocio 3-18 and deviation_sell 1.50 - 2.70 - r 12343"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 90-110 min con ma50 > incrocio 3-11 (!) and deviation_sell > 2.71 - r 12355"
                        action = "sell"
                        
                        
                        

                    ######################################################################################## con trend discendente
                    
                    
                    elif (  
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.25
                        and deviation_trend_ma100 > 0.10
                    ):
                        sell = "SELL 2 90-110 min con ma50 < MA ma100 > con deviation_ma39 <-0.25 - r 12370"
                        action = "sell"
                        
              
                    
                
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.22
                        and ma3_last < ma39_last
                        and deviation_trend_ma100 > 0.10
                    ):
                        sell = "SELL 2 90-110 min con ma50 < MA ma100 > and (deviation_sell < -0.22 and ma3_last < ma39_last) - r 12383"
                        action = "sell"
                        
                        # 1 ott dev sell -0.22 da -0.20
                  
                
                        
                    elif (  
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.22
                        and deviation_sell < -0.30
                        and deviation_trend_ma100 < 0.10
                    ):
                        sell = "SELL 2 90-110 min con ma50 < MA ma100 < con deviation_ma39 <-0.22 and deviation_sell < -0.30 - r 12395"
                        action = "sell"
                        
                        
                
                 
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.20
                        and ma3_last < ma39_last
                        and deviation_trend_ma100 < 0.10
                    ):
                        sell = "SELL 2 90-110 min con ma50 < MA ma100 < and (deviation_sell < -0.20 and ma3_last < ma39_last) - r 12408"
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
                        sell = "SELL 2 compa 90-110 min  con ma50 < con deviation_ma39 <-0.235 con > PERDITA TOLLERATA - r 12425"
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
                        sell = "SELL 2 compa 90-110 min con ma50 < (deviation_sell < -0.24 and ma3_last < ma39_last) con > PERDITA TOLLERATA - r 12440"
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
                        sell = "SELL 2 dopo 110 min con ma50 > and deviation_ma39 <-0.22 (no ma3<ma39) - r 12462"
                        action = "sell"
                        
                        
                    if (  
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma200_last
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.22
                        and ma200_last > ma200_60_min_ago
                    ):    
                        sell = "SELL 2 dopo 110 min con ma50 > and deviation_ma39 <-0.22 (no ma3<ma39) - r 12473"
                        action = "sell"
                        
                        # POTREBBE ESSERE SITUAZIONE DI CROLLO SOLO CON 39 E SENZA DEVIATION SELL
                        
                        
                        
                   
                
                    elif (      
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.21 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "sessione 2 SELL dopo 110 min con ma50 > and (deviation_sell < 0.21 and ma3_last < ma50_last) - r 12489"
                        action = "sell"
                        
                        
                        
                        
                    elif (  
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.23
                        and ma200_last < ma200_60_min_ago
                    ):    
                        sell = "sessione 2 SELL 2 dopo 110 min con ma50 > and deviation_ma39 < -0.23 - r 12501"
                        action = "sell"
                        
                   
                
                
                    elif (      
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.22 
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "sessione 2 SELL dopo 110 min con ma50 > and (deviation_sell < -0.22 and ma3_last < ma50_last) - r 12514"
                        action = "sell"
                        
                        
                        
                        
                    ################################################################################### fare maradona 1 e maradona 2 se ma2 sta sopra ma100
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma200_last
                        and ma300_last > ma300_180_min_ago
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 dopo 110 min ma300 > 300 180 min ago e con ma50 > and 5-200 (!) and dev_sell 0.25-0.56 - FINTA ALLA MARADONA - r 12530 A"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # 9 GIU 2022 5-59 da 5-50
                        # > estate 5-100 da 5-59
                        # 26 set se 300 > 300 180 min sell con 5-200 (!) da 5-100
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma100_last
                        and ma300_last < ma300_180_min_ago
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 2 dopo 110 min ma300 > 300 180 min ago e con ma50 > and 5-100 (!) and dev_sell 0.25-0.56 - FINTA ALLA MARADONA - r 12530 B"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # 9 GIU 2022 5-59 da 5-50
                        # > estate 5-100 da 5-59
                        
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma78_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 2 > 110 min con ma50 > con 4-78 and deviation_sell 0.57-0.90 DRIBBLING ALLA RONALDO - r 12544"
                        action = "sell"
                        
                        # > estate 4-78 da 4-20
                        
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma4_prev > ma42_prev and ma4_last < ma42_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 dopo 110 min con ma50 > incrocio 4-42 and deviation_sell 0.91 - 1.49 - r 12557"
                        action = "sell"

                        # evitare la ricompra e la rivendita con perdita !
                        # 18 set 4-42 da 3-15
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 dopo 110 min con ma50 > incrocio 3-78 and deviation_sell 1.50 - 2.70 - r 12572"
                        action = "sell"
                        
                        # > estate 3-78 da 3-13
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 2 dopo 110 min con ma50 > incrocio 3-11 (!) and deviation_sell > 2.71 - r 12584"
                        action = "sell"
                        
                        

                    ######################################################################################## con trend discendente
                    
                    
                    elif (  
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.25
                        and deviation_trend_ma100 > 0.10
                    ):
                        sell = "SELL 2 dopo 110 min con ma50 < MA ma100 > con deviation_ma39 <-0.25 - r 12598"
                        action = "sell"
                        
              
                    
                
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.20 
                        and ma3_last < ma39_last
                        and deviation_trend_ma100 > 0.10
                    ):
                        sell = "SELL 2 dopo 110 min con ma50 < MA ma100 > and (deviation_sell < -0.20 and ma3_last < ma39_last) - r 12611"
                        action = "sell"
                        
                  
                        
                    
                    elif (  
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.22
                        and deviation_trend_ma100 < 0.10
                    ):
                        sell = "SELL 2 dopo 110 min con ma50 < MA ma100 < con deviation_ma39 <-0.22 - r 12623"
                        action = "sell"
                        
                        
                
                 
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.18 
                        and ma3_last < ma39_last
                        and deviation_trend_ma100 < 0.10
                    ):
                        sell = "SELL 2 dopo 110 min con ma50 < MA ma100 < and (deviation_sell < -0.18 and ma3_last < ma39_last) - r 12636"
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
                        sell = "SELL 2 compa dopo 110 min con ma50 < con deviation_ma39 <-0.24 con > PERDITA TOLLERATA - r 12653"
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
                        sell = "SELL 2 compa dopo 110 min con ma50 < (deviation_sell < -0.24 and ma3_last < ma39_last) con > PERDITA TOLLERATA - r 12667"
                        action = "sell"
                        
                        
                        
                 
                    # ATTENZIONE : DOPO 110 MIN forse E' NECESSARIA SOLO QUESTA !
                    
                    elif (    
                        ma3_last < ma100_last
                        and deviation_sell < -0.15
                        and ma2_last < ma2_2_min_ago
                    ):
                   
                        sell = "SELL 2 > 110 min forse E' NECESSARA SOLO QUESTA ! - r 12681"
                        action = "sell"
                        
                        # > estate -0.15 da +0.02
                    
                        
                    
                    
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
                        sell = "SELL 3 (0-3 min) con ma50 > and 3<18 and deviation_sell < -0.33 - r 12704"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                     
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma25_prev and ma5_last < ma25_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.60
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 3 (0-3 min) con ma50 > and incrocio 5-25 and deviation_sell 0.25 - 0.60 MARADONA - r 12718"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 0.61 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (0-3 min) con ma50 > and incrocio 3-15 and deviation_sell 0.61 - 0.90 RONALDO - r 12732"
                        action = "sell"
                        
                        
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell 0.91 - 1.20 - r 12745"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 (0-3 min) con ma50 > and incrocio 3-11 and deviation_sell > 1.21 (che sarebbe come IL DRIBBLING ALLA RONALDO !) - r 12758"
                        action = "sell"
                        
                        
                        

                    ###########################################################################     trend in ribasso
                    

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (0-3 min) con ma50 < and incrocio 3-28 - r 12773"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 - r 12787"
                        action = "sell"
                        
                        

                    # ---------------------------------------------------------------------------------------------------------------------- crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - r 12800"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - r 12814"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                        and deviation_sell > 0.60
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - r 12827"
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
                        sell = "SELL 3 (3-5 min) con ma50 > and 3 < 18 and deviation_sell < -0.335 - r 12844"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 12859"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 > and 5<20 (no incrocio 3-9) and deviation_sell 0.57 - 0.90 - DRIBBLING ALLA RONALDO - r 12874"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - r 12888"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - r 12900"
                        action = "sell"
                        
                  
                    ###########################################################################     trend in ribasso
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 < and incrocio 3-28 - r 12913"
                        action = "sell"
                        
                        # deviation_sell_ma78 = ma3_last / ma78_last
                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.23 - r 12927"
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
                        sell = "SELL 3 (3-5 min) con ma50 < and incrocio 3-28 con > PERDITA TOLLERATA - r 12946"
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
                        sell = "SELL 3 (3-5 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.23 con > PERDITA TOLLERATA - r 12964"
                        action = "sell"
                        
                       

                    # -------------------------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 GUADAGNO CON CROLLO (3-5 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - r 12977"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 12989"
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
                        sell = "SELL 3 (5-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - r 13009"
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
                        sell = "SELL 3 (5-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - r 13025"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 13040"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                  
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 >  5<20 and deviation_sell 0.57 - 0.90 - DRIBBLING ALLA RONALDO - r 13055"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma20_prev and ma5_last < ma20_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 > and incrocio 5-20 and deviation_sell 0.91 - 1.20 - r 13070"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - r 13084"
                        action = "sell"
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 < and incrocio 3-28 - r 13097"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last > ma100_60_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.39
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 < and ma100 > 60 min ago and incrocio 3-100 (cuscino di sant' antonio) E dev_sell < -0.39 - r 13112"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.38
                        
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (5-12 min) con ma50 < and ma100 < 60 min ago and incrocio 3-100 (cuscino di sant' antonio) E dev_sell < -0.38  - r 13124"
                        action = "sell"
                        
                        
                        

                    # ------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 guadagno con crollo (5-12 min) con ma50 < and incrocio 3-23 - r 13138"
                        action = "sell"
                        
                        

                    # ------------------------------------------------------------------------------------------------------------ PARACADUTE crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.48
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 PARACADUTE CROLLO (0-3 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.48 - r 13151"
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
                        sell = "SELL 3 (12-21 min) con ma50 > and incrocio 3-72 and deviation sell -0.35 e vaffanculo ! - r 13173"
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
                        sell = "SELL 3 (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.36 - r 13190"
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
                        sell = "SELL 3 (12-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.54 - FINTA ALLA MARADONA - r 13209"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma20_last
                        and deviation_sell > 0.55 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and 5-20 and deviation_sell 0.55-0.90 - DOPPIO PASSO ALLA RONALDO - r 13227"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                    
                    
                    
                    
                    
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and incrocio 3-20 and deviation_sell 0.91 - 1.20 - r 13246"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                       
                    

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and incrocio 3-30 and deviation_sell > 1.21 - r 13260"
                        action = "sell"
                        
                  
                
                    ##########################################################################################
                    
                    # NON TOCCARE ! CUSCINO DI SANT' ANTONIO !
                    # L' INCROCIO 5-100 MI SALVA ! MA 5<100 VENDE DURANTE IL RIBASSO !
                    
                  
                    ##################################################################### con trend discendente
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.165
                        and deviation_sell < -0.33
                        
                        and deviation_ma100_sopra_ma200 < 0.25
                        and deviation_ma100_sopra_ma200 > -0.70
                        
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 < and deviation_ma39 < -0.165 100 spra 200 > -0.70 - r 13282 a"
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
                        sell = "SELL 3 (12-21 min) con ma50 < and deviation_ma39 < -0.165 100 spra 200 < -0.70 crollo ! - r 13304 b"
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
                        sell = "SELL 3 (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - r 13330"
                        action = "sell"
                        
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50< !
                        
                    

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - r 13344"
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
                        sell = "SELL 3 (12-21 min) con ma50 < and deviation_ma39 < -0.185 con > PERDITA TOLLERATA - r 13363"
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
                        sell = "SELL 3 (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.47 con > PERDITA TOLLERATA - r 13385"
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
                        sell = "SELL 3 (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO con > PERDITA TOLLERATA - r 13402"
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
                        sell = "SELL 3 PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 13419"
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
                        sell = "SELL 3 eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3 - 18 and deviation_sell > 0.23 - r 13437"
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
                        sell = "SELL 3 (21-60 min) con ma50 > and deviation_ma25 < -0.27 CON 100-200 > 0.30 - r 13463"
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
                        sell = "SELL 3 (21-60 min) con ma50 > and deviation_ma25 < -0.27 and deviation_sell < -0.30 CON 100-200 < 0.30 - r 13477"
                        action = "sell"
                        
                        # in basso con deviation sell 
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (      
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.25 
                        and ma3_last < ma42_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL (21-60 min) con ma50 > and (deviation_sell < -0.25 and ma3_last < ma42_last) - r 13498"
                        action = "sell"
                        
                        # 16 GIU 2022 3-42 da 3-50
                        
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.31
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and deviation_ma25 < -0.31 - r 13511"
                        action = "sell"
                        
                    
                    
                    
                    elif (      
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.30 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and (deviation_sell < -0.30 and ma3_last < ma50_last) - r 13524"
                        action = "sell"
                        
                        # 13 set dev sell -0.30 da -0.27
                        
                       
                    
                    
                        ##################################################################################################################
                        
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.32
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.32 - r 13539"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # > estate -0.32 da -0.26
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 > 0.70
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and (ma5_prev > ma50_prev and ma5_last < ma50_last)
                        
                        and ma39_last > ma100_last
                        
                        and ma2_last < ma2_2_min_ago
                   
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and 39>100 and incrocio 5-50 and dev_sell 0.25 - 0.56 FINTA MARADONA se 100 molto sopra 300 - r 13556 a"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # 5-50 da 5-39 dopo le dolomiti
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 < 0.70
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        
                        and ma39_last > ma100_last
                        
                        and ma2_last < ma2_2_min_ago
                   
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and 39>100 and incr 5-78 and dev_sell 0.25 - 0.56 FINTA MARADONA se 100 NON molto sopra 300 - r 13556 b"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # > estate 5-78 da 5-33
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and (ma5_prev > ma30_prev and ma5_last < ma30_last)
                        
                        and ma39_last < ma100_last
                        
                        and ma2_last < ma2_2_min_ago
                   
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and 39<100 and incrocio 5-39 and deviation_sell 0.25 - 0.56 FINTA DI MARADONA - r 13573"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma5_last < ma39_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and 5 < 39 and deviation_sell 0.57 - 0.90 ELASTICO ALLA RONALDO - r 13593"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # 31 maggio 2022 5-39 da 5-20
                        
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 3-30 and deviation_sell 0.91 - 1.20 - r 13609"
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
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 3-30 and dev_sell 1.21 -2.70 - ma100 e' ancora sotto ma300 e vende un po' prima - r 13623"
                        action = "sell"
                        
                        # vende un po' prima perche' e' ancora un po' preoccupato perche' ma100 sta sotto ma300
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last > ma300_last
                        and (ma3_prev > ma52_prev and ma3_last < ma52_last)
                        and deviation_sell > 1.21 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 3-52 and dev_sell 1.21 -2.70 - ma100 e' andata sopra ma300 e si distende - r 13636"
                        action = "sell"
                        
                        
                        
                        
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 3-11 and deviation_sell > 2.71 - r 13652"
                        action = "sell"
                    
                    
                   
                    ##################################################################### con trend discendente
                   
                    
                    elif (     
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.23
                        
                        and deviation_ma100_sopra_ma300 > 0.50
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and deviation_ma39 < -0.23 con 50 sopra 300 > 0.50 - r 13667"
                        action = "sell"
                        
                        # attenzione se ma100 sta molto sopra ma 300 basta deviation ma39
                        # ma se trend laterale metto anche una deviation sell ( vedi prossimo elif )
                        
                    
                    
                    
                    elif (     
                        ma50_last < ma50_2_min_ago
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.23
                        
                        and deviation_ma100_sopra_ma300 < 0.50
                        and deviation_sell < -0.28
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and deviation_ma39 < -0.23 and deviation_sell < -0.28 con 50 sopra 300 < 0.50 - r 13685"
                        action = "sell"
                        
                        # attenzione se ma100 sta molto sopra ma 300 basta deviation ma39
                        # ma se trend laterale metto anche una deviation sell
                        # dev sell 0.28 da 0.25 dopo dolomiti
                        
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma78_last > ma100_last
                        
                        and ma300_last > ma300_120_min_ago
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.34
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and ma300> and deviation_sell < -0.34 CON 78>100 - r 13713 A"
                        action = "sell"
                        
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma78_last < ma100_last
                        and ma300_last > ma300_301_min_ago
                        and ma300_last > ma300_120_min_ago
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.345
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and ma300> and deviation_sell < -0.335 CON 78 < 100 - r 13713 B1"
                        action = "sell"
                        
                        # 21 set 2022 dev sell a -0.335 da -0.32
                        # 28 set 2022 dev sell a -0.345 da -0.335
                        
                        
                        
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma78_last < ma100_last
                        and ma300_last < ma300_301_min_ago
                        and ma300_last > ma300_120_min_ago
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.335
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and ma300> and deviation_sell < -0.335 CON 78 < 100 - r 13713 B2"
                        action = "sell"
                        
                        # 21 set 2022 dev sell a -0.335 da -0.32
                        
                        
                        
                    
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma300_last < ma300_120_min_ago
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.28
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and ma300< and deviation_sell < -0.28 - r 13725"
                        action = "sell"
                        
                     
                    

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.37
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - r 13737"
                        action = "sell"
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_ma5_sotto_ma300 > 0.50
                        
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and 5 molto sopra 300 and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - r 13750 a"
                        action = "sell"
                        
                        # viva sant' antonio !
                        # NON INCROCERANNO MAI DURANTE IL CROLLO !
                        # non toccare ! INCROCIO 3-100 CUSCINO DI SANT' ANTONIO !
                        
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_ma5_sotto_ma300 < 0.50
                        and deviation_sell < -0.34
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and 5 vicino 300 and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO -0.34 - r 13750 b"
                        action = "sell"
                        
                        # viva sant' antonio !
                        # NON INCROCERANNO MAI DURANTE IL CROLLO !
                        # non toccare ! INCROCIO 3-100 CUSCINO DI SANT' ANTONIO !
                        # > estate -0.34 da -0.27
                    
                        
                    
                    ####################################################################################################  aumento perdita tollerata se....  
                    
                    # divido il maestro in 2
                    
                    
                    elif (  
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.26
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                       
                    ):
                        sell = "SELL 3 compa (21-60 min) con ma50 < and deviation_ma39 < -0.26 con PERDITA TOLLERATA > - r 13773"
                        action = "sell"
                        
                        
                     
                    
                    elif ( 
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.29
                        and deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                    ):
                        sell = "SELL 3 compa (21-60 min) con ma50 < and deviation_sell < 0.29 con PERDITA TOLLERATA > - r 13786"
                        action = "sell"
                        
                        
                        
                    
                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.39
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.39 con > perdita tollerata - r 13800"
                        action = "sell"
                        
                        
                    
                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - con > perdita tollerata - r 13814"
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
                        sell = "SELL 3 eventuale guadagno durante il crollo (21-60 min) con ma50 < incrocio 3 - 18 and deviation_sell > 0.23 - r 13831"
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
                        sell = "SELL 3 da 60 a 90 min con ma50 > and deviation_ma25 < -0.19 - r 13853"
                        action = "sell"
                        
                
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.20 
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 > and (deviation_sell < -0.19 and ma3_last < ma50_last) - r 13864"
                        action = "sell"
                        
                     
                        
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago
                        and deviation_ma25 < -0.21
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 > and deviation_ma25 < -0.19 - r 13875"
                        action = "sell"
                        
                        
                   
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.20 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 > and (deviation_sell < -0.19 and ma3_last < ma50_last) - r 13887"
                        action = "sell"
                        
                      
                        ############################################################################################################
                       
                     
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma50_prev and ma5_last < ma50_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 (21-60 min) con ma50 > and incrocio 5-50 and deviation_sell 0.25 - 0.56 FINTA DI MARADONA - r 13901"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma78_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 >60 min con ma50> and 4-78 and deviation_sell 0.57-0.90 DRIBBLING ALLA RONALDO - r 13915"
                        action = "sell"
                        
                        # > estate 4-78 da 4-18
                        
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 da 60 a 90 min con ma50 > and incrocio 3-30 and deviation_sell 0.91 - 1.49 - r 13928"
                        action = "sell"

                        # ma ricordati che in diverse occasioni 3-48 mi ha evitato la ricompra e la rivendita conseguente con perdita !
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma300_last
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 da 60 a 90 min con ma50 > incrocio 3-20 and dev_sell 1.50 - 2.70 - ma100 ancora sotto ma300 e vende un po' prima - r 13944"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last > ma300_last
                        and (ma3_prev > ma50_prev and ma3_last < ma50_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 da 60 a 90 min con ma50 > incrocio 3-50 and deviation_sell 1.50 - 2.70 - ma100 sopra ma300 e si distende - r 13956"
                        action = "sell"
                        
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 da 60 a 90 min con ma50 > incrocio 3-11 and deviation_sell > 2.71 - r 13970"
                        action = "sell"
                        
                        
                       
                    ############################################################################# con trend discendente MA 100 sopra di molto da 300
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.16
                        and ma2_last < ma2_2_min_ago
                        
                        and deviation_ma100_sopra_ma300 > 0.69
                       
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 < con deviation_ma39 <-0.16 TREND CRESCITA (100 sopra 300 > 0.69) - r 13986"
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
                        sell = "SELL 3 da 60 a 90 min con ma50 < CUSCINO SANT' ANTONIO (5-100) MA SOLO con TREND CRESCITA (100 sopra 300 > 0.69) - r 14006"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.17
                        and ma2_last < ma2_2_min_ago
                        
                        and deviation_ma100_sopra_ma300 < 0.69
                        and deviation_sell < -0.16
                       
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 < con deviation_ma39 <-0.17 and deviation_sell < 0.10 TREND LATERALE (100>300 MA <0.69) - r 14021"
                        action = "sell"
                        
                        # 27 giu 2022 deviation_sell < -0.16 da 0.15
                        
                        
                        
                        
                    ###########################################################################################################

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.18
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < -0.18 - r 14037"
                        action = "sell"
                        
                        # > estate -0.18 da -0.10 - una cosa curiosa : ha venduto mentre risaliva
                        
                        
                     
                    # maggiore perdita tollerata
                    
                    elif (
                        deviation_trend_ma200 > -0.10
                        and ma200_last > ma300_last
                        and ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.20
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 < con deviation_ma39 <-0.20 and deviation_sell < 0.10 con > perdita tollerata - r 14052"
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
                        and deviation_sell < -0.10
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < -0.10 con > perdita tollerata - r 14072"
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
                        sell = "SELL 3 dopo 90 min con ma50> and deviation_ma25 <-0.18 (no ma3<ma39) - r 14093"
                        action = "sell"
                    
                    
                    
                    
                    elif (     
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.20 
                        and ma3_last < ma50_last
                    ):
                        sell = "SELL 3 dopo 90 min con ma50> and (deviation_sell < 0.10 and ma3_last < ma50_last)- r 14105"
                        action = "sell"
                        
                    
                    
                        
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.23
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 dopo 90 min con ma50> and deviation_ma25 < -0.23 - r 14117"
                        action = "sell"
                        
                
                    
                    
                    elif (     
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.23 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 3 dopo 90 min con ma50> and (deviation_sell < -0.23 and ma3_last < ma50_last) - r 14130"
                        action = "sell"
                        
                       
                        
                        
                        
                    ############################################################################################################################### 
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma78_last
                        and deviation_sell > 0.29 and deviation_sell < 0.59
                        and ma2_last < ma2_2_min_ago
                        and deviation_ma100_sopra_ma200 > 0.20
                       
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and 5-78 and deviation_sell 0.29 - 0.59 - FINTA ALLA MARADONA se sale tanto - r 14147"
                        action = "sell"
                        
                        # > estate 5-78 da 5-39
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma150_last
                        and deviation_sell > 0.25 and deviation_sell < 0.59
                        and ma2_last < ma2_2_min_ago
                        and deviation_ma100_sopra_ma200 < 0.20
                       
                    ):
                        sell = "SELL 3 (12-21 min) con ma50 > and 5-150 (!) and deviation_sell 0.25 - 0.59 - FINTA ALLA MARADONA se sale poco - r 14159"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # al SELL 3 maradona e' ancora piu' stanco di quello che pensavo !
                        
                        
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma78_last
                        and deviation_sell > 0.60 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3 >90 min con ma50 > con 4<78 and deviation_sell 0.60 - 0.90 DRIBBLING ALLA RONALDO - r 14181"
                        action = "sell"
                        
                        # 6 giu 2022 4-30 da 4-25
                        # > estate 4-78 da 4-30
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 dopo 90 min con ma50 > incrocio 3-30 (!) and deviation_sell 0.91 - 1.49 - r 14195"
                        action = "sell"

                        # ma 3-48 mi evita la ricompra e la rivendita con perdita !
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 dopo 90 min con ma50 > incrocio 3-78 (!) and deviation_sell 1.50 - 2.70 - r 14210"
                        action = "sell"
                        
                        # > estate 3-78 da 3-30
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 > 0.30
                        and (ma3_prev > ma42_prev and ma3_last < ma42_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 dopo 90 min con ma50 > incrocio 3-42 and deviation_sell > 2.71 con 5-300 > 0.30 - r 14223 A"
                        action = "sell"
                        
                        # 18 set 2022 3-42 da 3-11
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 < 0.30
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 3 dopo 90 min con ma50 > incrocio 3-18 and deviation_sell > 2.71 SE 5-300 < 0.30 - r 14223 B"
                        action = "sell"
                        
                        # 18 set 2022 3-18 da 3-11
                        
                 
                
                
                    ######################################################################################## con trend discendente
                    
                    
                    elif (      
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma300_last
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.20
                       
                    ):
                        sell = "SELL 3 dopo 90 min con ma50 < con deviation_ma39 < -0.20 - r 14239"
                        action = "sell"
                        
                        
                    elif (      
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma300_last
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.16
                       
                    ):
                        sell = "SELL 3 dopo 90 min con ma50 < con deviation_ma39 < -0.16 - r 14250"
                        action = "sell"
                        
                     
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 > 0.40
                        and deviation_ma100_sopra_ma300 > 0.20
                        and ma2_last < ma2_2_min_ago 
                         
                        and ma3_last < ma78_last
                    ):
                        sell = "SELL 3 dopo 90 min CON 5-300 > 0.40 E con ma50< MA ma100 > ma300 and 5-86 - r 14270 A"
                        action = "sell"
                        
                        # se sta in alto NO DEVIATION SELL - la 100 se ne sta andando in alto.
                        # > estate 3-78 da 3-39
                        # 13 set 5-86 da 3-78
                        
                        
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 < 0.40
                        and deviation_ma100_sopra_ma300 > 0.20
                        and ma2_last < ma2_2_min_ago 
                         
                        and ma5_last < ma86_last
                    ):
                        sell = "SELL 3 dopo 90 min CON 5-300 > 0.40 E con ma50< MA ma100 > ma300 and 5-86 - r 14270 B"
                        action = "sell"
                        
                        # se sta in alto NO DEVIATION SELL - la 100 se ne sta andando in alto.
                        # > estate 3-78 da 3-39
                        # 13 set 5-86 da 3-78
                        
                    
                    
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 < 0.20
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.15 
                        and ma3_last < ma39_last
                    ):
                        sell = "SELL 3 dopo 90 min con ma50 < and ma100 NON DISTANTE dalla ma300 and (dev_sell < -0.15 and ma3_last < ma39_last) - r 14283"
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
                        sell = "SELL 4-5-x (0-3 min) con ma50 > and 3<18 and deviation_sell < -0.33 - r 14311"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma25_prev and ma5_last < ma25_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 4-5-x SELL (0-3 min) con ma50 > and incrocio 5-25 and deviation_sell 0.25 - 0.56 MARADONA - r 14326"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma4_prev > ma20_prev and ma4_last < ma20_last)
                        and deviation_sell > 0.57 and deviation_sell < 0.79
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (0-3 min) con ma50 > and incrocio 4-20 and deviation_sell 0.57 - 0.79 RONALDO - r 14340"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 0.80 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x (0-3 min) con ma50 > and incrocio 3-13 and deviation_sell 0.80 - 1.20 - r 14352"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma11_prev and ma3_last < ma11_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x (0-3 min) con ma50 > and incrocio 3-11 and dev_sell > 1.21 (che sarebbe come IL DRIBBLING ALLA RONALDO !) - r 14365"
                        action = "sell"
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (0-3 min) con ma50 < and incrocio 3-28 - r 14378"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (0-3 min) con ma50 < and incrocio 3-33 and deviation_sell -0.23 - r 14391"
                        action = "sell"
                        
                        

                    # ---------------------------------------------------------------------------------------------------------------------- crollo

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma16_prev and ma3_last < ma16_last)
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x CROLLO (0-3 min) con ma50 < and incrocio 3-16 and deviation_sell < -0.50 - r 14404"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x CROLLO (0-3 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - r 14418"
                        action = "sell"
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma8_prev and ma3_last < ma8_last)
                        and deviation_sell > 0.60
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x CROLLO (0-3 min) con ma50 < and incrocio 3-8 and deviation_sell > 0.60 - r 14431"
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
                        sell = "SELL 4-5-x (3-7 min) con ma50 >  and 39 > 200 and 3 < 16 and deviation_sell < -0.38 - r 14452"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma3_last < ma16_last
                        
                        and ma39_last < ma200_last
                        
                        and deviation_sell < -0.32
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 4-5-x (3-7 min) con ma50 > and 39 < 200 and 3 < 16 and deviation_sell < -0.32 - r 14470"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (3-7 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 14491"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 4-5-x (3-7 min) con ma50 > and 4<20 and deviation_sell 0.57 - 0.90 - DRIBBLING ALLA RONALDO - r 14506"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma20_prev and ma3_last < ma20_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.40
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (3-7 min) con ma50 > and incrocio 3-20 and deviation_sell 0.91 - 1.40 - r 14520"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma15_prev and ma3_last < ma15_last)
                        and deviation_sell > 1.41
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (3-7 min) con ma50 > and incrocio 3-15 and deviation_sell > 1.41 - r 14531"
                        action = "sell"
                        
                        
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 4-5-x (3-7 min) con ma50 < and incrocio 3-28 - r 14547"
                        action = "sell"
                        
                        # deviation_sell_ma78 = ma3_last / ma78_last
                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma33_prev and ma3_last < ma33_last)
                        and deviation_sell < -0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (3-7 min) con ma50 < and incrocio 3-33 and deviation_sell < -0.23 - r 14562"
                        action = "sell"
                        
                        

                    # --------------------------------------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x GUADAGNO CON CROLLO (3-7 min) con ma50 < and incrocio 3-23 and deviation_sell > 0.23 - r 14575"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x PARACADUTE CROLLO (3-7 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 14586"
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
                        sell = "SELL 4-5-x (7-12 min) con ma50 > and incrocio 3-78 and deviation_sell < -0.41 - r 14607"
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
                        sell = "SELL 4-5-x (7-12 min) con ma50 > and incrocio 5-100 (cuscino di sant' antonio) and deviation_sell < -0.25 - r 14624"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (7-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 14638"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                  
                    ):
                        sell = "SELL 4-5-x (7-12 min) con ma50 > and 4-20 and deviation_sell 0.57 - 0.90 - DRIBBLING ALLA RONALDO - r 14653"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.20
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 4-5-x (7-12 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - r 14668"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (7-12 min) con ma50 > and incrocio 3-25 and deviation_sell > 1.21 - r 14682"
                        action = "sell"
                        
                        

                    ###########################################################################     trend in ribasso

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma28_prev and ma3_last < ma28_last)
                        and deviation_sell < -0.30
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (7-12 min) con ma50 < and incrocio 3-28 - r 14695"
                        action = "sell"

                        # incrocio 3 -28 e' fondamentale per evitare punto rosso sovrapposto al punto verde !
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma78_prev and ma5_last < ma78_last)
                        and deviation_sell < -0.36
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (7-12 min) con ma50 < and incrocio 3-100 (cuscino di sant' antonio) - r 14708"
                        action = "sell"
                        
                        

                    # ------------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma23_prev and ma3_last < ma23_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x guadagno con crollo (7-12 min) con ma50 < and incrocio 3-23 - r 14721"
                        action = "sell"
                        
                        

                    # --------------------------------------------------------------------------------------------------- PARACADUTE crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma3_last < ma16_last
                        and deviation_sell < -0.50
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x PARACADUTE CROLLO (7-12 min) con ma50 < and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 14734"
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
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and incrocio 3-72 and deviation sell -0.65 e vaffanculo ! - r 14757"
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
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and incrocio 3-100 cuscino di sant' antonio and deviation_sell < 0.36 - r 14774"
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
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and 5-25 and dev_sell 0.25-0.56 - FINTA ALLA MARADONA sopra rialzo rialzo - GIORNO - r 14805"
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
                        sell = "SELL 4-5-x (12-21 min) con ma50>and 3-50 and dev_sell 0.25-0.56 - SOPRA RIBASSO RIALZO - CREPUSCOLO - FINTA MARADONA - r 14830"
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
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and 4-20 e dev_sell 0.57 - 0.90 - SORGERE DRIBBLING ALLA RONALDO - GIORNO - r 14863"
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
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and 3-50 and dev_sell 0.57 - 0.90 - DRIBBLING RONALDO sopra ribasso rialzo -CREPUSCOLO - r 14888"
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
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and incrocio 3-25 and deviation_sell 0.91 - 1.20 - r 14909"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        

                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 1.21
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and incrocio 3-30 and deviation_sell > 1.21 - r 14923"
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
                        sell = "SELL 4-5-x (12-21 min) con ma50 < and deviation_ma39 < -0.17 - r 14943"
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
                        sell = "SELL 4-5-x (12-21 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.45 - r 14963"
                        action = "sell"
                        
                        # ALLORA METTO incrocio 3-78 e deviation < 0.10 e vaffanculo ! ma solo se ma50< !
                        
                        
                        

                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                     
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 < and CUSCINO DI SANT' ANTONIO - r 14978"
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
                        sell = "SELL 4-5-x PARACADUTE CROLLO (12-21min) con ma50< and ma3<ma16 (no incrocio) and deviation_sell < -0.50 - r 14995"
                        action = "sell"

                        # AGGIUNTA PER SICUREZZA SE CONTINUA A PRECIPITARE
                        
                        
                        
                  
                    # ----------------------------------------------------------------------------- guadagno con crollo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and (ma3_prev > ma18_prev and ma3_last < ma18_last)
                        and deviation_sell > 0.23
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x eventuale guadagno con crollo (12-21 min) con ma50 < and incrocio 3 - 18 and deviation_sell > 0.23 - r 15011"
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
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and deviation_ma25 < -0.29 - r 15034"
                        action = "sell"
                        
                     
                    
                    elif ( 
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.24 
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and (deviation_sell < -0.24 and ma3_last < ma50_last) - r 15046"
                        action = "sell"
                        
                     
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.30
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and deviation_ma25 < -0.30 - r 15058"
                        action = "sell"
                        
                       
                    
                    
                    elif (        
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.26 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and (deviation_sell < -0.26 and ma3_last < ma50_last) - r 15071"
                        action = "sell"
                        
                      
                        #############################################################################################################
                    

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.26
                        and ma2_last < ma2_2_min_ago
                  
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and incrocio 5-100 cuscino di sant' antonio (no 5<100) and deviation_sell < -0.26 - r 15085"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    #######################################################
                    
                    
                    # FINTA DI MARADONA
                    
                    ###################################################### and rapporto_delta_1_delta_2 > 1 AND 100> SORGERE
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                        
                        
                        and delta_1 < delta_2
                        and ma100_last > ma100_60_min_ago
                        and ma300_last > ma300_120_min_ago
                        
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                   
                    ):
                        sell = "SELL 4-5-x (21-60 min) 300 > 120 min ago e con ma50 > and incr 5-100 and dev_sell 0.25 - 0.56 - GIORNO - FINTA MARADONA - r 15110 A"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # 22 set se 300 > 120 min ago 5-100 !
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        
                        
                        and delta_1 < delta_2
                        and ma100_last > ma100_60_min_ago
                        and ma300_last < ma300_120_min_ago
                        
                        and (ma5_prev > ma33_prev and ma5_last < ma33_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                   
                    ):
                        sell = "SELL 4-5-x (21-60 min) 300 < 120 min ago e con ma50 > and incr 5-33 and dev_sell 0.25 - 0.56 - GIORNO - FINTA MARADONA - r 15110 B"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                        
                    ##################################################################### and rapporto_delta_1_delta_2 < 1 tramonto
                    
                    
                    elif (
                        ma50_last >= ma50_2_min_ago
                   
                        and delta_1 > delta_2
                        and ma100_last > ma100_60_min_ago
                        and ma300_last > ma300_120_min_ago
                        
                        and deviation_ma100_sopra_ma200 > -0.10
                        and (ma4_prev > ma100_prev and ma4_last < ma100_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                   
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50> and incrocio 4-100 and dev_sell 0.25-0.56 FINTA MARADONA -CREPUSCOLO - r 15132 A"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # 100 deve stare sopra 200 per non vendere con ma50 durante il crollo.
                        # # 22 set se 300 > 120 min ago 5-100 !
                        
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                   
                        and delta_1 > delta_2
                        and ma100_last > ma100_60_min_ago
                        and ma300_last < ma300_120_min_ago
                        
                        and deviation_ma100_sopra_ma200 > -0.10
                        and (ma4_prev > ma50_prev and ma4_last < ma50_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                   
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50> and incrocio 4-50 and dev_sell 0.25-0.56 FINTA MARADONA -CREPUSCOLO - r 15132 B"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # 100 deve stare sopra 200 per non vendere con ma50 durante il crollo.
                        # # 22 set se 300 > 120 min ago 4-50 !
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    # tra MARADONA e RONALDO ho messo POCHI MALEDETTI E SUBITO se alla fine del trend da' una botta rialzista
                    
                    elif (
                        ma3_last < ma28_last
                        and ma200_last > ma200_60_min_ago
                        and deviation_sell > 0.78
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 3-4-x (21-60 min) SOLO QUI tra MARADONA e RONALDO ho messo P-M-S 18 SE DA! UNA BOTTA RIALZISTA  (solo quando ma200 >) - r 15157"
                        action = "sell"
                        
                        # 3-18 da 3-13 dopo dolomiti
                        # > estate 3-28 da 3-18
                        
                        
                        
                    
                    
                    
                    
                    
                    
                    # FINTA ALLA RONALDO
                    
                    
                    ######################################################################## and rapporto_delta_1_delta_2 > 1 AND 100> SORGERE
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        
                        
                        and delta_1 < delta_2
                        and ma100_last > ma100_60_min_ago
                        
                        and ma3_last < ma39_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                      
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and 3-39 (no incrocio 3-15) and deviation_sell 0.57 - 0.90 FINTA RONALDO - GIORNO - r 15185"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # > estate 3-39 da 3-28
                        
                        
                        
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
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and 3-50 (no incrocio 3-15) e dev_sell 0.57-0.90 FINTA ALLA RONALDO - CREPUSCOLO - r 15208"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        # 100 dee stare sopra 200 per non vendere con ma50 durante il crollo o un grande ribasso
                        
                        
                        
                        ###################################################################################################
                        
                        
                        
                        
                        
                        
                        
                        
                        
                      
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 > 1.20
                        and ma5_last < ma100_last
                        and deviation_sell > 0.91 and deviation_sell < 1.40
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (21-60 min) con 5-300 > 1.20 E con ma50 > and 5-100 and deviation_sell 0.91 - 1.40 - r 15236 A"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 < 1.20
                        and deviation_ma5_sotto_ma300 > 0.40
                        and ma5_last < ma78_last
                        and deviation_sell > 0.91 and deviation_sell < 1.40
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (21-60 min) con 5-300 tra 0.40 e 1.20 1.20 E con ma50 > and 5-78 and deviation_sell 0.91 - 1.40 - r 15236 B"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        
                        and deviation_ma5_sotto_ma300 < 0.40
                        and ma3_last < ma28_last
                        and deviation_sell > 0.91 and deviation_sell < 1.40
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (21-60 min) con 5-300 < 0.40 E con ma50 > and 3-28 and deviation_sell 0.91 - 1.40 - r 15236 C"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma3_last < ma25_last
                        and deviation_sell > 1.41 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and 3-25 and deviation_sell 1.41 -2.70 - r 15250"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and incrocio 3-13 and deviation_sell > 2.71 - r 15262"
                        action = "sell"
                    
                    
                    
                    ################################################################################################# con trend discendente
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma50_last > ma100_last
                        and deviation_ma5_sotto_ma300 > 0.35
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.29
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x RAFFORZATA (21-60 min) con ma50 < and deviation_ma39 < -0.29 - r 15277 A"
                        action = "sell"
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma50_last > ma100_last
                        and deviation_ma5_sotto_ma300 < 0.35
                        and deviation_sell < -0.331
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.29
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x RAFFORZATA (21-60 min) con ma50 < and deviation_ma39 < -0.29 - r 15277 B"
                        action = "sell"
                        
                        
                        
                        
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma50_last < ma100_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.28
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and deviation_ma39 < -0.28 - r 15290"
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
                        sell = "SELL 4-5-x RAFFORZATA (21-60 min) con ma50 < and deviation_sell < 0.32 100>200 !- r 15310"
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
                        sell = "SELL 4-5-x RAFFORZATA (21-60 min) con ma50 < and deviation_sell < 0.29 100<200 - r 15326"
                        action = "sell"
                        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma100_last < ma100_60_min_ago
                        and ma300_last < ma300_120_min_ago
                        
                        and ma5_last < ma100_last
                        and deviation_sell < -0.22
                        and ma2_last < ma2_2_min_ago
                        
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and 5-100 and dev_sell < -0.22 CUSCINO DELLA MADONNA se ma100 < E DE SANTO RENATO 300 < - r 15348"
                        action = "sell"
                        
                        
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma50_last < ma100_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.32
                        and ma3_last < ma39_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and deviation_sell < -0.32 - r 15349"
                        action = "sell"
                        
                        
                        
                        
                        
                        
                        
              
            
            
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_60_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.37
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.37 - r 15368"
                        action = "sell"
                    
                    
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last < ma200_60_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and INCROCIO 3-100 (no 3<100) CUSCINO DI SANT' ANTONIO - r 15383"
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
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and deviation_ma39 < -0.26 - r 15406"
                        action = "sell"
                        
                 
                    
                    
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.33
                        and ma3_last < ma39_last
                        and ma200_last > ma200_60_min_ago
                        and ma300_last > ma300_120_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and 200> 60 min and 300 > 120 min and deviation_sell < -0.33 - r 15422"
                        action = "sell"
                        
                        
                        
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.28
                        and ma3_last < ma39_last
                        and ma200_last > ma200_60_min_ago
                        and ma300_last < ma300_120_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and 200> 60 min and 300 < 120 min and deviation_sell < -0.28 - r 15435"
                        action = "sell"
                        
              
                    
                
                    
                    
                    
                    
                    
                    
                    
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma200_60_min_ago
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.39
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and incrocio 3-78 and deviation_sell < -0.39 - r 15456"
                        action = "sell"
                        
                        
                  
                    elif (
                        ma50_last < ma50_2_min_ago
                        and ma200_last > ma200_60_min_ago
                        and (ma5_prev > ma100_prev and ma5_last < ma100_last)
                        and deviation_sell < -0.29
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 < and INCROCIO 5-100 (no 5<100) and deviation_sell < -0.29  CUSCINO DI SANT' ANTONIO - r 15469"
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
                        sell = "SELL 4-5-x eventuale guadagno durante il crollo (21-60 min) con ma50 < incrocio 3 - 18 and deviation_sell > 0.23 - r 15487"
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
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > and deviation_ma25 < -0.19 - r 15514"
                        action = "sell"
                        
                        
                    
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.21 
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > and (deviation_sell < -0.19 and ma3_last < ma50_last) - r 15526"
                        action = "sell"
                        
                        
                        
                        
                    elif ( 
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.25
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > and deviation_ma25 < -0.25 - r 15538"
                        action = "sell"
                        
                        
                        
                    
                    elif (    
                        ma50_last > ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.24 
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > and (deviation_sell < -0.24 and ma3_last < ma50_last) - r 15551"
                        action = "sell"
                        
                        
                        
                        
                        #########################################################################################################################
                        
                      
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and (ma5_prev > ma25_prev and ma5_last < ma25_last)
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (21-60 min) con ma50 > and incrocio 5-25 and deviation_sell 0.25 - 0.56 FINTA DI MARADONA - r 15568"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma78_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x >60 min con ma50> and 4-78 and deviation_sell 0.57-0.90 DRIBBLING ALLA RONALDO - r 15582"
                        action = "sell"
                        
                        # > estate 4-78 da 4-20
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 > 0.59
                        and (ma4_prev > ma78_prev and ma4_last < ma78_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x da 60 a 90 min ma5 molto sopra ma300 e con ma50 > and incrocio 4-78 and deviation_sell 0.91 - 1.49 - r 15595 a"
                        action = "sell"
                        
                        # > estate  4-78 da 3-30

                        
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 < 0.59
                        and (ma4_prev > ma100_prev and ma4_last < ma100_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x da 60 a 90 min ma5 non distante da ma300 e con ma50 > and incrocio 4-100 and deviation_sell 0.91 - 1.49 - r 15595 b"
                        action = "sell"

                        
                        
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma25_prev and ma3_last < ma25_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > incrocio 3-25 and deviation_sell 1.50 - 2.70 - r 15610"
                        action = "sell"
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x da 60 a 90 min con ma50 > incrocio 3-13 and deviation_sell > 2.71 - r 15623"
                        action = "sell"
                        
                    
                    
                    
                    ######################################################################################## con trend discendente
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.25
                        and deviation_ma100_sopra_ma300 > 0.50
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 < con deviation_ma39 <-0.25 - r 15638 A"
                        action = "sell"
                        
                        # and ma3_last < ma33_last
                        # and deviation_sell < 0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # cuscino dell' angelo custode
                        
                        # > estate se 100 molto sopra 300 no dev sell ma solo dev39 aumentata -0.25 da -0.18
                        
                        
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma39 < -0.25
                        and deviation_ma100_sopra_ma300 < 0.50
                        and deviation_sell < -0.27
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 < con deviation_ma39 <-0.25 and dev_sell < -0.27 - r 15638 B"
                        action = "sell"
                        
                        # and ma3_last < ma33_last
                        # and deviation_sell < 0.10
                        # se non ha forza dopo 1 ora e' inutile continuare a sperare !
                        # qui non ho messo il crollo perche' dopo 40 min o gia' ha venduto o e' gia' risalita
                        # cuscino dell' angelo custode
                        
                        # > estate con 100 vicino 300 interviene ance que dev sell !
                        
                        
                    
                    
                    # sta in alto e stai attento
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 > 0.25
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.07
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < -0.07 meno tollerante (sta in alto) - r 15660"
                        action = "sell"
                        
                        
                        
                        
                    # sta in basso e, PARADOSSALMENTE, sta piu' calmo
                    
                    elif (
                        ma50_last < ma50_2_min_ago
                        and deviation_ma100_sopra_ma300 < 0.25
                        
                        and (ma3_prev > ma78_prev and ma3_last < ma78_last)
                        and deviation_sell < -0.19
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x da 60 a 90 min con ma50 < con incrocio 3-78 and deviation_sell < -0.19 piu' tollerante (sta in basso) - r 15676"
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
                        sell = "SELL 4-5-x dopo 90 min con ma50> and deviation_ma25 <-0.28 ( no ma3 < ma39 ) - r 15700"
                        action = "sell"
                        
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and ma50_last < ma100_last
                        
                        and ma2_last < ma2_2_min_ago
                        and deviation_ma25 < -0.29
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x RAFFORZATO dopo 90 min con ma50> and deviation_ma25 <-0.29 ( no ma3 < ma39 ) - r 15713"
                        action = "sell"
                        
                      
                    
                    
                    
                    
                    elif (     
                        ma50_last > ma50_2_min_ago
                        and ma50_last > ma100_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.29
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x RAFFORZATO dopo 90 min con ma50> and (deviation_sell < -0.29 and ma3_last < ma50_last) - r 15730"
                        action = "sell"
                        
                        
                        
                        
                    elif (     
                        ma50_last > ma50_2_min_ago
                        and ma50_last < ma100_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.28
                        and ma3_last < ma50_last
                        and ma200_last < ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x dopo 90 min con ma50> and (deviation_sell < -0.28 and ma3_last < ma50_last) - r 15745"
                        action = "sell"
                        
                      
                        
                    
                    
                    
                    
                    
                    
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and ma50_last > ma100_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.31
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x RAFFORZATO dopo 90 min con ma50> and deviation_ma25 < -0.31 TOLLERANTE - r 15764"
                        action = "sell"
                        
                        
                        
                    elif (    
                        ma50_last > ma50_2_min_ago
                        and ma50_last < ma100_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma25 < -0.30
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x dopo 90 min con ma50> and deviation_ma25 < -0.30 TOLLERANTE - r 15777"
                        action = "sell"
                        
                        
                        
                        
                        
                        
                        
                    elif (     
                        ma50_last > ma50_2_min_ago
                        and ma50_last > ma100_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.32
                        
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x RAFFORZATO dopo 90 min con ma50> and (deviation_sell < -0.32 and ma3_last < ma50_last) TOLLERANTE - r 15796"
                        action = "sell"
                        
                        
                        
                    elif (     
                        ma50_last > ma50_2_min_ago
                        and ma50_last < ma100_last
                        
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.31
                        and ma3_last < ma50_last
                        and ma200_last > ma200_60_min_ago
                    ):
                        sell = "SELL 4-5-x dopo 90 min con ma50> and (deviation_sell < -0.31 and ma3_last < ma50_last) TOLLERANTE - r 15810"
                        action = "sell"
                        
                        
                        
                        #############################################################################################################################
                       
                        
                    elif (
                        ma50_last >= ma50_2_min_ago
                        and ma5_last < ma25_last
                        and deviation_sell > 0.25 and deviation_sell < 0.56
                        and ma2_last < ma2_2_min_ago
                       
                    ):
                        sell = "SELL 4-5-x (12-21 min) con ma50 > and 5-25 and deviation_sell 0.25-0.56 - FINTA ALLA MARADONA - r 15825"
                        action = "sell"
                        
                        # deviation_sell = ma3_last/last_trade_price
                        
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and ma4_last < ma20_last
                        and deviation_sell > 0.57 and deviation_sell < 0.90
                        and ma2_last < ma2_2_min_ago
                    ):
                        sell = "SELL 4-5-x >90 min con ma50 > con 4 < 20 and deviation_sell 0.35 - 0.90 FINTA ALLA RONALDO - r 15839"
                        action = "sell"
                        
                        

                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma30_prev and ma3_last < ma30_last)
                        and deviation_sell > 0.91 and deviation_sell < 1.49
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x dopo 90 min con ma50 > incrocio 3-30 (!) and deviation_sell 0.91 - 1.49 - r 15851"
                        action = "sell"

                        # ma 3-48 mi evita la ricompra e la rivendita con perdita !
                    
                    
                    
                    
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma5_prev > ma30_prev and ma5_last < ma30_last)
                        and deviation_sell > 1.50 and deviation_sell < 2.70
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x dopo 90 min con ma50 > incrocio 5-30 (!) and deviation_sell 1.50 - 2.70 - r 15866"
                        action = "sell"
                        
                        # 5-30 da 3-25 dopo dolomiti
                        
                        
                        
                    elif (
                        ma50_last > ma50_2_min_ago
                        and (ma3_prev > ma13_prev and ma3_last < ma13_last)
                        and deviation_sell > 2.71
                        and ma2_last < ma2_2_min_ago
                    ):

                        sell = "SELL 4-5-x dopo 90 min con ma50 > incrocio 3-13 (!) and deviation_sell > 2.71 - r 15879"
                        action = "sell"
                        
                        

                    ######################################################################################## con trend discendente
                    
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago 
                        and ma2_last < ma2_2_min_ago 
                        and deviation_ma39 < -0.215
                    ):
                        sell = "SELL 4-5-x dopo 90 min con ma50 < con deviation_ma39 <-0.215 - r 15893"
                        action = "sell"
                        
                        
                    
                    
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma300_last > ma300_301_min_ago
                        and deviation_ma5_sotto_ma300 > 0.10
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.13 
                        and ma3_last < ma39_last
                    ):
                        sell = "SELL 4-5-x >90 min CON 300 > 301 min ago e con 5-300 > 0.10 E ma50 < and (dev_sell < -0.13 and ma3_last < ma39_last) - r 15906 A1"
                        action = "sell"
                        
                        # 26 set 2022 con 300 > 301 min ago dev sell a -0.11 da -0.13
                        
                        
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and ma300_last < ma300_301_min_ago
                        and deviation_ma5_sotto_ma300 > 0.10
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.11 
                        and ma3_last < ma39_last
                    ):
                        sell = "SELL 4-5-x >90 min CON 300 < 301 min ago e con 5-300 > 0.10 E ma50 < and (dev_sell < -0.11 and ma3_last < ma39_last) - r 15906 A2"
                        action = "sell"
                        
                    
                    
                    
                    
                    
                    
                    elif (    
                        ma50_last < ma50_2_min_ago
                        and deviation_ma5_sotto_ma300 < 0.10
                        and ma2_last < ma2_2_min_ago 
                        and deviation_sell < -0.21 
                        and ma3_last < ma39_last
                    ):
                        sell = "SELL 4-5-x dopo 90 min con 5-300 < 0.10 E ma50 < and (deviation_sell < -0.21 and ma3_last < ma39_last) - r 15906 B"
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
            
            
            
            # 1 - SELL condizione speciale SELL PIU' SEMPLICE DEL MONDO ! -0.78 %
          
            if (        
                deviation_sell < -0.78
            ):
                buy = "SELL condizione speciale 44 - SELL PIU' SEMPLICE DEL MONDO ! -0.78 % - r 15942"
                action = "sell"
                        
                # and ma2_last < ma2_2_min_ago
                
                
            # 2 - SELL condizione speciale ro cano VENDE CON UN SALVAGENTE con deviation_ma5_sotto_ma200 > -1.00
            
            elif (
                deviation_ma39 < -0.25
                and deviation_sell < -0.32
                and ma2_last < ma2_2_min_ago
                
                and ma50_last > ma50_2_min_ago
                and deviation_ma100_sopra_ma300 > 0.40
                
                and deviation_ma5_sotto_ma200 > -1.00
            ):
                sell = "SELL condizione speciale 1 - SALVAGENTE 1 3-39 con ma50 > - con deviation_ma5_sotto_ma200 > -1.00 - r 15943"
                action = "sell"
                
                # 14 giu 2022 deviation_sell -0.32
                

                
                
          
            
            # 3 - SELL condizione speciale ro cano VENDE CON UN SALVAGENTE con deviation_ma5_sotto_ma200 > -1.00   
            
            elif (
                deviation_ma39 < -0.25
                and deviation_sell < -0.34
                and ma2_last < ma2_2_min_ago 
                
                and ma50_last > ma50_2_min_ago
                and deviation_ma100_sopra_ma300 < 0.40
                
                and deviation_ma5_sotto_ma200 > -1.00
            ):
                sell = "SELL condizione speciale 2 - SALVAGENTE 2 3-39 con ma50 > - con deviation_ma5_sotto_ma200 > -1.00 and deviation < -0.34 - r 15965"
                action = "sell"   
                

                # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !)
                
                
         
            # 3 - SELL condizione speciale ro cano VENDE CON UN SALVAGENTE con deviation_ma5_sotto_ma200 > -1.00
            
            elif (
                deviation_ma39 < -0.24
                and deviation_sell < -0.30
                and ma2_last <= ma2_2_min_ago 
                
                and ma50_last < ma50_2_min_ago
                and deviation_ma100_sopra_ma300 > 0.20
                
                and deviation_ma3_sotto_ma200 > -1.20
            ):
                sell = "SELL cond. special 3 - SALVAGENTE 3 3-39 < -0.25 e dev sell < -0.31 and dev_sell< -0.305 con ma50< e dev_ma3_sotto_ma200 > -1.20 - r 15985 A"
                action = "sell"
                
                
                
                # 27 giu 2022 dev sell a 0.305 da 0.31
                # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !)
                # 21 giugno 2022 RICORDO TREMENDO 9372 ha venduto a -2.23% !!!
                # COME PRIMA COSA HO NOTATO CHE AVEVA DEVIATION INVECE DI DEVIATON SELL 
                # ma non sapendo se era questo il problema ho creato la prossima condizione speciale.
                
                
                # > estate dev 39 -0.24 da -0.25 dev sell -0.30 da -0.31 
                # 13 set -3% !!! deviation_ma3_sotto_ma200 > -1.20 da deviation_ma3_sotto_ma200 > -1.20 
                # 13 set -3% <= da <
                
            # 4 - SELL ricordo terribile del 21 giugno 2022
            
            elif (
                
                ma3_last < ma100_last
                and deviation_sell < -0.69
                and deviation_ma100_sopra_ma300 > 0.20
                and ma2_last < ma2_2_min_ago 
             
            ):
                sell = "SELL condizione speciale 4 - 21 giugno 2022 - deviation_sell < -0.69 - r 16010 Ba"
                action = "sell"   
             
                # 21 giugno 2022 RICORDO TERRIBILE del 21 giugno 2022 !  9372 A ha venduto a -2.23% !!!
                
                
                
            # 4 - SELL ricordo terribile del 21 giugno 2022
            
            elif (
                
                ma3_last < ma100_last
                and deviation_sell < -0.68
                and deviation_ma100_sopra_ma300 < 0.20
                and ma2_last < ma2_2_min_ago 
             
            ):
                sell = "SELL condizione speciale 5 - 21 giugno 2022 - deviation_sell < -0.68 - r 16027 Bb"
                action = "sell"   
             
                # 21 giugno 2022 RICORDO TERRIBILE del 21 giugno 2022 !  9372 A ha venduto a -2.23% !!!
                
                
            
                
            # 5 - SELL condizione speciale ro cano VENDE CON UN SALVAGENTE con deviation_ma5_sotto_ma200 > -1.00
            
            elif (
                deviation_ma39 < -0.255
                and deviation_sell < -0.36
                and ma2_last < ma2_2_min_ago 
                
                and ma50_last < ma50_2_min_ago
                and deviation_ma100_sopra_ma300 < 0.40
                
                and deviation_ma5_sotto_ma200 > -1.00
            ):
                sell = "SELL condizione speciale 6 - SALVAGENTE 4 deviation 3-39 <-0.255 and dev <-0.36 - con ma50 < e con ma5 sotto ma200 > -1.00 - r 16047"
                action = "sell"   
                

                # deviation_ma39 = ma4_last / ma39_last QUESTA HA VENDUTO NEL CROLLO IMPROVVISO DI 1 MINUTO (con -2.06% !!!)!
                # modifica solo devation.
                # > estate -0.37 da -0.33
                # 18 set HA FATTO -0.84 ! dev 39 -0.255 da 0.26 E dev sell -0.36 da -0.37
                
                
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
                sell = "SELL condizione speciale 7 - SALVAGENTE 1 3-39 con ma50 > - con deviation_ma5_sotto_ma200 < -1.00 and > -1.50 - r 16084"
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
                sell = "SELL condizione speciale 8 - SALVAGENTE 2 3-39 con ma50 > - con deviation_ma5_sotto_ma200 < -1.00 and > -1.50 - r 16106"
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
                sell = "SELL condizione speciale 9 - SALVAGENTE 3 3-39 con ma50 < - con deviation_ma5_sotto_ma200 < -1.00 and > -1.50 - r 16129"
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
                sell = "SELL condizione speciale 10 - SALVAGENTE 4C 3-39 con ma50 < - con deviation_ma5_sotto_ma200 < -1.50 CROLLO ! - r 16153 A"
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
                sell = "SELL condizione speciale 10 - SALVAGENTE 4 3-13 con ma50 < e con dev_ma5_sotto_ma200 < -1.00 and > -1.50 GRANDE RIBASSO ! - r 16179 B"
                action = "sell"
                
                # co deviation 3-39 NELLA PRESENTE SITUAZIONE CROLLO 3 SOTTO 39 E PARTIVA IL PUNTO ROSSO SOVRAPPOSTO AL PUNTO VERDE
                

                
                
                
                
                
                
                
            ##################################################################################### SALVAGENTE con deviation_ma5_sotto_ma200 < -1.50
            
            
            
            # 11 - SELL condizione speciale ro cano VENDE CON UN SALVAGENTE con deviation_ma5_sotto_ma200 < -1.50
            
            elif (
                deviation_ma39 < -0.25
                and deviation_sell < -0.50
                
                and ma50_last > ma50_2_min_ago
                and deviation_ma100_sopra_ma300 > 0.40
                
                and deviation_ma5_sotto_ma200 < -1.50
            ):
                sell = "SELL condizione speciale 11 - SALVAGENTE 1C 3-39 con ma50 > - con deviation_ma5_sotto_ma200 < -1.50 - r 16207"
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
                sell = "SELL condizione speciale 12 - SALVAGENTE 2C 3-39 con ma50 > - con deviation_ma5_sotto_ma200 < -1.50 - r 16228"
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
                sell = "SELL condizione speciale 13 - SALVAGENTE 3C 3-39 con ma50 < - con deviation_ma5_sotto_ma200 < -1.50 - r 16253 a"
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
                sell = "SELL condizione speciale 14 - SALVAGENTE 3C 3-39 con ma50 < - con deviation_ma5_sotto_ma200 < -1.50 - r 16277 b"
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
                  
                sell = "SELL condizione speciale 15 - CROLLO IMPROVVISO - and deviation_ma5_sotto_ma200 > -1.00 - r 16311"
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
                  
                sell = "SELL condizione speciale 16 - CROLLO IMPROVVISO - and deviation_ma5_sotto_ma200 < -1.00 - r 16335"
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
                
                and deviation_crollo_24_aprile < -0.55
                
                and deviation_ma5_sotto_ma200 > -1.00
            ): 
                
                sell = "SELL cond. special 17 - DOPO CROLLO IMPROVVISO del 24 aprile 2022 - and dev_ma5_sotto_ma200 > -1.00 - (-0.55) giorno E 33>78 - r 16369 a1"
                action = "sell"
                        
                # ho aggiunto anche questa vendita speciale dopo il 24 aprile -1%
                # deviation_crollo_24_aprile = ma2_last / last_trade_price        
                # -0.58 ha generato perdita -0.82 il 10 maggio 2022 cosi' ho ridotto a -0.575
                # -0.575 ha generato perdita -1.12 il 10 maggio 2022 cosi' ho ridotto a -0.57
                # -0.57 ha generato perdita -1.37 il 12 maggio 2022 cosi' ho ridotto a -0.56
                # -0.56 ha generato perdita -1.19 il 13 maggio 2022 cosi' ho ridotto a -0.55
                
                # con delta_1_200_30 < delta_2_200_30_30_min ho aumentato a -0.56
                # -0.56 HA GENERATO PERDITA DI -1.42 il 22 luglio 2022 ! cazzo !
                
                # 21 giu 2022 a -0.56 da -0.57
                # 22 lug 2022 a -0.55 da -0.56 dopo grande perdita !
                # ATTENZIONE ! 22 lug 2022 questa condizione ha fatto -1.42 % !!! per fortuna RCCR ha fatto -0.52 e l' ho portata in MADDOG
                
                
                
            # 18 - SELL condizione speciale dopo crollo improvviso del 24 aprile 2022 ! and deviation_ma5_sotto_ma200 > -1.00
                    
            elif (    
                ma2_last < ma4_last
                and ma2_last < ma6_last
                and ma33_last < ma78_last
                
                and delta_1_200_30 < delta_2_200_30_30_min
                
                and deviation_crollo_24_aprile < -0.56
                
                and deviation_ma5_sotto_ma200 > -1.00
            ): 
                
                sell = "SELL cond. special 18 - DOPO CROLLO IMPROVVISO del 24 aprile 2022 - and dev_ma5_sotto_ma200 > -1.00 - (-0.56) giorno MA 33<78 - r 16399 a2"
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
                
                sell = "SELL cond. special 19 - DOPO IL CROLLO IMPROVVISO del 24 aprile 2022 - and deviation_ma5_sotto_ma200 > -1.00 - (-0.56) notte - r 16427 b"
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
                
                sell = "SELL cond. special 20 - DOPO IL CROLLO IMPROVVISO del 24 aprile 2022 - and delta_1 < delta_2 and dev_ma5_sotto_ma200 < -1.00 - r 16456 a"
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
                and deviation_crollo_24_aprile < -0.57
                
                and delta_1 > delta_2
                and deviation_ma5_sotto_ma200 < -1.00
            ): 
                
                sell = "SELL cond special 21 - DOPO IL CROLLO IMPROVVISO del 24 apr 2022 - and delta_1 > delta_2 and dev_ma5_sotto_ma200 < -1.00 < -0.57 - r 16480 b"
                action = "sell"
                        
                # ho aggiunto anche questa vendita speciale dopo il 24 aprile -1%
                # deviation_crollo_24_aprile = ma2_last / last_trade_price        
                # -0.58 ha generato perdita -0.82 il 10 maggio 2022 cosi' ho ridotto a -0.575
                # -0.575 ha generato perdita -1.12 il 10 maggio 2022 cosi' ho ridotto a -0.57
                
                # -0.60 ha generato perdita -0.84 il 13 maggio 2022 cosi' ho ridotto a -0.59
                # MA VA BENE !
                # 27 giu 2022 a -0.58 da -0.59
                # 2 lug 2022 a -0.57 da -0.58 dopo che ha fatto -0.96 durante un crollo
                
                
                ######################################################################################### fine dopo il crollo improvviso del 24 aprile 2022
                
                
                
            
            
            
            # 22 - SELL condizione speciale RIBASSO IMPROVVISO con deviation_sell < -0.60
            
            elif (
                ma78_last > ma78_2_min_ago
                and deviation_ribasso_improvviso < -0.63
                and deviation_evita_ribasso_improvviso_crollo_ferrari > -0.62
                and deviation_sell < -0.60
            ):
                sell = "SELL condizione speciale 22 RIBASSO IMPROVVISO - r 16509"
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
                sell = "SELL condizione speciale 23 RIBASSO IMPROVVISO - r 16530"
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

                sell = "SELL condizione speciale 24 - DOLCE ATTESA con ma100 > e ma13 > and deviation < -0.39 - r 16556"
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

                sell = "SELL condizione speciale 25 - DOLCE ATTESA con ma100 > e ma13 < and deviation < -0.37 - r 16574"
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

                sell = "SELL condizione speciale 26 - DOLCE ATTESA con ma100 < e con ma13 > and deviation < -0.41 - r 16592"
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

                sell = "SELL condizione speciale 27 - DOLCE ATTESA con ma100 < e con ma13 < and dev_sell < -0.355 ( and 20 > 100 ) - r 16614"
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

                sell = "SELL condizione speciale 28 - DOLCE ATTESA 300 > con ma100 < e con ma13 < and deviation < -0.39 ( and 20 < 100 ) - r 16638 a"
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

                sell = "SELL condizione speciale 29 - DOLCE ATTESA 300 < con ma100 < e con ma13 < and deviation < -0.42 ( and 20 < 100 ) - r 16670 b"
                action = "sell"

                
                
                
                
                
             
            # 30 - SELL condizione speciale ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma13 <
            
            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and deviation_sell < -0.43
                
                and deviation_ma100_sopra_ma200 > -0.70
                and deviation_ma100_sopra_ma300 > 0.50
               
                and ma13_last < ma13_2_min_ago
                
                and ma2_last < last_trade_price
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL cond. special 30 A - DOLCE ATTESA 270 sec con ma13 < and deviation < -0.43 CON 100 sopra 300 > 0.50 statt' accorto ! - r 16694 a"
                action = "sell"
                
                # 4 feb 2022 con <-0.26 ha fatto -0.88% (dopo +4.29%)
                # 7 feb 2022 con <-0.345 e 270 sec ha fatto -0.38% - aumenta a 0.355 ! - eventualmente ci pensa la condizione CROLLO IMPROVVISO CHE FUNZIONA !
                
                
                
                
                
                
                
                
            # 30 - SELL condizione speciale ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma13 <
            
            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and deviation_sell < -0.57
                
                and deviation_ma100_sopra_ma200 > -0.70
                and deviation_ma100_sopra_ma300 < 0.50
              
                and ma13_last < ma13_2_min_ago
                
                and ma2_last < last_trade_price
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL cond. special 30 B - DOLCE ATTESA 270 sec con ma13 < E dev_sell < -0.43 CON 100 sopra 300 < 0.50 MA non e' situazione crollo - r 16694 B"
                action = "sell"
             
                # 4 feb 2022 con <-0.26 ha fatto -0.88% (dopo +4.29%)
                # 7 feb 2022 con <-0.345 e 270 sec ha fatto -0.38% - aumenta a 0.355 ! - eventualmente ci pensa la condizione CROLLO IMPROVVISO CHE FUNZIONA !
                # 17 set -0.57 da -0.47
                
                
                
                
                
                
                
                
            # 31 - SELL condizione speciale ro cano VENDE " DOPO x MINUTI " "max hold time" - DOLCE ATTESA con ma13 <
            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and deviation_ma100_sopra_ma200 < -0.70
                
                and deviation_sell < -0.50
                and ma13_last < ma13_2_min_ago
                
                and ma2_last < last_trade_price
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL condizione speciale 31 - DOLCE ATTESA 270 sec con ma13 < and deviation < -0.50 con 100 sotto di molto 200 durante crollo ! - r 16719"
                action = "sell"
                
                # durante il crollo sono un po' piu' tollerante - paradossalmente ! HO ATTESO MOLTO QUESTO MOMENTO !

                
                        
            
            
            
            
            
            
            # 32 A - SELL condizione speciale ro cano VENDE " DOPO x MINUTI " and...
            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and deviation_sell < -0.49
                and ma8_last < ma50_last
                
                and ma2_last < ma2_2_min_ago
            ):

                sell = "SELL condizione speciale 32 - TEMPO e se ma8 < ma50 and deviation_sell < -0.49 - r 16743 A"
                action = "sell"
                        
                # ma13 troppo lenta !
                # max_hold_time_in_seconds = 360 = 6 min (con 8 min perdita di 0.70 %)
                
                
                
                
                
                
            # 32 B - SELL condizione speciale ROOT DOWN DEEP - ro cano VENDE dopo 150 min = 9000 sec con 5-90
            
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds_sell_5_90
                and ma300_last > ma300_120_min_ago
                and ma5_last < ma90_last
                and ma2_last < ma2_2_min_ago
           
            ):

                sell = "SELL condizione speciale 32 B ROOT DOWN DEEP - ro cano VENDE dopo 150 min = 9000 sec con 5-90 - r 16743 B1"
                action = "sell"
                        
                # 24 set 2022 ore 17:23
                
                
                
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds_sell_5_90
                and ma300_last < ma300_120_min_ago
                and ma5_last < ma300_last
                and ma2_last < ma2_2_min_ago
           
            ):

                sell = "SELL condizione speciale 32 B ROOT DOWN DEEP - ro cano VENDE dopo 150 min = 9000 sec con 5-90 - r 16743 B2"
                action = "sell"
                        
                # 24 set 2022 ore 17:23
                
                        
                        
               
            
            
            
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
                sell = "SELL cond. special 33 - POCHI MALEDETTI E SUBITO QUANDO SALE FORTE 3-28 ( cerca di inibirlo ) con ma200> e con dev_sell > 0.70 - r 16767"
                action = "sell"
                    
                # and ma2_last > ma100_last (altrimenti vende durante il crollo con la ma3-ma9)
                # incredibile questa and deviation_trend_ma100 < 1.00 - se ma100 sale "forte" da 60 min non deve intervenire sell 3-9
                
                
                
            # 34 - SELL condizione speciale POCHI MALEDETTI E SUBITO QUANDO SALE PIANO con ma200 > MA ma100 NON DEVE SALIRE TROPPO ! - dedicated to comparo meo
            
            elif (
                ma3_last < ma39_last
                and deviation_ma100_sopra_ma200 < 0.40      
                and ma200_last > ma200_60_min_ago
                    
                and deviation_sell > 0.70
                and deviation_sell < 0.99
                and deviation_trend_ma100 < 1.00
                and deviation_pochi_maledetti > 0.25
                and ma2_last > ma100_last
                
            ):    
                sell = "SELL condizione speciale 34 - POCHI MALEDETTI E SUBITO 3-39 QUANDO SALE PIANO quando ma200 > e con dev_sell > 0.70 and < 0.99 - r 16789"
                action = "sell"
                    
                # and ma2_last > ma100_last (altrimenti vende durante il crollo con la ma3-ma9)
                # incredibile questa and deviation_trend_ma100 < 1.00 - se ma100 sale "forte" da 60 min non deve intervenire sell 3-9
                # > estate 3-39 da 3-25    
                
                
            
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
                sell = "SELL cond. special 35 - POCHI MALEDETTI E SUBITO 3-20 quando ma200 < e con dev_sell > 0.90 and < 1.30 - dedicated to comparo meo - r 16809"
                action = "sell"
                    
                # and ma2_last > ma100_last (altrimenti vende durante il crollo con la ma3-ma9)
                
                
                
                
            # 36 - SELL condizione speciale POCHI MALEDETTI E SUBITO ma non troppo ! 3-18 quando ma200 < e con deviation_sell > 1.31 and < 2.50
            
            elif (
                ma3_last < ma18_last 
                and ma200_last < ma200_60_min_ago
                and deviation_sell > 1.31
                and deviation_sell < 2.50
                and deviation_pochi_maledetti > 0.70
                and ma2_last > ma100_last
                and ma2_last < ma2_2_min_ago
            ):    
                sell = "SELL condizione speciale 36 - POCHI MALEDETTI E SUBITO ma non troppo ! 3-18 quando ma200 < e con dev_sell > 1.31 and < 2.50 - r 16828"
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
                sell = "SELL condizione speciale 37 - POCHI MALEDETTI E SUBITO ma non troppo mentre sale 3-28 quando ma200 < e con deviation > 2.51 - r 16852 a"
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
                sell = "SELL condizione speciale 38 - POCHI MALEDETTI E SUBITO 3-8 quando ma200 < e con deviation > 2.51 - dedicated to comparo meo - r 16872 b"
                action = "sell"
                    
                # and ma2_last > ma100_last (altrimenti vende durante il crollo con la ma3-ma9)
                
                
                
                
            # 39 - POCHI MALEDETTI E SUBITO ma non troppo mentre scende > ESTATE 
            
            elif (
                ma5_last < ma39_last
                and ma300_last > ma300_120_min_ago
                and ma3_last < ma300_last
                
                and deviation_sell > 0.90
                
                and ma2_last > ma100_last
                and ma2_last < ma2_2_min_ago
            ):    
                sell = "SELL condizione speciale 39 5-39 - POCHI MALEDETTI E SUBITO ma non troppo mentre scende > ESTATE  e con deviation > 0.90 - r 16873 A"
                action = "sell"
                    
                # and ma2_last > ma100_last (altrimenti vende durante il crollo con la ma3-ma9)
                
                
                
            # 39 - POCHI MALEDETTI E SUBITO ma non troppo mentre scende > ESTATE 
            
            elif (
                ma5_last < ma33_last
                and ma300_last < ma300_120_min_ago
                and ma3_last < ma300_last
                
                and deviation_sell > 0.90
                
                and ma2_last > ma100_last
                and ma2_last < ma2_2_min_ago
            ):    
                sell = "SELL condizione speciale 39 5-33 - POCHI MALEDETTI E SUBITO ma non troppo mentre scende > ESTATE  e con deviation > 0.90 - r 16873 B"
                action = "sell"
                    
                # and ma2_last > ma100_last (altrimenti vende durante il crollo con la ma3-ma9)
                
                
                
                
            
            ######################################################################### vendite dedicate al BUY FIAT - AUDI - MASERATI - FERRARI 
            
            # 40 - SELL condizione speciale FIAT 
                    
            elif (     
                seconds_since_last_trade > max_hold_time_in_seconds_fiat
                and deviation_buy_crollo_1 < -0.15
                and deviation_buy_crollo_1 > -0.59
                        
                and deviation_ma100_sopra_ma300 < -0.70
                and deviation_sell < -0.30
            ):    
                 
                buy = "SELL condizione speciale 39 - FIAT se > 2 min dal BUY FIAT la perdita e' < -0.30 ! - r 16894"
                action = "sell"
                        
                # and ma2_last < ma2_2_min_ago
                # and deviation_ma100_sopra_ma300 < -0.70 significa che c'e' un grande ribasso. 100 sta lontana da 300. 
                # EVITO COSI' PROBLEMI AL TREND LATERALE.
                        
                        
                        
                
            # 41 - SELL condizione speciale AUDI 
                    
            elif (     
                seconds_since_last_trade > max_hold_time_in_seconds_audi
                and deviation_buy_crollo_1 < -0.60
                and deviation_buy_crollo_1 > -0.90
                        
                and deviation_ma100_sopra_ma300 < -0.70
                and deviation_sell < -0.40
                        
            ):
                buy = "SELL condizione speciale 40 - AUDI se > 2 min dal BUY AUDI la perdita e' < -0.40 - r 16915"
                action = "sell"
                        
                # and ma2_last < ma2_2_min_ago
                        
                        
            
            
            # 42 - SELL condizione speciale MASERATI 
                    
            elif (     
                seconds_since_last_trade > max_hold_time_in_seconds_maserati
                and deviation_buy_crollo_1 < -0.91
                and deviation_buy_crollo_1 > -1.50
                      
                and deviation_ma100_sopra_ma300 < -0.70
                and deviation_sell < -0.50
                        
            ):
                buy = "SELL condizione speciale 41 - MASERATI se > 2 min dal BUY MASERATI la perdita e' < -0.50 - r 16934"
                action = "sell"
                        
                # and ma2_last < ma2_2_min_ago
                
                
                        
            # 43 - SELL condizione speciale FERRARI 
                    
            elif (     
                seconds_since_last_trade > max_hold_time_in_seconds_ferrari
                and deviation_buy_crollo_1 < -1.51
                        
                and deviation_ma100_sopra_ma300 < -0.70
                and deviation_sell < -0.58
            ):
                buy = "SELL condizione speciale 42 - FERRARI se > 2 min dal BUY FERRARI la perdita e' < -0.70 - r 16935"
                action = "sell"
                        
                # and ma2_last < ma2_2_min_ago
                
                
                
            # 44 SELL condizione speciale da RCCR ! IPOTESI PEGGIORE con ma50< con dev_ma39 < -0.225 and deviation_sell < -0.22 MA DOPPIO DELTA RIALZO 
                     
            elif (
                ma50_last < ma50_2_min_ago
                and ma3_last < ma300_last
                and ma200_last < ma300_last
                and deviation_trend_ma200 < -0.10
                        
                and deviation_ma39 < -0.225
                and deviation_sell < -0.23
                        
                and rapporto_delta_1_delta_2 < 1
                        
                and ma2_last < ma2_2_min_ago
            ):
                sell = "SELL 1 da RCCR ! IPOTESI PEGGIORE con ma50< con dev_ma39 < -0.225 and deviation_sell < -0.23 MA DOPPIO DELTA RIALZO - r 16936"
                action = "sell"
                        
                # 19 SET r 10546 la condizione precedente ha fatto -1.65 ed e' partita insieme ad altre 2 condizioni speciali !
                
                # quindi, ho aggiunto questa condizione importata da RCCR SIA QUA CHE NELLE CONDIZIONI SPECIALI ( nuova condizione speciale )
                # 19 set 2022 IMPORTATO DA RCCR > sell 4:18 del 19 set -1.65 % !
                # 19 set 2022 deviation_ma39 < -0.22 AND and deviation_sell < -0.22
                # 20 set 2022 ho aumentato SOLO LA dev sella a -0.23 !
                
                
                
               
                    
                
                
                

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
            
            
            # 5 luglio 2022 fine ordine e progresso.
            # combaro meo, grazie di tutto !
            
            
            # i know how to speak- manchester orchestra 
            # core 'ngrato - enrico caruso
           
        
        
        
        
