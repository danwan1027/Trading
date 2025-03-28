# import dispatcher
from Dispatcher import Dispatcher
from SignalList import *

# import Module
from OrderExecution import OrderExecution
from MarketData import MarketData
from BinanceAPIClient import BinanceAPIClient
from Strategy import Strategy
from RiskManagement import RiskManagement
from Logger import Logger


logger = Logger()
dispatcher = Dispatcher(logger)
order_operator = OrderExecution(dispatcher)
client = BinanceAPIClient()
market_data = MarketData(dispatcher, client, "BTCUSDT", "1s",)
strategy = Strategy(dispatcher, market_data)
risk_management = RiskManagement(dispatcher)


# main program
market_data.start_websocket()



