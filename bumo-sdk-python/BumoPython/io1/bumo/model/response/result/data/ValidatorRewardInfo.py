# encoding=utf-8

class ValidatorRewardInfo:
    validator = ""
    reward = 0L

    def getValidator(self):
        return self.validator

    def setValidator(self, validator):
        self.validator = validator

    def getReward(self):
        return self.reward

    def setReward(self, reward):
        self.reward = reward
