# encoding=utf-8
from typing import List, Any


class TransactionFees:
    feeLimit = 0L
    gasPrice = 0L

    def getFeeLimit(self):
        return self.feeLimit

    def setFeeLimit(self, feeLimit):
        self.feeLimit = feeLimit

    def getGasPrice(self):
        return self.gasPrice

    def setGasPrice(self, gasPrice):
        self.gasPrice = gasPrice
