# encoding=utf-8
from typing import List
import json

from io1.bumo.model.response.result.data.TypeThreshold import TypeThreshold


class Threshold:
    tx_threshold = 0L
    type_thresholds = []  # type: List[TypeThreshold]

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
                        if i == "type_threshold":
                            b = TypeThreshold()
                            b.parseDict(sj)
                            arr.append(b)
                setattr(self, i, arr)
            else:
                # 基本类型处理，如字符串 数字等
                setattr(self, i, j)
        self.dict = d
        return self

    def getTxThreshold(self):
        return self.tx_threshold

    def setTxThreshold(self, txThreshold):
        self.tx_threshold = txThreshold

    def getTypeThresholds(self):
        return self.type_thresholds

    def setTypeThresholds(self, typeThresholds):
        self.type_thresholds = typeThresholds

    def addTypeThreshold(self, typeThreshold):
        if not self.type_thresholds:
            self.type_thresholds = []
        self.type_thresholds.append(typeThreshold)

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
