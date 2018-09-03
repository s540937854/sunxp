# encoding=utf-8
from io1.bumo.encryption.key.PrivateKey import PrivateKey


class Keypair:
    def __init__(self, address, publicKey, privateKey):
        self.address = address
        self.publicKey = publicKey
        self.privateKey = privateKey

    @classmethod
    def generator(cls):
        try:
            priKey = PrivateKey()
            return Keypair(priKey.getEncAddress(), priKey.getEncPublicKey(), priKey.getEncPrivateKey())
        except Exception, e:
            repr(e)

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getPublicKey(self):
        return self.publicKey

    def setPublicKey(self, publicKey):
        self.publicKey = publicKey

    def getPrivateKey(self):
        return self.privateKey

    def setPrivateKey(self, privateKey):
        self.privateKey = privateKey
