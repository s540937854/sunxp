# encoding=utf-8
import json

from typing import List

from io1.bumo.model.response.result.data.Signer import Signer
from io1.bumo.model.response.result.data.TypeThreshold import TypeThreshold


class AccountSetPrivilegeInfo:
    master_weight = ""
    signers = []  # type: List[Signer]
    tx_threshold = ""
    type_thresholds = []  # type: List[TypeThreshold]

    def getMasterWeight(self):
        return self.master_weight

    def setMasterWeight(self, masterWeight):
        self.master_weight = masterWeight

    def getSigners(self):
        return self.signers

    def setSigners(self, signers):
        self.signers = signers

    def getTxThreshold(self):
        return self.tx_threshold

    def setTxThreshold(self, txThreshold):
        self.tx_threshold = txThreshold

    def getTypeThresholds(self):
        return self.type_thresholds

    def setTypeThresholds(self, typeThresholds):
        self.type_thresholds = typeThresholds

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
                        b = None
                        if i == "signers":
                            b = Signer()
                        elif i == "type_thresholds":
                            b = TypeThreshold()
                        b.parseDict(sj)
                        arr.append(b)
                setattr(self, i, arr)
            else:
                # 基本类型处理，如字符串 数字等
                setattr(self, i, j)
        self.dict = d
        return self

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
