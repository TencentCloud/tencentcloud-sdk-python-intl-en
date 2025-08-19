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

# Internal error.
INTERNALERROR = 'InternalError'

# Internal error.
INTERNALERROR_INTERNAL = 'InternalError.Internal'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# Report embedding error.
INVALIDPARAMETER_EMBED = 'InvalidParameter.Embed'

# Parameter value error.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# Parameters are missing.
MISSINGPARAMETER = 'MissingParameter'

# The required parameter is missing.
MISSINGPARAMETER_MISSINGPARAM = 'MissingParameter.MissingParam'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# Too many and frequent requests.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Permission error.
UNAUTHORIZEDOPERATION_AUTHORIZE = 'UnauthorizedOperation.Authorize'

# User is not enabled.
UNAUTHORIZEDOPERATION_INACTIVE = 'UnauthorizedOperation.Inactive'

# The user does not exist.
UNAUTHORIZEDOPERATION_USERNOTEXIST = 'UnauthorizedOperation.UserNotExist'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# The operation is not supported.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# Default business exception.
UNSUPPORTEDOPERATION_BIERROR = 'UnsupportedOperation.BIError'
