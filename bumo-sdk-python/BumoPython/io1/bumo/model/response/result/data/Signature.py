# encoding=utf-8

class Signature:
    signData = ""
    publicKey = ""

    def getSignData(self):
        return self.signData

    def setSignData(self, signData):
        self.signData = signData

    def getPublicKey(self):
        return self.publicKey

    def setPublicKey(self, publicKey):
        self.publicKey = publicKey
