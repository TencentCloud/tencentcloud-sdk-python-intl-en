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


# Authentication failed.
AUTHFAILURE_INVALIDAUTHORIZATION = 'AuthFailure.InvalidAuthorization'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# This operation cannot be performed across algorithm model versions.
FAILEDOPERATION_ACROSSVERSIONSERROR = 'FailedOperation.AcrossVersionsError'

# The operations conflict. Do not operate on the same person simultaneously.
FAILEDOPERATION_CONFLICTOPERATION = 'FailedOperation.ConflictOperation'

# Faces cannot be added concurrently.
FAILEDOPERATION_CREATEFACECONCURRENT = 'FailedOperation.CreateFaceConcurrent'

# The custom description field must be unique in the group.
FAILEDOPERATION_DUPLICATEDGROUPDESCRIPTION = 'FailedOperation.DuplicatedGroupDescription'

# The face image quality does not meet the requirement.
FAILEDOPERATION_FACEQUALITYNOTQUALIFIED = 'FailedOperation.FaceQualityNotQualified'

# The face frame size is smaller than the `MinFaceSize` value, and the face is filtered out.
FAILEDOPERATION_FACESIZETOOSMALL = 'FailedOperation.FaceSizeTooSmall'

# The current group is being deleted. Please wait.
FAILEDOPERATION_GROUPINDELETEDSTATE = 'FailedOperation.GroupInDeletedState'

# The ID of the corresponding person is already in the group.
FAILEDOPERATION_GROUPPERSONMAPEXIST = 'FailedOperation.GroupPersonMapExist'

# The ID of the corresponding person is not in the group.
FAILEDOPERATION_GROUPPERSONMAPNOTEXIST = 'FailedOperation.GroupPersonMapNotExist'

# Image decoding failed.
FAILEDOPERATION_IMAGEDECODEFAILED = 'FailedOperation.ImageDecodeFailed'

# An error occurred while downloading the image.
FAILEDOPERATION_IMAGEDOWNLOADERROR = 'FailedOperation.ImageDownloadError'

# Face detection failed.
FAILEDOPERATION_IMAGEFACEDETECTFAILED = 'FailedOperation.ImageFacedetectFailed'

# The image resolution is too high.
FAILEDOPERATION_IMAGERESOLUTIONEXCEED = 'FailedOperation.ImageResolutionExceed'

# The image short edge resolution is smaller than 64.
FAILEDOPERATION_IMAGERESOLUTIONTOOSMALL = 'FailedOperation.ImageResolutionTooSmall'

# The size of the Base64-encoded image cannot exceed 5 MB.
FAILEDOPERATION_IMAGESIZEEXCEED = 'FailedOperation.ImageSizeExceed'

# The request frequency exceeds the limit.
FAILEDOPERATION_REQUESTLIMITEXCEEDED = 'FailedOperation.RequestLimitExceeded'

# The backend service timed out.
FAILEDOPERATION_REQUESTTIMEOUT = 'FailedOperation.RequestTimeout'

# The number of faces searched for exceeds the limit.
FAILEDOPERATION_SEARCHFACESEXCEED = 'FailedOperation.SearchFacesExceed'

# The algorithm service is exceptional. Please retry.
FAILEDOPERATION_SERVERERROR = 'FailedOperation.ServerError'

# Internal error.
INTERNALERROR = 'InternalError'

# Invalid parameter.
INVALIDPARAMETER_INVALIDPARAMETER = 'InvalidParameter.InvalidParameter'

# The number of faces in the account exceeds the limit.
INVALIDPARAMETERVALUE_ACCOUNTFACENUMEXCEED = 'InvalidParameterValue.AccountFaceNumExceed'

# The number of faces to be deleted exceeds the limit. Every person must have at least one face image.
INVALIDPARAMETERVALUE_DELETEFACENUMEXCEED = 'InvalidParameterValue.DeleteFaceNumExceed'

# Invalid `FaceMatchThreshold` parameter.
INVALIDPARAMETERVALUE_FACEMATCHTHRESHOLDILLEGAL = 'InvalidParameterValue.FaceMatchThresholdIllegal'

# The algorithm model version is invalid.
INVALIDPARAMETERVALUE_FACEMODELVERSIONILLEGAL = 'InvalidParameterValue.FaceModelVersionIllegal'

# The array length of the group's custom description fields exceeds the limit. Up to 5 fields can be created.
INVALIDPARAMETERVALUE_GROUPEXDESCRIPTIONSEXCEED = 'InvalidParameterValue.GroupExDescriptionsExceed'

# The name of the group's custom description field must be unique.
INVALIDPARAMETERVALUE_GROUPEXDESCRIPTIONSNAMEIDENTICAL = 'InvalidParameterValue.GroupExDescriptionsNameIdentical'

# The name of the group's custom description field contains invalid characters. It can contain only letters, `-`, `_`, and digits.
INVALIDPARAMETERVALUE_GROUPEXDESCRIPTIONSNAMEILLEGAL = 'InvalidParameterValue.GroupExDescriptionsNameIllegal'

# The name of the group's custom description field exceeds the length limit.
INVALIDPARAMETERVALUE_GROUPEXDESCRIPTIONSNAMETOOLONG = 'InvalidParameterValue.GroupExDescriptionsNameTooLong'

# The number of faces in the group exceeds the limit.
INVALIDPARAMETERVALUE_GROUPFACENUMEXCEED = 'InvalidParameterValue.GroupFaceNumExceed'

# The group ID already exists. It must be unique.
INVALIDPARAMETERVALUE_GROUPIDALREADYEXIST = 'InvalidParameterValue.GroupIdAlreadyExist'

# The group ID contains invalid characters. It can contain only letters, digits, and special symbols (-%@#&_).
INVALIDPARAMETERVALUE_GROUPIDILLEGAL = 'InvalidParameterValue.GroupIdIllegal'

# The group ID does not exist.
INVALIDPARAMETERVALUE_GROUPIDNOTEXIST = 'InvalidParameterValue.GroupIdNotExist'

# The corresponding group ID does not exist.
INVALIDPARAMETERVALUE_GROUPIDNOTEXISTS = 'InvalidParameterValue.GroupIdNotExists'

# The group ID exceeds the length limit.
INVALIDPARAMETERVALUE_GROUPIDTOOLONG = 'InvalidParameterValue.GroupIdTooLong'

# The list of groups passed in exceeds the limit.
INVALIDPARAMETERVALUE_GROUPIDSEXCEED = 'InvalidParameterValue.GroupIdsExceed'

# The group name already exists. It must be unique.
INVALIDPARAMETERVALUE_GROUPNAMEALREADYEXIST = 'InvalidParameterValue.GroupNameAlreadyExist'

# The group name contains invalid characters. It can contain only letters, `-`, `_`, and digits.
INVALIDPARAMETERVALUE_GROUPNAMEILLEGAL = 'InvalidParameterValue.GroupNameIllegal'

# The group name exceeds the length limit.
INVALIDPARAMETERVALUE_GROUPNAMETOOLONG = 'InvalidParameterValue.GroupNameTooLong'

# The number of groups exceeds the limit. If you need more, please contact us.
INVALIDPARAMETERVALUE_GROUPNUMEXCEED = 'InvalidParameterValue.GroupNumExceed'

# The number of groups exceeds the limit. One person can be added to up to 100 groups.
INVALIDPARAMETERVALUE_GROUPNUMPERPERSONEXCEED = 'InvalidParameterValue.GroupNumPerPersonExceed'

# The group remarks field contains invalid characters. It can contain only letters, `-`, `_`, and digits.
INVALIDPARAMETERVALUE_GROUPTAGILLEGAL = 'InvalidParameterValue.GroupTagIllegal'

# The group remarks field exceeds the length limit.
INVALIDPARAMETERVALUE_GROUPTAGTOOLONG = 'InvalidParameterValue.GroupTagTooLong'

# Empty image.
INVALIDPARAMETERVALUE_IMAGEEMPTY = 'InvalidParameterValue.ImageEmpty'

# Empty image.
INVALIDPARAMETERVALUE_IMAGEEMPTYERROR = 'InvalidParameterValue.ImageEmptyError'

# The number of returned results exceeds the limit.
INVALIDPARAMETERVALUE_LIMITEXCEED = 'InvalidParameterValue.LimitExceed'

# There are no faces in the specified group.
INVALIDPARAMETERVALUE_NOFACEINGROUPS = 'InvalidParameterValue.NoFaceInGroups'

# There are no faces in the image.
INVALIDPARAMETERVALUE_NOFACEINPHOTO = 'InvalidParameterValue.NoFaceInPhoto'

# The starting number is too large. Please check the length of the array to be requested.
INVALIDPARAMETERVALUE_OFFSETEXCEED = 'InvalidParameterValue.OffsetExceed'

# The array length of the person's custom description fields exceeds the limit. Up to 5 fields are allowed.
INVALIDPARAMETERVALUE_PERSONEXDESCRIPTIONINFOSEXCEED = 'InvalidParameterValue.PersonExDescriptionInfosExceed'

# The name of the person's custom description field must be unique.
INVALIDPARAMETERVALUE_PERSONEXDESCRIPTIONSNAMEIDENTICAL = 'InvalidParameterValue.PersonExDescriptionsNameIdentical'

# The name of the person's custom description field contains invalid characters. It can contain only letters, `-`, `_`, and digits.
INVALIDPARAMETERVALUE_PERSONEXDESCRIPTIONSNAMEILLEGAL = 'InvalidParameterValue.PersonExDescriptionsNameIllegal'

# The name of the person's custom description field exceeds the length limit.
INVALIDPARAMETERVALUE_PERSONEXDESCRIPTIONSNAMETOOLONG = 'InvalidParameterValue.PersonExDescriptionsNameTooLong'

# The ID of the corresponding person is already in the group.
INVALIDPARAMETERVALUE_PERSONEXISTINGROUP = 'InvalidParameterValue.PersonExistInGroup'

# The number of face images for the person exceeds the limit. One person can have up to 5 face images.
INVALIDPARAMETERVALUE_PERSONFACENUMEXCEED = 'InvalidParameterValue.PersonFaceNumExceed'

# An error occurred while setting person gender. 0: empty; 1: male; 2: female.
INVALIDPARAMETERVALUE_PERSONGENDERILLEGAL = 'InvalidParameterValue.PersonGenderIllegal'

# The person ID already exists. It must be unique.
INVALIDPARAMETERVALUE_PERSONIDALREADYEXIST = 'InvalidParameterValue.PersonIdAlreadyExist'

# The person ID contains invalid characters. It can contain only letters, digits, and -%@#&_.
INVALIDPARAMETERVALUE_PERSONIDILLEGAL = 'InvalidParameterValue.PersonIdIllegal'

# The person ID does not exist.
INVALIDPARAMETERVALUE_PERSONIDNOTEXIST = 'InvalidParameterValue.PersonIdNotExist'

# The person ID field exceeds the length limit.
INVALIDPARAMETERVALUE_PERSONIDTOOLONG = 'InvalidParameterValue.PersonIdTooLong'

# The person name contains invalid characters. It can contain only letters, `-`, `_`, and digits.
INVALIDPARAMETERVALUE_PERSONNAMEILLEGAL = 'InvalidParameterValue.PersonNameIllegal'

# The person name exceeds the length limit.
INVALIDPARAMETERVALUE_PERSONNAMETOOLONG = 'InvalidParameterValue.PersonNameTooLong'

# Invalid `QualityControl` parameter.
INVALIDPARAMETERVALUE_QUALITYCONTROLILLEGAL = 'InvalidParameterValue.QualityControlIllegal'

# The number of persons searched for exceeds the limit.
INVALIDPARAMETERVALUE_SEARCHPERSONSEXCEED = 'InvalidParameterValue.SearchPersonsExceed'

# Invalid `UniquePersonControl` parameter.
INVALIDPARAMETERVALUE_UNIQUEPERSONCONTROLILLEGAL = 'InvalidParameterValue.UniquePersonControlIllegal'

# This operation is not supported by algorithm model v2.0 or below.
INVALIDPARAMETERVALUE_UNSUPPORTEDGROUPFACEMODELVERSION = 'InvalidParameterValue.UnsupportedGroupFaceModelVersion'

# Up to four faces can be uploaded at a time.
INVALIDPARAMETERVALUE_UPLOADFACENUMEXCEED = 'InvalidParameterValue.UploadFaceNumExceed'

# Invalid URL format.
INVALIDPARAMETERVALUE_URLILLEGAL = 'InvalidParameterValue.UrlIllegal'

# The number of faces exceeds the limit.
LIMITEXCEEDED_ERRORFACENUMEXCEED = 'LimitExceeded.ErrorFaceNumExceed'

# A required parameter is empty.
MISSINGPARAMETER_ERRORPARAMETEREMPTY = 'MissingParameter.ErrorParameterEmpty'

# The account is in arrears.
RESOURCEUNAVAILABLE_CHARGESTATUSEXCEPTION = 'ResourceUnavailable.ChargeStatusException'

# The resource is being shipped.
RESOURCEUNAVAILABLE_DELIVERING = 'ResourceUnavailable.Delivering'

# The account is frozen.
RESOURCEUNAVAILABLE_FREEZE = 'ResourceUnavailable.Freeze'

# Failed to get the authentication information.
RESOURCEUNAVAILABLE_GETAUTHINFOERROR = 'ResourceUnavailable.GetAuthInfoError'

# The account is in arrears.
RESOURCEUNAVAILABLE_INARREARS = 'ResourceUnavailable.InArrears'

# Insufficient balance.
RESOURCEUNAVAILABLE_LOWBALANCE = 'ResourceUnavailable.LowBalance'

# The billing status is unknown. Please check whether the service has been activated in the console.
RESOURCEUNAVAILABLE_NOTEXIST = 'ResourceUnavailable.NotExist'

# The service is not activated.
RESOURCEUNAVAILABLE_NOTREADY = 'ResourceUnavailable.NotReady'

# The resource has been repossessed.
RESOURCEUNAVAILABLE_RECOVER = 'ResourceUnavailable.Recover'

# The service has been suspended for the account.
RESOURCEUNAVAILABLE_STOPUSING = 'ResourceUnavailable.StopUsing'

# The billing status is unknown.
RESOURCEUNAVAILABLE_UNKNOWNSTATUS = 'ResourceUnavailable.UnknownStatus'

# The billing status is exceptional.
RESOURCESSOLDOUT_CHARGESTATUSEXCEPTION = 'ResourcesSoldOut.ChargeStatusException'

# Unknown method name.
UNSUPPORTEDOPERATION_UNKNOWMETHOD = 'UnsupportedOperation.UnknowMethod'
