from SignalList import *

class RiskManagement:
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        dispatcher.connect(self.check_risk, signal = STRADEGY_CHECKED_BUY)

    def check_risk(self):
        self.dispatcher.send(signal = BUY)
        pass