

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
        
        ma13_last, ma13_prev = self.algo_helper.ma_last_prev(13)
        ma15_last, ma15_prev = self.algo_helper.ma_last_prev(15)
        
        ma16_last, ma16_prev = self.algo_helper.ma_last_prev(16)
        
        ma17_last, ma17_prev = self.algo_helper.ma_last_prev(17)
        ma18_last, ma18_prev = self.algo_helper.ma_last_prev(18)
        ma20_last, ma20_prev = self.algo_helper.ma_last_prev(20)
        
        ma25_last, ma25_prev = self.algo_helper.ma_last_prev(25)
        
        ma30_last, ma30_prev = self.algo_helper.ma_last_prev(30)
        ma33_last, ma33_prev = self.algo_helper.ma_last_prev(33)
        ma36_last, ma36_prev = self.algo_helper.ma_last_prev(36)
        ma38_last, ma38_prev = self.algo_helper.ma_last_prev(38)
        
        ma39_last, ma39_prev = self.algo_helper.ma_last_prev(39)
        
        ma40_last, ma40_prev = self.algo_helper.ma_last_prev(40)
        ma45_last, ma45_prev = self.algo_helper.ma_last_prev(45)
        ma50_last, ma50_prev = self.algo_helper.ma_last_prev(50)
        ma60_last, ma60_prev = self.algo_helper.ma_last_prev(60)
        ma78_last, ma78_prev = self.algo_helper.ma_last_prev(78)
        ma82_last, ma82_prev = self.algo_helper.ma_last_prev(82)
        
 
        # moving average (2-3-4-5-7-8-20-43-100) di x minuti prima
        
        ma2_2_min_ago = self.algo_helper.ma_minutes_ago(2, 2)
        ma2_3_min_ago = self.algo_helper.ma_minutes_ago(2, 3)
       
        ma3_2_min_ago = self.algo_helper.ma_minutes_ago(3,2)
        ma4_2_min_ago = self.algo_helper.ma_minutes_ago(4,2)
        ma6_2_min_ago = self.algo_helper.ma_minutes_ago(6,2)
        
        ma13_2_min_ago = self.algo_helper.ma_minutes_ago(13,2)
        
        ma16_2_min_ago = self.algo_helper.ma_minutes_ago(16,2)
        ma25_2_min_ago = self.algo_helper.ma_minutes_ago(25,2)
        ma39_2_min_ago = self.algo_helper.ma_minutes_ago(39,2)
        ma39_42_min_ago = self.algo_helper.ma_minutes_ago(39,42)
        ma39_52_min_ago = self.algo_helper.ma_minutes_ago(39,52)
        ma50_2_min_ago = self.algo_helper.ma_minutes_ago(50,2)
        
        ma78_2_min_ago = self.algo_helper.ma_minutes_ago(78,2)
        
        ma78_20_min_ago = self.algo_helper.ma_minutes_ago(78,20)
        
        ma78_40_min_ago = self.algo_helper.ma_minutes_ago(78,40)
        
        
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
        
        
        # PREZZO di X MINUTI FA (di mercato) - PREV PRICE
        price_1_min_ago = self.algo_helper.price_minutes_ago(1)
        price_2_min_ago = self.algo_helper.price_minutes_ago(2)
        price_3_min_ago = self.algo_helper.price_minutes_ago(3)
        price_5_min_ago = self.algo_helper.price_minutes_ago(5)
        
        
        #############################################################################################################################################################
        
        

        # VENDE DOPO x secondi = x minuti * 60 ("e se") ro cano torna a casa - riga 817
        max_hold_time_in_seconds = 2400

        # VENDE DOPO 600 secondi = 10 minuti ("e se") - ro cano perde la forza - riga 323
        max_hold_without_force_time_in_seconds = 600
        
        
        #############################################################################################################################################################
        
        
        # TEMPO in cui (PER COMPRARE) (a tutte le condizioni gia' attive) SI AGGIUNGE una condizione aggiuntiva LA DEVIATION !

        # dall' ULTIMO trade ( 15 minuti = 15 * 60 = 900 secondi )
        min_buy_delay_in_seconds = 900

        # dal PENULTIMO trade ( 150 minuti = 150 * 60 = 9000 secondi )
        min_prev_buy_delay_in_seconds = 9000

       ###############################################################################################################################################################
    
        # formula DEVIATION_gabbia 
        deviation_gabbia = ( ma8_last / ma78_last - 1 ) * 100 if ma78_last else 0
        self.algo_helper.log("deviation_gabbia: {}".format(deviation_gabbia))
        
        # formula DEVIATION_buy1 per comprare durante il TREND RIBASSISTA 
        deviation_buy1 = ( ma8_last / ma78_last - 1 ) * 100 if ma78_last else 0
        self.algo_helper.log("deviation_buy1: {}".format(deviation_buy1))
        
        
        # formula DEVIATION_buy2 per la compra 2 
        deviation_buy2 = ( ma8_last / ma78_last - 1 ) * 100 if ma78_last else 0
        self.algo_helper.log("deviation_buy2: {}".format(deviation_buy2))
        
        
        # formula DEVIATION_buy3 per la compra 3
        deviation_buy3 = ( ma8_last / ma78_last - 1 ) * 100 if ma78_last else 0
        self.algo_helper.log("deviation_buy3: {}".format(deviation_buy3))
        
        ########################################################################################################################
        
        
        # formula DEVIATION_buy per comprare UN PO' PIU' SOPRA DEL LAST TRADE ( di solito l' ultimo SELL ) 
        deviation_buy = ( ma2_last / last_trade_price - 1 ) * 100 if last_trade_price else 0
        self.algo_helper.log("deviation_buy: {}".format(deviation_buy))
        
        # formula DEVIATION_buy_ma4 per comprare UN PO' PIU' SOPRA DEL LAST TRADE ( di solito l' ultimo SELL ) ma PIU' LENTA ! PERCHE' ma2 si muove troppo disinvoltamente
        deviation_buy_ma4 = ( ma4_last / last_trade_price - 1 ) * 100 if last_trade_price else 0
        self.algo_helper.log("deviation_buy: {}".format(deviation_buy_ma4))
        
        
        # formula DEVIATION_prev per comprare UN PO' PIU' SOPRA DEL PREV TRADE ( di solito l' ultimo BUY )
        deviation_prev = ( price / prev_trade_price - 1 ) * 100 if prev_trade_price else 0
        self.algo_helper.log("deviation_prev: {}".format(deviation_prev))

        # formula DEVIATION_sell per vendere
        deviation_sell = ( ma3_last / last_trade_price - 1 ) * 100 if last_trade_price else 0
        self.algo_helper.log("deviation_sell: {}".format(deviation_sell))
        
        
        # formula DEVIATION_ma50 per vendere a una certa distanza da ma50
        deviation_ma50 = ( ma2_last / ma50_last - 1 ) * 100 if ma50_last else 0
        self.algo_helper.log("deviation_ma50: {}".format(deviation_ma50))
        
        
        # formula DEVIATION_buy_crollo per comprare a una certa distanza da ma13
        deviation_buy_crollo = ( ma3_last / ma13_last - 1 ) * 100 if ma13_last else 0
        self.algo_helper.log("deviation_buy_crollo: {}".format(deviation_buy_crollo))
        
        
        
        #######################################################################################################################################################
        # formula prezzo piu' alto nella fascia ! riga 242 - 266
        highest_price_50_min_ago = self.algo_helper.highest_price_minutes_ago(50)
        
        ######################################################################################################################################################
        # formula DEVIATION_sell_ma78
        deviation_sell_ma78 = ( ma2_last / ma78_last - 1 ) * 100 if ma78_last else 0
        self.algo_helper.log("deviation_sell_ma78: {}".format(deviation_sell_ma78))
        
        
        
        # formula DEVIATION_ma3_sopra_ma40
        deviation_ma3_sopra_ma40 = ( ma3_last / ma40_last - 1 ) * 100 if ma40_last else 0
        self.algo_helper.log("deviation_ma3_sopra_ma40: {}".format(deviation_ma3_sopra_ma40))
        
        
        
        
        ###################################################################################################################################
        
        

        # DEFAULT ACTION DICE DI NON FARE NIENTE (=None, NON TOCCARE)
        action = None

        
        
        ##########################################################################################################################################

        # APRE E CHIUDE GABBIA

        #if ma50_last >= ma50_2_min_ago and deviation_gabbia > -0.15 or ( deviation_buy1 < -1.90 ):
        if deviation_gabbia > -0.60 or ( deviation_buy1 < -1.90 ):
        
        #ti ricordo che deviation_gabbia = (ma8_last / ma78_last)
           
            
            # NON TOCCARE QUESTA CONDIZIONE SERVE PER APERTURA DI GABBIA !
            if not self.session or not self.open:
                self.session = 1
                self.open = True
                self.algo_helper.log("session {}: open segment".format(self.session))

        # SI CHIUDE LA GABBIA SE
        elif self.open:
            self.open = False
            self.algo_helper.log("session {}: closed segment".format(self.session))

        #############################################################################################################################################

        ############################################################################################################################################
        
        # COMPRA
        # NON TOCCARE QUESTA CONDIZIONE (QUESTA DICE CHE STA IN MODO BUY, DEVO COMPRARE)
        if self.open and self.session and last_trade_action != "buy":

        ###################################################################################
            
            
            
            # COMPRA UN PO' PIU' SOPRA DELL' ULTIMO TRADE SE deviation_buy > x nei 540 secondi  ( quasi sempre IL SELL )
            if (
            
                (
                    seconds_since_last_trade > 0
                    and seconds_since_last_trade <= min_buy_delay_in_seconds
                    and deviation_buy > 0.20
                )
                
                # COMPRA UN PO' PIU' SOPRA DEL PENULTIMO TRADE SE deviation_prev > x nei 300 secondi ( qualche volta IL BUY)
                
                or (
                    seconds_since_prev_trade > 0
                    and seconds_since_prev_trade <= min_prev_buy_delay_in_seconds
                    and deviation_prev > 0.20
                )
                
                
                or (
                    seconds_since_last_trade == 0
                    or seconds_since_last_trade > min_buy_delay_in_seconds
                )
              
                
            ):

############################################################################################################################################################################
############################################################################################################################################################################


                # COMPRA sessione 1
          
                if self.session == 1:
               
            
                    
                    if (
                       
                        
                        ma78_last > ma78_20_min_ago
                      
                        and ( deviation_buy1 > 0.10 and ( ma8_prev < ma50_prev and ma8_last > ma50_last ))
                        
                        and price > price_2_min_ago
                        and ma2_last > ma2_2_min_ago
                        and ma4_last > ma4_2_min_ago
                        and ma4_last > ma8_last
                        and ma8_last > ma50_last
                        and ma16_last > ma16_2_min_ago
                        
                        #deviation_buy1 = ma8_last / ma78_last
                       
                    
                    ):
                    
                        buy = "BUY #1-INCROCIO CLASSICO"
                        action = "buy"
                        
                        
                        
                        
                    elif (
                       
                        
                        ma78_last > ma78_20_min_ago
                      
                        and ( deviation_buy1 > 0.15 )
                        
                        and price > price_2_min_ago
                        and ma2_last > ma2_2_min_ago
                        and ma4_last > ma4_2_min_ago
                        and ma4_last > ma8_last
                        and ma8_last > ma50_last
                        and ma16_last > ma16_2_min_ago
                        
                        #deviation_buy1 = ma8_last / ma78_last
                       
                    
                    ):
                    
                        buy = "BUY #1-CON LA DEVIATION BUY "
                        action = "buy"
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    
                    elif (
                        
                        ma78_last < ma78_20_min_ago
                       
                        and ( deviation_buy1 > 0.90 and (ma18_prev < ma78_prev and ma18_last > ma78_last ))
                        
                        #and ma39_last > ma50_last
                        #questa sta nel maddog che va molto bene durante i ribassi
                        
                        and ma8_last > ma50_last
                        
                        and price > price_2_min_ago
                        and ma2_last > ma2_2_min_ago
                        and ma4_last > ma4_2_min_ago
                        
                        
                        and ma4_last > ma8_last
                        
                        #deviation_buy1 = ma8_last / ma78_last
                        
                     
                    ):
                    
                        buy = "BUY #1- INCROCIO CLASSICO DURANTE IL RIBASSO"
                        action = "buy"
                    
                    
                    
                    
                    
                    
                    elif (
                        
                        ma78_last < ma78_20_min_ago
                        
                        and ( deviation_buy1 > 0.99 )
                        
                        #and ma39_last > ma50_last
                        #questa sta nel maddog che va molto bene durante i ribassi
                        
                        and ma8_last > ma50_last
                        
                        and price > price_2_min_ago
                        and ma2_last > ma2_2_min_ago
                        and ma4_last > ma4_2_min_ago
                        
                        
                        and ma4_last > ma8_last
                        
                        #deviation_buy1 = ma8_last / ma78_last
                        
                     
                    ):
                    
                        buy = "BUY #1-CON DEVIATION DURANTE IL RIBASSO"
                        action = "buy" 
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    ##############################################################################################################################
                    # IMPORTANTISSIMO ! SOLO PER IL BUY 1
                    ##############################################################################################################################

                    # PER COMPRARE DURANTE IL CROLLO - compa prega per me - ( cruise - david gilmour )
                    elif (
                         
                          price > price_2_min_ago
                          and ma2_last > ma2_2_min_ago
                          
                          
                          and ( deviation_buy1 < -2.40 and ma3_prev < ma15_prev and ma3_last > ma15_last ) or ( deviation_buy1 < -2.40 and deviation_buy_crollo > 0.39 )
                        
                          #and ma3_prev < ma8_prev and ma3_last > ma8_last or ( deviation_buy_crollo > 0.39 )
                          #questa ha fatto comprare NON DURANTE UN CROLLO.
                          #COSI' HO LEGATO deviation_buy_crollo > 0.39 al crollo vero e proprio (deviation_buy1 < -1.90)
                     
                    ):
                        buy = "BUY #1- DURANTE IL CROLLO"
                        action = "buy"
                    
                    
##############################################################################################################################
                
    
                # COMPRA sessione 2
        
                elif self.session == 2:
              
                    if (
                       
                        deviation_ma3_sopra_ma40 > 0.12
                        
                        and (( ma4_prev < ma9_prev and ma4_last > ma9_last ) and deviation_buy_ma4 > 0.12 ) or (deviation_buy2 > 0.12 and deviation_buy_ma4 > 0.12 and deviation_prev > 0.22 )
                        #deviation_buy_ma4 = ma4_last / last_trade_price
                        #deviation_buy = ma2_last / last_trade_price SCHIZZA IN ALTO TROPPO VELOCEMENTE QUASI COME IL PREZZO
                        #deviation_buy2 = ma8_last / ma78_last
                        
                        
                        and ma25_last > ma25_2_min_ago
                        #ma8>ma78
                        #punto verde dall' ultimo punto rosso (ma3-last trade)
                        #punto verde dall' ultimo punto verde
                       
                        and ma2_last > ma2_2_min_ago
                        and price > price_2_min_ago
                        
                        and ma4_last > ma78_last
                        
                        #and ma39_last > ma39_42_min_ago
                        and ma3_last > ma40_last
                        #incredibile ma vero E' NECESSARIA quando deve ricomprare dopo la correzione al ribasso
                        
                    ):
                        buy = "BUY #2-A"
                        action = "buy"

                       
                    
                    
                        
                    elif (
                          
                          deviation_ma3_sopra_ma40 > 0.12
                          
                          and (( ma4_prev < ma9_prev and ma4_last > ma9_last ) and deviation_buy_ma4 > 0.12 ) or ( deviation_buy2 > 0.15 and deviation_buy_ma4 > 0.16 )
                          #deviation_buy_ma4 = ma4_last / last_trade_price
                          #deviation_buy = ma2_last / last_trade_price
                          #deviation_buy2 = ma8_last / ma78_last
                          
                          and ma25_last > ma25_2_min_ago
                          and ma4_last > ma78_last
                          
                          
                          
                         
                          and ma2_last > ma2_2_min_ago
                          and price > price_1_min_ago
                          and price > price_2_min_ago
                          
                          
                          and ma3_last > ma40_last
                          #incredibile ma vero E' NECESSARIA quando deve ricomprare dopo la correzione al ribasso
                          
                          #and ma39_last > ma39_42_min_ago
                        
                         
                    ):
                        buy = "BUY #2-B"
                        action = "buy"
                    
#############################################################################################################################################



                # COMPRA sessione 3 in poi
    
                #elif self.session == 3:
                # CON " elif self.session == 3: " NON COMPRAVA PIU' ALLORA HO PRESO ELSE DA MADDOG CHE INVECE ANDAVA BENE
        
                else:
                    if (
                        
                        deviation_ma3_sopra_ma40 > 0.12
                        
                        and (( ma4_prev < ma9_prev and ma4_last > ma9_last ) and deviation_buy_ma4 > 0.12 ) or (deviation_buy3 > 0.13 and deviation_buy_ma4 > 0.15 and deviation_prev > 0.20 )
                        
                        #deviation_buy_ma4 = ma4_last / last_trade_price
                        #deviation_buy = ma2_last / last_trade_price
                        #deviation_buy3 = ma8_last / ma78_last
                       
                        and ma4_last > ma78_last
                        and ma13_last > ma13_2_min_ago
                        and ma2_last >= ma4_last
                        and price > price_2_min_ago
                        and ma3_last > ma6_last
                        and ma2_last > ma50_last
                        and ma2_last > ma78_last
                        
                        #and ma39_last > ma39_2_min_ago
                        #and price > price_3_min_ago
                        #and ma2_last > ma2_2_min_ago
                        
                        #and ma39_last > ma39_42_min_ago
                        
                        
                        #deviation_buy3 = ma8_last / ma78_last
                        #deviation_buy = ma2_last / last_trade_price
                        #deviation_prev = price / prev_trade_price  
                    
                    ):
                        buy = "BUY #3-A"
                        action = "buy"

                        
                        
                    elif (
                        
                          deviation_ma3_sopra_ma40 > 0.12
                          
                          and (( ma3_prev < ma8_prev and ma3_last > ma8_last ) and deviation_buy_ma4 > 0.15 ) or (deviation_buy3 > 0.12 and deviation_buy_ma4 > 0.16 )
                          #deviation_buy_ma4 = ma4_last / last_trade_price
                          #deviation_buy = ma2_last / last_trade_price
                          #deviation_buy3 = ma8_last / ma78_last
                        
                        
                          
                          and ma39_last < ma39_2_min_ago
                          and ma3_last > ma40_last
                          and ma2_last >= ma4_last
                          and ma2_last > ma50_last
                          and ma2_last > ma78_last
                          and ma4_last > ma78_last
                          and ma6_last > ma6_2_min_ago
                          and ma3_last > ma6_last
                          
                          #and price > price_2_min_ago
                          #and price > price_3_min_ago
                          #and ma2_last > ma2_2_min_ago
                          
                          #and ma13_last > ma13_2_min_ago
                       
                          #and ma39_last > ma39_42_min_ago
                        
                          #deviation_buy3 = ma8_last / ma78_last
                          #deviation_buy = ma2_last / last_trade_price
                          #deviation_prev = price / prev_trade_price
                          
                    ):
                        buy = "BUY #3-B"
                        action = "buy"
                        
        
        
        
        #############################################################################################################################################################            
        #############################################################################################################################################################
        
        
        
        # VENDITA
        
        # NON TOCCARE QUESTA CONDIZIONE (QUESTA DICE CHE STA IN MODO SELL, DEVO VENDERE)
        elif last_trade_action == "buy":

            self.algo_helper.log("ma2_prev: {}".format(ma2_prev))
            self.algo_helper.log("ma7_prev: {}".format(ma7_prev))
            self.algo_helper.log("ma2_last: {}".format(ma2_last))
            self.algo_helper.log("ma7_last: {}".format(ma7_last))
            self.algo_helper.log("deviation_sell: {}".format(deviation_sell))
            self.algo_helper.log("session: {}".format(self.session))

            ##################################################################################

            # VENDITA 1 - con fasce di tempo ! c'e' vita su marte !

            #    minuti
            #   0 -  3 ----------  fatto - e' quello che sta dando qualche problemino. INVECE DI DIRE ma3 < ma 25 FACCIO "incrocio dall' alto"  ma3 - ma25
            #   3 -  5 ----------- fatto
            #   5 - 12 ----------- 
            
            #  12 - 18 -----------
            #  18 - 40 -----------
            #   > 40   ----------- fatto
            
            #avevo messo incrocio 4-8 and deviation_sell < -0.20 per vendere durante il crollo - non dimenticarlo
                
            
            
            
            
            ###############################################################################################################################################################          0 -3 min

            # VENDITA - da 0 a 3 minuti = da 0 a 180 secondi

            if seconds_since_last_trade > 0 and seconds_since_last_trade <= 180:
                
                if (
                    #( ma50_last >= ma50_2_min_ago and ( ma3_last > ma30_last and ma3_last < ma30_last ) and deviation_sell > 0.18 ) or ( ma50_last >= ma50_2_min_ago and ( ma2_last > ma18_last and ma2_last < ma18_last ) and deviation_sell > 0.80 ) or ( ma50_last >= ma50_2_min_ago and ( ma3_last > ma78_last and ma3_last < ma78_last ) and deviation_sell < -0.20 ) 
                    #ma2_last < ma2_2_min_ago
                    
                    
                    ( ma50_last >= ma50_2_min_ago and ( ma3_last > ma30_last and ma3_last < ma30_last ) and deviation_sell > 0.18 ) or ( ma50_last >= ma50_2_min_ago and ( ma3_last > ma50_last and ma3_last < ma50_last )
                    #deviation_sell = ma2_last / last_trade_price
                   
                )):
                   
                    sell = " SELL #1 (0-3 min) con ma50 > "
                    action = "sell"
                    
                
                
                
                
                elif (
                   
                    
                    ( ma50_last >= ma50_2_min_ago and ( ma2_last > ma13_last and ma2_last < ma13_last ) and deviation_sell > 0.80 )
                    #deviation_sell = ma2_last / last_trade_price
                   
                ):
                   
                    sell = " SELL #2 (0-3 min) con ma50 > "
                    action = "sell"
                    
                 
                
                
                    
                elif (
                   
                    
                    ( ma50_last >= ma50_2_min_ago and ( ma3_last > ma78_last and ma3_last < ma78_last ) and deviation_sell < -0.20 ) 
                    #deviation_sell = ma2_last / last_trade_price
                   
                ):
                   
                    sell = " SELL #3 (0-3 min) con ma50 > "
                    action = "sell"
                    
                    
                    
            ###################################################################################################        
                    
                    
                elif (
                    
                    #ma2_last < ma2_2_min_ago
                    ( ma50_last >= ma50_2_min_ago and deviation_sell < -0.45 )
                    #deviation_sell = ma2_last / last_trade_price
                 
                ):
                   
                    sell = " SELL #4 (0-3 min) con ma50 > "
                    action = "sell"
                    
                
                
           #################################################################################################################################################################     
                
                
                
                
                
                elif (
                    
                    #( ma50_last < ma50_2_min_ago and ( ma3_last > ma16_last and ma3_last < ma16_last ) and deviation_sell > 0.23 ) or ( ma50_last < ma50_2_min_ago and ( ma3_last > ma8_last and ma3_last < ma8_last ) and deviation_sell > 0.60 ) or ( ma50_last < ma50_2_min_ago and ( ma3_last > ma78_last and ma3_last < ma78_last ) and deviation_sell < -0.20 ) 
                    
                    
                    ( ma50_last < ma50_2_min_ago and ( ma3_last > ma18_last and ma3_last < ma16_last ) and deviation_sell > 0.23 ) or ( ma50_last < ma50_2_min_ago and ( ma3_last > ma8_last and ma3_last < ma8_last ) and deviation_sell > 0.60 ) or ( ma50_last < ma50_2_min_ago and ( ma3_last > ma78_last and ma3_last < ma78_last ) and deviation_sell < -0.20 ) 
                  
                ):
                   
                    sell = " SELL #5 (0-3 min) con ma50 < "
                    action = "sell"
                    
                
                
                
                
                elif (
                    
                    ( ma50_last < ma50_2_min_ago and ( ma3_last > ma8_last and ma3_last < ma8_last ) and deviation_sell > 0.60 )
                  
                ):
                   
                    sell = " SELL #6 (0-3 min) con ma50 <  "
                    action = "sell"
                    
                    
                    
                    
                    
                    
                elif (
                    
                    ( ma50_last < ma50_2_min_ago and ( ma3_last > ma78_last and ma3_last < ma78_last ) and deviation_sell < -0.20 )
                  
                ):
                   
                    sell = " SELL #7 (0-3 min) con ma50 < "
                    action = "sell"
                    
                    
                    
                    
                    
                    
            elif (
                    
                    #ma2_last < ma2_2_min_ago
                    ( ma50_last < ma50_2_min_ago and deviation_sell < -0.45 )
                    
                    #deviation_sell =  ma3_last / last_trade_price
                    
                   
                ):
                   
                    sell = " SELL #8 (0-3 min) con ma50 < "
                    action = "sell"   
                    
                    
                    
         #################################################################################################################################################################          3-5 min           
         #################################################################################################################################################################
        
        
            # VENDITA - da 3 a 5 minuti = da 180 a 300 secondi

            elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 300:

                
                if (
                    
                    #ma2_last < ma2_2_min_ago
                    ( ma50_last >= ma50_2_min_ago and ( ma3_last < ma25_last and deviation_sell > 0.18 )) or ( ma50_last >= ma50_2_min_ago and ( ma2_last < ma18_last and deviation_sell > 0.80 )) or ( ma50_last >= ma50_2_min_ago and ( ma3_last > ma78_last and ma3_last < ma78_last ) and deviation_sell < -0.20 ) or ( ma50_last >= ma50_2_min_ago and ( ma3_last > ma50_last and ma3_last < ma50_last )
                    
                    #deviation_sell = ma2_last / last_trade_price
                    
                    #and ma13_last > ma13_2_min_ago

                    
                )):
                    sell = " SELL #9 (3-5 min) con ma50 > "
                    action = "sell"

                
                
                
                
                elif (
                    #ma2_last < ma2_2_min_ago
                    ( ma50_last >= ma50_2_min_ago and deviation_sell < -0.45 )
                    
                    #deviation_sell = ma2_last / last_trade_price
                 
                ):
                    sell = " SELL #10 (3-5 min) con ma50 > "
                    action = "sell"
                    
                    
                
                
                elif (
                    
                    #ma2_last < ma2_2_min_ago
                    ( ma50_last < ma50_2_min_ago and ( ma3_last < ma18_last and deviation_sell > 0.23 ))  or ( ma50_last < ma50_2_min_ago and ( ma3_last > ma78_last and ma3_last < ma78_last ) and deviation_sell < -0.20 )
                    #or ( ma50_last < ma50_2_min_ago and ( ma3_last < ma8_last and deviation_sell > 0.60 )) vendeva mentre risaliva
                    #deviation_sell = ma2_last / last_trade_price
                   
                    
                ):
                    sell = " SELL #11 (3-5 min) con ma50 < "
                    action = "sell"
                    
                    
                
                    
                elif (
                    
                    #ma2_last < ma2_2_min_ago
                    ( ma50_last < ma50_2_min_ago and deviation_sell < -0.45 )
                    
                    #deviation_sell = ma2_last / last_trade_price
                    # or ( ma50_last < ma50_2_min_ago and deviation_buy1 < -0.20 ) QUESTA ERA LA COLPEVOLE CHE FACEVA VENDERE MENTRE RISALIVA DOPO IL CROLLO !
                    
                   
                ):
                   
                    sell = " SELL #12 (3-5 min) con ma50 < "
                    action = "sell"   
                    
                    
                    
                    
            ############################################################################################################################################################### 5-12 min         
                
            # VENDITA - da 5 a 12 minuti = da 300 a 720 secondi

            elif seconds_since_last_trade > 300 and seconds_since_last_trade <= 720:
                
                
                

                if (
                    
                    #ma2_last < ma2_2_min_ago
                    
                    ( ma50_last >= ma50_2_min_ago and ( ma3_last < ma25_last and deviation_sell > 0.18 )) or ( ma50_last >= ma50_2_min_ago and ( ma2_last < ma18_last and deviation_sell > 0.80 )) or ( ma50_last >= ma50_2_min_ago and ( ma3_last > ma78_last and ma3_last < ma78_last )) and ( ma50_last >= ma50_2_min_ago and deviation_sell < -0.20 ) or ( ma50_last >= ma50_2_min_ago and ( ma3_last > ma50_last and ma3_last < ma50_last ) 
                    #deviation_sell = ma2_last / last_trade_price
                   
                    
                )):
                    sell = " SELL #13 (5-12 min) con ma50 > "
                    action = "sell"
                    
             
                    
                elif (
                    
                    #ma2_last < ma2_2_min_ago
                    ( ma50_last >= ma50_2_min_ago and deviation_sell < -0.59 )
                    #deviation_sell = ma2_last / last_trade_price
                    
                    
                    
                    
                ):
                    sell = " SELL #14 (5-12 min) con ma50 > "
                    action = "sell"
                    
                    
                    
                elif (
                    
                    #ma2_last < ma2_2_min_ago
                    ( ma50_last < ma50_2_min_ago and ( ma3_last < ma18_last and deviation_sell > 0.23 ))  or ( ma50_last < ma50_2_min_ago and ( ma3_last > ma78_last and ma3_last < ma78_last ) and deviation_sell < -0.20 )
                    #or ( ma50_last < ma50_2_min_ago and ( ma3_last < ma8_last and deviation_sell > 0.60 )) vendeva mentre risaliva dal crollo
                    #deviation_sell = ma2_last / last_trade_price
                    
                    
                ):
                    sell = " SELL #15 (5-12 min) con ma50 < "
                    action = "sell"
                    
                    
                    
                
                    
                elif (
                    
                    #ma2_last < ma2_2_min_ago
                    ( ma50_last < ma50_2_min_ago and deviation_sell < -0.45 )
                    
                    #deviation_sell = ma2_last / last_trade_price
                    
                   
                    
                   
                ):
                   
                    sell = " SELL #16 (5-12 min) con ma50 < "
                    action = "sell"   
                    
                
            
            ########################################################################################################################################################     12-18 min
            
            

            
            # VENDITA - da 12 a 24 minuti = da 720 a 1440 secondi - attenzione da qua in poi e' rimasto "ma2_last < ma2_2_min_ago" che forse dovrai togliere
            
            elif seconds_since_last_trade > 720 and seconds_since_last_trade <= 1440:
                
                
                
                
                if (
                    
                    
                    #ma2_last < ma2_2_min_ago
                    ( ma50_last >= ma50_2_min_ago and ( ma3_last < ma25_last and deviation_sell > 0.18 )) or ( ma50_last >= ma50_2_min_ago and ( ma2_last < ma18_last and deviation_sell > 0.80 )) or ( ma50_last >= ma50_2_min_ago and ( ma3_last > ma78_last and ma3_last < ma78_last )) and ( ma50_last >= ma50_2_min_ago and deviation_sell < -0.20 ) or ( ma50_last >= ma50_2_min_ago and ( ma3_last > ma50_last and ma3_last < ma50_last )
                    #deviation_sell = ma2_last / last_trade_price
                    
                    
                  
                    
                )):
                    sell = " SELL #17 (12-24 min) con ma50 > "
                    action = "sell"
                    
                
                
                
                elif (
                    
                    
                    ( ma50_last >= ma50_2_min_ago and deviation_sell < -0.45 )
                    
                    #deviation_sell = ma2_last / last_trade_price
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                ):
                    sell = " SELL #18 (12-24 min) con ma50 >  "
                    action = "sell"
                    
                
                
                
                elif (
                    
                    #ma2_last < ma2_2_min_ago
                    ( ma50_last < ma50_2_min_ago and ( ma3_last < ma18_last and deviation_sell > 0.23 )) or ( ma50_last < ma50_2_min_ago and ( ma3_last > ma78_last and ma3_last < ma78_last )) and ( ma50_last < ma50_2_min_ago and deviation_sell < -0.20 )
                    #or ( ma50_last < ma50_2_min_ago and ( ma3_last < ma8_last and deviation_sell > 0.60 )) faceva vendere mentre risaliva dal crollo
                    #deviation_sell = ma2_last / last_trade_price
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    
                    
                ):
                    sell = " SELL #19 (12-24 min) con ma50 <  "
                    action = "sell"
                    
                    
                    
                
                    
                elif (
                    
                    #ma2_last < ma2_2_min_ago
                    ( ma50_last < ma50_2_min_ago and deviation_sell < -0.45 )
                    
                    #deviation_sell = ma2_last / last_trade_price
                    
                    
                     
                   
                ):
                   
                    sell = " SELL #20 (12-24 min) con ma50 < "
                    action = "sell"
                    
                    
                    
                    
            ################################################################################################################################################################### 24-40 min
            
            
            # VENDITA - da 24 a 40 minuti = da 1080 a 1800 secondi

            elif seconds_since_last_trade > 1440 and seconds_since_last_trade <= 2400:
                
                
            
                if (
                    
                    #ma2_last < ma2_2_min_ago
                    ( ma50_last >= ma50_2_min_ago and ( ma3_last < ma25_last and deviation_sell > 0.18 )) or ( ma50_last >= ma50_2_min_ago and ( ma2_last < ma18_last and deviation_sell > 0.80 )) or ( ma50_last >= ma50_2_min_ago and ( ma3_last > ma78_last and ma3_last < ma78_last ) and deviation_sell < -0.20 ) or ( ma50_last >= ma50_2_min_ago and ( ma3_last > ma50_last and ma3_last < ma50_last )
                    #deviation_sell = ma2_last / last_trade_price
                 
                )):
                    sell = " SELL #21 (24-40 min) con ma50 > "
                    action = "sell"
                
                
                
                elif (
                    
                    
                    ( ma50_last >= ma50_2_min_ago and deviation_sell < -0.45 )
                    
                    #deviation_sell = ma2_last / last_trade_price
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                ):
                    sell = " SELL #22 (24-40 min) con ma50 > "
                    action = "sell"
                    
                
                
                
                elif (
                    
                    #ma2_last < ma2_2_min_ago
                    ( ma50_last < ma50_2_min_ago and ( ma3_last < ma18_last and deviation_sell > 0.23 )) or ( ma50_last < ma50_2_min_ago and ( ma3_last > ma78_last and ma3_last < ma78_last ) and deviation_sell < -0.20 )
                    #or ( ma50_last < ma50_2_min_ago and ( ma3_last < ma8_last and deviation_sell > 0.60 )) faceva vendere mentre risaliva dal crollo
                    #deviation_sell = ma2_last / last_trade_price
                  
                ):
                    sell = " SELL #23  (24-40 min) con ma50 < "
                    action = "sell"
                    
                    
                    
                    
               
                    
                elif (
                    
                    #ma2_last < ma2_2_min_ago
                    ( ma50_last < ma50_2_min_ago and deviation_sell < -0.45 )
                    #deviation_sell = ma2_last / last_trade_price
                    
                    
                    #avevo messo 4-8 per vendere durante il crollo - non dimenticarlo
                    #and ma4_last < ma8_last and deviation_sell < -0.20
                  
                ):
                   
                    sell = " SELL #24 (24-40 min) con ma50 < "
                    action = "sell"   
                       
                 
                
                
            ############################################################################################################################################################      > 40 min
            
            
            # VENDITA - da 40 minuti in poi = da 2400 secondi in poi

            elif seconds_since_last_trade > 2400:
               
                
                if (
                    
                    ma2_last < ma2_2_min_ago
                    and ( ma50_last >= ma50_2_min_ago and ( ma3_last < ma25_last and deviation_sell > 0.18 )) or ( ma50_last >= ma50_2_min_ago and ( ma2_last < ma13_last and deviation_sell > 0.60 )) or ( ma50_last >= ma50_2_min_ago and ( ma3_last > ma78_last and ma3_last < ma78_last ) and deviation_sell < -0.20 ) or ( ma50_last >= ma50_2_min_ago and ( ma3_last > ma50_last and ma3_last < ma50_last )
                    #deviation_sell = ma2_last / last_trade_price
                    
                )):
                  
                    sell = " SELL #25 ( dopo 40 min ) con ma50 > "
                    action = "sell"
                    
                
                    
                elif (
                    
                    ( ma50_last >= ma50_2_min_ago and deviation_sell < -0.45 )
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                 
                ):
                    sell = " SELL #26 ( dopo 40 min ) con ma50 > "
                    action = "sell"
                    
                    
                elif (
                    
                    ( ma50_last < ma50_2_min_ago and ( ma3_last < ma18_last and deviation_sell > 0.23 )) or (( ma3_last > ma78_last and ma3_last < ma78_last ) and deviation_sell < -0.20 )
                    
                    #or ( ma3_last < ma8_last and deviation_sell > 0.60 ) faceva vendere nella risalita dal crollo
                    #deviation_sell = ma2_last / last_trade_price
                   
                    and ma2_last < ma2_2_min_ago
                   
                    
                ):
                    sell = " SELL #27 ( dopo 40 min ) con ma50 < "
                    action = "sell"
                    
                  
                
                elif (
                    ma2_last < ma2_2_min_ago
                    and ( ma50_last < ma50_2_min_ago and deviation_sell < -0.45 )
                    
                    #deviation_sell = ma2_last / last_trade_price
                   
                   
                ):
                   
                    sell = " SELL #28 ( dopo 40 min ) con ma50 < "
                    action = "sell"   
                       
                    
                  
            ################################################################################################################################## 
            
            # salvagente solo mentre sale !

            #1) STOP LOSS (salvagente)  
            # se ma78_last < ma78_2_min_ago si aziona lo stop loss in un modo !
            # se ma78_last > ma78_2_min_ago si aziona lo stop loss in un altro modo !
            
            if (
                ( ma50_last >= ma50_2_min_ago and ( ma2_last < ma36_last and deviation_sell < -0.68 )) or ( ma50_last >= ma50_2_min_ago and ma2_last < ma36_last and deviation_sell < -0.63 ) or ( ma50_last >= ma50_2_min_ago and ma8_last < ma39_last and deviation_sell < -0.45 )
                
           
            ):
                sell = " SELL # SALVAGENTE 1 "
                action = "sell"
                
            #######################################################################################################################################################    
            
            
            elif (
            
                ( ma50_last >= ma50_2_min_ago and ( ma2_last < ma36_last and deviation_sell < -0.50 )) or ( ma50_last >= ma50_2_min_ago and ( ma8_last < ma39_last and deviation_sell < -0.48 )) 
                
                #or ( deviation_sell_ma78 < -0.43 )
                #ha venduto anche questa durante il crollo - punto rosso sovrapposto al punto verde 
                # e gli ho detto che and ma3 deve andare sotto ma13 per vendere .
                #vediamo
            ):
                sell = " SELL # SALVAGENTE 2 "
                action = "sell"  
            
            
            #########################################################################################################################################################
           

            #2) ro cano VENDE " DOPO x MINUTI " "max hold time" riga 91
                # HA VENDUTO DOPO 20 MINUTI !
            elif (
                
                ma2_last > ma2_2_min_ago
                and ( seconds_since_last_trade > max_hold_time_in_seconds and ( ma2_last < ma78_last and deviation_sell < -0.40 )) or ( deviation_sell < 0.15 and seconds_since_last_trade > max_hold_time_in_seconds )
                 
                

                
                #deviation_sell = ma2_last / last_trade_price
            ):
                sell = " SELL # TEMPO 1 "
                action = "sell"
                
                
                
                
            elif (
                
                ma2_last > ma2_2_min_ago
                and ( seconds_since_last_trade > max_hold_time_in_seconds and ( ma78_last > ma78_2_min_ago and ma2_last < ma78_last ) and deviation_sell < -0.55 ) or ( seconds_since_last_trade > max_hold_time_in_seconds and deviation_sell < 0.10 )
                
                
                  
                
                #deviation_sell = ma2_last / last_trade_price
            ):
                sell = " SELL # TEMPO 2 "
                action = "sell"
                
                
                
            #################################################################################################################################    
               
            
            
            elif (
                
                ma2_last < ma2_2_min_ago
                and ( ma50_last >= ma50_2_min_ago and ma4_last < ma8_last and deviation_sell < -0.55 )
                
                
                
            ):    
                sell = " SELL # ALTRO SALVAGENTE "
                action = "sell"
                
                
                
            ####################################################################################################################################
            
            
            # se diminuisce la forza - al momento disattivato
            
            #elif (
                
                #ma2_last < ma36_last 
                #and deviation_sell < -0.50
            #):    
                #action = "sell"
                
                
           
        
        
        

        ############### FINE ALGORITH ###################
        
        

        self.algo_helper.log("action {}".format(action))

        if action == "sell":
            self.algo_helper.log("action sell {}".format(sell))
            self.session += 1
        elif action == 'buy':
            self.algo_helper.log("action buy {}".format(buy))

        return action

        # ave comparo meo ! ###### ######
        # compa caro #
        # comparo de dio ###
        # gloria al mio compare ######
        
