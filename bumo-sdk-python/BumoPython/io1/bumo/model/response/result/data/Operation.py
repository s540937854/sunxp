# encoding=utf-8
from io1.bumo.model.response.result.data.AccountActiviateInfo import AccountActiviateInfo
from io1.bumo.model.response.result.data.AccountSetMetadataInfo import AccountSetMetadataInfo
from io1.bumo.model.response.result.data.AccountSetPrivilegeInfo import AccountSetPrivilegeInfo
from io1.bumo.model.response.result.data.AssetIssueInfo import AssetIssueInfo
from io1.bumo.model.response.result.data.AssetSendInfo import AssetSendInfo
from io1.bumo.model.response.result.data.BUSendInfo import BUSendInfo
from io1.bumo.model.response.result.data.LogInfo import LogInfo
import json


class Operation:
    type = 0
    source_address = ""
    metadata = ""
    create_account = None  # type: AccountActiviateInfo
    issue_asset = None  # type: AssetIssueInfo
    pay_asset = None  # type: AssetSendInfo
    pay_coin = None  # type: BUSendInfo
    set_metadata = None  # type: AccountSetMetadataInfo
    set_privilege = None  # type: AccountSetPrivilegeInfo
    log = None  # type: LogInfo

    def parseDict(self, d):
        for i, j in d.items():
            if isinstance(j, dict):
                # 对象转换处理，转换成固定对象或者包含键值的当前对象
                if i == 'create_account':
                    setattr(self, i, AccountActiviateInfo().parseDict(j))
                elif i == 'issue_asset':
                    setattr(self, i, AssetIssueInfo().parseDict(j))
                elif i == 'pay_asset':
                    setattr(self, i, AssetSendInfo().parseDict(j))
                elif i == 'pay_coin':
                    setattr(self, i, BUSendInfo().parseDict(j))
                elif i == 'set_metadata':
                    setattr(self, i, AccountSetMetadataInfo().parseDict(j))
                elif i == 'set_privilege':
                    setattr(self, i, AccountSetPrivilegeInfo().parseDict(j))
                elif i == 'log':
                    setattr(self, i, LogInfo().parseDict(j))
                else:
                    setattr(self, i, self.parseDict(j))
            else:
                # 基本类型处理，如字符串 数字等
                setattr(self, i, j)
        self.dict = d
        return self

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getSourceAddress(self):
        return self.source_address

    def setSourceAddress(self, sourceAddress):
        self.source_address = sourceAddress

    def getMetadata(self):
        return self.metadata

    def setMetadata(self, metadata):
        self.metadata = str.decode(metadata, 'hex')

    def getCreateAccount(self):
        return self.create_account

    def setCreateAccount(self, createAccount):
        self.create_account = createAccount

    def getIssueAsset(self):
        return self.issue_asset

    def setIssueAsset(self, issueAsset):
        self.issue_asset = issueAsset

    def getSendAsset(self):
        return self.pay_asset

    def setSendAsset(self, sendAsset):
        self.pay_asset = sendAsset

    def getSendBU(self):
        return self.pay_coin

    def setSendBU(self, sendBU):
        self.pay_coin = sendBU

    def getSetMetadata(self):
        return self.set_metadata

    def setSetMetadata(self, setMetadata):
        self.set_metadata = setMetadata

    def getSetPrivilege(self):
        return self.set_privilege

    def setSetPrivilege(self, setPrivilege):
        self.set_privilege = setPrivilege

    def getLog(self):
        return self.log

    def setLog(self, log):
        self.log = log

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
