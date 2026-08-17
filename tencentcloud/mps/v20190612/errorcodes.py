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


# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# Operation failure: bucket notifications have already been set.
FAILEDOPERATION_BUCKETNOTIFYALREADYEXIST = 'FailedOperation.BucketNotifyAlreadyExist'

# Operation failed: COS service is suspended.
FAILEDOPERATION_COSSTATUSINAVLID = 'FailedOperation.CosStatusInavlid'

# 
FAILEDOPERATION_CREATEAIGCTASKFAILED = 'FailedOperation.CreateAIGCTaskFailed'

# Resource generation failed.
FAILEDOPERATION_GENERATERESOURCE = 'FailedOperation.GenerateResource'

# Operation failure: error retrieving source notification.
FAILEDOPERATION_GETSOURCENOTIFY = 'FailedOperation.GetSourceNotify'

# Operation failed: unauthorized MPS user.
FAILEDOPERATION_INVALIDMPSUSER = 'FailedOperation.InvalidMpsUser'

# Operation failed: invalid user.
FAILEDOPERATION_INVALIDUSER = 'FailedOperation.InvalidUser'

# Operation failed due to a network error.
FAILEDOPERATION_NETWORKERROR = 'FailedOperation.NetWorkError'

# 
FAILEDOPERATION_QUERYAIGCTASKFAILED = 'FailedOperation.QueryAIGCTaskFailed'

# Operation failure: error setting source notification.
FAILEDOPERATION_SETSOURCENOTIFY = 'FailedOperation.SetSourceNotify'

# 
FAILEDOPERATION_USERARREARS = 'FailedOperation.UserArrears'

# Internal error.
INTERNALERROR = 'InternalError'

# Data error.
INTERNALERROR_ACCESSDBERROR = 'InternalError.AccessDBError'

# Internal error: failed to generate template ID.
INTERNALERROR_GENDEFINITION = 'InternalError.GenDefinition'

# Recognition error.
INTERNALERROR_RECOGNITIONERROR = 'InternalError.RecognitionError'

# Internal error: failed to upload watermark image.
INTERNALERROR_UPLOADWATERMARKERROR = 'InternalError.UploadWatermarkError'

# Parameter error.
INVALIDPARAMETER = 'InvalidParameter'

# InvalidParameter.Id
INVALIDPARAMETER_ID = 'InvalidParameter.Id'

# Illegal input.
INVALIDPARAMETER_INPUTINFO = 'InvalidParameter.InputInfo'

# The Url in the request parameter is invalid
INVALIDPARAMETER_INVALIDURL = 'InvalidParameter.InvalidUrl'

# Invalid parameters. The model is not supported.
INVALIDPARAMETER_MODELNOTSUPPORTED = 'InvalidParameter.ModelNotSupported'

# InvalidParameter.NotFound
INVALIDPARAMETER_NOTFOUND = 'InvalidParameter.NotFound'

# JSON parsing failure; `Uin` / `SubAccountUin` / `Message` missing
INVALIDPARAMETER_VALUE = 'InvalidParameter.Value'

# Review blocklist for user-submitted input.
INVALIDPARAMETER_VIOLATIONCONTENT = 'InvalidParameter.ViolationContent'

# Incorrect parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# The value of the hotword lexicon configuration parameter is incorrect.
INVALIDPARAMETERVALUE_ASRHOTWORDSCONFIGURE = 'InvalidParameterValue.AsrHotWordsConfigure'

# The value of the hotword lexicon ID parameter is incorrect.
INVALIDPARAMETERVALUE_ASRHOTWORDSLIBRARYID = 'InvalidParameterValue.AsrHotWordsLibraryId'

# The value of the hotword lexicon switch parameter is incorrect.
INVALIDPARAMETERVALUE_ASRHOTWORDSSWITCH = 'InvalidParameterValue.AsrHotWordsSwitch'

# Invalid parameter: audio stream bitrate.
INVALIDPARAMETERVALUE_AUDIOBITRATE = 'InvalidParameterValue.AudioBitrate'

# Parameter value error: AudioChannel.
INVALIDPARAMETERVALUE_AUDIOCHANNEL = 'InvalidParameterValue.AudioChannel'

# Invalid parameter: audio stream encoding format.
INVALIDPARAMETERVALUE_AUDIOCODEC = 'InvalidParameterValue.AudioCodec'

# Invalid audio data.
INVALIDPARAMETERVALUE_AUDIODATA = 'InvalidParameterValue.AudioData'

# The audio data is too long.
INVALIDPARAMETERVALUE_AUDIODATATOOLONG = 'InvalidParameterValue.AudioDataTooLong'

# Unsupported audio data format.
INVALIDPARAMETERVALUE_AUDIOFORMAT = 'InvalidParameterValue.AudioFormat'

# Invalid parameter: audio stream sampling rate.
INVALIDPARAMETERVALUE_AUDIOSAMPLERATE = 'InvalidParameterValue.AudioSampleRate'

# The configuration for the automatic erasing area of the erasing template is incorrect.
INVALIDPARAMETERVALUE_AUTOAREAS = 'InvalidParameterValue.AutoAreas'

# Invalid audio/video bitrate.
INVALIDPARAMETERVALUE_BITRATE = 'InvalidParameterValue.Bitrate'

# Incorrect parameter value: the value of the `BlockConfidence` parameter is invalid.
INVALIDPARAMETERVALUE_BLOCKCONFIDENCE = 'InvalidParameterValue.BlockConfidence'

# Parameter value error: Intelligent classification control field parameter error.
INVALIDPARAMETERVALUE_CLASSIFCATIONCONFIGURE = 'InvalidParameterValue.ClassifcationConfigure'

# Invalid audio/video codec.
INVALIDPARAMETERVALUE_CODEC = 'InvalidParameterValue.Codec'

# Incorrect parameter value: ColumnCount.
INVALIDPARAMETERVALUE_COLUMNCOUNT = 'InvalidParameterValue.ColumnCount'

# Parameter error: template description.
INVALIDPARAMETERVALUE_COMMENT = 'InvalidParameterValue.Comment'

# Invalid parameter: muxing format.
INVALIDPARAMETERVALUE_CONTAINER = 'InvalidParameterValue.Container'

# Incorrect parameter value: ContainerType.
INVALIDPARAMETERVALUE_CONTAINERTYPE = 'InvalidParameterValue.ContainerType'

# Incorrect parameter value: CoordinateOrigin.
INVALIDPARAMETERVALUE_COORDINATEORIGIN = 'InvalidParameterValue.CoordinateOrigin'

# Parameter value error: Intelligent cover control field parameter error.
INVALIDPARAMETERVALUE_COVERCONFIGURE = 'InvalidParameterValue.CoverConfigure'

# The specified area of the erasing template is incorrect.
INVALIDPARAMETERVALUE_CUSTOMAREAS = 'InvalidParameterValue.CustomAreas'

# Parameter value error: the filter tag of the default human face library is invalid.
INVALIDPARAMETERVALUE_DEFAULTLIBRARYLABELSET = 'InvalidParameterValue.DefaultLibraryLabelSet'

# Parameter error: Definition.
INVALIDPARAMETERVALUE_DEFINITION = 'InvalidParameterValue.Definition'

# Parameter error: Definitions.
INVALIDPARAMETERVALUE_DEFINITIONS = 'InvalidParameterValue.Definitions'

# Incorrect parameter value: the default template cannot be deleted.
INVALIDPARAMETERVALUE_DELETEDEFAULTTEMPLATE = 'InvalidParameterValue.DeleteDefaultTemplate'

# A DestinationLanguage parameter error occurs.
INVALIDPARAMETERVALUE_DESTINATIONLANGUAGE = 'InvalidParameterValue.DestinationLanguage'

# Invalid switch value used to prohibit transcoding from low bitrate to high bitrate.
INVALIDPARAMETERVALUE_DISABLEHIGHERVIDEOBITRATE = 'InvalidParameterValue.DisableHigherVideoBitrate'

# Invalid switch value used to prohibit transcoding from low resolution to high resolution.
INVALIDPARAMETERVALUE_DISABLEHIGHERVIDEORESOLUTION = 'InvalidParameterValue.DisableHigherVideoResolution'

# Duplicated watermark text.
INVALIDPARAMETERVALUE_DUPLICATEDTEXTCONTENT = 'InvalidParameterValue.DuplicatedTextContent'

# The Duration parameter is too large.
INVALIDPARAMETERVALUE_DURATIONTOOLONG = 'InvalidParameterValue.DurationTooLong'

# The enabled detection items of the template are empty.
INVALIDPARAMETERVALUE_EMPTYDETECTITEM = 'InvalidParameterValue.EmptyDetectItem'

# The privacy protection configuration of the erasing template is incorrect.
INVALIDPARAMETERVALUE_ERASEPRIVACYCONFIG = 'InvalidParameterValue.ErasePrivacyConfig'

# The subtitle erasing configuration of the erasing template is incorrect.
INVALIDPARAMETERVALUE_ERASESUBTITLECONFIG = 'InvalidParameterValue.EraseSubtitleConfig'

# The erasing type of the erasing template is incorrect.
INVALIDPARAMETERVALUE_ERASETYPE = 'InvalidParameterValue.EraseType'

# The watermark erasing configuration of the erasing template is incorrect.
INVALIDPARAMETERVALUE_ERASEWATERMARKCONFIG = 'InvalidParameterValue.EraseWatermarkConfig'

# Incorrect parameter value: duplicated face.
INVALIDPARAMETERVALUE_FACEDUPLICATE = 'InvalidParameterValue.FaceDuplicate'

# Parameter value error: the face library parameter is invalid.
INVALIDPARAMETERVALUE_FACELIBRARY = 'InvalidParameterValue.FaceLibrary'

# Parameter value error: the Face Score parameter value is invalid.
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

# Parameter value error: Intelligent frame tagging control field parameter error.
INVALIDPARAMETERVALUE_FRAMETAGCONFIGURE = 'InvalidParameterValue.FrameTagConfigure'

# Parameter value error: FunctionArg.
INVALIDPARAMETERVALUE_FUNCTIONARG = 'InvalidParameterValue.FunctionArg'

# Parameter value error: FunctionName.
INVALIDPARAMETERVALUE_FUNCTIONNAME = 'InvalidParameterValue.FunctionName'

# Invalid GOP value.
INVALIDPARAMETERVALUE_GOP = 'InvalidParameterValue.Gop'

# Parameter error: height.
INVALIDPARAMETERVALUE_HEIGHT = 'InvalidParameterValue.Height'

# Parameter error. The hotword lexicon does not exist.
INVALIDPARAMETERVALUE_HOTWORDSNOTEXIST = 'InvalidParameterValue.HotWordsNotExist'

# Hot word lexicon format error. Refer to the hot word configuration instructions document (https://www.tencentcloud.com/document/product/862/116244?from_cn_redirect=1#afc37e17-2786 4289-9bc3-8e24435d3f45).
INVALIDPARAMETERVALUE_HOTWORDSFORMATERROR = 'InvalidParameterValue.HotwordsFormatError'

# Invalid ImageContent
INVALIDPARAMETERVALUE_IMAGECONTENT = 'InvalidParameterValue.ImageContent'

# Parameter error: image watermarking template.
INVALIDPARAMETERVALUE_IMAGETEMPLATE = 'InvalidParameterValue.ImageTemplate'

# Incorrect input parameters.
INVALIDPARAMETERVALUE_INPUTINFO = 'InvalidParameterValue.InputInfo'

# The value of Content is invalid.
INVALIDPARAMETERVALUE_INVALIDCONTENT = 'InvalidParameterValue.InvalidContent'

# Invalid operation type.
INVALIDPARAMETERVALUE_INVALIDOPERATIONTYPE = 'InvalidParameterValue.InvalidOperationType'

# Incorrect parameter value: invalid `LabelSet` value.
INVALIDPARAMETERVALUE_LABELSET = 'InvalidParameterValue.LabelSet'

# Parameter error: Limit.
INVALIDPARAMETERVALUE_LIMIT = 'InvalidParameterValue.Limit'

# Parameter value error: Default template not allowed to be modified.
INVALIDPARAMETERVALUE_MODIFYDEFAULTTEMPLATE = 'InvalidParameterValue.ModifyDefaultTemplate'

# Incorrect parameter value: `Name` exceeds the length limit.
INVALIDPARAMETERVALUE_NAME = 'InvalidParameterValue.Name'

# Tasks not in processing status are not supported.
INVALIDPARAMETERVALUE_NOTPROCESSINGTASK = 'InvalidParameterValue.NotProcessingTask'

# Parameter value error: the object library parameter is invalid.
INVALIDPARAMETERVALUE_OBJECTLIBRARY = 'InvalidParameterValue.ObjectLibrary'

# Incorrect parameter value: the OcrSwitch parameter value is invalid.
INVALIDPARAMETERVALUE_OCRSWITCH = 'InvalidParameterValue.OcrSwitch'

# Incorrect parameter value: incorrect face image format.
INVALIDPARAMETERVALUE_PICFORMATERROR = 'InvalidParameterValue.PicFormatError'

# The privacy protection model of the erasing template is incorrect.
INVALIDPARAMETERVALUE_PRIVACYMODEL = 'InvalidParameterValue.PrivacyModel'

# The privacy protection target of the erasing template is incorrect.
INVALIDPARAMETERVALUE_PRIVACYTARGETS = 'InvalidParameterValue.PrivacyTargets'

# The number of episode projects exceeds the upper limit.
INVALIDPARAMETERVALUE_PROJECTLIMITEXCEEDED = 'InvalidParameterValue.ProjectLimitExceeded'

# The episode project name already exists.
INVALIDPARAMETERVALUE_PROJECTNAMEDUPLICATE = 'InvalidParameterValue.ProjectNameDuplicate'

# The episode project does not exist.
INVALIDPARAMETERVALUE_PROJECTNOTFOUND = 'InvalidParameterValue.ProjectNotFound'

# Incorrect parameter value: Quality.
INVALIDPARAMETERVALUE_QUALITY = 'InvalidParameterValue.Quality'

# Parameter value error: RemoveAudio.
INVALIDPARAMETERVALUE_REMOVEAUDIO = 'InvalidParameterValue.RemoveAudio'

# Parameter value error: RemoveVideo.
INVALIDPARAMETERVALUE_REMOVEVIDEO = 'InvalidParameterValue.RemoveVideo'

# Parameter error: invalid `RepeatType`.
INVALIDPARAMETERVALUE_REPEATTYPE = 'InvalidParameterValue.RepeatType'

# Parameter error: Incorrect resolution.
INVALIDPARAMETERVALUE_RESOLUTION = 'InvalidParameterValue.Resolution'

# Invalid ResolutionAdaptive.
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

# A service parameter value error occurs.
INVALIDPARAMETERVALUE_SERVICE = 'InvalidParameterValue.Service'

# The SessionContext is too long.
INVALIDPARAMETERVALUE_SESSIONCONTEXTTOOLONG = 'InvalidParameterValue.SessionContextTooLong'

# Duplicate recognition code, request deduplicated.
INVALIDPARAMETERVALUE_SESSIONID = 'InvalidParameterValue.SessionId'

# SessionId is too long.
INVALIDPARAMETERVALUE_SESSIONIDTOOLONG = 'InvalidParameterValue.SessionIdTooLong'

# Invalid parameter: incorrect audio channel system.
INVALIDPARAMETERVALUE_SOUNDSYSTEM = 'InvalidParameterValue.SoundSystem'

# A SourceLanguage parameter error occurs.
INVALIDPARAMETERVALUE_SOURCELANGUAGE = 'InvalidParameterValue.SourceLanguage'

# A SourceText parameter error occurs.
INVALIDPARAMETERVALUE_SOURCETEXT = 'InvalidParameterValue.SourceText'

# Source file error.
INVALIDPARAMETERVALUE_SRCFILE = 'InvalidParameterValue.SrcFile'

# Subtitle suppression ID invalid
INVALIDPARAMETERVALUE_SUBTITLEEMBEDID = 'InvalidParameterValue.SubtitleEmbedId'

# The subtitle erasing method of the erasing template is incorrect.
INVALIDPARAMETERVALUE_SUBTITLEERASEMETHOD = 'InvalidParameterValue.SubtitleEraseMethod'

# Parameter value error: the SubtitleFormat parameter is invalid.
INVALIDPARAMETERVALUE_SUBTITLEFORMAT = 'InvalidParameterValue.SubtitleFormat'

# The language for the subtitle erasing of the erasing template is incorrect.
INVALIDPARAMETERVALUE_SUBTITLELANG = 'InvalidParameterValue.SubtitleLang'

# The subtitle erasing model of the erasing template is incorrect.
INVALIDPARAMETERVALUE_SUBTITLEMODEL = 'InvalidParameterValue.SubtitleModel'

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

# Parameter value error: TEHD Type invalid.
INVALIDPARAMETERVALUE_TEHDTYPE = 'InvalidParameterValue.TEHDType'

# Parameter value error: Intelligent tag control field parameter error.
INVALIDPARAMETERVALUE_TAGCONFIGURE = 'InvalidParameterValue.TagConfigure'

# The task ID does not exist.
INVALIDPARAMETERVALUE_TASKID = 'InvalidParameterValue.TaskId'

# Parameter error: text transparency.
INVALIDPARAMETERVALUE_TEXTALPHA = 'InvalidParameterValue.TextAlpha'

# A TextContent parameter value error occurs.
INVALIDPARAMETERVALUE_TEXTCONTENT = 'InvalidParameterValue.TextContent'

# Parameter error: text template.
INVALIDPARAMETERVALUE_TEXTTEMPLATE = 'InvalidParameterValue.TextTemplate'

# The configuration for the translation target language is incorrect under the smart erasing - subtitle erasing template.
INVALIDPARAMETERVALUE_TRANSDSTLANG = 'InvalidParameterValue.TransDstLang'

# Incorrect parameter value: the TransSwitch parameter value is invalid.
INVALIDPARAMETERVALUE_TRANSSWITCH = 'InvalidParameterValue.TransSwitch'

# The value of the target language parameter is incorrect.
INVALIDPARAMETERVALUE_TRANSLATEDSTLANGUAGE = 'InvalidParameterValue.TranslateDstLanguage'

# The value of the translation switch parameter is incorrect.
INVALIDPARAMETERVALUE_TRANSLATESWITCH = 'InvalidParameterValue.TranslateSwitch'

# Parameter error: Type parameter value error.
INVALIDPARAMETERVALUE_TYPE = 'InvalidParameterValue.Type'

# Unknown detection category.
INVALIDPARAMETERVALUE_UNKNOWNCATEGORY = 'InvalidParameterValue.UnknownCategory'

# UseOriginalPos unavailable
INVALIDPARAMETERVALUE_USEORIGINALPOS = 'InvalidParameterValue.UseOriginalPos'

# UseOriginalSize Unavailable
INVALIDPARAMETERVALUE_USEORIGINALSIZE = 'InvalidParameterValue.UseOriginalSize'

# Parameter value error: the filter tag of the custom face library is invalid.
INVALIDPARAMETERVALUE_USERDEFINELIBRARYLABELSET = 'InvalidParameterValue.UserDefineLibraryLabelSet'

# The user is not registered for MPS.
INVALIDPARAMETERVALUE_USERUNREGISTER = 'InvalidParameterValue.UserUnRegister'

# Parameter error: video stream bitrate.
INVALIDPARAMETERVALUE_VIDEOBITRATE = 'InvalidParameterValue.VideoBitrate'

# Invalid parameter: video stream encoding format.
INVALIDPARAMETERVALUE_VIDEOCODEC = 'InvalidParameterValue.VideoCodec'

# The value of the video source language parameter is incorrect.
INVALIDPARAMETERVALUE_VIDEOSRCLANGUAGE = 'InvalidParameterValue.VideoSrcLanguage'

# The watermark erasing method of the erasing template is incorrect.
INVALIDPARAMETERVALUE_WATERMARKERASEMETHOD = 'InvalidParameterValue.WatermarkEraseMethod'

# The watermark erasing model of the erasing template is incorrect.
INVALIDPARAMETERVALUE_WATERMARKMODEL = 'InvalidParameterValue.WatermarkModel'

# Parameter error: Wwdth.
INVALIDPARAMETERVALUE_WIDTH = 'InvalidParameterValue.Width'

# The horizontal position of the origin of the watermark relative to the origin of coordinates of the video. % and px formats are supported.
INVALIDPARAMETERVALUE_XPOS = 'InvalidParameterValue.XPos'

# The vertical position of the origin of the watermark relative to the origin of coordinates of the video. % and px formats are supported.
INVALIDPARAMETERVALUE_YPOS = 'InvalidParameterValue.YPos'

# 
LIMITEXCEEDED_CREATETASK = 'LimitExceeded.CreateTask'

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

# Download failed.
RESOURCENOTFOUND_DOWNLOADERROR = 'ResourceNotFound.DownloadError'

# The resource does not exist: figure.
RESOURCENOTFOUND_PERSON = 'ResourceNotFound.Person'

# 
RESOURCENOTFOUND_TASKNOTFOUND = 'ResourceNotFound.TaskNotFound'

# The resource does not exist: the template does not exist.
RESOURCENOTFOUND_TEMPLATENOTEXIST = 'ResourceNotFound.TemplateNotExist'

# The user is not registered.
RESOURCENOTFOUND_USERUNREGISTER = 'ResourceNotFound.UserUnregister'

# The resource does not exist: Keyword.
RESOURCENOTFOUND_WORD = 'ResourceNotFound.Word'

# Unauthorized operation.
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# The text for a single request exceeds the length limit.
UNSUPPORTEDOPERATION_TEXTTOOLONG = 'UnsupportedOperation.TextTooLong'
