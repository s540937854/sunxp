# encoding=utf-8
from io1.bumo.common.OperationType import OperationType
from io1.bumo.model.request.operation.BaseOperation import BaseOperation


class ContractInvokeByAssetOperation(BaseOperation):
    operationType = OperationType.CONTRACT_INVOKE_BY_ASSET
    code = ""
    issuer = ""
    assetAmount = 0L
    input = ""

    def getOperationType(self):
        return self.operationType

    def getCode(self):
        return self.code

    def setCode(self, code):
        self.code = code

    def getIssuer(self):
        return self.issuer

    def setIssuer(self, issuer):
        self.issuer = issuer

    def getInput(self):
        return self.input

    def setInput(self, input):
        self.input = input

    def setAssetAmount(self, assetAmount):
        self.assetAmount = assetAmount

    def getAssetAmount(self):
        return self.assetAmount
