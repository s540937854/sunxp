# encoding=utf-8
from typing import List

from io1.bumo.model.response.result.data.OperationFormat import OperationFormat


class TransactionSubmitHttpResult:
    hash = ""
    errorCode = 0
    errorDesc = ""

    def getHash(self):
        return self.hash

    def setHash(self, hash):
        self.hash = hash

    def getErrorCode(self):
        return self.errorCode

    def setErrorCode(self, errorCode):
        self.errorCode = errorCode

    def getErrorDesc(self):
        return self.errorDesc

    def setErrorDesc(self, errorDesc):
        self.errorDesc = errorDesc
