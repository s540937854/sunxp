# encoding=utf-8
from typing import List

from io1.bumo.model.response.result.data.Signature import Signature


class TransactionSignResult:
    signatures = []  # type: List[Signature]

    def getSignatures(self):
        return self.signatures

    def setSignatures(self, signatures):
        self.signatures = signatures
