# encoding=utf-8
import json


class AccountCreateResult:
    private_key = ""
    public_key = ""
    address = ""

    def parseDict(self, d):
        for i, j in d.items():
            # 基本类型处理，如字符串 数字等
            setattr(self, i, j)
        self.dict = d
        return self

    def getPrivateKey(self):
        return self.private_key

    def setPrivateKey(self, privateKey):
        self.private_key = privateKey

    def getPublicKey(self):
        return self.public_key

    def setPublicKey(self, publicKey):
        self.public_key = publicKey

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
