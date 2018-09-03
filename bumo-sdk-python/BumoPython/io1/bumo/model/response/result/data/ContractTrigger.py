# encoding=utf-8
from io1.bumo.model.response.result.data.TriggerTransaction import TriggerTransaction


class ContractTrigger:
    transaction = None  # type: TriggerTransaction

    def getTransaction(self):
        return self.transaction

    def setTransaction(self, transaction):
        self.transaction = transaction
