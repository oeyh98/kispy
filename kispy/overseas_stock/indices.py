"""
[해외주식] 지수
- 지수 조회
- 해외지수분봉조회
"""
from kispy.base import BaseAPI


class IndicesAPI(BaseAPI):
    def get_indices_minute_chart(
        self, 
        index_code: str,
        market_code: str = "N",
        hour_div: str = "0",
        include_past_data: str = "Y",
    ) -> dict:
        """
        해외지수분봉조회[v1_해외주식-031]

        Args:
            index_code (str): 지수코드 (예: SPX)
            market_code (str): 조건 시장 분류 코드 (N: 해외지수, X: 환율, KX: 원화환율)
            hour_div (str): 시간 구분 코드 (0: 정규장, 1: 시간외)
            include_past_data (str): 과거 데이터 포함 여부 (Y/N)

        Returns:
            dict: 해외지수 분봉 데이터

        실전계좌의 경우, 최근 102건까지 확인 가능합니다.
        """
        path = "uapi/overseas-price/v1/quotations/inquire-time-indexchartprice"
        url = f"{self._url}/{path}"

        tr_id = "FHKST03030200"  # 실전투자만 지원

        headers = self._auth.get_header()
        headers["tr_id"] = tr_id

        params = {
            "FID_COND_MRKT_DIV_CODE": market_code,  # 조건 시장 분류 코드
            "FID_INPUT_ISCD": index_code,  # 입력 종목코드
            "FID_HOUR_CLS_CODE": hour_div,  # 시간 구분 코드
            "FID_PW_DATA_INCU_YN": include_past_data,  # 과거 데이터 포함 여부
        }

        resp = self._request(method="get", url=url, headers=headers, params=params)
        return resp.json
