from kispy.auth import KisAuth
from kispy.client import KisClient


def test_get_indices_price(auth: KisAuth):
    indices = KisClient(auth).domestic_stock.indices
    resp = indices.get_indices_price(
        index_code="0001",  # KOSPI
        market_code="U"
    )

    assert isinstance(resp, dict)
    assert "output" in resp
    output = resp["output"]
    assert "bstp_nmix_prpr" in output  # 업종 지수 현재가
    assert "bstp_nmix_prdy_vrss" in output  # 업종 지수 전일 대비
    assert "prdy_vrss_sign" in output  # 전일 대비 부호
    assert "bstp_nmix_prdy_ctrt" in output  # 업종 지수 전일 대비율


def test_get_indices_daily_price(auth: KisAuth):
    indices = KisClient(auth).domestic_stock.indices
    resp = indices.get_indices_daily_price(
        index_code="0001",  # KOSPI
        base_date="20240101",
        period_type="D",
        market_code="U"
    )

    assert isinstance(resp, dict)
    assert "output1" in resp  # 현재가 정보
    assert "output2" in resp  # 일자별 데이터
    
    output1 = resp["output1"]
    assert "bstp_nmix_prpr" in output1  # 업종 지수 현재가
    assert "bstp_nmix_prdy_vrss" in output1  # 업종 지수 전일 대비
    assert "prdy_vrss_sign" in output1  # 전일 대비 부호
    
    output2 = resp["output2"]
    assert isinstance(output2, list)
    if output2:  # 데이터가 있는 경우에만 검증
        item = output2[0]
        assert "stck_bsop_date" in item  # 주식 영업 일자
        assert "bstp_nmix_prpr" in item  # 업종 지수 현재가
        assert "prdy_vrss_sign" in item  # 전일 대비 부호 