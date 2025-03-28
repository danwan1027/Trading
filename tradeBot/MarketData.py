import pandas as pd
from datetime import datetime
from SignalList import *
from BinanceAPIClient import BinanceAPIClient  # 確保這個檔案名稱正確

class MarketData:
    def __init__(self, dispatcher, client, symbol, interval, max_size=100):
        self.dispatcher = dispatcher
        self.client = client
        self.symbol = symbol.upper()
        self.interval = interval
        self.max_size = max_size
        self.df = pd.DataFrame(columns=['time', 'open', 'high', 'low', 'close', 'volume'])
        
        # **透過 BinanceAPIClient 取得前 100 根 K 線**
        self._fetch_historical_klines()

    def _fetch_historical_klines(self):
        """用 BinanceAPIClient 取得前 100 根 K 線"""
        klines = self.client.get_klines(self.symbol, self.interval, 100)
        if isinstance(klines, list):
            data = [{
                'time': datetime.fromtimestamp(k[0] / 1000),
                'open': float(k[1]),
                'high': float(k[2]),
                'low': float(k[3]),
                'close': float(k[4]),
                'volume': float(k[5])
            } for k in klines]
            
            self.df = pd.DataFrame(data)
        else:
            print("API 回應錯誤:", klines)

    def update_klines(self, data):
        """處理來自 WebSocket 的 K 線數據"""
        kline = data['k']
        new_kline = {
            'time': datetime.fromtimestamp(kline['t'] / 1000),
            'open': float(kline['o']),
            'high': float(kline['h']),
            'low': float(kline['l']),
            'close': float(kline['c']),
            'volume': float(kline['v'])
        }
        
        # 更新最後一根 K 線或加入新的
        if not self.df.empty and self.df.iloc[-1]['time'] == new_kline['time']:
            self.df.iloc[-1] = new_kline
        else:
            self.df = pd.concat([self.df, pd.DataFrame([new_kline])], ignore_index=True)
        
        # 只保留最近 max_size 根 K 線
        if len(self.df) > self.max_size:
            self.df = self.df.iloc[-self.max_size:]

        # 事件總線 
        self.dispatcher.send(signal = PRICE_UPDATED)

    def get_klines(self):
        """返回存儲的 K 線數據"""
        return self.df

    def start_websocket(self):
        """透過 BinanceAPIClient 訂閱 K 線 WebSocket"""
        self.client.subscribe_kline(self.symbol, self.interval, self.update_klines)
