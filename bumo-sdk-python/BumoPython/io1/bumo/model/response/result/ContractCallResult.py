# encoding=utf-8
from io1.bumo.model.response.result.data.ContractStat import ContractStat

from io1.bumo.model.response.result.data.TransactionEnvs import TransactionEnvs
import json


class ContractCallResult:
    logs = ""  # type jsonobjectd对象
    query_rets = ""  # type jsonoArray对象
    stat = None  # type: ContractStat
    txs = []  # type: list[TransactionEnvs]

    def parseDict(self, d):
        seqs = tuple, list, set, frozenset
        for i, j in d.items():
            if isinstance(j, dict):
                # 对象转换处理，转换成固定对象或者包含键值的当前对象
                if i == 'stae':
                    setattr(self, i, ContractStat().parseDict(j))
                else:
                    setattr(self, i, self.parseDict(j))
            elif isinstance(j, seqs):
                # 列表 元组 集合等处理，转换为对应类型的列表/或者当前对象的
                arr = []
                if i == "txs":
                    for sj in j:
                        if isinstance(sj, dict):
                            b = TransactionEnvs()
                            b.parseDict(sj)
                            arr.append(b)
                    setattr(self, i, arr)
                else:
                    setattr(self, i, type(j)(self.parseDict(sj) if isinstance(sj, dict) else sj for sj in j))
            else:
                # 基本类型处理，如字符串 数字等
                setattr(self, i, j)
        self.dict = d
        return self

    def getLogs(self):
        return self.logs

    def setLogs(self, logs):
        self.logs = logs

    def getQueryRets(self):
        return self.query_rets

    def setQueryRets(self, queryRets):
        self.query_rets = queryRets

    def getStat(self):
        return self.stat

    def setStat(self, stat):
        self.stat = stat

    def getTxs(self):
        return self.txs

    def setTxs(self, txs):
        self.txs = txs

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
