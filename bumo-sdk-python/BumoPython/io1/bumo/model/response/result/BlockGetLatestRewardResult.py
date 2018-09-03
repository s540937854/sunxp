# encoding=utf-8
from io1.bumo.model.response.result.data.ValidatorRewardInfo import ValidatorRewardInfo


class BlockGetLatestRewardResult:
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
