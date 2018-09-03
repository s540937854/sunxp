# encoding=utf-8
from io1.bumo.exception.SdkError import SdkError
from io1.bumo.model.response.BaseResponse import BaseResponse
from io1.bumo.model.response.result.BlockGetLatestInfoResult import BlockGetLatestInfoResult


class BlockGetLatestInfoResponse(BaseResponse):
    result = None  # type: BlockGetLatestInfoResult

    def getResult(self):
        return self.result

    def setResult(self, result):
        self.result = result

    def buildResponse(self, sdkError=None, errorCode=None, errorDesc=None, result=None):
        """
        :param sdkError:  io1.bumo.exception.SdkError
        :param errorCode: 当sdkError为空时比传
        :param errorDesc:当sdkError为空时比传
        :param result:
        :return:
        """
        if sdkError:
            self.error_code = sdkError.getCode()
            self.error_desc = sdkError.getDescription()
        else:
            self.error_code = errorCode
            self.error_desc = errorDesc
        self.result = result
