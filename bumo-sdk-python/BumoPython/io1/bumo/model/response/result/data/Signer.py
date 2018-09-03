# encoding=utf-8

class Signer:
    address = ""
    weight = 0L

    def __init__(self, address, weight):
        self.address = address
        self.weight = weight

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight
