# encoding=utf-8
from io1.bumo.encryption.model.KeyType import KeyType


class KeyMember:
    """
    KeyMember类
    """

    def __init__(self):
        self.__RawSKey = ""
        self.__rawPKey = ""
        self.__keyType = KeyType.ED25519

    def setRawSKey(self, rawSkey):
        self.__RawSKey = rawSkey

    def setRawPKey(self, rawPkey):
        self.__rawPKey = rawPkey

    def setKeyType(self, keytype):
        self.__keyType = keytype

    def getRawSKey(self):
        return self.__RawSKey

    def getRawPKey(self):
        return self.__rawPKey

    def getKeyType(self):
        return self.__keyType
