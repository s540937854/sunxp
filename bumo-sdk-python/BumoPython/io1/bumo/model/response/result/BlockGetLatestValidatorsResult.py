# encoding=utf-8
from io1.bumo.model.response.result.data.ValidatorInfo import ValidatorInfo


class BlockGetLatestValidatorsResult:
    validators = []  # type: list[ValidatorInfo]

    def getValidators(self):
        return self.validators

    def setValidators(self, validators):
        self.validators = validators
