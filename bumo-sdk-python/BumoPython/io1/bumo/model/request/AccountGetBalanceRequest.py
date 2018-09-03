# encoding=utf-8

class AccountGetBalanceRequest:
    address = ""

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address
