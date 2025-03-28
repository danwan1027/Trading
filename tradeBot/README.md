# Binance API Documentation

[Binance API Documentation｜Web-socket-api](https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-api.md)

[Binance API Documentation｜Rest-api](https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md)


# Structure

### 主要模組
1. MarketData : 訂閱 k 棒，並且存放歷史 k 棒數據
2. Strategy
3. RiskManagement
4. OrderExecution
5. PositionManagement

### 其他模組
1. main.py : 用來初始化 instance, 並以開始訂閱 k 棒為整個交易機器人的開端
2. BinanceAPIClient : 都是被其他模組呼叫的，整理在一起統一管理 API
3. SignalList : 用來存放所有的 signal
4. Dispatcher : 事件總線
5. Logger : logging

### 訊號
###### 種類
PRICE_UPDATED = "price_updated" </br>
STRADEGY_CHECKED_BUY = "stradegy_checked_buy" </br>
STRADEGY_CHECKED_SELL = "stradegy_checked_sell" </br>
RISK_CHECKED_BUY = "risk_checked_buy" </br>
RISK_CHECKED_SELL = "risk_checked_sell" </br>
BUY = "buy" </br>
SELL = "sell" </br>
ORDER_PLACED = "order_placed" </br>
ORDER_FILLED = "order_filled" </br>
STOP_LOSS = "stop_loss" </br>
TAKE_PROFIT = "take_profit" </br>

###### 訊號流
```mermaid
graph LR;
    MarketData --> |PRICE_UPDATED| Strategy;
    Strategy --> |STRADEGY_CHECKED_BUY or STRADEGY_CHECKED_SELL| RiskManagement;
    RiskManagement --> |BUY or SELL| OrderExecution;
```


---
Docker 包含 Grafana 以及 Loki