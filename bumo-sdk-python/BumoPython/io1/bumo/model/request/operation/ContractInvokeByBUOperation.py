# encoding=utf-8
from io1.bumo.common.OperationType import OperationType
from io1.bumo.model.request.operation.BaseOperation import BaseOperation


class ContractInvokeByAssetOperation(BaseOperation):
    operationType = OperationType.CONTRACT_INVOKE_BY_BU
    contractAddress = ""
    buAmount = 0L
    input = ""

    def getOperationType(self):
        return self.operationType

    def getContractAddress(self):
        return self.contractAddress

    def setContractAddress(self, contractAddress):
        self.contractAddress = contractAddress

    def setBuAmount(self, buAmount):
        self.buAmount = buAmount

    def getBuAmount(self):
        return self.buAmount

    def getInput(self):
        return self.input

    def setInput(self, input):
        self.input = input
