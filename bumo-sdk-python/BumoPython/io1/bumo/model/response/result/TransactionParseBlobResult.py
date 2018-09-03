# encoding=utf-8
from typing import List

from io1.bumo.model.response.result.data.OperationFormat import OperationFormat


class TransactionParseBlobResult:
    sourceAddress = ""
    feeLimit = 0L
    gasPrice = 0L
    nonce = 0L
    operations = []  # type: List[OperationFormat]

    def getSourceAddress(self):
        return self.sourceAddress

    def setSourceAddress(self, sourceAddress):
        self.sourceAddress = sourceAddress

    def getFeeLimit(self):
        return self.feeLimit

    def setFeeLimit(self, feeLimit):
        self.feeLimit = feeLimit

    def getGasPrice(self):
        return self.gasPrice

    def setGasPrice(self, gasPrice):
        self.gasPrice = gasPrice

    def getNonce(self):
        return self.nonce

    def setNonce(self, nonce):
        self.nonce = nonce

    def getOperations(self):
        return self.operations

    def setOperations(self, operations):
        self.operations = operations
