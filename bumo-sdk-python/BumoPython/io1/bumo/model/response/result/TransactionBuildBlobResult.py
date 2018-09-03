# encoding=utf-8
import json


class TransactionBuildBlobResult:
    transaction_blob = ""
    hash = ""

    def parseDict(self, d):
        for i, j in d.items():
            # 基本类型处理，如字符串 数字等
            setattr(self, i, j)
        self.dict = d
        return self

    def getTransactionBlob(self):
        return self.transaction_blob

    def setTransactionBlob(self, transactionBlob):
        self.transaction_blob = transactionBlob

    def getHash(self):
        return self.hash

    def setHash(self, hash):
        self.hash = hash

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
