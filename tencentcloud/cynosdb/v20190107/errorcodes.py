# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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

# Authentication failure. No permission to operate.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Batch query failed.
FAILEDOPERATION_BATCHGETINSTANCEERROR = 'FailedOperation.BatchGetInstanceError'

# Failed to bind the resource package
FAILEDOPERATION_BINDSOURCEPACKAGEERROR = 'FailedOperation.BindSourcePackageError'

# Failed to obtain permissions. Try again later. If the issue persists, contact customer service.
FAILEDOPERATION_CAMCHECKRESOURCEERROR = 'FailedOperation.CamCheckResourceError'

# Authentication failed. Try again later. If the issue persists, contact customer service.
FAILEDOPERATION_CAMSIGANDAUTHERROR = 'FailedOperation.CamSigAndAuthError'

# VPC/subnet verification failure: {{1}}.
FAILEDOPERATION_CHECKVPCANDSUBNETERROR = 'FailedOperation.CheckVpcAndSubnetError'

# Failed to create audit
FAILEDOPERATION_CREATEAUDITFAILERROR = 'FailedOperation.CreateAuditFailError'

# Failed to create and pay the order.
FAILEDOPERATION_CREATEORDER = 'FailedOperation.CreateOrder'

# Failed to create the resource pack
FAILEDOPERATION_CREATESOURCEPACKAGEERROR = 'FailedOperation.CreateSourcePackageError'

# Failed to set the backup strategy. Try again later. If the issue persists, contact customer service.
FAILEDOPERATION_CYNOSDBMYSQLSETBACKUPSTRATEGY = 'FailedOperation.CynosdbMysqlSetBackupStrategy'

# Database access failed. Try again later. If the issue persists, contact customer service.
FAILEDOPERATION_DATABASEACCESSERROR = 'FailedOperation.DatabaseAccessError'

# Failed to modify account permissions.
FAILEDOPERATION_DESCRIBEACCOUNTPRIVILEGESERROR = 'FailedOperation.DescribeAccountPrivilegesError'

# Failed to create the process. Please retry later. If the issue continues, contact customer service.
FAILEDOPERATION_FLOWCREATEERROR = 'FailedOperation.FlowCreateError'

# The Flow does not exist.
FAILEDOPERATION_FLOWNOTFOUNDERROR = 'FailedOperation.FlowNotFoundError'

# Failed to get the backup policy. Try again later. If the issue persists, contact customer service.
FAILEDOPERATION_GETBACKUPSTRATEGYERROR = 'FailedOperation.GetBackupStrategyError'

# Failed to query the access group network information.
FAILEDOPERATION_GETNETSERVICEINFOERROR = 'FailedOperation.GetNetServiceInfoError'

# Failed to query the details of the primary instance.
FAILEDOPERATION_GETOSSINFOERROR = 'FailedOperation.GetOssInfoError'

# Request to query instance information failed
FAILEDOPERATION_INSTANCEQUERYERROR = 'FailedOperation.InstanceQueryError'

# Insufficient account balance.
FAILEDOPERATION_INSUFFICIENTBALANCE = 'FailedOperation.InsufficientBalance'

# Failed to modify the deduction priority of a resource pack. Check the parameters and try again later.
FAILEDOPERATION_MODIFYDEDUCTIONPRIORITYERROR = 'FailedOperation.ModifyDeductionPriorityError'

# Operation failed. Try again later. If the issue persists, contact customer service.
FAILEDOPERATION_OPERATIONFAILEDERROR = 'FailedOperation.OperationFailedError'

# Proxy verification failure: {{1}}.
FAILEDOPERATION_PROXYCHECKERROR = 'FailedOperation.ProxyCheckError'

# When the proxy group is set to read-only mode, the cluster must contain at least one read-only instance.
FAILEDOPERATION_PROXYGROUPRWSPLITNOROINSTANCEERROR = 'FailedOperation.ProxyGroupRwSplitNoRoInstanceError'

# Failed to query resource package consumption details
FAILEDOPERATION_QUERYSOURCEPACKAGEDETAILERROR = 'FailedOperation.QuerySourcePackageDetailError'

# Failed to query the resource package
FAILEDOPERATION_QUERYSOURCEPACKAGEERROR = 'FailedOperation.QuerySourcePackageError'

# Specification information query failed.
FAILEDOPERATION_QUERYSPECBYSPECCODEERROR = 'FailedOperation.QuerySpecBySpecCodeError'

# Resource package refund failure
FAILEDOPERATION_REFUNDSOURCEPACKAGEERROR = 'FailedOperation.RefundSourcePackageError'

# Policy modification failed.
FAILEDOPERATION_SERVERLESSSETSTRATEGYERROR = 'FailedOperation.ServerlessSetStrategyError'

# Log query failed. Narrow down the query range. If the issue persists, contact customer service.
FAILEDOPERATION_SERVICEACCESSERROR = 'FailedOperation.ServiceAccessError'

# Specification information {{1}} search failure
FAILEDOPERATION_SPECNOTFOUNDERROR = 'FailedOperation.SpecNotFoundError'

# Failed to create and pay for the order. Try again later. If the issue persists, contact customer service.
FAILEDOPERATION_TRADECREATEORDERERROR = 'FailedOperation.TradeCreateOrderError'

# Failed to unbind the resource package
FAILEDOPERATION_UNBINDSOURCEPACKAGEERROR = 'FailedOperation.UnBindSourcePackageError'

# Internal error.
INTERNALERROR = 'InternalError'

# DB access exception.
INTERNALERROR_DBERROR = 'InternalError.DBError'

# Query database failed.
INTERNALERROR_DBOPERATIONFAILED = 'InternalError.DbOperationFailed'

# Customer unauthorized.
INTERNALERROR_GETROLEERROR = 'InternalError.GetRoleError'

# Failed to obtain the security group information.
INTERNALERROR_GETSECURITYGROUPDETAILFAILED = 'InternalError.GetSecurityGroupDetailFailed'

# Failed to obtain the subnet.
INTERNALERROR_GETSUBNETFAILED = 'InternalError.GetSubnetFailed'

# Failed to get the VPC.
INTERNALERROR_GETVPCFAILED = 'InternalError.GetVpcFailed'

# Network error.
INTERNALERROR_HTTPERROR = 'InternalError.HttpError'

# http request execution error.
INTERNALERROR_INTERNALHTTPSERVERERROR = 'InternalError.InternalHttpServerError'

# Internal service error.
INTERNALERROR_INTERNALINNERSERVICEERROR = 'InternalError.InternalInnerServiceError'

# Failed to query the instance in the security group.
INTERNALERROR_LISTINSTANCEFAILED = 'InternalError.ListInstanceFailed'

# Query instance error
INTERNALERROR_LISTINSTANCESERROR = 'InternalError.ListInstancesError'

# Operation on the public network failed.
INTERNALERROR_OPERATEWANFAIL = 'InternalError.OperateWanFail'

# The operation is not supported.
INTERNALERROR_OPERATIONNOTSUPPORT = 'InternalError.OperationNotSupport'

# Query database failed.
INTERNALERROR_QUERYDATABASEFAILED = 'InternalError.QueryDatabaseFailed'

# Internal service error.
INTERNALERROR_SERVICEERROR = 'InternalError.ServiceError'

# Internal system error.
INTERNALERROR_SYSTEMERROR = 'InternalError.SystemError'

# Unknown internal error.
INTERNALERROR_UNKNOWNERROR = 'InternalError.UnknownError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# The API does not exist.
INVALIDPARAMETER_CONTROLLERNOTFOUNDERROR = 'InvalidParameter.ControllerNotFoundError'

# Parameter error.
INVALIDPARAMETER_EXCEPTIONPARAM = 'InvalidParameter.ExceptionParam'

# Unknown parameter. Check whether the parameter is valid.
INVALIDPARAMETER_INVALIDPARAMETERERROR = 'InvalidParameter.InvalidParameterError'

# The current instance is non-isolatable.
INVALIDPARAMETER_ISOLATENOTALLOWED = 'InvalidParameter.IsolateNotAllowed'

# Parameter value error.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The account already exists.
INVALIDPARAMETERVALUE_ACCOUNTALREADYEXISTERROR = 'InvalidParameterValue.AccountAlreadyExistError'

# The account already exists.
INVALIDPARAMETERVALUE_ACCOUNTEXIST = 'InvalidParameterValue.AccountExist'

# The instance does not have an account.
INVALIDPARAMETERVALUE_ACCOUNTNOTEXISTERROR = 'InvalidParameterValue.AccountNotExistError'

# Cluster not found.
INVALIDPARAMETERVALUE_CLUSTERNOTFOUND = 'InvalidParameterValue.ClusterNotFound'

# Unsupported instance type.
INVALIDPARAMETERVALUE_DBTYPENOTFOUND = 'InvalidParameterValue.DBTypeNotFound'

# ClusterType must be serverless.
INVALIDPARAMETERVALUE_DBMODENOTSERVERLESSERROR = 'InvalidParameterValue.DbModeNotServerlessError'

# Order id not found.
INVALIDPARAMETERVALUE_DEALNAMENOTFOUND = 'InvalidParameterValue.DealNameNotFound'

# Task flow ID does not exist.
INVALIDPARAMETERVALUE_FLOWNOTFOUND = 'InvalidParameterValue.FlowNotFound'

# Instance name contains illegal characters.
INVALIDPARAMETERVALUE_ILLEGALINSTANCENAME = 'InvalidParameterValue.IllegalInstanceName'

# Invalid sorting field.
INVALIDPARAMETERVALUE_ILLEGALORDERBY = 'InvalidParameterValue.IllegalOrderBy'

# The password does not meet requirements.
INVALIDPARAMETERVALUE_ILLEGALPASSWORD = 'InvalidParameterValue.IllegalPassword'

# The instance does not exist.
INVALIDPARAMETERVALUE_INSTANCENOTFOUND = 'InvalidParameterValue.InstanceNotFound'

# No operations allowed for built-in accounts.
INVALIDPARAMETERVALUE_INTERNALACCOUNT = 'InvalidParameterValue.InternalAccount'

# Intranet domain name exists. The retention time of the old IP must be more than {{1}} hours.
INVALIDPARAMETERVALUE_INTERNALDOMAINRESERVETOOSHORTERROR = 'InvalidParameterValue.InternalDomainReserveTooShortError'

# Invalid instance version.
INVALIDPARAMETERVALUE_INVALIDDBVERSION = 'InvalidParameterValue.InvalidDBVersion'

# Parameter value is invalid.
INVALIDPARAMETERVALUE_INVALIDPARAMETERVALUEERROR = 'InvalidParameterValue.InvalidParameterValueError'

# The password is non-compliant.
INVALIDPARAMETERVALUE_INVALIDPASSWORDVALUEERROR = 'InvalidParameterValue.InvalidPasswordValueError'

# The region is invalid.
INVALIDPARAMETERVALUE_INVALIDREGIONIDERROR = 'InvalidParameterValue.InvalidRegionIdError'

# Invalid instance specification.
INVALIDPARAMETERVALUE_INVALIDSPEC = 'InvalidParameterValue.InvalidSpec'

# Invalid AZ.
INVALIDPARAMETERVALUE_INVALIDZONEIDERROR = 'InvalidParameterValue.InvalidZoneIdError'

# Both parameters cannot be set simultaneously.
INVALIDPARAMETERVALUE_PARAMBOTHSETERROR = 'InvalidParameterValue.ParamBothSetError'

# Parameter error.
INVALIDPARAMETERVALUE_PARAMERROR = 'InvalidParameterValue.ParamError'

# The input parameter {{1}} is invalid. Check parameters and try again.
INVALIDPARAMETERVALUE_PARAMETERMISMATCHERROR = 'InvalidParameterValue.ParameterMismatchError'

# Invalid parameter value. The value exceeds the maximum allowed.
INVALIDPARAMETERVALUE_PARAMETEROUTRANGEERROR = 'InvalidParameterValue.ParameterOutRangeError'

# Operation not allowed for prepaid payment type.
INVALIDPARAMETERVALUE_PREPAYPAYMODEERROR = 'InvalidParameterValue.PrePayPayModeError'

# ProjectId not found
INVALIDPARAMETERVALUE_PROJECTIDNOTFOUND = 'InvalidParameterValue.ProjectIdNotFound'

# The selected region and availability zone are unavailable.
INVALIDPARAMETERVALUE_REGIONZONEUNAVAILABLE = 'InvalidParameterValue.RegionZoneUnavailable'

# Storage pool not found.
INVALIDPARAMETERVALUE_STORAGEPOOLNOTFOUND = 'InvalidParameterValue.StoragePoolNotFound'

# Subnet not found.
INVALIDPARAMETERVALUE_SUBNETNOTFOUND = 'InvalidParameterValue.SubnetNotFound'

# The subnet of access group {{1}} matches the target subnet. No replacement is needed.
INVALIDPARAMETERVALUE_SUBNETUNCHANGEDERROR = 'InvalidParameterValue.SubnetUnchangedError'

# Data not found.
INVALIDPARAMETERVALUE_VALUENOTFOUND = 'InvalidParameterValue.ValueNotFound'

# The selected VPC network is not found.
INVALIDPARAMETERVALUE_VPCNOTFOUND = 'InvalidParameterValue.VpcNotFound'

# Number of nodes in the cluster exceeds the maximum limit.
LIMITEXCEEDED_CLUSTERINSTANCELIMIT = 'LimitExceeded.ClusterInstanceLimit'

# Number of user instances exceeds the limit.
LIMITEXCEEDED_USERINSTANCELIMIT = 'LimitExceeded.UserInstanceLimit'

# Insufficient permissions for the cloud account. This operation is not supported.
OPERATIONDENIED_ACCOUNTOPERATIONDENIED = 'OperationDenied.AccountOperationDenied'

# The audit log of instance {{1}} is disabled, so operations cannot be performed.
OPERATIONDENIED_AUDITLOGCLOSEDERROR = 'OperationDenied.AuditLogClosedError'

# Audit status exception.
OPERATIONDENIED_AUDITSTATUSERROR = 'OperationDenied.AuditStatusError'

# Backup safe resource {{1}} is in {{2}} and unable to perform {{3}} operation
OPERATIONDENIED_BACKUPVAULTTASKCONFLICTERROR = 'OperationDenied.BackupVaultTaskConflictError'

# Permission verification failed.
OPERATIONDENIED_CAMDENIEDERROR = 'OperationDenied.CamDeniedError'

# Operation forbidden. The current cluster does not allow this operation.
OPERATIONDENIED_CLUSTEROPNOTALLOWEDERROR = 'OperationDenied.ClusterOpNotAllowedError'

# Operation not allowed in the current status of the cluster.
OPERATIONDENIED_CLUSTERSTATUSDENIEDERROR = 'OperationDenied.ClusterStatusDeniedError'

# Cluster {{1}} is currently performing {{2}} and cannot perform {{3}}
OPERATIONDENIED_CLUSTERTASKCONFLICTERROR = 'OperationDenied.ClusterTaskConflictError'

# Task creation failed. {{1}}
OPERATIONDENIED_CREATETASKANDFLOWERROR = 'OperationDenied.CreateTaskAndFlowError'

# Unsupported for instance kernel version {{1}}
OPERATIONDENIED_CYNOSDBVERSIONNOTSUPPORTERROR = 'OperationDenied.CynosdbVersionNotSupportError'

# Multi-AZ deployment for the new storage architecture is not yet available.
OPERATIONDENIED_DISABLENEWSTORAGEMULTIZONEDEPLOYMENTERROR = 'OperationDenied.DisableNewStorageMultiZoneDeploymentError'

# Function {{1}} not currently supported
OPERATIONDENIED_FEATURENOTSUPPORTERROR = 'OperationDenied.FeatureNotSupportError'

# Failed to get proxy
OPERATIONDENIED_GETPROXYGROUPFAILEDERROR = 'OperationDenied.GetProxyGroupFailedError'

# You do not have permission to operate the resource.
OPERATIONDENIED_INSTANCEACCESSDENIEDERROR = 'OperationDenied.InstanceAccessDeniedError'

# Instance group {{1}} is currently performing {{2}} and cannot perform {{3}}.
OPERATIONDENIED_INSTANCEGRPTASKCONFLICTERROR = 'OperationDenied.InstanceGrpTaskConflictError'

# Operation not allowed in the current instance status.
OPERATIONDENIED_INSTANCESTATUSDENIEDERROR = 'OperationDenied.InstanceStatusDeniedError'

# Instance is not in a running state
OPERATIONDENIED_INSTANCESTATUSLIMITERROR = 'OperationDenied.InstanceStatusLimitError'

# Instance {{1}} is currently performing {{2}} and cannot perform {{3}}
OPERATIONDENIED_INSTANCETASKCONFLICTERROR = 'OperationDenied.InstanceTaskConflictError'

# Insufficient account balance.
OPERATIONDENIED_INSUFFICIENTBALANCEERROR = 'OperationDenied.InsufficientBalanceError'

# Invalid region input
OPERATIONDENIED_INVALIDREGIONFORROLLBACKNEWCLUSTER = 'OperationDenied.InvalidRegionForRollbackNewCluster'

# Not the rollback cluster of {{1}}
OPERATIONDENIED_ISNOTROLLBACKCLUSTERERROR = 'OperationDenied.IsNotRollbackClusterError'

# size exceeds limit: {{1}}. Reduce the number of queries.
OPERATIONDENIED_LENGTHOVERLIMIT = 'OperationDenied.LengthOverLimit'

# The clone cluster is not within {{1}} days {{2}}.
OPERATIONDENIED_LIMITDAYFORAUDITREPLAYERROR = 'OperationDenied.LimitDayForAuditReplayError'

# Parameter missing, {{1}}
OPERATIONDENIED_MISSINGPARAMETERERROR = 'OperationDenied.MissingParameterError'

# Storage compression is only supported in storage architecture 2.0 for v8.0.
OPERATIONDENIED_NEWSTORAGEONLYSUPPORT80ERROR = 'OperationDenied.NewStorageOnlySupport80Error'

# No available resources.
OPERATIONDENIED_NOAVALIABLERESOUCEERROR = 'OperationDenied.NoAvaliableResouceError'

# Only storage architecture 2.0 supports the storage compression feature.
OPERATIONDENIED_ONLYNEWSTORAGESUPPORTSTORAGECOMPRESSIONERROR = 'OperationDenied.OnlyNewStorageSupportStorageCompressionError'

# You do not have permission to operate the resource (carry out this operation).
OPERATIONDENIED_OPERATIONDENIEDERROR = 'OperationDenied.OperationDeniedError'

# serverless in paused state is not allowed to be modified for multi-AZ.
OPERATIONDENIED_PAUSEDSLSNOTALLOWMODIFYSLAVE = 'OperationDenied.PausedSlsNotAllowModifySlave'

# The number of creatable connections supported by the proxy node does not match. Supported connections: {{1}}. Current connections: {{2}}.
OPERATIONDENIED_PROXYCONNECTCOUNTCHECKERROR = 'OperationDenied.ProxyConnectCountCheckError'

# Proxy node quantity check failed
OPERATIONDENIED_PROXYNODECOUNTCHECKERROR = 'OperationDenied.ProxyNodeCountCheckError'

# Non-running proxy
OPERATIONDENIED_PROXYNOTRUNNINGERROR = 'OperationDenied.ProxyNotRunningError'

# The availability zone does not exist.
OPERATIONDENIED_PROXYSALEZONECHECKERROR = 'OperationDenied.ProxySaleZoneCheckError'

# Insufficient proxy inventory
OPERATIONDENIED_PROXYSTOCKCHECKERROR = 'OperationDenied.ProxyStockCheckError'

# Proxy version check failed
OPERATIONDENIED_PROXYVERSIONCHECKERROR = 'OperationDenied.ProxyVersionCheckError'

# proxy AZ verification failure
OPERATIONDENIED_PROXYZONECHECKERROR = 'OperationDenied.ProxyZoneCheckError'

# Instance does not exist
OPERATIONDENIED_RESOURCENOTFUNDERROR = 'OperationDenied.ResourceNotFundError'

# Unknown exception. Contact our customer service to handle.
OPERATIONDENIED_SECONDARYCACHEUNKNOWNERROR = 'OperationDenied.SecondaryCacheUnknownError'

# Operation not allowed in the current status of the serverless cluster.
OPERATIONDENIED_SERVERLESSCLUSTERSTATUSDENIED = 'OperationDenied.ServerlessClusterStatusDenied'

# Operation not allowed in the current status of the serverless instance.
OPERATIONDENIED_SERVERLESSINSTANCESTATUSDENIED = 'OperationDenied.ServerlessInstanceStatusDenied'

# Task conflict check failed.
OPERATIONDENIED_TASKCONFLICTERROR = 'OperationDenied.TaskConflictError'

# Business inspection failed: {{1}}
OPERATIONDENIED_TRADEBUSINESSCHECKERROR = 'OperationDenied.TradeBusinessCheckError'

# The sale of this type and specification is not supported.
OPERATIONDENIED_UNSUPPORTSALESPECERROR = 'OperationDenied.UnSupportSaleSpecError'

# Audit enabling is not supported.
OPERATIONDENIED_UNSUPPORTOPENAUDITERROR = 'OperationDenied.UnsupportOpenAuditError'

# User not verified with real-name authentication. Please proceed with real-name authentication before purchase.
OPERATIONDENIED_USERNOTAUTHENTICATEDERROR = 'OperationDenied.UserNotAuthenticatedError'

# User resource {{1}} is currently performing {{2}} and cannot perform {{3}}
OPERATIONDENIED_USERRESOURCETASKCONFLICTERROR = 'OperationDenied.UserResourceTaskConflictError'

# Serverless does not support this version.
OPERATIONDENIED_VERSIONNOTSUPPORTERROR = 'OperationDenied.VersionNotSupportError'

# The cluster does not exist.
RESOURCENOTFOUND_CLUSTERNOTFOUNDERROR = 'ResourceNotFound.ClusterNotFoundError'

# The instance does not exist.
RESOURCENOTFOUND_INSTANCENOTFOUNDERROR = 'ResourceNotFound.InstanceNotFoundError'

# The resource corresponding to the parameter does not exist.
RESOURCENOTFOUND_RESOURCEERROR = 'ResourceNotFound.ResourceError'

# User resource is not found
RESOURCENOTFOUND_RESOURCENOTFOUNDERR = 'ResourceNotFound.ResourceNotFoundErr'

# Failed to lock the instance. It is temporarily inoperable.
RESOURCEUNAVAILABLE_INSTANCELOCKFAIL = 'ResourceUnavailable.InstanceLockFail'

# Instance status is abnormal and temporarily not operable.
RESOURCEUNAVAILABLE_INSTANCESTATUSABNORMAL = 'ResourceUnavailable.InstanceStatusAbnormal'

# Non-verified users are prohibited from purchasing.
UNAUTHORIZEDOPERATION_NOTREALNAMEACCOUNT = 'UnauthorizedOperation.NotRealNameAccount'

# CAM authentication failed.
UNAUTHORIZEDOPERATION_PERMISSIONDENIED = 'UnauthorizedOperation.PermissionDenied'

# Authorization failed or authorization canceled.
UNAUTHORIZEDOPERATION_ROLEUNAUTHORIZED = 'UnauthorizedOperation.RoleUnauthorized'
