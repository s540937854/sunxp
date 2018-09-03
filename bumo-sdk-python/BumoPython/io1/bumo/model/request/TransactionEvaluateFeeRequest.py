# encoding=utf-8
from typing import List, Any

from io1.bumo.model.request.operation.BaseOperation import BaseOperation


class TransactionEvaluateFeeRequest:
    sourceAddress = ""
    nonce = 0L
    operations = []  # type: List[BaseOperation]
    signatureNumber = 0
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

    def getSignatureNumber(self):
        return self.signatureNumber

    def setSignatureNumber(self, signatureNumber):
        self.signatureNumber = signatureNumber

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
