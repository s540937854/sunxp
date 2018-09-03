# encoding=utf-8
from typing import List, Any


class TransactionSignRequest:
    blob = ""
    privateKeys = []  # type: List[str]

    def getBlob(self):
        return self.blob

    def setBlob(self, blob):
        self.blob = blob

    def getPrivateKeys(self):
        return self.privateKeys

    def setPrivateKeys(self, privateKeys):
        self.privateKeys = privateKeys

    def addPrivateKey(self, privateKey):
        if not self.privateKeys:
            self.privateKeys = []
        self.privateKeys.append(privateKey)
