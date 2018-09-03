# encoding=utf-8

class AccountCreateResult:
    privateKey = ""
    publicKey = ""
    address = ""

    def getPrivateKey(self):
        return self.privateKey

    def setPrivateKey(self, privateKey):
        self.privateKey = privateKey

    def getPublicKey(self):
        return self.publicKey

    def setPublicKey(self, publicKey):
        self.publicKey = publicKey

    def getAddress(self):
        return self.address

    def setAddress(self,address):
        self.address = address
