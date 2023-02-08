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

# API operation authentication error.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# The old password has expired.
FAILEDOPERATION_OLDPASSWORDHASEXPIRED = 'FailedOperation.OldPasswordHasExpired'

# The old password has not expired.
FAILEDOPERATION_OLDPASSWORDINUSE = 'FailedOperation.OldPasswordInUse'

# Incorrect password.
FAILEDOPERATION_PASSWORDFAILURE = 'FailedOperation.PasswordFailure'

# The requested region does not match.
FAILEDOPERATION_REGIONMISMATCH = 'FailedOperation.RegionMismatch'

# Internal error.
INTERNALERROR = 'InternalError'

# Invalid parameter.
INVALIDPARAMETER = 'InvalidParameter'

# Incorrect parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Invalid cluster name
INVALIDPARAMETERVALUE_INVALIDAPPNAME = 'InvalidParameterValue.InvalidAppName'

# Invalid cluster name.
INVALIDPARAMETERVALUE_INVALIDCLUSTERNAME = 'InvalidParameterValue.InvalidClusterName'

# Invalid table group name.
INVALIDPARAMETERVALUE_INVALIDTABLEGROUPNAME = 'InvalidParameterValue.InvalidTableGroupName'

# Invalid time format.
INVALIDPARAMETERVALUE_INVALIDTIMEVALUE = 'InvalidParameterValue.InvalidTimeValue'

# Invalid AZ name
INVALIDPARAMETERVALUE_INVALIDZONENAME = 'InvalidParameterValue.InvalidZoneName'

# Unsupported application data description type.
INVALIDPARAMETERVALUE_UNSUPPORTIDLTYPE = 'InvalidParameterValue.UnsupportIdlType'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# The resource is in use.
RESOURCEINUSE = 'ResourceInUse'

# Insufficient resources.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# Insufficient balance.
RESOURCEINSUFFICIENT_BALANCEERROR = 'ResourceInsufficient.BalanceError'

# No available cluster resources.
RESOURCEINSUFFICIENT_NOAVAILABLEAPP = 'ResourceInsufficient.NoAvailableApp'

# No cluster resources available.
RESOURCEINSUFFICIENT_NOAVAILABLECLUSTER = 'ResourceInsufficient.NoAvailableCluster'

# There are no VIP resources available in the VPC.
RESOURCEINSUFFICIENT_NOENOUGHVIPINVPC = 'ResourceInsufficient.NoEnoughVipInVPC'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The cluster name already exists.
RESOURCEUNAVAILABLE_DUPLICATECLUSTERNAME = 'ResourceUnavailable.DuplicateClusterName'

# The table group ID or name already exists.
RESOURCEUNAVAILABLE_DUPLICATETABLEGROUPINFO = 'ResourceUnavailable.DuplicateTableGroupInfo'

# The table group name already exists.
RESOURCEUNAVAILABLE_DUPLICATETABLEGROUPNAME = 'ResourceUnavailable.DuplicateTableGroupName'

# No table group resources available.
RESOURCEUNAVAILABLE_NOAVAILABLETABLEGROUP = 'ResourceUnavailable.NoAvailableTableGroup'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
