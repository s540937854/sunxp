# encoding=utf-8
from io1.bumo.model.response.result.data.AssetInfo import AssetInfo


class AssetSendInfo:
    destAddress = ""
    asset = None  # type: AssetInfo
    input = ""

    def getDestAddress(self):
        return self.destAddress

    def setDestAddress(self, destAddress):
        self.destAddress = destAddress

    def getAsset(self):
        return self.asset

    def setAsset(self, asset):
        self.asset = asset

    def getInput(self):
        return self.input

    def setInput(self, input):
        self.input = input
