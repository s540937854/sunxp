# encoding=utf-8
from io1.bumo.model.response.result.data.Signature import Signature


class TransactionSubmitRequest(object):
    transactionBlob = ""
    signatures = []  # type: List[Signature]

    def getTransactionBlob(self):
        return self.transactionBlob

    def setTransactionBlob(self, transactionBlob):
        self.transactionBlob = transactionBlob

    def getSignature(self):
        return self.signatures

    def setSignature(self, signatures):
        self.signatures = signatures

    def addSignature(self, signature):
        if not self.signatures:
            self.signatures = []
        self.signatures.append(signature)
