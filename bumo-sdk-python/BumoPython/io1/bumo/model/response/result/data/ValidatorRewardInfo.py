# encoding=utf-8
import json


class ValidatorRewardInfo:
    validator = ""
    reward = 0L

    def parseDict(self, d):
        for i, j in d.items():
            # 基本类型处理，如字符串 数字等
            setattr(self, i, j)
        self.dict = d
        return self

    def getValidator(self):
        return self.validator

    def setValidator(self, validator):
        self.validator = validator

    def getReward(self):
        return self.reward

    def setReward(self, reward):
        self.reward = reward

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
