from datetime import datetime

class ro_cano_che_ritorna(object):

    def __init__(self, helper):
        self.algo_helper = helper
        self.session = 0
        self.open = False

    @property
    def action(self):
        
        # TIME dopo quanto tempo ro cano ritorna ( per esempio 60 minuti x 60 = 3600 secondi )
        max_hold_time_in_seconds = 7200

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
        
        # moving average (2-3-4-5-7-8-20-43-100) di x minuti prima (NON METTERE MAI 1 min !)
        ma2_2_min_ago = self.algo_helper.ma_minutes_ago(2, 2) 
        ma4_2_min_ago = self.algo_helper.ma_minutes_ago(4, 2)
        ma5_2_min_ago = self.algo_helper.ma_minutes_ago(5, 2)
        ma7_2_min_ago = self.algo_helper.ma_minutes_ago(7, 2)
        ma11_2_min_ago = self.algo_helper.ma_minutes_ago(11, 2)
        ma16_2_min_ago = self.algo_helper.ma_minutes_ago(16, 2)
        ma34_2_min_ago = self.algo_helper.ma_minutes_ago(34, 2)
        ma43_2_min_ago = self.algo_helper.ma_minutes_ago(43, 2)
        
        # LAST TRADE
        last_trade_action = self.algo_helper.last_trade_action
        last_trade_time = self.algo_helper.last_trade_time
        last_trade_price = self.algo_helper.last_trade_price
        
        seconds_since_last_trade = 0
        if last_trade_time:
            seconds_since_last_trade = (datetime.now() - datetime.strptime(last_trade_time[:last_trade_time.index('.')], '%Y-%m-%dT%H:%M:%S')).seconds
            self.algo_helper.log('last trade time {}'.format(last_trade_time)) 
            self.algo_helper.log('seconds since last trade: {}'.format(seconds_since_last_trade))
        
        # CURRENT PRICE
        price = self.algo_helper.price
        
        # la deviaton stabilisce i limiti della VENDITA MENTRE SALE e della VENDITA MENTRE SCENDE.
        deviation = (price / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.log('deviation: {}'.format(deviation))
        
        action = None
      
    
        #######################################################################
        # APRE E CHIUDE GABBIA
        # SI APRE LA GABBIA SE 
        if ma43_last > ma43_2_min_ago:  
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
            
            #and ma100_last > ma100_2_min_ago
            #and ma11_prev < ma24_prev and ma11_last > ma24_last): CON QUESTA NON COMPRA MAI MA BUONO CHE LA ma11 STA SOPRA LA ma24
                
            # COMPRA sessione 1
            if self.session == 1:
                if (ma2_last > ma2_2_min_ago
                    and ma4_last > ma4_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma7_last > ma7_2_min_ago
                    and ma11_last > ma11_2_min_ago
                    and ma16_last > ma16_2_min_ago
                    and ma34_last > ma34_2_min_ago
                    and ma43_last > ma43_2_min_ago
                    and macd < 60):
                    action = 'buy'
                
            # COMPRA sessione 2
            elif self.session == 2:
                if (ma2_last > ma2_2_min_ago
                    and ma4_last > ma4_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma7_last > ma7_2_min_ago
                    and ma11_last > ma11_2_min_ago
                    and ma16_last > ma16_2_min_ago
                    and ma34_last > ma34_2_min_ago
                    and ma43_last > ma43_2_min_ago
                    and macd < 60):
                    action = 'buy'
              
            # COMPRA sessione 3 in poi
            else:
                if (ma2_last > ma2_2_min_ago
                    and ma4_last > ma4_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma7_last > ma7_2_min_ago
                    and ma11_last > ma11_2_min_ago
                    and ma16_last > ma16_2_min_ago
                    and ma34_last > ma34_2_min_ago
                    and ma43_last > ma43_2_min_ago
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

            # VENDE CON INCROCIO ma2 - ma7

            # VENDE sessione 1
            if self.session == 1:
                if ma2_prev > ma7_prev and ma2_last < ma7_last:
                    if deviation > 0.21 or deviation < -0.8:
                        action = 'sell'

            # VENDE sessione 2
            elif self.session == 2:   
                if ma2_prev > ma7_prev and ma2_last < ma7_last:
                    if deviation > 0.21 or deviation < -0.7:
                        action = 'sell'     
                        
            # VENDE sessione 3 in poi
            else:
                if (ma2_prev > ma7_prev and ma2_last < ma7_last):
                    if deviation > 0.21 or deviation < -0.6:
                        action = 'sell'
                    
            #FORSE QUI GLI DOBBIAMO DIRE CHE DEVE CHIUDERE LA GABBIA ) (?)
           
            # ATTESA max hold time
            if seconds_since_last_trade > max_hold_time_in_seconds:
                 action = 'sell'

        self.algo_helper.log('action {}'.format(action))

        if action == 'sell':
            self.session += 1

        return action
