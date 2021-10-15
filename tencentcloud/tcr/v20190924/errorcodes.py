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

# Operation failed
FAILEDOPERATION = 'FailedOperation'

# Internal error. Please check and try again.
INTERNALERROR = 'InternalError'

# Database error. Please check and try again.
INTERNALERROR_DBERROR = 'InternalError.DbError'

# Target conflicts.
INTERNALERROR_ERRCONFLICT = 'InternalError.ErrConflict'

# The target does not exist.
INTERNALERROR_ERRNOTEXIST = 'InternalError.ErrNotExist'

# The resource already exists.
INTERNALERROR_ERRORCONFLICT = 'InternalError.ErrorConflict'

# The resource quota is exceeded.
INTERNALERROR_ERROROVERLIMIT = 'InternalError.ErrorOverLimit'

# Internal error with the TCR instance.
INTERNALERROR_ERRORTCRINTERNAL = 'InternalError.ErrorTcrInternal'

# Invalid request header
INTERNALERROR_ERRORTCRINVALIDMEDIATYPE = 'InternalError.ErrorTcrInvalidMediaType'

# TCR instance resource conflict.
INTERNALERROR_ERRORTCRRESOURCECONFLICT = 'InternalError.ErrorTcrResourceConflict'

# No permission for TCR operation.
INTERNALERROR_ERRORTCRUNAUTHORIZED = 'InternalError.ErrorTcrUnauthorized'

# Unknown error.
INTERNALERROR_UNKNOWN = 'InternalError.Unknown'

# Parameter error. Please check and try again.
INVALIDPARAMETER = 'InvalidParameter'

# The instance name already exists.
INVALIDPARAMETER_ERRORNAMEEXISTS = 'InvalidParameter.ErrorNameExists'

# Invalid instance name. Its format is incorrect or it has been reserved.
INVALIDPARAMETER_ERRORREGISTRYNAME = 'InvalidParameter.ErrorRegistryName'

# The instance can bind up to 10 Tencent Cloud tags.
INVALIDPARAMETER_ERRORTAGOVERLIMIT = 'InvalidParameter.ErrorTagOverLimit'

# Invalid TCR request.
INVALIDPARAMETER_ERRORTCRINVALIDPARAMETER = 'InvalidParameter.ErrorTcrInvalidParameter'

# Creating instance is not supported in this region.
INVALIDPARAMETER_UNSUPPORTEDREGION = 'InvalidParameter.UnsupportedRegion'

# Missing parameters. Please check and try again.
MISSINGPARAMETER = 'MissingParameter'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# Exceptional instance status.
RESOURCEINSUFFICIENT_ERRORINSTANCENOTRUNNING = 'ResourceInsufficient.ErrorInstanceNotRunning'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The resource of the TCR instance was not found.
RESOURCENOTFOUND_TCRRESOURCENOTFOUND = 'ResourceNotFound.TcrResourceNotFound'

# The operation is unauthorized.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Unknown parameter error. Please check and try again.
UNKNOWNPARAMETER = 'UnknownParameter'

# Unsupported operation
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
