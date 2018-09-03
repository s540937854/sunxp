# encoding=utf-8
from typing import List, Any

from io1.bumo.model.response.result.data.ContractInfo import ContractInfo
from io1.bumo.model.response.result.data.MetadataInfo import MetadataInfo
from io1.bumo.model.response.result.data.Priv import Priv


class AccountActiviateInfo:
    destAddress = ""
    contract = None  # type: ContractInfo
    priv = None  # type: Priv
    metadatas = []  # type: List[MetadataInfo]
    initBalance = 0L
    initInput = ""

    def getDestAddress(self):
        return self.destAddress

    def setDestAddress(self, destAddress):
        self.destAddress = destAddress

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
        return self.initBalance

    def setInitBalance(self, initBalance):
        self.initBalance = initBalance

    def getInitInput(self):
        return self.initInput

    def setInitInput(self, initInput):
        self.initInput = initInput
