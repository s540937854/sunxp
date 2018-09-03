# encoding=utf-8
from io1.bumo.common.OperationType import OperationType
from io1.bumo.model.request.operation.BaseOperation import BaseOperation


class AssetSendOperation(BaseOperation):
    operationType = OperationType.ASSET_SEND
    destAddress = ""
    code = ""
    issuer = ""
    amount = 0L

    def getOperationType(self):
        return self.operationType

    def getDestAddress(self):
        return self.destAddress

    def setDestAddress(self, destAddress):
        self.destAddress = destAddress

    def getCode(self):
        return self.code

    def setCode(self, code):
        self.code = code

    def getIssuer(self):
        return self.issuer

    def setIssuer(self, issuer):
        self.issuer = issuer

    def setAmount(self, amount):
        self.amount = amount

    def getAmount(self):
        return self.amount
