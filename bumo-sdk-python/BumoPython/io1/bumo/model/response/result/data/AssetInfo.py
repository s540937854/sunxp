# encoding=utf-8
import json

from io1.bumo.model.response.result.data.AssetKey import AssetKey


class AssetInfo:
    key = None  # type: AssetKey
    amount = 0L

    def parseDict(self, d):
        for i, j in d.items():
            if isinstance(j, dict):
                # 对象转换处理，转换成固定对象或者包含键值的当前对象
                if i == "key":
                    setattr(self, i, AssetKey().parseDict(j))
            else:
                # 基本类型处理，如字符串 数字等
                setattr(self, i, j)
        self.dict = d
        return self

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key

    def getAmount(self):
        return self.amount

    def setAmount(self, amount):
        self.amount = amount

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
