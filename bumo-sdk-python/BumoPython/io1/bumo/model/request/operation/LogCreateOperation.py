# encoding=utf-8
from io1.bumo.common.OperationType import OperationType
from io1.bumo.model.request.operation.BaseOperation import BaseOperation


class LogCreateOperation(BaseOperation):
    topic = ""
    datas = []

    def __init__(self):
        self.operationType = OperationType.LOG_CREATE

    def getTopic(self):
        return self.topic

    def setTopic(self, topic):
        self.topic = topic

    def getDatas(self):
        return self.datas

    def setData(self, datas):
        self.datas = datas

    def addData(self, data):
        if not self.datas:
            self.datas = []
        self.datas.append(data)
