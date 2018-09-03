# encoding=utf-8
import json


class AccountCheckActivatedResult:
    is_activated = False

    def parseDict(self, d):
        for i, j in d.items():
            # 基本类型处理，如字符串 数字等
            setattr(self, i, j)
        self.dict = d
        return self

    def getIsActivated(self):
        return self.is_activated

    def setIsActivated(self, isActivated):
        self.is_activated = isActivated

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
