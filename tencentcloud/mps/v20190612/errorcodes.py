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

# Incorrect parameter value.
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# Parameter configuration error: improper AAC frame timestamp interval.
INVALIDPARAMETERVALUE_AACDURATIONDEVIATION = 'InvalidParameterValue.AACDurationDeviation'

# Parameter configuration error: improper audio-video interleaving.
INVALIDPARAMETERVALUE_AVTIMESTAMPINTERLEAVE = 'InvalidParameterValue.AVTimestampInterleave'

# Parameter error: Audio stream bitrate.
INVALIDPARAMETERVALUE_AUDIOBITRATE = 'InvalidParameterValue.AudioBitrate'

# Parameter configuration error: audio stream bitrate out of range.
INVALIDPARAMETERVALUE_AUDIOBITRATEOUTOFRANGE = 'InvalidParameterValue.AudioBitrateOutofRange'

# Incorrect parameter value: AudioChannel.
INVALIDPARAMETERVALUE_AUDIOCHANNEL = 'InvalidParameterValue.AudioChannel'

# Parameter configuration error: audio track change.
INVALIDPARAMETERVALUE_AUDIOCHANNELSCHANGED = 'InvalidParameterValue.AudioChannelsChanged'

# Parameter error: audio stream codec.
INVALIDPARAMETERVALUE_AUDIOCODEC = 'InvalidParameterValue.AudioCodec'

# Parameter configuration error: audio decoding error.
INVALIDPARAMETERVALUE_AUDIODECODEFAILED = 'InvalidParameterValue.AudioDecodeFailed'

# Parameter configuration error: audio frame dropping.
INVALIDPARAMETERVALUE_AUDIODROPPINGFRAMES = 'InvalidParameterValue.AudioDroppingFrames'

# Parameter configuration error: duplicate frames in audio streams.
INVALIDPARAMETERVALUE_AUDIODUPLICATEDFRAME = 'InvalidParameterValue.AudioDuplicatedFrame'

# Parameter configuration error: opposite phase in dual-channel audio.
INVALIDPARAMETERVALUE_AUDIOOUTOFPHASE = 'InvalidParameterValue.AudioOutOfPhase'

# Parameter error: audio stream sample rate.
INVALIDPARAMETERVALUE_AUDIOSAMPLERATE = 'InvalidParameterValue.AudioSampleRate'

# Parameter configuration error: audio sample rate change.
INVALIDPARAMETERVALUE_AUDIOSAMPLERATECHANGED = 'InvalidParameterValue.AudioSampleRateChanged'

# Parameter configuration error: no audio stream.
INVALIDPARAMETERVALUE_AUDIOSTREAMLACK = 'InvalidParameterValue.AudioStreamLack'

# Invalid audio/video bitrate.
INVALIDPARAMETERVALUE_BITRATE = 'InvalidParameterValue.Bitrate'

# Parameter configuration error: black and white edges detection.
INVALIDPARAMETERVALUE_BLACKWHITEEDGE = 'InvalidParameterValue.BlackWhiteEdge'

# Incorrect parameter value: the value of the `BlockConfidence` parameter is invalid.
INVALIDPARAMETERVALUE_BLOCKCONFIDENCE = 'InvalidParameterValue.BlockConfidence'

# Parameter configuration error: blur detection.
INVALIDPARAMETERVALUE_BLUR = 'InvalidParameterValue.Blur'

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

# Parameter configuration error: screen glitch detection.
INVALIDPARAMETERVALUE_CRASHSCREEN = 'InvalidParameterValue.CrashScreen'

# Parameter configuration error: video aspect ratio exception.
INVALIDPARAMETERVALUE_DARORSARINVALID = 'InvalidParameterValue.DarOrSarInvalid'

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

# Parameter configuration error: DTS jitter too high.
INVALIDPARAMETERVALUE_DTSJITTER = 'InvalidParameterValue.DtsJitter'

# Enabled detection items in template configuration are empty.
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

# Parameter configuration error: significant jitter in the stream frame rate calculated via PTS.
INVALIDPARAMETERVALUE_FPSJITTER = 'InvalidParameterValue.FpsJitter'

# Incorrect parameter value: the control field parameter for intelligent frame-specific tagging is incorrect.
INVALIDPARAMETERVALUE_FRAMETAGCONFIGURE = 'InvalidParameterValue.FrameTagConfigure'

# Incorrect parameter value: FunctionArg.
INVALIDPARAMETERVALUE_FUNCTIONARG = 'InvalidParameterValue.FunctionArg'

# Incorrect parameter value: FunctionName.
INVALIDPARAMETERVALUE_FUNCTIONNAME = 'InvalidParameterValue.FunctionName'

# Invalid GOP value.
INVALIDPARAMETERVALUE_GOP = 'InvalidParameterValue.Gop'

# Parameter configuration error: invalid M3U8 file.
INVALIDPARAMETERVALUE_HLSBADM3U8FORMAT = 'InvalidParameterValue.HLSBadM3u8Format'

# Parameter configuration error: invalid main M3U8 file.
INVALIDPARAMETERVALUE_HLSINVALIDMASTERM3U8 = 'InvalidParameterValue.HLSInvalidMasterM3u8'

# Parameter configuration error: invalid media M3U8 file.
INVALIDPARAMETERVALUE_HLSINVALIDMEDIAM3U8 = 'InvalidParameterValue.HLSInvalidMediaM3u8'

# Parameter configuration error: parameters recommended by standards missing in main M3U8.
INVALIDPARAMETERVALUE_HLSMASTERM3U8RECOMMENDED = 'InvalidParameterValue.HLSMasterM3u8Recommended'

# Parameter configuration error: EXT-X-DISCONTINUITY in media M3U8.
INVALIDPARAMETERVALUE_HLSMEDIAM3U8DISCONTINUITYEXIST = 'InvalidParameterValue.HLSMediaM3u8DiscontinuityExist'

# Parameter configuration error: parameters recommended by standards missing in media M3U8.
INVALIDPARAMETERVALUE_HLSMEDIAM3U8RECOMMENDED = 'InvalidParameterValue.HLSMediaM3u8Recommended'

# Parameter configuration error: DTS jumps between segments without EXT-X-DISCONTINUITY.
INVALIDPARAMETERVALUE_HLSMEDIASEGMENTSDTSJITTERDEVIATION = 'InvalidParameterValue.HLSMediaSegmentsDTSJitterDeviation'

# Parameter configuration error: PTS jumps between segments without EXT-X-DISCONTINUITY.
INVALIDPARAMETERVALUE_HLSMEDIASEGMENTSPTSJITTERDEVIATION = 'InvalidParameterValue.HLSMediaSegmentsPTSJitterDeviation'

# Parameter configuration error: changed number of streams in segments.
INVALIDPARAMETERVALUE_HLSMEDIASEGMENTSSTREAMNUMCHANGE = 'InvalidParameterValue.HLSMediaSegmentsStreamNumChange'

# Parameter error: height.
INVALIDPARAMETERVALUE_HEIGHT = 'InvalidParameterValue.Height'

# Parameter configuration error: brightness anomaly of overexposure.
INVALIDPARAMETERVALUE_HIGHLIGHTING = 'InvalidParameterValue.HighLighting'

# Parameter configuration error: high voice detection.
INVALIDPARAMETERVALUE_HIGHVOICE = 'InvalidParameterValue.HighVoice'

# Invalid ImageContent
INVALIDPARAMETERVALUE_IMAGECONTENT = 'InvalidParameterValue.ImageContent'

# Parameter error: image watermarking template.
INVALIDPARAMETERVALUE_IMAGETEMPLATE = 'InvalidParameterValue.ImageTemplate'

# The value of the parsed `Content` is invalid.
INVALIDPARAMETERVALUE_INVALIDCONTENT = 'InvalidParameterValue.InvalidContent'

# Invalid operation type.
INVALIDPARAMETERVALUE_INVALIDOPERATIONTYPE = 'InvalidParameterValue.InvalidOperationType'

# Incorrect parameter value: invalid `LabelSet` value.
INVALIDPARAMETERVALUE_LABELSET = 'InvalidParameterValue.LabelSet'

# Parameter configuration error: missing audio stream recovery.
INVALIDPARAMETERVALUE_LACKAUDIORECOVER = 'InvalidParameterValue.LackAudioRecover'

# Parameter configuration error: missing video stream recovery.
INVALIDPARAMETERVALUE_LACKVIDEORECOVER = 'InvalidParameterValue.LackVideoRecover'

# Parameter error: Limit.
INVALIDPARAMETERVALUE_LIMIT = 'InvalidParameterValue.Limit'

# Parameter configuration error: no-reference scoring.
INVALIDPARAMETERVALUE_LOWEVALUATION = 'InvalidParameterValue.LowEvaluation'

# Parameter configuration error: brightness anomaly of low light.
INVALIDPARAMETERVALUE_LOWLIGHTING = 'InvalidParameterValue.LowLighting'

# Parameter configuration error: low voice detection.
INVALIDPARAMETERVALUE_LOWVOICE = 'InvalidParameterValue.LowVoice'

# Incorrect parameter value: the default template cannot be modified.
INVALIDPARAMETERVALUE_MODIFYDEFAULTTEMPLATE = 'InvalidParameterValue.ModifyDefaultTemplate'

# Parameter configuration error: mosaic detection.
INVALIDPARAMETERVALUE_MOSAIC = 'InvalidParameterValue.Mosaic'

# Parameter configuration error: codec FourCC in MP4 not meeting Apple HLS requirements.
INVALIDPARAMETERVALUE_MP4INVALIDCODECFOURCC = 'InvalidParameterValue.Mp4InvalidCodecFourcc'

# Incorrect parameter value: `Name` exceeds the length limit.
INVALIDPARAMETERVALUE_NAME = 'InvalidParameterValue.Name'

# Parameter configuration error: no voice detection.
INVALIDPARAMETERVALUE_NOVOICE = 'InvalidParameterValue.NoVoice'

# Tasks not in processing status are not supported.
INVALIDPARAMETERVALUE_NOTPROCESSINGTASK = 'InvalidParameterValue.NotProcessingTask'

# Incorrect parameter value: object library parameter is invalid.
INVALIDPARAMETERVALUE_OBJECTLIBRARY = 'InvalidParameterValue.ObjectLibrary'

# Parameter configuration error: stream parameter set information change.
INVALIDPARAMETERVALUE_PARAMETERSETSCHANGED = 'InvalidParameterValue.ParameterSetsChanged'

# Incorrect parameter value: incorrect face image format.
INVALIDPARAMETERVALUE_PICFORMATERROR = 'InvalidParameterValue.PicFormatError'

# Parameter configuration error: PTS jitter too high.
INVALIDPARAMETERVALUE_PTSJITTER = 'InvalidParameterValue.PtsJitter'

# Parameter configuration error: PTS less than DTS for media streams.
INVALIDPARAMETERVALUE_PTSLESSTHANDTS = 'InvalidParameterValue.PtsLessThanDts'

# Incorrect parameter value: Quality.
INVALIDPARAMETERVALUE_QUALITY = 'InvalidParameterValue.Quality'

# Parameter configuration error: significant jitter in the network receive frame rate.
INVALIDPARAMETERVALUE_RECEIVEFPSJITTER = 'InvalidParameterValue.ReceiveFpsJitter'

# Parameter configuration error: network receive video frame rate too low.
INVALIDPARAMETERVALUE_RECEIVEFPSTOOSMALL = 'InvalidParameterValue.ReceiveFpsTooSmall'

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

# Parameter configuration error: stream end.
INVALIDPARAMETERVALUE_STREAMEND = 'InvalidParameterValue.StreamEnd'

# Parameter configuration error: NALU start code error.
INVALIDPARAMETERVALUE_STREAMNALUERROR = 'InvalidParameterValue.StreamNALUError'

# Parameter configuration error: stream open failure.
INVALIDPARAMETERVALUE_STREAMOPENFAILED = 'InvalidParameterValue.StreamOpenFailed'

# Parameter configuration error: stream parsing failure.
INVALIDPARAMETERVALUE_STREAMPARSEFAILED = 'InvalidParameterValue.StreamParseFailed'

# Incorrect parameter value: The value of the `SubtitleFormat` parameter is invalid.
INVALIDPARAMETERVALUE_SUBTITLEFORMAT = 'InvalidParameterValue.SubtitleFormat'

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

# Parameter configuration error: TMCD track in MP4.
INVALIDPARAMETERVALUE_TIMECODETRACKEXIST = 'InvalidParameterValue.TimecodeTrackExist'

# Parameter configuration error: DTS timestamp rollback.
INVALIDPARAMETERVALUE_TIMESTAMPFALLBACK = 'InvalidParameterValue.TimestampFallback'

# Parameter configuration error: multiple programs in MPEG2-TS streams.
INVALIDPARAMETERVALUE_TSMULTIPROGRAMS = 'InvalidParameterValue.TsMultiPrograms'

# Parameter configuration error: no AUD NALU in the H26x stream of MPEG-TS.
INVALIDPARAMETERVALUE_TSSTREAMNOAUD = 'InvalidParameterValue.TsStreamNoAud'

# Parameter error: incorrect `Type` value.
INVALIDPARAMETERVALUE_TYPE = 'InvalidParameterValue.Type'

# Unknown diagnostic category.
INVALIDPARAMETERVALUE_UNKNOWNCATEGORY = 'InvalidParameterValue.UnknownCategory'

# Incorrect parameter value: the custom face library filter tag is invalid.
INVALIDPARAMETERVALUE_USERDEFINELIBRARYLABELSET = 'InvalidParameterValue.UserDefineLibraryLabelSet'

# Parameter error: video stream bitrate.
INVALIDPARAMETERVALUE_VIDEOBITRATE = 'InvalidParameterValue.VideoBitrate'

# Parameter configuration error: video stream bitrate out of range.
INVALIDPARAMETERVALUE_VIDEOBITRATEOUTOFRANGE = 'InvalidParameterValue.VideoBitrateOutofRange'

# Parameter error: video stream codec.
INVALIDPARAMETERVALUE_VIDEOCODEC = 'InvalidParameterValue.VideoCodec'

# Parameter configuration error: video decoding error.
INVALIDPARAMETERVALUE_VIDEODECODEFAILED = 'InvalidParameterValue.VideoDecodeFailed'

# Parameter configuration error: video frame dropping.
INVALIDPARAMETERVALUE_VIDEODROPPINGFRAMES = 'InvalidParameterValue.VideoDroppingFrames'

# Parameter configuration error: duplicate frames in video streams.
INVALIDPARAMETERVALUE_VIDEODUPLICATEDFRAME = 'InvalidParameterValue.VideoDuplicatedFrame'

# Parameter configuration error: first frame not an IDR frame.
INVALIDPARAMETERVALUE_VIDEOFIRSTFRAMENOTIDR = 'InvalidParameterValue.VideoFirstFrameNotIdr'

# Parameter configuration error: video freezing.
INVALIDPARAMETERVALUE_VIDEOFREEZEDFRAME = 'InvalidParameterValue.VideoFreezedFrame'

# Parameter configuration error: video resolution change.
INVALIDPARAMETERVALUE_VIDEORESOLUTIONCHANGED = 'InvalidParameterValue.VideoResolutionChanged'

# Parameter configuration error: video rotation.
INVALIDPARAMETERVALUE_VIDEOROTATION = 'InvalidParameterValue.VideoRotation'

# Parameter configuration error: no video stream.
INVALIDPARAMETERVALUE_VIDEOSTREAMLACK = 'InvalidParameterValue.VideoStreamLack'

# Parameter error: Wwdth.
INVALIDPARAMETERVALUE_WIDTH = 'InvalidParameterValue.Width'

# The horizontal position of the origin of the watermark relative to the origin of coordinates of the video. % and px formats are supported.
INVALIDPARAMETERVALUE_XPOS = 'InvalidParameterValue.XPos'

# The vertical position of the origin of the watermark relative to the origin of coordinates of the video. % and px formats are supported.
INVALIDPARAMETERVALUE_YPOS = 'InvalidParameterValue.YPos'

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
