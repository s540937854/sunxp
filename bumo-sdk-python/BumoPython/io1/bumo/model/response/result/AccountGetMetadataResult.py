# encoding=utf-8
from io1.bumo.model.response.result.data.MetadataInfo import MetadataInfo


class AccountGetMetadataResult:
    metadatas = []  # type: list[MetadataInfo]

    def getMetadatas(self):
        return self.metadatas

    def setMetadatas(self, metadatas):
        self.metadatas = metadatas
