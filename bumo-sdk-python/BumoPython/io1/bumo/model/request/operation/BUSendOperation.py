# encoding=utf-8
from io1.bumo.common.OperationType import OperationType
from io1.bumo.model.request.operation.BaseOperation import BaseOperation


class AssetSendOperation(BaseOperation):
    destAddress = ""
    amount = 0L

    def __init__(self):
        self.operationType = OperationType.BU_SEND

    def getOperationType(self):
        return self.operationType

    def getDestAddress(self):
        return self.destAddress

    def setDestAddress(self, destAddress):
        self.destAddress = destAddress

    def setAmount(self, amount):
        self.amount = amount

    def getAmount(self):
        return self.amount
