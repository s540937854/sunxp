# encoding=utf-8
from typing import List, Any

from io1.bumo.model.response.result.data.TestTx import TestTx


class TransactionEvaluateFeeResult:
    txs = []  # type: List[TestTx]

    def getTxs(self):
        return self.txs

    def setTxs(self, txs):
        self.txs = txs
