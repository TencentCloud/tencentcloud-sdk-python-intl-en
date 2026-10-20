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


# Authentication fail.
AUTHFAILURE_INVALIDAUTHORIZATION = 'AuthFailure.InvalidAuthorization'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# This operation cannot be performed across algorithm model versions.
FAILEDOPERATION_ACROSSVERSIONSERROR = 'FailedOperation.AcrossVersionsError'

# Comparison failed.
FAILEDOPERATION_COMPAREFAIL = 'FailedOperation.CompareFail'

# Operation conflict. Do not operate the same Person at the same time.
FAILEDOPERATION_CONFLICTOPERATION = 'FailedOperation.ConflictOperation'

# Faces cannot be added concurrently.
FAILEDOPERATION_CREATEFACECONCURRENT = 'FailedOperation.CreateFaceConcurrent'

# Custom description fields in the same person library cannot be repeated.
FAILEDOPERATION_DUPLICATEDGROUPDESCRIPTION = 'FailedOperation.DuplicatedGroupDescription'

# The face image quality does not meet the requirement.
FAILEDOPERATION_FACEQUALITYNOTQUALIFIED = 'FailedOperation.FaceQualityNotQualified'

# Face frame size is less than the MinFaceSize setting, and the human face is filtered.
FAILEDOPERATION_FACESIZETOOSMALL = 'FailedOperation.FaceSizeTooSmall'

# The current group is being deleted. Please wait.
FAILEDOPERATION_GROUPINDELETEDSTATE = 'FailedOperation.GroupInDeletedState'

# The group already contains the corresponding personnel Id.
FAILEDOPERATION_GROUPPERSONMAPEXIST = 'FailedOperation.GroupPersonMapExist'

# The group does not include the corresponding personnel Id.
FAILEDOPERATION_GROUPPERSONMAPNOTEXIST = 'FailedOperation.GroupPersonMapNotExist'

# Image decoding failed.
FAILEDOPERATION_IMAGEDECODEFAILED = 'FailedOperation.ImageDecodeFailed'

# Image download error.
FAILEDOPERATION_IMAGEDOWNLOADERROR = 'FailedOperation.ImageDownloadError'

# Face detection failed.
FAILEDOPERATION_IMAGEFACEDETECTFAILED = 'FailedOperation.ImageFacedetectFailed'

# The image resolution is too high.
FAILEDOPERATION_IMAGERESOLUTIONEXCEED = 'FailedOperation.ImageResolutionExceed'

# The short edge resolution of the image is lower than 64 pixels.
FAILEDOPERATION_IMAGERESOLUTIONTOOSMALL = 'FailedOperation.ImageResolutionTooSmall'

# The size of the image after base64 encoding cannot exceed 5 MB.
FAILEDOPERATION_IMAGESIZEEXCEED = 'FailedOperation.ImageSizeExceed'

# Multiple faces detected.
FAILEDOPERATION_LIFEPHOTODETECTFACES = 'FailedOperation.LifePhotoDetectFaces'

# Real person comparison failed.
FAILEDOPERATION_LIFEPHOTODETECTFAKE = 'FailedOperation.LifePhotoDetectFake'

# Full face not detected.
FAILEDOPERATION_LIFEPHOTODETECTNOFACES = 'FailedOperation.LifePhotoDetectNoFaces'

# Uploaded image too large or too small.
FAILEDOPERATION_LIFEPHOTOSIZEERROR = 'FailedOperation.LifePhotoSizeError'

# Request frequency exceeds the limit.
FAILEDOPERATION_REQUESTLIMITEXCEEDED = 'FailedOperation.RequestLimitExceeded'

# The backend service timed out.
FAILEDOPERATION_REQUESTTIMEOUT = 'FailedOperation.RequestTimeout'

# Rpc call failed.
FAILEDOPERATION_RPCFAIL = 'FailedOperation.RpcFail'

# The number of retrieved human faces exceeds the limit.
FAILEDOPERATION_SEARCHFACESEXCEED = 'FailedOperation.SearchFacesExceed'

# Algorithm service exception. Retry.
FAILEDOPERATION_SERVERERROR = 'FailedOperation.ServerError'

# Internal error.
FAILEDOPERATION_UNKNOWERROR = 'FailedOperation.UnKnowError'

# Internal error.
INTERNALERROR = 'InternalError'

# Invalid parameters.
INVALIDPARAMETER_INVALIDPARAMETER = 'InvalidParameter.InvalidParameter'

# Number of faces in the account exceeds the limit.
INVALIDPARAMETERVALUE_ACCOUNTFACENUMEXCEED = 'InvalidParameterValue.AccountFaceNumExceed'

# The number of faces to delete exceeds the limit. Each person must contain at least one face.
INVALIDPARAMETERVALUE_DELETEFACENUMEXCEED = 'InvalidParameterValue.DeleteFaceNumExceed'

# Invalid `FaceMatchThreshold` parameter.
INVALIDPARAMETERVALUE_FACEMATCHTHRESHOLDILLEGAL = 'InvalidParameterValue.FaceMatchThresholdIllegal'

# Invalid algorithm model version.
INVALIDPARAMETERVALUE_FACEMODELVERSIONILLEGAL = 'InvalidParameterValue.FaceModelVersionIllegal'

# The person library customized description field array exceeds the length limit. You can create up to 5.
INVALIDPARAMETERVALUE_GROUPEXDESCRIPTIONSEXCEED = 'InvalidParameterValue.GroupExDescriptionsExceed'

# The custom description field name in the person library cannot be repeated.
INVALIDPARAMETERVALUE_GROUPEXDESCRIPTIONSNAMEIDENTICAL = 'InvalidParameterValue.GroupExDescriptionsNameIdentical'

# The custom description field name of the personnel database contains invalid characters. It can only contain Chinese and English characters, -, _, and digits.
INVALIDPARAMETERVALUE_GROUPEXDESCRIPTIONSNAMEILLEGAL = 'InvalidParameterValue.GroupExDescriptionsNameIllegal'

# Personnel library custom description field name length exceeds the limit.
INVALIDPARAMETERVALUE_GROUPEXDESCRIPTIONSNAMETOOLONG = 'InvalidParameterValue.GroupExDescriptionsNameTooLong'

# The number of faces in the person library exceeds the limit.
INVALIDPARAMETERVALUE_GROUPFACENUMEXCEED = 'InvalidParameterValue.GroupFaceNumExceed'

# Personnel database ID already exists. Personnel database ID cannot be repeated.
INVALIDPARAMETERVALUE_GROUPIDALREADYEXIST = 'InvalidParameterValue.GroupIdAlreadyExist'

# The personnel database ID contains invalid characters. The personnel database ID supports only English, digits, -%@#&_.
INVALIDPARAMETERVALUE_GROUPIDILLEGAL = 'InvalidParameterValue.GroupIdIllegal'

# Personnel database ID does not exist.
INVALIDPARAMETERVALUE_GROUPIDNOTEXIST = 'InvalidParameterValue.GroupIdNotExist'

# The corresponding group ID does not exist.
INVALIDPARAMETERVALUE_GROUPIDNOTEXISTS = 'InvalidParameterValue.GroupIdNotExists'

# Personnel database ID exceeds the length limit.
INVALIDPARAMETERVALUE_GROUPIDTOOLONG = 'InvalidParameterValue.GroupIdTooLong'

# The incoming personnel library list exceeds the limit.
INVALIDPARAMETERVALUE_GROUPIDSEXCEED = 'InvalidParameterValue.GroupIdsExceed'

# Person library name already exists. Person library name should be unique.
INVALIDPARAMETERVALUE_GROUPNAMEALREADYEXIST = 'InvalidParameterValue.GroupNameAlreadyExist'

# The personnel database name contains invalid characters. It can only contain Chinese and English characters, -, _, and digits.
INVALIDPARAMETERVALUE_GROUPNAMEILLEGAL = 'InvalidParameterValue.GroupNameIllegal'

# Personnel database name exceeds the length limit.
INVALIDPARAMETERVALUE_GROUPNAMETOOLONG = 'InvalidParameterValue.GroupNameTooLong'

# The number of person libraries exceeds the limit. To add more, contact us.
INVALIDPARAMETERVALUE_GROUPNUMEXCEED = 'InvalidParameterValue.GroupNumExceed'

# The number of person libraries exceeds the limit. A single person can be added to up to 100 person libraries.
INVALIDPARAMETERVALUE_GROUPNUMPERPERSONEXCEED = 'InvalidParameterValue.GroupNumPerPersonExceed'

# Personnel database remarks contain invalid characters. Personnel database remarks only support Chinese, English, -, _, and digits.
INVALIDPARAMETERVALUE_GROUPTAGILLEGAL = 'InvalidParameterValue.GroupTagIllegal'

# Personnel database remarks exceed the length limit.
INVALIDPARAMETERVALUE_GROUPTAGTOOLONG = 'InvalidParameterValue.GroupTagTooLong'

# No image is input.
INVALIDPARAMETERVALUE_IMAGEEMPTY = 'InvalidParameterValue.ImageEmpty'

# Empty image.
INVALIDPARAMETERVALUE_IMAGEEMPTYERROR = 'InvalidParameterValue.ImageEmptyError'

# Number of returns exceeds the limit.
INVALIDPARAMETERVALUE_LIMITEXCEED = 'InvalidParameterValue.LimitExceed'

# No human face in the specified group.
INVALIDPARAMETERVALUE_NOFACEINGROUPS = 'InvalidParameterValue.NoFaceInGroups'

# The image contains no human face.
INVALIDPARAMETERVALUE_NOFACEINPHOTO = 'InvalidParameterValue.NoFaceInPhoto'

# Starting number is too large. Please check the required length of the array.
INVALIDPARAMETERVALUE_OFFSETEXCEED = 'InvalidParameterValue.OffsetExceed'

# The customized description field array exceeds the length limit. Up to 5.
INVALIDPARAMETERVALUE_PERSONEXDESCRIPTIONINFOSEXCEED = 'InvalidParameterValue.PersonExDescriptionInfosExceed'

# The custom description field name of a person cannot be repeated.
INVALIDPARAMETERVALUE_PERSONEXDESCRIPTIONSNAMEIDENTICAL = 'InvalidParameterValue.PersonExDescriptionsNameIdentical'

# The custom description field name contains invalid characters. The custom description field name supports only Chinese, English, -, _, and digits.
INVALIDPARAMETERVALUE_PERSONEXDESCRIPTIONSNAMEILLEGAL = 'InvalidParameterValue.PersonExDescriptionsNameIllegal'

# Person custom description field name length exceeds the limit.
INVALIDPARAMETERVALUE_PERSONEXDESCRIPTIONSNAMETOOLONG = 'InvalidParameterValue.PersonExDescriptionsNameTooLong'

# The group already contains the corresponding personnel Id.
INVALIDPARAMETERVALUE_PERSONEXISTINGROUP = 'InvalidParameterValue.PersonExistInGroup'

# The number of faces for a single person exceeds the limit. A single person can contain up to five faces.
INVALIDPARAMETERVALUE_PERSONFACENUMEXCEED = 'InvalidParameterValue.PersonFaceNumExceed'

# Error in gender of personnel settings. 0 represents empty, 1 represents man, 2 represents woman.
INVALIDPARAMETERVALUE_PERSONGENDERILLEGAL = 'InvalidParameterValue.PersonGenderIllegal'

# Person ID already exists. Person ID should be unique.
INVALIDPARAMETERVALUE_PERSONIDALREADYEXIST = 'InvalidParameterValue.PersonIdAlreadyExist'

# The person ID contains invalid characters. The person ID supports only English, digits, -%@#&_.
INVALIDPARAMETERVALUE_PERSONIDILLEGAL = 'InvalidParameterValue.PersonIdIllegal'

# Personnel ID does not exist.
INVALIDPARAMETERVALUE_PERSONIDNOTEXIST = 'InvalidParameterValue.PersonIdNotExist'

# Person ID exceeds the length limit.
INVALIDPARAMETERVALUE_PERSONIDTOOLONG = 'InvalidParameterValue.PersonIdTooLong'

# The person name contains invalid characters. It can only contain Chinese and English characters, -, _, and digits.
INVALIDPARAMETERVALUE_PERSONNAMEILLEGAL = 'InvalidParameterValue.PersonNameIllegal'

# Person name exceeds the length limit.
INVALIDPARAMETERVALUE_PERSONNAMETOOLONG = 'InvalidParameterValue.PersonNameTooLong'

# Invalid `QualityControl` parameter.
INVALIDPARAMETERVALUE_QUALITYCONTROLILLEGAL = 'InvalidParameterValue.QualityControlIllegal'

# The number of personnel found exceeds the limit.
INVALIDPARAMETERVALUE_SEARCHPERSONSEXCEED = 'InvalidParameterValue.SearchPersonsExceed'

# Invalid `UniquePersonControl` parameter.
INVALIDPARAMETERVALUE_UNIQUEPERSONCONTROLILLEGAL = 'InvalidParameterValue.UniquePersonControlIllegal'

# This operation is not supported by algorithm model v2.0 or below.
INVALIDPARAMETERVALUE_UNSUPPORTEDGROUPFACEMODELVERSION = 'InvalidParameterValue.UnsupportedGroupFaceModelVersion'

# Upload up to four human faces.
INVALIDPARAMETERVALUE_UPLOADFACENUMEXCEED = 'InvalidParameterValue.UploadFaceNumExceed'

# The URL format is invalid.
INVALIDPARAMETERVALUE_URLILLEGAL = 'InvalidParameterValue.UrlIllegal'

# The quota limit is reached.
LIMITEXCEEDED = 'LimitExceeded'

# The number of human faces exceeds the limit.
LIMITEXCEEDED_ERRORFACENUMEXCEED = 'LimitExceeded.ErrorFaceNumExceed'

# The required parameter is empty.
MISSINGPARAMETER_ERRORPARAMETEREMPTY = 'MissingParameter.ErrorParameterEmpty'

# The account is in arrears.
RESOURCEUNAVAILABLE_CHARGESTATUSEXCEPTION = 'ResourceUnavailable.ChargeStatusException'

# The resource is being delivered.
RESOURCEUNAVAILABLE_DELIVERING = 'ResourceUnavailable.Delivering'

# The account has been frozen.
RESOURCEUNAVAILABLE_FREEZE = 'ResourceUnavailable.Freeze'

# Failed to get the authentication information.
RESOURCEUNAVAILABLE_GETAUTHINFOERROR = 'ResourceUnavailable.GetAuthInfoError'

# The account is in arrears.
RESOURCEUNAVAILABLE_INARREARS = 'ResourceUnavailable.InArrears'

# Insufficient balance.
RESOURCEUNAVAILABLE_LOWBALANCE = 'ResourceUnavailable.LowBalance'

# The billing status is unknown. Check whether the service has been activated in the console.
RESOURCEUNAVAILABLE_NOTEXIST = 'ResourceUnavailable.NotExist'

# The service is not activated.
RESOURCEUNAVAILABLE_NOTREADY = 'ResourceUnavailable.NotReady'

# The resource has been possessed.
RESOURCEUNAVAILABLE_RECOVER = 'ResourceUnavailable.Recover'

# Services for the account has been stopped.
RESOURCEUNAVAILABLE_STOPUSING = 'ResourceUnavailable.StopUsing'

# The billing status is unknown.
RESOURCEUNAVAILABLE_UNKNOWNSTATUS = 'ResourceUnavailable.UnknownStatus'

# The billing status is abnormal.
RESOURCESSOLDOUT_CHARGESTATUSEXCEPTION = 'ResourcesSoldOut.ChargeStatusException'

# The method name is unknown.
UNSUPPORTEDOPERATION_UNKNOWMETHOD = 'UnsupportedOperation.UnknowMethod'
