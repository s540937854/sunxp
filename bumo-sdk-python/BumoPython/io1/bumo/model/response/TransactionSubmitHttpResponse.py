# encoding=utf-8
from typing import List, Any

from io1.bumo.model.response.result.TransactionSubmitHttpResult import TransactionSubmitHttpResult


class TransactionSubmitHttpResponse:
    successCount = 0
    results = []  # type: List[TransactionSubmitHttpResult]

    def getSuccessCount(self):
        return self.successCount

    def setSuccessCount(self, successCount):
        self.successCount = successCount

    def getResults(self):
        return self.results

    def setResults(self, results):
        self.results = results
