import json
from tradeBot.BinanceAPIClient import BinanceAPIClient

client = BinanceAPIClient()

def my_callback(data):
    """處理 WebSocket 傳來的數據"""
    print("收到 WebSocket 訊息：", json.dumps(data, indent=2, ensure_ascii=False))

# 訂閱 BTC/USDT 的即時價格
client.subscribe_ticker("BTCUSDT", my_callback)