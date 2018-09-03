# encoding=utf-8
import hashlib

from io1.bumo.encryption.model.KeyType import KeyType


class CheckKey:
    def CheckSum(self, keyType, keyBytes):
        '''
        :param keyType:KeyType.ED25519 or KeyType.ECCSM2 目前只支持ED25519
        :param keyBytes: Private key or public key
        :return:true or false
        '''
        return self.checkKey(keyType, keyBytes)

    def checkKey(self, keyType, keyBytes):
        SumIsRight = True
        lenth = len(keyBytes)
        checkSrc = keyBytes[0:lenth - 4]
        checkSum = keyBytes[lenth - 4:lenth]
        hash1 = self.CalHash(keyType, checkSrc)
        hash2 = self.CalHash(keyType, hash1)
        HashSum = hash2[0:4]
        if checkSum != HashSum:
            SumIsRight = False
        return SumIsRight

    def CalHash(self, keyType, data):
        '''
        get hash
        :param keyType:KeyType.ED25519 or KeyType.ECCSM2目前只支持ED25519
        :param data:Data before hash
        :return:data after hash
        '''
        result = ""
        if keyType == KeyType.ED25519:
            try:
                sha = hashlib.new('sha256')
                sha.update(data)
                result = sha.digest()
            except:
                raise ArithmeticError()
        return result
