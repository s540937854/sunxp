# encoding=utf-8
import json


class Signature:
    sign_data = ""
    public_key = ""

    def parseDict(self, d):
        for i, j in d.items():
            # 基本类型处理，如字符串 数字等
            setattr(self, i, j)
        self.dict = d
        return self

    def getSignData(self):
        return self.sign_data

    def setSignData(self, signData):
        self.sign_data = signData

    def getPublicKey(self):
        return self.public_key

    def setPublicKey(self, publicKey):
        self.public_key = publicKey

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
