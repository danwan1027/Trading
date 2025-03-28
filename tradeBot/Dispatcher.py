from pydispatch import dispatcher
from SignalList import *

class Dispatcher:
    def __init__(self, logger):
        self.logger = logger
        pass

    def connect(self, calling_function, signal):
        """
        註冊接收函數 (calling_function) 用來接收特定信號 (signal)
        """
        dispatcher.connect(calling_function, signal=signal)

    def send(self, signal, *args, **kwargs):
        """
        發送信號，通知所有已註冊的接收函數
        """
        self.logger.log(f"Signal '{signal}' sent with args={args}, kwargs={kwargs}")
        dispatcher.send(signal, *args, **kwargs)
        

    def test(self, price):
        print(price)

