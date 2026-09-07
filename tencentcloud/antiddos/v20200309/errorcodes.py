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

# The DryRun operation means that the request will be successful, but an extra DryRun parameter is passed.
DRYRUNOPERATION = 'DryRunOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Insufficient account balance.
FAILEDOPERATION_INSUFFICIENTBALANCE = 'FailedOperation.InsufficientBalance'

# Internal error. Please try again later.
INTERNALERROR = 'InternalError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# This parameter can only be used when the allowlist feature is enabled.
INVALIDPARAMETER_SPECIALPARAMETERFORSPECIALACCOUNT = 'InvalidParameter.SpecialParameterForSpecialAccount'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The quota limit should not be exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# Missing parameters. Please check and try again.
MISSINGPARAMETER = 'MissingParameter'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# The number of requests should not exceed the frequency limit.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# The resource is occupied.
RESOURCEINUSE = 'ResourceInUse'

# Insufficient resource.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource does not exist. Please try again later.
RESOURCENOTFOUND = 'ResourceNotFound'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The resources have been sold out.
RESOURCESSOLDOUT = 'ResourcesSoldOut'

# The operation is unauthorized.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Unknown parameter error. Please check and try again.
UNKNOWNPARAMETER = 'UnknownParameter'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# This business bandwidth is not supported.
UNSUPPORTEDOPERATION_BANDWIDTHNOTSUPPORTED = 'UnsupportedOperation.BandwidthNotSupported'

# This base protection bandwidth value is unsupported.
UNSUPPORTEDOPERATION_BASICPROTECTBANDWIDTHNOTSUPPORTED = 'UnsupportedOperation.BasicProtectBandwidthNotSupported'

# This elastic bandwidth value is not supported.
UNSUPPORTEDOPERATION_ELASTICPROTECTBANDWIDTHNOTSUPPORTED = 'UnsupportedOperation.ElasticProtectBandwidthNotSupported'

# This payment type is not supported.
UNSUPPORTEDOPERATION_INSTANCECHARGETYPENOTSUPPORTED = 'UnsupportedOperation.InstanceChargeTypeNotSupported'

# The billing period is not supported. see the corresponding billing periods supported by the anti-ddos pro package.
UNSUPPORTEDOPERATION_PERIODNOTSUPPORTED = 'UnsupportedOperation.PeriodNotSupported'

# The number of protected ips is not supported.
UNSUPPORTEDOPERATION_PROTECTIPCOUNTNOTSUPPORTED = 'UnsupportedOperation.ProtectIpCountNotSupported'

# This region is not supported.
UNSUPPORTEDOPERATION_REGIONNOTSUPPORTED = 'UnsupportedOperation.RegionNotSupported'
