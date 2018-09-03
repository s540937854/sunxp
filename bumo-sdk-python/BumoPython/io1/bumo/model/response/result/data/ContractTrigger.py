# encoding=utf-8
import json

from io1.bumo.model.response.result.data.TriggerTransaction import TriggerTransaction


class ContractTrigger:
    transaction = None  # type: TriggerTransaction

    def parseDict(self, d):
        seqs = tuple, list, set, frozenset
        for i, j in d.items():
            if isinstance(j, dict):
                # 对象转换处理，转换成固定对象或者包含键值的当前对象
                if i == 'transaction':
                    setattr(self, i, TriggerTransaction().parseDict(j))
                else:
                    setattr(self, i, self.parseDict(j))
            else:
                # 基本类型处理，如字符串 数字等
                setattr(self, i, j)
        self.dict = d
        return self

    def getTransaction(self):
        return self.transaction

    def setTransaction(self, transaction):
        self.transaction = transaction

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
