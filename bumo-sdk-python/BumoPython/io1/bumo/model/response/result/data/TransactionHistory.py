# encoding=utf-8
from typing import List, Any

from io1.bumo.model.response.result.data.Signature import Signature
from io1.bumo.model.response.result.data.TransactionInfo import TransactionInfo


class TransactionHistory:
    actualFee = ""
    closeTime = 0L
    errorCode = 0
    errorDesc = ""
    hash = ""
    ledgerSeq = 0L
    signatures = []  # type: List[Signature]
    transaction = None  # type: TransactionInfo
    txSize = 0L

    def getActualFee(self):
        return self.actualFee

    def setActualFee(self, actualFee):
        self.actualFee = actualFee

    def getCloseTime(self):
        return self.closeTime

    def setCloseTime(self, closeTime):
        self.closeTime = closeTime

    def getErrorCode(self):
        return self.errorCode

    def setErrorCode(self, errorCode):
        self.errorCode = errorCode

    def getErrorDesc(self):
        return self.errorDesc

    def setErrorDesc(self, errorDesc):
        self.errorDesc = errorDesc

    def getHash(self):
        return self.hash

    def setHash(self, hash):
        self.hash = hash

    def getLedgerSeq(self):
        return self.ledgerSeq

    def setLedgerSeq(self, ledgerSeq):
        self.ledgerSeq = ledgerSeq

    def getSignatures(self):
        return self.signatures

    def setSignatures(self, signatures):
        self.signatures = signatures

    def getTransaction(self):
        return self.transaction

    def setTransaction(self, transaction):
        self.transaction = transaction

    def getTxSize(self):
        return self.txSize

    def setTxSize(self, txSize):
        self.txSize = txSize
