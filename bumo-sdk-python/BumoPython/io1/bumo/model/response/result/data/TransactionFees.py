# encoding=utf-8
import json


class TransactionFees:
    fee_limit = 0L
    gas_price = 0L

    def parseDict(self, d):
        for i, j in d.items():
            # 基本类型处理，如字符串 数字等
            setattr(self, i, j)
        self.dict = d
        return self

    def getFeeLimit(self):
        return self.fee_limit

    def setFeeLimit(self, feeLimit):
        self.fee_limit = feeLimit

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
