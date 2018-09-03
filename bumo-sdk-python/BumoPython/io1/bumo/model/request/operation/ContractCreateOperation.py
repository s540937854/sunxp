# encoding=utf-8
from io1.bumo.common.OperationType import OperationType
from io1.bumo.model.request.operation.BaseOperation import BaseOperation


class AssetSendOperation(BaseOperation):
    initBalance = 0L
    type = 0
    payload = ""
    initInput = ""

    def __init__(self):
        self.operationType = OperationType.CONTRACT_CREATE

    def getOperationType(self):
        return self.operationType

    def getInitBalance(self):
        return self.initBalance

    def setInitBalance(self, initBalance):
        self.initBalance = initBalance

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getPayload(self):
        return self.payload

    def setPayload(self, payload):
        self.payload = payload

    def getInitInput(self):
        return self.initInput

    def setInitInput(self, initInput):
        self.initInput = initInput
