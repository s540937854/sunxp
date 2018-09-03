# encoding=utf-8
from typing import List, Any

from io1.bumo.model.request.operation.BaseOperation import BaseOperation


class TransactionBuildBlobRequest:
    sourceAddress = ""
    nonce = 0L
    gasPrice = 0L
    feeLimit = 0L
    operations = []  # type: List[BaseOperation]
    ceilLedgerSeq = 0L
    metadata = ""

    def getSourceAddress(self):
        return self.sourceAddress

    def setSourceAddress(self, sourceAddress):
        self.sourceAddress = sourceAddress

    def getNonce(self):
        return self.nonce

    def setNonce(self, nonce):
        self.nonce = nonce

    def getGasPrice(self):
        return self.gasPrice

    def setGasPrice(self, gasPrice):
        self.gasPrice = gasPrice

    def getFeeLimit(self):
        return self.feeLimit

    def setFeeLimit(self, feeLimit):
        self.feeLimit = feeLimit

    def getOperations(self):
        return self.operations

    def setOperations(self, operations):
        self.operations = operations

    def addOperation(self, operation):
        if not self.operations:
            self.operations = []
        self.operations.append(operation)

    def getCeilLedgerSeq(self):
        return self.ceilLedgerSeq

    def setCeiLedgerSeq(self, ceiLedgerSeq):
        self.ceilLedgerSeq = ceiLedgerSeq

    def getMetadata(self):
        return self.metadata

    def setMetadata(self, metadata):
        self.metadata = metadata
