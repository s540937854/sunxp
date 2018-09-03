# encoding=utf-8
import json


class ContractStat:
    apply_time = 0L
    memory_usage = 0L
    stack_usage = 0L
    step = 0L

    def parseDict(self, d):
        for i, j in d.items():
            # 基本类型处理，如字符串 数字等
            setattr(self, i, j)
        self.dict = d
        return self

    def getApplyTime(self):
        return self.apply_time

    def setApplyTime(self, applyTime):
        self.apply_time = applyTime

    def getMemoryUsage(self):
        return self.memory_usage

    def setMemoryUsage(self, memoryUsage):
        self.memory_usage = memoryUsage

    def getStackUsage(self):
        return self.stack_usage

    def setStackUsage(self, stackUsage):
        self.stack_usage = stackUsage

    def getStep(self):
        return self.step

    def setStep(self, step):
        self.step = step

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
