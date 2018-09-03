# encoding=utf-8

class ContractInfo:
    type = 0
    payload = ""

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getPayload(self):
        return self.payload

    def setPaylaod(self, payload):
        self.payload = payload
