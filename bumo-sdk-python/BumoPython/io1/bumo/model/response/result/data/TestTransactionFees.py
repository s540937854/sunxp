# encoding=utf-8
from io1.bumo.model.response.result.data.TransactionFees import TransactionFees


class TestTransactionFees:
    transactionFees = None  # type: TransactionFees

    def getTransactionFees(self):
        return self.transactionFees

    def setTransactionFees(self, transactionFees):
        self.transactionFees = transactionFees
