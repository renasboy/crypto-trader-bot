
class ro_cano_che_ritorna(object):

    def __init__(self, helper):
        self.algo_helper = helper
        self.session = 0
        self.open = False

    @property
    def action(self):
        
        # TIME dopo quanto tempo ro cano ritorna automaticamente ( per esempio 60 minuti x 60 = 3600 secondi ) e 
        max_hold_time_in_seconds = 660
        
        #durata segmento in cui a tutte le condizioni buy PER COMPRARE si aggiunge la deviation 
        # per il BUY UN PO' PIU' SOPRA DELL' ULTIMO SELL
        # e per il BUY UN PO' PIU' SOPRA DELL' ULTIMO BUY ( ma adesso a 660 secondi ro cano vende automaticamente !)
        min_buy_delay_in_seconds = 2100

        # MACD di 1-2-3-4 minuti prima
        macd = self.algo_helper.macd
        
        macd_2_min_ago = self.algo_helper.macd_minutes_ago(2)
      
        # moving average (2-3-4-5-x)
        ma2_last, ma2_prev = self.algo_helper.ma_last_prev(2)
        ma4_last, ma4_prev = self.algo_helper.ma_last_prev(4)
        ma5_last, ma5_prev = self.algo_helper.ma_last_prev(5)
        ma7_last, ma7_prev = self.algo_helper.ma_last_prev(7)  
        ma11_last, ma11_prev = self.algo_helper.ma_last_prev(11)
        ma16_last, ma16_prev = self.algo_helper.ma_last_prev(16)
        ma34_last, ma34_prev = self.algo_helper.ma_last_prev(34)
        ma43_last, ma43_prev = self.algo_helper.ma_last_prev(43)
        ma50_last, ma50_prev = self.algo_helper.ma_last_prev(50)
        
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
        ma34_2_min_ago = self.algo_helper.ma_minutes_ago(34, 2)
        ma43_2_min_ago = self.algo_helper.ma_minutes_ago(43, 2)
        ma50_2_min_ago = self.algo_helper.ma_minutes_ago(50, 2)
        
        # LAST TRADE
        last_trade_action = self.algo_helper.last_trade_action
        last_trade_time = self.algo_helper.last_trade_time
        last_trade_price = self.algo_helper.last_trade_price 
        seconds_since_last_trade = self.algo_helper.seconds_since_last_trade
        
        # CURRENT PRICE
        price = self.algo_helper.price
        
        # la deviaton stabilisce i limiti della VENDITA MENTRE SALE e della VENDITA MENTRE SCENDE.
        deviation = (price / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.log('deviation: {}'.format(deviation))
        
        action = None
      
    
        #######################################################################
        # APRE E CHIUDE GABBIA
        # SI APRE LA GABBIA SE 
        if ma50_last > ma50_2_min_ago:  
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

            # COMPRA UN PO' PIU' SOPRA DELL' ULTIMO SELL SE DEVIATION > 0.37
            if ((seconds_since_last_trade > 0 and seconds_since_last_trade <= min_buy_delay_in_seconds and deviation > 0.4)
                or (seconds_since_last_trade == 0 or seconds_since_last_trade > min_buy_delay_in_seconds)):
                
            # COMPRA UN PO' PIU' SOPRA DELL' ULTIMO BUY SE DEVIATION > 0.27
            #if ((seconds_since_last_trade > 0 and seconds_since_last_trade >= min_buy_delay_in_seconds and deviation > 0.27)
                #or (seconds_since_last_trade == 0 or seconds_since_last_trade > min_buy_delay_in_seconds)):
            
            

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
                        and ma43_last >= ma43_2_min_ago
                        and ma50_last >= ma50_2_min_ago
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
                        and ma34_last > ma34_2_min_ago
                        and ma43_last >= ma43_2_min_ago
                        and ma50_last >= ma50_2_min_ago
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
                        and ma34_last > ma34_2_min_ago
                        and ma43_last >= ma43_2_min_ago
                        and ma50_last >= ma50_2_min_ago
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
                if ma2_prev > ma7_prev and ma2_last < ma7_last:
                    if deviation > 0.24:
                        action = 'sell'

            # VENDE sessione 2
            elif self.session == 2:   
                if ma2_prev > ma7_prev and ma2_last < ma7_last:
                    if deviation > 0.24:
                        action = 'sell'     
                        
            # VENDE sessione 3 in poi
            else:
                if ma2_prev > ma7_prev and ma2_last < ma7_last:
                    if deviation > 0.24:
                        action = 'sell'

            # SE LA PERDITA E' TROPPA VENDE SUBITO (SALVAGENTE)
            if deviation < -0.9:
                action = 'sell'
            
            # compa qua aiutami tu a capire ! " salvagente piu' lontano e salvagente piu' vicino "
            # ( compa, una volta c'e' stata una grande vendita al 3° minuto dopo il buy ! ) - ( forse si puo' risolvere con ma2 al posto del price nella deviation )
            # da 0 a 240 secondi dal buy VENDI se ma2 < ma7 "E SE" deviation < -1.8
            # da 241 secondi dal buy VENDI se ma2 < ma16 "E SE" deviation < -0.5 ( provo a ridurre le perdite nel ribasso improvviso e improbabile ) 
            
            
            
            
            # RO CANO TORNA A CASA 
            # 1) (salvagente 1) ATTESA DI 1 ORA = 3600 SECONDI "max hold time" " DOPO UN' ORA VENDE SUBITO " 
            # 2) (salvagente 2 ) ma aggiungere VENDI SE DIMINUISCE LA FORZA! ( DOPO 11 MINUTI VENDE SE deviation <-0,4 "E SE" ma1 < ma16  ( aggiungi dopo )"E SE" ma7 < ma7 3 min ago "E SE" ma11 < ma11 3 min ago "E SE" ma16 < ma16 3 min ago )
            
            if seconds_since_last_trade > max_hold_time_in_seconds:
                
                action = 'sell'
                
                
            if (seconds_since_last_trade > max_hold_time_in_seconds
                and deviation < -0.4
                and ma1 < ma16):
                
                action = 'sell'

                
        self.algo_helper.log('action {}'.format(action))

        if action == 'sell':
            self.session += 1

        return action
