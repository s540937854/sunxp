# encoding=utf-8

class ContractCallRequest:
    sourceAddress = ""
    contractAddress = ""
    code = ""
    input = ""
    contractBalance = 0L
    optType = 0
    feeLimit = 0L
    gasPrice = 0L

    def getSourceAddress(self):
        return self.sourceAddress

    def setSourceAddress(self, sourceAddress):
        self.sourceAddress = sourceAddress

    def getContractAddress(self):
        return self.contractAddress

    def setContractAddress(self, contractAddress):
        self.contractAddress = contractAddress

    def getCode(self):
        return self.code

    def setCode(self, code):
        self.code = code

    def getInput(self):
        return self.input

    def setInput(self, input):
        self.input = input

    def getContractBalance(self):
        return self.contractBalance

    def setContractBalance(self, contractBalance):
        self.contractBalance = contractBalance

    def getOptType(self):
        return self.optType

    def setOptType(self, optType):
        self.optType = optType

    def getFeeLimit(self):
        return self.feeLimit

    def setFeeLimit(self, feeLimit):
        self.feeLimit = feeLimit

    def getGasPrice(self):
        return self.gasPrice

    def setGasPrice(self, gasPrice):
        self.gasPrice = gasPrice
