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


# CAM signature/authentication error.
AUTHFAILURE = 'AuthFailure'

# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Operation failed: category level limit exceeded.
FAILEDOPERATION_CLASSLEVELLIMITEXCEEDED = 'FailedOperation.ClassLevelLimitExceeded'

# Operation failed: duplicated category name.
FAILEDOPERATION_CLASSNAMEDUPLICATE = 'FailedOperation.ClassNameDuplicate'

# Operation failed: Category not found.
FAILEDOPERATION_CLASSNOFOUND = 'FailedOperation.ClassNoFound'

# Operation failed: Unsupported cover type.
FAILEDOPERATION_COVERTYPE = 'FailedOperation.CoverType'

# Operation failed: Database operation failed.
FAILEDOPERATION_DBERROR = 'FailedOperation.DBError'

# Configuration cannot be changed during domain name deployment.
FAILEDOPERATION_DOMAINDEPLOYING = 'FailedOperation.DomainDeploying'

# User account exception.
FAILEDOPERATION_INVALIDACCOUNT = 'FailedOperation.InvalidAccount'

# The VOD service is not enabled.
FAILEDOPERATION_INVALIDVODUSER = 'FailedOperation.InvalidVodUser'

# Media is banned by the system.
FAILEDOPERATION_MEDIAFORBIDEDBYSYSTEM = 'FailedOperation.MediaForbidedBySystem'

# Operation failed: unsupported media type.
FAILEDOPERATION_MEDIATYPE = 'FailedOperation.MediaType'

# Network error.
FAILEDOPERATION_NETWORKERROR = 'FailedOperation.NetWorkError'

# No need for bitrate reduction.
FAILEDOPERATION_NONEEDTOREDUCEMEDIABITRATE = 'FailedOperation.NoNeedToReduceMediaBitrate'

# Operation failed: Parent class ID not found.
FAILEDOPERATION_PARENTIDNOFOUND = 'FailedOperation.ParentIdNoFound'

# Operation failed: The number of subcategories exceeds the limit.
FAILEDOPERATION_SUBCLASSLIMITEXCEEDED = 'FailedOperation.SubclassLimitExceeded'

# Operation failed: duplicate task.
FAILEDOPERATION_TASKDUPLICATE = 'FailedOperation.TaskDuplicate'

# Operation failed: Failed to upload the file to cos.
FAILEDOPERATION_UPLOADCOSFAIL = 'FailedOperation.UploadCosFail'

# Services for the user have been stopped.
FAILEDOPERATION_USERSTATUSINAVLID = 'FailedOperation.UserStatusInavlid'

# Internal error.
INTERNALERROR = 'InternalError'

# Internal error. Failed to access the DB.
INTERNALERROR_DBERROR = 'InternalError.DBError'

# Internal error: Failed to create a template ID.
INTERNALERROR_GENDEFINITION = 'InternalError.GenDefinition'

# Internal error: media file info error.
INTERNALERROR_GETFILEINFOERROR = 'InternalError.GetFileInfoError'

# Internal error: media list error.
INTERNALERROR_GETMEDIALISTERROR = 'InternalError.GetMediaListError'

# Time parsing error.
INTERNALERROR_TIMEPARSEERROR = 'InternalError.TimeParseError'

# Internal error: failed to refresh media file info.
INTERNALERROR_UPDATEMEDIAERROR = 'InternalError.UpdateMediaError'

# Internal error: Error uploading the cover image.
INTERNALERROR_UPLOADCOVERIMAGEERROR = 'InternalError.UploadCoverImageError'

# Internal error: Failed to upload the watermark image.
INTERNALERROR_UPLOADWATERMARKERROR = 'InternalError.UploadWatermarkError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# Task flow template name already exists.
INVALIDPARAMETER_EXISTEDPROCEDURENAME = 'InvalidParameter.ExistedProcedureName'

# Parameter value error. Expiration time.
INVALIDPARAMETER_EXPIRETIME = 'InvalidParameter.ExpireTime'

# Parameter error: Tag error.
INVALIDPARAMETER_LABELS = 'InvalidParameter.Labels'

# The task flow template name does not exist.
INVALIDPARAMETER_PROCEDURENAMENOTEXIST = 'InvalidParameter.ProcedureNameNotExist'

# Parameter value error. Storage region.
INVALIDPARAMETER_STORAGEREGION = 'InvalidParameter.StorageRegion'

# InvalidParameter.ViolationContent
INVALIDPARAMETER_VIOLATIONCONTENT = 'InvalidParameter.ViolationContent'

# Parameter value error.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Parameter value error: AddKeyFrameDescs conflicts with ClearKeyFrameDescs.
INVALIDPARAMETERVALUE_ADDKEYFRAMEDESCSANDCLEARKEYFRAMEDESCSCONFLICT = 'InvalidParameterValue.AddKeyFrameDescsAndClearKeyFrameDescsConflict'

# Parameter value error: AddKeyFrameDescs conflicts with DeleteKeyFrameDescs.
INVALIDPARAMETERVALUE_ADDKEYFRAMEDESCSANDDELETEKEYFRAMEDESCSCONFLICT = 'InvalidParameterValue.AddKeyFrameDescsAndDeleteKeyFrameDescsConflict'

# Parameter value error: AddTags conflicts with ClearTags.
INVALIDPARAMETERVALUE_ADDTAGSANDCLEARTAGSCONFLICT = 'InvalidParameterValue.AddTagsAndClearTagsConflict'

# Parameter value error: AddTags conflicts with DeleteTags.
INVALIDPARAMETERVALUE_ADDTAGSANDDELETETAGSCONFLICT = 'InvalidParameterValue.AddTagsAndDeleteTagsConflict'

# Parameter value error: AI analysis Definition.
INVALIDPARAMETERVALUE_AIANALYSISTASKDEFINITION = 'InvalidParameterValue.AiAnalysisTaskDefinition'

# Parameter value error: AI content review Definition.
INVALIDPARAMETERVALUE_AICONTENTREVIEWTASKDEFINITION = 'InvalidParameterValue.AiContentReviewTaskDefinition'

# Parameter value error: AI recognition Definition.
INVALIDPARAMETERVALUE_AIRECOGNITIONTASKDEFINITION = 'InvalidParameterValue.AiRecognitionTaskDefinition'

# The VOD service is not activated.
INVALIDPARAMETERVALUE_APPID = 'InvalidParameterValue.AppId'

# Area parameter error.
INVALIDPARAMETERVALUE_AREA = 'InvalidParameterValue.Area'

# Parameter error: audio stream bitrate.
INVALIDPARAMETERVALUE_AUDIOBITRATE = 'InvalidParameterValue.AudioBitrate'

# Parameter value error: AudioChannel.
INVALIDPARAMETERVALUE_AUDIOCHANNEL = 'InvalidParameterValue.AudioChannel'

# Parameter error: audio stream encoding format.
INVALIDPARAMETERVALUE_AUDIOCODEC = 'InvalidParameterValue.AudioCodec'

# Parameter error: audio stream sampling rate.
INVALIDPARAMETERVALUE_AUDIOSAMPLERATE = 'InvalidParameterValue.AudioSampleRate'

# Invalid audio/video bitrate.
INVALIDPARAMETERVALUE_BITRATE = 'InvalidParameterValue.Bitrate'

# Incorrect parameter value: the BlockConfidence parameter value is invalid.
INVALIDPARAMETERVALUE_BLOCKCONFIDENCE = 'InvalidParameterValue.BlockConfidence'

# Invalid file type.
INVALIDPARAMETERVALUE_CATEGORIES = 'InvalidParameterValue.Categories'

# Parameter value error: category ID.
INVALIDPARAMETERVALUE_CLASSID = 'InvalidParameterValue.ClassId'

# Parameter value error: ClassIds is invalid.
INVALIDPARAMETERVALUE_CLASSIDS = 'InvalidParameterValue.ClassIds'

# Parameter value error: ClassName is invalid.
INVALIDPARAMETERVALUE_CLASSNAME = 'InvalidParameterValue.ClassName'

# Intelligent classification control field parameter error.
INVALIDPARAMETERVALUE_CLASSIFCATIONCONFIGURE = 'InvalidParameterValue.ClassifcationConfigure'

# Parameter value error: The cropping time period is too long.
INVALIDPARAMETERVALUE_CLIPDURATION = 'InvalidParameterValue.ClipDuration'

# Invalid audio/video coding format.
INVALIDPARAMETERVALUE_CODEC = 'InvalidParameterValue.Codec'

# Invalid parameter value: ColumnCount.
INVALIDPARAMETERVALUE_COLUMNCOUNT = 'InvalidParameterValue.ColumnCount'

# Parameter error: description of this template.
INVALIDPARAMETERVALUE_COMMENT = 'InvalidParameterValue.Comment'

# Parameter error: Muxing format.
INVALIDPARAMETERVALUE_CONTAINER = 'InvalidParameterValue.Container'

# Parameter value error: ContainerType.
INVALIDPARAMETERVALUE_CONTAINERTYPE = 'InvalidParameterValue.ContainerType'

# Parameter value error: CoordinateOrigin.
INVALIDPARAMETERVALUE_COORDINATEORIGIN = 'InvalidParameterValue.CoordinateOrigin'

# Intelligent cover control field parameter error.
INVALIDPARAMETERVALUE_COVERCONFIGURE = 'InvalidParameterValue.CoverConfigure'

# Parameter value error: Cover Type.
INVALIDPARAMETERVALUE_COVERTYPE = 'InvalidParameterValue.CoverType'

# Parameter value error: Cover URL.
INVALIDPARAMETERVALUE_COVERURL = 'InvalidParameterValue.CoverUrl'

# Incorrect parameter value: the CutAndCrops parameter value is invalid.
INVALIDPARAMETERVALUE_CUTANDCROPS = 'InvalidParameterValue.CutAndCrops'

# Parameter value error. Time granularity.
INVALIDPARAMETERVALUE_DATAINTERVAL = 'InvalidParameterValue.DataInterval'

# Parameter value error. Data types.
INVALIDPARAMETERVALUE_DATATYPE = 'InvalidParameterValue.DataType'

# Parameter value error: Date.
INVALIDPARAMETERVALUE_DATE = 'InvalidParameterValue.Date'

# Parameter value error: The default face library filter tag is illegal.
INVALIDPARAMETERVALUE_DEFAULTLIBRARYLABELSET = 'InvalidParameterValue.DefaultLibraryLabelSet'

# Parameter error: Definition.
INVALIDPARAMETERVALUE_DEFINITION = 'InvalidParameterValue.Definition'

# Parameter error: Definitions.
INVALIDPARAMETERVALUE_DEFINITIONS = 'InvalidParameterValue.Definitions'

# Parameter value error: deletion of the default template is not allowed.
INVALIDPARAMETERVALUE_DELETEDEFAULTTEMPLATE = 'InvalidParameterValue.DeleteDefaultTemplate'

# Parameter value error: Description exceeds the length limit.
INVALIDPARAMETERVALUE_DESCRIPTION = 'InvalidParameterValue.Description'

# Invalid forbidden low-to-high bitrate switch value.
INVALIDPARAMETERVALUE_DISABLEHIGHERVIDEOBITRATE = 'InvalidParameterValue.DisableHigherVideoBitrate'

# Invalid forbidden low-to-high resolution switch value.
INVALIDPARAMETERVALUE_DISABLEHIGHERVIDEORESOLUTION = 'InvalidParameterValue.DisableHigherVideoResolution'

# Districts parameter value error.
INVALIDPARAMETERVALUE_DISTRICTS = 'InvalidParameterValue.Districts'

# Parameter error: non-existent domain name.
INVALIDPARAMETERVALUE_DOMAINNAME = 'InvalidParameterValue.DomainName'

# Malicious domain name. It cannot be added.
INVALIDPARAMETERVALUE_DOMAINNAMEINBLACKLIST = 'InvalidParameterValue.DomainNameInBlackList'

# Parameter value error: The domain name list is too large.
INVALIDPARAMETERVALUE_DOMAINNAMES = 'InvalidParameterValue.DomainNames'

# Invalid DRM type.
INVALIDPARAMETERVALUE_DRMTYPE = 'InvalidParameterValue.DrmType'

# Parameter value error: EndDate is invalid.
INVALIDPARAMETERVALUE_ENDDATE = 'InvalidParameterValue.EndDate'

# Parameter value error: EndTime is invalid.
INVALIDPARAMETERVALUE_ENDTIME = 'InvalidParameterValue.EndTime'

# Parameter error: invalid end time.
INVALIDPARAMETERVALUE_ENDTIMEOFFSET = 'InvalidParameterValue.EndTimeOffset'

# Duplicate name.
INVALIDPARAMETERVALUE_EXISTEDNAME = 'InvalidParameterValue.ExistedName'

# Parameter value error: Incorrect ExpireTime format.
INVALIDPARAMETERVALUE_EXPIRETIME = 'InvalidParameterValue.ExpireTime'

# ExpiredTime error.
INVALIDPARAMETERVALUE_EXPIREDTIME = 'InvalidParameterValue.ExpiredTime'

# Incorrect parameter value: the ExtendedParameter parameter value is invalid.
INVALIDPARAMETERVALUE_EXTENDEDPARAMETER = 'InvalidParameterValue.ExtendedParameter'

# Parameter value error: face duplication.
INVALIDPARAMETERVALUE_FACEDUPLICATE = 'InvalidParameterValue.FaceDuplicate'

# Parameter value error: The face library parameter is invalid.
INVALIDPARAMETERVALUE_FACELIBRARY = 'InvalidParameterValue.FaceLibrary'

# Parameter value error: The face score parameter value is invalid.
INVALIDPARAMETERVALUE_FACESCORE = 'InvalidParameterValue.FaceScore'

# FileId does not exist.
INVALIDPARAMETERVALUE_FILEID = 'InvalidParameterValue.FileId'

# FileIds parameter error.
INVALIDPARAMETERVALUE_FILEIDS = 'InvalidParameterValue.FileIds'

# FileIds array is empty.
INVALIDPARAMETERVALUE_FILEIDSEMPTY = 'InvalidParameterValue.FileIdsEmpty'

# FileIds array exceeds the limit
INVALIDPARAMETERVALUE_FILEIDSOVERLIMIT = 'InvalidParameterValue.FileIdsOverLimit'

# Parameter value error: too many FileIds.
INVALIDPARAMETERVALUE_FILEIDSTOOMANY = 'InvalidParameterValue.FileIdsTooMany'

# Parameter error: incorrect filling method.
INVALIDPARAMETERVALUE_FILLTYPE = 'InvalidParameterValue.FillType'

# Parameter error: whether to remove video should be 0 or 1.
INVALIDPARAMETERVALUE_FILTRATEAUDIO = 'InvalidParameterValue.FiltrateAudio'

# Parameter error: remove video.
INVALIDPARAMETERVALUE_FILTRATEVIDEO = 'InvalidParameterValue.FiltrateVideo'

# Parameter value error: Format.
INVALIDPARAMETERVALUE_FORMAT = 'InvalidParameterValue.Format'

# Parameter value error: When Format is webp, Width and Height are empty.
INVALIDPARAMETERVALUE_FORMATWEBPLACKWIDTHANDHEIGHT = 'InvalidParameterValue.FormatWebpLackWidthAndHeight'

# Parameter value error: When Format is webp, Width and Height cannot both be 0.
INVALIDPARAMETERVALUE_FORMATWEBPWIDTHANDHEIGHTBOTHZERO = 'InvalidParameterValue.FormatWebpWidthAndHeightBothZero'

# Parameter error: video frame rate.
INVALIDPARAMETERVALUE_FPS = 'InvalidParameterValue.Fps'

# Intelligent frame tagging control field parameter error.
INVALIDPARAMETERVALUE_FRAMETAGCONFIGURE = 'InvalidParameterValue.FrameTagConfigure'

# Parameter value error: FunctionArg.
INVALIDPARAMETERVALUE_FUNCTIONARG = 'InvalidParameterValue.FunctionArg'

# Parameter value error: FunctionName.
INVALIDPARAMETERVALUE_FUNCTIONNAME = 'InvalidParameterValue.FunctionName'

# Parameter error: height.
INVALIDPARAMETERVALUE_HEIGHT = 'InvalidParameterValue.Height'

# Intelligent highlights control parameter error.
INVALIDPARAMETERVALUE_HIGHLIGHTCONFIGURE = 'InvalidParameterValue.HighlightConfigure'

# The ImageContent parameter value is invalid.
INVALIDPARAMETERVALUE_IMAGECONTENT = 'InvalidParameterValue.ImageContent'

# Failed to decode the Base64-encoded image.
INVALIDPARAMETERVALUE_IMAGEDECODEERROR = 'InvalidParameterValue.ImageDecodeError'

# Parameter error: image watermark template.
INVALIDPARAMETERVALUE_IMAGETEMPLATE = 'InvalidParameterValue.ImageTemplate'

# Index parameter error.
INVALIDPARAMETERVALUE_INDEX = 'InvalidParameterValue.Index'

# Parameter value error. Interval is invalid.
INVALIDPARAMETERVALUE_INTERVAL = 'InvalidParameterValue.Interval'

# Parameter error. Invalid operation type.
INVALIDPARAMETERVALUE_INVALIDOPERATIONTYPE = 'InvalidParameterValue.InvalidOperationType'

# Parameter value error: incorrectly fixed parameters.
INVALIDPARAMETERVALUE_ISPERSISTENCE = 'InvalidParameterValue.IsPersistence'

# Invalid Isps parameter.
INVALIDPARAMETERVALUE_ISPS = 'InvalidParameterValue.Isps'

# ItemId error.
INVALIDPARAMETERVALUE_ITEMID = 'InvalidParameterValue.ItemId'

# Parameter value error: Dotting information content too long.
INVALIDPARAMETERVALUE_KEYFRAMEDESCCONTENTTOOLONG = 'InvalidParameterValue.KeyFrameDescContentTooLong'

# Incorrect parameter value: the LabelSet parameter value is invalid.
INVALIDPARAMETERVALUE_LABELSET = 'InvalidParameterValue.LabelSet'

# Parameter error: Tag error.
INVALIDPARAMETERVALUE_LABELS = 'InvalidParameterValue.Labels'

# Parameter error: Limit.
INVALIDPARAMETERVALUE_LIMIT = 'InvalidParameterValue.Limit'

# Parameter value error: Limit is too large.
INVALIDPARAMETERVALUE_LIMITTOOLARGE = 'InvalidParameterValue.LimitTooLarge'

# Invalid parameter value: MediaManifestContent.
INVALIDPARAMETERVALUE_MEDIAMANIFESTCONTENT = 'InvalidParameterValue.MediaManifestContent'

# Parameter value error: media storage path.
INVALIDPARAMETERVALUE_MEDIASTORAGEPATH = 'InvalidParameterValue.MediaStoragePath'

# Parameter value error: media type.
INVALIDPARAMETERVALUE_MEDIATYPE = 'InvalidParameterValue.MediaType'

# Parameter value error: Media file URL.
INVALIDPARAMETERVALUE_MEDIAURL = 'InvalidParameterValue.MediaUrl'

# Parameter error: Metric is invalid.
INVALIDPARAMETERVALUE_METRIC = 'InvalidParameterValue.Metric'

# Parameter value error: The default template is not allowed to be modified.
INVALIDPARAMETERVALUE_MODIFYDEFAULTTEMPLATE = 'InvalidParameterValue.ModifyDefaultTemplate'

# Parameter value error: Name exceeds the length limit.
INVALIDPARAMETERVALUE_NAME = 'InvalidParameterValue.Name'

# Invalid file name prefix.
INVALIDPARAMETERVALUE_NAMEPREFIXES = 'InvalidParameterValue.NamePrefixes'

# Too many elements in the Names array.
INVALIDPARAMETERVALUE_NAMES = 'InvalidParameterValue.Names'

# Parameter error: The file does not support unfreezing.
INVALIDPARAMETERVALUE_NOTRESTORABLE = 'InvalidParameterValue.NotRestorable'

# Parameter value error: Invalid object library parameter.
INVALIDPARAMETERVALUE_OBJECTLIBRARY = 'InvalidParameterValue.ObjectLibrary'

# Parameter value error. Offset is invalid.
INVALIDPARAMETERVALUE_OFFSET = 'InvalidParameterValue.Offset'

# Parameter value error: Offset is too large.
INVALIDPARAMETERVALUE_OFFSETTOOLARGE = 'InvalidParameterValue.OffsetTooLarge'

# Parameter value error: Operation is invalid.
INVALIDPARAMETERVALUE_OPERATION = 'InvalidParameterValue.Operation'

# Parameter value error. The original storage type of the file is abnormal.
INVALIDPARAMETERVALUE_ORIGINALSTORAGECLASS = 'InvalidParameterValue.OriginalStorageClass'

# Parameter value error: Incorrect output media file type.
INVALIDPARAMETERVALUE_OUTPUTMEDIATYPE = 'InvalidParameterValue.OutputMediaType'

# Parameter value error: ParentId is invalid.
INVALIDPARAMETERVALUE_PARENTID = 'InvalidParameterValue.ParentId'

# Parameter value error: incorrect human face image format.
INVALIDPARAMETERVALUE_PICFORMATERROR = 'InvalidParameterValue.PicFormatError'

# Parameter value error: incorrect precision parameter.
INVALIDPARAMETERVALUE_PRECISION = 'InvalidParameterValue.Precision'

# Invalid parameter value: incorrect Procedure.
INVALIDPARAMETERVALUE_PROCEDURE = 'InvalidParameterValue.Procedure'

# Task flow template name is invalid.
INVALIDPARAMETERVALUE_PROCEDURENAME = 'InvalidParameterValue.ProcedureName'

# Parameter value error: Quality.
INVALIDPARAMETERVALUE_QUALITY = 'InvalidParameterValue.Quality'

# Invalid parameter value: RemoveAudio.
INVALIDPARAMETERVALUE_REMOVEAUDIO = 'InvalidParameterValue.RemoveAudio'

# Invalid parameter value: RemoveVideo.
INVALIDPARAMETERVALUE_REMOVEVIDEO = 'InvalidParameterValue.RemoveVideo'

# Parameter error: RepeatType is invalid.
INVALIDPARAMETERVALUE_REPEATTYPE = 'InvalidParameterValue.RepeatType'

# Parameter error: Resolution error.
INVALIDPARAMETERVALUE_RESOLUTION = 'InvalidParameterValue.Resolution'

# Invalid ResolutionAdaptive.
INVALIDPARAMETERVALUE_RESOLUTIONADAPTIVE = 'InvalidParameterValue.ResolutionAdaptive'

# Parameter error: Invalid number of unfreeze days.
INVALIDPARAMETERVALUE_RESTOREDAY = 'InvalidParameterValue.RestoreDay'

# Parameter error: Unsupported thawing mode.
INVALIDPARAMETERVALUE_RESTORETIER = 'InvalidParameterValue.RestoreTier'

# Incorrect parameter value: the ReviewConfidence parameter value is invalid.
INVALIDPARAMETERVALUE_REVIEWCONFIDENCE = 'InvalidParameterValue.ReviewConfidence'

# Incorrect parameter value: the ReviewWallSwitch parameter value is invalid.
INVALIDPARAMETERVALUE_REVIEWWALLSWITCH = 'InvalidParameterValue.ReviewWallSwitch'

# A playlist with the same ID already exists.
INVALIDPARAMETERVALUE_ROUNDPLAYALREADYEXISTS = 'InvalidParameterValue.RoundPlayAlreadyExists'

# RoundPlayId parameter error.
INVALIDPARAMETERVALUE_ROUNDPLAYID = 'InvalidParameterValue.RoundPlayId'

# Invalid RoundPlaylist parameter length.
INVALIDPARAMETERVALUE_ROUNDPLAYLIST = 'InvalidParameterValue.RoundPlaylist'

# Invalid parameter value: RowCount.
INVALIDPARAMETERVALUE_ROWCOUNT = 'InvalidParameterValue.RowCount'

# Invalid parameter value: SampleInterval.
INVALIDPARAMETERVALUE_SAMPLEINTERVAL = 'InvalidParameterValue.SampleInterval'

# Invalid audio sample rate.
INVALIDPARAMETERVALUE_SAMPLERATE = 'InvalidParameterValue.SampleRate'

# Parameter value error: SampleType.
INVALIDPARAMETERVALUE_SAMPLETYPE = 'InvalidParameterValue.SampleType'

# Invalid ScenarioType parameter value.
INVALIDPARAMETERVALUE_SCENARIOTYPE = 'InvalidParameterValue.ScenarioType'

# Parameter error: Invalid Scheme.
INVALIDPARAMETERVALUE_SCHEME = 'InvalidParameterValue.Scheme'

# Domain name does not have https enabled.
INVALIDPARAMETERVALUE_SCHEMECONFLICT = 'InvalidParameterValue.SchemeConflict'

# Incorrect parameter value: the ScreenshotInterval parameter value is invalid.
INVALIDPARAMETERVALUE_SCREENSHOTINTERVAL = 'InvalidParameterValue.ScreenshotInterval'

# SessionContext is too long.
INVALIDPARAMETERVALUE_SESSIONCONTEXTTOOLONG = 'InvalidParameterValue.SessionContextTooLong'

# Duplicate recognition code. Request deduplicated.
INVALIDPARAMETERVALUE_SESSIONID = 'InvalidParameterValue.SessionId'

# SessionId is too long.
INVALIDPARAMETERVALUE_SESSIONIDTOOLONG = 'InvalidParameterValue.SessionIdTooLong'

# Parameter value error: Sort is invalid.
INVALIDPARAMETERVALUE_SORT = 'InvalidParameterValue.Sort'

# Incorrect parameter: audio channel mode.
INVALIDPARAMETERVALUE_SOUNDSYSTEM = 'InvalidParameterValue.SoundSystem'

# Parameter value error: SourceType is invalid.
INVALIDPARAMETERVALUE_SOURCETYPE = 'InvalidParameterValue.SourceType'

# Unknown media file source.
INVALIDPARAMETERVALUE_SOURCETYPES = 'InvalidParameterValue.SourceTypes'

# Source file error.
INVALIDPARAMETERVALUE_SRCFILE = 'InvalidParameterValue.SrcFile'

# Parameter value error: StartDate is invalid.
INVALIDPARAMETERVALUE_STARTDATE = 'InvalidParameterValue.StartDate'

# Parameter value error: StartTime is invalid.
INVALIDPARAMETERVALUE_STARTTIME = 'InvalidParameterValue.StartTime'

# Parameter error: invalid start time.
INVALIDPARAMETERVALUE_STARTTIMEOFFSET = 'InvalidParameterValue.StartTimeOffset'

# Parameter value error: invalid manual confirmation result.
INVALIDPARAMETERVALUE_STATUS = 'InvalidParameterValue.Status'

# Parameter value error. The target storage type is not in the available values.
INVALIDPARAMETERVALUE_STORAGECLASS = 'InvalidParameterValue.StorageClass'

# Parameter value error: storage region.
INVALIDPARAMETERVALUE_STORAGEREGION = 'InvalidParameterValue.StorageRegion'

# Parameter value error. StorageRegions is invalid.
INVALIDPARAMETERVALUE_STORAGEREGIONS = 'InvalidParameterValue.StorageRegions'

# Parameter value error: StorageType.
INVALIDPARAMETERVALUE_STORAGETYPE = 'InvalidParameterValue.StorageType'

# Parameter value error: StreamId is invalid.
INVALIDPARAMETERVALUE_STREAMIDINVALID = 'InvalidParameterValue.StreamIdInvalid'

# Invalid stream ID parameter.
INVALIDPARAMETERVALUE_STREAMIDS = 'InvalidParameterValue.StreamIds'

# Parameter value error: app ID.
INVALIDPARAMETERVALUE_SUBAPPID = 'InvalidParameterValue.SubAppId'

# Parameter value error: Invalid SubtitleFormat parameter.
INVALIDPARAMETERVALUE_SUBTITLEFORMAT = 'InvalidParameterValue.SubtitleFormat'

# Parameter value error: SVG is empty.
INVALIDPARAMETERVALUE_SVGTEMPLATE = 'InvalidParameterValue.SvgTemplate'

# Parameter value error: SVG height.
INVALIDPARAMETERVALUE_SVGTEMPLATEHEIGHT = 'InvalidParameterValue.SvgTemplateHeight'

# Parameter value error: SVG width.
INVALIDPARAMETERVALUE_SVGTEMPLATEWIDTH = 'InvalidParameterValue.SvgTemplateWidth'

# Parameter value error: invalid Switch parameter value.
INVALIDPARAMETERVALUE_SWITCH = 'InvalidParameterValue.Switch'

# Parameter value error: TEHD Type is invalid.
INVALIDPARAMETERVALUE_TEHDTYPE = 'InvalidParameterValue.TEHDType'

# Intelligent tag control field parameter error.
INVALIDPARAMETERVALUE_TAGCONFIGURE = 'InvalidParameterValue.TagConfigure'

# Parameter value error: Tag too long.
INVALIDPARAMETERVALUE_TAGTOOLONG = 'InvalidParameterValue.TagTooLong'

# Parameter value error: Tags is invalid.
INVALIDPARAMETERVALUE_TAGS = 'InvalidParameterValue.Tags'

# The task ID does not exist.
INVALIDPARAMETERVALUE_TASKID = 'InvalidParameterValue.TaskId'

# Parameter value error: search text.
INVALIDPARAMETERVALUE_TEXT = 'InvalidParameterValue.Text'

# Parameter error: Text opacity.
INVALIDPARAMETERVALUE_TEXTALPHA = 'InvalidParameterValue.TextAlpha'

# Parameter error: text template.
INVALIDPARAMETERVALUE_TEXTTEMPLATE = 'InvalidParameterValue.TextTemplate'

# Parameter value error: Invalid Thumbnail parameter value.
INVALIDPARAMETERVALUE_THUMBNAILS = 'InvalidParameterValue.Thumbnails'

# Parameter value error: TimeType.
INVALIDPARAMETERVALUE_TIMETYPE = 'InvalidParameterValue.TimeType'

# Type parameter value error.
INVALIDPARAMETERVALUE_TYPE = 'InvalidParameterValue.Type'

# Invalid Types parameter.
INVALIDPARAMETERVALUE_TYPES = 'InvalidParameterValue.Types'

# Duplicate recognition code within one day. Request deduplicated.
INVALIDPARAMETERVALUE_UNIQUEIDENTIFIER = 'InvalidParameterValue.UniqueIdentifier'

# Domain name cannot be set.
INVALIDPARAMETERVALUE_UNSUPPORTDOMAIN = 'InvalidParameterValue.UnsupportDomain'

# Parameter value error: The file does not support this unfreeze method.
INVALIDPARAMETERVALUE_UNSUPPORTEDRESTORETIER = 'InvalidParameterValue.UnsupportedRestoreTier'

# Parameter value error. Unsupported target storage type. Deep archive is only supported in select parks.
INVALIDPARAMETERVALUE_UNSUPPORTEDSTORAGECLASS = 'InvalidParameterValue.UnsupportedStorageClass'

# Parameter value error. Unsupported storage type switch.
INVALIDPARAMETERVALUE_UNSUPPORTEDTRANSITION = 'InvalidParameterValue.UnsupportedTransition'

# Parameter error: Invalid Url.
INVALIDPARAMETERVALUE_URL = 'InvalidParameterValue.Url'

# Parameter value error: The custom face library filter tag is illegal.
INVALIDPARAMETERVALUE_USERDEFINELIBRARYLABELSET = 'InvalidParameterValue.UserDefineLibraryLabelSet'

# Parameter error: vcrf.
INVALIDPARAMETERVALUE_VCRF = 'InvalidParameterValue.Vcrf'

# Parameter error: video stream bitrate.
INVALIDPARAMETERVALUE_VIDEOBITRATE = 'InvalidParameterValue.VideoBitrate'

# Parameter error: video stream encoding format.
INVALIDPARAMETERVALUE_VIDEOCODEC = 'InvalidParameterValue.VideoCodec'

# Invalid Vids parameter.
INVALIDPARAMETERVALUE_VIDS = 'InvalidParameterValue.Vids'

# Parameter value error: VOD session.
INVALIDPARAMETERVALUE_VODSESSIONKEY = 'InvalidParameterValue.VodSessionKey'

# Parameter value error: Invalid Watermarks value.
INVALIDPARAMETERVALUE_WATERMARKS = 'InvalidParameterValue.Watermarks'

# Parameter error: width.
INVALIDPARAMETERVALUE_WIDTH = 'InvalidParameterValue.Width'

# Horizontal position of the watermark origin from the origin of coordinates of the video image. Supports % and px formats.
INVALIDPARAMETERVALUE_XPOS = 'InvalidParameterValue.XPos'

# Vertical position of the watermark origin from the origin of coordinates of the video image. Supports % and px formats.
INVALIDPARAMETERVALUE_YPOS = 'InvalidParameterValue.YPos'

# The quota limit is exceeded.
LIMITEXCEEDED = 'LimitExceeded'

# Exceed the limit: The total count of new and old dotting information exceeds the limit.
LIMITEXCEEDED_KEYFRAMEDESCCOUNTREACHMAX = 'LimitExceeded.KeyFrameDescCountReachMax'

# Playlist length is too large.
LIMITEXCEEDED_PLAYLIST = 'LimitExceeded.PlayList'

# The quota limit is exceeded.
LIMITEXCEEDED_QUOTA = 'LimitExceeded.Quota'

# The playlist length exceeds the upper limit.
LIMITEXCEEDED_ROUNDPLAYLIST = 'LimitExceeded.RoundPlaylist'

# Exceeds the total number of playlists limit.
LIMITEXCEEDED_ROUNDPLAYS = 'LimitExceeded.RoundPlays'

# The number of running playlists exceeds the maximum limit.
LIMITEXCEEDED_RUNNINGROUNDPLAYS = 'LimitExceeded.RunningRoundPlays'

# Exceed the limit: The total number of new and old tags exceeds the limit.
LIMITEXCEEDED_TAGCOUNTREACHMAX = 'LimitExceeded.TagCountReachMax'

# Exceed the limit: The number of templates exceeds the upper limit of 100. If needed, submit a ticket (https://console.cloud.tencent.com/workorder/category).
LIMITEXCEEDED_TOOMUCHTEMPLATE = 'LimitExceeded.TooMuchTemplate'

# Parameters are missing.
MISSINGPARAMETER = 'MissingParameter'

# Number of requests exceeds the frequency limit.
REQUESTLIMITEXCEEDED = 'RequestLimitExceeded'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# Resource does not exist: cover not found.
RESOURCENOTFOUND_COVERURL = 'ResourceNotFound.CoverUrl'

# Resource does not exist: file not found.
RESOURCENOTFOUND_FILENOTEXIST = 'ResourceNotFound.FileNotExist'

# Resource does not exist: person.
RESOURCENOTFOUND_PERSON = 'ResourceNotFound.Person'

# The service is not activated.
RESOURCENOTFOUND_SERVICENOTEXIST = 'ResourceNotFound.ServiceNotExist'

# Resource does not exist: template does not exist.
RESOURCENOTFOUND_TEMPLATENOTEXIST = 'ResourceNotFound.TemplateNotExist'

# The user does not exist.
RESOURCENOTFOUND_USERNOTEXIST = 'ResourceNotFound.UserNotExist'

# Resource does not exist: keyword.
RESOURCENOTFOUND_WORD = 'ResourceNotFound.Word'

# Resources are unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# Parameter error: M3u8 of MasterPlaylist is not supported.
RESOURCEUNAVAILABLE_MASTERPLAYLIST = 'ResourceUnavailable.MasterPlaylist'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# Domain resolution verification failed
UNAUTHORIZEDOPERATION_DOMAINRECORDNOTVERIFIED = 'UnauthorizedOperation.DomainRecordNotVerified'

# Unknown parameter error.
UNKNOWNPARAMETER = 'UnknownParameter'

# The operation is not supported.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# Deletion is not supported for non-empty categories.
UNSUPPORTEDOPERATION_CLASSNOTEMPTY = 'UnsupportedOperation.ClassNotEmpty'
