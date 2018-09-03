# encoding=utf-8
from typing import List

from io1.bumo.model.response.result.data.TransactionHistory import TransactionHistory


class TransactionGetInfoResult:
    totalCount = 0L
    transactions = []  # type: List[TransactionHistory]

    def getTransactions(self):
        return self.transactions

    def setTransactions(self, transactions):
        self.transactions = transactions

    def getTotalCount(self):
        return self.totalCount

    def setTotalCount(self, totalCount):
        self.totalCount = totalCount
