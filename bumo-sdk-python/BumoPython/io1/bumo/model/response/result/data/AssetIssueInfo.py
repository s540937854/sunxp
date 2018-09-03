# encoding=utf-8
import json


class AssetIssueInfo:
    code = ""
    amount = 0L

    def parseDict(self, d):
        for i, j in d.items():
            # 基本类型处理，如字符串 数字等
            setattr(self, i, j)
        self.dict = d
        return self

    def getCode(self):
        return self.code

    def setCode(self, code):
        self.code = code

    def getAmount(self):
        return self.amount

    def setAmount(self, amount):
        self.amount = amount

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
