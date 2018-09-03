# encoding=utf-8
from typing import List, Any

from io1.bumo.model.response.result.data.Operation import Operation


class TransactionInfo:
    sourceAddress = ""
    feeLimit = 0L
    gasPrice = 0L
    nonce = 0L
    metadata = ""
    operations = []  # type: List[Operation]

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

    def getMetadata(self):
        return self.metadata

    def setMetadata(self, metadata):
        self.metadata = str.decode(metadata, 'hex')

    def getOperations(self):
        return self.operations

    def setOperations(self, operations):
        self.operations = operations
