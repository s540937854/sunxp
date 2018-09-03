# encoding=utf-8
from io1.bumo.model.response.result.data.Priv import Priv


class AccountGetInfoResult:
    address = ""
    balance = 0L
    nonce = 0L
    priv = None  # type: Priv

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
