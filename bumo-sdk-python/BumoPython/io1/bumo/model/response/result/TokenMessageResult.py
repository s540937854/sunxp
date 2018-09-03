# encoding=utf-8
from io1.bumo.model.response.result.data.ContractInfo import ContractInfo

from io1.bumo.model.response.result.data.MetadataInfo import MetadataInfo


class TokenMessageResult:
    contract = None  # type: ContractInfo
    metadatas = []  # type: list[MetadataInfo]

    def getContract(self):
        return self.contract

    def setContract(self, contract):
        self.contract = contract

    def getMetadatas(self):
        return self.metadatas

    def setMetadatas(self, metadatas):
        self.metadatas = metadatas
