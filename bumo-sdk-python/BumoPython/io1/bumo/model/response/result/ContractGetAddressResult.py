# encoding=utf-8
from io1.bumo.model.response.result.data.ContractAddressInfo import ContractAddressInfo
import json


class ContractGetAddressResult:
    contract_address_infos = []  # type: list[ContractAddressInfo]

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
                        if i == "contract_address_infos":
                            b = ContractAddressInfo()
                            b.parseDict(sj)
                            arr.append(b)
                setattr(self, i, arr)
            else:
                # 基本类型处理，如字符串 数字等
                setattr(self, i, j)
        self.dict = d
        return self

    def getContractAddressInfos(self):
        return self.contract_address_infos

    def setContractAddressInfos(self, contractAddressInfos):
        self.contract_address_infos = contractAddressInfos

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
