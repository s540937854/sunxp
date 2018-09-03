# encoding=utf-8
from io1.bumo.model.response.result.data.LedgerSeq import LedgerSeq
import json


class BlockCheckStatusLedgerSeqResponse:
    ledger_manager = None  # type: LedgerSeq

    def parseDict(self, d):
        for i, j in d.items():
            if isinstance(j, dict):
                # 对象转换处理，转换成固定对象或者包含键值的当前对象
                if i == 'ledger_manager':
                    setattr(self, i, LedgerSeq().parseDict(j))
                else:
                    setattr(self, i, self.parseDict(j))
            else:
                # 基本类型处理，如字符串 数字等
                setattr(self, i, j)
        self.dict = d
        return self

    def getLedgerSeq(self):
        return self.ledger_manager

    def setLedgerSeq(self, ledgerSeq):
        self.ledger_manager = ledgerSeq

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
