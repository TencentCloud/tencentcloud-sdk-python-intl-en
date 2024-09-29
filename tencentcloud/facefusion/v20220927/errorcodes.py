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


# Insufficient balance, failed to open, please recharge and open again.
FAILEDOPERATION_BALANCEINSUFFICIENT = 'FailedOperation.BalanceInsufficient'

# The face was filtered because it was too small. It is recommended that the face size is not less than 34x34 pixels.
FAILEDOPERATION_FACESIZETOOSMALL = 'FailedOperation.FaceSizeTooSmall'

# The material has not been reviewed.
FAILEDOPERATION_FUSEMATERIALNOTAUTH = 'FailedOperation.FuseMaterialNotAuth'

# The material does not exist.
FAILEDOPERATION_FUSEMATERIALNOTEXIST = 'FailedOperation.FuseMaterialNotExist'

# Image decoding failed.
FAILEDOPERATION_IMAGEDECODEFAILED = 'FailedOperation.ImageDecodeFailed'

# Image download failed.
FAILEDOPERATION_IMAGEDOWNLOADERROR = 'FailedOperation.ImageDownloadError'

# The short edge resolution of the image is lower than 64 pixels.
FAILEDOPERATION_IMAGERESOLUTIONTOOSMALL = 'FailedOperation.ImageResolutionTooSmall'

# The image after Base64 encoding exceeds in size.
FAILEDOPERATION_IMAGESIZEEXCEED = 'FailedOperation.ImageSizeExceed'

# The image size is too large or too small and does not meet algorithm requirements.
FAILEDOPERATION_IMAGESIZEINVALID = 'FailedOperation.ImageSizeInvalid'

# Internal service error.
FAILEDOPERATION_INNERERROR = 'FailedOperation.InnerError'

# The face cannot be detected because the face box is too small.
FAILEDOPERATION_NOFACEDETECTED = 'FailedOperation.NoFaceDetected'

# Parameter or value is invalid.
FAILEDOPERATION_PARAMETERVALUEERROR = 'FailedOperation.ParameterValueError'

# The backend service timed out.
FAILEDOPERATION_REQUESTTIMEOUT = 'FailedOperation.RequestTimeout'

# RPC request failed, typically due to algorithm service malfunction.
FAILEDOPERATION_RPCFAIL = 'FailedOperation.RpcFail'

# The material face ID does not exist.
FAILEDOPERATION_TEMPLATEFACEIDNOTEXIST = 'FailedOperation.TemplateFaceIDNotExist'

# Internal error.
FAILEDOPERATION_UNKNOWERROR = 'FailedOperation.UnKnowError'

# Unknown error.
FAILEDOPERATION_UNKNOWN = 'FailedOperation.Unknown'

# Activity ID is not found.
INVALIDPARAMETERVALUE_ACTIVITYIDNOTFOUND = 'InvalidParameterValue.ActivityIdNotFound'

# Face box parameters are invalid, or the face box is too small.
INVALIDPARAMETERVALUE_FACERECTPARAMETERVALUEERROR = 'InvalidParameterValue.FaceRectParameterValueError'

# No material ID is found.
INVALIDPARAMETERVALUE_MATERIALIDNOTFOUND = 'InvalidParameterValue.MaterialIdNotFound'

# The URL format is invalid.
INVALIDPARAMETERVALUE_URLILLEGAL = 'InvalidParameterValue.UrlIllegal'

# The number of requests exceeded the rate limit.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# Resources are insufficient.
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The account has been frozen.
RESOURCEUNAVAILABLE_FREEZE = 'ResourceUnavailable.Freeze'

# The account is in arrears.
RESOURCEUNAVAILABLE_INARREARS = 'ResourceUnavailable.InArrears'

# The service is being opened, please wait.
RESOURCEUNAVAILABLE_ISOPENING = 'ResourceUnavailable.IsOpening'

# The billing status is unknown. Check whether the service has been activated in the console.
RESOURCEUNAVAILABLE_NOTEXIST = 'ResourceUnavailable.NotExist'

# The resource has been possessed.
RESOURCEUNAVAILABLE_RECOVER = 'ResourceUnavailable.Recover'

# Services for the account has been stopped.
RESOURCEUNAVAILABLE_STOPUSING = 'ResourceUnavailable.StopUsing'
