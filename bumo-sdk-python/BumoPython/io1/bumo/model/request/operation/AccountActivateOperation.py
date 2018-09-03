# encoding=utf-8
from io1.bumo.common.OperationType import OperationType
from io1.bumo.model.request.operation.BaseOperation import BaseOperation


class AccountActivateOperation(BaseOperation):
    destAddress = ""
    initBalance = 0L

    def __init__(self):
        self.operationType = OperationType.ACCOUNT_ACTIVATE

    def getOperationType(self):
        return self.operationType

    def getDestAddress(self):
        return self.destAddress

    def setDestAddress(self, destAddress):
        self.destAddress = destAddress

    def getInitBalance(self):
        return self.initBalance

    def setInitBalance(self, balance):
        self.initBalance = balance
