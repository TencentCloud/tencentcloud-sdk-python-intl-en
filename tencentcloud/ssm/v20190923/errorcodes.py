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


# Error with CAM signature/authentication.
AUTHFAILURE = 'AuthFailure'

# `DryRun` Operation. It means that the request would have succeeded, but the `DryRun` parameter was used.
DRYRUNOPERATION = 'DryRunOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# KMS operation failed.
FAILEDOPERATION_ACCESSKMSERROR = 'FailedOperation.AccessKmsError'

# The rotation is prohibited.
FAILEDOPERATION_ROTATIONFORBIDDEN = 'FailedOperation.RotationForbidden'

# An internal error occurred.
INTERNALERROR = 'InternalError'

# Incorrect parameter.
INVALIDPARAMETER = 'InvalidParameter'

# The parameter value is invalid.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The tag keys are duplicated.
INVALIDPARAMETERVALUE_TAGKEYSDUPLICATED = 'InvalidParameterValue.TagKeysDuplicated'

# The tag key or tag value does not exist.
INVALIDPARAMETERVALUE_TAGSNOTEXISTED = 'InvalidParameterValue.TagsNotExisted'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# Reached the upper limit of access keys.
OPERATIONDENIED_ACCESSKEYOVERLIMIT = 'OperationDenied.AccessKeyOverLimit'

# It is not allowed to manually update credentials with automatic rotation enabled.
OPERATIONDENIED_AUTOROTATEDRESOURCE = 'OperationDenied.AutoRotatedResource'

# The role does not exist.
OPERATIONDENIED_ROLENOTEXIST = 'OperationDenied.RoleNotExist'

# The secret is not owned by the current account. 
OPERATIONDENIED_UINNOTMATCH = 'OperationDenied.UinNotMatch'

# The number of requests exceeds the frequency limit.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# The resource is in use.
RESOURCEINUSE = 'ResourceInUse'

# The Secret name already exists.
RESOURCEINUSE_SECRETEXISTS = 'ResourceInUse.SecretExists'

# The Version ID already exists.
RESOURCEINUSE_VERSIONIDEXISTS = 'ResourceInUse.VersionIdExists'

# Insufficient resource.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The secret does not exist.
RESOURCENOTFOUND_SECRETNOTEXIST = 'ResourceNotFound.SecretNotExist'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The service is not purchased.
RESOURCEUNAVAILABLE_NOTPURCHASED = 'ResourceUnavailable.NotPurchased'

# The Secret is disabled.
RESOURCEUNAVAILABLE_RESOURCEDISABLED = 'ResourceUnavailable.ResourceDisabled'

# The Secret is in `PendingDelete` status.
RESOURCEUNAVAILABLE_RESOURCEPENDINGDELETED = 'ResourceUnavailable.ResourcePendingDeleted'

# The credential has not been initialized.
RESOURCEUNAVAILABLE_RESOURCEUNINITIALIZED = 'ResourceUnavailable.ResourceUninitialized'

# The resources have been sold out.
RESOURCESSOLDOUT = 'ResourcesSoldOut'

# The operation is unauthorized.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Failed to access KMS.
UNAUTHORIZEDOPERATION_ACCESSKMSERROR = 'UnauthorizedOperation.AccessKmsError'

# Unknown parameter.
UNKNOWNPARAMETER = 'UnknownParameter'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
