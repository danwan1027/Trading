import requests
import asyncio
import websockets
import json
import os
from dotenv import load_dotenv
from SignalList import *

load_dotenv()

class BinanceAPIClient:
    BASE_URL = "https://api.binance.com"
    WS_URL = "wss://stream.binance.com:9443/ws"
    
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")
        self.headers = {"X-MBX-APIKEY": self.api_key} if self.api_key else {}
    
    def _request(self, method, endpoint, params=None, data=None):
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.request(method, url, headers=self.headers, params=params, json=data)
        return response.json()
    
    # 測試連線
    def test_connectivity(self):
        return self._request("GET", "/api/v3/ping")
    
    # 市場數據
    def get_price(self, symbol):
        return self._request("GET", "/api/v3/ticker/price", {"symbol": symbol})
    
    def get_order_book(self, symbol, limit=5):
        return self._request("GET", "/api/v3/depth", {"symbol": symbol, "limit": limit})
    
    def get_klines(self, symbol, interval, limit=100):
        return self._request("GET", "/api/v3/klines", {"symbol": symbol, "interval": interval, "limit": limit})
    
    # 帳戶資訊
    def get_account_info(self):
        return self._request("GET", "/api/v3/account")
    
    # 交易
    def create_order(self, symbol, side, type, quantity, price=None):
        data = {
            "symbol": symbol,
            "side": side,
            "type": type,
            "quantity": quantity,
        }
        if price:
            data["price"] = price
        return self._request("POST", "/api/v3/order", data=data)
    
    def cancel_order(self, symbol, orderId):
        return self._request("DELETE", "/api/v3/order", {"symbol": symbol, "orderId": orderId})
    
    # WebSocket 訂閱
    async def _ws_listener(self, stream, callback):
        async with websockets.connect(f"{self.WS_URL}/{stream}") as websocket:
            while True:
                data = await websocket.recv()
                callback(json.loads(data))
    
    # 即時價格
    def subscribe_ticker(self, symbol, callback):
        stream = f"{symbol.lower()}@ticker"
        asyncio.run(self._ws_listener(stream, callback))
    
    # 訂單簿
    def subscribe_depth(self, symbol, callback):
        stream = f"{symbol.lower()}@depth"
        asyncio.run(self._ws_listener(stream, callback))
    
    # k 棒
    def subscribe_kline(self, symbol, interval, callback):
        stream = f"{symbol.lower()}@kline_{interval}"
        asyncio.run(self._ws_listener(stream, callback))