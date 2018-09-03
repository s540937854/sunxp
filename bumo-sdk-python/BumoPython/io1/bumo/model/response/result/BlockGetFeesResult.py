# encoding=utf-8
from io1.bumo.model.response.result.data.Fees import Fees


class BlockGetFeesResult:
    fees = None  # type: Fees

    def getFees(self):
        return self.fees

    def setFees(self, fees):
        self.fees = fees
