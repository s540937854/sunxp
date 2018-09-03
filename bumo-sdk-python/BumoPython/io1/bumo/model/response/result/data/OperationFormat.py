# encoding=utf-8
from io1.bumo.model.response.result.data.AccountActiviateInfo import AccountActiviateInfo
from io1.bumo.model.response.result.data.AccountSetMetadataInfo import AccountSetMetadataInfo
from io1.bumo.model.response.result.data.AccountSetPrivilegeInfo import AccountSetPrivilegeInfo
from io1.bumo.model.response.result.data.AssetIssueInfo import AssetIssueInfo
from io1.bumo.model.response.result.data.AssetSendInfo import AssetSendInfo
from io1.bumo.model.response.result.data.BUSendInfo import BUSendInfo
from io1.bumo.model.response.result.data.LogInfo import LogInfo


class OperationFormat:
    type = ""
    sourceAddress = ""
    metadata = ""
    createAccount = None  # type: AccountActiviateInfo
    issueAsset = None  # type: AssetIssueInfo
    sendAsset = None  # type: AssetSendInfo
    sendBU = None  # type: BUSendInfo
    setMetadata = None  # type: AccountSetMetadataInfo
    setPrivilege = None  # type: AccountSetPrivilegeInfo
    log = None  # type: LogInfo

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getSourceAddress(self):
        return self.sourceAddress

    def setSourceAddress(self, sourceAddress):
        self.sourceAddress = sourceAddress

    def getMetadata(self):
        return self.metadata

    def setMetadata(self, metadata):
        self.metadata = metadata

    def getCreateAccount(self):
        return self.createAccount

    def setCreateAccount(self, createAccount):
        self.createAccount = createAccount

    def getIssueAsset(self):
        return self.issueAsset

    def setIssueAsset(self, issueAsset):
        self.issueAsset = issueAsset

    def getSendAsset(self):
        return self.sendAsset

    def setSendAsset(self, sendAsset):
        self.sendAsset = sendAsset

    def getSendBU(self):
        return self.sendBU

    def setSendBU(self, sendBU):
        self.sendBU = sendBU

    def getSetMetadata(self):
        return self.setMetadata

    def setSetMetadata(self, setMetadata):
        self.setMetadata = setMetadata

    def getSetPrivilege(self):
        return self.setPrivilege

    def setSetPrivilege(self, setPrivilege):
        self.setPrivilege = setPrivilege

    def getLog(self):
        return self.log

    def setLog(self, log):
        self.log = log
