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

# The sub-account has no permissions.
AUTHFAILURE_SUBACCOUNTDENIED = 'AuthFailure.SubAccountDenied'

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

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Async task exception.
FAILEDOPERATION_ASYNCTASKSTATUSERROR = 'FailedOperation.AsyncTaskStatusError'

# Failed to lock the instance while performing exclusive operations. Please try again later.
FAILEDOPERATION_CDBINSTANCELOCKFAILERROR = 'FailedOperation.CdbInstanceLockFailError'

# Creation failed. Please check whether the user already exists.
FAILEDOPERATION_CREATEACCOUNTERROR = 'FailedOperation.CreateAccountError'

# Failed to create the audit rule.
FAILEDOPERATION_CREATEAUDITFAILERROR = 'FailedOperation.CreateAuditFailError'

# Failed to assign an exclusive VIP to the read-only replica.
FAILEDOPERATION_CREATEROVIPERROR = 'FailedOperation.CreateRoVipError'

# Database operation failed.
FAILEDOPERATION_DBOPERATIONACTIONERROR = 'FailedOperation.DBOperationActionError'

# Failed to query database proxy.
FAILEDOPERATION_DESCRIBEPROXYGROUPERROR = 'FailedOperation.DescribeProxyGroupError'

# An error occurred while obtaining permissions.
FAILEDOPERATION_GETPRIVILEGEERROR = 'FailedOperation.GetPrivilegeError'

# Query failed.
FAILEDOPERATION_INSTANCEQUERYERROR = 'FailedOperation.InstanceQueryError'

# Failed to deserialize JSON.
FAILEDOPERATION_JSONUNMARSHALERROR = 'FailedOperation.JsonUnmarshalError'

# It is not a read-only instance with delayed replication enabled.
FAILEDOPERATION_NOTDELAYRO = 'FailedOperation.NotDelayRo'

# The executed operation to modify permissions is invalid. You can refer to product documentation for more information about permissions that can be modified for this instance. If you have any questions, please contact customer service.
FAILEDOPERATION_PRIVILEGEDATAILLEGAL = 'FailedOperation.PrivilegeDataIllegal'

# Database proxy in an exceptional status.
FAILEDOPERATION_PROXYGROUPSTATUSERROR = 'FailedOperation.ProxyGroupStatusError'

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

# The query timed out.
FAILEDOPERATION_TIMEOUTERROR = 'FailedOperation.TimeoutError'

# This type of operations cannot be performed.
FAILEDOPERATION_TYPEINCONFLICT = 'FailedOperation.TypeInConflict'

# An internal error occurred.
INTERNALERROR = 'InternalError'

# An error occurred while querying async tasks.
INTERNALERROR_ASYNCREQUESTERROR = 'InternalError.AsyncRequestError'

# An error occurred in the internal service of the audit service.
INTERNALERROR_AUDITERROR = 'InternalError.AuditError'

# Internal exception of the audit service.
INTERNALERROR_AUDITOSSLOGICERROR = 'InternalError.AuditOssLogicError'

# Authentication failed.
INTERNALERROR_AUTHERROR = 'InternalError.AuthError'

# Authentication failed.
INTERNALERROR_CAUTHERROR = 'InternalError.CauthError'

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

# Failed to execute the HTTP request
INTERNALERROR_EXECHTTPREQUESTERROR = 'InternalError.ExecHttpRequestError'

# Failed to execute SQL statement
INTERNALERROR_EXECUTESQLERROR = 'InternalError.ExecuteSQLError'

# File transfer exception
INTERNALERROR_FTPERROR = 'InternalError.FtpError'

# Exceptional HTTP request
INTERNALERROR_HTTPERROR = 'InternalError.HttpError'

# Import failed
INTERNALERROR_IMPORTERROR = 'InternalError.ImportError'

# Internal service error
INTERNALERROR_INNERCOMMONERROR = 'InternalError.InnerCommonError'

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

# Internal error of the system.
INTERNALERROR_SERVERERROR = 'InternalError.ServerError'

# An exception occurred in the internal service.
INTERNALERROR_SERVICEERROR = 'InternalError.ServiceError'

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

# Operation failed
INTERNALERROR_TRANSACTIONBEGINERROR = 'InternalError.TransactionBeginError'

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

# Parameter exception.
INVALIDPARAMETER_EXCEPTIONPARAM = 'InvalidParameter.ExceptionParam'

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

# Failed to deserialize JSON.
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

# Invalid parameter value
INVALIDPARAMETERVALUE_INVALIDPARAMETERVALUEERROR = 'InvalidParameterValue.InvalidParameterValueError'

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

# The quota limit has been reached.
LIMITEXCEEDED = 'LimitExceeded'

# Missing parameter
MISSINGPARAMETER = 'MissingParameter'

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

# The audit policies conflict.
OPERATIONDENIED_AUDITPOLICYCONFLICTERROR = 'OperationDenied.AuditPolicyConflictError'

# The audit policy already exists.
OPERATIONDENIED_AUDITPOLICYEXISTERROR = 'OperationDenied.AuditPolicyExistError'

# The number of audit policies exceeds the limit.
OPERATIONDENIED_AUDITPOLICYOVERQUOTAERROR = 'OperationDenied.AuditPolicyOverQuotaError'

# The audit rule has been associated.
OPERATIONDENIED_AUDITRULEHASBIND = 'OperationDenied.AuditRuleHasBind'

# The audit rule does not exist.
OPERATIONDENIED_AUDITRULENOTEXISTERROR = 'OperationDenied.AuditRuleNotExistError'

# Exceptional audit status.
OPERATIONDENIED_AUDITSTATUSERROR = 'OperationDenied.AuditStatusError'

# The audit tasks conflict.
OPERATIONDENIED_AUDITTASKCONFLICTERROR = 'OperationDenied.AuditTaskConflictError'

# The operation is not allowed as the RO group contains an invalid read-only instance.
OPERATIONDENIED_CONFLICTROSTATUS = 'OperationDenied.ConflictRoStatus'

# The configuration of read-only group is being modified. Please do not make repeated requests.
OPERATIONDENIED_CONFLICTSTATUS = 'OperationDenied.ConflictStatus'

# You have enabled the compliance audit feature of DBbrain, so you cannot enable the rule-based audit.
OPERATIONDENIED_DBBRAINPOLICYCONFLICT = 'OperationDenied.DBBrainPolicyConflict'

# The operation is not allowed during the delayed replication.
OPERATIONDENIED_DELAYREPLICATIONRUNNING = 'OperationDenied.DelayReplicationRunning'

# The root account cannot be deleted.
OPERATIONDENIED_DELETEROOTACCOUNTERROR = 'OperationDenied.DeleteRootAccountError'

# This instance needs permissions to use this feature.
OPERATIONDENIED_FUNCTIONDENIED = 'OperationDenied.FunctionDenied'

# The current instance type does not support this operation.
OPERATIONDENIED_INSTTYPENOTSUPPORT = 'OperationDenied.InstTypeNotSupport'

# Instance locks are in conflict. Please try again later.
OPERATIONDENIED_INSTANCELOCKERCONFLICT = 'OperationDenied.InstanceLockerConflict'

# Exceptional instance status
OPERATIONDENIED_INSTANCESTATUSERROR = 'OperationDenied.InstanceStatusError'

# Delayed replication is not allowed because the instance is executing another task.
OPERATIONDENIED_INSTANCETASKRUNNING = 'OperationDenied.InstanceTaskRunning'

# Abnormal instance task status.
OPERATIONDENIED_INSTANCETASKSTATUSERROR = 'OperationDenied.InstanceTaskStatusError'

# The instance does not support this operation.
OPERATIONDENIED_INSTANCEUNSUPPORTEDOPERATEERROR = 'OperationDenied.InstanceUnsupportedOperateError'

# Basic instances do not support this operation (feature).
OPERATIONDENIED_NOTSUPPORTBASIC = 'OperationDenied.NotSupportBasic'

# The host information of the local root account cannot be modified.
OPERATIONDENIED_NOTSUPPORTMODIFYLOCALROOTHOSTERROR = 'OperationDenied.NotSupportModifyLocalRootHostError'

# There are other orders being submitted. Please try again later.
OPERATIONDENIED_OTHERODERINPROCESS = 'OperationDenied.OtherOderInProcess'

# This operation is not allowed during database proxy upgrade task.
OPERATIONDENIED_PROXYUPGRADETASKSTATUSERROR = 'OperationDenied.ProxyUpgradeTaskStatusError'

# The maximum number of results has been reached. Please narrow down your query.
OPERATIONDENIED_RESULTOVERLIMIT = 'OperationDenied.ResultOverLimit'

# The Tencent Cloud sub-account is not allowed to perform the operation due to insufficient permissions.
OPERATIONDENIED_SUBACCOUNTOPERATIONDENIED = 'OperationDenied.SubAccountOperationDenied'

# This instance is not refundable.
OPERATIONDENIED_UNSUPPORTREFUNDERROR = 'OperationDenied.UnSupportRefundError'

# The audit feature cannot be enabled.
OPERATIONDENIED_UNSUPPORTOPENAUDITERROR = 'OperationDenied.UnsupportOpenAuditError'

# This account is not authorized to access the requested resource.
OPERATIONDENIED_USERHASNOSTRATEGY = 'OperationDenied.UserHasNoStrategy'

# Incorrect password or verification failed.
OPERATIONDENIED_WRONGPASSWORD = 'OperationDenied.WrongPassword'

# The backend task status is invalid.
OPERATIONDENIED_WRONGSTATUS = 'OperationDenied.WrongStatus'

# Limit exceeded.
OVERQUOTA = 'OverQuota'

# The resource is occupied.
RESOURCEINUSE = 'ResourceInUse'

# Insufficient resource.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The instance cannot be found. Please check whether your instance status is normal.
RESOURCENOTFOUND_CDBINSTANCENOTFOUNDERROR = 'ResourceNotFound.CdbInstanceNotFoundError'

# The instance does not exist.
RESOURCENOTFOUND_INSTANCENOTFUNDERROR = 'ResourceNotFound.InstanceNotFundError'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# Verification failed. Insufficient permissions.
UNAUTHORIZEDOPERATION_NOTENOUGHPRIVILEGES = 'UnauthorizedOperation.NotEnoughPrivileges'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# Unsupported permission.
UNSUPPORTEDOPERATION_PRIVILEGESUNSUPPORTEDERROR = 'UnsupportedOperation.PrivilegesUnsupportedError'
