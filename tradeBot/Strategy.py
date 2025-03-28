from SignalList import *

class Strategy:
    def __init__(self, dispatcher, market_data):
        self.dispatcher = dispatcher
        self.market_data = market_data
        
        dispatcher.connect(self.strategy, signal = PRICE_UPDATED)
    
    def strategy(self):
        self.dispatcher.send(signal = STRADEGY_CHECKED_BUY)
        pass