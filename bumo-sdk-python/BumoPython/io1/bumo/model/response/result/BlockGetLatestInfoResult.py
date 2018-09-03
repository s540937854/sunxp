# encoding=utf-8
from io1.bumo.model.response.result.data.BlockHeader import BlockHeader


class BlockGetLatestInfoResult:
    header = None  # type: BlockHeader

    def getHeader(self):
        return self.header

    def setHeader(self, header):
        self.header = header
