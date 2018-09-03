# encoding=utf-8
import json
from io1.bumo.model.response.BaseResponse import BaseResponse
from io1.bumo.model.response.result.BlockGetLatestInfoResult import BlockGetLatestInfoResult


class BlockGetLatestInfoResponse(BaseResponse):
    result = None  # type: BlockGetLatestInfoResult

    def parseDict(self, d):
        for i, j in d.items():
            if isinstance(j, dict):
                # 对象转换处理，转换成固定对象或者包含键值的当前对象
                if i == 'result':
                    setattr(self, i, BlockGetLatestInfoResult().parseDict(j))
                else:
                    setattr(self, i, self.parseDict(j))
            else:
                # 基本类型处理，如字符串 数字等
                setattr(self, i, j)
        self.dict = d
        return self

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
