from dataclasses import dataclass
from datetime import datetime
from typing import Any, Self

from kispy.constants import ExchangeCode
from kispy.models.base import CustomBaseModel


@dataclass
class Symbol:
    symbol: str
    exchange_code: ExchangeCode
    realtime_symbol: str


class OHLCV(CustomBaseModel):
    date: datetime
    open: str
    high: str
    low: str
    close: str
    volume: str

    @classmethod
    def from_response(cls, response: dict[str, Any]) -> Self:
        if "stck_cntg_hour" in response:  # 국내주식 1분봉 데이터
            date = datetime.strptime(response["stck_bsop_date"] + response["stck_cntg_hour"], "%Y%m%d%H%M%S")
            open=response["stck_oprc"]
            high=response["stck_hgpr"]
            low=response["stck_lwpr"]
            close = response["stck_prpr"]
            volume = response["cntg_vol"]

        elif "stck_bsop_date" in response:  # 국내주식 일/주/월/년 데이터
            date = datetime.strptime(response["stck_bsop_date"], "%Y%m%d")
            open=response["stck_oprc"]
            high=response["stck_hgpr"]
            low=response["stck_lwpr"]
            close=response["stck_clpr"]
            volume=response["acml_vol"]
            
        elif "xhms" in response:  # 해외주식 분봉 데이터
            date = datetime.strptime(response["xymd"] + response["xhms"], "%Y%m%d%H%M%S")
            open=response["open"]
            high=response["high"]
            low=response["low"]
            close = response["last"]
            volume = response["evol"]

        else:  # 해외주식 일/주/월 데이터
            date = datetime.strptime(response["xymd"], "%Y%m%d")
            open=response["open"]
            high=response["high"]
            low=response["low"]
            close = response["clos"]
            volume = response["tvol"]

        return cls(
            date=date,
            open=open,
            high=high,
            low=low,
            close=close,
            volume=volume,
        )
