# encoding=utf-8

class ContractStat:
    applyTime = 0L
    memoryUsage = 0L
    stackUsage = 0L
    step = 0L

    def getApplyTime(self):
        return self.applyTime

    def setApplyTime(self, applyTime):
        self.applyTime = applyTime

    def getMemoryUsage(self):
        return self.memoryUsage

    def setMemoryUsage(self, memoryUsage):
        self.memoryUsage = memoryUsage

    def getStackUsage(self):
        return self.stackUsage

    def setStackUsage(self, stackUsage):
        self.stackUsage = stackUsage

    def getStep(self):
        return self.step

    def setStep(self, step):
        self.step = step
