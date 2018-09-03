# encoding=utf-8
import json


class Fees:
    base_reserve = 0L
    gas_price = 0L

    def parseDict(self, d):
        for i, j in d.items():
            # 基本类型处理，如字符串 数字等
            setattr(self, i, j)
        self.dict = d
        return self

    def getBaseReserve(self):
        return self.base_reserve

    def setBaseReverse(self, baseReverse):
        self.base_reserve = baseReverse

    def getGasPrice(self):
        return self.gas_price

    def setGasPrice(self, gasPrice):
        self.gas_price = gasPrice

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
