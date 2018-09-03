# encoding=utf-8
from io1.bumo.model.response.result.data.Priv import Priv
import json


class AccountGetInfoResult:
    address = ""
    balance = 0L
    nonce = 0L
    priv = None  # type: Priv

    def parseDict(self, d):
        for i, j in d.items():
            if isinstance(j, dict):
                # 对象转换处理，转换成固定对象或者包含键值的当前对象
                if i == 'pri':
                    setattr(self, i, Priv().parseDict(j))
                else:
                    setattr(self, i, self.parseDict(j))
            else:
                # 基本类型处理，如字符串 数字等
                setattr(self, i, j)
        self.dict = d
        return self

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getBalance(self):
        return self.balance

    def setBalance(self, balance):
        self.balance = balance

    def getNonce(self):
        return self.nonce

    def setNonce(self, nonce):
        self.nonce = nonce

    def getPriv(self):
        return self.priv

    def setPriv(self, priv):
        self.priv = priv

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
