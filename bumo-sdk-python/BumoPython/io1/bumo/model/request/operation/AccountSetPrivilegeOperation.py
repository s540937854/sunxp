# encoding=utf-8
from io1.bumo.common.OperationType import OperationType
from io1.bumo.model.request.operation.BaseOperation import BaseOperation


class AccountSetPrivilegeOperation(BaseOperation):
    masterWeight = ""
    signers = []
    txThreshold = ""
    typeThresholds = []

    def __init__(self):
        self.operationType = OperationType.ACCOUNT_SET_PRIVILEGE

    def getOperationType(self):
        return self.operationType

    def getMasterWeight(self):
        return self.masterWeight

    def setMasterWeight(self, masterWeight):
        self.masterWeight = masterWeight

    def setSigners(self, signers):
        self.signers = signers

    def getSigners(self):
        return self.signers

    def addSigners(self, signer):
        if not self.signers:
            self.signers = []
        self.signers.append(signer)

    def getTxThreshold(self):
        return self.txThreshold

    def setTxThreshold(self, txThreshold):
        self.txThreshold = txThreshold

    def getTypeThresholds(self):
        return self.typeThresholds

    def setTypeThresholds(self, typeThresholds):
        self.typeThresholds = typeThresholds

    def addTypeThresholds(self, typeThreshold):
        if not self.typeThresholds:
            self.typeThresholds = []
        self.typeThresholds.append(typeThreshold)
