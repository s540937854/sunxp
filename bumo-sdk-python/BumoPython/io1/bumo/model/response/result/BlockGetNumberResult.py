# encoding=utf-8
from io1.bumo.model.response.result.data.BlockNumber import BlockNumber


class BlockGetNumberResult:
    header = None  # type: BlockNumber

    def getHeader(self):
        return self.header

    def setHeader(self, header):
        self.header = header
