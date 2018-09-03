# encoding=utf-8
from io1.bumo.model.response.result.data.TransactionHistory import TransactionHistory


class BlockGetTransactionsResult:
    totalCount = 0L
    transactions = []  # type: list[TransactionHistory]

    def getTotalCount(self):
        return self.totalCount

    def setTotalCount(self, totalCount):
        self.totalCount = totalCount

    def getTransactions(self):
        return self.transactions

    def setTransactions(self, transactions):
        self.transactions = transactions
