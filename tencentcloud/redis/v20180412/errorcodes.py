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

# Invalid authorization.
AUTHFAILURE_INVALIDAUTHORIZATION = 'AuthFailure.InvalidAuthorization'

# Failed to add the security group information of an instance.
FAILEDOPERATION_ADDINSTANCEINFOFAILED = 'FailedOperation.AddInstanceInfoFailed'

# Failed to associate the security group.
FAILEDOPERATION_ASSOCIATESECURITYGROUPSFAILED = 'FailedOperation.AssociateSecurityGroupsFailed'

# Failed to clear the security group information of an instance.
FAILEDOPERATION_CLEARINSTANCEINFOFAILED = 'FailedOperation.ClearInstanceInfoFailed'

# Failed to unassociate the security group.
FAILEDOPERATION_DISASSOCIATESECURITYGROUPSFAILED = 'FailedOperation.DisassociateSecurityGroupsFailed'

# This operation is not allowed under the current DTS state.
FAILEDOPERATION_DTSSTATUSABNORMAL = 'FailedOperation.DtsStatusAbnormal'

# No process exists.
FAILEDOPERATION_FLOWNOTEXISTS = 'FailedOperation.FlowNotExists'

# Failed to query the security group details. Please try again later.
FAILEDOPERATION_GETSECURITYGROUPDETAILFAILED = 'FailedOperation.GetSecurityGroupDetailFailed'

# Payment failed.
FAILEDOPERATION_PAYFAILED = 'FailedOperation.PayFailed'

# No exact description for this error code for the time being.
FAILEDOPERATION_REDOFLOWFAILED = 'FailedOperation.RedoFlowFailed'

# Failed to set a rule.
FAILEDOPERATION_SETRULELOCATIONFAILED = 'FailedOperation.SetRuleLocationFailed'

# Internal system error, which is irrelevant to the business.
FAILEDOPERATION_SYSTEMERROR = 'FailedOperation.SystemError'

# The instance does not support this API.
FAILEDOPERATION_UNSUPPORTERROR = 'FailedOperation.UnSupportError'

# Invalid data is entered for weekday.
FAILEDOPERATION_UNKNOWN = 'FailedOperation.Unknown'

# Failed to update the security group information of an instance.
FAILEDOPERATION_UPDATEINSTANCEINFOFAILED = 'FailedOperation.UpdateInstanceInfoFailed'

# Failed to update the security group.
FAILEDOPERATION_UPDATESECURITYGROUPSFAILED = 'FailedOperation.UpdateSecurityGroupsFailed'

# Internal system error with the database operation, which may be update, insert, select, etc.
INTERNALERROR_DBOPERATIONFAILED = 'InternalError.DbOperationFailed'

# Failed to execute the HTTP request. Please try again later.
INTERNALERROR_EXECHTTPREQUESTERROR = 'InternalError.ExecHttpRequestError'

# Internal error.
INTERNALERROR_INTERNALERROR = 'InternalError.InternalError'

# An error occurred while obtaining the instance list. Please try again later.
INTERNALERROR_LISTINSTANCESERROR = 'InternalError.ListInstancesError'

# Network error
INTERNALERROR_NETWORKERR = 'InternalError.NetWorkErr'

# Incorrect parameter.
INVALIDPARAMETER = 'InvalidParameter'

# The parameter is empty.
INVALIDPARAMETER_EMPTYPARAM = 'InvalidParameter.EmptyParam'

# Invalid parameter.
INVALIDPARAMETER_ILLEGALPARAMETERERROR = 'InvalidParameter.IllegalParameterError'

# Invalid service parameter.
INVALIDPARAMETER_INVALIDPARAMETER = 'InvalidParameter.InvalidParameter'

# Only VPCs are provided in the Shanghai Finance AZ.
INVALIDPARAMETER_ONLYVPCONSPECZONEID = 'InvalidParameter.OnlyVPCOnSpecZoneId'

# Invalid time format or time range
INVALIDPARAMETER_PERIOD = 'InvalidParameter.Period'

# The API has no CAM permissions.
INVALIDPARAMETER_PERMISSIONDENIED = 'InvalidParameter.PermissionDenied'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The backup does not exist.
INVALIDPARAMETERVALUE_BACKUPNOTEXISTS = 'InvalidParameterValue.BackupNotExists'

# The instance is not in a VPC.
INVALIDPARAMETERVALUE_BASENETWORKACCESSDENY = 'InvalidParameterValue.BaseNetWorkAccessDeny'

# Incorrect type of instances requested for purchase (TypeId - 1: cluster edition; 2: primary-secondary edition, i.e., the legacy primary-secondary edition).
INVALIDPARAMETERVALUE_INVALIDINSTANCETYPEID = 'InvalidParameterValue.InvalidInstanceTypeId'

# In a VPC, vpcid or subnet ID is invalid.
INVALIDPARAMETERVALUE_INVALIDSUBNETID = 'InvalidParameterValue.InvalidSubnetId'

# The requested capacity is out of the purchasable capacity range.
INVALIDPARAMETERVALUE_MEMSIZENOTINRANGE = 'InvalidParameterValue.MemSizeNotInRange'

# The password is empty.
INVALIDPARAMETERVALUE_PASSWORDEMPTY = 'InvalidParameterValue.PasswordEmpty'

# Password verification error due to incorrect password.
INVALIDPARAMETERVALUE_PASSWORDERROR = 'InvalidParameterValue.PasswordError'

#  
INVALIDPARAMETERVALUE_PASSWORDFREEDENIED = 'InvalidParameterValue.PasswordFreeDenied'

# When the password is set, the old password passed in by MC does not match the previously set password.
INVALIDPARAMETERVALUE_PASSWORDRULEERROR = 'InvalidParameterValue.PasswordRuleError'

# The request capacity is too small. Capacity reduction is not supported.
INVALIDPARAMETERVALUE_REDUCECAPACITYNOTALLOWED = 'InvalidParameterValue.ReduceCapacityNotAllowed'

# Incorrect request parameter or security group ID.
INVALIDPARAMETERVALUE_SECURITYGROUPIDSNOTEXISTS = 'InvalidParameterValue.SecurityGroupIdsNotExists'

# The instance specification does not exist.
INVALIDPARAMETERVALUE_SPECNOTEXIST = 'InvalidParameterValue.SpecNotExist'

# The instance type is not supported.
INVALIDPARAMETERVALUE_UNSUPPORTEDTYPE = 'InvalidParameterValue.UnSupportedType'

# Invalid VPC subnet ID of `uniqVpcId`.
INVALIDPARAMETERVALUE_UNVPCIDNOTEXISTS = 'InvalidParameterValue.UnVpcIdNotExists'

# Invalid data is entered for weekday.
INVALIDPARAMETERVALUE_WEEKDAYSISINVALID = 'InvalidParameterValue.WeekDaysIsInvalid'

# The requested capacity is out of the purchasable specification range (`memSize` should be an integer multiple of 1,024 in MB).
LIMITEXCEEDED_INVALIDMEMSIZE = 'LimitExceeded.InvalidMemSize'

# The number of instances requested for purchase at a time is out of the purchasable quantity range.
LIMITEXCEEDED_INVALIDPARAMETERGOODSNUMNOTINRANGE = 'LimitExceeded.InvalidParameterGoodsNumNotInRange'

# The requested capacity is out of the purchasable capacity range.
LIMITEXCEEDED_MEMSIZENOTINRANGE = 'LimitExceeded.MemSizeNotInRange'

# The requested length of purchase is more than 3 years and exceeds the maximum value.
LIMITEXCEEDED_PERIODEXCEEDMAXLIMIT = 'LimitExceeded.PeriodExceedMaxLimit'

# The length of purchase is invalid. It must be at least one month.
LIMITEXCEEDED_PERIODLESSTHANMINLIMIT = 'LimitExceeded.PeriodLessThanMinLimit'

# The instance is locked by another process.
RESOURCEINUSE_INSTANCEBEENLOCKED = 'ResourceInUse.InstanceBeenLocked'

# The uin value is blank.
RESOURCENOTFOUND_ACCOUNTDOESNOTEXISTS = 'ResourceNotFound.AccountDoesNotExists'

# No Redis instance is found by the serialId.
RESOURCENOTFOUND_INSTANCENOTEXISTS = 'ResourceNotFound.InstanceNotExists'

# Instance not found.
RESOURCENOTFOUND_INSTANCENOTFOUND = 'ResourceNotFound.InstanceNotFound'

# The request order number does not exist.
RESOURCEUNAVAILABLE_ACCOUNTBALANCENOTENOUGH = 'ResourceUnavailable.AccountBalanceNotEnough'

# The backup has been locked by another task, and the operation cannot be performed temporarily.
RESOURCEUNAVAILABLE_BACKUPLOCKEDERROR = 'ResourceUnavailable.BackupLockedError'

# Backup status exception. The operation cannot be performed temporarily. The backup may have expired or been deleted.
RESOURCEUNAVAILABLE_BACKUPSTATUSABNORMAL = 'ResourceUnavailable.BackupStatusAbnormal'

# Failed to call the backend API.
RESOURCEUNAVAILABLE_CALLOSSERROR = 'ResourceUnavailable.CallOssError'

# Failed to get the security group information.
RESOURCEUNAVAILABLE_GETSECURITYERROR = 'ResourceUnavailable.GetSecurityError'

# Instance configuration error.
RESOURCEUNAVAILABLE_INSTANCECONFERROR = 'ResourceUnavailable.InstanceConfError'

# The instance has already been repossessed.
RESOURCEUNAVAILABLE_INSTANCEDELETED = 'ResourceUnavailable.InstanceDeleted'

# The instance has expired.
RESOURCEUNAVAILABLE_INSTANCEISOLATED = 'ResourceUnavailable.InstanceIsolated'

# Redis has been locked by another process.
RESOURCEUNAVAILABLE_INSTANCELOCKEDERROR = 'ResourceUnavailable.InstanceLockedError'

# The order does not exist.
RESOURCEUNAVAILABLE_INSTANCENODEAL = 'ResourceUnavailable.InstanceNoDeal'

# Instances in this status do not support the operation.
RESOURCEUNAVAILABLE_INSTANCENOTSUPPORTOPERATION = 'ResourceUnavailable.InstanceNotSupportOperation'

# Instance status error.
RESOURCEUNAVAILABLE_INSTANCESTATEERROR = 'ResourceUnavailable.InstanceStateError'

# The Redis status is exceptional, and the corresponding process cannot be executed.
RESOURCEUNAVAILABLE_INSTANCESTATUSABNORMAL = 'ResourceUnavailable.InstanceStatusAbnormal'

# Operation unsupported: the instance is exceptional.
RESOURCEUNAVAILABLE_INSTANCESTATUSERROR = 'ResourceUnavailable.InstanceStatusError'

# Insufficient IP resources in the VPC.
RESOURCEUNAVAILABLE_NOENOUGHVIPINVPC = 'ResourceUnavailable.NoEnoughVipInVPC'

# The requested region currently does not provide the Redis service.
RESOURCEUNAVAILABLE_NOREDISSERVICE = 'ResourceUnavailable.NoRedisService'

# The requested region currently does not provide the requested type of Redis service.
RESOURCEUNAVAILABLE_NOTYPEIDREDISSERVICE = 'ResourceUnavailable.NoTypeIdRedisService'

# The product has not been connected to any security group.
RESOURCEUNAVAILABLE_SECURITYGROUPNOTSUPPORTED = 'ResourceUnavailable.SecurityGroupNotSupported'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# No CAM permissions.
UNAUTHORIZEDOPERATION_NOCAMAUTHED = 'UnauthorizedOperation.NoCAMAuthed'

# The user is not in the allowlist.
UNAUTHORIZEDOPERATION_USERNOTINWHITELIST = 'UnauthorizedOperation.UserNotInWhiteList'

# The Redis cluster edition is not allowed to connect to a security group.
UNSUPPORTEDOPERATION_CLUSTERINSTANCEACCESSEDDENY = 'UnsupportedOperation.ClusterInstanceAccessedDeny'

# Auto-renewal flag error.
UNSUPPORTEDOPERATION_ISAUTORENEWERROR = 'UnsupportedOperation.IsAutoRenewError'

# Only cluster edition instances support backup exporting.
UNSUPPORTEDOPERATION_ONLYCLUSTERINSTANCECANEXPORTBACKUP = 'UnsupportedOperation.OnlyClusterInstanceCanExportBackup'
