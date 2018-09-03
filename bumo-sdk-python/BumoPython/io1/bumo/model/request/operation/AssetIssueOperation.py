# encoding=utf-8
from io1.bumo.common.OperationType import OperationType
from io1.bumo.model.request.operation.BaseOperation import BaseOperation


class AssetIssueOperation(BaseOperation):
    code = ""
    amount = 0L

    def __init__(self):
        self.operationType = OperationType.ASSET_ISSUE

    def getOperationType(self):
        return self.operationType

    def getCode(self):
        return self.code

    def getAmount(self):
        return self.amount

    def setCode(self, code):
        self.code = code

    def setAmount(self, amount):
        self.amount = amount
