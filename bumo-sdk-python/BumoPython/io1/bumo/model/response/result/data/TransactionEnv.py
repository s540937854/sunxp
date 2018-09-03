# encoding=utf-8
from typing import List, Any

from io1.bumo.model.response.result.data.ContractTrigger import ContractTrigger
from io1.bumo.model.response.result.data.TransactionInfo import TransactionInfo


class TransactionEnv:
    transaction = None  # type:TransactionInfo
    trigger = None  # type: ContractTrigger

    def getFeeLimit(self):
        return self.feeLimit

    def setFeeLimit(self, feeLimit):
        self.feeLimit = feeLimit

    def getGasPrice(self):
        return self.gasPrice

    def setGasPrice(self, gasPrice):
        self.gasPrice = gasPrice
