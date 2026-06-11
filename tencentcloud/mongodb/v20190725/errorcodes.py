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


# CAM signature/authentication error
AUTHFAILURE = 'AuthFailure'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Termination protection is enabled for the instance. destruction is not allowed.
FAILEDOPERATION_DELETIONPROTECTIONENABLED = 'FailedOperation.DeletionProtectionEnabled'

# Kernel response timed out.
FAILEDOPERATION_KERNELRESPONSETIMEOUT = 'FailedOperation.KernelResponseTimeout'

# Public network access has been enabled for the current instance.
FAILEDOPERATION_NOTALLOWMODIFYADDRAFTEROPENWANSERVICE = 'FailedOperation.NotAllowModifyAddrAfterOpenWanService'

# Operations are not allowed to be performed while the instance is locked.
FAILEDOPERATION_OPERATIONNOTALLOWEDININSTANCELOCKING = 'FailedOperation.OperationNotAllowedInInstanceLocking'

# Physical backup is not supported when transparent data encryption is enabled for the instance.
FAILEDOPERATION_TRANSPARENTDATAENCRYPTIONALREADYOPEN = 'FailedOperation.TransparentDataEncryptionAlreadyOpen'

# Internal error.
INTERNALERROR = 'InternalError'

# Error creating an audit log file.
INTERNALERROR_AUDITCREATELOGFILEERROR = 'InternalError.AuditCreateLogFileError'

# Error deleting the audit log.
INTERNALERROR_AUDITDELETELOGFILEERROR = 'InternalError.AuditDeleteLogFileError'

# Error querying the audit log.
INTERNALERROR_AUDITDESCRIBELOGERROR = 'InternalError.AuditDescribeLogError'

# Internal audit service error.
INTERNALERROR_AUDITERROR = 'InternalError.AuditError'

# Failed to modify audit status.
INTERNALERROR_AUDITMODIFYSTATUSERROR = 'InternalError.AuditModifyStatusError'

# `appId` verification failed.
INTERNALERROR_CHECKAPPIDFAILED = 'InternalError.CheckAppIdFailed'

# Get file information failed.
INTERNALERROR_COSERROR = 'InternalError.CosError'

# Database exception.
INTERNALERROR_DBERROR = 'InternalError.DBError'

# An internal data storage exception occurs.
INTERNALERROR_DBOPERATEERROR = 'InternalError.DBOperateError'

# Database operation failed.
INTERNALERROR_DBOPERATIONERROR = 'InternalError.DBOperationError'

# Database internal error.
INTERNALERROR_DATABASEACCESSERROR = 'InternalError.DatabaseAccessError'

# Failed to query the instance.
INTERNALERROR_FINDINSTANCEFAILED = 'InternalError.FindInstanceFailed'

# Internal service error.
INTERNALERROR_INNERCOMMONERROR = 'InternalError.InnerCommonError'

# json parsing failure.
INTERNALERROR_JSONERROR = 'InternalError.JSONError'

# Json deserialization error.
INTERNALERROR_JSONUNMARSHALERROR = 'InternalError.JsonUnmarshalError'

# The password is different from the previously recorded one.
INTERNALERROR_PASSWORDERROR = 'InternalError.PasswordError'

# Transaction system error.
INTERNALERROR_TRADEERROR = 'InternalError.TradeError'

# Unknown error.
INTERNALERROR_UNKNOWNERROR = 'InternalError.UnknownError'

# Parameter error
INVALIDPARAMETER = 'InvalidParameter'

# API does not exist. Please confirm whether the API name in the request is correct.
INVALIDPARAMETER_ACTIONNOTFOUND = 'InvalidParameter.ActionNotFound'

# The instance does not support parameter setting.
INVALIDPARAMETER_CURRENTINSTANCENOTSUPPORTMODIFYPARAMS = 'InvalidParameter.CurrentInstanceNotSupportModifyParams'

# Invalid parameter value.
INVALIDPARAMETER_INVALIDPARAMETER = 'InvalidParameter.InvalidParameter'

# Parameter is invalid.
INVALIDPARAMETER_INVALIDPARAMETERERROR = 'InvalidParameter.InvalidParameterError'

# Invalid Vip information
INVALIDPARAMETER_INVALIDVIP = 'InvalidParameter.InvalidVip'

# The parameter name is incorrect.
INVALIDPARAMETER_MODIFYMONGODBPARAMS = 'InvalidParameter.ModifyMongodbParams'

# The current sub-account has no permission to perform this operation.
INVALIDPARAMETER_PERMISSIONDENIED = 'InvalidParameter.PermissionDenied'

# Instances are not purchasable in this AZ.
INVALIDPARAMETER_ZONECLOSED = 'InvalidParameter.ZoneClosed'

# Invalid parameter value
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The backup file was not found.
INVALIDPARAMETERVALUE_BACKUPFILENOTFOUND = 'InvalidParameterValue.BackupFileNotFound'

# `appId` verification failed.
INVALIDPARAMETERVALUE_CHECKAPPIDFAILED = 'InvalidParameterValue.CheckAppIdFailed'

# Invalid instance type.
INVALIDPARAMETERVALUE_CLUSTERTYPEERROR = 'InvalidParameterValue.ClusterTypeError'

# Data conversion failed
INVALIDPARAMETERVALUE_DATACONVERTERROR = 'InvalidParameterValue.DataConvertError'

# Invalid instance name
INVALIDPARAMETERVALUE_ILLEGALINSTANCENAME = 'InvalidParameterValue.IllegalInstanceName'

# Invalid instance status
INVALIDPARAMETERVALUE_ILLEGALINSTANCESTATUS = 'InvalidParameterValue.IllegalInstanceStatus'

# The instance cannot be deactivated in the current status. Only isolated instances can be deactivated.
INVALIDPARAMETERVALUE_ILLEGALSTATUSTOOFFLINE = 'InvalidParameterValue.IllegalStatusToOffline'

# The instance has been deleted.
INVALIDPARAMETERVALUE_INSTANCEHASBEENDELETED = 'InvalidParameterValue.InstanceHasBeenDeleted'

# The instance has been isolated.
INVALIDPARAMETERVALUE_INSTANCEHASBEENISOLATED = 'InvalidParameterValue.InstanceHasBeenIsolated'

# Billing error. Corresponding purchase/renewal/configuration change operations are not allowed for the current instance.
INVALIDPARAMETERVALUE_INVALIDTRADEOPERATION = 'InvalidParameterValue.InvalidTradeOperation'

# limit value ranges from 1 to 100.
INVALIDPARAMETERVALUE_LIMITPARAOUTOFRANGE = 'InvalidParameterValue.LimitParaOutOfRange'

# Instance lock failed.
INVALIDPARAMETERVALUE_LOCKFAILED = 'InvalidParameterValue.LockFailed'

# Incorrect model.
INVALIDPARAMETERVALUE_MACHINETYPEERROR = 'InvalidParameterValue.MachineTypeError'

# Memory and disk must be upgraded or degraded simultaneously.
INVALIDPARAMETERVALUE_MODIFYMODEERROR = 'InvalidParameterValue.ModifyModeError'

# The parameter value is incorrect.
INVALIDPARAMETERVALUE_MODIFYMONGODBPARAMS = 'InvalidParameterValue.ModifyMongodbParams'

# The instance version is incorrect.
INVALIDPARAMETERVALUE_MONGOVERSIONERROR = 'InvalidParameterValue.MongoVersionError'

# The instance version does not support querying the instance client information.
INVALIDPARAMETERVALUE_MONGOVERSIONNOTSUPPORTQUERYCLIENT = 'InvalidParameterValue.MongoVersionNotSupportQueryClient'

# The node is not found in the current replica set/shard.
INVALIDPARAMETERVALUE_NODENOTFOUNDINREPLICA = 'InvalidParameterValue.NodeNotFoundInReplica'

# The instance was not found.
INVALIDPARAMETERVALUE_NOTFOUNDINSTANCE = 'InvalidParameterValue.NotFoundInstance'

# offset value ranges from 0 to 10000.
INVALIDPARAMETERVALUE_OFFSETPARAOUTOFRANGE = 'InvalidParameterValue.OffsetParaOutOfRange'

# The `OplogSize` parameter is set incorrectly and should be between 10% and 90% of the disk capacity.
INVALIDPARAMETERVALUE_OPLOGSIZEOUTOFRANGE = 'InvalidParameterValue.OplogSizeOutOfRange'

# The password is non-compliant.
INVALIDPARAMETERVALUE_PASSWORDRULEFAILED = 'InvalidParameterValue.PasswordRuleFailed'

# The number of postpaid instances in a single region exceeds the limit.
INVALIDPARAMETERVALUE_POSTPAIDINSTANCEBEYONDLIMIT = 'InvalidParameterValue.PostPaidInstanceBeyondLimit'

# Prepaid instances cannot be terminated.
INVALIDPARAMETERVALUE_PREPAIDINSTANCEUNABLETOISOLATE = 'InvalidParameterValue.PrePaidInstanceUnableToIsolate'

# The project does not exist.
INVALIDPARAMETERVALUE_PROJECTNOTFOUND = 'InvalidParameterValue.ProjectNotFound'

# The proxy version does not support querying the instance client information. Please submit a ticket for upgrade.
INVALIDPARAMETERVALUE_PROXYNOTSUPPORTQUERYCLIENT = 'InvalidParameterValue.ProxyNotSupportQueryClient'

# The query offset is out of range.
INVALIDPARAMETERVALUE_QUERYOUTOFRANGE = 'InvalidParameterValue.QueryOutOfRange'

# Only slow logs generated in the past seven days can be queried.
INVALIDPARAMETERVALUE_QUERYTIMEOUTOFRANGE = 'InvalidParameterValue.QueryTimeOutOfRange'

# Only slow logs generated in the past seven days can be queried.
INVALIDPARAMETERVALUE_QUERYTIMERANGEBEYONDLIMIT = 'InvalidParameterValue.QueryTimeRangeBeyondLimit'

# Invalid region
INVALIDPARAMETERVALUE_REGIONERROR = 'InvalidParameterValue.RegionError'

# The current region does not support this operation.
INVALIDPARAMETERVALUE_REGIONNOTSUPPORTOPERATION = 'InvalidParameterValue.RegionNotSupportOperation'

# The region does not support querying the instance client information.
INVALIDPARAMETERVALUE_REGIONNOTSUPPORTQUERYCLIENT = 'InvalidParameterValue.RegionNotSupportQueryClient'

# The replica set/shard is not found.
INVALIDPARAMETERVALUE_REPLICANOTFOUND = 'InvalidParameterValue.ReplicaNotFound'

# Incorrect number of replica sets (shards).
INVALIDPARAMETERVALUE_REPLICASETNUMERROR = 'InvalidParameterValue.ReplicaSetNumError'

# Incorrect number of secondary nodes.
INVALIDPARAMETERVALUE_SECONDARYNUMERROR = 'InvalidParameterValue.SecondaryNumError'

# Invalid security group ID
INVALIDPARAMETERVALUE_SECURITYGROUPID = 'InvalidParameterValue.SecurityGroupId'

# The current instance has enabled Password-free Access or is not bound to a security group, with a low security level that does not allow public network access service.
INVALIDPARAMETERVALUE_SECURITYLEVELNOTALLOWOPENWANSERVICE = 'InvalidParameterValue.SecurityLevelNotAllowOpenWanService'

# The disk size to be set cannot be less than 1.2 times the used disk capacity.
INVALIDPARAMETERVALUE_SETDISKLESSTHANUSED = 'InvalidParameterValue.SetDiskLessThanUsed'

# The value range of the slowMS parameter is [100,65536].
INVALIDPARAMETERVALUE_SLOWMSBELOWLIMIT = 'InvalidParameterValue.SlowMSBelowLimit'

# Incorrect purchasable specification.
INVALIDPARAMETERVALUE_SPECNOTONSALE = 'InvalidParameterValue.SpecNotOnSale'

# The start time should be earlier than the end time.
INVALIDPARAMETERVALUE_STARTTIMENOTBEFORETHANENDTIME = 'InvalidParameterValue.StartTimeNotBeforeThanEndTime'

# The instance is in a status where operations are not allowed.
INVALIDPARAMETERVALUE_STATUSABNORMAL = 'InvalidParameterValue.StatusAbnormal'

# The specified tag was not found.
INVALIDPARAMETERVALUE_TAGNOTFOUND = 'InvalidParameterValue.TagNotFound'

# Illegal time format.
INVALIDPARAMETERVALUE_TIMEFORMATERR = 'InvalidParameterValue.TimeFormatErr'

# The user account does not exist.
INVALIDPARAMETERVALUE_USERNOTFOUND = 'InvalidParameterValue.UserNotFound'

# The VPC (subnet) was not found.
INVALIDPARAMETERVALUE_VPCIDORSUBNETIDNOTFOUND = 'InvalidParameterValue.VpcIdOrSubnetIdNotFound'

# Instances are not purchasable in this AZ.
INVALIDPARAMETERVALUE_ZONECLOSED = 'InvalidParameterValue.ZoneClosed'

# Invalid availability zone
INVALIDPARAMETERVALUE_ZONEERROR = 'InvalidParameterValue.ZoneError'

# The API frequency limit is triggered due to frequent requests.
LIMITEXCEEDED_TOOMANYREQUESTS = 'LimitExceeded.TooManyRequests'

# Audit policy conflict.
OPERATIONDENIED_AUDITPOLICYCONFLICTERROR = 'OperationDenied.AuditPolicyConflictError'

# Audit policy already exists.
OPERATIONDENIED_AUDITPOLICYEXISTERROR = 'OperationDenied.AuditPolicyExistError'

# Audit policy not found.
OPERATIONDENIED_AUDITPOLICYNOTEXISTERROR = 'OperationDenied.AuditPolicyNotExistError'

# Number of audit policies exceeds the limit.
OPERATIONDENIED_AUDITPOLICYOVERQUOTAERROR = 'OperationDenied.AuditPolicyOverQuotaError'

# The audit status is abnormal.
OPERATIONDENIED_AUDITSTATUSERROR = 'OperationDenied.AuditStatusError'

# Audit task conflict.
OPERATIONDENIED_AUDITTASKCONFLICTERROR = 'OperationDenied.AuditTaskConflictError'

# Resource is not found.
OPERATIONDENIED_RESOURCENOTFUNDERROR = 'OperationDenied.ResourceNotFundError'

# Audit activation is not supported.
OPERATIONDENIED_UNSUPPORTOPENAUDITERROR = 'OperationDenied.UnsupportOpenAuditError'

# Insufficient resources.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# Unsupported operation
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# Not supported for kernel versions.
UNSUPPORTEDOPERATION_KERNELVERSIONNOTSUPPORT = 'UnsupportedOperation.KernelVersionNotSupport'

# Not supported for minor versions.
UNSUPPORTEDOPERATION_SECONDARYVERSIONNOTSUPPORTAUDIT = 'UnsupportedOperation.SecondaryVersionNotSupportAudit'

# The current version does not support the operation.
UNSUPPORTEDOPERATION_VERSIONNOTSUPPORT = 'UnsupportedOperation.VersionNotSupport'
