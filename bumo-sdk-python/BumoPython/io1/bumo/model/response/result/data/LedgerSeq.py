# encoding=utf-8


class LedgerSeq:
    chainMaxLedgerSeq = 0L
    ledgerSequence = 0L

    def getChainMaxLedgerSeq(self):
        return self.chainMaxLedgerSeq

    def setChainMaxLedgerSeq(self, chainMaxLedgerSeq):
        self.chainMaxLedgerSeq = chainMaxLedgerSeq

    def getLedgerSequence(self):
        return self.ledgerSequence

    def setLedgerSequence(self, ledgerSequence):
        self.ledgerSequence = ledgerSequence
