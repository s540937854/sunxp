# encoding=utf-8
from io1.bumo.model.response.result.data.ContractInfo import ContractInfo


class ContractGetInfoResult:
    contract = None  # type: ContractInfo

    def getContract(self):
        return self.contract

    def setContract(self, contract):
        self.contract = contract
