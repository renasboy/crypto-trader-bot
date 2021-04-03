

class ro_cano_che_ritorna:
    def __init__(self, helper):
        self.algo_helper = helper
        self.session = 0
        self.open = False

    @property
    def action(self):

        # moving average (2-3-4-5-x)
        
        ma1_last, ma1_prev = self.algo_helper.ma_last_prev(1)
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
        ma12_last, ma12_prev = self.algo_helper.ma_last_prev(12)
        ma13_last, ma13_prev = self.algo_helper.ma_last_prev(13)
        ma14_last, ma14_prev = self.algo_helper.ma_last_prev(14)
        ma15_last, ma15_prev = self.algo_helper.ma_last_prev(15)
        ma16_last, ma16_prev = self.algo_helper.ma_last_prev(16)
        ma17_last, ma17_prev = self.algo_helper.ma_last_prev(17)
        ma18_last, ma18_prev = self.algo_helper.ma_last_prev(18)
        ma20_last, ma20_prev = self.algo_helper.ma_last_prev(20)
        ma21_last, ma21_prev = self.algo_helper.ma_last_prev(21)
        ma22_last, ma22_prev = self.algo_helper.ma_last_prev(22)
        ma24_last, ma24_prev = self.algo_helper.ma_last_prev(24)
        ma25_last, ma25_prev = self.algo_helper.ma_last_prev(25)
        ma28_last, ma28_prev = self.algo_helper.ma_last_prev(28)
        ma30_last, ma30_prev = self.algo_helper.ma_last_prev(30)
        ma32_last, ma32_prev = self.algo_helper.ma_last_prev(32)
        ma34_last, ma34_prev = self.algo_helper.ma_last_prev(34)
        ma36_last, ma36_prev = self.algo_helper.ma_last_prev(36)
        ma38_last, ma38_prev = self.algo_helper.ma_last_prev(38)
        ma39_last, ma39_prev = self.algo_helper.ma_last_prev(39)
        ma40_last, ma40_prev = self.algo_helper.ma_last_prev(40)
        ma50_last, ma50_prev = self.algo_helper.ma_last_prev(50)
        ma54_last, ma54_prev = self.algo_helper.ma_last_prev(54)
        ma60_last, ma60_prev = self.algo_helper.ma_last_prev(60)
        ma85_last, ma85_prev = self.algo_helper.ma_last_prev(85)
        ma78_last, ma78_prev = self.algo_helper.ma_last_prev(78)
        ma100_last, ma100_prev = self.algo_helper.ma_last_prev(100)
        ma110_last, ma110_prev = self.algo_helper.ma_last_prev(110)
        

        # moving average (2-3-4-5-7-8-20-43-100) di x minuti prima
        
        ma2_2_min_ago = self.algo_helper.ma_minutes_ago(2, 2)
        ma2_3_min_ago = self.algo_helper.ma_minutes_ago(2, 3)
        ma2_15_min_ago = self.algo_helper.ma_minutes_ago(2, 15)
        ma2_17_min_ago = self.algo_helper.ma_minutes_ago(2, 17)
        ma2_22_min_ago = self.algo_helper.ma_minutes_ago(2, 22)
        ma2_24_min_ago = self.algo_helper.ma_minutes_ago(2, 24)
        
        ma3_2_min_ago = self.algo_helper.ma_minutes_ago(3, 2)
        ma3_3_min_ago = self.algo_helper.ma_minutes_ago(3, 3)
        ma3_5_min_ago = self.algo_helper.ma_minutes_ago(3, 5)
        
        ma4_2_min_ago = self.algo_helper.ma_minutes_ago(4, 2)
        ma8_5_min_ago = self.algo_helper.ma_minutes_ago(8, 5)
        ma10_2_min_ago = self.algo_helper.ma_minutes_ago(10, 2)
        ma14_2_min_ago = self.algo_helper.ma_minutes_ago(14, 2)
        ma32_3_min_ago = self.algo_helper.ma_minutes_ago(32, 3)
        ma33_3_min_ago = self.algo_helper.ma_minutes_ago(33, 3)
        ma36_2_min_ago = self.algo_helper.ma_minutes_ago(36, 2)
        ma50_2_min_ago = self.algo_helper.ma_minutes_ago(50, 2)
        ma50_3_min_ago = self.algo_helper.ma_minutes_ago(50, 3)
        ma78_2_min_ago = self.algo_helper.ma_minutes_ago(78, 2)
        ma100_2_min_ago = self.algo_helper.ma_minutes_ago(100, 2)
        ma100_13_min_ago = self.algo_helper.ma_minutes_ago(100, 13)
        
        
        # LAST TRADE
        last_trade_action = self.algo_helper.last_trade_action
        last_trade_price = self.algo_helper.last_trade_price
        seconds_since_last_trade = self.algo_helper.seconds_since_last_trade
        

        ##############



        # PREV TRADE
        prev_trade_action = self.algo_helper.prev_trade_action
        prev_trade_time = self.algo_helper.prev_trade_time
        prev_trade_price = self.algo_helper.prev_trade_price
        seconds_since_prev_trade = self.algo_helper.seconds_since_prev_trade
        
        ###########################
        #########################################################################################################################################################
        
        # PREZZO DI ADESSO (di mercato) - CURRENT PRICE
        price = self.algo_helper.price
        
        
        
        # PREZZO DI "PRIMA" (di mercato) - PREV PRICE....................prova. vediamo se funziona - sembra di NO
        #prev_price = self.algo_helper.prev_price
        
        # PREZZO DI "DOPO" (di mercato) - LAST PRICE.....................prova. vediamo se funziona - sembra di NO
        #last_price = self.algo_helper.last_price
        
        ##########################################################################################################################################################
        #############################
        
        # PREZZO di X MINUTI FA (di mercato) - PREV PRICE
        price_1_min_ago = self.algo_helper.price_minutes_ago(1)
        price_2_min_ago = self.algo_helper.price_minutes_ago(2)
        price_3_min_ago = self.algo_helper.price_minutes_ago(3)
        price_5_min_ago = self.algo_helper.price_minutes_ago(5)
        
        
        #############################################################################################################################################################
        
        

        # VENDE DOPO 1800 secondi = 60 minuti ("e se") ro cano torna a casa
        max_hold_time_in_seconds = 3600

        # VENDE DOPO 600 secondi = 10 minuti ("e se") - ro cano perde la forza - riga 323
        max_hold_without_force_time_in_seconds = 600
        
        
        #############################################################################################################################################################
        
        
        
        # TEMPO in cui (PER COMPRARE) (a tutte le condizioni gia' attive) SI AGGIUNGE una condizione aggiuntiva LA DEVIATION !

        # dall' ULTIMO trade ( 15 minuti = 15 * 60 = 900 secondi )
        min_buy_delay_in_seconds = 900

        # dal PENULTIMO trade ( 20 minuti = 20 * 60 = 1800 secondi )
        min_prev_buy_delay_in_seconds = 1200

       ##############################################################################################################################################################
        
        
        
        
        
        
        # formula DEVIATION_buy per comprare UN PO' PIU' SOPRA DEL LAST TRADE ( di solito l' ultimo SELL ) 
        deviation_buy = (ma2_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.log("deviation_buy: {}".format(deviation_buy))
        
        #####################################################################################################################
        # formula DEVIATION_gabbia 
        deviation_gabbia = (ma6_last / ma38_last - 1) * 100 if ma38_last else 0
        self.algo_helper.log("deviation_gabbia: {}".format(deviation_gabbia))
        
        # formula DEVIATION_buy1 per comprare durante il TREND RIBASSISTA 
        deviation_buy1 = (ma6_last / ma38_last - 1) * 100 if ma38_last else 0
        self.algo_helper.log("deviation_buy1: {}".format(deviation_buy1))
        
        
        # formula DEVIATION_buy2 per la compra 2 
        deviation_buy2 = (ma8_last / ma78_last - 1) * 100 if ma78_last else 0
        self.algo_helper.log("deviation_buy2: {}".format(deviation_buy2))
        
        
        # formula DEVIATION_buy3 per la compra 3
        deviation_buy3 = (ma8_last / ma78_last - 1) * 100 if ma78_last else 0
        self.algo_helper.log("deviation_buy3: {}".format(deviation_buy3))
        
        ########################################################################################################################
        
        # formula DEVIATION_prev per comprare UN PO' PIU' SOPRA DEL PREV TRADE ( di solito l' ultimo BUY )
        deviation_prev = (price / prev_trade_price - 1) * 100 if prev_trade_price else 0
        self.algo_helper.log("deviation_prev: {}".format(deviation_prev))
      

        # formula DEVIATION_sell per vendere
        deviation_sell = (ma2_last / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.log("deviation_sell: {}".format(deviation_sell))

        

        # DEFAULT ACTION DICE DI NON FARE NIENTE (=None, NON TOCCARE)
        action = None

        
        
        ##########################################################################################################################################

        # APRE E CHIUDE GABBIA

        #si apriva la GABBIA se
      
        #condizione comparo meo - si apre la gabbia in 2 modi differenti !
        #if (ma36_last >= ma36_2_min_ago and ma8_last > ma14_last) or (ma36_last < ma36_2_min_ago and ma2_last > ma4_last):
        
        
        if ma50_last >= ma50_2_min_ago and deviation_gabbia > -0.15:
            #ti ricordo che deviation_gabbia = (ma6_last / ma38_last)
            
            # la gabbia continua ad essere aperta anche se trend ma50 si inclina un pochino verso il basso 
            # (o se per es il prezzo, come in precedenti versioni, va sotto la ma50 )
            #a questo punto la compra 2 deve essere piu' veloce (che vado a cambiare)
        
            
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
                    and deviation_buy > 0.01
                )
                
                # COMPRA UN PO' PIU' SOPRA DEL PENULTIMO TRADE SE deviation_prev > x nei 300 secondi ( qualche volta IL BUY)
                
                or (
                    seconds_since_prev_trade > 0
                    and seconds_since_prev_trade <= min_prev_buy_delay_in_seconds
                    and deviation_prev > 0.01
                )
                
                
                or (
                    seconds_since_last_trade == 0
                    or seconds_since_last_trade > min_buy_delay_in_seconds
                )
                
             ######################################################################
             ######################################################################
                
             # compa, forse qua manca deviation_ma
                
                # ma, domanda, vale per tutte le righe ? 
                # se voglio mettere deviation diverse ? ( se ma50 sale deviation diversa se ma50 scende ) 
                # ciao
                
                
            ):

###################################################################################################################################################
###################################################################################################################################################

                # COMPRA sessione 1
          
                if self.session == 1:
               
                    if (
                       
                        #se va su all' improvviso prende la deviation.
                        #se ci ripensa prima di salire prende l' incrocio
                        #GRAZIE COMPA
                        
                        price > price_2_min_ago
                        and price > price_3_min_ago
                        and ma8_prev < ma50_prev and ma6_last > ma60_last or deviation_buy1 > 0.19
                        
                        #roma 2 aprile 2021 - BUY 1
                        
                        
                        
                        # vedi grafico B -IL PREZZO NON SARA' PIU' ALT0 E NON COMPRERA' "LA PRIMA VOLTA" CHE INCROCIA AL RIALZO
                        
                        
                        #and ma4_prev < ma50_prev and ma4_last > ma50_last or deviation_buy1 > 0.195 DEVO PROVARE L' INCROCIO PERCHE' NON SONO SICURO CHE SI SIA ATTIVATO
                        #and ma4_prev < ma50_prev and ma4_last > ma50_last NON SEMPRE FA LA COMPRA NELLA SECONDA RISALITA
                        #ALLORA METTO ma7 - ma50 in modo tale che PRICE E' SCESO UN PO' E NON COMPRA NELLA PRIMA RISALITA
                        #and ma8_prev < ma50_prev and ma8_last > ma50_last
                        # 8-50 PRENDE NEL PRIMO ROUND MA non prende NEL SECONDO ROUND !
                        
                        #E' ARRIVATO IL MOMENTO DELL' INCROCIO ANTICLASSICO (8-50) (8-60)
                        #l' incrocio anticlassico (4-39) (4-50) sembra troppo PRECIPITOSO
                        
                        #AVE COMBARO MEO - HIGH HOPES - ROMA 30 MARZO 2021
                        #and ma8_prev < ma50_prev and ma8_last > ma60_last
                        
                        #OLE ALTRO INCROCIO ANTICLASSICO - VEDI SE FUNZIONA
                        #and ma8_prev < ma50_prev and ma6_last > ma60_last
                        
                        
                        #or deviation_buy1 > 0.19
                        #TIENITI PRONTA PER ANDARE SULLA RIGA 299
                        
                        
                        #deviation_buy1 > 0.18 or (ma24_prev < ma78_prev and ma24_last > ma78_last)
                        
                        
                        
                        #OPPURE
                        #deviation_buy1 > 0.18 or (ma7_prev < ma38_prev and ma7_last > ma38_last) 
                        #SARA' COSI' !
                        
                        # E forse dovrai aggiungere eventualmente and (ma3_last > ma39_last and ma12_last > ma12_2_min_ago)
                        
                        #oppure INCROCIO ANTICLASSICO
                        #ma4<ma38 and ma4>ma50 !
                        
                        
                        
                        
                        
                        
                        
                        #deviation_buy1 > 0.09
                        # ti ricordo che la deviation_ma = (ma4_last / ma38_last - 1) * 100
                        
                        #and (price_2_min_ago < ma3_2_min_ago and price < ma3_last) questa ha funzionato ! MA compra dopo 2 minuti che si incrociano al ribasso !
                        
                        #adesso proviamo questa
                        #and (price_2_min_ago < ma3_2_min_ago and price > ma3_last)anche questa ha funzionato! MA anche questa compra dopo 2 minuti che si incrociano al ribasso!
                        
                        #adesso proviamo questa
                        #and (price_3_min_ago < ma3_3_min_ago and price > ma3_last)
                        
                        #adesso proviamo questa
                        #and (price_5_min_ago < ma3_5_min_ago and price > ma3_last)
                        
                        #and (prev_price < ma3_2_min_ago and price > ma3_last)
                        #NON FUNZIONA. Ma non fa niente.
                        
                        #questa non ha comprato
                        #and (price_2_min_ago < ma3_2_min_ago and price < ma3_last and ma3_last > ma3_2_min_ago) 
                        
                        #and deviation_ma >= 0.23
                        #and (prev_price < ma3_prev and price > ma3_last)
                        
                        
                        
                        #ma50_last >= ma50_2_min_ago
                        #and ma2_last >= ma9_last
                        
                        #and ma36_last >= ma36_2_min_ago
                        #and ma8_last >= ma14_last
                        
                        
                        
                        #and (ma2_prev < ma3_prev and ma2_last > ma3_last) or (price_1_min_ago < ma3_prev and price > ma3_last)
                        #( e' un tentativo modesto di mettere incrocio (prev_price < ma3_prev and last_price > ma3_last)
                        
                        #( CHIEDI A COMPA, se hai il coraggio )
                        #( FUNZIONA ma compra dopo 1 minuto MENTRE SCENDE ! (dopo che si sono incrociati prezzo-ma3 al ribasso))
                        
                        #compra veloce e strano
                        #and (ma2_prev < ma3_prev and ma2_last > ma3_last) or (price_2_min_ago < ma3_2_min_ago and price > ma3_last)
                        
                        #mandrakata. vediamo disegno "strano 2 miracolo "
                        #and (price_1_min_ago > ma3_prev and price < ma3_last and ma3_last > ma3_2_min_ago) 
                        
                        #prova NON HA COMPRATO PROPRIO !
                        #and (prev_price < ma3_prev and last_price > ma3_last)
                        
                        #PROVO CON PRICE AL POSTO DI LAST_PRICE
                        #and (prev_price < ma3_prev and price > ma3_last)
                        
                        
                        
                        #and ma2_last > ma2_2_min_ago
                        #and ma2_last > ma2_3_min_ago
                        #and ma2_last >= ma7_last
                        #and ma4_last > ma4_2_min_ago
                        #and price > price_1_min_ago
                        
                    
                    ):
                        action = "buy"
                       

                        
                        
                    elif (
                          #porto al cane che ritorna il buy del maddog che e' molto bello (ma, attenzione, li la deviation e' 8-39)
                          #se va su all' improvviso prende la deviation.
                          #se ci ripensa prima di salire prende l' incrocio
                          #GRAZIE COMPA
                          
                          price > price_2_min_ago
                          and price > price_3_min_ago
                          and ma8_prev < ma50_prev and ma6_last > ma60_last or deviation_buy1 > 0.19
                        
                          #roma 2 aprile 2021 - BUY 1
                          
                        
                          
                          # vedi grafico B
                          
                          #and ma8_prev < ma50_prev and ma8_last > ma50_last
                        
                          #ECCO L' INCROCIO ANTICLASSICO - vediamo se funziona !
                          #and ma8_prev < ma50_prev and ma8_last > ma60_last
                          
                          #ALTRO INCROCIO ANTICLASSICO - vedi se funziona - funziona ma come al solito l' incrocio ha il problema che non prende sempre 
                          #and ma8_prev < ma50_prev and ma6_last > ma60_last


                          #and ma4_prev < ma50_prev and ma4_last > ma50_last VEDI BUY 1 SOPRA
                          #and ma4_prev < ma50_prev and ma4_last > ma50_last or deviation_buy1 > 0.195
                          
                          
                          #or deviation_buy1 > 0.19
                          #TIENITI PRONTA PER ANDARE SULLA RIGA 410
                          
                          #deviation_buy1 > 0.17 or (ma24_prev < ma78_prev and ma24_last > ma78_last) 
                          #SARA' COSI' !
                          
                          #forse dovrai aggiungere eventualmente and ma3_last > ma39_last and ma12_last > ma12_2_min_ago) 
                          
                          # avevo studiato or (deviation_buy1 < -2.9 and ma2_last > ma4_last) per i grandi ribassi
                        
                        
                        
                        
                          # ti ricordo che la deviation_buy1 = (ma4_last / ma38_last - 1) * 100


                        
                          #and (price_2_min_ago < ma3_2_min_ago and price < ma3_last) questa ha funzionato MA compra dopo 2 minuti che si incrociano al ribasso !
                          
                          #ma adesso proviamo questa
                          #and (price_2_min_ago < ma3_2_min_ago and price > ma3_last)anche questa ha funzionato ! MA anche questa compra dopo 2 minuti che si incrociano al ribasso !
                          
                          #and (price_3_min_ago < ma3_3_min_ago and price > ma3_last)
                          
                          #adesso proviamo questa
                          #and (price_5_min_ago < ma3_5_min_ago and price > ma3_last)
                          
                          #and (prev_price < ma3_2_min_ago and price > ma3_last)
                        
                        
                        
                          #and (price_2_min_ago < ma3_2_min_ago and price < ma3_last and ma3_last > ma3_2_min_ago) 
                          
                          
                          #prev_price < ma3_prev and price > ma3_last
                          #ma50_last < ma50_2_min_ago
                          #and ma2_last >= ma9_last
                        
                          #and ma36_last < ma36_2_min_ago
                          #and ma8_last > ma14_last
                        
                          
                          
                          #compra veloce
                          #and (price_2_min_ago < ma3_2_min_ago and price > ma3_last)
                          
                          #mandrakata. vediamo disegno "strano 2 miracolo "
                          #and (price_1_min_ago > ma3_prev and price < ma3_last and ma3_last > ma3_2_min_ago) 
                          
                          #prova non ha comprato proprio !
                          #and (prev_price < ma3_prev and last_price > ma3_last)
                          
                          #PROVO CON PRICE AL POSTO DI LAST_PRICE
                          
                          
                        
                          
                        
                          #and ma2_last > ma2_2_min_ago
                          #and ma2_last > ma7_last
                          #and ma4_last > ma4_2_min_ago
                        
                          #and price > price_1_min_ago
                          #and price > price_2_min_ago
                          #and price > price_3_min_ago
                 
                    ):

                        action = "buy"
                    
                    
##############################################################################################################################
##############################################################################################################################                       
    

    
                # COMPRA sessione 2
        
                elif self.session == 2:
              
                    if (
                        
                        #ma50_last >= ma50_2_min_ago
                        #and ma2_last >= ma9_last
                        
                        #and ma2_prev < ma3_prev and ma2_last > ma3_last
                        #and (ma2_prev < ma3_prev and ma2_last > ma3_last) or (price_2_min_ago < ma3_2_min_ago and price > ma3_last)
                        
                        #mandrakata. vediamo disegno "strano 2 miracolo "
                        #and (price_1_min_ago > ma3_prev and price < ma3_last and ma3_last > ma3_2_min_ago) 
                        
                        #and ma36_last >= ma36_2_min_ago
                        #and ma8_last >= ma14_last
                        
                        deviation_buy2 >= 0.15
                        # ma8>ma78
                        
                        and deviation_buy > 0.16
                        #punto verde dall' ultimo punto rosso (ma3-last trade)
                        
                        and deviation_prev > 0.14
                        #punto verde dall' ultimo punto verde
                        
                        #deviation_buy2 > 0.15 or (ma5_prev < ma36_prev and ma5_last > ma36_last and ma3_last > ma39_last and ma12_last > ma12_2_min_ago) 
                        #SARA' COSI' !
                        
                        
                        and ma2_last > ma2_2_min_ago
                        and price > price_1_min_ago
                        and price > price_2_min_ago
                        
                        #and ma2_last > ma7_last
                        #and ma2_last > ma2_2_min_ago
                        #and ma4_last > ma4_2_min_ago
                        
                        and ma3_last > ma40_last
                        #incredibile ma vero E' NECESSARIA quando deve ricomprare dopo la correzione al ribasso
                        
                        
                       
                 
                    ):

                        action = "buy"

                        
                        
                    elif (
                          
                          #ma50_last < ma50_2_min_ago
                          #and ma2_last >= ma9_last
                          
                          #and ma2_prev < ma3_prev and ma2_last > ma3_last
                          #and (ma2_prev < ma4_prev and ma2_last > ma4_last) or (price_2_min_ago < ma3_2_min_ago and price > ma3_last)
                          
                          #mandrakata. vediamo disegno "strano 2 miracolo "
                          #(price_1_min_ago > ma3_prev and price < ma3_last and ma3_last > ma3_2_min_ago) 
                          
                          
                        
                          #and ma36_last < ma36_2_min_ago
                          #and ma9_last >= ma15_last
                          

                          deviation_buy2 >= 0.15
                          
                          and deviation_buy > 0.16
                          
                          and deviation_prev > 0.14
                          
                          #deviation_buy2 > 0.15 or (ma5_prev < ma36_prev and ma5_last > ma36_last and ma3_last > ma39_last and ma12_last > ma12_2_min_ago) 
                          #SARA' COSI' !
                          
                          and ma2_last > ma2_2_min_ago
                          and price > price_1_min_ago
                          and price > price_2_min_ago
                        
                          
                          #and ma2_last > ma7_last
                          #and ma2_last > ma2_2_min_ago
                          #and ma4_last > ma4_2_min_ago
                          
                          and ma3_last > ma40_last
                          #incredibile ma vero E' NECESSARIA quando deve ricomprare dopo la correzione al ribasso
                          
                          
                 
                    ):

                        action = "buy"
                    
                    
                
                   
#############################################################################################################################################



                # COMPRA sessione 3 in poi
    
                elif self.session == 3:
            
            
            
                    if (
                      
                        #ma50_last >= ma50_2_min_ago
                        #and ma2_last >= ma8_last
                        
                        #and ma2_prev < ma5_prev and ma2_last > ma5_last
                        
                        #and ma36_last >= ma36_2_min_ago
                        #and ma8_last >= ma12_last
                        

                        #deviation_buy1 > 0.10
                        #and deviation_prev > 0.13
                        #and deviation_buy > 0.15
                        
                        #COPIATA DA MADDOG ! la buy 3 era andata in sovrapposizione al sell 2 . vediamo 
                        ma2_last >= ma4_last
                        and price >= price_2_min_ago
                        
                        and deviation_buy > 0.08
                        
                        and deviation_buy3 > 0.10
                        #deviation_buy3 = (ma8_last / ma78_last
                        
                        #deve essere anche questo
                        and ma2_last > ma50_last
                        and ma2_last > ma78_last
                        
                        and ma3_last > ma40_last
                        #incredibile ma vero E' NECESSARIA quando deve ricomprare dopo la correzione al ribasso
                        
                        #deviation_buy3 > 0.14 or (ma5_prev < ma36_prev and ma5_last > ma36_last and ma3_last > ma39_last and ma12_last > ma12_2_min_ago) 
                        #SARA' COSI' !
                        
                        
                        #deviation_buy1 > 0.08 e' stata aggiunta all' incrocio classico ma3-ma7 (che pero' non sembrava attivarsi...)
                        
                        ###############################################################
                        #QUESTO E' IL BUY 3 DEL MADDOG
                        #ma2_last >= ma4_last
                        #and deviation_buy1 > 0.08 or (ma3_prev < ma8_prev and ma3_last > ma8_last and ma12_last > ma12_2_min_ago)
                        #and deviation > 0.08
                        #and price > price_2_min_ago
                        #################################################################
                        
                        
                        #and ma2_last > ma7_last
                        #and ma2_last > ma2_2_min_ago
                        #and ma4_last > ma4_2_min_ago
                       
                        #and price > price_1_min_ago
                        #and price > price_2_min_ago
                       
                    ):

                        action = "buy"

                        
                        
                    elif (
                          
                          #ma50_last < ma50_2_min_ago
                          #and ma2_last >= ma8_last
                          
                          #and ma2_prev < ma5_prev and ma2_last > ma5_last
                          
                          #and ma36_last < ma36_2_min_ago
                          #and ma9_last >= ma15_last
                          
                          
                          
                          #deviation_buy1 >= 0.10
                          #and deviation_prev > 0.15
                          #and deviation_buy > 0.17
                          
                          
                          #COPIATA DA MADDOG ! la buy 3 era andata in sovrapposizione al sell 2 . vediamo 
                          ma2_last >= ma4_last
                          and price > price_2_min_ago
                          
                          and deviation_buy > 0.08
                        
                          and deviation_buy3 > 0.10
                        
                          #deve essere anche questo
                          and ma2_last > ma50_last
                          and ma2_last > ma78_last
                          
                          and ma3_last > ma40_last
                          #incredibile ma vero E' NECESSARIA quando deve ricomprare dopo la correzione al ribasso
                          
                          #deviation_buy3 > 0.14 or (ma5_prev < ma36_prev and ma5_last > ma36_last and ma3_last > ma39_last and ma12_last > ma12_2_min_ago) 
                          #SARA' COSI' !
                          
                        
                          
                          #and ma2_last > ma7_last
                          #and ma4_last > ma4_2_min_ago
                        
                          #in aggiunta
                          and price > price_1_min_ago
                          and price > price_2_min_ago
                          and ma2_last > ma2_2_min_ago
                    ):

                        action = "buy"
                        
               
                    
        #####################################################################

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

            # VENDITA 1 - con fasce di tempo !

            #    minuti
            #   0 -  3 -----------if 13 > 39 vende come adesso ma se 13 < 39 vende 0,10 prima - c'e' vita su marte !
            #   3 -  5 -----------
            #   5 - 12 -----------
            
            #  12 - 18 ----------- 
            #  18 - 30 -----------
            #   > 30   -----------

            ##################################################################################
            
            ###########################################################################################################################0 -3 min

            # VENDITA - da 0 a 3 minuti = da 0 a 180 secondi

            if seconds_since_last_trade > 0 and seconds_since_last_trade <= 180:
                
                
                if (
                    #ma50_last > ma50_2_min_ago
                    #and ma36_last > ma36_2_min_ago
                    ma2_last < ma15_last 
                    and deviation_sell > 0.15
                    
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                    #metto la chiusura della gabbia per essere sicuro che venda !
                    
                    #deviation_gabbia = ma6_last / ma38_last
                ):
                   
                    action = "sell"
                    
                   
                
              
                elif (
                    #ma50_last > ma50_2_min_ago
                    #and ma36_last > ma36_2_min_ago
                    
                    ma13_last >= ma39_last
                    
                    and deviation_sell < -0.62 or (ma50_last < ma50_2_min_ago and deviation_gabbia < -0.15)
                    #and ma2_last < ma39_last < -0.49
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                    #metto la chiusura della gabbia per essere sicuro che venda !
                    
                    #deviation_gabbia = ma6_last / ma38_last
                    
                ):
                   
                    action = "sell"
                    
                    
                    
                    
                elif (
                    #ma50_last > ma50_2_min_ago
                    #and ma36_last > ma36_2_min_ago
                    
                    ma13_last < ma39_last
                    
                    and deviation_sell < -0.52 or (ma50_last < ma50_2_min_ago and deviation_gabbia < -0.10)
                    #and ma2_last < ma39_last < -0.49
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                    #metto la chiusura della gabbia per essere sicuro che venda !
                    
                    #deviation_gabbia = ma6_last / ma38_last
                    
                ):
                   
                    action = "sell"
                    
                    
         #########################################################################################################################3-5 min           

            # VENDITA - da 3 a 5 minuti = da 180 a 300 secondi

            elif seconds_since_last_trade > 180 and seconds_since_last_trade <= 300:

                
                if (
                    #ma50_last > ma50_2_min_ago
                    #and ma36_last > ma36_2_min_ago
                    ma2_last < ma15_last 
                    and deviation_sell > 0.15
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                    #metto la chiusura della gabbia per essere sicuro che venda !
                    
                    #deviation_gabbia = ma6_last / ma38_last
                  
                ):
                    action = "sell"

                    
                elif (
                    #ma50_last >= ma50_2_min_ago
                    #and ma36_last >= ma36_2_min_ago
                    ma13_last >= ma39_last
                    
                    and deviation_sell < -0.62 or (ma50_last < ma50_2_min_ago and deviation_gabbia < -0.15)
                    
                   
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                    #metto la chiusura della gabbia per essere sicuro che venda !
                    
                    #deviation_gabbia = ma6_last / ma38_last
                    
                ):
                    action = "sell"
                    
                    
                    
                elif (
                    #ma50_last >= ma50_2_min_ago
                    #and ma36_last >= ma36_2_min_ago
                    ma13_last < ma39_last
                    
                    and deviation_sell < -0.52 or (ma50_last < ma50_2_min_ago and deviation_gabbia < -0.10)
                    
                   
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                    #metto la chiusura della gabbia per essere sicuro che venda !
                    
                    #deviation_gabbia = ma6_last / ma38_last
                    
                ):
                    action = "sell"
          
            ########################################################################################################################5-12 min         
                
            # VENDITA - da 5 a 12 minuti = da 300 a 720 secondi

            elif seconds_since_last_trade > 300 and seconds_since_last_trade <= 720:
                

                if (
                    #ma50_last >= ma50_2_min_ago
                    #and ma36_last >= ma36_2_min_ago
                    ma2_last < ma17_last 
                    and deviation_sell > 0.15
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_3_min_ago
                    
                    #metto la chiusura della gabbia per essere sicuro che venda !
                    
                    #deviation_gabbia = ma6_last / ma38_last
                    
                ):
                    action = "sell"
                    
             
                    
                elif (
                    #ma50_last >= ma50_2_min_ago
                    #and ma36_last >= ma36_2_min_ago
                    
                    deviation_sell < -0.62 or (ma50_last < ma50_2_min_ago and deviation_gabbia < -0.15)
                    
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_3_min_ago
                    
                    #metto la chiusura della gabbia per essere sicuro che venda !
                    
                    #deviation_gabbia = ma6_last / ma38_last
                    
                ):
                    action = "sell"
                    
                    
                    
                    
                    
                    
            
                    

            # VENDITA - da 12 a 18 minuti = da 720 a 1080 secondi

            elif seconds_since_last_trade > 720 and seconds_since_last_trade <= 1080:

                if (
                    #ma50_last >= ma50_2_min_ago
                    #and ma36_last >= ma36_2_min_ago
                    ma2_last < ma17_last 
                    and deviation_sell > 0.12
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                    #metto la chiusura della gabbia per essere sicuro che venda !
                    
                    #deviation_gabbia = ma6_last / ma38_last
                    
                    
                ):
                    action = "sell"
                    
                  
                elif (
                    #ma50_last >= ma50_2_min_ago
                    #and ma36_last >= ma36_2_min_ago
                    deviation_sell < -0.62 or (ma50_last < ma50_2_min_ago and deviation_gabbia < -0.15)
                    
                    
                    #and deviation_sell < -0.61
                    #and ma2_last < ma20_last
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                    #metto la chiusura della gabbia per essere sicuro che venda !
                    
                    #deviation_gabbia = ma6_last / ma38_last
                    
                ):
                    action = "sell"
                    
                    
          

            # VENDITA - da 18 a 30 minuti = da 1080 a 1800 secondi

            elif seconds_since_last_trade > 1080 and seconds_since_last_trade <= 1800:
                
                

                if (
                    #ma50_last > ma50_2_min_ago
                    #and ma36_last > ma36_2_min_ago
                    ma2_last < ma17_last 
                    and deviation_sell > 0.12
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                    #metto la chiusura della gabbia per essere sicuro che venda !
                    
                    #deviation_gabbia = ma6_last / ma38_last
                    
                ):
                    action = "sell"
                
                    
                elif (
                    #ma50_last > ma50_2_min_ago
                    #and ma36_last > ma36_2_min_ago
                    
                    deviation_sell < -0.59 or (ma50_last < ma50_2_min_ago and deviation_gabbia < -0.15)
                    
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                    #metto la chiusura della gabbia per essere sicuro che venda !
                  
                    #deviation_gabbia = ma6_last / ma38_last
                    
                ):
                    action = "sell"
                    
                    
                    
              

            # VENDITA - da 30 minuti in poi = da 1800 secondi in poi

            elif seconds_since_last_trade > 1800:
               
                
                if (
                    #ma50_last > ma50_2_min_ago
                    #and ma36_last > ma36_2_min_ago
                    ma2_last < ma17_last 
                    and deviation_sell > 0.12
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                    #metto la chiusura della gabbia per essere sicuro che venda !
                    
                    #deviation_gabbia = ma6_last / ma38_last
                    
                ):
                    
               
                    action = "sell"
                    
                
                    
                elif (
                    #ma50_last > ma50_2_min_ago
                    #and ma36_last > ma36_2_min_ago
                    
                    deviation_sell < -0.59 or (ma50_last < ma50_2_min_ago and deviation_gabbia < -0.15)
                    
                    
                    #questa ho dovuto metterla perche' ha venduto "da sotto" mentre ma2 saliva !
                    and ma2_last < ma2_2_min_ago
                    
                    #metto la chiusura della gabbia per essere sicuro che venda !
                    
                    #deviation_gabbia = ma6_last / ma38_last
                    
                ):
                    action = "sell"
                    
                    
                    
              

            #########################################################################################

            # 1) (STOP LOSS) (salvagente)  
            # se ma100_last >= ma100_13_min_ago vende in un modo 
            # se ma100_last < ma100_13_min_ago vende in un altro modo
            
            if (
                ma2_last < ma36_last and deviation_sell < -0.63 or (ma2_last < ma36_last and deviation_sell < -0.64)
                
                
              
            ):
                action = "sell"
            
            
            #elif (
                
                #ma2_last < ma36_last 
                #and deviation_sell < -0.50
            #):    
                #action = "sell"
            
            
            
           

            #2) ro cano VENDE " DOPO 60 MINUTI " "max hold time" riga 128
            elif (
                seconds_since_last_trade > max_hold_time_in_seconds
                and ma8_last < ma39_last and deviation_sell < -0.60
                
            ):
                action = "sell"

        ############### FINE ALGORITH #################
        
        

        self.algo_helper.log("action {}".format(action))

        if action == "sell":
            self.session += 1

        return action

        #ave comparo meo ! #####
        #ole ### ## 
        
        #sempre ole #######
        ###### AVE COMBA #### 
        ## non fa reset ## bla bla bla ...##
        ##
        
        #

        
