# encoding=utf-8
import json


class ContractAddressInfo:
    contract_address = ""
    operation_index = 0

    def parseDict(self, d):
        for i, j in d.items():
            # 基本类型处理，如字符串 数字等
            setattr(self, i, j)
        self.dict = d
        return self

    def getContractAddress(self):
        return self.contract_address

    def setContractAddress(self, contractAddress):
        self.contract_address = contractAddress

    def getOperationIndex(self):
        return self.operation_index

    def setOperationIndex(self, operationIndex):
        self.operation_index = operationIndex

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
