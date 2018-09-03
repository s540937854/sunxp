# encoding=utf-8
from io1.bumo.common.OperationType import OperationType
from io1.bumo.model.request.operation.BaseOperation import BaseOperation


class AccountSetMetadataOperation(BaseOperation):
    key = ""
    value = ""
    version = 0L
    deleteFlag = False

    def __init__(self):
        self.operationType = OperationType.ACCOUNT_SET_METADATA

    def getOperationType(self):
        return self.operationType

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getVersion(self):
        return self.version

    def setVersion(self, version):
        self.version = version

    def getDeleteFlag(self):
        return self.deleteFlag

    def setDeleteFlag(self, deleteFlag):
        self.deleteFlag = deleteFlag
