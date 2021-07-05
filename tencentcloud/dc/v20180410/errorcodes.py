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

# Unauthorized operation: CAM signature or authentication error.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# An internal error occurred.
INTERNALERROR = 'InternalError'

# Invalid parameter.
INVALIDPARAMETER = 'InvalidParameter'

# Wrong IP address.
INVALIDPARAMETER_ADDRESSERROR = 'InvalidParameter.AddressError'

# The connection does not belong to this account.
INVALIDPARAMETER_DIRECTCONNECTIDISNOTUIN = 'InvalidParameter.DirectConnectIdIsNotUin'

# The account ID does not exist.
INVALIDPARAMETER_UINISNOTEXIST = 'InvalidParameter.UinIsNotExist'

# VLAN conflict.
INVALIDPARAMETER_VLANCONFLICT = 'InvalidParameter.VlanConflict'

# The parameter value is invalid.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# VLAN conflict.
INVALIDPARAMETERVALUE_VLANCONFLICT = 'InvalidParameterValue.VlanConfLict'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# The number of connections has reached the upper limit.
LIMITEXCEEDED_DIRECTCONNECTLIMITEXCEEDED = 'LimitExceeded.DirectConnectLimitExceeded'

# The number of the dedicated tunnels of the connection has reached the upper limit.
LIMITEXCEEDED_DIRECTCONNECTTUNNELLIMITEXCEEDED = 'LimitExceeded.DirectConnectTunnelLimitExceeded'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# The connection VPC already exists.
RESOURCEINUSE_DCVPCISEXIST = 'ResourceInUse.DcVpcIsExist'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The dedicated tunnel does not exist.
RESOURCENOTFOUND_DIRECTCONNECTTUNNELIDISNOTEXIST = 'ResourceNotFound.DirectConnectTunnelIdIsNotExist'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# Your account is in arrears, and the service cannot be activated. Please top up your account first.
RESOURCEUNAVAILABLE_INSUFFICIENTBALANCE = 'ResourceUnavailable.InsufficientBalance'

# The operation is unauthorized.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# Cross-border dedicated tunnel is not allowed. Please contact us.
UNSUPPORTEDOPERATION_CROSSBORDERDIRECTCONNECTTUNNEL = 'UnsupportedOperation.CrossBorderDirectConnectTunnel'

# Status conflict.
UNSUPPORTEDOPERATION_STATECONFLICT = 'UnsupportedOperation.StateConfLict'
