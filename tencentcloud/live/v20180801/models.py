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
        """
        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.\n        :type AppName: str\n        :param DomainName: Push domain name.\n        :type DomainName: str\n        :param StreamName: Stream name.\n        :type StreamName: str\n        :param DelayTime: Delay time in seconds, up to 600s.\n        :type DelayTime: int\n        :param ExpireTime: Expiration time of the configured delayed playback in UTC format, such as 2018-11-29T19:00:00Z.
Notes:
1. The configuration will expire after 7 days by default and can last up to 7 days.
2. The Beijing time is in UTC+8. This value should be in the format as required by ISO 8601. For more information, please see [ISO Date and Time Format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).\n        :type ExpireTime: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddLiveDomainRequest(AbstractModel):
    """AddLiveDomain request structure.

    """

    def __init__(self):
        """
        :param DomainName: Domain name.\n        :type DomainName: str\n        :param DomainType: Domain name type.
0: push domain name.
1: playback domain name.\n        :type DomainType: int\n        :param PlayType: Pull domain name type:
1: Mainland China.
2: global.
3: outside Mainland China.
Default value: 1.\n        :type PlayType: int\n        :param IsDelayLive: Whether it is LCB:
0: LVB,
1: LCB.
Default value: 0.\n        :type IsDelayLive: int\n        :param IsMiniProgramLive: Whether it is LVB on Mini Program.
0: LVB.
1: LVB on Mini Program.
Default value: 0.\n        :type IsMiniProgramLive: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddLiveWatermarkRequest(AbstractModel):
    """AddLiveWatermark request structure.

    """

    def __init__(self):
        """
        :param PictureUrl: Watermark image URL.
Unallowed characters in the URL:
 ;(){}$>`#"\'|\n        :type PictureUrl: str\n        :param WatermarkName: Watermark name.
Up to 16 bytes.\n        :type WatermarkName: str\n        :param XPosition: Display position: X-axis offset in %. Default value: 0.\n        :type XPosition: int\n        :param YPosition: Display position: Y-axis offset in %. Default value: 0.\n        :type YPosition: int\n        :param Width: Watermark width or its percentage of the live streaming video width. It is recommended to just specify either height or width as the other will be scaled proportionally to avoid distortions. The original width is used by default.\n        :type Width: int\n        :param Height: Watermark height, which is set by entering a percentage of the live stream image’s original height. You are advised to set either the height or width as the other will be scaled proportionally to avoid distortions. Default value: original height.\n        :type Height: int\n        """
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
        """
        :param WatermarkId: Watermark ID.\n        :type WatermarkId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.WatermarkId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WatermarkId = params.get("WatermarkId")
        self.RequestId = params.get("RequestId")


class BandwidthInfo(AbstractModel):
    """Bandwidth information

    """

    def __init__(self):
        """
        :param Time: Format of return value:
yyyy-mm-dd HH:MM:SS
The time accuracy matches with the query granularity.\n        :type Time: str\n        :param Bandwidth: Bandwidth.\n        :type Bandwidth: float\n        """
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
        


class BillAreaInfo(AbstractModel):
    """Region information, `DescribeAreaBillBandwidthAndFluxList` output parameter

    """

    def __init__(self):
        """
        :param Name: Region name\n        :type Name: str\n        :param Countrys: Detailed country information\n        :type Countrys: list of BillCountryInfo\n        """
        self.Name = None
        self.Countrys = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Countrys") is not None:
            self.Countrys = []
            for item in params.get("Countrys"):
                obj = BillCountryInfo()
                obj._deserialize(item)
                self.Countrys.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillCountryInfo(AbstractModel):
    """The bandwidth information of a country, `DescribeAreaBillBandwidthAndFluxList` output parameter

    """

    def __init__(self):
        """
        :param Name: Country\n        :type Name: str\n        :param BandInfoList: Detailed bandwidth information\n        :type BandInfoList: list of BillDataInfo\n        """
        self.Name = None
        self.BandInfoList = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("BandInfoList") is not None:
            self.BandInfoList = []
            for item in params.get("BandInfoList"):
                obj = BillDataInfo()
                obj._deserialize(item)
                self.BandInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillDataInfo(AbstractModel):
    """Bandwidth and traffic information.

    """

    def __init__(self):
        """
        :param Time: Time point in the format of `yyyy-mm-dd HH:MM:SS`.\n        :type Time: str\n        :param Bandwidth: Bandwidth in Mbps.\n        :type Bandwidth: float\n        :param Flux: Traffic in MB.\n        :type Flux: float\n        :param PeakTime: Time point of peak value in the format of `yyyy-mm-dd HH:MM:SS`. As raw data is at a 5-minute granularity, if data at a 1-hour or 1-day granularity is queried, the time point of peak bandwidth value at the corresponding granularity will be returned.\n        :type PeakTime: str\n        """
        self.Time = None
        self.Bandwidth = None
        self.Flux = None
        self.PeakTime = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Bandwidth = params.get("Bandwidth")
        self.Flux = params.get("Flux")
        self.PeakTime = params.get("PeakTime")
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
        """
        :param CertId: Certificate ID, which can be obtained through the `CreateLiveCert` API.\n        :type CertId: int\n        :param DomainName: Playback domain name.\n        :type DomainName: str\n        :param Status: HTTPS status. 0: disabled, 1: enabled.\n        :type Status: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CallBackRuleInfo(AbstractModel):
    """Rule information

    """

    def __init__(self):
        """
        :param CreateTime: Rule creation time.\n        :type CreateTime: str\n        :param UpdateTime: Rule update time.\n        :type UpdateTime: str\n        :param TemplateId: Template ID.\n        :type TemplateId: int\n        :param DomainName: Push domain name.\n        :type DomainName: str\n        :param AppName: Push path.\n        :type AppName: str\n        """
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
        """
        :param TemplateId: Template ID.\n        :type TemplateId: int\n        :param TemplateName: Template name.\n        :type TemplateName: str\n        :param Description: Description.\n        :type Description: str\n        :param StreamBeginNotifyUrl: Stream starting callback URL.\n        :type StreamBeginNotifyUrl: str\n        :param StreamMixNotifyUrl: Stream mixing callback URL (disused)\n        :type StreamMixNotifyUrl: str\n        :param StreamEndNotifyUrl: Interruption callback URL.\n        :type StreamEndNotifyUrl: str\n        :param RecordNotifyUrl: Recording callback URL.\n        :type RecordNotifyUrl: str\n        :param SnapshotNotifyUrl: Screencapturing callback URL.\n        :type SnapshotNotifyUrl: str\n        :param PornCensorshipNotifyUrl: Porn detection callback URL.\n        :type PornCensorshipNotifyUrl: str\n        :param CallbackKey: Callback authentication key.\n        :type CallbackKey: str\n        """
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
        """
        :param MixStreamSessionId: ID of stream mix session (from applying for stream mix to canceling stream mix).
This value is the same as the `MixStreamSessionId` in `CreateCommonMixStream`.\n        :type MixStreamSessionId: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CdnPlayStatData(AbstractModel):
    """Downstream playback statistical metrics

    """

    def __init__(self):
        """
        :param Time: Time point in the format of `yyyy-mm-dd HH:MM:SS`.\n        :type Time: str\n        :param Bandwidth: Bandwidth in Mbps.\n        :type Bandwidth: float\n        :param Flux: Traffic in MB.\n        :type Flux: float\n        :param Request: Number of new requests.\n        :type Request: int\n        :param Online: Number of concurrent connections.\n        :type Online: int\n        """
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
        """
        :param CertId: Certificate ID.\n        :type CertId: int\n        :param CertName: Certificate name.\n        :type CertName: str\n        :param Description: Description.\n        :type Description: str\n        :param CreateTime: Creation time in UTC format.\n        :type CreateTime: str\n        :param HttpsCrt: Certificate content.\n        :type HttpsCrt: str\n        :param CertType: Certificate type.
0: user-added certificate
1: Tencent Cloud-hosted certificate\n        :type CertType: int\n        :param CertExpireTime: Certificate expiration time in UTC format.\n        :type CertExpireTime: str\n        :param DomainList: List of domain names that use this certificate.\n        :type DomainList: list of str\n        """
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
        """
        :param ClientIp: Client IP in dotted-decimal notation.\n        :type ClientIp: str\n        :param Province: District where the client is located.\n        :type Province: str\n        :param TotalFlux: Total traffic.\n        :type TotalFlux: float\n        :param TotalRequest: Total number of requests.\n        :type TotalRequest: int\n        :param TotalFailedRequest: Total number of failed requests.\n        :type TotalFailedRequest: int\n        :param CountryArea: Country/region where the client is located.\n        :type CountryArea: str\n        """
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
        """
        :param UseMixCropCenter: Value range: [0,1]. 
If 1 is entered, when the layer resolution in the parameter is different from the actual video resolution, the video will be automatically cropped according to the resolution set by the layer.\n        :type UseMixCropCenter: int\n        :param AllowCopy: Value range: [0,1].
If this parameter is set to 1, when both `InputStreamList` and `OutputParams.OutputStreamType` are set to 1, you can copy a stream instead of canceling it.\n        :type AllowCopy: int\n        :param PassInputSei: Valid values: 0, 1
If you set this parameter to 1, SEI (Supplemental Enhanced Information) of the input streams will be passed through.\n        :type PassInputSei: int\n        """
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
        """
        :param CropWidth: Crop width. Value range: [0,2000].\n        :type CropWidth: float\n        :param CropHeight: Crop height. Value range: [0,2000].\n        :type CropHeight: float\n        :param CropStartLocationX: Starting crop X coordinate. Value range: [0,2000].\n        :type CropStartLocationX: float\n        :param CropStartLocationY: Starting crop Y coordinate. Value range: [0,2000].\n        :type CropStartLocationY: float\n        """
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
        """
        :param InputStreamName: Input stream name of up to 80 bytes, which is a string containing letters, digits, and underscores.\n        :type InputStreamName: str\n        :param LayoutParams: Input stream layout parameter.\n        :type LayoutParams: :class:`tencentcloud.live.v20180801.models.CommonMixLayoutParams`\n        :param CropParams: Input stream crop parameter.\n        :type CropParams: :class:`tencentcloud.live.v20180801.models.CommonMixCropParams`\n        """
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
        """
        :param ImageLayer: Input layer. Value range: [1,16].
1) For `image_layer` of background stream (i.e., main host video image or canvas), enter 1.
2) For audio stream mix, this parameter is also required.\n        :type ImageLayer: int\n        :param InputType: Input type. Value range: [0,5].
If this parameter is left empty, 0 will be used by default.
0: the input stream is audio/video.
2: the input stream is image.
3: the input stream is canvas. 
4: the input stream is audio.
5: the input stream is pure video.\n        :type InputType: int\n        :param ImageWidth: Output width of input video image. Value range:
Pixel: [0,2000]
Percentage: [0.01,0.99]
If this parameter is left empty, the input stream width will be used by default.
If percentage is used, the expected output is (percentage * background width).\n        :type ImageWidth: float\n        :param ImageHeight: Output height of input video image. Value range:
Pixel: [0,2000]
Percentage: [0.01,0.99]
If this parameter is left empty, the input stream height will be used by default.
If percentage is used, the expected output is (percentage * background height).\n        :type ImageHeight: float\n        :param LocationX: X-axis offset of input in output video image. Value range:
Pixel: [0,2000]
Percentage: [0.01,0.99]
If this parameter is left empty, 0 will be used by default.
Horizontal offset from the top-left corner of main host background video image. 
If percentage is used, the expected output is (percentage * background width).\n        :type LocationX: float\n        :param LocationY: Y-axis offset of input in output video image. Value range:
Pixel: [0,2000]
Percentage: [0.01,0.99]
If this parameter is left empty, 0 will be used by default.
Vertical offset from the top-left corner of main host background video image. 
If percentage is used, the expected output is (percentage * background width)\n        :type LocationY: float\n        :param Color: When `InputType` is 3 (canvas), this value indicates the canvas color.
Commonly used colors include:
Red: 0xcc0033.
Yellow: 0xcc9900.
Green: 0xcccc33.
Blue: 0x99CCFF.
Black: 0x000000.
White: 0xFFFFFF.
Gray: 0x999999\n        :type Color: str\n        :param WatermarkId: When `InputType` is 2 (image), this value is the watermark ID.\n        :type WatermarkId: int\n        """
        self.ImageLayer = None
        self.InputType = None
        self.ImageWidth = None
        self.ImageHeight = None
        self.LocationX = None
        self.LocationY = None
        self.Color = None
        self.WatermarkId = None


    def _deserialize(self, params):
        self.ImageLayer = params.get("ImageLayer")
        self.InputType = params.get("InputType")
        self.ImageWidth = params.get("ImageWidth")
        self.ImageHeight = params.get("ImageHeight")
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
        """
        :param OutputStreamName: Output stream name.\n        :type OutputStreamName: str\n        :param OutputStreamType: Output stream type. Valid values: [0,1].
If this parameter is left empty, 0 will be used by default.
If the output stream is a stream in the input stream list, enter 0.
If you want the stream mix result to be a new stream, enter 1.
If this value is 1, `output_stream_id` cannot appear in `input_stram_list`, and there cannot be a stream with the same ID on the LVB backend.\n        :type OutputStreamType: int\n        :param OutputStreamBitRate: Output stream bitrate. Value range: [1,50000].
If this parameter is left empty, the system will automatically determine.\n        :type OutputStreamBitRate: int\n        :param OutputStreamGop: Output stream GOP size. Value range: [1,10].
If this parameter is left empty, the system will automatically determine.\n        :type OutputStreamGop: int\n        :param OutputStreamFrameRate: Output stream frame rate. Value range: [1,60].
If this parameter is left empty, the system will automatically determine.\n        :type OutputStreamFrameRate: int\n        :param OutputAudioBitRate: Output stream audio bitrate. Value range: [1,500]
If this parameter is left empty, the system will automatically determine.\n        :type OutputAudioBitRate: int\n        :param OutputAudioSampleRate: Output stream audio sample rate. Valid values: [96000, 88200, 64000, 48000, 44100, 32000,24000, 22050, 16000, 12000, 11025, 8000].
If this parameter is left empty, the system will automatically determine.\n        :type OutputAudioSampleRate: int\n        :param OutputAudioChannels: Output stream audio sound channel. Valid values: [1,2].
If this parameter is left empty, the system will automatically determine.\n        :type OutputAudioChannels: int\n        :param MixSei: SEI information in output stream. If there are no special needs, leave it empty.\n        :type MixSei: str\n        """
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
        """
        :param Time: Time point.\n        :type Time: str\n        :param Num: Number of channels.\n        :type Num: int\n        """
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
        """
        :param MixStreamSessionId: ID of stream mix session (from applying for stream mix to canceling stream mix).\n        :type MixStreamSessionId: str\n        :param InputStreamList: Input stream list for stream mix.\n        :type InputStreamList: list of CommonMixInputParam\n        :param OutputParams: Output stream parameter for stream mix.\n        :type OutputParams: :class:`tencentcloud.live.v20180801.models.CommonMixOutputParams`\n        :param MixStreamTemplateId: Input template ID. If this parameter is set, the output will be generated according to the default template layout, and there is no need to enter the custom position parameters.
If this parameter is left empty, 0 will be used by default.
For two input sources, 10, 20, 30, 40, and 50 are supported.
For three input sources, 310, 390, and 391 are supported.
For four input sources, 410 is supported.
For five input sources, 510 and 590 are supported.
For six input sources, 610 is supported.\n        :type MixStreamTemplateId: int\n        :param ControlParams: Special control parameter for stream mix. If there are no special needs, leave it empty.\n        :type ControlParams: :class:`tencentcloud.live.v20180801.models.CommonMixControlParams`\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLiveCallbackRuleRequest(AbstractModel):
    """CreateLiveCallbackRule request structure.

    """

    def __init__(self):
        """
        :param DomainName: Push domain name.\n        :type DomainName: str\n        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.\n        :type AppName: str\n        :param TemplateId: Template ID.\n        :type TemplateId: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLiveCallbackTemplateRequest(AbstractModel):
    """CreateLiveCallbackTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateName: Template name.
Maximum length: 255 bytes.
Only letters, digits, underscores, and hyphens can be contained.\n        :type TemplateName: str\n        :param Description: Description.
Maximum length: 1,024 bytes.
Only letters, digits, underscores, and hyphens can be contained.\n        :type Description: str\n        :param StreamBeginNotifyUrl: Stream starting callback URL,
Protocol document: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1).\n        :type StreamBeginNotifyUrl: str\n        :param StreamEndNotifyUrl: Interruption callback URL,
Protocol document: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1).\n        :type StreamEndNotifyUrl: str\n        :param RecordNotifyUrl: Recording callback URL,
Protocol document: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1).\n        :type RecordNotifyUrl: str\n        :param SnapshotNotifyUrl: Screencapturing callback URL,
Protocol document: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1).\n        :type SnapshotNotifyUrl: str\n        :param PornCensorshipNotifyUrl: Porn detection callback URL,
Protocol document: [Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32741?from_cn_redirect=1).\n        :type PornCensorshipNotifyUrl: str\n        :param CallbackKey: Callback key. The callback URL is public. For the callback signature, please see the event message notification document.
[Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1).\n        :type CallbackKey: str\n        :param StreamMixNotifyUrl: Disused\n        :type StreamMixNotifyUrl: str\n        """
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
        """
        :param TemplateId: Template ID.\n        :type TemplateId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class CreateLiveCertRequest(AbstractModel):
    """CreateLiveCert request structure.

    """

    def __init__(self):
        """
        :param CertType: Certificate type. 0: user-added certificate, 1: Tencent Cloud-hosted certificate.
Note: if the certificate type is 0, `HttpsCrt` and `HttpsKey` are required;
If the certificate type is 1, the certificate corresponding to `CloudCertId` will be used first. If `CloudCertId` is empty, `HttpsCrt` and `HttpsKey` will be used.\n        :type CertType: int\n        :param CertName: Certificate name.\n        :type CertName: str\n        :param HttpsCrt: Certificate content, i.e., public key.\n        :type HttpsCrt: str\n        :param HttpsKey: Private key.\n        :type HttpsKey: str\n        :param Description: Description.\n        :type Description: str\n        :param CloudCertId: Tencent Cloud-hosted certificate ID.\n        :type CloudCertId: str\n        """
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
        """
        :param CertId: Certificate ID\n        :type CertId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.CertId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.RequestId = params.get("RequestId")


class CreateLiveRecordRequest(AbstractModel):
    """CreateLiveRecord request structure.

    """

    def __init__(self):
        """
        :param StreamName: Stream name.\n        :type StreamName: str\n        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.\n        :type AppName: str\n        :param DomainName: Push domain name. This parameter must be set for multi-domain name push.\n        :type DomainName: str\n        :param StartTime: Recording start time, which is China standard time and should be URL-encoded (RFC3986). For example, the encoding of 2017-01-01 10:10:01 is 2017-01-01+10%3a10%3a01.
In scheduled recording mode, this field must be set; in real-time video recording mode, this field is ignored.\n        :type StartTime: str\n        :param EndTime: Recording end time, which is China standard time and should be URL-encoded (RFC3986). For example, the encoding of 2017-01-01 10:30:01 is 2017-01-01+10%3a30%3a01.
In scheduled recording mode, this field must be set; in real-time video recording mode, this field is optional. If the recording is set to real-time video recording mode through the `Highlight` parameter, the set end time should not be more than 30 minutes after the current time. If the set end time is more than 30 minutes after the current time, earlier than the current time, or left empty, the actual end time will be 30 minutes after the current time.\n        :type EndTime: str\n        :param RecordType: Recording type.
"video": Audio-video recording **(default)**.
"audio": audio recording.
In both scheduled and real-time video recording modes, this parameter is valid and is not case sensitive.\n        :type RecordType: str\n        :param FileFormat: Recording file format. Valid values:
"flv" **(default)**, "hls", "mp4", "aac", "mp3".
In both scheduled and real-time video recording modes, this parameter is valid and is not case sensitive.\n        :type FileFormat: str\n        :param Highlight: Mark for enabling real-time video recording mode.
0: Real-time video recording mode is not enabled, i.e., the scheduled recording mode is used **(default)**. See [Sample 1](#.E7.A4.BA.E4.BE.8B1-.E5.88.9B.E5.BB.BA.E5.AE.9A.E6.97.B6.E5.BD.95.E5.88.B6.E4.BB.BB.E5.8A.A1).
1: Real-time video recording mode is enabled. See [Sample 2](#.E7.A4.BA.E4.BE.8B2-.E5.88.9B.E5.BB.BA.E5.AE.9E.E6.97.B6.E5.BD.95.E5.88.B6.E4.BB.BB.E5.8A.A1).\n        :type Highlight: int\n        :param MixStream: Flag for enabling A+B=C mixed stream recording.
0: A+B=C mixed stream recording is not enabled **(default)**.
1: A+B=C mixed stream recording is enabled.
In both scheduled and real-time video recording modes, this parameter is valid.\n        :type MixStream: int\n        :param StreamParam: Recording stream parameter. The following parameters are supported currently:
record_interval: recording interval in seconds. Value range: 1800-7200.
storage_time: recording file storage duration in seconds.
Example: record_interval=3600&storage_time=2592000.
Note: the parameter needs to be URL-encoded.
In both scheduled and real-time video recording modes, this parameter is valid.\n        :type StreamParam: str\n        """
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
        """
        :param TaskId: Task ID, which uniquely identifies a recording task globally.\n        :type TaskId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateLiveRecordRuleRequest(AbstractModel):
    """CreateLiveRecordRule request structure.

    """

    def __init__(self):
        """
        :param DomainName: Push domain name.\n        :type DomainName: str\n        :param TemplateId: Template ID.\n        :type TemplateId: int\n        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.\n        :type AppName: str\n        :param StreamName: Stream name.
Note: If the parameter is a non-empty string, the rule will be only applicable to the particular stream.\n        :type StreamName: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLiveRecordTemplateRequest(AbstractModel):
    """CreateLiveRecordTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateName: Template name. Only letters, digits, underscores, and hyphens can be contained.\n        :type TemplateName: str\n        :param Description: Message description\n        :type Description: str\n        :param FlvParam: FLV recording parameter, which is set when FLV recording is enabled.\n        :type FlvParam: :class:`tencentcloud.live.v20180801.models.RecordParam`\n        :param HlsParam: HLS recording parameter, which is set when HLS recording is enabled.\n        :type HlsParam: :class:`tencentcloud.live.v20180801.models.RecordParam`\n        :param Mp4Param: Mp4 recording parameter, which is set when Mp4 recording is enabled.\n        :type Mp4Param: :class:`tencentcloud.live.v20180801.models.RecordParam`\n        :param AacParam: AAC recording parameter, which is set when AAC recording is enabled.\n        :type AacParam: :class:`tencentcloud.live.v20180801.models.RecordParam`\n        :param IsDelayLive: LVB type. Default value: 0.
0: LVB.
1: LCB.\n        :type IsDelayLive: int\n        :param HlsSpecialParam: HLS-specific recording parameter.\n        :type HlsSpecialParam: :class:`tencentcloud.live.v20180801.models.HlsSpecialParam`\n        :param Mp3Param: Mp3 recording parameter, which is set when Mp3 recording is enabled.\n        :type Mp3Param: :class:`tencentcloud.live.v20180801.models.RecordParam`\n        """
        self.TemplateName = None
        self.Description = None
        self.FlvParam = None
        self.HlsParam = None
        self.Mp4Param = None
        self.AacParam = None
        self.IsDelayLive = None
        self.HlsSpecialParam = None
        self.Mp3Param = None


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
        """
        :param TemplateId: Template ID.\n        :type TemplateId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class CreateLiveSnapshotRuleRequest(AbstractModel):
    """CreateLiveSnapshotRule request structure.

    """

    def __init__(self):
        """
        :param DomainName: Push domain name.\n        :type DomainName: str\n        :param TemplateId: Template ID.\n        :type TemplateId: int\n        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.\n        :type AppName: str\n        :param StreamName: Stream name.
Note: if this parameter is a non-empty string, the rule will take effect only for the particular stream.\n        :type StreamName: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLiveSnapshotTemplateRequest(AbstractModel):
    """CreateLiveSnapshotTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateName: Template name.
Maximum length: 255 bytes.
Only letters, digits, underscores, and hyphens can be contained.\n        :type TemplateName: str\n        :param CosAppId: COS application ID.\n        :type CosAppId: int\n        :param CosBucket: COS bucket name.
Note: the value of `CosBucket` cannot contain `-[appid]`.\n        :type CosBucket: str\n        :param CosRegion: COS region.\n        :type CosRegion: str\n        :param Description: Description.
Maximum length: 1,024 bytes.
Only letters, digits, underscores, and hyphens can be contained.\n        :type Description: str\n        :param SnapshotInterval: Screencapturing interval in seconds. Default value: 10s.
Value range: 5-300s.\n        :type SnapshotInterval: int\n        :param Width: Screenshot width. Default value: 0 (original width).\n        :type Width: int\n        :param Height: Screenshot height. Default value: 0 (original height).\n        :type Height: int\n        :param PornFlag: Whether to enable porn detection. 0: no, 1: yes. Default value: 0\n        :type PornFlag: int\n        :param CosPrefix: COS Bucket folder prefix.
If no value is entered, the default value
`/{Year}-{Month}-{Day}`
will be used.\n        :type CosPrefix: str\n        :param CosFileName: COS filename.
If no value is entered, the default value 
`{StreamID}-screenshot-{Hour}-{Minute}-{Second}-{Width}x{Height}{Ext}`
will be used.\n        :type CosFileName: str\n        """
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
        """
        :param TemplateId: Template ID.\n        :type TemplateId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class CreateLiveTranscodeRuleRequest(AbstractModel):
    """CreateLiveTranscodeRule request structure.

    """

    def __init__(self):
        """
        :param DomainName: Playback domain name.\n        :type DomainName: str\n        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default. If you only bind a domain name, leave this parameter empty.\n        :type AppName: str\n        :param StreamName: Stream name. If only the domain name or path is bound, leave this parameter blank.\n        :type StreamName: str\n        :param TemplateId: Designates an existing template ID.\n        :type TemplateId: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateLiveTranscodeTemplateRequest(AbstractModel):
    """CreateLiveTranscodeTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateName: Template name, such as “900p”. This can be only a combination of letters and digits.
Length limit:
  Standard transcoding: 1-10 characters
  Top speed codec transcoding: 3-10 characters\n        :type TemplateName: str\n        :param VideoBitrate: Video bitrate in Kbps. Value range: 100-8000.
Note: the transcoding template requires that the bitrate be unique. Therefore, the final saved bitrate may be different from the input bitrate.\n        :type VideoBitrate: int\n        :param Acodec: Audio codec. Default value: aac.
Note: this parameter is unsupported now.\n        :type Acodec: str\n        :param AudioBitrate: Audio bitrate. Default value: 0.
Value range: 0-500.\n        :type AudioBitrate: int\n        :param Vcodec: Video codec. Valid values: h264, h265, origin (default)

origin: original codec as the output codec\n        :type Vcodec: str\n        :param Description: Template description.\n        :type Description: str\n        :param NeedVideo: Whether to keep the video. 0: no; 1: yes. Default value: 1.\n        :type NeedVideo: int\n        :param Width: Width. Default value: 0.
Value range: 0-3000
It must be a multiple of 2. The original width is 0.\n        :type Width: int\n        :param NeedAudio: Whether to keep the audio. 0: no; 1: yes. Default value: 1.\n        :type NeedAudio: int\n        :param Height: Height. Default value: 0.
Value range: [0,3000]
The value must be a multiple of 2, and 0 is the original height.\n        :type Height: int\n        :param Fps: Frame rate. Default value: 0.
Value range: 0-60\n        :type Fps: int\n        :param Gop: Keyframe interval in seconds. Default value: original interval
Value range: 2-6\n        :type Gop: int\n        :param Rotate: Rotation angle. Default value: 0.
Valid values: 0, 90, 180, 270\n        :type Rotate: int\n        :param Profile: Encoding quality:
baseline/main/high. Default value: baseline.\n        :type Profile: str\n        :param BitrateToOrig: Whether to use the original bitrate when the set bitrate is larger than the original bitrate.
0: no, 1: yes
Default value: 0.\n        :type BitrateToOrig: int\n        :param HeightToOrig: Whether to use the original height when the set height is higher than the original height.
0: no, 1: yes
Default value: 0.\n        :type HeightToOrig: int\n        :param FpsToOrig: Whether to use the original frame rate when the set frame rate is larger than the original frame rate.
0: no, 1: yes
Default value: 0.\n        :type FpsToOrig: int\n        :param AiTransCode: Whether it is a top speed codec template. 0: no, 1: yes. Default value: 0.\n        :type AiTransCode: int\n        :param AdaptBitratePercent: Bitrate compression ratio of top speed codec video.
Target bitrate of top speed code = VideoBitrate * (1-AdaptBitratePercent)

Value range: 0.0-0.5.\n        :type AdaptBitratePercent: float\n        :param ShortEdgeAsHeight: Whether to use the short side as the video height. 0: no, 1: yes. Default value: 0.\n        :type ShortEdgeAsHeight: int\n        """
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
        """
        :param TemplateId: Template ID.\n        :type TemplateId: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class CreateLiveWatermarkRuleRequest(AbstractModel):
    """CreateLiveWatermarkRule request structure.

    """

    def __init__(self):
        """
        :param DomainName: Push domain name.\n        :type DomainName: str\n        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.\n        :type AppName: str\n        :param StreamName: Stream name.\n        :type StreamName: str\n        :param TemplateId: Watermark ID, which is the `WatermarkId` returned by the [AddLiveWatermark](https://intl.cloud.tencent.com/document/product/267/30154?from_cn_redirect=1) API.\n        :type TemplateId: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateRecordTaskRequest(AbstractModel):
    """CreateRecordTask request structure.

    """

    def __init__(self):
        """
        :param StreamName: Stream name.\n        :type StreamName: str\n        :param DomainName: Push domain name.\n        :type DomainName: str\n        :param AppName: Push path.\n        :type AppName: str\n        :param EndTime: Recording end time in UNIX timestamp format. “EndTime” should be later than “StartTime”, and the duration between “EndTime” and “StartTime” is up to 24 hours.\n        :type EndTime: int\n        :param StartTime: Recording start time in UNIX timestamp format. If “StartTime” is not entered, recording will start immediately after the API is successfully called. “StartTime” should be within 6 days from the current time.\n        :type StartTime: int\n        :param StreamType: Push type. Default value: 0. Valid values:
0: LVB push.
1: mixed stream, i.e., A + B = C mixed stream.\n        :type StreamType: int\n        :param TemplateId: Recording template ID, which is the returned value of `CreateLiveRecordTemplate`. If this parameter is left empty or incorrect, the stream will be recorded in HLS format and retained permanently by default.\n        :type TemplateId: int\n        :param Extension: Extension field which is not defined now. It is empty by default.\n        :type Extension: str\n        """
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
        """
        :param TaskId: A globally unique task ID. If `TaskId` is returned, the recording task has been successfully created.\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DayStreamPlayInfo(AbstractModel):
    """Stream playback information

    """

    def __init__(self):
        """
        :param Time: Data point in time in the format of `yyyy-mm-dd HH:MM:SS`.\n        :type Time: str\n        :param Bandwidth: Bandwidth in Mbps.\n        :type Bandwidth: float\n        :param Flux: Traffic in MB.\n        :type Flux: float\n        :param Request: Number of requests.\n        :type Request: int\n        :param Online: Number of online viewers.\n        :type Online: int\n        """
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
        """
        :param DomainName: Push domain name.\n        :type DomainName: str\n        :param AppName: Push path, which is the same as the 
 `AppName` in push and playback addresses and is `live` by default.\n        :type AppName: str\n        :param StreamName: Stream name.\n        :type StreamName: str\n        :param DelayInterval: Delay time in seconds.\n        :type DelayInterval: int\n        :param CreateTime: Creation time in UTC time.
Note: the difference between UTC time and Beijing time is 8 hours.
Example: 2019-06-18T12:00:00Z (i.e., June 18, 2019 20:00:00 Beijing time).\n        :type CreateTime: str\n        :param ExpireTime: Expiration time in UTC time.
Note: the difference between UTC time and Beijing time is 8 hours.
Example: 2019-06-18T12:00:00Z (i.e., June 18, 2019 20:00:00 Beijing time).\n        :type ExpireTime: str\n        :param Status: Current status:
-1: expired.
1: in effect.\n        :type Status: int\n        """
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
        """
        :param DomainName: Push domain name.\n        :type DomainName: str\n        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.\n        :type AppName: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveCallbackTemplateRequest(AbstractModel):
    """DeleteLiveCallbackTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.
1. Get the template ID in the returned value of the [CreateLiveCallbackTemplate](https://intl.cloud.tencent.com/document/product/267/32637?from_cn_redirect=1) API call.
2. You can query the list of created templates through the [DescribeLiveCallbackTemplates](https://intl.cloud.tencent.com/document/product/267/32632?from_cn_redirect=1) API.\n        :type TemplateId: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveCertRequest(AbstractModel):
    """DeleteLiveCert request structure.

    """

    def __init__(self):
        """
        :param CertId: Certificate ID obtained through the `DescribeLiveCerts` API.\n        :type CertId: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveDomainRequest(AbstractModel):
    """DeleteLiveDomain request structure.

    """

    def __init__(self):
        """
        :param DomainName: Domain name to be deleted.\n        :type DomainName: str\n        :param DomainType: Type. 0: push, 1: playback.\n        :type DomainType: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveRecordRequest(AbstractModel):
    """DeleteLiveRecord request structure.

    """

    def __init__(self):
        """
        :param StreamName: Stream name.\n        :type StreamName: str\n        :param TaskId: Task ID returned by the `CreateLiveRecord` API.\n        :type TaskId: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveRecordRuleRequest(AbstractModel):
    """DeleteLiveRecordRule request structure.

    """

    def __init__(self):
        """
        :param DomainName: Push domain name.
Domain name+AppName+StreamName uniquely identifies a single transcoding rule. If you need to delete it, strong match is required. For example, even if AppName is blank, you need to pass in a blank string to make a strong match.\n        :type DomainName: str\n        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.
Domain name+AppName+StreamName uniquely identifies a single transcoding rule. If you need to delete it, strong match is required. For example, even if AppName is blank, you need to pass in a blank string to make a strong match.\n        :type AppName: str\n        :param StreamName: Stream name.
Domain name+AppName+StreamName uniquely identifies a single transcoding rule. If you need to delete it, strong match is required. For example, even if AppName is blank, you need to pass in a blank string to make a strong match.\n        :type StreamName: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveRecordTemplateRequest(AbstractModel):
    """DeleteLiveRecordTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID obtained through the `DescribeRecordTemplates` API.\n        :type TemplateId: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveSnapshotRuleRequest(AbstractModel):
    """DeleteLiveSnapshotRule request structure.

    """

    def __init__(self):
        """
        :param DomainName: Push domain name.\n        :type DomainName: str\n        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.\n        :type AppName: str\n        :param StreamName: Stream name.\n        :type StreamName: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveSnapshotTemplateRequest(AbstractModel):
    """DeleteLiveSnapshotTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.
1. Get from the returned value of the [CreateLiveSnapshotTemplate](https://intl.cloud.tencent.com/document/product/267/32624?from_cn_redirect=1) API call.
2. You can query the list of created screencapturing templates through the [DescribeLiveSnapshotTemplates](https://intl.cloud.tencent.com/document/product/267/32619?from_cn_redirect=1) API.\n        :type TemplateId: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveTranscodeRuleRequest(AbstractModel):
    """DeleteLiveTranscodeRule request structure.

    """

    def __init__(self):
        """
        :param DomainName: Playback domain name.\n        :type DomainName: str\n        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.\n        :type AppName: str\n        :param StreamName: Stream name.\n        :type StreamName: str\n        :param TemplateId: Template ID.\n        :type TemplateId: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveTranscodeTemplateRequest(AbstractModel):
    """DeleteLiveTranscodeTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.
1. Get the template ID in the returned value of the [CreateLiveTranscodeTemplate](https://intl.cloud.tencent.com/document/product/267/32646?from_cn_redirect=1) API call.
2. You can query the list of created templates through the [DescribeLiveTranscodeTemplates](https://intl.cloud.tencent.com/document/product/267/32641?from_cn_redirect=1) API.\n        :type TemplateId: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveWatermarkRequest(AbstractModel):
    """DeleteLiveWatermark request structure.

    """

    def __init__(self):
        """
        :param WatermarkId: Watermark ID.
Watermark ID obtained in the returned value of the [AddLiveWatermark](https://intl.cloud.tencent.com/document/product/267/30154?from_cn_redirect=1) API call.
Watermark ID returned by the `DescribeLiveWatermarks` API.\n        :type WatermarkId: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLiveWatermarkRuleRequest(AbstractModel):
    """DeleteLiveWatermarkRule request structure.

    """

    def __init__(self):
        """
        :param DomainName: Push domain name.\n        :type DomainName: str\n        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.\n        :type AppName: str\n        :param StreamName: Stream name.\n        :type StreamName: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRecordTaskRequest(AbstractModel):
    """DeleteRecordTask request structure.

    """

    def __init__(self):
        """
        :param TaskId: Task ID returned by `CreateRecordTask`. The recording task specified by `TaskId` will be deleted.\n        :type TaskId: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAllStreamPlayInfoListRequest(AbstractModel):
    """DescribeAllStreamPlayInfoList request structure.

    """

    def __init__(self):
        """
        :param QueryTime: Query time point accurate to the minute. You can query data within the last month. As there is a 5-minute delay in the data, you're advised to pass in a time point 5 minutes earlier than needed. Format: yyyy-mm-dd HH:MM:00. As the accuracy is to the minute, please set the value of second to `00`.\n        :type QueryTime: str\n        :param PlayDomains: Playback domain name list. If this parameter is left empty, full data will be queried.\n        :type PlayDomains: list of str\n        """
        self.QueryTime = None
        self.PlayDomains = None


    def _deserialize(self, params):
        self.QueryTime = params.get("QueryTime")
        self.PlayDomains = params.get("PlayDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllStreamPlayInfoListResponse(AbstractModel):
    """DescribeAllStreamPlayInfoList response structure.

    """

    def __init__(self):
        """
        :param QueryTime: Query point in time in the returned input parameters.\n        :type QueryTime: str\n        :param DataInfoList: Data information list.\n        :type DataInfoList: list of MonitorStreamPlayInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.QueryTime = None
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.QueryTime = params.get("QueryTime")
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = MonitorStreamPlayInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAreaBillBandwidthAndFluxListRequest(AbstractModel):
    """DescribeAreaBillBandwidthAndFluxList request structure.

    """

    def __init__(self):
        """
        :param StartTime: Start time point in the format of yyyy-mm-dd HH:MM:SS.\n        :type StartTime: str\n        :param EndTime: End time point in the format of yyyy-mm-dd HH:MM:SS. The difference between the start time and end time cannot be greater than 1 days.\n        :type EndTime: str\n        :param PlayDomains: LVB playback domain name. If it is left blank, the full data will be queried.\n        :type PlayDomains: list of str\n        """
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
        


class DescribeAreaBillBandwidthAndFluxListResponse(AbstractModel):
    """DescribeAreaBillBandwidthAndFluxList response structure.

    """

    def __init__(self):
        """
        :param DataInfoList: Detailed data information.\n        :type DataInfoList: list of BillAreaInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = BillAreaInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBillBandwidthAndFluxListRequest(AbstractModel):
    """DescribeBillBandwidthAndFluxList request structure.

    """

    def __init__(self):
        """
        :param StartTime: Start time point in the format of `yyyy-mm-dd HH:MM:SS`.\n        :type StartTime: str\n        :param EndTime: End time point in the format of yyyy-mm-dd HH:MM:SS. The difference between the start time and end time cannot be greater than 31 days. Data in the last 3 years can be queried.\n        :type EndTime: str\n        :param PlayDomains: LVB playback domain name. If this parameter is left empty, full data will be queried.\n        :type PlayDomains: list of str\n        :param MainlandOrOversea: Valid values:
Mainland: query data for Mainland China,
Oversea: query data for regions outside Mainland China,
Default: query data for all regions.
Note: LEB only supports querying data for all regions.\n        :type MainlandOrOversea: str\n        :param Granularity: Data granularity. Valid values:
5: 5-minute granularity (the query time span should be within 1 day),
60: 1-hour granularity (the query time span should be within one month),
1440: 1-day granularity (the query time span should be within one month).
Default value: 5.\n        :type Granularity: int\n        :param ServiceName: Service name. Valid values: LVB, LEB. The sum of LVB and LEB usage will be returned if this parameter is left empty.\n        :type ServiceName: str\n        """
        self.StartTime = None
        self.EndTime = None
        self.PlayDomains = None
        self.MainlandOrOversea = None
        self.Granularity = None
        self.ServiceName = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PlayDomains = params.get("PlayDomains")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.Granularity = params.get("Granularity")
        self.ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillBandwidthAndFluxListResponse(AbstractModel):
    """DescribeBillBandwidthAndFluxList response structure.

    """

    def __init__(self):
        """
        :param PeakBandwidthTime: Time point of peak bandwidth value in the format of `yyyy-mm-dd HH:MM:SS`.\n        :type PeakBandwidthTime: str\n        :param PeakBandwidth: Peak bandwidth in Mbps.\n        :type PeakBandwidth: float\n        :param P95PeakBandwidthTime: Time point of 95th percentile bandwidth value in the format of `yyyy-mm-dd HH:MM:SS`.\n        :type P95PeakBandwidthTime: str\n        :param P95PeakBandwidth: 95th percentile bandwidth in Mbps.\n        :type P95PeakBandwidth: float\n        :param SumFlux: Total traffic in MB.\n        :type SumFlux: float\n        :param DataInfoList: Detailed data information.\n        :type DataInfoList: list of BillDataInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.PeakBandwidthTime = None
        self.PeakBandwidth = None
        self.P95PeakBandwidthTime = None
        self.P95PeakBandwidth = None
        self.SumFlux = None
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PeakBandwidthTime = params.get("PeakBandwidthTime")
        self.PeakBandwidth = params.get("PeakBandwidth")
        self.P95PeakBandwidthTime = params.get("P95PeakBandwidthTime")
        self.P95PeakBandwidth = params.get("P95PeakBandwidth")
        self.SumFlux = params.get("SumFlux")
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = BillDataInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeConcurrentRecordStreamNumRequest(AbstractModel):
    """DescribeConcurrentRecordStreamNum request structure.

    """

    def __init__(self):
        """
        :param LiveType: Live streaming type. SlowLive: LCB.
NormalLive: LVB.\n        :type LiveType: str\n        :param StartTime: Start time in the format of `yyyy-mm-dd HH:MM:SS`.
Data for the last 180 days can be queried.\n        :type StartTime: str\n        :param EndTime: End time in the format of `yyyy-mm-dd HH:MM:SS`.
The maximum time span supported is 31 days.\n        :type EndTime: str\n        :param MainlandOrOversea: Valid values: Mainland (data for Mainland China), Oversea (data for regions outside Mainland China). If this parameter is left empty, data for all regions will be queried.\n        :type MainlandOrOversea: str\n        :param PushDomains: Playback domain name list. If this parameter is left empty, full data will be queried.\n        :type PushDomains: list of str\n        """
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
        """
        :param DataInfoList: Statistics list.\n        :type DataInfoList: list of ConcurrentRecordStreamNum\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param StartTime: Start time in the format of "%Y-%m-%d %H:%M:%S".\n        :type StartTime: str\n        :param EndTime: End time in the format of "%Y-%m-%d %H:%M:%S". Data in the last 3 months can be queried, and the query period is up to 1 month.\n        :type EndTime: str\n        """
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
        """
        :param DataInfoList: Billable bandwidth of live stream relaying.\n        :type DataInfoList: list of BandwidthInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param StartTime: Start time point in the format of `yyyy-mm-dd HH:MM:SS`.\n        :type StartTime: str\n        :param EndTime: End time point in the format of `yyyy-mm-dd HH:MM:SS`
The time span is (0,3 hours]. Data for the last month can be queried.\n        :type EndTime: str\n        :param PlayDomains: Playback domain name. If this parameter is left empty, full data will be queried.\n        :type PlayDomains: list of str\n        :param ProvinceNames: District list. If this parameter is left empty, data for all districts will be returned.\n        :type ProvinceNames: list of str\n        :param IspNames: ISP list. If this parameter is left empty, data of all ISPs will be returned.\n        :type IspNames: list of str\n        :param MainlandOrOversea: Within or outside Mainland China. Valid values: Mainland (data for Mainland China), Oversea (data for regions outside Mainland China). If this parameter is left empty, data for all regions will be queried.\n        :type MainlandOrOversea: str\n        """
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
        """
        :param DataInfoList: Data content.\n        :type DataInfoList: list of GroupProIspDataInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param StartTime: Start time (Beijing time).
Format: yyyy-mm-dd HH:MM:SS.\n        :type StartTime: str\n        :param EndTime: End time (Beijing time).
Format: yyyy-mm-dd HH:MM:SS.
Note: data in the last 3 months can be queried and the query period is up to 1 day.\n        :type EndTime: str\n        :param PlayDomains: Playback domain name list.\n        :type PlayDomains: list of str\n        """
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
        """
        :param DataInfoList: Playback status code list.\n        :type DataInfoList: list of HttpStatusData\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Rules: Rule information list.\n        :type Rules: list of CallBackRuleInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param TemplateId: Template ID.
1. Get the template ID in the returned value of the [CreateLiveCallbackTemplate](https://intl.cloud.tencent.com/document/product/267/32637?from_cn_redirect=1) API call.
2. You can query the list of created templates through the [DescribeLiveCallbackTemplates](https://intl.cloud.tencent.com/document/product/267/32632?from_cn_redirect=1) API.\n        :type TemplateId: int\n        """
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
        """
        :param Template: Callback template information.\n        :type Template: :class:`tencentcloud.live.v20180801.models.CallBackTemplateInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Templates: Template information list.\n        :type Templates: list of CallBackTemplateInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param CertId: Certificate ID obtained through the `DescribeLiveCerts` API.\n        :type CertId: int\n        """
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
        """
        :param CertInfo: Certificate information.\n        :type CertInfo: :class:`tencentcloud.live.v20180801.models.CertInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param CertInfoSet: Certificate information list.\n        :type CertInfoSet: list of CertInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param DelayInfoList: Delayed playback information list.\n        :type DelayInfoList: list of DelayInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param DomainName: Playback domain name.\n        :type DomainName: str\n        """
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
        """
        :param DomainCertInfo: Certificate information.\n        :type DomainCertInfo: :class:`tencentcloud.live.v20180801.models.DomainCertInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DomainCertInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainCertInfo") is not None:
            self.DomainCertInfo = DomainCertInfo()
            self.DomainCertInfo._deserialize(params.get("DomainCertInfo"))
        self.RequestId = params.get("RequestId")


class DescribeLiveDomainPlayInfoListRequest(AbstractModel):
    """DescribeLiveDomainPlayInfoList request structure.

    """

    def __init__(self):
        """
        :param PlayDomains: Playback domain name list.\n        :type PlayDomains: list of str\n        """
        self.PlayDomains = None


    def _deserialize(self, params):
        self.PlayDomains = params.get("PlayDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLiveDomainPlayInfoListResponse(AbstractModel):
    """DescribeLiveDomainPlayInfoList response structure.

    """

    def __init__(self):
        """
        :param Time: Data time in the format of `yyyy-mm-dd HH:MM:SS`.\n        :type Time: str\n        :param TotalBandwidth: Real-time total bandwidth.\n        :type TotalBandwidth: float\n        :param TotalFlux: Real-time total traffic.\n        :type TotalFlux: float\n        :param TotalRequest: Total number of requests.\n        :type TotalRequest: int\n        :param TotalOnline: Real-time total number of connections.\n        :type TotalOnline: int\n        :param DomainInfoList: Data by domain name.\n        :type DomainInfoList: list of DomainInfoList\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Time = None
        self.TotalBandwidth = None
        self.TotalFlux = None
        self.TotalRequest = None
        self.TotalOnline = None
        self.DomainInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.TotalBandwidth = params.get("TotalBandwidth")
        self.TotalFlux = params.get("TotalFlux")
        self.TotalRequest = params.get("TotalRequest")
        self.TotalOnline = params.get("TotalOnline")
        if params.get("DomainInfoList") is not None:
            self.DomainInfoList = []
            for item in params.get("DomainInfoList"):
                obj = DomainInfoList()
                obj._deserialize(item)
                self.DomainInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveDomainRefererRequest(AbstractModel):
    """DescribeLiveDomainReferer request structure.

    """

    def __init__(self):
        """
        :param DomainName: Playback domain name\n        :type DomainName: str\n        """
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
        """
        :param RefererAuthConfig: Referer allowlist/blocklist configuration of a domain name\n        :type RefererAuthConfig: :class:`tencentcloud.live.v20180801.models.RefererAuthConfig`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param DomainName: Domain name.\n        :type DomainName: str\n        """
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
        """
        :param DomainInfo: Domain name information.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type DomainInfo: :class:`tencentcloud.live.v20180801.models.DomainInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param DomainStatus: Filter by domain name status. 0: disabled, 1: enabled.\n        :type DomainStatus: int\n        :param DomainType: Filter by domain name type. 0: push. 1: playback\n        :type DomainType: int\n        :param PageSize: Number of entries per page. Value range: 10-100. Default value: 10.\n        :type PageSize: int\n        :param PageNum: Page number to get. Value range: 1-100000. Default value: 1.\n        :type PageNum: int\n        :param IsDelayLive: 0: LVB, 1: LCB. Default value: 0.\n        :type IsDelayLive: int\n        :param DomainPrefix: Domain name prefix.\n        :type DomainPrefix: str\n        """
        self.DomainStatus = None
        self.DomainType = None
        self.PageSize = None
        self.PageNum = None
        self.IsDelayLive = None
        self.DomainPrefix = None


    def _deserialize(self, params):
        self.DomainStatus = params.get("DomainStatus")
        self.DomainType = params.get("DomainType")
        self.PageSize = params.get("PageSize")
        self.PageNum = params.get("PageNum")
        self.IsDelayLive = params.get("IsDelayLive")
        self.DomainPrefix = params.get("DomainPrefix")
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
        """
        :param AllCount: Total number of results.\n        :type AllCount: int\n        :param DomainList: List of domain name details.\n        :type DomainList: list of DomainInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.AllCount = None
        self.DomainList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AllCount = params.get("AllCount")
        if params.get("DomainList") is not None:
            self.DomainList = []
            for item in params.get("DomainList"):
                obj = DomainInfo()
                obj._deserialize(item)
                self.DomainList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeLiveForbidStreamListRequest(AbstractModel):
    """DescribeLiveForbidStreamList request structure.

    """

    def __init__(self):
        """
        :param PageNum: Page number to get. Default value: 1.\n        :type PageNum: int\n        :param PageSize: Number of entries per page. Maximum value: 100. 
Value: any integer between 1 and 100.
Default value: 10.\n        :type PageSize: int\n        :param StreamName: The stream name to search for\n        :type StreamName: str\n        """
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
        """
        :param TotalNum: Total number of eligible ones.\n        :type TotalNum: int\n        :param TotalPage: Total number of pages.\n        :type TotalPage: int\n        :param PageNum: Page number.\n        :type PageNum: int\n        :param PageSize: Number of entries displayed per page.\n        :type PageSize: int\n        :param ForbidStreamList: List of forbidden streams.\n        :type ForbidStreamList: list of ForbidStreamInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param DomainName: Domain name.\n        :type DomainName: str\n        """
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
        """
        :param PlayAuthKeyInfo: Playback authentication key information.\n        :type PlayAuthKeyInfo: :class:`tencentcloud.live.v20180801.models.PlayAuthKeyInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.PlayAuthKeyInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PlayAuthKeyInfo") is not None:
            self.PlayAuthKeyInfo = PlayAuthKeyInfo()
            self.PlayAuthKeyInfo._deserialize(params.get("PlayAuthKeyInfo"))
        self.RequestId = params.get("RequestId")


class DescribeLivePushAuthKeyRequest(AbstractModel):
    """DescribeLivePushAuthKey request structure.

    """

    def __init__(self):
        """
        :param DomainName: Push domain name.\n        :type DomainName: str\n        """
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
        """
        :param PushAuthKeyInfo: Push authentication key information.\n        :type PushAuthKeyInfo: :class:`tencentcloud.live.v20180801.models.PushAuthKeyInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Rules: List of rules.\n        :type Rules: list of RuleInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param TemplateId: Template ID obtained by [DescribeLiveRecordTemplates](https://intl.cloud.tencent.com/document/product/267/32609?from_cn_redirect=1).\n        :type TemplateId: int\n        """
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
        """
        :param Template: Recording template information.\n        :type Template: :class:`tencentcloud.live.v20180801.models.RecordTemplateInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param IsDelayLive: Whether it is an LCB template. Default value: 0.
0: LVB.
1: LCB.\n        :type IsDelayLive: int\n        """
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
        """
        :param Templates: Recording template information list.\n        :type Templates: list of RecordTemplateInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Rules: Rule list.\n        :type Rules: list of RuleInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param TemplateId: Template ID.
Template ID returned by the [CreateLiveSnapshotTemplate](https://intl.cloud.tencent.com/document/product/267/32624?from_cn_redirect=1) API call.\n        :type TemplateId: int\n        """
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
        """
        :param Template: Screencapturing template information.\n        :type Template: :class:`tencentcloud.live.v20180801.models.SnapshotTemplateInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Templates: Screencapturing template list.\n        :type Templates: list of SnapshotTemplateInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param StartTime: Start time. 
In UTC format, such as 2018-12-29T19:00:00Z.
This supports querying the history of 60 days.\n        :type StartTime: str\n        :param EndTime: End time.
In UTC format, such as 2018-12-29T20:00:00Z.
This cannot be after the current time and cannot be more than 30 days after the start time.\n        :type EndTime: str\n        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.\n        :type AppName: str\n        :param DomainName: Push domain name.\n        :type DomainName: str\n        :param StreamName: Stream name; query with wildcard (*) is not supported; fuzzy match by default.
The IsStrict field can be used to change to exact query.\n        :type StreamName: str\n        :param PageNum: Page number to get.
Default value: 1.
Note: Currently, query for up to 10,000 entries is supported.\n        :type PageNum: int\n        :param PageSize: Number of entries per page.
Maximum value: 100.
Value range: any integer between 1 and 100.
Default value: 10.
Note: currently, query for up to 10,000 entries is supported.\n        :type PageSize: int\n        :param IsFilter: Whether to filter. No filtering by default.
0: No filtering at all.
1: Filter out the failing streams and return only the successful ones.\n        :type IsFilter: int\n        :param IsStrict: Whether to query exactly. Fuzzy match by default.
0: Fuzzy match.
1: Exact query.
Note: This parameter takes effect when StreamName is used.\n        :type IsStrict: int\n        :param IsAsc: Whether to display in ascending order by end time. Descending order by default.
0: Descending.
1: Ascending.\n        :type IsAsc: int\n        """
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
        """
        :param EventList: List of streaming events.\n        :type EventList: list of StreamEventInfo\n        :param PageNum: Page number.\n        :type PageNum: int\n        :param PageSize: Number of entries per page.\n        :type PageSize: int\n        :param TotalNum: Total number of eligible ones.\n        :type TotalNum: int\n        :param TotalPage: Total number of pages.\n        :type TotalPage: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param DomainName: Push domain name. If you use multiple paths, enter the `DomainName`.\n        :type DomainName: str\n        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default. If you use multiple paths, enter the `AppName`.\n        :type AppName: str\n        :param PageNum: Page number to get. Default value: 1.\n        :type PageNum: int\n        :param PageSize: Number of entries per page. Maximum value: 100. 
Value: any integer between 10 and 100.
Default value: 10.\n        :type PageSize: int\n        :param StreamName: Stream name, which is used for exact query.\n        :type StreamName: str\n        """
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
        """
        :param TotalNum: Total number of eligible ones.\n        :type TotalNum: int\n        :param TotalPage: Total number of pages.\n        :type TotalPage: int\n        :param PageNum: Page number.\n        :type PageNum: int\n        :param PageSize: Number of entries displayed per page.\n        :type PageSize: int\n        :param OnlineInfo: Active push information list.\n        :type OnlineInfo: list of StreamOnlineInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param DomainName: Your push domain name.\n        :type DomainName: str\n        :param EndTime: End time.
In UTC format, such as 2016-06-30T19:00:00Z.
This cannot be after the current time.
Note: The difference between EndTime and StartTime cannot be greater than 30 days.\n        :type EndTime: str\n        :param StartTime: Start time. 
In UTC format, such as 2016-06-29T19:00:00Z.
This supports querying data in the past 60 days.\n        :type StartTime: str\n        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default. Fuzzy match is not supported.\n        :type AppName: str\n        :param PageNum: Page number to get.
Default value: 1.\n        :type PageNum: int\n        :param PageSize: Number of entries per page.
Maximum value: 100
Valid values: integers between 10 and 100
Default value: 10\n        :type PageSize: int\n        :param StreamName: Stream name, which supports fuzzy match.\n        :type StreamName: str\n        """
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
        """
        :param PublishInfo: Push record information.\n        :type PublishInfo: list of StreamName\n        :param PageNum: Page number.\n        :type PageNum: int\n        :param PageSize: Number of entries per page\n        :type PageSize: int\n        :param TotalNum: Total number of eligible ones.\n        :type TotalNum: int\n        :param TotalPage: Total number of pages.\n        :type TotalPage: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param PushDomain: Push domain name.\n        :type PushDomain: str\n        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.\n        :type AppName: str\n        :param PageNum: Number of pages,
Value range: [1,10000],
Default value: 1.\n        :type PageNum: int\n        :param PageSize: Number of entries per page,
Value range: [1,1000],
Default value: 200.\n        :type PageSize: int\n        """
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
        """
        :param DataInfoList: Live stream statistics list.\n        :type DataInfoList: list of PushDataInfo\n        :param TotalNum: Total number of live streams.\n        :type TotalNum: int\n        :param TotalPage: Total number of pages.\n        :type TotalPage: int\n        :param PageNum: Page number where the current data resides.\n        :type PageNum: int\n        :param PageSize: Number of live streams per page.\n        :type PageSize: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.\n        :type AppName: str\n        :param DomainName: Your push domain name.\n        :type DomainName: str\n        :param StreamName: Stream name.\n        :type StreamName: str\n        """
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
        """
        :param StreamState: Stream status,
active: active
inactive: Inactive
forbid: forbidden.\n        :type StreamState: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.StreamState = None
        self.RequestId = None


    def _deserialize(self, params):
        self.StreamState = params.get("StreamState")
        self.RequestId = params.get("RequestId")


class DescribeLiveTranscodeDetailInfoRequest(AbstractModel):
    """DescribeLiveTranscodeDetailInfo request structure.

    """

    def __init__(self):
        """
        :param PushDomain: Push domain name.\n        :type PushDomain: str\n        :param StreamName: Stream name.\n        :type StreamName: str\n        :param DayTime: Query date (UTC+8)
Format: yyyymmdd
Note: you can query the statistics for a day in the past month, with yesterday as the latest date allowed.\n        :type DayTime: str\n        :param PageNum: Number of pages. Default value: 1.
Up to 100 pages.\n        :type PageNum: int\n        :param PageSize: Number of entries per page. Default value: 20,
Value range: [10,1000].\n        :type PageSize: int\n        :param StartDayTime: Start day time (Beijing time),
In the format of `yyyymmdd`.
Note: details for the last month can be queried.\n        :type StartDayTime: str\n        :param EndDayTime: End date (UTC+8)
Format: yyyymmdd
Note: you can query the statistics for a period in the past month, with yesterday as the latest date allowed. You must specify either `DayTime`, or `StartDayTime` and `EndDayTime`. If you specify all three parameters, only `DayTime` will be applied.\n        :type EndDayTime: str\n        """
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
        """
        :param DataInfoList: Statistics list.\n        :type DataInfoList: list of TranscodeDetailInfo\n        :param PageNum: Page number.\n        :type PageNum: int\n        :param PageSize: Number of entries per page.\n        :type PageSize: int\n        :param TotalNum: Total number.\n        :type TotalNum: int\n        :param TotalPage: Total number of pages.\n        :type TotalPage: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param TemplateIds: An array of template IDs to be filtered.\n        :type TemplateIds: list of int\n        :param DomainNames: An array of domain names to be filtered.\n        :type DomainNames: list of str\n        """
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
        """
        :param Rules: List of transcoding rules.\n        :type Rules: list of RuleInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param TemplateId: Template ID.
Note: get the template ID in the returned value of the [CreateLiveTranscodeTemplate](https://intl.cloud.tencent.com/document/product/267/32646?from_cn_redirect=1) API call.\n        :type TemplateId: int\n        """
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
        """
        :param Template: Template information.\n        :type Template: :class:`tencentcloud.live.v20180801.models.TemplateInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Templates: List of transcoding templates.\n        :type Templates: list of TemplateInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeLiveWatermarkRequest(AbstractModel):
    """DescribeLiveWatermark request structure.

    """

    def __init__(self):
        """
        :param WatermarkId: Watermark ID returned by the `DescribeLiveWatermarks` API.\n        :type WatermarkId: int\n        """
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
        """
        :param Watermark: Watermark information.\n        :type Watermark: :class:`tencentcloud.live.v20180801.models.WatermarkInfo`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param Rules: Watermarking rule list.\n        :type Rules: list of RuleInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param TotalNum: Total number of watermarks.\n        :type TotalNum: int\n        :param WatermarkList: Watermark information list.\n        :type WatermarkList: list of WatermarkInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param StartTime: Start time (Beijing time),
In the format of `yyyy-mm-dd HH:MM:SS`.\n        :type StartTime: str\n        :param EndTime: End time (Beijing time),
In the format of `yyyy-mm-dd HH:MM:SS`.
Note: `EndTime` and `StartTime` only support querying data for the last day.\n        :type EndTime: str\n        :param Granularity: Query granularity:
1: 1-minute granularity.\n        :type Granularity: int\n        :param StatType: Yes. Valid values: "4xx", "5xx". Mixed codes in the format of `4xx,5xx` are also supported.\n        :type StatType: str\n        :param PlayDomains: Playback domain name list.\n        :type PlayDomains: list of str\n        :param MainlandOrOversea: Region. Valid values: Mainland (data for Mainland China), Oversea (data for regions outside Mainland China), China (data for China, including Hong Kong, Macao, and Taiwan), Foreign (data for regions outside China, excluding Hong Kong, Macao, and Taiwan), Global (default). If this parameter is left empty, data for all regions will be queried.\n        :type MainlandOrOversea: str\n        """
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
        """
        :param HttpCodeList: Statistics list.\n        :type HttpCodeList: list of HttpCodeInfo\n        :param StatType: Statistics type.\n        :type StatType: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param StartTime: Start point in time (Beijing time).
In the format of `yyyy-mm-dd HH:MM:SS`.\n        :type StartTime: str\n        :param EndTime: End point in time (Beijing time).
In the format of `yyyy-mm-dd HH:MM:SS`.
Note: `EndTime` and `StartTime` only support querying data for the last day.\n        :type EndTime: str\n        :param PlayDomains: Playback domain name list. If this parameter is left empty, full data will be queried.\n        :type PlayDomains: list of str\n        :param PageNum: Number of pages. Value range: [1,1000]. Default value: 1.\n        :type PageNum: int\n        :param PageSize: Number of entries per page. Value range: [1,1000]. Default value: 20.\n        :type PageSize: int\n        :param MainlandOrOversea: Region. Valid values: Mainland (data for Mainland China), Oversea (data for regions outside Mainland China), China (data for China, including Hong Kong, Macao, and Taiwan), Foreign (data for regions outside China, excluding Hong Kong, Macao, and Taiwan), Global (default). If this parameter is left empty, data for all regions will be queried.\n        :type MainlandOrOversea: str\n        :param GroupType: Grouping parameter. Valid values: CountryProIsp (default value), Country (country/region). Grouping is made by country/region + district + ISP by default. Currently, districts and ISPs outside Mainland China cannot be recognized.\n        :type GroupType: str\n        :param OutLanguage: Language used in the output field. Valid values: Chinese (default), English. Currently, country/region, district, and ISP parameters support multiple languages.\n        :type OutLanguage: str\n        """
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
        """
        :param ProIspInfoList: Information of error codes starting with 2, 3, 4, or 5 by district and ISP.\n        :type ProIspInfoList: list of ProIspPlayCodeDataInfo\n        :param TotalCodeAll: Total occurrences of all status codes.\n        :type TotalCodeAll: int\n        :param TotalCode4xx: Occurrences of 4xx status codes.\n        :type TotalCode4xx: int\n        :param TotalCode5xx: Occurrences of 5xx status codes.\n        :type TotalCode5xx: int\n        :param TotalCodeList: Total occurrences of each status code.\n        :type TotalCodeList: list of PlayCodeTotalInfo\n        :param PageNum: Page number.\n        :type PageNum: int\n        :param PageSize: Number of entries per page.\n        :type PageSize: int\n        :param TotalPage: Total number of pages.\n        :type TotalPage: int\n        :param TotalNum: Total number of results.\n        :type TotalNum: int\n        :param TotalCode2xx: Occurrences of 2xx status codes.\n        :type TotalCode2xx: int\n        :param TotalCode3xx: Occurrences of 3xx status codes.\n        :type TotalCode3xx: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeProIspPlaySumInfoListRequest(AbstractModel):
    """DescribeProIspPlaySumInfoList request structure.

    """

    def __init__(self):
        """
        :param StartTime: Start time (Beijing time).
In the format of `yyyy-mm-dd HH:MM:SS`.\n        :type StartTime: str\n        :param EndTime: End time (Beijing time).
In the format of `yyyy-mm-dd HH:MM:SS`.
Note: `EndTime` and `StartTime` only support querying data for the last day.\n        :type EndTime: str\n        :param StatType: Statistics type. Valid values: Province (district), Isp (ISP), CountryOrArea (country or region).\n        :type StatType: str\n        :param PlayDomains: Playback domain name list. If it is left empty, it refers to all playback domain names.\n        :type PlayDomains: list of str\n        :param PageNum: Page number. Value range: [1,1000]. Default value: 1.\n        :type PageNum: int\n        :param PageSize: Number of entries per page. Value range: [1,1000]. Default value: 20.\n        :type PageSize: int\n        :param MainlandOrOversea: Region. Valid values: Mainland (data for Mainland China), Oversea (data for regions outside Mainland China), China (data for China, including Hong Kong, Macao, and Taiwan), Foreign (data for regions outside China, excluding Hong Kong, Macao, and Taiwan), Global (default). If this parameter is left empty, data for all regions will be queried.\n        :type MainlandOrOversea: str\n        :param OutLanguage: Language used in the output field. Valid values: Chinese (default), English. Currently, country/region, district, and ISP parameters support multiple languages.\n        :type OutLanguage: str\n        """
        self.StartTime = None
        self.EndTime = None
        self.StatType = None
        self.PlayDomains = None
        self.PageNum = None
        self.PageSize = None
        self.MainlandOrOversea = None
        self.OutLanguage = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.StatType = params.get("StatType")
        self.PlayDomains = params.get("PlayDomains")
        self.PageNum = params.get("PageNum")
        self.PageSize = params.get("PageSize")
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.OutLanguage = params.get("OutLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProIspPlaySumInfoListResponse(AbstractModel):
    """DescribeProIspPlaySumInfoList response structure.

    """

    def __init__(self):
        """
        :param TotalFlux: Total traffic.\n        :type TotalFlux: float\n        :param TotalRequest: Total number of requests.\n        :type TotalRequest: int\n        :param StatType: Statistics type.\n        :type StatType: str\n        :param PageSize: Number of results per page.\n        :type PageSize: int\n        :param PageNum: Page number.\n        :type PageNum: int\n        :param TotalNum: Total number of results.\n        :type TotalNum: int\n        :param TotalPage: Total number of pages.\n        :type TotalPage: int\n        :param DataInfoList: Aggregated data list by district, ISP, or country/region.\n        :type DataInfoList: list of ProIspPlaySumInfo\n        :param AvgFluxPerSecond: Download speed in MB/s. Calculation method: total traffic/total duration.\n        :type AvgFluxPerSecond: float\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalFlux = None
        self.TotalRequest = None
        self.StatType = None
        self.PageSize = None
        self.PageNum = None
        self.TotalNum = None
        self.TotalPage = None
        self.DataInfoList = None
        self.AvgFluxPerSecond = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalFlux = params.get("TotalFlux")
        self.TotalRequest = params.get("TotalRequest")
        self.StatType = params.get("StatType")
        self.PageSize = params.get("PageSize")
        self.PageNum = params.get("PageNum")
        self.TotalNum = params.get("TotalNum")
        self.TotalPage = params.get("TotalPage")
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = ProIspPlaySumInfo()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.AvgFluxPerSecond = params.get("AvgFluxPerSecond")
        self.RequestId = params.get("RequestId")


class DescribeProvinceIspPlayInfoListRequest(AbstractModel):
    """DescribeProvinceIspPlayInfoList request structure.

    """

    def __init__(self):
        """
        :param StartTime: Start point in time (Beijing time).
Example: 2019-02-21 10:00:00.\n        :type StartTime: str\n        :param EndTime: End point in time (Beijing time).
Example: 2019-02-21 12:00:00.
Note: `EndTime` and `StartTime` only support querying data for the last day.\n        :type EndTime: str\n        :param Granularity: Supported granularities:
1: 1-minute granularity (the query interval should be within 1 day)\n        :type Granularity: int\n        :param StatType: Statistical metric type:
"Bandwidth": bandwidth
"FluxPerSecond": average traffic
"Flux": traffic
"Request": number of requests
"Online": number of concurrent connections\n        :type StatType: str\n        :param PlayDomains: Playback domain name list.\n        :type PlayDomains: list of str\n        :param ProvinceNames: List of the districts to be queried, such as Beijing.\n        :type ProvinceNames: list of str\n        :param IspNames: List of the ISPs to be queried, such as China Mobile. If this parameter is left empty, the data of all ISPs will be queried.\n        :type IspNames: list of str\n        :param MainlandOrOversea: Region. Valid values: Mainland (data for Mainland China), Oversea (data for regions outside Mainland China), China (data for China, including Hong Kong, Macao, and Taiwan), Foreign (data for regions outside China, excluding Hong Kong, Macao, and Taiwan), Global (default). If this parameter is left empty, data for all regions will be queried.\n        :type MainlandOrOversea: str\n        :param IpType: IP type:
"Ipv6": IPv6 data
Data of all IPs will be returned if this parameter is left empty.\n        :type IpType: str\n        """
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
        """
        :param DataInfoList: Playback information list.\n        :type DataInfoList: list of PlayStatInfo\n        :param StatType: Statistics type, which is the same as the input parameter.\n        :type StatType: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param StartTime: Start time in UTC time in the format of `yyyy-mm-ddTHH:MM:SSZ`.\n        :type StartTime: str\n        :param EndTime: End time in UTC time in the format of `yyyy-mm-ddTHH:MM:SSZ`. Data for the last year can be queried.\n        :type EndTime: str\n        :param Zone: Region information. Valid values: Mainland, Oversea. The former is to query data within Mainland China, while the latter outside Mainland China. If this parameter is left empty, data of all regions will be queried.\n        :type Zone: str\n        :param PushDomains: Push domain name (data at the domain name level after November 1, 2019 can be queried).\n        :type PushDomains: list of str\n        :param Granularity: Data dimension. The data has a delay of one and a half hours. Valid values: 1. Minute (5-minute granularity, which supports a maximum query time range of 31 days); 2. Day (1-day granularity, which is the default value and supports a maximum query time range of 186 days).\n        :type Granularity: str\n        """
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
        """
        :param DataInfoList: Data information list.\n        :type DataInfoList: list of TimeValue\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param DayTime: Date in the format of YYYY-mm-dd
Data is available at 3am Beijing Time the next day. You are recommended to query the latest data after this time point. Data in the last 3 months can be queried.\n        :type DayTime: str\n        :param PlayDomain: Playback domain name.\n        :type PlayDomain: str\n        :param PageNum: Page number. Value range: [1,1000]. Default value: 1.\n        :type PageNum: int\n        :param PageSize: Number of entries per page. Value range: [100,1000]. Default value: 1,000.\n        :type PageSize: int\n        :param MainlandOrOversea: Valid values:
Mainland: query data for Mainland China,
Oversea: query data for regions outside Mainland China,
Default: query data for all regions.\n        :type MainlandOrOversea: str\n        :param ServiceName: Service name. Valid values: LVB, LEB. If this parameter is left empty, all data of LVB and LEB will be queried.\n        :type ServiceName: str\n        """
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
        """
        :param DataInfoList: Playback data information list.\n        :type DataInfoList: list of PlayDataInfoByStream\n        :param TotalNum: Total number.\n        :type TotalNum: int\n        :param TotalPage: Total number of pages.\n        :type TotalPage: int\n        :param PageNum: Page number where the current data resides.\n        :type PageNum: int\n        :param PageSize: Number of entries per page.\n        :type PageSize: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param StartTime: Start time (Beijing time) in the format of yyyy-mm-dd HH:MM:SS\n        :type StartTime: str\n        :param EndTime: End time (Beijing time) in the format of yyyy-mm-dd HH:MM:SS.
The difference between the start time and end time cannot be greater than 24 hours. Data in the last 30 days can be queried.\n        :type EndTime: str\n        :param PlayDomain: Playback domain name,
If this parameter is left empty, data of live streams of all playback domain names will be queried.\n        :type PlayDomain: str\n        :param StreamName: Stream name (exact match).
If this parameter is left empty, full playback data will be queried.\n        :type StreamName: str\n        :param AppName: Push address. Its value is the same as the `AppName` in playback address. It supports exact match, and takes effect only when `StreamName` is passed at the same time.
If it is left empty, the full playback data will be queried.
Note: to query by `AppName`, you need to submit a ticket first. After your application succeeds, it will take about 5 business days (subject to the time in the reply) for the configuration to take effect.\n        :type AppName: str\n        :param ServiceName: Service name. Valid values: LVB, LEB. If this parameter is left empty, all data of LVB and LEB will be queried.\n        :type ServiceName: str\n        """
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
        """
        :param DataInfoList: Statistics list at a 1-minute granularity.\n        :type DataInfoList: list of DayStreamPlayInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeStreamPushInfoListRequest(AbstractModel):
    """DescribeStreamPushInfoList request structure.

    """

    def __init__(self):
        """
        :param StreamName: Stream name.\n        :type StreamName: str\n        :param StartTime: Start time point in the format of `yyyy-mm-dd HH:MM:SS`.\n        :type StartTime: str\n        :param EndTime: End time point in the format of `yyyy-mm-dd HH:MM:SS`. The maximum time span is 6 hours. Data for the last 6 days can be queried.\n        :type EndTime: str\n        :param PushDomain: Push domain name.\n        :type PushDomain: str\n        :param AppName: Push path, which is the same as the `AppName` in push and playback addresses and is `live` by default.\n        :type AppName: str\n        """
        self.StreamName = None
        self.StartTime = None
        self.EndTime = None
        self.PushDomain = None
        self.AppName = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.PushDomain = params.get("PushDomain")
        self.AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStreamPushInfoListResponse(AbstractModel):
    """DescribeStreamPushInfoList response structure.

    """

    def __init__(self):
        """
        :param DataInfoList: Returned data list.\n        :type DataInfoList: list of PushQualityData\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.DataInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DataInfoList") is not None:
            self.DataInfoList = []
            for item in params.get("DataInfoList"):
                obj = PushQualityData()
                obj._deserialize(item)
                self.DataInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTopClientIpSumInfoListRequest(AbstractModel):
    """DescribeTopClientIpSumInfoList request structure.

    """

    def __init__(self):
        """
        :param StartTime: Start point in time in the format of `yyyy-mm-dd HH:MM:SS`.\n        :type StartTime: str\n        :param EndTime: End point in time in the format of `yyyy-mm-dd HH:MM:SS`
The time span is [0,4 hours]. Data for the last day can be queried.\n        :type EndTime: str\n        :param PlayDomains: Playback domain name. If this parameter is left empty, full data will be queried by default.\n        :type PlayDomains: list of str\n        :param PageNum: Page number. Value range: [1,1000]. Default value: 1.\n        :type PageNum: int\n        :param PageSize: Number of entries per page. Value range: [1,1000]. Default value: 20.\n        :type PageSize: int\n        :param OrderParam: Sorting metric. Valid values: TotalRequest (default value), FailedRequest, TotalFlux.\n        :type OrderParam: str\n        :param MainlandOrOversea: Region. Valid values: Mainland (data for Mainland China), Oversea (data for regions outside Mainland China), China (data for China, including Hong Kong, Macao, and Taiwan), Foreign (data for regions outside China, excluding Hong Kong, Macao, and Taiwan), Global (default). If this parameter is left empty, data for all regions will be queried.\n        :type MainlandOrOversea: str\n        :param OutLanguage: Language used in the output field. Valid values: Chinese (default), English. Currently, country/region, district, and ISP parameters support multiple languages.\n        :type OutLanguage: str\n        """
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
        """
        :param PageNum: Page number. Value range: [1,1000]. Default value: 1.\n        :type PageNum: int\n        :param PageSize: Number of entries per page. Value range: [1,1000]. Default value: 20.\n        :type PageSize: int\n        :param OrderParam: Sorting metric. Valid values: "TotalRequest", "FailedRequest", "TotalFlux".\n        :type OrderParam: str\n        :param TotalNum: Total number of results.\n        :type TotalNum: int\n        :param TotalPage: Total number of result pages.\n        :type TotalPage: int\n        :param DataInfoList: Data content.\n        :type DataInfoList: list of ClientIpPlaySumInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param StartTime: Start time point in the format of yyyy-mm-dd HH:MM:SS.\n        :type StartTime: str\n        :param EndTime: End time point in the format of yyyy-mm-dd HH:MM:SS. The difference between the start time and end time cannot be greater than 31 days. Data in the last 31 days can be queried.\n        :type EndTime: str\n        :param Domains: LVB domain names. If this parameter is left empty, data of all domain names will be queried.\n        :type Domains: list of str\n        :param Granularity: Time granularity of the data. Valid values:
5: 5-minute granularity (the query period is up to 1 day)
1440: 1-day granularity (the query period is up to 1 month)
Default value: 5\n        :type Granularity: int\n        """
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
        """
        :param DataInfoList: Detailed data.\n        :type DataInfoList: list of ConcurrentRecordStreamNum\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param StartTime: Start point in time in the format of `yyyy-mm-dd HH:MM:SS`.\n        :type StartTime: str\n        :param EndTime: End point in time in the format of `yyyy-mm-dd HH:MM:SS`
The time span is (0,4 hours]. Data for the last day can be queried.\n        :type EndTime: str\n        :param TopIndex: Bandwidth metric. Valid values: "Domain", "StreamId".\n        :type TopIndex: str\n        :param PlayDomains: Playback domain name. If this parameter is left empty, full data will be queried by default.\n        :type PlayDomains: list of str\n        :param PageNum: Page number,
Value range: [1,1000],
Default value: 1.\n        :type PageNum: int\n        :param PageSize: Number of entries per page. Value range: [1,1000].
Default value: 20.\n        :type PageSize: int\n        :param OrderParam: Sorting metric. Valid values: "AvgFluxPerSecond", "TotalRequest" (default), "TotalFlux".\n        :type OrderParam: str\n        """
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
        """
        :param PageNum: Page number,
Value range: [1,1000],
Default value: 1.\n        :type PageNum: int\n        :param PageSize: Number of entries per page. Value range: [1,1000].
Default value: 20.\n        :type PageSize: int\n        :param TopIndex: Bandwidth metric. Valid values: "Domain", "StreamId".\n        :type TopIndex: str\n        :param OrderParam: Sorting metric. Valid values: AvgFluxPerSecond (sort by average traffic per second), TotalRequest (sort by total requests), TotalFlux (sort by total traffic). Default value: TotalRequest.\n        :type OrderParam: str\n        :param TotalNum: Total number of results.\n        :type TotalNum: int\n        :param TotalPage: Total number of result pages.\n        :type TotalPage: int\n        :param DataInfoList: Data content.\n        :type DataInfoList: list of PlaySumStatInfo\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        """
        :param CertId: Certificate ID.\n        :type CertId: int\n        :param CertName: Certificate name.\n        :type CertName: str\n        :param Description: Description.\n        :type Description: str\n        :param CreateTime: Creation time in UTC format.\n        :type CreateTime: str\n        :param HttpsCrt: Certificate content.\n        :type HttpsCrt: str\n        :param CertType: Certificate type.
0: user-added certificate
1: Tencent Cloud-hosted certificate.\n        :type CertType: int\n        :param CertExpireTime: Certificate expiration time in UTC format.\n        :type CertExpireTime: str\n        :param DomainName: Domain name that uses this certificate.\n        :type DomainName: str\n        :param Status: Certificate status.\n        :type Status: int\n        :param CertDomains: List of domain names in the certificate.
["*.x.com"] for example.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type CertDomains: list of str\n        :param CloudCertId: Tencent Cloud SSL certificate ID.
Note: this field may return `null`, indicating that no valid values can be obtained.\n        :type CloudCertId: str\n        """
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
        


class DomainDetailInfo(AbstractModel):
    """Statistics of each domain name.

    """

    def __init__(self):
        """
        :param MainlandOrOversea: In or outside Mainland China:
Mainland: data in Mainland China.
Oversea: data outside Mainland China.\n        :type MainlandOrOversea: str\n        :param Bandwidth: Bandwidth in Mbps.\n        :type Bandwidth: float\n        :param Flux: Traffic in MB.\n        :type Flux: float\n        :param Online: Number of viewers.\n        :type Online: int\n        :param Request: Number of requests.\n        :type Request: int\n        """
        self.MainlandOrOversea = None
        self.Bandwidth = None
        self.Flux = None
        self.Online = None
        self.Request = None


    def _deserialize(self, params):
        self.MainlandOrOversea = params.get("MainlandOrOversea")
        self.Bandwidth = params.get("Bandwidth")
        self.Flux = params.get("Flux")
        self.Online = params.get("Online")
        self.Request = params.get("Request")
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
        """
        :param Name: LVB domain name.\n        :type Name: str\n        :param Type: Domain name type:
0: push.
1: playback.\n        :type Type: int\n        :param Status: Domain name status:
0: deactivated.
1: activated.\n        :type Status: int\n        :param CreateTime: Creation time.\n        :type CreateTime: str\n        :param BCName: Whether there is a CNAME record pointing to a fixed rule domain name:
0: no.
1: yes.\n        :type BCName: int\n        :param TargetDomain: Domain name corresponding to CNAME record.\n        :type TargetDomain: str\n        :param PlayType: Playback region. This parameter is valid only if `Type` is 1.
1: in Mainland China.
2: global.
3: outside Mainland China.\n        :type PlayType: int\n        :param IsDelayLive: Whether it is LCB:
0: LVB.
1: LCB.\n        :type IsDelayLive: int\n        :param CurrentCName: Information of currently used CNAME record.\n        :type CurrentCName: str\n        :param RentTag: Disused parameter, which can be ignored.\n        :type RentTag: int\n        :param RentExpireTime: Disused parameter, which can be ignored.\n        :type RentExpireTime: str\n        :param IsMiniProgramLive: 0: LVB.
1: LVB on Mini Program.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IsMiniProgramLive: int\n        """
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
        


class DomainInfoList(AbstractModel):
    """Multi-domain name information list

    """

    def __init__(self):
        """
        :param Domain: Domain name.\n        :type Domain: str\n        :param DetailInfoList: Details.\n        :type DetailInfoList: list of DomainDetailInfo\n        """
        self.Domain = None
        self.DetailInfoList = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("DetailInfoList") is not None:
            self.DetailInfoList = []
            for item in params.get("DetailInfoList"):
                obj = DomainDetailInfo()
                obj._deserialize(item)
                self.DetailInfoList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DropLiveStreamRequest(AbstractModel):
    """DropLiveStream request structure.

    """

    def __init__(self):
        """
        :param StreamName: Stream name.\n        :type StreamName: str\n        :param DomainName: Your acceleration domain name.\n        :type DomainName: str\n        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.\n        :type AppName: str\n        """
        self.StreamName = None
        self.DomainName = None
        self.AppName = None


    def _deserialize(self, params):
        self.StreamName = params.get("StreamName")
        self.DomainName = params.get("DomainName")
        self.AppName = params.get("AppName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DropLiveStreamResponse(AbstractModel):
    """DropLiveStream response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableLiveDomainRequest(AbstractModel):
    """EnableLiveDomain request structure.

    """

    def __init__(self):
        """
        :param DomainName: LVB domain name to be enabled.\n        :type DomainName: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ForbidLiveDomainRequest(AbstractModel):
    """ForbidLiveDomain request structure.

    """

    def __init__(self):
        """
        :param DomainName: LVB domain name to be disabled.\n        :type DomainName: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ForbidLiveStreamRequest(AbstractModel):
    """ForbidLiveStream request structure.

    """

    def __init__(self):
        """
        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.\n        :type AppName: str\n        :param DomainName: Your push domain name.\n        :type DomainName: str\n        :param StreamName: Stream name.\n        :type StreamName: str\n        :param ResumeTime: Time to resume the stream in UTC format, such as 2018-11-29T19:00:00Z.
Notes:
1. The duration of forbidding is 7 days by default and can be up to 90 days.
2. The Beijing time is in UTC+8. This value should be in the format as required by ISO 8601. For more information, please see [ISO Date and Time Format](https://intl.cloud.tencent.com/document/product/266/11732?from_cn_redirect=1#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F).\n        :type ResumeTime: str\n        :param Reason: Reason for forbidding.
Note: Be sure to enter the reason for forbidding to avoid any faulty operations.
Length limit: 2,048 bytes.\n        :type Reason: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ForbidStreamInfo(AbstractModel):
    """List of forbidden streams

    """

    def __init__(self):
        """
        :param StreamName: Stream name.\n        :type StreamName: str\n        :param CreateTime: Creation time.\n        :type CreateTime: str\n        :param ExpireTime: Forbidding expiration time.\n        :type ExpireTime: str\n        """
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
        """
        :param ProvinceName: District.\n        :type ProvinceName: str\n        :param IspName: ISP.\n        :type IspName: str\n        :param DetailInfoList: Detailed data at the minute level.\n        :type DetailInfoList: list of CdnPlayStatData\n        """
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
        """
        :param FlowContinueDuration: Timeout period for restarting an interrupted HLS push.
Value range: [0, 1,800].\n        :type FlowContinueDuration: int\n        """
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
        """
        :param HttpCode: HTTP return code.
Example: "2xx", "3xx", "4xx", "5xx".\n        :type HttpCode: str\n        :param ValueList: Statistics. 0 will be added for points in time when there is no data.\n        :type ValueList: list of HttpCodeValue\n        """
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
        """
        :param Time: Time in the format of `yyyy-mm-dd HH:MM:SS`.\n        :type Time: str\n        :param Numbers: Occurrences.\n        :type Numbers: int\n        :param Percentage: Proportion.\n        :type Percentage: float\n        """
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
        """
        :param Time: Data point in time,
In the format of `yyyy-mm-dd HH:MM:SS`.\n        :type Time: str\n        :param HttpStatusInfoList: Playback status code details.\n        :type HttpStatusInfoList: list of HttpStatusInfo\n        """
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
        """
        :param HttpStatus: Playback HTTP status code.\n        :type HttpStatus: str\n        :param Num: Quantity.\n        :type Num: int\n        """
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
        """
        :param TemplateId: Template ID returned by the `DescribeLiveCallbackTemplates` API.\n        :type TemplateId: int\n        :param TemplateName: Template name.\n        :type TemplateName: str\n        :param Description: Description.\n        :type Description: str\n        :param StreamBeginNotifyUrl: Stream starting callback URL.\n        :type StreamBeginNotifyUrl: str\n        :param StreamEndNotifyUrl: Interruption callback URL.\n        :type StreamEndNotifyUrl: str\n        :param RecordNotifyUrl: Recording callback URL.\n        :type RecordNotifyUrl: str\n        :param SnapshotNotifyUrl: Screencapturing callback URL.\n        :type SnapshotNotifyUrl: str\n        :param PornCensorshipNotifyUrl: Porn detection callback URL.\n        :type PornCensorshipNotifyUrl: str\n        :param CallbackKey: Callback key. The callback URL is public. For the callback signature, please see the event message notification document.
[Event Message Notification](https://intl.cloud.tencent.com/document/product/267/32744?from_cn_redirect=1).\n        :type CallbackKey: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveCertRequest(AbstractModel):
    """ModifyLiveCert request structure.

    """

    def __init__(self):
        """
        :param CertId: Certificate ID.\n        :type CertId: str\n        :param CertType: Certificate type. 0: user-added certificate, 1: Tencent Cloud-hosted certificate.\n        :type CertType: int\n        :param CertName: Certificate name.\n        :type CertName: str\n        :param HttpsCrt: Certificate content, i.e., public key.\n        :type HttpsCrt: str\n        :param HttpsKey: Private key.\n        :type HttpsKey: str\n        :param Description: Description.\n        :type Description: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveDomainCertRequest(AbstractModel):
    """ModifyLiveDomainCert request structure.

    """

    def __init__(self):
        """
        :param DomainName: Playback domain name.\n        :type DomainName: str\n        :param CertId: Certificate ID.\n        :type CertId: int\n        :param Status: Status. 0: off, 1: on.\n        :type Status: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveDomainRefererRequest(AbstractModel):
    """ModifyLiveDomainReferer request structure.

    """

    def __init__(self):
        """
        :param DomainName: Playback domain name\n        :type DomainName: str\n        :param Enable: Whether to enable referer allowlist/blocklist authentication for the current domain name\n        :type Enable: int\n        :param Type: List type. Valid values: `0` (blocklist), `1` (allowlist)\n        :type Type: int\n        :param AllowEmpty: Whether to allow empty referer. Valid values: `0` (no), `1` (yes)\n        :type AllowEmpty: int\n        :param Rules: Referer list. Separate items in it with semicolons (;).\n        :type Rules: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLivePlayAuthKeyRequest(AbstractModel):
    """ModifyLivePlayAuthKey request structure.

    """

    def __init__(self):
        """
        :param DomainName: Playback domain name.\n        :type DomainName: str\n        :param Enable: Whether to enable. 0: disabled; 1: enabled.
If this parameter is left empty, the current value will not be modified.\n        :type Enable: int\n        :param AuthKey: Authentication key.
If this parameter is left empty, the current value will not be modified.\n        :type AuthKey: str\n        :param AuthDelta: Validity period in seconds.
If this parameter is left empty, the current value will not be modified.\n        :type AuthDelta: int\n        :param AuthBackKey: Backup authentication key.
If this parameter is left empty, the current value will not be modified.\n        :type AuthBackKey: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLivePlayDomainRequest(AbstractModel):
    """ModifyLivePlayDomain request structure.

    """

    def __init__(self):
        """
        :param DomainName: Playback domain name.\n        :type DomainName: str\n        :param PlayType: Pull domain name type. 1: Mainland China. 2: global, 3: outside Mainland China\n        :type PlayType: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLivePushAuthKeyRequest(AbstractModel):
    """ModifyLivePushAuthKey request structure.

    """

    def __init__(self):
        """
        :param DomainName: Push domain name.\n        :type DomainName: str\n        :param Enable: Whether to enable. 0: disabled; 1: enabled.
If this parameter is left empty, the current value will not be modified.\n        :type Enable: int\n        :param MasterAuthKey: Master authentication key.
If this parameter is left empty, the current value will not be modified.\n        :type MasterAuthKey: str\n        :param BackupAuthKey: Backup authentication key.
If this parameter is left empty, the current value will not be modified.\n        :type BackupAuthKey: str\n        :param AuthDelta: Validity period in seconds.\n        :type AuthDelta: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveRecordTemplateRequest(AbstractModel):
    """ModifyLiveRecordTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID obtained through the `DescribeRecordTemplates` API.\n        :type TemplateId: int\n        :param TemplateName: Template name.\n        :type TemplateName: str\n        :param Description: Message description\n        :type Description: str\n        :param FlvParam: FLV recording parameter, which is set when FLV recording is enabled.\n        :type FlvParam: :class:`tencentcloud.live.v20180801.models.RecordParam`\n        :param HlsParam: HLS recording parameter, which is set when HLS recording is enabled.\n        :type HlsParam: :class:`tencentcloud.live.v20180801.models.RecordParam`\n        :param Mp4Param: MP4 recording parameter, which is set when MP4 recording is enabled.\n        :type Mp4Param: :class:`tencentcloud.live.v20180801.models.RecordParam`\n        :param AacParam: AAC recording parameter, which is set when AAC recording is enabled.\n        :type AacParam: :class:`tencentcloud.live.v20180801.models.RecordParam`\n        :param HlsSpecialParam: Custom HLS recording parameter.\n        :type HlsSpecialParam: :class:`tencentcloud.live.v20180801.models.HlsSpecialParam`\n        :param Mp3Param: MP3 recording parameter, which is set when MP3 recording is enabled.\n        :type Mp3Param: :class:`tencentcloud.live.v20180801.models.RecordParam`\n        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.FlvParam = None
        self.HlsParam = None
        self.Mp4Param = None
        self.AacParam = None
        self.HlsSpecialParam = None
        self.Mp3Param = None


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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveSnapshotTemplateRequest(AbstractModel):
    """ModifyLiveSnapshotTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.\n        :type TemplateId: int\n        :param TemplateName: Template name.
Maximum length: 255 bytes.\n        :type TemplateName: str\n        :param Description: Description.
Maximum length: 1,024 bytes.\n        :type Description: str\n        :param SnapshotInterval: Screencapturing interval in seconds. Default value: 10s.
Value range: 5-300s.\n        :type SnapshotInterval: int\n        :param Width: Screenshot width. Default value: 0 (original width).\n        :type Width: int\n        :param Height: Screenshot height. Default value: 0 (original height).\n        :type Height: int\n        :param PornFlag: Whether to enable porn detection. Default value: 0.
0: do not enable.
1: enable.\n        :type PornFlag: int\n        :param CosAppId: COS application ID.\n        :type CosAppId: int\n        :param CosBucket: COS bucket name.
Note: the value of `CosBucket` cannot contain `-[appid]`.\n        :type CosBucket: str\n        :param CosRegion: COS region.\n        :type CosRegion: str\n        :param CosPrefix: COS bucket folder prefix.\n        :type CosPrefix: str\n        :param CosFileName: COS filename.\n        :type CosFileName: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLiveTranscodeTemplateRequest(AbstractModel):
    """ModifyLiveTranscodeTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateId: Template ID.\n        :type TemplateId: int\n        :param Vcodec: Video codec. Valid values: h264, h265, origin (default)

origin: original codec as the output codec\n        :type Vcodec: str\n        :param Acodec: Audio codec. Defaut value: aac.
Note: this parameter is unsupported now.\n        :type Acodec: str\n        :param AudioBitrate: Audio bitrate. Default value: 0.
Value range: 0-500.\n        :type AudioBitrate: int\n        :param Description: Template description.\n        :type Description: str\n        :param VideoBitrate: Video bitrate in Kbps. Value range: 100-8000.
Note: the transcoding template requires that the bitrate be unique. Therefore, the final saved bitrate may be different from the input bitrate.\n        :type VideoBitrate: int\n        :param Width: Width in pixels. Value range: 0-3000.
It must be a multiple of 2. The original width is 0.\n        :type Width: int\n        :param NeedVideo: Whether to keep the video. 0: no; 1: yes. Default value: 1.\n        :type NeedVideo: int\n        :param NeedAudio: Whether to keep the audio. 0: no; 1: yes. Default value: 1.\n        :type NeedAudio: int\n        :param Height: Height in pixels. Value range: 0-3000.
It must be a multiple of 2. The original height is 0.\n        :type Height: int\n        :param Fps: Frame rate in fps. Default value: 0.
Value range: 0-60\n        :type Fps: int\n        :param Gop: Keyframe interval in seconds.
Value range: 2-6\n        :type Gop: int\n        :param Rotate: Rotation angle. Default value: 0.
Valid values: 0, 90, 180, 270\n        :type Rotate: int\n        :param Profile: Encoding quality:
baseline/main/high.\n        :type Profile: str\n        :param BitrateToOrig: Whether to use the original bitrate when the set bitrate is larger than the original bitrate.
0: no, 1: yes
Default value: 0.\n        :type BitrateToOrig: int\n        :param HeightToOrig: Whether to use the original height when the set height is higher than the original height.
0: no, 1: yes
Default value: 0.\n        :type HeightToOrig: int\n        :param FpsToOrig: Whether to use the original frame rate when the set frame rate is larger than the original frame rate.
0: no, 1: yes
Default value: 0.\n        :type FpsToOrig: int\n        :param AdaptBitratePercent: Bitrate compression ratio of top speed codec video.
Target bitrate of top speed code = VideoBitrate * (1-AdaptBitratePercent)

Value range: 0.0-0.5.\n        :type AdaptBitratePercent: float\n        :param ShortEdgeAsHeight: Whether to use the short side as the video height. 0: no, 1: yes. Default value: 0.\n        :type ShortEdgeAsHeight: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MonitorStreamPlayInfo(AbstractModel):
    """Monitored playback data

    """

    def __init__(self):
        """
        :param PlayDomain: Playback domain name.\n        :type PlayDomain: str\n        :param StreamName: Stream ID.\n        :type StreamName: str\n        :param Rate: Playback bitrate. 0 indicates the original bitrate.\n        :type Rate: int\n        :param Protocol: Playback protocol. Valid values: Unknown, Flv, Hls, Rtmp, Huyap2p.\n        :type Protocol: str\n        :param Bandwidth: Bandwidth in Mbps.\n        :type Bandwidth: float\n        :param Online: Number of online viewers. A data point is sampled per minute, and the number of TCP connections across the sample points is calculated.\n        :type Online: int\n        :param Request: Number of requests.\n        :type Request: int\n        """
        self.PlayDomain = None
        self.StreamName = None
        self.Rate = None
        self.Protocol = None
        self.Bandwidth = None
        self.Online = None
        self.Request = None


    def _deserialize(self, params):
        self.PlayDomain = params.get("PlayDomain")
        self.StreamName = params.get("StreamName")
        self.Rate = params.get("Rate")
        self.Protocol = params.get("Protocol")
        self.Bandwidth = params.get("Bandwidth")
        self.Online = params.get("Online")
        self.Request = params.get("Request")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PlayAuthKeyInfo(AbstractModel):
    """Playback authentication key information.

    """

    def __init__(self):
        """
        :param DomainName: Domain name.\n        :type DomainName: str\n        :param Enable: Whether to enable:
0: disable.
1: enable.\n        :type Enable: int\n        :param AuthKey: Authentication key.\n        :type AuthKey: str\n        :param AuthDelta: Validity period in seconds.\n        :type AuthDelta: int\n        :param AuthBackKey: Authentication `BackKey`.\n        :type AuthBackKey: str\n        """
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
        """
        :param Code: HTTP code. Valid values:
400, 403, 404, 500, 502, 503, 504.\n        :type Code: str\n        :param Num: Total occurrences.\n        :type Num: int\n        """
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
        """
        :param StreamName: Stream name.\n        :type StreamName: str\n        :param TotalFlux: Total traffic in MB.\n        :type TotalFlux: float\n        """
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
        """
        :param Time: Data point in time.\n        :type Time: str\n        :param Value: Value of bandwidth/traffic/number of requests/number of concurrent connections/download speed. If there is no data returned, the value is 0.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Value: float\n        """
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
        """
        :param Name: Domain name or stream ID.\n        :type Name: str\n        :param AvgFluxPerSecond: Average download speed,
In MB/s.
Calculation formula: average download speed per minute.\n        :type AvgFluxPerSecond: float\n        :param TotalFlux: Total traffic in MB.\n        :type TotalFlux: float\n        :param TotalRequest: Total number of requests.\n        :type TotalRequest: int\n        """
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
        """
        :param CountryAreaName: Country or region.\n        :type CountryAreaName: str\n        :param ProvinceName: District.\n        :type ProvinceName: str\n        :param IspName: ISP.\n        :type IspName: str\n        :param Code2xx: Occurrences of 2xx error codes.\n        :type Code2xx: int\n        :param Code3xx: Occurrences of 3xx error codes.\n        :type Code3xx: int\n        :param Code4xx: Occurrences of 4xx error codes.\n        :type Code4xx: int\n        :param Code5xx: Occurrences of 5xx error codes.\n        :type Code5xx: int\n        """
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
        


class ProIspPlaySumInfo(AbstractModel):
    """Queries playback information by district/ISP.

    """

    def __init__(self):
        """
        :param Name: District/ISP/country/region.\n        :type Name: str\n        :param TotalFlux: Total traffic in MB.\n        :type TotalFlux: float\n        :param TotalRequest: Total number of requests.\n        :type TotalRequest: int\n        :param AvgFluxPerSecond: Average download traffic in MB/s.\n        :type AvgFluxPerSecond: float\n        """
        self.Name = None
        self.TotalFlux = None
        self.TotalRequest = None
        self.AvgFluxPerSecond = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.TotalFlux = params.get("TotalFlux")
        self.TotalRequest = params.get("TotalRequest")
        self.AvgFluxPerSecond = params.get("AvgFluxPerSecond")
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
        """
        :param PublishTime: Push time.
In UTC format, such as 2018-06-29T19:00:00Z.\n        :type PublishTime: str\n        """
        self.PublishTime = None


    def _deserialize(self, params):
        self.PublishTime = params.get("PublishTime")
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
        """
        :param DomainName: Domain name.\n        :type DomainName: str\n        :param Enable: Whether to enable. 0: disabled; 1: enabled.\n        :type Enable: int\n        :param MasterAuthKey: Master authentication key.\n        :type MasterAuthKey: str\n        :param BackupAuthKey: Standby authentication key.\n        :type BackupAuthKey: str\n        :param AuthDelta: Validity period in seconds.\n        :type AuthDelta: int\n        """
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
        """
        :param StreamName: Stream name.\n        :type StreamName: str\n        :param AppName: Push path.\n        :type AppName: str\n        :param ClientIp: Push client IP.\n        :type ClientIp: str\n        :param ServerIp: IP of the server that receives the stream.\n        :type ServerIp: str\n        :param VideoFps: Pushed video frame rate in Hz.\n        :type VideoFps: int\n        :param VideoSpeed: Pushed video bitrate in bps.\n        :type VideoSpeed: int\n        :param AudioFps: Pushed audio frame rate in Hz.\n        :type AudioFps: int\n        :param AudioSpeed: Pushed audio bitrate in bps.\n        :type AudioSpeed: int\n        :param PushDomain: Push domain name.\n        :type PushDomain: str\n        :param BeginPushTime: Push start time.\n        :type BeginPushTime: str\n        :param Acodec: Audio codec,
Example: AAC.\n        :type Acodec: str\n        :param Vcodec: Video codec,
Example: H.264.\n        :type Vcodec: str\n        :param Resolution: Resolution.\n        :type Resolution: str\n        :param AsampleRate: Sample rate.\n        :type AsampleRate: int\n        :param MetaAudioSpeed: Audio bitrate in `metadata` in Kbps.\n        :type MetaAudioSpeed: int\n        :param MetaVideoSpeed: Video bitrate in `metadata` in Kbps.\n        :type MetaVideoSpeed: int\n        :param MetaFps: Frame rate in `metadata`.\n        :type MetaFps: int\n        """
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
        


class PushQualityData(AbstractModel):
    """Push quality data of a stream.

    """

    def __init__(self):
        """
        :param Time: Data time in the format of `%Y-%m-%d %H:%M:%S.%ms` and accurate down to the millisecond level.\n        :type Time: str\n        :param PushDomain: Push domain name.\n        :type PushDomain: str\n        :param AppName: Push path.\n        :type AppName: str\n        :param ClientIp: Push client IP.\n        :type ClientIp: str\n        :param BeginPushTime: Push start time in the format of `%Y-%m-%d %H:%M:%S.%ms` and accurate down to the millisecond level.\n        :type BeginPushTime: str\n        :param Resolution: Resolution information.\n        :type Resolution: str\n        :param VCodec: Video codec.\n        :type VCodec: str\n        :param ACodec: Audio codec.\n        :type ACodec: str\n        :param Sequence: Push serial number, which uniquely identifies a push.\n        :type Sequence: str\n        :param VideoFps: Video frame rate.\n        :type VideoFps: int\n        :param VideoRate: Video bitrate in bps.\n        :type VideoRate: int\n        :param AudioFps: Audio frame rate.\n        :type AudioFps: int\n        :param AudioRate: Audio bitrate in bps.\n        :type AudioRate: int\n        :param LocalTs: Local elapsed time in milliseconds. The greater the difference between audio/video elapsed time and local elapsed time, the poorer the push quality and the more serious the upstream lag.\n        :type LocalTs: int\n        :param VideoTs: Video elapsed time in milliseconds.\n        :type VideoTs: int\n        :param AudioTs: Audio elapsed time in milliseconds.\n        :type AudioTs: int\n        :param MetaVideoRate: Video bitrate in `metadata` in Kbps.\n        :type MetaVideoRate: int\n        :param MetaAudioRate: Audio bitrate in `metadata` in Kbps.\n        :type MetaAudioRate: int\n        :param MateFps: Frame rate in `metadata`.\n        :type MateFps: int\n        :param StreamParam: Push parameter\n        :type StreamParam: str\n        """
        self.Time = None
        self.PushDomain = None
        self.AppName = None
        self.ClientIp = None
        self.BeginPushTime = None
        self.Resolution = None
        self.VCodec = None
        self.ACodec = None
        self.Sequence = None
        self.VideoFps = None
        self.VideoRate = None
        self.AudioFps = None
        self.AudioRate = None
        self.LocalTs = None
        self.VideoTs = None
        self.AudioTs = None
        self.MetaVideoRate = None
        self.MetaAudioRate = None
        self.MateFps = None
        self.StreamParam = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.PushDomain = params.get("PushDomain")
        self.AppName = params.get("AppName")
        self.ClientIp = params.get("ClientIp")
        self.BeginPushTime = params.get("BeginPushTime")
        self.Resolution = params.get("Resolution")
        self.VCodec = params.get("VCodec")
        self.ACodec = params.get("ACodec")
        self.Sequence = params.get("Sequence")
        self.VideoFps = params.get("VideoFps")
        self.VideoRate = params.get("VideoRate")
        self.AudioFps = params.get("AudioFps")
        self.AudioRate = params.get("AudioRate")
        self.LocalTs = params.get("LocalTs")
        self.VideoTs = params.get("VideoTs")
        self.AudioTs = params.get("AudioTs")
        self.MetaVideoRate = params.get("MetaVideoRate")
        self.MetaAudioRate = params.get("MetaAudioRate")
        self.MateFps = params.get("MateFps")
        self.StreamParam = params.get("StreamParam")
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
        """
        :param RecordInterval: Max recording time per file
Default value: `1800` (seconds)
Value range: 60-7200
This parameter is invalid for HLS. Only one HLS file will be generated from push start to push end.\n        :type RecordInterval: int\n        :param StorageTime: Storage duration of the recording file
Value range: 0-129600000 seconds (0-1500 days)
`0`: permanent\n        :type StorageTime: int\n        :param Enable: Whether to enable recording in the current format. Default value: 0. 0: no, 1: yes.\n        :type Enable: int\n        :param VodSubAppId: VOD subapplication ID.\n        :type VodSubAppId: int\n        :param VodFileName: Recording filename.
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

If this parameter is not set, the recording filename will be `{StreamID}_{StartYear}-{StartMonth}-{StartDay}-{StartHour}-{StartMinute}-{StartSecond}_{EndYear}-{EndMonth}-{EndDay}-{EndHour}-{EndMinute}-{EndSecond}` by default\n        :type VodFileName: str\n        :param Procedure: Task flow
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type Procedure: str\n        :param StorageMode: Video storage class. Valid values:
`normal`: STANDARD
`cold`: STANDARD_IA
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type StorageMode: str\n        :param ClassId: VOD subapplication category
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type ClassId: int\n        """
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
        """
        :param TemplateId: Template ID.\n        :type TemplateId: int\n        :param TemplateName: Template name.\n        :type TemplateName: str\n        :param Description: Message description\n        :type Description: str\n        :param FlvParam: FLV recording parameter.\n        :type FlvParam: :class:`tencentcloud.live.v20180801.models.RecordParam`\n        :param HlsParam: HLS recording parameter.\n        :type HlsParam: :class:`tencentcloud.live.v20180801.models.RecordParam`\n        :param Mp4Param: MP4 recording parameter.\n        :type Mp4Param: :class:`tencentcloud.live.v20180801.models.RecordParam`\n        :param AacParam: AAC recording parameter.\n        :type AacParam: :class:`tencentcloud.live.v20180801.models.RecordParam`\n        :param IsDelayLive: 0: LVB,
1: LCB.\n        :type IsDelayLive: int\n        :param HlsSpecialParam: Custom HLS recording parameter\n        :type HlsSpecialParam: :class:`tencentcloud.live.v20180801.models.HlsSpecialParam`\n        :param Mp3Param: MP3 recording parameter.\n        :type Mp3Param: :class:`tencentcloud.live.v20180801.models.RecordParam`\n        """
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
        """
        :param DomainName: Domain name\n        :type DomainName: str\n        :param Enable: Whether to enable referer. Valid values: `0` (no), `1` (yes)\n        :type Enable: int\n        :param Type: List type. Valid values: `0` (blocklist), `1` (allowlist)\n        :type Type: int\n        :param AllowEmpty: Whether to allow empty referer. Valid values: `0` (no), `1` (yes)\n        :type AllowEmpty: int\n        :param Rules: Referer list. Separate items in it with semicolons (;).\n        :type Rules: str\n        """
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
        """
        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.\n        :type AppName: str\n        :param DomainName: Push domain name.\n        :type DomainName: str\n        :param StreamName: Stream name.\n        :type StreamName: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResumeLiveStreamRequest(AbstractModel):
    """ResumeLiveStream request structure.

    """

    def __init__(self):
        """
        :param AppName: Push path, which is the same as the AppName in push and playback addresses and is "live" by default.\n        :type AppName: str\n        :param DomainName: Your push domain name.\n        :type DomainName: str\n        :param StreamName: Stream name.\n        :type StreamName: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RuleInfo(AbstractModel):
    """Rule information.

    """

    def __init__(self):
        """
        :param CreateTime: Rule creation time.\n        :type CreateTime: str\n        :param UpdateTime: Rule update time.\n        :type UpdateTime: str\n        :param TemplateId: Template ID.\n        :type TemplateId: int\n        :param DomainName: Push domain name.\n        :type DomainName: str\n        :param AppName: Push path.\n        :type AppName: str\n        :param StreamName: Stream name.\n        :type StreamName: str\n        """
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
        """
        :param TemplateId: Template ID.\n        :type TemplateId: int\n        :param TemplateName: Template name.\n        :type TemplateName: str\n        :param SnapshotInterval: Screencapturing interval. Value range: 5-300s.\n        :type SnapshotInterval: int\n        :param Width: Screenshot width. Value range: 0-3000. 
0: original width and fit to the original ratio.\n        :type Width: int\n        :param Height: Screenshot height. Value range: 0-2000.
0: original height and fit to the original ratio.\n        :type Height: int\n        :param PornFlag: Whether to enable porn detection. 0: no, 1: yes.\n        :type PornFlag: int\n        :param CosAppId: COS application ID.\n        :type CosAppId: int\n        :param CosBucket: COS bucket name.\n        :type CosBucket: str\n        :param CosRegion: COS region.\n        :type CosRegion: str\n        :param Description: Template description.\n        :type Description: str\n        :param CosPrefix: COS bucket folder prefix.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CosPrefix: str\n        :param CosFileName: COS filename.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CosFileName: str\n        """
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
        """
        :param StreamName: Stream name.\n        :type StreamName: str\n        :param TaskId: Task ID returned by the `CreateLiveRecord` API.\n        :type TaskId: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopRecordTaskRequest(AbstractModel):
    """StopRecordTask request structure.

    """

    def __init__(self):
        """
        :param TaskId: Recording task ID.\n        :type TaskId: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StreamEventInfo(AbstractModel):
    """Streaming event information.

    """

    def __init__(self):
        """
        :param AppName: Application name.\n        :type AppName: str\n        :param DomainName: Push domain name.\n        :type DomainName: str\n        :param StreamName: Stream name.\n        :type StreamName: str\n        :param StreamStartTime: Push start time.
In UTC format, such as 2019-01-07T12:00:00Z.\n        :type StreamStartTime: str\n        :param StreamEndTime: Push end time.
In UTC format, such as 2019-01-07T15:00:00Z.\n        :type StreamEndTime: str\n        :param StopReason: Stop reason.\n        :type StopReason: str\n        :param Duration: Push duration in seconds.\n        :type Duration: int\n        :param ClientIp: Host IP.\n        :type ClientIp: str\n        :param Resolution: Resolution.\n        :type Resolution: str\n        """
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
        """
        :param StreamName: Stream name.\n        :type StreamName: str\n        :param AppName: Application name.\n        :type AppName: str\n        :param DomainName: Push domain name.\n        :type DomainName: str\n        :param StreamStartTime: Push start time.
In UTC format, such as 2019-01-07T12:00:00Z.\n        :type StreamStartTime: str\n        :param StreamEndTime: Push end time.
In UTC format, such as 2019-01-07T15:00:00Z.\n        :type StreamEndTime: str\n        :param StopReason: Stop reason.\n        :type StopReason: str\n        :param Duration: Push duration in seconds.\n        :type Duration: int\n        :param ClientIp: Host IP.\n        :type ClientIp: str\n        :param Resolution: Resolution.\n        :type Resolution: str\n        """
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
        """
        :param StreamName: Stream name.\n        :type StreamName: str\n        :param PublishTimeList: Push time list\n        :type PublishTimeList: list of PublishTime\n        :param AppName: Application name.\n        :type AppName: str\n        :param DomainName: Push domain name.\n        :type DomainName: str\n        """
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
        """
        :param Vcodec: Codec: h264/h265/origin. Default value: h264.

origin: keep the original codec.\n        :type Vcodec: str\n        :param VideoBitrate: Video bitrate. Value range: 0–8,000 Kbps.
If the value is 0, the original bitrate will be retained.
Note: transcoding templates require a unique bitrate. The final saved bitrate may differ from the input bitrate.\n        :type VideoBitrate: int\n        :param Acodec: Audio codec: aac. Default value: aac.
Note: This parameter will not take effect for now and will be supported soon.\n        :type Acodec: str\n        :param AudioBitrate: Audio bitrate. Value range: 0–500 Kbps.
0 by default.\n        :type AudioBitrate: int\n        :param Width: Width. Default value: 0.
Value range: [0-3,000].
The value must be a multiple of 2. The original width is 0.\n        :type Width: int\n        :param Height: Height. Default value: 0.
Value range: [0-3,000].
The value must be a multiple of 2. The original width is 0.\n        :type Height: int\n        :param Fps: Frame rate. Default value: 0.
Range: 0-60 Fps.\n        :type Fps: int\n        :param Gop: Keyframe interval, unit: second.
Original interval by default
Range: 2-6\n        :type Gop: int\n        :param Rotate: Rotation angle. Default value: 0.
Value range: 0, 90, 180, 270\n        :type Rotate: int\n        :param Profile: Encoding quality:
baseline/main/high. Default value: baseline.\n        :type Profile: str\n        :param BitrateToOrig: Whether to use the original bitrate when the set bitrate is larger than the original bitrate.
0: no, 1: yes
Default value: 0.\n        :type BitrateToOrig: int\n        :param HeightToOrig: Whether to use the original height when the set height is higher than the original height.
0: no, 1: yes
Default value: 0.\n        :type HeightToOrig: int\n        :param FpsToOrig: Whether to use the original frame rate when the set frame rate is larger than the original frame rate.
0: no, 1: yes
Default value: 0.\n        :type FpsToOrig: int\n        :param NeedVideo: Whether to keep the video. 0: no; 1: yes.\n        :type NeedVideo: int\n        :param NeedAudio: Whether to keep the audio. 0: no; 1: yes.\n        :type NeedAudio: int\n        :param TemplateId: Template ID.\n        :type TemplateId: int\n        :param TemplateName: Template name.\n        :type TemplateName: str\n        :param Description: Template description.\n        :type Description: str\n        :param AiTransCode: Whether it is a top speed codec template. 0: no, 1: yes. Default value: 0.\n        :type AiTransCode: int\n        :param AdaptBitratePercent: Bitrate compression ratio of top speed code video.
Target bitrate of top speed code = VideoBitrate * (1-AdaptBitratePercent)

Value range: 0.0-0.5.\n        :type AdaptBitratePercent: float\n        :param ShortEdgeAsHeight: Whether to take the shorter side as height. 0: no, 1: yes. Default value: 0.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type ShortEdgeAsHeight: int\n        """
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
        """
        :param Time: UTC time in the format of `yyyy-mm-ddTHH:MM:SSZ`.\n        :type Time: str\n        :param Num: Value.\n        :type Num: int\n        """
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
        """
        :param StreamName: Stream name.\n        :type StreamName: str\n        :param StartTime: Start time (Beijing time) in the format of `yyyy-mm-dd HH:MM`.\n        :type StartTime: str\n        :param EndTime: End time (Beijing time) in the format of `yyyy-mm-dd HH:MM`.\n        :type EndTime: str\n        :param Duration: Transcoding duration in minutes.
Note: given the possible interruptions during push, duration here is the sum of actual duration of transcoding instead of the interval between the start time and end time.\n        :type Duration: int\n        :param ModuleCodec: Codec with modules,
Example:
liveprocessor_H264: LVB transcoding - H264,
liveprocessor_H265: LVB transcoding - H265,
topspeed_H264: top speed codec - H264,
topspeed_H265: top speed codec - H265.\n        :type ModuleCodec: str\n        :param Bitrate: Bitrate.\n        :type Bitrate: int\n        :param Type: Type. Valid values: Transcode, MixStream, WaterMark.\n        :type Type: str\n        :param PushDomain: Push domain name.\n        :type PushDomain: str\n        :param Resolution: Resolution.\n        :type Resolution: str\n        """
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
        


class UnBindLiveDomainCertRequest(AbstractModel):
    """UnBindLiveDomainCert request structure.

    """

    def __init__(self):
        """
        :param DomainName: Playback domain name.\n        :type DomainName: str\n        :param Type: Valid values:
`gray`: unbind the canary certificate
`formal` (default): unbind the formal certificate

`formal` will be used if no value is passed in\n        :type Type: str\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateLiveWatermarkRequest(AbstractModel):
    """UpdateLiveWatermark request structure.

    """

    def __init__(self):
        """
        :param WatermarkId: Watermark ID.
Get the watermark ID in the returned value of the [AddLiveWatermark](https://intl.cloud.tencent.com/document/product/267/30154?from_cn_redirect=1) API call.\n        :type WatermarkId: int\n        :param PictureUrl: Watermark image URL.
Unallowed characters in the URL:
 ;(){}$>`#"\'|\n        :type PictureUrl: str\n        :param XPosition: Display position: X-axis offset in %. Default value: 0.\n        :type XPosition: int\n        :param YPosition: Display position: Y-axis offset in %. Default value: 0.\n        :type YPosition: int\n        :param WatermarkName: Watermark name.
Up to 16 bytes.\n        :type WatermarkName: str\n        :param Width: Watermark width or its percentage of the live streaming video width. It is recommended to just specify either height or width as the other will be scaled proportionally to avoid distortions. The original width is used by default.\n        :type Width: int\n        :param Height: Watermark height or its percentage of the live streaming video width. It is recommended to just specify either height or width as the other will be scaled proportionally to avoid distortions. The original height is used by default.\n        :type Height: int\n        """
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
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class WatermarkInfo(AbstractModel):
    """Watermark information.

    """

    def __init__(self):
        """
        :param WatermarkId: Watermark ID.\n        :type WatermarkId: int\n        :param PictureUrl: Watermark image URL.\n        :type PictureUrl: str\n        :param XPosition: Display position: X-axis offset.\n        :type XPosition: int\n        :param YPosition: Display position: Y-axis offset.\n        :type YPosition: int\n        :param WatermarkName: Watermark name.\n        :type WatermarkName: str\n        :param Status: Current status. 0: not used. 1: in use.\n        :type Status: int\n        :param CreateTime: Creation time.\n        :type CreateTime: str\n        :param Width: Watermark width.\n        :type Width: int\n        :param Height: Watermark height.\n        :type Height: int\n        """
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
        