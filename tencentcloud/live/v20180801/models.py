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


class AddDelayLiveStreamRequest(AbstractModel):
    """AddDelayLiveStream request structure.

    """

    def __init__(self):
        r"""
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.
        :type AppName: str
        :param DomainName: Push domain name.
        :type DomainName: str
        :param StreamName: Stream name.
        :type StreamName: str
        :param DelayTime: Delay time in seconds, up to 600s.
        :type DelayTime: int
        :param ExpireTime: Expiration time of the configured delayed playback in UTC format, such as 2018-11-29T19:00:00Z.
Notes:
1. The configuration will expire after 7 days by default and can last up to 7 days.
2. The Beijing time is in UTC+8. This value should be in the format as required by ISO 8601. For more information, please see [ISO Date and Time Format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).
        :type ExpireTime: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None
        self.DelayTime = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        self.DelayTime = params.get("DelayTime")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddDelayLiveStreamResponse(AbstractModel):
    """AddDelayLiveStream response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddLiveDomainRequest(AbstractModel):
    """AddLiveDomain request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Domain name.
        :type DomainName: str
        :param DomainType: Domain name type.
0: push domain name.
1: playback domain name.
        :type DomainType: int
        :param PlayType: Pull domain name type:
1: Mainland China.
2: global.
3: outside Mainland China.
Default value: 1.
        :type PlayType: int
        :param IsDelayLive: Whether it is LCB:
0: LVB,
1: LCB.
Default value: 0.
        :type IsDelayLive: int
        :param IsMiniProgramLive: Whether it is LVB on Mini Program.
0: LVB.
1: LVB on Mini Program.
Default value: 0.
        :type IsMiniProgramLive: int
        """
        self.DomainName = None
        self.DomainType = None
        self.PlayType = None
        self.IsDelayLive = None
        self.IsMiniProgramLive = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.DomainType = params.get("DomainType")
        self.PlayType = params.get("PlayType")
        self.IsDelayLive = params.get("IsDelayLive")
        self.IsMiniProgramLive = params.get("IsMiniProgramLive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddLiveDomainResponse(AbstractModel):
    """AddLiveDomain response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddLiveWatermarkRequest(AbstractModel):
    """AddLiveWatermark request structure.

    """

    def __init__(self):
        r"""
        :param PictureUrl: Watermark image URL.
Unallowed characters in the URL:
 ;(){}$>`#"\'|
        :type PictureUrl: str
        :param WatermarkName: Watermark name.
Up to 16 bytes.
        :type WatermarkName: str
        :param XPosition: Display position: X-axis offset in %. Default value: 0.
        :type XPosition: int
        :param YPosition: Display position: Y-axis offset in %. Default value: 0.
        :type YPosition: int
        :param Width: Watermark width or its percentage of the live streaming video width. It is recommended to just specify either height or width as the other will be scaled proportionally to avoid distortions. The original width is used by default.
        :type Width: int
        :param Height: Watermark height, which is set by entering a percentage of the live stream image’s original height. You are advised to set either the height or width as the other will be scaled proportionally to avoid distortions. Default value: original height.
        :type Height: int
        """
        self.PictureUrl = None
        self.WatermarkName = None
        self.XPosition = None
        self.YPosition = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.PictureUrl = params.get("PictureUrl")
        self.WatermarkName = params.get("WatermarkName")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddLiveWatermarkResponse(AbstractModel):
    """AddLiveWatermark response structure.

    """

    def __init__(self):
        r"""
        :param WatermarkId: Watermark ID.
        :type WatermarkId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.WatermarkId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        self.RequestId = params.get("RequestId")


class BandwidthInfo(AbstractModel):
    """Bandwidth information

    """

    def __init__(self):
        r"""
        :param Time: Format of return value:
yyyy-mm-dd HH:MM:SS
The time accuracy matches with the query granularity.
        :type Time: str
        :param Bandwidth: Bandwidth.
        :type Bandwidth: float
        """
        self.Time = None
        self.Bandwidth = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Bandwidth = params.get("Bandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindLiveDomainCertRequest(AbstractModel):
    """BindLiveDomainCert request structure.

    """

    def __init__(self):
        r"""
        :param CertId: Certificate ID, which can be obtained through the `CreateLiveCert` API.
        :type CertId: int
        :param DomainName: Playback domain name.
        :type DomainName: str
        :param Status: HTTPS status. 0: disabled, 1: enabled.
        :type Status: int
        """
        self.CertId = None
        self.DomainName = None
        self.Status = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.DomainName = params.get("DomainName")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindLiveDomainCertResponse(AbstractModel):
    """BindLiveDomainCert response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CallBackRuleInfo(AbstractModel):
    """Rule information

    """

    def __init__(self):
        r"""
        :param CreateTime: Rule creation time.
        :type CreateTime: str
        :param UpdateTime: Rule update time.
        :type UpdateTime: str
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param DomainName: Push domain name.
        :type DomainName: str
        :param AppName: Push path.
        :type AppName: str
        """
        self.CreateTime = None
        self.UpdateTime = None
        self.TemplateId = None
        self.DomainName = None
        self.AppName = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.TemplateId = params.get("TemplateId")
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CallBackTemplateInfo(AbstractModel):
    """Callback template information.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param TemplateName: Template name.
        :type TemplateName: str
        :param Description: Description.
        :type Description: str
        :param StreamBeginNotifyUrl: Stream starting callback URL.
        :type StreamBeginNotifyUrl: str
        :param StreamMixNotifyUrl: Stream mixing callback URL (disused)
        :type StreamMixNotifyUrl: str
        :param StreamEndNotifyUrl: Interruption callback URL.
        :type StreamEndNotifyUrl: str
        :param RecordNotifyUrl: Recording callback URL.
        :type RecordNotifyUrl: str
        :param SnapshotNotifyUrl: Screencapturing callback URL.
        :type SnapshotNotifyUrl: str
        :param PornCensorshipNotifyUrl: Porn detection callback URL.
        :type PornCensorshipNotifyUrl: str
        :param CallbackKey: Callback authentication key.
        :type CallbackKey: str
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.StreamBeginNotifyUrl = None
        self.StreamMixNotifyUrl = None
        self.StreamEndNotifyUrl = None
        self.RecordNotifyUrl = None
        self.SnapshotNotifyUrl = None
        self.PornCensorshipNotifyUrl = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        self.StreamBeginNotifyUrl = params.get("StreamBeginNotifyUrl")
        self.StreamMixNotifyUrl = params.get("StreamMixNotifyUrl")
        self.StreamEndNotifyUrl = params.get("StreamEndNotifyUrl")
        self.RecordNotifyUrl = params.get("RecordNotifyUrl")
        self.SnapshotNotifyUrl = params.get("SnapshotNotifyUrl")
        self.PornCensorshipNotifyUrl = params.get("PornCensorshipNotifyUrl")
        self.CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelCommonMixStreamRequest(AbstractModel):
    """CancelCommonMixStream request structure.

    """

    def __init__(self):
        r"""
        :param MixStreamSessionId: ID of stream mix session (from applying for stream mix to canceling stream mix).
This value is the same as the `MixStreamSessionId` in `CreateCommonMixStream`.
        :type MixStreamSessionId: str
        """
        self.MixStreamSessionId = None


    def _deserialize(self, params):
        self.MixStreamSessionId = params.get("MixStreamSessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelCommonMixStreamResponse(AbstractModel):
    """CancelCommonMixStream response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CdnPlayStatData(AbstractModel):
    """Downstream playback statistical metrics

    """

    def __init__(self):
        r"""
        :param Time: Time point in the format of `yyyy-mm-dd HH:MM:SS`.
        :type Time: str
        :param Bandwidth: Bandwidth in Mbps.
        :type Bandwidth: float
        :param Flux: Traffic in MB.
        :type Flux: float
        :param Request: Number of new requests.
        :type Request: int
        :param Online: Number of concurrent connections.
        :type Online: int
        """
        self.Time = None
        self.Bandwidth = None
        self.Flux = None
        self.Request = None
        self.Online = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Bandwidth = params.get("Bandwidth")
        self.Flux = params.get("Flux")
        self.Request = params.get("Request")
        self.Online = params.get("Online")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertInfo(AbstractModel):
    """Certificate information.

    """

    def __init__(self):
        r"""
        :param CertId: Certificate ID.
        :type CertId: int
        :param CertName: Certificate name.
        :type CertName: str
        :param Description: Description.
        :type Description: str
        :param CreateTime: Creation time in UTC format.
        :type CreateTime: str
        :param HttpsCrt: Certificate content.
        :type HttpsCrt: str
        :param CertType: Certificate type.
0: user-added certificate
1: Tencent Cloud-hosted certificate
        :type CertType: int
        :param CertExpireTime: Certificate expiration time in UTC format.
        :type CertExpireTime: str
        :param DomainList: List of domain names that use this certificate.
        :type DomainList: list of str
        """
        self.CertId = None
        self.CertName = None
        self.Description = None
        self.CreateTime = None
        self.HttpsCrt = None
        self.CertType = None
        self.CertExpireTime = None
        self.DomainList = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.CertName = params.get("CertName")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.HttpsCrt = params.get("HttpsCrt")
        self.CertType = params.get("CertType")
        self.CertExpireTime = params.get("CertExpireTime")
        self.DomainList = params.get("DomainList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClientIpPlaySumInfo(AbstractModel):
    """Aggregated playback information of client IP.

    """

    def __init__(self):
        r"""
        :param ClientIp: Client IP in dotted-decimal notation.
        :type ClientIp: str
        :param Province: District where the client is located.
        :type Province: str
        :param TotalFlux: Total traffic.
        :type TotalFlux: float
        :param TotalRequest: Total number of requests.
        :type TotalRequest: int
        :param TotalFailedRequest: Total number of failed requests.
        :type TotalFailedRequest: int
        :param CountryArea: Country/region where the client is located.
        :type CountryArea: str
        """
        self.ClientIp = None
        self.Province = None
        self.TotalFlux = None
        self.TotalRequest = None
        self.TotalFailedRequest = None
        self.CountryArea = None


    def _deserialize(self, params):
        self.ClientIp = params.get("ClientIp")
        self.Province = params.get("Province")
        self.TotalFlux = params.get("TotalFlux")
        self.TotalRequest = params.get("TotalRequest")
        self.TotalFailedRequest = params.get("TotalFailedRequest")
        self.CountryArea = params.get("CountryArea")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonMixControlParams(AbstractModel):
    """General stream mix control parameter

    """

    def __init__(self):
        r"""
        :param UseMixCropCenter: Value range: [0,1]. 
If 1 is entered, when the layer resolution in the parameter is different from the actual video resolution, the video will be automatically cropped according to the resolution set by the layer.
        :type UseMixCropCenter: int
        :param AllowCopy: Value range: [0,1].
If this parameter is set to 1, when both `InputStreamList` and `OutputParams.OutputStreamType` are set to 1, you can copy a stream instead of canceling it.
        :type AllowCopy: int
        :param PassInputSei: Valid values: 0, 1
If you set this parameter to 1, SEI (Supplemental Enhanced Information) of the input streams will be passed through.
        :type PassInputSei: int
        """
        self.UseMixCropCenter = None
        self.AllowCopy = None
        self.PassInputSei = None


    def _deserialize(self, params):
        self.UseMixCropCenter = params.get("UseMixCropCenter")
        self.AllowCopy = params.get("AllowCopy")
        self.PassInputSei = params.get("PassInputSei")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonMixCropParams(AbstractModel):
    """General stream mix input crop parameter.

    """

    def __init__(self):
        r"""
        :param CropWidth: Crop width. Value range: [0,2000].
        :type CropWidth: float
        :param CropHeight: Crop height. Value range: [0,2000].
        :type CropHeight: float
        :param CropStartLocationX: Starting crop X coordinate. Value range: [0,2000].
        :type CropStartLocationX: float
        :param CropStartLocationY: Starting crop Y coordinate. Value range: [0,2000].
        :type CropStartLocationY: float
        """
        self.CropWidth = None
        self.CropHeight = None
        self.CropStartLocationX = None
        self.CropStartLocationY = None


    def _deserialize(self, params):
        self.CropWidth = params.get("CropWidth")
        self.CropHeight = params.get("CropHeight")
        self.CropStartLocationX = params.get("CropStartLocationX")
        self.CropStartLocationY = params.get("CropStartLocationY")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonMixInputParam(AbstractModel):
    """General stream mix input parameter.

    """

    def __init__(self):
        r"""
        :param InputStreamName: Input stream name, which can contain up to 80 bytes of letters, digits, and underscores.
The value should be the name of an input stream for stream mix when `LayoutParams.InputType` is set to `0` (audio and video), `4` (pure audio), or `5` (pure video).
The value can be a random name for identification, such as `Canvas1` or `Picture1`, when `LayoutParams.InputType` is set to `2` (image) or `3` (canvas).
        :type InputStreamName: str
        :param LayoutParams: Input stream layout parameter.
        :type LayoutParams: :class:`tencentcloud.live.v20180801.models.CommonMixLayoutParams`
        :param CropParams: Input stream crop parameter.
        :type CropParams: :class:`tencentcloud.live.v20180801.models.CommonMixCropParams`
        """
        self.InputStreamName = None
        self.LayoutParams = None
        self.CropParams = None


    def _deserialize(self, params):
        self.InputStreamName = params.get("InputStreamName")
        if params.get("LayoutParams") is not None:
            self.LayoutParams = CommonMixLayoutParams()
            self.LayoutParams._deserialize(params.get("LayoutParams"))
        if params.get("CropParams") is not None:
            self.CropParams = CommonMixCropParams()
            self.CropParams._deserialize(params.get("CropParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonMixLayoutParams(AbstractModel):
    """General stream mix layout parameter.

    """

    def __init__(self):
        r"""
        :param ImageLayer: Input layer. Value range: [1,16]
(1) For the background stream, i.e., the room owner’s image or the canvas, set this parameter to `1`.
(2) This parameter is required for audio-only stream mixing as well.
Note that two inputs cannot have the same `ImageLayer` value.
        :type ImageLayer: int
        :param InputType: Input type. Value range: [0,5].
If this parameter is left empty, 0 will be used by default.
0: the input stream is audio/video.
2: the input stream is image.
3: the input stream is canvas. 
4: the input stream is audio.
5: the input stream is pure video.
        :type InputType: int
        :param ImageHeight: Output height of input video image. Value range:
Pixel: [0,2000]
Percentage: [0.01,0.99]
If this parameter is left empty, the input stream height will be used by default.
If percentage is used, the expected output is (percentage * background height).
        :type ImageHeight: float
        :param ImageWidth: Output width of input video image. Value range:
Pixel: [0,2000]
Percentage: [0.01,0.99]
If this parameter is left empty, the input stream width will be used by default.
If percentage is used, the expected output is (percentage * background width).
        :type ImageWidth: float
        :param LocationX: X-axis offset of input in output video image. Value range:
Pixel: [0,2000]
Percentage: [0.01,0.99]
If this parameter is left empty, 0 will be used by default.
Horizontal offset from the top-left corner of main host background video image. 
If percentage is used, the expected output is (percentage * background width).
        :type LocationX: float
        :param LocationY: Y-axis offset of input in output video image. Value range:
Pixel: [0,2000]
Percentage: [0.01,0.99]
If this parameter is left empty, 0 will be used by default.
Vertical offset from the top-left corner of main host background video image. 
If percentage is used, the expected output is (percentage * background width)
        :type LocationY: float
        :param Color: When `InputType` is 3 (canvas), this value indicates the canvas color.
Commonly used colors include:
Red: 0xcc0033.
Yellow: 0xcc9900.
Green: 0xcccc33.
Blue: 0x99CCFF.
Black: 0x000000.
White: 0xFFFFFF.
Gray: 0x999999
        :type Color: str
        :param WatermarkId: When `InputType` is 2 (image), this value is the watermark ID.
        :type WatermarkId: int
        """
        self.ImageLayer = None
        self.InputType = None
        self.ImageHeight = None
        self.ImageWidth = None
        self.LocationX = None
        self.LocationY = None
        self.Color = None
        self.WatermarkId = None


    def _deserialize(self, params):
        self.ImageLayer = params.get("ImageLayer")
        self.InputType = params.get("InputType")
        self.ImageHeight = params.get("ImageHeight")
        self.ImageWidth = params.get("ImageWidth")
        self.LocationX = params.get("LocationX")
        self.LocationY = params.get("LocationY")
        self.Color = params.get("Color")
        self.WatermarkId = params.get("WatermarkId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonMixOutputParams(AbstractModel):
    """General stream mix output parameter.

    """

    def __init__(self):
        r"""
        :param OutputStreamName: Output stream name.
        :type OutputStreamName: str
        :param OutputStreamType: Output stream type. Valid values: [0,1].
If this parameter is left empty, 0 will be used by default.
If the output stream is a stream in the input stream list, enter 0.
If you want the stream mix result to be a new stream, enter 1.
If this value is 1, `output_stream_id` cannot appear in `input_stram_list`, and there cannot be a stream with the same ID on the LVB backend.
        :type OutputStreamType: int
        :param OutputStreamBitRate: Output stream bitrate. Value range: [1,50000].
If this parameter is left empty, the system will automatically determine.
        :type OutputStreamBitRate: int
        :param OutputStreamGop: Output stream GOP size. Value range: [1,10].
If this parameter is left empty, the system will automatically determine.
        :type OutputStreamGop: int
        :param OutputStreamFrameRate: Output stream frame rate. Value range: [1,60].
If this parameter is left empty, the system will automatically determine.
        :type OutputStreamFrameRate: int
        :param OutputAudioBitRate: Output stream audio bitrate. Value range: [1,500]
If this parameter is left empty, the system will automatically determine.
        :type OutputAudioBitRate: int
        :param OutputAudioSampleRate: Output stream audio sample rate. Valid values: [96000, 88200, 64000, 48000, 44100, 32000,24000, 22050, 16000, 12000, 11025, 8000].
If this parameter is left empty, the system will automatically determine.
        :type OutputAudioSampleRate: int
        :param OutputAudioChannels: Output stream audio sound channel. Valid values: [1,2].
If this parameter is left empty, the system will automatically determine.
        :type OutputAudioChannels: int
        :param MixSei: SEI information in output stream. If there are no special needs, leave it empty.
        :type MixSei: str
        """
        self.OutputStreamName = None
        self.OutputStreamType = None
        self.OutputStreamBitRate = None
        self.OutputStreamGop = None
        self.OutputStreamFrameRate = None
        self.OutputAudioBitRate = None
        self.OutputAudioSampleRate = None
        self.OutputAudioChannels = None
        self.MixSei = None


    def _deserialize(self, params):
        self.OutputStreamName = params.get("OutputStreamName")
        self.OutputStreamType = params.get("OutputStreamType")
        self.OutputStreamBitRate = params.get("OutputStreamBitRate")
        self.OutputStreamGop = params.get("OutputStreamGop")
        self.OutputStreamFrameRate = params.get("OutputStreamFrameRate")
        self.OutputAudioBitRate = params.get("OutputAudioBitRate")
        self.OutputAudioSampleRate = params.get("OutputAudioSampleRate")
        self.OutputAudioChannels = params.get("OutputAudioChannels")
        self.MixSei = params.get("MixSei")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConcurrentRecordStreamNum(AbstractModel):
    """Number of concurrent recording channels

    """

    def __init__(self):
        r"""
        :param Time: Time point.
        :type Time: str
        :param Num: Number of channels.
        :type Num: int
        """
        self.Time = None
        self.Num = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Num = params.get("Num")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCommonMixStreamRequest(AbstractModel):
    """CreateCommonMixStream request structure.

    """

    def __init__(self):
        r"""
        :param MixStreamSessionId: ID of a stream mix session (from applying for the stream mix to cancelling it). This parameter can contain up to 80 bytes of letters, digits, and underscores.
        :type MixStreamSessionId: str
        :param InputStreamList: Input stream list for stream mix.
        :type InputStreamList: list of CommonMixInputParam
        :param OutputParams: Output stream parameter for stream mix.
        :type OutputParams: :class:`tencentcloud.live.v20180801.models.CommonMixOutputParams`
        :param MixStreamTemplateId: Input template ID. If this parameter is set, the output will be generated according to the default template layout, and there is no need to enter the custom position parameters.
If this parameter is left empty, 0 will be used by default.
For two input sources, 10, 20, 30, 40, and 50 are supported.
For three input sources, 310, 390, and 391 are supported.
For four input sources, 410 is supported.
For five input sources, 510 and 590 are supported.
For six input sources, 610 is supported.
        :type MixStreamTemplateId: int
        :param ControlParams: Special control parameter for stream mix. If there are no special needs, leave it empty.
        :type ControlParams: :class:`tencentcloud.live.v20180801.models.CommonMixControlParams`
        """
        self.MixStreamSessionId = None
        self.InputStreamList = None
        self.OutputParams = None
        self.MixStreamTemplateId = None
        self.ControlParams = None


    def _deserialize(self, params):
        self.MixStreamSessionId = params.get("MixStreamSessionId")
        if params.get("InputStreamList") is not None:
            self.InputStreamList = []
            for item in params.get("InputStreamList"):
                obj = CommonMixInputParam()
                obj._deserialize(item)
                self.InputStreamList.append(obj)
        if params.get("OutputParams") is not None:
            self.OutputParams = CommonMixOutputParams()
            self.OutputParams._deserialize(params.get("OutputParams"))
        self.MixStreamTemplateId = params.get("MixStreamTemplateId")
        if params.get("ControlParams") is not None:
            self.ControlParams = CommonMixControlParams()
            self.ControlParams._deserialize(params.get("ControlParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCommonMixStreamResponse(AbstractModel):
    """CreateCommonMixStream response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLiveCallbackRuleRequest(AbstractModel):
    """CreateLiveCallbackRule request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Push domain name.
        :type DomainName: str
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.
        :type AppName: str
        :param TemplateId: Template ID.
        :type TemplateId: int
        """
        self.DomainName = None
        self.AppName = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveCallbackRuleResponse(AbstractModel):
    """CreateLiveCallbackRule response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLiveCallbackTemplateRequest(AbstractModel):
    """CreateLiveCallbackTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateName: Template name.
Maximum length: 255 bytes.
Only letters, digits, underscores, and hyphens can be contained.
        :type TemplateName: str
        :param Description: Description.
Maximum length: 1,024 bytes.
Only letters, digits, underscores, and hyphens can be contained.
        :type Description: str
        :param StreamBeginNotifyUrl: Stream starting callback URL,
Protocol document: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1).
        :type StreamBeginNotifyUrl: str
        :param StreamEndNotifyUrl: Interruption callback URL,
Protocol document: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1).
        :type StreamEndNotifyUrl: str
        :param RecordNotifyUrl: Recording callback URL,
Protocol document: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1).
        :type RecordNotifyUrl: str
        :param SnapshotNotifyUrl: Screencapturing callback URL,
Protocol document: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1).
        :type SnapshotNotifyUrl: str
        :param PornCensorshipNotifyUrl: Porn detection callback URL,
Protocol document: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32741?from_cn_redirect=1).
        :type PornCensorshipNotifyUrl: str
        :param CallbackKey: Callback key. The callback URL is public. For the callback signature, please see the event message notification document.
[Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1).
        :type CallbackKey: str
        :param StreamMixNotifyUrl: Disused
        :type StreamMixNotifyUrl: str
        """
        self.TemplateName = None
        self.Description = None
        self.StreamBeginNotifyUrl = None
        self.StreamEndNotifyUrl = None
        self.RecordNotifyUrl = None
        self.SnapshotNotifyUrl = None
        self.PornCensorshipNotifyUrl = None
        self.CallbackKey = None
        self.StreamMixNotifyUrl = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        self.StreamBeginNotifyUrl = params.get("StreamBeginNotifyUrl")
        self.StreamEndNotifyUrl = params.get("StreamEndNotifyUrl")
        self.RecordNotifyUrl = params.get("RecordNotifyUrl")
        self.SnapshotNotifyUrl = params.get("SnapshotNotifyUrl")
        self.PornCensorshipNotifyUrl = params.get("PornCensorshipNotifyUrl")
        self.CallbackKey = params.get("CallbackKey")
        self.StreamMixNotifyUrl = params.get("StreamMixNotifyUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveCallbackTemplateResponse(AbstractModel):
    """CreateLiveCallbackTemplate response structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class CreateLiveCertRequest(AbstractModel):
    """CreateLiveCert request structure.

    """

    def __init__(self):
        r"""
        :param CertType: Certificate type. 0: user-added certificate, 1: Tencent Cloud-hosted certificate.
Note: if the certificate type is 0, `HttpsCrt` and `HttpsKey` are required;
If the certificate type is 1, the certificate corresponding to `CloudCertId` will be used first. If `CloudCertId` is empty, `HttpsCrt` and `HttpsKey` will be used.
        :type CertType: int
        :param CertName: Certificate name.
        :type CertName: str
        :param HttpsCrt: Certificate content, i.e., public key.
        :type HttpsCrt: str
        :param HttpsKey: Private key.
        :type HttpsKey: str
        :param Description: Description.
        :type Description: str
        :param CloudCertId: Tencent Cloud-hosted certificate ID.
        :type CloudCertId: str
        """
        self.CertType = None
        self.CertName = None
        self.HttpsCrt = None
        self.HttpsKey = None
        self.Description = None
        self.CloudCertId = None


    def _deserialize(self, params):
        self.CertType = params.get("CertType")
        self.CertName = params.get("CertName")
        self.HttpsCrt = params.get("HttpsCrt")
        self.HttpsKey = params.get("HttpsKey")
        self.Description = params.get("Description")
        self.CloudCertId = params.get("CloudCertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveCertResponse(AbstractModel):
    """CreateLiveCert response structure.

    """

    def __init__(self):
        r"""
        :param CertId: Certificate ID
        :type CertId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CertId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.RequestId = params.get("RequestId")


class CreateLivePullStreamTaskRequest(AbstractModel):
    """CreateLivePullStreamTask request structure.

    """

    def __init__(self):
        r"""
        :param SourceType: The source type. Valid values:
PullLivePushLive: Live streaming
PullVodPushLive: Video files
        :type SourceType: str
        :param SourceUrls: The source URL(s).
If `SourceType` is `PullLivePushLive`, you can specify only one source URL.
If `SourceType` is `PullVodPushLive`, you can specify at most 30 source URLs.
Supported file formats: FLV, MP4, HLS.
Supported protocols: HTTP, HTTPS, RTMP, RTMPS, RTSP, SRT.
Notes:
1. We recommend you use FLV files as the source. Poorly interleaved MP4 files may result in playback stuttering. You can also re-interleave your MP4 files before adding them as the source.
2. Do not use private network domains or malicious URLs. CSS will block accounts that do.
3. To avoid push and playback issues, make sure the source files are properly interleaved.
4. Supported video coding formats: H.264, H.265.
5. Supported audio coding format: AAC.
6. Use small video files, preferably not longer than one hour. Large files may take a long time to load or resume after pause. Relay may fail if the time consumed exceeds 15 seconds.
        :type SourceUrls: list of str
        :param DomainName: The push domain name.
The pulled stream is pushed to this domain.
Use a push domain you have added in the CSS console.
        :type DomainName: str
        :param AppName: The application to push to.
The pulled stream is pushed to this application.
        :type AppName: str
        :param StreamName: The stream name.
The pulled stream is pushed under this name.
        :type StreamName: str
        :param StartTime: The start time.
It must be in UTC format.
Example: 2019-01-08T10:00:00Z.
Note: Beijing time is 8 hours ahead of UTC. The [ISO 8601 format](https://intl.cloud.tencent.com/document/product/266/11732#iso-date-format) is used.
        :type StartTime: str
        :param EndTime: The end time. Notes:
1. The end time must be later than the start time.
2. The end time and start time must be later than the current time.
3. The end time and start time must be less than seven days apart.
It must be in UTC format.
Example: 2019-01-08T10:00:00Z.
Note: Beijing time is 8 hours ahead of UTC. The [ISO 8601 format](https://intl.cloud.tencent.com/document/product/266/11732#iso-date-format) is used.
        :type EndTime: str
        :param Operator: The operator.
        :type Operator: str
        :param PushArgs: The push parameter.
This is a custom parameter carried during push.
Example:
bak=1&test=2
        :type PushArgs: str
        :param CallbackEvents: The events to listen for. If you do not pass this parameter, all events will be listened for.
TaskStart: Callback for starting a task
TaskExit: Callback for ending a task
VodSourceFileStart: Callback for starting to pull from video files
VodSourceFileFinish: Callback for stopping pulling from video files
ResetTaskConfig: Callback for modifying a task

`TaskAlarm` indicates a warning event. `AlarmType` examples:
PullFileUnstable: Pull from video files is unstable.
PushStreamUnstable: Push is unstable.
PullFileFailed: Error pulling from video files.
PushStreamFailed: Push error.
FileEndEarly: The video file ended prematurely.
        :type CallbackEvents: list of str
        :param VodLoopTimes: The number of times to loop video files. Default value: -1.
-1: Loop indefinitely
0: Do not loop
> 0: The number of loop times. A task will end either when the videos are looped for the specified number of times or at the specified task end time, whichever is earlier.
This parameter is valid only when the source is video files.
        :type VodLoopTimes: str
        :param VodRefreshType: The behavior after the source video files (`SourceUrls`) are changed.
ImmediateNewSource: Play the new videos immediately
ContinueBreakPoint: Play the new videos after the current video is finished playing (the remaining videos in the old playlist will not be played).

This parameter is valid only if the source before the change is video files.
        :type VodRefreshType: str
        :param CallbackUrl: A custom callback URL.
Callbacks about pull and relay events will be sent to this URL.
        :type CallbackUrl: str
        :param ExtraCmd: Other parameters.
For example, you can use `ignore_region` to ignore the region passed in and assign a region based on load distribution.
        :type ExtraCmd: str
        :param Comment: The remarks for a task, not longer than 512 bytes.
        :type Comment: str
        :param ToUrl: The complete destination URL.
If you specify this parameter, make sure you pass in an empty string for `DomainName`, `AppName`, and `StreamName`.

Note: Make sure that the expiration time of the signature is later than the task end time.
        :type ToUrl: str
        :param BackupSourceType: The backup source type.
PullLivePushLive: Live streaming
PullVodPushLive: Video files
Notes:
1. Backup sources are supported only if the primary source type is live streaming.
2. When pull from the primary source is interrupted, the system will pull from the backup source.
3. If the backup source is a video file, each time the video is finished, the system will check if the primary source is recovered and will switch back if it is.
        :type BackupSourceType: str
        :param BackupSourceUrl: The URL of the backup source.
You can specify only one backup source URL.
        :type BackupSourceUrl: str
        """
        self.SourceType = None
        self.SourceUrls = None
        self.DomainName = None
        self.AppName = None
        self.StreamName = None
        self.StartTime = None
        self.EndTime = None
        self.Operator = None
        self.PushArgs = None
        self.CallbackEvents = None
        self.VodLoopTimes = None
        self.VodRefreshType = None
        self.CallbackUrl = None
        self.ExtraCmd = None
        self.Comment = None
        self.ToUrl = None
        self.BackupSourceType = None
        self.BackupSourceUrl = None


    def _deserialize(self, params):
        self.SourceType = params.get("SourceType")
        self.SourceUrls = params.get("SourceUrls")
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Operator = params.get("Operator")
        self.PushArgs = params.get("PushArgs")
        self.CallbackEvents = params.get("CallbackEvents")
        self.VodLoopTimes = params.get("VodLoopTimes")
        self.VodRefreshType = params.get("VodRefreshType")
        self.CallbackUrl = params.get("CallbackUrl")
        self.ExtraCmd = params.get("ExtraCmd")
        self.Comment = params.get("Comment")
        self.ToUrl = params.get("ToUrl")
        self.BackupSourceType = params.get("BackupSourceType")
        self.BackupSourceUrl = params.get("BackupSourceUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLivePullStreamTaskResponse(AbstractModel):
    """CreateLivePullStreamTask response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: The task ID.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateLiveRecordRequest(AbstractModel):
    """CreateLiveRecord request structure.

    """

    def __init__(self):
        r"""
        :param StreamName: Stream name.
        :type StreamName: str
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.
        :type AppName: str
        :param DomainName: Push domain name. This parameter must be set for multi-domain name push.
        :type DomainName: str
        :param StartTime: Recording start time, which is China standard time and should be URL-encoded (RFC3986). For example, the encoding of 2017-01-01 10:10:01 is 2017-01-01+10%3a10%3a01.
In scheduled recording mode, this field must be set; in real-time video recording mode, this field is ignored.
        :type StartTime: str
        :param EndTime: Recording end time, which is China standard time and should be URL-encoded (RFC3986). For example, the encoding of 2017-01-01 10:30:01 is 2017-01-01+10%3a30%3a01.
In scheduled recording mode, this field must be set; in real-time video recording mode, this field is optional. If the recording is set to real-time video recording mode through the `Highlight` parameter, the set end time should not be more than 30 minutes after the current time. If the set end time is more than 30 minutes after the current time, earlier than the current time, or left empty, the actual end time will be 30 minutes after the current time.
        :type EndTime: str
        :param RecordType: Recording type.
"video": Audio-video recording **(default)**.
"audio": audio recording.
In both scheduled and real-time video recording modes, this parameter is valid and is not case sensitive.
        :type RecordType: str
        :param FileFormat: Recording file format. Valid values:
"flv" **(default)**, "hls", "mp4", "aac", "mp3".
In both scheduled and real-time video recording modes, this parameter is valid and is not case sensitive.
        :type FileFormat: str
        :param Highlight: Mark for enabling real-time video recording mode.
0: Real-time video recording mode is not enabled, i.e., the scheduled recording mode is used **(default)**. See [Sample 1](#.E7.A4.BA.E4.BE.8B1-.E5.88.9B.E5.BB.BA.E5.AE.9A.E6.97.B6.E5.BD.95.E5.88.B6.E4.BB.BB.E5.8A.A1).
1: Real-time video recording mode is enabled. See [Sample 2](#.E7.A4.BA.E4.BE.8B2-.E5.88.9B.E5.BB.BA.E5.AE.9E.E6.97.B6.E5.BD.95.E5.88.B6.E4.BB.BB.E5.8A.A1).
        :type Highlight: int
        :param MixStream: Flag for enabling A+B=C mixed stream recording.
0: A+B=C mixed stream recording is not enabled **(default)**.
1: A+B=C mixed stream recording is enabled.
In both scheduled and real-time video recording modes, this parameter is valid.
        :type MixStream: int
        :param StreamParam: Recording stream parameter. The following parameters are supported currently:
record_interval: recording interval in seconds. Value range: 1800-7200.
storage_time: recording file storage duration in seconds.
Example: record_interval=3600&storage_time=2592000.
Note: the parameter needs to be URL-encoded.
In both scheduled and real-time video recording modes, this parameter is valid.
        :type StreamParam: str
        """
        self.StreamName = None
        self.AppName = None
        self.DomainName = None
        self.StartTime = None
        self.EndTime = None
        self.RecordType = None
        self.FileFormat = None
        self.Highlight = None
        self.MixStream = None
        self.StreamParam = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RecordType = params.get("RecordType")
        self.FileFormat = params.get("FileFormat")
        self.Highlight = params.get("Highlight")
        self.MixStream = params.get("MixStream")
        self.StreamParam = params.get("StreamParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveRecordResponse(AbstractModel):
    """CreateLiveRecord response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Task ID, which uniquely identifies a recording task globally.
        :type TaskId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateLiveRecordRuleRequest(AbstractModel):
    """CreateLiveRecordRule request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Push domain name.
        :type DomainName: str
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.
        :type AppName: str
        :param StreamName: Stream name.
Note: If the parameter is a non-empty string, the rule will be only applicable to the particular stream.
        :type StreamName: str
        """
        self.DomainName = None
        self.TemplateId = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.TemplateId = params.get("TemplateId")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveRecordRuleResponse(AbstractModel):
    """CreateLiveRecordRule response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLiveRecordTemplateRequest(AbstractModel):
    """CreateLiveRecordTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateName: Template name. Only letters, digits, underscores, and hyphens can be contained.
        :type TemplateName: str
        :param Description: Message description
        :type Description: str
        :param FlvParam: FLV recording parameter, which is set when FLV recording is enabled.
        :type FlvParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param HlsParam: HLS recording parameter, which is set when HLS recording is enabled.
        :type HlsParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param Mp4Param: Mp4 recording parameter, which is set when Mp4 recording is enabled.
        :type Mp4Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param AacParam: AAC recording parameter, which is set when AAC recording is enabled.
        :type AacParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param IsDelayLive: LVB type. Default value: 0.
0: LVB.
1: LCB.
        :type IsDelayLive: int
        :param HlsSpecialParam: HLS-specific recording parameter.
        :type HlsSpecialParam: :class:`tencentcloud.live.v20180801.models.HlsSpecialParam`
        :param Mp3Param: Mp3 recording parameter, which is set when Mp3 recording is enabled.
        :type Mp3Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param RemoveWatermark: Whether to remove the watermark. This parameter is invalid if `IsDelayLive` is `1`.
        :type RemoveWatermark: bool
        :param FlvSpecialParam: A special parameter for FLV recording.
        :type FlvSpecialParam: :class:`tencentcloud.live.v20180801.models.FlvSpecialParam`
        """
        self.TemplateName = None
        self.Description = None
        self.FlvParam = None
        self.HlsParam = None
        self.Mp4Param = None
        self.AacParam = None
        self.IsDelayLive = None
        self.HlsSpecialParam = None
        self.Mp3Param = None
        self.RemoveWatermark = None
        self.FlvSpecialParam = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        if params.get("FlvParam") is not None:
            self.FlvParam = RecordParam()
            self.FlvParam._deserialize(params.get("FlvParam"))
        if params.get("HlsParam") is not None:
            self.HlsParam = RecordParam()
            self.HlsParam._deserialize(params.get("HlsParam"))
        if params.get("Mp4Param") is not None:
            self.Mp4Param = RecordParam()
            self.Mp4Param._deserialize(params.get("Mp4Param"))
        if params.get("AacParam") is not None:
            self.AacParam = RecordParam()
            self.AacParam._deserialize(params.get("AacParam"))
        self.IsDelayLive = params.get("IsDelayLive")
        if params.get("HlsSpecialParam") is not None:
            self.HlsSpecialParam = HlsSpecialParam()
            self.HlsSpecialParam._deserialize(params.get("HlsSpecialParam"))
        if params.get("Mp3Param") is not None:
            self.Mp3Param = RecordParam()
            self.Mp3Param._deserialize(params.get("Mp3Param"))
        self.RemoveWatermark = params.get("RemoveWatermark")
        if params.get("FlvSpecialParam") is not None:
            self.FlvSpecialParam = FlvSpecialParam()
            self.FlvSpecialParam._deserialize(params.get("FlvSpecialParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveRecordTemplateResponse(AbstractModel):
    """CreateLiveRecordTemplate response structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class CreateLiveSnapshotRuleRequest(AbstractModel):
    """CreateLiveSnapshotRule request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Push domain name.
        :type DomainName: str
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.
        :type AppName: str
        :param StreamName: Stream name.
Note: if this parameter is a non-empty string, the rule will take effect only for the particular stream.
        :type StreamName: str
        """
        self.DomainName = None
        self.TemplateId = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.TemplateId = params.get("TemplateId")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveSnapshotRuleResponse(AbstractModel):
    """CreateLiveSnapshotRule response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLiveSnapshotTemplateRequest(AbstractModel):
    """CreateLiveSnapshotTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateName: Template name.
Maximum length: 255 bytes.
Only letters, digits, underscores, and hyphens can be contained.
        :type TemplateName: str
        :param CosAppId: COS application ID.
        :type CosAppId: int
        :param CosBucket: COS bucket name.
Note: the value of `CosBucket` cannot contain `-[appid]`.
        :type CosBucket: str
        :param CosRegion: COS region.
        :type CosRegion: str
        :param Description: Description.
Maximum length: 1,024 bytes.
Only letters, digits, underscores, and hyphens can be contained.
        :type Description: str
        :param SnapshotInterval: Screencapturing interval (s). Default value: 10
Value range: 2-300
        :type SnapshotInterval: int
        :param Width: Screenshot width. Default value: `0` (original width)
Value range: 0-3000
        :type Width: int
        :param Height: Screenshot height. Default value: `0` (original height)
Value range: 0-2000
        :type Height: int
        :param PornFlag: Whether to enable porn detection. 0: no, 1: yes. Default value: 0
        :type PornFlag: int
        :param CosPrefix: COS Bucket folder prefix.
If no value is entered, the default value
`/{Year}-{Month}-{Day}`
will be used.
        :type CosPrefix: str
        :param CosFileName: COS filename.
If no value is entered, the default value 
`{StreamID}-screenshot-{Hour}-{Minute}-{Second}-{Width}x{Height}{Ext}`
will be used.
        :type CosFileName: str
        """
        self.TemplateName = None
        self.CosAppId = None
        self.CosBucket = None
        self.CosRegion = None
        self.Description = None
        self.SnapshotInterval = None
        self.Width = None
        self.Height = None
        self.PornFlag = None
        self.CosPrefix = None
        self.CosFileName = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        self.CosAppId = params.get("CosAppId")
        self.CosBucket = params.get("CosBucket")
        self.CosRegion = params.get("CosRegion")
        self.Description = params.get("Description")
        self.SnapshotInterval = params.get("SnapshotInterval")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.PornFlag = params.get("PornFlag")
        self.CosPrefix = params.get("CosPrefix")
        self.CosFileName = params.get("CosFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveSnapshotTemplateResponse(AbstractModel):
    """CreateLiveSnapshotTemplate response structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class CreateLiveTranscodeRuleRequest(AbstractModel):
    """CreateLiveTranscodeRule request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Playback domain name.
        :type DomainName: str
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default. If you only bind a domain name, leave this parameter empty.
        :type AppName: str
        :param StreamName: Stream name. If only the domain name or path is bound, leave this parameter blank.
        :type StreamName: str
        :param TemplateId: Designates an existing template ID.
        :type TemplateId: int
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveTranscodeRuleResponse(AbstractModel):
    """CreateLiveTranscodeRule response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLiveTranscodeTemplateRequest(AbstractModel):
    """CreateLiveTranscodeTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateName: Template name, such as “900p”. This can be only a combination of letters and digits.
Length limit:
  Standard transcoding: 1-10 characters
  Top speed codec transcoding: 3-10 characters
        :type TemplateName: str
        :param VideoBitrate: Video bitrate in Kbps. Value range: 100-8000.
Note: the transcoding template requires that the bitrate be unique. Therefore, the final saved bitrate may be different from the input bitrate.
        :type VideoBitrate: int
        :param Acodec: Audio codec. Default value: aac.
Note: this parameter is unsupported now.
        :type Acodec: str
        :param AudioBitrate: Audio bitrate. Default value: 0.
Value range: 0-500.
        :type AudioBitrate: int
        :param Vcodec: Video codec. Valid values: h264, h265, origin (default)

origin: original codec as the output codec
        :type Vcodec: str
        :param Description: Template description.
        :type Description: str
        :param NeedVideo: Whether to keep the video. 0: no; 1: yes. Default value: 1.
        :type NeedVideo: int
        :param Width: Width. Default value: 0.
Value range: 0-3000
It must be a multiple of 2. The original width is 0.
        :type Width: int
        :param NeedAudio: Whether to keep the audio. 0: no; 1: yes. Default value: 1.
        :type NeedAudio: int
        :param Height: Height. Default value: 0
Value range: 0-3000
The value must be a multiple of 2. The original height is `0`.
This parameter is required for a top speed codec template (when `AiTransCode` is `1`).
        :type Height: int
        :param Fps: Frame rate. Default value: 0.
Value range: 0-60
        :type Fps: int
        :param Gop: Keyframe interval in seconds. Default value: original interval
Value range: 2-6
        :type Gop: int
        :param Rotate: Rotation angle. Default value: 0.
Valid values: 0, 90, 180, 270
        :type Rotate: int
        :param Profile: Encoding quality:
baseline/main/high. Default value: baseline.
        :type Profile: str
        :param BitrateToOrig: Whether to use the original bitrate when the set bitrate is larger than the original bitrate.
0: no, 1: yes
Default value: 0.
        :type BitrateToOrig: int
        :param HeightToOrig: Whether to use the original height when the set height is higher than the original height.
0: no, 1: yes
Default value: 0.
        :type HeightToOrig: int
        :param FpsToOrig: Whether to use the original frame rate when the set frame rate is larger than the original frame rate.
0: no, 1: yes
Default value: 0.
        :type FpsToOrig: int
        :param AiTransCode: Whether it is a top speed codec template. 0: no, 1: yes. Default value: 0.
        :type AiTransCode: int
        :param AdaptBitratePercent: Bitrate compression ratio of top speed codec video.
Target bitrate of top speed code = VideoBitrate * (1-AdaptBitratePercent)

Value range: 0.0-0.5.
        :type AdaptBitratePercent: float
        :param ShortEdgeAsHeight: Whether to use the short side as the video height. 0: no, 1: yes. Default value: 0.
        :type ShortEdgeAsHeight: int
        :param DRMType: The DRM encryption type. Valid values: fairplay, normalaes, widevine.
If you do not pass this parameter or pass in an empty string, the existing configuration will be reset.
        :type DRMType: str
        :param DRMTracks: The tracks to encrypt. Valid values: AUDIO, SD, HD, UHD1, UHD2. You can choose only one video track (SD, HD, UHD1, or UHD2).
If you do not pass this parameter or pass in an empty string, the existing configuration will be reset.
        :type DRMTracks: str
        """
        self.TemplateName = None
        self.VideoBitrate = None
        self.Acodec = None
        self.AudioBitrate = None
        self.Vcodec = None
        self.Description = None
        self.NeedVideo = None
        self.Width = None
        self.NeedAudio = None
        self.Height = None
        self.Fps = None
        self.Gop = None
        self.Rotate = None
        self.Profile = None
        self.BitrateToOrig = None
        self.HeightToOrig = None
        self.FpsToOrig = None
        self.AiTransCode = None
        self.AdaptBitratePercent = None
        self.ShortEdgeAsHeight = None
        self.DRMType = None
        self.DRMTracks = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        self.VideoBitrate = params.get("VideoBitrate")
        self.Acodec = params.get("Acodec")
        self.AudioBitrate = params.get("AudioBitrate")
        self.Vcodec = params.get("Vcodec")
        self.Description = params.get("Description")
        self.NeedVideo = params.get("NeedVideo")
        self.Width = params.get("Width")
        self.NeedAudio = params.get("NeedAudio")
        self.Height = params.get("Height")
        self.Fps = params.get("Fps")
        self.Gop = params.get("Gop")
        self.Rotate = params.get("Rotate")
        self.Profile = params.get("Profile")
        self.BitrateToOrig = params.get("BitrateToOrig")
        self.HeightToOrig = params.get("HeightToOrig")
        self.FpsToOrig = params.get("FpsToOrig")
        self.AiTransCode = params.get("AiTransCode")
        self.AdaptBitratePercent = params.get("AdaptBitratePercent")
        self.ShortEdgeAsHeight = params.get("ShortEdgeAsHeight")
        self.DRMType = params.get("DRMType")
        self.DRMTracks = params.get("DRMTracks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveTranscodeTemplateResponse(AbstractModel):
    """CreateLiveTranscodeTemplate response structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class CreateLiveWatermarkRuleRequest(AbstractModel):
    """CreateLiveWatermarkRule request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Push domain name.
        :type DomainName: str
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.
        :type AppName: str
        :param StreamName: Stream name.
        :type StreamName: str
        :param TemplateId: Watermark ID, which is the `WatermarkId` returned by the [AddLiveWatermark](https://intl.cloud.tencent.com/document/product/267/30154?from_cn_redirect=1) API.
        :type TemplateId: int
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLiveWatermarkRuleResponse(AbstractModel):
    """CreateLiveWatermarkRule response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateRecordTaskRequest(AbstractModel):
    """CreateRecordTask request structure.

    """

    def __init__(self):
        r"""
        :param StreamName: Stream name.
        :type StreamName: str
        :param DomainName: Push domain name.
        :type DomainName: str
        :param AppName: Push path.
        :type AppName: str
        :param EndTime: Recording end time in UNIX timestamp format. `EndTime` should be later than `StartTime` and the current time, and the duration between `EndTime` and `StartTime` is up to 24 hours.
        :type EndTime: int
        :param StartTime: Recording start time in UNIX timestamp format. Leaving this parameter empty means starting recording now. `StartTime` cannot be later than the current time plus 6 days.
        :type StartTime: int
        :param StreamType: Push type. Default value: 0. Valid values:
0: LVB push.
1: mixed stream, i.e., A + B = C mixed stream.
        :type StreamType: int
        :param TemplateId: Recording template ID, which is the returned value of `CreateLiveRecordTemplate`. If this parameter is left empty or incorrect, the stream will be recorded in HLS format and retained permanently by default.
        :type TemplateId: int
        :param Extension: Extension field which is not defined now. It is empty by default.
        :type Extension: str
        """
        self.StreamName = None
        self.DomainName = None
        self.AppName = None
        self.EndTime = None
        self.StartTime = None
        self.StreamType = None
        self.TemplateId = None
        self.Extension = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.StreamType = params.get("StreamType")
        self.TemplateId = params.get("TemplateId")
        self.Extension = params.get("Extension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRecordTaskResponse(AbstractModel):
    """CreateRecordTask response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: A globally unique task ID. If `TaskId` is returned, the recording task has been successfully created.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DayStreamPlayInfo(AbstractModel):
    """Stream playback information

    """

    def __init__(self):
        r"""
        :param Time: Data point in time in the format of `yyyy-mm-dd HH:MM:SS`.
        :type Time: str
        :param Bandwidth: Bandwidth in Mbps.
        :type Bandwidth: float
        :param Flux: Traffic in MB.
        :type Flux: float
        :param Request: Number of requests.
        :type Request: int
        :param Online: Number of online viewers.
        :type Online: int
        """
        self.Time = None
        self.Bandwidth = None
        self.Flux = None
        self.Request = None
        self.Online = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Bandwidth = params.get("Bandwidth")
        self.Flux = params.get("Flux")
        self.Request = params.get("Request")
        self.Online = params.get("Online")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DelayInfo(AbstractModel):
    """Delayed playback information.

    """

    def __init__(self):
        r"""
        :param DomainName: Push domain name.
        :type DomainName: str
        :param AppName: Push path, which is the same as the 
 `AppName` in push and playback addresses and is `live` by default.
        :type AppName: str
        :param StreamName: Stream name.
        :type StreamName: str
        :param DelayInterval: Delay time in seconds.
        :type DelayInterval: int
        :param CreateTime: Creation time in UTC time.
Note: the difference between UTC time and Beijing time is 8 hours.
Example: 2019-06-18T12:00:00Z (i.e., June 18, 2019 20:00:00 Beijing time).
        :type CreateTime: str
        :param ExpireTime: Expiration time in UTC time.
Note: the difference between UTC time and Beijing time is 8 hours.
Example: 2019-06-18T12:00:00Z (i.e., June 18, 2019 20:00:00 Beijing time).
        :type ExpireTime: str
        :param Status: Current status:
-1: expired.
1: in effect.
        :type Status: int
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None
        self.DelayInterval = None
        self.CreateTime = None
        self.ExpireTime = None
        self.Status = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.DelayInterval = params.get("DelayInterval")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveCallbackRuleRequest(AbstractModel):
    """DeleteLiveCallbackRule request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Push domain name.
        :type DomainName: str
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.
        :type AppName: str
        """
        self.DomainName = None
        self.AppName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveCallbackRuleResponse(AbstractModel):
    """DeleteLiveCallbackRule response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveCallbackTemplateRequest(AbstractModel):
    """DeleteLiveCallbackTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID.
1. Get the template ID in the returned value of the [CreateLiveCallbackTemplate](https://intl.cloud.tencent.com/document/product/267/32637?from_cn_redirect=1) API call.
2. You can query the list of created templates through the [DescribeLiveCallbackTemplates](https://intl.cloud.tencent.com/document/product/267/32632?from_cn_redirect=1) API.
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveCallbackTemplateResponse(AbstractModel):
    """DeleteLiveCallbackTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveCertRequest(AbstractModel):
    """DeleteLiveCert request structure.

    """

    def __init__(self):
        r"""
        :param CertId: Certificate ID obtained through the `DescribeLiveCerts` API.
        :type CertId: int
        """
        self.CertId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveCertResponse(AbstractModel):
    """DeleteLiveCert response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveDomainRequest(AbstractModel):
    """DeleteLiveDomain request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Domain name to be deleted.
        :type DomainName: str
        :param DomainType: Type. 0: push, 1: playback.
        :type DomainType: int
        """
        self.DomainName = None
        self.DomainType = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.DomainType = params.get("DomainType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveDomainResponse(AbstractModel):
    """DeleteLiveDomain response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLivePullStreamTaskRequest(AbstractModel):
    """DeleteLivePullStreamTask request structure.

    """

    def __init__(self):
        r"""
        :param TaskId: The task ID.
        :type TaskId: str
        :param Operator: The operator.
        :type Operator: str
        """
        self.TaskId = None
        self.Operator = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLivePullStreamTaskResponse(AbstractModel):
    """DeleteLivePullStreamTask response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveRecordRequest(AbstractModel):
    """DeleteLiveRecord request structure.

    """

    def __init__(self):
        r"""
        :param StreamName: Stream name.
        :type StreamName: str
        :param TaskId: Task ID returned by the `CreateLiveRecord` API.
        :type TaskId: int
        """
        self.StreamName = None
        self.TaskId = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveRecordResponse(AbstractModel):
    """DeleteLiveRecord response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveRecordRuleRequest(AbstractModel):
    """DeleteLiveRecordRule request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Push domain name.
Domain name+AppName+StreamName uniquely identifies a single transcoding rule. If you need to delete it, strong match is required. For example, even if AppName is blank, you need to pass in a blank string to make a strong match.
        :type DomainName: str
        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.
Domain name+AppName+StreamName uniquely identifies a single transcoding rule. If you need to delete it, strong match is required. For example, even if AppName is blank, you need to pass in a blank string to make a strong match.
        :type AppName: str
        :param StreamName: Stream name.
Domain name+AppName+StreamName uniquely identifies a single transcoding rule. If you need to delete it, strong match is required. For example, even if AppName is blank, you need to pass in a blank string to make a strong match.
        :type StreamName: str
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveRecordRuleResponse(AbstractModel):
    """DeleteLiveRecordRule response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveRecordTemplateRequest(AbstractModel):
    """DeleteLiveRecordTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID obtained through the `DescribeRecordTemplates` API.
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveRecordTemplateResponse(AbstractModel):
    """DeleteLiveRecordTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveSnapshotRuleRequest(AbstractModel):
    """DeleteLiveSnapshotRule request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Push domain name.
        :type DomainName: str
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.
        :type AppName: str
        :param StreamName: Stream name.
        :type StreamName: str
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveSnapshotRuleResponse(AbstractModel):
    """DeleteLiveSnapshotRule response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveSnapshotTemplateRequest(AbstractModel):
    """DeleteLiveSnapshotTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID.
1. Get from the returned value of the [CreateLiveSnapshotTemplate](https://intl.cloud.tencent.com/document/product/267/32624?from_cn_redirect=1) API call.
2. You can query the list of created screencapturing templates through the [DescribeLiveSnapshotTemplates](https://intl.cloud.tencent.com/document/product/267/32619?from_cn_redirect=1) API.
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveSnapshotTemplateResponse(AbstractModel):
    """DeleteLiveSnapshotTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveTranscodeRuleRequest(AbstractModel):
    """DeleteLiveTranscodeRule request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Playback domain name.
        :type DomainName: str
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.
        :type AppName: str
        :param StreamName: Stream name.
        :type StreamName: str
        :param TemplateId: Template ID.
        :type TemplateId: int
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveTranscodeRuleResponse(AbstractModel):
    """DeleteLiveTranscodeRule response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveTranscodeTemplateRequest(AbstractModel):
    """DeleteLiveTranscodeTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID.
1. Get the template ID in the returned value of the [CreateLiveTranscodeTemplate](https://intl.cloud.tencent.com/document/product/267/32646?from_cn_redirect=1) API call.
2. You can query the list of created templates through the [DescribeLiveTranscodeTemplates](https://intl.cloud.tencent.com/document/product/267/32641?from_cn_redirect=1) API.
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveTranscodeTemplateResponse(AbstractModel):
    """DeleteLiveTranscodeTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveWatermarkRequest(AbstractModel):
    """DeleteLiveWatermark request structure.

    """

    def __init__(self):
        r"""
        :param WatermarkId: Watermark ID.
Watermark ID obtained in the returned value of the [AddLiveWatermark](https://intl.cloud.tencent.com/document/product/267/30154?from_cn_redirect=1) API call.
Watermark ID returned by the `DescribeLiveWatermarks` API.
        :type WatermarkId: int
        """
        self.WatermarkId = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveWatermarkResponse(AbstractModel):
    """DeleteLiveWatermark response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveWatermarkRuleRequest(AbstractModel):
    """DeleteLiveWatermarkRule request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Push domain name.
        :type DomainName: str
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.
        :type AppName: str
        :param StreamName: Stream name.
        :type StreamName: str
        """
        self.DomainName = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLiveWatermarkRuleResponse(AbstractModel):
    """DeleteLiveWatermarkRule response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRecordTaskRequest(AbstractModel):
    """DeleteRecordTask request structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Task ID returned by `CreateRecordTask`. The recording task specified by `TaskId` will be deleted.
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRecordTaskResponse(AbstractModel):
    """DeleteRecordTask response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeConcurrentRecordStreamNumRequest(AbstractModel):
    """DescribeConcurrentRecordStreamNum request structure.

    """

    def __init__(self):
        r"""
        :param LiveType: Live streaming type. SlowLive: LCB.
NormalLive: LVB.
        :type LiveType: str
        :param StartTime: Start time in the format of `yyyy-mm-dd HH:MM:SS`.
Data for the last 180 days can be queried.
        :type StartTime: str
        :param EndTime: End time in the format of `yyyy-mm-dd HH:MM:SS`.
The maximum time span supported is 31 days.
        :type EndTime: str
        :param MainlandOrOversea: Valid values: Mainland (data for Mainland China), Oversea (data for regions outside Mainland China). If this parameter is left empty, data for all regions will be queried.
        :type MainlandOrOversea: str
        :param PushDomains: Playback domain name list. If this parameter is left empty, full data will be queried.
        :type PushDomains: list of str
        """
        self.LiveType = None
        self.StartTime = None
        self.EndTime = None
        self.MainlandOrOversea = None
        self.PushDomains = None


    def _deserialize(self, params):
        self.LiveType = params.get("LiveType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.PushDomains = params.get("PushDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConcurrentRecordStreamNumResponse(AbstractModel):
    """DescribeConcurrentRecordStreamNum response structure.

    """

    def __init__(self):
        r"""
        :param DataInfoList: Statistics list.
        :type DataInfoList: list of ConcurrentRecordStreamNum
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = ConcurrentRecordStreamNum()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDeliverBandwidthListRequest(AbstractModel):
    """DescribeDeliverBandwidthList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time in the format of "%Y-%m-%d %H:%M:%S".
        :type StartTime: str
        :param EndTime: End time in the format of "%Y-%m-%d %H:%M:%S". Data in the last 3 months can be queried, and the query period is up to 1 month.
        :type EndTime: str
        """
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeliverBandwidthListResponse(AbstractModel):
    """DescribeDeliverBandwidthList response structure.

    """

    def __init__(self):
        r"""
        :param DataInfoList: Billable bandwidth of live stream relaying.
        :type DataInfoList: list of BandwidthInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = BandwidthInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeGroupProIspPlayInfoListRequest(AbstractModel):
    """DescribeGroupProIspPlayInfoList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time point in the format of `yyyy-mm-dd HH:MM:SS`.
        :type StartTime: str
        :param EndTime: End time point in the format of `yyyy-mm-dd HH:MM:SS`
The time span is (0,3 hours]. Data for the last month can be queried.
        :type EndTime: str
        :param PlayDomains: Playback domain name. If this parameter is left empty, full data will be queried.
        :type PlayDomains: list of str
        :param ProvinceNames: District list. If this parameter is left empty, data for all districts will be returned.
        :type ProvinceNames: list of str
        :param IspNames: ISP list. If this parameter is left empty, data of all ISPs will be returned.
        :type IspNames: list of str
        :param MainlandOrOversea: Within or outside Mainland China. Valid values: Mainland (data for Mainland China), Oversea (data for regions outside Mainland China). If this parameter is left empty, data for all regions will be queried.
        :type MainlandOrOversea: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomains = None
        self.ProvinceNames = None
        self.IspNames = None
        self.MainlandOrOversea = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomains = params.get("PlayDomains")
        self.ProvinceNames = params.get("ProvinceNames")
        self.IspNames = params.get("IspNames")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupProIspPlayInfoListResponse(AbstractModel):
    """DescribeGroupProIspPlayInfoList response structure.

    """

    def __init__(self):
        r"""
        :param DataInfoList: Data content.
        :type DataInfoList: list of GroupProIspDataInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = GroupProIspDataInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHttpStatusInfoListRequest(AbstractModel):
    """DescribeHttpStatusInfoList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time (Beijing time).
Format: yyyy-mm-dd HH:MM:SS.
        :type StartTime: str
        :param EndTime: End time (Beijing time).
Format: yyyy-mm-dd HH:MM:SS.
Note: data in the last 3 months can be queried and the query period is up to 1 day.
        :type EndTime: str
        :param PlayDomains: Playback domain name list.
        :type PlayDomains: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomains = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomains = params.get("PlayDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHttpStatusInfoListResponse(AbstractModel):
    """DescribeHttpStatusInfoList response structure.

    """

    def __init__(self):
        r"""
        :param DataInfoList: Playback status code list.
        :type DataInfoList: list of HttpStatusData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = HttpStatusData()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveCallbackRulesRequest(AbstractModel):
    """DescribeLiveCallbackRules request structure.

    """


class DescribeLiveCallbackRulesResponse(AbstractModel):
    """DescribeLiveCallbackRules response structure.

    """

    def __init__(self):
        r"""
        :param Rules: Rule information list.
        :type Rules: list of CallBackRuleInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = CallBackRuleInfo()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveCallbackTemplateRequest(AbstractModel):
    """DescribeLiveCallbackTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID.
1. Get the template ID in the returned value of the [CreateLiveCallbackTemplate](https://intl.cloud.tencent.com/document/product/267/32637?from_cn_redirect=1) API call.
2. You can query the list of created templates through the [DescribeLiveCallbackTemplates](https://intl.cloud.tencent.com/document/product/267/32632?from_cn_redirect=1) API.
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveCallbackTemplateResponse(AbstractModel):
    """DescribeLiveCallbackTemplate response structure.

    """

    def __init__(self):
        r"""
        :param Template: Callback template information.
        :type Template: :class:`tencentcloud.live.v20180801.models.CallBackTemplateInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = CallBackTemplateInfo()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")


class DescribeLiveCallbackTemplatesRequest(AbstractModel):
    """DescribeLiveCallbackTemplates request structure.

    """


class DescribeLiveCallbackTemplatesResponse(AbstractModel):
    """DescribeLiveCallbackTemplates response structure.

    """

    def __init__(self):
        r"""
        :param Templates: Template information list.
        :type Templates: list of CallBackTemplateInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Templates = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = CallBackTemplateInfo()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveCertRequest(AbstractModel):
    """DescribeLiveCert request structure.

    """

    def __init__(self):
        r"""
        :param CertId: Certificate ID obtained through the `DescribeLiveCerts` API.
        :type CertId: int
        """
        self.CertId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveCertResponse(AbstractModel):
    """DescribeLiveCert response structure.

    """

    def __init__(self):
        r"""
        :param CertInfo: Certificate information.
        :type CertInfo: :class:`tencentcloud.live.v20180801.models.CertInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CertInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CertInfo") is not None:
            self.CertInfo = CertInfo()
            self.CertInfo._deserialize(params.get("CertInfo"))
        self.RequestId = params.get("RequestId")


class DescribeLiveCertsRequest(AbstractModel):
    """DescribeLiveCerts request structure.

    """


class DescribeLiveCertsResponse(AbstractModel):
    """DescribeLiveCerts response structure.

    """

    def __init__(self):
        r"""
        :param CertInfoSet: Certificate information list.
        :type CertInfoSet: list of CertInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CertInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CertInfoSet") is not None:
            self.CertInfoSet = []
            for item in params.get("CertInfoSet"):
                obj = CertInfo()
                obj._deserialize(item)
                self.CertInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveDelayInfoListRequest(AbstractModel):
    """DescribeLiveDelayInfoList request structure.

    """


class DescribeLiveDelayInfoListResponse(AbstractModel):
    """DescribeLiveDelayInfoList response structure.

    """

    def __init__(self):
        r"""
        :param DelayInfoList: Delayed playback information list.
        :type DelayInfoList: list of DelayInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DelayInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DelayInfoList") is not None:
            self.DelayInfoList = []
            for item in params.get("DelayInfoList"):
                obj = DelayInfo()
                obj._deserialize(item)
                self.DelayInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveDomainCertRequest(AbstractModel):
    """DescribeLiveDomainCert request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Playback domain name.
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveDomainCertResponse(AbstractModel):
    """DescribeLiveDomainCert response structure.

    """

    def __init__(self):
        r"""
        :param DomainCertInfo: Certificate information.
        :type DomainCertInfo: :class:`tencentcloud.live.v20180801.models.DomainCertInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DomainCertInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainCertInfo") is not None:
            self.DomainCertInfo = DomainCertInfo()
            self.DomainCertInfo._deserialize(params.get("DomainCertInfo"))
        self.RequestId = params.get("RequestId")


class DescribeLiveDomainRefererRequest(AbstractModel):
    """DescribeLiveDomainReferer request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Playback domain name
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveDomainRefererResponse(AbstractModel):
    """DescribeLiveDomainReferer response structure.

    """

    def __init__(self):
        r"""
        :param RefererAuthConfig: Referer allowlist/blocklist configuration of a domain name
        :type RefererAuthConfig: :class:`tencentcloud.live.v20180801.models.RefererAuthConfig`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RefererAuthConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RefererAuthConfig") is not None:
            self.RefererAuthConfig = RefererAuthConfig()
            self.RefererAuthConfig._deserialize(params.get("RefererAuthConfig"))
        self.RequestId = params.get("RequestId")


class DescribeLiveDomainRequest(AbstractModel):
    """DescribeLiveDomain request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Domain name.
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveDomainResponse(AbstractModel):
    """DescribeLiveDomain response structure.

    """

    def __init__(self):
        r"""
        :param DomainInfo: Domain name information.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type DomainInfo: :class:`tencentcloud.live.v20180801.models.DomainInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DomainInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainInfo") is not None:
            self.DomainInfo = DomainInfo()
            self.DomainInfo._deserialize(params.get("DomainInfo"))
        self.RequestId = params.get("RequestId")


class DescribeLiveDomainsRequest(AbstractModel):
    """DescribeLiveDomains request structure.

    """

    def __init__(self):
        r"""
        :param DomainStatus: Filter by domain name status. 0: disabled, 1: enabled.
        :type DomainStatus: int
        :param DomainType: Filter by domain name type. 0: push. 1: playback
        :type DomainType: int
        :param PageSize: Number of entries per page. Value range: 10-100. Default value: 10.
        :type PageSize: int
        :param PageNum: Page number to get. Value range: 1-100000. Default value: 1.
        :type PageNum: int
        :param IsDelayLive: 0: LVB, 1: LCB. Default value: 0.
        :type IsDelayLive: int
        :param DomainPrefix: Domain name prefix.
        :type DomainPrefix: str
        :param PlayType: Playback region. This parameter is valid only when `DomainType` is set to `1`.
`1`: Chinese mainland
`2`: global
`3`: outside Chinese mainland
        :type PlayType: int
        """
        self.DomainStatus = None
        self.DomainType = None
        self.PageSize = None
        self.PageNum = None
        self.IsDelayLive = None
        self.DomainPrefix = None
        self.PlayType = None


    def _deserialize(self, params):
        self.DomainStatus = params.get("DomainStatus")
        self.DomainType = params.get("DomainType")
        self.PageSize = params.get("PageSize")
        self.PageNum = params.get("PageNum")
        self.IsDelayLive = params.get("IsDelayLive")
        self.DomainPrefix = params.get("DomainPrefix")
        self.PlayType = params.get("PlayType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveDomainsResponse(AbstractModel):
    """DescribeLiveDomains response structure.

    """

    def __init__(self):
        r"""
        :param AllCount: Total number of results.
        :type AllCount: int
        :param DomainList: List of domain name details.
        :type DomainList: list of DomainInfo
        :param CreateLimitCount: The number of domain names that can be added
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CreateLimitCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AllCount = None
        self.DomainList = None
        self.CreateLimitCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AllCount = params.get("AllCount")
        if params.get("DomainList") is not None:
            self.DomainList = []
            for item in params.get("DomainList"):
                obj = DomainInfo()
                obj._deserialize(item)
                self.DomainList.append(obj)
        self.CreateLimitCount = params.get("CreateLimitCount")
        self.RequestId = params.get("RequestId")


class DescribeLiveForbidStreamListRequest(AbstractModel):
    """DescribeLiveForbidStreamList request structure.

    """

    def __init__(self):
        r"""
        :param PageNum: Page number to get. Default value: 1.
        :type PageNum: int
        :param PageSize: Number of entries per page. Maximum value: 100. 
Value: any integer between 1 and 100.
Default value: 10.
        :type PageSize: int
        :param StreamName: Stream name for query
        :type StreamName: str
        """
        self.PageNum = None
        self.PageSize = None
        self.StreamName = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveForbidStreamListResponse(AbstractModel):
    """DescribeLiveForbidStreamList response structure.

    """

    def __init__(self):
        r"""
        :param TotalNum: Total number of eligible ones.
        :type TotalNum: int
        :param TotalPage: Total number of pages.
        :type TotalPage: int
        :param PageNum: Page number.
        :type PageNum: int
        :param PageSize: Number of entries displayed per page.
        :type PageSize: int
        :param ForbidStreamList: List of forbidden streams.
        :type ForbidStreamList: list of ForbidStreamInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalNum = None
        self.TotalPage = None
        self.PageNum = None
        self.PageSize = None
        self.ForbidStreamList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        if params.get("ForbidStreamList") is not None:
            self.ForbidStreamList = []
            for item in params.get("ForbidStreamList"):
                obj = ForbidStreamInfo()
                obj._deserialize(item)
                self.ForbidStreamList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLivePlayAuthKeyRequest(AbstractModel):
    """DescribeLivePlayAuthKey request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Domain name.
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLivePlayAuthKeyResponse(AbstractModel):
    """DescribeLivePlayAuthKey response structure.

    """

    def __init__(self):
        r"""
        :param PlayAuthKeyInfo: Playback authentication key information.
        :type PlayAuthKeyInfo: :class:`tencentcloud.live.v20180801.models.PlayAuthKeyInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PlayAuthKeyInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlayAuthKeyInfo") is not None:
            self.PlayAuthKeyInfo = PlayAuthKeyInfo()
            self.PlayAuthKeyInfo._deserialize(params.get("PlayAuthKeyInfo"))
        self.RequestId = params.get("RequestId")


class DescribeLivePullStreamTasksRequest(AbstractModel):
    """DescribeLivePullStreamTasks request structure.

    """

    def __init__(self):
        r"""
        :param TaskId: The task ID. 
A task ID is returned by the `CreateLivePullStreamTask` API.
If you do not pass this parameter, all tasks will be returned, sorted by last updated time in descending order.
        :type TaskId: str
        :param PageNum: The number of page to start from. Default value: 1.
        :type PageNum: int
        :param PageSize: The maximum number of records per page. Default value: 10.
Valid values: Any integer between 1 and 20.
        :type PageSize: int
        """
        self.TaskId = None
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLivePullStreamTasksResponse(AbstractModel):
    """DescribeLivePullStreamTasks response structure.

    """

    def __init__(self):
        r"""
        :param TaskInfos: The information of stream pulling tasks.
        :type TaskInfos: list of PullStreamTaskInfo
        :param PageNum: The page number.
        :type PageNum: int
        :param PageSize: The number of records per page.
        :type PageSize: int
        :param TotalNum: The total number of records.
        :type TotalNum: int
        :param TotalPage: The total number of pages.
        :type TotalPage: int
        :param LimitTaskNum: The maximum number of tasks allowed.
        :type LimitTaskNum: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskInfos = None
        self.PageNum = None
        self.PageSize = None
        self.TotalNum = None
        self.TotalPage = None
        self.LimitTaskNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskInfos") is not None:
            self.TaskInfos = []
            for item in params.get("TaskInfos"):
                obj = PullStreamTaskInfo()
                obj._deserialize(item)
                self.TaskInfos.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.LimitTaskNum = params.get("LimitTaskNum")
        self.RequestId = params.get("RequestId")


class DescribeLivePushAuthKeyRequest(AbstractModel):
    """DescribeLivePushAuthKey request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Push domain name.
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLivePushAuthKeyResponse(AbstractModel):
    """DescribeLivePushAuthKey response structure.

    """

    def __init__(self):
        r"""
        :param PushAuthKeyInfo: Push authentication key information.
        :type PushAuthKeyInfo: :class:`tencentcloud.live.v20180801.models.PushAuthKeyInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PushAuthKeyInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PushAuthKeyInfo") is not None:
            self.PushAuthKeyInfo = PushAuthKeyInfo()
            self.PushAuthKeyInfo._deserialize(params.get("PushAuthKeyInfo"))
        self.RequestId = params.get("RequestId")


class DescribeLiveRecordRulesRequest(AbstractModel):
    """DescribeLiveRecordRules request structure.

    """


class DescribeLiveRecordRulesResponse(AbstractModel):
    """DescribeLiveRecordRules response structure.

    """

    def __init__(self):
        r"""
        :param Rules: List of rules.
        :type Rules: list of RuleInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleInfo()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveRecordTemplateRequest(AbstractModel):
    """DescribeLiveRecordTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID obtained by [DescribeLiveRecordTemplates](https://intl.cloud.tencent.com/document/product/267/32609?from_cn_redirect=1).
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveRecordTemplateResponse(AbstractModel):
    """DescribeLiveRecordTemplate response structure.

    """

    def __init__(self):
        r"""
        :param Template: Recording template information.
        :type Template: :class:`tencentcloud.live.v20180801.models.RecordTemplateInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = RecordTemplateInfo()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")


class DescribeLiveRecordTemplatesRequest(AbstractModel):
    """DescribeLiveRecordTemplates request structure.

    """

    def __init__(self):
        r"""
        :param IsDelayLive: Whether it is an LCB template. Default value: 0.
0: LVB.
1: LCB.
        :type IsDelayLive: int
        """
        self.IsDelayLive = None


    def _deserialize(self, params):
        self.IsDelayLive = params.get("IsDelayLive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveRecordTemplatesResponse(AbstractModel):
    """DescribeLiveRecordTemplates response structure.

    """

    def __init__(self):
        r"""
        :param Templates: Recording template information list.
        :type Templates: list of RecordTemplateInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Templates = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = RecordTemplateInfo()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveSnapshotRulesRequest(AbstractModel):
    """DescribeLiveSnapshotRules request structure.

    """


class DescribeLiveSnapshotRulesResponse(AbstractModel):
    """DescribeLiveSnapshotRules response structure.

    """

    def __init__(self):
        r"""
        :param Rules: Rule list.
        :type Rules: list of RuleInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleInfo()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveSnapshotTemplateRequest(AbstractModel):
    """DescribeLiveSnapshotTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID.
Template ID returned by the [CreateLiveSnapshotTemplate](https://intl.cloud.tencent.com/document/product/267/32624?from_cn_redirect=1) API call.
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveSnapshotTemplateResponse(AbstractModel):
    """DescribeLiveSnapshotTemplate response structure.

    """

    def __init__(self):
        r"""
        :param Template: Screencapturing template information.
        :type Template: :class:`tencentcloud.live.v20180801.models.SnapshotTemplateInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = SnapshotTemplateInfo()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")


class DescribeLiveSnapshotTemplatesRequest(AbstractModel):
    """DescribeLiveSnapshotTemplates request structure.

    """


class DescribeLiveSnapshotTemplatesResponse(AbstractModel):
    """DescribeLiveSnapshotTemplates response structure.

    """

    def __init__(self):
        r"""
        :param Templates: Screencapturing template list.
        :type Templates: list of SnapshotTemplateInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Templates = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = SnapshotTemplateInfo()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveStreamEventListRequest(AbstractModel):
    """DescribeLiveStreamEventList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time. 
In UTC format, such as 2018-12-29T19:00:00Z.
This supports querying the history of 60 days.
        :type StartTime: str
        :param EndTime: End time.
In UTC format, such as 2018-12-29T20:00:00Z.
This cannot be after the current time and cannot be more than 30 days after the start time.
        :type EndTime: str
        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.
        :type AppName: str
        :param DomainName: Push domain name.
        :type DomainName: str
        :param StreamName: Stream name; query with wildcard (*) is not supported; fuzzy match by default.
The IsStrict field can be used to change to exact query.
        :type StreamName: str
        :param PageNum: Page number to get.
Default value: 1.
Note: Currently, query for up to 10,000 entries is supported.
        :type PageNum: int
        :param PageSize: Number of entries per page.
Maximum value: 100.
Value range: any integer between 1 and 100.
Default value: 10.
Note: currently, query for up to 10,000 entries is supported.
        :type PageSize: int
        :param IsFilter: Whether to filter. No filtering by default.
0: No filtering at all.
1: Filter out the failing streams and return only the successful ones.
        :type IsFilter: int
        :param IsStrict: Whether to query exactly. Fuzzy match by default.
0: Fuzzy match.
1: Exact query.
Note: This parameter takes effect when StreamName is used.
        :type IsStrict: int
        :param IsAsc: Whether to display in ascending order by end time. Descending order by default.
0: Descending.
1: Ascending.
        :type IsAsc: int
        """
        self.StartTime = None
        self.EndTime = None
        self.AppName = None
        self.DomainName = None
        self.StreamName = None
        self.PageNum = None
        self.PageSize = None
        self.IsFilter = None
        self.IsStrict = None
        self.IsAsc = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.IsFilter = params.get("IsFilter")
        self.IsStrict = params.get("IsStrict")
        self.IsAsc = params.get("IsAsc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveStreamEventListResponse(AbstractModel):
    """DescribeLiveStreamEventList response structure.

    """

    def __init__(self):
        r"""
        :param EventList: List of streaming events.
        :type EventList: list of StreamEventInfo
        :param PageNum: Page number.
        :type PageNum: int
        :param PageSize: Number of entries per page.
        :type PageSize: int
        :param TotalNum: Total number of eligible ones.
        :type TotalNum: int
        :param TotalPage: Total number of pages.
        :type TotalPage: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EventList = None
        self.PageNum = None
        self.PageSize = None
        self.TotalNum = None
        self.TotalPage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EventList") is not None:
            self.EventList = []
            for item in params.get("EventList"):
                obj = StreamEventInfo()
                obj._deserialize(item)
                self.EventList.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.RequestId = params.get("RequestId")


class DescribeLiveStreamOnlineListRequest(AbstractModel):
    """DescribeLiveStreamOnlineList request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Push domain name. If you use multiple paths, enter the `DomainName`.
        :type DomainName: str
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default. If you use multiple paths, enter the `AppName`.
        :type AppName: str
        :param PageNum: Page number to get. Default value: 1.
        :type PageNum: int
        :param PageSize: Number of entries per page. Maximum value: 100. 
Value: any integer between 10 and 100.
Default value: 10.
        :type PageSize: int
        :param StreamName: Stream name, which is used for exact query.
        :type StreamName: str
        """
        self.DomainName = None
        self.AppName = None
        self.PageNum = None
        self.PageSize = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveStreamOnlineListResponse(AbstractModel):
    """DescribeLiveStreamOnlineList response structure.

    """

    def __init__(self):
        r"""
        :param TotalNum: Total number of eligible ones.
        :type TotalNum: int
        :param TotalPage: Total number of pages.
        :type TotalPage: int
        :param PageNum: Page number.
        :type PageNum: int
        :param PageSize: Number of entries displayed per page.
        :type PageSize: int
        :param OnlineInfo: Active push information list.
        :type OnlineInfo: list of StreamOnlineInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalNum = None
        self.TotalPage = None
        self.PageNum = None
        self.PageSize = None
        self.OnlineInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        if params.get("OnlineInfo") is not None:
            self.OnlineInfo = []
            for item in params.get("OnlineInfo"):
                obj = StreamOnlineInfo()
                obj._deserialize(item)
                self.OnlineInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveStreamPublishedListRequest(AbstractModel):
    """DescribeLiveStreamPublishedList request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Your push domain name.
        :type DomainName: str
        :param EndTime: End time.
In UTC format, such as 2016-06-30T19:00:00Z.
This cannot be after the current time.
Note: The difference between EndTime and StartTime cannot be greater than 30 days.
        :type EndTime: str
        :param StartTime: Start time. 
In UTC format, such as 2016-06-29T19:00:00Z.
This supports querying data in the past 60 days.
        :type StartTime: str
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default. Fuzzy match is not supported.
        :type AppName: str
        :param PageNum: Page number to get.
Default value: 1.
        :type PageNum: int
        :param PageSize: Number of entries per page.
Maximum value: 100
Valid values: integers between 10 and 100
Default value: 10
        :type PageSize: int
        :param StreamName: Stream name, which supports fuzzy match.
        :type StreamName: str
        """
        self.DomainName = None
        self.EndTime = None
        self.StartTime = None
        self.AppName = None
        self.PageNum = None
        self.PageSize = None
        self.StreamName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.EndTime = params.get("EndTime")
        self.StartTime = params.get("StartTime")
        self.AppName = params.get("AppName")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveStreamPublishedListResponse(AbstractModel):
    """DescribeLiveStreamPublishedList response structure.

    """

    def __init__(self):
        r"""
        :param PublishInfo: Push record information.
        :type PublishInfo: list of StreamName
        :param PageNum: Page number.
        :type PageNum: int
        :param PageSize: Number of entries per page
        :type PageSize: int
        :param TotalNum: Total number of eligible ones.
        :type TotalNum: int
        :param TotalPage: Total number of pages.
        :type TotalPage: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PublishInfo = None
        self.PageNum = None
        self.PageSize = None
        self.TotalNum = None
        self.TotalPage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PublishInfo") is not None:
            self.PublishInfo = []
            for item in params.get("PublishInfo"):
                obj = StreamName()
                obj._deserialize(item)
                self.PublishInfo.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.RequestId = params.get("RequestId")


class DescribeLiveStreamPushInfoListRequest(AbstractModel):
    """DescribeLiveStreamPushInfoList request structure.

    """

    def __init__(self):
        r"""
        :param PushDomain: Push domain name.
        :type PushDomain: str
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.
        :type AppName: str
        :param PageNum: Number of pages,
Value range: [1,10000],
Default value: 1.
        :type PageNum: int
        :param PageSize: Number of entries per page,
Value range: [1,1000],
Default value: 200.
        :type PageSize: int
        """
        self.PushDomain = None
        self.AppName = None
        self.PageNum = None
        self.PageSize = None


    def _deserialize(self, params):
        self.PushDomain = params.get("PushDomain")
        self.AppName = params.get("AppName")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveStreamPushInfoListResponse(AbstractModel):
    """DescribeLiveStreamPushInfoList response structure.

    """

    def __init__(self):
        r"""
        :param DataInfoList: Live stream statistics list.
        :type DataInfoList: list of PushDataInfo
        :param TotalNum: Total number of live streams.
        :type TotalNum: int
        :param TotalPage: Total number of pages.
        :type TotalPage: int
        :param PageNum: Page number where the current data resides.
        :type PageNum: int
        :param PageSize: Number of live streams per page.
        :type PageSize: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DataInfoList = None
        self.TotalNum = None
        self.TotalPage = None
        self.PageNum = None
        self.PageSize = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = PushDataInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.RequestId = params.get("RequestId")


class DescribeLiveStreamStateRequest(AbstractModel):
    """DescribeLiveStreamState request structure.

    """

    def __init__(self):
        r"""
        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.
        :type AppName: str
        :param DomainName: Your push domain name.
        :type DomainName: str
        :param StreamName: Stream name.
        :type StreamName: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveStreamStateResponse(AbstractModel):
    """DescribeLiveStreamState response structure.

    """

    def __init__(self):
        r"""
        :param StreamState: Stream status,
active: active
inactive: Inactive
forbid: forbidden.
        :type StreamState: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.StreamState = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StreamState = params.get("StreamState")
        self.RequestId = params.get("RequestId")


class DescribeLiveTimeShiftBillInfoListRequest(AbstractModel):
    """DescribeLiveTimeShiftBillInfoList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: The start time for query. You can query data from the past three months. The longest time period that can be queried is one month.

It must be in UTC format.
Example: 2019-01-08T10:00:00Z.
Note: Beijing time is 8 hours ahead of UTC. The [ISO 8601 format](https://intl.cloud.tencent.com/document/product/266/11732#iso-date-format) is used.
        :type StartTime: str
        :param EndTime: The end time for query. You can query data from the past three months. The longest time period that can be queried is one month.

It must be in UTC format.
Example: 2019-01-08T10:00:00Z.
Note: Beijing time is 8 hours ahead of UTC. The [ISO 8601 format](https://intl.cloud.tencent.com/document/product/266/11732#iso-date-format) is used.
        :type EndTime: str
        :param PushDomains: The push domains to query. If you leave this empty, the time shifting billing data of all push domains will be returned.
        :type PushDomains: list of str
        """
        self.StartTime = None
        self.EndTime = None
        self.PushDomains = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PushDomains = params.get("PushDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveTimeShiftBillInfoListResponse(AbstractModel):
    """DescribeLiveTimeShiftBillInfoList response structure.

    """

    def __init__(self):
        r"""
        :param DataInfoList: The time shifting billing data.
        :type DataInfoList: list of TimeShiftBillData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = TimeShiftBillData()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveTranscodeDetailInfoRequest(AbstractModel):
    """DescribeLiveTranscodeDetailInfo request structure.

    """

    def __init__(self):
        r"""
        :param PushDomain: Push domain name.
        :type PushDomain: str
        :param StreamName: Stream name.
        :type StreamName: str
        :param DayTime: Query date (UTC+8)
Format: yyyymmdd
Note: you can query the statistics for a day in the past month, with yesterday as the latest date allowed.
        :type DayTime: str
        :param PageNum: Number of pages. Default value: 1.
Up to 100 pages.
        :type PageNum: int
        :param PageSize: Number of entries per page. Default value: 20,
Value range: [10,1000].
        :type PageSize: int
        :param StartDayTime: Start day time (Beijing time),
In the format of `yyyymmdd`.
Note: details for the last month can be queried.
        :type StartDayTime: str
        :param EndDayTime: End date (UTC+8)
Format: yyyymmdd
Note: you can query the statistics for a period in the past month, with yesterday as the latest date allowed. You must specify either `DayTime`, or `StartDayTime` and `EndDayTime`. If you specify all three parameters, only `DayTime` will be applied.
        :type EndDayTime: str
        """
        self.PushDomain = None
        self.StreamName = None
        self.DayTime = None
        self.PageNum = None
        self.PageSize = None
        self.StartDayTime = None
        self.EndDayTime = None


    def _deserialize(self, params):
        self.PushDomain = params.get("PushDomain")
        self.StreamName = params.get("StreamName")
        self.DayTime = params.get("DayTime")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.StartDayTime = params.get("StartDayTime")
        self.EndDayTime = params.get("EndDayTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveTranscodeDetailInfoResponse(AbstractModel):
    """DescribeLiveTranscodeDetailInfo response structure.

    """

    def __init__(self):
        r"""
        :param DataInfoList: Statistics list.
        :type DataInfoList: list of TranscodeDetailInfo
        :param PageNum: Page number.
        :type PageNum: int
        :param PageSize: Number of entries per page.
        :type PageSize: int
        :param TotalNum: Total number.
        :type TotalNum: int
        :param TotalPage: Total number of pages.
        :type TotalPage: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DataInfoList = None
        self.PageNum = None
        self.PageSize = None
        self.TotalNum = None
        self.TotalPage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = TranscodeDetailInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.RequestId = params.get("RequestId")


class DescribeLiveTranscodeRulesRequest(AbstractModel):
    """DescribeLiveTranscodeRules request structure.

    """

    def __init__(self):
        r"""
        :param TemplateIds: An array of template IDs to be filtered.
        :type TemplateIds: list of int
        :param DomainNames: An array of domain names to be filtered.
        :type DomainNames: list of str
        """
        self.TemplateIds = None
        self.DomainNames = None


    def _deserialize(self, params):
        self.TemplateIds = params.get("TemplateIds")
        self.DomainNames = params.get("DomainNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveTranscodeRulesResponse(AbstractModel):
    """DescribeLiveTranscodeRules response structure.

    """

    def __init__(self):
        r"""
        :param Rules: List of transcoding rules.
        :type Rules: list of RuleInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleInfo()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveTranscodeTemplateRequest(AbstractModel):
    """DescribeLiveTranscodeTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID.
Note: get the template ID in the returned value of the [CreateLiveTranscodeTemplate](https://intl.cloud.tencent.com/document/product/267/32646?from_cn_redirect=1) API call.
        :type TemplateId: int
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveTranscodeTemplateResponse(AbstractModel):
    """DescribeLiveTranscodeTemplate response structure.

    """

    def __init__(self):
        r"""
        :param Template: Template information.
        :type Template: :class:`tencentcloud.live.v20180801.models.TemplateInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = TemplateInfo()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")


class DescribeLiveTranscodeTemplatesRequest(AbstractModel):
    """DescribeLiveTranscodeTemplates request structure.

    """


class DescribeLiveTranscodeTemplatesResponse(AbstractModel):
    """DescribeLiveTranscodeTemplates response structure.

    """

    def __init__(self):
        r"""
        :param Templates: List of transcoding templates.
        :type Templates: list of TemplateInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Templates = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = TemplateInfo()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveTranscodeTotalInfoRequest(AbstractModel):
    """DescribeLiveTranscodeTotalInfo request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time (Beijing time)
Format: yyyy-mm-dd HH:MM:SS
        :type StartTime: str
        :param EndTime: End time (Beijing time)
Format: yyyy-mm-dd HH:MM:SS
        :type EndTime: str
        :param PushDomains: List of push domains to query. If this parameter is left empty, the data of all domains is queried.
If this parameter is specified, the data returned will be on an hourly basis.
        :type PushDomains: list of str
        :param MainlandOrOversea: Valid values:
`Mainland`: queries transcoding data in the Chinese mainland
`Oversea`: queries transcoding data outside the Chinese mainland
By default, the data both in and outside the Chinese mainland is queried.
        :type MainlandOrOversea: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PushDomains = None
        self.MainlandOrOversea = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PushDomains = params.get("PushDomains")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveTranscodeTotalInfoResponse(AbstractModel):
    """DescribeLiveTranscodeTotalInfo response structure.

    """

    def __init__(self):
        r"""
        :param DataInfoList: List of transcoding data
Note: This field may return `null`, indicating that no valid value can be found.
        :type DataInfoList: list of TranscodeTotalInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = TranscodeTotalInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveWatermarkRequest(AbstractModel):
    """DescribeLiveWatermark request structure.

    """

    def __init__(self):
        r"""
        :param WatermarkId: Watermark ID returned by the `DescribeLiveWatermarks` API.
        :type WatermarkId: int
        """
        self.WatermarkId = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveWatermarkResponse(AbstractModel):
    """DescribeLiveWatermark response structure.

    """

    def __init__(self):
        r"""
        :param Watermark: Watermark information.
        :type Watermark: :class:`tencentcloud.live.v20180801.models.WatermarkInfo`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Watermark = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Watermark") is not None:
            self.Watermark = WatermarkInfo()
            self.Watermark._deserialize(params.get("Watermark"))
        self.RequestId = params.get("RequestId")


class DescribeLiveWatermarkRulesRequest(AbstractModel):
    """DescribeLiveWatermarkRules request structure.

    """


class DescribeLiveWatermarkRulesResponse(AbstractModel):
    """DescribeLiveWatermarkRules response structure.

    """

    def __init__(self):
        r"""
        :param Rules: Watermarking rule list.
        :type Rules: list of RuleInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Rules = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleInfo()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveWatermarksRequest(AbstractModel):
    """DescribeLiveWatermarks request structure.

    """


class DescribeLiveWatermarksResponse(AbstractModel):
    """DescribeLiveWatermarks response structure.

    """

    def __init__(self):
        r"""
        :param TotalNum: Total number of watermarks.
        :type TotalNum: int
        :param WatermarkList: Watermark information list.
        :type WatermarkList: list of WatermarkInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalNum = None
        self.WatermarkList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalNum = params.get("TotalNum")
        if params.get("WatermarkList") is not None:
            self.WatermarkList = []
            for item in params.get("WatermarkList"):
                obj = WatermarkInfo()
                obj._deserialize(item)
                self.WatermarkList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePlayErrorCodeDetailInfoListRequest(AbstractModel):
    """DescribePlayErrorCodeDetailInfoList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time (Beijing time),
In the format of `yyyy-mm-dd HH:MM:SS`.
        :type StartTime: str
        :param EndTime: End time (Beijing time),
In the format of `yyyy-mm-dd HH:MM:SS`.
Note: `EndTime` and `StartTime` only support querying data for the last day.
        :type EndTime: str
        :param Granularity: Query granularity:
1: 1-minute granularity.
        :type Granularity: int
        :param StatType: Yes. Valid values: "4xx", "5xx". Mixed codes in the format of `4xx,5xx` are also supported.
        :type StatType: str
        :param PlayDomains: Playback domain name list.
        :type PlayDomains: list of str
        :param MainlandOrOversea: Region. Valid values: Mainland (data for Mainland China), Oversea (data for regions outside Mainland China), China (data for China, including Hong Kong, Macao, and Taiwan), Foreign (data for regions outside China, excluding Hong Kong, Macao, and Taiwan), Global (default). If this parameter is left empty, data for all regions will be queried.
        :type MainlandOrOversea: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Granularity = None
        self.StatType = None
        self.PlayDomains = None
        self.MainlandOrOversea = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Granularity = params.get("Granularity")
        self.StatType = params.get("StatType")
        self.PlayDomains = params.get("PlayDomains")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePlayErrorCodeDetailInfoListResponse(AbstractModel):
    """DescribePlayErrorCodeDetailInfoList response structure.

    """

    def __init__(self):
        r"""
        :param HttpCodeList: Statistics list.
        :type HttpCodeList: list of HttpCodeInfo
        :param StatType: Statistics type.
        :type StatType: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.HttpCodeList = None
        self.StatType = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HttpCodeList") is not None:
            self.HttpCodeList = []
            for item in params.get("HttpCodeList"):
                obj = HttpCodeInfo()
                obj._deserialize(item)
                self.HttpCodeList.append(obj)
        self.StatType = params.get("StatType")
        self.RequestId = params.get("RequestId")


class DescribePlayErrorCodeSumInfoListRequest(AbstractModel):
    """DescribePlayErrorCodeSumInfoList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start point in time (Beijing time).
In the format of `yyyy-mm-dd HH:MM:SS`.
        :type StartTime: str
        :param EndTime: End point in time (Beijing time).
In the format of `yyyy-mm-dd HH:MM:SS`.
Note: `EndTime` and `StartTime` only support querying data for the last day.
        :type EndTime: str
        :param PlayDomains: Playback domain name list. If this parameter is left empty, full data will be queried.
        :type PlayDomains: list of str
        :param PageNum: Number of pages. Value range: [1,1000]. Default value: 1.
        :type PageNum: int
        :param PageSize: Number of entries per page. Value range: [1,1000]. Default value: 20.
        :type PageSize: int
        :param MainlandOrOversea: Region. Valid values: Mainland (data for Mainland China), Oversea (data for regions outside Mainland China), China (data for China, including Hong Kong, Macao, and Taiwan), Foreign (data for regions outside China, excluding Hong Kong, Macao, and Taiwan), Global (default). If this parameter is left empty, data for all regions will be queried.
        :type MainlandOrOversea: str
        :param GroupType: Grouping parameter. Valid values: CountryProIsp (default value), Country (country/region). Grouping is made by country/region + district + ISP by default. Currently, districts and ISPs outside Mainland China cannot be recognized.
        :type GroupType: str
        :param OutLanguage: Language used in the output field. Valid values: Chinese (default), English. Currently, country/region, district, and ISP parameters support multiple languages.
        :type OutLanguage: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomains = None
        self.PageNum = None
        self.PageSize = None
        self.MainlandOrOversea = None
        self.GroupType = None
        self.OutLanguage = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomains = params.get("PlayDomains")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.GroupType = params.get("GroupType")
        self.OutLanguage = params.get("OutLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePlayErrorCodeSumInfoListResponse(AbstractModel):
    """DescribePlayErrorCodeSumInfoList response structure.

    """

    def __init__(self):
        r"""
        :param ProIspInfoList: Information of error codes starting with 2, 3, 4, or 5 by district and ISP.
        :type ProIspInfoList: list of ProIspPlayCodeDataInfo
        :param TotalCodeAll: Total occurrences of all status codes.
        :type TotalCodeAll: int
        :param TotalCode4xx: Occurrences of 4xx status codes.
        :type TotalCode4xx: int
        :param TotalCode5xx: Occurrences of 5xx status codes.
        :type TotalCode5xx: int
        :param TotalCodeList: Total occurrences of each status code.
        :type TotalCodeList: list of PlayCodeTotalInfo
        :param PageNum: Page number.
        :type PageNum: int
        :param PageSize: Number of entries per page.
        :type PageSize: int
        :param TotalPage: Total number of pages.
        :type TotalPage: int
        :param TotalNum: Total number of results.
        :type TotalNum: int
        :param TotalCode2xx: Occurrences of 2xx status codes.
        :type TotalCode2xx: int
        :param TotalCode3xx: Occurrences of 3xx status codes.
        :type TotalCode3xx: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ProIspInfoList = None
        self.TotalCodeAll = None
        self.TotalCode4xx = None
        self.TotalCode5xx = None
        self.TotalCodeList = None
        self.PageNum = None
        self.PageSize = None
        self.TotalPage = None
        self.TotalNum = None
        self.TotalCode2xx = None
        self.TotalCode3xx = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProIspInfoList") is not None:
            self.ProIspInfoList = []
            for item in params.get("ProIspInfoList"):
                obj = ProIspPlayCodeDataInfo()
                obj._deserialize(item)
                self.ProIspInfoList.append(obj)
        self.TotalCodeAll = params.get("TotalCodeAll")
        self.TotalCode4xx = params.get("TotalCode4xx")
        self.TotalCode5xx = params.get("TotalCode5xx")
        if params.get("TotalCodeList") is not None:
            self.TotalCodeList = []
            for item in params.get("TotalCodeList"):
                obj = PlayCodeTotalInfo()
                obj._deserialize(item)
                self.TotalCodeList.append(obj)
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TotalPage = params.get("TotalPage")
        self.TotalNum = params.get("TotalNum")
        self.TotalCode2xx = params.get("TotalCode2xx")
        self.TotalCode3xx = params.get("TotalCode3xx")
        self.RequestId = params.get("RequestId")


class DescribeProvinceIspPlayInfoListRequest(AbstractModel):
    """DescribeProvinceIspPlayInfoList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start point in time (Beijing time).
Example: 2019-02-21 10:00:00.
        :type StartTime: str
        :param EndTime: End point in time (Beijing time).
Example: 2019-02-21 12:00:00.
Note: `EndTime` and `StartTime` only support querying data for the last day.
        :type EndTime: str
        :param Granularity: Supported granularities:
1: 1-minute granularity (the query interval should be within 1 day)
        :type Granularity: int
        :param StatType: Statistical metric type:
"Bandwidth": bandwidth
"FluxPerSecond": average traffic
"Flux": traffic
"Request": number of requests
"Online": number of concurrent connections
        :type StatType: str
        :param PlayDomains: Playback domain name list.
        :type PlayDomains: list of str
        :param ProvinceNames: List of the districts to be queried, such as Beijing.
        :type ProvinceNames: list of str
        :param IspNames: List of the ISPs to be queried, such as China Mobile. If this parameter is left empty, the data of all ISPs will be queried.
        :type IspNames: list of str
        :param MainlandOrOversea: Region. Valid values: Mainland (data for Mainland China), Oversea (data for regions outside Mainland China), China (data for China, including Hong Kong, Macao, and Taiwan), Foreign (data for regions outside China, excluding Hong Kong, Macao, and Taiwan), Global (default). If this parameter is left empty, data for all regions will be queried.
        :type MainlandOrOversea: str
        :param IpType: IP type:
"Ipv6": IPv6 data
Data of all IPs will be returned if this parameter is left empty.
        :type IpType: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Granularity = None
        self.StatType = None
        self.PlayDomains = None
        self.ProvinceNames = None
        self.IspNames = None
        self.MainlandOrOversea = None
        self.IpType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Granularity = params.get("Granularity")
        self.StatType = params.get("StatType")
        self.PlayDomains = params.get("PlayDomains")
        self.ProvinceNames = params.get("ProvinceNames")
        self.IspNames = params.get("IspNames")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.IpType = params.get("IpType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProvinceIspPlayInfoListResponse(AbstractModel):
    """DescribeProvinceIspPlayInfoList response structure.

    """

    def __init__(self):
        r"""
        :param DataInfoList: Playback information list.
        :type DataInfoList: list of PlayStatInfo
        :param StatType: Statistics type, which is the same as the input parameter.
        :type StatType: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DataInfoList = None
        self.StatType = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = PlayStatInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.StatType = params.get("StatType")
        self.RequestId = params.get("RequestId")


class DescribeScreenShotSheetNumListRequest(AbstractModel):
    """DescribeScreenShotSheetNumList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time in UTC time in the format of `yyyy-mm-ddTHH:MM:SSZ`.
        :type StartTime: str
        :param EndTime: End time in UTC time in the format of `yyyy-mm-ddTHH:MM:SSZ`. Data for the last year can be queried.
        :type EndTime: str
        :param Zone: Region information. Valid values: Mainland, Oversea. The former is to query data within Mainland China, while the latter outside Mainland China. If this parameter is left empty, data of all regions will be queried.
        :type Zone: str
        :param PushDomains: Push domain name (data at the domain name level after November 1, 2019 can be queried).
        :type PushDomains: list of str
        :param Granularity: Data granularity. There is a 1.5-hour delay in data reporting. Valid values: `Minute` (5-minute granularity; query period of up to 31 days); `Day` (1-day granularity based on UTC+8:00; query period of up to 186 days)
        :type Granularity: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Zone = None
        self.PushDomains = None
        self.Granularity = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Zone = params.get("Zone")
        self.PushDomains = params.get("PushDomains")
        self.Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScreenShotSheetNumListResponse(AbstractModel):
    """DescribeScreenShotSheetNumList response structure.

    """

    def __init__(self):
        r"""
        :param DataInfoList: Data information list.
        :type DataInfoList: list of TimeValue
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = TimeValue()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeStreamDayPlayInfoListRequest(AbstractModel):
    """DescribeStreamDayPlayInfoList request structure.

    """

    def __init__(self):
        r"""
        :param DayTime: Date in the format of YYYY-mm-dd
Data is available at 3am Beijing Time the next day. You are recommended to query the latest data after this time point. Data in the last 3 months can be queried.
        :type DayTime: str
        :param PlayDomain: Playback domain name.
        :type PlayDomain: str
        :param PageNum: Page number. Value range: [1,1000]. Default value: 1.
        :type PageNum: int
        :param PageSize: Number of entries per page. Value range: [100,1000]. Default value: 1,000.
        :type PageSize: int
        :param MainlandOrOversea: Valid values:
Mainland: query data for Mainland China,
Oversea: query data for regions outside Mainland China,
Default: query data for all regions.
        :type MainlandOrOversea: str
        :param ServiceName: Service name. Valid values: LVB, LEB. If this parameter is left empty, all data of LVB and LEB will be queried.
        :type ServiceName: str
        """
        self.DayTime = None
        self.PlayDomain = None
        self.PageNum = None
        self.PageSize = None
        self.MainlandOrOversea = None
        self.ServiceName = None


    def _deserialize(self, params):
        self.DayTime = params.get("DayTime")
        self.PlayDomain = params.get("PlayDomain")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamDayPlayInfoListResponse(AbstractModel):
    """DescribeStreamDayPlayInfoList response structure.

    """

    def __init__(self):
        r"""
        :param DataInfoList: Playback data information list.
        :type DataInfoList: list of PlayDataInfoByStream
        :param TotalNum: Total number.
        :type TotalNum: int
        :param TotalPage: Total number of pages.
        :type TotalPage: int
        :param PageNum: Page number where the current data resides.
        :type PageNum: int
        :param PageSize: Number of entries per page.
        :type PageSize: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DataInfoList = None
        self.TotalNum = None
        self.TotalPage = None
        self.PageNum = None
        self.PageSize = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = PlayDataInfoByStream()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.RequestId = params.get("RequestId")


class DescribeStreamPlayInfoListRequest(AbstractModel):
    """DescribeStreamPlayInfoList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time (Beijing time) in the format of yyyy-mm-dd HH:MM:SS
        :type StartTime: str
        :param EndTime: End time (Beijing time) in the format of yyyy-mm-dd HH:MM:SS
The start time and end time cannot be more than 24 hours apart and must be within the last 15 days.
        :type EndTime: str
        :param PlayDomain: Playback domain name,
If this parameter is left empty, data of live streams of all playback domain names will be queried.
        :type PlayDomain: str
        :param StreamName: Stream name (exact match).
If this parameter is left empty, full playback data will be queried.
        :type StreamName: str
        :param AppName: Push address. Its value is the same as the `AppName` in playback address. It supports exact match, and takes effect only when `StreamName` is passed at the same time.
If it is left empty, the full playback data will be queried.
Note: to query by `AppName`, you need to submit a ticket first. After your application succeeds, it will take about 5 business days (subject to the time in the reply) for the configuration to take effect.
        :type AppName: str
        :param ServiceName: Service name. Valid values: LVB, LEB. If this parameter is left empty, all data of LVB and LEB will be queried.
        :type ServiceName: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomain = None
        self.StreamName = None
        self.AppName = None
        self.ServiceName = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomain = params.get("PlayDomain")
        self.StreamName = params.get("StreamName")
        self.AppName = params.get("AppName")
        self.ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamPlayInfoListResponse(AbstractModel):
    """DescribeStreamPlayInfoList response structure.

    """

    def __init__(self):
        r"""
        :param DataInfoList: Statistics list at a 1-minute granularity.
        :type DataInfoList: list of DayStreamPlayInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = DayStreamPlayInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTopClientIpSumInfoListRequest(AbstractModel):
    """DescribeTopClientIpSumInfoList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start point in time in the format of `yyyy-mm-dd HH:MM:SS`.
        :type StartTime: str
        :param EndTime: End point in time in the format of `yyyy-mm-dd HH:MM:SS`
The time span is [0,4 hours]. Data for the last day can be queried.
        :type EndTime: str
        :param PlayDomains: Playback domain name. If this parameter is left empty, full data will be queried by default.
        :type PlayDomains: list of str
        :param PageNum: Page number. Value range: [1,1000]. Default value: 1.
        :type PageNum: int
        :param PageSize: Number of entries per page. Value range: [1,1000]. Default value: 20.
        :type PageSize: int
        :param OrderParam: Sorting metric. Valid values: TotalRequest (default value), FailedRequest, TotalFlux.
        :type OrderParam: str
        :param MainlandOrOversea: Region. Valid values: Mainland (data for Mainland China), Oversea (data for regions outside Mainland China), China (data for China, including Hong Kong, Macao, and Taiwan), Foreign (data for regions outside China, excluding Hong Kong, Macao, and Taiwan), Global (default). If this parameter is left empty, data for all regions will be queried.
        :type MainlandOrOversea: str
        :param OutLanguage: Language used in the output field. Valid values: Chinese (default), English. Currently, country/region, district, and ISP parameters support multiple languages.
        :type OutLanguage: str
        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomains = None
        self.PageNum = None
        self.PageSize = None
        self.OrderParam = None
        self.MainlandOrOversea = None
        self.OutLanguage = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomains = params.get("PlayDomains")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.OrderParam = params.get("OrderParam")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.OutLanguage = params.get("OutLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopClientIpSumInfoListResponse(AbstractModel):
    """DescribeTopClientIpSumInfoList response structure.

    """

    def __init__(self):
        r"""
        :param PageNum: Page number. Value range: [1,1000]. Default value: 1.
        :type PageNum: int
        :param PageSize: Number of entries per page. Value range: [1,1000]. Default value: 20.
        :type PageSize: int
        :param OrderParam: Sorting metric. Valid values: "TotalRequest", "FailedRequest", "TotalFlux".
        :type OrderParam: str
        :param TotalNum: Total number of results.
        :type TotalNum: int
        :param TotalPage: Total number of result pages.
        :type TotalPage: int
        :param DataInfoList: Data content.
        :type DataInfoList: list of ClientIpPlaySumInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PageNum = None
        self.PageSize = None
        self.OrderParam = None
        self.TotalNum = None
        self.TotalPage = None
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.OrderParam = params.get("OrderParam")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = ClientIpPlaySumInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUploadStreamNumsRequest(AbstractModel):
    """DescribeUploadStreamNums request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start time point in the format of yyyy-mm-dd HH:MM:SS.
        :type StartTime: str
        :param EndTime: End time point in the format of yyyy-mm-dd HH:MM:SS. The difference between the start time and end time cannot be greater than 31 days. Data in the last 31 days can be queried.
        :type EndTime: str
        :param Domains: LVB domain names. If this parameter is left empty, data of all domain names will be queried.
        :type Domains: list of str
        :param Granularity: Time granularity of the data. Valid values:
5: 5-minute granularity (the query period is up to 1 day)
1440: 1-day granularity (the query period is up to 1 month)
Default value: 5
        :type Granularity: int
        """
        self.StartTime = None
        self.EndTime = None
        self.Domains = None
        self.Granularity = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Domains = params.get("Domains")
        self.Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUploadStreamNumsResponse(AbstractModel):
    """DescribeUploadStreamNums response structure.

    """

    def __init__(self):
        r"""
        :param DataInfoList: Detailed data.
        :type DataInfoList: list of ConcurrentRecordStreamNum
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = ConcurrentRecordStreamNum()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVisitTopSumInfoListRequest(AbstractModel):
    """DescribeVisitTopSumInfoList request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Start point in time in the format of `yyyy-mm-dd HH:MM:SS`.
        :type StartTime: str
        :param EndTime: End point in time in the format of `yyyy-mm-dd HH:MM:SS`
The time span is (0,4 hours]. Data for the last day can be queried.
        :type EndTime: str
        :param TopIndex: Bandwidth metric. Valid values: "Domain", "StreamId".
        :type TopIndex: str
        :param PlayDomains: Playback domain name. If this parameter is left empty, full data will be queried by default.
        :type PlayDomains: list of str
        :param PageNum: Page number,
Value range: [1,1000],
Default value: 1.
        :type PageNum: int
        :param PageSize: Number of entries per page. Value range: [1,1000].
Default value: 20.
        :type PageSize: int
        :param OrderParam: Sorting metric. Valid values: "AvgFluxPerSecond", "TotalRequest" (default), "TotalFlux".
        :type OrderParam: str
        """
        self.StartTime = None
        self.EndTime = None
        self.TopIndex = None
        self.PlayDomains = None
        self.PageNum = None
        self.PageSize = None
        self.OrderParam = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TopIndex = params.get("TopIndex")
        self.PlayDomains = params.get("PlayDomains")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.OrderParam = params.get("OrderParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVisitTopSumInfoListResponse(AbstractModel):
    """DescribeVisitTopSumInfoList response structure.

    """

    def __init__(self):
        r"""
        :param PageNum: Page number,
Value range: [1,1000],
Default value: 1.
        :type PageNum: int
        :param PageSize: Number of entries per page. Value range: [1,1000].
Default value: 20.
        :type PageSize: int
        :param TopIndex: Bandwidth metric. Valid values: "Domain", "StreamId".
        :type TopIndex: str
        :param OrderParam: Sorting metric. Valid values: AvgFluxPerSecond (sort by average traffic per second), TotalRequest (sort by total requests), TotalFlux (sort by total traffic). Default value: TotalRequest.
        :type OrderParam: str
        :param TotalNum: Total number of results.
        :type TotalNum: int
        :param TotalPage: Total number of result pages.
        :type TotalPage: int
        :param DataInfoList: Data content.
        :type DataInfoList: list of PlaySumStatInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PageNum = None
        self.PageSize = None
        self.TopIndex = None
        self.OrderParam = None
        self.TotalNum = None
        self.TotalPage = None
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.TopIndex = params.get("TopIndex")
        self.OrderParam = params.get("OrderParam")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = PlaySumStatInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DomainCertInfo(AbstractModel):
    """Domain name certificate information

    """

    def __init__(self):
        r"""
        :param CertId: Certificate ID.
        :type CertId: int
        :param CertName: Certificate name.
        :type CertName: str
        :param Description: Description.
        :type Description: str
        :param CreateTime: Creation time in UTC format.
        :type CreateTime: str
        :param HttpsCrt: Certificate content.
        :type HttpsCrt: str
        :param CertType: Certificate type.
0: user-added certificate
1: Tencent Cloud-hosted certificate.
        :type CertType: int
        :param CertExpireTime: Certificate expiration time in UTC format.
        :type CertExpireTime: str
        :param DomainName: Domain name that uses this certificate.
        :type DomainName: str
        :param Status: Certificate status.
        :type Status: int
        :param CertDomains: List of domain names in the certificate.
["*.x.com"] for example.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CertDomains: list of str
        :param CloudCertId: Tencent Cloud SSL certificate ID.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CloudCertId: str
        """
        self.CertId = None
        self.CertName = None
        self.Description = None
        self.CreateTime = None
        self.HttpsCrt = None
        self.CertType = None
        self.CertExpireTime = None
        self.DomainName = None
        self.Status = None
        self.CertDomains = None
        self.CloudCertId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.CertName = params.get("CertName")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.HttpsCrt = params.get("HttpsCrt")
        self.CertType = params.get("CertType")
        self.CertExpireTime = params.get("CertExpireTime")
        self.DomainName = params.get("DomainName")
        self.Status = params.get("Status")
        self.CertDomains = params.get("CertDomains")
        self.CloudCertId = params.get("CloudCertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainInfo(AbstractModel):
    """LVB domain name information

    """

    def __init__(self):
        r"""
        :param Name: LVB domain name.
        :type Name: str
        :param Type: Domain name type:
0: push.
1: playback.
        :type Type: int
        :param Status: Domain name status:
0: deactivated.
1: activated.
        :type Status: int
        :param CreateTime: Creation time.
        :type CreateTime: str
        :param BCName: Whether there is a CNAME record pointing to a fixed rule domain name:
0: no.
1: yes.
        :type BCName: int
        :param TargetDomain: Domain name corresponding to CNAME record.
        :type TargetDomain: str
        :param PlayType: Playback region. This parameter is valid only if `Type` is 1.
1: in Mainland China.
2: global.
3: outside Mainland China.
        :type PlayType: int
        :param IsDelayLive: Whether it is LCB:
0: LVB.
1: LCB.
        :type IsDelayLive: int
        :param CurrentCName: Information of currently used CNAME record.
        :type CurrentCName: str
        :param RentTag: Disused parameter, which can be ignored.
        :type RentTag: int
        :param RentExpireTime: Disused parameter, which can be ignored.
        :type RentExpireTime: str
        :param IsMiniProgramLive: 0: LVB.
1: LVB on Mini Program.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IsMiniProgramLive: int
        """
        self.Name = None
        self.Type = None
        self.Status = None
        self.CreateTime = None
        self.BCName = None
        self.TargetDomain = None
        self.PlayType = None
        self.IsDelayLive = None
        self.CurrentCName = None
        self.RentTag = None
        self.RentExpireTime = None
        self.IsMiniProgramLive = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.BCName = params.get("BCName")
        self.TargetDomain = params.get("TargetDomain")
        self.PlayType = params.get("PlayType")
        self.IsDelayLive = params.get("IsDelayLive")
        self.CurrentCName = params.get("CurrentCName")
        self.RentTag = params.get("RentTag")
        self.RentExpireTime = params.get("RentExpireTime")
        self.IsMiniProgramLive = params.get("IsMiniProgramLive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableLiveDomainRequest(AbstractModel):
    """EnableLiveDomain request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: LVB domain name to be enabled.
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableLiveDomainResponse(AbstractModel):
    """EnableLiveDomain response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class FlvSpecialParam(AbstractModel):
    """Special FLV recording setting.

    """

    def __init__(self):
        r"""
        :param UploadInRecording: Whether to enable upload while recording. This parameter is only valid for FLV recording.
        :type UploadInRecording: bool
        """
        self.UploadInRecording = None


    def _deserialize(self, params):
        self.UploadInRecording = params.get("UploadInRecording")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForbidLiveDomainRequest(AbstractModel):
    """ForbidLiveDomain request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: LVB domain name to be disabled.
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForbidLiveDomainResponse(AbstractModel):
    """ForbidLiveDomain response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ForbidLiveStreamRequest(AbstractModel):
    """ForbidLiveStream request structure.

    """

    def __init__(self):
        r"""
        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.
        :type AppName: str
        :param DomainName: Your push domain name.
        :type DomainName: str
        :param StreamName: Stream name.
        :type StreamName: str
        :param ResumeTime: The time (in UTC format) to resume the stream, such as 2018-11-29T19:00:00Z.
Notes:
1. The default stream disabling period is seven days. A stream can be disabled for up to 90 days.
2. Beijing time is 8 hours ahead of UTC. The [ISO 8601 format](https://intl.cloud.tencent.com/document/product/266/11732#iso-date-format) is used.
        :type ResumeTime: str
        :param Reason: Reason for forbidding.
Note: Be sure to enter the reason for forbidding to avoid any faulty operations.
Length limit: 2,048 bytes.
        :type Reason: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None
        self.ResumeTime = None
        self.Reason = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        self.ResumeTime = params.get("ResumeTime")
        self.Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForbidLiveStreamResponse(AbstractModel):
    """ForbidLiveStream response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ForbidStreamInfo(AbstractModel):
    """List of forbidden streams

    """

    def __init__(self):
        r"""
        :param StreamName: Stream name.
        :type StreamName: str
        :param CreateTime: Creation time.
        :type CreateTime: str
        :param ExpireTime: Forbidding expiration time.
        :type ExpireTime: str
        """
        self.StreamName = None
        self.CreateTime = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupProIspDataInfo(AbstractModel):
    """Bandwidth, traffic, number of requests, and number of concurrent connections of an ISP in a district.

    """

    def __init__(self):
        r"""
        :param ProvinceName: District.
        :type ProvinceName: str
        :param IspName: ISP.
        :type IspName: str
        :param DetailInfoList: Detailed data at the minute level.
        :type DetailInfoList: list of CdnPlayStatData
        """
        self.ProvinceName = None
        self.IspName = None
        self.DetailInfoList = None


    def _deserialize(self, params):
        self.ProvinceName = params.get("ProvinceName")
        self.IspName = params.get("IspName")
        if params.get("DetailInfoList") is not None:
            self.DetailInfoList = []
            for item in params.get("DetailInfoList"):
                obj = CdnPlayStatData()
                obj._deserialize(item)
                self.DetailInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HlsSpecialParam(AbstractModel):
    """HLS-specific recording parameter

    """

    def __init__(self):
        r"""
        :param FlowContinueDuration: Timeout period for restarting an interrupted HLS push.
Value range: [0, 1,800].
        :type FlowContinueDuration: int
        """
        self.FlowContinueDuration = None


    def _deserialize(self, params):
        self.FlowContinueDuration = params.get("FlowContinueDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpCodeInfo(AbstractModel):
    """HTTP return code and statistics

    """

    def __init__(self):
        r"""
        :param HttpCode: HTTP return code.
Example: "2xx", "3xx", "4xx", "5xx".
        :type HttpCode: str
        :param ValueList: Statistics. 0 will be added for points in time when there is no data.
        :type ValueList: list of HttpCodeValue
        """
        self.HttpCode = None
        self.ValueList = None


    def _deserialize(self, params):
        self.HttpCode = params.get("HttpCode")
        if params.get("ValueList") is not None:
            self.ValueList = []
            for item in params.get("ValueList"):
                obj = HttpCodeValue()
                obj._deserialize(item)
                self.ValueList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpCodeValue(AbstractModel):
    """HTTP return code data

    """

    def __init__(self):
        r"""
        :param Time: Time in the format of `yyyy-mm-dd HH:MM:SS`.
        :type Time: str
        :param Numbers: Occurrences.
        :type Numbers: int
        :param Percentage: Proportion.
        :type Percentage: float
        """
        self.Time = None
        self.Numbers = None
        self.Percentage = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Numbers = params.get("Numbers")
        self.Percentage = params.get("Percentage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpStatusData(AbstractModel):
    """Playback error code information

    """

    def __init__(self):
        r"""
        :param Time: Data point in time,
In the format of `yyyy-mm-dd HH:MM:SS`.
        :type Time: str
        :param HttpStatusInfoList: Playback status code details.
        :type HttpStatusInfoList: list of HttpStatusInfo
        """
        self.Time = None
        self.HttpStatusInfoList = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        if params.get("HttpStatusInfoList") is not None:
            self.HttpStatusInfoList = []
            for item in params.get("HttpStatusInfoList"):
                obj = HttpStatusInfo()
                obj._deserialize(item)
                self.HttpStatusInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpStatusInfo(AbstractModel):
    """Playback error code information

    """

    def __init__(self):
        r"""
        :param HttpStatus: Playback HTTP status code.
        :type HttpStatus: str
        :param Num: Quantity.
        :type Num: int
        """
        self.HttpStatus = None
        self.Num = None


    def _deserialize(self, params):
        self.HttpStatus = params.get("HttpStatus")
        self.Num = params.get("Num")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveCallbackTemplateRequest(AbstractModel):
    """ModifyLiveCallbackTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID returned by the `DescribeLiveCallbackTemplates` API.
        :type TemplateId: int
        :param TemplateName: Template name.
        :type TemplateName: str
        :param Description: Description.
        :type Description: str
        :param StreamBeginNotifyUrl: Stream starting callback URL.
        :type StreamBeginNotifyUrl: str
        :param StreamEndNotifyUrl: Interruption callback URL.
        :type StreamEndNotifyUrl: str
        :param RecordNotifyUrl: Recording callback URL.
        :type RecordNotifyUrl: str
        :param SnapshotNotifyUrl: Screencapturing callback URL.
        :type SnapshotNotifyUrl: str
        :param PornCensorshipNotifyUrl: Porn detection callback URL.
        :type PornCensorshipNotifyUrl: str
        :param CallbackKey: Callback key. The callback URL is public. For the callback signature, please see the event message notification document.
[Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1).
        :type CallbackKey: str
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.StreamBeginNotifyUrl = None
        self.StreamEndNotifyUrl = None
        self.RecordNotifyUrl = None
        self.SnapshotNotifyUrl = None
        self.PornCensorshipNotifyUrl = None
        self.CallbackKey = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        self.StreamBeginNotifyUrl = params.get("StreamBeginNotifyUrl")
        self.StreamEndNotifyUrl = params.get("StreamEndNotifyUrl")
        self.RecordNotifyUrl = params.get("RecordNotifyUrl")
        self.SnapshotNotifyUrl = params.get("SnapshotNotifyUrl")
        self.PornCensorshipNotifyUrl = params.get("PornCensorshipNotifyUrl")
        self.CallbackKey = params.get("CallbackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveCallbackTemplateResponse(AbstractModel):
    """ModifyLiveCallbackTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveCertRequest(AbstractModel):
    """ModifyLiveCert request structure.

    """

    def __init__(self):
        r"""
        :param CertId: Certificate ID.
        :type CertId: str
        :param CertType: Certificate type. 0: user-added certificate, 1: Tencent Cloud-hosted certificate.
        :type CertType: int
        :param CertName: Certificate name.
        :type CertName: str
        :param HttpsCrt: Certificate content, i.e., public key.
        :type HttpsCrt: str
        :param HttpsKey: Private key.
        :type HttpsKey: str
        :param Description: Description.
        :type Description: str
        """
        self.CertId = None
        self.CertType = None
        self.CertName = None
        self.HttpsCrt = None
        self.HttpsKey = None
        self.Description = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.CertType = params.get("CertType")
        self.CertName = params.get("CertName")
        self.HttpsCrt = params.get("HttpsCrt")
        self.HttpsKey = params.get("HttpsKey")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveCertResponse(AbstractModel):
    """ModifyLiveCert response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveDomainCertRequest(AbstractModel):
    """ModifyLiveDomainCert request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Playback domain name.
        :type DomainName: str
        :param CertId: Certificate ID.
        :type CertId: int
        :param Status: Status. 0: off, 1: on.
        :type Status: int
        """
        self.DomainName = None
        self.CertId = None
        self.Status = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.CertId = params.get("CertId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveDomainCertResponse(AbstractModel):
    """ModifyLiveDomainCert response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveDomainRefererRequest(AbstractModel):
    """ModifyLiveDomainReferer request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Playback domain name
        :type DomainName: str
        :param Enable: Whether to enable referer allowlist/blocklist authentication for the current domain name
        :type Enable: int
        :param Type: List type. Valid values: `0` (blocklist), `1` (allowlist)
        :type Type: int
        :param AllowEmpty: Whether to allow empty referer. Valid values: `0` (no), `1` (yes)
        :type AllowEmpty: int
        :param Rules: Referer list. Separate items in it with semicolons (;).
        :type Rules: str
        """
        self.DomainName = None
        self.Enable = None
        self.Type = None
        self.AllowEmpty = None
        self.Rules = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.Type = params.get("Type")
        self.AllowEmpty = params.get("AllowEmpty")
        self.Rules = params.get("Rules")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveDomainRefererResponse(AbstractModel):
    """ModifyLiveDomainReferer response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLivePlayAuthKeyRequest(AbstractModel):
    """ModifyLivePlayAuthKey request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Playback domain name.
        :type DomainName: str
        :param Enable: Whether to enable. 0: disabled; 1: enabled.
If this parameter is left empty, the current value will not be modified.
        :type Enable: int
        :param AuthKey: Authentication key.
If this parameter is left empty, the current value will not be modified.
        :type AuthKey: str
        :param AuthDelta: Validity period in seconds.
If this parameter is left empty, the current value will not be modified.
        :type AuthDelta: int
        :param AuthBackKey: Backup authentication key.
If this parameter is left empty, the current value will not be modified.
        :type AuthBackKey: str
        """
        self.DomainName = None
        self.Enable = None
        self.AuthKey = None
        self.AuthDelta = None
        self.AuthBackKey = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.AuthKey = params.get("AuthKey")
        self.AuthDelta = params.get("AuthDelta")
        self.AuthBackKey = params.get("AuthBackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLivePlayAuthKeyResponse(AbstractModel):
    """ModifyLivePlayAuthKey response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLivePlayDomainRequest(AbstractModel):
    """ModifyLivePlayDomain request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Playback domain name.
        :type DomainName: str
        :param PlayType: Pull domain name type. 1: Mainland China. 2: global, 3: outside Mainland China
        :type PlayType: int
        """
        self.DomainName = None
        self.PlayType = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.PlayType = params.get("PlayType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLivePlayDomainResponse(AbstractModel):
    """ModifyLivePlayDomain response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLivePullStreamTaskRequest(AbstractModel):
    """ModifyLivePullStreamTask request structure.

    """

    def __init__(self):
        r"""
        :param TaskId: The task ID.
        :type TaskId: str
        :param Operator: The operator.
        :type Operator: str
        :param SourceUrls: The source URL(s).
If `SourceType` is `PullLivePushLive`, you can specify only one source URL.
If `SourceType` is `PullVodPushLive`, you can specify at most 30 source URLs.
        :type SourceUrls: list of str
        :param StartTime: The start time.
It must be in UTC format.
Example: 2019-01-08T10:00:00Z.
Note: Beijing time is 8 hours ahead of UTC. The [ISO 8601 format](https://intl.cloud.tencent.com/document/product/266/11732#iso-date-format) is used.
        :type StartTime: str
        :param EndTime: The end time. Notes:
1. The end time must be later than the start time.
2. The end time and start time must be later than the current time.
3. The end time and start time must be less than seven days apart.
It must be in UTC format.
Example: 2019-01-08T10:00:00Z.
Note: Beijing time is 8 hours ahead of UTC. The [ISO 8601 format](https://intl.cloud.tencent.com/document/product/266/11732#iso-date-format) is used.
        :type EndTime: str
        :param VodLoopTimes: The number of times to loop video files.
-1: Loop indefinitely
0: Do not loop
> 0: The number of loop times. A task will end either when the videos are looped for the specified number of times or at the specified task end time, whichever is earlier.
This parameter is valid only if the source is video files.
        :type VodLoopTimes: int
        :param VodRefreshType: The behavior after the source video files (`SourceUrls`) are changed.
ImmediateNewSource: Play the new videos immediately
ContinueBreakPoint: Finish the current video first and then pull from the new source.
This parameter is valid only if the source is video files.
        :type VodRefreshType: str
        :param Status: Whether to enable or pause the task. Valid values:
enable
pause
        :type Status: str
        :param CallbackEvents: The events to listen for. If you do not pass this parameter, all events will be listened for.
TaskStart: Callback for starting a task
TaskExit: Callback for ending a task
VodSourceFileStart: Callback for starting to pull from video files
VodSourceFileFinish: Callback for stopping pulling from video files
ResetTaskConfig: Callback for modifying a task
        :type CallbackEvents: list of str
        :param CallbackUrl: A custom callback URL.
Callbacks will be sent to this URL.
        :type CallbackUrl: str
        :param FileIndex: The index of the video to start from.
The value of this parameter cannot be smaller than 1 or larger than the number of elements in `SourceUrls`.
        :type FileIndex: int
        :param OffsetTime: The playback offset (seconds).
Notes:
1. This parameter should be used together with `FileIndex`.
        :type OffsetTime: int
        :param Comment: The remarks for the task.
        :type Comment: str
        :param BackupSourceType: The backup source type.
PullLivePushLive: Live streaming
PullVodPushLive: Video files
Notes:
1. Backup sources are supported only if the primary source type is live streaming.
2. When pull from the primary source is interrupted, the system will pull from the backup source.
3. If the backup source is a video file, each time the video is finished, the system will check if the primary source is recovered and will switch back if it is.
        :type BackupSourceType: str
        :param BackupSourceUrl: The URL of the backup source.
You can specify only one backup source URL.
        :type BackupSourceUrl: str
        """
        self.TaskId = None
        self.Operator = None
        self.SourceUrls = None
        self.StartTime = None
        self.EndTime = None
        self.VodLoopTimes = None
        self.VodRefreshType = None
        self.Status = None
        self.CallbackEvents = None
        self.CallbackUrl = None
        self.FileIndex = None
        self.OffsetTime = None
        self.Comment = None
        self.BackupSourceType = None
        self.BackupSourceUrl = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Operator = params.get("Operator")
        self.SourceUrls = params.get("SourceUrls")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.VodLoopTimes = params.get("VodLoopTimes")
        self.VodRefreshType = params.get("VodRefreshType")
        self.Status = params.get("Status")
        self.CallbackEvents = params.get("CallbackEvents")
        self.CallbackUrl = params.get("CallbackUrl")
        self.FileIndex = params.get("FileIndex")
        self.OffsetTime = params.get("OffsetTime")
        self.Comment = params.get("Comment")
        self.BackupSourceType = params.get("BackupSourceType")
        self.BackupSourceUrl = params.get("BackupSourceUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLivePullStreamTaskResponse(AbstractModel):
    """ModifyLivePullStreamTask response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLivePushAuthKeyRequest(AbstractModel):
    """ModifyLivePushAuthKey request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Push domain name.
        :type DomainName: str
        :param Enable: Whether to enable. 0: disabled; 1: enabled.
If this parameter is left empty, the current value will not be modified.
        :type Enable: int
        :param MasterAuthKey: Master authentication key.
If this parameter is left empty, the current value will not be modified.
        :type MasterAuthKey: str
        :param BackupAuthKey: Backup authentication key.
If this parameter is left empty, the current value will not be modified.
        :type BackupAuthKey: str
        :param AuthDelta: Validity period in seconds.
        :type AuthDelta: int
        """
        self.DomainName = None
        self.Enable = None
        self.MasterAuthKey = None
        self.BackupAuthKey = None
        self.AuthDelta = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.MasterAuthKey = params.get("MasterAuthKey")
        self.BackupAuthKey = params.get("BackupAuthKey")
        self.AuthDelta = params.get("AuthDelta")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLivePushAuthKeyResponse(AbstractModel):
    """ModifyLivePushAuthKey response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveRecordTemplateRequest(AbstractModel):
    """ModifyLiveRecordTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID obtained through the `DescribeRecordTemplates` API.
        :type TemplateId: int
        :param TemplateName: Template name.
        :type TemplateName: str
        :param Description: Message description
        :type Description: str
        :param FlvParam: FLV recording parameter, which is set when FLV recording is enabled.
        :type FlvParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param HlsParam: HLS recording parameter, which is set when HLS recording is enabled.
        :type HlsParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param Mp4Param: MP4 recording parameter, which is set when MP4 recording is enabled.
        :type Mp4Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param AacParam: AAC recording parameter, which is set when AAC recording is enabled.
        :type AacParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param HlsSpecialParam: Custom HLS recording parameter.
        :type HlsSpecialParam: :class:`tencentcloud.live.v20180801.models.HlsSpecialParam`
        :param Mp3Param: MP3 recording parameter, which is set when MP3 recording is enabled.
        :type Mp3Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param RemoveWatermark: Whether to remove the watermark. This parameter is invalid if `IsDelayLive` is `1`.
        :type RemoveWatermark: bool
        :param FlvSpecialParam: A special parameter for FLV recording.
        :type FlvSpecialParam: :class:`tencentcloud.live.v20180801.models.FlvSpecialParam`
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.FlvParam = None
        self.HlsParam = None
        self.Mp4Param = None
        self.AacParam = None
        self.HlsSpecialParam = None
        self.Mp3Param = None
        self.RemoveWatermark = None
        self.FlvSpecialParam = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        if params.get("FlvParam") is not None:
            self.FlvParam = RecordParam()
            self.FlvParam._deserialize(params.get("FlvParam"))
        if params.get("HlsParam") is not None:
            self.HlsParam = RecordParam()
            self.HlsParam._deserialize(params.get("HlsParam"))
        if params.get("Mp4Param") is not None:
            self.Mp4Param = RecordParam()
            self.Mp4Param._deserialize(params.get("Mp4Param"))
        if params.get("AacParam") is not None:
            self.AacParam = RecordParam()
            self.AacParam._deserialize(params.get("AacParam"))
        if params.get("HlsSpecialParam") is not None:
            self.HlsSpecialParam = HlsSpecialParam()
            self.HlsSpecialParam._deserialize(params.get("HlsSpecialParam"))
        if params.get("Mp3Param") is not None:
            self.Mp3Param = RecordParam()
            self.Mp3Param._deserialize(params.get("Mp3Param"))
        self.RemoveWatermark = params.get("RemoveWatermark")
        if params.get("FlvSpecialParam") is not None:
            self.FlvSpecialParam = FlvSpecialParam()
            self.FlvSpecialParam._deserialize(params.get("FlvSpecialParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveRecordTemplateResponse(AbstractModel):
    """ModifyLiveRecordTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveSnapshotTemplateRequest(AbstractModel):
    """ModifyLiveSnapshotTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param TemplateName: Template name.
Maximum length: 255 bytes.
        :type TemplateName: str
        :param Description: Description.
Maximum length: 1,024 bytes.
        :type Description: str
        :param SnapshotInterval: Screencapturing interval in seconds. Default value: 10s.
Value range: 5-300s.
        :type SnapshotInterval: int
        :param Width: Screenshot width. Default value: 0 (original width).
        :type Width: int
        :param Height: Screenshot height. Default value: 0 (original height).
        :type Height: int
        :param PornFlag: Whether to enable porn detection. Default value: 0.
0: do not enable.
1: enable.
        :type PornFlag: int
        :param CosAppId: COS application ID.
        :type CosAppId: int
        :param CosBucket: COS bucket name.
Note: the value of `CosBucket` cannot contain `-[appid]`.
        :type CosBucket: str
        :param CosRegion: COS region.
        :type CosRegion: str
        :param CosPrefix: COS bucket folder prefix.
        :type CosPrefix: str
        :param CosFileName: COS filename.
        :type CosFileName: str
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.SnapshotInterval = None
        self.Width = None
        self.Height = None
        self.PornFlag = None
        self.CosAppId = None
        self.CosBucket = None
        self.CosRegion = None
        self.CosPrefix = None
        self.CosFileName = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        self.SnapshotInterval = params.get("SnapshotInterval")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.PornFlag = params.get("PornFlag")
        self.CosAppId = params.get("CosAppId")
        self.CosBucket = params.get("CosBucket")
        self.CosRegion = params.get("CosRegion")
        self.CosPrefix = params.get("CosPrefix")
        self.CosFileName = params.get("CosFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveSnapshotTemplateResponse(AbstractModel):
    """ModifyLiveSnapshotTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveTranscodeTemplateRequest(AbstractModel):
    """ModifyLiveTranscodeTemplate request structure.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param Vcodec: Video codec. Valid values: h264, h265, origin (default)

origin: original codec as the output codec
        :type Vcodec: str
        :param Acodec: Audio codec. Defaut value: aac.
Note: this parameter is unsupported now.
        :type Acodec: str
        :param AudioBitrate: Audio bitrate. Default value: 0.
Value range: 0-500.
        :type AudioBitrate: int
        :param Description: Template description.
        :type Description: str
        :param VideoBitrate: Video bitrate in Kbps. Value range: 100-8000.
Note: the transcoding template requires that the bitrate be unique. Therefore, the final saved bitrate may be different from the input bitrate.
        :type VideoBitrate: int
        :param Width: Width in pixels. Value range: 0-3000.
It must be a multiple of 2. The original width is 0.
        :type Width: int
        :param NeedVideo: Whether to keep the video. 0: no; 1: yes. Default value: 1.
        :type NeedVideo: int
        :param NeedAudio: Whether to keep the audio. 0: no; 1: yes. Default value: 1.
        :type NeedAudio: int
        :param Height: Height in pixels. Value range: 0-3000.
It must be a multiple of 2. The original height is 0.
        :type Height: int
        :param Fps: Frame rate in fps. Default value: 0.
Value range: 0-60
        :type Fps: int
        :param Gop: Keyframe interval in seconds.
Value range: 2-6
        :type Gop: int
        :param Rotate: Rotation angle. Default value: 0.
Valid values: 0, 90, 180, 270
        :type Rotate: int
        :param Profile: Encoding quality:
baseline/main/high.
        :type Profile: str
        :param BitrateToOrig: Whether to use the original bitrate when the set bitrate is larger than the original bitrate.
0: no, 1: yes
Default value: 0.
        :type BitrateToOrig: int
        :param HeightToOrig: Whether to use the original height when the set height is higher than the original height.
0: no, 1: yes
Default value: 0.
        :type HeightToOrig: int
        :param FpsToOrig: Whether to use the original frame rate when the set frame rate is larger than the original frame rate.
0: no, 1: yes
Default value: 0.
        :type FpsToOrig: int
        :param AdaptBitratePercent: Bitrate compression ratio of top speed codec video.
Target bitrate of top speed code = VideoBitrate * (1-AdaptBitratePercent)

Value range: 0.0-0.5.
        :type AdaptBitratePercent: float
        :param ShortEdgeAsHeight: Whether to use the short side as the video height. 0: no, 1: yes. Default value: 0.
        :type ShortEdgeAsHeight: int
        :param DRMType: The DRM encryption type. Valid values: fairplay, normalaes, widevine.
If you do not pass this parameter or pass in an empty string, the existing configuration will be reset.
        :type DRMType: str
        :param DRMTracks: The tracks to encrypt. Valid values: AUDIO, SD, HD, UHD1, UHD2. You can choose only one video track (SD, HD, UHD1, or UHD2).
If you do not pass this parameter or pass in an empty string, the existing configuration will be reset.
        :type DRMTracks: str
        """
        self.TemplateId = None
        self.Vcodec = None
        self.Acodec = None
        self.AudioBitrate = None
        self.Description = None
        self.VideoBitrate = None
        self.Width = None
        self.NeedVideo = None
        self.NeedAudio = None
        self.Height = None
        self.Fps = None
        self.Gop = None
        self.Rotate = None
        self.Profile = None
        self.BitrateToOrig = None
        self.HeightToOrig = None
        self.FpsToOrig = None
        self.AdaptBitratePercent = None
        self.ShortEdgeAsHeight = None
        self.DRMType = None
        self.DRMTracks = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Vcodec = params.get("Vcodec")
        self.Acodec = params.get("Acodec")
        self.AudioBitrate = params.get("AudioBitrate")
        self.Description = params.get("Description")
        self.VideoBitrate = params.get("VideoBitrate")
        self.Width = params.get("Width")
        self.NeedVideo = params.get("NeedVideo")
        self.NeedAudio = params.get("NeedAudio")
        self.Height = params.get("Height")
        self.Fps = params.get("Fps")
        self.Gop = params.get("Gop")
        self.Rotate = params.get("Rotate")
        self.Profile = params.get("Profile")
        self.BitrateToOrig = params.get("BitrateToOrig")
        self.HeightToOrig = params.get("HeightToOrig")
        self.FpsToOrig = params.get("FpsToOrig")
        self.AdaptBitratePercent = params.get("AdaptBitratePercent")
        self.ShortEdgeAsHeight = params.get("ShortEdgeAsHeight")
        self.DRMType = params.get("DRMType")
        self.DRMTracks = params.get("DRMTracks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLiveTranscodeTemplateResponse(AbstractModel):
    """ModifyLiveTranscodeTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PlayAuthKeyInfo(AbstractModel):
    """Playback authentication key information.

    """

    def __init__(self):
        r"""
        :param DomainName: Domain name.
        :type DomainName: str
        :param Enable: Whether to enable:
0: disable.
1: enable.
        :type Enable: int
        :param AuthKey: Authentication key.
        :type AuthKey: str
        :param AuthDelta: Validity period in seconds.
        :type AuthDelta: int
        :param AuthBackKey: Authentication `BackKey`.
        :type AuthBackKey: str
        """
        self.DomainName = None
        self.Enable = None
        self.AuthKey = None
        self.AuthDelta = None
        self.AuthBackKey = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.AuthKey = params.get("AuthKey")
        self.AuthDelta = params.get("AuthDelta")
        self.AuthBackKey = params.get("AuthBackKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayCodeTotalInfo(AbstractModel):
    """Total occurrences of each status code. Most HTTP return codes are supported.

    """

    def __init__(self):
        r"""
        :param Code: HTTP code. Valid values:
400, 403, 404, 500, 502, 503, 504.
        :type Code: str
        :param Num: Total occurrences.
        :type Num: int
        """
        self.Code = None
        self.Num = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Num = params.get("Num")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayDataInfoByStream(AbstractModel):
    """Playback information at the stream level.

    """

    def __init__(self):
        r"""
        :param StreamName: Stream name.
        :type StreamName: str
        :param TotalFlux: Total traffic in MB.
        :type TotalFlux: float
        """
        self.StreamName = None
        self.TotalFlux = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.TotalFlux = params.get("TotalFlux")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayStatInfo(AbstractModel):
    """Queries the playback information by ISP and district.

    """

    def __init__(self):
        r"""
        :param Time: Data point in time.
        :type Time: str
        :param Value: Value of bandwidth/traffic/number of requests/number of concurrent connections/download speed. If there is no data returned, the value is 0.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Value: float
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlaySumStatInfo(AbstractModel):
    """Aggregated playback statistics.

    """

    def __init__(self):
        r"""
        :param Name: Domain name or stream ID.
        :type Name: str
        :param AvgFluxPerSecond: Average download speed,
In MB/s.
Calculation formula: average download speed per minute.
        :type AvgFluxPerSecond: float
        :param TotalFlux: Total traffic in MB.
        :type TotalFlux: float
        :param TotalRequest: Total number of requests.
        :type TotalRequest: int
        """
        self.Name = None
        self.AvgFluxPerSecond = None
        self.TotalFlux = None
        self.TotalRequest = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.AvgFluxPerSecond = params.get("AvgFluxPerSecond")
        self.TotalFlux = params.get("TotalFlux")
        self.TotalRequest = params.get("TotalRequest")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProIspPlayCodeDataInfo(AbstractModel):
    """Playback error code information

    """

    def __init__(self):
        r"""
        :param CountryAreaName: Country or region.
        :type CountryAreaName: str
        :param ProvinceName: District.
        :type ProvinceName: str
        :param IspName: ISP.
        :type IspName: str
        :param Code2xx: Occurrences of 2xx error codes.
        :type Code2xx: int
        :param Code3xx: Occurrences of 3xx error codes.
        :type Code3xx: int
        :param Code4xx: Occurrences of 4xx error codes.
        :type Code4xx: int
        :param Code5xx: Occurrences of 5xx error codes.
        :type Code5xx: int
        """
        self.CountryAreaName = None
        self.ProvinceName = None
        self.IspName = None
        self.Code2xx = None
        self.Code3xx = None
        self.Code4xx = None
        self.Code5xx = None


    def _deserialize(self, params):
        self.CountryAreaName = params.get("CountryAreaName")
        self.ProvinceName = params.get("ProvinceName")
        self.IspName = params.get("IspName")
        self.Code2xx = params.get("Code2xx")
        self.Code3xx = params.get("Code3xx")
        self.Code4xx = params.get("Code4xx")
        self.Code5xx = params.get("Code5xx")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishTime(AbstractModel):
    """Push time.

    """

    def __init__(self):
        r"""
        :param PublishTime: Push time.
In UTC format, such as 2018-06-29T19:00:00Z.
        :type PublishTime: str
        """
        self.PublishTime = None


    def _deserialize(self, params):
        self.PublishTime = params.get("PublishTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PullStreamTaskInfo(AbstractModel):
    """The information of a stream pulling task.

    """

    def __init__(self):
        r"""
        :param TaskId: The task ID.
        :type TaskId: str
        :param SourceType: The source type. Valid values:
PullLivePushLive: Live streaming
PullVodPushLive: Video files
        :type SourceType: str
        :param SourceUrls: The source URL(s).
If `SourceType` is `PullLiveToLive`, there can be only one source URL.
If `SourceType` is `PullVodToLive`, there can be at most 10 source URLs.
        :type SourceUrls: list of str
        :param DomainName: The push domain name.
The pulled stream is pushed to this domain.
        :type DomainName: str
        :param AppName: The application to push to.
The pulled stream is pushed to this application.
        :type AppName: str
        :param StreamName: The stream name.
The pulled stream is pushed under this name.
        :type StreamName: str
        :param PushArgs: The push parameter.
A custom push parameter.
        :type PushArgs: str
        :param StartTime: The start time.
It must be in UTC format.
Example: 2019-01-08T10:00:00Z.
Note: Beijing time is 8 hours ahead of UTC. The [ISO 8601 format](https://intl.cloud.tencent.com/document/product/266/11732#iso-date-format) is used.
        :type StartTime: str
        :param EndTime: The end time. Notes:
1. The end time must be later than the start time.
2. The end time and start time must be later than the current time.
3. The end time and start time must be less than seven days apart.
It must be in UTC format.
Example: 2019-01-08T10:00:00Z.
Note: Beijing time is 8 hours ahead of UTC. The [ISO 8601 format](https://intl.cloud.tencent.com/document/product/266/11732#iso-date-format) is used.
        :type EndTime: str
        :param Region: The region of the source (please choose the nearest region).
ap-beijing: North China (Beijing)
ap-shanghai: East China (Shanghai)
ap-guangzhou: South China (Guangzhou)
ap-mumbai: India
        :type Region: str
        :param VodLoopTimes: The number of times to loop video files.
-1: Loop indefinitely
0: Do not loop
> 0: The number of loop times. A task will end either when the videos are looped for the specified number of times or at the specified task end time, whichever is earlier.
This parameter is valid only if the source is video files.
        :type VodLoopTimes: int
        :param VodRefreshType: The behavior after the source video files (`SourceUrls`) are changed.
ImmediateNewSource: Play the new videos immediately
ContinueBreakPoint: Finish the current video first and then pull from the new source.

This parameter is valid only if the source is video files.
        :type VodRefreshType: str
        :param CreateTime: The task creation time.
It must be in UTC format.
Example: 2019-01-08T10:00:00Z.
Note: Beijing time is 8 hours ahead of UTC. The [ISO 8601 format](https://intl.cloud.tencent.com/document/product/266/11732#iso-date-format) is used.
        :type CreateTime: str
        :param UpdateTime: The last updated time.
It must be in UTC format.
Example: 2019-01-08T10:00:00Z.
Note: Beijing time is 8 hours ahead of UTC. The [ISO 8601 format](https://intl.cloud.tencent.com/document/product/266/11732#iso-date-format) is used.
        :type UpdateTime: str
        :param CreateBy: The task creator.
        :type CreateBy: str
        :param UpdateBy: The operator of the last update.
        :type UpdateBy: str
        :param CallbackUrl: The callback URL.
        :type CallbackUrl: str
        :param CallbackEvents: The events to listen for.
TaskStart: Callback for starting a task
TaskExit: Callback for ending a task
VodSourceFileStart: Callback for starting to pull from video files
VodSourceFileFinish: Callback for stopping pulling from video files
ResetTaskConfig: Callback for modifying a task
        :type CallbackEvents: list of str
        :param CallbackInfo: Note: This parameter is not returned currently.
The information of the last callback.
        :type CallbackInfo: str
        :param ErrorInfo: Note: This parameter is not returned currently.
Error message.
        :type ErrorInfo: str
        :param Status: The task status.
enable: Enabled
pause: Paused
        :type Status: str
        :param RecentPullInfo: Note: This parameter is returned only if one task is queried.
The latest pull information.
The information includes the source URL, offset, and report time.
        :type RecentPullInfo: :class:`tencentcloud.live.v20180801.models.RecentPullInfo`
        :param Comment: The remarks for the task.
        :type Comment: str
        """
        self.TaskId = None
        self.SourceType = None
        self.SourceUrls = None
        self.DomainName = None
        self.AppName = None
        self.StreamName = None
        self.PushArgs = None
        self.StartTime = None
        self.EndTime = None
        self.Region = None
        self.VodLoopTimes = None
        self.VodRefreshType = None
        self.CreateTime = None
        self.UpdateTime = None
        self.CreateBy = None
        self.UpdateBy = None
        self.CallbackUrl = None
        self.CallbackEvents = None
        self.CallbackInfo = None
        self.ErrorInfo = None
        self.Status = None
        self.RecentPullInfo = None
        self.Comment = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.SourceType = params.get("SourceType")
        self.SourceUrls = params.get("SourceUrls")
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        self.PushArgs = params.get("PushArgs")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Region = params.get("Region")
        self.VodLoopTimes = params.get("VodLoopTimes")
        self.VodRefreshType = params.get("VodRefreshType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateBy = params.get("CreateBy")
        self.UpdateBy = params.get("UpdateBy")
        self.CallbackUrl = params.get("CallbackUrl")
        self.CallbackEvents = params.get("CallbackEvents")
        self.CallbackInfo = params.get("CallbackInfo")
        self.ErrorInfo = params.get("ErrorInfo")
        self.Status = params.get("Status")
        if params.get("RecentPullInfo") is not None:
            self.RecentPullInfo = RecentPullInfo()
            self.RecentPullInfo._deserialize(params.get("RecentPullInfo"))
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushAuthKeyInfo(AbstractModel):
    """Push authentication key information.

    """

    def __init__(self):
        r"""
        :param DomainName: Domain name.
        :type DomainName: str
        :param Enable: Whether to enable. 0: disabled; 1: enabled.
        :type Enable: int
        :param MasterAuthKey: Master authentication key.
        :type MasterAuthKey: str
        :param BackupAuthKey: Standby authentication key.
        :type BackupAuthKey: str
        :param AuthDelta: Validity period in seconds.
        :type AuthDelta: int
        """
        self.DomainName = None
        self.Enable = None
        self.MasterAuthKey = None
        self.BackupAuthKey = None
        self.AuthDelta = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.MasterAuthKey = params.get("MasterAuthKey")
        self.BackupAuthKey = params.get("BackupAuthKey")
        self.AuthDelta = params.get("AuthDelta")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushDataInfo(AbstractModel):
    """Push information

    """

    def __init__(self):
        r"""
        :param StreamName: Stream name.
        :type StreamName: str
        :param AppName: Push path.
        :type AppName: str
        :param ClientIp: Push client IP.
        :type ClientIp: str
        :param ServerIp: IP of the server that receives the stream.
        :type ServerIp: str
        :param VideoFps: Pushed video frame rate in Hz.
        :type VideoFps: int
        :param VideoSpeed: Video bitrate (bps) for publishing
        :type VideoSpeed: int
        :param AudioFps: Pushed audio frame rate in Hz.
        :type AudioFps: int
        :param AudioSpeed: Audio bitrate (bps) for publishing
        :type AudioSpeed: int
        :param PushDomain: Push domain name.
        :type PushDomain: str
        :param BeginPushTime: Push start time.
        :type BeginPushTime: str
        :param Acodec: Audio codec,
Example: AAC.
        :type Acodec: str
        :param Vcodec: Video codec,
Example: H.264.
        :type Vcodec: str
        :param Resolution: Resolution.
        :type Resolution: str
        :param AsampleRate: Sample rate.
        :type AsampleRate: int
        :param MetaAudioSpeed: Audio bitrate (bps) in metadata
        :type MetaAudioSpeed: int
        :param MetaVideoSpeed: Video bitrate (bps) in metadata
        :type MetaVideoSpeed: int
        :param MetaFps: Frame rate in `metadata`.
        :type MetaFps: int
        """
        self.StreamName = None
        self.AppName = None
        self.ClientIp = None
        self.ServerIp = None
        self.VideoFps = None
        self.VideoSpeed = None
        self.AudioFps = None
        self.AudioSpeed = None
        self.PushDomain = None
        self.BeginPushTime = None
        self.Acodec = None
        self.Vcodec = None
        self.Resolution = None
        self.AsampleRate = None
        self.MetaAudioSpeed = None
        self.MetaVideoSpeed = None
        self.MetaFps = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.AppName = params.get("AppName")
        self.ClientIp = params.get("ClientIp")
        self.ServerIp = params.get("ServerIp")
        self.VideoFps = params.get("VideoFps")
        self.VideoSpeed = params.get("VideoSpeed")
        self.AudioFps = params.get("AudioFps")
        self.AudioSpeed = params.get("AudioSpeed")
        self.PushDomain = params.get("PushDomain")
        self.BeginPushTime = params.get("BeginPushTime")
        self.Acodec = params.get("Acodec")
        self.Vcodec = params.get("Vcodec")
        self.Resolution = params.get("Resolution")
        self.AsampleRate = params.get("AsampleRate")
        self.MetaAudioSpeed = params.get("MetaAudioSpeed")
        self.MetaVideoSpeed = params.get("MetaVideoSpeed")
        self.MetaFps = params.get("MetaFps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecentPullInfo(AbstractModel):
    """The latest pull information.

    """

    def __init__(self):
        r"""
        :param FileUrl: The URL of the file currently pulled.
        :type FileUrl: str
        :param OffsetTime: The offset of the file currently pulled.
        :type OffsetTime: int
        :param ReportTime: The time when the offset is reported, in UTC format.
Example: 2020-07-23T03:20:39Z
Note: Beijing time is 8 hours ahead of UTC.
        :type ReportTime: str
        :param LoopedTimes: The number of times looped.
        :type LoopedTimes: int
        """
        self.FileUrl = None
        self.OffsetTime = None
        self.ReportTime = None
        self.LoopedTimes = None


    def _deserialize(self, params):
        self.FileUrl = params.get("FileUrl")
        self.OffsetTime = params.get("OffsetTime")
        self.ReportTime = params.get("ReportTime")
        self.LoopedTimes = params.get("LoopedTimes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordParam(AbstractModel):
    """Recording template parameter.

    """

    def __init__(self):
        r"""
        :param RecordInterval: Max recording time per file
Default value: `1800` (seconds)
Value range: 30-7200
This parameter is invalid for HLS. Only one HLS file will be generated from push start to push end.
        :type RecordInterval: int
        :param StorageTime: Storage duration of the recording file
Value range: 0-129600000 seconds (0-1500 days)
`0`: permanent
        :type StorageTime: int
        :param Enable: Whether to enable recording in the current format. Default value: 0. 0: no, 1: yes.
        :type Enable: int
        :param VodSubAppId: VOD subapplication ID.
        :type VodSubAppId: int
        :param VodFileName: Recording filename.
Supported special placeholders include:
{StreamID}: stream ID
{StartYear}: start time - year
{StartMonth}: start time - month
{StartDay}: start time - day
{StartHour}: start time - hour
{StartMinute}: start time - minute
{StartSecond}: start time - second
{StartMillisecond}: start time - millisecond
{EndYear}: end time - year
{EndMonth}: end time - month
{EndDay}: end time - day
{EndHour}: end time - hour
{EndMinute}: end time - minute
{EndSecond}: end time - second
{EndMillisecond}: end time - millisecond

If this parameter is not set, the recording filename will be `{StreamID}_{StartYear}-{StartMonth}-{StartDay}-{StartHour}-{StartMinute}-{StartSecond}_{EndYear}-{EndMonth}-{EndDay}-{EndHour}-{EndMinute}-{EndSecond}` by default
        :type VodFileName: str
        :param Procedure: Task flow
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Procedure: str
        :param StorageMode: Video storage class. Valid values:
`normal`: STANDARD
`cold`: STANDARD_IA
Note: this field may return `null`, indicating that no valid value is obtained.
        :type StorageMode: str
        :param ClassId: VOD subapplication category
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ClassId: int
        """
        self.RecordInterval = None
        self.StorageTime = None
        self.Enable = None
        self.VodSubAppId = None
        self.VodFileName = None
        self.Procedure = None
        self.StorageMode = None
        self.ClassId = None


    def _deserialize(self, params):
        self.RecordInterval = params.get("RecordInterval")
        self.StorageTime = params.get("StorageTime")
        self.Enable = params.get("Enable")
        self.VodSubAppId = params.get("VodSubAppId")
        self.VodFileName = params.get("VodFileName")
        self.Procedure = params.get("Procedure")
        self.StorageMode = params.get("StorageMode")
        self.ClassId = params.get("ClassId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecordTemplateInfo(AbstractModel):
    """Recording template information

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param TemplateName: Template name.
        :type TemplateName: str
        :param Description: Message description
        :type Description: str
        :param FlvParam: FLV recording parameter.
        :type FlvParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param HlsParam: HLS recording parameter.
        :type HlsParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param Mp4Param: MP4 recording parameter.
        :type Mp4Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param AacParam: AAC recording parameter.
        :type AacParam: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param IsDelayLive: 0: LVB,
1: LCB.
        :type IsDelayLive: int
        :param HlsSpecialParam: A special parameter for HLS recording.
        :type HlsSpecialParam: :class:`tencentcloud.live.v20180801.models.HlsSpecialParam`
        :param Mp3Param: MP3 recording parameter.
        :type Mp3Param: :class:`tencentcloud.live.v20180801.models.RecordParam`
        :param RemoveWatermark: Whether the watermark is removed.
Note: This field may return `null`, indicating that no valid value was found.
        :type RemoveWatermark: bool
        :param FlvSpecialParam: A special parameter for FLV recording.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FlvSpecialParam: :class:`tencentcloud.live.v20180801.models.FlvSpecialParam`
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.FlvParam = None
        self.HlsParam = None
        self.Mp4Param = None
        self.AacParam = None
        self.IsDelayLive = None
        self.HlsSpecialParam = None
        self.Mp3Param = None
        self.RemoveWatermark = None
        self.FlvSpecialParam = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        if params.get("FlvParam") is not None:
            self.FlvParam = RecordParam()
            self.FlvParam._deserialize(params.get("FlvParam"))
        if params.get("HlsParam") is not None:
            self.HlsParam = RecordParam()
            self.HlsParam._deserialize(params.get("HlsParam"))
        if params.get("Mp4Param") is not None:
            self.Mp4Param = RecordParam()
            self.Mp4Param._deserialize(params.get("Mp4Param"))
        if params.get("AacParam") is not None:
            self.AacParam = RecordParam()
            self.AacParam._deserialize(params.get("AacParam"))
        self.IsDelayLive = params.get("IsDelayLive")
        if params.get("HlsSpecialParam") is not None:
            self.HlsSpecialParam = HlsSpecialParam()
            self.HlsSpecialParam._deserialize(params.get("HlsSpecialParam"))
        if params.get("Mp3Param") is not None:
            self.Mp3Param = RecordParam()
            self.Mp3Param._deserialize(params.get("Mp3Param"))
        self.RemoveWatermark = params.get("RemoveWatermark")
        if params.get("FlvSpecialParam") is not None:
            self.FlvSpecialParam = FlvSpecialParam()
            self.FlvSpecialParam._deserialize(params.get("FlvSpecialParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefererAuthConfig(AbstractModel):
    """Referer allowlist/blocklist configuration of a live streaming domain name

    """

    def __init__(self):
        r"""
        :param DomainName: Domain name
        :type DomainName: str
        :param Enable: Whether to enable referer. Valid values: `0` (no), `1` (yes)
        :type Enable: int
        :param Type: List type. Valid values: `0` (blocklist), `1` (allowlist)
        :type Type: int
        :param AllowEmpty: Whether to allow empty referer. Valid values: `0` (no), `1` (yes)
        :type AllowEmpty: int
        :param Rules: Referer list. Separate items in it with semicolons (;).
        :type Rules: str
        """
        self.DomainName = None
        self.Enable = None
        self.Type = None
        self.AllowEmpty = None
        self.Rules = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Enable = params.get("Enable")
        self.Type = params.get("Type")
        self.AllowEmpty = params.get("AllowEmpty")
        self.Rules = params.get("Rules")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeDelayLiveStreamRequest(AbstractModel):
    """ResumeDelayLiveStream request structure.

    """

    def __init__(self):
        r"""
        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.
        :type AppName: str
        :param DomainName: Push domain name.
        :type DomainName: str
        :param StreamName: Stream name.
        :type StreamName: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeDelayLiveStreamResponse(AbstractModel):
    """ResumeDelayLiveStream response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResumeLiveStreamRequest(AbstractModel):
    """ResumeLiveStream request structure.

    """

    def __init__(self):
        r"""
        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.
        :type AppName: str
        :param DomainName: Your push domain name.
        :type DomainName: str
        :param StreamName: Stream name.
        :type StreamName: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeLiveStreamResponse(AbstractModel):
    """ResumeLiveStream response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RuleInfo(AbstractModel):
    """Rule information.

    """

    def __init__(self):
        r"""
        :param CreateTime: Rule creation time.
        :type CreateTime: str
        :param UpdateTime: Rule update time.
        :type UpdateTime: str
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param DomainName: Push domain name.
        :type DomainName: str
        :param AppName: Push path.
        :type AppName: str
        :param StreamName: Stream name.
        :type StreamName: str
        """
        self.CreateTime = None
        self.UpdateTime = None
        self.TemplateId = None
        self.DomainName = None
        self.AppName = None
        self.StreamName = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.TemplateId = params.get("TemplateId")
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        self.StreamName = params.get("StreamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SnapshotTemplateInfo(AbstractModel):
    """Screencapturing template information.

    """

    def __init__(self):
        r"""
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param TemplateName: Template name.
        :type TemplateName: str
        :param SnapshotInterval: Screencapturing interval. Value range: 5-300s.
        :type SnapshotInterval: int
        :param Width: Screenshot width. Value range: 0-3000. 
0: original width and fit to the original ratio.
        :type Width: int
        :param Height: Screenshot height. Value range: 0-2000.
0: original height and fit to the original ratio.
        :type Height: int
        :param PornFlag: Whether to enable porn detection. 0: no, 1: yes.
        :type PornFlag: int
        :param CosAppId: COS application ID.
        :type CosAppId: int
        :param CosBucket: COS bucket name.
        :type CosBucket: str
        :param CosRegion: COS region.
        :type CosRegion: str
        :param Description: Template description.
        :type Description: str
        :param CosPrefix: COS bucket folder prefix.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CosPrefix: str
        :param CosFileName: COS filename.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CosFileName: str
        """
        self.TemplateId = None
        self.TemplateName = None
        self.SnapshotInterval = None
        self.Width = None
        self.Height = None
        self.PornFlag = None
        self.CosAppId = None
        self.CosBucket = None
        self.CosRegion = None
        self.Description = None
        self.CosPrefix = None
        self.CosFileName = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.SnapshotInterval = params.get("SnapshotInterval")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.PornFlag = params.get("PornFlag")
        self.CosAppId = params.get("CosAppId")
        self.CosBucket = params.get("CosBucket")
        self.CosRegion = params.get("CosRegion")
        self.Description = params.get("Description")
        self.CosPrefix = params.get("CosPrefix")
        self.CosFileName = params.get("CosFileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopLiveRecordRequest(AbstractModel):
    """StopLiveRecord request structure.

    """

    def __init__(self):
        r"""
        :param StreamName: Stream name.
        :type StreamName: str
        :param TaskId: Task ID returned by the `CreateLiveRecord` API.
        :type TaskId: int
        """
        self.StreamName = None
        self.TaskId = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopLiveRecordResponse(AbstractModel):
    """StopLiveRecord response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopRecordTaskRequest(AbstractModel):
    """StopRecordTask request structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Recording task ID.
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopRecordTaskResponse(AbstractModel):
    """StopRecordTask response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StreamEventInfo(AbstractModel):
    """Streaming event information.

    """

    def __init__(self):
        r"""
        :param AppName: Application name.
        :type AppName: str
        :param DomainName: Push domain name.
        :type DomainName: str
        :param StreamName: Stream name.
        :type StreamName: str
        :param StreamStartTime: Push start time.
In UTC format, such as 2019-01-07T12:00:00Z.
        :type StreamStartTime: str
        :param StreamEndTime: Push end time.
In UTC format, such as 2019-01-07T15:00:00Z.
        :type StreamEndTime: str
        :param StopReason: Stop reason.
        :type StopReason: str
        :param Duration: Push duration in seconds.
        :type Duration: int
        :param ClientIp: Host IP.
        :type ClientIp: str
        :param Resolution: Resolution.
        :type Resolution: str
        """
        self.AppName = None
        self.DomainName = None
        self.StreamName = None
        self.StreamStartTime = None
        self.StreamEndTime = None
        self.StopReason = None
        self.Duration = None
        self.ClientIp = None
        self.Resolution = None


    def _deserialize(self, params):
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamName = params.get("StreamName")
        self.StreamStartTime = params.get("StreamStartTime")
        self.StreamEndTime = params.get("StreamEndTime")
        self.StopReason = params.get("StopReason")
        self.Duration = params.get("Duration")
        self.ClientIp = params.get("ClientIp")
        self.Resolution = params.get("Resolution")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamName(AbstractModel):
    """Stream name list.

    """

    def __init__(self):
        r"""
        :param StreamName: Stream name.
        :type StreamName: str
        :param AppName: Application name.
        :type AppName: str
        :param DomainName: Push domain name.
        :type DomainName: str
        :param StreamStartTime: Push start time.
In UTC format, such as 2019-01-07T12:00:00Z.
        :type StreamStartTime: str
        :param StreamEndTime: Push end time.
In UTC format, such as 2019-01-07T15:00:00Z.
        :type StreamEndTime: str
        :param StopReason: Stop reason.
        :type StopReason: str
        :param Duration: Push duration in seconds.
        :type Duration: int
        :param ClientIp: Host IP.
        :type ClientIp: str
        :param Resolution: Resolution.
        :type Resolution: str
        """
        self.StreamName = None
        self.AppName = None
        self.DomainName = None
        self.StreamStartTime = None
        self.StreamEndTime = None
        self.StopReason = None
        self.Duration = None
        self.ClientIp = None
        self.Resolution = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        self.StreamStartTime = params.get("StreamStartTime")
        self.StreamEndTime = params.get("StreamEndTime")
        self.StopReason = params.get("StopReason")
        self.Duration = params.get("Duration")
        self.ClientIp = params.get("ClientIp")
        self.Resolution = params.get("Resolution")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StreamOnlineInfo(AbstractModel):
    """Queries active push information

    """

    def __init__(self):
        r"""
        :param StreamName: Stream name.
        :type StreamName: str
        :param PublishTimeList: Push time list
        :type PublishTimeList: list of PublishTime
        :param AppName: Application name.
        :type AppName: str
        :param DomainName: Push domain name.
        :type DomainName: str
        """
        self.StreamName = None
        self.PublishTimeList = None
        self.AppName = None
        self.DomainName = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        if params.get("PublishTimeList") is not None:
            self.PublishTimeList = []
            for item in params.get("PublishTimeList"):
                obj = PublishTime()
                obj._deserialize(item)
                self.PublishTimeList.append(obj)
        self.AppName = params.get("AppName")
        self.DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateInfo(AbstractModel):
    """Transcoding template information.

    """

    def __init__(self):
        r"""
        :param Vcodec: Codec: h264/h265/origin. Default value: h264.

origin: keep the original codec.
        :type Vcodec: str
        :param VideoBitrate: Video bitrate. Value range: 0–8,000 Kbps.
If the value is 0, the original bitrate will be retained.
Note: transcoding templates require a unique bitrate. The final saved bitrate may differ from the input bitrate.
        :type VideoBitrate: int
        :param Acodec: Audio codec: aac. Default value: aac.
Note: This parameter will not take effect for now and will be supported soon.
        :type Acodec: str
        :param AudioBitrate: Audio bitrate. Value range: 0–500 Kbps.
0 by default.
        :type AudioBitrate: int
        :param Width: Width. Default value: 0.
Value range: [0-3,000].
The value must be a multiple of 2. The original width is 0.
        :type Width: int
        :param Height: Height. Default value: 0.
Value range: [0-3,000].
The value must be a multiple of 2. The original width is 0.
        :type Height: int
        :param Fps: Frame rate. Default value: 0.
Range: 0-60 Fps.
        :type Fps: int
        :param Gop: Keyframe interval, unit: second.
Original interval by default
Range: 2-6
        :type Gop: int
        :param Rotate: Rotation angle. Default value: 0.
Value range: 0, 90, 180, 270
        :type Rotate: int
        :param Profile: Encoding quality:
baseline/main/high. Default value: baseline.
        :type Profile: str
        :param BitrateToOrig: Whether to use the original bitrate when the set bitrate is larger than the original bitrate.
0: no, 1: yes
Default value: 0.
        :type BitrateToOrig: int
        :param HeightToOrig: Whether to use the original height when the set height is higher than the original height.
0: no, 1: yes
Default value: 0.
        :type HeightToOrig: int
        :param FpsToOrig: Whether to use the original frame rate when the set frame rate is larger than the original frame rate.
0: no, 1: yes
Default value: 0.
        :type FpsToOrig: int
        :param NeedVideo: Whether to keep the video. 0: no; 1: yes.
        :type NeedVideo: int
        :param NeedAudio: Whether to keep the audio. 0: no; 1: yes.
        :type NeedAudio: int
        :param TemplateId: Template ID.
        :type TemplateId: int
        :param TemplateName: Template name.
        :type TemplateName: str
        :param Description: Template description.
        :type Description: str
        :param AiTransCode: Whether it is a top speed codec template. 0: no, 1: yes. Default value: 0.
        :type AiTransCode: int
        :param AdaptBitratePercent: Bitrate compression ratio of top speed code video.
Target bitrate of top speed code = VideoBitrate * (1-AdaptBitratePercent)

Value range: 0.0-0.5.
        :type AdaptBitratePercent: float
        :param ShortEdgeAsHeight: Whether to take the shorter side as height. 0: no, 1: yes. Default value: 0.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ShortEdgeAsHeight: int
        :param DRMType: The DRM encryption type. Valid values: fairplay, normalaes, widevine.
Note: This field may return null, indicating that no valid values can be obtained.
        :type DRMType: str
        :param DRMTracks: The tracks to encrypt. Valid values: AUDIO, SD, HD, UHD1, UHD2. Separate multiple tracks with “|”. You can choose only one video track (SD, HD, UHD1, or UHD2).
Note: This field may return null, indicating that no valid values can be obtained.
        :type DRMTracks: str
        """
        self.Vcodec = None
        self.VideoBitrate = None
        self.Acodec = None
        self.AudioBitrate = None
        self.Width = None
        self.Height = None
        self.Fps = None
        self.Gop = None
        self.Rotate = None
        self.Profile = None
        self.BitrateToOrig = None
        self.HeightToOrig = None
        self.FpsToOrig = None
        self.NeedVideo = None
        self.NeedAudio = None
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.AiTransCode = None
        self.AdaptBitratePercent = None
        self.ShortEdgeAsHeight = None
        self.DRMType = None
        self.DRMTracks = None


    def _deserialize(self, params):
        self.Vcodec = params.get("Vcodec")
        self.VideoBitrate = params.get("VideoBitrate")
        self.Acodec = params.get("Acodec")
        self.AudioBitrate = params.get("AudioBitrate")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Fps = params.get("Fps")
        self.Gop = params.get("Gop")
        self.Rotate = params.get("Rotate")
        self.Profile = params.get("Profile")
        self.BitrateToOrig = params.get("BitrateToOrig")
        self.HeightToOrig = params.get("HeightToOrig")
        self.FpsToOrig = params.get("FpsToOrig")
        self.NeedVideo = params.get("NeedVideo")
        self.NeedAudio = params.get("NeedAudio")
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        self.AiTransCode = params.get("AiTransCode")
        self.AdaptBitratePercent = params.get("AdaptBitratePercent")
        self.ShortEdgeAsHeight = params.get("ShortEdgeAsHeight")
        self.DRMType = params.get("DRMType")
        self.DRMTracks = params.get("DRMTracks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeShiftBillData(AbstractModel):
    """The time shifting billing data.

    """

    def __init__(self):
        r"""
        :param Domain: The push domain name.
        :type Domain: str
        :param Duration: The time-shift video length (minutes).
        :type Duration: float
        :param StoragePeriod: The time-shift days.
        :type StoragePeriod: float
        :param Time: The time for the data returned. Format: YYYY-MM-DDThh:mm:ssZ.
        :type Time: str
        :param TotalDuration: The total time-shift duration (minutes).
        :type TotalDuration: float
        """
        self.Domain = None
        self.Duration = None
        self.StoragePeriod = None
        self.Time = None
        self.TotalDuration = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Duration = params.get("Duration")
        self.StoragePeriod = params.get("StoragePeriod")
        self.Time = params.get("Time")
        self.TotalDuration = params.get("TotalDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeValue(AbstractModel):
    """Metric value at a specified point in time.

    """

    def __init__(self):
        r"""
        :param Time: UTC time in the format of `yyyy-mm-ddTHH:MM:SSZ`.
        :type Time: str
        :param Num: Value.
        :type Num: int
        """
        self.Time = None
        self.Num = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Num = params.get("Num")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscodeDetailInfo(AbstractModel):
    """Transcoding details.

    """

    def __init__(self):
        r"""
        :param StreamName: Stream name.
        :type StreamName: str
        :param StartTime: Start time (Beijing time) in the format of `yyyy-mm-dd HH:MM`.
        :type StartTime: str
        :param EndTime: End time (Beijing time) in the format of `yyyy-mm-dd HH:MM`.
        :type EndTime: str
        :param Duration: Transcoding duration in minutes.
Note: given the possible interruptions during push, duration here is the sum of actual duration of transcoding instead of the interval between the start time and end time.
        :type Duration: int
        :param ModuleCodec: Codec with modules,
Example:
liveprocessor_H264: LVB transcoding - H264,
liveprocessor_H265: LVB transcoding - H265,
topspeed_H264: top speed codec - H264,
topspeed_H265: top speed codec - H265.
        :type ModuleCodec: str
        :param Bitrate: Bitrate.
        :type Bitrate: int
        :param Type: Type. Valid values: Transcode, MixStream, WaterMark.
        :type Type: str
        :param PushDomain: Push domain name.
        :type PushDomain: str
        :param Resolution: Resolution.
        :type Resolution: str
        """
        self.StreamName = None
        self.StartTime = None
        self.EndTime = None
        self.Duration = None
        self.ModuleCodec = None
        self.Bitrate = None
        self.Type = None
        self.PushDomain = None
        self.Resolution = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Duration = params.get("Duration")
        self.ModuleCodec = params.get("ModuleCodec")
        self.Bitrate = params.get("Bitrate")
        self.Type = params.get("Type")
        self.PushDomain = params.get("PushDomain")
        self.Resolution = params.get("Resolution")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TranscodeTotalInfo(AbstractModel):
    """Total usage of the transcoding service

    """

    def __init__(self):
        r"""
        :param Time: Usage time (Beijing time)
Example: 2019-03-01 00:00:00
        :type Time: str
        :param Duration: Transcoding duration in minutes
        :type Duration: int
        :param ModuleCodec: Codec, with modules
Examples:
`liveprocessor_H264`: live transcoding-H264
`liveprocessor_H265`: live transcoding-H265
`topspeed_H264`: top speed codec-H264
`topspeed_H265`: top speed codec-H265
        :type ModuleCodec: str
        :param Resolution: Resolution
Example: 540*480
        :type Resolution: str
        """
        self.Time = None
        self.Duration = None
        self.ModuleCodec = None
        self.Resolution = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Duration = params.get("Duration")
        self.ModuleCodec = params.get("ModuleCodec")
        self.Resolution = params.get("Resolution")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindLiveDomainCertRequest(AbstractModel):
    """UnBindLiveDomainCert request structure.

    """

    def __init__(self):
        r"""
        :param DomainName: Playback domain name.
        :type DomainName: str
        :param Type: Valid values:
`gray`: unbind the canary certificate
`formal` (default): unbind the formal certificate

`formal` will be used if no value is passed in
        :type Type: str
        """
        self.DomainName = None
        self.Type = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindLiveDomainCertResponse(AbstractModel):
    """UnBindLiveDomainCert response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateLiveWatermarkRequest(AbstractModel):
    """UpdateLiveWatermark request structure.

    """

    def __init__(self):
        r"""
        :param WatermarkId: Watermark ID.
Get the watermark ID in the returned value of the [AddLiveWatermark](https://intl.cloud.tencent.com/document/product/267/30154?from_cn_redirect=1) API call.
        :type WatermarkId: int
        :param PictureUrl: Watermark image URL.
Unallowed characters in the URL:
 ;(){}$>`#"\'|
        :type PictureUrl: str
        :param XPosition: Display position: X-axis offset in %. Default value: 0.
        :type XPosition: int
        :param YPosition: Display position: Y-axis offset in %. Default value: 0.
        :type YPosition: int
        :param WatermarkName: Watermark name.
Up to 16 bytes.
        :type WatermarkName: str
        :param Width: Watermark width or its percentage of the live streaming video width. It is recommended to just specify either height or width as the other will be scaled proportionally to avoid distortions. The original width is used by default.
        :type Width: int
        :param Height: Watermark height or its percentage of the live streaming video width. It is recommended to just specify either height or width as the other will be scaled proportionally to avoid distortions. The original height is used by default.
        :type Height: int
        """
        self.WatermarkId = None
        self.PictureUrl = None
        self.XPosition = None
        self.YPosition = None
        self.WatermarkName = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        self.PictureUrl = params.get("PictureUrl")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")
        self.WatermarkName = params.get("WatermarkName")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateLiveWatermarkResponse(AbstractModel):
    """UpdateLiveWatermark response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class WatermarkInfo(AbstractModel):
    """Watermark information.

    """

    def __init__(self):
        r"""
        :param WatermarkId: Watermark ID.
        :type WatermarkId: int
        :param PictureUrl: Watermark image URL.
        :type PictureUrl: str
        :param XPosition: Display position: X-axis offset.
        :type XPosition: int
        :param YPosition: Display position: Y-axis offset.
        :type YPosition: int
        :param WatermarkName: Watermark name.
        :type WatermarkName: str
        :param Status: Current status. 0: not used. 1: in use.
        :type Status: int
        :param CreateTime: Creation time.
        :type CreateTime: str
        :param Width: Watermark width.
        :type Width: int
        :param Height: Watermark height.
        :type Height: int
        """
        self.WatermarkId = None
        self.PictureUrl = None
        self.XPosition = None
        self.YPosition = None
        self.WatermarkName = None
        self.Status = None
        self.CreateTime = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        self.PictureUrl = params.get("PictureUrl")
        self.XPosition = params.get("XPosition")
        self.YPosition = params.get("YPosition")
        self.WatermarkName = params.get("WatermarkName")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        