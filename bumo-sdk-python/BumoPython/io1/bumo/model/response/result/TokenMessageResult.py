# encoding=utf-8
from io1.bumo.model.response.result.data.ContractInfo import ContractInfo
import json
from io1.bumo.model.response.result.data.MetadataInfo import MetadataInfo


class TokenMessageResult:
    contract = None  # type: ContractInfo
    metadatas = []  # type: list[MetadataInfo]

    def parseDict(self, d):
        seqs = tuple, list, set, frozenset
        for i, j in d.items():
            if isinstance(j, dict):
                # 对象转换处理，转换成固定对象或者包含键值的当前对象
                if i == 'contract':
                    setattr(self, i, ContractInfo().parseDict(j))
                else:
                    setattr(self, i, self.parseDict(j))
            elif isinstance(j, seqs):
                # 列表 元组 集合等处理，转换为对应类型的列表/或者当前对象的
                arr = []
                for sj in j:
                    if isinstance(sj, dict):
                        if i == "metadatas":
                            b = MetadataInfo()
                            b.parseDict(sj)
                            arr.append(b)
                setattr(self, i, arr)
            else:
                # 基本类型处理，如字符串 数字等
                setattr(self, i, j)
        self.dict = d
        return self

    def getContract(self):
        return self.contract

    def setContract(self, contract):
        self.contract = contract

    def getMetadatas(self):
        return self.metadatas

    def setMetadatas(self, metadatas):
        self.metadatas = metadatas

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
