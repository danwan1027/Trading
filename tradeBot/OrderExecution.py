from SignalList import *

class OrderExecution:
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        dispatcher.connect(self.buy, signal = BUY)
        dispatcher.connect(self.sell, signal = SELL)

    def buy(self):
        print("buy one stock")  

    def sell(self):
        print("sell one stock")