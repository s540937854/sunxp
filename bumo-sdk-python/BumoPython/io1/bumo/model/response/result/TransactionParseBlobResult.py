# encoding=utf-8
from typing import List
import json
from io1.bumo.model.response.result.data.OperationFormat import OperationFormat


class TransactionParseBlobResult:
    source_address = ""
    fee_limit = 0L
    gas_price = 0L
    nonce = 0L
    operations = []  # type: List[OperationFormat]

    def parseDict(self, d):
        seqs = tuple, list, set, frozenset
        for i, j in d.items():
            if isinstance(j, dict):
                # 对象转换处理，转换成固定对象或者包含键值的当前对象
                setattr(self, i, self.parseDict(j))
            elif isinstance(j, seqs):
                # 列表 元组 集合等处理，转换为对应类型的列表/或者当前对象的
                arr = []
                for sj in j:
                    if isinstance(sj, dict):
                        if i == "operations":
                            b = OperationFormat()
                            b.parseDict(sj)
                            arr.append(b)
                setattr(self, i, arr)
            else:
                # 基本类型处理，如字符串 数字等
                setattr(self, i, j)
        self.dict = d
        return self

    def getSourceAddress(self):
        return self.source_address

    def setSourceAddress(self, sourceAddress):
        self.source_address = sourceAddress

    def getFeeLimit(self):
        return self.fee_limit

    def setFeeLimit(self, feeLimit):
        self.fee_limit = feeLimit

    def getGasPrice(self):
        return self.gas_price

    def setGasPrice(self, gasPrice):
        self.gas_price = gasPrice

    def getNonce(self):
        return self.nonce

    def setNonce(self, nonce):
        self.nonce = nonce

    def getOperations(self):
        return self.operations

    def setOperations(self, operations):
        self.operations = operations

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
