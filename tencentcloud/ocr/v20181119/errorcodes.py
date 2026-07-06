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


# The CardSide type of the ID card is incorrect.
FAILEDOPERATION_CARDSIDEERROR = 'FailedOperation.CardSideError'

# Failed to download the file.
FAILEDOPERATION_DOWNLOADERROR = 'FailedOperation.DownLoadError'

# The image is empty.
FAILEDOPERATION_EMPTYIMAGEERROR = 'FailedOperation.EmptyImageError'

# Recognition by the engine timed out.
FAILEDOPERATION_ENGINERECOGNIZETIMEOUT = 'FailedOperation.EngineRecognizeTimeout'

# The field value does not meet expectations.
FAILEDOPERATION_FIELDEXCEPTION = 'FailedOperation.FieldException'

# The ID card information (ID number, name, etc.) is invalid.
FAILEDOPERATION_IDCARDINFOILLEGAL = 'FailedOperation.IdCardInfoIllegal'

# The resolution of the image is too low or the proportion of the ID card in the image is too small.
FAILEDOPERATION_IDCARDTOOSMALL = 'FailedOperation.IdCardTooSmall'

# The image is blurry.
FAILEDOPERATION_IMAGEBLUR = 'FailedOperation.ImageBlur'

# Failed to decode the image.
FAILEDOPERATION_IMAGEDECODEFAILED = 'FailedOperation.ImageDecodeFailed'

# No ID card is detected in the image.
FAILEDOPERATION_IMAGENOIDCARD = 'FailedOperation.ImageNoIdCard'

# The card in the image is not of the specified type.
FAILEDOPERATION_IMAGENOSPECIFIEDCARD = 'FailedOperation.ImageNoSpecifiedCard'

# No text is detected in the image.
FAILEDOPERATION_IMAGENOTEXT = 'FailedOperation.ImageNoText'

# The image size exceeds the limit. Refer to the image size constraints in the input parameter description.
FAILEDOPERATION_IMAGESIZETOOLARGE = 'FailedOperation.ImageSizeTooLarge'

# The information in the visual zone does not match that in the machine-readable zone.
FAILEDOPERATION_INCONSISTENCYBETWEENMRZANDVRZ = 'FailedOperation.InconsistencyBetweenMRZAndVRZ'

# The length of the postal code recognized from the Malaysian ID card is incorrect.
FAILEDOPERATION_INVALIDPOSTALCODELENGTH = 'FailedOperation.InvalidPostalCodeLength'

# Large model service invocation failed. Try again later.
FAILEDOPERATION_LLMSERVICEFAILED = 'FailedOperation.LLMServiceFailed'

# The input language is not supported.
FAILEDOPERATION_LANGUAGENOTSUPPORT = 'FailedOperation.LanguageNotSupport'

# Multiple cards of the same side are detected in the image. Please upload an image with a single side or one front and one back side.
FAILEDOPERATION_MULTICARDERROR = 'FailedOperation.MultiCardError'

# Not a Hong Kong identity card.
FAILEDOPERATION_NOHKIDCARD = 'FailedOperation.NoHKIDCard'

# The image does not contain a Malaysian ID card.
FAILEDOPERATION_NOMASIDCARD = 'FailedOperation.NoMASIDCard'

# Not a passport.
FAILEDOPERATION_NOPASSPORT = 'FailedOperation.NoPassport'

# OCR recognition failed. This error may be caused by unstable network connections, service anomalies, or other issues.
FAILEDOPERATION_OCRFAILED = 'FailedOperation.OcrFailed'

# Unknown error.
FAILEDOPERATION_UNKNOWERROR = 'FailedOperation.UnKnowError'

# Unknown file type.
FAILEDOPERATION_UNKNOWFILETYPEERROR = 'FailedOperation.UnKnowFileTypeError'

# The service has not been activated.
FAILEDOPERATION_UNOPENERROR = 'FailedOperation.UnOpenError'

# The general warning service encountered an exception.
FAILEDOPERATION_WARNINGSERVICEFAILED = 'FailedOperation.WarningServiceFailed'

# Config is not in valid JSON format.
INVALIDPARAMETER_CONFIGFORMATERROR = 'InvalidParameter.ConfigFormatError'

# Image decoding failed.
INVALIDPARAMETER_ENGINEIMAGEDECODEFAILED = 'InvalidParameter.EngineImageDecodeFailed'

# The image file size is invalid or exceeds the allowed limit.
INVALIDPARAMETERVALUE_INVALIDFILECONTENTSIZE = 'InvalidParameterValue.InvalidFileContentSize'

# Incorrect parameter value.
INVALIDPARAMETERVALUE_INVALIDPARAMETERVALUELIMIT = 'InvalidParameterValue.InvalidParameterValueLimit'

# The file size exceeds the limit
LIMITEXCEEDED_TOOLARGEFILEERROR = 'LimitExceeded.TooLargeFileError'

# Image file download failed.
RESOURCEUNAVAILABLE_IMAGEDOWNLOADERROR = 'ResourceUnavailable.ImageDownloadError'

# The account has insufficient balance.
RESOURCEUNAVAILABLE_INARREARS = 'ResourceUnavailable.InArrears'

# The resource package has been exhausted.
RESOURCEUNAVAILABLE_RESOURCEPACKAGERUNOUT = 'ResourceUnavailable.ResourcePackageRunOut'

# The billing status is abnormal.
RESOURCESSOLDOUT_CHARGESTATUSEXCEPTION = 'ResourcesSoldOut.ChargeStatusException'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'
