# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# The current account does not exist.
ACCOUNTNOTEXIST = 'AccountNotExist'

# CAM signature/authentication error.
AUTHFAILURE = 'AuthFailure'

# Authentication failed.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# Backend database execution error.
DBERROR = 'DBError'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Failed to access classic network. Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_BASENETWORKACCESSERROR = 'FailedOperation.BaseNetworkAccessError'

# Failed to access CMQ.
FAILEDOPERATION_CMQRESPONSEERROR = 'FailedOperation.CMQResponseError'

# CAM authentication failed.
FAILEDOPERATION_CAMAUTHFAILED = 'FailedOperation.CamAuthFailed'

# Failed to get permissions. Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_CAMCHECKRESOURCEERROR = 'FailedOperation.CamCheckResourceError'

# Failed to check resource permissions through CAM.
FAILEDOPERATION_CAMCHECKRESOURCEFAILED = 'FailedOperation.CamCheckResourceFailed'

# Authentication failed. Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_CAMSIGANDAUTHERROR = 'FailedOperation.CamSigAndAuthError'

# Failed to get project information. Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_CDBCGWCONNECTERROR = 'FailedOperation.CdbCgwConnectError'

# Classic network creation is unsupported.
FAILEDOPERATION_CREATEBASICNETWORKDENIEDERROR = 'FailedOperation.CreateBasicNetworkDeniedError'

# Failed to create the renewal order.
FAILEDOPERATION_CREATEORDERFAILED = 'FailedOperation.CreateOrderFailed'

# Failed to access database management service. Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_DATABASEACCESSERROR = 'FailedOperation.DatabaseAccessError'

# Data operation failed. Please contact customer service.
FAILEDOPERATION_DATABASEAFFECTEDERROR = 'FailedOperation.DatabaseAffectedError'

# Failed to delete VPC routes.
FAILEDOPERATION_DELETEALLROUTE = 'FailedOperation.DeleteAllRoute'

# Failed to unbind resources from a project.
FAILEDOPERATION_DELETERESOURCEPROJECTTAGERROR = 'FailedOperation.DeleteResourceProjectTagError'

# Failed to unbind the resource from the tag.
FAILEDOPERATION_DELETERESOURCESTOTAGERROR = 'FailedOperation.DeleteResourcesToTagError'

# Failed to access ES. Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_ESCONNECTERROR = 'FailedOperation.ESConnectError'

# Failed to query ES. Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_ESQUERYERROR = 'FailedOperation.ESQueryError'

# Operation failed. Please try again later.
FAILEDOPERATION_FAILEDOPERATIONERROR = 'FailedOperation.FailedOperationError'

# Failed to create a task. Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_FLOWCREATEERROR = 'FailedOperation.FlowCreateError'

# Failed to query the instance information. Please try again later.
FAILEDOPERATION_GETINSTANCEBYRESOURCEIDERROR = 'FailedOperation.GetInstanceByResourceIdError'

# Failed to get the purchase record.
FAILEDOPERATION_GETPURCHASERECORDFAILED = 'FailedOperation.GetPurchaseRecordFailed'

# Failed to query VPC subnets.
FAILEDOPERATION_GETSUBNETERROR = 'FailedOperation.GetSubnetError'

# Failed to query VPC information. Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_GETVPCINFOERROR = 'FailedOperation.GetVpcInfoError'

# Invalid number of read-only replicas.
FAILEDOPERATION_ILLEGALROINSTANCENUM = 'FailedOperation.IllegalROInstanceNum'

# The account status is incorrect, so the operation is not allowed.
FAILEDOPERATION_INVALIDACCOUNTSTATUS = 'FailedOperation.InvalidAccountStatus'

# Billing error. Corresponding purchase/renewal/configuration change operations are not allowed for the current instance.
FAILEDOPERATION_INVALIDTRADEOPERATE = 'FailedOperation.InvalidTradeOperate'

# Operations are not allowed on the instance.
FAILEDOPERATION_LIMITOPERATION = 'FailedOperation.LimitOperation'

# Failed to query the primary instance information.
FAILEDOPERATION_MASTERINSTANCEQUERYERROR = 'FailedOperation.MasterInstanceQueryError'

# Failed to modify RO group configuration.
FAILEDOPERATION_MODIFYROGROUPERROR = 'FailedOperation.ModifyROGroupError'

# The number of networks does not meet resource requirements.
FAILEDOPERATION_NETWORKNUMLIMITERROR = 'FailedOperation.NetworkNumLimitError'

# Failed to access database management service. Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_OSSACCESSERROR = 'FailedOperation.OssAccessError'

# Failed to request the backend API.
FAILEDOPERATION_OSSOPERATIONFAILED = 'FailedOperation.OssOperationFailed'

# Failed to make order payment.
FAILEDOPERATION_PAYORDERFAILED = 'FailedOperation.PayOrderFailed'

# Failed to unfreeze the account of a pay-as-you-go instance. Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_POSTPAIDUNBLOCKERROR = 'FailedOperation.PostPaidUnblockError'

# An error occurred while getting the pre-signed authorization URL.
FAILEDOPERATION_PRESIGNEDURLGETERROR = 'FailedOperation.PresignedURLGetError'

# Failed to query the order information.
FAILEDOPERATION_QUERYDEALFAILED = 'FailedOperation.QueryDealFailed'

# Failed to query instance information in batches. Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_QUERYINSTANCEBATCHERROR = 'FailedOperation.QueryInstanceBatchError'

# Failed to query the price.
FAILEDOPERATION_QUERYPRICEFAILED = 'FailedOperation.QueryPriceFailed'

# Failed to query specifications.
FAILEDOPERATION_QUERYSPECBYSPECCODEERROR = 'FailedOperation.QuerySpecBySpecCodeError'

# Failed to query specifications. Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_QUERYSPECERROR = 'FailedOperation.QuerySpecError'

# Failed to query the order status.
FAILEDOPERATION_QUERYTRADESTATUSERROR = 'FailedOperation.QueryTradeStatusError'

# Failed to query VPC.
FAILEDOPERATION_QUERYVPCFAILED = 'FailedOperation.QueryVpcFailed'

# Failed to get VPC details.
FAILEDOPERATION_QUERYVPCFALIED = 'FailedOperation.QueryVpcFalied'

# This RO group has at least one read-only replica, so it cannot be deleted.
FAILEDOPERATION_ROGROUPCANNOTBEDELETEDERROR = 'FailedOperation.ROGroupCannotBeDeletedError'

# The primary instance information of the RO group is not matched.
FAILEDOPERATION_ROGROUPMASTERINSTANCENOTRIGHT = 'FailedOperation.ROGroupMasterInstanceNotRight'

# The RO group does not exist.
FAILEDOPERATION_ROGROUPNOTFOUNDERROR = 'FailedOperation.ROGroupNotFoundError'

# The maximum number of RO groups has been reached.
FAILEDOPERATION_ROGROUPNUMEXCEEDERROR = 'FailedOperation.ROGroupNumExceedError'

# This read-only replica already belongs to another RO group.
FAILEDOPERATION_ROINSTANCEHASINROGROUPERROR = 'FailedOperation.ROInstanceHasInROGroupError'

# Serverless instances do not support the operation.
FAILEDOPERATION_SERVERLESSNOTSUPPORTEDERROR = 'FailedOperation.ServerlessNotSupportedError'

# Failed to access internal service. Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_SERVICEACCESSERROR = 'FailedOperation.ServiceAccessError'

# Failed to set the auto-renewal flag.
FAILEDOPERATION_SETAUTORENEWFLAGERROR = 'FailedOperation.SetAutoRenewFlagError'

# The memory and storage capacity to which an instance is upgraded should be higher than its original memory and storage capacity.
FAILEDOPERATION_STORAGEMEMORYCHECKERROR = 'FailedOperation.StorageMemoryCheckError'

# Incorrect storage path format
FAILEDOPERATION_STOREPATHSPLITERROR = 'FailedOperation.StorePathSplitError'

# Failed to access the billing platform. Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_TRADEACCESSERROR = 'FailedOperation.TradeAccessError'

# Failed to request the billing platform to create an order.
FAILEDOPERATION_TRADECREATEERROR = 'FailedOperation.TradeCreateError'

# Failed to request to pay for the order.
FAILEDOPERATION_TRADEPAYORDERSERROR = 'FailedOperation.TradePayOrdersError'

# Failed to query order information. Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_TRADEQUERYORDERERROR = 'FailedOperation.TradeQueryOrderError'

# Failed to query pricing information. Please try again later. If the problem persists, please contact customer service.
FAILEDOPERATION_TRADEQUERYPRICEERROR = 'FailedOperation.TradeQueryPriceError'

# Failed to modify the resource tag.
FAILEDOPERATION_UPDATERESOURCEPROJECTTAGVALUEERROR = 'FailedOperation.UpdateResourceProjectTagValueError'

# Failed to configure the VPC.
FAILEDOPERATION_VPCRESETSERVICEERROR = 'FailedOperation.VPCResetServiceError'

# Failed to update VPC routes.
FAILEDOPERATION_VPCUPDATEROUTEERROR = 'FailedOperation.VPCUpdateRouteError'

# Failed to create the task.
FLOWERROR = 'FlowError'

# The current instance does not exist.
INSTANCENOTEXIST = 'InstanceNotExist'

# `ACTION` input error.
INTERFACENAMENOTFOUND = 'InterfaceNameNotFound'

# Internal error.
INTERNALERROR = 'InternalError'

# CGW error.
INTERNALERROR_CGWERROR = 'InternalError.CgwError'

# Basic network error.
INTERNALERROR_CNSERROR = 'InternalError.CnsError'

# Backend database execution error.
INTERNALERROR_DBERROR = 'InternalError.DBError'

# DFW error.
INTERNALERROR_DFWERROR = 'InternalError.DfwError'

# Failed to create the flow.
INTERNALERROR_FLOWERROR = 'InternalError.FlowError'

# Failed to access database management service. Please contact customer service.
INTERNALERROR_INSTANCEDATAERROR = 'InternalError.InstanceDataError'

# Failed to parse background data. Please contact customer service.
INTERNALERROR_MARSHALERROR = 'InternalError.MarshalError'

# System error. When this error occurs, please contact customer service for assistance.
INTERNALERROR_SYSTEMERROR = 'InternalError.SystemError'

# Unknown error. When this error occurs, please contact customer service for assistance.
INTERNALERROR_UNKNOWNERROR = 'InternalError.UnknownError'

# VPC error.
INTERNALERROR_VPCERROR = 'InternalError.VpcError'

# Incorrect account password.
INVALIDACCOUNTPASSWORD = 'InvalidAccountPassword'

# The current account status is incorrect, so the operation is not allowed.
INVALIDACCOUNTSTATUS = 'InvalidAccountStatus'

# Incorrect instance status.
INVALIDINSTANCESTATUS = 'InvalidInstanceStatus'

# Billing error: invalid order type ID.
INVALIDORDERNUM = 'InvalidOrderNum'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# The instance name already exists.
INVALIDPARAMETER_INSTANCENAMEEXIST = 'InvalidParameter.InstanceNameExist'

# Failed to check the parameter.
INVALIDPARAMETER_PARAMETERCHECKERROR = 'InvalidParameter.ParameterCheckError'

# Incorrect PID
INVALIDPARAMETER_TRADEACCESSDENIEDERROR = 'InvalidParameter.TradeAccessDeniedError'

# Failed to query VPC information.
INVALIDPARAMETER_VPCNOTFOUNDERROR = 'InvalidParameter.VpcNotFoundError'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The current account already exists.
INVALIDPARAMETERVALUE_ACCOUNTEXIST = 'InvalidParameterValue.AccountExist'

# The current account does not exist.
INVALIDPARAMETERVALUE_ACCOUNTNOTEXIST = 'InvalidParameterValue.AccountNotExist'

# The account does not exist.
INVALIDPARAMETERVALUE_ACCOUNTNOTEXISTERROR = 'InvalidParameterValue.AccountNotExistError'

# The instance specification to upgrade to is not purchasable.
INVALIDPARAMETERVALUE_BADSPEC = 'InvalidParameterValue.BadSpec'

# Incorrect database character set
INVALIDPARAMETERVALUE_CHARSETNOTFOUNDERROR = 'InvalidParameterValue.CharsetNotFoundError'

# Failed to convert data format. Please contact customer service.
INVALIDPARAMETERVALUE_DATACONVERTERROR = 'InvalidParameterValue.DataConvertError'

# Unsupported billing type.
INVALIDPARAMETERVALUE_ILLEGALCHARGETYPE = 'InvalidParameterValue.IllegalChargeType'

# Incorrect billing mode.
INVALIDPARAMETERVALUE_ILLEGALINSTANCECHARGETYPE = 'InvalidParameterValue.IllegalInstanceChargeType'

# Invalid `ProjectId`.
INVALIDPARAMETERVALUE_ILLEGALPROJECTID = 'InvalidParameterValue.IllegalProjectId'

# Invalid `Region` parameter.
INVALIDPARAMETERVALUE_ILLEGALREGION = 'InvalidParameterValue.IllegalRegion'

# Invalid `Zone` parameter.
INVALIDPARAMETERVALUE_ILLEGALZONE = 'InvalidParameterValue.IllegalZone'

# The account already exists.
INVALIDPARAMETERVALUE_INSTANCENAMEEXIST = 'InvalidParameterValue.InstanceNameExist'

# The current instance does not exist.
INVALIDPARAMETERVALUE_INSTANCENOTEXIST = 'InvalidParameterValue.InstanceNotExist'

# Incorrect `ACTION`.
INVALIDPARAMETERVALUE_INTERFACENAMENOTFOUND = 'InvalidParameterValue.InterfaceNameNotFound'

# Invalid account. The account name is case-insensitive, must contain 1-16 characters comprised of letters, digits, underscores, and should neither be "postgres" nor start with a digit or "pg_".
INVALIDPARAMETERVALUE_INVALIDACCOUNTERROR = 'InvalidParameterValue.InvalidAccountError'

# Incorrect account format.
INVALIDPARAMETERVALUE_INVALIDACCOUNTFORMAT = 'InvalidParameterValue.InvalidAccountFormat'

# The current account name cannot be a reserved character.
INVALIDPARAMETERVALUE_INVALIDACCOUNTNAME = 'InvalidParameterValue.InvalidAccountName'

# Incorrect database character set. Currently, only `UTF8` and `LATIN1` are supported.
INVALIDPARAMETERVALUE_INVALIDCHARSET = 'InvalidParameterValue.InvalidCharset'

# The number of purchased instances exceeds the limit.
INVALIDPARAMETERVALUE_INVALIDINSTANCENUM = 'InvalidParameterValue.InvalidInstanceNum'

# The instance specification to upgrade to cannot be lower than the current instance specification.
INVALIDPARAMETERVALUE_INVALIDINSTANCEVOLUME = 'InvalidParameterValue.InvalidInstanceVolume'

# Billing error. Invalid order type ID.
INVALIDPARAMETERVALUE_INVALIDORDERNUM = 'InvalidParameterValue.InvalidOrderNum'

# Incorrect parameter value
INVALIDPARAMETERVALUE_INVALIDPARAMETERVALUEERROR = 'InvalidParameterValue.InvalidParameterValueError'

# Incorrect password format.
INVALIDPARAMETERVALUE_INVALIDPASSWORDFORMAT = 'InvalidParameterValue.InvalidPasswordFormat'

# Invalid password. The password length does not meet the requirements.
INVALIDPARAMETERVALUE_INVALIDPASSWORDLENGTHERROR = 'InvalidParameterValue.InvalidPasswordLengthError'

# Invalid password. The password must contain uppercase letters, lowercase letters, digits, and symbols (()`~!@#$%^&*-+=_|{}[]:;'<>,.?/), and cannot start with a slash (/).
INVALIDPARAMETERVALUE_INVALIDPASSWORDVALUEERROR = 'InvalidParameterValue.InvalidPasswordValueError'

# Incorrect `PID` parameter.
INVALIDPARAMETERVALUE_INVALIDPID = 'InvalidParameterValue.InvalidPid'

# RO group in incorrect status
INVALIDPARAMETERVALUE_INVALIDREADONLYGROUPSTATUS = 'InvalidParameterValue.InvalidReadOnlyGroupStatus'

# Invalid availability zone.
INVALIDPARAMETERVALUE_INVALIDZONEIDERROR = 'InvalidParameterValue.InvalidZoneIdError'

# Empty order name.
INVALIDPARAMETERVALUE_NULLDEALNAMES = 'InvalidParameterValue.NullDealNames'

# Invalid parameter. The parameter can contain only letters, digits, underscores, and hyphens.
INVALIDPARAMETERVALUE_PARAMETERCHARACTERERROR = 'InvalidParameterValue.ParameterCharacterError'

# The parameter is invalid. Please modify it and try again.
INVALIDPARAMETERVALUE_PARAMETERCHARACTERLIMITERROR = 'InvalidParameterValue.ParameterCharacterLimitError'

# The parameter prefix is invalid. Please modify it and try again.
INVALIDPARAMETERVALUE_PARAMETERCHARACTERPRELIMITERROR = 'InvalidParameterValue.ParameterCharacterPreLimitError'

# Failed to process the parameter. Please check if the parameter value is valid.
INVALIDPARAMETERVALUE_PARAMETERHANDLEERROR = 'InvalidParameterValue.ParameterHandleError'

# The length of parameter exceeds the limit.
INVALIDPARAMETERVALUE_PARAMETERLENGTHLIMITERROR = 'InvalidParameterValue.ParameterLengthLimitError'

# Invalid parameter values.
INVALIDPARAMETERVALUE_PARAMETEROUTRANGEERROR = 'InvalidParameterValue.ParameterOutRangeError'

# The maximum value of the parameter has been reached.
INVALIDPARAMETERVALUE_PARAMETERVALUEEXCEEDERROR = 'InvalidParameterValue.ParameterValueExceedError'

# The RO group does not exist.
INVALIDPARAMETERVALUE_READONLYGROUPNOTEXIST = 'InvalidParameterValue.ReadOnlyGroupNotExist'

# The current region is not supported.
INVALIDPARAMETERVALUE_REGIONNOTSUPPORTED = 'InvalidParameterValue.RegionNotSupported'

# Failed to identify the specification ({{1}}).
INVALIDPARAMETERVALUE_SPECNOTRECOGNIZEDERROR = 'InvalidParameterValue.SpecNotRecognizedError'

# An error occurred while parsing parameters.
INVALIDPARAMETERVALUE_STRUCTPARSEFAILED = 'InvalidParameterValue.StructParseFailed'

# Incorrect `PID` parameter.
INVALIDPID = 'InvalidPid'

# Billing error: such operations as purchase, renewal, and configuration change are not allowed for the instance.
INVALIDTRADEOPERATE = 'InvalidTradeOperate'

# Billing error: the specified voucher is invalid.
INVALIDVOUCHERID = 'InvalidVoucherId'

# Quota limit exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# Operations are not allowed on the instance.
LIMITOPERATION = 'LimitOperation'

# Missing parameters.
MISSINGPARAMETER = 'MissingParameter'

# This operation cannot be performed.
OPERATIONDENIED_CAMDENIEDERROR = 'OperationDenied.CamDeniedError'

# The target instance failed the status check.
OPERATIONDENIED_DTSINSTANCESTATUSERROR = 'OperationDenied.DTSInstanceStatusError'

# You do not have the permission to operate this resource.
OPERATIONDENIED_INSTANCEACCESSDENIEDERROR = 'OperationDenied.InstanceAccessDeniedError'

# IPv6 is not supported.
OPERATIONDENIED_INSTANCEIPV6NOTSUPPORTEDERROR = 'OperationDenied.InstanceIpv6NotSupportedError'

# This operation cannot be performed on an instance in this status.
OPERATIONDENIED_INSTANCESTATUSDENIEDERROR = 'OperationDenied.InstanceStatusDeniedError'

# This operation cannot be performed on an instance in this status.
OPERATIONDENIED_INSTANCESTATUSLIMITERROR = 'OperationDenied.InstanceStatusLimitError'

# This operation cannot be performed on an instance in this status.
OPERATIONDENIED_INSTANCESTATUSLIMITOPERROR = 'OperationDenied.InstanceStatusLimitOpError'

# Serverless is not supported in this availability zone.
OPERATIONDENIED_NOTSUPPORTZONEERROR = 'OperationDenied.NotSupportZoneError'

# Unsupported billing mode
OPERATIONDENIED_PAYMODEERROR = 'OperationDenied.PayModeError'

# Pay-as-you-go instances cannot be renewed.
OPERATIONDENIED_POSTPAIDPAYMODEERROR = 'OperationDenied.PostPaidPayModeError'

# This operation cannot be performed on an RO group in this status.
OPERATIONDENIED_ROGROUPSTATUSERROR = 'OperationDenied.ROGroupStatusError'

# Read-only instances do not support IPv6.
OPERATIONDENIED_ROINSTANCEIPV6NOTSUPPORTEDERROR = 'OperationDenied.ROInstanceIpv6NotSupportedError'

# The total number of read-only nodes should not exceed the upper limit.
OPERATIONDENIED_ROINSTANCECOUNTEXEEDERROR = 'OperationDenied.RoInstanceCountExeedError'

# You need to verify your identity to make a purchase.
OPERATIONDENIED_USERNOTAUTHENTICATEDERROR = 'OperationDenied.UserNotAuthenticatedError'

# Serverless is not supported on this version of PostgreSQL.
OPERATIONDENIED_VERSIONNOTSUPPORTERROR = 'OperationDenied.VersionNotSupportError'

# You do not have the permission to operate the VPC.
OPERATIONDENIED_VPCDENIEDERROR = 'OperationDenied.VpcDeniedError'

# The region is not supported.
REGIONNOTSUPPORTED = 'RegionNotSupported'

# The number of requests exceeds the frequency limit.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# There are not enough resources to purchase instances of this specification in the current region.
RESOURCEINSUFFICIENT_RESOURCENOTENOUGH = 'ResourceInsufficient.ResourceNotEnough'

# Resource not found.
RESOURCENOTFOUND = 'ResourceNotFound'

# The instance does not exist.
RESOURCENOTFOUND_INSTANCENOTFOUNDERROR = 'ResourceNotFound.InstanceNotFoundError'

# Incorrect instance status.
RESOURCEUNAVAILABLE_INVALIDINSTANCESTATUS = 'ResourceUnavailable.InvalidInstanceStatus'

# No permission for the VPC.
RESOURCEUNAVAILABLE_RESOURCENOPERMISSION = 'ResourceUnavailable.ResourceNoPermission'

# Failed to get the information of the VPC where the instance resides.
RESOURCEUNAVAILABLE_VPCRESOURCENOTFOUND = 'ResourceUnavailable.VpcResourceNotFound'

# An error occurred while parsing parameters.
STRUCTPARSEFAILED = 'StructParseFailed'

# System error. When this error occurs, please contact customer service for assistance.
SYSTEMERROR = 'SystemError'

# Unverified user.
UNAUTHORIZEDOPERATION_USERHASNOREALNAMEAUTHENTICATION = 'UnauthorizedOperation.UserHasNoRealnameAuthentication'

# Unknown error. When this error occurs, please contact customer service for assistance.
UNKNOWNERROR = 'UnknownError'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# VPC error
VPCERROR = 'VpcError'
