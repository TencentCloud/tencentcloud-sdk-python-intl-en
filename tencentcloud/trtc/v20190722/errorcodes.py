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


# Identity verification has not been completed, so this operation is not allowed.
AUTHFAILURE_UNREALNAMEAUTHENTICATED = 'AuthFailure.UnRealNameAuthenticated'

# No On-Cloud MixTranscoding template is set for this room.
FAILEDOPERATION_MIXSESSIONNOTEXIST = 'FailedOperation.MixSessionNotExist'

# The TencentCloud API On-Cloud MixTranscoding template conflicts with On-Cloud MixTranscoding settings in the SDK.
FAILEDOPERATION_REQUESTREJECTION = 'FailedOperation.RequestRejection'

# The room does not exist.
FAILEDOPERATION_ROOMNOTEXIST = 'FailedOperation.RoomNotExist'

# Application ID does not exist.
FAILEDOPERATION_SDKAPPIDNOTEXIST = 'FailedOperation.SdkAppIdNotExist'

# Internal error.
INTERNALERROR = 'InternalError'

# Failed to access the backend service.
INTERNALERROR_BACKENDFAIL = 'InternalError.BackendFail'

# Backend service access timed out.
INTERNALERROR_BACKENDTIMEOUT = 'InternalError.BackendTimeOut'

# An error occurred while querying the database.
INTERNALERROR_DBERROR = 'InternalError.DBError'

# An error occurred while querying ES.
INTERNALERROR_ESQUERYERROR = 'InternalError.EsQueryError'

# Failed to query the room.
INTERNALERROR_GETROOMCACHEIPERROR = 'InternalError.GetRoomCacheIpError'

# Failed to get room information.
INTERNALERROR_GETROOMFROMCACHEERROR = 'InternalError.GetRoomFromCacheError'

# Failed to parse the HTTP request.
INTERNALERROR_HTTPPARASEFALIED = 'InternalError.HttpParaseFalied'

# API error.
INTERNALERROR_INTERFACEERR = 'InternalError.InterfaceErr'

# Unsupported method.
INTERNALERROR_METHODERR = 'InternalError.MethodErr'

# Failed to query seconds-level monitoring data.
INTERNALERROR_MONITORQUERYERR = 'InternalError.MonitorQueryErr'

# Invalid parameter.
INVALIDPARAMETER = 'InvalidParameter'

# Invalid audio codec parameter.
INVALIDPARAMETER_AUDIOENCODEPARAMS = 'InvalidParameter.AudioEncodeParams'

# Failed to parse the body parameter.
INVALIDPARAMETER_BODYPARAMSERROR = 'InvalidParameter.BodyParamsError'

# The image is too large.
INVALIDPARAMETER_CHECKCONTENTFAILED = 'InvalidParameter.CheckContentFailed'

# Invalid file extension.
INVALIDPARAMETER_CHECKSUFFIXFAILED = 'InvalidParameter.CheckSuffixFailed'

# Invalid `EncodeParams`.
INVALIDPARAMETER_ENCODEPARAMS = 'InvalidParameter.EncodeParams'

# Invalid `EndTs`.
INVALIDPARAMETER_ENDTS = 'InvalidParameter.EndTs'

# Invalid `MainVideoRightAlign` (parameter specifying whether to display the big image on the right).
INVALIDPARAMETER_MAINVIDEORIGHTALIGN = 'InvalidParameter.MainVideoRightAlign'

# Invalid stream type of the big image.
INVALIDPARAMETER_MAINVIDEOSTREAMTYPE = 'InvalidParameter.MainVideoStreamType'

# Incorrect `OutputParams` parameter.
INVALIDPARAMETER_OUTPUTPARAMS = 'InvalidParameter.OutputParams'

# Invalid `PageNumber`.
INVALIDPARAMETER_PAGENUMBER = 'InvalidParameter.PageNumber'

# Invalid `PageSize`.
INVALIDPARAMETER_PAGESIZE = 'InvalidParameter.PageSize'

# The value of `PageSize` exceeds 100.
INVALIDPARAMETER_PAGESIZEOVERSIZE = 'InvalidParameter.PageSizeOversize'

# Incorrect parameters for custom layout.
INVALIDPARAMETER_PRESETLAYOUTCONFIG = 'InvalidParameter.PresetLayoutConfig'

# Incorrect parameters for audio-only stream pushing.
INVALIDPARAMETER_PUREAUDIOSTREAM = 'InvalidParameter.PureAudioStream'

# The query time range exceeds 1 hour.
INVALIDPARAMETER_QUERYSCALEOVERSIZE = 'InvalidParameter.QueryScaleOversize'

# Incorrect parameters for audio-only recording.
INVALIDPARAMETER_RECORDAUDIOONLY = 'InvalidParameter.RecordAudioOnly'

# Incorrect `RecordId` parameter.
INVALIDPARAMETER_RECORDID = 'InvalidParameter.RecordId'

# `RoomId` is incorrect.
INVALIDPARAMETER_ROOMID = 'InvalidParameter.RoomId'

# `SdkAppId` is incorrect.
INVALIDPARAMETER_SDKAPPID = 'InvalidParameter.SdkAppId'

# Invalid small image layout parameter.
INVALIDPARAMETER_SMALLVIDEOLAYOUTPARAMS = 'InvalidParameter.SmallVideoLayoutParams'

# Invalid `StreamType` under `SmallVideoLayoutParams`.
INVALIDPARAMETER_SMALLVIDEOSTREAMTYPE = 'InvalidParameter.SmallVideoStreamType'

# The query start time is more than 24 hours earlier than now.
INVALIDPARAMETER_STARTTIMEEXPIRE = 'InvalidParameter.StartTimeExpire'

# Invalid `StartTs`.
INVALIDPARAMETER_STARTTS = 'InvalidParameter.StartTs'

# The query start time is more than 5 days earlier than now.
INVALIDPARAMETER_STARTTSOVERSIZE = 'InvalidParameter.StartTsOversize'

# Incorrect `StreamId` parameter.
INVALIDPARAMETER_STREAMID = 'InvalidParameter.StreamId'

# Failed to parse the URL parameter.
INVALIDPARAMETER_URLPARAMSERROR = 'InvalidParameter.UrlParamsError'

# Invalid `UserId`.
INVALIDPARAMETER_USERID = 'InvalidParameter.UserId'

# `UserIds` is incorrect.
INVALIDPARAMETER_USERIDS = 'InvalidParameter.UserIds'

# The number of users exceeds 6.
INVALIDPARAMETER_USERIDSMORETHANSIX = 'InvalidParameter.UserIdsMorethanSix'

# Invalid video resolution.
INVALIDPARAMETER_VIDEORESOLUTION = 'InvalidParameter.VideoResolution'

# Invalid RoomId.
INVALIDPARAMETERVALUE_ROOMID = 'InvalidParameterValue.RoomId'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# `AppId` missing.
MISSINGPARAMETER_APPID = 'MissingParameter.AppId'

# Audio output parameters are missing in `EncodeParams`.
MISSINGPARAMETER_AUDIOENCODEPARAMS = 'MissingParameter.AudioEncodeParams'

# BizId missing in relayed push parameters.
MISSINGPARAMETER_BIZID = 'MissingParameter.BizId'

# `CommId` is missing.
MISSINGPARAMETER_COMMID = 'MissingParameter.CommId'

# `SdkAppId` or `CommID` missing.
MISSINGPARAMETER_COMMIDORSDKAPPID = 'MissingParameter.CommIdOrSdkAppId'

# Missing `EncodeParams` parameter.
MISSINGPARAMETER_ENCODEPARAMS = 'MissingParameter.EncodeParams'

# `endTS_s` is missing.
MISSINGPARAMETER_ENDTS = 'MissingParameter.EndTs'

# Missing `OutputParams` parameter.
MISSINGPARAMETER_OUTPUTPARAMS = 'MissingParameter.OutputParams'

# Custom layout parameter missing.
MISSINGPARAMETER_PRESETLAYOUTCONFIG = 'MissingParameter.PresetLayoutConfig'

# Relaying parameter missing.
MISSINGPARAMETER_PUBLISHCDNPARAMS = 'MissingParameter.PublishCdnParams'

# Destination missing in relayed push parameters.
MISSINGPARAMETER_PUBLISHCDNURLS = 'MissingParameter.PublishCdnUrls'

# `RoomId` is missing.
MISSINGPARAMETER_ROOMID = 'MissingParameter.RoomId'

# `RoomNum` is missing.
MISSINGPARAMETER_ROOMNUM = 'MissingParameter.RoomNum'

# `SdkAppId` is missing.
MISSINGPARAMETER_SDKAPPID = 'MissingParameter.SdkAppId'

# `startTS_s` is missing.
MISSINGPARAMETER_STARTTS = 'MissingParameter.StartTs'

# The `StreamId` parameter is missing in `OutputParams`.
MISSINGPARAMETER_STREAMID = 'MissingParameter.StreamId'

# Missing `UserId` parameter.
MISSINGPARAMETER_USERID = 'MissingParameter.UserId'

# `UserIds` is missing.
MISSINGPARAMETER_USERIDS = 'MissingParameter.UserIds'

# Video output parameters are missing in `EncodeParams`.
MISSINGPARAMETER_VIDEOENCODEPARAMS = 'MissingParameter.VideoEncodeParams'

# No permission to manipulate `SdkAppId`.
UNAUTHORIZEDOPERATION_SDKAPPID = 'UnauthorizedOperation.SdkAppId'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'
