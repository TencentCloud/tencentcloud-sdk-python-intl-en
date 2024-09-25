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


# You have no permission to perform this operation. check your CAM policies to make sure that you have the corresponding CAM permissions.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# The generated image failed the review. Please try again.
FAILEDOPERATION_GENERATEIMAGEFAILED = 'FailedOperation.GenerateImageFailed'

# Image decoding failed.
FAILEDOPERATION_IMAGEDECODEFAILED = 'FailedOperation.ImageDecodeFailed'

# Image download error.
FAILEDOPERATION_IMAGEDOWNLOADERROR = 'FailedOperation.ImageDownloadError'

# The image resolution is too high, which exceeds 2000×2000.
FAILEDOPERATION_IMAGERESOLUTIONEXCEED = 'FailedOperation.ImageResolutionExceed'

# The size of the image after base64 encoding cannot exceed 10 MB.
FAILEDOPERATION_IMAGESIZEEXCEED = 'FailedOperation.ImageSizeExceed'

# Internal service error. Please try again.
FAILEDOPERATION_INNERERROR = 'FailedOperation.InnerError'

# The entire request body (usually images) is too large .
FAILEDOPERATION_REQUESTENTITYTOOLARGE = 'FailedOperation.RequestEntityTooLarge'

# The backend service timed out.
FAILEDOPERATION_REQUESTTIMEOUT = 'FailedOperation.RequestTimeout'

# RPC request failed, typically due to algorithm service malfunction.
FAILEDOPERATION_RPCFAIL = 'FailedOperation.RpcFail'

# Internal service error.
FAILEDOPERATION_SERVERERROR = 'FailedOperation.ServerError'

# Unknown error.
FAILEDOPERATION_UNKNOWN = 'FailedOperation.Unknown'

# Invalid parameters.
INVALIDPARAMETER_INVALIDPARAMETER = 'InvalidParameter.InvalidParameter'

# No image is input.
INVALIDPARAMETERVALUE_IMAGEEMPTY = 'InvalidParameterValue.ImageEmpty'

# Parameter or value is invalid.
INVALIDPARAMETERVALUE_PARAMETERVALUEERROR = 'InvalidParameterValue.ParameterValueError'

# 1xx styles cannot be used together with other styles.
INVALIDPARAMETERVALUE_STYLECONFLICT = 'InvalidParameterValue.StyleConflict'

# The input text is too long. Use a shorter one and try again.
INVALIDPARAMETERVALUE_TEXTLENGTHEXCEED = 'InvalidParameterValue.TextLengthExceed'

# The URL format is invalid.
INVALIDPARAMETERVALUE_URLILLEGAL = 'InvalidParameterValue.UrlIllegal'

# The image failed the review because it contains illegal information.
OPERATIONDENIED_IMAGEILLEGALDETECTED = 'OperationDenied.ImageIllegalDetected'

# The text failed the review because it contains illegal information.
OPERATIONDENIED_TEXTILLEGALDETECTED = 'OperationDenied.TextIllegalDetected'

# Too frequent requests
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# Too many tasks are being processed simultaneously. Please try again later.
REQUESTLIMITEXCEEDED_JOBNUMEXCEED = 'RequestLimitExceeded.JobNumExceed'

# The resource is being delivered.
RESOURCEUNAVAILABLE_DELIVERING = 'ResourceUnavailable.Delivering'

# The account is in arrears.
RESOURCEUNAVAILABLE_INARREARS = 'ResourceUnavailable.InArrears'

# Insufficient balance.
RESOURCEUNAVAILABLE_LOWBALANCE = 'ResourceUnavailable.LowBalance'

# The billing status is unknown. Check whether the service has been activated in the console.
RESOURCEUNAVAILABLE_NOTEXIST = 'ResourceUnavailable.NotExist'

# Services for the account has been stopped.
RESOURCEUNAVAILABLE_STOPUSING = 'ResourceUnavailable.StopUsing'

# The billing status is abnormal.
RESOURCESSOLDOUT_CHARGESTATUSEXCEPTION = 'ResourcesSoldOut.ChargeStatusException'
