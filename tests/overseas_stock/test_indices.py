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
    assert "output1" in resp  # 현재가 정보
    assert "output2" in resp  # 분봉 데이터
    
    output2 = resp["output2"]
    assert isinstance(output2, list)
    if output2:  # 데이터가 있는 경우에만 검증
        item = output2[0]
        assert "stck_bsop_date" in item  # 영업일자
        assert "stck_bsop_time" in item  # 영업시간
        assert "ovrs_nmix_prpr" in item  # 해외지수 현재가 