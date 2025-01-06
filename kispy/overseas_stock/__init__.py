from kispy.auth import KisAuth

from .account import AccountAPI
from .order import OrderAPI
from .quote import QuoteAPI
from .indices import IndicesAPI


class OverseasStock:
    def __init__(self, auth: KisAuth):
        self.account = AccountAPI(auth)
        self.order = OrderAPI(auth)
        self.quote = QuoteAPI(auth)
        self.indices = IndicesAPI(auth)
