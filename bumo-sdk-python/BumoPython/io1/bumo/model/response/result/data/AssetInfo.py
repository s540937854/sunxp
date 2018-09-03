# encoding=utf-8
from io1.bumo.model.response.result.data.AssetKey import AssetKey


class AssetInfo:
    key = None  # type: AssetKey
    amount = 0L

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key

    def getAmount(self):
        return self.amount

    def setAmount(self, amount):
        self.amount = amount
