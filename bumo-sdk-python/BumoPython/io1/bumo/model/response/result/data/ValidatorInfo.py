# encoding=utf-8

class ValidatorInfo:
    address = ""
    pledgeCoinAmount = 0L

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getPledgeCoinAmount(self):
        return self.pledgeCoinAmount

    def setPledgeCoinAmount(self, pledgeCoinAmount):
        self.pledgeCoinAmount = pledgeCoinAmount
