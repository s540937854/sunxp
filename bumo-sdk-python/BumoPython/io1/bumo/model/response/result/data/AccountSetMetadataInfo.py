# encoding=utf-8
import json


class AccountSetMetadataInfo:
    key = ""
    value = ""
    version = 0L
    delete_flag = False

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
        return self.delete_flag

    def setDeleteFlag(self, deleteFlag):
        self.delete_flag = deleteFlag

    def parseDict(self, d):
        for i, j in d.items():
            # 基本类型处理，如字符串 数字等
            setattr(self, i, j)
        self.dict = d
        return self

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
