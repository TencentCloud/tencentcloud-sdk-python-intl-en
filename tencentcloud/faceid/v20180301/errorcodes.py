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

# The first motion is not detected.
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

# Unknown internal error.
FAILEDOPERATION_UNKNOWN = 'FailedOperation.UnKnown'

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

# Invalid parameter.
INVALIDPARAMETER = 'InvalidParameter'

# Incorrect parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# The account is in arrears.
UNAUTHORIZEDOPERATION_ARREARS = 'UnauthorizedOperation.Arrears'

# Identity verification has not been completed for the account.
UNAUTHORIZEDOPERATION_NONAUTHORIZE = 'UnauthorizedOperation.NonAuthorize'

# The service has not been activated.
UNAUTHORIZEDOPERATION_NONACTIVATED = 'UnauthorizedOperation.Nonactivated'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
