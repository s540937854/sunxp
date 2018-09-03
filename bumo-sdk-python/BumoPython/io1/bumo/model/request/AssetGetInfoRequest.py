# encoding=utf-8

class AssetGetInfoRequest:
    address = ""
    code = ""
    issuer = ""

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address

    def getCode(self):
        return self.code

    def setCode(self, code):
        self.code = code

    def getIssuer(self):
        return self.issuer

    def setIssuer(self, issuer):
        self.issuer = issuer
