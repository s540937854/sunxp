# encoding=utf-8

class TransactionBuildBlobResult:
    transactionBlob = ""
    hash = ""

    def getTransactionBlob(self):
        return self.transactionBlob

    def setTransactionBlob(self, transactionBlob):
        self.transactionBlob = transactionBlob

    def getHash(self):
        return self.hash

    def setHash(self, hash):
        self.hash = hash
