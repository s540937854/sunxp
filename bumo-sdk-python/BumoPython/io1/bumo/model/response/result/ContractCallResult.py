# encoding=utf-8
from io1.bumo.model.response.result.data.ContractStat import ContractStat

from io1.bumo.model.response.result.data.TransactionEnvs import TransactionEnvs


class ContractCallResult:
    logs = ""  # type jsonobjectd对象
    queryRets = ""  # type jsonoArray对象
    stat = None  # type: ContractStat
    txs = []  # type: list[TransactionEnvs]

    def getLogs(self):
        return self.logs

    def setLogs(self, logs):
        self.logs = logs

    def getQueryRets(self):
        return self.queryRets

    def setQueryRets(self, queryRets):
        self.queryRets = queryRets

    def getStat(self):
        return self.stat

    def setStat(self, stat):
        self.stat = stat

    def getTxs(self):
        return self.txs

    def setTxs(self, txs):
        self.txs = txs
