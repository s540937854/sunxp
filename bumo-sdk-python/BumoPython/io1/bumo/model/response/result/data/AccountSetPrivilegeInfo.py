# encoding=utf-8
from typing import List, Any

from io1.bumo.model.response.result.data.Signer import Signer
from io1.bumo.model.response.result.data.TypeThreshold import TypeThreshold


class AccountSetPrivilegeInfo:
    masterWeight = ""
    signers = []  # type: List[Signer]
    txThreshold = ""
    typeThresholds = []  # type: List[TypeThreshold]

    def getMasterWeight(self):
        return self.masterWeight

    def setMasterWeight(self, masterWeight):
        self.masterWeight = masterWeight

    def getSigners(self):
        return self.signers

    def setSigners(self, signers):
        self.signers = signers

    def getTxThreshold(self):
        return self.txThreshold

    def setTxThreshold(self, txThreshold):
        self.txThreshold = txThreshold

    def getTypeThresholds(self):
        return self.typeThresholds

    def setTypeThresholds(self, typeThresholds):
        self.typeThresholds = typeThresholds
