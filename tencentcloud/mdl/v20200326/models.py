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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AVTemplate(AbstractModel):
    """Audio/Video transcoding template

    """

    def __init__(self):
        r"""
        :param _Name: Name of an audio/video transcoding template, which can contain 1-20 case-sensitive letters and digits
        :type Name: str
        :param _NeedVideo: Whether video is needed. `0`: not needed; `1`: needed
        :type NeedVideo: int
        :param _Vcodec: Video codec. Valid values: `H264`, `H265`. If this parameter is left empty, the original video codec will be used.
        :type Vcodec: str
        :param _Width: Video width. Value range: (0, 3000]. The value must be an integer multiple of 4. If this parameter is left empty, the original video width will be used.
        :type Width: int
        :param _Height: Video height. Value range: (0, 3000]. The value must be an integer multiple of 4. If this parameter is left empty, the original video height will be used.
        :type Height: int
        :param _Fps: Video frame rate. Value range: [1, 240]. If this parameter is left empty, the original frame rate will be used.
        :type Fps: int
        :param _TopSpeed: Whether to enable top speed codec transcoding. Valid values: `CLOSE` (disable), `OPEN` (enable). Default value: `CLOSE`
        :type TopSpeed: str
        :param _BitrateCompressionRatio: Compression ratio for top speed codec transcoding. Value range: [0, 50]. The lower the compression ratio, the higher the image quality.
        :type BitrateCompressionRatio: int
        :param _NeedAudio: Whether audio is needed. `0`: not needed; `1`: needed
        :type NeedAudio: int
        :param _Acodec: Audio codec. Valid value: `AAC` (default)
        :type Acodec: str
        :param _AudioBitrate: Audio bitrate. If this parameter is left empty, the original bitrate will be used.
Valid values: `6000`, `7000`, `8000`, `10000`, `12000`, `14000`, `16000`, `20000`, `24000`, `28000`, `32000`, `40000`, `48000`, `56000`, `64000`, `80000`, `96000`, `112000`, `128000`, `160000`, `192000`, `224000`, `256000`, `288000`, `320000`, `384000`, `448000`, `512000`, `576000`, `640000`, `768000`, `896000`, `1024000`
        :type AudioBitrate: int
        :param _VideoBitrate: Video bitrate. Value range: [50000, 40000000]. The value must be an integer multiple of 1000. If this parameter is left empty, the original bitrate will be used.
        :type VideoBitrate: int
        :param _RateControlMode: Bitrate control mode. Valid values: `CBR`, `ABR` (default)
        :type RateControlMode: str
        :param _WatermarkId: Watermark ID
        :type WatermarkId: str
        :param _SmartSubtitles: Whether to convert audio to text. `0` (default): No; `1`: Yes.
        :type SmartSubtitles: int
        :param _SubtitleConfiguration: The subtitle settings. Currently, the following subtitles are supported:
`eng2eng`: English speech to English text.
`eng2chs`: English speech to Chinese text. 
`eng2chseng`: English speech to English and Chinese text. 
`chs2chs`: Chinese speech to Chinese text.   
`chs2eng`: Chinese speech to English text. 
`chs2chseng`: Chinese speech to Chinese and English text.
        :type SubtitleConfiguration: str
        :param _FaceBlurringEnabled: Whether to enable the face blur function, 1 is on, 0 is off, and the default is 0.
        :type FaceBlurringEnabled: int
        :param _AudioSelectorName: Only AttachedInputs.AudioSelectors.Name can be selected. The following types need to be filled in: 'RTP_PUSH', 'SRT_PUSH', 'UDP_PUSH', 'RTP-FEC_PUSH'.
        :type AudioSelectorName: str
        :param _AudioNormalization: Audio transcoding special configuration information.
        :type AudioNormalization: :class:`tencentcloud.mdl.v20200326.models.AudioNormalizationSettings`
        :param _AudioSampleRate: Audio sampling rate, unit HZ.
        :type AudioSampleRate: int
        :param _FrameRateType: This field indicates how to specify the output video frame rate. If FOLLOW_SOURCE is selected, the output video frame rate will be set equal to the input video frame rate of the first input. If SPECIFIED_FRACTION is selected, the output video frame rate is determined by the fraction (frame rate numerator and frame rate denominator). If SPECIFIED_HZ is selected, the frame rate of the output video is determined by the HZ you enter.
        :type FrameRateType: str
        :param _FrameRateNumerator: Valid when the FrameRateType type you select is SPECIFIED_FRACTION, the output frame rate numerator setting.
        :type FrameRateNumerator: int
        :param _FrameRateDenominator: Valid when the FrameRateType type you select is SPECIFIED_FRACTION, the output frame rate denominator setting.
        :type FrameRateDenominator: int
        :param _BFramesNum: The number of B frames can be selected from 1 to 3.
        :type BFramesNum: int
        :param _RefFramesNum: The number of reference frames can be selected from 1 to 16.
        :type RefFramesNum: int
        :param _AdditionalRateSettings: Additional video bitrate configuration.
        :type AdditionalRateSettings: :class:`tencentcloud.mdl.v20200326.models.AdditionalRateSetting`
        :param _VideoCodecDetails: Video encoding configuration.
        :type VideoCodecDetails: :class:`tencentcloud.mdl.v20200326.models.VideoCodecDetail`
        :param _AudioCodecDetails: Audio encoding configuration.
        :type AudioCodecDetails: :class:`tencentcloud.mdl.v20200326.models.AudioCodecDetail`
        :param _MultiAudioTrackEnabled: Whether to enable multiple audio tracks 0: Not required 1: Required Default value 0.
        :type MultiAudioTrackEnabled: int
        :param _AudioTracks: Quantity limit 0-20 Valid when MultiAudioTrackEnabled is turned on.
        :type AudioTracks: list of AudioTrackInfo
        """
        self._Name = None
        self._NeedVideo = None
        self._Vcodec = None
        self._Width = None
        self._Height = None
        self._Fps = None
        self._TopSpeed = None
        self._BitrateCompressionRatio = None
        self._NeedAudio = None
        self._Acodec = None
        self._AudioBitrate = None
        self._VideoBitrate = None
        self._RateControlMode = None
        self._WatermarkId = None
        self._SmartSubtitles = None
        self._SubtitleConfiguration = None
        self._FaceBlurringEnabled = None
        self._AudioSelectorName = None
        self._AudioNormalization = None
        self._AudioSampleRate = None
        self._FrameRateType = None
        self._FrameRateNumerator = None
        self._FrameRateDenominator = None
        self._BFramesNum = None
        self._RefFramesNum = None
        self._AdditionalRateSettings = None
        self._VideoCodecDetails = None
        self._AudioCodecDetails = None
        self._MultiAudioTrackEnabled = None
        self._AudioTracks = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NeedVideo(self):
        return self._NeedVideo

    @NeedVideo.setter
    def NeedVideo(self, NeedVideo):
        self._NeedVideo = NeedVideo

    @property
    def Vcodec(self):
        return self._Vcodec

    @Vcodec.setter
    def Vcodec(self, Vcodec):
        self._Vcodec = Vcodec

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Fps(self):
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def TopSpeed(self):
        return self._TopSpeed

    @TopSpeed.setter
    def TopSpeed(self, TopSpeed):
        self._TopSpeed = TopSpeed

    @property
    def BitrateCompressionRatio(self):
        return self._BitrateCompressionRatio

    @BitrateCompressionRatio.setter
    def BitrateCompressionRatio(self, BitrateCompressionRatio):
        self._BitrateCompressionRatio = BitrateCompressionRatio

    @property
    def NeedAudio(self):
        return self._NeedAudio

    @NeedAudio.setter
    def NeedAudio(self, NeedAudio):
        self._NeedAudio = NeedAudio

    @property
    def Acodec(self):
        return self._Acodec

    @Acodec.setter
    def Acodec(self, Acodec):
        self._Acodec = Acodec

    @property
    def AudioBitrate(self):
        return self._AudioBitrate

    @AudioBitrate.setter
    def AudioBitrate(self, AudioBitrate):
        self._AudioBitrate = AudioBitrate

    @property
    def VideoBitrate(self):
        return self._VideoBitrate

    @VideoBitrate.setter
    def VideoBitrate(self, VideoBitrate):
        self._VideoBitrate = VideoBitrate

    @property
    def RateControlMode(self):
        return self._RateControlMode

    @RateControlMode.setter
    def RateControlMode(self, RateControlMode):
        self._RateControlMode = RateControlMode

    @property
    def WatermarkId(self):
        return self._WatermarkId

    @WatermarkId.setter
    def WatermarkId(self, WatermarkId):
        self._WatermarkId = WatermarkId

    @property
    def SmartSubtitles(self):
        return self._SmartSubtitles

    @SmartSubtitles.setter
    def SmartSubtitles(self, SmartSubtitles):
        self._SmartSubtitles = SmartSubtitles

    @property
    def SubtitleConfiguration(self):
        return self._SubtitleConfiguration

    @SubtitleConfiguration.setter
    def SubtitleConfiguration(self, SubtitleConfiguration):
        self._SubtitleConfiguration = SubtitleConfiguration

    @property
    def FaceBlurringEnabled(self):
        return self._FaceBlurringEnabled

    @FaceBlurringEnabled.setter
    def FaceBlurringEnabled(self, FaceBlurringEnabled):
        self._FaceBlurringEnabled = FaceBlurringEnabled

    @property
    def AudioSelectorName(self):
        return self._AudioSelectorName

    @AudioSelectorName.setter
    def AudioSelectorName(self, AudioSelectorName):
        self._AudioSelectorName = AudioSelectorName

    @property
    def AudioNormalization(self):
        return self._AudioNormalization

    @AudioNormalization.setter
    def AudioNormalization(self, AudioNormalization):
        self._AudioNormalization = AudioNormalization

    @property
    def AudioSampleRate(self):
        return self._AudioSampleRate

    @AudioSampleRate.setter
    def AudioSampleRate(self, AudioSampleRate):
        self._AudioSampleRate = AudioSampleRate

    @property
    def FrameRateType(self):
        return self._FrameRateType

    @FrameRateType.setter
    def FrameRateType(self, FrameRateType):
        self._FrameRateType = FrameRateType

    @property
    def FrameRateNumerator(self):
        return self._FrameRateNumerator

    @FrameRateNumerator.setter
    def FrameRateNumerator(self, FrameRateNumerator):
        self._FrameRateNumerator = FrameRateNumerator

    @property
    def FrameRateDenominator(self):
        return self._FrameRateDenominator

    @FrameRateDenominator.setter
    def FrameRateDenominator(self, FrameRateDenominator):
        self._FrameRateDenominator = FrameRateDenominator

    @property
    def BFramesNum(self):
        return self._BFramesNum

    @BFramesNum.setter
    def BFramesNum(self, BFramesNum):
        self._BFramesNum = BFramesNum

    @property
    def RefFramesNum(self):
        return self._RefFramesNum

    @RefFramesNum.setter
    def RefFramesNum(self, RefFramesNum):
        self._RefFramesNum = RefFramesNum

    @property
    def AdditionalRateSettings(self):
        return self._AdditionalRateSettings

    @AdditionalRateSettings.setter
    def AdditionalRateSettings(self, AdditionalRateSettings):
        self._AdditionalRateSettings = AdditionalRateSettings

    @property
    def VideoCodecDetails(self):
        return self._VideoCodecDetails

    @VideoCodecDetails.setter
    def VideoCodecDetails(self, VideoCodecDetails):
        self._VideoCodecDetails = VideoCodecDetails

    @property
    def AudioCodecDetails(self):
        return self._AudioCodecDetails

    @AudioCodecDetails.setter
    def AudioCodecDetails(self, AudioCodecDetails):
        self._AudioCodecDetails = AudioCodecDetails

    @property
    def MultiAudioTrackEnabled(self):
        return self._MultiAudioTrackEnabled

    @MultiAudioTrackEnabled.setter
    def MultiAudioTrackEnabled(self, MultiAudioTrackEnabled):
        self._MultiAudioTrackEnabled = MultiAudioTrackEnabled

    @property
    def AudioTracks(self):
        return self._AudioTracks

    @AudioTracks.setter
    def AudioTracks(self, AudioTracks):
        self._AudioTracks = AudioTracks


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._NeedVideo = params.get("NeedVideo")
        self._Vcodec = params.get("Vcodec")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Fps = params.get("Fps")
        self._TopSpeed = params.get("TopSpeed")
        self._BitrateCompressionRatio = params.get("BitrateCompressionRatio")
        self._NeedAudio = params.get("NeedAudio")
        self._Acodec = params.get("Acodec")
        self._AudioBitrate = params.get("AudioBitrate")
        self._VideoBitrate = params.get("VideoBitrate")
        self._RateControlMode = params.get("RateControlMode")
        self._WatermarkId = params.get("WatermarkId")
        self._SmartSubtitles = params.get("SmartSubtitles")
        self._SubtitleConfiguration = params.get("SubtitleConfiguration")
        self._FaceBlurringEnabled = params.get("FaceBlurringEnabled")
        self._AudioSelectorName = params.get("AudioSelectorName")
        if params.get("AudioNormalization") is not None:
            self._AudioNormalization = AudioNormalizationSettings()
            self._AudioNormalization._deserialize(params.get("AudioNormalization"))
        self._AudioSampleRate = params.get("AudioSampleRate")
        self._FrameRateType = params.get("FrameRateType")
        self._FrameRateNumerator = params.get("FrameRateNumerator")
        self._FrameRateDenominator = params.get("FrameRateDenominator")
        self._BFramesNum = params.get("BFramesNum")
        self._RefFramesNum = params.get("RefFramesNum")
        if params.get("AdditionalRateSettings") is not None:
            self._AdditionalRateSettings = AdditionalRateSetting()
            self._AdditionalRateSettings._deserialize(params.get("AdditionalRateSettings"))
        if params.get("VideoCodecDetails") is not None:
            self._VideoCodecDetails = VideoCodecDetail()
            self._VideoCodecDetails._deserialize(params.get("VideoCodecDetails"))
        if params.get("AudioCodecDetails") is not None:
            self._AudioCodecDetails = AudioCodecDetail()
            self._AudioCodecDetails._deserialize(params.get("AudioCodecDetails"))
        self._MultiAudioTrackEnabled = params.get("MultiAudioTrackEnabled")
        if params.get("AudioTracks") is not None:
            self._AudioTracks = []
            for item in params.get("AudioTracks"):
                obj = AudioTrackInfo()
                obj._deserialize(item)
                self._AudioTracks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdditionalRateSetting(AbstractModel):
    """additional bit rate configuration.

    """

    def __init__(self):
        r"""
        :param _VideoMaxBitrate: The maximum bit rate in a VBR scenario must be a multiple of 1000 and between 50000 - 40000000.
        :type VideoMaxBitrate: int
        :param _BufferSize: Cache configuration supports configuring a Max Bitrate value of 1-4 times.
        :type BufferSize: int
        :param _QualityLevel: VBR scene is valid, video quality level, only supports user input numbers between 1-51.
        :type QualityLevel: int
        """
        self._VideoMaxBitrate = None
        self._BufferSize = None
        self._QualityLevel = None

    @property
    def VideoMaxBitrate(self):
        return self._VideoMaxBitrate

    @VideoMaxBitrate.setter
    def VideoMaxBitrate(self, VideoMaxBitrate):
        self._VideoMaxBitrate = VideoMaxBitrate

    @property
    def BufferSize(self):
        return self._BufferSize

    @BufferSize.setter
    def BufferSize(self, BufferSize):
        self._BufferSize = BufferSize

    @property
    def QualityLevel(self):
        return self._QualityLevel

    @QualityLevel.setter
    def QualityLevel(self, QualityLevel):
        self._QualityLevel = QualityLevel


    def _deserialize(self, params):
        self._VideoMaxBitrate = params.get("VideoMaxBitrate")
        self._BufferSize = params.get("BufferSize")
        self._QualityLevel = params.get("QualityLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AmazonS3Settings(AbstractModel):
    """Amazon S3 destination setting.

    """

    def __init__(self):
        r"""
        :param _AccessKeyID: Access key ID of the S3 sub-account.
        :type AccessKeyID: str
        :param _SecretAccessKey: Secret access key of the S3 sub-account.
        :type SecretAccessKey: str
        :param _Region: Region of S3.
        :type Region: str
        :param _Bucket: Bucket name of S3.
        :type Bucket: str
        :param _FilePath: File output path, which can be empty. If it is not empty, it starts with / and ends with /.
        :type FilePath: str
        :param _FileName: User-defined name, supports alphanumeric characters, underscores, and hyphens, with a length between 1 and 32 characters.
        :type FileName: str
        :param _FileExt: File suffix, only supports `jpg`.
        :type FileExt: str
        :param _TimeFormat: Support `unix` or `utc0`, default unix.
        :type TimeFormat: str
        """
        self._AccessKeyID = None
        self._SecretAccessKey = None
        self._Region = None
        self._Bucket = None
        self._FilePath = None
        self._FileName = None
        self._FileExt = None
        self._TimeFormat = None

    @property
    def AccessKeyID(self):
        return self._AccessKeyID

    @AccessKeyID.setter
    def AccessKeyID(self, AccessKeyID):
        self._AccessKeyID = AccessKeyID

    @property
    def SecretAccessKey(self):
        return self._SecretAccessKey

    @SecretAccessKey.setter
    def SecretAccessKey(self, SecretAccessKey):
        self._SecretAccessKey = SecretAccessKey

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def FilePath(self):
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileExt(self):
        return self._FileExt

    @FileExt.setter
    def FileExt(self, FileExt):
        self._FileExt = FileExt

    @property
    def TimeFormat(self):
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat


    def _deserialize(self, params):
        self._AccessKeyID = params.get("AccessKeyID")
        self._SecretAccessKey = params.get("SecretAccessKey")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        self._FilePath = params.get("FilePath")
        self._FileName = params.get("FileName")
        self._FileExt = params.get("FileExt")
        self._TimeFormat = params.get("TimeFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachedInput(AbstractModel):
    """Channel-associated input

    """

    def __init__(self):
        r"""
        :param _Id: Input ID
        :type Id: str
        :param _AudioSelectors: Audio selector for the input. There can be 0 to 20 audio selectors.
Note: this field may return `null`, indicating that no valid value was found.
        :type AudioSelectors: list of AudioSelectorInfo
        :param _PullBehavior: Pull mode. If the input type is `HLS_PULL` or `MP4_PULL`, you can set this parameter to `LOOP` or `ONCE`. `LOOP` is the default value.
Note: this field may return `null`, indicating that no valid value was found.
        :type PullBehavior: str
        :param _FailOverSettings: Input failover configuration
Note: this field may return `null`, indicating that no valid value was found.
        :type FailOverSettings: :class:`tencentcloud.mdl.v20200326.models.FailOverSettings`
        :param _CaptionSelectors: Caption selector for the input. There can be 0 to 1 audio selectors.
        :type CaptionSelectors: list of CaptionSelector
        """
        self._Id = None
        self._AudioSelectors = None
        self._PullBehavior = None
        self._FailOverSettings = None
        self._CaptionSelectors = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AudioSelectors(self):
        return self._AudioSelectors

    @AudioSelectors.setter
    def AudioSelectors(self, AudioSelectors):
        self._AudioSelectors = AudioSelectors

    @property
    def PullBehavior(self):
        return self._PullBehavior

    @PullBehavior.setter
    def PullBehavior(self, PullBehavior):
        self._PullBehavior = PullBehavior

    @property
    def FailOverSettings(self):
        return self._FailOverSettings

    @FailOverSettings.setter
    def FailOverSettings(self, FailOverSettings):
        self._FailOverSettings = FailOverSettings

    @property
    def CaptionSelectors(self):
        return self._CaptionSelectors

    @CaptionSelectors.setter
    def CaptionSelectors(self, CaptionSelectors):
        self._CaptionSelectors = CaptionSelectors


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("AudioSelectors") is not None:
            self._AudioSelectors = []
            for item in params.get("AudioSelectors"):
                obj = AudioSelectorInfo()
                obj._deserialize(item)
                self._AudioSelectors.append(obj)
        self._PullBehavior = params.get("PullBehavior")
        if params.get("FailOverSettings") is not None:
            self._FailOverSettings = FailOverSettings()
            self._FailOverSettings._deserialize(params.get("FailOverSettings"))
        if params.get("CaptionSelectors") is not None:
            self._CaptionSelectors = []
            for item in params.get("CaptionSelectors"):
                obj = CaptionSelector()
                obj._deserialize(item)
                self._CaptionSelectors.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioCodecDetail(AbstractModel):
    """Audio codec configuration.

    """

    def __init__(self):
        r"""
        :param _ChannelMode: Channel configuration, optional values: MONO (mono), STEREO (two-channel), 5.1 (surround).
        :type ChannelMode: str
        :param _Profile: Level in aac case, optional values: "LC" "HE-AAC" "HE-AACV2".
        :type Profile: str
        """
        self._ChannelMode = None
        self._Profile = None

    @property
    def ChannelMode(self):
        return self._ChannelMode

    @ChannelMode.setter
    def ChannelMode(self, ChannelMode):
        self._ChannelMode = ChannelMode

    @property
    def Profile(self):
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile


    def _deserialize(self, params):
        self._ChannelMode = params.get("ChannelMode")
        self._Profile = params.get("Profile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioNormalizationSettings(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _AudioNormalizationEnabled: 
        :type AudioNormalizationEnabled: int
        :param _TargetLUFS: 
        :type TargetLUFS: float
        """
        self._AudioNormalizationEnabled = None
        self._TargetLUFS = None

    @property
    def AudioNormalizationEnabled(self):
        return self._AudioNormalizationEnabled

    @AudioNormalizationEnabled.setter
    def AudioNormalizationEnabled(self, AudioNormalizationEnabled):
        self._AudioNormalizationEnabled = AudioNormalizationEnabled

    @property
    def TargetLUFS(self):
        return self._TargetLUFS

    @TargetLUFS.setter
    def TargetLUFS(self, TargetLUFS):
        self._TargetLUFS = TargetLUFS


    def _deserialize(self, params):
        self._AudioNormalizationEnabled = params.get("AudioNormalizationEnabled")
        self._TargetLUFS = params.get("TargetLUFS")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioPidSelectionInfo(AbstractModel):
    """Audio `Pid` selection.

    """

    def __init__(self):
        r"""
        :param _Pid: Audio `Pid`. Default value: 0.
        :type Pid: int
        """
        self._Pid = None

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid


    def _deserialize(self, params):
        self._Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioPipelineInputStatistics(AbstractModel):
    """Pipeline input audio statistics.

    """

    def __init__(self):
        r"""
        :param _Fps: Audio FPS.
        :type Fps: int
        :param _Rate: Audio bitrate in bps.
        :type Rate: int
        :param _Pid: Audio `Pid`, which is available only if the input is `rtp/udp`.
        :type Pid: int
        """
        self._Fps = None
        self._Rate = None
        self._Pid = None

    @property
    def Fps(self):
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid


    def _deserialize(self, params):
        self._Fps = params.get("Fps")
        self._Rate = params.get("Rate")
        self._Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioSelectorInfo(AbstractModel):
    """Audio selector.

    """

    def __init__(self):
        r"""
        :param _Name: Audio name, which can contain 1-32 letters, digits, and underscores.
        :type Name: str
        :param _AudioPidSelection: Audio `Pid` selection.
        :type AudioPidSelection: :class:`tencentcloud.mdl.v20200326.models.AudioPidSelectionInfo`
        :param _AudioSelectorType: Audio input type, optional values: 'PID_SELECTOR' 'TRACK_SELECTOR', default value PID_SELECTOR.
        :type AudioSelectorType: str
        :param _AudioTrackSelection: AudioTrack configuration.
        :type AudioTrackSelection: :class:`tencentcloud.mdl.v20200326.models.InputTracks`
        """
        self._Name = None
        self._AudioPidSelection = None
        self._AudioSelectorType = None
        self._AudioTrackSelection = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AudioPidSelection(self):
        return self._AudioPidSelection

    @AudioPidSelection.setter
    def AudioPidSelection(self, AudioPidSelection):
        self._AudioPidSelection = AudioPidSelection

    @property
    def AudioSelectorType(self):
        return self._AudioSelectorType

    @AudioSelectorType.setter
    def AudioSelectorType(self, AudioSelectorType):
        self._AudioSelectorType = AudioSelectorType

    @property
    def AudioTrackSelection(self):
        return self._AudioTrackSelection

    @AudioTrackSelection.setter
    def AudioTrackSelection(self, AudioTrackSelection):
        self._AudioTrackSelection = AudioTrackSelection


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("AudioPidSelection") is not None:
            self._AudioPidSelection = AudioPidSelectionInfo()
            self._AudioPidSelection._deserialize(params.get("AudioPidSelection"))
        self._AudioSelectorType = params.get("AudioSelectorType")
        if params.get("AudioTrackSelection") is not None:
            self._AudioTrackSelection = InputTracks()
            self._AudioTrackSelection._deserialize(params.get("AudioTrackSelection"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioTemplateInfo(AbstractModel):
    """Audio transcoding template.

    """

    def __init__(self):
        r"""
        :param _AudioSelectorName: Only `AttachedInputs.AudioSelectors.Name` can be selected. This parameter is required for RTP_PUSH and UDP_PUSH.
        :type AudioSelectorName: str
        :param _Name: Audio transcoding template name, which can contain 1-20 letters and digits.
        :type Name: str
        :param _Acodec: Audio codec. Valid value: AAC. Default value: AAC.
        :type Acodec: str
        :param _AudioBitrate: Audio bitrate. If this parameter is left empty, the original value will be used.
Valid values: 6000, 7000, 8000, 10000, 12000, 14000, 16000, 20000, 24000, 28000, 32000, 40000, 48000, 56000, 64000, 80000, 96000, 112000, 128000, 160000, 192000, 224000, 256000, 288000, 320000, 384000, 448000, 512000, 576000, 640000, 768000, 896000, 1024000
        :type AudioBitrate: int
        :param _LanguageCode: Audio language code, whose length is always 3 characters.
        :type LanguageCode: str
        :param _AudioNormalization: Audio transcoding special configuration information.
        :type AudioNormalization: :class:`tencentcloud.mdl.v20200326.models.AudioNormalizationSettings`
        :param _AudioSampleRate: Audio sampling rate, unit HZ.
        :type AudioSampleRate: int
        :param _AudioCodecDetails: Audio encoding parameters.
        :type AudioCodecDetails: :class:`tencentcloud.mdl.v20200326.models.AudioCodecDetail`
        """
        self._AudioSelectorName = None
        self._Name = None
        self._Acodec = None
        self._AudioBitrate = None
        self._LanguageCode = None
        self._AudioNormalization = None
        self._AudioSampleRate = None
        self._AudioCodecDetails = None

    @property
    def AudioSelectorName(self):
        return self._AudioSelectorName

    @AudioSelectorName.setter
    def AudioSelectorName(self, AudioSelectorName):
        self._AudioSelectorName = AudioSelectorName

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Acodec(self):
        return self._Acodec

    @Acodec.setter
    def Acodec(self, Acodec):
        self._Acodec = Acodec

    @property
    def AudioBitrate(self):
        return self._AudioBitrate

    @AudioBitrate.setter
    def AudioBitrate(self, AudioBitrate):
        self._AudioBitrate = AudioBitrate

    @property
    def LanguageCode(self):
        return self._LanguageCode

    @LanguageCode.setter
    def LanguageCode(self, LanguageCode):
        self._LanguageCode = LanguageCode

    @property
    def AudioNormalization(self):
        return self._AudioNormalization

    @AudioNormalization.setter
    def AudioNormalization(self, AudioNormalization):
        self._AudioNormalization = AudioNormalization

    @property
    def AudioSampleRate(self):
        return self._AudioSampleRate

    @AudioSampleRate.setter
    def AudioSampleRate(self, AudioSampleRate):
        self._AudioSampleRate = AudioSampleRate

    @property
    def AudioCodecDetails(self):
        return self._AudioCodecDetails

    @AudioCodecDetails.setter
    def AudioCodecDetails(self, AudioCodecDetails):
        self._AudioCodecDetails = AudioCodecDetails


    def _deserialize(self, params):
        self._AudioSelectorName = params.get("AudioSelectorName")
        self._Name = params.get("Name")
        self._Acodec = params.get("Acodec")
        self._AudioBitrate = params.get("AudioBitrate")
        self._LanguageCode = params.get("LanguageCode")
        if params.get("AudioNormalization") is not None:
            self._AudioNormalization = AudioNormalizationSettings()
            self._AudioNormalization._deserialize(params.get("AudioNormalization"))
        self._AudioSampleRate = params.get("AudioSampleRate")
        if params.get("AudioCodecDetails") is not None:
            self._AudioCodecDetails = AudioCodecDetail()
            self._AudioCodecDetails._deserialize(params.get("AudioCodecDetails"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioTrackInfo(AbstractModel):
    """Audio track configuration.

    """

    def __init__(self):
        r"""
        :param _TrackName: User input is limited to letters and numbers, the length should not exceed 20, and should not be repeated in the same channel.
        :type TrackName: str
        :param _AudioCodec: Only AAC is supported.
        :type AudioCodec: str
        :param _AudioBitrate: Audio bitrate.
        :type AudioBitrate: int
        :param _AudioSampleRate: Audio sample rate.
        :type AudioSampleRate: int
        :param _AudioSelectorName: Only values defined by AttachedInputs.$.AudioSelectors.$.audioPidSelection.pid can be entered.
        :type AudioSelectorName: str
        :param _AudioNormalization: Audio loudness configuration.
        :type AudioNormalization: :class:`tencentcloud.mdl.v20200326.models.AudioNormalizationSettings`
        :param _AudioCodecDetails: Audio encoding configuration.
        :type AudioCodecDetails: :class:`tencentcloud.mdl.v20200326.models.AudioCodecDetail`
        """
        self._TrackName = None
        self._AudioCodec = None
        self._AudioBitrate = None
        self._AudioSampleRate = None
        self._AudioSelectorName = None
        self._AudioNormalization = None
        self._AudioCodecDetails = None

    @property
    def TrackName(self):
        return self._TrackName

    @TrackName.setter
    def TrackName(self, TrackName):
        self._TrackName = TrackName

    @property
    def AudioCodec(self):
        return self._AudioCodec

    @AudioCodec.setter
    def AudioCodec(self, AudioCodec):
        self._AudioCodec = AudioCodec

    @property
    def AudioBitrate(self):
        return self._AudioBitrate

    @AudioBitrate.setter
    def AudioBitrate(self, AudioBitrate):
        self._AudioBitrate = AudioBitrate

    @property
    def AudioSampleRate(self):
        return self._AudioSampleRate

    @AudioSampleRate.setter
    def AudioSampleRate(self, AudioSampleRate):
        self._AudioSampleRate = AudioSampleRate

    @property
    def AudioSelectorName(self):
        return self._AudioSelectorName

    @AudioSelectorName.setter
    def AudioSelectorName(self, AudioSelectorName):
        self._AudioSelectorName = AudioSelectorName

    @property
    def AudioNormalization(self):
        return self._AudioNormalization

    @AudioNormalization.setter
    def AudioNormalization(self, AudioNormalization):
        self._AudioNormalization = AudioNormalization

    @property
    def AudioCodecDetails(self):
        return self._AudioCodecDetails

    @AudioCodecDetails.setter
    def AudioCodecDetails(self, AudioCodecDetails):
        self._AudioCodecDetails = AudioCodecDetails


    def _deserialize(self, params):
        self._TrackName = params.get("TrackName")
        self._AudioCodec = params.get("AudioCodec")
        self._AudioBitrate = params.get("AudioBitrate")
        self._AudioSampleRate = params.get("AudioSampleRate")
        self._AudioSelectorName = params.get("AudioSelectorName")
        if params.get("AudioNormalization") is not None:
            self._AudioNormalization = AudioNormalizationSettings()
            self._AudioNormalization._deserialize(params.get("AudioNormalization"))
        if params.get("AudioCodecDetails") is not None:
            self._AudioCodecDetails = AudioCodecDetail()
            self._AudioCodecDetails._deserialize(params.get("AudioCodecDetails"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CaptionSelector(AbstractModel):
    """Caption selector.

    """

    def __init__(self):
        r"""
        :param _Name: Caption selector name, which can contain 1-32 letters, digits, and underscores.
        :type Name: str
        :param _CaptionSourceType: Caption source type, only support `SCTE-128`.
        :type CaptionSourceType: str
        """
        self._Name = None
        self._CaptionSourceType = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CaptionSourceType(self):
        return self._CaptionSourceType

    @CaptionSourceType.setter
    def CaptionSourceType(self, CaptionSourceType):
        self._CaptionSourceType = CaptionSourceType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CaptionSourceType = params.get("CaptionSourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelAlertInfos(AbstractModel):
    """Channel alarm information.

    """

    def __init__(self):
        r"""
        :param _Pipeline0: Alarm details of pipeline 0 under this channel.
        :type Pipeline0: list of ChannelPipelineAlerts
        :param _Pipeline1: Alarm details of pipeline 1 under this channel.
        :type Pipeline1: list of ChannelPipelineAlerts
        """
        self._Pipeline0 = None
        self._Pipeline1 = None

    @property
    def Pipeline0(self):
        return self._Pipeline0

    @Pipeline0.setter
    def Pipeline0(self, Pipeline0):
        self._Pipeline0 = Pipeline0

    @property
    def Pipeline1(self):
        return self._Pipeline1

    @Pipeline1.setter
    def Pipeline1(self, Pipeline1):
        self._Pipeline1 = Pipeline1


    def _deserialize(self, params):
        if params.get("Pipeline0") is not None:
            self._Pipeline0 = []
            for item in params.get("Pipeline0"):
                obj = ChannelPipelineAlerts()
                obj._deserialize(item)
                self._Pipeline0.append(obj)
        if params.get("Pipeline1") is not None:
            self._Pipeline1 = []
            for item in params.get("Pipeline1"):
                obj = ChannelPipelineAlerts()
                obj._deserialize(item)
                self._Pipeline1.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelInputStatistics(AbstractModel):
    """Channel output statistics.

    """

    def __init__(self):
        r"""
        :param _InputId: Input ID.
        :type InputId: str
        :param _Statistics: Input statistics.
        :type Statistics: :class:`tencentcloud.mdl.v20200326.models.InputStatistics`
        """
        self._InputId = None
        self._Statistics = None

    @property
    def InputId(self):
        return self._InputId

    @InputId.setter
    def InputId(self, InputId):
        self._InputId = InputId

    @property
    def Statistics(self):
        return self._Statistics

    @Statistics.setter
    def Statistics(self, Statistics):
        self._Statistics = Statistics


    def _deserialize(self, params):
        self._InputId = params.get("InputId")
        if params.get("Statistics") is not None:
            self._Statistics = InputStatistics()
            self._Statistics._deserialize(params.get("Statistics"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelOutputsStatistics(AbstractModel):
    """Channel output information.

    """

    def __init__(self):
        r"""
        :param _OutputGroupName: Output group name.
        :type OutputGroupName: str
        :param _Statistics: Output group statistics.
        :type Statistics: :class:`tencentcloud.mdl.v20200326.models.OutputsStatistics`
        """
        self._OutputGroupName = None
        self._Statistics = None

    @property
    def OutputGroupName(self):
        return self._OutputGroupName

    @OutputGroupName.setter
    def OutputGroupName(self, OutputGroupName):
        self._OutputGroupName = OutputGroupName

    @property
    def Statistics(self):
        return self._Statistics

    @Statistics.setter
    def Statistics(self, Statistics):
        self._Statistics = Statistics


    def _deserialize(self, params):
        self._OutputGroupName = params.get("OutputGroupName")
        if params.get("Statistics") is not None:
            self._Statistics = OutputsStatistics()
            self._Statistics._deserialize(params.get("Statistics"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChannelPipelineAlerts(AbstractModel):
    """Channel alarm details.

    """

    def __init__(self):
        r"""
        :param _SetTime: Alarm start time in UTC time.
        :type SetTime: str
        :param _ClearTime: Alarm end time in UTC time.
This time is available only after the alarm ends.
        :type ClearTime: str
        :param _Type: Alarm type.
        :type Type: str
        :param _Message: Alarm details.
        :type Message: str
        """
        self._SetTime = None
        self._ClearTime = None
        self._Type = None
        self._Message = None

    @property
    def SetTime(self):
        return self._SetTime

    @SetTime.setter
    def SetTime(self, SetTime):
        self._SetTime = SetTime

    @property
    def ClearTime(self):
        return self._ClearTime

    @ClearTime.setter
    def ClearTime(self, ClearTime):
        self._ClearTime = ClearTime

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._SetTime = params.get("SetTime")
        self._ClearTime = params.get("ClearTime")
        self._Type = params.get("Type")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosSettings(AbstractModel):
    """Cos destination setting.

    """

    def __init__(self):
        r"""
        :param _Region: Region of COS.
        :type Region: str
        :param _Bucket: Bucket name of COS.
        :type Bucket: str
        :param _FilePath: File output path, which can be empty. If it is not empty, it  ends with /.
        :type FilePath: str
        :param _FileName: User-defined name, supports alphanumeric characters, underscores, and hyphens, with a length between 1 and 32 characters.
        :type FileName: str
        :param _FileExt: File suffix, only supports `jpg`.
        :type FileExt: str
        :param _TimeFormat: Support `unix` or `utc0`, default unix.
        :type TimeFormat: str
        """
        self._Region = None
        self._Bucket = None
        self._FilePath = None
        self._FileName = None
        self._FileExt = None
        self._TimeFormat = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def FilePath(self):
        return self._FilePath

    @FilePath.setter
    def FilePath(self, FilePath):
        self._FilePath = FilePath

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileExt(self):
        return self._FileExt

    @FileExt.setter
    def FileExt(self, FileExt):
        self._FileExt = FileExt

    @property
    def TimeFormat(self):
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        self._FilePath = params.get("FilePath")
        self._FileName = params.get("FileName")
        self._FileExt = params.get("FileExt")
        self._TimeFormat = params.get("TimeFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageSettings(AbstractModel):
    """Watermark image settings

    """

    def __init__(self):
        r"""
        :param _ImageType: Image file format. Valid values: png, jpg.
        :type ImageType: str
        :param _ImageContent: Base64 encoded image content
        :type ImageContent: str
        :param _Location: Origin. Valid values: TOP_LEFT, BOTTOM_LEFT, TOP_RIGHT, BOTTOM_RIGHT.
        :type Location: str
        :param _XPos: The watermark’s horizontal distance from the origin as a percentage of the video width. Value range: 0-100. Default: 10.
        :type XPos: int
        :param _YPos: The watermark’s vertical distance from the origin as a percentage of the video height. Value range: 0-100. Default: 10.
        :type YPos: int
        :param _Width: The watermark image’s width as a percentage of the video width. Value range: 0-100. Default: 10.
`0` means to scale the width proportionally to the height.
You cannot set both `Width` and `Height` to `0`.
        :type Width: int
        :param _Height: The watermark image’s height as a percentage of the video height. Value range: 0-100. Default: 10.
`0` means to scale the height proportionally to the width.
You cannot set both `Width` and `Height` to `0`.
        :type Height: int
        """
        self._ImageType = None
        self._ImageContent = None
        self._Location = None
        self._XPos = None
        self._YPos = None
        self._Width = None
        self._Height = None

    @property
    def ImageType(self):
        return self._ImageType

    @ImageType.setter
    def ImageType(self, ImageType):
        self._ImageType = ImageType

    @property
    def ImageContent(self):
        return self._ImageContent

    @ImageContent.setter
    def ImageContent(self, ImageContent):
        self._ImageContent = ImageContent

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def XPos(self):
        return self._XPos

    @XPos.setter
    def XPos(self, XPos):
        self._XPos = XPos

    @property
    def YPos(self):
        return self._YPos

    @YPos.setter
    def YPos(self, YPos):
        self._YPos = YPos

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._ImageType = params.get("ImageType")
        self._ImageContent = params.get("ImageContent")
        self._Location = params.get("Location")
        self._XPos = params.get("XPos")
        self._YPos = params.get("YPos")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLiveChannelRequest(AbstractModel):
    """CreateStreamLiveChannel request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Channel name, which can contain 1-32 case-sensitive letters, digits, and underscores and must be unique at the region level
        :type Name: str
        :param _AttachedInputs: Inputs to attach. You can attach 1 to 5 inputs.
        :type AttachedInputs: list of AttachedInput
        :param _OutputGroups: Configuration information of the channel's output groups. Quantity: [1, 10]
        :type OutputGroups: list of StreamLiveOutputGroupsInfo
        :param _AudioTemplates: Audio transcoding templates. Quantity: [1, 20]
        :type AudioTemplates: list of AudioTemplateInfo
        :param _VideoTemplates: Video transcoding templates. Quantity: [1, 10]
        :type VideoTemplates: list of VideoTemplateInfo
        :param _AVTemplates: Audio/Video transcoding templates. Quantity: [1, 10]
        :type AVTemplates: list of AVTemplate
        :param _CaptionTemplates: Subtitle template configuration, only AVTemplates are valid.
        :type CaptionTemplates: list of SubtitleConf
        :param _PlanSettings: Event settings
        :type PlanSettings: :class:`tencentcloud.mdl.v20200326.models.PlanSettings`
        :param _EventNotifySettings: The callback settings.
        :type EventNotifySettings: :class:`tencentcloud.mdl.v20200326.models.EventNotifySetting`
        :param _InputLossBehavior: Complement the last video frame settings.
        :type InputLossBehavior: :class:`tencentcloud.mdl.v20200326.models.InputLossBehaviorInfo`
        :param _PipelineInputSettings: Pipeline configuration.
        :type PipelineInputSettings: :class:`tencentcloud.mdl.v20200326.models.PipelineInputSettingsInfo`
        :param _InputAnalysisSettings: Recognition configuration for input content.
        :type InputAnalysisSettings: :class:`tencentcloud.mdl.v20200326.models.InputAnalysisInfo`
        :param _Tags: Console tag list.
        :type Tags: list of Tag
        :param _FrameCaptureTemplates: Frame capture templates.
        :type FrameCaptureTemplates: list of FrameCaptureTemplate
        """
        self._Name = None
        self._AttachedInputs = None
        self._OutputGroups = None
        self._AudioTemplates = None
        self._VideoTemplates = None
        self._AVTemplates = None
        self._CaptionTemplates = None
        self._PlanSettings = None
        self._EventNotifySettings = None
        self._InputLossBehavior = None
        self._PipelineInputSettings = None
        self._InputAnalysisSettings = None
        self._Tags = None
        self._FrameCaptureTemplates = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AttachedInputs(self):
        return self._AttachedInputs

    @AttachedInputs.setter
    def AttachedInputs(self, AttachedInputs):
        self._AttachedInputs = AttachedInputs

    @property
    def OutputGroups(self):
        return self._OutputGroups

    @OutputGroups.setter
    def OutputGroups(self, OutputGroups):
        self._OutputGroups = OutputGroups

    @property
    def AudioTemplates(self):
        return self._AudioTemplates

    @AudioTemplates.setter
    def AudioTemplates(self, AudioTemplates):
        self._AudioTemplates = AudioTemplates

    @property
    def VideoTemplates(self):
        return self._VideoTemplates

    @VideoTemplates.setter
    def VideoTemplates(self, VideoTemplates):
        self._VideoTemplates = VideoTemplates

    @property
    def AVTemplates(self):
        return self._AVTemplates

    @AVTemplates.setter
    def AVTemplates(self, AVTemplates):
        self._AVTemplates = AVTemplates

    @property
    def CaptionTemplates(self):
        return self._CaptionTemplates

    @CaptionTemplates.setter
    def CaptionTemplates(self, CaptionTemplates):
        self._CaptionTemplates = CaptionTemplates

    @property
    def PlanSettings(self):
        return self._PlanSettings

    @PlanSettings.setter
    def PlanSettings(self, PlanSettings):
        self._PlanSettings = PlanSettings

    @property
    def EventNotifySettings(self):
        return self._EventNotifySettings

    @EventNotifySettings.setter
    def EventNotifySettings(self, EventNotifySettings):
        self._EventNotifySettings = EventNotifySettings

    @property
    def InputLossBehavior(self):
        return self._InputLossBehavior

    @InputLossBehavior.setter
    def InputLossBehavior(self, InputLossBehavior):
        self._InputLossBehavior = InputLossBehavior

    @property
    def PipelineInputSettings(self):
        return self._PipelineInputSettings

    @PipelineInputSettings.setter
    def PipelineInputSettings(self, PipelineInputSettings):
        self._PipelineInputSettings = PipelineInputSettings

    @property
    def InputAnalysisSettings(self):
        return self._InputAnalysisSettings

    @InputAnalysisSettings.setter
    def InputAnalysisSettings(self, InputAnalysisSettings):
        self._InputAnalysisSettings = InputAnalysisSettings

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def FrameCaptureTemplates(self):
        return self._FrameCaptureTemplates

    @FrameCaptureTemplates.setter
    def FrameCaptureTemplates(self, FrameCaptureTemplates):
        self._FrameCaptureTemplates = FrameCaptureTemplates


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("AttachedInputs") is not None:
            self._AttachedInputs = []
            for item in params.get("AttachedInputs"):
                obj = AttachedInput()
                obj._deserialize(item)
                self._AttachedInputs.append(obj)
        if params.get("OutputGroups") is not None:
            self._OutputGroups = []
            for item in params.get("OutputGroups"):
                obj = StreamLiveOutputGroupsInfo()
                obj._deserialize(item)
                self._OutputGroups.append(obj)
        if params.get("AudioTemplates") is not None:
            self._AudioTemplates = []
            for item in params.get("AudioTemplates"):
                obj = AudioTemplateInfo()
                obj._deserialize(item)
                self._AudioTemplates.append(obj)
        if params.get("VideoTemplates") is not None:
            self._VideoTemplates = []
            for item in params.get("VideoTemplates"):
                obj = VideoTemplateInfo()
                obj._deserialize(item)
                self._VideoTemplates.append(obj)
        if params.get("AVTemplates") is not None:
            self._AVTemplates = []
            for item in params.get("AVTemplates"):
                obj = AVTemplate()
                obj._deserialize(item)
                self._AVTemplates.append(obj)
        if params.get("CaptionTemplates") is not None:
            self._CaptionTemplates = []
            for item in params.get("CaptionTemplates"):
                obj = SubtitleConf()
                obj._deserialize(item)
                self._CaptionTemplates.append(obj)
        if params.get("PlanSettings") is not None:
            self._PlanSettings = PlanSettings()
            self._PlanSettings._deserialize(params.get("PlanSettings"))
        if params.get("EventNotifySettings") is not None:
            self._EventNotifySettings = EventNotifySetting()
            self._EventNotifySettings._deserialize(params.get("EventNotifySettings"))
        if params.get("InputLossBehavior") is not None:
            self._InputLossBehavior = InputLossBehaviorInfo()
            self._InputLossBehavior._deserialize(params.get("InputLossBehavior"))
        if params.get("PipelineInputSettings") is not None:
            self._PipelineInputSettings = PipelineInputSettingsInfo()
            self._PipelineInputSettings._deserialize(params.get("PipelineInputSettings"))
        if params.get("InputAnalysisSettings") is not None:
            self._InputAnalysisSettings = InputAnalysisInfo()
            self._InputAnalysisSettings._deserialize(params.get("InputAnalysisSettings"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("FrameCaptureTemplates") is not None:
            self._FrameCaptureTemplates = []
            for item in params.get("FrameCaptureTemplates"):
                obj = FrameCaptureTemplate()
                obj._deserialize(item)
                self._FrameCaptureTemplates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLiveChannelResponse(AbstractModel):
    """CreateStreamLiveChannel response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Channel ID
        :type Id: str
        :param _TagMsg: Tag prompt information, this information will be attached when the tag operation fails.
        :type TagMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._TagMsg = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TagMsg(self):
        return self._TagMsg

    @TagMsg.setter
    def TagMsg(self, TagMsg):
        self._TagMsg = TagMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._TagMsg = params.get("TagMsg")
        self._RequestId = params.get("RequestId")


class CreateStreamLiveInputRequest(AbstractModel):
    """CreateStreamLiveInput request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Input name, which can contain 1-32 case-sensitive letters, digits, and underscores and must be unique at the region level
        :type Name: str
        :param _Type: Input type
Valid values: `RTMP_PUSH`, `RTP_PUSH`, `UDP_PUSH`, `RTMP_PULL`, `HLS_PULL`, `MP4_PULL`
        :type Type: str
        :param _SecurityGroupIds: ID of the input security group to attach
You can attach only one security group to an input.
        :type SecurityGroupIds: list of str
        :param _InputSettings: Input settings. For the type `RTMP_PUSH`, `RTMP_PULL`, `HLS_PULL`, or `MP4_PULL`, 1 or 2 inputs of the corresponding type can be configured.
        :type InputSettings: list of InputSettingInfo
        """
        self._Name = None
        self._Type = None
        self._SecurityGroupIds = None
        self._InputSettings = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def InputSettings(self):
        return self._InputSettings

    @InputSettings.setter
    def InputSettings(self, InputSettings):
        self._InputSettings = InputSettings


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("InputSettings") is not None:
            self._InputSettings = []
            for item in params.get("InputSettings"):
                obj = InputSettingInfo()
                obj._deserialize(item)
                self._InputSettings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLiveInputResponse(AbstractModel):
    """CreateStreamLiveInput response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Input ID
        :type Id: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateStreamLiveInputSecurityGroupRequest(AbstractModel):
    """CreateStreamLiveInputSecurityGroup request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Input security group name, which can contain case-sensitive letters, digits, and underscores and must be unique at the region level
        :type Name: str
        :param _Whitelist: Allowlist entries. Quantity: [1, 10]
        :type Whitelist: list of str
        """
        self._Name = None
        self._Whitelist = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Whitelist(self):
        return self._Whitelist

    @Whitelist.setter
    def Whitelist(self, Whitelist):
        self._Whitelist = Whitelist


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Whitelist = params.get("Whitelist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLiveInputSecurityGroupResponse(AbstractModel):
    """CreateStreamLiveInputSecurityGroup response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Security group ID
        :type Id: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateStreamLivePlanRequest(AbstractModel):
    """CreateStreamLivePlan request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: ID of the channel for which you want to configure an event
        :type ChannelId: str
        :param _Plan: Event configuration
        :type Plan: :class:`tencentcloud.mdl.v20200326.models.PlanReq`
        """
        self._ChannelId = None
        self._Plan = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def Plan(self):
        return self._Plan

    @Plan.setter
    def Plan(self, Plan):
        self._Plan = Plan


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        if params.get("Plan") is not None:
            self._Plan = PlanReq()
            self._Plan._deserialize(params.get("Plan"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLivePlanResponse(AbstractModel):
    """CreateStreamLivePlan response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateStreamLiveWatermarkRequest(AbstractModel):
    """CreateStreamLiveWatermark request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Watermark name
        :type Name: str
        :param _Type: Watermark type. Valid values: STATIC_IMAGE, TEXT.
        :type Type: str
        :param _ImageSettings: Watermark image settings. This parameter is valid if `Type` is `STATIC_IMAGE`.
        :type ImageSettings: :class:`tencentcloud.mdl.v20200326.models.CreateImageSettings`
        :param _TextSettings: Watermark text settings. This parameter is valid if `Type` is `TEXT`.
        :type TextSettings: :class:`tencentcloud.mdl.v20200326.models.CreateTextSettings`
        """
        self._Name = None
        self._Type = None
        self._ImageSettings = None
        self._TextSettings = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ImageSettings(self):
        return self._ImageSettings

    @ImageSettings.setter
    def ImageSettings(self, ImageSettings):
        self._ImageSettings = ImageSettings

    @property
    def TextSettings(self):
        return self._TextSettings

    @TextSettings.setter
    def TextSettings(self, TextSettings):
        self._TextSettings = TextSettings


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("ImageSettings") is not None:
            self._ImageSettings = CreateImageSettings()
            self._ImageSettings._deserialize(params.get("ImageSettings"))
        if params.get("TextSettings") is not None:
            self._TextSettings = CreateTextSettings()
            self._TextSettings._deserialize(params.get("TextSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStreamLiveWatermarkResponse(AbstractModel):
    """CreateStreamLiveWatermark response structure.

    """

    def __init__(self):
        r"""
        :param _Id: Watermark ID
        :type Id: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateTextSettings(AbstractModel):
    """Watermark text settings

    """

    def __init__(self):
        r"""
        :param _Text: Text
        :type Text: str
        :param _Location: Origin. Valid values: TOP_LEFT, BOTTOM_LEFT, TOP_RIGHT, BOTTOM_RIGHT.
        :type Location: str
        :param _XPos: The watermark’s horizontal distance from the origin as a percentage of the video width. Value range: 0-100. Default: 10.
        :type XPos: int
        :param _YPos: The watermark’s vertical distance from the origin as a percentage of the video height. Value range: 0-100. Default: 10.
        :type YPos: int
        :param _FontSize: Font size. Value range: 25-50.
        :type FontSize: int
        :param _FontColor: Font color, which is an RGB color value. Default value: 0x000000.
        :type FontColor: str
        """
        self._Text = None
        self._Location = None
        self._XPos = None
        self._YPos = None
        self._FontSize = None
        self._FontColor = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def XPos(self):
        return self._XPos

    @XPos.setter
    def XPos(self, XPos):
        self._XPos = XPos

    @property
    def YPos(self):
        return self._YPos

    @YPos.setter
    def YPos(self, YPos):
        self._YPos = YPos

    @property
    def FontSize(self):
        return self._FontSize

    @FontSize.setter
    def FontSize(self, FontSize):
        self._FontSize = FontSize

    @property
    def FontColor(self):
        return self._FontColor

    @FontColor.setter
    def FontColor(self, FontColor):
        self._FontColor = FontColor


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Location = params.get("Location")
        self._XPos = params.get("XPos")
        self._YPos = params.get("YPos")
        self._FontSize = params.get("FontSize")
        self._FontColor = params.get("FontColor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DashRemuxSettingsInfo(AbstractModel):
    """DASH configuration information.

    """

    def __init__(self):
        r"""
        :param _SegmentDuration: Segment duration in ms. Value range: [1000,30000]. Default value: 4000. The value can only be a multiple of 1,000.
        :type SegmentDuration: int
        :param _SegmentNumber: Number of segments. Value range: [1,30]. Default value: 5.
        :type SegmentNumber: int
        :param _PeriodTriggers: Whether to enable multi-period. Valid values: CLOSE/OPEN. Default value: CLOSE.
        :type PeriodTriggers: str
        :param _H265PackageType: The HLS package type when the H.265 codec is used. Valid values: `hvc1`, `hev1` (default).
        :type H265PackageType: str
        """
        self._SegmentDuration = None
        self._SegmentNumber = None
        self._PeriodTriggers = None
        self._H265PackageType = None

    @property
    def SegmentDuration(self):
        return self._SegmentDuration

    @SegmentDuration.setter
    def SegmentDuration(self, SegmentDuration):
        self._SegmentDuration = SegmentDuration

    @property
    def SegmentNumber(self):
        return self._SegmentNumber

    @SegmentNumber.setter
    def SegmentNumber(self, SegmentNumber):
        self._SegmentNumber = SegmentNumber

    @property
    def PeriodTriggers(self):
        return self._PeriodTriggers

    @PeriodTriggers.setter
    def PeriodTriggers(self, PeriodTriggers):
        self._PeriodTriggers = PeriodTriggers

    @property
    def H265PackageType(self):
        return self._H265PackageType

    @H265PackageType.setter
    def H265PackageType(self, H265PackageType):
        self._H265PackageType = H265PackageType


    def _deserialize(self, params):
        self._SegmentDuration = params.get("SegmentDuration")
        self._SegmentNumber = params.get("SegmentNumber")
        self._PeriodTriggers = params.get("PeriodTriggers")
        self._H265PackageType = params.get("H265PackageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamLiveChannelRequest(AbstractModel):
    """DeleteStreamLiveChannel request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Channel ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamLiveChannelResponse(AbstractModel):
    """DeleteStreamLiveChannel response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteStreamLiveInputRequest(AbstractModel):
    """DeleteStreamLiveInput request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Input ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamLiveInputResponse(AbstractModel):
    """DeleteStreamLiveInput response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteStreamLiveInputSecurityGroupRequest(AbstractModel):
    """DeleteStreamLiveInputSecurityGroup request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Input security group ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamLiveInputSecurityGroupResponse(AbstractModel):
    """DeleteStreamLiveInputSecurityGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteStreamLivePlanRequest(AbstractModel):
    """DeleteStreamLivePlan request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: ID of the channel whose event is to be deleted
        :type ChannelId: str
        :param _EventName: Name of the event to delete
        :type EventName: str
        """
        self._ChannelId = None
        self._EventName = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def EventName(self):
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._EventName = params.get("EventName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamLivePlanResponse(AbstractModel):
    """DeleteStreamLivePlan response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteStreamLiveWatermarkRequest(AbstractModel):
    """DeleteStreamLiveWatermark request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Watermark ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStreamLiveWatermarkResponse(AbstractModel):
    """DeleteStreamLiveWatermark response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeliveryRestrictionsInfo(AbstractModel):
    """Distribution configuration information.

    """

    def __init__(self):
        r"""
        :param _WebDeliveryAllowed: Corresponds to SCTE-35 web_delivery_allowed_flag parameter.
        :type WebDeliveryAllowed: str
        :param _NoRegionalBlackout: Corresponds to SCTE-35 no_regional_blackout_flag parameter.
        :type NoRegionalBlackout: str
        :param _ArchiveAllowed: Corresponds to SCTE-35 archive_allowed_flag.
        :type ArchiveAllowed: str
        :param _DeviceRestrictions: Corresponds to SCTE-35 device_restrictions parameter.
        :type DeviceRestrictions: str
        """
        self._WebDeliveryAllowed = None
        self._NoRegionalBlackout = None
        self._ArchiveAllowed = None
        self._DeviceRestrictions = None

    @property
    def WebDeliveryAllowed(self):
        return self._WebDeliveryAllowed

    @WebDeliveryAllowed.setter
    def WebDeliveryAllowed(self, WebDeliveryAllowed):
        self._WebDeliveryAllowed = WebDeliveryAllowed

    @property
    def NoRegionalBlackout(self):
        return self._NoRegionalBlackout

    @NoRegionalBlackout.setter
    def NoRegionalBlackout(self, NoRegionalBlackout):
        self._NoRegionalBlackout = NoRegionalBlackout

    @property
    def ArchiveAllowed(self):
        return self._ArchiveAllowed

    @ArchiveAllowed.setter
    def ArchiveAllowed(self, ArchiveAllowed):
        self._ArchiveAllowed = ArchiveAllowed

    @property
    def DeviceRestrictions(self):
        return self._DeviceRestrictions

    @DeviceRestrictions.setter
    def DeviceRestrictions(self, DeviceRestrictions):
        self._DeviceRestrictions = DeviceRestrictions


    def _deserialize(self, params):
        self._WebDeliveryAllowed = params.get("WebDeliveryAllowed")
        self._NoRegionalBlackout = params.get("NoRegionalBlackout")
        self._ArchiveAllowed = params.get("ArchiveAllowed")
        self._DeviceRestrictions = params.get("DeviceRestrictions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageSettings(AbstractModel):
    """Watermark image settings

    """

    def __init__(self):
        r"""
        :param _Location: Origin
        :type Location: str
        :param _XPos: The watermark image’s horizontal distance from the origin as a percentage of the video width
        :type XPos: int
        :param _YPos: The watermark image’s vertical distance from the origin as a percentage of the video height
        :type YPos: int
        :param _Width: The watermark image’s width as a percentage of the video width
        :type Width: int
        :param _Height: The watermark image’s height as a percentage of the video height
        :type Height: int
        """
        self._Location = None
        self._XPos = None
        self._YPos = None
        self._Width = None
        self._Height = None

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def XPos(self):
        return self._XPos

    @XPos.setter
    def XPos(self, XPos):
        self._XPos = XPos

    @property
    def YPos(self):
        return self._YPos

    @YPos.setter
    def YPos(self, YPos):
        self._YPos = YPos

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._Location = params.get("Location")
        self._XPos = params.get("XPos")
        self._YPos = params.get("YPos")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMediaLiveHighlightResultRequest(AbstractModel):
    """DescribeMediaLiveHighlightResult request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Media live broadcast channel ID.
        :type Id: str
        :param _StartTime: Query start time, unix timestamp, query data within the last 6 hours by default, and the maximum query range supports the last 7 days.
        :type StartTime: int
        :param _EndTime: Query end time, Unix timestamp, query data within the last 6 hours by default, and the maximum query range supports the last 7 days.
        :type EndTime: int
        :param _PageNum: Paging query page number.
        :type PageNum: int
        :param _PageSize: Paging query the size of each page.
        :type PageSize: int
        """
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._PageNum = None
        self._PageSize = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMediaLiveHighlightResultResponse(AbstractModel):
    """DescribeMediaLiveHighlightResult response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Highlight results information.
        :type Info: list of HighlightResInfoResp
        :param _Id: Collection id.
        :type Id: str
        :param _ChannelId: Media live broadcast channel id.
        :type ChannelId: str
        :param _PageNum: Number of pages.
        :type PageNum: int
        :param _PageSize: Paging Size.
        :type PageSize: int
        :param _TotalNum: The total number of eligible entries in the background.
        :type TotalNum: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._Id = None
        self._ChannelId = None
        self._PageNum = None
        self._PageSize = None
        self._TotalNum = None
        self._RequestId = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = []
            for item in params.get("Info"):
                obj = HighlightResInfoResp()
                obj._deserialize(item)
                self._Info.append(obj)
        self._Id = params.get("Id")
        self._ChannelId = params.get("ChannelId")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TotalNum = params.get("TotalNum")
        self._RequestId = params.get("RequestId")


class DescribeStreamLiveChannelAlertsRequest(AbstractModel):
    """DescribeStreamLiveChannelAlerts request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel ID
        :type ChannelId: str
        """
        self._ChannelId = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLiveChannelAlertsResponse(AbstractModel):
    """DescribeStreamLiveChannelAlerts response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: Alarm information of the channel’s two pipelines
        :type Infos: :class:`tencentcloud.mdl.v20200326.models.ChannelAlertInfos`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._RequestId = None

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self._Infos = ChannelAlertInfos()
            self._Infos._deserialize(params.get("Infos"))
        self._RequestId = params.get("RequestId")


class DescribeStreamLiveChannelInputStatisticsRequest(AbstractModel):
    """DescribeStreamLiveChannelInputStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel ID
        :type ChannelId: str
        :param _StartTime: Start time for query, which is 1 hour ago by default. You can query statistics in the last 7 days.
UTC time, such as `2020-01-01T12:00:00Z`
        :type StartTime: str
        :param _EndTime: End time for query, which is 1 hour after `StartTime` by default
UTC time, such as `2020-01-01T12:00:00Z`
        :type EndTime: str
        :param _Period: Data collection interval. Valid values: `5s`, `1min` (default), `5min`, `15min`
        :type Period: str
        """
        self._ChannelId = None
        self._StartTime = None
        self._EndTime = None
        self._Period = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLiveChannelInputStatisticsResponse(AbstractModel):
    """DescribeStreamLiveChannelInputStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: Channel input statistics
        :type Infos: list of ChannelInputStatistics
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._RequestId = None

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = ChannelInputStatistics()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamLiveChannelLogsRequest(AbstractModel):
    """DescribeStreamLiveChannelLogs request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel ID
        :type ChannelId: str
        :param _StartTime: Start time for query, which is 1 hour ago by default. You can query logs in the last 7 days.
UTC time, such as `2020-01-01T12:00:00Z`
        :type StartTime: str
        :param _EndTime: End time for query, which is 1 hour after `StartTime` by default
UTC time, such as `2020-01-01T12:00:00Z`
        :type EndTime: str
        """
        self._ChannelId = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLiveChannelLogsResponse(AbstractModel):
    """DescribeStreamLiveChannelLogs response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: Pipeline push information
        :type Infos: :class:`tencentcloud.mdl.v20200326.models.PipelineLogInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._RequestId = None

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self._Infos = PipelineLogInfo()
            self._Infos._deserialize(params.get("Infos"))
        self._RequestId = params.get("RequestId")


class DescribeStreamLiveChannelOutputStatisticsRequest(AbstractModel):
    """DescribeStreamLiveChannelOutputStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: Channel ID
        :type ChannelId: str
        :param _StartTime: Start time for query, which is 1 hour ago by default. You can query statistics in the last 7 days.
UTC time, such as `2020-01-01T12:00:00Z`
        :type StartTime: str
        :param _EndTime: End time for query, which is 1 hour after `StartTime` by default
UTC time, such as `2020-01-01T12:00:00Z`
        :type EndTime: str
        :param _Period: Data collection interval. Valid values: `5s`, `1min` (default), `5min`, `15min`
        :type Period: str
        """
        self._ChannelId = None
        self._StartTime = None
        self._EndTime = None
        self._Period = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLiveChannelOutputStatisticsResponse(AbstractModel):
    """DescribeStreamLiveChannelOutputStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: Channel output information
        :type Infos: list of ChannelOutputsStatistics
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._RequestId = None

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = ChannelOutputsStatistics()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamLiveChannelRequest(AbstractModel):
    """DescribeStreamLiveChannel request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Channel ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLiveChannelResponse(AbstractModel):
    """DescribeStreamLiveChannel response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Channel information
        :type Info: :class:`tencentcloud.mdl.v20200326.models.StreamLiveChannelInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = StreamLiveChannelInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class DescribeStreamLiveChannelsRequest(AbstractModel):
    """DescribeStreamLiveChannels request structure.

    """


class DescribeStreamLiveChannelsResponse(AbstractModel):
    """DescribeStreamLiveChannels response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: List of channel information
Note: this field may return `null`, indicating that no valid value was found.
        :type Infos: list of StreamLiveChannelInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._RequestId = None

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = StreamLiveChannelInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamLiveInputRequest(AbstractModel):
    """DescribeStreamLiveInput request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Input ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLiveInputResponse(AbstractModel):
    """DescribeStreamLiveInput response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Input information
        :type Info: :class:`tencentcloud.mdl.v20200326.models.InputInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = InputInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class DescribeStreamLiveInputSecurityGroupRequest(AbstractModel):
    """DescribeStreamLiveInputSecurityGroup request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Input security group ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLiveInputSecurityGroupResponse(AbstractModel):
    """DescribeStreamLiveInputSecurityGroup response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Input security group information
        :type Info: :class:`tencentcloud.mdl.v20200326.models.InputSecurityGroupInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = InputSecurityGroupInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class DescribeStreamLiveInputSecurityGroupsRequest(AbstractModel):
    """DescribeStreamLiveInputSecurityGroups request structure.

    """


class DescribeStreamLiveInputSecurityGroupsResponse(AbstractModel):
    """DescribeStreamLiveInputSecurityGroups response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: List of input security group information
        :type Infos: list of InputSecurityGroupInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._RequestId = None

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = InputSecurityGroupInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamLiveInputsRequest(AbstractModel):
    """DescribeStreamLiveInputs request structure.

    """


class DescribeStreamLiveInputsResponse(AbstractModel):
    """DescribeStreamLiveInputs response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: List of input information
Note: this field may return `null`, indicating that no valid value was found.
        :type Infos: list of InputInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._RequestId = None

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = InputInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamLivePlansRequest(AbstractModel):
    """DescribeStreamLivePlans request structure.

    """

    def __init__(self):
        r"""
        :param _ChannelId: ID of the channel whose events you want to query
        :type ChannelId: str
        """
        self._ChannelId = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLivePlansResponse(AbstractModel):
    """DescribeStreamLivePlans response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: List of event information
Note: this field may return `null`, indicating that no valid value was found.
        :type Infos: list of PlanResp
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._RequestId = None

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = PlanResp()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStreamLiveRegionsRequest(AbstractModel):
    """DescribeStreamLiveRegions request structure.

    """


class DescribeStreamLiveRegionsResponse(AbstractModel):
    """DescribeStreamLiveRegions response structure.

    """

    def __init__(self):
        r"""
        :param _Info: StreamLive region information
        :type Info: :class:`tencentcloud.mdl.v20200326.models.StreamLiveRegionInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = StreamLiveRegionInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class DescribeStreamLiveTranscodeDetailRequest(AbstractModel):
    """DescribeStreamLiveTranscodeDetail request structure.

    """

    def __init__(self):
        r"""
        :param _StartDayTime: The query start time (UTC+8) in the format of yyyy-MM-dd.
You can only query data in the last month (not including the current day).
        :type StartDayTime: str
        :param _EndDayTime: The query end time (UTC+8) in the format of yyyy-MM-dd.
You can only query data in the last month (not including the current day).
        :type EndDayTime: str
        :param _ChannelId: The channel ID (optional).
        :type ChannelId: str
        :param _PageNum: The number of pages. Default value: 1.
The value cannot exceed 100.
        :type PageNum: int
        :param _PageSize: The number of records per page. Default value: 10.
Value range: 1-1000.
        :type PageSize: int
        """
        self._StartDayTime = None
        self._EndDayTime = None
        self._ChannelId = None
        self._PageNum = None
        self._PageSize = None

    @property
    def StartDayTime(self):
        return self._StartDayTime

    @StartDayTime.setter
    def StartDayTime(self, StartDayTime):
        self._StartDayTime = StartDayTime

    @property
    def EndDayTime(self):
        return self._EndDayTime

    @EndDayTime.setter
    def EndDayTime(self, EndDayTime):
        self._EndDayTime = EndDayTime

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._StartDayTime = params.get("StartDayTime")
        self._EndDayTime = params.get("EndDayTime")
        self._ChannelId = params.get("ChannelId")
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLiveTranscodeDetailResponse(AbstractModel):
    """DescribeStreamLiveTranscodeDetail response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: A list of the transcoding information.
        :type Infos: list of DescribeTranscodeDetailInfo
        :param _PageNum: The number of the current page.
        :type PageNum: int
        :param _PageSize: The number of records per page.
        :type PageSize: int
        :param _TotalNum: The total number of records.
        :type TotalNum: int
        :param _TotalPage: The total number of pages.
        :type TotalPage: int
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._PageNum = None
        self._PageSize = None
        self._TotalNum = None
        self._TotalPage = None
        self._RequestId = None

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def TotalNum(self):
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def TotalPage(self):
        return self._TotalPage

    @TotalPage.setter
    def TotalPage(self, TotalPage):
        self._TotalPage = TotalPage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = DescribeTranscodeDetailInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._TotalNum = params.get("TotalNum")
        self._TotalPage = params.get("TotalPage")
        self._RequestId = params.get("RequestId")


class DescribeStreamLiveWatermarkRequest(AbstractModel):
    """DescribeStreamLiveWatermark request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Watermark ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamLiveWatermarkResponse(AbstractModel):
    """DescribeStreamLiveWatermark response structure.

    """

    def __init__(self):
        r"""
        :param _Info: Watermark information
        :type Info: :class:`tencentcloud.mdl.v20200326.models.DescribeWatermarkInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = DescribeWatermarkInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class DescribeStreamLiveWatermarksRequest(AbstractModel):
    """DescribeStreamLiveWatermarks request structure.

    """


class DescribeStreamLiveWatermarksResponse(AbstractModel):
    """DescribeStreamLiveWatermarks response structure.

    """

    def __init__(self):
        r"""
        :param _Infos: List of watermark information
        :type Infos: list of DescribeWatermarkInfo
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Infos = None
        self._RequestId = None

    @property
    def Infos(self):
        return self._Infos

    @Infos.setter
    def Infos(self, Infos):
        self._Infos = Infos

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Infos") is not None:
            self._Infos = []
            for item in params.get("Infos"):
                obj = DescribeWatermarkInfo()
                obj._deserialize(item)
                self._Infos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTextSettings(AbstractModel):
    """Watermark text settings

    """

    def __init__(self):
        r"""
        :param _Text: Text
        :type Text: str
        :param _Location: Origin
        :type Location: str
        :param _XPos: The watermark image’s horizontal distance from the origin as a percentage of the video width
        :type XPos: int
        :param _YPos: The watermark image’s vertical distance from the origin as a percentage of the video height
        :type YPos: int
        :param _FontSize: Font size
        :type FontSize: int
        :param _FontColor: Font color
        :type FontColor: str
        """
        self._Text = None
        self._Location = None
        self._XPos = None
        self._YPos = None
        self._FontSize = None
        self._FontColor = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def XPos(self):
        return self._XPos

    @XPos.setter
    def XPos(self, XPos):
        self._XPos = XPos

    @property
    def YPos(self):
        return self._YPos

    @YPos.setter
    def YPos(self, YPos):
        self._YPos = YPos

    @property
    def FontSize(self):
        return self._FontSize

    @FontSize.setter
    def FontSize(self, FontSize):
        self._FontSize = FontSize

    @property
    def FontColor(self):
        return self._FontColor

    @FontColor.setter
    def FontColor(self, FontColor):
        self._FontColor = FontColor


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Location = params.get("Location")
        self._XPos = params.get("XPos")
        self._YPos = params.get("YPos")
        self._FontSize = params.get("FontSize")
        self._FontColor = params.get("FontColor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTranscodeDetailInfo(AbstractModel):
    """Transcoding details.

    """

    def __init__(self):
        r"""
        :param _ChannelId: The channel ID.
        :type ChannelId: str
        :param _StartTime: The start time (UTC+8) of transcoding in the format of yyyy-MM-dd HH:mm:ss.
        :type StartTime: str
        :param _EndTime: The end time (UTC+8) of transcoding in the format of yyyy-MM-dd HH:mm:ss.
        :type EndTime: str
        :param _Duration: The duration (s) of transcoding.
        :type Duration: int
        :param _ModuleCodec: The encoding method.
Examples:
`liveprocessor_H264`: Live transcoding-H264
`liveprocessor_H265`: Live transcoding-H265
`topspeed_H264`: Top speed codec-H264
`topspeed_H265`: Top speed codec-H265
        :type ModuleCodec: str
        :param _Bitrate: The target bitrate (Kbps).
        :type Bitrate: int
        :param _Type: The transcoding type.
        :type Type: str
        :param _PushDomain: The push domain name.
        :type PushDomain: str
        :param _Resolution: The target resolution.
        :type Resolution: str
        """
        self._ChannelId = None
        self._StartTime = None
        self._EndTime = None
        self._Duration = None
        self._ModuleCodec = None
        self._Bitrate = None
        self._Type = None
        self._PushDomain = None
        self._Resolution = None

    @property
    def ChannelId(self):
        return self._ChannelId

    @ChannelId.setter
    def ChannelId(self, ChannelId):
        self._ChannelId = ChannelId

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def ModuleCodec(self):
        return self._ModuleCodec

    @ModuleCodec.setter
    def ModuleCodec(self, ModuleCodec):
        self._ModuleCodec = ModuleCodec

    @property
    def Bitrate(self):
        return self._Bitrate

    @Bitrate.setter
    def Bitrate(self, Bitrate):
        self._Bitrate = Bitrate

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PushDomain(self):
        return self._PushDomain

    @PushDomain.setter
    def PushDomain(self, PushDomain):
        self._PushDomain = PushDomain

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution


    def _deserialize(self, params):
        self._ChannelId = params.get("ChannelId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Duration = params.get("Duration")
        self._ModuleCodec = params.get("ModuleCodec")
        self._Bitrate = params.get("Bitrate")
        self._Type = params.get("Type")
        self._PushDomain = params.get("PushDomain")
        self._Resolution = params.get("Resolution")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWatermarkInfo(AbstractModel):
    """Watermark information

    """

    def __init__(self):
        r"""
        :param _Id: Watermark ID
        :type Id: str
        :param _Name: Watermark name
        :type Name: str
        :param _Type: Watermark type. Valid values: STATIC_IMAGE, TEXT.
        :type Type: str
        :param _ImageSettings: Watermark image settings. This parameter is valid if `Type` is `STATIC_IMAGE`.
Note: This field may return `null`, indicating that no valid value was found.
        :type ImageSettings: :class:`tencentcloud.mdl.v20200326.models.DescribeImageSettings`
        :param _TextSettings: Watermark text settings. This parameter is valid if `Type` is `TEXT`.
Note: This field may return `null`, indicating that no valid value was found.
        :type TextSettings: :class:`tencentcloud.mdl.v20200326.models.DescribeTextSettings`
        :param _UpdateTime: Last modified time (UTC+0) of the watermark, in the format of `2020-01-01T12:00:00Z`
Note: This field may return `null`, indicating that no valid value was found.
        :type UpdateTime: str
        :param _AttachedChannels: List of channel IDs the watermark is bound to
Note: This field may return `null`, indicating that no valid value was found.
        :type AttachedChannels: list of str
        """
        self._Id = None
        self._Name = None
        self._Type = None
        self._ImageSettings = None
        self._TextSettings = None
        self._UpdateTime = None
        self._AttachedChannels = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ImageSettings(self):
        return self._ImageSettings

    @ImageSettings.setter
    def ImageSettings(self, ImageSettings):
        self._ImageSettings = ImageSettings

    @property
    def TextSettings(self):
        return self._TextSettings

    @TextSettings.setter
    def TextSettings(self, TextSettings):
        self._TextSettings = TextSettings

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def AttachedChannels(self):
        return self._AttachedChannels

    @AttachedChannels.setter
    def AttachedChannels(self, AttachedChannels):
        self._AttachedChannels = AttachedChannels


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("ImageSettings") is not None:
            self._ImageSettings = DescribeImageSettings()
            self._ImageSettings._deserialize(params.get("ImageSettings"))
        if params.get("TextSettings") is not None:
            self._TextSettings = DescribeTextSettings()
            self._TextSettings._deserialize(params.get("TextSettings"))
        self._UpdateTime = params.get("UpdateTime")
        self._AttachedChannels = params.get("AttachedChannels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestinationInfo(AbstractModel):
    """Relay destination address.

    """

    def __init__(self):
        r"""
        :param _OutputUrl: Relay destination address. Length limit: [1,512].
        :type OutputUrl: str
        :param _AuthKey: Authentication key. Length limit: [1,128].
Note: this field may return null, indicating that no valid values can be obtained.
        :type AuthKey: str
        :param _Username: Authentication username. Length limit: [1,128].
Note: this field may return null, indicating that no valid values can be obtained.
        :type Username: str
        :param _Password: Authentication password. Length limit: [1,128].
Note: this field may return null, indicating that no valid values can be obtained.
        :type Password: str
        :param _DestinationType: The destination type of the retweet. Currently available values are: Standard, AWS_MediaPackageV1, AWS_MediaPackageV2. The default is: Standard. When the output group type is FRAME_CAPTURE, valid values are: AWS_AmazonS3, COS.
        :type DestinationType: str
        :param _AmazonS3Settings: Aws S3 destination setting.
        :type AmazonS3Settings: :class:`tencentcloud.mdl.v20200326.models.AmazonS3Settings`
        :param _CosSettings: Cos destination setting.
        :type CosSettings: :class:`tencentcloud.mdl.v20200326.models.CosSettings`
        """
        self._OutputUrl = None
        self._AuthKey = None
        self._Username = None
        self._Password = None
        self._DestinationType = None
        self._AmazonS3Settings = None
        self._CosSettings = None

    @property
    def OutputUrl(self):
        return self._OutputUrl

    @OutputUrl.setter
    def OutputUrl(self, OutputUrl):
        self._OutputUrl = OutputUrl

    @property
    def AuthKey(self):
        return self._AuthKey

    @AuthKey.setter
    def AuthKey(self, AuthKey):
        self._AuthKey = AuthKey

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def DestinationType(self):
        return self._DestinationType

    @DestinationType.setter
    def DestinationType(self, DestinationType):
        self._DestinationType = DestinationType

    @property
    def AmazonS3Settings(self):
        return self._AmazonS3Settings

    @AmazonS3Settings.setter
    def AmazonS3Settings(self, AmazonS3Settings):
        self._AmazonS3Settings = AmazonS3Settings

    @property
    def CosSettings(self):
        return self._CosSettings

    @CosSettings.setter
    def CosSettings(self, CosSettings):
        self._CosSettings = CosSettings


    def _deserialize(self, params):
        self._OutputUrl = params.get("OutputUrl")
        self._AuthKey = params.get("AuthKey")
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        self._DestinationType = params.get("DestinationType")
        if params.get("AmazonS3Settings") is not None:
            self._AmazonS3Settings = AmazonS3Settings()
            self._AmazonS3Settings._deserialize(params.get("AmazonS3Settings"))
        if params.get("CosSettings") is not None:
            self._CosSettings = CosSettings()
            self._CosSettings._deserialize(params.get("CosSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrmKey(AbstractModel):
    """Custom DRM key.

    """

    def __init__(self):
        r"""
        :param _Key: DRM key, which is a 32-bit hexadecimal string.
Note: uppercase letters in the string will be automatically converted to lowercase ones.
        :type Key: str
        :param _Track: Required for Widevine encryption. Valid values: SD, HD, UHD1, UHD2, AUDIO, ALL.
ALL refers to all tracks. If this parameter is set to ALL, no other tracks can be added.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Track: str
        :param _KeyId: Required for Widevine encryption. It is a 32-bit hexadecimal string.
Note: uppercase letters in the string will be automatically converted to lowercase ones.
Note: this field may return null, indicating that no valid values can be obtained.
        :type KeyId: str
        :param _Iv: Required when FairPlay uses the AES encryption method. It is a 32-bit hexadecimal string.
For more information about this parameter, please see: 
https://tools.ietf.org/html/rfc3826
Note: uppercase letters in the string will be automatically converted to lowercase ones.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Iv: str
        :param _KeyUri: The URI of the license server when AES-128 is used. This parameter may be empty.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type KeyUri: str
        """
        self._Key = None
        self._Track = None
        self._KeyId = None
        self._Iv = None
        self._KeyUri = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Track(self):
        return self._Track

    @Track.setter
    def Track(self, Track):
        self._Track = Track

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Iv(self):
        return self._Iv

    @Iv.setter
    def Iv(self, Iv):
        self._Iv = Iv

    @property
    def KeyUri(self):
        return self._KeyUri

    @KeyUri.setter
    def KeyUri(self, KeyUri):
        self._KeyUri = KeyUri


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Track = params.get("Track")
        self._KeyId = params.get("KeyId")
        self._Iv = params.get("Iv")
        self._KeyUri = params.get("KeyUri")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DrmSettingsInfo(AbstractModel):
    """DRM configuration information, which takes effect only for HLS and DASH.

    """

    def __init__(self):
        r"""
        :param _State: Whether to enable DRM encryption. Valid values: `CLOSE` (disable), `OPEN` (enable). Default value: `CLOSE`
DRM encryption is supported only for HLS, DASH, HLS_ARCHIVE, DASH_ARCHIVE, HLS_MEDIAPACKAGE, and DASH_MEDIAPACKAGE outputs.
        :type State: str
        :param _Scheme: Valid values: `CustomDRMKeys` (default value), `SDMCDRM`
`CustomDRMKeys` means encryption keys customized by users.
`SDMCDRM` means the DRM key management system of SDMC.
        :type Scheme: str
        :param _ContentId: If `Scheme` is set to `CustomDRMKeys`, this parameter is required.
If `Scheme` is set to `SDMCDRM`, this parameter is optional. It supports digits, letters, hyphens, and underscores and must contain 1 to 36 characters. If it is not specified, the value of `ChannelId` will be used.
        :type ContentId: str
        :param _Keys: The key customized by the content user, which is required when `Scheme` is set to CustomDRMKeys.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Keys: list of DrmKey
        :param _SDMCSettings: SDMC key configuration. This parameter is used when `Scheme` is set to `SDMCDRM`.
Note: This field may return `null`, indicating that no valid value was found.
        :type SDMCSettings: :class:`tencentcloud.mdl.v20200326.models.SDMCSettingsInfo`
        :param _DrmType: The DRM type. Valid values: `FAIRPLAY`, `WIDEVINE`, `AES128`, `PLAYREADY`. For HLS, this can be `FAIRPLAY` or `AES128` or `PLAYREADY`. For DASH, valid values: `WIDEVINE` or `PLAYREADY`. 
        :type DrmType: str
        """
        self._State = None
        self._Scheme = None
        self._ContentId = None
        self._Keys = None
        self._SDMCSettings = None
        self._DrmType = None

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Scheme(self):
        return self._Scheme

    @Scheme.setter
    def Scheme(self, Scheme):
        self._Scheme = Scheme

    @property
    def ContentId(self):
        return self._ContentId

    @ContentId.setter
    def ContentId(self, ContentId):
        self._ContentId = ContentId

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def SDMCSettings(self):
        return self._SDMCSettings

    @SDMCSettings.setter
    def SDMCSettings(self, SDMCSettings):
        self._SDMCSettings = SDMCSettings

    @property
    def DrmType(self):
        return self._DrmType

    @DrmType.setter
    def DrmType(self, DrmType):
        self._DrmType = DrmType


    def _deserialize(self, params):
        self._State = params.get("State")
        self._Scheme = params.get("Scheme")
        self._ContentId = params.get("ContentId")
        if params.get("Keys") is not None:
            self._Keys = []
            for item in params.get("Keys"):
                obj = DrmKey()
                obj._deserialize(item)
                self._Keys.append(obj)
        if params.get("SDMCSettings") is not None:
            self._SDMCSettings = SDMCSettingsInfo()
            self._SDMCSettings._deserialize(params.get("SDMCSettings"))
        self._DrmType = params.get("DrmType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventNotifySetting(AbstractModel):
    """The callback settings.

    """

    def __init__(self):
        r"""
        :param _PushEventSettings: The callback configuration for push events.
        :type PushEventSettings: :class:`tencentcloud.mdl.v20200326.models.PushEventSetting`
        """
        self._PushEventSettings = None

    @property
    def PushEventSettings(self):
        return self._PushEventSettings

    @PushEventSettings.setter
    def PushEventSettings(self, PushEventSettings):
        self._PushEventSettings = PushEventSettings


    def _deserialize(self, params):
        if params.get("PushEventSettings") is not None:
            self._PushEventSettings = PushEventSetting()
            self._PushEventSettings._deserialize(params.get("PushEventSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventSettingsDestinationReq(AbstractModel):
    """Destination address information in event settings

    """

    def __init__(self):
        r"""
        :param _Url: URL of the COS bucket to save recording files
        :type Url: str
        """
        self._Url = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventSettingsDestinationResp(AbstractModel):
    """Destination address information in event settings

    """

    def __init__(self):
        r"""
        :param _Url: URL of the COS bucket where recording files are saved
        :type Url: str
        """
        self._Url = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventSettingsReq(AbstractModel):
    """Configuration information of an event in the plan

    """

    def __init__(self):
        r"""
        :param _EventType: Valid values: `INPUT_SWITCH`, `TIMED_RECORD`, SCTE35_TIME_SIGNAL, SCTE35_SPLICE_INSERT, SCTE35_RETURN_TO_NETWORK. If it is not specified, `INPUT_SWITCH` will be used.
        :type EventType: str
        :param _InputAttachment: ID of the input to attach, which is required if `EventType` is `INPUT_SWITCH`
        :type InputAttachment: str
        :param _OutputGroupName: Name of the output group to attach. This parameter is required if `EventType` is `TIMED_RECORD`.
        :type OutputGroupName: str
        :param _ManifestName: Name of the manifest file for timed recording, which must end with `.m3u8` for HLS and `.mpd` for DASH. This parameter is required if `EventType` is `TIMED_RECORD`.
        :type ManifestName: str
        :param _Destinations: URL of the COS bucket to save recording files. This parameter is required if `EventType` is `TIMED_RECORD`. It may contain 1 or 2 URLs. The first URL corresponds to pipeline 0 and the second pipeline 1.
        :type Destinations: list of EventSettingsDestinationReq
        :param _SCTE35SegmentationDescriptor: SCTE-35 configuration information.
        :type SCTE35SegmentationDescriptor: list of SegmentationDescriptorInfo
        :param _SpliceEventID: A 32-bit unique segmentation event identifier.Only one occurrence of a given segmentation_event_id value shall be active at any one time.
        :type SpliceEventID: int
        :param _SpliceDuration: The duration of the segment in 90kHz ticks.It used to  give the splicer an indication of when the break will be over and when the network In Point will occur. If not specifyed,the splice_insert will continue when enter a return_to_network to end the splice_insert at the appropriate time.
        :type SpliceDuration: int
        :param _TimedMetadataSetting: Meta information plan configuration.
        :type TimedMetadataSetting: :class:`tencentcloud.mdl.v20200326.models.TimedMetadataInfo`
        """
        self._EventType = None
        self._InputAttachment = None
        self._OutputGroupName = None
        self._ManifestName = None
        self._Destinations = None
        self._SCTE35SegmentationDescriptor = None
        self._SpliceEventID = None
        self._SpliceDuration = None
        self._TimedMetadataSetting = None

    @property
    def EventType(self):
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def InputAttachment(self):
        return self._InputAttachment

    @InputAttachment.setter
    def InputAttachment(self, InputAttachment):
        self._InputAttachment = InputAttachment

    @property
    def OutputGroupName(self):
        return self._OutputGroupName

    @OutputGroupName.setter
    def OutputGroupName(self, OutputGroupName):
        self._OutputGroupName = OutputGroupName

    @property
    def ManifestName(self):
        return self._ManifestName

    @ManifestName.setter
    def ManifestName(self, ManifestName):
        self._ManifestName = ManifestName

    @property
    def Destinations(self):
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def SCTE35SegmentationDescriptor(self):
        return self._SCTE35SegmentationDescriptor

    @SCTE35SegmentationDescriptor.setter
    def SCTE35SegmentationDescriptor(self, SCTE35SegmentationDescriptor):
        self._SCTE35SegmentationDescriptor = SCTE35SegmentationDescriptor

    @property
    def SpliceEventID(self):
        return self._SpliceEventID

    @SpliceEventID.setter
    def SpliceEventID(self, SpliceEventID):
        self._SpliceEventID = SpliceEventID

    @property
    def SpliceDuration(self):
        return self._SpliceDuration

    @SpliceDuration.setter
    def SpliceDuration(self, SpliceDuration):
        self._SpliceDuration = SpliceDuration

    @property
    def TimedMetadataSetting(self):
        return self._TimedMetadataSetting

    @TimedMetadataSetting.setter
    def TimedMetadataSetting(self, TimedMetadataSetting):
        self._TimedMetadataSetting = TimedMetadataSetting


    def _deserialize(self, params):
        self._EventType = params.get("EventType")
        self._InputAttachment = params.get("InputAttachment")
        self._OutputGroupName = params.get("OutputGroupName")
        self._ManifestName = params.get("ManifestName")
        if params.get("Destinations") is not None:
            self._Destinations = []
            for item in params.get("Destinations"):
                obj = EventSettingsDestinationReq()
                obj._deserialize(item)
                self._Destinations.append(obj)
        if params.get("SCTE35SegmentationDescriptor") is not None:
            self._SCTE35SegmentationDescriptor = []
            for item in params.get("SCTE35SegmentationDescriptor"):
                obj = SegmentationDescriptorInfo()
                obj._deserialize(item)
                self._SCTE35SegmentationDescriptor.append(obj)
        self._SpliceEventID = params.get("SpliceEventID")
        self._SpliceDuration = params.get("SpliceDuration")
        if params.get("TimedMetadataSetting") is not None:
            self._TimedMetadataSetting = TimedMetadataInfo()
            self._TimedMetadataSetting._deserialize(params.get("TimedMetadataSetting"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventSettingsResp(AbstractModel):
    """Configuration information of an event in the plan

    """

    def __init__(self):
        r"""
        :param _EventType: Valid values: INPUT_SWITCH, TIMED_RECORD, SCTE35_TIME_SIGNAL, SCTE35_SPLICE_INSERT, SCTE35_RETURN_TO_NETWORK.
        :type EventType: str
        :param _InputAttachment: ID of the input attached, which is not empty if `EventType` is `INPUT_SWITCH`
        :type InputAttachment: str
        :param _OutputGroupName: Name of the output group attached. This parameter is not empty if `EventType` is `TIMED_RECORD`.
        :type OutputGroupName: str
        :param _ManifestName: Name of the manifest file for timed recording, which ends with `.m3u8` for HLS and `.mpd` for DASH. This parameter is not empty if `EventType` is `TIMED_RECORD`.
        :type ManifestName: str
        :param _Destinations: URL of the COS bucket where recording files are saved. This parameter is not empty if `EventType` is `TIMED_RECORD`. It may contain 1 or 2 URLs. The first URL corresponds to pipeline 0 and the second pipeline 1.
        :type Destinations: list of EventSettingsDestinationResp
        :param _SCTE35SegmentationDescriptor: SCTE-35 configuration information.
        :type SCTE35SegmentationDescriptor: list of SegmentationDescriptorRespInfo
        :param _SpliceEventID: A 32-bit unique segmentation event identifier.Only one occurrence of a given segmentation_event_id value shall be active at any one time.
        :type SpliceEventID: int
        :param _SpliceDuration: The duration of the segment in 90kHz ticks.It used to  give the splicer an indication of when the break will be over and when the network In Point will occur. If not specifyed,the splice_insert will continue when enter a return_to_network to end the splice_insert at the appropriate time.
        :type SpliceDuration: str
        :param _TimedMetadataSetting: Meta information plan configuration.
        :type TimedMetadataSetting: :class:`tencentcloud.mdl.v20200326.models.TimedMetadataInfo`
        """
        self._EventType = None
        self._InputAttachment = None
        self._OutputGroupName = None
        self._ManifestName = None
        self._Destinations = None
        self._SCTE35SegmentationDescriptor = None
        self._SpliceEventID = None
        self._SpliceDuration = None
        self._TimedMetadataSetting = None

    @property
    def EventType(self):
        return self._EventType

    @EventType.setter
    def EventType(self, EventType):
        self._EventType = EventType

    @property
    def InputAttachment(self):
        return self._InputAttachment

    @InputAttachment.setter
    def InputAttachment(self, InputAttachment):
        self._InputAttachment = InputAttachment

    @property
    def OutputGroupName(self):
        return self._OutputGroupName

    @OutputGroupName.setter
    def OutputGroupName(self, OutputGroupName):
        self._OutputGroupName = OutputGroupName

    @property
    def ManifestName(self):
        return self._ManifestName

    @ManifestName.setter
    def ManifestName(self, ManifestName):
        self._ManifestName = ManifestName

    @property
    def Destinations(self):
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def SCTE35SegmentationDescriptor(self):
        return self._SCTE35SegmentationDescriptor

    @SCTE35SegmentationDescriptor.setter
    def SCTE35SegmentationDescriptor(self, SCTE35SegmentationDescriptor):
        self._SCTE35SegmentationDescriptor = SCTE35SegmentationDescriptor

    @property
    def SpliceEventID(self):
        return self._SpliceEventID

    @SpliceEventID.setter
    def SpliceEventID(self, SpliceEventID):
        self._SpliceEventID = SpliceEventID

    @property
    def SpliceDuration(self):
        return self._SpliceDuration

    @SpliceDuration.setter
    def SpliceDuration(self, SpliceDuration):
        self._SpliceDuration = SpliceDuration

    @property
    def TimedMetadataSetting(self):
        return self._TimedMetadataSetting

    @TimedMetadataSetting.setter
    def TimedMetadataSetting(self, TimedMetadataSetting):
        self._TimedMetadataSetting = TimedMetadataSetting


    def _deserialize(self, params):
        self._EventType = params.get("EventType")
        self._InputAttachment = params.get("InputAttachment")
        self._OutputGroupName = params.get("OutputGroupName")
        self._ManifestName = params.get("ManifestName")
        if params.get("Destinations") is not None:
            self._Destinations = []
            for item in params.get("Destinations"):
                obj = EventSettingsDestinationResp()
                obj._deserialize(item)
                self._Destinations.append(obj)
        if params.get("SCTE35SegmentationDescriptor") is not None:
            self._SCTE35SegmentationDescriptor = []
            for item in params.get("SCTE35SegmentationDescriptor"):
                obj = SegmentationDescriptorRespInfo()
                obj._deserialize(item)
                self._SCTE35SegmentationDescriptor.append(obj)
        self._SpliceEventID = params.get("SpliceEventID")
        self._SpliceDuration = params.get("SpliceDuration")
        if params.get("TimedMetadataSetting") is not None:
            self._TimedMetadataSetting = TimedMetadataInfo()
            self._TimedMetadataSetting._deserialize(params.get("TimedMetadataSetting"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FailOverSettings(AbstractModel):
    """Input failover settings

    """

    def __init__(self):
        r"""
        :param _SecondaryInputId: ID of the backup input
Note: this field may return `null`, indicating that no valid value was found.
        :type SecondaryInputId: str
        :param _LossThreshold: The wait time (ms) for triggering failover after the primary input becomes unavailable. Value range: [1000, 86400000]. Default value: `3000`
        :type LossThreshold: int
        :param _RecoverBehavior: Failover policy. Valid values: `CURRENT_PREFERRED` (default), `PRIMARY_PREFERRED`
        :type RecoverBehavior: str
        """
        self._SecondaryInputId = None
        self._LossThreshold = None
        self._RecoverBehavior = None

    @property
    def SecondaryInputId(self):
        return self._SecondaryInputId

    @SecondaryInputId.setter
    def SecondaryInputId(self, SecondaryInputId):
        self._SecondaryInputId = SecondaryInputId

    @property
    def LossThreshold(self):
        return self._LossThreshold

    @LossThreshold.setter
    def LossThreshold(self, LossThreshold):
        self._LossThreshold = LossThreshold

    @property
    def RecoverBehavior(self):
        return self._RecoverBehavior

    @RecoverBehavior.setter
    def RecoverBehavior(self, RecoverBehavior):
        self._RecoverBehavior = RecoverBehavior


    def _deserialize(self, params):
        self._SecondaryInputId = params.get("SecondaryInputId")
        self._LossThreshold = params.get("LossThreshold")
        self._RecoverBehavior = params.get("RecoverBehavior")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FrameCaptureTemplate(AbstractModel):
    """Frame capture template.

    """

    def __init__(self):
        r"""
        :param _Name: Name of frame capture template, limited to uppercase and lowercase letters and numbers, with a length between 1 and 20 characters.
        :type Name: str
        :param _Width: Width of frame capture, optional, input range is from 0 to 3000, must be a multiple of 2.
        :type Width: int
        :param _Height: Height of frame capture, optional, input range is from 0 to 3000, must be a multiple of 2.
        :type Height: int
        :param _CaptureInterval: Interval of frame capture, an integer between 1 and 3600.
        :type CaptureInterval: int
        :param _CaptureIntervalUnits: Interval units of frame capture, only supports SECONDS.
        :type CaptureIntervalUnits: str
        :param _ScalingBehavior: Scaling behavior of frame capture, supports DEFAULT or STRETCH_TO_OUTPUT, with DEFAULT being the default option.
        :type ScalingBehavior: str
        :param _Sharpness: Sharpness, an integer between 0 and 100.
        :type Sharpness: int
        """
        self._Name = None
        self._Width = None
        self._Height = None
        self._CaptureInterval = None
        self._CaptureIntervalUnits = None
        self._ScalingBehavior = None
        self._Sharpness = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def CaptureInterval(self):
        return self._CaptureInterval

    @CaptureInterval.setter
    def CaptureInterval(self, CaptureInterval):
        self._CaptureInterval = CaptureInterval

    @property
    def CaptureIntervalUnits(self):
        return self._CaptureIntervalUnits

    @CaptureIntervalUnits.setter
    def CaptureIntervalUnits(self, CaptureIntervalUnits):
        self._CaptureIntervalUnits = CaptureIntervalUnits

    @property
    def ScalingBehavior(self):
        return self._ScalingBehavior

    @ScalingBehavior.setter
    def ScalingBehavior(self, ScalingBehavior):
        self._ScalingBehavior = ScalingBehavior

    @property
    def Sharpness(self):
        return self._Sharpness

    @Sharpness.setter
    def Sharpness(self, Sharpness):
        self._Sharpness = Sharpness


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._CaptureInterval = params.get("CaptureInterval")
        self._CaptureIntervalUnits = params.get("CaptureIntervalUnits")
        self._ScalingBehavior = params.get("ScalingBehavior")
        self._Sharpness = params.get("Sharpness")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HighlightInfo(AbstractModel):
    """Collection configuration.

    """

    def __init__(self):
        r"""
        :param _HighlightEnabled: Whether to enable input recognition 0: Disable 1 Enable Default value 0 Disable.
        :type HighlightEnabled: int
        :param _Type: The product where the results are saved, optional: COS. Currently, only Tencent Cloud COS is supported. In the future, it will be connected to AWS S3 and COS will be used by default.
        :type Type: str
        :param _Region: Valid when Type is COS, the region where COS is stored.
        :type Region: str
        :param _Bucket: Valid when Type is COS, the bucket name stored in COS.
        :type Bucket: str
        :param _Path: Valid when Type is COS, the path where cos is stored.
        :type Path: str
        :param _Filename: Valid when Type is COS, the file name stored in cos.
        :type Filename: str
        :param _TimestampFormat: Valid when Type is COS, the file name suffix stored in COS is automatically generated in the time format, optional values: unix, utc. Unix is the second-level timestamp and UTC is the year, month and day represented by the zero time zone.
        :type TimestampFormat: str
        :param _AudioSelectorNames: Audio selector list is optional and can be empty. If not filled in, an audio will be used as the output of the recognition result by default.
        :type AudioSelectorNames: list of str
        """
        self._HighlightEnabled = None
        self._Type = None
        self._Region = None
        self._Bucket = None
        self._Path = None
        self._Filename = None
        self._TimestampFormat = None
        self._AudioSelectorNames = None

    @property
    def HighlightEnabled(self):
        return self._HighlightEnabled

    @HighlightEnabled.setter
    def HighlightEnabled(self, HighlightEnabled):
        self._HighlightEnabled = HighlightEnabled

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Filename(self):
        return self._Filename

    @Filename.setter
    def Filename(self, Filename):
        self._Filename = Filename

    @property
    def TimestampFormat(self):
        return self._TimestampFormat

    @TimestampFormat.setter
    def TimestampFormat(self, TimestampFormat):
        self._TimestampFormat = TimestampFormat

    @property
    def AudioSelectorNames(self):
        return self._AudioSelectorNames

    @AudioSelectorNames.setter
    def AudioSelectorNames(self, AudioSelectorNames):
        self._AudioSelectorNames = AudioSelectorNames


    def _deserialize(self, params):
        self._HighlightEnabled = params.get("HighlightEnabled")
        self._Type = params.get("Type")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        self._Path = params.get("Path")
        self._Filename = params.get("Filename")
        self._TimestampFormat = params.get("TimestampFormat")
        self._AudioSelectorNames = params.get("AudioSelectorNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HighlightResInfoResp(AbstractModel):
    """Highlight results information.

    """

    def __init__(self):
        r"""
        :param _TaskId: MPS task ID.
        :type TaskId: str
        :param _SegmentUrl: Highlights video link.
        :type SegmentUrl: str
        :param _CovImgUrl: Collection cover link.
        :type CovImgUrl: str
        :param _CreateTime: Generation time, UTC format.
        :type CreateTime: int
        :param _StartTime: Starting pts.
        :type StartTime: float
        :param _EndTime: End pts.
        :type EndTime: float
        :param _Duration: Duration in seconds.
        :type Duration: float
        """
        self._TaskId = None
        self._SegmentUrl = None
        self._CovImgUrl = None
        self._CreateTime = None
        self._StartTime = None
        self._EndTime = None
        self._Duration = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def SegmentUrl(self):
        return self._SegmentUrl

    @SegmentUrl.setter
    def SegmentUrl(self, SegmentUrl):
        self._SegmentUrl = SegmentUrl

    @property
    def CovImgUrl(self):
        return self._CovImgUrl

    @CovImgUrl.setter
    def CovImgUrl(self, CovImgUrl):
        self._CovImgUrl = CovImgUrl

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._SegmentUrl = params.get("SegmentUrl")
        self._CovImgUrl = params.get("CovImgUrl")
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Duration = params.get("Duration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HlsRemuxSettingsInfo(AbstractModel):
    """HLS protocol configuration.

    """

    def __init__(self):
        r"""
        :param _SegmentDuration: Segment duration in ms. Value range: [1000,30000]. Default value: 4000. The value can only be a multiple of 1,000.
        :type SegmentDuration: int
        :param _SegmentNumber: Number of segments. Value range: [1,30]. Default value: 5.
        :type SegmentNumber: int
        :param _PdtInsertion: Whether to enable PDT insertion. Valid values: CLOSE/OPEN. Default value: CLOSE.
        :type PdtInsertion: str
        :param _PdtDuration: PDT duration in seconds. Value range: (0,3000]. Default value: 600.
        :type PdtDuration: int
        :param _Scheme: Audio/Video packaging scheme. Valid values: `SEPARATE`, `MERGE`. Default value is: SEPARATE.
        :type Scheme: str
        :param _SegmentType: The segment type. Valid values: `ts` (default), `fmp4`.
Currently, fMP4 segments do not support DRM or time shifting.
        :type SegmentType: str
        :param _H265PackageType: The HLS package type when the H.265 codec is used. Valid values: `hvc1`, `hev1` (default).
        :type H265PackageType: str
        :param _LowLatency: Whether to enable low latency 0:CLOSE, 1:OPEN, default value: 0.
        :type LowLatency: int
        :param _PartialSegmentDuration: Low latency slice size, unit ms. Value range: integer [200-HlsRemuxSettings.SegmentDuration] Default value: 500ms.
        :type PartialSegmentDuration: int
        :param _PartialSegmentPlaySite: Low latency slice playback position, unit ms. Value range: integer [3*HlsRemuxSettings.PartiSegmentDuration - 3*HlsRemuxSettings.SegmentDuration], Default value: 3*HlsRemuxSettings.PartiSegmentDuration.
        :type PartialSegmentPlaySite: int
        :param _StreamOrder: Hls main m3u8 file sorting rules by bitrate, optional values: 1: video bitrate ascending order; 2: video bitrate descending order. Default value: 1.
        :type StreamOrder: int
        :param _VideoResolution: Whether the Hls main m3u8 file contains resolution information, optional values: 1: INCLUDE includes video resolution; 2: EXCLUDE does not include video resolution. Default value: 1.
        :type VideoResolution: int
        """
        self._SegmentDuration = None
        self._SegmentNumber = None
        self._PdtInsertion = None
        self._PdtDuration = None
        self._Scheme = None
        self._SegmentType = None
        self._H265PackageType = None
        self._LowLatency = None
        self._PartialSegmentDuration = None
        self._PartialSegmentPlaySite = None
        self._StreamOrder = None
        self._VideoResolution = None

    @property
    def SegmentDuration(self):
        return self._SegmentDuration

    @SegmentDuration.setter
    def SegmentDuration(self, SegmentDuration):
        self._SegmentDuration = SegmentDuration

    @property
    def SegmentNumber(self):
        return self._SegmentNumber

    @SegmentNumber.setter
    def SegmentNumber(self, SegmentNumber):
        self._SegmentNumber = SegmentNumber

    @property
    def PdtInsertion(self):
        return self._PdtInsertion

    @PdtInsertion.setter
    def PdtInsertion(self, PdtInsertion):
        self._PdtInsertion = PdtInsertion

    @property
    def PdtDuration(self):
        return self._PdtDuration

    @PdtDuration.setter
    def PdtDuration(self, PdtDuration):
        self._PdtDuration = PdtDuration

    @property
    def Scheme(self):
        return self._Scheme

    @Scheme.setter
    def Scheme(self, Scheme):
        self._Scheme = Scheme

    @property
    def SegmentType(self):
        return self._SegmentType

    @SegmentType.setter
    def SegmentType(self, SegmentType):
        self._SegmentType = SegmentType

    @property
    def H265PackageType(self):
        return self._H265PackageType

    @H265PackageType.setter
    def H265PackageType(self, H265PackageType):
        self._H265PackageType = H265PackageType

    @property
    def LowLatency(self):
        return self._LowLatency

    @LowLatency.setter
    def LowLatency(self, LowLatency):
        self._LowLatency = LowLatency

    @property
    def PartialSegmentDuration(self):
        return self._PartialSegmentDuration

    @PartialSegmentDuration.setter
    def PartialSegmentDuration(self, PartialSegmentDuration):
        self._PartialSegmentDuration = PartialSegmentDuration

    @property
    def PartialSegmentPlaySite(self):
        return self._PartialSegmentPlaySite

    @PartialSegmentPlaySite.setter
    def PartialSegmentPlaySite(self, PartialSegmentPlaySite):
        self._PartialSegmentPlaySite = PartialSegmentPlaySite

    @property
    def StreamOrder(self):
        return self._StreamOrder

    @StreamOrder.setter
    def StreamOrder(self, StreamOrder):
        self._StreamOrder = StreamOrder

    @property
    def VideoResolution(self):
        return self._VideoResolution

    @VideoResolution.setter
    def VideoResolution(self, VideoResolution):
        self._VideoResolution = VideoResolution


    def _deserialize(self, params):
        self._SegmentDuration = params.get("SegmentDuration")
        self._SegmentNumber = params.get("SegmentNumber")
        self._PdtInsertion = params.get("PdtInsertion")
        self._PdtDuration = params.get("PdtDuration")
        self._Scheme = params.get("Scheme")
        self._SegmentType = params.get("SegmentType")
        self._H265PackageType = params.get("H265PackageType")
        self._LowLatency = params.get("LowLatency")
        self._PartialSegmentDuration = params.get("PartialSegmentDuration")
        self._PartialSegmentPlaySite = params.get("PartialSegmentPlaySite")
        self._StreamOrder = params.get("StreamOrder")
        self._VideoResolution = params.get("VideoResolution")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputAnalysisInfo(AbstractModel):
    """Recognition configuration for input content.

    """

    def __init__(self):
        r"""
        :param _HighlightSetting: Highlight configuration.
        :type HighlightSetting: :class:`tencentcloud.mdl.v20200326.models.HighlightInfo`
        """
        self._HighlightSetting = None

    @property
    def HighlightSetting(self):
        return self._HighlightSetting

    @HighlightSetting.setter
    def HighlightSetting(self, HighlightSetting):
        self._HighlightSetting = HighlightSetting


    def _deserialize(self, params):
        if params.get("HighlightSetting") is not None:
            self._HighlightSetting = HighlightInfo()
            self._HighlightSetting._deserialize(params.get("HighlightSetting"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputInfo(AbstractModel):
    """Input information.

    """

    def __init__(self):
        r"""
        :param _Region: Input region.
        :type Region: str
        :param _Id: Input ID.
        :type Id: str
        :param _Name: Input name.
        :type Name: str
        :param _Type: Input type.
        :type Type: str
        :param _SecurityGroupIds: Array of security groups associated with input.
        :type SecurityGroupIds: list of str
        :param _AttachedChannels: Array of channels associated with input.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AttachedChannels: list of str
        :param _InputSettings: Input configuration array.
        :type InputSettings: list of InputSettingInfo
        """
        self._Region = None
        self._Id = None
        self._Name = None
        self._Type = None
        self._SecurityGroupIds = None
        self._AttachedChannels = None
        self._InputSettings = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def AttachedChannels(self):
        return self._AttachedChannels

    @AttachedChannels.setter
    def AttachedChannels(self, AttachedChannels):
        self._AttachedChannels = AttachedChannels

    @property
    def InputSettings(self):
        return self._InputSettings

    @InputSettings.setter
    def InputSettings(self, InputSettings):
        self._InputSettings = InputSettings


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._AttachedChannels = params.get("AttachedChannels")
        if params.get("InputSettings") is not None:
            self._InputSettings = []
            for item in params.get("InputSettings"):
                obj = InputSettingInfo()
                obj._deserialize(item)
                self._InputSettings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputLossBehaviorInfo(AbstractModel):
    """Complement the last video frame related settings.

    """

    def __init__(self):
        r"""
        :param _RepeatLastFrameMs: The time to fill in the last video frame, unit ms, range 0-1000000, 1000000 means always inserting, default 0 means filling in black screen frame.
        :type RepeatLastFrameMs: int
        :param _InputLossImageType: Fill frame type, COLOR means solid color filling, IMAGE means picture filling, the default is COLOR.
        :type InputLossImageType: str
        :param _ColorRGB: When the type is COLOR, the corresponding rgb value
        :type ColorRGB: str
        :param _ImageUrl: When the type is IMAGE, the corresponding image url value
        :type ImageUrl: str
        """
        self._RepeatLastFrameMs = None
        self._InputLossImageType = None
        self._ColorRGB = None
        self._ImageUrl = None

    @property
    def RepeatLastFrameMs(self):
        return self._RepeatLastFrameMs

    @RepeatLastFrameMs.setter
    def RepeatLastFrameMs(self, RepeatLastFrameMs):
        self._RepeatLastFrameMs = RepeatLastFrameMs

    @property
    def InputLossImageType(self):
        return self._InputLossImageType

    @InputLossImageType.setter
    def InputLossImageType(self, InputLossImageType):
        self._InputLossImageType = InputLossImageType

    @property
    def ColorRGB(self):
        return self._ColorRGB

    @ColorRGB.setter
    def ColorRGB(self, ColorRGB):
        self._ColorRGB = ColorRGB

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._RepeatLastFrameMs = params.get("RepeatLastFrameMs")
        self._InputLossImageType = params.get("InputLossImageType")
        self._ColorRGB = params.get("ColorRGB")
        self._ImageUrl = params.get("ImageUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputSecurityGroupInfo(AbstractModel):
    """Input security group information.

    """

    def __init__(self):
        r"""
        :param _Id: Input security group ID.
        :type Id: str
        :param _Name: Input security group name.
        :type Name: str
        :param _Whitelist: List of allowlist entries.
        :type Whitelist: list of str
        :param _OccupiedInputs: List of bound input streams.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OccupiedInputs: list of str
        :param _Region: Input security group address.
        :type Region: str
        """
        self._Id = None
        self._Name = None
        self._Whitelist = None
        self._OccupiedInputs = None
        self._Region = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Whitelist(self):
        return self._Whitelist

    @Whitelist.setter
    def Whitelist(self, Whitelist):
        self._Whitelist = Whitelist

    @property
    def OccupiedInputs(self):
        return self._OccupiedInputs

    @OccupiedInputs.setter
    def OccupiedInputs(self, OccupiedInputs):
        self._OccupiedInputs = OccupiedInputs

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Whitelist = params.get("Whitelist")
        self._OccupiedInputs = params.get("OccupiedInputs")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputSettingInfo(AbstractModel):
    """The input settings.
    The format of an RTMP_PUSH address is ${InputAddress}/${AppName}/${StreamName}.
    The format of an SRT_PUSH address is ${InputAddress}?streamid=${StreamName},h=${InputDomain}.

    """

    def __init__(self):
        r"""
        :param _AppName: Application name, which is valid if `Type` is `RTMP_PUSH` and can contain 1-32 letters and digits
Note: This field may return `null`, indicating that no valid value was found.
        :type AppName: str
        :param _StreamName: Stream name, which is valid if `Type` is `RTMP_PUSH` and can contain 1-32 letters and digits
Note: This field may return `null`, indicating that no valid value was found.
        :type StreamName: str
        :param _SourceUrl: Source URL, which is valid if `Type` is `RTMP_PULL`, `HLS_PULL`, or `MP4_PULL` and can contain 1-512 characters
Note: This field may return `null`, indicating that no valid value was found.
        :type SourceUrl: str
        :param _InputAddress: RTP/UDP input address, which does not need to be entered for the input parameter.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InputAddress: str
        :param _SourceType: Source type for stream pulling and relaying. To pull content from private-read COS buckets under the current account, set this parameter to `TencentCOS`; otherwise, leave it empty.
Note: this field may return `null`, indicating that no valid value was found.
        :type SourceType: str
        :param _DelayTime: Delayed time (ms) for playback, which is valid if `Type` is `RTMP_PUSH`
Value range: 0 (default) or 10000-600000
The value must be a multiple of 1,000.
Note: This field may return `null`, indicating that no valid value was found.
        :type DelayTime: int
        :param _InputDomain: The domain of an SRT_PUSH address. If this is a request parameter, you don’t need to specify it.
Note: This field may return `null`, indicating that no valid value was found.
        :type InputDomain: str
        :param _UserName: The username, which is used for authentication.
Note: This field may return `null`, indicating that no valid value was found.
        :type UserName: str
        :param _Password: The password, which is used for authentication.
Note: This field may return `null`, indicating that no valid value was found.
        :type Password: str
        """
        self._AppName = None
        self._StreamName = None
        self._SourceUrl = None
        self._InputAddress = None
        self._SourceType = None
        self._DelayTime = None
        self._InputDomain = None
        self._UserName = None
        self._Password = None

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def SourceUrl(self):
        return self._SourceUrl

    @SourceUrl.setter
    def SourceUrl(self, SourceUrl):
        self._SourceUrl = SourceUrl

    @property
    def InputAddress(self):
        return self._InputAddress

    @InputAddress.setter
    def InputAddress(self, InputAddress):
        self._InputAddress = InputAddress

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def DelayTime(self):
        return self._DelayTime

    @DelayTime.setter
    def DelayTime(self, DelayTime):
        self._DelayTime = DelayTime

    @property
    def InputDomain(self):
        return self._InputDomain

    @InputDomain.setter
    def InputDomain(self, InputDomain):
        self._InputDomain = InputDomain

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        self._SourceUrl = params.get("SourceUrl")
        self._InputAddress = params.get("InputAddress")
        self._SourceType = params.get("SourceType")
        self._DelayTime = params.get("DelayTime")
        self._InputDomain = params.get("InputDomain")
        self._UserName = params.get("UserName")
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputStatistics(AbstractModel):
    """Input statistics.

    """

    def __init__(self):
        r"""
        :param _Pipeline0: Input statistics of pipeline 0.
        :type Pipeline0: list of PipelineInputStatistics
        :param _Pipeline1: Input statistics of pipeline 1.
        :type Pipeline1: list of PipelineInputStatistics
        """
        self._Pipeline0 = None
        self._Pipeline1 = None

    @property
    def Pipeline0(self):
        return self._Pipeline0

    @Pipeline0.setter
    def Pipeline0(self, Pipeline0):
        self._Pipeline0 = Pipeline0

    @property
    def Pipeline1(self):
        return self._Pipeline1

    @Pipeline1.setter
    def Pipeline1(self, Pipeline1):
        self._Pipeline1 = Pipeline1


    def _deserialize(self, params):
        if params.get("Pipeline0") is not None:
            self._Pipeline0 = []
            for item in params.get("Pipeline0"):
                obj = PipelineInputStatistics()
                obj._deserialize(item)
                self._Pipeline0.append(obj)
        if params.get("Pipeline1") is not None:
            self._Pipeline1 = []
            for item in params.get("Pipeline1"):
                obj = PipelineInputStatistics()
                obj._deserialize(item)
                self._Pipeline1.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputStreamInfo(AbstractModel):
    """The input stream information.

    """

    def __init__(self):
        r"""
        :param _InputAddress: The input stream address.
        :type InputAddress: str
        :param _AppName: The input stream path.
        :type AppName: str
        :param _StreamName: The input stream name.
        :type StreamName: str
        :param _Status: The input stream status. `1` indicates the stream is active.
        :type Status: int
        """
        self._InputAddress = None
        self._AppName = None
        self._StreamName = None
        self._Status = None

    @property
    def InputAddress(self):
        return self._InputAddress

    @InputAddress.setter
    def InputAddress(self, InputAddress):
        self._InputAddress = InputAddress

    @property
    def AppName(self):
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def StreamName(self):
        return self._StreamName

    @StreamName.setter
    def StreamName(self, StreamName):
        self._StreamName = StreamName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._InputAddress = params.get("InputAddress")
        self._AppName = params.get("AppName")
        self._StreamName = params.get("StreamName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputTrack(AbstractModel):
    """Audio track configuration.

    """

    def __init__(self):
        r"""
        :param _TrackIndex: Audio track index 1-based index mapping to the specified audio track integer starting from 1.
        :type TrackIndex: int
        """
        self._TrackIndex = None

    @property
    def TrackIndex(self):
        return self._TrackIndex

    @TrackIndex.setter
    def TrackIndex(self, TrackIndex):
        self._TrackIndex = TrackIndex


    def _deserialize(self, params):
        self._TrackIndex = params.get("TrackIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputTracks(AbstractModel):
    """

    """

    def __init__(self):
        r"""
        :param _Tracks: Audio track configuration information.
        :type Tracks: list of InputTrack
        """
        self._Tracks = None

    @property
    def Tracks(self):
        return self._Tracks

    @Tracks.setter
    def Tracks(self, Tracks):
        self._Tracks = Tracks


    def _deserialize(self, params):
        if params.get("Tracks") is not None:
            self._Tracks = []
            for item in params.get("Tracks"):
                obj = InputTrack()
                obj._deserialize(item)
                self._Tracks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogInfo(AbstractModel):
    """Log information.

    """

    def __init__(self):
        r"""
        :param _Type: Log type.
It contains the value of `StreamStart` which refers to the push information.
        :type Type: str
        :param _Time: Time when the log is printed.
        :type Time: str
        :param _Message: Log details.
        :type Message: :class:`tencentcloud.mdl.v20200326.models.LogMessageInfo`
        """
        self._Type = None
        self._Time = None
        self._Message = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Time = params.get("Time")
        if params.get("Message") is not None:
            self._Message = LogMessageInfo()
            self._Message._deserialize(params.get("Message"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogMessageInfo(AbstractModel):
    """Log details.

    """

    def __init__(self):
        r"""
        :param _StreamInfo: Push information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StreamInfo: :class:`tencentcloud.mdl.v20200326.models.StreamInfo`
        """
        self._StreamInfo = None

    @property
    def StreamInfo(self):
        return self._StreamInfo

    @StreamInfo.setter
    def StreamInfo(self, StreamInfo):
        self._StreamInfo = StreamInfo


    def _deserialize(self, params):
        if params.get("StreamInfo") is not None:
            self._StreamInfo = StreamInfo()
            self._StreamInfo._deserialize(params.get("StreamInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLiveChannelRequest(AbstractModel):
    """ModifyStreamLiveChannel request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Channel ID
        :type Id: str
        :param _Name: Channel name, which can contain 1-32 case-sensitive letters, digits, and underscores and must be unique at the region level
        :type Name: str
        :param _AttachedInputs: Inputs to attach. You can attach 1 to 5 inputs.
        :type AttachedInputs: list of AttachedInput
        :param _OutputGroups: Configuration information of the channel's output groups. Quantity: [1, 10]
        :type OutputGroups: list of StreamLiveOutputGroupsInfo
        :param _AudioTemplates: Audio transcoding templates. Quantity: [1, 20]
        :type AudioTemplates: list of AudioTemplateInfo
        :param _VideoTemplates: Video transcoding templates. Quantity: [1, 10]
        :type VideoTemplates: list of VideoTemplateInfo
        :param _AVTemplates: Audio/Video transcoding templates. Quantity: [1, 10]
        :type AVTemplates: list of AVTemplate
        :param _CaptionTemplates: Subtitle template configuration, only AVTemplates are valid.
        :type CaptionTemplates: list of SubtitleConf
        :param _PlanSettings: Event settings
        :type PlanSettings: :class:`tencentcloud.mdl.v20200326.models.PlanSettings`
        :param _EventNotifySettings: The callback settings.
        :type EventNotifySettings: :class:`tencentcloud.mdl.v20200326.models.EventNotifySetting`
        :param _InputLossBehavior: Complement the last video frame settings.
        :type InputLossBehavior: :class:`tencentcloud.mdl.v20200326.models.InputLossBehaviorInfo`
        :param _PipelineInputSettings: Pipeline configuration.
        :type PipelineInputSettings: :class:`tencentcloud.mdl.v20200326.models.PipelineInputSettingsInfo`
        :param _InputAnalysisSettings: Recognition configuration for input content.
        :type InputAnalysisSettings: :class:`tencentcloud.mdl.v20200326.models.InputAnalysisInfo`
        :param _Tags: Console tag list.
        :type Tags: list of Tag
        :param _FrameCaptureTemplates: Frame capture templates.
        :type FrameCaptureTemplates: list of FrameCaptureTemplate
        """
        self._Id = None
        self._Name = None
        self._AttachedInputs = None
        self._OutputGroups = None
        self._AudioTemplates = None
        self._VideoTemplates = None
        self._AVTemplates = None
        self._CaptionTemplates = None
        self._PlanSettings = None
        self._EventNotifySettings = None
        self._InputLossBehavior = None
        self._PipelineInputSettings = None
        self._InputAnalysisSettings = None
        self._Tags = None
        self._FrameCaptureTemplates = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AttachedInputs(self):
        return self._AttachedInputs

    @AttachedInputs.setter
    def AttachedInputs(self, AttachedInputs):
        self._AttachedInputs = AttachedInputs

    @property
    def OutputGroups(self):
        return self._OutputGroups

    @OutputGroups.setter
    def OutputGroups(self, OutputGroups):
        self._OutputGroups = OutputGroups

    @property
    def AudioTemplates(self):
        return self._AudioTemplates

    @AudioTemplates.setter
    def AudioTemplates(self, AudioTemplates):
        self._AudioTemplates = AudioTemplates

    @property
    def VideoTemplates(self):
        return self._VideoTemplates

    @VideoTemplates.setter
    def VideoTemplates(self, VideoTemplates):
        self._VideoTemplates = VideoTemplates

    @property
    def AVTemplates(self):
        return self._AVTemplates

    @AVTemplates.setter
    def AVTemplates(self, AVTemplates):
        self._AVTemplates = AVTemplates

    @property
    def CaptionTemplates(self):
        return self._CaptionTemplates

    @CaptionTemplates.setter
    def CaptionTemplates(self, CaptionTemplates):
        self._CaptionTemplates = CaptionTemplates

    @property
    def PlanSettings(self):
        return self._PlanSettings

    @PlanSettings.setter
    def PlanSettings(self, PlanSettings):
        self._PlanSettings = PlanSettings

    @property
    def EventNotifySettings(self):
        return self._EventNotifySettings

    @EventNotifySettings.setter
    def EventNotifySettings(self, EventNotifySettings):
        self._EventNotifySettings = EventNotifySettings

    @property
    def InputLossBehavior(self):
        return self._InputLossBehavior

    @InputLossBehavior.setter
    def InputLossBehavior(self, InputLossBehavior):
        self._InputLossBehavior = InputLossBehavior

    @property
    def PipelineInputSettings(self):
        return self._PipelineInputSettings

    @PipelineInputSettings.setter
    def PipelineInputSettings(self, PipelineInputSettings):
        self._PipelineInputSettings = PipelineInputSettings

    @property
    def InputAnalysisSettings(self):
        return self._InputAnalysisSettings

    @InputAnalysisSettings.setter
    def InputAnalysisSettings(self, InputAnalysisSettings):
        self._InputAnalysisSettings = InputAnalysisSettings

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def FrameCaptureTemplates(self):
        return self._FrameCaptureTemplates

    @FrameCaptureTemplates.setter
    def FrameCaptureTemplates(self, FrameCaptureTemplates):
        self._FrameCaptureTemplates = FrameCaptureTemplates


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        if params.get("AttachedInputs") is not None:
            self._AttachedInputs = []
            for item in params.get("AttachedInputs"):
                obj = AttachedInput()
                obj._deserialize(item)
                self._AttachedInputs.append(obj)
        if params.get("OutputGroups") is not None:
            self._OutputGroups = []
            for item in params.get("OutputGroups"):
                obj = StreamLiveOutputGroupsInfo()
                obj._deserialize(item)
                self._OutputGroups.append(obj)
        if params.get("AudioTemplates") is not None:
            self._AudioTemplates = []
            for item in params.get("AudioTemplates"):
                obj = AudioTemplateInfo()
                obj._deserialize(item)
                self._AudioTemplates.append(obj)
        if params.get("VideoTemplates") is not None:
            self._VideoTemplates = []
            for item in params.get("VideoTemplates"):
                obj = VideoTemplateInfo()
                obj._deserialize(item)
                self._VideoTemplates.append(obj)
        if params.get("AVTemplates") is not None:
            self._AVTemplates = []
            for item in params.get("AVTemplates"):
                obj = AVTemplate()
                obj._deserialize(item)
                self._AVTemplates.append(obj)
        if params.get("CaptionTemplates") is not None:
            self._CaptionTemplates = []
            for item in params.get("CaptionTemplates"):
                obj = SubtitleConf()
                obj._deserialize(item)
                self._CaptionTemplates.append(obj)
        if params.get("PlanSettings") is not None:
            self._PlanSettings = PlanSettings()
            self._PlanSettings._deserialize(params.get("PlanSettings"))
        if params.get("EventNotifySettings") is not None:
            self._EventNotifySettings = EventNotifySetting()
            self._EventNotifySettings._deserialize(params.get("EventNotifySettings"))
        if params.get("InputLossBehavior") is not None:
            self._InputLossBehavior = InputLossBehaviorInfo()
            self._InputLossBehavior._deserialize(params.get("InputLossBehavior"))
        if params.get("PipelineInputSettings") is not None:
            self._PipelineInputSettings = PipelineInputSettingsInfo()
            self._PipelineInputSettings._deserialize(params.get("PipelineInputSettings"))
        if params.get("InputAnalysisSettings") is not None:
            self._InputAnalysisSettings = InputAnalysisInfo()
            self._InputAnalysisSettings._deserialize(params.get("InputAnalysisSettings"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("FrameCaptureTemplates") is not None:
            self._FrameCaptureTemplates = []
            for item in params.get("FrameCaptureTemplates"):
                obj = FrameCaptureTemplate()
                obj._deserialize(item)
                self._FrameCaptureTemplates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLiveChannelResponse(AbstractModel):
    """ModifyStreamLiveChannel response structure.

    """

    def __init__(self):
        r"""
        :param _TagMsg: Tag prompt information, this information will be attached when the tag operation fails.
        :type TagMsg: str
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TagMsg = None
        self._RequestId = None

    @property
    def TagMsg(self):
        return self._TagMsg

    @TagMsg.setter
    def TagMsg(self, TagMsg):
        self._TagMsg = TagMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TagMsg = params.get("TagMsg")
        self._RequestId = params.get("RequestId")


class ModifyStreamLiveInputRequest(AbstractModel):
    """ModifyStreamLiveInput request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Input ID
        :type Id: str
        :param _Name: Input name, which can contain 1-32 case-sensitive letters, digits, and underscores and must be unique at the region level
        :type Name: str
        :param _SecurityGroupIds: List of the IDs of the security groups to attach
        :type SecurityGroupIds: list of str
        :param _InputSettings: Input settings
For the type `RTMP_PUSH`, `RTMP_PULL`, `HLS_PULL`, or `MP4_PULL`, 1 or 2 inputs of the corresponding type can be configured.
This parameter can be left empty for RTP_PUSH and UDP_PUSH inputs.
Note: If this parameter is not specified or empty, the original input settings will be used.
        :type InputSettings: list of InputSettingInfo
        """
        self._Id = None
        self._Name = None
        self._SecurityGroupIds = None
        self._InputSettings = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def InputSettings(self):
        return self._InputSettings

    @InputSettings.setter
    def InputSettings(self, InputSettings):
        self._InputSettings = InputSettings


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("InputSettings") is not None:
            self._InputSettings = []
            for item in params.get("InputSettings"):
                obj = InputSettingInfo()
                obj._deserialize(item)
                self._InputSettings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLiveInputResponse(AbstractModel):
    """ModifyStreamLiveInput response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyStreamLiveInputSecurityGroupRequest(AbstractModel):
    """ModifyStreamLiveInputSecurityGroup request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Input security group ID
        :type Id: str
        :param _Name: Input security group name, which can contain 1-32 case-sensitive letters, digits, and underscores and must be unique at the region level
        :type Name: str
        :param _Whitelist: Allowlist entries (max: 10)
        :type Whitelist: list of str
        """
        self._Id = None
        self._Name = None
        self._Whitelist = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Whitelist(self):
        return self._Whitelist

    @Whitelist.setter
    def Whitelist(self, Whitelist):
        self._Whitelist = Whitelist


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Whitelist = params.get("Whitelist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLiveInputSecurityGroupResponse(AbstractModel):
    """ModifyStreamLiveInputSecurityGroup response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyStreamLiveWatermarkRequest(AbstractModel):
    """ModifyStreamLiveWatermark request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Watermark ID
        :type Id: str
        :param _Name: Watermark name
        :type Name: str
        :param _ImageSettings: Watermark image settings. This parameter is valid if `Type` is `STATIC_IMAGE`.
        :type ImageSettings: :class:`tencentcloud.mdl.v20200326.models.CreateImageSettings`
        :param _TextSettings: Watermark text settings. This parameter is valid if `Type` is `TEXT`.
        :type TextSettings: :class:`tencentcloud.mdl.v20200326.models.CreateTextSettings`
        """
        self._Id = None
        self._Name = None
        self._ImageSettings = None
        self._TextSettings = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ImageSettings(self):
        return self._ImageSettings

    @ImageSettings.setter
    def ImageSettings(self, ImageSettings):
        self._ImageSettings = ImageSettings

    @property
    def TextSettings(self):
        return self._TextSettings

    @TextSettings.setter
    def TextSettings(self, TextSettings):
        self._TextSettings = TextSettings


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        if params.get("ImageSettings") is not None:
            self._ImageSettings = CreateImageSettings()
            self._ImageSettings._deserialize(params.get("ImageSettings"))
        if params.get("TextSettings") is not None:
            self._TextSettings = CreateTextSettings()
            self._TextSettings._deserialize(params.get("TextSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStreamLiveWatermarkResponse(AbstractModel):
    """ModifyStreamLiveWatermark response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class OutputInfo(AbstractModel):
    """Output information.

    """

    def __init__(self):
        r"""
        :param _Name: Output name.
        :type Name: str
        :param _AudioTemplateNames: Audio transcoding template name array.
Quantity limit: [0,1] for RTMP; [0,20] for others.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AudioTemplateNames: list of str
        :param _VideoTemplateNames: Video transcoding template name array. Quantity limit: [0,1].
Note: this field may return null, indicating that no valid values can be obtained.
        :type VideoTemplateNames: list of str
        :param _Scte35Settings: SCTE-35 information configuration.
        :type Scte35Settings: :class:`tencentcloud.mdl.v20200326.models.Scte35SettingsInfo`
        :param _AVTemplateNames: Audio/Video transcoding template name. If `HlsRemuxSettings.Scheme` is `MERGE`, there is 1 audio/video transcoding template. Otherwise, this parameter is empty.
Note: this field may return `null`, indicating that no valid value was found.
        :type AVTemplateNames: list of str
        :param _CaptionTemplateNames: For the subtitle template used, only the AVTemplateNames is valid.
        :type CaptionTemplateNames: list of str
        :param _TimedMetadataSettings: Meta information controls configuration.
        :type TimedMetadataSettings: :class:`tencentcloud.mdl.v20200326.models.TimedMetadataSettingInfo`
        :param _FrameCaptureTemplateNames: Frame capture template name array. Quantity limit: [0,1].
        :type FrameCaptureTemplateNames: list of str
        """
        self._Name = None
        self._AudioTemplateNames = None
        self._VideoTemplateNames = None
        self._Scte35Settings = None
        self._AVTemplateNames = None
        self._CaptionTemplateNames = None
        self._TimedMetadataSettings = None
        self._FrameCaptureTemplateNames = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AudioTemplateNames(self):
        return self._AudioTemplateNames

    @AudioTemplateNames.setter
    def AudioTemplateNames(self, AudioTemplateNames):
        self._AudioTemplateNames = AudioTemplateNames

    @property
    def VideoTemplateNames(self):
        return self._VideoTemplateNames

    @VideoTemplateNames.setter
    def VideoTemplateNames(self, VideoTemplateNames):
        self._VideoTemplateNames = VideoTemplateNames

    @property
    def Scte35Settings(self):
        return self._Scte35Settings

    @Scte35Settings.setter
    def Scte35Settings(self, Scte35Settings):
        self._Scte35Settings = Scte35Settings

    @property
    def AVTemplateNames(self):
        return self._AVTemplateNames

    @AVTemplateNames.setter
    def AVTemplateNames(self, AVTemplateNames):
        self._AVTemplateNames = AVTemplateNames

    @property
    def CaptionTemplateNames(self):
        return self._CaptionTemplateNames

    @CaptionTemplateNames.setter
    def CaptionTemplateNames(self, CaptionTemplateNames):
        self._CaptionTemplateNames = CaptionTemplateNames

    @property
    def TimedMetadataSettings(self):
        return self._TimedMetadataSettings

    @TimedMetadataSettings.setter
    def TimedMetadataSettings(self, TimedMetadataSettings):
        self._TimedMetadataSettings = TimedMetadataSettings

    @property
    def FrameCaptureTemplateNames(self):
        return self._FrameCaptureTemplateNames

    @FrameCaptureTemplateNames.setter
    def FrameCaptureTemplateNames(self, FrameCaptureTemplateNames):
        self._FrameCaptureTemplateNames = FrameCaptureTemplateNames


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AudioTemplateNames = params.get("AudioTemplateNames")
        self._VideoTemplateNames = params.get("VideoTemplateNames")
        if params.get("Scte35Settings") is not None:
            self._Scte35Settings = Scte35SettingsInfo()
            self._Scte35Settings._deserialize(params.get("Scte35Settings"))
        self._AVTemplateNames = params.get("AVTemplateNames")
        self._CaptionTemplateNames = params.get("CaptionTemplateNames")
        if params.get("TimedMetadataSettings") is not None:
            self._TimedMetadataSettings = TimedMetadataSettingInfo()
            self._TimedMetadataSettings._deserialize(params.get("TimedMetadataSettings"))
        self._FrameCaptureTemplateNames = params.get("FrameCaptureTemplateNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OutputsStatistics(AbstractModel):
    """Channel output statistics.

    """

    def __init__(self):
        r"""
        :param _Pipeline0: Output information of pipeline 0.
        :type Pipeline0: list of PipelineOutputStatistics
        :param _Pipeline1: Output information of pipeline 1.
        :type Pipeline1: list of PipelineOutputStatistics
        """
        self._Pipeline0 = None
        self._Pipeline1 = None

    @property
    def Pipeline0(self):
        return self._Pipeline0

    @Pipeline0.setter
    def Pipeline0(self, Pipeline0):
        self._Pipeline0 = Pipeline0

    @property
    def Pipeline1(self):
        return self._Pipeline1

    @Pipeline1.setter
    def Pipeline1(self, Pipeline1):
        self._Pipeline1 = Pipeline1


    def _deserialize(self, params):
        if params.get("Pipeline0") is not None:
            self._Pipeline0 = []
            for item in params.get("Pipeline0"):
                obj = PipelineOutputStatistics()
                obj._deserialize(item)
                self._Pipeline0.append(obj)
        if params.get("Pipeline1") is not None:
            self._Pipeline1 = []
            for item in params.get("Pipeline1"):
                obj = PipelineOutputStatistics()
                obj._deserialize(item)
                self._Pipeline1.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PipelineInputSettingsInfo(AbstractModel):
    """Pipeline failover information.

    """

    def __init__(self):
        r"""
        :param _FaultBehavior: Pipeline failover configuration, the valid value is: 1.PIPELINE_FAILOVER (channels are mutually failover); 2.PIPELINE_FILLING (channels fill in themselves). Default value: PIPELINE_FILLING. The specific content is specified by FaultBehavior.
        :type FaultBehavior: str
        """
        self._FaultBehavior = None

    @property
    def FaultBehavior(self):
        return self._FaultBehavior

    @FaultBehavior.setter
    def FaultBehavior(self, FaultBehavior):
        self._FaultBehavior = FaultBehavior


    def _deserialize(self, params):
        self._FaultBehavior = params.get("FaultBehavior")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PipelineInputStatistics(AbstractModel):
    """Pipeline input statistics.

    """

    def __init__(self):
        r"""
        :param _Timestamp: Data timestamp in seconds.
        :type Timestamp: int
        :param _NetworkIn: Input bandwidth in bps.
        :type NetworkIn: int
        :param _Video: Video information array.
For `rtp/udp` input, the quantity is the number of `Pid` of the input video.
For other inputs, the quantity is 1.
        :type Video: list of VideoPipelineInputStatistics
        :param _Audio: Audio information array.
For `rtp/udp` input, the quantity is the number of `Pid` of the input audio.
For other inputs, the quantity is 1.
        :type Audio: list of AudioPipelineInputStatistics
        """
        self._Timestamp = None
        self._NetworkIn = None
        self._Video = None
        self._Audio = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def NetworkIn(self):
        return self._NetworkIn

    @NetworkIn.setter
    def NetworkIn(self, NetworkIn):
        self._NetworkIn = NetworkIn

    @property
    def Video(self):
        return self._Video

    @Video.setter
    def Video(self, Video):
        self._Video = Video

    @property
    def Audio(self):
        return self._Audio

    @Audio.setter
    def Audio(self, Audio):
        self._Audio = Audio


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._NetworkIn = params.get("NetworkIn")
        if params.get("Video") is not None:
            self._Video = []
            for item in params.get("Video"):
                obj = VideoPipelineInputStatistics()
                obj._deserialize(item)
                self._Video.append(obj)
        if params.get("Audio") is not None:
            self._Audio = []
            for item in params.get("Audio"):
                obj = AudioPipelineInputStatistics()
                obj._deserialize(item)
                self._Audio.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PipelineLogInfo(AbstractModel):
    """Pipeline log information.

    """

    def __init__(self):
        r"""
        :param _Pipeline0: Log information of pipeline 0.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Pipeline0: list of LogInfo
        :param _Pipeline1: Log information of pipeline 1.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Pipeline1: list of LogInfo
        """
        self._Pipeline0 = None
        self._Pipeline1 = None

    @property
    def Pipeline0(self):
        return self._Pipeline0

    @Pipeline0.setter
    def Pipeline0(self, Pipeline0):
        self._Pipeline0 = Pipeline0

    @property
    def Pipeline1(self):
        return self._Pipeline1

    @Pipeline1.setter
    def Pipeline1(self, Pipeline1):
        self._Pipeline1 = Pipeline1


    def _deserialize(self, params):
        if params.get("Pipeline0") is not None:
            self._Pipeline0 = []
            for item in params.get("Pipeline0"):
                obj = LogInfo()
                obj._deserialize(item)
                self._Pipeline0.append(obj)
        if params.get("Pipeline1") is not None:
            self._Pipeline1 = []
            for item in params.get("Pipeline1"):
                obj = LogInfo()
                obj._deserialize(item)
                self._Pipeline1.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PipelineOutputStatistics(AbstractModel):
    """Channel output statistics.

    """

    def __init__(self):
        r"""
        :param _Timestamp: Timestamp.
In seconds, indicating data time.
        :type Timestamp: int
        :param _NetworkOut: Output bandwidth in bps.
        :type NetworkOut: int
        """
        self._Timestamp = None
        self._NetworkOut = None

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def NetworkOut(self):
        return self._NetworkOut

    @NetworkOut.setter
    def NetworkOut(self, NetworkOut):
        self._NetworkOut = NetworkOut


    def _deserialize(self, params):
        self._Timestamp = params.get("Timestamp")
        self._NetworkOut = params.get("NetworkOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlanReq(AbstractModel):
    """Event configuration information

    """

    def __init__(self):
        r"""
        :param _EventName: Event name
        :type EventName: str
        :param _TimingSettings: Event trigger time settings
        :type TimingSettings: :class:`tencentcloud.mdl.v20200326.models.TimingSettingsReq`
        :param _EventSettings: Event configuration
        :type EventSettings: :class:`tencentcloud.mdl.v20200326.models.EventSettingsReq`
        """
        self._EventName = None
        self._TimingSettings = None
        self._EventSettings = None

    @property
    def EventName(self):
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def TimingSettings(self):
        return self._TimingSettings

    @TimingSettings.setter
    def TimingSettings(self, TimingSettings):
        self._TimingSettings = TimingSettings

    @property
    def EventSettings(self):
        return self._EventSettings

    @EventSettings.setter
    def EventSettings(self, EventSettings):
        self._EventSettings = EventSettings


    def _deserialize(self, params):
        self._EventName = params.get("EventName")
        if params.get("TimingSettings") is not None:
            self._TimingSettings = TimingSettingsReq()
            self._TimingSettings._deserialize(params.get("TimingSettings"))
        if params.get("EventSettings") is not None:
            self._EventSettings = EventSettingsReq()
            self._EventSettings._deserialize(params.get("EventSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlanResp(AbstractModel):
    """Event configuration information

    """

    def __init__(self):
        r"""
        :param _EventName: Event name
        :type EventName: str
        :param _TimingSettings: Event trigger time settings
        :type TimingSettings: :class:`tencentcloud.mdl.v20200326.models.TimingSettingsResp`
        :param _EventSettings: Event configuration
        :type EventSettings: :class:`tencentcloud.mdl.v20200326.models.EventSettingsResp`
        """
        self._EventName = None
        self._TimingSettings = None
        self._EventSettings = None

    @property
    def EventName(self):
        return self._EventName

    @EventName.setter
    def EventName(self, EventName):
        self._EventName = EventName

    @property
    def TimingSettings(self):
        return self._TimingSettings

    @TimingSettings.setter
    def TimingSettings(self, TimingSettings):
        self._TimingSettings = TimingSettings

    @property
    def EventSettings(self):
        return self._EventSettings

    @EventSettings.setter
    def EventSettings(self, EventSettings):
        self._EventSettings = EventSettings


    def _deserialize(self, params):
        self._EventName = params.get("EventName")
        if params.get("TimingSettings") is not None:
            self._TimingSettings = TimingSettingsResp()
            self._TimingSettings._deserialize(params.get("TimingSettings"))
        if params.get("EventSettings") is not None:
            self._EventSettings = EventSettingsResp()
            self._EventSettings._deserialize(params.get("EventSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlanSettings(AbstractModel):
    """Event settings

    """

    def __init__(self):
        r"""
        :param _TimedRecordSettings: Timed recording settings
Note: This field may return `null`, indicating that no valid value was found.
        :type TimedRecordSettings: :class:`tencentcloud.mdl.v20200326.models.TimedRecordSettings`
        """
        self._TimedRecordSettings = None

    @property
    def TimedRecordSettings(self):
        return self._TimedRecordSettings

    @TimedRecordSettings.setter
    def TimedRecordSettings(self, TimedRecordSettings):
        self._TimedRecordSettings = TimedRecordSettings


    def _deserialize(self, params):
        if params.get("TimedRecordSettings") is not None:
            self._TimedRecordSettings = TimedRecordSettings()
            self._TimedRecordSettings._deserialize(params.get("TimedRecordSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushEventSetting(AbstractModel):
    """The callback configuration for push events.

    """

    def __init__(self):
        r"""
        :param _NotifyUrl: The callback URL (required).
        :type NotifyUrl: str
        :param _NotifyKey: The callback key (optional).
        :type NotifyKey: str
        """
        self._NotifyUrl = None
        self._NotifyKey = None

    @property
    def NotifyUrl(self):
        return self._NotifyUrl

    @NotifyUrl.setter
    def NotifyUrl(self, NotifyUrl):
        self._NotifyUrl = NotifyUrl

    @property
    def NotifyKey(self):
        return self._NotifyKey

    @NotifyKey.setter
    def NotifyKey(self, NotifyKey):
        self._NotifyKey = NotifyKey


    def _deserialize(self, params):
        self._NotifyUrl = params.get("NotifyUrl")
        self._NotifyKey = params.get("NotifyKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryDispatchInputInfo(AbstractModel):
    """The stream status of the queried input.

    """

    def __init__(self):
        r"""
        :param _InputID: The input ID.
        :type InputID: str
        :param _InputName: The input name.
        :type InputName: str
        :param _Protocol: The input protocol.
        :type Protocol: str
        :param _InputStreamInfoList: The stream status of the input.
        :type InputStreamInfoList: list of InputStreamInfo
        """
        self._InputID = None
        self._InputName = None
        self._Protocol = None
        self._InputStreamInfoList = None

    @property
    def InputID(self):
        return self._InputID

    @InputID.setter
    def InputID(self, InputID):
        self._InputID = InputID

    @property
    def InputName(self):
        return self._InputName

    @InputName.setter
    def InputName(self, InputName):
        self._InputName = InputName

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def InputStreamInfoList(self):
        return self._InputStreamInfoList

    @InputStreamInfoList.setter
    def InputStreamInfoList(self, InputStreamInfoList):
        self._InputStreamInfoList = InputStreamInfoList


    def _deserialize(self, params):
        self._InputID = params.get("InputID")
        self._InputName = params.get("InputName")
        self._Protocol = params.get("Protocol")
        if params.get("InputStreamInfoList") is not None:
            self._InputStreamInfoList = []
            for item in params.get("InputStreamInfoList"):
                obj = InputStreamInfo()
                obj._deserialize(item)
                self._InputStreamInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryInputStreamStateRequest(AbstractModel):
    """QueryInputStreamState request structure.

    """

    def __init__(self):
        r"""
        :param _Id: The StreamLive input ID.
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryInputStreamStateResponse(AbstractModel):
    """QueryInputStreamState response structure.

    """

    def __init__(self):
        r"""
        :param _Info: The information of the StreamLive input queried.
        :type Info: :class:`tencentcloud.mdl.v20200326.models.QueryDispatchInputInfo`
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Info = None
        self._RequestId = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = QueryDispatchInputInfo()
            self._Info._deserialize(params.get("Info"))
        self._RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """Region information

    """

    def __init__(self):
        r"""
        :param _Name: Region name
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SDMCSettingsInfo(AbstractModel):
    """SDMC DRM configuration information. This parameter is valid only when `Scheme` is set to `SDMCDRM`.

    """

    def __init__(self):
        r"""
        :param _Uid: User ID in the SDMC DRM system
        :type Uid: str
        :param _Tracks: Tracks of the SDMC DRM system. This parameter is valid for DASH output groups.
`1`: audio
`2`: SD
`4`: HD
`8`: UHD1
`16`: UHD2

Default value: `31` (audio + SD + HD + UHD1 + UHD2)
        :type Tracks: int
        :param _SecretId: Key ID in the SDMC DRM system; required
        :type SecretId: str
        :param _SecretKey: Key in the SDMC DRM system; required
        :type SecretKey: str
        :param _Url: Key request URL of the SDMC DRM system, which is `https://uat.multidrm.tv/cpix/2.2/getcontentkey` by default
        :type Url: str
        :param _TokenName: Token name in an SDMC key request URL, which is `token` by default
        :type TokenName: str
        """
        self._Uid = None
        self._Tracks = None
        self._SecretId = None
        self._SecretKey = None
        self._Url = None
        self._TokenName = None

    @property
    def Uid(self):
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        self._Uid = Uid

    @property
    def Tracks(self):
        return self._Tracks

    @Tracks.setter
    def Tracks(self, Tracks):
        self._Tracks = Tracks

    @property
    def SecretId(self):
        return self._SecretId

    @SecretId.setter
    def SecretId(self, SecretId):
        self._SecretId = SecretId

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def TokenName(self):
        return self._TokenName

    @TokenName.setter
    def TokenName(self, TokenName):
        self._TokenName = TokenName


    def _deserialize(self, params):
        self._Uid = params.get("Uid")
        self._Tracks = params.get("Tracks")
        self._SecretId = params.get("SecretId")
        self._SecretKey = params.get("SecretKey")
        self._Url = params.get("Url")
        self._TokenName = params.get("TokenName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Scte35SettingsInfo(AbstractModel):
    """SCTE-35 configuration information.

    """

    def __init__(self):
        r"""
        :param _Behavior: Whether to pass through SCTE-35 information. Valid values: NO_PASSTHROUGH/PASSTHROUGH. Default value: NO_PASSTHROUGH.
        :type Behavior: str
        """
        self._Behavior = None

    @property
    def Behavior(self):
        return self._Behavior

    @Behavior.setter
    def Behavior(self, Behavior):
        self._Behavior = Behavior


    def _deserialize(self, params):
        self._Behavior = params.get("Behavior")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SegmentationDescriptorInfo(AbstractModel):
    """SCTE-35 configuration information.

    """

    def __init__(self):
        r"""
        :param _EventID: A 32-bit unique segmentation event identifier. Only one occurrence of a given segmentation_event_id value shall be active at any one time.
        :type EventID: int
        :param _EventCancelIndicator: Indicates that a previously sent segmentation event, identified by segmentation_event_id, has been cancelled.
        :type EventCancelIndicator: int
        :param _DeliveryRestrictions: Distribution configuration.
        :type DeliveryRestrictions: :class:`tencentcloud.mdl.v20200326.models.DeliveryRestrictionsInfo`
        :param _Duration: The duration of the segment in 90kHz ticks. indicat when the segment will be over and when the next segmentation message will occur.Shall be 0 for end messages.the time signal will continue until insert a cancellation message when not specify the duration.
        :type Duration: int
        :param _UPIDType: Corresponds to SCTE-35 segmentation_upid_type parameter.
        :type UPIDType: int
        :param _UPID: Corresponds to SCTE-35 segmentation_upid. 
        :type UPID: str
        :param _TypeID: Corresponds to SCTE-35 segmentation_type_id.
        :type TypeID: int
        :param _Num: Corresponds to SCTE-35 segment_num。This field provides support for numbering segments within a given collection of segments.
        :type Num: int
        :param _Expected: Corresponds to SCTE-35 segment_expected.This field provides a count of the expected number of individual segments within a collection of segments.
        :type Expected: int
        :param _SubSegmentNum: Corresponds to SCTE-35 sub_segment_num.This field provides identification for a specific sub-segment within a collection of sub-segments.
        :type SubSegmentNum: int
        :param _SubSegmentsExpected: Corresponds to SCTE-35 sub_segments_expected.This field provides a count of the expected number of individual sub-segments within the collection of sub-segments.
        :type SubSegmentsExpected: int
        """
        self._EventID = None
        self._EventCancelIndicator = None
        self._DeliveryRestrictions = None
        self._Duration = None
        self._UPIDType = None
        self._UPID = None
        self._TypeID = None
        self._Num = None
        self._Expected = None
        self._SubSegmentNum = None
        self._SubSegmentsExpected = None

    @property
    def EventID(self):
        return self._EventID

    @EventID.setter
    def EventID(self, EventID):
        self._EventID = EventID

    @property
    def EventCancelIndicator(self):
        return self._EventCancelIndicator

    @EventCancelIndicator.setter
    def EventCancelIndicator(self, EventCancelIndicator):
        self._EventCancelIndicator = EventCancelIndicator

    @property
    def DeliveryRestrictions(self):
        return self._DeliveryRestrictions

    @DeliveryRestrictions.setter
    def DeliveryRestrictions(self, DeliveryRestrictions):
        self._DeliveryRestrictions = DeliveryRestrictions

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def UPIDType(self):
        return self._UPIDType

    @UPIDType.setter
    def UPIDType(self, UPIDType):
        self._UPIDType = UPIDType

    @property
    def UPID(self):
        return self._UPID

    @UPID.setter
    def UPID(self, UPID):
        self._UPID = UPID

    @property
    def TypeID(self):
        return self._TypeID

    @TypeID.setter
    def TypeID(self, TypeID):
        self._TypeID = TypeID

    @property
    def Num(self):
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def Expected(self):
        return self._Expected

    @Expected.setter
    def Expected(self, Expected):
        self._Expected = Expected

    @property
    def SubSegmentNum(self):
        return self._SubSegmentNum

    @SubSegmentNum.setter
    def SubSegmentNum(self, SubSegmentNum):
        self._SubSegmentNum = SubSegmentNum

    @property
    def SubSegmentsExpected(self):
        return self._SubSegmentsExpected

    @SubSegmentsExpected.setter
    def SubSegmentsExpected(self, SubSegmentsExpected):
        self._SubSegmentsExpected = SubSegmentsExpected


    def _deserialize(self, params):
        self._EventID = params.get("EventID")
        self._EventCancelIndicator = params.get("EventCancelIndicator")
        if params.get("DeliveryRestrictions") is not None:
            self._DeliveryRestrictions = DeliveryRestrictionsInfo()
            self._DeliveryRestrictions._deserialize(params.get("DeliveryRestrictions"))
        self._Duration = params.get("Duration")
        self._UPIDType = params.get("UPIDType")
        self._UPID = params.get("UPID")
        self._TypeID = params.get("TypeID")
        self._Num = params.get("Num")
        self._Expected = params.get("Expected")
        self._SubSegmentNum = params.get("SubSegmentNum")
        self._SubSegmentsExpected = params.get("SubSegmentsExpected")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SegmentationDescriptorRespInfo(AbstractModel):
    """SCTE-35 configuration information.

    """

    def __init__(self):
        r"""
        :param _EventID: A 32-bit unique segmentation event identifier. Only one occurrence of a given segmentation_event_id value shall be active at any one time.
        :type EventID: int
        :param _EventCancelIndicator: Indicates that a previously sent segmentation event, identified by segmentation_event_id, has been cancelled.
        :type EventCancelIndicator: int
        :param _DeliveryRestrictions: Distribution configuration.
        :type DeliveryRestrictions: :class:`tencentcloud.mdl.v20200326.models.DeliveryRestrictionsInfo`
        :param _Duration: The duration of the segment in 90kHz ticks. indicat when the segment will be over and when the next segmentation message will occur.Shall be 0 for end messages.the time signal will continue until insert a cancellation message when not specify the duration.
        :type Duration: str
        :param _UPIDType: Corresponds to SCTE-35 segmentation_upid_type parameter.
        :type UPIDType: int
        :param _UPID: Corresponds to SCTE-35 segmentation_upid. 
        :type UPID: str
        :param _TypeID: Corresponds to SCTE-35 segmentation_type_id.
        :type TypeID: int
        :param _Num: Corresponds to SCTE-35 segment_num。This field provides support for numbering segments within a given collection of segments.
        :type Num: int
        :param _Expected: Corresponds to SCTE-35 segment_expected.This field provides a count of the expected number of individual segments within a collection of segments.
        :type Expected: int
        :param _SubSegmentNum: Corresponds to SCTE-35 sub_segment_num.This field provides identification for a specific sub-segment within a collection of sub-segments.
        :type SubSegmentNum: int
        :param _SubSegmentsExpected: Corresponds to SCTE-35 sub_segments_expected.This field provides a count of the expected number of individual sub-segments within the collection of sub-segments.
        :type SubSegmentsExpected: int
        """
        self._EventID = None
        self._EventCancelIndicator = None
        self._DeliveryRestrictions = None
        self._Duration = None
        self._UPIDType = None
        self._UPID = None
        self._TypeID = None
        self._Num = None
        self._Expected = None
        self._SubSegmentNum = None
        self._SubSegmentsExpected = None

    @property
    def EventID(self):
        return self._EventID

    @EventID.setter
    def EventID(self, EventID):
        self._EventID = EventID

    @property
    def EventCancelIndicator(self):
        return self._EventCancelIndicator

    @EventCancelIndicator.setter
    def EventCancelIndicator(self, EventCancelIndicator):
        self._EventCancelIndicator = EventCancelIndicator

    @property
    def DeliveryRestrictions(self):
        return self._DeliveryRestrictions

    @DeliveryRestrictions.setter
    def DeliveryRestrictions(self, DeliveryRestrictions):
        self._DeliveryRestrictions = DeliveryRestrictions

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def UPIDType(self):
        return self._UPIDType

    @UPIDType.setter
    def UPIDType(self, UPIDType):
        self._UPIDType = UPIDType

    @property
    def UPID(self):
        return self._UPID

    @UPID.setter
    def UPID(self, UPID):
        self._UPID = UPID

    @property
    def TypeID(self):
        return self._TypeID

    @TypeID.setter
    def TypeID(self, TypeID):
        self._TypeID = TypeID

    @property
    def Num(self):
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def Expected(self):
        return self._Expected

    @Expected.setter
    def Expected(self, Expected):
        self._Expected = Expected

    @property
    def SubSegmentNum(self):
        return self._SubSegmentNum

    @SubSegmentNum.setter
    def SubSegmentNum(self, SubSegmentNum):
        self._SubSegmentNum = SubSegmentNum

    @property
    def SubSegmentsExpected(self):
        return self._SubSegmentsExpected

    @SubSegmentsExpected.setter
    def SubSegmentsExpected(self, SubSegmentsExpected):
        self._SubSegmentsExpected = SubSegmentsExpected


    def _deserialize(self, params):
        self._EventID = params.get("EventID")
        self._EventCancelIndicator = params.get("EventCancelIndicator")
        if params.get("DeliveryRestrictions") is not None:
            self._DeliveryRestrictions = DeliveryRestrictionsInfo()
            self._DeliveryRestrictions._deserialize(params.get("DeliveryRestrictions"))
        self._Duration = params.get("Duration")
        self._UPIDType = params.get("UPIDType")
        self._UPID = params.get("UPID")
        self._TypeID = params.get("TypeID")
        self._Num = params.get("Num")
        self._Expected = params.get("Expected")
        self._SubSegmentNum = params.get("SubSegmentNum")
        self._SubSegmentsExpected = params.get("SubSegmentsExpected")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartStreamLiveChannelRequest(AbstractModel):
    """StartStreamLiveChannel request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Channel ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartStreamLiveChannelResponse(AbstractModel):
    """StartStreamLiveChannel response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopStreamLiveChannelRequest(AbstractModel):
    """StopStreamLiveChannel request structure.

    """

    def __init__(self):
        r"""
        :param _Id: Channel ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopStreamLiveChannelResponse(AbstractModel):
    """StopStreamLiveChannel response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, generated by the server, will be returned for every request (if the request fails to reach the server for other reasons, the request will not obtain a RequestId). RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StreamAudioInfo(AbstractModel):
    """Audio information.

    """

    def __init__(self):
        r"""
        :param _Pid: Audio `Pid`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Pid: int
        :param _Codec: Audio codec.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Codec: str
        :param _Fps: Audio frame rate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Fps: int
        :param _Rate: Audio bitrate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Rate: int
        :param _SampleRate: Audio sample rate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SampleRate: int
        """
        self._Pid = None
        self._Codec = None
        self._Fps = None
        self._Rate = None
        self._SampleRate = None

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def Codec(self):
        return self._Codec

    @Codec.setter
    def Codec(self, Codec):
        self._Codec = Codec

    @property
    def Fps(self):
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def SampleRate(self):
        return self._SampleRate

    @SampleRate.setter
    def SampleRate(self, SampleRate):
        self._SampleRate = SampleRate


    def _deserialize(self, params):
        self._Pid = params.get("Pid")
        self._Codec = params.get("Codec")
        self._Fps = params.get("Fps")
        self._Rate = params.get("Rate")
        self._SampleRate = params.get("SampleRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamInfo(AbstractModel):
    """Push information.

    """

    def __init__(self):
        r"""
        :param _ClientIp: Client IP.
        :type ClientIp: str
        :param _Video: Video information of pushed streams.
        :type Video: list of StreamVideoInfo
        :param _Audio: Audio information of pushed streams.
        :type Audio: list of StreamAudioInfo
        :param _Scte35: SCTE-35 information of pushed streams.
        :type Scte35: list of StreamScte35Info
        """
        self._ClientIp = None
        self._Video = None
        self._Audio = None
        self._Scte35 = None

    @property
    def ClientIp(self):
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def Video(self):
        return self._Video

    @Video.setter
    def Video(self, Video):
        self._Video = Video

    @property
    def Audio(self):
        return self._Audio

    @Audio.setter
    def Audio(self, Audio):
        self._Audio = Audio

    @property
    def Scte35(self):
        return self._Scte35

    @Scte35.setter
    def Scte35(self, Scte35):
        self._Scte35 = Scte35


    def _deserialize(self, params):
        self._ClientIp = params.get("ClientIp")
        if params.get("Video") is not None:
            self._Video = []
            for item in params.get("Video"):
                obj = StreamVideoInfo()
                obj._deserialize(item)
                self._Video.append(obj)
        if params.get("Audio") is not None:
            self._Audio = []
            for item in params.get("Audio"):
                obj = StreamAudioInfo()
                obj._deserialize(item)
                self._Audio.append(obj)
        if params.get("Scte35") is not None:
            self._Scte35 = []
            for item in params.get("Scte35"):
                obj = StreamScte35Info()
                obj._deserialize(item)
                self._Scte35.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamLiveChannelInfo(AbstractModel):
    """Channel information

    """

    def __init__(self):
        r"""
        :param _Id: Channel ID
        :type Id: str
        :param _State: Channel status
        :type State: str
        :param _AttachedInputs: Information of attached inputs
        :type AttachedInputs: list of AttachedInput
        :param _OutputGroups: Information of output groups
        :type OutputGroups: list of StreamLiveOutputGroupsInfo
        :param _Name: Channel name
        :type Name: str
        :param _AudioTemplates: Audio transcoding templates
Note: this field may return `null`, indicating that no valid value was found.
        :type AudioTemplates: list of AudioTemplateInfo
        :param _VideoTemplates: Video transcoding templates
Note: this field may return `null`, indicating that no valid value was found.
        :type VideoTemplates: list of VideoTemplateInfo
        :param _AVTemplates: Audio/Video transcoding templates
Note: this field may return `null`, indicating that no valid value was found.
        :type AVTemplates: list of AVTemplate
        :param _CaptionTemplates: 
        :type CaptionTemplates: list of SubtitleConf
        :param _PlanSettings: Event settings
Note: This field may return `null`, indicating that no valid value was found.
        :type PlanSettings: :class:`tencentcloud.mdl.v20200326.models.PlanSettings`
        :param _EventNotifySettings: The callback settings.
Note: This field may return `null`, indicating that no valid value was found.
        :type EventNotifySettings: :class:`tencentcloud.mdl.v20200326.models.EventNotifySetting`
        :param _InputLossBehavior: Supplement the last video frame configuration settings.
        :type InputLossBehavior: :class:`tencentcloud.mdl.v20200326.models.InputLossBehaviorInfo`
        :param _PipelineInputSettings: Pipeline configuration.
        :type PipelineInputSettings: :class:`tencentcloud.mdl.v20200326.models.PipelineInputSettingsInfo`
        :param _InputAnalysisSettings: Recognition configuration for input content.
        :type InputAnalysisSettings: :class:`tencentcloud.mdl.v20200326.models.InputAnalysisInfo`
        :param _Tags: Console tag list.
        :type Tags: list of Tag
        :param _FrameCaptureTemplates: Frame capture templates.
        :type FrameCaptureTemplates: list of FrameCaptureTemplate
        """
        self._Id = None
        self._State = None
        self._AttachedInputs = None
        self._OutputGroups = None
        self._Name = None
        self._AudioTemplates = None
        self._VideoTemplates = None
        self._AVTemplates = None
        self._CaptionTemplates = None
        self._PlanSettings = None
        self._EventNotifySettings = None
        self._InputLossBehavior = None
        self._PipelineInputSettings = None
        self._InputAnalysisSettings = None
        self._Tags = None
        self._FrameCaptureTemplates = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def AttachedInputs(self):
        return self._AttachedInputs

    @AttachedInputs.setter
    def AttachedInputs(self, AttachedInputs):
        self._AttachedInputs = AttachedInputs

    @property
    def OutputGroups(self):
        return self._OutputGroups

    @OutputGroups.setter
    def OutputGroups(self, OutputGroups):
        self._OutputGroups = OutputGroups

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AudioTemplates(self):
        return self._AudioTemplates

    @AudioTemplates.setter
    def AudioTemplates(self, AudioTemplates):
        self._AudioTemplates = AudioTemplates

    @property
    def VideoTemplates(self):
        return self._VideoTemplates

    @VideoTemplates.setter
    def VideoTemplates(self, VideoTemplates):
        self._VideoTemplates = VideoTemplates

    @property
    def AVTemplates(self):
        return self._AVTemplates

    @AVTemplates.setter
    def AVTemplates(self, AVTemplates):
        self._AVTemplates = AVTemplates

    @property
    def CaptionTemplates(self):
        return self._CaptionTemplates

    @CaptionTemplates.setter
    def CaptionTemplates(self, CaptionTemplates):
        self._CaptionTemplates = CaptionTemplates

    @property
    def PlanSettings(self):
        return self._PlanSettings

    @PlanSettings.setter
    def PlanSettings(self, PlanSettings):
        self._PlanSettings = PlanSettings

    @property
    def EventNotifySettings(self):
        return self._EventNotifySettings

    @EventNotifySettings.setter
    def EventNotifySettings(self, EventNotifySettings):
        self._EventNotifySettings = EventNotifySettings

    @property
    def InputLossBehavior(self):
        return self._InputLossBehavior

    @InputLossBehavior.setter
    def InputLossBehavior(self, InputLossBehavior):
        self._InputLossBehavior = InputLossBehavior

    @property
    def PipelineInputSettings(self):
        return self._PipelineInputSettings

    @PipelineInputSettings.setter
    def PipelineInputSettings(self, PipelineInputSettings):
        self._PipelineInputSettings = PipelineInputSettings

    @property
    def InputAnalysisSettings(self):
        return self._InputAnalysisSettings

    @InputAnalysisSettings.setter
    def InputAnalysisSettings(self, InputAnalysisSettings):
        self._InputAnalysisSettings = InputAnalysisSettings

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def FrameCaptureTemplates(self):
        return self._FrameCaptureTemplates

    @FrameCaptureTemplates.setter
    def FrameCaptureTemplates(self, FrameCaptureTemplates):
        self._FrameCaptureTemplates = FrameCaptureTemplates


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._State = params.get("State")
        if params.get("AttachedInputs") is not None:
            self._AttachedInputs = []
            for item in params.get("AttachedInputs"):
                obj = AttachedInput()
                obj._deserialize(item)
                self._AttachedInputs.append(obj)
        if params.get("OutputGroups") is not None:
            self._OutputGroups = []
            for item in params.get("OutputGroups"):
                obj = StreamLiveOutputGroupsInfo()
                obj._deserialize(item)
                self._OutputGroups.append(obj)
        self._Name = params.get("Name")
        if params.get("AudioTemplates") is not None:
            self._AudioTemplates = []
            for item in params.get("AudioTemplates"):
                obj = AudioTemplateInfo()
                obj._deserialize(item)
                self._AudioTemplates.append(obj)
        if params.get("VideoTemplates") is not None:
            self._VideoTemplates = []
            for item in params.get("VideoTemplates"):
                obj = VideoTemplateInfo()
                obj._deserialize(item)
                self._VideoTemplates.append(obj)
        if params.get("AVTemplates") is not None:
            self._AVTemplates = []
            for item in params.get("AVTemplates"):
                obj = AVTemplate()
                obj._deserialize(item)
                self._AVTemplates.append(obj)
        if params.get("CaptionTemplates") is not None:
            self._CaptionTemplates = []
            for item in params.get("CaptionTemplates"):
                obj = SubtitleConf()
                obj._deserialize(item)
                self._CaptionTemplates.append(obj)
        if params.get("PlanSettings") is not None:
            self._PlanSettings = PlanSettings()
            self._PlanSettings._deserialize(params.get("PlanSettings"))
        if params.get("EventNotifySettings") is not None:
            self._EventNotifySettings = EventNotifySetting()
            self._EventNotifySettings._deserialize(params.get("EventNotifySettings"))
        if params.get("InputLossBehavior") is not None:
            self._InputLossBehavior = InputLossBehaviorInfo()
            self._InputLossBehavior._deserialize(params.get("InputLossBehavior"))
        if params.get("PipelineInputSettings") is not None:
            self._PipelineInputSettings = PipelineInputSettingsInfo()
            self._PipelineInputSettings._deserialize(params.get("PipelineInputSettings"))
        if params.get("InputAnalysisSettings") is not None:
            self._InputAnalysisSettings = InputAnalysisInfo()
            self._InputAnalysisSettings._deserialize(params.get("InputAnalysisSettings"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("FrameCaptureTemplates") is not None:
            self._FrameCaptureTemplates = []
            for item in params.get("FrameCaptureTemplates"):
                obj = FrameCaptureTemplate()
                obj._deserialize(item)
                self._FrameCaptureTemplates.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamLiveOutputGroupsInfo(AbstractModel):
    """Channel output group information

    """

    def __init__(self):
        r"""
        :param _Name: Output group name, which can contain 1-32 case-sensitive letters, digits, and underscores and must be unique at the channel level
        :type Name: str
        :param _Type: Output protocol
Valid values: `HLS`, `DASH`, `HLS_ARCHIVE`, `HLS_STREAM_PACKAGE`, `DASH_STREAM_PACKAGE`, `FRAME_CAPTURE`
        :type Type: str
        :param _Outputs: Output information
If the type is RTMP or RTP, only one output is allowed; if it is HLS or DASH, 1-10 outputs are allowed.
        :type Outputs: list of OutputInfo
        :param _Destinations: Relay destinations. Quantity: [1, 2]
        :type Destinations: list of DestinationInfo
        :param _HlsRemuxSettings: HLS protocol configuration information, which takes effect only for HLS/HLS_ARCHIVE/HLS_STREAM_PACKAGE outputs.
Note: this field may return `null`, indicating that no valid value was found.
        :type HlsRemuxSettings: :class:`tencentcloud.mdl.v20200326.models.HlsRemuxSettingsInfo`
        :param _DrmSettings: DRM configuration information
Note: this field may return `null`, indicating that no valid value was found.
        :type DrmSettings: :class:`tencentcloud.mdl.v20200326.models.DrmSettingsInfo`
        :param _DashRemuxSettings: DASH protocol configuration information, which takes effect only for DASH/DASH_ARCHIVE outputs
Note: this field may return `null`, indicating that no valid value was found.
        :type DashRemuxSettings: :class:`tencentcloud.mdl.v20200326.models.DashRemuxSettingsInfo`
        :param _StreamPackageSettings: StreamPackage configuration information, which is required if the output type is StreamPackage
Note: this field may return `null`, indicating that no valid value was found.
        :type StreamPackageSettings: :class:`tencentcloud.mdl.v20200326.models.StreamPackageSettingsInfo`
        :param _TimeShiftSettings: Time-shift configuration information
Note: This field may return `null`, indicating that no valid value was found.
        :type TimeShiftSettings: :class:`tencentcloud.mdl.v20200326.models.TimeShiftSettingsInfo`
        """
        self._Name = None
        self._Type = None
        self._Outputs = None
        self._Destinations = None
        self._HlsRemuxSettings = None
        self._DrmSettings = None
        self._DashRemuxSettings = None
        self._StreamPackageSettings = None
        self._TimeShiftSettings = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Outputs(self):
        return self._Outputs

    @Outputs.setter
    def Outputs(self, Outputs):
        self._Outputs = Outputs

    @property
    def Destinations(self):
        return self._Destinations

    @Destinations.setter
    def Destinations(self, Destinations):
        self._Destinations = Destinations

    @property
    def HlsRemuxSettings(self):
        return self._HlsRemuxSettings

    @HlsRemuxSettings.setter
    def HlsRemuxSettings(self, HlsRemuxSettings):
        self._HlsRemuxSettings = HlsRemuxSettings

    @property
    def DrmSettings(self):
        return self._DrmSettings

    @DrmSettings.setter
    def DrmSettings(self, DrmSettings):
        self._DrmSettings = DrmSettings

    @property
    def DashRemuxSettings(self):
        return self._DashRemuxSettings

    @DashRemuxSettings.setter
    def DashRemuxSettings(self, DashRemuxSettings):
        self._DashRemuxSettings = DashRemuxSettings

    @property
    def StreamPackageSettings(self):
        return self._StreamPackageSettings

    @StreamPackageSettings.setter
    def StreamPackageSettings(self, StreamPackageSettings):
        self._StreamPackageSettings = StreamPackageSettings

    @property
    def TimeShiftSettings(self):
        return self._TimeShiftSettings

    @TimeShiftSettings.setter
    def TimeShiftSettings(self, TimeShiftSettings):
        self._TimeShiftSettings = TimeShiftSettings


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("Outputs") is not None:
            self._Outputs = []
            for item in params.get("Outputs"):
                obj = OutputInfo()
                obj._deserialize(item)
                self._Outputs.append(obj)
        if params.get("Destinations") is not None:
            self._Destinations = []
            for item in params.get("Destinations"):
                obj = DestinationInfo()
                obj._deserialize(item)
                self._Destinations.append(obj)
        if params.get("HlsRemuxSettings") is not None:
            self._HlsRemuxSettings = HlsRemuxSettingsInfo()
            self._HlsRemuxSettings._deserialize(params.get("HlsRemuxSettings"))
        if params.get("DrmSettings") is not None:
            self._DrmSettings = DrmSettingsInfo()
            self._DrmSettings._deserialize(params.get("DrmSettings"))
        if params.get("DashRemuxSettings") is not None:
            self._DashRemuxSettings = DashRemuxSettingsInfo()
            self._DashRemuxSettings._deserialize(params.get("DashRemuxSettings"))
        if params.get("StreamPackageSettings") is not None:
            self._StreamPackageSettings = StreamPackageSettingsInfo()
            self._StreamPackageSettings._deserialize(params.get("StreamPackageSettings"))
        if params.get("TimeShiftSettings") is not None:
            self._TimeShiftSettings = TimeShiftSettingsInfo()
            self._TimeShiftSettings._deserialize(params.get("TimeShiftSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamLiveRegionInfo(AbstractModel):
    """StreamLive region information

    """

    def __init__(self):
        r"""
        :param _Regions: List of StreamLive regions
        :type Regions: list of RegionInfo
        """
        self._Regions = None

    @property
    def Regions(self):
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions


    def _deserialize(self, params):
        if params.get("Regions") is not None:
            self._Regions = []
            for item in params.get("Regions"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._Regions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamPackageSettingsInfo(AbstractModel):
    """StreamPackage settings when the output type is StreamPackage

    """

    def __init__(self):
        r"""
        :param _Id: Channel ID in StreamPackage
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamScte35Info(AbstractModel):
    """SCTE-35 information.

    """

    def __init__(self):
        r"""
        :param _Pid: SCTE-35 `Pid`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Pid: int
        """
        self._Pid = None

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid


    def _deserialize(self, params):
        self._Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamVideoInfo(AbstractModel):
    """Video information of pushed streams.

    """

    def __init__(self):
        r"""
        :param _Pid: Video `Pid`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Pid: int
        :param _Codec: Video codec.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Codec: str
        :param _Fps: Video frame rate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Fps: int
        :param _Rate: Video bitrate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Rate: int
        :param _Width: Video width.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Width: int
        :param _Height: Video height.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Height: int
        """
        self._Pid = None
        self._Codec = None
        self._Fps = None
        self._Rate = None
        self._Width = None
        self._Height = None

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid

    @property
    def Codec(self):
        return self._Codec

    @Codec.setter
    def Codec(self, Codec):
        self._Codec = Codec

    @property
    def Fps(self):
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._Pid = params.get("Pid")
        self._Codec = params.get("Codec")
        self._Fps = params.get("Fps")
        self._Rate = params.get("Rate")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubtitleConf(AbstractModel):
    """Subtitle template configuration.

    """

    def __init__(self):
        r"""
        :param _Name: Template name.
        :type Name: str
        :param _CaptionSelectorName: Name of caption selector. Required when CaptionSource selects `INPUT`.
        :type CaptionSelectorName: str
        :param _CaptionSource: Optional values: INPUT (source subtitle information), ANALYSIS (intelligent speech recognition to subtitles).
        :type CaptionSource: str
        :param _ContentType: Optional values: 1 Source, 2 Source+Target, 3 Target (original language only, original language + translation language, translation language). Required when CaptionSource selects `ANALYSIS `.
        :type ContentType: int
        :param _TargetType: Output mode: 1 Burn in, 2 Embedded. Support `2` when CaptionSource selects `INPUT`. Support `1` when CaptionSource selects `ANALYSIS `.
        :type TargetType: int
        :param _SourceLanguage: Original phonetic language.
Optional values: Chinese, English, Japanese, Korean. Required when CaptionSource selects `ANALYSIS `.
        :type SourceLanguage: str
        :param _TargetLanguage: Target language.
Optional values: Chinese, English, Japanese, Korean. Required when CaptionSource selects `ANALYSIS `.
        :type TargetLanguage: str
        :param _FontStyle: Font style configuration. Required when CaptionSource selects `ANALYSIS `.
        :type FontStyle: :class:`tencentcloud.mdl.v20200326.models.SubtitleFontConf`
        :param _StateEffectMode: There are two modes: STEADY and DYNAMIC, corresponding to steady state and unstable state respectively; the default is STEADY. Required when CaptionSource selects `ANALYSIS `.
        :type StateEffectMode: str
        :param _SteadyStateDelayedTime: Steady-state delay time, unit seconds; optional values: 10, 20, default 10. Required when CaptionSource selects `ANALYSIS `.
        :type SteadyStateDelayedTime: int
        """
        self._Name = None
        self._CaptionSelectorName = None
        self._CaptionSource = None
        self._ContentType = None
        self._TargetType = None
        self._SourceLanguage = None
        self._TargetLanguage = None
        self._FontStyle = None
        self._StateEffectMode = None
        self._SteadyStateDelayedTime = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CaptionSelectorName(self):
        return self._CaptionSelectorName

    @CaptionSelectorName.setter
    def CaptionSelectorName(self, CaptionSelectorName):
        self._CaptionSelectorName = CaptionSelectorName

    @property
    def CaptionSource(self):
        return self._CaptionSource

    @CaptionSource.setter
    def CaptionSource(self, CaptionSource):
        self._CaptionSource = CaptionSource

    @property
    def ContentType(self):
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def SourceLanguage(self):
        return self._SourceLanguage

    @SourceLanguage.setter
    def SourceLanguage(self, SourceLanguage):
        self._SourceLanguage = SourceLanguage

    @property
    def TargetLanguage(self):
        return self._TargetLanguage

    @TargetLanguage.setter
    def TargetLanguage(self, TargetLanguage):
        self._TargetLanguage = TargetLanguage

    @property
    def FontStyle(self):
        return self._FontStyle

    @FontStyle.setter
    def FontStyle(self, FontStyle):
        self._FontStyle = FontStyle

    @property
    def StateEffectMode(self):
        return self._StateEffectMode

    @StateEffectMode.setter
    def StateEffectMode(self, StateEffectMode):
        self._StateEffectMode = StateEffectMode

    @property
    def SteadyStateDelayedTime(self):
        return self._SteadyStateDelayedTime

    @SteadyStateDelayedTime.setter
    def SteadyStateDelayedTime(self, SteadyStateDelayedTime):
        self._SteadyStateDelayedTime = SteadyStateDelayedTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CaptionSelectorName = params.get("CaptionSelectorName")
        self._CaptionSource = params.get("CaptionSource")
        self._ContentType = params.get("ContentType")
        self._TargetType = params.get("TargetType")
        self._SourceLanguage = params.get("SourceLanguage")
        self._TargetLanguage = params.get("TargetLanguage")
        if params.get("FontStyle") is not None:
            self._FontStyle = SubtitleFontConf()
            self._FontStyle._deserialize(params.get("FontStyle"))
        self._StateEffectMode = params.get("StateEffectMode")
        self._SteadyStateDelayedTime = params.get("SteadyStateDelayedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubtitleFontConf(AbstractModel):
    """Subtitle style configuration.

    """

    def __init__(self):
        r"""
        :param _LineSpacing: Line spacing.
        :type LineSpacing: int
        :param _Margins: Margins.
        :type Margins: int
        :param _Lines: Rows.
        :type Lines: int
        :param _CharactersPerLine: Number of characters per line.
        :type CharactersPerLine: int
        :param _SourceTextFont: Original font Helvetica: simhei.ttf Song Dynasty: simsun.ttc Dynacw Diamond Black: hkjgh.ttf Helvetica font: helvetica.ttf; Need to be set in Source or Source+Target mode
        :type SourceTextFont: str
        :param _TextColor: Font color is represented by 6 RGB hexadecimal characters.
        :type TextColor: str
        :param _BackgroundColor: The background color is represented by 6 RGB hexadecimal characters.
        :type BackgroundColor: str
        :param _BackgroundAlpha: Background transparency, a number from 0-100.
        :type BackgroundAlpha: int
        :param _PreviewContent: Preview copy.
        :type PreviewContent: str
        :param _PreviewWindowHeight: Preview window height.
        :type PreviewWindowHeight: int
        :param _PreviewWindowWidth: Preview window width.
        :type PreviewWindowWidth: int
        :param _TranslatedTextFont: Translation language font, the enumeration value is the same as Font, the fonts supported by the language need to be distinguished; TextColor needs to be set in Target or Source+Target mode
        :type TranslatedTextFont: str
        """
        self._LineSpacing = None
        self._Margins = None
        self._Lines = None
        self._CharactersPerLine = None
        self._SourceTextFont = None
        self._TextColor = None
        self._BackgroundColor = None
        self._BackgroundAlpha = None
        self._PreviewContent = None
        self._PreviewWindowHeight = None
        self._PreviewWindowWidth = None
        self._TranslatedTextFont = None

    @property
    def LineSpacing(self):
        return self._LineSpacing

    @LineSpacing.setter
    def LineSpacing(self, LineSpacing):
        self._LineSpacing = LineSpacing

    @property
    def Margins(self):
        return self._Margins

    @Margins.setter
    def Margins(self, Margins):
        self._Margins = Margins

    @property
    def Lines(self):
        return self._Lines

    @Lines.setter
    def Lines(self, Lines):
        self._Lines = Lines

    @property
    def CharactersPerLine(self):
        return self._CharactersPerLine

    @CharactersPerLine.setter
    def CharactersPerLine(self, CharactersPerLine):
        self._CharactersPerLine = CharactersPerLine

    @property
    def SourceTextFont(self):
        return self._SourceTextFont

    @SourceTextFont.setter
    def SourceTextFont(self, SourceTextFont):
        self._SourceTextFont = SourceTextFont

    @property
    def TextColor(self):
        return self._TextColor

    @TextColor.setter
    def TextColor(self, TextColor):
        self._TextColor = TextColor

    @property
    def BackgroundColor(self):
        return self._BackgroundColor

    @BackgroundColor.setter
    def BackgroundColor(self, BackgroundColor):
        self._BackgroundColor = BackgroundColor

    @property
    def BackgroundAlpha(self):
        return self._BackgroundAlpha

    @BackgroundAlpha.setter
    def BackgroundAlpha(self, BackgroundAlpha):
        self._BackgroundAlpha = BackgroundAlpha

    @property
    def PreviewContent(self):
        return self._PreviewContent

    @PreviewContent.setter
    def PreviewContent(self, PreviewContent):
        self._PreviewContent = PreviewContent

    @property
    def PreviewWindowHeight(self):
        return self._PreviewWindowHeight

    @PreviewWindowHeight.setter
    def PreviewWindowHeight(self, PreviewWindowHeight):
        self._PreviewWindowHeight = PreviewWindowHeight

    @property
    def PreviewWindowWidth(self):
        return self._PreviewWindowWidth

    @PreviewWindowWidth.setter
    def PreviewWindowWidth(self, PreviewWindowWidth):
        self._PreviewWindowWidth = PreviewWindowWidth

    @property
    def TranslatedTextFont(self):
        return self._TranslatedTextFont

    @TranslatedTextFont.setter
    def TranslatedTextFont(self, TranslatedTextFont):
        self._TranslatedTextFont = TranslatedTextFont


    def _deserialize(self, params):
        self._LineSpacing = params.get("LineSpacing")
        self._Margins = params.get("Margins")
        self._Lines = params.get("Lines")
        self._CharactersPerLine = params.get("CharactersPerLine")
        self._SourceTextFont = params.get("SourceTextFont")
        self._TextColor = params.get("TextColor")
        self._BackgroundColor = params.get("BackgroundColor")
        self._BackgroundAlpha = params.get("BackgroundAlpha")
        self._PreviewContent = params.get("PreviewContent")
        self._PreviewWindowHeight = params.get("PreviewWindowHeight")
        self._PreviewWindowWidth = params.get("PreviewWindowWidth")
        self._TranslatedTextFont = params.get("TranslatedTextFont")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Console Tag, for documentation please refer to: https://www.tencentcloud.com/document/product/651.

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key, for restrictions please refer to the tag documentation: https://www.tencentcloud.com/document/product/651/13354.
        :type TagKey: str
        :param _TagValue: Tag value, for restrictions please refer to the tag documentation: https://www.tencentcloud.com/document/product/651/13354.
        :type TagValue: str
        :param _Category: Tag type, optional; for documentation please refer to: https://www.tencentcloud.com/document/product/651/33023#tag.
        :type Category: str
        """
        self._TagKey = None
        self._TagValue = None
        self._Category = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeShiftSettingsInfo(AbstractModel):
    """Time-shift configuration. This parameter is valid only for HLS_ARCHIVE and DASH_ARCHIVE output groups.

    """

    def __init__(self):
        r"""
        :param _State: Whether to enable time shifting. Valid values: `OPEN`; `CLOSE`
Note: This field may return `null`, indicating that no valid value was found.
        :type State: str
        :param _PlayDomain: Domain name bound for time shifting
Note: This field may return `null`, indicating that no valid value was found.
        :type PlayDomain: str
        :param _StartoverWindow: Allowable time-shift period (s). Value range: [300, 2592000]. Default value: 300Note: This field may return `null`, indicating that no valid value was found.
        :type StartoverWindow: int
        """
        self._State = None
        self._PlayDomain = None
        self._StartoverWindow = None

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def PlayDomain(self):
        return self._PlayDomain

    @PlayDomain.setter
    def PlayDomain(self, PlayDomain):
        self._PlayDomain = PlayDomain

    @property
    def StartoverWindow(self):
        return self._StartoverWindow

    @StartoverWindow.setter
    def StartoverWindow(self, StartoverWindow):
        self._StartoverWindow = StartoverWindow


    def _deserialize(self, params):
        self._State = params.get("State")
        self._PlayDomain = params.get("PlayDomain")
        self._StartoverWindow = params.get("StartoverWindow")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimedMetadataInfo(AbstractModel):
    """Transparent transmission of meta information plan configuration.

    """

    def __init__(self):
        r"""
        :param _ID3: Base64-encoded id3 metadata information, with a maximum limit of 1024 characters.
        :type ID3: str
        """
        self._ID3 = None

    @property
    def ID3(self):
        return self._ID3

    @ID3.setter
    def ID3(self, ID3):
        self._ID3 = ID3


    def _deserialize(self, params):
        self._ID3 = params.get("ID3")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimedMetadataSettingInfo(AbstractModel):
    """Transparent transmission of ID3 information configuration.

    """

    def __init__(self):
        r"""
        :param _Behavior: Whether to transparently transmit ID3 information, optional values: 0:NO_PASSTHROUGH, 1:PASSTHROUGH, default 0.
        :type Behavior: int
        """
        self._Behavior = None

    @property
    def Behavior(self):
        return self._Behavior

    @Behavior.setter
    def Behavior(self, Behavior):
        self._Behavior = Behavior


    def _deserialize(self, params):
        self._Behavior = params.get("Behavior")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimedRecordSettings(AbstractModel):
    """Timed recording settings

    """

    def __init__(self):
        r"""
        :param _AutoClear: Whether to automatically delete finished recording events. Valid values: `CLOSE`, `OPEN`. If this parameter is left empty, `CLOSE` will be used.
If it is set to `OPEN`, a recording event will be deleted 7 days after it is finished.
Note: This field may return `null`, indicating that no valid value was found.
        :type AutoClear: str
        """
        self._AutoClear = None

    @property
    def AutoClear(self):
        return self._AutoClear

    @AutoClear.setter
    def AutoClear(self, AutoClear):
        self._AutoClear = AutoClear


    def _deserialize(self, params):
        self._AutoClear = params.get("AutoClear")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimingSettingsReq(AbstractModel):
    """Event trigger time settings

    """

    def __init__(self):
        r"""
        :param _StartType: Event trigger type. Valid values: `FIXED_TIME`, `IMMEDIATE`. This parameter is required if `EventType` is `INPUT_SWITCH`.
        :type StartType: str
        :param _Time: This parameter is required if `EventType` is `INPUT_SWITCH` and `StartType` is `FIXED_TIME`.
It must be in UTC format, e.g., `2020-01-01T12:00:00Z`.
        :type Time: str
        :param _StartTime: This parameter is required if `EventType` is `TIMED_RECORD`.
It specifies the recording start time in UTC format (e.g., `2020-01-01T12:00:00Z`) and must be at least 1 minute later than the current time.
        :type StartTime: str
        :param _EndTime: This parameter is required if `EventType` is `TIMED_RECORD`.
It specifies the recording end time in UTC format (e.g., `2020-01-01T12:00:00Z`) and must be at least 1 minute later than the recording start time.
        :type EndTime: str
        """
        self._StartType = None
        self._Time = None
        self._StartTime = None
        self._EndTime = None

    @property
    def StartType(self):
        return self._StartType

    @StartType.setter
    def StartType(self, StartType):
        self._StartType = StartType

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._StartType = params.get("StartType")
        self._Time = params.get("Time")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimingSettingsResp(AbstractModel):
    """Event trigger time settings

    """

    def __init__(self):
        r"""
        :param _StartType: Event trigger type
        :type StartType: str
        :param _Time: Not empty if `StartType` is `FIXED_TIME`
UTC time, such as `2020-01-01T12:00:00Z`
        :type Time: str
        :param _StartTime: This parameter cannot be empty if `EventType` is `TIMED_RECORD`.
It indicates the start time for recording in UTC format (e.g., `2020-01-01T12:00:00Z`) and must be at least 1 minute later than the current time.
        :type StartTime: str
        :param _EndTime: This parameter cannot be empty if `EventType` is `TIMED_RECORD`.
It indicates the end time for recording in UTC format (e.g., `2020-01-01T12:00:00Z`) and must be at least 1 minute later than the start time for recording.
        :type EndTime: str
        """
        self._StartType = None
        self._Time = None
        self._StartTime = None
        self._EndTime = None

    @property
    def StartType(self):
        return self._StartType

    @StartType.setter
    def StartType(self, StartType):
        self._StartType = StartType

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._StartType = params.get("StartType")
        self._Time = params.get("Time")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoCodecDetail(AbstractModel):
    """Video codec additional configuration.

    """

    def __init__(self):
        r"""
        :param _Profile: The three image quality levels of h264 include: BASELINE, HIGH, and MAIN. The default option is MAIN.
        :type Profile: str
        :param _Level: Profile corresponding codec performance, options include: 1, 1.1, 1.2, 1.3, 2, 2.1, 2.2, 2.3, 3, 3.1, 3.2, 4, 4.1, 4.2, 5, 5.1, AUTO. The default option is AUTO.
        :type Level: str
        :param _EntropyEncoding: Codecs include entropy coding and lossless coding, and options include: CABAC and CAVLC. The default option is CABAC. .
        :type EntropyEncoding: str
        :param _AdaptiveQuantization: Mode, options include: AUTO, HIGH, HIGHER, LOW, MAX, MEDIUM, OFF. The default option is: AUTO. .
        :type AdaptiveQuantization: str
        :param _LookAheadRateControl: Analyze subsequent encoded frames in advance, options include: HIGH, LOW, MEDIUM. The default option is: MEDIUM. .
        :type LookAheadRateControl: str
        """
        self._Profile = None
        self._Level = None
        self._EntropyEncoding = None
        self._AdaptiveQuantization = None
        self._LookAheadRateControl = None

    @property
    def Profile(self):
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def EntropyEncoding(self):
        return self._EntropyEncoding

    @EntropyEncoding.setter
    def EntropyEncoding(self, EntropyEncoding):
        self._EntropyEncoding = EntropyEncoding

    @property
    def AdaptiveQuantization(self):
        return self._AdaptiveQuantization

    @AdaptiveQuantization.setter
    def AdaptiveQuantization(self, AdaptiveQuantization):
        self._AdaptiveQuantization = AdaptiveQuantization

    @property
    def LookAheadRateControl(self):
        return self._LookAheadRateControl

    @LookAheadRateControl.setter
    def LookAheadRateControl(self, LookAheadRateControl):
        self._LookAheadRateControl = LookAheadRateControl


    def _deserialize(self, params):
        self._Profile = params.get("Profile")
        self._Level = params.get("Level")
        self._EntropyEncoding = params.get("EntropyEncoding")
        self._AdaptiveQuantization = params.get("AdaptiveQuantization")
        self._LookAheadRateControl = params.get("LookAheadRateControl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoPipelineInputStatistics(AbstractModel):
    """Pipeline input video statistics.

    """

    def __init__(self):
        r"""
        :param _Fps: Video FPS.
        :type Fps: int
        :param _Rate: Video bitrate in bps.
        :type Rate: int
        :param _Pid: Video `Pid`, which is available only if the input is `rtp/udp`.
        :type Pid: int
        """
        self._Fps = None
        self._Rate = None
        self._Pid = None

    @property
    def Fps(self):
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def Rate(self):
        return self._Rate

    @Rate.setter
    def Rate(self, Rate):
        self._Rate = Rate

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid


    def _deserialize(self, params):
        self._Fps = params.get("Fps")
        self._Rate = params.get("Rate")
        self._Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoTemplateInfo(AbstractModel):
    """Video transcoding template.

    """

    def __init__(self):
        r"""
        :param _Name: Video transcoding template name, which can contain 1-20 letters and digits.
        :type Name: str
        :param _Vcodec: Video codec. Valid values: H264/H265. If this parameter is left empty, the original value will be used.
        :type Vcodec: str
        :param _VideoBitrate: Video bitrate. Value range: [50000,40000000]. The value can only be a multiple of 1,000. If this parameter is left empty, the original value will be used.
        :type VideoBitrate: int
        :param _Width: Video width. Value range: (0,3000]. The value can only be a multiple of 4. If this parameter is left empty, the original value will be used.
        :type Width: int
        :param _Height: Video height. Value range: (0,3000]. The value can only be a multiple of 4. If this parameter is left empty, the original value will be used.
        :type Height: int
        :param _Fps: Video frame rate. Value range: [1,240]. If this parameter is left empty, the original value will be used.
        :type Fps: int
        :param _TopSpeed: Whether to enable top speed codec. Valid value: CLOSE/OPEN. Default value: CLOSE.
        :type TopSpeed: str
        :param _BitrateCompressionRatio: Top speed codec compression ratio. Value range: [0,50]. The lower the compression ratio, the higher the image quality.
        :type BitrateCompressionRatio: int
        :param _RateControlMode: Bitrate control mode. Valid values: `CBR`, `ABR` (default)
        :type RateControlMode: str
        :param _WatermarkId: Watermark ID
Note: This field may return `null`, indicating that no valid value was found.
        :type WatermarkId: str
        :param _FaceBlurringEnabled: Whether to enable the face blur function, 1 is on, 0 is off, and the default is 0.
        :type FaceBlurringEnabled: int
        :param _FrameRateType: This field indicates how to specify the output video frame rate. If FOLLOW_SOURCE is selected, the output video frame rate will be set equal to the input video frame rate of the first input. If SPECIFIED_FRACTION is selected, the output video frame rate is determined by the fraction (frame rate numerator and frame rate denominator). If SPECIFIED_HZ is selected, the frame rate of the output video is determined by the HZ you enter.
        :type FrameRateType: str
        :param _FrameRateNumerator: Valid when the FrameRateType type you select is SPECIFIED_FRACTION, the output frame rate numerator setting.
        :type FrameRateNumerator: int
        :param _FrameRateDenominator: Valid when the FrameRateType type you select is SPECIFIED_FRACTION, the output frame rate denominator setting.
        :type FrameRateDenominator: int
        :param _BFramesNum: The number of B frames can be selected from 1 to 3.
        :type BFramesNum: int
        :param _RefFramesNum: The number of reference frames can be selected from 1 to 16.
        :type RefFramesNum: int
        :param _AdditionalRateSettings: Additional video bitrate configuration.
        :type AdditionalRateSettings: :class:`tencentcloud.mdl.v20200326.models.AdditionalRateSetting`
        :param _VideoCodecDetails: Video encoding configuration.
        :type VideoCodecDetails: :class:`tencentcloud.mdl.v20200326.models.VideoCodecDetail`
        """
        self._Name = None
        self._Vcodec = None
        self._VideoBitrate = None
        self._Width = None
        self._Height = None
        self._Fps = None
        self._TopSpeed = None
        self._BitrateCompressionRatio = None
        self._RateControlMode = None
        self._WatermarkId = None
        self._FaceBlurringEnabled = None
        self._FrameRateType = None
        self._FrameRateNumerator = None
        self._FrameRateDenominator = None
        self._BFramesNum = None
        self._RefFramesNum = None
        self._AdditionalRateSettings = None
        self._VideoCodecDetails = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Vcodec(self):
        return self._Vcodec

    @Vcodec.setter
    def Vcodec(self, Vcodec):
        self._Vcodec = Vcodec

    @property
    def VideoBitrate(self):
        return self._VideoBitrate

    @VideoBitrate.setter
    def VideoBitrate(self, VideoBitrate):
        self._VideoBitrate = VideoBitrate

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Fps(self):
        return self._Fps

    @Fps.setter
    def Fps(self, Fps):
        self._Fps = Fps

    @property
    def TopSpeed(self):
        return self._TopSpeed

    @TopSpeed.setter
    def TopSpeed(self, TopSpeed):
        self._TopSpeed = TopSpeed

    @property
    def BitrateCompressionRatio(self):
        return self._BitrateCompressionRatio

    @BitrateCompressionRatio.setter
    def BitrateCompressionRatio(self, BitrateCompressionRatio):
        self._BitrateCompressionRatio = BitrateCompressionRatio

    @property
    def RateControlMode(self):
        return self._RateControlMode

    @RateControlMode.setter
    def RateControlMode(self, RateControlMode):
        self._RateControlMode = RateControlMode

    @property
    def WatermarkId(self):
        return self._WatermarkId

    @WatermarkId.setter
    def WatermarkId(self, WatermarkId):
        self._WatermarkId = WatermarkId

    @property
    def FaceBlurringEnabled(self):
        return self._FaceBlurringEnabled

    @FaceBlurringEnabled.setter
    def FaceBlurringEnabled(self, FaceBlurringEnabled):
        self._FaceBlurringEnabled = FaceBlurringEnabled

    @property
    def FrameRateType(self):
        return self._FrameRateType

    @FrameRateType.setter
    def FrameRateType(self, FrameRateType):
        self._FrameRateType = FrameRateType

    @property
    def FrameRateNumerator(self):
        return self._FrameRateNumerator

    @FrameRateNumerator.setter
    def FrameRateNumerator(self, FrameRateNumerator):
        self._FrameRateNumerator = FrameRateNumerator

    @property
    def FrameRateDenominator(self):
        return self._FrameRateDenominator

    @FrameRateDenominator.setter
    def FrameRateDenominator(self, FrameRateDenominator):
        self._FrameRateDenominator = FrameRateDenominator

    @property
    def BFramesNum(self):
        return self._BFramesNum

    @BFramesNum.setter
    def BFramesNum(self, BFramesNum):
        self._BFramesNum = BFramesNum

    @property
    def RefFramesNum(self):
        return self._RefFramesNum

    @RefFramesNum.setter
    def RefFramesNum(self, RefFramesNum):
        self._RefFramesNum = RefFramesNum

    @property
    def AdditionalRateSettings(self):
        return self._AdditionalRateSettings

    @AdditionalRateSettings.setter
    def AdditionalRateSettings(self, AdditionalRateSettings):
        self._AdditionalRateSettings = AdditionalRateSettings

    @property
    def VideoCodecDetails(self):
        return self._VideoCodecDetails

    @VideoCodecDetails.setter
    def VideoCodecDetails(self, VideoCodecDetails):
        self._VideoCodecDetails = VideoCodecDetails


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Vcodec = params.get("Vcodec")
        self._VideoBitrate = params.get("VideoBitrate")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        self._Fps = params.get("Fps")
        self._TopSpeed = params.get("TopSpeed")
        self._BitrateCompressionRatio = params.get("BitrateCompressionRatio")
        self._RateControlMode = params.get("RateControlMode")
        self._WatermarkId = params.get("WatermarkId")
        self._FaceBlurringEnabled = params.get("FaceBlurringEnabled")
        self._FrameRateType = params.get("FrameRateType")
        self._FrameRateNumerator = params.get("FrameRateNumerator")
        self._FrameRateDenominator = params.get("FrameRateDenominator")
        self._BFramesNum = params.get("BFramesNum")
        self._RefFramesNum = params.get("RefFramesNum")
        if params.get("AdditionalRateSettings") is not None:
            self._AdditionalRateSettings = AdditionalRateSetting()
            self._AdditionalRateSettings._deserialize(params.get("AdditionalRateSettings"))
        if params.get("VideoCodecDetails") is not None:
            self._VideoCodecDetails = VideoCodecDetail()
            self._VideoCodecDetails._deserialize(params.get("VideoCodecDetails"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        