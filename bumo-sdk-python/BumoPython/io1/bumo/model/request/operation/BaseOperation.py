# encoding=utf-8

class BaseOperation:
    operationType = None
    sourceAddress = ""
    metadata = ""

    def getOperationType(self):
        return self.operationType

    def getSourceAddress(self):
        return self.sourceAddress

    def setSourceAddress(self, sourceAddress):
        self.sourceAddress = sourceAddress

    def getMetadata(self):
        return self.metadata

    def setMetadata(self, metadata):
        self.metadata = metadata
