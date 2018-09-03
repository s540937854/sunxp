# encoding=utf-8
from io1.bumo.model.response.result.data.ContractAddressInfo import ContractAddressInfo


class ContractGetAddressResult:
    contractAddressInfos = []  # type: list[ContractAddressInfo]

    def getContractAddressInfos(self):
        return self.contractAddressInfos

    def setContractAddressInfos(self, contractAddressInfos):
        self.contractAddressInfos = contractAddressInfos
