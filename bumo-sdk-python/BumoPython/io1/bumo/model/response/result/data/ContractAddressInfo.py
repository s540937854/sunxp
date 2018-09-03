# encoding=utf-8

class ContractAddressInfo:
    contractAddress = ""
    operationIndex = 0

    def getContractAddress(self):
        return self.contractAddress

    def setContractAddress(self, contractAddress):
        self.contractAddress = contractAddress

    def getOperationIndex(self):
        return self.operationIndex

    def setOperationIndex(self, operationIndex):
        self.operationIndex = operationIndex
