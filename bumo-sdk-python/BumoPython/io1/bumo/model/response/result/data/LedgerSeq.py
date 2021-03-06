# encoding=utf-8
import json


class LedgerSeq:
    chain_max_ledger_seq = 0L
    ledger_sequence = 0L

    def parseDict(self, d):
        for i, j in d.items():
            # 基本类型处理，如字符串 数字等
            setattr(self, i, j)
        self.dict = d
        return self

    def getChainMaxLedgerSeq(self):
        return self.chain_max_ledger_seq

    def setChainMaxLedgerSeq(self, chainMaxLedgerSeq):
        self.chain_max_ledger_seq = chainMaxLedgerSeq

    def getLedgerSequence(self):
        return self.ledger_sequence

    def setLedgerSequence(self, ledgerSequence):
        self.ledger_sequence = ledgerSequence

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
