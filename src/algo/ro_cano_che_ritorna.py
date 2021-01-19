
class ro_cano_che_ritorna(object):

    def __init__(self, helper):
        self.algo_helper = helper
        self.session = 0
        self.open = False

    @property
    def action(self):
        
        
        
        
        # MACD di 1-2-3-4 minuti prima
        macd = self.algo_helper.macd
        
        # macd_1_min_ago = self.algo_helper.macd_minutes_ago(1) (NON UTILIZZARLO ! e' uguale al macd !)
        macd_2_min_ago = self.algo_helper.macd_minutes_ago(2)
      
        # moving average (2-3-4-5-x) 
        ma2_last, ma2_prev = self.algo_helper.ma_last_prev(2)
        ma4_last, ma4_prev = self.algo_helper.ma_last_prev(4)
        ma5_last, ma5_prev = self.algo_helper.ma_last_prev(5)
        ma7_last, ma7_prev = self.algo_helper.ma_last_prev(7)  
        ma11_last, ma11_prev = self.algo_helper.ma_last_prev(11)
        ma13_last, ma13_prev = self.algo_helper.ma_last_prev(13)
        ma15_last, ma15_prev = self.algo_helper.ma_last_prev(15)
        ma16_last, ma16_prev = self.algo_helper.ma_last_prev(16)
        ma18_last, ma18_prev = self.algo_helper.ma_last_prev(18)
        ma25_last, ma25_prev = self.algo_helper.ma_last_prev(25)
        ma34_last, ma34_prev = self.algo_helper.ma_last_prev(34)
        ma41_last, ma41_prev = self.algo_helper.ma_last_prev(41)
        ma48_last, ma48_prev = self.algo_helper.ma_last_prev(48)
        ma78_last, ma78_prev = self.algo_helper.ma_last_prev(78)
        
        # moving average (2-3-4-5-7-8-20-43-100) di x minuti prima (NON METTERE MAI 1 min !)
        ma2_2_min_ago = self.algo_helper.ma_minutes_ago(2, 2) 
        ma4_2_min_ago = self.algo_helper.ma_minutes_ago(4, 2)
        ma5_2_min_ago = self.algo_helper.ma_minutes_ago(5, 2)
        ma5_3_min_ago = self.algo_helper.ma_minutes_ago(5, 3)
        ma7_2_min_ago = self.algo_helper.ma_minutes_ago(7, 2)
        ma7_3_min_ago = self.algo_helper.ma_minutes_ago(7, 3)
        ma11_2_min_ago = self.algo_helper.ma_minutes_ago(11, 2)
        ma11_3_min_ago = self.algo_helper.ma_minutes_ago(11, 3)
        ma16_2_min_ago = self.algo_helper.ma_minutes_ago(16, 2)
        ma16_3_min_ago = self.algo_helper.ma_minutes_ago(16, 3)
        ma18_2_min_ago = self.algo_helper.ma_minutes_ago(18, 2)
        ma25_2_min_ago = self.algo_helper.ma_minutes_ago(25, 2)
        ma34_2_min_ago = self.algo_helper.ma_minutes_ago(34, 2)
        ma41_2_min_ago = self.algo_helper.ma_minutes_ago(41, 2)
        ma41_18_min_ago = self.algo_helper.ma_minutes_ago(41, 18)
        ma48_2_min_ago = self.algo_helper.ma_minutes_ago(48, 2)
        ma78_2_min_ago = self.algo_helper.ma_minutes_ago(78, 2)
        
        # LAST TRADE
        last_trade_action = self.algo_helper.last_trade_action
        last_trade_time = self.algo_helper.last_trade_time
        last_trade_price = self.algo_helper.last_trade_price 
        seconds_since_last_trade = self.algo_helper.seconds_since_last_trade

        # PREV TRADE
        prev_trade_action = self.algo_helper.prev_trade_action
        prev_trade_time = self.algo_helper.prev_trade_time
        prev_trade_price = self.algo_helper.prev_trade_price 
        seconds_since_prev_trade = self.algo_helper.seconds_since_prev_trade
        
        
       
        # PREZZO DI MERCATO - CURRENT PRICE
        price = self.algo_helper.price
        
        
        # TEMPO DOPO IL QUALE ro cano ritorna a casa ( 60 minuti = 60 * 60 = 3600 secondi ) ) (E SE ma7 < ma7 3 min ago)
        max_hold_time_in_seconds = 3600
        
        # TEMPO DOPO IL QUALE "se ro cano COMINCIA A PERDERE LA FORZA" vende ! ( 20 minuti = 20 * 60 = 1200 secondi ) ( ma anche alcune ma devono incrociare al ribasso )
        max_hold_without_force_time_in_seconds = 1200
        
        
        
        # TEMPO in cui SI AGGIUNGE LA DEVIATION !  (a tutte le altre condizioni gia' stabilite per comprare)  
        # per ULTIMO trade ( 70 minuti = 70 * 60 = 4200 secondi )
        # per PENULTIMO trade ( 60 minuti = 60 * 60 = 3600 secondi )
        min_buy_delay_in_seconds = 4200
        min_prev_buy_delay_in_seconds = 3600
      
        
        # formula DEVIATION last_trade (di solito il SELL) per comprare UN PO' PIU' SOPRA DEL LAST TRADE (di solito ultimo sell)
        
        deviation = (price / last_trade_price - 1) * 100 if last_trade_price else 0
        
        self.algo_helper.log('deviation: {}'.format(deviation))
        
        
        
        # formula DEVIATION prev_trade (qualche volta il BUY ) per comprare UN PO' PIU' SOPRA DEL PREV TRADE (eccezionalmente ultimo buy)
        
        deviation_prev = (price / prev_trade_price - 1) * 100 if prev_trade_price else 0
        
        #self.algo_helper.log('deviation_prev: {}'.format(deviation_prev))
        
        
        
        
        # 1) ro cano COMPRA UN PO' PIU' SOPRA DELL' ULTIMO TRADE
        
        # 2) ro cano COMPRA UN PO' PIU' SOPRA anche DEL PENULTIMO TRADE 
        
        
        
        
        # 1) ro cano VENDE SE DIMINUISCE LA FORZA !
        
        # 2) ro cano VENDE " DOPO UN' ORA " "max hold time" 
        
        # 3) ro cano VENDE SE LA PERDITA E' TROPPA ( CROLLO IMPROVVISO ) VENDE SUBITO ! (SALVAGENTE)
        
        
        
        
        
        
        
        action = None
      
    
        #######################################################################
        
        # APRE E CHIUDE GABBIA
        # SI APRE LA GABBIA SE 
        if ma78_last > ma78_2_min_ago:  
            # NON TOCCARE QUESTA CONDIZIONE SERVE PER APERTURA DI GABBIA
            if not self.session or not self.open:
               self.session = 1
               self.open = True
               self.algo_helper.log('session {}: open segment'.format(self.session))
        # SI CHIUDE LA GABBIA SE
        else:
           self.open = False
           self.algo_helper.log('session {}: closed segment'.format(self.session))
        
        #######################################################################
        
        # COMPRA
        # NON TOCCARE QUESTA CONDIZIONE (QUESTA DICE CHE STA IN MODO BUY, DEVO COMPRARE)
        if self.open and self.session and last_trade_action != 'buy':

            # COMPRA UN PO' PIU' SOPRA DELL' ULTIMO TRADE SE DEVIATION > 0.35 nei 540 secondi dall' ultimo trade ( quasi sempre IL SELL )
            # COMPRA UN PO' PIU' SOPRA anche DEL PENULTIMO TRADE SE DEVIATION > 0.27 nei 540 secondi (ci vorrebbe un altro tempo ) dal PENULTIMO TRADE ( qualche volta IL BUY)
            
            if ((seconds_since_last_trade > 0 and seconds_since_last_trade <= min_buy_delay_in_seconds and deviation > 0.35)
                or (seconds_since_prev_trade > 0 and seconds_since_prev_trade <= min_prev_buy_delay_in_seconds and deviation_prev > 0.25)
                or (seconds_since_last_trade == 0 or seconds_since_last_trade > min_buy_delay_in_seconds)):
                
            
            
                
                
               
            

                # COMPRA sessione 1
                if self.session == 1:
                    if (ma2_last > ma2_2_min_ago
                        and ma4_last > ma4_2_min_ago
                        and ma5_last > ma5_2_min_ago
                        and ma5_2_min_ago > ma5_3_min_ago
                        and ma7_last > ma7_2_min_ago
                        and ma11_last > ma11_2_min_ago
                        and ma16_last > ma16_2_min_ago
                        and ma16_2_min_ago > ma16_3_min_ago
                        and ma18_last > ma18_2_min_ago
                        and ma25_last > ma25_2_min_ago
                        and ma34_last > ma34_2_min_ago
                        and ma41_last >= ma41_2_min_ago
                        and ma41_last >= ma41_18_min_ago
                        and ma48_last >= ma48_2_min_ago
                        and ma78_last >= ma78_2_min_ago
                        and macd < 50):
                        action = 'buy'
                    
                # COMPRA sessione 2
                elif self.session == 2:
                    if (ma2_last > ma2_2_min_ago
                        and ma4_last > ma4_2_min_ago
                        and ma5_last > ma5_2_min_ago
                        and ma5_2_min_ago > ma5_3_min_ago
                        and ma7_last > ma7_2_min_ago
                        and ma11_last > ma11_2_min_ago
                        and ma16_last > ma16_2_min_ago
                        and ma16_2_min_ago > ma16_3_min_ago
                        and ma18_last > ma18_2_min_ago
                        and ma25_last > ma25_2_min_ago
                        and ma34_last > ma34_2_min_ago
                        and ma41_last >= ma41_2_min_ago
                        and ma41_last >= ma41_18_min_ago
                        and ma48_last >= ma48_2_min_ago
                        and ma78_last >= ma78_2_min_ago
                        and macd < 50):
                        action = 'buy'
                  
                # COMPRA sessione 3 in poi
                else:
                    if (ma2_last > ma2_2_min_ago
                        and ma4_last > ma4_2_min_ago
                        and ma5_last > ma5_2_min_ago
                        and ma5_2_min_ago > ma5_3_min_ago
                        and ma7_last > ma7_2_min_ago
                        and ma11_last > ma11_2_min_ago
                        and ma16_last > ma16_2_min_ago
                        and ma16_2_min_ago > ma16_3_min_ago
                        and ma18_last > ma18_2_min_ago
                        and ma25_last > ma25_2_min_ago
                        and ma34_last > ma34_2_min_ago
                        and ma41_last >= ma41_2_min_ago
                        and ma41_last >= ma41_18_min_ago
                        and ma48_last >= ma48_2_min_ago
                        and ma78_last >= ma78_2_min_ago
                        and macd < 50):
                        action = 'buy'
    
    
    
        #######################################################################
        # VENDA
        # NON TOCCARE QUESTA CONDIZIONE (QUESTA DICE CHE STA IN MODO SELL, DEVO VENDERE)
        elif last_trade_action == 'buy':

            self.algo_helper.log('ma2_prev: {}'.format(ma2_prev))
            self.algo_helper.log('ma7_prev: {}'.format(ma7_prev))
            self.algo_helper.log('ma2_last: {}'.format(ma2_last))
            self.algo_helper.log('ma7_last: {}'.format(ma7_last))
            self.algo_helper.log('deviation: {}'.format(deviation))
            self.algo_helper.log('session: {}'.format(self.session))

            # VENDE CON INCROCIO ma2 - ma7 ( + DEVIATION BUY )

            # VENDE sessione 1
            if self.session == 1:
                if ma2_prev > ma15_prev and ma2_last < ma15_last:
                    if deviation > 0.27:
                        action = 'sell'

            # VENDE sessione 2
            elif self.session == 2:   
                if ma2_prev > ma15_prev and ma2_last < ma15_last:
                    if deviation > 0.27:
                        action = 'sell'     
                        
            # VENDE sessione 3 in poi
            else:
                if ma2_prev > ma15_prev and ma2_last < ma15_last:
                    if deviation > 0.27:
                        action = 'sell'

            # SE LA PERDITA E' TROPPA VENDE SUBITO (SALVAGENTE) (stop loss)
            if (deviation < -1.6
                and ma2_prev > ma16_prev and ma2_last < ma16_last):
                    action = 'sell'
            
            
            
            # IDEA da 241 secondi dal buy VENDI se ma2 < ma16 ( SI ALZA LA MEDIA )
            
            
           
            # RO CANO TORNA A CASA.
            
            # 1) ro cano VENDE SE DIMINUISCE LA FORZA ! (vende se perdita  < -0.84 e se etc.)
          
            if (seconds_since_last_trade > max_hold_without_force_time_in_seconds
                and deviation < -0.84
                and ma7_last < ma7_3_min_ago
                and ma11_last < ma11_3_min_ago
                and ma16_last < ma16_3_min_ago
                and ma11_last < ma16_last
                and ma2_last < ma16_last):
                
                action = 'sell'
                
                
                
            # 2) ro cano VENDE " DOPO UN' ORA " "max hold time" (vende dopo 1 ora e se ma7_last < ma7_3_min_ago)   
            
            elif (seconds_since_last_trade > max_hold_time_in_seconds
                  and ma7_last < ma7_3_min_ago):
                
                action = 'sell'
                
                
            

                
        self.algo_helper.log('action {}'.format(action))

        if action == 'sell':
            self.session += 1

        return action
