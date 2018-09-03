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


class AA:
    w = 0
    ww = 0

    def parseDict(self, d):
        for i, j in d.items():
            setattr(self, i, j)
        self.dict = d
        return self

    def getW(self):
        return self.w

    def getWW(self):
        return self.ww


class parseObject():
    def parseDict(self, d):
        seqs = tuple, list, set, frozenset
        for i, j in d.items():
            if isinstance(j, dict):
                #对象转换处理，转换成固定对象或者包含键值的当前对象
                if i == 'aa':
                    setattr(self, i, AA().parseDict(j))
                else:
                    setattr(self, i, self.parseDict(j))
            elif isinstance(j, seqs):
                #列表 元组 集合等处理，转换为对应类型的列表/或者当前对象的
                arr = []
                for sj in j:
                    if isinstance(sj, dict):
                        b = B()
                        b.parseDict(sj)
                        arr.append(b)
                setattr(self, i, arr)
                # setattr(self, i, type(j)(self.parseDict(sj) if isinstance(sj, dict) else sj for sj in j))
            else:
                #基本类型处理，如字符串 数字等
                setattr(self, i, j)
        self.dict = d
        return self

    def parseStr(self, str):
        j = json.loads(str)
        p = self.parseDict(j)
        return p

    def __str__(self):
        return json.dumps(self.dict, sort_keys=True, ensure_ascii=False, indent=2)


jsonStr = '{"a":1,"b":"world","c":[{"d":"Scholar","e":" "},{"d":"Scholar1","e":"11 "}],"aa":{"w":11,"www":22}}'
obj = parseObject().parseStr(jsonStr)
print obj.__str__()
# print obj.getA(), obj.getAA().getW()
print obj.getC()[0].getD()
