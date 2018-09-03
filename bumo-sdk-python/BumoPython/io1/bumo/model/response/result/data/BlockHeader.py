# encoding=utf-8
import json

from io1.bumo.model.response.result.data.AssetInfo import AssetInfo


class BlockHeader:
    close_time = 0L
    number = 0L
    tx_count = 0L
    version = ""

    def parseDict(self, d):
        for i, j in d.items():
            # 基本类型处理，如字符串 数字等
            setattr(self, i, j)
        self.dict = d
        return self

    def getCloseTime(self):
        return self.close_time

    def setCloseTime(self, closeTime):
        self.close_time = closeTime

    def getNumber(self):
        return self.number

    def setNumber(self, number):
        self.number = number

    def getTxCount(self):
        return self.tx_count

    def setTxCount(self, txCount):
        self.tx_count = txCount

    def getVersion(self):
        return self.version

    def setVersion(self, version):
        self.version = version

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
