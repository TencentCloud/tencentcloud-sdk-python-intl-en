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

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Operation failed: the number of category levels exceeds the limit.
FAILEDOPERATION_CLASSLEVELLIMITEXCEEDED = 'FailedOperation.ClassLevelLimitExceeded'

# Operation failed: the category name already exists.
FAILEDOPERATION_CLASSNAMEDUPLICATE = 'FailedOperation.ClassNameDuplicate'

# Operation failed: the category does not exist.
FAILEDOPERATION_CLASSNOFOUND = 'FailedOperation.ClassNoFound'

# Operation failed: unsupported cover type.
FAILEDOPERATION_COVERTYPE = 'FailedOperation.CoverType'

# Operation failed: The database operation failed.
FAILEDOPERATION_DBERROR = 'FailedOperation.DBError'

# You cannot modify the settings of the domain name as it is being deployed.
FAILEDOPERATION_DOMAINDEPLOYING = 'FailedOperation.DomainDeploying'

# User account exception.
FAILEDOPERATION_INVALIDACCOUNT = 'FailedOperation.InvalidAccount'

# The VOD service is not activated.
FAILEDOPERATION_INVALIDVODUSER = 'FailedOperation.InvalidVodUser'

# Media blocked by the system.
FAILEDOPERATION_MEDIAFORBIDEDBYSYSTEM = 'FailedOperation.MediaForbidedBySystem'

# Operation failed: unsupported media type.
FAILEDOPERATION_MEDIATYPE = 'FailedOperation.MediaType'

# Network error.
FAILEDOPERATION_NETWORKERROR = 'FailedOperation.NetWorkError'

# No need to reduce the bitrate.
FAILEDOPERATION_NONEEDTOREDUCEMEDIABITRATE = 'FailedOperation.NoNeedToReduceMediaBitrate'

# Operation failed: the parent category ID does not exist.
FAILEDOPERATION_PARENTIDNOFOUND = 'FailedOperation.ParentIdNoFound'

# Operation failed: the number of subcategories exceeds the limit.
FAILEDOPERATION_SUBCLASSLIMITEXCEEDED = 'FailedOperation.SubclassLimitExceeded'

# Operation failed: the task already exists.
FAILEDOPERATION_TASKDUPLICATE = 'FailedOperation.TaskDuplicate'

# Operation failed: failed to upload file to COS.
FAILEDOPERATION_UPLOADCOSFAIL = 'FailedOperation.UploadCosFail'

# The service has been suspended.
FAILEDOPERATION_USERSTATUSINAVLID = 'FailedOperation.UserStatusInavlid'

# Internal error.
INTERNALERROR = 'InternalError'

# Internal error. Failed to access DB.
INTERNALERROR_DBERROR = 'InternalError.DBError'

# Internal error: failed to generate template ID.
INTERNALERROR_GENDEFINITION = 'InternalError.GenDefinition'

# Internal error: an error occurred while getting media file information.
INTERNALERROR_GETFILEINFOERROR = 'InternalError.GetFileInfoError'

# Internal error: an error occurred while getting the media list.
INTERNALERROR_GETMEDIALISTERROR = 'InternalError.GetMediaListError'

# An error occurred while parsing the time.
INTERNALERROR_TIMEPARSEERROR = 'InternalError.TimeParseError'

# Internal error: an error occurred while updating media file information.
INTERNALERROR_UPDATEMEDIAERROR = 'InternalError.UpdateMediaError'

# Internal error: an error occurred while uploading cover image.
INTERNALERROR_UPLOADCOVERIMAGEERROR = 'InternalError.UploadCoverImageError'

# Internal error: failed to upload watermark image.
INTERNALERROR_UPLOADWATERMARKERROR = 'InternalError.UploadWatermarkError'

# Invalid parameter.
INVALIDPARAMETER = 'InvalidParameter'

# The task flow template name already exists.
INVALIDPARAMETER_EXISTEDPROCEDURENAME = 'InvalidParameter.ExistedProcedureName'

# Incorrect parameter value: expiration time.
INVALIDPARAMETER_EXPIRETIME = 'InvalidParameter.ExpireTime'

# Parameter error: Invalid label.
INVALIDPARAMETER_LABELS = 'InvalidParameter.Labels'

# The task flow template name does not exist.
INVALIDPARAMETER_PROCEDURENAMENOTEXIST = 'InvalidParameter.ProcedureNameNotExist'

# Incorrect parameter value: storage region.
INVALIDPARAMETER_STORAGEREGION = 'InvalidParameter.StorageRegion'

# Incorrect parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Incorrect parameter value: `AddKeyFrameDescs` conflicts with `ClearKeyFrameDescs`.
INVALIDPARAMETERVALUE_ADDKEYFRAMEDESCSANDCLEARKEYFRAMEDESCSCONFLICT = 'InvalidParameterValue.AddKeyFrameDescsAndClearKeyFrameDescsConflict'

# Incorrect parameter value: `AddKeyFrameDescs` conflicts with `DeleteKeyFrameDescs`.
INVALIDPARAMETERVALUE_ADDKEYFRAMEDESCSANDDELETEKEYFRAMEDESCSCONFLICT = 'InvalidParameterValue.AddKeyFrameDescsAndDeleteKeyFrameDescsConflict'

# Incorrect parameter value: `AddTags` conflicts with `ClearTags`.
INVALIDPARAMETERVALUE_ADDTAGSANDCLEARTAGSCONFLICT = 'InvalidParameterValue.AddTagsAndClearTagsConflict'

# Incorrect parameter value: `AddTags` conflicts with `DeleteTags`.
INVALIDPARAMETERVALUE_ADDTAGSANDDELETETAGSCONFLICT = 'InvalidParameterValue.AddTagsAndDeleteTagsConflict'

# Incorrect parameter value: `Definition` for AI-based analysis.
INVALIDPARAMETERVALUE_AIANALYSISTASKDEFINITION = 'InvalidParameterValue.AiAnalysisTaskDefinition'

# Incorrect parameter value: `Definition` AI-based content audit.
INVALIDPARAMETERVALUE_AICONTENTREVIEWTASKDEFINITION = 'InvalidParameterValue.AiContentReviewTaskDefinition'

# Incorrect parameter value: `Definition` for AI-based recognition.
INVALIDPARAMETERVALUE_AIRECOGNITIONTASKDEFINITION = 'InvalidParameterValue.AiRecognitionTaskDefinition'

# Invalid `Area`.
INVALIDPARAMETERVALUE_AREA = 'InvalidParameterValue.Area'

# Invalid parameter: audio stream bitrate.
INVALIDPARAMETERVALUE_AUDIOBITRATE = 'InvalidParameterValue.AudioBitrate'

# Incorrect parameter value: AudioChannel.
INVALIDPARAMETERVALUE_AUDIOCHANNEL = 'InvalidParameterValue.AudioChannel'

# Invalid parameter: audio stream encoder.
INVALIDPARAMETERVALUE_AUDIOCODEC = 'InvalidParameterValue.AudioCodec'

# Invalid parameter: audio stream sample rate.
INVALIDPARAMETERVALUE_AUDIOSAMPLERATE = 'InvalidParameterValue.AudioSampleRate'

# Invalid audio/video bitrate.
INVALIDPARAMETERVALUE_BITRATE = 'InvalidParameterValue.Bitrate'

# Incorrect parameter value: the value of the `BlockConfidence` parameter is invalid.
INVALIDPARAMETERVALUE_BLOCKCONFIDENCE = 'InvalidParameterValue.BlockConfidence'

# Invalid file type.
INVALIDPARAMETERVALUE_CATEGORIES = 'InvalidParameterValue.Categories'

# Incorrect parameter value: category ID.
INVALIDPARAMETERVALUE_CLASSID = 'InvalidParameterValue.ClassId'

# Incorrect parameter value: invalid `ClassIds`.
INVALIDPARAMETERVALUE_CLASSIDS = 'InvalidParameterValue.ClassIds'

# Incorrect parameter value: invalid `ClassName`
INVALIDPARAMETERVALUE_CLASSNAME = 'InvalidParameterValue.ClassName'

# The control field parameter for intelligent categorization is incorrect.
INVALIDPARAMETERVALUE_CLASSIFCATIONCONFIGURE = 'InvalidParameterValue.ClassifcationConfigure'

# Incorrect parameter value: the clipping duration is too long.
INVALIDPARAMETERVALUE_CLIPDURATION = 'InvalidParameterValue.ClipDuration'

# Invalid audio/video codec.
INVALIDPARAMETERVALUE_CODEC = 'InvalidParameterValue.Codec'

# Incorrect parameter value: ColumnCount.
INVALIDPARAMETERVALUE_COLUMNCOUNT = 'InvalidParameterValue.ColumnCount'

# Invalid parameter: template description.
INVALIDPARAMETERVALUE_COMMENT = 'InvalidParameterValue.Comment'

# Invalid parameter: container.
INVALIDPARAMETERVALUE_CONTAINER = 'InvalidParameterValue.Container'

# Incorrect parameter value: ContainerType.
INVALIDPARAMETERVALUE_CONTAINERTYPE = 'InvalidParameterValue.ContainerType'

# Incorrect parameter value: CoordinateOrigin.
INVALIDPARAMETERVALUE_COORDINATEORIGIN = 'InvalidParameterValue.CoordinateOrigin'

# The control field parameter for intelligent cover generation is incorrect.
INVALIDPARAMETERVALUE_COVERCONFIGURE = 'InvalidParameterValue.CoverConfigure'

# Incorrect parameter value: cover type.
INVALIDPARAMETERVALUE_COVERTYPE = 'InvalidParameterValue.CoverType'

# Incorrect parameter value: cover URL.
INVALIDPARAMETERVALUE_COVERURL = 'InvalidParameterValue.CoverUrl'

# Parameter error: Invalid `CutAndCrops` value.
INVALIDPARAMETERVALUE_CUTANDCROPS = 'InvalidParameterValue.CutAndCrops'

# Incorrect parameter value: time granularity.
INVALIDPARAMETERVALUE_DATAINTERVAL = 'InvalidParameterValue.DataInterval'

# Incorrect parameter value: data type.
INVALIDPARAMETERVALUE_DATATYPE = 'InvalidParameterValue.DataType'

# Incorrect parameter value: the default face library filter tag is invalid.
INVALIDPARAMETERVALUE_DEFAULTLIBRARYLABELSET = 'InvalidParameterValue.DefaultLibraryLabelSet'

# Invalid parameter: Definition.
INVALIDPARAMETERVALUE_DEFINITION = 'InvalidParameterValue.Definition'

# Invalid parameter: Definitions.
INVALIDPARAMETERVALUE_DEFINITIONS = 'InvalidParameterValue.Definitions'

# Incorrect parameter value: the default template cannot be deleted.
INVALIDPARAMETERVALUE_DELETEDEFAULTTEMPLATE = 'InvalidParameterValue.DeleteDefaultTemplate'

# Incorrect parameter value: `Description` exceeds the length limit.
INVALIDPARAMETERVALUE_DESCRIPTION = 'InvalidParameterValue.Description'

# Invalid value of the switch for prohibiting transcoding from low bitrate to high bitrate.
INVALIDPARAMETERVALUE_DISABLEHIGHERVIDEOBITRATE = 'InvalidParameterValue.DisableHigherVideoBitrate'

# Invalid value of the switch for prohibiting transcoding from low resolution to high resolution.
INVALIDPARAMETERVALUE_DISABLEHIGHERVIDEORESOLUTION = 'InvalidParameterValue.DisableHigherVideoResolution'

# Incorrect `Districts`.
INVALIDPARAMETERVALUE_DISTRICTS = 'InvalidParameterValue.Districts'

# Invalid parameter: the domain name does not exist.
INVALIDPARAMETERVALUE_DOMAINNAME = 'InvalidParameterValue.DomainName'

# This domain name cannot be added as it is invalid.
INVALIDPARAMETERVALUE_DOMAINNAMEINBLACKLIST = 'InvalidParameterValue.DomainNameInBlackList'

# Parameter value. The domain name list is too large.
INVALIDPARAMETERVALUE_DOMAINNAMES = 'InvalidParameterValue.DomainNames'

# Invalid DRM type.
INVALIDPARAMETERVALUE_DRMTYPE = 'InvalidParameterValue.DrmType'

# Incorrect parameter value: invalid `EndTime`.
INVALIDPARAMETERVALUE_ENDTIME = 'InvalidParameterValue.EndTime'

# Incorrect parameter: the end time is invalid.
INVALIDPARAMETERVALUE_ENDTIMEOFFSET = 'InvalidParameterValue.EndTimeOffset'

# Duplicate name
INVALIDPARAMETERVALUE_EXISTEDNAME = 'InvalidParameterValue.ExistedName'

# Incorrect parameter value: incorrect `ExpireTime` format.
INVALIDPARAMETERVALUE_EXPIRETIME = 'InvalidParameterValue.ExpireTime'

# Incorrect `expiretime`.
INVALIDPARAMETERVALUE_EXPIREDTIME = 'InvalidParameterValue.ExpiredTime'

# Incorrect parameter value: the same face already exists.
INVALIDPARAMETERVALUE_FACEDUPLICATE = 'InvalidParameterValue.FaceDuplicate'

# Incorrect parameter value: the face library parameter is invalid.
INVALIDPARAMETERVALUE_FACELIBRARY = 'InvalidParameterValue.FaceLibrary'

# Incorrect parameter value: the value of the face score parameter is invalid.
INVALIDPARAMETERVALUE_FACESCORE = 'InvalidParameterValue.FaceScore'

# The `FileId` does not exist.
INVALIDPARAMETERVALUE_FILEID = 'InvalidParameterValue.FileId'

# Incorrect `FileIds` parameter.
INVALIDPARAMETERVALUE_FILEIDS = 'InvalidParameterValue.FileIds'

# The `FileIds` array is empty.
INVALIDPARAMETERVALUE_FILEIDSEMPTY = 'InvalidParameterValue.FileIdsEmpty'

# Incorrect parameter value: too many `FileId`
INVALIDPARAMETERVALUE_FILEIDSTOOMANY = 'InvalidParameterValue.FileIdsTooMany'

# Invalid parameter: incorrect fill type.
INVALIDPARAMETERVALUE_FILLTYPE = 'InvalidParameterValue.FillType'

#  
INVALIDPARAMETERVALUE_FILTRATEAUDIO = 'InvalidParameterValue.FiltrateAudio'

#  
INVALIDPARAMETERVALUE_FILTRATEVIDEO = 'InvalidParameterValue.FiltrateVideo'

# Incorrect parameter value: Format.
INVALIDPARAMETERVALUE_FORMAT = 'InvalidParameterValue.Format'

# Incorrect parameter value: `Format` is `webp`, but both `Width` and `Height` are empty.
INVALIDPARAMETERVALUE_FORMATWEBPLACKWIDTHANDHEIGHT = 'InvalidParameterValue.FormatWebpLackWidthAndHeight'

# Incorrect parameter value: when `Format` is `webp`, `Width` and `Height` cannot be both 0.
INVALIDPARAMETERVALUE_FORMATWEBPWIDTHANDHEIGHTBOTHZERO = 'InvalidParameterValue.FormatWebpWidthAndHeightBothZero'

# Invalid parameter: video frame rate.
INVALIDPARAMETERVALUE_FPS = 'InvalidParameterValue.Fps'

# The control field parameter for intelligent frame-specific tagging is incorrect.
INVALIDPARAMETERVALUE_FRAMETAGCONFIGURE = 'InvalidParameterValue.FrameTagConfigure'

# Incorrect parameter value: FunctionArg.
INVALIDPARAMETERVALUE_FUNCTIONARG = 'InvalidParameterValue.FunctionArg'

# Incorrect parameter value: FunctionName.
INVALIDPARAMETERVALUE_FUNCTIONNAME = 'InvalidParameterValue.FunctionName'

# Invalid parameter: height.
INVALIDPARAMETERVALUE_HEIGHT = 'InvalidParameterValue.Height'

# Invalid intelligent highlight generating control parameter.
INVALIDPARAMETERVALUE_HIGHLIGHTCONFIGURE = 'InvalidParameterValue.HighlightConfigure'

# Invalid `ImageContent`.
INVALIDPARAMETERVALUE_IMAGECONTENT = 'InvalidParameterValue.ImageContent'

# Failed to Base64-decode the image.
INVALIDPARAMETERVALUE_IMAGEDECODEERROR = 'InvalidParameterValue.ImageDecodeError'

# Invalid parameter: image watermarking template.
INVALIDPARAMETERVALUE_IMAGETEMPLATE = 'InvalidParameterValue.ImageTemplate'

# Index parameter error.
INVALIDPARAMETERVALUE_INDEX = 'InvalidParameterValue.Index'

# Invalid `Interval` value
INVALIDPARAMETERVALUE_INTERVAL = 'InvalidParameterValue.Interval'

# Invalid `OperationType`.
INVALIDPARAMETERVALUE_INVALIDOPERATIONTYPE = 'InvalidParameterValue.InvalidOperationType'

# 
INVALIDPARAMETERVALUE_ISPERSISTENCE = 'InvalidParameterValue.IsPersistence'

# Invalid `Isps`.
INVALIDPARAMETERVALUE_ISPS = 'InvalidParameterValue.Isps'

# 
INVALIDPARAMETERVALUE_ITEMID = 'InvalidParameterValue.ItemId'

# Incorrect parameter value: the timestamp content is too long.
INVALIDPARAMETERVALUE_KEYFRAMEDESCCONTENTTOOLONG = 'InvalidParameterValue.KeyFrameDescContentTooLong'

# Incorrect parameter value: the value of the `LabelSet` parameter is invalid.
INVALIDPARAMETERVALUE_LABELSET = 'InvalidParameterValue.LabelSet'

# Parameter error: Invalid label.
INVALIDPARAMETERVALUE_LABELS = 'InvalidParameterValue.Labels'

# Invalid parameter: Limit.
INVALIDPARAMETERVALUE_LIMIT = 'InvalidParameterValue.Limit'

# Incorrect parameter value: `Limit` is too large.
INVALIDPARAMETERVALUE_LIMITTOOLARGE = 'InvalidParameterValue.LimitTooLarge'

# Incorrect parameter value: MediaManifestContent.
INVALIDPARAMETERVALUE_MEDIAMANIFESTCONTENT = 'InvalidParameterValue.MediaManifestContent'

# Incorrect parameter value: media type.
INVALIDPARAMETERVALUE_MEDIATYPE = 'InvalidParameterValue.MediaType'

# Incorrect parameter value: media file URL.
INVALIDPARAMETERVALUE_MEDIAURL = 'InvalidParameterValue.MediaUrl'

# Parameter error: Invalid metric.
INVALIDPARAMETERVALUE_METRIC = 'InvalidParameterValue.Metric'

# Incorrect parameter value: the default template cannot be modified.
INVALIDPARAMETERVALUE_MODIFYDEFAULTTEMPLATE = 'InvalidParameterValue.ModifyDefaultTemplate'

# Incorrect parameter value: `Name` exceeds the length limit.
INVALIDPARAMETERVALUE_NAME = 'InvalidParameterValue.Name'

# Invalid filename prefix.
INVALIDPARAMETERVALUE_NAMEPREFIXES = 'InvalidParameterValue.NamePrefixes'

# Too many elements in the `Names` array.
INVALIDPARAMETERVALUE_NAMES = 'InvalidParameterValue.Names'

# Parameter error: The file cannot be restored.
INVALIDPARAMETERVALUE_NOTRESTORABLE = 'InvalidParameterValue.NotRestorable'

# Incorrect parameter value: the value of the object library parameter is invalid.
INVALIDPARAMETERVALUE_OBJECTLIBRARY = 'InvalidParameterValue.ObjectLibrary'

# Incorrect parameter value: invalid `Offset`.
INVALIDPARAMETERVALUE_OFFSET = 'InvalidParameterValue.Offset'

# Incorrect parameter value: `Offset` is too large.
INVALIDPARAMETERVALUE_OFFSETTOOLARGE = 'InvalidParameterValue.OffsetTooLarge'

# Incorrect parameter value: invalid `Operation`.
INVALIDPARAMETERVALUE_OPERATION = 'InvalidParameterValue.Operation'

# Parameter error: Current storage class error.
INVALIDPARAMETERVALUE_ORIGINALSTORAGECLASS = 'InvalidParameterValue.OriginalStorageClass'

# 
INVALIDPARAMETERVALUE_OUTPUTMEDIATYPE = 'InvalidParameterValue.OutputMediaType'

# Incorrect parameter value: invalid `ParentId`
INVALIDPARAMETERVALUE_PARENTID = 'InvalidParameterValue.ParentId'

# Incorrect parameter value: the face image format is incorrect.
INVALIDPARAMETERVALUE_PICFORMATERROR = 'InvalidParameterValue.PicFormatError'

# 
INVALIDPARAMETERVALUE_PRECISION = 'InvalidParameterValue.Precision'

# 
INVALIDPARAMETERVALUE_PROCEDURE = 'InvalidParameterValue.Procedure'

# The task flow template name is invalid.
INVALIDPARAMETERVALUE_PROCEDURENAME = 'InvalidParameterValue.ProcedureName'

# Incorrect parameter value: Quality.
INVALIDPARAMETERVALUE_QUALITY = 'InvalidParameterValue.Quality'

# Incorrect parameter value: RemoveAudio.
INVALIDPARAMETERVALUE_REMOVEAUDIO = 'InvalidParameterValue.RemoveAudio'

# Incorrect parameter value: RemoveVideo.
INVALIDPARAMETERVALUE_REMOVEVIDEO = 'InvalidParameterValue.RemoveVideo'

# Invalid parameter: invalid `RepeatType`.
INVALIDPARAMETERVALUE_REPEATTYPE = 'InvalidParameterValue.RepeatType'

# Invalid parameter: incorrect resolution.
INVALIDPARAMETERVALUE_RESOLUTION = 'InvalidParameterValue.Resolution'

# Invalid `ResolutionAdaptive`.
INVALIDPARAMETERVALUE_RESOLUTIONADAPTIVE = 'InvalidParameterValue.ResolutionAdaptive'

# Parameter error: Invalid `RestoreDay`.
INVALIDPARAMETERVALUE_RESTOREDAY = 'InvalidParameterValue.RestoreDay'

# Parameter error: Unsupported retrieval mode.
INVALIDPARAMETERVALUE_RESTORETIER = 'InvalidParameterValue.RestoreTier'

# Incorrect parameter value: the value of the `ReviewConfidence` parameter is invalid.
INVALIDPARAMETERVALUE_REVIEWCONFIDENCE = 'InvalidParameterValue.ReviewConfidence'

# Incorrect parameter value: the value of the `ReviewWallSwitch` parameter is invalid.
INVALIDPARAMETERVALUE_REVIEWWALLSWITCH = 'InvalidParameterValue.ReviewWallSwitch'

# A playlist with the same id already exists.
INVALIDPARAMETERVALUE_ROUNDPLAYALREADYEXISTS = 'InvalidParameterValue.RoundPlayAlreadyExists'

# RoundPlayId parameter error.
INVALIDPARAMETERVALUE_ROUNDPLAYID = 'InvalidParameterValue.RoundPlayId'

# RoundPlaylist parameter length error.
INVALIDPARAMETERVALUE_ROUNDPLAYLIST = 'InvalidParameterValue.RoundPlaylist'

# Incorrect parameter value: RowCount.
INVALIDPARAMETERVALUE_ROWCOUNT = 'InvalidParameterValue.RowCount'

# Incorrect parameter value: SampleInterval.
INVALIDPARAMETERVALUE_SAMPLEINTERVAL = 'InvalidParameterValue.SampleInterval'

# Invalid audio sample rate.
INVALIDPARAMETERVALUE_SAMPLERATE = 'InvalidParameterValue.SampleRate'

# Incorrect parameter value: SampleType.
INVALIDPARAMETERVALUE_SAMPLETYPE = 'InvalidParameterValue.SampleType'

# Incorrect parameter value: the value of the `ScreenshotInterval` parameter is invalid.
INVALIDPARAMETERVALUE_SCREENSHOTINTERVAL = 'InvalidParameterValue.ScreenshotInterval'

# `SessionContext` is too long.
INVALIDPARAMETERVALUE_SESSIONCONTEXTTOOLONG = 'InvalidParameterValue.SessionContextTooLong'

# The deduplication ID already exists. The request is removed due to duplication.
INVALIDPARAMETERVALUE_SESSIONID = 'InvalidParameterValue.SessionId'

# `SessionId` is too long.
INVALIDPARAMETERVALUE_SESSIONIDTOOLONG = 'InvalidParameterValue.SessionIdTooLong'

# Incorrect parameter value: invalid `Sort`.
INVALIDPARAMETERVALUE_SORT = 'InvalidParameterValue.Sort'

# Incorrect parameter: audio channel system.
INVALIDPARAMETERVALUE_SOUNDSYSTEM = 'InvalidParameterValue.SoundSystem'

# Incorrect parameter value: invalid `SourceType`.
INVALIDPARAMETERVALUE_SOURCETYPE = 'InvalidParameterValue.SourceType'

# Unknown media file source.
INVALIDPARAMETERVALUE_SOURCETYPES = 'InvalidParameterValue.SourceTypes'

# Incorrect parameter value: invalid `StartTime`.
INVALIDPARAMETERVALUE_STARTTIME = 'InvalidParameterValue.StartTime'

# Incorrect parameter: the start time is invalid.
INVALIDPARAMETERVALUE_STARTTIMEOFFSET = 'InvalidParameterValue.StartTimeOffset'

# Incorrect parameter value: the value of human confirmation result is invalid.
INVALIDPARAMETERVALUE_STATUS = 'InvalidParameterValue.Status'

# Parameter error: The target storage class is not allowed.
INVALIDPARAMETERVALUE_STORAGECLASS = 'InvalidParameterValue.StorageClass'

# Incorrect parameter value: `StorageRegion`.
INVALIDPARAMETERVALUE_STORAGEREGION = 'InvalidParameterValue.StorageRegion'

# Invalid `StorageRegions`.
INVALIDPARAMETERVALUE_STORAGEREGIONS = 'InvalidParameterValue.StorageRegions'

# Incorrect parameter value: StorageType.
INVALIDPARAMETERVALUE_STORAGETYPE = 'InvalidParameterValue.StorageType'

# Incorrect parameter value: invalid `StreamId`.
INVALIDPARAMETERVALUE_STREAMIDINVALID = 'InvalidParameterValue.StreamIdInvalid'

# Invalid stream ID.
INVALIDPARAMETERVALUE_STREAMIDS = 'InvalidParameterValue.StreamIds'

# Incorrect parameter value: application id.
INVALIDPARAMETERVALUE_SUBAPPID = 'InvalidParameterValue.SubAppId'

# Incorrect parameter value: the value of the `SubtitleFormat` parameter is invalid.
INVALIDPARAMETERVALUE_SUBTITLEFORMAT = 'InvalidParameterValue.SubtitleFormat'

# Incorrect parameter value: SVG is empty.
INVALIDPARAMETERVALUE_SVGTEMPLATE = 'InvalidParameterValue.SvgTemplate'

# Incorrect parameter value: SVG height.
INVALIDPARAMETERVALUE_SVGTEMPLATEHEIGHT = 'InvalidParameterValue.SvgTemplateHeight'

# Incorrect parameter value: SVG width.
INVALIDPARAMETERVALUE_SVGTEMPLATEWIDTH = 'InvalidParameterValue.SvgTemplateWidth'

# Incorrect parameter value: the value of the `Switch` parameter is invalid.
INVALIDPARAMETERVALUE_SWITCH = 'InvalidParameterValue.Switch'

# Incorrect parameter value: `TEHD Type` is invalid.
INVALIDPARAMETERVALUE_TEHDTYPE = 'InvalidParameterValue.TEHDType'

# The control field parameter for intelligent tagging is incorrect.
INVALIDPARAMETERVALUE_TAGCONFIGURE = 'InvalidParameterValue.TagConfigure'

# Incorrect parameter value: the tag is too long.
INVALIDPARAMETERVALUE_TAGTOOLONG = 'InvalidParameterValue.TagTooLong'

# Incorrect parameter value: invalid `Tags`.
INVALIDPARAMETERVALUE_TAGS = 'InvalidParameterValue.Tags'

# The task ID does not exist.
INVALIDPARAMETERVALUE_TASKID = 'InvalidParameterValue.TaskId'

# Incorrect parameter value: search text.
INVALIDPARAMETERVALUE_TEXT = 'InvalidParameterValue.Text'

# Invalid parameter: text transparency.
INVALIDPARAMETERVALUE_TEXTALPHA = 'InvalidParameterValue.TextAlpha'

# Invalid parameter: text template.
INVALIDPARAMETERVALUE_TEXTTEMPLATE = 'InvalidParameterValue.TextTemplate'

# Parameter error: Invalid `Thumbnail` value.
INVALIDPARAMETERVALUE_THUMBNAILS = 'InvalidParameterValue.Thumbnails'

# Incorrect parameter value: TimeType.
INVALIDPARAMETERVALUE_TIMETYPE = 'InvalidParameterValue.TimeType'

# Incorrect `Type` parameter value.
INVALIDPARAMETERVALUE_TYPE = 'InvalidParameterValue.Type'

# Invalid `Types`.
INVALIDPARAMETERVALUE_TYPES = 'InvalidParameterValue.Types'

# The deduplication ID already exists on the same day. The request is removed due to duplication.
INVALIDPARAMETERVALUE_UNIQUEIDENTIFIER = 'InvalidParameterValue.UniqueIdentifier'

# Parameter error: This retrieval mode is not supported for the file.
INVALIDPARAMETERVALUE_UNSUPPORTEDRESTORETIER = 'InvalidParameterValue.UnsupportedRestoreTier'

# Parameter error: Unsupported target storage class. DEEP ARCHIVE is only supported in certain regions.
INVALIDPARAMETERVALUE_UNSUPPORTEDSTORAGECLASS = 'InvalidParameterValue.UnsupportedStorageClass'

# Parameter error: Unsupported storage class change.
INVALIDPARAMETERVALUE_UNSUPPORTEDTRANSITION = 'InvalidParameterValue.UnsupportedTransition'

# Incorrect parameter: the URL is invalid.
INVALIDPARAMETERVALUE_URL = 'InvalidParameterValue.Url'

# Incorrect parameter value: the custom face library filter tag is invalid.
INVALIDPARAMETERVALUE_USERDEFINELIBRARYLABELSET = 'InvalidParameterValue.UserDefineLibraryLabelSet'

# Incorrect `vcrf`.
INVALIDPARAMETERVALUE_VCRF = 'InvalidParameterValue.Vcrf'

# Invalid parameter: video stream bitrate.
INVALIDPARAMETERVALUE_VIDEOBITRATE = 'InvalidParameterValue.VideoBitrate'

# Invalid parameter: video stream encoder.
INVALIDPARAMETERVALUE_VIDEOCODEC = 'InvalidParameterValue.VideoCodec'

# Invalid `Vids`.
INVALIDPARAMETERVALUE_VIDS = 'InvalidParameterValue.Vids'

# Incorrect parameter value: VOD session.
INVALIDPARAMETERVALUE_VODSESSIONKEY = 'InvalidParameterValue.VodSessionKey'

# Parameter error: Invalid `Watermarks` value.
INVALIDPARAMETERVALUE_WATERMARKS = 'InvalidParameterValue.Watermarks'

# Invalid parameter: width.
INVALIDPARAMETERVALUE_WIDTH = 'InvalidParameterValue.Width'

# The horizontal position of the origin of the watermark relative to the origin of coordinates of the video. % and px formats are supported.
INVALIDPARAMETERVALUE_XPOS = 'InvalidParameterValue.XPos'

# The vertical position of the origin of the watermark relative to the origin of coordinates of the video. % and px formats are supported.
INVALIDPARAMETERVALUE_YPOS = 'InvalidParameterValue.YPos'

# Quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# Limit exceeded: the total number of new and old timestamps exceeds the limit.
LIMITEXCEEDED_KEYFRAMEDESCCOUNTREACHMAX = 'LimitExceeded.KeyFrameDescCountReachMax'

# Playlist length too large.
LIMITEXCEEDED_PLAYLIST = 'LimitExceeded.PlayList'

# Exceeds broadcast playlist total limit.
LIMITEXCEEDED_ROUNDPLAYS = 'LimitExceeded.RoundPlays'

# Running broadcast playlists exceed maximum quantity.
LIMITEXCEEDED_RUNNINGROUNDPLAYS = 'LimitExceeded.RunningRoundPlays'

# Limit exceeded: the total number of new and old tags exceeds the limit.
LIMITEXCEEDED_TAGCOUNTREACHMAX = 'LimitExceeded.TagCountReachMax'

# Limit exceeded: The number of templates exceeds the upper limit of 100. If you need more, please[Submit a ticket](https://console.tencentcloud.com/workorder/category).
LIMITEXCEEDED_TOOMUCHTEMPLATE = 'LimitExceeded.TooMuchTemplate'

# Missing parameter.
MISSINGPARAMETER = 'MissingParameter'

# Too many requests.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The resource does not exist: the cover does not exist.
RESOURCENOTFOUND_COVERURL = 'ResourceNotFound.CoverUrl'

# The resource does not exist: the file does not exist.
RESOURCENOTFOUND_FILENOTEXIST = 'ResourceNotFound.FileNotExist'

# The resource does not exist: figure.
RESOURCENOTFOUND_PERSON = 'ResourceNotFound.Person'

# The service is not activated.
RESOURCENOTFOUND_SERVICENOTEXIST = 'ResourceNotFound.ServiceNotExist'

# The resource does not exist: the template does not exist.
RESOURCENOTFOUND_TEMPLATENOTEXIST = 'ResourceNotFound.TemplateNotExist'

# The user does not exist.
RESOURCENOTFOUND_USERNOTEXIST = 'ResourceNotFound.UserNotExist'

# The resource does not exist: keyword.
RESOURCENOTFOUND_WORD = 'ResourceNotFound.Word'

# The resource is unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# Incorrect parameter: M3U8 of `MasterPlaylist` is not supported.
RESOURCEUNAVAILABLE_MASTERPLAYLIST = 'ResourceUnavailable.MasterPlaylist'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# 
UNAUTHORIZEDOPERATION_DOMAINRECORDNOTVERIFIED = 'UnauthorizedOperation.DomainRecordNotVerified'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# Unsupported operation.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# Non-empty categories cannot be deleted.
UNSUPPORTEDOPERATION_CLASSNOTEMPTY = 'UnsupportedOperation.ClassNotEmpty'
