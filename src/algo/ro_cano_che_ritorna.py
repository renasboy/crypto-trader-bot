from datetime import datetime

class ro_cano_che_ritorna(object):

    def __init__(self, helper):
        self.algo_helper = helper
        self.session = 0
        self.open = False

    @property
    def action(self):
        
        # TIME dopo quanto tempo ro cano ritorna ( per esempio 60 minuti x 60 = 3600 secondi )

        # MACD
        macd = self.algo_helper.macd

        # MACD di 2-3-4 minuti prima
        #macd_2_min_ago = self.algo_helper.macd_minutes_ago(2)
        macd_3_min_ago = self.algo_helper.macd_minutes_ago(3)
        #macd_4_min_ago = self.algo_helper.macd_minutes_ago(4)
        
        # MAs
        #ma1_last, ma1_prev = self.algo_helper.ma_last_prev(1)
        #ma2_last, ma2_prev = self.algo_helper.ma_last_prev(2)
        #ma5_last, ma5_prev = self.algo_helper.ma_last_prev(5)  
        #ma7_last, ma7_prev = self.algo_helper.ma_last_prev(7)
        #ma8_last, ma8_prev = self.algo_helper.ma_last_prev(8)
        #ma9_last, ma9_prev = self.algo_helper.ma_last_prev(9)
        #ma10_last, ma10_prev = self.algo_helper.ma_last_prev(10)
        ma20_last, ma20_prev = self.algo_helper.ma_last_prev(20)
        #ma25_last, ma25_prev = self.algo_helper.ma_last_prev(25)
        #ma34_last, ma34_prev = self.algo_helper.ma_last_prev(34)
        #ma43_last, ma43_prev = self.algo_helper.ma_last_prev(43)
        #ma100_last, ma100_prev = self.algo_helper.ma_last_prev(100)
        
        # MA (2-5-8-20-43-100) di  x minuti prima
        #ma2_1_min_ago = self.algo_helper.ma_minutes_ago(2, 1)
        #ma5_3_min_ago = self.algo_helper.ma_minutes_ago(5, 3)
        #ma8_2_min_ago = self.algo_helper.ma_minutes_ago(8, 2)
        #ma8_3_min_ago = self.algo_helper.ma_minutes_ago(8, 3)
        #ma8_7_min_ago = self.algo_helper.ma_minutes_ago(8, 7)
        ma20_3_min_ago = self.algo_helper.ma_minutes_ago(20, 3)
        #ma43_3_min_ago = self.algo_helper.ma_minutes_ago(43, 3)
        #ma43_7_min_ago = self.algo_helper.ma_minutes_ago(43, 7)
        #ma100_5_min_ago = self.algo_helper.ma_minutes_ago(100, 5)
        
        # LAST TRADE
        last_trade_action = self.algo_helper.last_trade_action
        last_trade_time = self.algo_helper.last_trade_time

        seconds_since_last_trade = 0
        if last_trade_time:
            seconds_since_last_trade = (datetime.now() - datetime.strptime(last_trade_time[:last_trade_time.index('.')], '%Y-%m-%dT%H:%M:%S')).seconds
            self.algo_helper.log('last trade time {}'.format(last_trade_time)) 
            self.algo_helper.log('seconds since last trade: {}'.format(seconds_since_last_trade))
        
        # CURRENT PRICE
        price = self.algo_helper.price
        action = None
        
        
        
        
        
        
        
        
        
        
        
        
        # SI APRE LA GABBIA se macd > macd_3_min_ago
        if macd > macd_3_min_ago:
            if not self.session or not self.open:
               self.session = 1
               self.open = True
               self.algo_helper.log('session {}: open segment'.format(self.session))
        
        
        
        # COMPRA sessione 1
      
        # se macd > macd_3_min_ago 
        
        if (self.open and self.session and last_trade_action != 'buy'
        and macd > macd_3_min_ago):
        
        
                if self.session == 1:
                    action = 'buy'
                elif self.session == 2:
                    action = 'buy' 
                else:
                    action = 'buy' 
        
     
 






        # SI CHIUDE LA GABBIA se macd < macd_3_min_ago
        #if macd < macd_3_min_ago:
        #or seconds_since_last_trade > 1200:
            #self.open = False
            #self.algo_helper.log('session {}: closed segment'.format(self.session))
    
    
    
    
    
        # VENDE sessione 1
        
        
        # vende anche se (oppure se) macd < macd_3min_ago
        # anche se secondi passati della compra > 1200 (20 minuti)
    
            
        
        # vende
        elif last_trade_action == 'buy':
           
            if self.session == 1:
                if macd < macd_3_min_ago:
                    action = 'sell'
            elif self.session == 2:
                if macd < macd_3_min_ago:
                    action = 'sell' 
            else:
                if macd < macd_3_min_ago:
                    action = 'sell' 
            
            
            
            
           
            if seconds_since_last_trade > 1200:
                 action = 'sell'

        self.algo_helper.log('action {}'.format(action))

        if action == 'sell':
            self.session += 1

        return action
