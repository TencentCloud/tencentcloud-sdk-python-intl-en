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

# DryRun operation, which means the DryRun parameter is passed in yet the request will still be successful.
DRYRUNOPERATION = 'DryRunOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Internal error.
INTERNALERROR = 'InternalError'

# Invalid parameter.
INVALIDPARAMETER = 'InvalidParameter'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The instance does not exist.
INVALIDPARAMETERVALUE_INSTANCENOTEXIST = 'InvalidParameterValue.InstanceNotExist'

# The parameter is required.
INVALIDPARAMETERVALUE_NOTALLOWEDEMPTY = 'InvalidParameterValue.NotAllowedEmpty'

# The parameter already exists.
INVALIDPARAMETERVALUE_REPETITIONVALUE = 'InvalidParameterValue.RepetitionValue'

# Invalid subnet ID.
INVALIDPARAMETERVALUE_SUBNETIDINVALID = 'InvalidParameterValue.SubnetIdInvalid'

# The subnet is not in the zone.
INVALIDPARAMETERVALUE_SUBNETNOTBELONGTOZONE = 'InvalidParameterValue.SubnetNotBelongToZone'

# Invalid VPC ID.
INVALIDPARAMETERVALUE_VPCIDINVALID = 'InvalidParameterValue.VpcIdInvalid'

# The value of the `Action` parameter is incorrect.
INVALIDPARAMETERVALUE_WRONGACTION = 'InvalidParameterValue.WrongAction'

# The zone is not supported.
INVALIDPARAMETERVALUE_ZONENOTSUPPORT = 'InvalidParameterValue.ZoneNotSupport'

# The quota limit has been reached.
LIMITEXCEEDED = 'LimitExceeded'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# Task paused.
OPERATIONDENIED_RESOURCETASKPAUSED = 'OperationDenied.ResourceTaskPaused'

# The number of requests exceeds the frequency limit.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# The resource is occupied.
RESOURCEINUSE = 'ResourceInUse'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# The batch instance deletion limit is reached.
UNSUPPORTEDOPERATION_BATCHDELINSTANCELIMIT = 'UnsupportedOperation.BatchDelInstanceLimit'

# Oss rejected the operation.
UNSUPPORTEDOPERATION_OSSREJECT = 'UnsupportedOperation.OssReject'
