# encoding=utf-8

class AccountSetMetadataInfo:
    key = ""
    value = ""
    version = 0L
    deleteFlag = False

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getVersion(self):
        return self.version

    def setVersion(self, version):
        self.version = version

    def getDeleteFlag(self):
        return self.deleteFlag

    def setDeleteFlag(self, deleteFlag):
        self.deleteFlag = deleteFlag
