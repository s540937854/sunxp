# encoding=utf-8

class TypeThreshold:
    type = 0
    threshold = 0L

    def __init__(self, type, threshold):
        self.type = type
        self.threshold = threshold

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getThreshold(self):
        return self.threshold

    def setThreshold(self, threshold):
        self.threshold = threshold
