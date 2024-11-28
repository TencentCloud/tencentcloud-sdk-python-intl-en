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


# CAM signature/authentication error.
AUTHFAILURE = 'AuthFailure'

# Failed to detect human body keypoints.
FAILEDOPERATION_BODYJOINTSFAIL = 'FailedOperation.BodyJointsFail'

# Driving failed.
FAILEDOPERATION_DRIVERFAILED = 'FailedOperation.DriverFailed'

# The face box is too small and cannot be used for face detection.
FAILEDOPERATION_FACESIZETOOSMALL = 'FailedOperation.FaceSizeTooSmall'

# The human body in the image is obscured or incomplete. Please upload another image.
FAILEDOPERATION_IMAGEBODYJOINSUNDETECTED = 'FailedOperation.ImageBodyJoinsUndetected'

# The height of the body (from head to ankle) in the input image accounts for less than half of the image height.
FAILEDOPERATION_IMAGEBODYSMALL = 'FailedOperation.ImageBodySmall'

# No human body is detected in the input image.
FAILEDOPERATION_IMAGECHECKNOBODY = 'FailedOperation.ImageCheckNoBody'

# Image decoding failed.
FAILEDOPERATION_IMAGEDECODEFAILED = 'FailedOperation.ImageDecodeFailed'

# Failed to detect the face in the input image.
FAILEDOPERATION_IMAGEDETECTFACEFAILED = 'FailedOperation.ImageDetectFaceFailed'

# Face detection failed.
FAILEDOPERATION_IMAGEFACEDETECTFAILED = 'FailedOperation.ImageFaceDetectFailed'

# Multiple human faces are detected in the input image.
FAILEDOPERATION_IMAGEMANYPEOPLE = 'FailedOperation.ImageManyPeople'

# The image file is not supported.
FAILEDOPERATION_IMAGENOTSUPPORTED = 'FailedOperation.ImageNotSupported'

# The aspect ratio of the input image is not within the range of 1:1.2 to 1:2.
FAILEDOPERATION_IMAGERADIOEXCCEED = 'FailedOperation.ImageRadioExcceed'

# The image aspect ratio exceeds the limit.
FAILEDOPERATION_IMAGERATIOEXCCEED = 'FailedOperation.ImageRatioExcceed'

# The image resolution is too high.
FAILEDOPERATION_IMAGERESOLUTIONEXCEED = 'FailedOperation.ImageResolutionExceed'

# The size of the image after base64 encoding exceeds the upper limit.
FAILEDOPERATION_IMAGESIZEEXCEED = 'FailedOperation.ImageSizeExceed'

# Internal service error. Please try again.
FAILEDOPERATION_INNERERROR = 'FailedOperation.InnerError'

# The task does not exist.
FAILEDOPERATION_JOBNOTFOUND = 'FailedOperation.JobNotFound'

# Too many tasks are in queue. Please try again later.
FAILEDOPERATION_JOBQUEUEFULL = 'FailedOperation.JobQueueFull'

# The core joints are not detected.
FAILEDOPERATION_KEYPOINTUNDETECTED = 'FailedOperation.KeyPointUndetected'

# Failed to pass the content review.
FAILEDOPERATION_MODERATIONFAILED = 'FailedOperation.ModerationFailed'

# No face is detected in the first frame of the template video.
FAILEDOPERATION_TEMPLATEFIRSTFRAMENOTDETECTFACE = 'FailedOperation.TemplateFirstFrameNotDetectFace'

# The template video contains frames with no human body detected.
FAILEDOPERATION_TEMPLATENOTDETECTBODY = 'FailedOperation.TemplateNotDetectBody'

# Internal error.
INTERNALERROR = 'InternalError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# The template does not exist.
INVALIDPARAMETER_TEMPLATENOTEXISTED = 'InvalidParameter.TemplateNotExisted'

# Invalid parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The resolution is not supported.
INVALIDPARAMETERVALUE_INVALIDVIDEORESOLUTION = 'InvalidParameterValue.InvalidVideoResolution'

# The image contains no human face.
INVALIDPARAMETERVALUE_NOFACEINPHOTO = 'InvalidParameterValue.NoFaceInPhoto'

# Parameter field or value is invalid.
INVALIDPARAMETERVALUE_PARAMETERVALUEERROR = 'InvalidParameterValue.ParameterValueError'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# Too many and frequent requests. 
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# The number of submitted tasks exceeds the maximum number of concurrent tasks.
REQUESTLIMITEXCEEDED_JOBNUMEXCEED = 'RequestLimitExceeded.JobNumExceed'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# The operation is not supported.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
