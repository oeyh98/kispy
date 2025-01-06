import concurrent.futures
import logging
from concurrent.futures import as_completed
from pprint import pprint

import pandas as pd

from kispy import KisAuth, KisClientV2, KisClient
from kispy.models.account import Order

# set log level
logging.basicConfig(level=logging.INFO)

KISPY_APP_KEY = ""
KISPY_APP_SECRET = ""
KISPY_ACCOUNT_NO = ""


auth = KisAuth(KISPY_APP_KEY, KISPY_APP_SECRET, KISPY_ACCOUNT_NO, is_real=True)
client = KisClientV2(auth, "US")


symbol = "TSLL"
start_date = None
end_date = None
period = "1m"
limit = None
quantity = 1

# 실시간 가격 조회
price = client.get_price(symbol)
print(f"price: {price}")

price = "11"

# 기간별 시세 조회
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = [
        executor.submit(client.fetch_ohlcv, symbol, start_date, end_date, period=period, limit=None) for _ in range(10)
    ]
    for future in as_completed(futures):
        ohlcvs = future.result()
        df = pd.DataFrame([ohlcv.model_dump() for ohlcv in ohlcvs])
        print(f"ohlcv: {df}")

# 주문 생성
# order_id = client.create_order(symbol, "buy", price, quantity)
# print(f"order_id: {order_id}")

# order_id = client.create_order(symbol, "sell", price, quantity)
# print(f"order_id: {order_id}")

# 주문 취소
# client.cancel_order(symbol, order_id)

# 잔고 조회
balance = client.fetch_balance()
pprint(balance)

# 보유종목 조회
positions = client.fetch_positions()
pprint(positions)

# 미체결 내역 조회
pending_orders = client.fetch_pending_orders()
pprint(pending_orders)

# 총 자산 조회
summary = client.fetch_account_summary()
pprint(summary)

# # 주문 조회
# orders = client.client.overseas_stock.order.inquire_orders(start_date, end_date)
# for order in orders:
#     order_obj = Order.from_response(order)
#     print(order_obj)

# order_id = "0030036440"
# order = client.fetch_order(order_id)
# pprint(order)


from kispy.utils import get_overseas_master_data

print(get_overseas_master_data("AMS"))