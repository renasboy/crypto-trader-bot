
class ro_cano_che_ritorna(object):

    def __init__(self, helper):
        self.algo_helper = helper
        self.session = 0
        self.open = False

    @property
    def action(self):
        
        # TIME dopo quanto tempo ro cano ritorna automaticamente ( per esempio 11 minuti x 60 = 3600 secondi )
        max_hold_time_in_seconds = 3600
        
        # tempo di attesa "quaqndo comincia a perdere la forza" ( adesso 11 minuti )
        max_hold_without_force_time_in_seconds = 660
        
        # DURATA SEGMENTO ( 5 minuti * 60 = 300 secondi 5 ) 
        # in cui,
        # se ro cano deve comprare :
        # a tutte le condizioni gia' stabilite per comprare SI AGGIUNGE la "deviation" 
        # sia per il BUY UN PO' PIU' SOPRA DELL' ULTIMO SELL
        # che per il BUY UN PO' PIU' SOPRA DELL' ULTIMO BUY ( ma qua ho fatto casino !)
        min_buy_delay_in_seconds = 300
        
        # MACD di 1-2-3-4 minuti prima
        macd = self.algo_helper.macd
        
        # macd_1_min_ago = self.algo_helper.macd_minutes_ago(1) NON UTILIZZARLO ! E' UGUALE AL MACD.
        macd_2_min_ago = self.algo_helper.macd_minutes_ago(2)
      
        # moving average (2-3-4-5-x) ( GRANDE IDEA : in futuro metti invece di ma50 ma49 e testa - invece di ma49 ma48 e testa - adesso compra un po' troppo tardi,,,)
        ma2_last, ma2_prev = self.algo_helper.ma_last_prev(2)
        ma4_last, ma4_prev = self.algo_helper.ma_last_prev(4)
        ma5_last, ma5_prev = self.algo_helper.ma_last_prev(5)
        ma7_last, ma7_prev = self.algo_helper.ma_last_prev(7)  
        ma11_last, ma11_prev = self.algo_helper.ma_last_prev(11)
        ma16_last, ma16_prev = self.algo_helper.ma_last_prev(16)
        ma34_last, ma34_prev = self.algo_helper.ma_last_prev(34)
        ma42_last, ma42_prev = self.algo_helper.ma_last_prev(42)
        ma49_last, ma49_prev = self.algo_helper.ma_last_prev(49)
        
        # moving average (2-3-4-5-7-8-20-43-100) di x minuti prima (NON METTERE MAI 1 min !) ( GRANDE IDEA : in futuro metti invece di ma50 2min ago ma49 2min ago e testa - invece di ma49 2min ago ma48 2min ago e testa - adesso compra un po' troppo tardi,,,)
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
        ma34_2_min_ago = self.algo_helper.ma_minutes_ago(34, 2)
        ma42_2_min_ago = self.algo_helper.ma_minutes_ago(42, 2)
        ma49_2_min_ago = self.algo_helper.ma_minutes_ago(49, 2)
        
        
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
        
        
        # compa
        # forse bisogna fare questo LAST SELL
        # last_sell_time = self.algo_helper.last_sell_time
        
        # forse bisogna fare questo LAST BUY
        # last_buy_time = self.algo_helper.last_buy_time
        
        
        # CURRENT PRICE
        price = self.algo_helper.price
        
        
        
        # la "deviaton" stabilisce i limiti 
        
        # SOPRA I QUALI ro cano COMPRA ( deve dimostrare una certa forza ) ( e compra sopra l' ULTIMO SELL e compra anche sopra l' ULTIMO BUY )
        # SOPRA I QUALI ro cano VENDE ( guadagno minimo mentre sale ) 
        
        # SOTTO I QUALI ro cano VENDE ( se comincia a perdere forza mentre scende).
        # SOTTO I QUALI VENDE IMMEDIATAMENTE ( SALVAGENTE )
        
        deviation = (price / last_trade_price - 1) * 100 if last_trade_price else 0
        
        self.algo_helper.log('deviation: {}'.format(deviation))
        
        
        
        # deviation buy = (price / last_buy - 1) * 100 if last_buy else 0
        
        
        
        
        
        action = None
      
    
        #######################################################################
        # APRE E CHIUDE GABBIA
        # SI APRE LA GABBIA SE 
        if ma49_last > ma49_2_min_ago:  
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

            # COMPRA UN PO' PIU' SOPRA DELL' ULTIMO SELL SE DEVIATION > 0.40
            if ((seconds_since_last_trade > 0 and seconds_since_last_trade <= min_buy_delay_in_seconds and deviation > 0.4)
                or (seconds_since_last_trade == 0 or seconds_since_last_trade > min_buy_delay_in_seconds)):
                
            # COMPRA UN PO' PIU' SOPRA anche DELL' ULTIMO BUY SE DEVIATION > 0.20 ( qua ho fatto il casino )
            #if ((seconds_since_last_trade > 0 and seconds_since_last_trade >= min_buy_delay_in_seconds and deviation > 0.27)
                #or (seconds_since_last_trade == 0 or seconds_since_last_trade > min_buy_delay_in_seconds)):
                
                
               
                # compa, forse, ci deve essere 
                # una attesa che comincia dall' ULTIMO SELL
                # e una attesa che comincia dall' ULTIMO BUY
            

                # COMPRA sessione 1
                if self.session == 1:
                    if (ma2_last > ma2_2_min_ago
                        and ma4_last > ma4_2_min_ago
                        and ma5_last > ma5_2_min_ago
                        and ma5_2_min_ago > ma5_3_min_ago
                        and ma7_last > ma7_2_min_ago
                        and ma11_last > ma11_2_min_ago
                        and ma16_last > ma16_2_min_ago
                        and ma34_last > ma34_2_min_ago
                        and ma42_last >= ma42_2_min_ago
                        and ma49_last >= ma49_2_min_ago
                        and macd < 60):
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
                        and ma34_last > ma34_2_min_ago
                        and ma42_last >= ma42_2_min_ago
                        and ma49_last >= ma49_2_min_ago
                        and macd < 60):
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
                        and ma34_last > ma34_2_min_ago
                        and ma42_last >= ma42_2_min_ago
                        and ma49_last >= ma49_2_min_ago
                        and macd < 60):
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
                if ma2_prev > ma7_prev and ma2_last < ma7_last:
                    if deviation > 0.25:
                        action = 'sell'

            # VENDE sessione 2
            elif self.session == 2:   
                if ma2_prev > ma7_prev and ma2_last < ma7_last:
                    if deviation > 0.25:
                        action = 'sell'     
                        
            # VENDE sessione 3 in poi
            else:
                if ma2_prev > ma7_prev and ma2_last < ma7_last:
                    if deviation > 0.25:
                        action = 'sell'

            # SE LA PERDITA E' TROPPA VENDE SUBITO (SALVAGENTE)
            if deviation < -1.6:
                action = 'sell'
            
            # compa qua aiutami tu a capire !  " vendita piu' lontana e vendita piu' vicina "
            # ( compa, una volta c'e' stata una grande vendita al 3° minuto dopo il buy ! ) - ( forse si puo' risolvere con ma2 al posto del price nella deviation )
            # da 0 a 240 secondi dal buy VENDI se ma2 < ma7 "E SE" deviation < -1.8
            # da 241 secondi dal buy VENDI se ma2 < ma16 "E SE" deviation < -0.5 ( provo a ridurre le perdite nel ribasso improvviso e improbabile ) 
            
            
            
            
            # RO CANO TORNA A CASA ( VENDE !) 
            # 1) VENDE SE DIMINUISCE LA FORZA ! ( vende dopo 11 minuti SE deviation <-0,4 "E SE" ma1 < ma16  ( dopo, se vuoi, puoi aggiungere ) "E SE" ma7 < ma7 3 min ago "E SE" ma11 < ma11 3 min ago "E SE" ma16 < ma16 3 min ago )
            # 2) VENDE " DOPO UN' ORA " "max hold time" 
           
            
            
            if (seconds_since_last_trade > max_hold_without_force_time_in_seconds
                and deviation < -0.70
                and ma2_last < ma16_last):
                
                action = 'sell'
            
            elif (seconds_since_last_trade > max_hold_time_in_seconds
                  and ma7_last < ma7_3_min_ago):
                
                action = 'sell'
                
                
            

                
        self.algo_helper.log('action {}'.format(action))

        if action == 'sell':
            self.session += 1

        return action
