# encoding=utf-8
from io1.bumo.model.response.result.data.AssetInfo import AssetInfo


class AssetGetInfoResult:
    assets = []  # type: list[AssetInfo]

    def getAssets(self):
        return self.assets

    def setAssets(self, assets):
        self.assets = assets
