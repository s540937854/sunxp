# encoding=utf-8


class Fees:
    baseReserve = 0L
    gasPrice = 0L

    def getBaseReserve(self):
        return self.baseReserve

    def setBaseReverse(self, baseReverse):
        self.baseReserve = baseReverse

    def getGasPrice(self):
        return self.gasPrice

    def setGasPrice(self, gasPrice):
        self.gasPrice = gasPrice
