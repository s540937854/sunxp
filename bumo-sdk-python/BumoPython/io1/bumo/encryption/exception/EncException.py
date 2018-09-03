# encoding=utf-8


class EncException(Exception):
    """加密过程中引发的异常"""

    def __init__(self, errDes):
        """加密错误 :param errDes: 错误描述"""
        Exception.__init__(self, errDes)
        self.errDes = errDes
