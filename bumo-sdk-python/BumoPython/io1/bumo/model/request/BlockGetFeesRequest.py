# encoding=utf-8

class BlockGetFeesRequest:
    blockNumber = 0L

    def getBlockNumber(self):
        return self.blockNumber

    def setBlockNumber(self, blockNumber):
        self.blockNumber = blockNumber
