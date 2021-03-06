# encoding=utf-8
from enum import Enum

from io1.bumo.exception.SdkError import SdkError


class SdkErrors(Enum):
    SUCCESS = SdkError(0, "1111")
    ACCOUNT_CREATE_ERROR = SdkError(11001, "Failed to create the account")
    INVALID_SOURCEADDRESS_ERROR = SdkError(11002, "Invalid sourceAddress")
    INVALID_DESTADDRESS_ERROR = SdkError(11003, "Invalid destAddress")
    INVALID_INITBALANCE_ERROR = SdkError(11004, "InitBalance must be between 1 and Long.MAX_VALUE")
    SOURCEADDRESS_EQUAL_DESTADDRESS_ERROR = SdkError(11005, "SourceAddress cannot be equal to destAddress")
    INVALID_ADDRESS_ERROR = SdkError(11006, "Invalid address")
    CONNECTNETWORK_ERROR = SdkError(11007, "Failed to connect to the network")
    INVALID_ISSUE_AMOUNT_ERROR = SdkError(11008,
                                          "Amount of the token to be issued must be between 1 and Long.MAX_VALUE")
    NO_ASSET_ERROR = SdkError(11009, "The account does not have this token")
    NO_METADATA_ERROR = SdkError(11010, "The account does not have this metadata")
    INVALID_DATAKEY_ERROR = SdkError(11011, "The length of key must be between 1 and 1024")
    INVALID_DATAVALUE_ERROR = SdkError(11012, "The length of value must be between 0 and 256000")
    INVALID_DATAVERSION_ERROR = SdkError(11013, "The version must be equal to or greater than 0")
    INVALID_MASTERWEIGHT_ERROR = SdkError(11015,
                                          "MasterWeight must be between 0 and (Integer.MAX_VALUE * 2L + 1)")
    INVALID_SIGNER_ADDRESS_ERROR = SdkError(11016, "Invalid signer address")
    INVALID_SIGNER_WEIGHT_ERROR = SdkError(11017,
                                           "Signer weight must be between 0 and (Integer.MAX_VALUE * 2L + 1)")
    INVALID_TX_THRESHOLD_ERROR = SdkError(11018, "TxThreshold must be between 0 and Long.MAX_VALUE")
    INVALID_TYPETHRESHOLD_TYPE_ERROR = SdkError(11019, "Type of TypeThreshold is invalid")
    INVALID_TYPE_THRESHOLD_ERROR = SdkError(11020, "TypeThreshold must be between 0 and Long.MAX_VALUE")
    INVALID_ASSET_CODE_ERROR = SdkError(11023, "The length of key must be between 1 and 64")
    INVALID_ASSET_AMOUNT_ERROR = SdkError(11024, "AssetAmount must be between 0 and Long.MAX_VALUE")
    INVALID_CONTRACT_HASH_ERROR = SdkError(11025, "Invalid transaction hash to create contract")
    INVALID_BU_AMOUNT_ERROR = SdkError(11026, "BuAmount must be between 0 and Long.MAX_VALUE")
    INVALID_ISSUER_ADDRESS_ERROR = SdkError(11027, "Invalid issuer address")
    NO_SUCH_TOKEN_ERROR = SdkError(11030, "No such token")
    INVALID_TOKEN_NAME_ERROR = SdkError(11031, "The length of token name must be between 1 and 1024")
    INVALID_TOKEN_SYMBOL_ERROR = SdkError(11032, "The length of symbol must be between 1 and 1024")
    INVALID_TOKEN_DECIMALS_ERROR = SdkError(11033, "Decimals must be between 0 and 8")
    INVALID_TOKEN_TOTALSUPPLY_ERROR = SdkError(11034, "TotalSupply must be between 1 and Long.MAX_VALUE")
    INVALID_TOKENOWNER_ERRO = SdkError(1035, "Invalid token owner")
    INVALID_TOKEN_SUPPLY_ERRO = SdkError(1036, "Supply * (10 ^ decimals) must be between 1 and Long.MAX_VALUE")
    INVALID_CONTRACTADDRESS_ERRO = SdkError(1037, "Invalid contract address")
    CONTRACTADDRESS_NOT_CONTRACTACCOUNT_ERRO = SdkError(1038, "contractAddress is not a contract account")
    INVALID_TOKEN_AMOUNT_ERRO = SdkError(1039, "TokenAmount must be between 1 and Long.MAX_VALUE")
    SOURCEADDRESS_EQUAL_CONTRACTADDRESS_ERRO = SdkError(1040, "SourceAddress cannot be equal to contractAddress")
    INVALID_FROMADDRESS_ERRO = SdkError(1041, "Invalid fromAddress")
    FROMADDRESS_EQUAL_DESTADDRESS_ERRO = SdkError(1042, "FromAddress cannot be equal to destAddress")
    INVALID_SPENDER_ERRO = SdkError(1043, "Invalid spender")
    PAYLOAD_EMPTY_ERRO = SdkError(1044, "Payload cannot be empty")
    INVALID_LOG_TOPIC_ERRO = SdkError(1045, "The length of a log topic must be between 1 and 128")
    INVALID_LOG_DATA_ERRO = SdkError(1046, "The length of one piece of log data must be between 1 and 1024")
    INVALID_CONTRACT_TYPE_ERRO = SdkError(1047, "Invalid contract type")
    INVALID_NONCE_ERRO = SdkError(1048, "Nonce must be between 1 and Long.MAX_VALUE")
    INVALID_GASPRICE_ERRO = SdkError(1049, "GasPrice must be between 1000 and Long.MAX_VALUE")
    INVALID_FEELIMIT_ERRO = SdkError(1050, "FeeLimit must be between 1 and Long.MAX_VALUE")
    OPERATIONS_EMPTY_ERRO = SdkError(1051, "Operations cannot be empty")
    INVALID_CEILLEDGERSEQ_ERRO = SdkError(1052, "CeilLedgerSeq must be equal to or greater than 0")
    OPERATIONS_ONE_ERRO = SdkError(1053, "One of the operations cannot be resolved")
    INVALID_SIGNATURENUMBER_ERRO = SdkError(1054, "SignagureNumber must be between 1 and Integer.MAX_VALUE")
    INVALID_HASH_ERRO = SdkError(1055, "Invalid transaction hash")
    INVALID_BLOB_ERRO = SdkError(1056, "Invalid blob")
    PRIVATEKEY_NULL_ERRO = SdkError(1057, "PrivateKeys cannot be empty")
    PRIVATEKEY_ONE_ERRO = SdkError(1058, "One of privateKeys is invalid")
    SIGNDATA_NULL_ERRO = SdkError(1059, "SignData cannot be empty")
    INVALID_BLOCKNUMBER_ERRO = SdkError(1060, "BlockNumber must be bigger than 0")
    PUBLICKEY_NULL_ERRO = SdkError(1061, "PublicKey cannot be empty")
    URL_EMPTY_ERRO = SdkError(1062, "Url cannot be empty")
    CONTRACTADDRESS_CODE_BOTH_NULL_ERRO = SdkError(1063,
                                                   "ContractAddress and code cannot be empty at the same time")
    INVALID_OPTTYPE_ERRO = SdkError(1064, "OptType must be between 0 and 2")
    GET_ALLOWANCE_ERRO = SdkError(1065, "Failed to get allowance")
    GET_TOKEN_INFO_ERRO = SdkError(1066, "Failed to get token info")
    SIGNATURE_EMPTY_ERRO = SdkError(1067, "The signatures cannot be empty")
    INVALID_ISSUE_TYPE_ERRO = SdkError(1068, "Invalid issuing type")
    INVALID_TOKEN_CODE_ERRO = SdkError(1069, "The length of token code must be between 1 and 64")
    INVALID_TOKEN_DESCRIPTION_ERRO = SdkError(1070, "The length of description must be between 1 and 1024")
    INVALID_LIMITED_TOKEN_NOW_SUPPLY_ERRO = SdkError(1071,
                                                     "The nowSupply must be between 1 and supply in the limited issuance")
    INVALID_ONE_OFF_NOWSUPPLY_NOT_EQUAL_SUPPLY_ERRO = SdkError(1072,
                                                               "In the one-off issuance, the nowSupply must be equal to supply")
    INVALID_TOKEN_APPEND_SUPPLY_ERRO = SdkError(1073, "The appendSupply must be between 1 and Long.MAX_VALUE")
    INVALID_UNLIMITED_TOKEN_NOW_SUPPLY_ERRO = SdkError(1074,
                                                       "The nowSupply must be between 1 and Long.MAX_VALUE in the unlimited issuance")
    INVALID_ATP10TOKEN_HASH_ERRO = SdkError(1075, "Invalid transaction hash to issue atp1.0 token")
    TOKEN_NOT_FOUND_ERRO = SdkError(1076, "The token is not found")
    CONNECTN_BLOCKCHAIN_ERRO = SdkError(9999, "Failed to connect blockchain")
    SYSTEM_ERROR = SdkError(20000, "System error")
    REQUEST_NULL_ERRO = SdkError(2001, "Request parameter cannot be null")
