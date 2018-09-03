# encoding=utf-8
import json


class BUSendInfo:
    dest_address = ""
    amount = 0L
    input = ""

    def parseDict(self, d):
        for i, j in d.items():
            # 基本类型处理，如字符串 数字等
            setattr(self, i, j)
        self.dict = d
        return self

    def getDestAddress(self):
        return self.dest_address

    def setDestAddress(self, destAddress):
        self.dest_address = destAddress

    def getAmount(self):
        return self.amount

    def setAsset(self, amount):
        self.amount = amount

    def getInput(self):
        return self.input

    def setInput(self, input):
        self.input = input

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
