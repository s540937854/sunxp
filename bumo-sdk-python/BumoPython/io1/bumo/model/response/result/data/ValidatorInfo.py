# encoding=utf-8
import json


class ValidatorInfo:
    address = ""
    pledge_coin_amount = 0L

    def parseDict(self, d):
        for i, j in d.items():
            # 基本类型处理，如字符串 数字等
            setattr(self, i, j)
        self.dict = d
        return self

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getPledgeCoinAmount(self):
        return self.pledge_coin_amount

    def setPledgeCoinAmount(self, pledgeCoinAmount):
        self.pledge_coin_amount = pledgeCoinAmount

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
