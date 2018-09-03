# encoding=utf-8
from typing import List, Any


class LogInfo:
    topic = ""
    datas = []  # type: List[str]

    def getTopic(self):
        return self.topic

    def setTopic(self, topic):
        self.topic = topic

    def getDatas(self):
        return self.datas

    def setDatas(self, datas):
        self.datas = datas
