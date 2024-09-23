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
AUTHFAILURE_INVALIDAUTHORIZATION = 'AuthFailure.InvalidAuthorization'

# No motions of eye closing are detected.
FAILEDOPERATION_ACTIONCLOSEEYE = 'FailedOperation.ActionCloseEye'

# The face is too close to the screen.
FAILEDOPERATION_ACTIONFACECLOSE = 'FailedOperation.ActionFaceClose'

# The face is too far from the screen.
FAILEDOPERATION_ACTIONFACEFAR = 'FailedOperation.ActionFaceFar'

# The face is too far left from the screen.
FAILEDOPERATION_ACTIONFACELEFT = 'FailedOperation.ActionFaceLeft'

# The face is too far right from the screen.
FAILEDOPERATION_ACTIONFACERIGHT = 'FailedOperation.ActionFaceRight'

# No movement is detected.
FAILEDOPERATION_ACTIONFIRSTACTION = 'FailedOperation.ActionFirstAction'

# The lighting is too dim.
FAILEDOPERATION_ACTIONLIGHTDARK = 'FailedOperation.ActionLightDark'

# The lighting is too strong.
FAILEDOPERATION_ACTIONLIGHTSTRONG = 'FailedOperation.ActionLightStrong'

# Failed to detect a full face.
FAILEDOPERATION_ACTIONNODETECTFACE = 'FailedOperation.ActionNodetectFace'

# No motions of mouth opening are detected.
FAILEDOPERATION_ACTIONOPENMOUTH = 'FailedOperation.ActionOpenMouth'

# Comparison failed.
FAILEDOPERATION_COMPAREFAIL = 'FailedOperation.CompareFail'

# The comparison similarity did not reach the passing standard.
FAILEDOPERATION_COMPARELOWSIMILARITY = 'FailedOperation.CompareLowSimilarity'

# Error calling the comparison engine API.
FAILEDOPERATION_COMPARESYSTEMERROR = 'FailedOperation.CompareSystemError'

# The face in the picture is blocked, please upload a picture without any blockage
FAILEDOPERATION_COVEREDFACE = 'FailedOperation.CoveredFace'

# The service engine call failed, please try again
FAILEDOPERATION_DETECTENGINESYSTEMERROR = 'FailedOperation.DetectEngineSystemError'

# File download failed.
FAILEDOPERATION_DOWNLOADERROR = 'FailedOperation.DownLoadError'

# File download timed out.
FAILEDOPERATION_DOWNLOADTIMEOUTERROR = 'FailedOperation.DownLoadTimeoutError'

# The image is blurry.
FAILEDOPERATION_IMAGEBLUR = 'FailedOperation.ImageBlur'

# Image decoding failed.
FAILEDOPERATION_IMAGEDECODEFAILED = 'FailedOperation.ImageDecodeFailed'

# The image is too large.
FAILEDOPERATION_IMAGESIZETOOLARGE = 'FailedOperation.ImageSizeTooLarge'

# No complete face was detected. Please enter a complete face image.
FAILEDOPERATION_INCOMPLETEFACE = 'FailedOperation.IncompleteFace'

# Multiple faces are detected.
FAILEDOPERATION_LIFEPHOTODETECTFACES = 'FailedOperation.LifePhotoDetectFaces'

# Real person comparison failed.
FAILEDOPERATION_LIFEPHOTODETECTFAKE = 'FailedOperation.LifePhotoDetectFake'

# Failed to detect a full face.
FAILEDOPERATION_LIFEPHOTODETECTNOFACES = 'FailedOperation.LifePhotoDetectNoFaces'

# The resolution of the image passed in is too low. Please upload a new one.
FAILEDOPERATION_LIFEPHOTOPOORQUALITY = 'FailedOperation.LifePhotoPoorQuality'

# The image passed in is too large or too small.
FAILEDOPERATION_LIFEPHOTOSIZEERROR = 'FailedOperation.LifePhotoSizeError'

# The face is not fully exposed.
FAILEDOPERATION_LIPFACEINCOMPLETE = 'FailedOperation.LipFaceIncomplete'

# The lip movement range is too small.
FAILEDOPERATION_LIPMOVESMALL = 'FailedOperation.LipMoveSmall'

# Failed to pull the video. Please try again.
FAILEDOPERATION_LIPNETFAILED = 'FailedOperation.LipNetFailed'

# The video is empty or its size is inappropriate. The recording duration should be about 6 seconds.
FAILEDOPERATION_LIPSIZEERROR = 'FailedOperation.LipSizeError'

# The video format is incorrect.
FAILEDOPERATION_LIPVIDEOINVALID = 'FailedOperation.LipVideoInvalid'

# The video definition is too low.
FAILEDOPERATION_LIPVIDEOQUAILITY = 'FailedOperation.LipVideoQuaility'

# No sound is detected.
FAILEDOPERATION_LIPVOICEDETECT = 'FailedOperation.LipVoiceDetect'

# The volume of the video is too low.
FAILEDOPERATION_LIPVOICELOW = 'FailedOperation.LipVoiceLow'

# Speech recognition failed.
FAILEDOPERATION_LIPVOICERECOGNIZE = 'FailedOperation.LipVoiceRecognize'

# Face detection failed. Unable to extract the photo for comparison.
FAILEDOPERATION_LIVESSBESTFRAMEERROR = 'FailedOperation.LivessBestFrameError'

# Liveness detection failed.
FAILEDOPERATION_LIVESSDETECTFAIL = 'FailedOperation.LivessDetectFail'

# Suspected spoofed recording.
FAILEDOPERATION_LIVESSDETECTFAKE = 'FailedOperation.LivessDetectFake'

# Error calling the liveness engine API.
FAILEDOPERATION_LIVESSSYSTEMERROR = 'FailedOperation.LivessSystemError'

# Video-based real person detection failed.
FAILEDOPERATION_LIVESSUNKNOWNERROR = 'FailedOperation.LivessUnknownError'

# The image quality is too poor, please check the image quality
FAILEDOPERATION_POORIMAGEQUALITY = 'FailedOperation.PoorImageQuality'

# Real person detection failed.
FAILEDOPERATION_SILENTDETECTFAIL = 'FailedOperation.SilentDetectFail'

# Eye detection failed.
FAILEDOPERATION_SILENTEYELIVEFAIL = 'FailedOperation.SilentEyeLiveFail'

# No face is detected in the video.
FAILEDOPERATION_SILENTFACEDETECTFAIL = 'FailedOperation.SilentFaceDetectFail'

# Low face quality.
FAILEDOPERATION_SILENTFACEQUALITYFAIL = 'FailedOperation.SilentFaceQualityFail'

# A face mask is detected.
FAILEDOPERATION_SILENTFACEWITHMASKFAIL = 'FailedOperation.SilentFaceWithMaskFail'

# Mouth detection failed.
FAILEDOPERATION_SILENTMOUTHLIVEFAIL = 'FailedOperation.SilentMouthLiveFail'

# Multiple faces are detected in the video.
FAILEDOPERATION_SILENTMULTIFACEFAIL = 'FailedOperation.SilentMultiFaceFail'

# The video might be spoofed.
FAILEDOPERATION_SILENTPICTURELIVEFAIL = 'FailedOperation.SilentPictureLiveFail'

# Real person detection did not reach the passing standard.
FAILEDOPERATION_SILENTTHRESHOLD = 'FailedOperation.SilentThreshold'

# The video is too short. Please capture a video longer than 2 seconds.
FAILEDOPERATION_SILENTTOOSHORT = 'FailedOperation.SilentTooShort'

# Unknown error.
FAILEDOPERATION_UNKNOWERROR = 'FailedOperation.UnKnowError'

# Unknown internal error.
FAILEDOPERATION_UNKNOWN = 'FailedOperation.UnKnown'

# The service is not activated.
FAILEDOPERATION_UNOPENERROR = 'FailedOperation.UnOpenError'

# Video decoding abnormality
FAILEDOPERATION_VIDEODECODEFAILED = 'FailedOperation.VideoDecodeFailed'

# Internal error.
INTERNALERROR = 'InternalError'

# The lighting is too dim.
INTERNALERROR_ACTIONLIGHTDARK = 'InternalError.ActionLightDark'

# The lighting is too strong.
INTERNALERROR_ACTIONLIGHTSTRONG = 'InternalError.ActionLightStrong'

# Failed to detect a full face.
INTERNALERROR_ACTIONNODETECTFACE = 'InternalError.ActionNodetectFace'

# The similarity did not reach the passing standard.
INTERNALERROR_COMPARELOWSIMILARITY = 'InternalError.CompareLowSimilarity'

# The resolution of the image passed in is too low. Please upload a new one.
INTERNALERROR_LIFEPHOTOPOORQUALITY = 'InternalError.LifePhotoPoorQuality'

# The image passed in is too large or too small.
INTERNALERROR_LIFEPHOTOSIZEERROR = 'InternalError.LifePhotoSizeError'

# Unknown internal error.
INTERNALERROR_UNKNOWN = 'InternalError.UnKnown'

# Invalid parameter.
INVALIDPARAMETER = 'InvalidParameter'

# Image decoding failed.
INVALIDPARAMETER_ENGINEIMAGEDECODEFAILED = 'InvalidParameter.EngineImageDecodeFailed'

# Incorrect parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# BizToken expired.
INVALIDPARAMETERVALUE_BIZTOKENEXPIRED = 'InvalidParameterValue.BizTokenExpired'

# Invalid BizToken.
INVALIDPARAMETERVALUE_BIZTOKENILLEGAL = 'InvalidParameterValue.BizTokenIllegal'

# The image file content size is abnormal.
INVALIDPARAMETERVALUE_INVALIDFILECONTENTSIZE = 'InvalidParameterValue.InvalidFileContentSize'

# Parameter value is wrong.
INVALIDPARAMETERVALUE_INVALIDPARAMETERVALUELIMIT = 'InvalidParameterValue.InvalidParameterValueLimit'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# Image file download failed.
RESOURCEUNAVAILABLE_IMAGEDOWNLOADERROR = 'ResourceUnavailable.ImageDownloadError'

# The account is in arrears.
RESOURCEUNAVAILABLE_INARREARS = 'ResourceUnavailable.InArrears'

# The account has exhausted the resource package for this service.
RESOURCEUNAVAILABLE_RESOURCEPACKAGERUNOUT = 'ResourceUnavailable.ResourcePackageRunOut'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Service activation exception.
UNAUTHORIZEDOPERATION_ACTIVATEERROR = 'UnauthorizedOperation.ActivateError'

# Activating the service.
UNAUTHORIZEDOPERATION_ACTIVATING = 'UnauthorizedOperation.Activating'

# The account is in arrears.
UNAUTHORIZEDOPERATION_ARREARS = 'UnauthorizedOperation.Arrears'

# The billing status is abnormal.
UNAUTHORIZEDOPERATION_CHARGESTATUSEXCEPTION = 'UnauthorizedOperation.ChargeStatusException'

# Identity verification has not been completed for the account.
UNAUTHORIZEDOPERATION_NONAUTHORIZE = 'UnauthorizedOperation.NonAuthorize'

# The service has not been activated.
UNAUTHORIZEDOPERATION_NONACTIVATED = 'UnauthorizedOperation.Nonactivated'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
