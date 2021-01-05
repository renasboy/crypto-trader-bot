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

        # MACD di 1-2-3-4 minuti prima
        #macd_1_min_ago = self.algo_helper.macd_minutes_ago(1) NON METTERE MAI !
        macd_2_min_ago = self.algo_helper.macd_minutes_ago(2)
        #macd_3_min_ago = self.algo_helper.macd_minutes_ago(3)
        #macd_4_min_ago = self.algo_helper.macd_minutes_ago(4)
        #macd_5_min_ago = self.algo_helper.macd_minutes_ago(5)
        
        
        # moving average (2-3-4-5-x)
        #ma1_last, ma1_prev = self.algo_helper.ma_last_prev(1) NON METTERE MAI !
        ma2_last, ma2_prev = self.algo_helper.ma_last_prev(2)
        #ma3_last, ma3_prev = self.algo_helper.ma_last_prev(3)
        ma4_last, ma4_prev = self.algo_helper.ma_last_prev(4)
        ma5_last, ma5_prev = self.algo_helper.ma_last_prev(5)  
        ma6_last, ma6_prev = self.algo_helper.ma_last_prev(6)  
        #ma7_last, ma7_prev = self.algo_helper.ma_last_prev(7)
        ma8_last, ma8_prev = self.algo_helper.ma_last_prev(8)
        #ma9_last, ma9_prev = self.algo_helper.ma_last_prev(9)
        #ma10_last, ma10_prev = self.algo_helper.ma_last_prev(10)
        ma11_last, ma11_prev = self.algo_helper.ma_last_prev(11)
        #ma13_last, ma13_prev = self.algo_helper.ma_last_prev(13)
        #ma20_last, ma20_prev = self.algo_helper.ma_last_prev(20)
        ma24_last, ma24_prev = self.algo_helper.ma_last_prev(24)
        ma34_last, ma34_prev = self.algo_helper.ma_last_prev(34)
        #ma43_last, ma43_prev = self.algo_helper.ma_last_prev(43)
        #ma100_last, ma100_prev = self.algo_helper.ma_last_prev(100)
        #ma200_last, ma200_prev = self.algo_helper.ma_last_prev(200)
        
        
        # moving average (2-3-4-5-7-8-20-43-100) di x minuti prima (NON METTERE MAI 1 min !)
        ma2_2_min_ago = self.algo_helper.ma_minutes_ago(2, 2) 
        ma2_3_min_ago = self.algo_helper.ma_minutes_ago(2, 3)
        #ma3_2_min_ago = self.algo_helper.ma_minutes_ago(3, 2)
        ma4_2_min_ago = self.algo_helper.ma_minutes_ago(4, 2)
        ma5_2_min_ago = self.algo_helper.ma_minutes_ago(5, 2)
        #ma7_2_min_ago = self.algo_helper.ma_minutes_ago(7, 2)
        ma8_2_min_ago = self.algo_helper.ma_minutes_ago(8, 2)
        #ma8_3_min_ago = self.algo_helper.ma_minutes_ago(8, 3)
        #ma8_7_min_ago = self.algo_helper.ma_minutes_ago(8, 7)
        ma11_2_min_ago = self.algo_helper.ma_minutes_ago(11, 2)
        #ma13_2_min_ago = self.algo_helper.ma_minutes_ago(13, 2)
        #ma20_2_min_ago = self.algo_helper.ma_minutes_ago(20, 2)
        ma24_2_min_ago = self.algo_helper.ma_minutes_ago(24, 2)
        ma34_2_min_ago = self.algo_helper.ma_minutes_ago(34, 2)
        #ma43_3_min_ago = self.algo_helper.ma_minutes_ago(43, 3)
        #ma43_7_min_ago = self.algo_helper.ma_minutes_ago(43, 7)
        #ma100_5_min_ago = self.algo_helper.ma_minutes_ago(100, 5)
        #ma200_3_min_ago = self.algo_helper.ma_minutes_ago(200, 3)
        
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
        
        
        
        
        
        
        
        
        
        
        
        
        # SI APRE LA GABBIA (PENSAVO CHE NON FUNZIONASSE) ( E INVECE HO CAMBIATO LA "if (ma8_last > ma8_2_min_ago):" E IL CANO NON FUNZIONAVA PIU' !)
        # if ma8_last > ma8_2_min_ago
        
        # e se macd > macd_2_min_ago
        # e se ma4_last > ma4_2_min_ago
        # e se ma8_last > ma8_3_min_ago
        # e se ma20_last > ma20_3_min_ago
        # e se ma100_last > ma100_5_min_ago
        # e se ma200_last > ma200_3_min_ago
        # ( questa in un secondo momento ) e se ma200_prev and ma200_last and ma20_prev < ma200_prev and ma20_last >= ma200_last:
   
        
        if (ma34_last > ma34_2_min_ago):  
            #macd > macd_2_min_ago
            #and ma4_last > ma4_2_min_ago
            #"and if" ma8_last > ma8_3_min_ago
            #"and if" ma20_last > ma20_3_min_ago
            #"and if" ma100_last > ma100_5_min_ago
            #"and if" ma200_last > ma200_3_min_ago
            # ( questa in un secondo momento ) "and if" ma200_prev and ma200_last and ma20_prev < ma200_prev and ma20_last >= ma200_last:
            
            if not self.session or not self.open:
               self.session = 1
               self.open = True
               self.algo_helper.log('session {}: open segment'.format(self.session))
        
        
        
        # COMPRA sessione 1
      
        # se macd > macd_2_min_ago 
        # e se ma4_last > ma4_2_min_ago
        # e se ma8_last > ma8_3_min_ago
        # e se ma20_last > ma20_3_min_ago
        # e se ma100_last > ma100_5_min_ago
        # e se ma200_last > ma200_3_min_ago
        # ( questa in un secondo momento ) e se ma200_prev and ma200_last and ma20_prev < ma200_prev and ma20_last >= ma200_last:
        
       
        if (self.open and self.session and last_trade_action != 'buy'    
            and ma2_last > ma2_2_min_ago
            and ma4_last > ma4_2_min_ago
            and ma5_last > ma5_2_min_ago
            and ma11_last > ma11_2_min_ago
            and ma24_last > ma24_2_min_ago
            and ma34_last > ma34_2_min_ago):
            #and ma11_prev < ma24_prev and ma11_last > ma24_last): CON QUESTA NON COMPRA MAI MA BUONO CHE LA ma11 STA SOPRA LA ma24
            
            
            #and ma2_last > ma2_3_min_ago
            #and ma8_last > ma8_2_min_ago):
            
            #and ma8_last>ma8_3_min_ago
            #and ma100_last > ma100_5_min_ago
            
            #and macd > macd_2_min_ago
            
            #"and if" ma20_last>ma20_3_min_ago
            
            #"and if" ma200_last > ma200_3_min_ago
            # ( questa in un secondo momento ) "and if" ma200_prev and ma200_last and ma20_prev < ma200_prev and ma20_last >= ma200_last:
            
            
            
                if self.session == 1:
                    action = 'buy'
                    
                    
                    
                elif (self.open and self.session and last_trade_action != 'buy'  
                    and ma2_last > ma2_2_min_ago
                    and ma2_last > ma2_3_min_ago
                    and ma4_last > ma4_2_min_ago
                    and ma5_last > ma5_2_min_ago
                    and ma8_last > ma8_2_min_ago
                    and ma11_last > ma11_2_min_ago
                    and ma24_last > ma24_2_min_ago
                    and macd > macd_2_min_ago):
                      
                      
                    #and ma8_last > ma8_2_min_ago (LA MA8 DALLA SECONDA SESSIONE IN POI PER RENDERE L' ACQUISTO UN PO' PIU' DIFFICILE MA, FORSE, PIU' SICURO.)
                    #and ma2_last > ma2_3_min_ago (LA MA2 > MA 3 min AGO DALLA SECONDA SESSIONE IN POI PER RENDERE L' ACQUISTO UN PO' PIU' DIFFICILE MA, FORSE, PIU' SICURO.)
                    #and macd > macd_2_min_ago ( IL MACD >MACD 2 min AGO DALLA SECONDA SESSIONE IN POI PER RENDERE L' ACQUISTO UN PO' PIU' DIFFICILE MA, FORSE, PIU' SICURO.)
                    #if ma2_last > ma2_2_min_ago
                    #and ma4_last > ma4_2_min_ago
                    
                    #and ma13_last > ma13_2_min_ago):
                    
                    
                elif self.session == 2:
                    action = 'buy' 
                    
                    
                    
                else:
                    action = 'buy' 
        
     
 






        # SI CHIUDE LA GABBIA ( non e' necessario chiuderla )
 
        #if macd < macd_2_min_ago:
        #or seconds_since_last_trade > 3600:
            #self.open = False
            #self.algo_helper.log('session {}: closed segment'.format(self.session))
    
    
    
    
    
        # VENDE sessione 1
        
        # VENDE CON INCROCIO ma2 - ma4
        
        # vende anche se (oppure se) macd < macd_2_min_ago
        # vende anche se macd < macd_1_min_ago NON METTERE !
        # vende anche se macd < macd_3_min_ago
        # vende anche se macd_1_min_ago < macd_2_min_ago
        # vende anche se macd_4_min_ago < macd_5_min_ago
        # anche se secondi passati della compra > 3600 (60 minuti)
    
        #"oppure" se ma7_last < ma7_2_min_ago
        
        # vende
        elif last_trade_action == 'buy':
            #self.algo_helper.log('MACD: {}'.format(macd)) questa riga fa comparire la variabile sul log
            if self.session == 1:
                if ma2_prev > ma4_prev and ma2_last < ma4_last:
                    if deviation > 0.20 or deviation < -0.70: 
                        
                        action = 'sell'
                    
                    #(VENDITA MENTRE SALE e VENDITA MENTRE SCENDE) 
                    
                    
               
                    
                
                    #(ma5_last < ma5_2_min_ago
                    #and ma3_last < ma3_2_min_ago):
                    
                    #and macd < macd_2_min_ago
                    #and macd < macd_3_min_ago  lettera a di and allineata con la m di ma5 di sopra e togli la parentesei e i ":" sopra 
                    #and macd_2_min_ago < macd_3_min_ago
                    
                    
                
                #elif (ma2_prev > ma4_prev and ma2_last < ma4_last):
                
                
                
                       #ma2_prev > ma5_prev and ma2_last < ma5_last):
                       #(ma5_last < ma5_2_min_ago
                       #and ma3_last < ma3_2_min_ago):
                        
                       #macd < macd_2_min_ago
                       #and macd < macd_3_min_ago
                       #macd_2_min_ago < macd_3_min_ago):
                       
                
                    #action = 'sell'
                        
                        
            elif self.session == 2:   
                if ma2_prev > ma4_prev and ma2_last < ma4_last:
                    if deviation > 0.20 or deviation < -0.80: 
                        action = 'sell'     
                    
                    
                    #ma2_prev > ma5_prev and ma2_last < ma5_last):
                    #(ma5_last < ma5_2_min_ago
                    #and ma3_last < ma3_2_min_ago):
                    
                    #macd < macd_2_min_ago
                    #and macd < macd_3_min_ago
                    #and macd_2_min_ago < macd_3_min_ago):
                    
                        
            else:
                if (ma2_prev > ma4_prev and ma2_last < ma4_last):
                    if deviation > 0.20 or deviation < -0.80: 
                        action = 'sell'
                    
                    #ma2_prev > ma5_prev and ma2_last < ma5_last):
                    #(ma5_last < ma5_2_min_ago
                    #and ma3_last < ma3_2_min_ago):
                    
                    #macd < macd_2_min_ago
                    #and macd < macd_3_min_ago
                    #and macd_2_min_ago < macd_3_min_ago):
           
                         
            
            
            
            
           
            if seconds_since_last_trade > 3600:
                 action = 'sell'

        self.algo_helper.log('action {}'.format(action))

        if action == 'sell':
            self.session += 1

        return action
