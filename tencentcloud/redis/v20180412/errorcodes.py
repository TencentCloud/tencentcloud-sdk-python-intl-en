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


# No exact description for this error code for the time being.
FAILEDOPERATION_REDOFLOWFAILED = 'FailedOperation.RedoFlowFailed'

# Internal system error, which is irrelevant to the business.
FAILEDOPERATION_SYSTEMERROR = 'FailedOperation.SystemError'

# Internal system error with the database operation, which may be update, insert, select, etc.
INTERNALERROR_DBOPERATIONFAILED = 'InternalError.DbOperationFailed'

# Internal error.
INTERNALERROR_INTERNALERROR = 'InternalError.InternalError'

# Incorrect parameter.
INVALIDPARAMETER = 'InvalidParameter'

# The parameter is empty.
INVALIDPARAMETER_EMPTYPARAM = 'InvalidParameter.EmptyParam'

# Invalid service parameter.
INVALIDPARAMETER_INVALIDPARAMETER = 'InvalidParameter.InvalidParameter'

# The API has no CAM permissions.
INVALIDPARAMETER_PERMISSIONDENIED = 'InvalidParameter.PermissionDenied'

# Password verification error due to incorrect password.
INVALIDPARAMETERVALUE_PASSWORDERROR = 'InvalidParameterValue.PasswordError'

# When the password is set, the old password passed in by MC does not match the previously set password.
INVALIDPARAMETERVALUE_PASSWORDRULEERROR = 'InvalidParameterValue.PasswordRuleError'

# The request capacity is too small. Capacity reduction is not supported.
INVALIDPARAMETERVALUE_REDUCECAPACITYNOTALLOWED = 'InvalidParameterValue.ReduceCapacityNotAllowed'

# The global replication group doesn’t exist.
INVALIDPARAMETERVALUE_REPLICATIONGROUPNOTEXISTS = 'InvalidParameterValue.ReplicationGroupNotExists'

# The instance type is not supported.
INVALIDPARAMETERVALUE_UNSUPPORTEDTYPE = 'InvalidParameterValue.UnSupportedType'

# The requested capacity is out of the purchasable capacity range.
LIMITEXCEEDED_MEMSIZENOTINRANGE = 'LimitExceeded.MemSizeNotInRange'

# No Redis instance is found by the serialId.
RESOURCENOTFOUND_INSTANCENOTEXISTS = 'ResourceNotFound.InstanceNotExists'

# Redis has been locked by another process.
RESOURCEUNAVAILABLE_INSTANCELOCKEDERROR = 'ResourceUnavailable.InstanceLockedError'

# Instance status error.
RESOURCEUNAVAILABLE_INSTANCESTATEERROR = 'ResourceUnavailable.InstanceStateError'

# The Redis status is exceptional, and the corresponding process cannot be executed.
RESOURCEUNAVAILABLE_INSTANCESTATUSABNORMAL = 'ResourceUnavailable.InstanceStatusAbnormal'

# Operation unsupported: the instance is exceptional.
RESOURCEUNAVAILABLE_INSTANCESTATUSERROR = 'ResourceUnavailable.InstanceStatusError'

# No CAM permissions.
UNAUTHORIZEDOPERATION_NOCAMAUTHED = 'UnauthorizedOperation.NoCAMAuthed'

# The user is not in the allowlist.
UNAUTHORIZEDOPERATION_USERNOTINWHITELIST = 'UnauthorizedOperation.UserNotInWhiteList'

# The Redis cluster edition is not allowed to connect to a security group.
UNSUPPORTEDOPERATION_CLUSTERINSTANCEACCESSEDDENY = 'UnsupportedOperation.ClusterInstanceAccessedDeny'
