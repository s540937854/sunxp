# encoding=utf-8
from io1.bumo.model.response.result.data.AssetInfo import AssetInfo


class BlockNumber:
    blockNumber = 0L

    def getBlockNumber(self):
        return self.blockNumber

    def setBlockNumber(self, blockNumber):
        self.blockNumber = blockNumber
