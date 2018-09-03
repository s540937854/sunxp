# encoding=utf-8
# import json
#
#
# class Response:
#     code = 0
#     message = ""
#     mobile = ""
#     taskId = ""
#
#     def __init__(self):
#         pass
#
#
# class Result(object):
#     __aaaa = 1
#
#     def __init__(self, code, message, response=None):
#         if response is None:
#             response = []
#         self.__code = code
#         self.message = message
#         self.response = response
#
#     def getCode(self):
#         return self.__code
#
#     def getResponse(self):
#         aa = []
#         for s in self.response:
#             res = Response()
#             print type(s)
#             aa.append(res)
#         return aa
#
#
# test_str = '{"code":200,"message":"发送成功","response":[{"code":2,"message":"xxxxxxxx","mobile":"xxxxxx","taskId":null},{"code":2,"message":"xxxxxx","mobile":"xxxxxx","taskId":null}]}'
#
# result = Result(**json.loads(test_str))
# print result.getResponse()
# for res in result.response:
#     print res

__author__ = 'Scholar'

import sys
import json

reload(sys)
sys.setdefaultencoding('utf-8')


class parseObject():
    def parseDict(self, d):
        # top = parseObject()
        seqs = tuple, list, set, frozenset

        for i, j in d.items():
            if isinstance(j, dict):
                setattr(self, i, self.parseDict(j))
            elif isinstance(j, seqs):
                setattr(self, i,
                        type(j)(self.parseDict(sj) if isinstance(sj, dict) else sj for sj in j))
            else:
                setattr(self, i, j)
                self.dict = d
        return self

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    a = ""
    b = ""
    c = []

    def getA(self):
        return self.a

    def getC(self):
        return self.c


class B(object):
    d = ""
    e = ""

    def getD(self):
        return self.d

    def getE(self):
        return self.e


class A(object):
    a = ""
    b = ""
    c = []

    def getA(self):
        return self.a

    def getC(self):
        return self.c


jsonStr = '{"a":1,"b":"world","c":[{"d":"Scholar","e":" "},{"d":"Scholar1","e":"11 "}]}'
a = A()
obj = parseObject().parseStr(jsonStr)
# print obj.a
print obj.getA(), type(obj.c[1])
