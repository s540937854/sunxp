# encoding=utf-8
from typing import List, Any

from io1.bumo.model.response.result.data.TypeThreshold import TypeThreshold


class Threshold:
    txThreshold = 0L
    typeThresholds = []  # type: List[TypeThreshold]

    def getTxThreshold(self):
        return self.txThreshold

    def setTxThreshold(self, txThreshold):
        self.txThreshold = txThreshold

    def getTypeThresholds(self):
        return self.typeThresholds

    def setTypeThresholds(self, typeThresholds):
        self.typeThresholds = typeThresholds

    def addTypeThreshold(self, typeThreshold):
        if not self.typeThresholds:
            self.typeThresholds = []
        self.typeThresholds.append(typeThreshold)
