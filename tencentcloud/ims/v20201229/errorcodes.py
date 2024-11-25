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


# `DryRun` Operation. It means that the request would have succeeded, but the `DryRun` parameter was used.
DRYRUNOPERATION = 'DryRunOperation'

# The operation failed.
FAILEDOPERATION = 'FailedOperation'

# An internal error occurred.
INTERNALERROR = 'InternalError'

# An internal error occurred.
INTERNALERROR_INTERNALERROR = 'InternalError.InternalError'

# The parameter is incorrect.
INVALIDPARAMETER = 'InvalidParameter'

# 
INVALIDPARAMETER_IMAGEASPECTRATIOTOOLARGE = 'InvalidParameter.ImageAspectRatioTooLarge'

# 
INVALIDPARAMETER_IMAGEDATATOOSMALL = 'InvalidParameter.ImageDataTooSmall'

# The image resolution is too low.
INVALIDPARAMETER_IMAGESIZETOOSMALL = 'InvalidParameter.ImageSizeTooSmall'

# The image content is incorrect.
INVALIDPARAMETER_INVALIDIMAGECONTENT = 'InvalidParameter.InvalidImageContent'

# The parameter is invalid.
INVALIDPARAMETER_INVALIDPARAMETER = 'InvalidParameter.InvalidParameter'

# The parameter value is incorrect.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The image content parameter is empty.
INVALIDPARAMETERVALUE_EMPTYIMAGECONTENT = 'InvalidParameterValue.EmptyImageContent'

# The image resolution is too low.
INVALIDPARAMETERVALUE_IMAGESIZETOOSMALL = 'InvalidParameterValue.ImageSizeTooSmall'

# `FileContent` and `FileUrl` are empty.
INVALIDPARAMETERVALUE_INVALIDCONTENT = 'InvalidParameterValue.InvalidContent'

# The `DataId` format is incorrect.
INVALIDPARAMETERVALUE_INVALIDDATAID = 'InvalidParameterValue.InvalidDataId'

# The image file content size is exceptional.
INVALIDPARAMETERVALUE_INVALIDFILECONTENTSIZE = 'InvalidParameterValue.InvalidFileContentSize'

# The image content is incorrect.
INVALIDPARAMETERVALUE_INVALIDIMAGECONTENT = 'InvalidParameterValue.InvalidImageContent'

# The parameter value is incorrect.
INVALIDPARAMETERVALUE_INVALIDPARAMETER = 'InvalidParameterValue.InvalidParameter'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# The parameter is missing.
MISSINGPARAMETER = 'MissingParameter'

# The operation was denied.
OPERATIONDENIED = 'OperationDenied'

# The number of requests exceeds the frequency limit.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# The resource is in use.
RESOURCEINUSE = 'ResourceInUse'

# The resource is insufficient.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# Image file download failed.
RESOURCEUNAVAILABLE_IMAGEDOWNLOADERROR = 'ResourceUnavailable.ImageDownloadError'

# The image resource is incorrect.
RESOURCEUNAVAILABLE_INVALIDIMAGECONTENT = 'ResourceUnavailable.InvalidImageContent'

# 
RESOURCEUNAVAILABLE_MODELCALLFAILED = 'ResourceUnavailable.ModelCallFailed'

# The resources have been sold out.
RESOURCESSOLDOUT = 'ResourcesSoldOut'

# The operation is unauthorized.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Operation not authorized/No valid package/The account is overdue
UNAUTHORIZEDOPERATION_UNAUTHORIZED = 'UnauthorizedOperation.Unauthorized'

# The parameter is unknown.
UNKNOWNPARAMETER = 'UnknownParameter'

# The operation is not supported.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
