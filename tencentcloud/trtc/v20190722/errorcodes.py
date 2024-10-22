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

# Identity verification has not been completed, so this operation is not allowed.
AUTHFAILURE_UNREALNAMEAUTHENTICATED = 'AuthFailure.UnRealNameAuthenticated'

# CAM authentication failed.
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# Unsupported operation.
AUTHFAILURE_UNSUPPORTEDOPERATION = 'AuthFailure.UnsupportedOperation'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Unsupported on-cloud recording method.
FAILEDOPERATION_CRUNSUPPORTMETHOD = 'FailedOperation.CRUnsupportMethod'

# Need to unlock the required ability
FAILEDOPERATION_NOTABILITY = 'FailedOperation.NotAbility'

# This operation is not allowed, please submit a ticket to contact us
FAILEDOPERATION_NOTALLOWED = 'FailedOperation.NotAllowed'

# 
FAILEDOPERATION_NOTRTMPFUNCTION = 'FailedOperation.NotRtmpFunction'

# Query task failed
FAILEDOPERATION_QUERYTASKINFOFAILED = 'FailedOperation.QueryTaskInfoFailed'

# Maximum number of concurrent on-cloud recording tasks reached. Contact us to raise the limit.
FAILEDOPERATION_RESTRICTEDCONCURRENCY = 'FailedOperation.RestrictedConcurrency'

# The room does not exist.
FAILEDOPERATION_ROOMNOTEXIST = 'FailedOperation.RoomNotExist'

# The application ID does not exist.
FAILEDOPERATION_SDKAPPIDNOTEXIST = 'FailedOperation.SdkAppIdNotExist'

# There is no resource for this SdkAppId  In this AppId
FAILEDOPERATION_SDKAPPIDNOTUNDERAPPID = 'FailedOperation.SdkAppIdNotUnderAppId'

# Task already exists
FAILEDOPERATION_TASKEXIST = 'FailedOperation.TaskExist'

# Task has ended when calling the interface.
FAILEDOPERATION_TASKFINISHED = 'FailedOperation.TaskFinished'

# The task does not exist.
FAILEDOPERATION_TASKNOTEXIST = 'FailedOperation.TaskNotExist'

# The user is not in the room.
FAILEDOPERATION_USERNOTEXIST = 'FailedOperation.UserNotExist'

# Internal error.
INTERNALERROR = 'InternalError'

# On-cloud recording internal error.
INTERNALERROR_CRINTERNALERROR = 'InternalError.CRInternalError'

# An error occurred while querying the database.
INTERNALERROR_DBERROR = 'InternalError.DBError'

# An error occurred during an ES query.
INTERNALERROR_ESQUERYERROR = 'InternalError.EsQueryError'

# Failed to query the room.
INTERNALERROR_GETROOMCACHEIPERROR = 'InternalError.GetRoomCacheIpError'

# Failed to get room information.
INTERNALERROR_GETROOMFROMCACHEERROR = 'InternalError.GetRoomFromCacheError'

# Failed to parse the HTTP request.
INTERNALERROR_HTTPPARASEFALIED = 'InternalError.HttpParaseFalied'

# HTTP request parsing failed.
INTERNALERROR_HTTPPARSEFAILED = 'InternalError.HttpParseFailed'

# API error.
INTERNALERROR_INTERFACEERR = 'InternalError.InterfaceErr'

# Internal error, please retry.
INTERNALERROR_INTERNALERROR = 'InternalError.InternalError'

# Unsupported method.
INTERNALERROR_METHODERR = 'InternalError.MethodErr'

# The user is not in the room.
INTERNALERROR_USERNOTEXIST = 'InternalError.UserNotExist'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# Failed to parse body parameters.
INVALIDPARAMETER_BODYPARAMSERROR = 'InvalidParameter.BodyParamsError'

# Invalid `EncodeParams`.
INVALIDPARAMETER_ENCODEPARAMS = 'InvalidParameter.EncodeParams'

# Invalid `EndTs`.
INVALIDPARAMETER_ENDTS = 'InvalidParameter.EndTs'

# Parameter value is out of range.
INVALIDPARAMETER_OUTOFRANGE = 'InvalidParameter.OutOfRange'

# Invalid `PageNumber`.
INVALIDPARAMETER_PAGENUMBER = 'InvalidParameter.PageNumber'

# Invalid `PageSize`.
INVALIDPARAMETER_PAGESIZE = 'InvalidParameter.PageSize'

# The value of `PageSize` exceeds 100.
INVALIDPARAMETER_PAGESIZEOVERSIZE = 'InvalidParameter.PageSizeOversize'

# The query period exceeds the limit.
INVALIDPARAMETER_QUERYSCALEOVERSIZE = 'InvalidParameter.QueryScaleOversize'

# `RoomId` is incorrect.
INVALIDPARAMETER_ROOMID = 'InvalidParameter.RoomId'

# `SdkAppId` is incorrect.
INVALIDPARAMETER_SDKAPPID = 'InvalidParameter.SdkAppId'

# The start time for query exceeded the limit.
INVALIDPARAMETER_STARTTIMEEXPIRE = 'InvalidParameter.StartTimeExpire'

# The query start time exceeds the range allowed by the current dashboard edition. For details, see https://intl.cloud.tencent.com/document/product/647/81331?from_cn_redirect=1
INVALIDPARAMETER_STARTTIMEOVERSIZE = 'InvalidParameter.StartTimeOversize'

# Invalid `StartTs`.
INVALIDPARAMETER_STARTTS = 'InvalidParameter.StartTs'

# The start time for query exceeded the limit.
INVALIDPARAMETER_STARTTSOVERSIZE = 'InvalidParameter.StartTsOversize'

# StrRoomId parameter error.
INVALIDPARAMETER_STRROOMID = 'InvalidParameter.StrRoomId'

# Invalid StreamUrl format
INVALIDPARAMETER_STREAMURL = 'InvalidParameter.StreamUrl'

# TaskId parameter error.
INVALIDPARAMETER_TASKID = 'InvalidParameter.TaskId'

# Failed to parse URL parameters.
INVALIDPARAMETER_URLPARAMSERROR = 'InvalidParameter.UrlParamsError'

# Invalid `UserId`.
INVALIDPARAMETER_USERID = 'InvalidParameter.UserId'

# `UserIds` is incorrect.
INVALIDPARAMETER_USERIDS = 'InvalidParameter.UserIds'

# The number of users exceeds 6.
INVALIDPARAMETER_USERIDSMORETHANSIX = 'InvalidParameter.UserIdsMorethanSix'

# UserSig is expired or wrong
INVALIDPARAMETER_USERSIG = 'InvalidParameter.UserSig'

# 
INVALIDPARAMETER_USERSIGNOTADMIN = 'InvalidParameter.UserSigNotAdmin'

# Invalid RoomId.
INVALIDPARAMETERVALUE_ROOMID = 'InvalidParameterValue.RoomId'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# `AccessKey` parameter missing.
MISSINGPARAMETER_ACCESSKEY = 'MissingParameter.AccessKey'

# `AppId` missing.
MISSINGPARAMETER_APPID = 'MissingParameter.AppId'

# `Bucket` parameter missing.
MISSINGPARAMETER_BUCKET = 'MissingParameter.Bucket'

# `CloudStorage` parameter missing.
MISSINGPARAMETER_CLOUDSTORAGE = 'MissingParameter.CloudStorage'

# `CommId` is missing.
MISSINGPARAMETER_COMMID = 'MissingParameter.CommId'

# `SdkAppId` or `CommID` missing.
MISSINGPARAMETER_COMMIDORSDKAPPID = 'MissingParameter.CommIdOrSdkAppId'

# `endTS_s` is missing.
MISSINGPARAMETER_ENDTS = 'MissingParameter.EndTs'

# `RecordMode` parameter missing.
MISSINGPARAMETER_RECORDMODE = 'MissingParameter.RecordMode'

# `RecordParams` parameter missing.
MISSINGPARAMETER_RECORDPARAMS = 'MissingParameter.RecordParams'

# `Region` parameter missing.
MISSINGPARAMETER_REGION = 'MissingParameter.Region'

# `RoomId` is missing.
MISSINGPARAMETER_ROOMID = 'MissingParameter.RoomId'

# `RoomNum` is missing.
MISSINGPARAMETER_ROOMNUM = 'MissingParameter.RoomNum'

# `SdkAppId` is missing.
MISSINGPARAMETER_SDKAPPID = 'MissingParameter.SdkAppId'

# `SecretKey` parameter missing.
MISSINGPARAMETER_SECRETKEY = 'MissingParameter.SecretKey'

# `startTS_s` is missing.
MISSINGPARAMETER_STARTTS = 'MissingParameter.StartTs'

# `StorageParams` parameter missing.
MISSINGPARAMETER_STORAGEPARAMS = 'MissingParameter.StorageParams'

# `StreamType` parameter missing.
MISSINGPARAMETER_STREAMTYPE = 'MissingParameter.StreamType'

# `TaskId` parameter missing.
MISSINGPARAMETER_TASKID = 'MissingParameter.TaskId'

# Missing `UserId` parameter.
MISSINGPARAMETER_USERID = 'MissingParameter.UserId'

# `UserIds` is missing.
MISSINGPARAMETER_USERIDS = 'MissingParameter.UserIds'

# `UserSig` parameter missing.
MISSINGPARAMETER_USERSIG = 'MissingParameter.UserSig'

# `Vendor` parameter missing.
MISSINGPARAMETER_VENDOR = 'MissingParameter.Vendor'

# Insufficient resources.
RESOURCEINSUFFICIENT_REQUESTREJECTION = 'ResourceInsufficient.RequestRejection'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# No permission to manipulate `SdkAppId`.
UNAUTHORIZEDOPERATION_SDKAPPID = 'UnauthorizedOperation.SdkAppId'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
