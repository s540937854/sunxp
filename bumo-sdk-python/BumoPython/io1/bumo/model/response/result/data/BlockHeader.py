# encoding=utf-8
from io1.bumo.model.response.result.data.AssetInfo import AssetInfo


class BlockHeader:
    closeTime = 0L
    number = 0L
    txCount = 0L
    version = ""

    def getCloseTime(self):
        return self.closeTime

    def setCloseTime(self, closeTime):
        self.closeTime = closeTime

    def getNumber(self):
        return self.number

    def setNumber(self, number):
        self.number = number

    def getTxCount(self):
        return self.txCount

    def setTxCount(self, txCount):
        self.txCount = txCount

    def getVersion(self):
        return self.version

    def setVersion(self, version):
        self.version = version
