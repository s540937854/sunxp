# encoding=utf-8
import json


class BaseResponse:

    def __init__(self, error_code, error_desc):
        self.error_code = error_code
        self.error_desc = error_desc

    def getErrorCode(self):
        return self.error_code

    def setErrorCode(self, error_code):
        self.error_code = error_code

    def getErrorDesc(self):
        return self.error_desc

    def setErrorDesc(self, error_desc):
        self.error_desc = error_desc

    def buildResponse(self, sdkError=None, errorCode=None, errorDesc=None):
        if sdkError:
            self.error_code = sdkError.getCode()
            self.error_desc = sdkError.getDescription()
        else:
            self.error_code = errorCode
            self.error_desc = errorDesc

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)
