# encoding=utf-8
from typing import List

from io1.bumo.model.response.result.data.AssetInfo import AssetInfo


class AccountGetAssetsResult:
    assets = []  # type: List[AssetInfo]

    def getAssets(self):
        return self.assets

    def setAssets(self, assets):
        self.assets = assets
