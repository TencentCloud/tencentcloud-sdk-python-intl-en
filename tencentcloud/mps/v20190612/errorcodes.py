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


# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Operation failed: notification has already been set for the bucket.
FAILEDOPERATION_BUCKETNOTIFYALREADYEXIST = 'FailedOperation.BucketNotifyAlreadyExist'

# Operation failed: COS service is suspended.
FAILEDOPERATION_COSSTATUSINAVLID = 'FailedOperation.CosStatusInavlid'

# Resource generation failed.
FAILEDOPERATION_GENERATERESOURCE = 'FailedOperation.GenerateResource'

# Operation failed: Error getting the source notification.
FAILEDOPERATION_GETSOURCENOTIFY = 'FailedOperation.GetSourceNotify'

# Operation failed: unauthorized MPS user.
FAILEDOPERATION_INVALIDMPSUSER = 'FailedOperation.InvalidMpsUser'

# Operation failed: invalid user.
FAILEDOPERATION_INVALIDUSER = 'FailedOperation.InvalidUser'

# Operation failed: Error setting the source notification.
FAILEDOPERATION_SETSOURCENOTIFY = 'FailedOperation.SetSourceNotify'

# Internal error.
INTERNALERROR = 'InternalError'

# Data error.
INTERNALERROR_ACCESSDBERROR = 'InternalError.AccessDBError'

# Internal error: failed to generate template ID.
INTERNALERROR_GENDEFINITION = 'InternalError.GenDefinition'

# Internal error: failed to upload watermark image.
INTERNALERROR_UPLOADWATERMARKERROR = 'InternalError.UploadWatermarkError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# InvalidParameter.Id
INVALIDPARAMETER_ID = 'InvalidParameter.Id'

# InvalidParameter.NotFound
INVALIDPARAMETER_NOTFOUND = 'InvalidParameter.NotFound'

# Incorrect parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The value of the hotword lexicon configuration parameter is incorrect.
INVALIDPARAMETERVALUE_ASRHOTWORDSCONFIGURE = 'InvalidParameterValue.AsrHotWordsConfigure'

# The value of the hotword lexicon ID parameter is incorrect.
INVALIDPARAMETERVALUE_ASRHOTWORDSLIBRARYID = 'InvalidParameterValue.AsrHotWordsLibraryId'

# The value of the hotword lexicon switch parameter is incorrect.
INVALIDPARAMETERVALUE_ASRHOTWORDSSWITCH = 'InvalidParameterValue.AsrHotWordsSwitch'

# Parameter error: Audio stream bitrate.
INVALIDPARAMETERVALUE_AUDIOBITRATE = 'InvalidParameterValue.AudioBitrate'

# Incorrect parameter value: AudioChannel.
INVALIDPARAMETERVALUE_AUDIOCHANNEL = 'InvalidParameterValue.AudioChannel'

# Parameter error: audio stream codec.
INVALIDPARAMETERVALUE_AUDIOCODEC = 'InvalidParameterValue.AudioCodec'

# Parameter error: audio stream sample rate.
INVALIDPARAMETERVALUE_AUDIOSAMPLERATE = 'InvalidParameterValue.AudioSampleRate'

# Invalid audio/video bitrate.
INVALIDPARAMETERVALUE_BITRATE = 'InvalidParameterValue.Bitrate'

# Incorrect parameter value: the value of the `BlockConfidence` parameter is invalid.
INVALIDPARAMETERVALUE_BLOCKCONFIDENCE = 'InvalidParameterValue.BlockConfidence'

# Incorrect parameter value: the control field parameter for intelligent categorization is incorrect.
INVALIDPARAMETERVALUE_CLASSIFCATIONCONFIGURE = 'InvalidParameterValue.ClassifcationConfigure'

# Invalid audio/video codec.
INVALIDPARAMETERVALUE_CODEC = 'InvalidParameterValue.Codec'

# Incorrect parameter value: ColumnCount.
INVALIDPARAMETERVALUE_COLUMNCOUNT = 'InvalidParameterValue.ColumnCount'

# Parameter error: template description.
INVALIDPARAMETERVALUE_COMMENT = 'InvalidParameterValue.Comment'

# Parameter error: container format.
INVALIDPARAMETERVALUE_CONTAINER = 'InvalidParameterValue.Container'

# Incorrect parameter value: ContainerType.
INVALIDPARAMETERVALUE_CONTAINERTYPE = 'InvalidParameterValue.ContainerType'

# Incorrect parameter value: CoordinateOrigin.
INVALIDPARAMETERVALUE_COORDINATEORIGIN = 'InvalidParameterValue.CoordinateOrigin'

# Incorrect parameter value: the control field parameter for intelligent cover generation is incorrect.
INVALIDPARAMETERVALUE_COVERCONFIGURE = 'InvalidParameterValue.CoverConfigure'

# Incorrect parameter value: the default face library filter tag is invalid.
INVALIDPARAMETERVALUE_DEFAULTLIBRARYLABELSET = 'InvalidParameterValue.DefaultLibraryLabelSet'

# Parameter error: Definition.
INVALIDPARAMETERVALUE_DEFINITION = 'InvalidParameterValue.Definition'

# Parameter error: Definitions.
INVALIDPARAMETERVALUE_DEFINITIONS = 'InvalidParameterValue.Definitions'

# Incorrect parameter value: the default template cannot be deleted.
INVALIDPARAMETERVALUE_DELETEDEFAULTTEMPLATE = 'InvalidParameterValue.DeleteDefaultTemplate'

# 
INVALIDPARAMETERVALUE_DESTINATIONLANGUAGE = 'InvalidParameterValue.DestinationLanguage'

# Invalid switch value used to prohibit transcoding from low bitrate to high bitrate.
INVALIDPARAMETERVALUE_DISABLEHIGHERVIDEOBITRATE = 'InvalidParameterValue.DisableHigherVideoBitrate'

# Invalid switch value used to prohibit transcoding from low resolution to high resolution.
INVALIDPARAMETERVALUE_DISABLEHIGHERVIDEORESOLUTION = 'InvalidParameterValue.DisableHigherVideoResolution'

# The enabled detection items of the template are empty.
INVALIDPARAMETERVALUE_EMPTYDETECTITEM = 'InvalidParameterValue.EmptyDetectItem'

# Incorrect parameter value: duplicated face.
INVALIDPARAMETERVALUE_FACEDUPLICATE = 'InvalidParameterValue.FaceDuplicate'

# Incorrect parameter value: invalid face library parameter.
INVALIDPARAMETERVALUE_FACELIBRARY = 'InvalidParameterValue.FaceLibrary'

# Incorrect parameter value: the value of the face score parameter is invalid.
INVALIDPARAMETERVALUE_FACESCORE = 'InvalidParameterValue.FaceScore'

# Invalid parameter: incorrect fill type.
INVALIDPARAMETERVALUE_FILLTYPE = 'InvalidParameterValue.FillType'

# Incorrect parameter value: Format.
INVALIDPARAMETERVALUE_FORMAT = 'InvalidParameterValue.Format'

# Incorrect parameter value: `Format` is `webp`, but both `Width` and `Height` are empty.
INVALIDPARAMETERVALUE_FORMATWEBPLACKWIDTHANDHEIGHT = 'InvalidParameterValue.FormatWebpLackWidthAndHeight'

# Incorrect parameter value: when `Format` is `webp`, `Width` and `Height` cannot be both 0.
INVALIDPARAMETERVALUE_FORMATWEBPWIDTHANDHEIGHTBOTHZERO = 'InvalidParameterValue.FormatWebpWidthAndHeightBothZero'

# Parameter error: video frame rate.
INVALIDPARAMETERVALUE_FPS = 'InvalidParameterValue.Fps'

# Incorrect parameter value: the control field parameter for intelligent frame-specific tagging is incorrect.
INVALIDPARAMETERVALUE_FRAMETAGCONFIGURE = 'InvalidParameterValue.FrameTagConfigure'

# Incorrect parameter value: FunctionArg.
INVALIDPARAMETERVALUE_FUNCTIONARG = 'InvalidParameterValue.FunctionArg'

# Incorrect parameter value: FunctionName.
INVALIDPARAMETERVALUE_FUNCTIONNAME = 'InvalidParameterValue.FunctionName'

# Invalid GOP value.
INVALIDPARAMETERVALUE_GOP = 'InvalidParameterValue.Gop'

# Parameter error: height.
INVALIDPARAMETERVALUE_HEIGHT = 'InvalidParameterValue.Height'

# Parameter error. The hotword lexicon does not exist.
INVALIDPARAMETERVALUE_HOTWORDSNOTEXIST = 'InvalidParameterValue.HotWordsNotExist'

# Hot word vocabulary format error. see the hot word configuration instruction document (https://intl.cloud.tencent.com/document/product/862/116244?from_cn_redirect=1#afc37e17-2786-4289-9bc3-8e24435d3f45).
INVALIDPARAMETERVALUE_HOTWORDSFORMATERROR = 'InvalidParameterValue.HotwordsFormatError'

# Invalid ImageContent
INVALIDPARAMETERVALUE_IMAGECONTENT = 'InvalidParameterValue.ImageContent'

# Parameter error: image watermarking template.
INVALIDPARAMETERVALUE_IMAGETEMPLATE = 'InvalidParameterValue.ImageTemplate'

# Incorrect input parameters.
INVALIDPARAMETERVALUE_INPUTINFO = 'InvalidParameterValue.InputInfo'

# The value of the parsed `Content` is invalid.
INVALIDPARAMETERVALUE_INVALIDCONTENT = 'InvalidParameterValue.InvalidContent'

# Invalid operation type.
INVALIDPARAMETERVALUE_INVALIDOPERATIONTYPE = 'InvalidParameterValue.InvalidOperationType'

# Incorrect parameter value: invalid `LabelSet` value.
INVALIDPARAMETERVALUE_LABELSET = 'InvalidParameterValue.LabelSet'

# Parameter error: Limit.
INVALIDPARAMETERVALUE_LIMIT = 'InvalidParameterValue.Limit'

# Incorrect parameter value: the default template cannot be modified.
INVALIDPARAMETERVALUE_MODIFYDEFAULTTEMPLATE = 'InvalidParameterValue.ModifyDefaultTemplate'

# Incorrect parameter value: `Name` exceeds the length limit.
INVALIDPARAMETERVALUE_NAME = 'InvalidParameterValue.Name'

# Tasks not in processing status are not supported.
INVALIDPARAMETERVALUE_NOTPROCESSINGTASK = 'InvalidParameterValue.NotProcessingTask'

# Incorrect parameter value: object library parameter is invalid.
INVALIDPARAMETERVALUE_OBJECTLIBRARY = 'InvalidParameterValue.ObjectLibrary'

# Incorrect parameter value: incorrect face image format.
INVALIDPARAMETERVALUE_PICFORMATERROR = 'InvalidParameterValue.PicFormatError'

# Incorrect parameter value: Quality.
INVALIDPARAMETERVALUE_QUALITY = 'InvalidParameterValue.Quality'

# Incorrect parameter value: RemoveAudio.
INVALIDPARAMETERVALUE_REMOVEAUDIO = 'InvalidParameterValue.RemoveAudio'

# Incorrect parameter value: RemoveVideo.
INVALIDPARAMETERVALUE_REMOVEVIDEO = 'InvalidParameterValue.RemoveVideo'

# Parameter error: invalid `RepeatType`.
INVALIDPARAMETERVALUE_REPEATTYPE = 'InvalidParameterValue.RepeatType'

# Parameter error: Incorrect resolution.
INVALIDPARAMETERVALUE_RESOLUTION = 'InvalidParameterValue.Resolution'

# Invalid ResolutionAdaptive
INVALIDPARAMETERVALUE_RESOLUTIONADAPTIVE = 'InvalidParameterValue.ResolutionAdaptive'

# Incorrect parameter value: The value of the `ReviewConfidence` parameter is invalid.
INVALIDPARAMETERVALUE_REVIEWCONFIDENCE = 'InvalidParameterValue.ReviewConfidence'

# Incorrect parameter value: RowCount.
INVALIDPARAMETERVALUE_ROWCOUNT = 'InvalidParameterValue.RowCount'

# Incorrect parameter value: SampleInterval.
INVALIDPARAMETERVALUE_SAMPLEINTERVAL = 'InvalidParameterValue.SampleInterval'

# Invalid audio sample rate.
INVALIDPARAMETERVALUE_SAMPLERATE = 'InvalidParameterValue.SampleRate'

# Incorrect parameter value: SampleType.
INVALIDPARAMETERVALUE_SAMPLETYPE = 'InvalidParameterValue.SampleType'

# `SessionContext` is too long.
INVALIDPARAMETERVALUE_SESSIONCONTEXTTOOLONG = 'InvalidParameterValue.SessionContextTooLong'

# The deduplication ID already exists. The request is removed due to duplication.
INVALIDPARAMETERVALUE_SESSIONID = 'InvalidParameterValue.SessionId'

# `SessionId` is too long.
INVALIDPARAMETERVALUE_SESSIONIDTOOLONG = 'InvalidParameterValue.SessionIdTooLong'

# Invalid parameter: incorrect audio channel system.
INVALIDPARAMETERVALUE_SOUNDSYSTEM = 'InvalidParameterValue.SoundSystem'

# 
INVALIDPARAMETERVALUE_SOURCELANGUAGE = 'InvalidParameterValue.SourceLanguage'

# Source file error.
INVALIDPARAMETERVALUE_SRCFILE = 'InvalidParameterValue.SrcFile'

# Incorrect parameter value: The value of the `SubtitleFormat` parameter is invalid.
INVALIDPARAMETERVALUE_SUBTITLEFORMAT = 'InvalidParameterValue.SubtitleFormat'

# The value of the subtitle language type is incorrect.
INVALIDPARAMETERVALUE_SUBTITLETYPE = 'InvalidParameterValue.SubtitleType'

# Incorrect parameter value: SVG is empty.
INVALIDPARAMETERVALUE_SVGTEMPLATE = 'InvalidParameterValue.SvgTemplate'

# Incorrect parameter value: SVG height.
INVALIDPARAMETERVALUE_SVGTEMPLATEHEIGHT = 'InvalidParameterValue.SvgTemplateHeight'

# Incorrect parameter value: SVG width.
INVALIDPARAMETERVALUE_SVGTEMPLATEWIDTH = 'InvalidParameterValue.SvgTemplateWidth'

# Incorrect parameter value: invalid `Switch` value.
INVALIDPARAMETERVALUE_SWITCH = 'InvalidParameterValue.Switch'

# Incorrect parameter value: invalid `TEHD Type` .
INVALIDPARAMETERVALUE_TEHDTYPE = 'InvalidParameterValue.TEHDType'

# Incorrect parameter value: the control field parameter for intelligent tagging is incorrect.
INVALIDPARAMETERVALUE_TAGCONFIGURE = 'InvalidParameterValue.TagConfigure'

# The task ID does not exist.
INVALIDPARAMETERVALUE_TASKID = 'InvalidParameterValue.TaskId'

# Parameter error: text transparency.
INVALIDPARAMETERVALUE_TEXTALPHA = 'InvalidParameterValue.TextAlpha'

# Parameter error: text template.
INVALIDPARAMETERVALUE_TEXTTEMPLATE = 'InvalidParameterValue.TextTemplate'

# The value of the target language parameter is incorrect.
INVALIDPARAMETERVALUE_TRANSLATEDSTLANGUAGE = 'InvalidParameterValue.TranslateDstLanguage'

# The value of the translation switch parameter is incorrect.
INVALIDPARAMETERVALUE_TRANSLATESWITCH = 'InvalidParameterValue.TranslateSwitch'

# Parameter error: incorrect `Type` value.
INVALIDPARAMETERVALUE_TYPE = 'InvalidParameterValue.Type'

# Unknown detection category.
INVALIDPARAMETERVALUE_UNKNOWNCATEGORY = 'InvalidParameterValue.UnknownCategory'

# Incorrect parameter value: the custom face library filter tag is invalid.
INVALIDPARAMETERVALUE_USERDEFINELIBRARYLABELSET = 'InvalidParameterValue.UserDefineLibraryLabelSet'

# Parameter error: video stream bitrate.
INVALIDPARAMETERVALUE_VIDEOBITRATE = 'InvalidParameterValue.VideoBitrate'

# Parameter error: video stream codec.
INVALIDPARAMETERVALUE_VIDEOCODEC = 'InvalidParameterValue.VideoCodec'

# The value of the video source language parameter is incorrect.
INVALIDPARAMETERVALUE_VIDEOSRCLANGUAGE = 'InvalidParameterValue.VideoSrcLanguage'

# Parameter error: Wwdth.
INVALIDPARAMETERVALUE_WIDTH = 'InvalidParameterValue.Width'

# The horizontal position of the origin of the watermark relative to the origin of coordinates of the video. % and px formats are supported.
INVALIDPARAMETERVALUE_XPOS = 'InvalidParameterValue.XPos'

# The vertical position of the origin of the watermark relative to the origin of coordinates of the video. % and px formats are supported.
INVALIDPARAMETERVALUE_YPOS = 'InvalidParameterValue.YPos'

# The number of created hotword lexicons has reached the default upper limit.
LIMITEXCEEDED_TOOMUCHHOTWORDS = 'LimitExceeded.TooMuchHotWords'

# The number of created large hotword lexicons has reached the upper limit.
LIMITEXCEEDED_TOOMUCHLARGEHOTWORDS = 'LimitExceeded.TooMuchLargeHotWords'

# Limit reached: the number of templates exceeds the limit.
LIMITEXCEEDED_TOOMUCHTEMPLATE = 'LimitExceeded.TooMuchTemplate'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The resource does not exist: invalid COS bucket name.
RESOURCENOTFOUND_COSBUCKETNAMEINVALID = 'ResourceNotFound.CosBucketNameInvalid'

# The resource does not exist: the COS bucket does not exist.
RESOURCENOTFOUND_COSBUCKETNOTEXIST = 'ResourceNotFound.CosBucketNotExist'

# The resource does not exist: figure.
RESOURCENOTFOUND_PERSON = 'ResourceNotFound.Person'

# The resource does not exist: the template does not exist.
RESOURCENOTFOUND_TEMPLATENOTEXIST = 'ResourceNotFound.TemplateNotExist'

# The resource does not exist: Keyword.
RESOURCENOTFOUND_WORD = 'ResourceNotFound.Word'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'
