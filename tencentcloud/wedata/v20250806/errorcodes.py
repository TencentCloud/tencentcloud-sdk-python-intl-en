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

# Not logged in or login has expired.
AUTHFAILURE_SIGNATUREEXPIRE = 'AuthFailure.SignatureExpire'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Resource status of the current operation is invalid.
FAILEDOPERATION_EXECUTORCLUSTERSTATUSERROR = 'FailedOperation.ExecutorClusterStatusError'

# Internal error.
INTERNALERROR = 'InternalError'

# Missing required parameters or invalid parameters.
INTERNALERROR_INVALIDPARAMETER = 'InternalError.InvalidParameter'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# Client ip is unauthorized.
INVALIDPARAMETER_CLIENTIPNOTAUTHORIZED = 'InvalidParameter.ClientIpNotAuthorized'

# Incorrect query filter parameter.
INVALIDPARAMETER_INVALIDFILTERPARAMETER = 'InvalidParameter.InvalidFilterParameter'

# Illegal parameter.
INVALIDPARAMETER_INVALIDPARAMSERROR = 'InvalidParameter.InvalidParamsError'

# Missing Servlet Request Parameter
INVALIDPARAMETER_MISSINGREQUESTPARAMETER = 'InvalidParameter.MissingRequestParameter'

# System security quota exceeded.
INVALIDPARAMETER_QUOTAEXCEEDERROR = 'InvalidParameter.QuotaExceedError'

# Duplicate project name.
INVALIDPARAMETER_WORKSPACENAMEDUPLICATION = 'InvalidParameter.WorkspaceNameDuplication'

# Workspace does not exist.
INVALIDPARAMETER_WORKSPACENOTEXIST = 'InvalidParameter.WorkspaceNotExist'

# Parameter value error.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Alarm rule name is duplicate.
INVALIDPARAMETERVALUE_RULENAMEREPEATED = 'InvalidParameterValue.RuleNameRepeated'

# Param Validation Error
INVALIDPARAMETERVALUE_VALIDATIONERROR = 'InvalidParameterValue.ValidationError'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# Parameter missing.
MISSINGPARAMETER = 'MissingParameter'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# User not in allowlist.
OPERATIONDENIED_USERNOTINWHITELISTERROR = 'OperationDenied.UserNotInWhitelistError'

# The resource is occupied.
RESOURCEINUSE = 'ResourceInUse'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# The user is not a member of the current project.
UNAUTHORIZEDOPERATION_USERNOTINPROJECT = 'UnauthorizedOperation.UserNotInProject'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# The operation is not supported.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
