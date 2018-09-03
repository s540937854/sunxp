# encoding=utf-8
import json

from io1.bumo.model.response.result.data.AssetInfo import AssetInfo


class AssetSendInfo:
    dest_address = ""
    asset = None  # type: AssetInfo
    input = ""

    def parseDict(self, d):
        for i, j in d.items():
            if isinstance(j, dict):
                # 对象转换处理，转换成固定对象或者包含键值的当前对象
                if i == 'asset':
                    setattr(self, i, AssetInfo().parseDict(j))
                else:
                    setattr(self, i, self.parseDict(j))
            else:
                # 基本类型处理，如字符串 数字等
                setattr(self, i, j)
        self.dict = d
        return self

    def getDestAddress(self):
        return self.dest_address

    def setDestAddress(self, destAddress):
        self.dest_address = destAddress

    def getAsset(self):
        return self.asset

    def setAsset(self, asset):
        self.asset = asset

    def getInput(self):
        return self.input

    def setInput(self, input):
        self.input = input

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
