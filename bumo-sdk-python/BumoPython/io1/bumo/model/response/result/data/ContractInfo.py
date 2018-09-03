# encoding=utf-8
import json


class ContractInfo:
    type = 0
    payload = ""

    def parseDict(self, d):
        for i, j in d.items():
            # 基本类型处理，如字符串 数字等
            setattr(self, i, j)
        self.dict = d
        return self

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getPayload(self):
        return self.payload

    def setPaylaod(self, payload):
        self.payload = payload

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
