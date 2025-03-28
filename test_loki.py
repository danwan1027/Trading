import logging
import logging_loki
from datetime import datetime

# 設定 Loki Handler
handler = logging_loki.LokiHandler(
    url="http://localhost:3100/loki/api/v1/push",
    tags={"application": "trading-bot"},
    auth=("username", "password"),
    version="1",
)

# 設定 Logger
logger = logging.getLogger("trading-bot-logger")
logger.setLevel(logging.INFO)
logger.addHandler(handler)

# 交易機器人日誌模板
def log_trade_event(level, event_type, symbol, price, quantity, order_type, status, extra_tags=None):
    log_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "symbol": symbol,
        "price": price,
        "quantity": quantity,
        "order_type": order_type,
        "status": status,
    }
    if extra_tags:
        log_data["tags"] = extra_tags
    
    if level == "info":
        logger.info("Trade Event", extra={"tags": log_data})
    elif level == "warning":
        logger.warning("Trade Warning", extra={"tags": log_data})
    elif level == "error":
        logger.error("Trade Error", extra={"tags": log_data})
    elif level == "debug":
        logger.debug("Trade Debug", extra={"tags": log_data})

# 測試日誌
log_trade_event(
    level="info",
    event_type="order_placed",
    symbol="BTC/USDT",
    price=65000.5,
    quantity=0.01,
    order_type="limit",
    status="success",
    extra_tags={"strategy": "mean_reversion", "environment": "production"}
)

print("Trade log sent to Loki!")
