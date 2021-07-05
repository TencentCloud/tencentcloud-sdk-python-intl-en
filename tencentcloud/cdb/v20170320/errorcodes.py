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


# CAM signature/authentication error.
AUTHFAILURE = 'AuthFailure'

# Backend or process error.
CDBERROR = 'CdbError'

# Backup error.
CDBERROR_BACKUPERROR = 'CdbError.BackupError'

# Backend database error.
CDBERROR_DATABASEERROR = 'CdbError.DatabaseError'

# Import task error.
CDBERROR_IMPORTERROR = 'CdbError.ImportError'

# Backend task error.
CDBERROR_TASKERROR = 'CdbError.TaskError'

# Async task exception.
FAILEDOPERATION_ASYNCTASKSTATUSERROR = 'FailedOperation.AsyncTaskStatusError'

# Creation failed. Please check whether the user already exists.
FAILEDOPERATION_CREATEACCOUNTERROR = 'FailedOperation.CreateAccountError'

# Failed to assign an exclusive VIP to the read-only replica.
FAILEDOPERATION_CREATEROVIPERROR = 'FailedOperation.CreateRoVipError'

# Database operation failed.
FAILEDOPERATION_DBOPERATIONACTIONERROR = 'FailedOperation.DBOperationActionError'

# An error occurred while obtaining permissions.
FAILEDOPERATION_GETPRIVILEGEERROR = 'FailedOperation.GetPrivilegeError'

# Failed to deserialize JSON.
FAILEDOPERATION_JSONUNMARSHALERROR = 'FailedOperation.JsonUnmarshalError'

# The instance is not a delayed RO replica.
FAILEDOPERATION_NOTDELAYRO = 'FailedOperation.NotDelayRo'

# Failed to call the backend API to enable delayed replication.
FAILEDOPERATION_OPERATIONREPLICATIONERROR = 'FailedOperation.OperationReplicationError'

# The executed operation to modify permissions is invalid. You can refer to product documentation for more information about permissions that can be modified for this instance. If you have any questions, please contact customer service.
FAILEDOPERATION_PRIVILEGEDATAILLEGAL = 'FailedOperation.PrivilegeDataIllegal'

# Log query failed.
FAILEDOPERATION_QUERYLOGERROR = 'FailedOperation.QueryLogError'

# Exception with the backend request for the service. Please contact customer service.
FAILEDOPERATION_RESPONSEVALUEERROR = 'FailedOperation.ResponseValueError'

# Failed to initiate the operation. Please try again later. If the operation remains unsuccessful, please contact customer service.
FAILEDOPERATION_STARTFLOWERROR = 'FailedOperation.StartFlowError'

# Task status conflict.
FAILEDOPERATION_STATUSCONFLICT = 'FailedOperation.StatusConflict'

# Failed to submit the task. Please try again later. If the submission remains unsuccessful, please contact customer service.
FAILEDOPERATION_SUBMITASYNCTASKERROR = 'FailedOperation.SubmitAsyncTaskError'

# An internal error occurred.
INTERNALERROR = 'InternalError'

# An error occurred while querying async tasks.
INTERNALERROR_ASYNCREQUESTERROR = 'InternalError.AsyncRequestError'

# Authentication failed.
INTERNALERROR_AUTHERROR = 'InternalError.AuthError'

# Internal system error.
INTERNALERROR_CDBCGWERROR = 'InternalError.CdbCgwError'

# System error.
INTERNALERROR_CDBERROR = 'InternalError.CdbError'

# Failed to obtain file information.
INTERNALERROR_COSERROR = 'InternalError.CosError'

# Database exception
INTERNALERROR_DBERROR = 'InternalError.DBError'

# Database operation failed.
INTERNALERROR_DBOPERATIONERROR = 'InternalError.DBOperationError'

# The database record does not exist.
INTERNALERROR_DBRECORDNOTEXISTERROR = 'InternalError.DBRecordNotExistError'

# Internal database error.
INTERNALERROR_DATABASEACCESSERROR = 'InternalError.DatabaseAccessError'

# Internal system error.
INTERNALERROR_DESERROR = 'InternalError.DesError'

# Security group operation error.
INTERNALERROR_DFWERROR = 'InternalError.DfwError'

# SQL statement error
INTERNALERROR_EXESQLERROR = 'InternalError.ExeSqlError'

# File transfer exception
INTERNALERROR_FTPERROR = 'InternalError.FtpError'

# Exceptional HTTP request
INTERNALERROR_HTTPERROR = 'InternalError.HttpError'

# Internal service error. Please contact customer service.
INTERNALERROR_INTERNALASSERTERROR = 'InternalError.InternalAssertError'

# An exception occurred while executing the request.
INTERNALERROR_INTERNALHTTPSERVERERROR = 'InternalError.InternalHttpServerError'

# The backend failed to request the service. Please contact customer service.
INTERNALERROR_INTERNALREQUESTERROR = 'InternalError.InternalRequestError'

# An error occurred while accessing internal service.
INTERNALERROR_INTERNALSERVICEERRORERR = 'InternalError.InternalServiceErrorErr'

# Failed to parse JSON.
INTERNALERROR_JSONERROR = 'InternalError.JSONError'

# Network error
INTERNALERROR_NETWORKERROR = 'InternalError.NetworkError'

# An error occurred in TencentDB for MySQL High-Availability Edition database service.
INTERNALERROR_OSSERROR = 'InternalError.OssError'

# Parameter error
INTERNALERROR_PARAMERROR = 'InternalError.ParamError'

# Regular expression compilation error.
INTERNALERROR_REGEXPCOMPILEERROR = 'InternalError.RegexpCompileError'

# The resource does not match.
INTERNALERROR_RESOURCENOTMATCH = 'InternalError.ResourceNotMatch'

# The resource is not unique.
INTERNALERROR_RESOURCENOTUNIQUE = 'InternalError.ResourceNotUnique'

# Security group error
INTERNALERROR_SECURITYGROUPERROR = 'InternalError.SecurityGroupError'

# Failed to modify the tag. Please try again later.
INTERNALERROR_TAGERROR = 'InternalError.TagError'

# Task exception
INTERNALERROR_TASKERROR = 'InternalError.TaskError'

# Async task error.
INTERNALERROR_TASKFRAMEERROR = 'InternalError.TaskFrameError'

# Time window error
INTERNALERROR_TIMEWINDOWERROR = 'InternalError.TimeWindowError'

# Transaction system error.
INTERNALERROR_TRADEERROR = 'InternalError.TradeError'

# Unknown error
INTERNALERROR_UNDEFINEDERROR = 'InternalError.UndefinedError'

# Unknown error
INTERNALERROR_UNKNOWNERROR = 'InternalError.UnknownError'

# VPC or subnet error.
INTERNALERROR_VPCERROR = 'InternalError.VpcError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# This API was not found.
INVALIDPARAMETER_CONTROLLERNOTFOUNDERROR = 'InvalidParameter.ControllerNotFoundError'

# There are resources in the placement group.
INVALIDPARAMETER_DEPLOYGROUPNOTEMPTY = 'InvalidParameter.DeployGroupNotEmpty'

# The instance is not found.
INVALIDPARAMETER_INSTANCENAMENOTFOUND = 'InvalidParameter.InstanceNameNotFound'

# The instance does not exist.
INVALIDPARAMETER_INSTANCENOTFOUND = 'InvalidParameter.InstanceNotFound'

# The async task does not exist.
INVALIDPARAMETER_INVALIDASYNCREQUESTID = 'InvalidParameter.InvalidAsyncRequestId'

# Invalid name.
INVALIDPARAMETER_INVALIDNAME = 'InvalidParameter.InvalidName'

# Invalid parameter value
INVALIDPARAMETER_INVALIDPARAMETERERROR = 'InvalidParameter.InvalidParameterError'

# 
INVALIDPARAMETER_JSONUNMARSHALERROR = 'InvalidParameter.JsonUnmarshalError'

# The quota of placement group resources has been exceeded.
INVALIDPARAMETER_OVERDEPLOYGROUPQUOTA = 'InvalidParameter.OverDeployGroupQuota'

# The resource already exists.
INVALIDPARAMETER_RESOURCEEXISTS = 'InvalidParameter.ResourceExists'

# The resource does not exist.
INVALIDPARAMETER_RESOURCENOTEXISTS = 'InvalidParameter.ResourceNotExists'

# The resource is not found.
INVALIDPARAMETER_RESOURCENOTFOUND = 'InvalidParameter.ResourceNotFound'

# The account description contains special characters.
INVALIDPARAMETERVALUE_ACCOUNTDESCRIPTIONCHARACTERERROR = 'InvalidParameterValue.AccountDescriptionCharacterError'

# The account description should not exceed 255 characters.
INVALIDPARAMETERVALUE_ACCOUNTDESCRIPTIONLENGTHERROR = 'InvalidParameterValue.AccountDescriptionLengthError'

# Incorrect format of the `host` parameter in the account.
INVALIDPARAMETERVALUE_ACCOUNTHOSTRULEERROR = 'InvalidParameterValue.AccountHostRuleError'

# The account password contains invalid characters.
INVALIDPARAMETERVALUE_ACCOUNTPASSWORDCHARACTERERROR = 'InvalidParameterValue.AccountPasswordCharacterError'

# The account password is too long or too short.
INVALIDPARAMETERVALUE_ACCOUNTPASSWORDLENGTHERROR = 'InvalidParameterValue.AccountPasswordLengthError'

# The password format is incorrect. It should contain 8 to 64 characters and must contain at least two character sets of the following: letters, digits, and special symbols (_+-&=!@#$%^*()).
INVALIDPARAMETERVALUE_ACCOUNTPASSWORDRULEERROR = 'InvalidParameterValue.AccountPasswordRuleError'

# Data conversion failed.
INVALIDPARAMETERVALUE_DATACONVERTERROR = 'InvalidParameterValue.DataConvertError'

# The specified point in time should not be later than the current time.
INVALIDPARAMETERVALUE_DUETIMEWRONG = 'InvalidParameterValue.DueTimeWrong'

# Invalid parameter value
INVALIDPARAMETERVALUE_INVALIDPARAMETERVALUEERROR = 'InvalidParameterValue.InvalidParameterValueError'

# The original type should not be the same as the target type.
INVALIDPARAMETERVALUE_SRCTYPEEQUALDSTTYPE = 'InvalidParameterValue.SrcTypeEqualDstType'

# The RO replica is not the type of instance allowed by the operation.
INVALIDPARAMETERVALUE_SRCTYPENOTEQUALDSTTYPE = 'InvalidParameterValue.SrcTypeNotEqualDstType'

# Incorrect format of the account username.
INVALIDPARAMETERVALUE_USERNAMERULEERROR = 'InvalidParameterValue.UserNameRuleError'

# The account does not exist.
INVALIDPARAMETERVALUE_USERNOTEXISTERROR = 'InvalidParameterValue.UserNotExistError'

# No root account found.
INVALIDPARAMETERVALUE_VERIFYACCOUNTNOROOTERROR = 'InvalidParameterValue.VerifyAccountNoRootError'

# Invalid account password.
INVALIDPARAMETERVALUE_VERIFYACCOUNTPASSWORDERROR = 'InvalidParameterValue.VerifyAccountPasswordError'

# The account does not have the GRANT permission.
INVALIDPARAMETERVALUE_VERIFYACCOUNTPRIVERROR = 'InvalidParameterValue.VerifyAccountPrivError'

# Account-related parameters are missing.
MISSINGPARAMETER_ACCOUNTMISSINGPARAMETERERROR = 'MissingParameter.AccountMissingParameterError'

# Required parameters are missing.
MISSINGPARAMETER_MISSINGPARAMERROR = 'MissingParameter.MissingParamError'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# The instance is performing another task.
OPERATIONDENIED_ACTIONINPROCESS = 'OperationDenied.ActionInProcess'

# Unsupported operation.
OPERATIONDENIED_ACTIONNOTSUPPORT = 'OperationDenied.ActionNotSupport'

# The operation is not allowed during the delayed replication.
OPERATIONDENIED_DELAYREPLICATIONRUNNING = 'OperationDenied.DelayReplicationRunning'

# The root account cannot be deleted.
OPERATIONDENIED_DELETEROOTACCOUNTERROR = 'OperationDenied.DeleteRootAccountError'

# This instance needs permissions to use this feature.
OPERATIONDENIED_FUNCTIONDENIED = 'OperationDenied.FunctionDenied'

# Exceptional instance status
OPERATIONDENIED_INSTANCESTATUSERROR = 'OperationDenied.InstanceStatusError'

# Delayed replication is not allowed because the instance is executing another task.
OPERATIONDENIED_INSTANCETASKRUNNING = 'OperationDenied.InstanceTaskRunning'

# The host information of the local root account cannot be modified.
OPERATIONDENIED_NOTSUPPORTMODIFYLOCALROOTHOSTERROR = 'OperationDenied.NotSupportModifyLocalRootHostError'

# There are other orders being submitted. Please try again later.
OPERATIONDENIED_OTHERODERINPROCESS = 'OperationDenied.OtherOderInProcess'

# This instance is not refundable.
OPERATIONDENIED_UNSUPPORTREFUNDERROR = 'OperationDenied.UnSupportRefundError'

# This account is not authorized to access the requested resource.
OPERATIONDENIED_USERHASNOSTRATEGY = 'OperationDenied.UserHasNoStrategy'

# Incorrect password or verification failed.
OPERATIONDENIED_WRONGPASSWORD = 'OperationDenied.WrongPassword'

# The backend task status is invalid.
OPERATIONDENIED_WRONGSTATUS = 'OperationDenied.WrongStatus'

# Limit exceeded.
OVERQUOTA = 'OverQuota'

# The instance cannot be found. Please check whether your instance status is normal.
RESOURCENOTFOUND_CDBINSTANCENOTFOUNDERROR = 'ResourceNotFound.CdbInstanceNotFoundError'

# The instance does not exist.
RESOURCENOTFOUND_INSTANCENOTFUNDERROR = 'ResourceNotFound.InstanceNotFundError'

# Verification failed. Insufficient permissions.
UNAUTHORIZEDOPERATION_NOTENOUGHPRIVILEGES = 'UnauthorizedOperation.NotEnoughPrivileges'

# Unsupported permission.
UNSUPPORTEDOPERATION_PRIVILEGESUNSUPPORTEDERROR = 'UnsupportedOperation.PrivilegesUnsupportedError'
