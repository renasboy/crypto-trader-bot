from datetime import datetime

class ro_cano_che_ritorna(object):

    def __init__(self, helper):
        self.algo_helper = helper
        self.session = 0
        self.open = False

    @property
    def action(self):
        
        # TIME dopo quanto tempo ro cano ritorna ( per esempio 60 minuti x 60 = 3600 secondi )

        # MACD di 1-2-3-4 minuti prima
        macd = self.algo_helper.macd
        
        macd_2_min_ago = self.algo_helper.macd_minutes_ago(2)
        
      
        # moving average (2-3-4-5-x)
        
        ma2_last, ma2_prev = self.algo_helper.ma_last_prev(2)
        ma4_last, ma4_prev = self.algo_helper.ma_last_prev(4)
        ma5_last, ma5_prev = self.algo_helper.ma_last_prev(5)  
        ma6_last, ma6_prev = self.algo_helper.ma_last_prev(6)  
        ma7_last, ma7_prev = self.algo_helper.ma_last_prev(7)
        ma8_last, ma8_prev = self.algo_helper.ma_last_prev(8)
        ma11_last, ma11_prev = self.algo_helper.ma_last_prev(11)
        ma16_last, ma16_prev = self.algo_helper.ma_last_prev(16)
        ma34_last, ma34_prev = self.algo_helper.ma_last_prev(34)
        ma43_last, ma43_prev = self.algo_helper.ma_last_prev(43)
        
        #ma100_last, ma100_prev = self.algo_helper.ma_last_prev(100)
        
        
        
        # moving average (2-3-4-5-7-8-20-43-100) di x minuti prima (NON METTERE MAI 1 min !)
        ma2_2_min_ago = self.algo_helper.ma_minutes_ago(2, 2) 
        ma4_2_min_ago = self.algo_helper.ma_minutes_ago(4, 2)
        ma5_2_min_ago = self.algo_helper.ma_minutes_ago(5, 2)
        ma7_2_min_ago = self.algo_helper.ma_minutes_ago(7, 2)
        ma8_2_min_ago = self.algo_helper.ma_minutes_ago(8, 2)
        ma11_2_min_ago = self.algo_helper.ma_minutes_ago(11, 2)
        ma16_2_min_ago = self.algo_helper.ma_minutes_ago(16, 2)
        ma34_2_min_ago = self.algo_helper.ma_minutes_ago(34, 2)
        ma43_2_min_ago = self.algo_helper.ma_minutes_ago(43, 2)
        
        #ma100_2_min_ago = self.algo_helper.ma_minutes_ago(100, 2)
        
        
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
        
        # deviation
        deviation = (price / last_trade_price - 1) * 100 if last_trade_price else 0
        self.algo_helper.log('deviation: {}'.format(deviation))
        
        
        
        
        action = None
      
        
    
        
        
        # SI APRE LA GABBIA SE 
        
        if (ma43_last > ma43_2_min_ago):  
           
            
            
            if not self.session or not self.open:
               self.session = 1
               self.open = True
               self.algo_helper.log('session {}: open segment'.format(self.session))
        
        
        
        # COMPRA sessione 1
      
        if (self.open and self.session and last_trade_action != 'buy'    
            and ma2_last > ma2_2_min_ago
            and ma4_last > ma4_2_min_ago
            and ma5_last > ma5_2_min_ago
            and ma8_last > ma8_2_min_ago
            and ma11_last > ma11_2_min_ago
            and ma16_last > ma16_2_min_ago
            and ma24_last > ma24_2_min_ago
            and ma34_last > ma34_2_min_ago
            and ma43_last > ma43_2_min_ago
            and macd < 60):
            
            #and ma100_last > ma100_2_min_ago
            #and ma11_prev < ma24_prev and ma11_last > ma24_last): CON QUESTA NON COMPRA MAI MA BUONO CHE LA ma11 STA SOPRA LA ma24
            
               
                
                if self.session == 1:
                    action = 'buy'
                    
                    
                    
                elif (self.open and self.session and last_trade_action != 'buy'
                    and ma2_last > ma2_2_min_ago
                    and ma2_last > ma2_3_min_ago
                    and ma4_last > ma4_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma8_last > ma8_2_min_ago 
                    and macd > macd_2_min_ago):  
                    
                    
                    action = 'buy'
                      
                    
                  
                    
                elif self.session == 2:
                    action = 'buy' 
                  
                else:
                    action = 'buy' 
       
    
    
        # VENDE sessione 1
        # VENDE CON INCROCIO ma2 - ma7
        
        elif last_trade_action == 'buy':
            #self.algo_helper.log('MACD: {}'.format(macd)) questa riga fa comparire la variabile sul log
            if self.session == 1:
                if ma2_prev > ma7_prev and ma2_last < ma7_last:
                    if deviation > 0.21 or deviation < -0.70: 
                        
                        action = 'sell'
                    
                    # la deviaton stabilisce i termini della VENDITA MENTRE SALE e della VENDITA MENTRE SCENDE.
                    
                     
                        
            elif self.session == 2:   
                if ma2_prev > ma7_prev and ma2_last < ma7_last:
                    if deviation > 0.21 or deviation < -0.60: 
                        action = 'sell'     
                     
                        
            else:
                if (ma2_prev > ma7_prev and ma2_last < ma7_last):
                    if deviation > 0.21 or deviation < -0.50: 
                        action = 'sell'
                    
                    
                   
            #FORSE QUI GLI DOBBIAMO DIRE CHE DEVE CHIUDERE LA GABBIA ) (?)
            
           
            if seconds_since_last_trade > 7200:
                 action = 'sell'

        self.algo_helper.log('action {}'.format(action))

        if action == 'sell':
            self.session += 1

        return action
