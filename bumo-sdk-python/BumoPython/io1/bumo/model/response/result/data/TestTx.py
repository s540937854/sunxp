# encoding=utf-8
from io1.bumo.model.response.result.data.TestTransactionFees import TestTransactionFees


class TestTx:
    transactionEnv = None  # type: TestTransactionFees

    def getTestTransactionFees(self):
        return self.testTransactionFees

    def setTestTransactionFees(self, testTransactionFees):
        self.testTransactionFees = testTransactionFees
