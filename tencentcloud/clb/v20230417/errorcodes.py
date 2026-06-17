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

# DryRun operation means the request will be successful, but the DryRun parameter is passed.
DRYRUNOPERATION = 'DryRunOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# LB status exception.
FAILEDOPERATION_INVALIDLBSTATUS = 'FailedOperation.InvalidLBStatus'

# Internal error.
INTERNALERROR = 'InternalError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# To ensure no resource leakage and maintain the ID idempotence of created resources, ClientToken is used to create resources. If the order process has ended and shipment failed, or the order process has not been updated for a long time, a message will indicate that the current ClientToken has timed out.
INVALIDPARAMETER_CLIENTTOKENLIMITEXCEEDED = 'InvalidParameter.ClientTokenLimitExceeded'

# Incorrect parameter format.
INVALIDPARAMETER_FORMATERROR = 'InvalidParameter.FormatError'

# CLB instance ID error.
INVALIDPARAMETER_LBIDNOTFOUND = 'InvalidParameter.LBIdNotFound'

# Listener ID error.
INVALIDPARAMETER_LISTENERIDNOTFOUND = 'InvalidParameter.ListenerIdNotFound'

# Unable to find eligible forwarding rules.
INVALIDPARAMETER_LOCATIONNOTFOUND = 'InvalidParameter.LocationNotFound'

# Listener port check due to port conflicts or other reasons.
INVALIDPARAMETER_PORTCHECKFAILED = 'InvalidParameter.PortCheckFailed'

# Listener protocol check failed because, for example, the protocol used is incompatible with the corresponding operation.
INVALIDPARAMETER_PROTOCOLCHECKFAILED = 'InvalidParameter.ProtocolCheckFailed'

# Invalid region.
INVALIDPARAMETER_REGIONNOTFOUND = 'InvalidParameter.RegionNotFound'

# The forwarding rule has been bound to a redirection relationship.
INVALIDPARAMETER_REWRITEALREADYEXIST = 'InvalidParameter.RewriteAlreadyExist'

# Some redirection rules do not exist.
INVALIDPARAMETER_SOMEREWRITENOTFOUND = 'InvalidParameter.SomeRewriteNotFound'

# Parameter value error.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Duplicate parameter values.
INVALIDPARAMETERVALUE_DUPLICATE = 'InvalidParameterValue.Duplicate'

# Filter parameter input error.
INVALIDPARAMETERVALUE_INVALIDFILTER = 'InvalidParameterValue.InvalidFilter'

# Invalid parameter length.
INVALIDPARAMETERVALUE_LENGTH = 'InvalidParameterValue.Length'

# Invalid parameter value range.
INVALIDPARAMETERVALUE_RANGE = 'InvalidParameterValue.Range'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# Parameters are missing.
MISSINGPARAMETER = 'MissingParameter'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# Number of requests exceeds the frequency limit.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# The resource is occupied.
RESOURCEINUSE = 'ResourceInUse'

# Insufficient resources.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# Resources are sold out.
RESOURCESSOLDOUT = 'ResourcesSoldOut'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# The operation is not supported.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
