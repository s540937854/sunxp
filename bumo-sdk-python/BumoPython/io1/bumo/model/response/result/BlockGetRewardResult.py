# encoding=utf-8
from io1.bumo.model.response.result.data.ValidatorRewardInfo import ValidatorRewardInfo


class BlockGetRewardResult:
    blockReward = 0L
    rewardResults = []  # type: list[ValidatorRewardInfo]

    def getBlockReward(self):
        return self.blockReward

    def setBlockReward(self, blockReward):
        self.blockReward = blockReward

    def getRewardResults(self):
        return self.rewardResults

    def setRewardResults(self, rewardResults):
        self.rewardResults = rewardResults

    def addRewareResult(self, rewardResult):
        if not self.rewardResults:
            self.rewardResults = []
        self.rewardResults.append(rewardResult)
