# encoding=utf-8
from typing import List
import json

from io1.bumo.model.response.result.data.Signature import Signature
from io1.bumo.model.response.result.data.TransactionInfo import TransactionInfo


class TransactionHistory:
    actual_fee = ""
    close_time = 0L
    error_code = 0
    error_desc = ""
    hash = ""
    ledger_seq = 0L
    signatures = []  # type: List[Signature]
    transaction = None  # type: TransactionInfo
    tx_size = 0L

    def parseDict(self, d):
        seqs = tuple, list, set, frozenset
        for i, j in d.items():
            if isinstance(j, dict):
                # 对象转换处理，转换成固定对象或者包含键值的当前对象
                if i == 'transaction':
                    setattr(self, i, TransactionInfo().parseDict(j))
                else:
                    setattr(self, i, self.parseDict(j))
            elif isinstance(j, seqs):
                # 列表 元组 集合等处理，转换为对应类型的列表/或者当前对象的
                arr = []
                for sj in j:
                    if isinstance(sj, dict):
                        if i == "signatures":
                            b = Signature()
                            b.parseDict(sj)
                            arr.append(b)
                setattr(self, i, arr)
            else:
                # 基本类型处理，如字符串 数字等
                setattr(self, i, j)
        self.dict = d
        return self

    def getActualFee(self):
        return self.actual_fee

    def setActualFee(self, actualFee):
        self.actual_fee = actualFee

    def getCloseTime(self):
        return self.close_time

    def setCloseTime(self, closeTime):
        self.close_time = closeTime

    def getErrorCode(self):
        return self.error_code

    def setErrorCode(self, errorCode):
        self.error_code = errorCode

    def getErrorDesc(self):
        return self.error_desc

    def setErrorDesc(self, errorDesc):
        self.error_desc = errorDesc

    def getHash(self):
        return self.hash

    def setHash(self, hash):
        self.hash = hash

    def getLedgerSeq(self):
        return self.ledger_seq

    def setLedgerSeq(self, ledgerSeq):
        self.ledger_seq = ledgerSeq

    def getSignatures(self):
        return self.signatures

    def setSignatures(self, signatures):
        self.signatures = signatures

    def getTransaction(self):
        return self.transaction

    def setTransaction(self, transaction):
        self.transaction = transaction

    def getTxSize(self):
        return self.tx_size

    def setTxSize(self, txSize):
        self.tx_size = txSize

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
