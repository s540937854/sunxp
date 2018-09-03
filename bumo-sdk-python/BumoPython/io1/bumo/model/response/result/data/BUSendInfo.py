# encoding=utf-8

class BUSendInfo:
    destAddress = ""
    amount = 0L
    input = ""

    def getDestAddress(self):
        return self.destAddress

    def setDestAddress(self, destAddress):
        self.destAddress = destAddress

    def getAmount(self):
        return self.amount

    def setAsset(self, amount):
        self.amount = amount

    def getInput(self):
        return self.input

    def setInput(self, input):
        self.input = input
