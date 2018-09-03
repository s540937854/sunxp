# encoding=utf-8
from io1.bumo.exception.SdkErrors import SdkErrors
from io1.bumo.exception.SDKException import SDKException


class SdkError:
    def __init__(self, code, description):
        self.code = code
        self.description = description

    def checkErrorCode(self, baseResponse=None, errorCode=None, errorDesc=None):
        if baseResponse:
            errCode = baseResponse.error_code
            if not errCode and errCode != 0:
                raise SDKException(SdkErrors.CONNECTNETWORK_ERROR.getCode(),
                                   SdkErrors.CONNECTNETWORK_ERROR.getDescription())
            else:
                if errCode != 0:
                    errDesc = baseResponse.error_desc
                    if errDesc:
                        raise SDKException(errCode, errDesc)
                    else:
                        raise SDKException(errCode, "error")
        else:
            if not errorCode and errorCode != 0:
                raise SDKException(SdkErrors.CONNECTNETWORK_ERROR.getCode(),
                                   SdkErrors.CONNECTNETWORK_ERROR.getDescription())
            else:
                if errorCode != 0:
                    if errorDesc:
                        raise SDKException(errorCode, errorDesc)
                    else:
                        raise SDKException(errorCode, "error")

    def getCode(self):
        return self.code

    def getDescription(self):
        return self.description
