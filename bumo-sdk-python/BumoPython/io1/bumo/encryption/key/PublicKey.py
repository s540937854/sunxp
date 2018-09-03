# encoding=utf-8
import base58 as base58
import ed25519
from ed25519._ed25519 import BadSignatureError

from io1.bumo.encryption.common.CheckKey import CheckKey
from io1.bumo.encryption.exception.EncException import EncException
from io1.bumo.encryption.model.KeyMember import KeyMember
from io1.bumo.encryption.model.KeyType import KeyType


class PublicKey:
    def __init__(self, encPublicKey=None):
        self.__keyMember = KeyMember()
        if encPublicKey:
            self.getPublicKey(encPublicKey, self.__keyMember)

    def setEncPublicKey(self, encPublicKey):
        self.getPublicKey(encPublicKey, self.__keyMember)

    def setRawPublicKey(self, rawPKey):
        """
        set raw public key
        :param rawPKey: raw public key
        :return:
        """
        self.__keyMember.setRawPKey(rawPKey)

    def getRawPublicKey(self):
        """
        get raw public key
        :return:raw public key
        """
        return self.__keyMember.getRawPKey()

    def setKeyType(self, keyType):
        """
        set key type
        :param keyType: key type
        :return:
        """
        self.__keyMember.setKeyType(keyType)

    def getKeyType(self):
        """
        get key type
        :return: key type
        """
        return self.__keyMember.getKeyType()

    def getEncAddress(self, pKey=None):
        if pKey:
            self.getPublicKey(pKey, self.__keyMember)
            return self.encAddress(self.__keyMember.getKeyType(), self.__keyMember.getRawPKey())
        else:
            raw_pkey = self.__keyMember.getRawPKey()
            if not raw_pkey:
                raise EncException("public key is null")
            return self.encAddress(self.__keyMember.getKeyType(), raw_pkey)

    def isAddressValid(self, encAddress):
        return self.encAddressValid(encAddress)

    def isPublicKeyValid(self, encPulickKey):
        return self.encPublicKeyValid(encPulickKey)

    def verify(self, msg, signMsg, encPublicKey=None):
        if encPublicKey:
            member = KeyMember()
            self.getPublicKey(encPublicKey, member)
            verifySuccess = self.verifyMessage(msg, signMsg, member)
            return verifySuccess
        else:
            verifySuccess = self.verifyMessage(msg, signMsg, self.__keyMember)
            return verifySuccess

    def getPublicKey(self, bPkey=None, member=None):
        if not bPkey:
            raise EncException("public key cannot be null")
        buffPkey = bPkey
        if len(buffPkey) < 6:
            raise EncException("public key (" + bPkey + ") is invalid, please check")
        if buffPkey[0] != chr(0xB0):
            raise EncException("public key (" + bPkey + ") is invalid, please check")
        if buffPkey[1] != chr(1):
            raise EncException("public key (" + bPkey + ") is invalid, please check")
        keyType = KeyType.ED25519
        if not CheckKey().CheckSum(keyType, buffPkey):
            raise EncException("public key (" + bPkey + ") is invalid, please check")
        rawPKey = buffPkey[2:len(buffPkey) - 4]
        member.setRawPKey(rawPKey)
        member.setKeyType(keyType)

    def encPublicKeyValid(self, encPublicKey):
        valid = False
        try:
            if not encPublicKey:
                raise EncException("Invalid publicKey")
            buffPKey = encPublicKey
            if len(buffPKey) < 6 or buffPKey[0] != chr(176) or buffPKey[1] != chr(1):
                raise EncException("Invalid publicKey")
            lenth = len(buffPKey)
            checkSum = buffPKey[lenth - 4:lenth]
            buff = buffPKey[0:lenth - 4]
            hash1 = CheckKey().CalHash(KeyType.ED25519, buff)
            hash2 = CheckKey().CalHash(KeyType.ED25519, hash1)
            checkSumCol = hash2[0:4]
            if checkSum != checkSumCol:
                raise EncException("Invalid publicKey")
            valid = True
        except EncException:
            valid = False
        return valid

    def encAddress(self, keyType, raw_pkey):
        buff = ""
        buff = buff + chr(1)
        buff = buff + chr(86)
        buff = buff + chr(1)
        hashPkey = CheckKey().CalHash(keyType, raw_pkey)
        buff = buff + hashPkey[12:32]
        hash1 = CheckKey().CalHash(keyType, buff)
        hash2 = CheckKey().CalHash(keyType, hash1)
        temp = buff + hash2[0:4]
        base58.alphabet = b'123456789AbCDEFGHJKLMNPQRSTuVWXYZaBcdefghijkmnopqrstUvwxyz'
        return base58.b58encode(temp)

    def encAddressValid(self, encAddress):
        valid = False
        try:
            if not encAddress:
                raise EncException("Invalid address")
            base58.alphabet = b'123456789AbCDEFGHJKLMNPQRSTuVWXYZaBcdefghijkmnopqrstUvwxyz'
            adTemp = base58.b58decode(encAddress)
            if len(adTemp) != 27 or adTemp[0] != chr(1) or adTemp[1] != chr(86) or adTemp[2] != chr(1):
                raise EncException("Invalid address")
            lenth = len(adTemp)
            checkSum = adTemp[lenth - 4:lenth]
            buff = adTemp[0:lenth - 4]
            hash1 = CheckKey().CalHash(KeyType.ED25519, buff)
            hash2 = CheckKey().CalHash(KeyType.ED25519, hash1)
            checkSumCol = hash2[0:4]
            if checkSum != checkSumCol:
                raise EncException("Invalid address")
            valid = True
        except EncException:
            valid = False
        return valid

    def verifyMessage(self, msg, sign, member):
        """
        :param msg:srcAddress
        :param sign:PrivateKey.sign
        :param member:
        :return:
        """
        verifySuccess = False
        try:
            if member.getKeyType() == KeyType.ED25519:
                verifyingKey = ed25519.VerifyingKey(member.getRawPKey())
                verifyingKey.verify(sign, msg)
                return True
            else:
                raise EncException('type does not exist')
        except EncException:
            verifySuccess = False
        except BadSignatureError:
            verifySuccess = False
        return verifySuccess
