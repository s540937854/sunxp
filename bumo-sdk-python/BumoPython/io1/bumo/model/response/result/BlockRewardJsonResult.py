# encoding=utf-8
import json


class BlockRewardJsonResult:
    block_reward = 0L
    validators_reward = ""  # type jsonobjectd对象

    def parseDict(self, d):
        for i, j in d.items():
            if isinstance(j, dict):
                # 对象转换处理，转换成固定对象或者包含键值的当前对象
                setattr(self, i, self.parseDict(j))
            else:
                # 基本类型处理，如字符串 数字等
                setattr(self, i, j)
        self.dict = d
        return self

    def getBlockReward(self):
        return self.block_reward

    def setBlockReward(self, blockReward):
        self.block_reward = blockReward

    def getValidatorsReward(self):
        return self.validators_reward

    def setValidatorsReward(self, validatorsReward):
        self.validators_reward = validatorsReward

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
