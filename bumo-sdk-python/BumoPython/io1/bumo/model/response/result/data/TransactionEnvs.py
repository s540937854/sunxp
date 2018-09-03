# encoding=utf-8
from io1.bumo.model.response.result.data.TransactionEnv import TransactionEnv


class TransactionEnvs:
    transactionEnv = None  # type:TransactionEnv

    def getTransactionEnv(self):
        return self.transactionEnv

    def setTransactionEnv(self, transactionEnv):
        self.transactionEnv = transactionEnv
