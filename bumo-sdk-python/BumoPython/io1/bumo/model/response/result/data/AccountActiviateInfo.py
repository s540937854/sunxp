# encoding=utf-8
import json

from typing import List

from io1.bumo.model.response.result.data.ContractInfo import ContractInfo
from io1.bumo.model.response.result.data.MetadataInfo import MetadataInfo
from io1.bumo.model.response.result.data.Priv import Priv


class AccountActiviateInfo:
    dest_address = ""
    contract = None  # type: ContractInfo
    priv = None  # type: Priv
    metadatas = []  # type: List[MetadataInfo]
    init_balance = 0L
    init_input = ""

    def parseDict(self, d):
        seqs = tuple, list, set, frozenset
        for i, j in d.items():
            if isinstance(j, dict):
                # 对象转换处理，转换成固定对象或者包含键值的当前对象
                if i == 'priv':
                    setattr(self, i, Priv().parseDict(j))
                elif i == 'contract':
                    setattr(self, i, ContractInfo().parseDict(j))
                else:
                    setattr(self, i, self.parseDict(j))
            elif isinstance(j, seqs):
                # 列表 元组 集合等处理，转换为对应类型的列表/或者当前对象的
                arr = []
                for sj in j:
                    if isinstance(sj, dict):
                        b = MetadataInfo()
                        b.parseDict(sj)
                        arr.append(b)
                setattr(self, i, arr)
            else:
                # 基本类型处理，如字符串 数字等
                setattr(self, i, j)
        self.dict = d
        return self

    def getDestAddress(self):
        return self.dest_address

    def setDestAddress(self, destAddress):
        self.dest_address = destAddress

    def getContract(self):
        return self.contract

    def setContract(self, contract):
        self.contract = contract

    def getPriv(self):
        return self.priv

    def setPriv(self, priv):
        self.priv = priv

    def getMetadatas(self):
        return self.metadatas

    def setMetadatas(self, metadatas):
        self.metadatas = metadatas

    def getInitBalance(self):
        return self.init_balance

    def setInitBalance(self, initBalance):
        self.init_balance = initBalance

    def getInitInput(self):
        return self.init_input

    def setInitInput(self, initInput):
        self.init_input = initInput

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
