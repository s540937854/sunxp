# encoding=utf-8
from typing import List, Any

from io1.bumo.model.response.result.data.MetadataInfo import MetadataInfo
from io1.bumo.model.response.result.data.Signer import Signer
from io1.bumo.model.response.result.data.Threshold import Threshold


class Priv:
    masterWeight = ""
    signers = []  # type: List[Signer]
    threshold = None  # type: Threshold
    # metadatas = []  # type: List[MetadataInfo]
    # initBalance = 0L
    # initInput = ""

    def getMasterWeight(self):
        return self.masterWeight

    def setMasterWeight(self, masterWeight):
        self.masterWeight = masterWeight

    def getSigners(self):
        return self.signers

    def setSigners(self, signers):
        self.signers = signers

    def getThreshold(self):
        return self.threshold

    def setThreshold(self, threshold):
        self.threshold = threshold

    # def getMetadatas(self):
    #     return self.metadatas
    #
    # def setMetadatas(self, metadatas):
    #     self.metadatas = metadatas
    #
    # def getInitBalance(self):
    #     return self.initBalance
    #
    # def setInitBalance(self, initBalance):
    #     self.initBalance = initBalance
    #
    # def getInitInput(self):
    #     return self.initInput
    #
    # def setInitInput(self, initInput):
    #     self.initInput = initInput
