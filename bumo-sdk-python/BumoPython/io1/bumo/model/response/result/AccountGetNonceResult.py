# encoding=utf-8


class AccountGetNonceResult:
    nonce = 0L

    def getNonce(self):
        return self.nonce

    def setNonce(self, nonce):
        self.nonce = nonce
