from kispy.auth import KisAuth
from kispy.client import KisClient


def test_get_indices_minute_chart(auth: KisAuth):
    indices = KisClient(auth).overseas_stock.indices
    resp = indices.get_indices_minute_chart(
        index_code="SPX",  # S&P 500
        market_code="N",  # 해외지수
        hour_div="0",  # 정규장
        include_past_data="Y"
    )

    assert isinstance(resp, dict)
    # 현재가 정보 검증
    assert "output1" in resp
    output1 = resp["output1"]
    assert "ovrs_nmix_prdy_clpr" in output1  # 해외 지수 전일 종가
    assert "ovrs_nmix_prpr" in output1  # 해외 지수 현재가
    assert "ovrs_nmix_prdy_vrss" in output1  # 해외 지수 전일 대비
    assert "prdy_vrss_sign" in output1  # 전일 대비 부호
    
    # 분봉 데이터 검증
    assert "output2" in resp
    output2 = resp["output2"]
    assert isinstance(output2, list)
    if output2:  # 데이터가 있는 경우에만 검증
        item = output2[0]
        # OHLCV 데이터
        assert "optn_prpr" in item  # 현재가 (종가)
        assert "optn_oprc" in item  # 시가
        assert "optn_hgpr" in item  # 고가
        assert "optn_lwpr" in item  # 저가
        assert "cntg_vol" in item  # 거래량 