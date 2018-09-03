# encoding=utf-8
from io1.bumo.model.response.result.data.LedgerSeq import LedgerSeq


class BlockCheckStatusLedgerSeqResponse:
    ledgerSeq = None  # type: LedgerSeq

    def getLedgerSeq(self):
        return self.ledgerSeq

    def setLedgerSeq(self, ledgerSeq):
        self.ledgerSeq = ledgerSeq
