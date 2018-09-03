# encoding=utf-8
from io1.bumo.crypto.protobuf import chain_pb2
from io1.bumo.encryption.key.PublicKey import PublicKey
from io1.bumo.exception.SDKException import SDKException
from io1.bumo.exception.SdkErrors import SdkErrors


class AccountService:

    @classmethod
    def activate(cls, accountActivateOperation, transSourceAddress):
        operation = None
        try:
            if not accountActivateOperation:
                raise SDKException(SdkErrors.REQUEST_NULL_ERRO.getCode(), SdkErrors.REQUEST_NULL_ERRO.getDescription())
            sourceAddress = accountActivateOperation.getSourceAddress()
            if not (not sourceAddress) and not PublicKey().isAddressValid(sourceAddress):
                raise SDKException(SdkErrors.INVALID_SOURCEADDRESS_ERROR.getCode(),
                                   SdkErrors.INVALID_SOURCEADDRESS_ERROR.getDescription())
            destAddress = accountActivateOperation.getDestAddress()
            if not PublicKey().isAddressValid(destAddress):
                raise SDKException(SdkErrors.INVALID_DESTADDRESS_ERROR.getCode(),
                                   SdkErrors.INVALID_DESTADDRESS_ERROR.getDescription())
            isNotValid = not (not sourceAddress) and sourceAddress == destAddress and transSourceAddress == destAddress
            if isNotValid:
                raise SDKException(SdkErrors.SOURCEADDRESS_EQUAL_DESTADDRESS_ERROR.getCode(),
                                   SdkErrors.SOURCEADDRESS_EQUAL_DESTADDRESS_ERROR.getDescription())
            initBalance = accountActivateOperation.getInitBalance()
            if not initBalance or initBalance <= 0:
                raise SDKException(SdkErrors.INVALID_INITBALANCE_ERROR.getCode(),
                                   SdkErrors.INVALID_INITBALANCE_ERROR.getDescription())

            metadata = accountActivateOperation.getMetadata()
            operation = cls.buildActivateOperation(sourceAddress, destAddress, initBalance, metadata)

        except SDKException, e:
            raise e
        except Exception:
            return SDKException(SdkErrors.SYSTEM_ERROR.getCode(), SdkErrors.SYSTEM_ERROR.getDescription())

    @classmethod
    def buildActivateOperation(cls, sourceAddress, destAddress, initBalance, metadata):
        transaction = chain_pb2.Transaction()
        operation = transaction.operations.add()