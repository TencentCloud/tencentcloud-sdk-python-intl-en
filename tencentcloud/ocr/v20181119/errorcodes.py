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


# The CardSide type of the ID card is incorrect.
FAILEDOPERATION_CARDSIDEERROR = 'FailedOperation.CardSideError'

# File download failed.
FAILEDOPERATION_DOWNLOADERROR = 'FailedOperation.DownLoadError'

# The image is empty.
FAILEDOPERATION_EMPTYIMAGEERROR = 'FailedOperation.EmptyImageError'

# Recognition by the engine timed out.
FAILEDOPERATION_ENGINERECOGNIZETIMEOUT = 'FailedOperation.EngineRecognizeTimeout'

# 
FAILEDOPERATION_FIELDEXCEPTION = 'FailedOperation.FieldException'

# The ID card information (ID number, name, etc.) is invalid.
FAILEDOPERATION_IDCARDINFOILLEGAL = 'FailedOperation.IdCardInfoIllegal'

# The resolution of the image is too low or the proportion of the ID card in the image is too small.
FAILEDOPERATION_IDCARDTOOSMALL = 'FailedOperation.IdCardTooSmall'

# Invalid bank card information.
FAILEDOPERATION_ILLEGALBANKCARDERROR = 'FailedOperation.IllegalBankCardError'

# The image is blurry.
FAILEDOPERATION_IMAGEBLUR = 'FailedOperation.ImageBlur'

# Image decoding failed.
FAILEDOPERATION_IMAGEDECODEFAILED = 'FailedOperation.ImageDecodeFailed'

# No ID card is detected in the image.
FAILEDOPERATION_IMAGENOIDCARD = 'FailedOperation.ImageNoIdCard'

# The card in the image is not of the specified type.
FAILEDOPERATION_IMAGENOSPECIFIEDCARD = 'FailedOperation.ImageNoSpecifiedCard'

# No text is detected in the image.
FAILEDOPERATION_IMAGENOTEXT = 'FailedOperation.ImageNoText'

# The image is too large. Please see the description of image size limit in the output parameters.
FAILEDOPERATION_IMAGESIZETOOLARGE = 'FailedOperation.ImageSizeTooLarge'

# 
FAILEDOPERATION_INCONSISTENCYBETWEENMRZANDVRZ = 'FailedOperation.InconsistencyBetweenMRZAndVRZ'

# The input language is not supported.
FAILEDOPERATION_LANGUAGENOTSUPPORT = 'FailedOperation.LanguageNotSupport'

# There are multiple cards in the photo.
FAILEDOPERATION_MULTICARDERROR = 'FailedOperation.MultiCardError'

# No bank card found.
FAILEDOPERATION_NOBANKCARDERROR = 'FailedOperation.NoBankCardError'

# Not a Hong Kong identity card.
FAILEDOPERATION_NOHKIDCARD = 'FailedOperation.NoHKIDCard'

# Non-Malaysian ID cards.
FAILEDOPERATION_NOMASIDCARD = 'FailedOperation.NoMASIDCard'

# Not a passport.
FAILEDOPERATION_NOPASSPORT = 'FailedOperation.NoPassport'

# OCR failed. This error may be caused by unstable network connections,service anomalies or other issues.
FAILEDOPERATION_OCRFAILED = 'FailedOperation.OcrFailed'

# Unknown error.
FAILEDOPERATION_UNKNOWERROR = 'FailedOperation.UnKnowError'

# The service is not activated.
FAILEDOPERATION_UNOPENERROR = 'FailedOperation.UnOpenError'

# Warning service error.
FAILEDOPERATION_WARNINGSERVICEFAILED = 'FailedOperation.WarningServiceFailed'

# Config is not in valid JSON format.
INVALIDPARAMETER_CONFIGFORMATERROR = 'InvalidParameter.ConfigFormatError'

# Image decoding failed.
INVALIDPARAMETER_ENGINEIMAGEDECODEFAILED = 'InvalidParameter.EngineImageDecodeFailed'

# Incorrect parameter value.
INVALIDPARAMETERVALUE_INVALIDPARAMETERVALUELIMIT = 'InvalidParameterValue.InvalidParameterValueLimit'

# The file is too large.
LIMITEXCEEDED_TOOLARGEFILEERROR = 'LimitExceeded.TooLargeFileError'

# The account is in arrears.
RESOURCEUNAVAILABLE_INARREARS = 'ResourceUnavailable.InArrears'

# The account resource package is exhausted.
RESOURCEUNAVAILABLE_RESOURCEPACKAGERUNOUT = 'ResourceUnavailable.ResourcePackageRunOut'

# Exceptional billing status.
RESOURCESSOLDOUT_CHARGESTATUSEXCEPTION = 'ResourcesSoldOut.ChargeStatusException'

# Unrecognized argument.
UNKNOWNPARAMETER = 'UnknownParameter'
