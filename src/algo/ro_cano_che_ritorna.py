from datetime import datetime

class ro_cano_che_ritorna(object):

    def __init__(self, helper):
        self.algo_helper = helper
        self.session = 0

    @property
    def action(self):

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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

        # compra sempre e subito
        if last_trade_action != 'buy':
            action = 'buy'

        # vende
        if last_trade_action == 'buy':

            # solo se secondi passati della compra > 3600 (60 minuti)
            if seconds_since_last_trade > 3600:
                action = 'sell'

        self.algo_helper.log('action {}'.format(action))

        if action == 'buy':
            self.session += 1

        return action
