# encoding=utf-8


class BlockRewardJsonResult:
    blockReward = 0L
    validatorsReward = ""  # type jsonobjectd对象

    def getBlockReward(self):
        return self.blockReward

    def setBlockReward(self, blockReward):
        self.blockReward = blockReward

    def getValidatorsReward(self):
        return self.validatorsReward

    def setValidatorsReward(self, validatorsReward):
        self.validatorsReward = validatorsReward
