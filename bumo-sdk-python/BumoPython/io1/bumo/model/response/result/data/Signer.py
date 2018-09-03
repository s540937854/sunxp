# encoding=utf-8
import json


class Signer:
    address = ""
    weight = 0L

    def parseDict(self, d):
        for i, j in d.items():
            # 基本类型处理，如字符串 数字等
            setattr(self, i, j)
        self.dict = d
        return self

    def __init__(self, address, weight):
        self.address = address
        self.weight = weight

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
