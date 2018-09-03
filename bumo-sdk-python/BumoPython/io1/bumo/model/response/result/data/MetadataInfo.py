# encoding=utf-8
from typing import List, Any

from io1.bumo.model.response.result.data.TypeThreshold import TypeThreshold


class MetadataInfo:
    key = ""
    value = ""
    version = 0L

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
