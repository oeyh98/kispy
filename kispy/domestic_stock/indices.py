"""
[국내주식] 지수
- 지수 조회
"""

from typing import Any, Literal, Dict, cast

from kispy.base import BaseAPI
from kispy.constants import REAL_URL


class DomesticStockIndices(BaseAPI):
    """국내주식 지수 조회 클래스"""

    def get_indices_price(
        self,
        index_code: str,
        market_code: Literal["U"] = "U",
    ) -> Dict[str, Any]: 
        """국내업종 현재지수 조회

        Args:
            index_code (str): 업종코드
                - 코스피: "0001"
                - 코스닥: "1001"
                - 코스피200: "2001"
            market_code (str): 시장 분류 코드. Defaults to "U" (업종)

        Returns:
            dict[str, Any]: 업종 현재지수 정보
                - output: 응답상세1
                    - bstp_nmix_prpr: 업종 지수 현재가
                    - bstp_nmix_prdy_vrss: 업종 지수 전일 대비
                    - prdy_vrss_sign: 전일 대비 부호
                    - bstp_nmix_prdy_ctrt: 업종 지수 전일 대비율
                    - acml_vol: 누적 거래량
                    - prdy_vol: 전일 거래량
                    - acml_tr_pbmn: 누적 거래 대금
                    - prdy_tr_pbmn: 전일 거래 대금
                    - bstp_nmix_oprc: 업종 지수 시가2
                    - bstp_nmix_hgpr: 업종 지수 최고가
                    - bstp_nmix_lwpr: 업종 지수 최저가
                    - ascn_issu_cnt: 상승 종목 수
                    - uplm_issu_cnt: 상한 종목 수
                    - stnr_issu_cnt: 보합 종목 수
                    - down_issu_cnt: 하락 종목 수
                    - lslm_issu_cnt: 하한 종목 수
        """

        path = "/uapi/domestic-stock/v1/quotations/inquire-index-price"
        url = f"{REAL_URL}{path}"
        headers = {
            "tr_id": "FHPUP02100000",
            "custtype": "P",
        }
        params = {
            "FID_COND_MRKT_DIV_CODE": market_code,
            "FID_INPUT_ISCD": index_code,
        }

        response = self._request(
            method="GET",
            url=url,
            headers=headers,
            params=params,
        )
        
        return cast(Dict[str, Any], response.json)

    def get_indices_daily_price(
        self,
        index_code: str,
        base_date: str,
        period_type: Literal["D", "W", "M"] = "D",
        market_code: Literal["U"] = "U",
    ) -> Dict[str, Any]:
        """국내업종 일자별지수 조회

        Args:
            index_code (str): 업종코드
                - 코스피: "0001"
                - 코스닥: "1001"
                - 코스피200: "2001"
            base_date (str): 기준일자 (YYYYMMDD)
            period_type (str): 기간 분류 코드. Defaults to "D".
                - "D": 일별
                - "W": 주별
                - "M": 월별
            market_code (str): 시장 분류 코드. Defaults to "U" (업종)

        Returns:
            dict[str, Any]: 업종 일자별 지수 정보
                - output1: 응답상세1 (현재가 정보)
                    - bstp_nmix_prpr: 업종 지수 현재가
                    - bstp_nmix_prdy_vrss: 업종 지수 전일 대비
                    - prdy_vrss_sign: 전일 대비 부호
                    - bstp_nmix_prdy_ctrt: 업종 지수 전일 대비율
                    - acml_vol: 누적 거래량
                    - acml_tr_pbmn: 누적 거래 대금
                    - bstp_nmix_oprc: 업종 지수 시가2
                    - bstp_nmix_hgpr: 업종 지수 최고가
                    - bstp_nmix_lwpr: 업종 지수 최저가
                - output2: 응답상세2 (일자별 데이터)
                    - stck_bsop_date: 주식 영업 일자
                    - bstp_nmix_prpr: 업종 지수 현재가
                    - prdy_vrss_sign: 전일 대비 부호
                    - bstp_nmix_prdy_vrss: 업종 지수 전일 대비
                    - bstp_nmix_prdy_ctrt: 업종 지수 전일 대비율
                    - bstp_nmix_oprc: 업종 지수 시가2
                    - bstp_nmix_hgpr: 업종 지수 최고가
                    - bstp_nmix_lwpr: 업종 지수 최저가
                    - acml_vol: 누적 거래량
                    - acml_tr_pbmn: 누적 거래 대금
                    - invt_new_psdg: 투자 신 심리도
                    - d20_dsrt: 20일 이격도
        """
        path = "/uapi/domestic-stock/v1/quotations/inquire-index-daily-price"
        url = f"{REAL_URL}{path}"
        headers = {
            "tr_id": "FHPUP02120000",
            "custtype": "P",
        }
        params = {
            "FID_COND_MRKT_DIV_CODE": market_code,
            "FID_INPUT_ISCD": index_code,
            "FID_INPUT_DATE_1": base_date,
            "FID_PERIOD_DIV_CODE": period_type,
        }

        response = self._request(
            method="GET",
            url=url,
            headers=headers,
            params=params,
        )
        
        return cast(Dict[str, Any], response.json)