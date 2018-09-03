# encoding=utf-8
from io1.bumo.exception.SdkErrors import SdkErrors


class SDKException(RuntimeError):

    def __init__(self, errorCode=None, errorDesc=None):
        if errorCode == 0 or errorCode:
            self.errorCode = errorCode
        else:
            self.errorCode = SdkErrors.SYSTEM_ERROR.getCode()
        if errorDesc:
            self.errorDesc = errorDesc
        else:
            self.errorDesc = SdkErrors.SYSTEM_ERROR.getDescription()

    def getErrorCode(self):
        return self.errorCode

    def getErrorDesc(self):
        return self.errorDesc
