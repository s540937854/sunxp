# encoding=utf-8
from os import urandom

import base58
import ed25519

from io1.bumo.encryption.common.CheckKey import CheckKey
from io1.bumo.encryption.exception.EncException import EncException
from io1.bumo.encryption.key.PublicKey import PublicKey
from io1.bumo.encryption.model.KeyMember import KeyMember
from io1.bumo.encryption.model.KeyType import KeyType


class PrivateKey:
    def __init__(self, skey=None):
        self.__keyMember = KeyMember()
        self.publicKey = PublicKey()
        if skey:
            self.__initBySkey(skey)
        else:
            self.__initByType(KeyType.ED25519)

    def __initByType(self, keyType):
        if keyType == KeyType.ED25519:
            sk, vk = ed25519.create_keypair(urandom)
            self.__keyMember.setRawSKey(sk.to_seed())
            rawPKey = self.getPublicKey(self.__keyMember)
            self.publicKey.setRawPublicKey(rawPKey)
        else:
            pass
        self.setKeyType(keyType)
        self.publicKey.setKeyType(keyType)

    def __initBySkey(self, skey):
        self.getPrivateKey(skey, self.__keyMember)
        self.publicKey.setKeyType(self.__keyMember.getKeyType())
        rawPKey = self.getPublicKey(self.__keyMember)
        self.publicKey.setRawPublicKey(rawPKey)
        self.__keyMember.setRawPKey(rawPKey)

    def setKeyType(self, keyType):
        self.__keyMember.setKeyType(keyType)

    def getKeyType(self):
        return self.__keyMember.getKeyType()

    def setRawPrivateKey(self, rawSKey):
        self.__keyMember.setRawSKey(rawSKey)

    def getRawPrivateKey(self):
        return self.__keyMember.getRawSKey()

    def getPublicKey(self):
        return self.publicKey

    def getEncPrivateKey(self):
        rawSKey = self.__keyMember.getRawSKey()
        if not rawSKey:
            raise EncException("raw private key is null")
        return self.EncPrivateKey(self.__keyMember.getKeyType(), rawSKey)

    def isPrivateKeyValid(self, encPrivateKey):
        return self.encPrivateKeyValid(encPrivateKey)

    def getEncPublicKey(self, skey=None):
        if not skey:
            rawPKey = self.publicKey.getRawPublicKey()
            if not rawPKey:
                raise EncException("raw public key is null")
            enPubkey = self.encPublicKey(self.__keyMember.getKeyType(), rawPKey)
            return enPubkey
        else:
            self.__keymember = KeyMember()
            self.getPrivateKey(skey, self.__keyMember)
            rawPKey = self.getPublicKey(self.__keyMember)
            enPubkey = self.encPublicKey(self.__keyMember.getKeyType(), rawPKey)
            return enPubkey

    def isPublicKeyValid(self, encPublicKey):
        return PublicKey().isPublicKeyValid(encPublicKey)

    def getEncAddress(self, pKey=None):
        if pKey:
            return PublicKey().getEncAddress(pKey)
        else:
            return self.publicKey.getEncAddress()

    def isAddressValid(self, encAddress):
        return PublicKey().isAddressValid(encAddress)

    def sign(self, msg, skey=None):
        if skey:
            member = KeyMember()
            self.getPrivateKey(skey, member)
            rawPKey = self.getPublicKey(member)
            member.setRawPKey(rawPKey)
            return self.signMessage(msg, member)
        else:
            return self.signMessage(msg, self.__keyMember)

    def getPrivateKey(self, bSkey, member):
        if not bSkey:
            raise EncException("Private key cannot be null")
        base58.alphabet = b'123456789AbCDEFGHJKLMNPQRSTuVWXYZaBcdefghijkmnopqrstUvwxyz'
        sKeyTemp = base58.b58decode(bSkey)
        if len(sKeyTemp) <= 9:
            raise EncException("Private key (" + bSkey + ") is invalid")
        if ord(sKeyTemp[3]) != 1:
            raise EncException("Private key (" + bSkey + ") is invalid")
        type = KeyType.ED25519
        if not CheckKey().CheckSum(type, sKeyTemp):
            raise EncException("Private key (" + bSkey + ") is invalid")
        rawSkey = sKeyTemp[4:len(sKeyTemp) - 5]
        member.setKeyType(type)
        member.setRawSKey(rawSkey)

    def getPublicKey(self, keyMember):
        if keyMember.getKeyType() != KeyType.ED25519:
            raise EncException("Type does not exist")
        else:
            sk = ed25519.SigningKey(keyMember.getRawSKey())
            vk = sk.get_verifying_key()
            rawPKey = vk.to_bytes()
        return rawPKey

    def EncPrivateKey(self, keytype, raw_skey):
        '''
        生成私钥
        :param keytype: KeyType 用于存储算法类型(Ed25519)和版本号默认1
        :param raw_skey:
        :return:
        '''
        if not raw_skey:
            raise EncException("Private key is null")
        buff = ""
        buff = buff + chr(int(0xDA))
        buff = buff + chr(int(0x37))
        buff = buff + chr(int(0x9F))
        buff = buff + chr(1)
        buff = buff + str(raw_skey)
        buff = buff + chr(0)
        hash1 = CheckKey().CalHash(keytype, buff)
        hash2 = CheckKey().CalHash(keytype, hash1)
        temp = buff + hash2[0:4]
        base58.alphabet = b'123456789AbCDEFGHJKLMNPQRSTuVWXYZaBcdefghijkmnopqrstUvwxyz'
        print "this is privateKey :", base58.b58encode(temp)
        return base58.b58encode(temp)

    def encPrivateKeyValid(self, encPrivateKey):
        valid = False
        try:
            if not encPrivateKey:
                raise EncException("Invalid privateKey")
            base58.alphabet = b'123456789AbCDEFGHJKLMNPQRSTuVWXYZaBcdefghijkmnopqrstUvwxyz'
            priKeyTemp = base58.b58decode(encPrivateKey)
            condition1 = len(priKeyTemp) != 41
            condition2 = priKeyTemp[0] != chr(218)
            condition3 = priKeyTemp[1] != chr(55)
            condition4 = priKeyTemp[2] != chr(159)
            condition5 = priKeyTemp[3] != chr(1)
            if condition1 or condition2 or condition3 or condition4 or condition5:
                raise EncException("Invalid privateKey")
            lenth = len(priKeyTemp)
            checkSum = priKeyTemp[lenth - 4:lenth]
            buff = priKeyTemp[0:lenth - 4]
            hash1 = CheckKey().CalHash(KeyType.ED25519, buff)
            hash2 = CheckKey().CalHash(KeyType.ED25519, hash1)
            checkSumCol = hash2[0:4]
            if checkSum != checkSumCol:
                raise EncException("Invalid privateKey")
            valid = True
        except Exception:
            valid = False
        return valid

    def encPublicKey(self, keyType, raw_pkey):
        if not raw_pkey:
            raise EncException("Public key is null")
        buff = ""
        buff = buff + chr(176)
        buff = buff + chr(1)
        buff = buff + raw_pkey
        hash1 = CheckKey().CalHash(keyType, buff)
        hash2 = CheckKey().CalHash(keyType, hash1)
        temp = buff + hash2[0:4]
        return temp

    def signMessage(self, msg, member):
        if not member.getRawSKey():
            raise EncException("Raw private key is null")
        if KeyType.ED25519 != member.getKeyType():
            raise EncException("Type does not exist")
        try:
            sk = ed25519.SigningKey(member.getRawSKey())
            return sk.sign(msg)
        except ArithmeticError:
            raise EncException("System error")
        except ValueError:
            raise EncException("Invalid privateKey")
        except Exception:
            raise EncException("Sign message failed")
        return ""
