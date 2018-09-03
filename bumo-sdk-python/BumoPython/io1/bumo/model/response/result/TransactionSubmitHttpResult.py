# encoding=utf-8
import json


class TransactionSubmitHttpResult:
    hash = ""
    error_code = 0
    error_desc = ""

    def parseDict(self, d):
        for i, j in d.items():
            # 基本类型处理，如字符串 数字等
            setattr(self, i, j)
        self.dict = d
        return self

    def getHash(self):
        return self.hash

    def setHash(self, hash):
        self.hash = hash

    def getErrorCode(self):
        return self.error_code

    def setErrorCode(self, errorCode):
        self.error_code = errorCode

    def getErrorDesc(self):
        return self.error_desc

    def setErrorDesc(self, errorDesc):
        self.error_desc = errorDesc

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
