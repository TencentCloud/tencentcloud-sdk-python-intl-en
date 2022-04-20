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


# CAM signature/authentication error
AUTHFAILURE = 'AuthFailure'

# Internal error
INTERNALERROR = 'InternalError'

# `appId` verification failed.
INTERNALERROR_CHECKAPPIDFAILED = 'InternalError.CheckAppIdFailed'

# Failed to query the instance.
INTERNALERROR_FINDINSTANCEFAILED = 'InternalError.FindInstanceFailed'

# Parameter error
INVALIDPARAMETER = 'InvalidParameter'

# The instance does not support parameter setting.
INVALIDPARAMETER_CURRENTINSTANCENOTSUPPORTMODIFYPARAMS = 'InvalidParameter.CurrentInstanceNotSupportModifyParams'

# Invalid Vip information
INVALIDPARAMETER_INVALIDVIP = 'InvalidParameter.InvalidVip'

# The current subaccount has no permission to perform this operation.
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

# Instance lock failed.
INVALIDPARAMETERVALUE_LOCKFAILED = 'InvalidParameterValue.LockFailed'

# Incorrect model.
INVALIDPARAMETERVALUE_MACHINETYPEERROR = 'InvalidParameterValue.MachineTypeError'

# Memory and disk must be upgraded or degraded simultaneously.
INVALIDPARAMETERVALUE_MODIFYMODEERROR = 'InvalidParameterValue.ModifyModeError'

# The instance version is incorrect.
INVALIDPARAMETERVALUE_MONGOVERSIONERROR = 'InvalidParameterValue.MongoVersionError'

# The instance version does not support querying the instance client information.
INVALIDPARAMETERVALUE_MONGOVERSIONNOTSUPPORTQUERYCLIENT = 'InvalidParameterValue.MongoVersionNotSupportQueryClient'

# The instance was not found.
INVALIDPARAMETERVALUE_NOTFOUNDINSTANCE = 'InvalidParameterValue.NotFoundInstance'

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

# Only slow logs generated in the past seven days can be queried.
INVALIDPARAMETERVALUE_QUERYTIMEOUTOFRANGE = 'InvalidParameterValue.QueryTimeOutOfRange'

# Only slow logs generated in the past seven days can be queried.
INVALIDPARAMETERVALUE_QUERYTIMERANGEBEYONDLIMIT = 'InvalidParameterValue.QueryTimeRangeBeyondLimit'

# Invalid region
INVALIDPARAMETERVALUE_REGIONERROR = 'InvalidParameterValue.RegionError'

# The region does not support querying the instance client information.
INVALIDPARAMETERVALUE_REGIONNOTSUPPORTQUERYCLIENT = 'InvalidParameterValue.RegionNotSupportQueryClient'

# Incorrect number of replica sets (shards).
INVALIDPARAMETERVALUE_REPLICASETNUMERROR = 'InvalidParameterValue.ReplicaSetNumError'

# Incorrect number of secondary nodes.
INVALIDPARAMETERVALUE_SECONDARYNUMERROR = 'InvalidParameterValue.SecondaryNumError'

# The disk size to be set cannot be less than 1.2 times the used disk capacity.
INVALIDPARAMETERVALUE_SETDISKLESSTHANUSED = 'InvalidParameterValue.SetDiskLessThanUsed'

# The value of the `slowMS` parameter should be at least 100 ms.
INVALIDPARAMETERVALUE_SLOWMSBELOWLIMIT = 'InvalidParameterValue.SlowMSBelowLimit'

# Incorrect purchasable specification.
INVALIDPARAMETERVALUE_SPECNOTONSALE = 'InvalidParameterValue.SpecNotOnSale'

# The start time should be earlier than the end time.
INVALIDPARAMETERVALUE_STARTTIMENOTBEFORETHANENDTIME = 'InvalidParameterValue.StartTimeNotBeforeThanEndTime'

# The instance is in a status where operations are not allowed.
INVALIDPARAMETERVALUE_STATUSABNORMAL = 'InvalidParameterValue.StatusAbnormal'

# The specified tag was not found.
INVALIDPARAMETERVALUE_TAGNOTFOUND = 'InvalidParameterValue.TagNotFound'

# The user account does not exist.
INVALIDPARAMETERVALUE_USERNOTFOUND = 'InvalidParameterValue.UserNotFound'

# The VPC (subnet) was not found.
INVALIDPARAMETERVALUE_VPCIDORSUBNETIDNOTFOUND = 'InvalidParameterValue.VpcIdOrSubnetIdNotFound'

# Instances are not purchasable in this AZ.
INVALIDPARAMETERVALUE_ZONECLOSED = 'InvalidParameterValue.ZoneClosed'

# Invalid availability zone
INVALIDPARAMETERVALUE_ZONEERROR = 'InvalidParameterValue.ZoneError'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The current version does not support the operation.
UNSUPPORTEDOPERATION_VERSIONNOTSUPPORT = 'UnsupportedOperation.VersionNotSupport'
