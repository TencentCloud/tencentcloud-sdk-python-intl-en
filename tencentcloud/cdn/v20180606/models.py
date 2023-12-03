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


class AccessControl(AbstractModel):
    """Request header and request URL access control

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable access control based on the request header and request URL. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _AccessControlRules: Request header and request URL access rule
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AccessControlRules: list of AccessControlRule
        :param _ReturnCode: Returns status code
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ReturnCode: int
        """
        self._Switch = None
        self._AccessControlRules = None
        self._ReturnCode = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def AccessControlRules(self):
        return self._AccessControlRules

    @AccessControlRules.setter
    def AccessControlRules(self, AccessControlRules):
        self._AccessControlRules = AccessControlRules

    @property
    def ReturnCode(self):
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("AccessControlRules") is not None:
            self._AccessControlRules = []
            for item in params.get("AccessControlRules"):
                obj = AccessControlRule()
                obj._deserialize(item)
                self._AccessControlRules.append(obj)
        self._ReturnCode = params.get("ReturnCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessControlRule(AbstractModel):
    """Access control rule

    """

    def __init__(self):
        r"""
        :param _RuleType: requestHeader: access control over request header
url: access control over access URL
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleType: str
        :param _RuleContent: Blocked content
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleContent: str
        :param _Regex: on: regular match
off: exact match
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Regex: str
        :param _RuleHeader: This parameter is required only if `RuleType` is `requestHeader`
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleHeader: str
        """
        self._RuleType = None
        self._RuleContent = None
        self._Regex = None
        self._RuleHeader = None

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RuleContent(self):
        return self._RuleContent

    @RuleContent.setter
    def RuleContent(self, RuleContent):
        self._RuleContent = RuleContent

    @property
    def Regex(self):
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex

    @property
    def RuleHeader(self):
        return self._RuleHeader

    @RuleHeader.setter
    def RuleHeader(self, RuleHeader):
        self._RuleHeader = RuleHeader


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._RuleContent = params.get("RuleContent")
        self._Regex = params.get("Regex")
        self._RuleHeader = params.get("RuleHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCLSTopicDomainsRequest(AbstractModel):
    """AddCLSTopicDomains request structure.

    """

    def __init__(self):
        r"""
        :param _LogsetId: Logset ID
        :type LogsetId: str
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _DomainAreaConfigs: Region configuration for domains
        :type DomainAreaConfigs: list of DomainAreaConfig
        :param _Channel: Specifies whether to access CDN or ECDN. Valid values: `cdn` (default) and `ecdn`.
        :type Channel: str
        """
        self._LogsetId = None
        self._TopicId = None
        self._DomainAreaConfigs = None
        self._Channel = None

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def DomainAreaConfigs(self):
        return self._DomainAreaConfigs

    @DomainAreaConfigs.setter
    def DomainAreaConfigs(self, DomainAreaConfigs):
        self._DomainAreaConfigs = DomainAreaConfigs

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        if params.get("DomainAreaConfigs") is not None:
            self._DomainAreaConfigs = []
            for item in params.get("DomainAreaConfigs"):
                obj = DomainAreaConfig()
                obj._deserialize(item)
                self._DomainAreaConfigs.append(obj)
        self._Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCLSTopicDomainsResponse(AbstractModel):
    """AddCLSTopicDomains response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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


class AddCdnDomainRequest(AbstractModel):
    """AddCdnDomain request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain name
        :type Domain: str
        :param _ServiceType: Acceleration domain name service type
`web`: Webpage file downloads
`download`: Large file downloads
`media`: Audio and video on demand acceleration
`hybrid`: Dynamic and static content acceleration
`dynamic`: Dynamic content acceleration
        :type ServiceType: str
        :param _Origin: Origin server configuration
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param _ProjectId: Project ID. Default value: 0, indicating `Default Project`
        :type ProjectId: int
        :param _IpFilter: IP blocklist/allowlist
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param _IpFreqLimit: IP rate limiting
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param _StatusCodeCache: Status code cache
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param _Compression: Smart compression
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param _BandwidthAlert: Bandwidth cap configuration
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param _RangeOriginPull: Range GETs configuration
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param _FollowRedirect: 301/302 origin-pull follow-redirect configuration
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param _ErrorPage: Error code redirection (in beta)
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param _RequestHeader: Request header configuration
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param _ResponseHeader: Response header configuration
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param _DownstreamCapping: Download speed configuration
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param _CacheKey: Node cache key configuration
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param _ResponseHeaderCache: Header cache configuration
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param _VideoSeek: Video dragging configuration
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        :param _Cache: Cache validity configuration
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param _OriginPullOptimization: Cross-MLC-border origin-pull optimization
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param _Https: HTTPS acceleration
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param _Authentication: Timestamp hotlink protection
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param _Seo: SEO optimization
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param _ForceRedirect: Force redirect by access protocol
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param _Referer: Referer hotlink protection
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param _MaxAge: Browser caching (in beta)
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param _Ipv6: IPv6 configuration (This feature is in beta and not generally available yet.)
        :type Ipv6: :class:`tencentcloud.cdn.v20180606.models.Ipv6`
        :param _SpecificConfig: Specific region configuration
Applicable to cases where the acceleration domain name configuration differs for regions in and outside mainland China.
        :type SpecificConfig: :class:`tencentcloud.cdn.v20180606.models.SpecificConfig`
        :param _Area: Domain name acceleration region
mainland: acceleration inside mainland China
overseas: acceleration outside mainland China
global: global acceleration
Overseas acceleration service must be enabled to use overseas acceleration and global acceleration.
        :type Area: str
        :param _OriginPullTimeout: Origin-pull timeout configuration
        :type OriginPullTimeout: :class:`tencentcloud.cdn.v20180606.models.OriginPullTimeout`
        :param _Tag: Tag configuration
        :type Tag: list of Tag
        :param _Ipv6Access: Ipv6 access configuration
        :type Ipv6Access: :class:`tencentcloud.cdn.v20180606.models.Ipv6Access`
        :param _OfflineCache: Offline cache
        :type OfflineCache: :class:`tencentcloud.cdn.v20180606.models.OfflineCache`
        :param _Quic: QUIC access, which is a paid service. You can check the product document and Billing Overview for more information.
        :type Quic: :class:`tencentcloud.cdn.v20180606.models.Quic`
        :param _AwsPrivateAccess: Access authentication for S3 origin
        :type AwsPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`
        :param _OssPrivateAccess: Access authentication for OSS origin
        :type OssPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.OssPrivateAccess`
        :param _HwPrivateAccess: Origin-pull authentication for Huawei Cloud OBS origin
        :type HwPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.HwPrivateAccess`
        :param _QnPrivateAccess: Origin-pull authentication for Qiniu Cloud Kodo origin
        :type QnPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.QnPrivateAccess`
        :param _OthersPrivateAccess: Origin-pull authentication for other origins
        :type OthersPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.OthersPrivateAccess`
        :param _HttpsBilling: HTTPS (enabled by default), which is a paid service. You can check the product document and Billing Overview for more information.
        :type HttpsBilling: :class:`tencentcloud.cdn.v20180606.models.HttpsBilling`
        """
        self._Domain = None
        self._ServiceType = None
        self._Origin = None
        self._ProjectId = None
        self._IpFilter = None
        self._IpFreqLimit = None
        self._StatusCodeCache = None
        self._Compression = None
        self._BandwidthAlert = None
        self._RangeOriginPull = None
        self._FollowRedirect = None
        self._ErrorPage = None
        self._RequestHeader = None
        self._ResponseHeader = None
        self._DownstreamCapping = None
        self._CacheKey = None
        self._ResponseHeaderCache = None
        self._VideoSeek = None
        self._Cache = None
        self._OriginPullOptimization = None
        self._Https = None
        self._Authentication = None
        self._Seo = None
        self._ForceRedirect = None
        self._Referer = None
        self._MaxAge = None
        self._Ipv6 = None
        self._SpecificConfig = None
        self._Area = None
        self._OriginPullTimeout = None
        self._Tag = None
        self._Ipv6Access = None
        self._OfflineCache = None
        self._Quic = None
        self._AwsPrivateAccess = None
        self._OssPrivateAccess = None
        self._HwPrivateAccess = None
        self._QnPrivateAccess = None
        self._OthersPrivateAccess = None
        self._HttpsBilling = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def IpFilter(self):
        return self._IpFilter

    @IpFilter.setter
    def IpFilter(self, IpFilter):
        self._IpFilter = IpFilter

    @property
    def IpFreqLimit(self):
        return self._IpFreqLimit

    @IpFreqLimit.setter
    def IpFreqLimit(self, IpFreqLimit):
        self._IpFreqLimit = IpFreqLimit

    @property
    def StatusCodeCache(self):
        return self._StatusCodeCache

    @StatusCodeCache.setter
    def StatusCodeCache(self, StatusCodeCache):
        self._StatusCodeCache = StatusCodeCache

    @property
    def Compression(self):
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def BandwidthAlert(self):
        return self._BandwidthAlert

    @BandwidthAlert.setter
    def BandwidthAlert(self, BandwidthAlert):
        self._BandwidthAlert = BandwidthAlert

    @property
    def RangeOriginPull(self):
        return self._RangeOriginPull

    @RangeOriginPull.setter
    def RangeOriginPull(self, RangeOriginPull):
        self._RangeOriginPull = RangeOriginPull

    @property
    def FollowRedirect(self):
        return self._FollowRedirect

    @FollowRedirect.setter
    def FollowRedirect(self, FollowRedirect):
        self._FollowRedirect = FollowRedirect

    @property
    def ErrorPage(self):
        return self._ErrorPage

    @ErrorPage.setter
    def ErrorPage(self, ErrorPage):
        self._ErrorPage = ErrorPage

    @property
    def RequestHeader(self):
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader

    @property
    def ResponseHeader(self):
        return self._ResponseHeader

    @ResponseHeader.setter
    def ResponseHeader(self, ResponseHeader):
        self._ResponseHeader = ResponseHeader

    @property
    def DownstreamCapping(self):
        return self._DownstreamCapping

    @DownstreamCapping.setter
    def DownstreamCapping(self, DownstreamCapping):
        self._DownstreamCapping = DownstreamCapping

    @property
    def CacheKey(self):
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def ResponseHeaderCache(self):
        return self._ResponseHeaderCache

    @ResponseHeaderCache.setter
    def ResponseHeaderCache(self, ResponseHeaderCache):
        self._ResponseHeaderCache = ResponseHeaderCache

    @property
    def VideoSeek(self):
        return self._VideoSeek

    @VideoSeek.setter
    def VideoSeek(self, VideoSeek):
        self._VideoSeek = VideoSeek

    @property
    def Cache(self):
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def OriginPullOptimization(self):
        return self._OriginPullOptimization

    @OriginPullOptimization.setter
    def OriginPullOptimization(self, OriginPullOptimization):
        self._OriginPullOptimization = OriginPullOptimization

    @property
    def Https(self):
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def Authentication(self):
        return self._Authentication

    @Authentication.setter
    def Authentication(self, Authentication):
        self._Authentication = Authentication

    @property
    def Seo(self):
        return self._Seo

    @Seo.setter
    def Seo(self, Seo):
        self._Seo = Seo

    @property
    def ForceRedirect(self):
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def Referer(self):
        return self._Referer

    @Referer.setter
    def Referer(self, Referer):
        self._Referer = Referer

    @property
    def MaxAge(self):
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def Ipv6(self):
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def SpecificConfig(self):
        return self._SpecificConfig

    @SpecificConfig.setter
    def SpecificConfig(self, SpecificConfig):
        self._SpecificConfig = SpecificConfig

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def OriginPullTimeout(self):
        return self._OriginPullTimeout

    @OriginPullTimeout.setter
    def OriginPullTimeout(self, OriginPullTimeout):
        self._OriginPullTimeout = OriginPullTimeout

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Ipv6Access(self):
        return self._Ipv6Access

    @Ipv6Access.setter
    def Ipv6Access(self, Ipv6Access):
        self._Ipv6Access = Ipv6Access

    @property
    def OfflineCache(self):
        return self._OfflineCache

    @OfflineCache.setter
    def OfflineCache(self, OfflineCache):
        self._OfflineCache = OfflineCache

    @property
    def Quic(self):
        return self._Quic

    @Quic.setter
    def Quic(self, Quic):
        self._Quic = Quic

    @property
    def AwsPrivateAccess(self):
        return self._AwsPrivateAccess

    @AwsPrivateAccess.setter
    def AwsPrivateAccess(self, AwsPrivateAccess):
        self._AwsPrivateAccess = AwsPrivateAccess

    @property
    def OssPrivateAccess(self):
        return self._OssPrivateAccess

    @OssPrivateAccess.setter
    def OssPrivateAccess(self, OssPrivateAccess):
        self._OssPrivateAccess = OssPrivateAccess

    @property
    def HwPrivateAccess(self):
        return self._HwPrivateAccess

    @HwPrivateAccess.setter
    def HwPrivateAccess(self, HwPrivateAccess):
        self._HwPrivateAccess = HwPrivateAccess

    @property
    def QnPrivateAccess(self):
        return self._QnPrivateAccess

    @QnPrivateAccess.setter
    def QnPrivateAccess(self, QnPrivateAccess):
        self._QnPrivateAccess = QnPrivateAccess

    @property
    def OthersPrivateAccess(self):
        return self._OthersPrivateAccess

    @OthersPrivateAccess.setter
    def OthersPrivateAccess(self, OthersPrivateAccess):
        self._OthersPrivateAccess = OthersPrivateAccess

    @property
    def HttpsBilling(self):
        return self._HttpsBilling

    @HttpsBilling.setter
    def HttpsBilling(self, HttpsBilling):
        self._HttpsBilling = HttpsBilling


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._ServiceType = params.get("ServiceType")
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        self._ProjectId = params.get("ProjectId")
        if params.get("IpFilter") is not None:
            self._IpFilter = IpFilter()
            self._IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self._IpFreqLimit = IpFreqLimit()
            self._IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("StatusCodeCache") is not None:
            self._StatusCodeCache = StatusCodeCache()
            self._StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("Compression") is not None:
            self._Compression = Compression()
            self._Compression._deserialize(params.get("Compression"))
        if params.get("BandwidthAlert") is not None:
            self._BandwidthAlert = BandwidthAlert()
            self._BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("RangeOriginPull") is not None:
            self._RangeOriginPull = RangeOriginPull()
            self._RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("FollowRedirect") is not None:
            self._FollowRedirect = FollowRedirect()
            self._FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ErrorPage") is not None:
            self._ErrorPage = ErrorPage()
            self._ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("RequestHeader") is not None:
            self._RequestHeader = RequestHeader()
            self._RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self._ResponseHeader = ResponseHeader()
            self._ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("DownstreamCapping") is not None:
            self._DownstreamCapping = DownstreamCapping()
            self._DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("ResponseHeaderCache") is not None:
            self._ResponseHeaderCache = ResponseHeaderCache()
            self._ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("VideoSeek") is not None:
            self._VideoSeek = VideoSeek()
            self._VideoSeek._deserialize(params.get("VideoSeek"))
        if params.get("Cache") is not None:
            self._Cache = Cache()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("OriginPullOptimization") is not None:
            self._OriginPullOptimization = OriginPullOptimization()
            self._OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        if params.get("Authentication") is not None:
            self._Authentication = Authentication()
            self._Authentication._deserialize(params.get("Authentication"))
        if params.get("Seo") is not None:
            self._Seo = Seo()
            self._Seo._deserialize(params.get("Seo"))
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirect()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Referer") is not None:
            self._Referer = Referer()
            self._Referer._deserialize(params.get("Referer"))
        if params.get("MaxAge") is not None:
            self._MaxAge = MaxAge()
            self._MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Ipv6") is not None:
            self._Ipv6 = Ipv6()
            self._Ipv6._deserialize(params.get("Ipv6"))
        if params.get("SpecificConfig") is not None:
            self._SpecificConfig = SpecificConfig()
            self._SpecificConfig._deserialize(params.get("SpecificConfig"))
        self._Area = params.get("Area")
        if params.get("OriginPullTimeout") is not None:
            self._OriginPullTimeout = OriginPullTimeout()
            self._OriginPullTimeout._deserialize(params.get("OriginPullTimeout"))
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        if params.get("Ipv6Access") is not None:
            self._Ipv6Access = Ipv6Access()
            self._Ipv6Access._deserialize(params.get("Ipv6Access"))
        if params.get("OfflineCache") is not None:
            self._OfflineCache = OfflineCache()
            self._OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("Quic") is not None:
            self._Quic = Quic()
            self._Quic._deserialize(params.get("Quic"))
        if params.get("AwsPrivateAccess") is not None:
            self._AwsPrivateAccess = AwsPrivateAccess()
            self._AwsPrivateAccess._deserialize(params.get("AwsPrivateAccess"))
        if params.get("OssPrivateAccess") is not None:
            self._OssPrivateAccess = OssPrivateAccess()
            self._OssPrivateAccess._deserialize(params.get("OssPrivateAccess"))
        if params.get("HwPrivateAccess") is not None:
            self._HwPrivateAccess = HwPrivateAccess()
            self._HwPrivateAccess._deserialize(params.get("HwPrivateAccess"))
        if params.get("QnPrivateAccess") is not None:
            self._QnPrivateAccess = QnPrivateAccess()
            self._QnPrivateAccess._deserialize(params.get("QnPrivateAccess"))
        if params.get("OthersPrivateAccess") is not None:
            self._OthersPrivateAccess = OthersPrivateAccess()
            self._OthersPrivateAccess._deserialize(params.get("OthersPrivateAccess"))
        if params.get("HttpsBilling") is not None:
            self._HttpsBilling = HttpsBilling()
            self._HttpsBilling._deserialize(params.get("HttpsBilling"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCdnDomainResponse(AbstractModel):
    """AddCdnDomain response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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


class AdvanceCacheRule(AbstractModel):
    """Advanced cache configuration rules

    """

    def __init__(self):
        r"""
        :param _CacheType: Rule types:
`all`: Apply to all files.
`file`: Apply to files with the specified suffixes.
`directory`: Apply to specified paths.
`path`: Apply to specified absolute paths.
`default`: the cache rules when the origin server has not returned max-age
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CacheType: str
        :param _CacheContents: Content for each CacheType:
For `all`, enter a wildcard `*`.
For `file`, enter a suffix, e.g., `jpg` or `txt`.
For `directory`, enter a path, e.g., `/xxx/test/`.
For `path`, enter an absolute path, e.g., `/xxx/test.html`.
For `default`, enter "no max-age".
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CacheContents: list of str
        :param _CacheTime: Cache expiration time
Unit: second. The maximum value is 365 days.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CacheTime: int
        """
        self._CacheType = None
        self._CacheContents = None
        self._CacheTime = None

    @property
    def CacheType(self):
        return self._CacheType

    @CacheType.setter
    def CacheType(self, CacheType):
        self._CacheType = CacheType

    @property
    def CacheContents(self):
        return self._CacheContents

    @CacheContents.setter
    def CacheContents(self, CacheContents):
        self._CacheContents = CacheContents

    @property
    def CacheTime(self):
        return self._CacheTime

    @CacheTime.setter
    def CacheTime(self, CacheTime):
        self._CacheTime = CacheTime


    def _deserialize(self, params):
        self._CacheType = params.get("CacheType")
        self._CacheContents = params.get("CacheContents")
        self._CacheTime = params.get("CacheTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvanceConfig(AbstractModel):
    """Advanced configuration settings

    """

    def __init__(self):
        r"""
        :param _Name: Advanced configuration name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Name: str
        :param _Value: Whether to support advanced configuration
`on`: Supported
`off`: Not supported
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvanceHttps(AbstractModel):
    """Custom HTTPS configuration for origin-pull

    """

    def __init__(self):
        r"""
        :param _CustomTlsStatus: Custom TLS data switch
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CustomTlsStatus: str
        :param _TlsVersion: TLS version settings. Valid values: `TLSv1`, `TLSV1.1`, `TLSV1.2`, and `TLSv1.3`. Only consecutive versions can be enabled at the same time.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TlsVersion: list of str
        :param _Cipher: Custom encryption suite
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Cipher: str
        :param _VerifyOriginType: Origin-pull verification status
`off`: Disables origin-pull verification
`oneWay`: Only verify the origin
`twoWay`: Enables two-way origin-pull verification
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type VerifyOriginType: str
        :param _CertInfo: Configuration information of the origin-pull certificate
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CertInfo: :class:`tencentcloud.cdn.v20180606.models.ServerCert`
        :param _OriginCertInfo: Configuration information of the origin server certificate
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type OriginCertInfo: :class:`tencentcloud.cdn.v20180606.models.ClientCert`
        """
        self._CustomTlsStatus = None
        self._TlsVersion = None
        self._Cipher = None
        self._VerifyOriginType = None
        self._CertInfo = None
        self._OriginCertInfo = None

    @property
    def CustomTlsStatus(self):
        return self._CustomTlsStatus

    @CustomTlsStatus.setter
    def CustomTlsStatus(self, CustomTlsStatus):
        self._CustomTlsStatus = CustomTlsStatus

    @property
    def TlsVersion(self):
        return self._TlsVersion

    @TlsVersion.setter
    def TlsVersion(self, TlsVersion):
        self._TlsVersion = TlsVersion

    @property
    def Cipher(self):
        return self._Cipher

    @Cipher.setter
    def Cipher(self, Cipher):
        self._Cipher = Cipher

    @property
    def VerifyOriginType(self):
        return self._VerifyOriginType

    @VerifyOriginType.setter
    def VerifyOriginType(self, VerifyOriginType):
        self._VerifyOriginType = VerifyOriginType

    @property
    def CertInfo(self):
        return self._CertInfo

    @CertInfo.setter
    def CertInfo(self, CertInfo):
        self._CertInfo = CertInfo

    @property
    def OriginCertInfo(self):
        return self._OriginCertInfo

    @OriginCertInfo.setter
    def OriginCertInfo(self, OriginCertInfo):
        self._OriginCertInfo = OriginCertInfo


    def _deserialize(self, params):
        self._CustomTlsStatus = params.get("CustomTlsStatus")
        self._TlsVersion = params.get("TlsVersion")
        self._Cipher = params.get("Cipher")
        self._VerifyOriginType = params.get("VerifyOriginType")
        if params.get("CertInfo") is not None:
            self._CertInfo = ServerCert()
            self._CertInfo._deserialize(params.get("CertInfo"))
        if params.get("OriginCertInfo") is not None:
            self._OriginCertInfo = ClientCert()
            self._OriginCertInfo._deserialize(params.get("OriginCertInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthentication(AbstractModel):
    """Timestamp hotlink protection advanced configuration (allowlist feature)

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable hot linking protection. Values:
`on`: Enable
`off`: Disable
Only one advanced configuration can be enabled. Set the rests to `null`.
        :type Switch: str
        :param _TypeA: Timestamp hotlink protection advanced configuration mode A
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TypeA: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeA`
        :param _TypeB: Timestamp hotlink protection advanced configuration mode B
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TypeB: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeB`
        :param _TypeC: Timestamp hotlink protection advanced configuration mode C
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TypeC: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeC`
        :param _TypeD: Timestamp hotlink protection advanced configuration mode D
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TypeD: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeD`
        :param _TypeE: Timestamp hotlink protection advanced configuration mode E
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TypeE: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeE`
        :param _TypeF: Timestamp hotlink protection advanced configuration mode F
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TypeF: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeF`
        """
        self._Switch = None
        self._TypeA = None
        self._TypeB = None
        self._TypeC = None
        self._TypeD = None
        self._TypeE = None
        self._TypeF = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def TypeA(self):
        return self._TypeA

    @TypeA.setter
    def TypeA(self, TypeA):
        self._TypeA = TypeA

    @property
    def TypeB(self):
        return self._TypeB

    @TypeB.setter
    def TypeB(self, TypeB):
        self._TypeB = TypeB

    @property
    def TypeC(self):
        return self._TypeC

    @TypeC.setter
    def TypeC(self, TypeC):
        self._TypeC = TypeC

    @property
    def TypeD(self):
        return self._TypeD

    @TypeD.setter
    def TypeD(self, TypeD):
        self._TypeD = TypeD

    @property
    def TypeE(self):
        return self._TypeE

    @TypeE.setter
    def TypeE(self, TypeE):
        self._TypeE = TypeE

    @property
    def TypeF(self):
        return self._TypeF

    @TypeF.setter
    def TypeF(self, TypeF):
        self._TypeF = TypeF


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("TypeA") is not None:
            self._TypeA = AdvancedAuthenticationTypeA()
            self._TypeA._deserialize(params.get("TypeA"))
        if params.get("TypeB") is not None:
            self._TypeB = AdvancedAuthenticationTypeB()
            self._TypeB._deserialize(params.get("TypeB"))
        if params.get("TypeC") is not None:
            self._TypeC = AdvancedAuthenticationTypeC()
            self._TypeC._deserialize(params.get("TypeC"))
        if params.get("TypeD") is not None:
            self._TypeD = AdvancedAuthenticationTypeD()
            self._TypeD._deserialize(params.get("TypeD"))
        if params.get("TypeE") is not None:
            self._TypeE = AdvancedAuthenticationTypeE()
            self._TypeE._deserialize(params.get("TypeE"))
        if params.get("TypeF") is not None:
            self._TypeF = AdvancedAuthenticationTypeF()
            self._TypeF._deserialize(params.get("TypeF"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeA(AbstractModel):
    """Timestamp hotlink protection advanced configuration mode A

    """

    def __init__(self):
        r"""
        :param _SecretKey: Key used for signature calculation, allowing 6 to 32 bytes of letters and digits.
        :type SecretKey: str
        :param _SignParam: Signature field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
        :type SignParam: str
        :param _TimeParam: Time field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
        :type TimeParam: str
        :param _ExpireTime: Expiration time in seconds
        :type ExpireTime: int
        :param _ExpireTimeRequired: Whether the expiration time parameter is required
        :type ExpireTimeRequired: bool
        :param _Format: URL composition, e.g., `${private_key}${schema}${host}${full_uri}`.
        :type Format: str
        :param _TimeFormat: Time format. Valid values: dec (decimal), hex (hexadecimal).
        :type TimeFormat: str
        :param _FailCode: Status code returned when the authentication failed
        :type FailCode: int
        :param _ExpireCode: Status code returned when the URL expired
        :type ExpireCode: int
        :param _RulePaths: List of URLs to be authenticated
        :type RulePaths: list of str
        :param _Transformation: Reserved field
        :type Transformation: int
        """
        self._SecretKey = None
        self._SignParam = None
        self._TimeParam = None
        self._ExpireTime = None
        self._ExpireTimeRequired = None
        self._Format = None
        self._TimeFormat = None
        self._FailCode = None
        self._ExpireCode = None
        self._RulePaths = None
        self._Transformation = None

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def SignParam(self):
        return self._SignParam

    @SignParam.setter
    def SignParam(self, SignParam):
        self._SignParam = SignParam

    @property
    def TimeParam(self):
        return self._TimeParam

    @TimeParam.setter
    def TimeParam(self, TimeParam):
        self._TimeParam = TimeParam

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ExpireTimeRequired(self):
        return self._ExpireTimeRequired

    @ExpireTimeRequired.setter
    def ExpireTimeRequired(self, ExpireTimeRequired):
        self._ExpireTimeRequired = ExpireTimeRequired

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def TimeFormat(self):
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat

    @property
    def FailCode(self):
        return self._FailCode

    @FailCode.setter
    def FailCode(self, FailCode):
        self._FailCode = FailCode

    @property
    def ExpireCode(self):
        return self._ExpireCode

    @ExpireCode.setter
    def ExpireCode(self, ExpireCode):
        self._ExpireCode = ExpireCode

    @property
    def RulePaths(self):
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths

    @property
    def Transformation(self):
        return self._Transformation

    @Transformation.setter
    def Transformation(self, Transformation):
        self._Transformation = Transformation


    def _deserialize(self, params):
        self._SecretKey = params.get("SecretKey")
        self._SignParam = params.get("SignParam")
        self._TimeParam = params.get("TimeParam")
        self._ExpireTime = params.get("ExpireTime")
        self._ExpireTimeRequired = params.get("ExpireTimeRequired")
        self._Format = params.get("Format")
        self._TimeFormat = params.get("TimeFormat")
        self._FailCode = params.get("FailCode")
        self._ExpireCode = params.get("ExpireCode")
        self._RulePaths = params.get("RulePaths")
        self._Transformation = params.get("Transformation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeB(AbstractModel):
    """Timestamp hotlink protection advanced configuration mode B

    """

    def __init__(self):
        r"""
        :param _KeyAlpha: Alpha key name
        :type KeyAlpha: str
        :param _KeyBeta: Beta key name
        :type KeyBeta: str
        :param _KeyGamma: Gamma key name
        :type KeyGamma: str
        :param _SignParam: Signature field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
        :type SignParam: str
        :param _TimeParam: Time field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
        :type TimeParam: str
        :param _ExpireTime: Expiration time in seconds
        :type ExpireTime: int
        :param _TimeFormat: Time format. Valid values: dec (decimal), hex (hexadecimal).
        :type TimeFormat: str
        :param _FailCode: Status code returned when the authentication failed
        :type FailCode: int
        :param _ExpireCode: Status code returned when the URL expired
        :type ExpireCode: int
        :param _RulePaths: List of URLs to be authenticated
        :type RulePaths: list of str
        """
        self._KeyAlpha = None
        self._KeyBeta = None
        self._KeyGamma = None
        self._SignParam = None
        self._TimeParam = None
        self._ExpireTime = None
        self._TimeFormat = None
        self._FailCode = None
        self._ExpireCode = None
        self._RulePaths = None

    @property
    def KeyAlpha(self):
        return self._KeyAlpha

    @KeyAlpha.setter
    def KeyAlpha(self, KeyAlpha):
        self._KeyAlpha = KeyAlpha

    @property
    def KeyBeta(self):
        return self._KeyBeta

    @KeyBeta.setter
    def KeyBeta(self, KeyBeta):
        self._KeyBeta = KeyBeta

    @property
    def KeyGamma(self):
        return self._KeyGamma

    @KeyGamma.setter
    def KeyGamma(self, KeyGamma):
        self._KeyGamma = KeyGamma

    @property
    def SignParam(self):
        return self._SignParam

    @SignParam.setter
    def SignParam(self, SignParam):
        self._SignParam = SignParam

    @property
    def TimeParam(self):
        return self._TimeParam

    @TimeParam.setter
    def TimeParam(self, TimeParam):
        self._TimeParam = TimeParam

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def TimeFormat(self):
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat

    @property
    def FailCode(self):
        return self._FailCode

    @FailCode.setter
    def FailCode(self, FailCode):
        self._FailCode = FailCode

    @property
    def ExpireCode(self):
        return self._ExpireCode

    @ExpireCode.setter
    def ExpireCode(self, ExpireCode):
        self._ExpireCode = ExpireCode

    @property
    def RulePaths(self):
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths


    def _deserialize(self, params):
        self._KeyAlpha = params.get("KeyAlpha")
        self._KeyBeta = params.get("KeyBeta")
        self._KeyGamma = params.get("KeyGamma")
        self._SignParam = params.get("SignParam")
        self._TimeParam = params.get("TimeParam")
        self._ExpireTime = params.get("ExpireTime")
        self._TimeFormat = params.get("TimeFormat")
        self._FailCode = params.get("FailCode")
        self._ExpireCode = params.get("ExpireCode")
        self._RulePaths = params.get("RulePaths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeC(AbstractModel):
    """Timestamp hotlink protection advanced configuration mode C

    """

    def __init__(self):
        r"""
        :param _AccessKey: Access key
        :type AccessKey: str
        :param _SecretKey: Authentication key
        :type SecretKey: str
        """
        self._AccessKey = None
        self._SecretKey = None

    @property
    def AccessKey(self):
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey


    def _deserialize(self, params):
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeD(AbstractModel):
    """Timestamp hotlink protection advanced configuration mode D

    """

    def __init__(self):
        r"""
        :param _SecretKey: Key used for signature calculation, allowing 6 to 32 bytes of letters and digits.
        :type SecretKey: str
        :param _BackupSecretKey: Alternative key used for authentication after the authentication key (`SecretKey`) failed
        :type BackupSecretKey: str
        :param _SignParam: Signature field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
        :type SignParam: str
        :param _TimeParam: Time field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
        :type TimeParam: str
        :param _ExpireTime: Expiration time in seconds
        :type ExpireTime: int
        :param _TimeFormat: Time format. Valid values: dec (decimal), hex (hexadecimal).
        :type TimeFormat: str
        """
        self._SecretKey = None
        self._BackupSecretKey = None
        self._SignParam = None
        self._TimeParam = None
        self._ExpireTime = None
        self._TimeFormat = None

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def BackupSecretKey(self):
        return self._BackupSecretKey

    @BackupSecretKey.setter
    def BackupSecretKey(self, BackupSecretKey):
        self._BackupSecretKey = BackupSecretKey

    @property
    def SignParam(self):
        return self._SignParam

    @SignParam.setter
    def SignParam(self, SignParam):
        self._SignParam = SignParam

    @property
    def TimeParam(self):
        return self._TimeParam

    @TimeParam.setter
    def TimeParam(self, TimeParam):
        self._TimeParam = TimeParam

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def TimeFormat(self):
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat


    def _deserialize(self, params):
        self._SecretKey = params.get("SecretKey")
        self._BackupSecretKey = params.get("BackupSecretKey")
        self._SignParam = params.get("SignParam")
        self._TimeParam = params.get("TimeParam")
        self._ExpireTime = params.get("ExpireTime")
        self._TimeFormat = params.get("TimeFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeE(AbstractModel):
    """Timestamp hotlink protection advanced configuration mode E

    """

    def __init__(self):
        r"""
        :param _SecretKey: Key used for signature calculation, allowing 6 to 32 bytes of letters and digits.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SecretKey: str
        :param _SignParam: Signature field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SignParam: str
        :param _AclSignParam: ACL signature field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AclSignParam: str
        :param _StartTimeParam: Start time field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type StartTimeParam: str
        :param _ExpireTimeParam: Expiration time field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ExpireTimeParam: str
        :param _TimeFormat: Time format (dec)
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TimeFormat: str
        """
        self._SecretKey = None
        self._SignParam = None
        self._AclSignParam = None
        self._StartTimeParam = None
        self._ExpireTimeParam = None
        self._TimeFormat = None

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def SignParam(self):
        return self._SignParam

    @SignParam.setter
    def SignParam(self, SignParam):
        self._SignParam = SignParam

    @property
    def AclSignParam(self):
        return self._AclSignParam

    @AclSignParam.setter
    def AclSignParam(self, AclSignParam):
        self._AclSignParam = AclSignParam

    @property
    def StartTimeParam(self):
        return self._StartTimeParam

    @StartTimeParam.setter
    def StartTimeParam(self, StartTimeParam):
        self._StartTimeParam = StartTimeParam

    @property
    def ExpireTimeParam(self):
        return self._ExpireTimeParam

    @ExpireTimeParam.setter
    def ExpireTimeParam(self, ExpireTimeParam):
        self._ExpireTimeParam = ExpireTimeParam

    @property
    def TimeFormat(self):
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat


    def _deserialize(self, params):
        self._SecretKey = params.get("SecretKey")
        self._SignParam = params.get("SignParam")
        self._AclSignParam = params.get("AclSignParam")
        self._StartTimeParam = params.get("StartTimeParam")
        self._ExpireTimeParam = params.get("ExpireTimeParam")
        self._TimeFormat = params.get("TimeFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeF(AbstractModel):
    """Timestamp hotlink protection advanced authentication configuration mode F (TypeF)

    """

    def __init__(self):
        r"""
        :param _SignParam: Signature field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SignParam: str
        :param _TimeParam: Time field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TimeParam: str
        :param _TransactionParam: Transaction field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TransactionParam: str
        :param _SecretKey: CMK used for signature calculation, allowing 6 to 32 bytes of letters and digits.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SecretKey: str
        :param _BackupSecretKey: Alternative key used for signature calculation, which is used after the CMK fails in authentication. It allows 6 to 32 bytes of letters and digits.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type BackupSecretKey: str
        """
        self._SignParam = None
        self._TimeParam = None
        self._TransactionParam = None
        self._SecretKey = None
        self._BackupSecretKey = None

    @property
    def SignParam(self):
        return self._SignParam

    @SignParam.setter
    def SignParam(self, SignParam):
        self._SignParam = SignParam

    @property
    def TimeParam(self):
        return self._TimeParam

    @TimeParam.setter
    def TimeParam(self, TimeParam):
        self._TimeParam = TimeParam

    @property
    def TransactionParam(self):
        return self._TransactionParam

    @TransactionParam.setter
    def TransactionParam(self, TransactionParam):
        self._TransactionParam = TransactionParam

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def BackupSecretKey(self):
        return self._BackupSecretKey

    @BackupSecretKey.setter
    def BackupSecretKey(self, BackupSecretKey):
        self._BackupSecretKey = BackupSecretKey


    def _deserialize(self, params):
        self._SignParam = params.get("SignParam")
        self._TimeParam = params.get("TimeParam")
        self._TransactionParam = params.get("TransactionParam")
        self._SecretKey = params.get("SecretKey")
        self._BackupSecretKey = params.get("BackupSecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedCCRules(AbstractModel):
    """SCDN custom CC rules

    """

    def __init__(self):
        r"""
        :param _RuleName: Rule name
        :type RuleName: str
        :param _DetectionTime: Detection duration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DetectionTime: int
        :param _FrequencyLimit: Detection frequency threshold
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FrequencyLimit: int
        :param _PunishmentSwitch: Whether to enable IP blocking. Values:
`on`: Enable
`off`: Disable
Note: This field may return·`null`, indicating that no valid values can be obtained.
        :type PunishmentSwitch: str
        :param _PunishmentTime: IP penalty duration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type PunishmentTime: int
        :param _Action: Action. Valid values: `intercept` and `redirect`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Action: str
        :param _RedirectUrl: A redirection URL used when Action is `redirect`
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RedirectUrl: str
        :param _Configure: Layer-7 rule configuration for CC frequency limiting
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Configure: list of ScdnSevenLayerRules
        :param _Switch: Whether to enable custom CC rules. Values:
`on`: Enable
`off`: Disable
Note: This field may return·`null`, indicating that no valid values can be obtained.
        :type Switch: str
        """
        self._RuleName = None
        self._DetectionTime = None
        self._FrequencyLimit = None
        self._PunishmentSwitch = None
        self._PunishmentTime = None
        self._Action = None
        self._RedirectUrl = None
        self._Configure = None
        self._Switch = None

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def DetectionTime(self):
        return self._DetectionTime

    @DetectionTime.setter
    def DetectionTime(self, DetectionTime):
        self._DetectionTime = DetectionTime

    @property
    def FrequencyLimit(self):
        return self._FrequencyLimit

    @FrequencyLimit.setter
    def FrequencyLimit(self, FrequencyLimit):
        self._FrequencyLimit = FrequencyLimit

    @property
    def PunishmentSwitch(self):
        return self._PunishmentSwitch

    @PunishmentSwitch.setter
    def PunishmentSwitch(self, PunishmentSwitch):
        self._PunishmentSwitch = PunishmentSwitch

    @property
    def PunishmentTime(self):
        return self._PunishmentTime

    @PunishmentTime.setter
    def PunishmentTime(self, PunishmentTime):
        self._PunishmentTime = PunishmentTime

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RedirectUrl(self):
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl

    @property
    def Configure(self):
        return self._Configure

    @Configure.setter
    def Configure(self, Configure):
        self._Configure = Configure

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._DetectionTime = params.get("DetectionTime")
        self._FrequencyLimit = params.get("FrequencyLimit")
        self._PunishmentSwitch = params.get("PunishmentSwitch")
        self._PunishmentTime = params.get("PunishmentTime")
        self._Action = params.get("Action")
        self._RedirectUrl = params.get("RedirectUrl")
        if params.get("Configure") is not None:
            self._Configure = []
            for item in params.get("Configure"):
                obj = ScdnSevenLayerRules()
                obj._deserialize(item)
                self._Configure.append(obj)
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedCache(AbstractModel):
    """(Disused) Advanced cache validity configuration. You can use `RuleCache` instead.

    """

    def __init__(self):
        r"""
        :param _CacheRules: Cache expiration rule
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CacheRules: list of AdvanceCacheRule
        :param _IgnoreCacheControl: Forced cache configuration
on: enabled
off: disabled
When this is enabled, if the origin server returns no-cache, no-store headers, node caching will still be performed according to the cache expiration rules.
This is disabled by default
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IgnoreCacheControl: str
        :param _IgnoreSetCookie: Whether to ignore the header and body on cache nodes if the origin server returns the header `Set-Cookie`.
`on`: Ignore; do not cache the header and body.
`off`: Do not ignore; follow the custom cache rules of cache nodes.
It is disabled by default.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IgnoreSetCookie: str
        """
        self._CacheRules = None
        self._IgnoreCacheControl = None
        self._IgnoreSetCookie = None

    @property
    def CacheRules(self):
        return self._CacheRules

    @CacheRules.setter
    def CacheRules(self, CacheRules):
        self._CacheRules = CacheRules

    @property
    def IgnoreCacheControl(self):
        return self._IgnoreCacheControl

    @IgnoreCacheControl.setter
    def IgnoreCacheControl(self, IgnoreCacheControl):
        self._IgnoreCacheControl = IgnoreCacheControl

    @property
    def IgnoreSetCookie(self):
        return self._IgnoreSetCookie

    @IgnoreSetCookie.setter
    def IgnoreSetCookie(self, IgnoreSetCookie):
        self._IgnoreSetCookie = IgnoreSetCookie


    def _deserialize(self, params):
        if params.get("CacheRules") is not None:
            self._CacheRules = []
            for item in params.get("CacheRules"):
                obj = AdvanceCacheRule()
                obj._deserialize(item)
                self._CacheRules.append(obj)
        self._IgnoreCacheControl = params.get("IgnoreCacheControl")
        self._IgnoreSetCookie = params.get("IgnoreSetCookie")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedScdnAclGroup(AbstractModel):
    """SCDN precise access control configuration

    """

    def __init__(self):
        r"""
        :param _RuleName: Rule name
        :type RuleName: str
        :param _Configure: Specific configurations
        :type Configure: list of AdvancedScdnAclRule
        :param _Result: Action. Valid values: `intercept` and `redirect`.
        :type Result: str
        :param _Status: Whether the rule is activated. Valid values: `active` and `inactive`.
        :type Status: str
        :param _ErrorPage: Error page configuration
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ScdnErrorPage`
        """
        self._RuleName = None
        self._Configure = None
        self._Result = None
        self._Status = None
        self._ErrorPage = None

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Configure(self):
        return self._Configure

    @Configure.setter
    def Configure(self, Configure):
        self._Configure = Configure

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorPage(self):
        return self._ErrorPage

    @ErrorPage.setter
    def ErrorPage(self, ErrorPage):
        self._ErrorPage = ErrorPage


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        if params.get("Configure") is not None:
            self._Configure = []
            for item in params.get("Configure"):
                obj = AdvancedScdnAclRule()
                obj._deserialize(item)
                self._Configure.append(obj)
        self._Result = params.get("Result")
        self._Status = params.get("Status")
        if params.get("ErrorPage") is not None:
            self._ErrorPage = ScdnErrorPage()
            self._ErrorPage._deserialize(params.get("ErrorPage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedScdnAclRule(AbstractModel):
    """Precise access control rule

    """

    def __init__(self):
        r"""
        :param _MatchKey: Keyword. Valid values:
`protocol`: HTTP protocol
`httpVersion`: HTTP version
`method`: request method
`ip`: requester IP
`ipAsn`: ASN of the requester IP
`ipCountry`: country/region of the requester IP
`ipArea`: region of the requester IP
`xForwardFor`: X-Forward-For request header
`directory`: Path
`index`: Homepage
`path`: Full path of a file
`file`: File extension
`param`: Request parameter
`referer`: Referer request header
`cookie`: Cookie request header
`userAgent`: User-Agent request header
`head`: Custom request header
        :type MatchKey: str
        :param _LogicOperator: Logical operator. Valid values:
`exclude`: The keyword is not included
`include`: The keyword is included
`notequal`: Not the same as the keyword
`equal`: The same as the keyword
`matching`: The prefix is matched
`null`: Empty or does not exist
        :type LogicOperator: str
        :param _MatchValue: Matched value.
When `MatchKey` is `protocol`,
Values: `HTTP` and `HTTPS`.

When `MatchKey` is `httpVersion`,
Values: `HTTP/1.0`, `HTTP/1.1`, `HTTP/1.2`, `HTTP/2`, and `HTTP/3`.

When `MatchKey` is `method`,
Values: `HEAD`, `GET`, `POST`, `PUT`, `OPTIONS`, `TRACE`, `DELETE`, `PATCH` and `CONNECT`.

When `MatchKey` is `ipCountry`, valid values include:
`OTHER`: Other areas
`VE`: Venezuela
`UY`: Uruguay
`SR`: Suriname
`PY`: Paraguay
`PE`: Peru
`GY`: Guyana
`EC`: Ecuador
`CO`: Colombia
`CL`: Chile
`BR`: Brazil
`BO`: Bolivia
`AR`: Argentina
`NZ`: New Zealand
`WS`: Samoa
`VU`: Vanuatu
`TV`: Tuvalu
`TO`: Tonga
`TK`: Tokelau
`PW`: Palau
`NU`: Niue
`NR`: Nauru
`KI`: Kiribati
`GU`: Guam
`FM`: Micronesia
`AU`: Australia
`US`: United States
`PR`: Puerto Rico
`DO`: Dominican Republic
`CR`: Costa Rica
`AS`: American Samoa
`AG`: Antigua and Barbuda
`PA`: Panama
`NI`: Nicaragua
`MX`: Mexico
`JM`: Jamaica
`HT`: Haiti
`HN`: Honduras
`GT`: Guatemala
`GP`: Guadeloupe
`GL`: Greenland
`GD`: Grenada
`CU`: Cuba
`CA`: Canada
`BZ`: Belize
`BS`: Bahamas
`BM`: Bermuda
`BB`: Barbados
`AW`: Aruba
`AI`: Anguilla
`VA`: Vatican
`SK`: Slovakia
`GB`: United Kingdom
`CZ`: Czech Republic
`UA`: Ukraine
`TR`: Türkiye
`SI`: Slovenia
`SE`: Sweden
`RS`: Republic of Serbia
`RO`: Romania
`PT`: Portugal
`PL`: Poland
`NO`: Norway
`NL`: Netherlands
`MT`: Malta
`MK`: Macedonia
`ME`: Montenegro
`MD`: Moldova
`MC`: Monaco
`LV`: Latvia
`LU`: Luxembourg
`LT`: Lithuania
`LI`: Liechtenstein
`KZ`: Kazakhstan
`IT`: Italy
`IS`: Iceland
`IE`: Ireland
`HU`: Hungary
`HR`: Croatia
`GR`: Greece
`GI`: Gibraltar
`GG`: Guernsey
`GE`: Georgia
`FR`: France
`FI`: Finland
`ES`: Spain
`EE`: Estonia
`DK`: Denmark
`DE`: Germany
`CY`: Cyprus
`CH`: Switzerland
`BY`: Belarus
`BG`: Bulgaria
`BE`: Belgium
`AZ`: Azerbaijan
`AT`: Austria
`AM`: Armenia
`AL`: Albania
`AD`: Andorra
`TL`: East Timor
`SY`: Syria
`SA`: Saudi Arabia
`PS`: Palestine
`LK`: Sri Lanka
`LK`: Sri Lanka
`KP`: North Korea
`KG`: Kyrgyzstan
`HK`: Hong Kong, China
`BN`: Brunei
`BD`: Bangladesh
`AE`: United Arab Emirates
`YE`: Yemen
`VN`: Vietnam
`UZ`: Uzbekistan
`TW`: Taiwan, China
`TM`: Turkmenistan
`TJ`: Tajikistan
`TH`: Thailand
`SG`: Singapore
`QA`: Qatar
`PK`: Pakistan
`PH`: Philippines
`OM`: Oman
`NP`: Nepal
`MY`: Malaysia
`MV`: Maldives
`MO`: Macao, China
`MN`: Mongolia
`MM`: Myanmar
`LB`: Lebanon
`KW`: Kuwait
`KR`: South Korea
`KH`: Cambodia
`JP`: Japan
`JO`: Jordan
`IR`: Iran
`IQ`: Iraq
`IN`: India
`IL`: Israel
`ID`: Indonesia
`CN`: China
`BT`: Bhutan
`BH`: Bahrain
`AF`: Afghanistan
`LY`: Libya
`CD`: Democratic Republic of the Congo
`RE`: La Réunion
`SZ`: Swaziland
`ZW`: Zimbabwe
`ZM`: Zambia
`YT`: Mayotte
`UG`: Uganda
`TZ`: Tanzania
`TN`: Tunisia
`TG`: Togo
`TD`: Chad
`SO`: Somalia
`SN`: Senegal
`SD`: Sudan
`SC`: Seychelles
`RW`: Rwanda
`NG`: Nigeria
`NE`: Niger
`NA`: Namibia
`MZ`: Mozambique
`MW`: Malawi
`MU`: Mauritius
`MR`: Mauritania
`ML`: Mali
`MG`: Madagascar
`MA`: Morocco
`LS`: Lesotho
`LR`: Liberia
`KM`: Comoros
`KE`: Kenya
`GN`: Guinea
`GM`: Gambia
`GH`: Ghana
`GA`: Gabon
`ET`: Ethiopia
`ER`: Eritrea
`EG`: Egypt
`DZ`: Algeria
`DJ`: Djibouti
`CM`: Cameroon
`CG`: Republic of the Congo
`BW`: Botswana
`BJ`: Benin
`BI`: Burundi
`AO`: Angola

When MatchKey is `ipArea`, valid values include:
`OTHER`: Other areas
`AS`: Asia
`EU`: Europe
`AN`: Antarctica
`AF`: Africa
`OC`: Oceania
`NA`: North America
`SA`: South America

When MatchKey is `index`,
valid value is `/;/index.html`.
        :type MatchValue: list of str
        :param _CaseSensitive: Whether to distinguish uppercase or lowercase letters. `true`: case sensitive; `false`: case insensitive.
        :type CaseSensitive: bool
        :param _MatchKeyParam: This field is required when `MatchKey` is `param` or `cookie`. For `param`, it indicates a key value of the request parameter if MatchKey is `param`, while a key value of the Cookie request header if MatchKey is `cookie`.
        :type MatchKeyParam: str
        """
        self._MatchKey = None
        self._LogicOperator = None
        self._MatchValue = None
        self._CaseSensitive = None
        self._MatchKeyParam = None

    @property
    def MatchKey(self):
        return self._MatchKey

    @MatchKey.setter
    def MatchKey(self, MatchKey):
        self._MatchKey = MatchKey

    @property
    def LogicOperator(self):
        return self._LogicOperator

    @LogicOperator.setter
    def LogicOperator(self, LogicOperator):
        self._LogicOperator = LogicOperator

    @property
    def MatchValue(self):
        return self._MatchValue

    @MatchValue.setter
    def MatchValue(self, MatchValue):
        self._MatchValue = MatchValue

    @property
    def CaseSensitive(self):
        return self._CaseSensitive

    @CaseSensitive.setter
    def CaseSensitive(self, CaseSensitive):
        self._CaseSensitive = CaseSensitive

    @property
    def MatchKeyParam(self):
        return self._MatchKeyParam

    @MatchKeyParam.setter
    def MatchKeyParam(self, MatchKeyParam):
        self._MatchKeyParam = MatchKeyParam


    def _deserialize(self, params):
        self._MatchKey = params.get("MatchKey")
        self._LogicOperator = params.get("LogicOperator")
        self._MatchValue = params.get("MatchValue")
        self._CaseSensitive = params.get("CaseSensitive")
        self._MatchKeyParam = params.get("MatchKeyParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Authentication(AbstractModel):
    """Timestamp hotlink protection configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable hot linking protection. Values:
`on`: Enable
`off`: Disable
Only one advanced configuration can be enabled. Set the rests to `null`.
        :type Switch: str
        :param _AuthAlgorithm: Authentication algorithm. Values:
`md5`: Calculate the hash using MD5.
`sha256`: Calculate the hash using SHA-256.
Default value: `md5`.
Note: This field may return·`null`, indicating that no valid values can be obtained.
        :type AuthAlgorithm: str
        :param _TypeA: Timestamp hotlink protection mode A configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TypeA: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeA`
        :param _TypeB: Timestamp hotlink protection mode B configuration (mode B is being upgraded and is currently not supported)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TypeB: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeB`
        :param _TypeC: Timestamp hotlink protection mode C configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TypeC: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeC`
        :param _TypeD: Timestamp hotlink protection mode D configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TypeD: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeD`
        """
        self._Switch = None
        self._AuthAlgorithm = None
        self._TypeA = None
        self._TypeB = None
        self._TypeC = None
        self._TypeD = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def AuthAlgorithm(self):
        return self._AuthAlgorithm

    @AuthAlgorithm.setter
    def AuthAlgorithm(self, AuthAlgorithm):
        self._AuthAlgorithm = AuthAlgorithm

    @property
    def TypeA(self):
        return self._TypeA

    @TypeA.setter
    def TypeA(self, TypeA):
        self._TypeA = TypeA

    @property
    def TypeB(self):
        return self._TypeB

    @TypeB.setter
    def TypeB(self, TypeB):
        self._TypeB = TypeB

    @property
    def TypeC(self):
        return self._TypeC

    @TypeC.setter
    def TypeC(self, TypeC):
        self._TypeC = TypeC

    @property
    def TypeD(self):
        return self._TypeD

    @TypeD.setter
    def TypeD(self, TypeD):
        self._TypeD = TypeD


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._AuthAlgorithm = params.get("AuthAlgorithm")
        if params.get("TypeA") is not None:
            self._TypeA = AuthenticationTypeA()
            self._TypeA._deserialize(params.get("TypeA"))
        if params.get("TypeB") is not None:
            self._TypeB = AuthenticationTypeB()
            self._TypeB._deserialize(params.get("TypeB"))
        if params.get("TypeC") is not None:
            self._TypeC = AuthenticationTypeC()
            self._TypeC._deserialize(params.get("TypeC"))
        if params.get("TypeD") is not None:
            self._TypeD = AuthenticationTypeD()
            self._TypeD._deserialize(params.get("TypeD"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthenticationTypeA(AbstractModel):
    """Timestamp hotlink protection mode A configuration
    The access URL format of timestamp hotlink protection mode A is as follows: http://DomainName/Filename?sign=timestamp-rand-uid-md5hash
    Here, timestamp is a decimal timestamp in Unix format;
    rand is a random string composed of 0-100 characters, including digits, upper and lower-case letters.
    uid is 0;
    md5hash: MD5 (file path-timestamp-rand-uid-custom key)

    """

    def __init__(self):
        r"""
        :param _SecretKey: The key for signature calculation
6-32 characters. Only digits and letters are allowed. 
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SecretKey: str
        :param _SignParam: Signature parameter name
Only upper and lower-case letters, digits, and underscores (_) are allowed. It cannot start with a digit. Length limit: 1-100 characters.
        :type SignParam: str
        :param _ExpireTime: Signature expiration time
Unit: second. The maximum value is 630720000.
        :type ExpireTime: int
        :param _FileExtensions: File extension list settings determining if authentication should be performed
If it contains an asterisk (*), this indicates all files.
        :type FileExtensions: list of str
        :param _FilterType: `whitelist`: All file types apart from the FileExtensions list are authenticated.
`blacklist`: Only the file types in the FileExtensions list are authenticated.
        :type FilterType: str
        :param _BackupSecretKey: Backup key, which is used to calculate a signature.
6-32 characters. Only digits and letters are allowed. 
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type BackupSecretKey: str
        """
        self._SecretKey = None
        self._SignParam = None
        self._ExpireTime = None
        self._FileExtensions = None
        self._FilterType = None
        self._BackupSecretKey = None

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def SignParam(self):
        return self._SignParam

    @SignParam.setter
    def SignParam(self, SignParam):
        self._SignParam = SignParam

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def FileExtensions(self):
        return self._FileExtensions

    @FileExtensions.setter
    def FileExtensions(self, FileExtensions):
        self._FileExtensions = FileExtensions

    @property
    def FilterType(self):
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def BackupSecretKey(self):
        return self._BackupSecretKey

    @BackupSecretKey.setter
    def BackupSecretKey(self, BackupSecretKey):
        self._BackupSecretKey = BackupSecretKey


    def _deserialize(self, params):
        self._SecretKey = params.get("SecretKey")
        self._SignParam = params.get("SignParam")
        self._ExpireTime = params.get("ExpireTime")
        self._FileExtensions = params.get("FileExtensions")
        self._FilterType = params.get("FilterType")
        self._BackupSecretKey = params.get("BackupSecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthenticationTypeB(AbstractModel):
    """Timestamp hotlink protection mode B configuration (mode B is being upgraded and is currently not supported)

    """

    def __init__(self):
        r"""
        :param _SecretKey: The key for signature calculation
6-32 characters. Only digits and letters are allowed. 
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SecretKey: str
        :param _ExpireTime: Signature expiration time
Unit: second. The maximum value is 630720000.
        :type ExpireTime: int
        :param _FileExtensions: File extension list settings determining if authentication should be performed
If it contains an asterisk (*), this indicates all files.
        :type FileExtensions: list of str
        :param _FilterType: whitelist: indicates that all file types apart from the FileExtensions list are authenticated
blacklist: indicates that only the file types in the FileExtensions list are authenticated
        :type FilterType: str
        :param _BackupSecretKey: Backup key, which is used to calculate a signature.
6-32 characters. Only digits and letters are allowed. 
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type BackupSecretKey: str
        """
        self._SecretKey = None
        self._ExpireTime = None
        self._FileExtensions = None
        self._FilterType = None
        self._BackupSecretKey = None

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def FileExtensions(self):
        return self._FileExtensions

    @FileExtensions.setter
    def FileExtensions(self, FileExtensions):
        self._FileExtensions = FileExtensions

    @property
    def FilterType(self):
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def BackupSecretKey(self):
        return self._BackupSecretKey

    @BackupSecretKey.setter
    def BackupSecretKey(self, BackupSecretKey):
        self._BackupSecretKey = BackupSecretKey


    def _deserialize(self, params):
        self._SecretKey = params.get("SecretKey")
        self._ExpireTime = params.get("ExpireTime")
        self._FileExtensions = params.get("FileExtensions")
        self._FilterType = params.get("FilterType")
        self._BackupSecretKey = params.get("BackupSecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthenticationTypeC(AbstractModel):
    """Timestamp hotlink protection mode C configuration
    The access URL format of timestamp hotlink protection mode C is as follows: http://DomainName/md5hash/timestamp/FileName
    Here, timestamp is a hexadecimal timestamp in Unix format;
    `md5hash`: MD5 (custom key + file path + timestamp)

    """

    def __init__(self):
        r"""
        :param _SecretKey: The key for signature calculation
6-32 characters. Only digits and letters are allowed. 
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SecretKey: str
        :param _ExpireTime: Signature expiration time
Unit: second. The maximum value is 630720000.
        :type ExpireTime: int
        :param _FileExtensions: File extension list settings determining if authentication should be performed
If it contains an asterisk (*), this indicates all files.
        :type FileExtensions: list of str
        :param _FilterType: `whitelist`: All file types apart from the FileExtensions list are authenticated.
`blacklist`: Only the file types in the FileExtensions list are authenticated.
        :type FilterType: str
        :param _TimeFormat: Timestamp settings
`dec`: Decimal
`hex`: Hexadecimal
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TimeFormat: str
        :param _BackupSecretKey: Backup key, which is used to calculate a signature.
6-32 characters. Only digits and letters are allowed. 
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type BackupSecretKey: str
        """
        self._SecretKey = None
        self._ExpireTime = None
        self._FileExtensions = None
        self._FilterType = None
        self._TimeFormat = None
        self._BackupSecretKey = None

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def FileExtensions(self):
        return self._FileExtensions

    @FileExtensions.setter
    def FileExtensions(self, FileExtensions):
        self._FileExtensions = FileExtensions

    @property
    def FilterType(self):
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def TimeFormat(self):
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat

    @property
    def BackupSecretKey(self):
        return self._BackupSecretKey

    @BackupSecretKey.setter
    def BackupSecretKey(self, BackupSecretKey):
        self._BackupSecretKey = BackupSecretKey


    def _deserialize(self, params):
        self._SecretKey = params.get("SecretKey")
        self._ExpireTime = params.get("ExpireTime")
        self._FileExtensions = params.get("FileExtensions")
        self._FilterType = params.get("FilterType")
        self._TimeFormat = params.get("TimeFormat")
        self._BackupSecretKey = params.get("BackupSecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthenticationTypeD(AbstractModel):
    """Timestamp hotlink protection mode D configuration
    The access URL format of timestamp hotlink protection mode D is as follows: http://DomainName/FileName?sign=md5hash&t=timestamp
    Here, timestamp is a decimal or hexadecimal timestamp in Unix format;
    `md5hash`: MD5 (custom key + file path + timestamp)

    """

    def __init__(self):
        r"""
        :param _SecretKey: The key for signature calculation
6-32 characters. Only digits and letters are allowed. 
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SecretKey: str
        :param _ExpireTime: Signature expiration time
Unit: second. The maximum value is 630720000.
        :type ExpireTime: int
        :param _FileExtensions: File extension list settings determining if authentication should be performed
If it contains an asterisk (*), this indicates all files.
        :type FileExtensions: list of str
        :param _FilterType: `whitelist`: All file types apart from the FileExtensions list are authenticated.
`blacklist`: Only the file types in the FileExtensions list are authenticated.
        :type FilterType: str
        :param _SignParam: Signature parameter name
Only upper and lower-case letters, digits, and underscores (_) are allowed. It cannot start with a digit. Length limit: 1-100 characters.
        :type SignParam: str
        :param _TimeParam: Timestamp parameter name
Only upper and lower-case letters, digits, and underscores (_) are allowed. It cannot start with a digit. Length limit: 1-100 characters.
        :type TimeParam: str
        :param _TimeFormat: Timestamp settings
`dec`: Decimal
`hex`: Hexadecimal
        :type TimeFormat: str
        :param _BackupSecretKey: Backup key, which is used to calculate a signature.
6-32 characters. Only digits and letters are allowed. 
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type BackupSecretKey: str
        """
        self._SecretKey = None
        self._ExpireTime = None
        self._FileExtensions = None
        self._FilterType = None
        self._SignParam = None
        self._TimeParam = None
        self._TimeFormat = None
        self._BackupSecretKey = None

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def FileExtensions(self):
        return self._FileExtensions

    @FileExtensions.setter
    def FileExtensions(self, FileExtensions):
        self._FileExtensions = FileExtensions

    @property
    def FilterType(self):
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def SignParam(self):
        return self._SignParam

    @SignParam.setter
    def SignParam(self, SignParam):
        self._SignParam = SignParam

    @property
    def TimeParam(self):
        return self._TimeParam

    @TimeParam.setter
    def TimeParam(self, TimeParam):
        self._TimeParam = TimeParam

    @property
    def TimeFormat(self):
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat

    @property
    def BackupSecretKey(self):
        return self._BackupSecretKey

    @BackupSecretKey.setter
    def BackupSecretKey(self, BackupSecretKey):
        self._BackupSecretKey = BackupSecretKey


    def _deserialize(self, params):
        self._SecretKey = params.get("SecretKey")
        self._ExpireTime = params.get("ExpireTime")
        self._FileExtensions = params.get("FileExtensions")
        self._FilterType = params.get("FilterType")
        self._SignParam = params.get("SignParam")
        self._TimeParam = params.get("TimeParam")
        self._TimeFormat = params.get("TimeFormat")
        self._BackupSecretKey = params.get("BackupSecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvifAdapter(AbstractModel):
    """AVIF adapter, used for image optimization

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable `AvifAdapter` for image optimization. Values:
`on`: Enable
`off`: Disable
Note: This field may return·`null`, indicating that no valid values can be obtained.
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AwsPrivateAccess(AbstractModel):
    """Origin access authentication for S3 bucket.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable origin-pull authentication for S3 buckets.
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _AccessKey: Access ID.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AccessKey: str
        :param _SecretKey: Key.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SecretKey: str
        :param _Region: Region.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Region: str
        :param _Bucket: BucketName
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Bucket: str
        """
        self._Switch = None
        self._AccessKey = None
        self._SecretKey = None
        self._Region = None
        self._Bucket = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def AccessKey(self):
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

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


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BandwidthAlert(AbstractModel):
    """Bandwidth cap configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable usage limit. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _BpsThreshold: The upper limit of bandwidth usage (in bps) or traffic usage (in bytes).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type BpsThreshold: int
        :param _CounterMeasure: Action taken when threshold is reached
`RETURN_404`: A 404 error will be returned for all requests.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CounterMeasure: str
        :param _LastTriggerTime: The last time when the usage upper limit in the Chinese mainland was reached
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LastTriggerTime: str
        :param _AlertSwitch: Whether to enable alerts for usage limit. Values:
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AlertSwitch: str
        :param _AlertPercentage: Triggers alarms when the ratio of bandwidth or traffic usage to the usage upper limit reaches the specified value
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AlertPercentage: int
        :param _LastTriggerTimeOverseas: The last time when the usage outside the Chinese mainland reached the upper limit
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LastTriggerTimeOverseas: str
        :param _Metric: Dimension of the usage limit
`bandwidth`: Bandwidth
`flux`: Traffic
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Metric: str
        :param _StatisticItems: Usage limit configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type StatisticItems: list of StatisticItem
        """
        self._Switch = None
        self._BpsThreshold = None
        self._CounterMeasure = None
        self._LastTriggerTime = None
        self._AlertSwitch = None
        self._AlertPercentage = None
        self._LastTriggerTimeOverseas = None
        self._Metric = None
        self._StatisticItems = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def BpsThreshold(self):
        return self._BpsThreshold

    @BpsThreshold.setter
    def BpsThreshold(self, BpsThreshold):
        self._BpsThreshold = BpsThreshold

    @property
    def CounterMeasure(self):
        return self._CounterMeasure

    @CounterMeasure.setter
    def CounterMeasure(self, CounterMeasure):
        self._CounterMeasure = CounterMeasure

    @property
    def LastTriggerTime(self):
        return self._LastTriggerTime

    @LastTriggerTime.setter
    def LastTriggerTime(self, LastTriggerTime):
        self._LastTriggerTime = LastTriggerTime

    @property
    def AlertSwitch(self):
        return self._AlertSwitch

    @AlertSwitch.setter
    def AlertSwitch(self, AlertSwitch):
        self._AlertSwitch = AlertSwitch

    @property
    def AlertPercentage(self):
        return self._AlertPercentage

    @AlertPercentage.setter
    def AlertPercentage(self, AlertPercentage):
        self._AlertPercentage = AlertPercentage

    @property
    def LastTriggerTimeOverseas(self):
        return self._LastTriggerTimeOverseas

    @LastTriggerTimeOverseas.setter
    def LastTriggerTimeOverseas(self, LastTriggerTimeOverseas):
        self._LastTriggerTimeOverseas = LastTriggerTimeOverseas

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def StatisticItems(self):
        return self._StatisticItems

    @StatisticItems.setter
    def StatisticItems(self, StatisticItems):
        self._StatisticItems = StatisticItems


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._BpsThreshold = params.get("BpsThreshold")
        self._CounterMeasure = params.get("CounterMeasure")
        self._LastTriggerTime = params.get("LastTriggerTime")
        self._AlertSwitch = params.get("AlertSwitch")
        self._AlertPercentage = params.get("AlertPercentage")
        self._LastTriggerTimeOverseas = params.get("LastTriggerTimeOverseas")
        self._Metric = params.get("Metric")
        if params.get("StatisticItems") is not None:
            self._StatisticItems = []
            for item in params.get("StatisticItems"):
                obj = StatisticItem()
                obj._deserialize(item)
                self._StatisticItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotCookie(AbstractModel):
    """Bot cookie policy

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable bot cookie policies. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _RuleType: Rule type, which can only be `all` currently.
        :type RuleType: str
        :param _RuleValue: Rule value. Valid value: `*`.
        :type RuleValue: list of str
        :param _Action: Action. Valid values: `monitor`, `intercept`, `redirect`, and `captcha`.
        :type Action: str
        :param _RedirectUrl: Redirection target page
Note: This field may return null, indicating that no valid values can be obtained.
        :type RedirectUrl: str
        :param _UpdateTime: Update time
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        """
        self._Switch = None
        self._RuleType = None
        self._RuleValue = None
        self._Action = None
        self._RedirectUrl = None
        self._UpdateTime = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RuleValue(self):
        return self._RuleValue

    @RuleValue.setter
    def RuleValue(self, RuleValue):
        self._RuleValue = RuleValue

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RedirectUrl(self):
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._RuleType = params.get("RuleType")
        self._RuleValue = params.get("RuleValue")
        self._Action = params.get("Action")
        self._RedirectUrl = params.get("RedirectUrl")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotJavaScript(AbstractModel):
    """Bot JS policy

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable bot JS policies. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _RuleType: Rule type, which can only be `file` currently.
        :type RuleType: str
        :param _RuleValue: Rule value. Valid values: `html` and `htm`.
        :type RuleValue: list of str
        :param _Action: Action. Valid values: `monitor`, `intercept`, `redirect`, and `captcha`.
        :type Action: str
        :param _RedirectUrl: Redirection target page
Note: This field may return null, indicating that no valid values can be obtained.
        :type RedirectUrl: str
        :param _UpdateTime: Update time
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        """
        self._Switch = None
        self._RuleType = None
        self._RuleValue = None
        self._Action = None
        self._RedirectUrl = None
        self._UpdateTime = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RuleValue(self):
        return self._RuleValue

    @RuleValue.setter
    def RuleValue(self, RuleValue):
        self._RuleValue = RuleValue

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RedirectUrl(self):
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._RuleType = params.get("RuleType")
        self._RuleValue = params.get("RuleValue")
        self._Action = params.get("Action")
        self._RedirectUrl = params.get("RedirectUrl")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BriefDomain(AbstractModel):
    """Basic domain configuration information, including CNAME, status, service type, acceleration region, creation time, last modified time, and origin server configuration.

    """

    def __init__(self):
        r"""
        :param _ResourceId: Domain name ID
        :type ResourceId: str
        :param _AppId: Tencent Cloud account ID
        :type AppId: int
        :param _Domain: Acceleration domain name
        :type Domain: str
        :param _Cname: CNAME address of domain name
        :type Cname: str
        :param _Status: Acceleration service status
`rejected`: The domain name is rejected due to expiration/deregistration of its ICP filing
`processing`: Deploying
`closing`: Disabling
`online`: Enabled
`offline`: Disabled
        :type Status: str
        :param _ProjectId: Project ID, which can be viewed on the Tencent Cloud project management page
        :type ProjectId: int
        :param _ServiceType: Domain name service type
`web`: Static acceleration
`download`: Download acceleration
`media`: Streaming media VOD acceleration
        :type ServiceType: str
        :param _CreateTime: Domain name creation time.
        :type CreateTime: str
        :param _UpdateTime: Domain name update time.
        :type UpdateTime: str
        :param _Origin: Origin server configuration details.
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param _Disable: Domain name block status
`normal`: Normal
`overdue`: The domain name has been disabled due to account arrears. The acceleration service can be resumed after the account is topped up.
`malicious`: The acceleration service has been forcibly disabled due to detection of malicious behavior.
`ddos`: The acceleration service has been disabled due to large-scale DDoS attacks to the domain name
`idle`: No operations or data has been detected for more than 90 days. The domain name is determined to be inactive which automatically disables the acceleration service. You can restart the service.
`unlicensed`: The acceleration service has been automatically disabled as the domain name has no ICP filing or its ICP filing is deregistered. Service can be resumed after an ICP filing is obtained.
`capping`: The configured upper limit for bandwidth has been reached.
`readonly`: The domain name has a special configuration and has been locked.
        :type Disable: str
        :param _Area: Acceleration region
`mainland`: Acceleration inside the Chinese mainland
`overseas`: Acceleration outside the Chinese mainland
`global`: Acceleration over the globe
        :type Area: str
        :param _Readonly: Domain name lock status
`normal`: Not locked
`mainland`: Locked in the Chinese mainland
overseas: Locked outside the Chinese mainland
global: Locked globally
        :type Readonly: str
        :param _Product: Product of the domain name, either `cdn` or `ecdn`.
        :type Product: str
        :param _ParentHost: Primary domain name
        :type ParentHost: str
        """
        self._ResourceId = None
        self._AppId = None
        self._Domain = None
        self._Cname = None
        self._Status = None
        self._ProjectId = None
        self._ServiceType = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Origin = None
        self._Disable = None
        self._Area = None
        self._Readonly = None
        self._Product = None
        self._ParentHost = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Cname(self):
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def Disable(self):
        return self._Disable

    @Disable.setter
    def Disable(self, Disable):
        self._Disable = Disable

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Readonly(self):
        return self._Readonly

    @Readonly.setter
    def Readonly(self, Readonly):
        self._Readonly = Readonly

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def ParentHost(self):
        return self._ParentHost

    @ParentHost.setter
    def ParentHost(self, ParentHost):
        self._ParentHost = ParentHost


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._AppId = params.get("AppId")
        self._Domain = params.get("Domain")
        self._Cname = params.get("Cname")
        self._Status = params.get("Status")
        self._ProjectId = params.get("ProjectId")
        self._ServiceType = params.get("ServiceType")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        self._Disable = params.get("Disable")
        self._Area = params.get("Area")
        self._Readonly = params.get("Readonly")
        self._Product = params.get("Product")
        self._ParentHost = params.get("ParentHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Cache(AbstractModel):
    """Node cache expiration time configuration. There are two types of configuration:
    + Basic cache expiration rules configuration
    + Advanced cache expiration rules configuration

    """

    def __init__(self):
        r"""
        :param _SimpleCache: Basic cache expiration time configuration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SimpleCache: :class:`tencentcloud.cdn.v20180606.models.SimpleCache`
        :param _AdvancedCache: (Disused) Advanced cache validity configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AdvancedCache: :class:`tencentcloud.cdn.v20180606.models.AdvancedCache`
        :param _RuleCache: Advanced path cache configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleCache: list of RuleCache
        """
        self._SimpleCache = None
        self._AdvancedCache = None
        self._RuleCache = None

    @property
    def SimpleCache(self):
        return self._SimpleCache

    @SimpleCache.setter
    def SimpleCache(self, SimpleCache):
        self._SimpleCache = SimpleCache

    @property
    def AdvancedCache(self):
        return self._AdvancedCache

    @AdvancedCache.setter
    def AdvancedCache(self, AdvancedCache):
        self._AdvancedCache = AdvancedCache

    @property
    def RuleCache(self):
        return self._RuleCache

    @RuleCache.setter
    def RuleCache(self, RuleCache):
        self._RuleCache = RuleCache


    def _deserialize(self, params):
        if params.get("SimpleCache") is not None:
            self._SimpleCache = SimpleCache()
            self._SimpleCache._deserialize(params.get("SimpleCache"))
        if params.get("AdvancedCache") is not None:
            self._AdvancedCache = AdvancedCache()
            self._AdvancedCache._deserialize(params.get("AdvancedCache"))
        if params.get("RuleCache") is not None:
            self._RuleCache = []
            for item in params.get("RuleCache"):
                obj = RuleCache()
                obj._deserialize(item)
                self._RuleCache.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfig(AbstractModel):
    """Heuristic cache validity configuration

    """

    def __init__(self):
        r"""
        :param _HeuristicCacheTimeSwitch: Whether to enable heuristic cache validity. Values:
`on`: Enable
`off`: Disable
Note: This field may return·`null`, indicating that no valid values can be obtained.
        :type HeuristicCacheTimeSwitch: str
        :param _HeuristicCacheTime: Unit: Second
Note: This field may return·`null`, indicating that no valid values can be obtained.
        :type HeuristicCacheTime: int
        """
        self._HeuristicCacheTimeSwitch = None
        self._HeuristicCacheTime = None

    @property
    def HeuristicCacheTimeSwitch(self):
        return self._HeuristicCacheTimeSwitch

    @HeuristicCacheTimeSwitch.setter
    def HeuristicCacheTimeSwitch(self, HeuristicCacheTimeSwitch):
        self._HeuristicCacheTimeSwitch = HeuristicCacheTimeSwitch

    @property
    def HeuristicCacheTime(self):
        return self._HeuristicCacheTime

    @HeuristicCacheTime.setter
    def HeuristicCacheTime(self, HeuristicCacheTime):
        self._HeuristicCacheTime = HeuristicCacheTime


    def _deserialize(self, params):
        self._HeuristicCacheTimeSwitch = params.get("HeuristicCacheTimeSwitch")
        self._HeuristicCacheTime = params.get("HeuristicCacheTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigCache(AbstractModel):
    """Path cache configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable path cache. Values:
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        :param _CacheTime: Cache expiration time settings
Unit: second. The maximum value is 365 days.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CacheTime: int
        :param _CompareMaxAge: Advanced cache expiration configuration. If this is enabled, the max-age value returned by the origin server will be compared with the cache expiration time set in CacheRules, and the smallest value will be cached on the node.
`on`: Enable
`off`: Disable
This is disabled by default.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CompareMaxAge: str
        :param _IgnoreCacheControl: Force cache
`on`: Enable
`off`: Disable
This is disabled by default. If enabled, the `no-store` and `no-cache` resources returned from the origin server will be cached according to `CacheRules` rules.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IgnoreCacheControl: str
        :param _IgnoreSetCookie: Whether to ignore the header and body on cache nodes if the origin server returns the header `Set-Cookie`.
`on`: Ignore; do not cache the header and body.
`off`: Do not ignore; follow the custom cache rules of cache nodes.
It is disabled by default.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IgnoreSetCookie: str
        """
        self._Switch = None
        self._CacheTime = None
        self._CompareMaxAge = None
        self._IgnoreCacheControl = None
        self._IgnoreSetCookie = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def CacheTime(self):
        return self._CacheTime

    @CacheTime.setter
    def CacheTime(self, CacheTime):
        self._CacheTime = CacheTime

    @property
    def CompareMaxAge(self):
        return self._CompareMaxAge

    @CompareMaxAge.setter
    def CompareMaxAge(self, CompareMaxAge):
        self._CompareMaxAge = CompareMaxAge

    @property
    def IgnoreCacheControl(self):
        return self._IgnoreCacheControl

    @IgnoreCacheControl.setter
    def IgnoreCacheControl(self, IgnoreCacheControl):
        self._IgnoreCacheControl = IgnoreCacheControl

    @property
    def IgnoreSetCookie(self):
        return self._IgnoreSetCookie

    @IgnoreSetCookie.setter
    def IgnoreSetCookie(self, IgnoreSetCookie):
        self._IgnoreSetCookie = IgnoreSetCookie


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._CacheTime = params.get("CacheTime")
        self._CompareMaxAge = params.get("CompareMaxAge")
        self._IgnoreCacheControl = params.get("IgnoreCacheControl")
        self._IgnoreSetCookie = params.get("IgnoreSetCookie")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigFollowOrigin(AbstractModel):
    """Path cache configuration follows the origin server configuration.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to follow the origin configuration for path cache. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _HeuristicCache: Heuristic cache configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type HeuristicCache: :class:`tencentcloud.cdn.v20180606.models.HeuristicCache`
        """
        self._Switch = None
        self._HeuristicCache = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def HeuristicCache(self):
        return self._HeuristicCache

    @HeuristicCache.setter
    def HeuristicCache(self, HeuristicCache):
        self._HeuristicCache = HeuristicCache


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("HeuristicCache") is not None:
            self._HeuristicCache = HeuristicCache()
            self._HeuristicCache._deserialize(params.get("HeuristicCache"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigNoCache(AbstractModel):
    """Path cache/no cache configuration.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable no-caching at the path. Values:
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        :param _Revalidate: Always forwards to the origin server for verification
`on`: Enable
`off`: Disable
It is disabled by default.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Revalidate: str
        """
        self._Switch = None
        self._Revalidate = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Revalidate(self):
        return self._Revalidate

    @Revalidate.setter
    def Revalidate(self, Revalidate):
        self._Revalidate = Revalidate


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Revalidate = params.get("Revalidate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheKey(AbstractModel):
    """Cache key configuration (Ignore Query String configuration)

    """

    def __init__(self):
        r"""
        :param _FullUrlCache: Whether to enable full-path cache
`on`: Enable full-path cache (i.e., disable Ignore Query String)
`off`: Disable full-path cache (i.e., enable Ignore Query String)
        :type FullUrlCache: str
        :param _IgnoreCase: Specifies whether the cache key is case sensitive
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IgnoreCase: str
        :param _QueryString: Request parameter contained in `CacheKey`
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type QueryString: :class:`tencentcloud.cdn.v20180606.models.QueryStringKey`
        :param _Cookie: Cookie contained in `CacheKey`
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cookie: :class:`tencentcloud.cdn.v20180606.models.CookieKey`
        :param _Header: Request header contained in `CacheKey`
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Header: :class:`tencentcloud.cdn.v20180606.models.HeaderKey`
        :param _CacheTag: Custom string contained in `CacheKey`
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CacheTag: :class:`tencentcloud.cdn.v20180606.models.CacheTagKey`
        :param _Scheme: Request protocol contained in `CacheKey`
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Scheme: :class:`tencentcloud.cdn.v20180606.models.SchemeKey`
        :param _KeyRules: Path-specific cache key configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type KeyRules: list of KeyRule
        """
        self._FullUrlCache = None
        self._IgnoreCase = None
        self._QueryString = None
        self._Cookie = None
        self._Header = None
        self._CacheTag = None
        self._Scheme = None
        self._KeyRules = None

    @property
    def FullUrlCache(self):
        return self._FullUrlCache

    @FullUrlCache.setter
    def FullUrlCache(self, FullUrlCache):
        self._FullUrlCache = FullUrlCache

    @property
    def IgnoreCase(self):
        return self._IgnoreCase

    @IgnoreCase.setter
    def IgnoreCase(self, IgnoreCase):
        self._IgnoreCase = IgnoreCase

    @property
    def QueryString(self):
        return self._QueryString

    @QueryString.setter
    def QueryString(self, QueryString):
        self._QueryString = QueryString

    @property
    def Cookie(self):
        return self._Cookie

    @Cookie.setter
    def Cookie(self, Cookie):
        self._Cookie = Cookie

    @property
    def Header(self):
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def CacheTag(self):
        return self._CacheTag

    @CacheTag.setter
    def CacheTag(self, CacheTag):
        self._CacheTag = CacheTag

    @property
    def Scheme(self):
        return self._Scheme

    @Scheme.setter
    def Scheme(self, Scheme):
        self._Scheme = Scheme

    @property
    def KeyRules(self):
        return self._KeyRules

    @KeyRules.setter
    def KeyRules(self, KeyRules):
        self._KeyRules = KeyRules


    def _deserialize(self, params):
        self._FullUrlCache = params.get("FullUrlCache")
        self._IgnoreCase = params.get("IgnoreCase")
        if params.get("QueryString") is not None:
            self._QueryString = QueryStringKey()
            self._QueryString._deserialize(params.get("QueryString"))
        if params.get("Cookie") is not None:
            self._Cookie = CookieKey()
            self._Cookie._deserialize(params.get("Cookie"))
        if params.get("Header") is not None:
            self._Header = HeaderKey()
            self._Header._deserialize(params.get("Header"))
        if params.get("CacheTag") is not None:
            self._CacheTag = CacheTagKey()
            self._CacheTag._deserialize(params.get("CacheTag"))
        if params.get("Scheme") is not None:
            self._Scheme = SchemeKey()
            self._Scheme._deserialize(params.get("Scheme"))
        if params.get("KeyRules") is not None:
            self._KeyRules = []
            for item in params.get("KeyRules"):
                obj = KeyRule()
                obj._deserialize(item)
                self._KeyRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheOptResult(AbstractModel):
    """Result of blocking/unblocking URLs

    """

    def __init__(self):
        r"""
        :param _SuccessUrls: List of succeeded URLs
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SuccessUrls: list of str
        :param _FailUrls: List of failed URLs
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FailUrls: list of str
        """
        self._SuccessUrls = None
        self._FailUrls = None

    @property
    def SuccessUrls(self):
        return self._SuccessUrls

    @SuccessUrls.setter
    def SuccessUrls(self, SuccessUrls):
        self._SuccessUrls = SuccessUrls

    @property
    def FailUrls(self):
        return self._FailUrls

    @FailUrls.setter
    def FailUrls(self, FailUrls):
        self._FailUrls = FailUrls


    def _deserialize(self, params):
        self._SuccessUrls = params.get("SuccessUrls")
        self._FailUrls = params.get("FailUrls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheTagKey(AbstractModel):
    """A part of `CacheKey`

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to include `CacheTag` as part of `CacheKey`. Values:
`on`: Yes
`off`: No
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        :param _Value: Value of custom `CacheTag`
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Value: str
        """
        self._Switch = None
        self._Value = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CappingRule(AbstractModel):
    """Downstream speed limit configuration rules. Up to 100 entries can be configured.

    """

    def __init__(self):
        r"""
        :param _RuleType: Rule types:
`all`: Apply to all files.
`file`: Apply to files with the specified suffixes.
`directory`: Apply to specified paths.
`path`: Apply to specified absolute paths.
        :type RuleType: str
        :param _RulePaths: Content for each `RuleType`: 
For `all`, enter a wildcard `*`.
For `file`, enter a suffix, e.g., `jpg` or `txt`.
For `directory`, enter a path, e.g., `/xxx/test/`.
For `path`, enter an absolute path, e.g., `/xxx/test.html`.
        :type RulePaths: list of str
        :param _KBpsThreshold: Downstream speed value settings (in KB/s)
        :type KBpsThreshold: int
        """
        self._RuleType = None
        self._RulePaths = None
        self._KBpsThreshold = None

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RulePaths(self):
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths

    @property
    def KBpsThreshold(self):
        return self._KBpsThreshold

    @KBpsThreshold.setter
    def KBpsThreshold(self, KBpsThreshold):
        self._KBpsThreshold = KBpsThreshold


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._RulePaths = params.get("RulePaths")
        self._KBpsThreshold = params.get("KBpsThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdnData(AbstractModel):
    """Detailed access data

    """

    def __init__(self):
        r"""
        :param _Metric: Queries by the specified metric:
`flux`: Traffic (in bytes)
`bandwidth`: Bandwidth (in bps)
`request`: Number of requests
`fluxHitRate`: Traffic hit rate (in %)
`statusCode`: Status code. The aggregate data for 2xx, 3xx, 4xx, and 5xx status codes will be returned (in entries)
`2XX`: Returns the aggregate list of 2xx status codes and the data for status codes starting with 2 (in entries)
`3XX`: Returns the aggregate list of 3xx status codes and the data for status codes starting with 3 (in entries)
`4XX`: Returns the aggregate list of 4xx status codes and the data for status codes starting with 4 (in entries)
`5XX`: Returns the aggregate list of 5xx status codes and the data for status codes starting with 5 (in entries)
You can also specify a status code for querying.
        :type Metric: str
        :param _DetailData: Detailed data combination
        :type DetailData: list of TimestampData
        :param _SummarizedData: Aggregate data combination
        :type SummarizedData: :class:`tencentcloud.cdn.v20180606.models.SummarizedData`
        """
        self._Metric = None
        self._DetailData = None
        self._SummarizedData = None

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def DetailData(self):
        return self._DetailData

    @DetailData.setter
    def DetailData(self, DetailData):
        self._DetailData = DetailData

    @property
    def SummarizedData(self):
        return self._SummarizedData

    @SummarizedData.setter
    def SummarizedData(self, SummarizedData):
        self._SummarizedData = SummarizedData


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        if params.get("DetailData") is not None:
            self._DetailData = []
            for item in params.get("DetailData"):
                obj = TimestampData()
                obj._deserialize(item)
                self._DetailData.append(obj)
        if params.get("SummarizedData") is not None:
            self._SummarizedData = SummarizedData()
            self._SummarizedData._deserialize(params.get("SummarizedData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdnIp(AbstractModel):
    """IP attribute information

    """

    def __init__(self):
        r"""
        :param _Ip: IP to be queried
        :type Ip: str
        :param _Platform: IP ownership:
yes: Tencent Cloud CDN node
no: non-Tencent Cloud CDN node
        :type Platform: str
        :param _Location: Node district/country
unknown: unknown node location
        :type Location: str
        :param _History: Activation and deactivation history of the node.
        :type History: list of CdnIpHistory
        :param _Area: Node region
`mainland`: Acceleration nodes inside the Chinese mainland
`overseas`: Acceleration nodes outside the Chinese mainland
`unknown`: Service region unknown
        :type Area: str
        :param _City: City where the nodes reside
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type City: str
        """
        self._Ip = None
        self._Platform = None
        self._Location = None
        self._History = None
        self._Area = None
        self._City = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Platform(self):
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Location(self):
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def History(self):
        return self._History

    @History.setter
    def History(self, History):
        self._History = History

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Platform = params.get("Platform")
        self._Location = params.get("Location")
        if params.get("History") is not None:
            self._History = []
            for item in params.get("History"):
                obj = CdnIpHistory()
                obj._deserialize(item)
                self._History.append(obj)
        self._Area = params.get("Area")
        self._City = params.get("City")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdnIpHistory(AbstractModel):
    """CDN node activation and deactivation history

    """

    def __init__(self):
        r"""
        :param _Status: Operation type
`online`: Nodes activated
`offline`: Nodes deactivated
        :type Status: str
        :param _Datetime: Operation time corresponding to operation type
If its value is `null`, it means there is no status change record.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Datetime: str
        """
        self._Status = None
        self._Datetime = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Datetime(self):
        return self._Datetime

    @Datetime.setter
    def Datetime(self, Datetime):
        self._Datetime = Datetime


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Datetime = params.get("Datetime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClientCert(AbstractModel):
    """HTTPS client certificate configuration

    """

    def __init__(self):
        r"""
        :param _Certificate: Client certificate
PEM format, requires Base64 encoding.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Certificate: str
        :param _CertName: Client certificate name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CertName: str
        :param _ExpireTime: Certificate expiration time
When this is used as an input parameter, it can be left blank.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ExpireTime: str
        :param _DeployTime: Certificate issuance time
When this is used as an input parameter, it can be left blank.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DeployTime: str
        """
        self._Certificate = None
        self._CertName = None
        self._ExpireTime = None
        self._DeployTime = None

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def DeployTime(self):
        return self._DeployTime

    @DeployTime.setter
    def DeployTime(self, DeployTime):
        self._DeployTime = DeployTime


    def _deserialize(self, params):
        self._Certificate = params.get("Certificate")
        self._CertName = params.get("CertName")
        self._ExpireTime = params.get("ExpireTime")
        self._DeployTime = params.get("DeployTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClsLogObject(AbstractModel):
    """CLS log search object

    """

    def __init__(self):
        r"""
        :param _TopicId: Topic ID
        :type TopicId: str
        :param _TopicName: Topic name
        :type TopicName: str
        :param _Timestamp: Log time
        :type Timestamp: str
        :param _Content: Log content
        :type Content: str
        :param _Filename: Capture path
        :type Filename: str
        :param _Source: Log source device
        :type Source: str
        """
        self._TopicId = None
        self._TopicName = None
        self._Timestamp = None
        self._Content = None
        self._Filename = None
        self._Source = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Filename(self):
        return self._Filename

    @Filename.setter
    def Filename(self, Filename):
        self._Filename = Filename

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._Timestamp = params.get("Timestamp")
        self._Content = params.get("Content")
        self._Filename = params.get("Filename")
        self._Source = params.get("Source")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClsSearchLogs(AbstractModel):
    """CLS log search result

    """

    def __init__(self):
        r"""
        :param _Context: Cursor for more search results
        :type Context: str
        :param _Listover: Whether all search results have been returned
        :type Listover: bool
        :param _Results: Log content information
        :type Results: list of ClsLogObject
        """
        self._Context = None
        self._Listover = None
        self._Results = None

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Listover(self):
        return self._Listover

    @Listover.setter
    def Listover(self, Listover):
        self._Listover = Listover

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results


    def _deserialize(self, params):
        self._Context = params.get("Context")
        self._Listover = params.get("Listover")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = ClsLogObject()
                obj._deserialize(item)
                self._Results.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Compatibility(AbstractModel):
    """Old configuration compatibility check

    """

    def __init__(self):
        r"""
        :param _Code: Compatibility flag status code.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Code: int
        """
        self._Code = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code


    def _deserialize(self, params):
        self._Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Compression(AbstractModel):
    """Smart compression configuration. By default, Gzip compression is performed for files with js, html, css, xml, json, shtml, and htm suffixes, and with sizes between 256 and 2097152 bytes.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable smart compression. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _CompressionRules: Compression rules array
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CompressionRules: list of CompressionRule
        """
        self._Switch = None
        self._CompressionRules = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def CompressionRules(self):
        return self._CompressionRules

    @CompressionRules.setter
    def CompressionRules(self, CompressionRules):
        self._CompressionRules = CompressionRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("CompressionRules") is not None:
            self._CompressionRules = []
            for item in params.get("CompressionRules"):
                obj = CompressionRule()
                obj._deserialize(item)
                self._CompressionRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompressionRule(AbstractModel):
    """Intelligent compression rule configuration

    """

    def __init__(self):
        r"""
        :param _Compress: true: must be set as true, enables compression
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Compress: bool
        :param _MinLength: The minimum file size to trigger compression (in bytes)
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MinLength: int
        :param _MaxLength: The maximum file size to trigger compression (in bytes).
The maximum value is 30 MB.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MaxLength: int
        :param _Algorithms: File compression algorithm
`gzip`: Gzip compression
`brotli`: Brotli compression
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Algorithms: list of str
        :param _FileExtensions: Compress based on file suffix.
File suffixes such as jpg and txt are supported.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FileExtensions: list of str
        :param _RuleType: Rule types:
`all`: Apply to all files.
`file`: Apply to files with the specified suffixes.
`directory`: Apply to specified paths.
`path`: Apply to specified absolute paths.
`contentType`: Apply when the `ContentType` is specified.
If this field is specified, `FileExtensions` does not take effect.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleType: str
        :param _RulePaths: Content for each `CacheType`:
For `all`, enter a wildcard `*`.
For `file`, enter a suffix, e.g., `jpg` or `txt`.
For `directory`, enter a path, e.g., `/xxx/test/`.
For `path`, enter an absolute path, e.g., `/xxx/test.html`.
For `contentType`, enter `text/html`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RulePaths: list of str
        """
        self._Compress = None
        self._MinLength = None
        self._MaxLength = None
        self._Algorithms = None
        self._FileExtensions = None
        self._RuleType = None
        self._RulePaths = None

    @property
    def Compress(self):
        return self._Compress

    @Compress.setter
    def Compress(self, Compress):
        self._Compress = Compress

    @property
    def MinLength(self):
        return self._MinLength

    @MinLength.setter
    def MinLength(self, MinLength):
        self._MinLength = MinLength

    @property
    def MaxLength(self):
        return self._MaxLength

    @MaxLength.setter
    def MaxLength(self, MaxLength):
        self._MaxLength = MaxLength

    @property
    def Algorithms(self):
        return self._Algorithms

    @Algorithms.setter
    def Algorithms(self, Algorithms):
        self._Algorithms = Algorithms

    @property
    def FileExtensions(self):
        return self._FileExtensions

    @FileExtensions.setter
    def FileExtensions(self, FileExtensions):
        self._FileExtensions = FileExtensions

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RulePaths(self):
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths


    def _deserialize(self, params):
        self._Compress = params.get("Compress")
        self._MinLength = params.get("MinLength")
        self._MaxLength = params.get("MaxLength")
        self._Algorithms = params.get("Algorithms")
        self._FileExtensions = params.get("FileExtensions")
        self._RuleType = params.get("RuleType")
        self._RulePaths = params.get("RulePaths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CookieKey(AbstractModel):
    """A part of `CacheKey`

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to include Cookie as part of CacheKey. Values:
`on`: Yes
`off`: No
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        :param _Value: Used cookies (separated by ';')
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Value: str
        """
        self._Switch = None
        self._Value = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClsLogTopicRequest(AbstractModel):
    """CreateClsLogTopic request structure.

    """

    def __init__(self):
        r"""
        :param _TopicName: Log topic name
        :type TopicName: str
        :param _LogsetId: Logset ID
        :type LogsetId: str
        :param _Channel: Specifies whether to access CDN or ECDN. Valid values: `cdn` (default) and `ecdn`.
        :type Channel: str
        :param _DomainAreaConfigs: Domain name region information
        :type DomainAreaConfigs: list of DomainAreaConfig
        """
        self._TopicName = None
        self._LogsetId = None
        self._Channel = None
        self._DomainAreaConfigs = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def DomainAreaConfigs(self):
        return self._DomainAreaConfigs

    @DomainAreaConfigs.setter
    def DomainAreaConfigs(self, DomainAreaConfigs):
        self._DomainAreaConfigs = DomainAreaConfigs


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._LogsetId = params.get("LogsetId")
        self._Channel = params.get("Channel")
        if params.get("DomainAreaConfigs") is not None:
            self._DomainAreaConfigs = []
            for item in params.get("DomainAreaConfigs"):
                obj = DomainAreaConfig()
                obj._deserialize(item)
                self._DomainAreaConfigs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClsLogTopicResponse(AbstractModel):
    """CreateClsLogTopic response structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Topic ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TopicId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TopicId = None
        self._RequestId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._RequestId = params.get("RequestId")


class CreateScdnFailedLogTaskRequest(AbstractModel):
    """CreateScdnFailedLogTask request structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: ID of the failed task to retry
        :type TaskId: str
        :param _Area: Region. Valid values: `mainland` and `overseas`.
        :type Area: str
        """
        self._TaskId = None
        self._Area = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScdnFailedLogTaskResponse(AbstractModel):
    """CreateScdnFailedLogTask response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Creation result. 
0: Creation succeeded
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteCdnDomainRequest(AbstractModel):
    """DeleteCdnDomain request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain name
The domain name status should be `Disabled`
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCdnDomainResponse(AbstractModel):
    """DeleteCdnDomain response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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


class DeleteClsLogTopicRequest(AbstractModel):
    """DeleteClsLogTopic request structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _LogsetId: Logset ID
        :type LogsetId: str
        :param _Channel: Specifies whether to access CDN or ECDN. Valid values: `cdn` (default) and `ecdn`.
        :type Channel: str
        """
        self._TopicId = None
        self._LogsetId = None
        self._Channel = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._LogsetId = params.get("LogsetId")
        self._Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClsLogTopicResponse(AbstractModel):
    """DeleteClsLogTopic response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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


class DescribeBillingDataRequest(AbstractModel):
    """DescribeBillingData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time of the query, e.g., 2018-09-04 10:40:00.
The specified start time will be rounded down based on the granularity parameter `Interval`. For example, if you set the start time to 2018-09-04 10:40:00 with 1-hour granularity, the time will be rounded down to 2018-09-04 10:00:00.
The period between the start time and end time can be up to 90 days.
        :type StartTime: str
        :param _EndTime: End time of the query, e.g. 2018-09-04 10:40:00.
The specified end time will be rounded down based on the granularity parameter `Interval`. For example, if you set the end time to 2018-09-04 10:40:00 with 1-hour granularity, the time will be rounded down to 2018-09-04 10:00:00.
The period between the start time and end time can be up to 90 days.
        :type EndTime: str
        :param _Interval: Time granularity, which can be:
`min`: 1-minute granularity. The query period cannot exceed 24 hours.
`5min`: 5-minute granularity. The query range cannot exceed 31 days.
`hour`: 1-hour granularity. The query period cannot exceed 31 days.
`day`: 1-day granularity. The query period cannot exceed 31 days.

`min` is not supported if the `Area` field is `overseas`.
        :type Interval: str
        :param _Domain: Domain name whose billing data is to be queried
        :type Domain: str
        :param _Project: Specifies the project ID to be queried. [Check project ID in the console](https://console.cloud.tencent.com/project)
If the `Domain` parameter is passed in, the `Proejct` parameter is ignored. Only the billing data of the specified domain name is returned. 
        :type Project: int
        :param _Area: Acceleration region whose billing data is to be queried:
`mainland`: Regions within the Chinese mainland
`overseas`: Regions outside the Chinese mainland
If this parameter is left empty, `mainland` will be used by default
        :type Area: str
        :param _District: Country/region to be queried if `Area` is `overseas`
To view codes of provinces or countries/regions, see [Province Code Mappings](https://intl.cloud.tencent.com/document/product/228/6316?from_cn_redirect=1#.E7.9C.81.E4.BB.BD.E6.98.A0.E5.B0.84)
If this parameter is left empty, all countries/regions will be queried
        :type District: int
        :param _Metric: Billing statistics type
`flux`: Bill by traffic
`bandwidth`: Bill by bandwidth
Default value: `bandwidth`
        :type Metric: str
        :param _Product: Specifies the product to query, either `cdn` (default) or `ecdn`.
        :type Product: str
        :param _TimeZone: 
        :type TimeZone: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Interval = None
        self._Domain = None
        self._Project = None
        self._Area = None
        self._District = None
        self._Metric = None
        self._Product = None
        self._TimeZone = None

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
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Project(self):
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def District(self):
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def TimeZone(self):
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Interval = params.get("Interval")
        self._Domain = params.get("Domain")
        self._Project = params.get("Project")
        self._Area = params.get("Area")
        self._District = params.get("District")
        self._Metric = params.get("Metric")
        self._Product = params.get("Product")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillingDataResponse(AbstractModel):
    """DescribeBillingData response structure.

    """

    def __init__(self):
        r"""
        :param _Interval: Time granularity, which is specified by the parameter passed in during the query:
`min`: 1 minute
`5min`: 5 minutes
`hour`: 1 hour
`day`: 1 day
        :type Interval: str
        :param _Data: Data details
        :type Data: list of ResourceBillingData
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Interval = None
        self._Data = None
        self._RequestId = None

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Interval = params.get("Interval")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ResourceBillingData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCdnDataRequest(AbstractModel):
    """DescribeCdnData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time of the query, e.g., 2018-09-04 10:40:00.
The specified start time will be rounded down based on the granularity parameter `Interval`. For example, if you set the start time to 2018-09-04 10:40:00 with 1-hour granularity, the time will be rounded down to 2018-09-04 10:00:00.
The period between the start time and end time can be up to 90 days.
        :type StartTime: str
        :param _EndTime: End time of the query, e.g. 2018-09-04 10:40:00.
The specified end time will be rounded down based on the granularity parameter `Interval`. For example, if you set the end time to 2018-09-04 10:40:00 with 1-hour granularity, the time will be rounded down to 2018-09-04 10:00:00.
The period between the start time and end time can be up to 90 days.
        :type EndTime: str
        :param _Metric: Specifies the metric to query, which can be:
`flux`: Traffic (in bytes)
`fluxIn`: Upstream traffic (in bytes), only used for the `ecdn` product
`fluxOut`: Downstream traffic (in bytes), only used for the `ecdn` product
`bandwidth`: Bandwidth (in bps)
`bandwidthIn`: Upstream bandwidth (in bps), only used for the `ecdn` product
`bandwidthOut`: Downstream bandwidth (in bps), only used for the `ecdn` product
`request`: Number of requests
`hitRequest`: Number of hit requests
`requestHitRate`: Request hit rate (in % with two decimal digits)
`hitFlux`: Hit traffic (in bytes)
`fluxHitRate`: Traffic hit rate (in % with two decimal digits)
`statusCode`: Status code. The aggregate data for 2xx, 3xx, 4xx, and 5xx status codes will be returned (in entries)
`2xx`: Returns the aggregate list of 2xx status codes and the data for status codes starting with 2 (in entries)
`3xx`: Returns the aggregate list of 3xx status codes and the data for status codes starting with 3 (in entries)
`4xx`: Returns the aggregate list of 4xx status codes and the data for status codes starting with 4 (in entries)
`5xx`: Returns the aggregate list of 5xx status codes and the data for status codes starting with 5 (in entries)
Specifies the status code to query. The return will be empty if the status code has never been generated.
        :type Metric: str
        :param _Domains: Specifies the list of domain names to be queried
You can specify one or more domain names.
Up to 30 domain names can be queried in one request.
If this parameter is not specified, it means to query all domain names under the current account.
        :type Domains: list of str
        :param _Project: Specifies the project ID to be queried. [Check project ID in the console](https://console.cloud.tencent.com/project)
Note that `Project` will be ignored if `Domains` is specified.
        :type Project: int
        :param _Interval: Sampling interval. The available options vary for different query period. See below: 
`min`: Return data with 1-minute granularity. It’s available when the query period is  within 24 hours and `Area` is `mainland`.
`5min`: Return data with 5-minute granularity. It’s available when the query period is within 31 days.
`hour`: Return data with 1-hour granularity. It’s available when the query period is within 31 days.
`day`: Return data with 1-day granularity. It’s available when the query period is longer than 31 days.
        :type Interval: str
        :param _Detail: The aggregate data for multiple domain names is returned by default (false) during a multi-domain-name query.
You can set it to true to return the details for each Domain (the statusCode metric is currently not supported).
        :type Detail: bool
        :param _Isp: Specifies an ISP when you query the CDN data within the Chinese mainland. If this is left blank, all ISPs will be queried.
To view ISP codes, see [ISP Code Mappings](https://intl.cloud.tencent.com/document/product/228/6316?from_cn_redirect=1#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)
Note that only one of `District`, `Isp` and `IpProtocol` can be specified.
        :type Isp: int
        :param _District: Specifies a province when you query the CDN data within the Chinese mainland. If this is left blank, all provinces will be queried.
Specifies a country/region when you query the CDN data outside the Chinese mainland. If this is left blank, all countries/regions will be queried.
To view codes of provinces or countries/regions, see [Province Code Mappings](https://intl.cloud.tencent.com/document/product/228/6316?from_cn_redirect=1#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8).
When `Area` is `mainland`, you can query by the province. Note that only one of `District`, `Isp` and `IpProtocol` can be specified.
        :type District: int
        :param _Protocol: Specifies the protocol to be queried; if you leave it blank, all protocols will be queried.
`all`: All protocols
`http`: Query HTTP data
`https`: Query HTTPS data
        :type Protocol: str
        :param _DataSource: Specifies the data source to be queried. It’s only open to beta users now. 
        :type DataSource: str
        :param _IpProtocol: Specifies the IP protocol to be queried. If it’s not specified, data of all IP protocols are returned.
`all`: All protocols
`ipv4`: Query IPv4 data
`ipv6`: Query IPv6 data
If `IpProtocol` is specified, `District` parameter can not be specified at the same time.
Note: `ipv4` and `ipv6` are only available to beta users. 
        :type IpProtocol: str
        :param _Area: Specifies the service area. If it’s not specified, CDN data of the Chinese mainland are returned.
`mainland`: Query CDN data in the Chinese mainland.
`overseas`: Query CDN data outside the Chinese mainland.
        :type Area: str
        :param _AreaType: Specify whether to query by the region of the server or client. This parameter is valid only when `Area` is `overseas`.
`server`: Query by the location of server (Tencent Cloud CDN nodes)
`client`: Query by the location of the client (where the request devices are located)
        :type AreaType: str
        :param _Product: Specifies the product to query, either `cdn` (default) or `ecdn`.
        :type Product: str
        :param _TimeZone: Specifies a time zone to query. The default time zone is UTC+08:00.
        :type TimeZone: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Metric = None
        self._Domains = None
        self._Project = None
        self._Interval = None
        self._Detail = None
        self._Isp = None
        self._District = None
        self._Protocol = None
        self._DataSource = None
        self._IpProtocol = None
        self._Area = None
        self._AreaType = None
        self._Product = None
        self._TimeZone = None

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
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Project(self):
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def District(self):
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def DataSource(self):
        return self._DataSource

    @DataSource.setter
    def DataSource(self, DataSource):
        self._DataSource = DataSource

    @property
    def IpProtocol(self):
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def AreaType(self):
        return self._AreaType

    @AreaType.setter
    def AreaType(self, AreaType):
        self._AreaType = AreaType

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def TimeZone(self):
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Metric = params.get("Metric")
        self._Domains = params.get("Domains")
        self._Project = params.get("Project")
        self._Interval = params.get("Interval")
        self._Detail = params.get("Detail")
        self._Isp = params.get("Isp")
        self._District = params.get("District")
        self._Protocol = params.get("Protocol")
        self._DataSource = params.get("DataSource")
        self._IpProtocol = params.get("IpProtocol")
        self._Area = params.get("Area")
        self._AreaType = params.get("AreaType")
        self._Product = params.get("Product")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCdnDataResponse(AbstractModel):
    """DescribeCdnData response structure.

    """

    def __init__(self):
        r"""
        :param _Interval: Time granularity of the returned data. 
`min`: 1 minute
`5min`: 5 minutes
`hour`: 1 hour
`day`: 1 day
        :type Interval: str
        :param _Data: Returned data details of the specified conditional query
        :type Data: list of ResourceData
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Interval = None
        self._Data = None
        self._RequestId = None

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Interval = params.get("Interval")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ResourceData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCdnDomainLogsRequest(AbstractModel):
    """DescribeCdnDomainLogs request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Specifies a domain name for the query
        :type Domain: str
        :param _StartTime: Starting time, such as `2019-09-04 00:00:00`
        :type StartTime: str
        :param _EndTime: End time, such as `2019-09-04 12:00:00`
        :type EndTime: str
        :param _Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param _Limit: Limit on paginated queries. Default value: 100. Maximum value: 1,000
        :type Limit: int
        :param _Area: Specifies a region for the query.
`mainland`: specifies to return the download link of logs on acceleration within Mainland China;
`overseas`: specifies to return the download link of logs on acceleration outside Mainland China;
`global`: specifies to return a download link of logs on acceleration within Mainland China and a link of logs on acceleration outside Mainland China.
Default value: `mainland`.
        :type Area: str
        :param _LogType: Specifies the type of logs to download (only access logs supported).
`access`: Access logs.
        :type LogType: str
        """
        self._Domain = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._Area = None
        self._LogType = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

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
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def LogType(self):
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Area = params.get("Area")
        self._LogType = params.get("LogType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCdnDomainLogsResponse(AbstractModel):
    """DescribeCdnDomainLogs response structure.

    """

    def __init__(self):
        r"""
        :param _DomainLogs: Download link of the log package.
You can open the link to download a .gz log package that contains all log files without extension.
        :type DomainLogs: list of DomainLog
        :param _TotalCount: Total number of entries obtained
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DomainLogs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DomainLogs(self):
        return self._DomainLogs

    @DomainLogs.setter
    def DomainLogs(self, DomainLogs):
        self._DomainLogs = DomainLogs

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DomainLogs") is not None:
            self._DomainLogs = []
            for item in params.get("DomainLogs"):
                obj = DomainLog()
                obj._deserialize(item)
                self._DomainLogs.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCdnIpRequest(AbstractModel):
    """DescribeCdnIp request structure.

    """

    def __init__(self):
        r"""
        :param _Ips: List of IPs to be queried
        :type Ips: list of str
        """
        self._Ips = None

    @property
    def Ips(self):
        return self._Ips

    @Ips.setter
    def Ips(self, Ips):
        self._Ips = Ips


    def _deserialize(self, params):
        self._Ips = params.get("Ips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCdnIpResponse(AbstractModel):
    """DescribeCdnIp response structure.

    """

    def __init__(self):
        r"""
        :param _Ips: Node ownership details
        :type Ips: list of CdnIp
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ips = None
        self._RequestId = None

    @property
    def Ips(self):
        return self._Ips

    @Ips.setter
    def Ips(self, Ips):
        self._Ips = Ips

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Ips") is not None:
            self._Ips = []
            for item in params.get("Ips"):
                obj = CdnIp()
                obj._deserialize(item)
                self._Ips.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCdnOriginIpRequest(AbstractModel):
    """DescribeCdnOriginIp request structure.

    """


class DescribeCdnOriginIpResponse(AbstractModel):
    """DescribeCdnOriginIp response structure.

    """

    def __init__(self):
        r"""
        :param _Ips: Intermediate node IP details
        :type Ips: list of OriginIp
        :param _TotalCount: Number of intermediate node IPs
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ips = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Ips(self):
        return self._Ips

    @Ips.setter
    def Ips(self, Ips):
        self._Ips = Ips

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Ips") is not None:
            self._Ips = []
            for item in params.get("Ips"):
                obj = OriginIp()
                obj._deserialize(item)
                self._Ips.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCertDomainsRequest(AbstractModel):
    """DescribeCertDomains request structure.

    """

    def __init__(self):
        r"""
        :param _Cert: Base64-encoded string of certificate in PEM format
        :type Cert: str
        :param _CertId: Managed certificate ID. `Cert` and `CertId` cannot be both empty. If they’re both filled in, `CerID` prevails.
        :type CertId: str
        :param _Product: Product of the domain name, either `cdn` (default) or `ecdn`.
        :type Product: str
        """
        self._Cert = None
        self._CertId = None
        self._Product = None

    @property
    def Cert(self):
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Cert = params.get("Cert")
        self._CertId = params.get("CertId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertDomainsResponse(AbstractModel):
    """DescribeCertDomains response structure.

    """

    def __init__(self):
        r"""
        :param _Domains: List of domain names connected to CDN
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Domains: list of str
        :param _CertifiedDomains: List of CDN domain names with certificates configured
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CertifiedDomains: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Domains = None
        self._CertifiedDomains = None
        self._RequestId = None

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def CertifiedDomains(self):
        return self._CertifiedDomains

    @CertifiedDomains.setter
    def CertifiedDomains(self, CertifiedDomains):
        self._CertifiedDomains = CertifiedDomains

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Domains = params.get("Domains")
        self._CertifiedDomains = params.get("CertifiedDomains")
        self._RequestId = params.get("RequestId")


class DescribeDomainsConfigRequest(AbstractModel):
    """DescribeDomainsConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param _Limit: Limit on paginated queries. Default value: 100. Maximum value: 1000.
        :type Limit: int
        :param _Filters: Query condition filter, complex type.
        :type Filters: list of DomainFilter
        :param _Sort: Sorting rules
        :type Sort: :class:`tencentcloud.cdn.v20180606.models.Sort`
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._Sort = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = DomainFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("Sort") is not None:
            self._Sort = Sort()
            self._Sort._deserialize(params.get("Sort"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainsConfigResponse(AbstractModel):
    """DescribeDomainsConfig response structure.

    """

    def __init__(self):
        r"""
        :param _Domains: List of domain names
        :type Domains: list of DetailDomain
        :param _TotalNumber: Number of domain names that match the specified query conditions
Used for paginated queries
        :type TotalNumber: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Domains = None
        self._TotalNumber = None
        self._RequestId = None

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def TotalNumber(self):
        return self._TotalNumber

    @TotalNumber.setter
    def TotalNumber(self, TotalNumber):
        self._TotalNumber = TotalNumber

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self._Domains = []
            for item in params.get("Domains"):
                obj = DetailDomain()
                obj._deserialize(item)
                self._Domains.append(obj)
        self._TotalNumber = params.get("TotalNumber")
        self._RequestId = params.get("RequestId")


class DescribeDomainsRequest(AbstractModel):
    """DescribeDomains request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param _Limit: Limit on paginated queries. Default value: 100. Maximum value: 1000.
        :type Limit: int
        :param _Filters: Query condition filter, which supports complex type.
        :type Filters: list of DomainFilter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = DomainFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainsResponse(AbstractModel):
    """DescribeDomains response structure.

    """

    def __init__(self):
        r"""
        :param _Domains: List of domain names
        :type Domains: list of BriefDomain
        :param _TotalNumber: The number of domain names that matched the query conditions
Used for paginated queries
        :type TotalNumber: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Domains = None
        self._TotalNumber = None
        self._RequestId = None

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def TotalNumber(self):
        return self._TotalNumber

    @TotalNumber.setter
    def TotalNumber(self, TotalNumber):
        self._TotalNumber = TotalNumber

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self._Domains = []
            for item in params.get("Domains"):
                obj = BriefDomain()
                obj._deserialize(item)
                self._Domains.append(obj)
        self._TotalNumber = params.get("TotalNumber")
        self._RequestId = params.get("RequestId")


class DescribeIpStatusRequest(AbstractModel):
    """DescribeIpStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Acceleration domain name
        :type Domain: str
        :param _Layer: Node type.
`edge`: Edge server
`last`: Intermediate server
If this parameter is left empty, edge server information will be returned by default
        :type Layer: str
        :param _Area: Specifies a region to query.
`mainland`: Nodes in the Chinese mainland
`overseas`: Nodes outside the Chinese mainland
`global`: Global nodes
        :type Area: str
        :param _Segment: Whether to return a value as an IP range
        :type Segment: bool
        :param _ShowIpv6: 
        :type ShowIpv6: bool
        :param _AbbreviationIpv6: Whether to abbreviate the IPv6 address.
        :type AbbreviationIpv6: bool
        """
        self._Domain = None
        self._Layer = None
        self._Area = None
        self._Segment = None
        self._ShowIpv6 = None
        self._AbbreviationIpv6 = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Layer(self):
        return self._Layer

    @Layer.setter
    def Layer(self, Layer):
        self._Layer = Layer

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Segment(self):
        return self._Segment

    @Segment.setter
    def Segment(self, Segment):
        self._Segment = Segment

    @property
    def ShowIpv6(self):
        return self._ShowIpv6

    @ShowIpv6.setter
    def ShowIpv6(self, ShowIpv6):
        self._ShowIpv6 = ShowIpv6

    @property
    def AbbreviationIpv6(self):
        return self._AbbreviationIpv6

    @AbbreviationIpv6.setter
    def AbbreviationIpv6(self, AbbreviationIpv6):
        self._AbbreviationIpv6 = AbbreviationIpv6


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Layer = params.get("Layer")
        self._Area = params.get("Area")
        self._Segment = params.get("Segment")
        self._ShowIpv6 = params.get("ShowIpv6")
        self._AbbreviationIpv6 = params.get("AbbreviationIpv6")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpStatusResponse(AbstractModel):
    """DescribeIpStatus response structure.

    """

    def __init__(self):
        r"""
        :param _Ips: Node list
        :type Ips: list of IpStatus
        :param _TotalCount: Total number of nodes
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Ips = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Ips(self):
        return self._Ips

    @Ips.setter
    def Ips(self, Ips):
        self._Ips = Ips

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Ips") is not None:
            self._Ips = []
            for item in params.get("Ips"):
                obj = IpStatus()
                obj._deserialize(item)
                self._Ips.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeIpVisitRequest(AbstractModel):
    """DescribeIpVisit request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Query start time, such as 2018-09-04 10:40:10; the returned result is later than or equal to the specified time.
According to the specified time granularity, forward rounding is applied; for example, if the query start time is 2018-09-04 10:40:10 and the query time granularity is 5 minutes, the time for the first returned entry will be 2018-09-04 10:40:00.
        :type StartTime: str
        :param _EndTime: Query end time, such as 2018-09-04 10:40:10; the returned result is earlier than or equal to the specified time.
According to the specified time granularity, forward rounding is applied; for example, if the query start time is 2018-09-04 10:40:10 and the query time granularity is 5 minutes, the time for the last returned entry will be 2018-09-04 10:40:00.
        :type EndTime: str
        :param _Domains: Specifies the list of domain names to be queried; up to 30 domain names can be queried at a time.
        :type Domains: list of str
        :param _Project: Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)
Please note that if domain names are specified, this parameter will be ignored.
        :type Project: int
        :param _Interval: Sampling interval in minutes. The available options vary for different query period. See below: 
5min: 5 minutes. If the query period is within 24 hours, `5min` will be used by default.
day: 1 day. If the query period is longer than 24 hours, `day` will be used by default.
        :type Interval: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Domains = None
        self._Project = None
        self._Interval = None

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
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Project(self):
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Domains = params.get("Domains")
        self._Project = params.get("Project")
        self._Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpVisitResponse(AbstractModel):
    """DescribeIpVisit response structure.

    """

    def __init__(self):
        r"""
        :param _Interval: Time granularity of data statistics, which supports 5min (5 minutes) and day (1 day).
        :type Interval: str
        :param _Data: Origin-pull data details of each resource.
        :type Data: list of ResourceData
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Interval = None
        self._Data = None
        self._RequestId = None

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Interval = params.get("Interval")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ResourceData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMapInfoRequest(AbstractModel):
    """DescribeMapInfo request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Query type:
`isp`: queries ISP codes
`district`: queries codes of provinces (Mainland China) or countries/regions (outside Mainland China)
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
        


class DescribeMapInfoResponse(AbstractModel):
    """DescribeMapInfo response structure.

    """

    def __init__(self):
        r"""
        :param _MapInfoList: Array of mappings.
        :type MapInfoList: list of MapInfo
        :param _ServerRegionRelation: Mapping relationship between server region ID and sub-region ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ServerRegionRelation: list of RegionMapRelation
        :param _ClientRegionRelation: Mapping relationship between client region ID and sub-region ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ClientRegionRelation: list of RegionMapRelation
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MapInfoList = None
        self._ServerRegionRelation = None
        self._ClientRegionRelation = None
        self._RequestId = None

    @property
    def MapInfoList(self):
        return self._MapInfoList

    @MapInfoList.setter
    def MapInfoList(self, MapInfoList):
        self._MapInfoList = MapInfoList

    @property
    def ServerRegionRelation(self):
        return self._ServerRegionRelation

    @ServerRegionRelation.setter
    def ServerRegionRelation(self, ServerRegionRelation):
        self._ServerRegionRelation = ServerRegionRelation

    @property
    def ClientRegionRelation(self):
        return self._ClientRegionRelation

    @ClientRegionRelation.setter
    def ClientRegionRelation(self, ClientRegionRelation):
        self._ClientRegionRelation = ClientRegionRelation

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MapInfoList") is not None:
            self._MapInfoList = []
            for item in params.get("MapInfoList"):
                obj = MapInfo()
                obj._deserialize(item)
                self._MapInfoList.append(obj)
        if params.get("ServerRegionRelation") is not None:
            self._ServerRegionRelation = []
            for item in params.get("ServerRegionRelation"):
                obj = RegionMapRelation()
                obj._deserialize(item)
                self._ServerRegionRelation.append(obj)
        if params.get("ClientRegionRelation") is not None:
            self._ClientRegionRelation = []
            for item in params.get("ClientRegionRelation"):
                obj = RegionMapRelation()
                obj._deserialize(item)
                self._ClientRegionRelation.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOriginDataRequest(AbstractModel):
    """DescribeOriginData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Start time of the query, e.g., 2018-09-04 10:40:00.
The specified start time will be rounded down based on the granularity parameter `Interval`. For example, if you set the start time to 2018-09-04 10:40:00 with 1-hour granularity, the time will be rounded down to 2018-09-04 10:00:00.
The period between the start time and end time can be up to 90 days.
        :type StartTime: str
        :param _EndTime: End time of the query, e.g. 2018-09-04 10:40:00.
The specified end time will be rounded down based on the granularity parameter `Interval`. For example, if you set the end time to 2018-09-04 10:40:00 with 1-hour granularity, the time will be rounded down to 2018-09-04 10:00:00.
The period between the start time and end time can be up to 90 days.
        :type EndTime: str
        :param _Metric: Specifies the metric to query, which can be:
`flux`: Origin-pull traffic (in bytes)
`bandwidth`: Origin-pull bandwidth (in bps)
`request`: Number of origin-pull requests
`failRequest`: Number of failed origin-pull requests
`failRate`: Origin-pull failure rate (in %)
`statusCode`: Origin-pull status code. The aggregate data for 2xx, 3xx, 4xx, and 5xx origin-pull status codes will be returned (in entries)
`2xx`: Returns the aggregate list of 2xx origin-pull status codes and the data for origin-pull status codes starting with 2 (in entries)
`3xx`: Returns the aggregate list of 3xx origin-pull status codes and the data for origin-pull status codes starting with 3 (in entries)
`4xx`: Returns the aggregate list of 4xx origin-pull status codes and the data for origin-pull status codes starting with 4 (in entries)
`5xx`: Returns the aggregate list of 5xx origin-pull status codes and the data for origin-pull status codes starting with 5 (in entries)
It is supported to specify a status code for query. The return will be empty if the status code has never been generated.
        :type Metric: str
        :param _Domains: Specifies the list of domain names to query. You can query up to 30 domain names at a time.
        :type Domains: list of str
        :param _Project: Specifies the project ID to be queried. [Check project ID in the console](https://console.cloud.tencent.com/project)
If the domain name is not specified, the specified project will be queried. Up to 30 acceleration domain names can be queried at a time.
If the domain name information is specified, this parameter can be ignored.
        :type Project: int
        :param _Interval: Time granularity, which can be:
`min`: Return data with 1-minute granularity. It’s available when the query period is  within 24 hours and `Area` is `mainland`.
`5min`: Return data with 5-minute granularity. It’s available when the query period is within 31 days.
`hour`: Return data with 1-hour granularity. It’s available when the query period is within 31 days.
`day`: Return data with 1-day granularity. It’s available when the query period is longer than 31 days.
        :type Interval: str
        :param _Detail: The aggregate data for multiple domain names is returned by default (false) when multiple `Domains` are passed in.
You can set it to true to return the details for each Domain (the statusCode metric is currently not supported)
        :type Detail: bool
        :param _Area: Specifies the service region. If this value is left blank, it means to query CDN data within the Chinese mainland.
`mainland`: Query CDN data in the Chinese mainland.
`overseas`: Query CDN data outside the Chinese mainland.
        :type Area: str
        :param _TimeZone: Specifies a time zone to query. The default time zone is UTC+08:00.
        :type TimeZone: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Metric = None
        self._Domains = None
        self._Project = None
        self._Interval = None
        self._Detail = None
        self._Area = None
        self._TimeZone = None

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
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Project(self):
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def TimeZone(self):
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Metric = params.get("Metric")
        self._Domains = params.get("Domains")
        self._Project = params.get("Project")
        self._Interval = params.get("Interval")
        self._Detail = params.get("Detail")
        self._Area = params.get("Area")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOriginDataResponse(AbstractModel):
    """DescribeOriginData response structure.

    """

    def __init__(self):
        r"""
        :param _Interval: Time granularity of data statistics, which supports `min` (1 minute), `5min` (5 minutes), `hour` (1 hour), and `day` (1 day).
        :type Interval: str
        :param _Data: Origin-pull data details of each resource.
        :type Data: list of ResourceOriginData
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Interval = None
        self._Data = None
        self._RequestId = None

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Interval = params.get("Interval")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ResourceOriginData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePayTypeRequest(AbstractModel):
    """DescribePayType request structure.

    """

    def __init__(self):
        r"""
        :param _Area: Specifies the service area.
`mainland`: Queries billing methods available in the Chinese mainland.
`overseas`: Queries billing methods available in the regions outside the Chinese mainland.
`Global`: Queries billing methods available across the globe.
If it is not specified, it defaults to `mainland`.
        :type Area: str
        :param _Product: Specifies the product to query, either `cdn` (default) or `ecdn`.
        :type Product: str
        :param _Type: Specifies resources.
`flux`: Traffic package
`https`: HTTPS requests
It defaults to `flux` if not specified. 
        :type Type: str
        """
        self._Area = None
        self._Product = None
        self._Type = None

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Area = params.get("Area")
        self._Product = params.get("Product")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePayTypeResponse(AbstractModel):
    """DescribePayType response structure.

    """

    def __init__(self):
        r"""
        :param _PayType: Billing type
`flux`: Bill by traffic
`bandwidth`: Bill by bandwidth
`request`: Bill by the number of requests
`flux_sep`: Bill by dynamic and static traffic separately 
`bandwidth_sep`: Bill by dynamic and static bandwidth separately
If you incur any usage when switching the billing mode, the new mode will take effect the next day. If no usage is incurred, the new mode takes effect immediately.
        :type PayType: str
        :param _BillingCycle: Billing cycle
`day`: Daily
`month`: Monthly
`hour`: Hourly
        :type BillingCycle: str
        :param _StatType: Statistic data
`monthMax`: Billed monthly based on the monthly average daily peak traffic
`day95`: Billed monthly based on the daily 95th percentile bandwidth
`month95`: Billed monthly based on the monthly 95th percentile bandwidth
`sum`: Billed daily/monthly based on the total traffic or requests
`max`: Billed daily based on the peak bandwidth
        :type StatType: str
        :param _RegionType: Regionl billing
`all`: Unified billing for all regions
`multiple`: Region-specific billing
        :type RegionType: str
        :param _CurrentPayType: Current billing mode
`flux`: Bill by traffic
`bandwidth`: Bill by bandwidth
`request`: Bill by the number of requests
`flux_sep`: Bill by dynamic and static traffic separately 
`bandwidth_sep`: Bill by dynamic and static bandwidth separately
        :type CurrentPayType: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PayType = None
        self._BillingCycle = None
        self._StatType = None
        self._RegionType = None
        self._CurrentPayType = None
        self._RequestId = None

    @property
    def PayType(self):
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def BillingCycle(self):
        return self._BillingCycle

    @BillingCycle.setter
    def BillingCycle(self, BillingCycle):
        self._BillingCycle = BillingCycle

    @property
    def StatType(self):
        return self._StatType

    @StatType.setter
    def StatType(self, StatType):
        self._StatType = StatType

    @property
    def RegionType(self):
        return self._RegionType

    @RegionType.setter
    def RegionType(self, RegionType):
        self._RegionType = RegionType

    @property
    def CurrentPayType(self):
        return self._CurrentPayType

    @CurrentPayType.setter
    def CurrentPayType(self, CurrentPayType):
        self._CurrentPayType = CurrentPayType

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PayType = params.get("PayType")
        self._BillingCycle = params.get("BillingCycle")
        self._StatType = params.get("StatType")
        self._RegionType = params.get("RegionType")
        self._CurrentPayType = params.get("CurrentPayType")
        self._RequestId = params.get("RequestId")


class DescribePurgeQuotaRequest(AbstractModel):
    """DescribePurgeQuota request structure.

    """


class DescribePurgeQuotaResponse(AbstractModel):
    """DescribePurgeQuota response structure.

    """

    def __init__(self):
        r"""
        :param _UrlPurge: URL purge usage and quota.
        :type UrlPurge: list of Quota
        :param _PathPurge: Directory purge usage and quota.
        :type PathPurge: list of Quota
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UrlPurge = None
        self._PathPurge = None
        self._RequestId = None

    @property
    def UrlPurge(self):
        return self._UrlPurge

    @UrlPurge.setter
    def UrlPurge(self, UrlPurge):
        self._UrlPurge = UrlPurge

    @property
    def PathPurge(self):
        return self._PathPurge

    @PathPurge.setter
    def PathPurge(self, PathPurge):
        self._PathPurge = PathPurge

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UrlPurge") is not None:
            self._UrlPurge = []
            for item in params.get("UrlPurge"):
                obj = Quota()
                obj._deserialize(item)
                self._UrlPurge.append(obj)
        if params.get("PathPurge") is not None:
            self._PathPurge = []
            for item in params.get("PathPurge"):
                obj = Quota()
                obj._deserialize(item)
                self._PathPurge.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePurgeTasksRequest(AbstractModel):
    """DescribePurgeTasks request structure.

    """

    def __init__(self):
        r"""
        :param _PurgeType: Specifies a purge type:
`url`: URL purge record
`path`: Directory purge record
        :type PurgeType: str
        :param _StartTime: Specifies the starting time of the period you want to query, such as `2018-08-08 00:00:00`
        :type StartTime: str
        :param _EndTime: Specifies the end time of the period you want to query, such as 2018-08-08 23:59:59
        :type EndTime: str
        :param _TaskId: Specifies a task ID when you want to query by task ID.
You must specify either a task ID or a starting time for your query.
        :type TaskId: str
        :param _Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param _Limit: Limit on paginated queries. Default value: 20
        :type Limit: int
        :param _Keyword: You can filter the results by domain name or a complete URL beginning with `http(s)://`
        :type Keyword: str
        :param _Status: Specifies a task state for your query:
`fail`: purge failed
`done`: purge succeeded
`process`: purge in progress
        :type Status: str
        :param _Area: Specifies a purge region for your query:
`mainland`: within Mainland China
`overseas`: outside Mainland China
`global`: global
        :type Area: str
        """
        self._PurgeType = None
        self._StartTime = None
        self._EndTime = None
        self._TaskId = None
        self._Offset = None
        self._Limit = None
        self._Keyword = None
        self._Status = None
        self._Area = None

    @property
    def PurgeType(self):
        return self._PurgeType

    @PurgeType.setter
    def PurgeType(self, PurgeType):
        self._PurgeType = PurgeType

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
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._PurgeType = params.get("PurgeType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TaskId = params.get("TaskId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Keyword = params.get("Keyword")
        self._Status = params.get("Status")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePurgeTasksResponse(AbstractModel):
    """DescribePurgeTasks response structure.

    """

    def __init__(self):
        r"""
        :param _PurgeLogs: Detailed purge record.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PurgeLogs: list of PurgeTask
        :param _TotalCount: Total number of tasks, which is used for pagination.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PurgeLogs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def PurgeLogs(self):
        return self._PurgeLogs

    @PurgeLogs.setter
    def PurgeLogs(self, PurgeLogs):
        self._PurgeLogs = PurgeLogs

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PurgeLogs") is not None:
            self._PurgeLogs = []
            for item in params.get("PurgeLogs"):
                obj = PurgeTask()
                obj._deserialize(item)
                self._PurgeLogs.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePushQuotaRequest(AbstractModel):
    """DescribePushQuota request structure.

    """


class DescribePushQuotaResponse(AbstractModel):
    """DescribePushQuota response structure.

    """

    def __init__(self):
        r"""
        :param _UrlPush: URL prefetch usage and quota.
        :type UrlPush: list of Quota
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UrlPush = None
        self._RequestId = None

    @property
    def UrlPush(self):
        return self._UrlPush

    @UrlPush.setter
    def UrlPush(self, UrlPush):
        self._UrlPush = UrlPush

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UrlPush") is not None:
            self._UrlPush = []
            for item in params.get("UrlPush"):
                obj = Quota()
                obj._deserialize(item)
                self._UrlPush.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePushTasksRequest(AbstractModel):
    """DescribePushTasks request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Starting time, such as `2018-08-08 00:00:00`
        :type StartTime: str
        :param _EndTime: End time, such as `2018-08-08 23:59:59`
        :type EndTime: str
        :param _TaskId: Specifies a task ID for your query.
You must specify either a task ID or a starting time.
        :type TaskId: str
        :param _Keyword: Specifies a keyword for your query. Please enter a domain name or a complete URL beginning with `http(s)://`
        :type Keyword: str
        :param _Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param _Limit: Limit on paginated queries. Default value: 20
        :type Limit: int
        :param _Area: Specifies a region to query the prefetch records
`mainland`: Chinese mainland
`overseas`: Outside the Chinese mainland
`global`: Globe
        :type Area: str
        :param _Status: Queries the status of a specified task
`fail`: Prefetch failed
`done`: Prefetch succeeded
`process`: Prefetch in progress
`invalid`: Invalid prefetch with 4XX/5XX status code returned from the origin server
        :type Status: str
        """
        self._StartTime = None
        self._EndTime = None
        self._TaskId = None
        self._Keyword = None
        self._Offset = None
        self._Limit = None
        self._Area = None
        self._Status = None

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
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TaskId = params.get("TaskId")
        self._Keyword = params.get("Keyword")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Area = params.get("Area")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePushTasksResponse(AbstractModel):
    """DescribePushTasks response structure.

    """

    def __init__(self):
        r"""
        :param _PushLogs: Prefetch history
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PushLogs: list of PushTask
        :param _TotalCount: Total number of tasks, which is used for pagination.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PushLogs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def PushLogs(self):
        return self._PushLogs

    @PushLogs.setter
    def PushLogs(self, PushLogs):
        self._PushLogs = PushLogs

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PushLogs") is not None:
            self._PushLogs = []
            for item in params.get("PushLogs"):
                obj = PushTask()
                obj._deserialize(item)
                self._PushLogs.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeReportDataRequest(AbstractModel):
    """DescribeReportData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Query the start time in the format of `yyyy-MM-dd`
If the report type is `daily`, the start time and end time must be of the same day.
If the report type is `weekly`, the start time must be Monday and the end time must be the Sunday of the same week.
If the report type is `monthly`, the start time must be the first day of the month and the end time must be the last day of the same month.
        :type StartTime: str
        :param _EndTime: Query the end time in the format of `yyyy-MM-dd`
If the report type is `daily`, the start time and end time must be of the same day.
If the report type is `weekly`, the start time must be Monday and the end time must be the Sunday of the same week.
If the report type is `monthly`, the start time must be the first day of the month and the end time must be the last day of the same month.
        :type EndTime: str
        :param _ReportType: Report type
daily: daily report
weekly: weekly report (Monday to Sunday)
monthly: monthly report (calendar month)
        :type ReportType: str
        :param _Area: Domain name acceleration region
`mainland`: Regions within the Chinese mainland
`overseas`: Regions outside the Chinese mainland
        :type Area: str
        :param _Offset: Offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of data entries. Default value: 1000.
        :type Limit: int
        :param _Project: Filters by project ID
        :type Project: int
        """
        self._StartTime = None
        self._EndTime = None
        self._ReportType = None
        self._Area = None
        self._Offset = None
        self._Limit = None
        self._Project = None

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
    def ReportType(self):
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Project(self):
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ReportType = params.get("ReportType")
        self._Area = params.get("Area")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Project = params.get("Project")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReportDataResponse(AbstractModel):
    """DescribeReportData response structure.

    """

    def __init__(self):
        r"""
        :param _DomainReport: Domain name-level data details.
        :type DomainReport: list of ReportData
        :param _ProjectReport: Project-level data details
        :type ProjectReport: list of ReportData
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DomainReport = None
        self._ProjectReport = None
        self._RequestId = None

    @property
    def DomainReport(self):
        return self._DomainReport

    @DomainReport.setter
    def DomainReport(self, DomainReport):
        self._DomainReport = DomainReport

    @property
    def ProjectReport(self):
        return self._ProjectReport

    @ProjectReport.setter
    def ProjectReport(self, ProjectReport):
        self._ProjectReport = ProjectReport

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DomainReport") is not None:
            self._DomainReport = []
            for item in params.get("DomainReport"):
                obj = ReportData()
                obj._deserialize(item)
                self._DomainReport.append(obj)
        if params.get("ProjectReport") is not None:
            self._ProjectReport = []
            for item in params.get("ProjectReport"):
                obj = ReportData()
                obj._deserialize(item)
                self._ProjectReport.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUrlViolationsRequest(AbstractModel):
    """DescribeUrlViolations request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param _Limit: Limit on paginated queries. Default value: 100.
        :type Limit: int
        :param _Domains: Specified domain name query
        :type Domains: list of str
        """
        self._Offset = None
        self._Limit = None
        self._Domains = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUrlViolationsResponse(AbstractModel):
    """DescribeUrlViolations response structure.

    """

    def __init__(self):
        r"""
        :param _UrlRecordList: Details of URLs in violation
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UrlRecordList: list of ViolationUrl
        :param _TotalCount: Total number of records, which is used for pagination.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UrlRecordList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def UrlRecordList(self):
        return self._UrlRecordList

    @UrlRecordList.setter
    def UrlRecordList(self, UrlRecordList):
        self._UrlRecordList = UrlRecordList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UrlRecordList") is not None:
            self._UrlRecordList = []
            for item in params.get("UrlRecordList"):
                obj = ViolationUrl()
                obj._deserialize(item)
                self._UrlRecordList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DetailDomain(AbstractModel):
    """Complete acceleration domain configuration information

    """

    def __init__(self):
        r"""
        :param _ResourceId: Domain name ID
        :type ResourceId: str
        :param _AppId: Tencent Cloud account ID
        :type AppId: int
        :param _Domain: Accelerated domain name.
        :type Domain: str
        :param _Cname: CNAME address of domain name
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Cname: str
        :param _Status: Acceleration service status
`rejected`: The domain name is rejected due to expiration/deregistration of its ICP filing
`processing`: Deploying
`closing`: Disabling
`online`: Enabled
`offline`: Disabled
        :type Status: str
        :param _ProjectId: Project ID, which can be viewed on the Tencent Cloud project management page
        :type ProjectId: int
        :param _ServiceType: Acceleration domain name service type
`web`: Webpage file downloads
`download`: Large file downloads
`media`: Audio and video on demand acceleration
`hybrid`: Dynamic and static content acceleration
`dynamic`: Dynamic content acceleration
        :type ServiceType: str
        :param _CreateTime: Domain name creation time
        :type CreateTime: str
        :param _UpdateTime: Domain name update time
        :type UpdateTime: str
        :param _Origin: Origin server configuration.
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param _IpFilter: IP blocklist/allowlist configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param _IpFreqLimit: IP access limit configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param _StatusCodeCache: Status code cache configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param _Compression: Smart compression configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param _BandwidthAlert: Bandwidth cap configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param _RangeOriginPull: Range GETs configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param _FollowRedirect: 301/302 origin-pull follow-redirect configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param _ErrorPage: Custom error page configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param _RequestHeader: Custom request header configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param _ResponseHeader: Custom response header configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param _DownstreamCapping: Single-link downstream speed limit configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param _CacheKey: Configuration of cache with/without parameter
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param _ResponseHeaderCache: Origin server header cache configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param _VideoSeek: Video dragging configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        :param _Cache: Node cache expiration rule configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param _OriginPullOptimization: Cross-border linkage optimization configuration (in beta)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param _Https: HTTPS Acceleration Configuration Guide
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param _Authentication: Timestamp hotlink protection configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param _Seo: SEO configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param _Disable: Domain name block status
`normal`: Normal
`overdue`: The domain name has been disabled due to account arrears. The acceleration service can be resumed after the account is topped up.
`malicious`: The acceleration service has been forcibly disabled due to detection of malicious behavior.
`ddos`: The acceleration service has been disabled due to large-scale DDoS attacks to the domain name
`idle`: No operations or data has been detected for more than 90 days. The domain name is determined to be inactive which automatically disables the acceleration service. You can restart the service.
`unlicensed`: The acceleration service has been automatically disabled as the domain name has no ICP filing or its ICP filing is deregistered. Service can be resumed after an ICP filing is obtained.
`capping`: The configured upper limit for bandwidth has been reached.
`readonly`: The domain name has a special configuration and has been locked.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Disable: str
        :param _ForceRedirect: Access protocol forced redirect configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param _Referer: Referer configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param _MaxAge: Browser cache expiration rule configuration (in beta)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param _Ipv6: IPv6 origin-pull configuration (in beta)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Ipv6: :class:`tencentcloud.cdn.v20180606.models.Ipv6`
        :param _Compatibility: Backwards compatibility configuration (compatibility field for internal use)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Compatibility: :class:`tencentcloud.cdn.v20180606.models.Compatibility`
        :param _SpecificConfig: Region-specific configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SpecificConfig: :class:`tencentcloud.cdn.v20180606.models.SpecificConfig`
        :param _Area: Acceleration region
`mainland`: Acceleration inside the Chinese mainland
`overseas`: Acceleration outside the Chinese mainland
`global`: Acceleration over the globe
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Area: str
        :param _Readonly: Domain name lock status
`normal`: Not locked
`mainland`: Locked in the Chinese mainland
`overseas`: Locked outside the Chinese mainland
global: Locked globally
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Readonly: str
        :param _OriginPullTimeout: Origin-pull timeout configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginPullTimeout: :class:`tencentcloud.cdn.v20180606.models.OriginPullTimeout`
        :param _AwsPrivateAccess: S3 bucket origin access authentication configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AwsPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`
        :param _SecurityConfig: SCDN configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SecurityConfig: :class:`tencentcloud.cdn.v20180606.models.SecurityConfig`
        :param _ImageOptimization: Image optimization configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ImageOptimization: :class:`tencentcloud.cdn.v20180606.models.ImageOptimization`
        :param _UserAgentFilter: UA blocklist/allowlist configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UserAgentFilter: :class:`tencentcloud.cdn.v20180606.models.UserAgentFilter`
        :param _AccessControl: Access control
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AccessControl: :class:`tencentcloud.cdn.v20180606.models.AccessControl`
        :param _Advance: Whether to support advanced configuration items
`on`: Supported
`off`: Not supported
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Advance: str
        :param _UrlRedirect: URL redirect configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UrlRedirect: :class:`tencentcloud.cdn.v20180606.models.UrlRedirect`
        :param _AccessPort: Access port configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AccessPort: list of int
        :param _Tag: Tag configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Tag: list of Tag
        :param _AdvancedAuthentication: Timestamp hotlink protection advanced configuration (allowlist feature)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AdvancedAuthentication: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthentication`
        :param _OriginAuthentication: Origin-pull authentication advanced configuration (allowlist feature)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginAuthentication: :class:`tencentcloud.cdn.v20180606.models.OriginAuthentication`
        :param _Ipv6Access: IPv6 access configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Ipv6Access: :class:`tencentcloud.cdn.v20180606.models.Ipv6Access`
        :param _AdvanceSet: Advanced configuration settings
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AdvanceSet: list of AdvanceConfig
        :param _OfflineCache: Offline cache (only available to beta users)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OfflineCache: :class:`tencentcloud.cdn.v20180606.models.OfflineCache`
        :param _OriginCombine: Merging origin-pull requests (only available to beta users)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginCombine: :class:`tencentcloud.cdn.v20180606.models.OriginCombine`
        :param _PostMaxSize: POST request configuration item
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PostMaxSize: :class:`tencentcloud.cdn.v20180606.models.PostSize`
        :param _Quic: QUIC configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Quic: :class:`tencentcloud.cdn.v20180606.models.Quic`
        :param _OssPrivateAccess: Access authentication for OSS origin
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OssPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.OssPrivateAccess`
        :param _WebSocket: WebSocket configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type WebSocket: :class:`tencentcloud.cdn.v20180606.models.WebSocket`
        :param _RemoteAuthentication: Remote authentication configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RemoteAuthentication: :class:`tencentcloud.cdn.v20180606.models.RemoteAuthentication`
        :param _ShareCname: Shared CNAME configuration (only available to beta users)
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ShareCname: :class:`tencentcloud.cdn.v20180606.models.ShareCname`
        :param _RuleEngine: Rule engine
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleEngine: :class:`tencentcloud.cdn.v20180606.models.RuleEngine`
        :param _ParentHost: Primary domain name
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ParentHost: str
        :param _HwPrivateAccess: Access authentication for Huawei Cloud OBS origin
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type HwPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.HwPrivateAccess`
        :param _QnPrivateAccess: Access authentication for QiNiu Cloud Kodo origin
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type QnPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.QnPrivateAccess`
        :param _HttpsBilling: HTTPS (enabled by default)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type HttpsBilling: :class:`tencentcloud.cdn.v20180606.models.HttpsBilling`
        :param _OthersPrivateAccess: Origin-pull authentication for other origins
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type OthersPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.OthersPrivateAccess`
        """
        self._ResourceId = None
        self._AppId = None
        self._Domain = None
        self._Cname = None
        self._Status = None
        self._ProjectId = None
        self._ServiceType = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Origin = None
        self._IpFilter = None
        self._IpFreqLimit = None
        self._StatusCodeCache = None
        self._Compression = None
        self._BandwidthAlert = None
        self._RangeOriginPull = None
        self._FollowRedirect = None
        self._ErrorPage = None
        self._RequestHeader = None
        self._ResponseHeader = None
        self._DownstreamCapping = None
        self._CacheKey = None
        self._ResponseHeaderCache = None
        self._VideoSeek = None
        self._Cache = None
        self._OriginPullOptimization = None
        self._Https = None
        self._Authentication = None
        self._Seo = None
        self._Disable = None
        self._ForceRedirect = None
        self._Referer = None
        self._MaxAge = None
        self._Ipv6 = None
        self._Compatibility = None
        self._SpecificConfig = None
        self._Area = None
        self._Readonly = None
        self._OriginPullTimeout = None
        self._AwsPrivateAccess = None
        self._SecurityConfig = None
        self._ImageOptimization = None
        self._UserAgentFilter = None
        self._AccessControl = None
        self._Advance = None
        self._UrlRedirect = None
        self._AccessPort = None
        self._Tag = None
        self._AdvancedAuthentication = None
        self._OriginAuthentication = None
        self._Ipv6Access = None
        self._AdvanceSet = None
        self._OfflineCache = None
        self._OriginCombine = None
        self._PostMaxSize = None
        self._Quic = None
        self._OssPrivateAccess = None
        self._WebSocket = None
        self._RemoteAuthentication = None
        self._ShareCname = None
        self._RuleEngine = None
        self._ParentHost = None
        self._HwPrivateAccess = None
        self._QnPrivateAccess = None
        self._HttpsBilling = None
        self._OthersPrivateAccess = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Cname(self):
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def IpFilter(self):
        return self._IpFilter

    @IpFilter.setter
    def IpFilter(self, IpFilter):
        self._IpFilter = IpFilter

    @property
    def IpFreqLimit(self):
        return self._IpFreqLimit

    @IpFreqLimit.setter
    def IpFreqLimit(self, IpFreqLimit):
        self._IpFreqLimit = IpFreqLimit

    @property
    def StatusCodeCache(self):
        return self._StatusCodeCache

    @StatusCodeCache.setter
    def StatusCodeCache(self, StatusCodeCache):
        self._StatusCodeCache = StatusCodeCache

    @property
    def Compression(self):
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def BandwidthAlert(self):
        return self._BandwidthAlert

    @BandwidthAlert.setter
    def BandwidthAlert(self, BandwidthAlert):
        self._BandwidthAlert = BandwidthAlert

    @property
    def RangeOriginPull(self):
        return self._RangeOriginPull

    @RangeOriginPull.setter
    def RangeOriginPull(self, RangeOriginPull):
        self._RangeOriginPull = RangeOriginPull

    @property
    def FollowRedirect(self):
        return self._FollowRedirect

    @FollowRedirect.setter
    def FollowRedirect(self, FollowRedirect):
        self._FollowRedirect = FollowRedirect

    @property
    def ErrorPage(self):
        return self._ErrorPage

    @ErrorPage.setter
    def ErrorPage(self, ErrorPage):
        self._ErrorPage = ErrorPage

    @property
    def RequestHeader(self):
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader

    @property
    def ResponseHeader(self):
        return self._ResponseHeader

    @ResponseHeader.setter
    def ResponseHeader(self, ResponseHeader):
        self._ResponseHeader = ResponseHeader

    @property
    def DownstreamCapping(self):
        return self._DownstreamCapping

    @DownstreamCapping.setter
    def DownstreamCapping(self, DownstreamCapping):
        self._DownstreamCapping = DownstreamCapping

    @property
    def CacheKey(self):
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def ResponseHeaderCache(self):
        return self._ResponseHeaderCache

    @ResponseHeaderCache.setter
    def ResponseHeaderCache(self, ResponseHeaderCache):
        self._ResponseHeaderCache = ResponseHeaderCache

    @property
    def VideoSeek(self):
        return self._VideoSeek

    @VideoSeek.setter
    def VideoSeek(self, VideoSeek):
        self._VideoSeek = VideoSeek

    @property
    def Cache(self):
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def OriginPullOptimization(self):
        return self._OriginPullOptimization

    @OriginPullOptimization.setter
    def OriginPullOptimization(self, OriginPullOptimization):
        self._OriginPullOptimization = OriginPullOptimization

    @property
    def Https(self):
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def Authentication(self):
        return self._Authentication

    @Authentication.setter
    def Authentication(self, Authentication):
        self._Authentication = Authentication

    @property
    def Seo(self):
        return self._Seo

    @Seo.setter
    def Seo(self, Seo):
        self._Seo = Seo

    @property
    def Disable(self):
        return self._Disable

    @Disable.setter
    def Disable(self, Disable):
        self._Disable = Disable

    @property
    def ForceRedirect(self):
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def Referer(self):
        return self._Referer

    @Referer.setter
    def Referer(self, Referer):
        self._Referer = Referer

    @property
    def MaxAge(self):
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def Ipv6(self):
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def Compatibility(self):
        return self._Compatibility

    @Compatibility.setter
    def Compatibility(self, Compatibility):
        self._Compatibility = Compatibility

    @property
    def SpecificConfig(self):
        return self._SpecificConfig

    @SpecificConfig.setter
    def SpecificConfig(self, SpecificConfig):
        self._SpecificConfig = SpecificConfig

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Readonly(self):
        return self._Readonly

    @Readonly.setter
    def Readonly(self, Readonly):
        self._Readonly = Readonly

    @property
    def OriginPullTimeout(self):
        return self._OriginPullTimeout

    @OriginPullTimeout.setter
    def OriginPullTimeout(self, OriginPullTimeout):
        self._OriginPullTimeout = OriginPullTimeout

    @property
    def AwsPrivateAccess(self):
        return self._AwsPrivateAccess

    @AwsPrivateAccess.setter
    def AwsPrivateAccess(self, AwsPrivateAccess):
        self._AwsPrivateAccess = AwsPrivateAccess

    @property
    def SecurityConfig(self):
        return self._SecurityConfig

    @SecurityConfig.setter
    def SecurityConfig(self, SecurityConfig):
        self._SecurityConfig = SecurityConfig

    @property
    def ImageOptimization(self):
        return self._ImageOptimization

    @ImageOptimization.setter
    def ImageOptimization(self, ImageOptimization):
        self._ImageOptimization = ImageOptimization

    @property
    def UserAgentFilter(self):
        return self._UserAgentFilter

    @UserAgentFilter.setter
    def UserAgentFilter(self, UserAgentFilter):
        self._UserAgentFilter = UserAgentFilter

    @property
    def AccessControl(self):
        return self._AccessControl

    @AccessControl.setter
    def AccessControl(self, AccessControl):
        self._AccessControl = AccessControl

    @property
    def Advance(self):
        return self._Advance

    @Advance.setter
    def Advance(self, Advance):
        self._Advance = Advance

    @property
    def UrlRedirect(self):
        return self._UrlRedirect

    @UrlRedirect.setter
    def UrlRedirect(self, UrlRedirect):
        self._UrlRedirect = UrlRedirect

    @property
    def AccessPort(self):
        return self._AccessPort

    @AccessPort.setter
    def AccessPort(self, AccessPort):
        self._AccessPort = AccessPort

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def AdvancedAuthentication(self):
        return self._AdvancedAuthentication

    @AdvancedAuthentication.setter
    def AdvancedAuthentication(self, AdvancedAuthentication):
        self._AdvancedAuthentication = AdvancedAuthentication

    @property
    def OriginAuthentication(self):
        return self._OriginAuthentication

    @OriginAuthentication.setter
    def OriginAuthentication(self, OriginAuthentication):
        self._OriginAuthentication = OriginAuthentication

    @property
    def Ipv6Access(self):
        return self._Ipv6Access

    @Ipv6Access.setter
    def Ipv6Access(self, Ipv6Access):
        self._Ipv6Access = Ipv6Access

    @property
    def AdvanceSet(self):
        return self._AdvanceSet

    @AdvanceSet.setter
    def AdvanceSet(self, AdvanceSet):
        self._AdvanceSet = AdvanceSet

    @property
    def OfflineCache(self):
        return self._OfflineCache

    @OfflineCache.setter
    def OfflineCache(self, OfflineCache):
        self._OfflineCache = OfflineCache

    @property
    def OriginCombine(self):
        return self._OriginCombine

    @OriginCombine.setter
    def OriginCombine(self, OriginCombine):
        self._OriginCombine = OriginCombine

    @property
    def PostMaxSize(self):
        return self._PostMaxSize

    @PostMaxSize.setter
    def PostMaxSize(self, PostMaxSize):
        self._PostMaxSize = PostMaxSize

    @property
    def Quic(self):
        return self._Quic

    @Quic.setter
    def Quic(self, Quic):
        self._Quic = Quic

    @property
    def OssPrivateAccess(self):
        return self._OssPrivateAccess

    @OssPrivateAccess.setter
    def OssPrivateAccess(self, OssPrivateAccess):
        self._OssPrivateAccess = OssPrivateAccess

    @property
    def WebSocket(self):
        return self._WebSocket

    @WebSocket.setter
    def WebSocket(self, WebSocket):
        self._WebSocket = WebSocket

    @property
    def RemoteAuthentication(self):
        return self._RemoteAuthentication

    @RemoteAuthentication.setter
    def RemoteAuthentication(self, RemoteAuthentication):
        self._RemoteAuthentication = RemoteAuthentication

    @property
    def ShareCname(self):
        return self._ShareCname

    @ShareCname.setter
    def ShareCname(self, ShareCname):
        self._ShareCname = ShareCname

    @property
    def RuleEngine(self):
        return self._RuleEngine

    @RuleEngine.setter
    def RuleEngine(self, RuleEngine):
        self._RuleEngine = RuleEngine

    @property
    def ParentHost(self):
        return self._ParentHost

    @ParentHost.setter
    def ParentHost(self, ParentHost):
        self._ParentHost = ParentHost

    @property
    def HwPrivateAccess(self):
        return self._HwPrivateAccess

    @HwPrivateAccess.setter
    def HwPrivateAccess(self, HwPrivateAccess):
        self._HwPrivateAccess = HwPrivateAccess

    @property
    def QnPrivateAccess(self):
        return self._QnPrivateAccess

    @QnPrivateAccess.setter
    def QnPrivateAccess(self, QnPrivateAccess):
        self._QnPrivateAccess = QnPrivateAccess

    @property
    def HttpsBilling(self):
        return self._HttpsBilling

    @HttpsBilling.setter
    def HttpsBilling(self, HttpsBilling):
        self._HttpsBilling = HttpsBilling

    @property
    def OthersPrivateAccess(self):
        return self._OthersPrivateAccess

    @OthersPrivateAccess.setter
    def OthersPrivateAccess(self, OthersPrivateAccess):
        self._OthersPrivateAccess = OthersPrivateAccess


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._AppId = params.get("AppId")
        self._Domain = params.get("Domain")
        self._Cname = params.get("Cname")
        self._Status = params.get("Status")
        self._ProjectId = params.get("ProjectId")
        self._ServiceType = params.get("ServiceType")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        if params.get("IpFilter") is not None:
            self._IpFilter = IpFilter()
            self._IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self._IpFreqLimit = IpFreqLimit()
            self._IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("StatusCodeCache") is not None:
            self._StatusCodeCache = StatusCodeCache()
            self._StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("Compression") is not None:
            self._Compression = Compression()
            self._Compression._deserialize(params.get("Compression"))
        if params.get("BandwidthAlert") is not None:
            self._BandwidthAlert = BandwidthAlert()
            self._BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("RangeOriginPull") is not None:
            self._RangeOriginPull = RangeOriginPull()
            self._RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("FollowRedirect") is not None:
            self._FollowRedirect = FollowRedirect()
            self._FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ErrorPage") is not None:
            self._ErrorPage = ErrorPage()
            self._ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("RequestHeader") is not None:
            self._RequestHeader = RequestHeader()
            self._RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self._ResponseHeader = ResponseHeader()
            self._ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("DownstreamCapping") is not None:
            self._DownstreamCapping = DownstreamCapping()
            self._DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("ResponseHeaderCache") is not None:
            self._ResponseHeaderCache = ResponseHeaderCache()
            self._ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("VideoSeek") is not None:
            self._VideoSeek = VideoSeek()
            self._VideoSeek._deserialize(params.get("VideoSeek"))
        if params.get("Cache") is not None:
            self._Cache = Cache()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("OriginPullOptimization") is not None:
            self._OriginPullOptimization = OriginPullOptimization()
            self._OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        if params.get("Authentication") is not None:
            self._Authentication = Authentication()
            self._Authentication._deserialize(params.get("Authentication"))
        if params.get("Seo") is not None:
            self._Seo = Seo()
            self._Seo._deserialize(params.get("Seo"))
        self._Disable = params.get("Disable")
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirect()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Referer") is not None:
            self._Referer = Referer()
            self._Referer._deserialize(params.get("Referer"))
        if params.get("MaxAge") is not None:
            self._MaxAge = MaxAge()
            self._MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Ipv6") is not None:
            self._Ipv6 = Ipv6()
            self._Ipv6._deserialize(params.get("Ipv6"))
        if params.get("Compatibility") is not None:
            self._Compatibility = Compatibility()
            self._Compatibility._deserialize(params.get("Compatibility"))
        if params.get("SpecificConfig") is not None:
            self._SpecificConfig = SpecificConfig()
            self._SpecificConfig._deserialize(params.get("SpecificConfig"))
        self._Area = params.get("Area")
        self._Readonly = params.get("Readonly")
        if params.get("OriginPullTimeout") is not None:
            self._OriginPullTimeout = OriginPullTimeout()
            self._OriginPullTimeout._deserialize(params.get("OriginPullTimeout"))
        if params.get("AwsPrivateAccess") is not None:
            self._AwsPrivateAccess = AwsPrivateAccess()
            self._AwsPrivateAccess._deserialize(params.get("AwsPrivateAccess"))
        if params.get("SecurityConfig") is not None:
            self._SecurityConfig = SecurityConfig()
            self._SecurityConfig._deserialize(params.get("SecurityConfig"))
        if params.get("ImageOptimization") is not None:
            self._ImageOptimization = ImageOptimization()
            self._ImageOptimization._deserialize(params.get("ImageOptimization"))
        if params.get("UserAgentFilter") is not None:
            self._UserAgentFilter = UserAgentFilter()
            self._UserAgentFilter._deserialize(params.get("UserAgentFilter"))
        if params.get("AccessControl") is not None:
            self._AccessControl = AccessControl()
            self._AccessControl._deserialize(params.get("AccessControl"))
        self._Advance = params.get("Advance")
        if params.get("UrlRedirect") is not None:
            self._UrlRedirect = UrlRedirect()
            self._UrlRedirect._deserialize(params.get("UrlRedirect"))
        self._AccessPort = params.get("AccessPort")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        if params.get("AdvancedAuthentication") is not None:
            self._AdvancedAuthentication = AdvancedAuthentication()
            self._AdvancedAuthentication._deserialize(params.get("AdvancedAuthentication"))
        if params.get("OriginAuthentication") is not None:
            self._OriginAuthentication = OriginAuthentication()
            self._OriginAuthentication._deserialize(params.get("OriginAuthentication"))
        if params.get("Ipv6Access") is not None:
            self._Ipv6Access = Ipv6Access()
            self._Ipv6Access._deserialize(params.get("Ipv6Access"))
        if params.get("AdvanceSet") is not None:
            self._AdvanceSet = []
            for item in params.get("AdvanceSet"):
                obj = AdvanceConfig()
                obj._deserialize(item)
                self._AdvanceSet.append(obj)
        if params.get("OfflineCache") is not None:
            self._OfflineCache = OfflineCache()
            self._OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("OriginCombine") is not None:
            self._OriginCombine = OriginCombine()
            self._OriginCombine._deserialize(params.get("OriginCombine"))
        if params.get("PostMaxSize") is not None:
            self._PostMaxSize = PostSize()
            self._PostMaxSize._deserialize(params.get("PostMaxSize"))
        if params.get("Quic") is not None:
            self._Quic = Quic()
            self._Quic._deserialize(params.get("Quic"))
        if params.get("OssPrivateAccess") is not None:
            self._OssPrivateAccess = OssPrivateAccess()
            self._OssPrivateAccess._deserialize(params.get("OssPrivateAccess"))
        if params.get("WebSocket") is not None:
            self._WebSocket = WebSocket()
            self._WebSocket._deserialize(params.get("WebSocket"))
        if params.get("RemoteAuthentication") is not None:
            self._RemoteAuthentication = RemoteAuthentication()
            self._RemoteAuthentication._deserialize(params.get("RemoteAuthentication"))
        if params.get("ShareCname") is not None:
            self._ShareCname = ShareCname()
            self._ShareCname._deserialize(params.get("ShareCname"))
        if params.get("RuleEngine") is not None:
            self._RuleEngine = RuleEngine()
            self._RuleEngine._deserialize(params.get("RuleEngine"))
        self._ParentHost = params.get("ParentHost")
        if params.get("HwPrivateAccess") is not None:
            self._HwPrivateAccess = HwPrivateAccess()
            self._HwPrivateAccess._deserialize(params.get("HwPrivateAccess"))
        if params.get("QnPrivateAccess") is not None:
            self._QnPrivateAccess = QnPrivateAccess()
            self._QnPrivateAccess._deserialize(params.get("QnPrivateAccess"))
        if params.get("HttpsBilling") is not None:
            self._HttpsBilling = HttpsBilling()
            self._HttpsBilling._deserialize(params.get("HttpsBilling"))
        if params.get("OthersPrivateAccess") is not None:
            self._OthersPrivateAccess = OthersPrivateAccess()
            self._OthersPrivateAccess._deserialize(params.get("OthersPrivateAccess"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableCachesRequest(AbstractModel):
    """DisableCaches request structure.

    """

    def __init__(self):
        r"""
        :param _Urls: List of URLs to be blocked (URLs must contain `http://` or `https://`).
Up to 100 entries can be submitted at a time and 3,000 entries per day.
        :type Urls: list of str
        """
        self._Urls = None

    @property
    def Urls(self):
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls


    def _deserialize(self, params):
        self._Urls = params.get("Urls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableCachesResponse(AbstractModel):
    """DisableCaches response structure.

    """

    def __init__(self):
        r"""
        :param _CacheOptResult: Submission result
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CacheOptResult: :class:`tencentcloud.cdn.v20180606.models.CacheOptResult`
        :param _TaskId: Task ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CacheOptResult = None
        self._TaskId = None
        self._RequestId = None

    @property
    def CacheOptResult(self):
        return self._CacheOptResult

    @CacheOptResult.setter
    def CacheOptResult(self, CacheOptResult):
        self._CacheOptResult = CacheOptResult

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CacheOptResult") is not None:
            self._CacheOptResult = CacheOptResult()
            self._CacheOptResult._deserialize(params.get("CacheOptResult"))
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DisableClsLogTopicRequest(AbstractModel):
    """DisableClsLogTopic request structure.

    """

    def __init__(self):
        r"""
        :param _LogsetId: Logset ID
        :type LogsetId: str
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _Channel: Specifies whether to access CDN or ECDN. Valid values: `cdn` (default) and `ecdn`.
        :type Channel: str
        """
        self._LogsetId = None
        self._TopicId = None
        self._Channel = None

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        self._Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableClsLogTopicResponse(AbstractModel):
    """DisableClsLogTopic response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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


class DomainAreaConfig(AbstractModel):
    """Region configuration for domain names

    """

    def __init__(self):
        r"""
        :param _Domain: Domain name
        :type Domain: str
        :param _Area: Region list, where the element can be `mainland`/`overseas`
        :type Area: list of str
        """
        self._Domain = None
        self._Area = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainFilter(AbstractModel):
    """Filter conditions for domain name query.

    """

    def __init__(self):
        r"""
        :param _Name: Filter filter. Values:
- `origin`: Primary origin server.
- `domain`: Domain name.
- `resourceId`: Domain name ID.
- `status`: Domain name status. Values: `online`, `offline`, and `processing`.
- `serviceType`: Service type. Values: `web`, `download`, `media`, `hybrid` and `dynamic`.
- `projectId`: Project ID.
- `domainType`: Primary origin type. Values: `cname` (customer origin), `COS` (COS origin), `third_party` (third-party object storage origin), and `igtm` (IGTM origin).
- `fullUrlCache`: Whether to enable path cache. Values: `on`, `off`.
- `https`: Whether to configure HTTPS. Values: `on`, `off` and `processing`.
- `originPullProtocol`: Origin-pull protocol type. Value: `http`, `follow`, and `https`.
- `tagKey`: Tag key.
        :type Name: str
        :param _Value: Filter field value.
        :type Value: list of str
        :param _Fuzzy: Whether to enable fuzzy query. Only `origin` or `domain` is supported for the filter field name.
When fuzzy query is enabled, the maximum Value length is 1. When fuzzy query is disabled, the maximum Value length is 5.
        :type Fuzzy: bool
        """
        self._Name = None
        self._Value = None
        self._Fuzzy = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Fuzzy(self):
        return self._Fuzzy

    @Fuzzy.setter
    def Fuzzy(self, Fuzzy):
        self._Fuzzy = Fuzzy


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainLog(AbstractModel):
    """Details about a log package download link

    """

    def __init__(self):
        r"""
        :param _StartTime: Starting time of the log package
        :type StartTime: str
        :param _EndTime: End time of the log package
        :type EndTime: str
        :param _LogPath: Log package download link
        :type LogPath: str
        :param _Area: Acceleration region corresponding to the log package
`mainland`: Within the Chinese mainland
`overseas`: Outside the Chinese mainland
        :type Area: str
        :param _LogName: Log package filename
        :type LogName: str
        :param _FileSize: File size, in bytes.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type FileSize: int
        """
        self._StartTime = None
        self._EndTime = None
        self._LogPath = None
        self._Area = None
        self._LogName = None
        self._FileSize = None

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
    def LogPath(self):
        return self._LogPath

    @LogPath.setter
    def LogPath(self, LogPath):
        self._LogPath = LogPath

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def LogName(self):
        return self._LogName

    @LogName.setter
    def LogName(self, LogName):
        self._LogName = LogName

    @property
    def FileSize(self):
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._LogPath = params.get("LogPath")
        self._Area = params.get("Area")
        self._LogName = params.get("LogName")
        self._FileSize = params.get("FileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownstreamCapping(AbstractModel):
    """Single link downstream speed limit configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable downstream speed limit. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _CappingRules: Downstream speed limiting rules
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CappingRules: list of CappingRule
        """
        self._Switch = None
        self._CappingRules = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def CappingRules(self):
        return self._CappingRules

    @CappingRules.setter
    def CappingRules(self, CappingRules):
        self._CappingRules = CappingRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("CappingRules") is not None:
            self._CappingRules = []
            for item in params.get("CappingRules"):
                obj = CappingRule()
                obj._deserialize(item)
                self._CappingRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableCachesRequest(AbstractModel):
    """EnableCaches request structure.

    """

    def __init__(self):
        r"""
        :param _Urls: List of unblocked URLs
        :type Urls: list of str
        :param _Date: URL blocking date
        :type Date: str
        """
        self._Urls = None
        self._Date = None

    @property
    def Urls(self):
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date


    def _deserialize(self, params):
        self._Urls = params.get("Urls")
        self._Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableCachesResponse(AbstractModel):
    """EnableCaches response structure.

    """

    def __init__(self):
        r"""
        :param _CacheOptResult: Result list
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CacheOptResult: :class:`tencentcloud.cdn.v20180606.models.CacheOptResult`
        :param _TaskId: Task ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._CacheOptResult = None
        self._TaskId = None
        self._RequestId = None

    @property
    def CacheOptResult(self):
        return self._CacheOptResult

    @CacheOptResult.setter
    def CacheOptResult(self, CacheOptResult):
        self._CacheOptResult = CacheOptResult

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CacheOptResult") is not None:
            self._CacheOptResult = CacheOptResult()
            self._CacheOptResult._deserialize(params.get("CacheOptResult"))
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class EnableClsLogTopicRequest(AbstractModel):
    """EnableClsLogTopic request structure.

    """

    def __init__(self):
        r"""
        :param _LogsetId: Logset ID
        :type LogsetId: str
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _Channel: Specifies whether to access CDN or ECDN. Valid values: `cdn` (default) and `ecdn`.
        :type Channel: str
        """
        self._LogsetId = None
        self._TopicId = None
        self._Channel = None

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        self._Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableClsLogTopicResponse(AbstractModel):
    """EnableClsLogTopic response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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


class ErrorPage(AbstractModel):
    """Status code redirect configuration, which is disabled by default.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable status code-based redirection. Values:
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        :param _PageRules: Status code redirect rules configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PageRules: list of ErrorPageRule
        """
        self._Switch = None
        self._PageRules = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def PageRules(self):
        return self._PageRules

    @PageRules.setter
    def PageRules(self, PageRules):
        self._PageRules = PageRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("PageRules") is not None:
            self._PageRules = []
            for item in params.get("PageRules"):
                obj = ErrorPageRule()
                obj._deserialize(item)
                self._PageRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorPageRule(AbstractModel):
    """Status code redirect rules configuration

    """

    def __init__(self):
        r"""
        :param _StatusCode: Status code
Supports 400, 403, 404, 500.
        :type StatusCode: int
        :param _RedirectCode: Redirect status code settings
Supports 301 or 302.
        :type RedirectCode: int
        :param _RedirectUrl: Redirect URL
Requires a full redirect path, such as https://www.test.com/error.html.
        :type RedirectUrl: str
        """
        self._StatusCode = None
        self._RedirectCode = None
        self._RedirectUrl = None

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def RedirectCode(self):
        return self._RedirectCode

    @RedirectCode.setter
    def RedirectCode(self, RedirectCode):
        self._RedirectCode = RedirectCode

    @property
    def RedirectUrl(self):
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl


    def _deserialize(self, params):
        self._StatusCode = params.get("StatusCode")
        self._RedirectCode = params.get("RedirectCode")
        self._RedirectUrl = params.get("RedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtraLogset(AbstractModel):
    """Information of logsets and log topics (except those created in the Shanghai region)

    """

    def __init__(self):
        r"""
        :param _Logset: Logset information
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Logset: :class:`tencentcloud.cdn.v20180606.models.LogSetInfo`
        :param _Topics: Log topic information
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Topics: list of TopicInfo
        """
        self._Logset = None
        self._Topics = None

    @property
    def Logset(self):
        return self._Logset

    @Logset.setter
    def Logset(self, Logset):
        self._Logset = Logset

    @property
    def Topics(self):
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics


    def _deserialize(self, params):
        if params.get("Logset") is not None:
            self._Logset = LogSetInfo()
            self._Logset._deserialize(params.get("Logset"))
        if params.get("Topics") is not None:
            self._Topics = []
            for item in params.get("Topics"):
                obj = TopicInfo()
                obj._deserialize(item)
                self._Topics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FollowRedirect(AbstractModel):
    """301/302 automatic origin-pull follow-redirect configuration. It is disabled by default.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable origin-pull to follow the origin configuration. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _RedirectConfig: Specifies a host header for 302 redirects. This feature is only available to beta users. To join the beta, please submit a ticket.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RedirectConfig: :class:`tencentcloud.cdn.v20180606.models.RedirectConfig`
        """
        self._Switch = None
        self._RedirectConfig = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RedirectConfig(self):
        return self._RedirectConfig

    @RedirectConfig.setter
    def RedirectConfig(self, RedirectConfig):
        self._RedirectConfig = RedirectConfig


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("RedirectConfig") is not None:
            self._RedirectConfig = RedirectConfig()
            self._RedirectConfig._deserialize(params.get("RedirectConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForceRedirect(AbstractModel):
    """Access protocol forced redirect configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable forced HTTPS redirects. Values:
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        :param _RedirectType: Access forced redirect types
http: forced HTTP redirect
https: forced HTTPS redirect
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RedirectType: str
        :param _RedirectStatusCode: Status code returned for forced redirect 
Supports 301, 302.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RedirectStatusCode: int
        :param _CarryHeaders: Whether to return the newly added header during force redirection
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CarryHeaders: str
        """
        self._Switch = None
        self._RedirectType = None
        self._RedirectStatusCode = None
        self._CarryHeaders = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RedirectType(self):
        return self._RedirectType

    @RedirectType.setter
    def RedirectType(self, RedirectType):
        self._RedirectType = RedirectType

    @property
    def RedirectStatusCode(self):
        return self._RedirectStatusCode

    @RedirectStatusCode.setter
    def RedirectStatusCode(self, RedirectStatusCode):
        self._RedirectStatusCode = RedirectStatusCode

    @property
    def CarryHeaders(self):
        return self._CarryHeaders

    @CarryHeaders.setter
    def CarryHeaders(self, CarryHeaders):
        self._CarryHeaders = CarryHeaders


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._RedirectType = params.get("RedirectType")
        self._RedirectStatusCode = params.get("RedirectStatusCode")
        self._CarryHeaders = params.get("CarryHeaders")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDisableRecordsRequest(AbstractModel):
    """GetDisableRecords request structure.

    """

    def __init__(self):
        r"""
        :param _Url: Specifies the URL to be queried
        :type Url: str
        :param _StartTime: Starting time, such as `2018-12-12 10:24:00`
        :type StartTime: str
        :param _EndTime: End time, such as `2018-12-14 10:24:00`
        :type EndTime: str
        :param _Status: Current URL status
disable: The URL remains disabled, and accessing it will return an error 403
enable: The URL is enabled (unblocked) and can be normally accessed
        :type Status: str
        :param _Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param _Limit: Pagination limit. Default value: 20.
        :type Limit: int
        :param _TaskId: Task ID. The task ID and start time cannot be both left empty.
        :type TaskId: str
        """
        self._Url = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._Offset = None
        self._Limit = None
        self._TaskId = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDisableRecordsResponse(AbstractModel):
    """GetDisableRecords response structure.

    """

    def __init__(self):
        r"""
        :param _UrlRecordList: Blocking history
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UrlRecordList: list of UrlRecord
        :param _TotalCount: Total number of tasks, which is used for pagination.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UrlRecordList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def UrlRecordList(self):
        return self._UrlRecordList

    @UrlRecordList.setter
    def UrlRecordList(self, UrlRecordList):
        self._UrlRecordList = UrlRecordList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UrlRecordList") is not None:
            self._UrlRecordList = []
            for item in params.get("UrlRecordList"):
                obj = UrlRecord()
                obj._deserialize(item)
                self._UrlRecordList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class GuetzliAdapter(AbstractModel):
    """Image optimization - `GuetzliAdapter` configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable AvifAdapter for image optimization. Values:
`on`: Enable
`off`: Disable
Note: This field may return·`null`, indicating that no valid values can be obtained.
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HTTPHeader(AbstractModel):
    """HTTP request header

    """

    def __init__(self):
        r"""
        :param _Name: Request header name
        :type Name: str
        :param _Value: Request header value
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HeaderKey(AbstractModel):
    """A part of `CacheKey`

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable Cachekey control. Values:
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        :param _Value: Array of headers that make up the `CacheKey` (separated by ';')
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Value: str
        """
        self._Switch = None
        self._Value = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HeuristicCache(AbstractModel):
    """Heuristic cache configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable heuristic caching. Values:
`on`: Enable
`off`: Disable
Note: This field may return·`null`, indicating that no valid values can be obtained.
        :type Switch: str
        :param _CacheConfig: Heuristic cache validity configuration
Note: This field may return·`null`, indicating that no valid values can be obtained.
        :type CacheConfig: :class:`tencentcloud.cdn.v20180606.models.CacheConfig`
        """
        self._Switch = None
        self._CacheConfig = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def CacheConfig(self):
        return self._CacheConfig

    @CacheConfig.setter
    def CacheConfig(self, CacheConfig):
        self._CacheConfig = CacheConfig


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("CacheConfig") is not None:
            self._CacheConfig = CacheConfig()
            self._CacheConfig._deserialize(params.get("CacheConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Hsts(AbstractModel):
    """HSTS configuration.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable HSTS. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _MaxAge: `MaxAge` value.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MaxAge: int
        :param _IncludeSubDomains: Whether to include subdomain names. Valid values: on, off.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IncludeSubDomains: str
        """
        self._Switch = None
        self._MaxAge = None
        self._IncludeSubDomains = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def MaxAge(self):
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def IncludeSubDomains(self):
        return self._IncludeSubDomains

    @IncludeSubDomains.setter
    def IncludeSubDomains(self, IncludeSubDomains):
        self._IncludeSubDomains = IncludeSubDomains


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._MaxAge = params.get("MaxAge")
        self._IncludeSubDomains = params.get("IncludeSubDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpHeaderPathRule(AbstractModel):
    """HTTP header setting rules. Up to 100 entries can be set.

    """

    def __init__(self):
        r"""
        :param _HeaderMode: HTTP header setting methods
`set`: sets a value for an existing header parameter, a new header parameter, or multiple header parameters. Multiple header parameters will be merged into one.
`del`: deletes a header parameter.
`add`: adds a header parameter. By default, you can repeat the same action to add the same header parameter, which may affect browser response. Please consider the set operation first.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type HeaderMode: str
        :param _HeaderName: HTTP header name. Up to 100 characters can be set.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type HeaderName: str
        :param _HeaderValue: HTTP header value. Up to 1000 characters can be set.
Not required when Mode is del
Required when Mode is add/set
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type HeaderValue: str
        :param _RuleType: Rule types:
`all`: Apply to all files.
`file`: Apply to files with the specified suffixes.
`directory`: Apply to specified paths.
`path`: Apply to specified absolute paths.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleType: str
        :param _RulePaths: Content for each `RuleType`:
For `all`, enter a wildcard `*`.
For `file`, enter a suffix, e.g., `jpg` or `txt`.
For `directory`, enter a path, e.g., `/xxx/test/`.
For `path`, enter an absolute path, e.g., `/xxx/test.html`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RulePaths: list of str
        """
        self._HeaderMode = None
        self._HeaderName = None
        self._HeaderValue = None
        self._RuleType = None
        self._RulePaths = None

    @property
    def HeaderMode(self):
        return self._HeaderMode

    @HeaderMode.setter
    def HeaderMode(self, HeaderMode):
        self._HeaderMode = HeaderMode

    @property
    def HeaderName(self):
        return self._HeaderName

    @HeaderName.setter
    def HeaderName(self, HeaderName):
        self._HeaderName = HeaderName

    @property
    def HeaderValue(self):
        return self._HeaderValue

    @HeaderValue.setter
    def HeaderValue(self, HeaderValue):
        self._HeaderValue = HeaderValue

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RulePaths(self):
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths


    def _deserialize(self, params):
        self._HeaderMode = params.get("HeaderMode")
        self._HeaderName = params.get("HeaderName")
        self._HeaderValue = params.get("HeaderValue")
        self._RuleType = params.get("RuleType")
        self._RulePaths = params.get("RulePaths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpHeaderRule(AbstractModel):
    """HTTP header setting rules.

    """

    def __init__(self):
        r"""
        :param _HeaderMode: HTTP header setting method. Valid values: `add` (add header), `set` (set header) or `del` (delete header).
        :type HeaderMode: str
        :param _HeaderName: HTTP header name
        :type HeaderName: str
        :param _HeaderValue: HTTP header value
        :type HeaderValue: str
        """
        self._HeaderMode = None
        self._HeaderName = None
        self._HeaderValue = None

    @property
    def HeaderMode(self):
        return self._HeaderMode

    @HeaderMode.setter
    def HeaderMode(self, HeaderMode):
        self._HeaderMode = HeaderMode

    @property
    def HeaderName(self):
        return self._HeaderName

    @HeaderName.setter
    def HeaderName(self, HeaderName):
        self._HeaderName = HeaderName

    @property
    def HeaderValue(self):
        return self._HeaderValue

    @HeaderValue.setter
    def HeaderValue(self, HeaderValue):
        self._HeaderValue = HeaderValue


    def _deserialize(self, params):
        self._HeaderMode = params.get("HeaderMode")
        self._HeaderName = params.get("HeaderName")
        self._HeaderValue = params.get("HeaderValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Https(AbstractModel):
    """Domain name HTTPS acceleration configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable HTTPS. Values:
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        :param _Http2: Whether to enable HTTP2
`on`: Enable
`off`: Disable
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Http2: str
        :param _OcspStapling: OCSP configuration switch
`on`: Enable
`off`: Disable
It is disabled by default.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OcspStapling: str
        :param _VerifyClient: Client certificate authentication feature
`on`: Enable
`off`: Disable
This is disabled by default. The client certificate information is needed when enabled. This is still in beta and not generally available yet.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type VerifyClient: str
        :param _CertInfo: Server certificate configuration information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CertInfo: :class:`tencentcloud.cdn.v20180606.models.ServerCert`
        :param _ClientCertInfo: Client certificate configuration information
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ClientCertInfo: :class:`tencentcloud.cdn.v20180606.models.ClientCert`
        :param _Spdy: Spdy configuration switch
`on`: Enable
`off`: Disable
It is disabled by default.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Spdy: str
        :param _SslStatus: HTTPS certificate deployment status
closed: already closed
deploying: in deployment
deployed: successfully deployed
failed: deployment failed
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SslStatus: str
        :param _Hsts: HSTS configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Hsts: :class:`tencentcloud.cdn.v20180606.models.Hsts`
        :param _TlsVersion: TLS version settings, which only support certain advanced domain names. Valid values: `TLSv1`, `TLSV1.1`, `TLSV1.2`, and `TLSv1.3`. Only consecutive versions can be enabled at the same time.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TlsVersion: list of str
        """
        self._Switch = None
        self._Http2 = None
        self._OcspStapling = None
        self._VerifyClient = None
        self._CertInfo = None
        self._ClientCertInfo = None
        self._Spdy = None
        self._SslStatus = None
        self._Hsts = None
        self._TlsVersion = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Http2(self):
        return self._Http2

    @Http2.setter
    def Http2(self, Http2):
        self._Http2 = Http2

    @property
    def OcspStapling(self):
        return self._OcspStapling

    @OcspStapling.setter
    def OcspStapling(self, OcspStapling):
        self._OcspStapling = OcspStapling

    @property
    def VerifyClient(self):
        return self._VerifyClient

    @VerifyClient.setter
    def VerifyClient(self, VerifyClient):
        self._VerifyClient = VerifyClient

    @property
    def CertInfo(self):
        return self._CertInfo

    @CertInfo.setter
    def CertInfo(self, CertInfo):
        self._CertInfo = CertInfo

    @property
    def ClientCertInfo(self):
        return self._ClientCertInfo

    @ClientCertInfo.setter
    def ClientCertInfo(self, ClientCertInfo):
        self._ClientCertInfo = ClientCertInfo

    @property
    def Spdy(self):
        return self._Spdy

    @Spdy.setter
    def Spdy(self, Spdy):
        self._Spdy = Spdy

    @property
    def SslStatus(self):
        return self._SslStatus

    @SslStatus.setter
    def SslStatus(self, SslStatus):
        self._SslStatus = SslStatus

    @property
    def Hsts(self):
        return self._Hsts

    @Hsts.setter
    def Hsts(self, Hsts):
        self._Hsts = Hsts

    @property
    def TlsVersion(self):
        return self._TlsVersion

    @TlsVersion.setter
    def TlsVersion(self, TlsVersion):
        self._TlsVersion = TlsVersion


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Http2 = params.get("Http2")
        self._OcspStapling = params.get("OcspStapling")
        self._VerifyClient = params.get("VerifyClient")
        if params.get("CertInfo") is not None:
            self._CertInfo = ServerCert()
            self._CertInfo._deserialize(params.get("CertInfo"))
        if params.get("ClientCertInfo") is not None:
            self._ClientCertInfo = ClientCert()
            self._ClientCertInfo._deserialize(params.get("ClientCertInfo"))
        self._Spdy = params.get("Spdy")
        self._SslStatus = params.get("SslStatus")
        if params.get("Hsts") is not None:
            self._Hsts = Hsts()
            self._Hsts._deserialize(params.get("Hsts"))
        self._TlsVersion = params.get("TlsVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpsBilling(AbstractModel):
    """HTTPS. When it’s disabled, HTTPS requests are blocked.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable HTTPS. Values:
`on`: When it's enabled, HTTPS requests are allowed and incur charges. If not specified, his field uses the default value `on`.
`off`: When it's disabled, HTTPS requests are blocked.

        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HwPrivateAccess(AbstractModel):
    """Origin-pull authentication for Huawei Cloud OBS origin

    """

    def __init__(self):
        r"""
        :param _Switch:  Whether to enable origin-pull authentication for Huawei Cloud OBS origin. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _AccessKey: Access ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AccessKey: str
        :param _SecretKey: Key
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type SecretKey: str
        :param _Bucket: BucketName
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Bucket: str
        """
        self._Switch = None
        self._AccessKey = None
        self._SecretKey = None
        self._Bucket = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def AccessKey(self):
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        self._Bucket = params.get("Bucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageOptimization(AbstractModel):
    """Image optimization configuration

    """

    def __init__(self):
        r"""
        :param _WebpAdapter: `WebpAdapter` configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type WebpAdapter: :class:`tencentcloud.cdn.v20180606.models.WebpAdapter`
        :param _TpgAdapter: `TpgAdapter` configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TpgAdapter: :class:`tencentcloud.cdn.v20180606.models.TpgAdapter`
        :param _GuetzliAdapter: `GuetzliAdapter` configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type GuetzliAdapter: :class:`tencentcloud.cdn.v20180606.models.GuetzliAdapter`
        :param _AvifAdapter: AVIF adapter configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AvifAdapter: :class:`tencentcloud.cdn.v20180606.models.AvifAdapter`
        """
        self._WebpAdapter = None
        self._TpgAdapter = None
        self._GuetzliAdapter = None
        self._AvifAdapter = None

    @property
    def WebpAdapter(self):
        return self._WebpAdapter

    @WebpAdapter.setter
    def WebpAdapter(self, WebpAdapter):
        self._WebpAdapter = WebpAdapter

    @property
    def TpgAdapter(self):
        return self._TpgAdapter

    @TpgAdapter.setter
    def TpgAdapter(self, TpgAdapter):
        self._TpgAdapter = TpgAdapter

    @property
    def GuetzliAdapter(self):
        return self._GuetzliAdapter

    @GuetzliAdapter.setter
    def GuetzliAdapter(self, GuetzliAdapter):
        self._GuetzliAdapter = GuetzliAdapter

    @property
    def AvifAdapter(self):
        return self._AvifAdapter

    @AvifAdapter.setter
    def AvifAdapter(self, AvifAdapter):
        self._AvifAdapter = AvifAdapter


    def _deserialize(self, params):
        if params.get("WebpAdapter") is not None:
            self._WebpAdapter = WebpAdapter()
            self._WebpAdapter._deserialize(params.get("WebpAdapter"))
        if params.get("TpgAdapter") is not None:
            self._TpgAdapter = TpgAdapter()
            self._TpgAdapter._deserialize(params.get("TpgAdapter"))
        if params.get("GuetzliAdapter") is not None:
            self._GuetzliAdapter = GuetzliAdapter()
            self._GuetzliAdapter._deserialize(params.get("GuetzliAdapter"))
        if params.get("AvifAdapter") is not None:
            self._AvifAdapter = AvifAdapter()
            self._AvifAdapter._deserialize(params.get("AvifAdapter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpFilter(AbstractModel):
    """IP blocklist/allowlist configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable IP blocklist/allowlist. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _FilterType: IP blocklist/allowlist type
`whitelist`: IP allowlist
`blacklist`: IP blocklist
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FilterType: str
        :param _Filters: IP blocklist/allowlist
Supports IPs in X.X.X.X format, or IP ranges in /8, /16, /24 format.
Up to 50 whitelists or blacklists can be entered
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Filters: list of str
        :param _FilterRules: IP blocklist/allowlist path-based configuration. This feature is only available to selected beta customers.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FilterRules: list of IpFilterPathRule
        :param _ReturnCode: (Disused) Expected HTTP code to return when the IP allowlist/blocklist verification fails. <br><font color=red>The 514 code is used instead.</font>
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ReturnCode: int
        """
        self._Switch = None
        self._FilterType = None
        self._Filters = None
        self._FilterRules = None
        self._ReturnCode = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def FilterType(self):
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def FilterRules(self):
        return self._FilterRules

    @FilterRules.setter
    def FilterRules(self, FilterRules):
        self._FilterRules = FilterRules

    @property
    def ReturnCode(self):
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._FilterType = params.get("FilterType")
        self._Filters = params.get("Filters")
        if params.get("FilterRules") is not None:
            self._FilterRules = []
            for item in params.get("FilterRules"):
                obj = IpFilterPathRule()
                obj._deserialize(item)
                self._FilterRules.append(obj)
        self._ReturnCode = params.get("ReturnCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpFilterPathRule(AbstractModel):
    """IP blocklist/allowlist path-based configuration

    """

    def __init__(self):
        r"""
        :param _FilterType: IP blocklist/allowlist type
`whitelist`: allowlist IPs
`blacklist`: blocklist IPs
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FilterType: str
        :param _Filters: IP blocklist/allowlist list
Supports IPs in X.X.X.X format, or /8, /16, /24 format IP ranges.
Up to 50 allowlists or blocklists can be entered.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Filters: list of str
        :param _RuleType: Rule types:
`all`: Effective for all files
`file`: Effective for specified file suffixes
`directory`: Effective for specified paths
`path`: Effective for specified absolute paths
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleType: str
        :param _RulePaths: Content for each RuleType:
For `all`, enter an asterisk (*).
For `file`, enter the suffix, such as jpg, txt.
For `directory`, enter the path, such as /xxx/test/.
For `path`, enter the corresponding absolute path, such as /xxx/test.html.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RulePaths: list of str
        """
        self._FilterType = None
        self._Filters = None
        self._RuleType = None
        self._RulePaths = None

    @property
    def FilterType(self):
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RulePaths(self):
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths


    def _deserialize(self, params):
        self._FilterType = params.get("FilterType")
        self._Filters = params.get("Filters")
        self._RuleType = params.get("RuleType")
        self._RulePaths = params.get("RulePaths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpFreqLimit(AbstractModel):
    """Access limit configuration for a single IP of a single node. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable IP rate limit. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _Qps: Sets the limited number of requests per second
514 will be returned for requests that exceed the limit
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Qps: int
        """
        self._Switch = None
        self._Qps = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Qps(self):
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Qps = params.get("Qps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpStatus(AbstractModel):
    """Node IP information

    """

    def __init__(self):
        r"""
        :param _Ip: Node IP
        :type Ip: str
        :param _District: Region of the node
        :type District: str
        :param _Isp: ISP of the node
        :type Isp: str
        :param _City: City of the node
        :type City: str
        :param _Status: Status of the node
`online`: The node is active and scheduling normally.
`offline`: The node is inactive.
        :type Status: str
        """
        self._Ip = None
        self._District = None
        self._Isp = None
        self._City = None
        self._Status = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def District(self):
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._District = params.get("District")
        self._Isp = params.get("Isp")
        self._City = params.get("City")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ipv6(AbstractModel):
    """IPv6 origin configuration (changes not allowed).

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable an IPv6 address for the origin server. Values:
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ipv6Access(AbstractModel):
    """IPv6 access configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable IPv6 access. Values:
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyRule(AbstractModel):
    """Path-based cache key configuration

    """

    def __init__(self):
        r"""
        :param _RulePaths: Content for each CacheType:
For `file`, enter a suffix, e.g., `jpg` or `txt`.
For `directory`, enter the path, such as /xxx/test/.
For `path`, enter an absolute path, e.g., `/xxx/test.html`.
For `index`, enter a backslash (/).
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type RulePaths: list of str
        :param _RuleType: Rule types:
`file`: Apply to files with the specified suffixes.
`directory`: Apply to specified paths.
`path`: Apply to specified absolute paths.
`index`: home page
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleType: str
        :param _FullUrlCache: Whether to enable full-path cache
`on`: Enable full-path cache (i.e., disable Ignore Query String).
`off`: Disable full-path cache (i.e., enable Ignore Query String).
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FullUrlCache: str
        :param _IgnoreCase: Whether caches are case insensitive
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IgnoreCase: str
        :param _QueryString: Request parameter contained in `CacheKey`
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type QueryString: :class:`tencentcloud.cdn.v20180606.models.RuleQueryString`
        :param _RuleTag: Path cache key tag, the value "user" is passed.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleTag: str
        """
        self._RulePaths = None
        self._RuleType = None
        self._FullUrlCache = None
        self._IgnoreCase = None
        self._QueryString = None
        self._RuleTag = None

    @property
    def RulePaths(self):
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def FullUrlCache(self):
        return self._FullUrlCache

    @FullUrlCache.setter
    def FullUrlCache(self, FullUrlCache):
        self._FullUrlCache = FullUrlCache

    @property
    def IgnoreCase(self):
        return self._IgnoreCase

    @IgnoreCase.setter
    def IgnoreCase(self, IgnoreCase):
        self._IgnoreCase = IgnoreCase

    @property
    def QueryString(self):
        return self._QueryString

    @QueryString.setter
    def QueryString(self, QueryString):
        self._QueryString = QueryString

    @property
    def RuleTag(self):
        return self._RuleTag

    @RuleTag.setter
    def RuleTag(self, RuleTag):
        self._RuleTag = RuleTag


    def _deserialize(self, params):
        self._RulePaths = params.get("RulePaths")
        self._RuleType = params.get("RuleType")
        self._FullUrlCache = params.get("FullUrlCache")
        self._IgnoreCase = params.get("IgnoreCase")
        if params.get("QueryString") is not None:
            self._QueryString = RuleQueryString()
            self._QueryString._deserialize(params.get("QueryString"))
        self._RuleTag = params.get("RuleTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListClsLogTopicsRequest(AbstractModel):
    """ListClsLogTopics request structure.

    """

    def __init__(self):
        r"""
        :param _Channel: Specifies whether to access CDN or ECDN. Valid values: `cdn` (default) and `ecdn`.
        :type Channel: str
        """
        self._Channel = None

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel


    def _deserialize(self, params):
        self._Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListClsLogTopicsResponse(AbstractModel):
    """ListClsLogTopics response structure.

    """

    def __init__(self):
        r"""
        :param _Logset: Information of logsets in the Shanghai region
        :type Logset: :class:`tencentcloud.cdn.v20180606.models.LogSetInfo`
        :param _Topics: Information of log topics in the Shanghai region
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Topics: list of TopicInfo
        :param _ExtraLogset: Information on logsets in regions except Shanghai
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ExtraLogset: list of ExtraLogset
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Logset = None
        self._Topics = None
        self._ExtraLogset = None
        self._RequestId = None

    @property
    def Logset(self):
        return self._Logset

    @Logset.setter
    def Logset(self, Logset):
        self._Logset = Logset

    @property
    def Topics(self):
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

    @property
    def ExtraLogset(self):
        return self._ExtraLogset

    @ExtraLogset.setter
    def ExtraLogset(self, ExtraLogset):
        self._ExtraLogset = ExtraLogset

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Logset") is not None:
            self._Logset = LogSetInfo()
            self._Logset._deserialize(params.get("Logset"))
        if params.get("Topics") is not None:
            self._Topics = []
            for item in params.get("Topics"):
                obj = TopicInfo()
                obj._deserialize(item)
                self._Topics.append(obj)
        if params.get("ExtraLogset") is not None:
            self._ExtraLogset = []
            for item in params.get("ExtraLogset"):
                obj = ExtraLogset()
                obj._deserialize(item)
                self._ExtraLogset.append(obj)
        self._RequestId = params.get("RequestId")


class ListClsTopicDomainsRequest(AbstractModel):
    """ListClsTopicDomains request structure.

    """

    def __init__(self):
        r"""
        :param _LogsetId: Logset ID
        :type LogsetId: str
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _Channel: Specifies whether to access CDN or ECDN. Valid values: `cdn` (default) and `ecdn`.
        :type Channel: str
        """
        self._LogsetId = None
        self._TopicId = None
        self._Channel = None

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        self._Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListClsTopicDomainsResponse(AbstractModel):
    """ListClsTopicDomains response structure.

    """

    def __init__(self):
        r"""
        :param _AppId: Developer ID
        :type AppId: int
        :param _Channel: Channel
        :type Channel: str
        :param _LogsetId: Logset ID
        :type LogsetId: str
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _DomainAreaConfigs: Domain name region configuration, which may contain deleted domain names. If this is to be used in `ManageClsTopicDomains` API, you need to exclude deleted domain names by using the `ListCdnDomains` API.
        :type DomainAreaConfigs: list of DomainAreaConfig
        :param _TopicName: Log topic name
        :type TopicName: str
        :param _UpdateTime: Last modified time of log topic
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UpdateTime: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._AppId = None
        self._Channel = None
        self._LogsetId = None
        self._TopicId = None
        self._DomainAreaConfigs = None
        self._TopicName = None
        self._UpdateTime = None
        self._RequestId = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def DomainAreaConfigs(self):
        return self._DomainAreaConfigs

    @DomainAreaConfigs.setter
    def DomainAreaConfigs(self, DomainAreaConfigs):
        self._DomainAreaConfigs = DomainAreaConfigs

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Channel = params.get("Channel")
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        if params.get("DomainAreaConfigs") is not None:
            self._DomainAreaConfigs = []
            for item in params.get("DomainAreaConfigs"):
                obj = DomainAreaConfig()
                obj._deserialize(item)
                self._DomainAreaConfigs.append(obj)
        self._TopicName = params.get("TopicName")
        self._UpdateTime = params.get("UpdateTime")
        self._RequestId = params.get("RequestId")


class ListTopDataRequest(AbstractModel):
    """ListTopData request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Query start time in the format of `yyyy-MM-dd HH:mm:ss`
Only data queries at the granularity of minutes are supported. The start time is truncated to minutes. For example, if the value of `StartTime` is 2018-09-04 10:40:23, the start time of the data returned is 2018-09-04 10:40:00.
Only data for the last 90 days can be queried.
        :type StartTime: str
        :param _EndTime: Query end time in the format of `yyyy-MM-dd HH:mm:ss`
Only data queries at the granularity of days are supported. Take the day in the input parameter as the end date, and the data generated on or before 23:59:59 on the end date is returned. For example, if the value of `EndTime` is 2018-09-05 22:40:00, the end time of the data returned is 2018-09-05 23:59:59.
`EndTime` must be later than or equal to `StartTime`.
        :type EndTime: str
        :param _Metric: Objects to be sorted. Valid values:
`url`: Sort by access URL (URLs carrying no parameters). Supported filters are `flux` and `request`.
`district`: sorts provinces or countries/regions. Supported filters are `flux` and `request`.
`isp`: sorts ISPs. Supported filters are `flux` and `request`.
`host`: Sort by domain name access data. Supported filters are `flux`, `request`, `bandwidth`, `fluxHitRate`, and `statusCode` (2XX, 3XX, 4XX, 5XX).
`originHost`: Sort by domain name origin-pull data. Supported filters are `flux`, `request`, `bandwidth`, and `OriginStatusCode` (origin_2XX, origin_3XX, origin_4XX, origin_5XX).
        :type Metric: str
        :param _Filter: Metric name used for sorting:
flux: If Metric is `host`, it indicates the access traffic; if Metric is `originHost`, it indicates the origin-pull traffic.
bandwidth: If Metric is `host`, it indicates the access bandwidth; if Metric is `originHost`, it indicates the origin-pull bandwidth.
request: If Metric is `host`, it indicates the number of access requests; if Metric is `originHost`, it indicates the number of origin-pull requests.
fluxHitRate: Average traffic hit rate
2XX: access 2XX status code
3XX: access 3XX status code
4XX: access 4XX status code
5XX: access 5XX status code
origin_2XX: origin-pull 2XX status code
origin_3XX: origin-pull 3XX status code
origin_4XX: origin-pull 4XX status code
origin_5XX: origin-pull 5XX status code
statusCode: statistics of a specific access status code which is specified in the `Code` parameter.
OriginStatusCode: statistics of a specific origin-pull status code which is specified in the `Code` parameter.
        :type Filter: str
        :param _Domains: Specifies the list of domain names to be queried; up to 30 domain names can be queried at a time.
        :type Domains: list of str
        :param _Project: Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)
Please note that if domain names are specified, this parameter will be ignored.
        :type Project: int
        :param _Detail: The sorted results of all domain names are returned by default (false) during a multi-domain-name query
If `Metric` is `url`, `path`, `district`, or `isp` and `Filter` is `flux` or `request`, it can be set to `true` to return the sorted results of each domain.
        :type Detail: bool
        :param _Code: When Filter is `statusCode` or `OriginStatusCode`, enter a code to query and sort results.
        :type Code: str
        :param _Area: Specifies the service region. If this value is left blank, it means to query CDN data within the Chinese mainland.
`mainland`: Query CDN data in the Chinese mainland.
`overseas`: Query CDN data outside the Chinese mainland. Supported metrics are `url`, `district`, `host`, and `originHost`. If `Metric` is `originHost`, supported filters are `flux`, `request`, and `bandwidth`.
        :type Area: str
        :param _AreaType: Specifies a region type for the query. If it is left blank, data of the service region will be queried. This parameter is only valid when `Area` is `overseas` and `Metric` is `district` or `host`.
`server`: Query by the location of server (Tencent Cloud CDN nodes).
`client`: Query data of the client region where the request devices are located; if `Metric` is `host`, supported filters are `flux`, `request`, and `bandwidth`.
        :type AreaType: str
        :param _Product: Specifies the product to query, either `cdn` (default) or `ecdn`.
        :type Product: str
        :param _Limit: Returns the first N data entries. The default value is 100 if this parameter is not specified, whereas 1000 if `Metric` is `url`.
        :type Limit: int
        """
        self._StartTime = None
        self._EndTime = None
        self._Metric = None
        self._Filter = None
        self._Domains = None
        self._Project = None
        self._Detail = None
        self._Code = None
        self._Area = None
        self._AreaType = None
        self._Product = None
        self._Limit = None

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
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Project(self):
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def Detail(self):
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def AreaType(self):
        return self._AreaType

    @AreaType.setter
    def AreaType(self, AreaType):
        self._AreaType = AreaType

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Metric = params.get("Metric")
        self._Filter = params.get("Filter")
        self._Domains = params.get("Domains")
        self._Project = params.get("Project")
        self._Detail = params.get("Detail")
        self._Code = params.get("Code")
        self._Area = params.get("Area")
        self._AreaType = params.get("AreaType")
        self._Product = params.get("Product")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTopDataResponse(AbstractModel):
    """ListTopData response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Top access data details of each resource
        :type Data: list of TopData
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TopData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class LogSetInfo(AbstractModel):
    """Logset information

    """

    def __init__(self):
        r"""
        :param _AppId: Developer ID
        :type AppId: int
        :param _Channel: Channel
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Channel: str
        :param _LogsetId: Logset ID
        :type LogsetId: str
        :param _LogsetName: Logset name
        :type LogsetName: str
        :param _IsDefault: Whether it is the default logset
        :type IsDefault: int
        :param _LogsetSavePeriod: Log retention period in days
        :type LogsetSavePeriod: int
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _Region: Region
        :type Region: str
        :param _Deleted: Whether the logset has been removed from CLS
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Deleted: str
        :param _RegionEn: Whether English is used in this region
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RegionEn: str
        """
        self._AppId = None
        self._Channel = None
        self._LogsetId = None
        self._LogsetName = None
        self._IsDefault = None
        self._LogsetSavePeriod = None
        self._CreateTime = None
        self._Region = None
        self._Deleted = None
        self._RegionEn = None

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def LogsetName(self):
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def IsDefault(self):
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def LogsetSavePeriod(self):
        return self._LogsetSavePeriod

    @LogsetSavePeriod.setter
    def LogsetSavePeriod(self, LogsetSavePeriod):
        self._LogsetSavePeriod = LogsetSavePeriod

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Deleted(self):
        return self._Deleted

    @Deleted.setter
    def Deleted(self, Deleted):
        self._Deleted = Deleted

    @property
    def RegionEn(self):
        return self._RegionEn

    @RegionEn.setter
    def RegionEn(self, RegionEn):
        self._RegionEn = RegionEn


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Channel = params.get("Channel")
        self._LogsetId = params.get("LogsetId")
        self._LogsetName = params.get("LogsetName")
        self._IsDefault = params.get("IsDefault")
        self._LogsetSavePeriod = params.get("LogsetSavePeriod")
        self._CreateTime = params.get("CreateTime")
        self._Region = params.get("Region")
        self._Deleted = params.get("Deleted")
        self._RegionEn = params.get("RegionEn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MainlandConfig(AbstractModel):
    """Specific configuration for domain names in the Chinese mainland. Specific configuration by region. The `UpdateDomainConfig` API only supports modification of some region configurations. A list of differences that may exist for older configurations will be provided for a compatibility check. The supported configuration list is as follows:
    + Authentication
    + BandwidthAlert
    + ErrorPage
    + IpFilter
    + Origin
    + Referer

    """

    def __init__(self):
        r"""
        :param _Authentication: Timestamp hotlink protection configuration.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param _BandwidthAlert: Bandwidth cap configuration.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param _Cache: Cache rule configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param _CacheKey: Cache configurations.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param _Compression: Smart compression configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param _DownstreamCapping: Download speed limit configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param _ErrorPage: Error code redirect configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param _FollowRedirect: 301 and 302 automatic origin-pull follow-redirect configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param _ForceRedirect: Force redirect by access protocol.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param _Https: HTTPS configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param _IpFilter: IP blocklist/allowlist configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param _IpFreqLimit: IP access limiting configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param _MaxAge: Browser cache rules configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param _Origin: Origin server configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param _OriginPullOptimization: Cross-border optimization configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param _RangeOriginPull: Range GETs configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param _Referer: Hotlink protection configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param _RequestHeader: Origin-pull request header configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param _ResponseHeader: Origin server response header configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param _ResponseHeaderCache: Follows origin server cache header configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param _Seo: SEO configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param _ServiceType: Domain name service type. Values: `web` (static acceleration); `download` (download acceleration); `media` (streaming media acceleration).
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ServiceType: str
        :param _StatusCodeCache: Status code cache configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param _VideoSeek: Video dragging configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        :param _AwsPrivateAccess: Access authentication for S3 origin
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AwsPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`
        :param _OssPrivateAccess: Access authentication for OSS origin
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OssPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.OssPrivateAccess`
        :param _HwPrivateAccess: Access authentication for Huawei Cloud OBS origin
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type HwPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.HwPrivateAccess`
        :param _QnPrivateAccess: Access authentication for QiNiu Cloud Kodo origin
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type QnPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.QnPrivateAccess`
        """
        self._Authentication = None
        self._BandwidthAlert = None
        self._Cache = None
        self._CacheKey = None
        self._Compression = None
        self._DownstreamCapping = None
        self._ErrorPage = None
        self._FollowRedirect = None
        self._ForceRedirect = None
        self._Https = None
        self._IpFilter = None
        self._IpFreqLimit = None
        self._MaxAge = None
        self._Origin = None
        self._OriginPullOptimization = None
        self._RangeOriginPull = None
        self._Referer = None
        self._RequestHeader = None
        self._ResponseHeader = None
        self._ResponseHeaderCache = None
        self._Seo = None
        self._ServiceType = None
        self._StatusCodeCache = None
        self._VideoSeek = None
        self._AwsPrivateAccess = None
        self._OssPrivateAccess = None
        self._HwPrivateAccess = None
        self._QnPrivateAccess = None

    @property
    def Authentication(self):
        return self._Authentication

    @Authentication.setter
    def Authentication(self, Authentication):
        self._Authentication = Authentication

    @property
    def BandwidthAlert(self):
        return self._BandwidthAlert

    @BandwidthAlert.setter
    def BandwidthAlert(self, BandwidthAlert):
        self._BandwidthAlert = BandwidthAlert

    @property
    def Cache(self):
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def CacheKey(self):
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def Compression(self):
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def DownstreamCapping(self):
        return self._DownstreamCapping

    @DownstreamCapping.setter
    def DownstreamCapping(self, DownstreamCapping):
        self._DownstreamCapping = DownstreamCapping

    @property
    def ErrorPage(self):
        return self._ErrorPage

    @ErrorPage.setter
    def ErrorPage(self, ErrorPage):
        self._ErrorPage = ErrorPage

    @property
    def FollowRedirect(self):
        return self._FollowRedirect

    @FollowRedirect.setter
    def FollowRedirect(self, FollowRedirect):
        self._FollowRedirect = FollowRedirect

    @property
    def ForceRedirect(self):
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def Https(self):
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def IpFilter(self):
        return self._IpFilter

    @IpFilter.setter
    def IpFilter(self, IpFilter):
        self._IpFilter = IpFilter

    @property
    def IpFreqLimit(self):
        return self._IpFreqLimit

    @IpFreqLimit.setter
    def IpFreqLimit(self, IpFreqLimit):
        self._IpFreqLimit = IpFreqLimit

    @property
    def MaxAge(self):
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def OriginPullOptimization(self):
        return self._OriginPullOptimization

    @OriginPullOptimization.setter
    def OriginPullOptimization(self, OriginPullOptimization):
        self._OriginPullOptimization = OriginPullOptimization

    @property
    def RangeOriginPull(self):
        return self._RangeOriginPull

    @RangeOriginPull.setter
    def RangeOriginPull(self, RangeOriginPull):
        self._RangeOriginPull = RangeOriginPull

    @property
    def Referer(self):
        return self._Referer

    @Referer.setter
    def Referer(self, Referer):
        self._Referer = Referer

    @property
    def RequestHeader(self):
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader

    @property
    def ResponseHeader(self):
        return self._ResponseHeader

    @ResponseHeader.setter
    def ResponseHeader(self, ResponseHeader):
        self._ResponseHeader = ResponseHeader

    @property
    def ResponseHeaderCache(self):
        return self._ResponseHeaderCache

    @ResponseHeaderCache.setter
    def ResponseHeaderCache(self, ResponseHeaderCache):
        self._ResponseHeaderCache = ResponseHeaderCache

    @property
    def Seo(self):
        return self._Seo

    @Seo.setter
    def Seo(self, Seo):
        self._Seo = Seo

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def StatusCodeCache(self):
        return self._StatusCodeCache

    @StatusCodeCache.setter
    def StatusCodeCache(self, StatusCodeCache):
        self._StatusCodeCache = StatusCodeCache

    @property
    def VideoSeek(self):
        return self._VideoSeek

    @VideoSeek.setter
    def VideoSeek(self, VideoSeek):
        self._VideoSeek = VideoSeek

    @property
    def AwsPrivateAccess(self):
        return self._AwsPrivateAccess

    @AwsPrivateAccess.setter
    def AwsPrivateAccess(self, AwsPrivateAccess):
        self._AwsPrivateAccess = AwsPrivateAccess

    @property
    def OssPrivateAccess(self):
        return self._OssPrivateAccess

    @OssPrivateAccess.setter
    def OssPrivateAccess(self, OssPrivateAccess):
        self._OssPrivateAccess = OssPrivateAccess

    @property
    def HwPrivateAccess(self):
        return self._HwPrivateAccess

    @HwPrivateAccess.setter
    def HwPrivateAccess(self, HwPrivateAccess):
        self._HwPrivateAccess = HwPrivateAccess

    @property
    def QnPrivateAccess(self):
        return self._QnPrivateAccess

    @QnPrivateAccess.setter
    def QnPrivateAccess(self, QnPrivateAccess):
        self._QnPrivateAccess = QnPrivateAccess


    def _deserialize(self, params):
        if params.get("Authentication") is not None:
            self._Authentication = Authentication()
            self._Authentication._deserialize(params.get("Authentication"))
        if params.get("BandwidthAlert") is not None:
            self._BandwidthAlert = BandwidthAlert()
            self._BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("Cache") is not None:
            self._Cache = Cache()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Compression") is not None:
            self._Compression = Compression()
            self._Compression._deserialize(params.get("Compression"))
        if params.get("DownstreamCapping") is not None:
            self._DownstreamCapping = DownstreamCapping()
            self._DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("ErrorPage") is not None:
            self._ErrorPage = ErrorPage()
            self._ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("FollowRedirect") is not None:
            self._FollowRedirect = FollowRedirect()
            self._FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirect()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        if params.get("IpFilter") is not None:
            self._IpFilter = IpFilter()
            self._IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self._IpFreqLimit = IpFreqLimit()
            self._IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("MaxAge") is not None:
            self._MaxAge = MaxAge()
            self._MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        if params.get("OriginPullOptimization") is not None:
            self._OriginPullOptimization = OriginPullOptimization()
            self._OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("RangeOriginPull") is not None:
            self._RangeOriginPull = RangeOriginPull()
            self._RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("Referer") is not None:
            self._Referer = Referer()
            self._Referer._deserialize(params.get("Referer"))
        if params.get("RequestHeader") is not None:
            self._RequestHeader = RequestHeader()
            self._RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self._ResponseHeader = ResponseHeader()
            self._ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("ResponseHeaderCache") is not None:
            self._ResponseHeaderCache = ResponseHeaderCache()
            self._ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("Seo") is not None:
            self._Seo = Seo()
            self._Seo._deserialize(params.get("Seo"))
        self._ServiceType = params.get("ServiceType")
        if params.get("StatusCodeCache") is not None:
            self._StatusCodeCache = StatusCodeCache()
            self._StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("VideoSeek") is not None:
            self._VideoSeek = VideoSeek()
            self._VideoSeek._deserialize(params.get("VideoSeek"))
        if params.get("AwsPrivateAccess") is not None:
            self._AwsPrivateAccess = AwsPrivateAccess()
            self._AwsPrivateAccess._deserialize(params.get("AwsPrivateAccess"))
        if params.get("OssPrivateAccess") is not None:
            self._OssPrivateAccess = OssPrivateAccess()
            self._OssPrivateAccess._deserialize(params.get("OssPrivateAccess"))
        if params.get("HwPrivateAccess") is not None:
            self._HwPrivateAccess = HwPrivateAccess()
            self._HwPrivateAccess._deserialize(params.get("HwPrivateAccess"))
        if params.get("QnPrivateAccess") is not None:
            self._QnPrivateAccess = QnPrivateAccess()
            self._QnPrivateAccess._deserialize(params.get("QnPrivateAccess"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageClsTopicDomainsRequest(AbstractModel):
    """ManageClsTopicDomains request structure.

    """

    def __init__(self):
        r"""
        :param _LogsetId: Logset ID
        :type LogsetId: str
        :param _TopicId: Log topic ID
        :type TopicId: str
        :param _Channel: Specifies whether to access CDN or ECDN. Valid values: `cdn` (default) and `ecdn`.
        :type Channel: str
        :param _DomainAreaConfigs: Domain name region configuration. Note: if this field is empty, it means to unbind all domain names from the corresponding topic
        :type DomainAreaConfigs: list of DomainAreaConfig
        """
        self._LogsetId = None
        self._TopicId = None
        self._Channel = None
        self._DomainAreaConfigs = None

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def DomainAreaConfigs(self):
        return self._DomainAreaConfigs

    @DomainAreaConfigs.setter
    def DomainAreaConfigs(self, DomainAreaConfigs):
        self._DomainAreaConfigs = DomainAreaConfigs


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        self._Channel = params.get("Channel")
        if params.get("DomainAreaConfigs") is not None:
            self._DomainAreaConfigs = []
            for item in params.get("DomainAreaConfigs"):
                obj = DomainAreaConfig()
                obj._deserialize(item)
                self._DomainAreaConfigs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageClsTopicDomainsResponse(AbstractModel):
    """ManageClsTopicDomains response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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


class MapInfo(AbstractModel):
    """Mapping between a name and an ID

    """

    def __init__(self):
        r"""
        :param _Id: Object ID
        :type Id: int
        :param _Name: Object name
        :type Name: str
        """
        self._Id = None
        self._Name = None

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


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaxAge(AbstractModel):
    """Browser cache rule configuration, which is used to set the default value of `MaxAge` and is disabled by default.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable browser caching. Values:
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        :param _MaxAgeRules: MaxAge rule
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MaxAgeRules: list of MaxAgeRule
        :param _MaxAgeCodeRule: MaxAge status code
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MaxAgeCodeRule: :class:`tencentcloud.cdn.v20180606.models.MaxAgeCodeRule`
        """
        self._Switch = None
        self._MaxAgeRules = None
        self._MaxAgeCodeRule = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def MaxAgeRules(self):
        return self._MaxAgeRules

    @MaxAgeRules.setter
    def MaxAgeRules(self, MaxAgeRules):
        self._MaxAgeRules = MaxAgeRules

    @property
    def MaxAgeCodeRule(self):
        return self._MaxAgeCodeRule

    @MaxAgeCodeRule.setter
    def MaxAgeCodeRule(self, MaxAgeCodeRule):
        self._MaxAgeCodeRule = MaxAgeCodeRule


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("MaxAgeRules") is not None:
            self._MaxAgeRules = []
            for item in params.get("MaxAgeRules"):
                obj = MaxAgeRule()
                obj._deserialize(item)
                self._MaxAgeRules.append(obj)
        if params.get("MaxAgeCodeRule") is not None:
            self._MaxAgeCodeRule = MaxAgeCodeRule()
            self._MaxAgeCodeRule._deserialize(params.get("MaxAgeCodeRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaxAgeCodeRule(AbstractModel):
    """MaxAge status code

    """

    def __init__(self):
        r"""
        :param _Action: Action to execute.
`clear`: Clear the cache-control header.
        :type Action: str
        :param _StatusCodes: Specifies the HTTP status code in the range 400-599.
        :type StatusCodes: list of str
        """
        self._Action = None
        self._StatusCodes = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def StatusCodes(self):
        return self._StatusCodes

    @StatusCodes.setter
    def StatusCodes(self, StatusCodes):
        self._StatusCodes = StatusCodes


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._StatusCodes = params.get("StatusCodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaxAgeRule(AbstractModel):
    """MaxAge rules configuration

    """

    def __init__(self):
        r"""
        :param _MaxAgeType: Rule types:
`all`: effective for all files.
`file`: effective for specified file suffixes.
`directory`: effective for specified paths.
`path`: effective for specified absolute paths.
`index`: effective for specified homepages.
        :type MaxAgeType: str
        :param _MaxAgeContents: Content for each `MaxAgeType`:
For `all`, enter a wildcard `*`.
For `file`, enter the suffix, e.g., `jpg` or `txt`.
For `directory`, enter the path, e.g., `/xxx/test/`.
For `path`, enter the absolute path, e.g., `/xxx/test.html`.
For `index`, enter a forward slash `/`.
Note: The rule `all` cannot be deleted. It follows origin by default and can be modified.
        :type MaxAgeContents: list of str
        :param _MaxAgeTime: MaxAge time (in seconds)
Note: The value `0` means not to cache.
        :type MaxAgeTime: int
        :param _FollowOrigin: Whether to follow the origin server. Valid values: `on` and `off`. If it's on, `MaxAgeTime` is ignored.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FollowOrigin: str
        """
        self._MaxAgeType = None
        self._MaxAgeContents = None
        self._MaxAgeTime = None
        self._FollowOrigin = None

    @property
    def MaxAgeType(self):
        return self._MaxAgeType

    @MaxAgeType.setter
    def MaxAgeType(self, MaxAgeType):
        self._MaxAgeType = MaxAgeType

    @property
    def MaxAgeContents(self):
        return self._MaxAgeContents

    @MaxAgeContents.setter
    def MaxAgeContents(self, MaxAgeContents):
        self._MaxAgeContents = MaxAgeContents

    @property
    def MaxAgeTime(self):
        return self._MaxAgeTime

    @MaxAgeTime.setter
    def MaxAgeTime(self, MaxAgeTime):
        self._MaxAgeTime = MaxAgeTime

    @property
    def FollowOrigin(self):
        return self._FollowOrigin

    @FollowOrigin.setter
    def FollowOrigin(self, FollowOrigin):
        self._FollowOrigin = FollowOrigin


    def _deserialize(self, params):
        self._MaxAgeType = params.get("MaxAgeType")
        self._MaxAgeContents = params.get("MaxAgeContents")
        self._MaxAgeTime = params.get("MaxAgeTime")
        self._FollowOrigin = params.get("FollowOrigin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainConfigRequest(AbstractModel):
    """ModifyDomainConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: The domain name.
        :type Domain: str
        :param _Route: Name of the configuration parameter.
        :type Route: str
        :param _Value: Value of the configuration parameter. This field is serialized to a JSON string {key:value}, where **key** is fixed to `update`.
        :type Value: str
        """
        self._Domain = None
        self._Route = None
        self._Value = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Route(self):
        return self._Route

    @Route.setter
    def Route(self, Route):
        self._Route = Route

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Route = params.get("Route")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainConfigResponse(AbstractModel):
    """ModifyDomainConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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


class OfflineCache(AbstractModel):
    """Offline cache feature status switch.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable offline caching. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Origin(AbstractModel):
    """Complex origin server configurations. The following configurations are supported:
    + Origin server specified as a single domain name
    + Origin server specified as multiple IPs. Supported port range: 1-65535; Supported weight range: 1-100. Format: IP:Port:Weight.
    + Origin-pull domain name configuration
    + Cloud Object Storage (COS) specified as origin server
    + Hot backup origin server specified as a single domain name
    + Hot backup origin server specified as multiple IPs. Supported port range: 1-65535. Weight configuration is not supported.
    + Hot backup origin server origin-pull domain name configuration

    """

    def __init__(self):
        r"""
        :param _Origins: List of primary origin servers
<font color=red>When modifying the origins, you need to specify `OriginType`.</font>
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Origins: list of str
        :param _OriginType: Primary origin server type
<font color=red>This field is used together with `Origins`.</font>
Input:
`domain`: Domain name
`domainv6`: IPv6 domain name
`cos`: COS bucket address
`third_party`: Third-party object storage origin
`igtm`: IGTM origin
`ip`: IP address
`ipv6`: One IPv6 address
`ip_ipv6`: Multiple IPv4 addresses and one IPv6 address
`ip_domain`: IP addresses and domain names (only available to beta users)
`ip_domainv6`: Multiple IPv4 addresses and one IPv6 domain name
`ipv6_domain`: Multiple IPv6 addresses and one domain name
`ipv6_domainv6`: Multiple IPv6 addresses and one IPv6 domain name
`domain_domainv6`: Multiple IPv4 domain names and one IPv6 domain name
`ip_ipv6_domain`: Multiple IPv4 and IPv6 addresses and one domain name
`ip_ipv6_domainv6`: Multiple IPv4 and IPv6 addresses and one IPv6 domain name
`ip_domain_domainv6`: Multiple IPv4 addresses and IPv4 domain names and one IPv6 domain name
`ipv6_domain_domainv6`: Multiple IPv4 domain names and IPv6 addresses and one IPv6 domain name
`ip_ipv6_domain_domainv6`: Multiple IPv4 and IPv6 addresses and IPv4 domain names and one IPv6 domain name
Output:
`image`: Cloud Infinite origin
`ftp`: FTP origin (disused)
When modifying `Origins`, you need to specify `OriginType`.
The IPv6 feature is now only available to beta users. Submit a ticket if you need it.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type OriginType: str
        :param _ServerName: Origin-pull host header.
<font color=red>This field is required when `OriginType=cos/third-party`.</font>
If not specified, this field defaults to the acceleration domain name.
For a wildcard domain name, the sub-domain name during the access is used by default.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ServerName: str
        :param _CosPrivateAccess: When OriginType is COS, you can specify if access to private buckets is allowed.
Note: To enable this configuration, you need to first grant CDN access to the private bucket. Values: `on` and `off`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CosPrivateAccess: str
        :param _OriginPullProtocol: Origin-pull protocol configuration
http: forced HTTP origin-pull
follow: protocol follow origin-pull
https: forced HTTPS origin-pull. This only supports origin server port 443 for origin-pull.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginPullProtocol: str
        :param _BackupOrigins: List of secondary origin servers
<font color=red>This field is used together with `BackupOriginType`.</font>
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type BackupOrigins: list of str
        :param _BackupOriginType: Secondary origin type
<font color=red>This field is used together with `BackupOrigins`.</font>
Values:
`domain`: Domain name
`ip`: IP address
The following secondary origin types are only available to beta users. Submit a ticket to use it.
`ipv6_domain`: Multiple IPv6 addresses and one domain name
`ip_ipv6`: Multiple IPv4 addresses and one IPv6 address
`ipv6_domain`: Multiple IPv6 addresses and one domain name
`ip_ipv6_domain`: Multiple IPv4 and IPv6 addresses and one domain name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type BackupOriginType: str
        :param _BackupServerName: Host header used when accessing the backup origin server. If it is left empty, the `ServerName` of primary origin server will be used by default.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type BackupServerName: str
        :param _BasePath: Origin-pull path
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type BasePath: str
        :param _PathRules: Origin-pull path rewriting configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PathRules: list of PathRule
        :param _PathBasedOrigin: Path-based origin-pull configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PathBasedOrigin: list of PathBasedOriginRule
        :param _Sni: HTTPS origin-pull SNI
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Sni: :class:`tencentcloud.cdn.v20180606.models.OriginSni`
        :param _AdvanceHttps: HTTPS advanced origin-pull configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AdvanceHttps: :class:`tencentcloud.cdn.v20180606.models.AdvanceHttps`
        :param _OriginCompany: Third-party object storage service vendor
<font color=red>This field is required when `OriginType=third-party`.</font>
Values:
`aws_s3`: AWS S3
`ali_oss`: Alibaba Cloud OSS
`hw_obs`: Huawei Cloud OBS
`Qiniu_kodo`: Qiniu Kodo
`Others`: Other object storage service vendors. Only AWS signature-compatible object storage services are supported, such as Tencent Cloud COS for Finance Zone.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type OriginCompany: str
        """
        self._Origins = None
        self._OriginType = None
        self._ServerName = None
        self._CosPrivateAccess = None
        self._OriginPullProtocol = None
        self._BackupOrigins = None
        self._BackupOriginType = None
        self._BackupServerName = None
        self._BasePath = None
        self._PathRules = None
        self._PathBasedOrigin = None
        self._Sni = None
        self._AdvanceHttps = None
        self._OriginCompany = None

    @property
    def Origins(self):
        return self._Origins

    @Origins.setter
    def Origins(self, Origins):
        self._Origins = Origins

    @property
    def OriginType(self):
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def CosPrivateAccess(self):
        return self._CosPrivateAccess

    @CosPrivateAccess.setter
    def CosPrivateAccess(self, CosPrivateAccess):
        self._CosPrivateAccess = CosPrivateAccess

    @property
    def OriginPullProtocol(self):
        return self._OriginPullProtocol

    @OriginPullProtocol.setter
    def OriginPullProtocol(self, OriginPullProtocol):
        self._OriginPullProtocol = OriginPullProtocol

    @property
    def BackupOrigins(self):
        return self._BackupOrigins

    @BackupOrigins.setter
    def BackupOrigins(self, BackupOrigins):
        self._BackupOrigins = BackupOrigins

    @property
    def BackupOriginType(self):
        return self._BackupOriginType

    @BackupOriginType.setter
    def BackupOriginType(self, BackupOriginType):
        self._BackupOriginType = BackupOriginType

    @property
    def BackupServerName(self):
        return self._BackupServerName

    @BackupServerName.setter
    def BackupServerName(self, BackupServerName):
        self._BackupServerName = BackupServerName

    @property
    def BasePath(self):
        return self._BasePath

    @BasePath.setter
    def BasePath(self, BasePath):
        self._BasePath = BasePath

    @property
    def PathRules(self):
        return self._PathRules

    @PathRules.setter
    def PathRules(self, PathRules):
        self._PathRules = PathRules

    @property
    def PathBasedOrigin(self):
        return self._PathBasedOrigin

    @PathBasedOrigin.setter
    def PathBasedOrigin(self, PathBasedOrigin):
        self._PathBasedOrigin = PathBasedOrigin

    @property
    def Sni(self):
        return self._Sni

    @Sni.setter
    def Sni(self, Sni):
        self._Sni = Sni

    @property
    def AdvanceHttps(self):
        return self._AdvanceHttps

    @AdvanceHttps.setter
    def AdvanceHttps(self, AdvanceHttps):
        self._AdvanceHttps = AdvanceHttps

    @property
    def OriginCompany(self):
        return self._OriginCompany

    @OriginCompany.setter
    def OriginCompany(self, OriginCompany):
        self._OriginCompany = OriginCompany


    def _deserialize(self, params):
        self._Origins = params.get("Origins")
        self._OriginType = params.get("OriginType")
        self._ServerName = params.get("ServerName")
        self._CosPrivateAccess = params.get("CosPrivateAccess")
        self._OriginPullProtocol = params.get("OriginPullProtocol")
        self._BackupOrigins = params.get("BackupOrigins")
        self._BackupOriginType = params.get("BackupOriginType")
        self._BackupServerName = params.get("BackupServerName")
        self._BasePath = params.get("BasePath")
        if params.get("PathRules") is not None:
            self._PathRules = []
            for item in params.get("PathRules"):
                obj = PathRule()
                obj._deserialize(item)
                self._PathRules.append(obj)
        if params.get("PathBasedOrigin") is not None:
            self._PathBasedOrigin = []
            for item in params.get("PathBasedOrigin"):
                obj = PathBasedOriginRule()
                obj._deserialize(item)
                self._PathBasedOrigin.append(obj)
        if params.get("Sni") is not None:
            self._Sni = OriginSni()
            self._Sni._deserialize(params.get("Sni"))
        if params.get("AdvanceHttps") is not None:
            self._AdvanceHttps = AdvanceHttps()
            self._AdvanceHttps._deserialize(params.get("AdvanceHttps"))
        self._OriginCompany = params.get("OriginCompany")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginAuthentication(AbstractModel):
    """Origin-pull authentication advanced configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable advanced origin-pull authentication. Values:
`on`: Enable
`off`: Disable

Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        :param _TypeA: Authentication type configuration A
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TypeA: :class:`tencentcloud.cdn.v20180606.models.OriginAuthenticationTypeA`
        """
        self._Switch = None
        self._TypeA = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def TypeA(self):
        return self._TypeA

    @TypeA.setter
    def TypeA(self, TypeA):
        self._TypeA = TypeA


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("TypeA") is not None:
            self._TypeA = OriginAuthenticationTypeA()
            self._TypeA._deserialize(params.get("TypeA"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginAuthenticationTypeA(AbstractModel):
    """Origin-pull authentication advanced configuration TypeA

    """

    def __init__(self):
        r"""
        :param _SecretKey: Key used for signature calculation, allowing 6 to 32 bytes of letters and digits.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SecretKey: str
        """
        self._SecretKey = None

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey


    def _deserialize(self, params):
        self._SecretKey = params.get("SecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginCombine(AbstractModel):
    """Merging pull requests configuration item

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable origin-pull merge. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginIp(AbstractModel):
    """IP information of CDN intermediate nodes

    """

    def __init__(self):
        r"""
        :param _Ip: Intermediate IP range/intermediate IP. The IP range information is returned by default.
        :type Ip: str
        """
        self._Ip = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginPullOptimization(AbstractModel):
    """(Disused) Cross-border origin-pull optimization

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable cross-MLC-border origin-pull optimization. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _OptimizationType: Cross-border types
OVToCN: origin-pull from outside mainland China to inside mainland China
CNToOV: origin-pull from inside mainland China to outside mainland China
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OptimizationType: str
        """
        self._Switch = None
        self._OptimizationType = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def OptimizationType(self):
        return self._OptimizationType

    @OptimizationType.setter
    def OptimizationType(self, OptimizationType):
        self._OptimizationType = OptimizationType


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._OptimizationType = params.get("OptimizationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginPullTimeout(AbstractModel):
    """Origin-pull timeout configuration

    """

    def __init__(self):
        r"""
        :param _ConnectTimeout: The origin-pull connection timeout (in seconds). Valid range: 5-60.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ConnectTimeout: int
        :param _ReceiveTimeout: The origin-pull receipt timeout (in seconds). Valid range: 10-300.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ReceiveTimeout: int
        """
        self._ConnectTimeout = None
        self._ReceiveTimeout = None

    @property
    def ConnectTimeout(self):
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def ReceiveTimeout(self):
        return self._ReceiveTimeout

    @ReceiveTimeout.setter
    def ReceiveTimeout(self, ReceiveTimeout):
        self._ReceiveTimeout = ReceiveTimeout


    def _deserialize(self, params):
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._ReceiveTimeout = params.get("ReceiveTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginSni(AbstractModel):
    """HTTPS origin-pull SNI

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable HTTPS origin-pull SNI. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _ServerName: Origin-pull domain name.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ServerName: str
        """
        self._Switch = None
        self._ServerName = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._ServerName = params.get("ServerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OssPrivateAccess(AbstractModel):
    """Access authentication configuration for OSS origin

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable OSS origin-pull authentication. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _AccessKey: Access ID.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AccessKey: str
        :param _SecretKey: Key.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SecretKey: str
        :param _Region: Region
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Region: str
        :param _Bucket: BucketName
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Bucket: str
        """
        self._Switch = None
        self._AccessKey = None
        self._SecretKey = None
        self._Region = None
        self._Bucket = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def AccessKey(self):
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

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


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OthersPrivateAccess(AbstractModel):
    """Origin-pull authentication for other origins

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable origin-pull authentication for other object storage origins. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _AccessKey: Access ID.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AccessKey: str
        :param _SecretKey: Key.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SecretKey: str
        :param _Region: Region.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Region: str
        :param _Bucket: Bucket name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Bucket: str
        """
        self._Switch = None
        self._AccessKey = None
        self._SecretKey = None
        self._Region = None
        self._Bucket = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def AccessKey(self):
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

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


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OverseaConfig(AbstractModel):
    """Specific configuration for domain names outside the Chinese mainland. The `UpdateDomainConfig` API only supports modification of some region configurations. A list of differences that may exist for older configurations will be provided for a compatibility check. The supported configuration list is as follows:
    + Authentication
    + BandwidthAlert
    + ErrorPage
    + IpFilter
    + Origin
    + Referer

    """

    def __init__(self):
        r"""
        :param _Authentication: Timestamp hotlink protection configuration.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param _BandwidthAlert: Bandwidth cap configuration.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param _Cache: Cache rule configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param _CacheKey: Cache configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param _Compression: Smart compression configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param _DownstreamCapping: Download speed limit configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param _ErrorPage: Error code redirect configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param _FollowRedirect: 301 and 302 automatic origin-pull follow-redirect configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param _ForceRedirect: Protocol redirect configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param _Https: HTTPS configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param _IpFilter: IP blocklist/allowlist configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param _IpFreqLimit: IP access limit configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param _MaxAge: Browser cache rules configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param _Origin: Origin server configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param _OriginPullOptimization: Cross-border optimization configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param _RangeOriginPull: Range GETs configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param _Referer: Hotlink protection configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param _RequestHeader: Origin-pull request header configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param _ResponseHeader: Origin server response header configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param _ResponseHeaderCache: Follows origin server cache header configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param _Seo: SEO configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param _ServiceType: Domain name service type. Values: `web` (static acceleration); `download` (download acceleration); `media` (streaming media acceleration).
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ServiceType: str
        :param _StatusCodeCache: Status code cache configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param _VideoSeek: Video dragging configuration.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        :param _AwsPrivateAccess: Access authentication for S3 origin
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AwsPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`
        :param _OssPrivateAccess: Access authentication for OSS origin
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type OssPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.OssPrivateAccess`
        :param _HwPrivateAccess: Access authentication for Huawei Cloud OBS origin
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type HwPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.HwPrivateAccess`
        :param _QnPrivateAccess: Access authentication for QiNiu Cloud Kodo origin
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type QnPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.QnPrivateAccess`
        """
        self._Authentication = None
        self._BandwidthAlert = None
        self._Cache = None
        self._CacheKey = None
        self._Compression = None
        self._DownstreamCapping = None
        self._ErrorPage = None
        self._FollowRedirect = None
        self._ForceRedirect = None
        self._Https = None
        self._IpFilter = None
        self._IpFreqLimit = None
        self._MaxAge = None
        self._Origin = None
        self._OriginPullOptimization = None
        self._RangeOriginPull = None
        self._Referer = None
        self._RequestHeader = None
        self._ResponseHeader = None
        self._ResponseHeaderCache = None
        self._Seo = None
        self._ServiceType = None
        self._StatusCodeCache = None
        self._VideoSeek = None
        self._AwsPrivateAccess = None
        self._OssPrivateAccess = None
        self._HwPrivateAccess = None
        self._QnPrivateAccess = None

    @property
    def Authentication(self):
        return self._Authentication

    @Authentication.setter
    def Authentication(self, Authentication):
        self._Authentication = Authentication

    @property
    def BandwidthAlert(self):
        return self._BandwidthAlert

    @BandwidthAlert.setter
    def BandwidthAlert(self, BandwidthAlert):
        self._BandwidthAlert = BandwidthAlert

    @property
    def Cache(self):
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def CacheKey(self):
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def Compression(self):
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def DownstreamCapping(self):
        return self._DownstreamCapping

    @DownstreamCapping.setter
    def DownstreamCapping(self, DownstreamCapping):
        self._DownstreamCapping = DownstreamCapping

    @property
    def ErrorPage(self):
        return self._ErrorPage

    @ErrorPage.setter
    def ErrorPage(self, ErrorPage):
        self._ErrorPage = ErrorPage

    @property
    def FollowRedirect(self):
        return self._FollowRedirect

    @FollowRedirect.setter
    def FollowRedirect(self, FollowRedirect):
        self._FollowRedirect = FollowRedirect

    @property
    def ForceRedirect(self):
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def Https(self):
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def IpFilter(self):
        return self._IpFilter

    @IpFilter.setter
    def IpFilter(self, IpFilter):
        self._IpFilter = IpFilter

    @property
    def IpFreqLimit(self):
        return self._IpFreqLimit

    @IpFreqLimit.setter
    def IpFreqLimit(self, IpFreqLimit):
        self._IpFreqLimit = IpFreqLimit

    @property
    def MaxAge(self):
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def OriginPullOptimization(self):
        return self._OriginPullOptimization

    @OriginPullOptimization.setter
    def OriginPullOptimization(self, OriginPullOptimization):
        self._OriginPullOptimization = OriginPullOptimization

    @property
    def RangeOriginPull(self):
        return self._RangeOriginPull

    @RangeOriginPull.setter
    def RangeOriginPull(self, RangeOriginPull):
        self._RangeOriginPull = RangeOriginPull

    @property
    def Referer(self):
        return self._Referer

    @Referer.setter
    def Referer(self, Referer):
        self._Referer = Referer

    @property
    def RequestHeader(self):
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader

    @property
    def ResponseHeader(self):
        return self._ResponseHeader

    @ResponseHeader.setter
    def ResponseHeader(self, ResponseHeader):
        self._ResponseHeader = ResponseHeader

    @property
    def ResponseHeaderCache(self):
        return self._ResponseHeaderCache

    @ResponseHeaderCache.setter
    def ResponseHeaderCache(self, ResponseHeaderCache):
        self._ResponseHeaderCache = ResponseHeaderCache

    @property
    def Seo(self):
        return self._Seo

    @Seo.setter
    def Seo(self, Seo):
        self._Seo = Seo

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def StatusCodeCache(self):
        return self._StatusCodeCache

    @StatusCodeCache.setter
    def StatusCodeCache(self, StatusCodeCache):
        self._StatusCodeCache = StatusCodeCache

    @property
    def VideoSeek(self):
        return self._VideoSeek

    @VideoSeek.setter
    def VideoSeek(self, VideoSeek):
        self._VideoSeek = VideoSeek

    @property
    def AwsPrivateAccess(self):
        return self._AwsPrivateAccess

    @AwsPrivateAccess.setter
    def AwsPrivateAccess(self, AwsPrivateAccess):
        self._AwsPrivateAccess = AwsPrivateAccess

    @property
    def OssPrivateAccess(self):
        return self._OssPrivateAccess

    @OssPrivateAccess.setter
    def OssPrivateAccess(self, OssPrivateAccess):
        self._OssPrivateAccess = OssPrivateAccess

    @property
    def HwPrivateAccess(self):
        return self._HwPrivateAccess

    @HwPrivateAccess.setter
    def HwPrivateAccess(self, HwPrivateAccess):
        self._HwPrivateAccess = HwPrivateAccess

    @property
    def QnPrivateAccess(self):
        return self._QnPrivateAccess

    @QnPrivateAccess.setter
    def QnPrivateAccess(self, QnPrivateAccess):
        self._QnPrivateAccess = QnPrivateAccess


    def _deserialize(self, params):
        if params.get("Authentication") is not None:
            self._Authentication = Authentication()
            self._Authentication._deserialize(params.get("Authentication"))
        if params.get("BandwidthAlert") is not None:
            self._BandwidthAlert = BandwidthAlert()
            self._BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("Cache") is not None:
            self._Cache = Cache()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Compression") is not None:
            self._Compression = Compression()
            self._Compression._deserialize(params.get("Compression"))
        if params.get("DownstreamCapping") is not None:
            self._DownstreamCapping = DownstreamCapping()
            self._DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("ErrorPage") is not None:
            self._ErrorPage = ErrorPage()
            self._ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("FollowRedirect") is not None:
            self._FollowRedirect = FollowRedirect()
            self._FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirect()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        if params.get("IpFilter") is not None:
            self._IpFilter = IpFilter()
            self._IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self._IpFreqLimit = IpFreqLimit()
            self._IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("MaxAge") is not None:
            self._MaxAge = MaxAge()
            self._MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        if params.get("OriginPullOptimization") is not None:
            self._OriginPullOptimization = OriginPullOptimization()
            self._OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("RangeOriginPull") is not None:
            self._RangeOriginPull = RangeOriginPull()
            self._RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("Referer") is not None:
            self._Referer = Referer()
            self._Referer._deserialize(params.get("Referer"))
        if params.get("RequestHeader") is not None:
            self._RequestHeader = RequestHeader()
            self._RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self._ResponseHeader = ResponseHeader()
            self._ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("ResponseHeaderCache") is not None:
            self._ResponseHeaderCache = ResponseHeaderCache()
            self._ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("Seo") is not None:
            self._Seo = Seo()
            self._Seo._deserialize(params.get("Seo"))
        self._ServiceType = params.get("ServiceType")
        if params.get("StatusCodeCache") is not None:
            self._StatusCodeCache = StatusCodeCache()
            self._StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("VideoSeek") is not None:
            self._VideoSeek = VideoSeek()
            self._VideoSeek._deserialize(params.get("VideoSeek"))
        if params.get("AwsPrivateAccess") is not None:
            self._AwsPrivateAccess = AwsPrivateAccess()
            self._AwsPrivateAccess._deserialize(params.get("AwsPrivateAccess"))
        if params.get("OssPrivateAccess") is not None:
            self._OssPrivateAccess = OssPrivateAccess()
            self._OssPrivateAccess._deserialize(params.get("OssPrivateAccess"))
        if params.get("HwPrivateAccess") is not None:
            self._HwPrivateAccess = HwPrivateAccess()
            self._HwPrivateAccess._deserialize(params.get("HwPrivateAccess"))
        if params.get("QnPrivateAccess") is not None:
            self._QnPrivateAccess = QnPrivateAccess()
            self._QnPrivateAccess._deserialize(params.get("QnPrivateAccess"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PathBasedOriginRule(AbstractModel):
    """Path-based origin-pull rule

    """

    def __init__(self):
        r"""
        :param _RuleType: Rule types:
`file`: Apply to files with the specified suffixes.
`directory`: Apply to specified paths.
`path`: Apply to specified absolute paths.
`index`: Apply to specified homepages.
        :type RuleType: str
        :param _RulePaths: Content for each `RuleType`:
For `file`, enter a suffix, e.g., `jpg` or `txt`.
For `directory`, enter a path, e.g., `/xxx/test/`.
For `path`, enter an absolute path, e.g., `/xxx/test.html`.
For `index`, enter a forward slash `/`.
        :type RulePaths: list of str
        :param _Origin: Origin server list. Domain name and IPv4 addresses are supported.
        :type Origin: list of str
        """
        self._RuleType = None
        self._RulePaths = None
        self._Origin = None

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RulePaths(self):
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._RulePaths = params.get("RulePaths")
        self._Origin = params.get("Origin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PathRule(AbstractModel):
    """Path-based origin-pull configuration rules

    """

    def __init__(self):
        r"""
        :param _Regex: Whether to enable wildcard match (`*`).
`false`: disabled
`true`: enabled
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Regex: bool
        :param _Path: Matched URL. Only URLs are supported, while parameters are not. The exact match is used by default. If wildcard match is enabled, up to 5 wildcards are supported. The URL can contain up to 1,024 characters.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Path: str
        :param _Origin: Origin server when the path matches. COS origin with private read/write is not supported. The default origin server will be used by default when this field is left empty.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Origin: str
        :param _ServerName: Origin server host header when the path matches. The default `ServerName` will be used by default when this field is left empty.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ServerName: str
        :param _OriginArea: Region of the origin server. Valid values: `CN` and `OV`.
`CN`: Within the Chinese mainland
`OV`: Outside the Chinese mainland
Default value: `CN`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type OriginArea: str
        :param _ForwardUri: Origin server URI path when the path matches, starting with `/` and excluding parameters. The path can contain up to 1,024 characters. The wildcards in the match path can be respectively captured using `$1`, `$2`, `$3`, `$4`, and `$5`. Up to 10 values can be captured.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ForwardUri: str
        :param _RequestHeaders: Origin-pull header setting when the path matches.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RequestHeaders: list of HttpHeaderRule
        :param _FullMatch: When `Regex` is `false`, this parameter should be `true`.
`false`: Disabled
`true`: enabled
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FullMatch: bool
        """
        self._Regex = None
        self._Path = None
        self._Origin = None
        self._ServerName = None
        self._OriginArea = None
        self._ForwardUri = None
        self._RequestHeaders = None
        self._FullMatch = None

    @property
    def Regex(self):
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def OriginArea(self):
        return self._OriginArea

    @OriginArea.setter
    def OriginArea(self, OriginArea):
        self._OriginArea = OriginArea

    @property
    def ForwardUri(self):
        return self._ForwardUri

    @ForwardUri.setter
    def ForwardUri(self, ForwardUri):
        self._ForwardUri = ForwardUri

    @property
    def RequestHeaders(self):
        return self._RequestHeaders

    @RequestHeaders.setter
    def RequestHeaders(self, RequestHeaders):
        self._RequestHeaders = RequestHeaders

    @property
    def FullMatch(self):
        return self._FullMatch

    @FullMatch.setter
    def FullMatch(self, FullMatch):
        self._FullMatch = FullMatch


    def _deserialize(self, params):
        self._Regex = params.get("Regex")
        self._Path = params.get("Path")
        self._Origin = params.get("Origin")
        self._ServerName = params.get("ServerName")
        self._OriginArea = params.get("OriginArea")
        self._ForwardUri = params.get("ForwardUri")
        if params.get("RequestHeaders") is not None:
            self._RequestHeaders = []
            for item in params.get("RequestHeaders"):
                obj = HttpHeaderRule()
                obj._deserialize(item)
                self._RequestHeaders.append(obj)
        self._FullMatch = params.get("FullMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostSize(AbstractModel):
    """Maximum size of the file uploaded for streaming via a POST request

    """

    def __init__(self):
        r"""
        :param _Switch: Maximum size of the file uploaded for streaming via a POST request. Values:
`on`: Enable. When enabled, it is set to 32 MB by default.
`off`: Disable

        :type Switch: str
        :param _MaxSize: Maximum size. Value range: 1 MB to 200 MB.
        :type MaxSize: int
        """
        self._Switch = None
        self._MaxSize = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurgePathCacheRequest(AbstractModel):
    """PurgePathCache request structure.

    """

    def __init__(self):
        r"""
        :param _Paths: List of directories. The protocol header such as "http://" or "https://" needs to be included.
        :type Paths: list of str
        :param _FlushType: Purge type:
`flush`: purges updated resources
`delete`: purges all resources
        :type FlushType: str
        :param _UrlEncode: Whether to encode Chinese characters before purge.
        :type UrlEncode: bool
        :param _Area: Region to purge
The acceleration region of the acceleration domain name will be purged if this parameter is not passed in.
If `mainland` is passed in, only the content cached on nodes in the Chinese mainland will be purged.
If `overseas` is passed in, only the content cached on nodes outside the Chinese mainland will be purged.
The specified region to purge should match the domain name’s acceleration region.
        :type Area: str
        """
        self._Paths = None
        self._FlushType = None
        self._UrlEncode = None
        self._Area = None

    @property
    def Paths(self):
        return self._Paths

    @Paths.setter
    def Paths(self, Paths):
        self._Paths = Paths

    @property
    def FlushType(self):
        return self._FlushType

    @FlushType.setter
    def FlushType(self, FlushType):
        self._FlushType = FlushType

    @property
    def UrlEncode(self):
        return self._UrlEncode

    @UrlEncode.setter
    def UrlEncode(self, UrlEncode):
        self._UrlEncode = UrlEncode

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._Paths = params.get("Paths")
        self._FlushType = params.get("FlushType")
        self._UrlEncode = params.get("UrlEncode")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurgePathCacheResponse(AbstractModel):
    """PurgePathCache response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Purge task ID. Directories submitted in one request share a task ID.
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class PurgeTask(AbstractModel):
    """Purge task details.

    """

    def __init__(self):
        r"""
        :param _TaskId: Purge task ID
        :type TaskId: str
        :param _Url: Purged URL
        :type Url: str
        :param _Status: Purge task status
`fail`: Purge failed
`done`: Purge succeeded
`process`: Purge in progress
        :type Status: str
        :param _PurgeType: Purge type
`url`: URL purge
`path`: directory purge
        :type PurgeType: str
        :param _FlushType: Purge method
`flush`: purges updated resources; this type is available only for directory purges
`delete`: Purge all resources
        :type FlushType: str
        :param _CreateTime: Purge task submission time
        :type CreateTime: str
        """
        self._TaskId = None
        self._Url = None
        self._Status = None
        self._PurgeType = None
        self._FlushType = None
        self._CreateTime = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PurgeType(self):
        return self._PurgeType

    @PurgeType.setter
    def PurgeType(self, PurgeType):
        self._PurgeType = PurgeType

    @property
    def FlushType(self):
        return self._FlushType

    @FlushType.setter
    def FlushType(self, FlushType):
        self._FlushType = FlushType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Url = params.get("Url")
        self._Status = params.get("Status")
        self._PurgeType = params.get("PurgeType")
        self._FlushType = params.get("FlushType")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurgeUrlsCacheRequest(AbstractModel):
    """PurgeUrlsCache request structure.

    """

    def __init__(self):
        r"""
        :param _Urls: List of URLs. The protocol header such as "http://" or "https://" needs to be included.
        :type Urls: list of str
        :param _Area: Purging region
The acceleration region of the acceleration domain name will be purged if this parameter is not passed in.
If `mainland` is passed in, only the content cached on nodes in the Chinese mainland will be purged.
If `overseas` is passed in, only the content cached on nodes outside the Chinese mainland will be purged.
The specified purging region should match the domain name acceleration region.
        :type Area: str
        :param _UrlEncode: Whether to encode Chinese characters for purge
        :type UrlEncode: bool
        """
        self._Urls = None
        self._Area = None
        self._UrlEncode = None

    @property
    def Urls(self):
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def UrlEncode(self):
        return self._UrlEncode

    @UrlEncode.setter
    def UrlEncode(self, UrlEncode):
        self._UrlEncode = UrlEncode


    def _deserialize(self, params):
        self._Urls = params.get("Urls")
        self._Area = params.get("Area")
        self._UrlEncode = params.get("UrlEncode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurgeUrlsCacheResponse(AbstractModel):
    """PurgeUrlsCache response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Purge task ID. URLs submitted in one request share a task ID.
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class PushTask(AbstractModel):
    """Prefetch task details.

    """

    def __init__(self):
        r"""
        :param _TaskId: Prefetch task ID
        :type TaskId: str
        :param _Url: Prefetched URL
        :type Url: str
        :param _Status: Prefetch task status
`fail`: Prefetch failed
`done`: Prefetch succeeded
`process`: Prefetch in progress
`invalid`: Invalid prefetch with 4XX/5XX status code returned from the origin server
        :type Status: str
        :param _Percent: Prefetch progress in percentage
        :type Percent: int
        :param _CreateTime: Prefetch task submission time
        :type CreateTime: str
        :param _Area: Prefetch region
`mainland`: Within the Chinese mainland
`overseas`: Outside the Chinese mainland
`global`: Globe
        :type Area: str
        :param _UpdateTime: Prefetch task update time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UpdateTime: str
        """
        self._TaskId = None
        self._Url = None
        self._Status = None
        self._Percent = None
        self._CreateTime = None
        self._Area = None
        self._UpdateTime = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Url = params.get("Url")
        self._Status = params.get("Status")
        self._Percent = params.get("Percent")
        self._CreateTime = params.get("CreateTime")
        self._Area = params.get("Area")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushUrlsCacheRequest(AbstractModel):
    """PushUrlsCache request structure.

    """

    def __init__(self):
        r"""
        :param _Urls: List of URLs. The protocol header such as "http://" or "https://" needs to be included.
        :type Urls: list of str
        :param _UserAgent: Specifies the User-Agent header of an HTTP prefetch request when it is forwarded to the origin server
Default value: `TencentCdn`
        :type UserAgent: str
        :param _Area: Destination region for the prefetch
`mainland`: prefetches resources to nodes within Mainland China
`overseas`: prefetches resources to nodes outside Mainland China
`global`: prefetches resources to global nodes
Default value: `mainland`. You can prefetch a URL to nodes in a region provided that CDN service has been enabled for the domain name in the URL in the region.
        :type Area: str
        :param _Layer: By default, prefetch for regions in the Chinese mainland is performed onto the intermediate nodes, while prefetch for regions outside the Chinese mainland is performed onto the edge nodes and the traffic generated will be billed.
If this parameter is `middle` or left empty, prefetch will be performed onto the intermediate node.
        :type Layer: str
        :param _ParseM3U8: Whether to recursively resolve the M3U8 index file and prefetch the TS shards in it.
Notes:
1. This feature requires that the M3U8 index file can be directly requested and obtained.
2. In the M3U8 index file, currently only the TS shards at the first to the third level can be recursively resolved.
3. Prefetching the TS shards obtained through recursive resolution consumes the daily prefetch quota. If the usage exceeds the quota, the feature will be disabled and TS shards will not be prefetched.
        :type ParseM3U8: bool
        :param _DisableRange: Specifies whether to disable Range GETs.
Notes:
This feature is in beta test.
        :type DisableRange: bool
        :param _Headers: Custom HTTP request headers (Up to 20). `Name`: Up to 128 characters. `Value`: Up to 1024 characters.
        :type Headers: list of HTTPHeader
        :param _UrlEncode: Whether to encode the URL
        :type UrlEncode: bool
        """
        self._Urls = None
        self._UserAgent = None
        self._Area = None
        self._Layer = None
        self._ParseM3U8 = None
        self._DisableRange = None
        self._Headers = None
        self._UrlEncode = None

    @property
    def Urls(self):
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls

    @property
    def UserAgent(self):
        return self._UserAgent

    @UserAgent.setter
    def UserAgent(self, UserAgent):
        self._UserAgent = UserAgent

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Layer(self):
        return self._Layer

    @Layer.setter
    def Layer(self, Layer):
        self._Layer = Layer

    @property
    def ParseM3U8(self):
        return self._ParseM3U8

    @ParseM3U8.setter
    def ParseM3U8(self, ParseM3U8):
        self._ParseM3U8 = ParseM3U8

    @property
    def DisableRange(self):
        return self._DisableRange

    @DisableRange.setter
    def DisableRange(self, DisableRange):
        self._DisableRange = DisableRange

    @property
    def Headers(self):
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers

    @property
    def UrlEncode(self):
        return self._UrlEncode

    @UrlEncode.setter
    def UrlEncode(self, UrlEncode):
        self._UrlEncode = UrlEncode


    def _deserialize(self, params):
        self._Urls = params.get("Urls")
        self._UserAgent = params.get("UserAgent")
        self._Area = params.get("Area")
        self._Layer = params.get("Layer")
        self._ParseM3U8 = params.get("ParseM3U8")
        self._DisableRange = params.get("DisableRange")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = HTTPHeader()
                obj._deserialize(item)
                self._Headers.append(obj)
        self._UrlEncode = params.get("UrlEncode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushUrlsCacheResponse(AbstractModel):
    """PushUrlsCache response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: ID of the submitted task
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class QnPrivateAccess(AbstractModel):
    """Access authentication for QiNiu Cloud Kodo origin

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable origin-pull authentication for QiNiu Cloud Kodo. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _AccessKey: Access ID
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AccessKey: str
        :param _SecretKey: Key
        :type SecretKey: str
        """
        self._Switch = None
        self._AccessKey = None
        self._SecretKey = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def AccessKey(self):
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryStringKey(AbstractModel):
    """A part of `CacheKey`

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to include `QueryString` as part of `CacheKey`. Values:
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        :param _Reorder: Whether to sort again
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Reorder: str
        :param _Action: Whether to include URL parameters. Values:
`includeAll`: Include all parameters.
`excludeAll`: Exclude all parameters.
`includeCustom`: Include custom parameters.
`excludeCustom`: Exclude custom parameters.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Action: str
        :param _Value: Array of included/excluded query strings (separated by ';')
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Value: str
        """
        self._Switch = None
        self._Reorder = None
        self._Action = None
        self._Value = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Reorder(self):
        return self._Reorder

    @Reorder.setter
    def Reorder(self, Reorder):
        self._Reorder = Reorder

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Reorder = params.get("Reorder")
        self._Action = params.get("Action")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quic(AbstractModel):
    """QUIC configuration item

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable QUIC. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quota(AbstractModel):
    """Purge/Prefetch available usage and quota

    """

    def __init__(self):
        r"""
        :param _Batch: Quota limit for one batch submission request.
        :type Batch: int
        :param _Total: Daily submission quota limit.
        :type Total: int
        :param _Available: Remaining daily submission quota.
        :type Available: int
        :param _Area: Quota region.
        :type Area: str
        """
        self._Batch = None
        self._Total = None
        self._Available = None
        self._Area = None

    @property
    def Batch(self):
        return self._Batch

    @Batch.setter
    def Batch(self, Batch):
        self._Batch = Batch

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Available(self):
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._Batch = params.get("Batch")
        self._Total = params.get("Total")
        self._Available = params.get("Available")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RangeOriginPull(AbstractModel):
    """Range GETs configuration which is enabled by default

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable Range GETs. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _RangeRules: Range GETs configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RangeRules: list of RangeOriginPullRule
        """
        self._Switch = None
        self._RangeRules = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RangeRules(self):
        return self._RangeRules

    @RangeRules.setter
    def RangeRules(self, RangeRules):
        self._RangeRules = RangeRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("RangeRules") is not None:
            self._RangeRules = []
            for item in params.get("RangeRules"):
                obj = RangeOriginPullRule()
                obj._deserialize(item)
                self._RangeRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RangeOriginPullRule(AbstractModel):
    """Range GETs configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable Range GETs. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _RuleType: Rule types:
`file`: effective for specified file suffixes.
`directory`: effective for specified paths.
`path`: effective for specified absolute paths.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RuleType: str
        :param _RulePaths: Content for each `RuleType`:
For `file`, enter a suffix, e.g., `jpg` or `txt`.
For `directory`, enter a path, e.g., `/xxx/test/`.
For `path`, enter an absolute path, e.g., `/xxx/test.html`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RulePaths: list of str
        """
        self._Switch = None
        self._RuleType = None
        self._RulePaths = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RulePaths(self):
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._RuleType = params.get("RuleType")
        self._RulePaths = params.get("RulePaths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedirectConfig(AbstractModel):
    """Host header for 302 redirects

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable the custom origin-pull request to follow the host when a 302 code is returned. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _FollowRedirectHost: The custom host header that is sent when the primary origin server follows 302 redirects
        :type FollowRedirectHost: str
        :param _FollowRedirectBackupHost: The custom host header that is sent when the secondary origin server follows 302 redirects
        :type FollowRedirectBackupHost: str
        """
        self._Switch = None
        self._FollowRedirectHost = None
        self._FollowRedirectBackupHost = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def FollowRedirectHost(self):
        return self._FollowRedirectHost

    @FollowRedirectHost.setter
    def FollowRedirectHost(self, FollowRedirectHost):
        self._FollowRedirectHost = FollowRedirectHost

    @property
    def FollowRedirectBackupHost(self):
        return self._FollowRedirectBackupHost

    @FollowRedirectBackupHost.setter
    def FollowRedirectBackupHost(self, FollowRedirectBackupHost):
        self._FollowRedirectBackupHost = FollowRedirectBackupHost


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._FollowRedirectHost = params.get("FollowRedirectHost")
        self._FollowRedirectBackupHost = params.get("FollowRedirectBackupHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Referer(AbstractModel):
    """Referer blacklist/whitelist configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable referer blocklist/allowlist. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _RefererRules: Referer blacklist/whitelist configuration rule
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RefererRules: list of RefererRule
        """
        self._Switch = None
        self._RefererRules = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RefererRules(self):
        return self._RefererRules

    @RefererRules.setter
    def RefererRules(self, RefererRules):
        self._RefererRules = RefererRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("RefererRules") is not None:
            self._RefererRules = []
            for item in params.get("RefererRules"):
                obj = RefererRule()
                obj._deserialize(item)
                self._RefererRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefererRule(AbstractModel):
    """Referer blacklist/whitelist configuration rules, which is effective for specific resources.

    """

    def __init__(self):
        r"""
        :param _RuleType: Rule types:
`all`: Apply to all files.
`file`: Apply to files with the specified suffixes.
`directory`: Apply to specified paths.
`path`: Apply to specified absolute paths.
        :type RuleType: str
        :param _RulePaths: Content for each `RuleType`:
For `all`, enter a wildcard `*`.
For `file`, enter a suffix, e.g., `jpg` or `txt`.
For `directory`, enter a path, e.g., `/xxx/test/`.
For `path`, enter an absolute path, e.g., `/xxx/test.html`.
        :type RulePaths: list of str
        :param _RefererType: Referer configuration types
`whitelist`: Allowlist
`blacklist`: Blocklist
        :type RefererType: str
        :param _Referers: Referer content list
        :type Referers: list of str
        :param _AllowEmpty: Whether to allow empty referer
`true`: Allow empty referer when `RefererType = whitelist`.
`false`: Reject empty refer when `RefererType = blacklist`.
        :type AllowEmpty: bool
        """
        self._RuleType = None
        self._RulePaths = None
        self._RefererType = None
        self._Referers = None
        self._AllowEmpty = None

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RulePaths(self):
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths

    @property
    def RefererType(self):
        return self._RefererType

    @RefererType.setter
    def RefererType(self, RefererType):
        self._RefererType = RefererType

    @property
    def Referers(self):
        return self._Referers

    @Referers.setter
    def Referers(self, Referers):
        self._Referers = Referers

    @property
    def AllowEmpty(self):
        return self._AllowEmpty

    @AllowEmpty.setter
    def AllowEmpty(self, AllowEmpty):
        self._AllowEmpty = AllowEmpty


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._RulePaths = params.get("RulePaths")
        self._RefererType = params.get("RefererType")
        self._Referers = params.get("Referers")
        self._AllowEmpty = params.get("AllowEmpty")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionMapRelation(AbstractModel):
    """Association between a region ID and sub-region IDs.

    """

    def __init__(self):
        r"""
        :param _RegionId: Region ID
        :type RegionId: int
        :param _SubRegionIdList: List of sub-region IDs
        :type SubRegionIdList: list of int
        """
        self._RegionId = None
        self._SubRegionIdList = None

    @property
    def RegionId(self):
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def SubRegionIdList(self):
        return self._SubRegionIdList

    @SubRegionIdList.setter
    def SubRegionIdList(self, SubRegionIdList):
        self._SubRegionIdList = SubRegionIdList


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._SubRegionIdList = params.get("SubRegionIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoteAuthentication(AbstractModel):
    """Configuration of remote authentication rules. Setting up multiple rules is supported.
    `RemoteAuthenticationRules` and `Server` cannot be configured at the same time.
    If only `Server` is configured, all parameters of `RemoteAuthenticationRules` will be set to the default values. The default values are described in each configuration parameter.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable remote authentication. Values:
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        :param _RemoteAuthenticationRules: Remote authentication rule configuration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RemoteAuthenticationRules: list of RemoteAuthenticationRule
        :param _Server: Remote authentication server
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Server: str
        """
        self._Switch = None
        self._RemoteAuthenticationRules = None
        self._Server = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RemoteAuthenticationRules(self):
        return self._RemoteAuthenticationRules

    @RemoteAuthenticationRules.setter
    def RemoteAuthenticationRules(self, RemoteAuthenticationRules):
        self._RemoteAuthenticationRules = RemoteAuthenticationRules

    @property
    def Server(self):
        return self._Server

    @Server.setter
    def Server(self, Server):
        self._Server = Server


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("RemoteAuthenticationRules") is not None:
            self._RemoteAuthenticationRules = []
            for item in params.get("RemoteAuthenticationRules"):
                obj = RemoteAuthenticationRule()
                obj._deserialize(item)
                self._RemoteAuthenticationRules.append(obj)
        self._Server = params.get("Server")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoteAuthenticationRule(AbstractModel):
    """Remote authentication rule

    """

    def __init__(self):
        r"""
        :param _Server: Remote authentication server
The server configured in `RemoteAutherntication` is used by default.
        :type Server: str
        :param _AuthMethod: HTTP method used by the remote authentication server. Valid values: `get`, `post`, `head`, and `all`. 
`all`: the remote authentication server follows the client request method.
Default: `all`
        :type AuthMethod: str
        :param _RuleType: Rule types:
`all`: apply to all files
`file`: apply to files with the specified suffixes
`directory`: apply to the specified directories
`path`: apply to the specified absolute paths
Default: `all`.
        :type RuleType: str
        :param _RulePaths: Content for each `RuleType`:
For `all`, enter a wildcard `*`.
For `file`, enter a suffix, e.g., `jpg` or `txt`.
For `directory`, enter a path, e.g., `/xxx/test/`.
For `path`, enter an absolute path, e.g., `/xxx/test.html`.
For `index`, enter a forward slash `/`.
Default: `*`
        :type RulePaths: list of str
        :param _AuthTimeout: Timeout period of the remote authentication server. Unit: ms.
Value range: [1, 30,000]
Default: 20000
        :type AuthTimeout: int
        :param _AuthTimeoutAction: Whether to deny or allow the request when the remote authentication server is timed out:
`RETURN_200`: the request is allowed when the remote authentication server is timed out.
`RETURN_403`: the request is denied when the remote authentication server is timed out.
Default: `RETURN_200`
        :type AuthTimeoutAction: str
        """
        self._Server = None
        self._AuthMethod = None
        self._RuleType = None
        self._RulePaths = None
        self._AuthTimeout = None
        self._AuthTimeoutAction = None

    @property
    def Server(self):
        return self._Server

    @Server.setter
    def Server(self, Server):
        self._Server = Server

    @property
    def AuthMethod(self):
        return self._AuthMethod

    @AuthMethod.setter
    def AuthMethod(self, AuthMethod):
        self._AuthMethod = AuthMethod

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RulePaths(self):
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths

    @property
    def AuthTimeout(self):
        return self._AuthTimeout

    @AuthTimeout.setter
    def AuthTimeout(self, AuthTimeout):
        self._AuthTimeout = AuthTimeout

    @property
    def AuthTimeoutAction(self):
        return self._AuthTimeoutAction

    @AuthTimeoutAction.setter
    def AuthTimeoutAction(self, AuthTimeoutAction):
        self._AuthTimeoutAction = AuthTimeoutAction


    def _deserialize(self, params):
        self._Server = params.get("Server")
        self._AuthMethod = params.get("AuthMethod")
        self._RuleType = params.get("RuleType")
        self._RulePaths = params.get("RulePaths")
        self._AuthTimeout = params.get("AuthTimeout")
        self._AuthTimeoutAction = params.get("AuthTimeoutAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportData(AbstractModel):
    """CDN report data

    """

    def __init__(self):
        r"""
        :param _ResourceId: Project ID/domain name ID.
        :type ResourceId: str
        :param _Resource: Project name/domain name.
        :type Resource: str
        :param _Value: Total traffic/max bandwidth in bytes and bps, respectively.
        :type Value: int
        :param _Percentage: Percentage of individual resource out of all resources.
        :type Percentage: float
        :param _BillingValue: Total billable traffic/max billable bandwidth in bytes and bps, respectively.
        :type BillingValue: int
        :param _BillingPercentage: Percentage of billable amount out of total amount.
        :type BillingPercentage: float
        """
        self._ResourceId = None
        self._Resource = None
        self._Value = None
        self._Percentage = None
        self._BillingValue = None
        self._BillingPercentage = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Percentage(self):
        return self._Percentage

    @Percentage.setter
    def Percentage(self, Percentage):
        self._Percentage = Percentage

    @property
    def BillingValue(self):
        return self._BillingValue

    @BillingValue.setter
    def BillingValue(self, BillingValue):
        self._BillingValue = BillingValue

    @property
    def BillingPercentage(self):
        return self._BillingPercentage

    @BillingPercentage.setter
    def BillingPercentage(self, BillingPercentage):
        self._BillingPercentage = BillingPercentage


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Resource = params.get("Resource")
        self._Value = params.get("Value")
        self._Percentage = params.get("Percentage")
        self._BillingValue = params.get("BillingValue")
        self._BillingPercentage = params.get("BillingPercentage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestHeader(AbstractModel):
    """Custom request header configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable custom request headers. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _HeaderRules: Custom request header configuration rules
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type HeaderRules: list of HttpHeaderPathRule
        """
        self._Switch = None
        self._HeaderRules = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def HeaderRules(self):
        return self._HeaderRules

    @HeaderRules.setter
    def HeaderRules(self, HeaderRules):
        self._HeaderRules = HeaderRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("HeaderRules") is not None:
            self._HeaderRules = []
            for item in params.get("HeaderRules"):
                obj = HttpHeaderPathRule()
                obj._deserialize(item)
                self._HeaderRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceBillingData(AbstractModel):
    """Billing data details

    """

    def __init__(self):
        r"""
        :param _Resource: Resource name, which is classified as follows based on different query filters:
When a domain name is specified: Details of the domain name
`multiDomains`: Aggregated details of multiple domain names
A specific project ID: ID of the specifically queried project
`all`: Details at the account level
        :type Resource: str
        :param _BillingData: Billing data details
        :type BillingData: list of CdnData
        """
        self._Resource = None
        self._BillingData = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def BillingData(self):
        return self._BillingData

    @BillingData.setter
    def BillingData(self, BillingData):
        self._BillingData = BillingData


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        if params.get("BillingData") is not None:
            self._BillingData = []
            for item in params.get("BillingData"):
                obj = CdnData()
                obj._deserialize(item)
                self._BillingData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceData(AbstractModel):
    """This API is used to query an object and its access details.

    """

    def __init__(self):
        r"""
        :param _Resource: Resource name. 
A single domain name: Queries domain name details by a domain name. The details of the domain name will be displayed when the passed parameter `detail` is `true`.
Multiple domain names: Queries domain name details by multiple domain names. The aggregated details of the domain names will be displayed.
Project ID: Queries domain name details by a project ID. The aggregated details of the domain names of the project will be displayed.
`all`: Account-level data, which is aggregated details of all domain names of an account.
        :type Resource: str
        :param _CdnData: Data details of a resource
        :type CdnData: list of CdnData
        """
        self._Resource = None
        self._CdnData = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def CdnData(self):
        return self._CdnData

    @CdnData.setter
    def CdnData(self, CdnData):
        self._CdnData = CdnData


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        if params.get("CdnData") is not None:
            self._CdnData = []
            for item in params.get("CdnData"):
                obj = CdnData()
                obj._deserialize(item)
                self._CdnData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceOriginData(AbstractModel):
    """This API is used to query an object and its origin-pull details.

    """

    def __init__(self):
        r"""
        :param _Resource: Resource name, which is classified as follows based on different query filters:
A specific domain name: Details of the domain name
`multiDomains`: Aggregated details of multiple domain names
Project ID: ID of the specifically queried project
`all`: Details at the account level
        :type Resource: str
        :param _OriginData: Origin-pull data details
        :type OriginData: list of CdnData
        """
        self._Resource = None
        self._OriginData = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def OriginData(self):
        return self._OriginData

    @OriginData.setter
    def OriginData(self, OriginData):
        self._OriginData = OriginData


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        if params.get("OriginData") is not None:
            self._OriginData = []
            for item in params.get("OriginData"):
                obj = CdnData()
                obj._deserialize(item)
                self._OriginData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResponseHeader(AbstractModel):
    """Custom response header configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable custom response headers. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _HeaderRules: Custom response header rules
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type HeaderRules: list of HttpHeaderPathRule
        """
        self._Switch = None
        self._HeaderRules = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def HeaderRules(self):
        return self._HeaderRules

    @HeaderRules.setter
    def HeaderRules(self, HeaderRules):
        self._HeaderRules = HeaderRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("HeaderRules") is not None:
            self._HeaderRules = []
            for item in params.get("HeaderRules"):
                obj = HttpHeaderPathRule()
                obj._deserialize(item)
                self._HeaderRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResponseHeaderCache(AbstractModel):
    """Origin server header cache configuration. This is enabled by default and caches all the header information.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable response header caching. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Revalidate(AbstractModel):
    """Whether to forward to the origin server for verification

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable origin-pull authentication. Values:
`on`: Enable
`off`: Disable

Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        :param _Path: Forwards to the origin server for verification only for specific request path
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Path: str
        """
        self._Switch = None
        self._Path = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleCache(AbstractModel):
    """Path-based cache rule configuration
    The cache expiration time for all files is 30 days by default.
    Static acceleration type domain names .php, .jsp, .asp, and .aspx are not cached by default.

    """

    def __init__(self):
        r"""
        :param _RulePaths: Content for each `CacheType`:
For `all`, enter a wildcard `*`.
For `file`, enter the suffix, e.g., `jpg` or `txt`.
For `directory`, enter the path, e.g., `/xxx/test/`.
For `path`, enter the absolute path, e.g., `/xxx/test.html`.
For `index`, enter a forward slash `/`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RulePaths: list of str
        :param _RuleType: Rule types:
`all`: effective for all files.
`file`: effective for specified file suffixes.
`directory`: effective for specified paths.
`path`: effective for specified absolute paths.
`index`: homepage.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RuleType: str
        :param _CacheConfig: Cache configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CacheConfig: :class:`tencentcloud.cdn.v20180606.models.RuleCacheConfig`
        """
        self._RulePaths = None
        self._RuleType = None
        self._CacheConfig = None

    @property
    def RulePaths(self):
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def CacheConfig(self):
        return self._CacheConfig

    @CacheConfig.setter
    def CacheConfig(self, CacheConfig):
        self._CacheConfig = CacheConfig


    def _deserialize(self, params):
        self._RulePaths = params.get("RulePaths")
        self._RuleType = params.get("RuleType")
        if params.get("CacheConfig") is not None:
            self._CacheConfig = RuleCacheConfig()
            self._CacheConfig._deserialize(params.get("CacheConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleCacheConfig(AbstractModel):
    """Path cache configuration, choose one from the following three cache modes.

    """

    def __init__(self):
        r"""
        :param _Cache: Cache configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.CacheConfigCache`
        :param _NoCache: No cache configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type NoCache: :class:`tencentcloud.cdn.v20180606.models.CacheConfigNoCache`
        :param _FollowOrigin: Follows the origin server configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FollowOrigin: :class:`tencentcloud.cdn.v20180606.models.CacheConfigFollowOrigin`
        """
        self._Cache = None
        self._NoCache = None
        self._FollowOrigin = None

    @property
    def Cache(self):
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def NoCache(self):
        return self._NoCache

    @NoCache.setter
    def NoCache(self, NoCache):
        self._NoCache = NoCache

    @property
    def FollowOrigin(self):
        return self._FollowOrigin

    @FollowOrigin.setter
    def FollowOrigin(self, FollowOrigin):
        self._FollowOrigin = FollowOrigin


    def _deserialize(self, params):
        if params.get("Cache") is not None:
            self._Cache = CacheConfigCache()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("NoCache") is not None:
            self._NoCache = CacheConfigNoCache()
            self._NoCache._deserialize(params.get("NoCache"))
        if params.get("FollowOrigin") is not None:
            self._FollowOrigin = CacheConfigFollowOrigin()
            self._FollowOrigin._deserialize(params.get("FollowOrigin"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleEngine(AbstractModel):
    """Rule engine configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable rule engine. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _Content: Rule
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Content: str
        """
        self._Switch = None
        self._Content = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleQueryString(AbstractModel):
    """Configuration to retain query strings for this path

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to include query string parameters. Values:
`on`: Include `QueryString` as part of `CacheKey`.
`off`: Do not include `QueryString` as part of `CacheKey`.

Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        :param _Action: `includeCustom` will retain partial query strings
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Action: str
        :param _Value: Array of included/excluded query strings (separated by ';')
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Value: str
        """
        self._Switch = None
        self._Action = None
        self._Value = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Action = params.get("Action")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnAclConfig(AbstractModel):
    """SCDN access control

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable SCDN access. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _ScriptData: This field is disused. Please use `AdvancedScriptData` instead.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ScriptData: list of ScdnAclGroup
        :param _ErrorPage: Error page configuration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ScdnErrorPage`
        :param _AdvancedScriptData: ACL rule group, which is required when the access control is on.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AdvancedScriptData: list of AdvancedScdnAclGroup
        """
        self._Switch = None
        self._ScriptData = None
        self._ErrorPage = None
        self._AdvancedScriptData = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def ScriptData(self):
        return self._ScriptData

    @ScriptData.setter
    def ScriptData(self, ScriptData):
        self._ScriptData = ScriptData

    @property
    def ErrorPage(self):
        return self._ErrorPage

    @ErrorPage.setter
    def ErrorPage(self, ErrorPage):
        self._ErrorPage = ErrorPage

    @property
    def AdvancedScriptData(self):
        return self._AdvancedScriptData

    @AdvancedScriptData.setter
    def AdvancedScriptData(self, AdvancedScriptData):
        self._AdvancedScriptData = AdvancedScriptData


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("ScriptData") is not None:
            self._ScriptData = []
            for item in params.get("ScriptData"):
                obj = ScdnAclGroup()
                obj._deserialize(item)
                self._ScriptData.append(obj)
        if params.get("ErrorPage") is not None:
            self._ErrorPage = ScdnErrorPage()
            self._ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("AdvancedScriptData") is not None:
            self._AdvancedScriptData = []
            for item in params.get("AdvancedScriptData"):
                obj = AdvancedScdnAclGroup()
                obj._deserialize(item)
                self._AdvancedScriptData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnAclGroup(AbstractModel):
    """SCDN precise access control configuration

    """

    def __init__(self):
        r"""
        :param _RuleName: Rule name
        :type RuleName: str
        :param _Configure: Specific configurations
        :type Configure: list of ScdnAclRule
        :param _Result: Action. Valid values: `intercept` and `redirect`.
        :type Result: str
        :param _Status: Whether the rule is activated. Valid values: `active` and `inactive`.
        :type Status: str
        :param _ErrorPage: Error page configuration
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ScdnErrorPage`
        """
        self._RuleName = None
        self._Configure = None
        self._Result = None
        self._Status = None
        self._ErrorPage = None

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Configure(self):
        return self._Configure

    @Configure.setter
    def Configure(self, Configure):
        self._Configure = Configure

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorPage(self):
        return self._ErrorPage

    @ErrorPage.setter
    def ErrorPage(self, ErrorPage):
        self._ErrorPage = ErrorPage


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        if params.get("Configure") is not None:
            self._Configure = []
            for item in params.get("Configure"):
                obj = ScdnAclRule()
                obj._deserialize(item)
                self._Configure.append(obj)
        self._Result = params.get("Result")
        self._Status = params.get("Status")
        if params.get("ErrorPage") is not None:
            self._ErrorPage = ScdnErrorPage()
            self._ErrorPage._deserialize(params.get("ErrorPage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnAclRule(AbstractModel):
    """Precise access control match rule

    """

    def __init__(self):
        r"""
        :param _MatchKey: Keyword
        :type MatchKey: str
        :param _LogiOperator: Logical operator. Valid values:
        :type LogiOperator: str
        :param _MatchValue: Matched value
        :type MatchValue: str
        """
        self._MatchKey = None
        self._LogiOperator = None
        self._MatchValue = None

    @property
    def MatchKey(self):
        return self._MatchKey

    @MatchKey.setter
    def MatchKey(self, MatchKey):
        self._MatchKey = MatchKey

    @property
    def LogiOperator(self):
        return self._LogiOperator

    @LogiOperator.setter
    def LogiOperator(self, LogiOperator):
        self._LogiOperator = LogiOperator

    @property
    def MatchValue(self):
        return self._MatchValue

    @MatchValue.setter
    def MatchValue(self, MatchValue):
        self._MatchValue = MatchValue


    def _deserialize(self, params):
        self._MatchKey = params.get("MatchKey")
        self._LogiOperator = params.get("LogiOperator")
        self._MatchValue = params.get("MatchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnBotConfig(AbstractModel):
    """Bot configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable SCDN bot configuration. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _BotCookie: Bot cookie policy
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type BotCookie: list of BotCookie
        :param _BotJavaScript: Bot JS policy
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type BotJavaScript: list of BotJavaScript
        """
        self._Switch = None
        self._BotCookie = None
        self._BotJavaScript = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def BotCookie(self):
        return self._BotCookie

    @BotCookie.setter
    def BotCookie(self, BotCookie):
        self._BotCookie = BotCookie

    @property
    def BotJavaScript(self):
        return self._BotJavaScript

    @BotJavaScript.setter
    def BotJavaScript(self, BotJavaScript):
        self._BotJavaScript = BotJavaScript


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("BotCookie") is not None:
            self._BotCookie = []
            for item in params.get("BotCookie"):
                obj = BotCookie()
                obj._deserialize(item)
                self._BotCookie.append(obj)
        if params.get("BotJavaScript") is not None:
            self._BotJavaScript = []
            for item in params.get("BotJavaScript"):
                obj = BotJavaScript()
                obj._deserialize(item)
                self._BotJavaScript.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnCCRules(AbstractModel):
    """SCDN custom CC rules

    """

    def __init__(self):
        r"""
        :param _RuleType: Rule types:
`all`: effective for all files.
`file`: Apply to files with the specified suffixes.
`directory`: Apply to specified paths.
`path`: Apply to specified absolute paths.
`index`: effective for web homepages and root directories.
        :type RuleType: str
        :param _RuleValue: Rule value (blocking condition)
        :type RuleValue: list of str
        :param _Qps: IP access limit rule
        :type Qps: int
        :param _DetectionTime: Detection granularity
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DetectionTime: int
        :param _FrequencyLimit: Frequency threshold
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FrequencyLimit: int
        :param _PunishmentSwitch: Whether to enable IP blocking. Values:
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PunishmentSwitch: str
        :param _PunishmentTime: Suspicious IP restriction duration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type PunishmentTime: int
        :param _Action: Action. Valid values: `intercept` and `redirect`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Action: str
        :param _RedirectUrl: The redirection target URL used when the `Action` is `redirect`
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RedirectUrl: str
        """
        self._RuleType = None
        self._RuleValue = None
        self._Qps = None
        self._DetectionTime = None
        self._FrequencyLimit = None
        self._PunishmentSwitch = None
        self._PunishmentTime = None
        self._Action = None
        self._RedirectUrl = None

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RuleValue(self):
        return self._RuleValue

    @RuleValue.setter
    def RuleValue(self, RuleValue):
        self._RuleValue = RuleValue

    @property
    def Qps(self):
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def DetectionTime(self):
        return self._DetectionTime

    @DetectionTime.setter
    def DetectionTime(self, DetectionTime):
        self._DetectionTime = DetectionTime

    @property
    def FrequencyLimit(self):
        return self._FrequencyLimit

    @FrequencyLimit.setter
    def FrequencyLimit(self, FrequencyLimit):
        self._FrequencyLimit = FrequencyLimit

    @property
    def PunishmentSwitch(self):
        return self._PunishmentSwitch

    @PunishmentSwitch.setter
    def PunishmentSwitch(self, PunishmentSwitch):
        self._PunishmentSwitch = PunishmentSwitch

    @property
    def PunishmentTime(self):
        return self._PunishmentTime

    @PunishmentTime.setter
    def PunishmentTime(self, PunishmentTime):
        self._PunishmentTime = PunishmentTime

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RedirectUrl(self):
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._RuleValue = params.get("RuleValue")
        self._Qps = params.get("Qps")
        self._DetectionTime = params.get("DetectionTime")
        self._FrequencyLimit = params.get("FrequencyLimit")
        self._PunishmentSwitch = params.get("PunishmentSwitch")
        self._PunishmentTime = params.get("PunishmentTime")
        self._Action = params.get("Action")
        self._RedirectUrl = params.get("RedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnConfig(AbstractModel):
    """CC attack defense configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable SCDN CC configuration. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _Rules: Custom CC attack defense rule
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Rules: list of ScdnCCRules
        :param _AdvancedRules: Advanced custom CC attack defense rule
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AdvancedRules: list of AdvancedCCRules
        :param _GlobalAdvancedRules: Global advanced CC protection rules
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type GlobalAdvancedRules: list of AdvancedCCRules
        """
        self._Switch = None
        self._Rules = None
        self._AdvancedRules = None
        self._GlobalAdvancedRules = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def AdvancedRules(self):
        return self._AdvancedRules

    @AdvancedRules.setter
    def AdvancedRules(self, AdvancedRules):
        self._AdvancedRules = AdvancedRules

    @property
    def GlobalAdvancedRules(self):
        return self._GlobalAdvancedRules

    @GlobalAdvancedRules.setter
    def GlobalAdvancedRules(self, GlobalAdvancedRules):
        self._GlobalAdvancedRules = GlobalAdvancedRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = ScdnCCRules()
                obj._deserialize(item)
                self._Rules.append(obj)
        if params.get("AdvancedRules") is not None:
            self._AdvancedRules = []
            for item in params.get("AdvancedRules"):
                obj = AdvancedCCRules()
                obj._deserialize(item)
                self._AdvancedRules.append(obj)
        if params.get("GlobalAdvancedRules") is not None:
            self._GlobalAdvancedRules = []
            for item in params.get("GlobalAdvancedRules"):
                obj = AdvancedCCRules()
                obj._deserialize(item)
                self._GlobalAdvancedRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnDdosConfig(AbstractModel):
    """DDoS configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable SCDN DDoS configuration. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnErrorPage(AbstractModel):
    """ACL error page

    """

    def __init__(self):
        r"""
        :param _RedirectCode: Status code
`403` is passed in when the action is `intercept`.
`301` is passed in when the action is `redirect`.
        :type RedirectCode: int
        :param _RedirectUrl: URL to be redirected
        :type RedirectUrl: str
        """
        self._RedirectCode = None
        self._RedirectUrl = None

    @property
    def RedirectCode(self):
        return self._RedirectCode

    @RedirectCode.setter
    def RedirectCode(self, RedirectCode):
        self._RedirectCode = RedirectCode

    @property
    def RedirectUrl(self):
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl


    def _deserialize(self, params):
        self._RedirectCode = params.get("RedirectCode")
        self._RedirectUrl = params.get("RedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnSevenLayerRules(AbstractModel):
    """SCDN layer-7 rule configuration for CC frequency limiting

    """

    def __init__(self):
        r"""
        :param _CaseSensitive: Whether values are case sensitive
        :type CaseSensitive: bool
        :param _RuleType: Rule types:
`protocol`: protocol. Valid values: `HTTP` and `HTTPS`.
`method`: request method. Valid values: `HEAD`, `GET`, `POST`, `PUT`, `OPTIONS`, `TRACE`, `DELETE`, `PATCH` and `CONNECT`.
`all`: domain name. The matching content is `*` and cannot be edited.
`ip`: IP in CIDR format.
`directory`: path starting with a slash (/). You can specify a directory or specific path using up to 128 characters.
`index`: default homepage, which is specified by `/;/index.html` and cannot be edited.
`path`: full path of the file, such as `/acb/test.png`. Wildcard is supported, such as `/abc/*.jpg`.
`file`: file extension, such as `jpg`, `png` and `css`.
`param`: request parameter. The value can contain up to 512 characters.
`referer`: Referer. The value can contain up to 512 characters.
`cookie`: Cookie. The value can contain up to 512 characters.
`user-agent`: User-Agent. The value can contain up to 512 characters.
`head`: custom header. The value can contain up to 512 characters. If the matching content is blank or does not exist, enter the matching parameter directly.
        :type RuleType: str
        :param _LogicOperator: Logical operator, which connects the relation between RuleType and RuleValue. Valid values:
`exclude`: the rule value is not contained. 
`include`: the rule value is contained. 
`notequal`: the rule value is not equal to the specified rule type. 
`equal`: the rule value is equal to the specified rule type. 
`matching`: the rule value matches with the prefix of the specified rule type.
`null`: the rule value is empty or does not exist.
        :type LogicOperator: str
        :param _RuleValue: Rule value
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RuleValue: list of str
        :param _RuleParam: Matched parameter. Only request parameters, Cookie, and custom request headers have a value.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RuleParam: str
        """
        self._CaseSensitive = None
        self._RuleType = None
        self._LogicOperator = None
        self._RuleValue = None
        self._RuleParam = None

    @property
    def CaseSensitive(self):
        return self._CaseSensitive

    @CaseSensitive.setter
    def CaseSensitive(self, CaseSensitive):
        self._CaseSensitive = CaseSensitive

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def LogicOperator(self):
        return self._LogicOperator

    @LogicOperator.setter
    def LogicOperator(self, LogicOperator):
        self._LogicOperator = LogicOperator

    @property
    def RuleValue(self):
        return self._RuleValue

    @RuleValue.setter
    def RuleValue(self, RuleValue):
        self._RuleValue = RuleValue

    @property
    def RuleParam(self):
        return self._RuleParam

    @RuleParam.setter
    def RuleParam(self, RuleParam):
        self._RuleParam = RuleParam


    def _deserialize(self, params):
        self._CaseSensitive = params.get("CaseSensitive")
        self._RuleType = params.get("RuleType")
        self._LogicOperator = params.get("LogicOperator")
        self._RuleValue = params.get("RuleValue")
        self._RuleParam = params.get("RuleParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnWafConfig(AbstractModel):
    """WAF configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable SCDN WAF configuration. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _Mode: WAF protection mode. Valid values: `intercept` and `observe`. Default value: `intercept`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Mode: str
        :param _ErrorPage: Redirection error page
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ScdnErrorPage`
        :param _WebShellSwitch: Whether to enable webshell blocking. Values:
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type WebShellSwitch: str
        :param _Rules: Attack blocking rules
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Rules: list of ScdnWafRule
        :param _Level: WAF rule level. Valid values: 100, 200, and 300.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Level: int
        :param _SubRuleSwitch: Whether to enable WAF sub-rules. Values:
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SubRuleSwitch: list of WafSubRuleStatus
        """
        self._Switch = None
        self._Mode = None
        self._ErrorPage = None
        self._WebShellSwitch = None
        self._Rules = None
        self._Level = None
        self._SubRuleSwitch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def ErrorPage(self):
        return self._ErrorPage

    @ErrorPage.setter
    def ErrorPage(self, ErrorPage):
        self._ErrorPage = ErrorPage

    @property
    def WebShellSwitch(self):
        return self._WebShellSwitch

    @WebShellSwitch.setter
    def WebShellSwitch(self, WebShellSwitch):
        self._WebShellSwitch = WebShellSwitch

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def SubRuleSwitch(self):
        return self._SubRuleSwitch

    @SubRuleSwitch.setter
    def SubRuleSwitch(self, SubRuleSwitch):
        self._SubRuleSwitch = SubRuleSwitch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Mode = params.get("Mode")
        if params.get("ErrorPage") is not None:
            self._ErrorPage = ScdnErrorPage()
            self._ErrorPage._deserialize(params.get("ErrorPage"))
        self._WebShellSwitch = params.get("WebShellSwitch")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = ScdnWafRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Level = params.get("Level")
        if params.get("SubRuleSwitch") is not None:
            self._SubRuleSwitch = []
            for item in params.get("SubRuleSwitch"):
                obj = WafSubRuleStatus()
                obj._deserialize(item)
                self._SubRuleSwitch.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnWafRule(AbstractModel):
    """WAF rule information

    """

    def __init__(self):
        r"""
        :param _AttackType: Attack type
        :type AttackType: str
        :param _Operate: Defense action. Valid value: `observe`.
        :type Operate: str
        """
        self._AttackType = None
        self._Operate = None

    @property
    def AttackType(self):
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def Operate(self):
        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        self._Operate = Operate


    def _deserialize(self, params):
        self._AttackType = params.get("AttackType")
        self._Operate = params.get("Operate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemeKey(AbstractModel):
    """A part of `CacheKey`

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable scheme as part of the cache key. Values:
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchClsLogRequest(AbstractModel):
    """SearchClsLog request structure.

    """

    def __init__(self):
        r"""
        :param _LogsetId: ID of logset to be queried
        :type LogsetId: str
        :param _TopicIds: List of IDs of log topics to be queried, separated by commas
        :type TopicIds: str
        :param _StartTime: Query start time in the format of YYYY-mm-dd HH:MM:SS
        :type StartTime: str
        :param _EndTime: Query end time in the format of YYYY-mm-dd HH:MM:SS
        :type EndTime: str
        :param _Limit: Number of logs to be returned at a time. Maximum value: 100
        :type Limit: int
        :param _Channel: Specifies whether to access CDN or ECDN. Valid values: `cdn` (default) and `ecdn`.
        :type Channel: str
        :param _Query: Query statement. For more details, see [https://intl.cloud.tencent.com/document/product/614/16982?from_cn_redirect=1].
        :type Query: str
        :param _Context: This field is used when loading more results. Pass through the last `context` value returned to get more log content. Up to 10,000 logs can be obtained through the cursor. Please narrow down the time range as much as possible.
        :type Context: str
        :param _Sort: Sorting by log time. Valid values: asc (ascending), desc (descending). Default value: desc
        :type Sort: str
        """
        self._LogsetId = None
        self._TopicIds = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Channel = None
        self._Query = None
        self._Context = None
        self._Sort = None

    @property
    def LogsetId(self):
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicIds(self):
        return self._TopicIds

    @TopicIds.setter
    def TopicIds(self, TopicIds):
        self._TopicIds = TopicIds

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
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Context(self):
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._TopicIds = params.get("TopicIds")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Channel = params.get("Channel")
        self._Query = params.get("Query")
        self._Context = params.get("Context")
        self._Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchClsLogResponse(AbstractModel):
    """SearchClsLog response structure.

    """

    def __init__(self):
        r"""
        :param _Logs: Query results
        :type Logs: :class:`tencentcloud.cdn.v20180606.models.ClsSearchLogs`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Logs = None
        self._RequestId = None

    @property
    def Logs(self):
        return self._Logs

    @Logs.setter
    def Logs(self, Logs):
        self._Logs = Logs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Logs") is not None:
            self._Logs = ClsSearchLogs()
            self._Logs._deserialize(params.get("Logs"))
        self._RequestId = params.get("RequestId")


class SecurityConfig(AbstractModel):
    """SCDN configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable SCDN. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Seo(AbstractModel):
    """SEO configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable SEO. Values:
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerCert(AbstractModel):
    """HTTPS acceleration server certificate configuration:
    + Supports deployment with certificates that are being hosted by the SSL Certificate Services
    + Supports uploading certificates of PEM format for deployment

    """

    def __init__(self):
        r"""
        :param _CertId: Server certificate ID, which is auto-generated when the certificate is being managed by the SSL Certificate Service
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CertId: str
        :param _CertName: Server certificate name
This is auto-generated when the certificate is being hosted by the SSL Certificate Service
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CertName: str
        :param _Certificate: Server certificate information
This is required when uploading an external certificate, which should contain the complete certificate chain.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Certificate: str
        :param _PrivateKey: Server key information
This is required when uploading an external certificate.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type PrivateKey: str
        :param _ExpireTime: Time when the certificate expires
Can be left blank when used as an input parameter
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type ExpireTime: str
        :param _DeployTime: Certificate issuance time
Can be left blank when used as an input parameter
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type DeployTime: str
        :param _Message: Certificate remarks
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Message: str
        :param _From: Certificate source
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type From: str
        """
        self._CertId = None
        self._CertName = None
        self._Certificate = None
        self._PrivateKey = None
        self._ExpireTime = None
        self._DeployTime = None
        self._Message = None
        self._From = None

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def PrivateKey(self):
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def DeployTime(self):
        return self._DeployTime

    @DeployTime.setter
    def DeployTime(self, DeployTime):
        self._DeployTime = DeployTime

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._CertName = params.get("CertName")
        self._Certificate = params.get("Certificate")
        self._PrivateKey = params.get("PrivateKey")
        self._ExpireTime = params.get("ExpireTime")
        self._DeployTime = params.get("DeployTime")
        self._Message = params.get("Message")
        self._From = params.get("From")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShareCname(AbstractModel):
    """Shared CNAME configuration
    ShareCname is only available to beta users. Submit a ticket if you need it.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable Shared CNAME. Values:
`on`: Enable. When enabled, it uses a shared CNAME.
`off`: Disable. When disabled, it uses a default CNAME.

        :type Switch: str
        :param _Cname: Shared CNAME to be configured
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Cname: str
        """
        self._Switch = None
        self._Cname = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Cname(self):
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Cname = params.get("Cname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SimpleCache(AbstractModel):
    """Cache configuration basic version
    The cache expiration time for all files is 30 days by default.
    Static acceleration type domain names .php, .jsp, .asp, and .aspx are not cached by default
    Note: this version does not support setting cache expiration rules if the origin server does not return max-age

    """

    def __init__(self):
        r"""
        :param _CacheRules: Cache expiration time rules
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CacheRules: list of SimpleCacheRule
        :param _FollowOrigin: Follows origin server Cache-Control: max-age configurations
`on`: Enable
`off`: Disable
If this is enabled, resources that do not match CacheRules rules will be cached by the node according to the max-age value returned by the origin server. Resources that match CacheRules rules will be cached on the node according to the cache expiration time set in CacheRules.
This conflicts with CompareMaxAge. The two cannot be enabled at the same time.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FollowOrigin: str
        :param _IgnoreCacheControl: Forced cache
`on`: Enable
`off`: Disable
This is disabled by default. If enabled, the `no-store` and `no-cache` resources returned from the origin server will be cached according to `CacheRules` rules.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IgnoreCacheControl: str
        :param _IgnoreSetCookie: Ignores the Set-Cookie header of the origin server
`on`: Enable
`off`: Disable
It is disabled by default.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IgnoreSetCookie: str
        :param _CompareMaxAge: Advanced cache expiration configuration. If this is enabled, the max-age value returned by the origin server will be compared with the cache expiration time set in CacheRules, and the smallest value will be cached on the node.
`on`: Enable
`off`: Disable
It is disabled by default.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CompareMaxAge: str
        :param _Revalidate: Always forwards to the origin server for verification
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Revalidate: :class:`tencentcloud.cdn.v20180606.models.Revalidate`
        """
        self._CacheRules = None
        self._FollowOrigin = None
        self._IgnoreCacheControl = None
        self._IgnoreSetCookie = None
        self._CompareMaxAge = None
        self._Revalidate = None

    @property
    def CacheRules(self):
        return self._CacheRules

    @CacheRules.setter
    def CacheRules(self, CacheRules):
        self._CacheRules = CacheRules

    @property
    def FollowOrigin(self):
        return self._FollowOrigin

    @FollowOrigin.setter
    def FollowOrigin(self, FollowOrigin):
        self._FollowOrigin = FollowOrigin

    @property
    def IgnoreCacheControl(self):
        return self._IgnoreCacheControl

    @IgnoreCacheControl.setter
    def IgnoreCacheControl(self, IgnoreCacheControl):
        self._IgnoreCacheControl = IgnoreCacheControl

    @property
    def IgnoreSetCookie(self):
        return self._IgnoreSetCookie

    @IgnoreSetCookie.setter
    def IgnoreSetCookie(self, IgnoreSetCookie):
        self._IgnoreSetCookie = IgnoreSetCookie

    @property
    def CompareMaxAge(self):
        return self._CompareMaxAge

    @CompareMaxAge.setter
    def CompareMaxAge(self, CompareMaxAge):
        self._CompareMaxAge = CompareMaxAge

    @property
    def Revalidate(self):
        return self._Revalidate

    @Revalidate.setter
    def Revalidate(self, Revalidate):
        self._Revalidate = Revalidate


    def _deserialize(self, params):
        if params.get("CacheRules") is not None:
            self._CacheRules = []
            for item in params.get("CacheRules"):
                obj = SimpleCacheRule()
                obj._deserialize(item)
                self._CacheRules.append(obj)
        self._FollowOrigin = params.get("FollowOrigin")
        self._IgnoreCacheControl = params.get("IgnoreCacheControl")
        self._IgnoreSetCookie = params.get("IgnoreSetCookie")
        self._CompareMaxAge = params.get("CompareMaxAge")
        if params.get("Revalidate") is not None:
            self._Revalidate = Revalidate()
            self._Revalidate._deserialize(params.get("Revalidate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SimpleCacheRule(AbstractModel):
    """Cache expiration rules configuration

    """

    def __init__(self):
        r"""
        :param _CacheType: Rule types:
`all`: Apply to all files.
`file`: Apply to files with the specified suffixes.
`directory`: Apply to specified paths.
`path`: Apply to specified absolute paths.
index: home page
        :type CacheType: str
        :param _CacheContents: Content for each `CacheType`:
For `all`, enter a wildcard `*`.
For `file`, enter a suffix, e.g., `jpg` or `txt`.
For `directory`, enter a path, e.g., `/xxx/test/`.
For `path`, enter an absolute path, e.g., `/xxx/test.html`.
For `index`, enter a forward slash `/`.
        :type CacheContents: list of str
        :param _CacheTime: Cache expiration time settings
Unit: second. The maximum value is 365 days.
        :type CacheTime: int
        """
        self._CacheType = None
        self._CacheContents = None
        self._CacheTime = None

    @property
    def CacheType(self):
        return self._CacheType

    @CacheType.setter
    def CacheType(self, CacheType):
        self._CacheType = CacheType

    @property
    def CacheContents(self):
        return self._CacheContents

    @CacheContents.setter
    def CacheContents(self, CacheContents):
        self._CacheContents = CacheContents

    @property
    def CacheTime(self):
        return self._CacheTime

    @CacheTime.setter
    def CacheTime(self, CacheTime):
        self._CacheTime = CacheTime


    def _deserialize(self, params):
        self._CacheType = params.get("CacheType")
        self._CacheContents = params.get("CacheContents")
        self._CacheTime = params.get("CacheTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Sort(AbstractModel):
    """Sorting conditions for query results.

    """

    def __init__(self):
        r"""
        :param _Key: Fields that can be sorted. Currently supports:
`createTime`: domain name creation time.
`certExpireTime`: certificate expiration time.
Default value: createTime.
        :type Key: str
        :param _Sequence: asc/desc. Default value: desc.
        :type Sequence: str
        """
        self._Key = None
        self._Sequence = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Sequence(self):
        return self._Sequence

    @Sequence.setter
    def Sequence(self, Sequence):
        self._Sequence = Sequence


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Sequence = params.get("Sequence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecificConfig(AbstractModel):
    """Specific configuration for domain names inside and outside mainland China by regions.

    """

    def __init__(self):
        r"""
        :param _Mainland: Specific configuration for domain name inside mainland China.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Mainland: :class:`tencentcloud.cdn.v20180606.models.MainlandConfig`
        :param _Overseas: Specific configuration for domain name outside mainland China.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Overseas: :class:`tencentcloud.cdn.v20180606.models.OverseaConfig`
        """
        self._Mainland = None
        self._Overseas = None

    @property
    def Mainland(self):
        return self._Mainland

    @Mainland.setter
    def Mainland(self, Mainland):
        self._Mainland = Mainland

    @property
    def Overseas(self):
        return self._Overseas

    @Overseas.setter
    def Overseas(self, Overseas):
        self._Overseas = Overseas


    def _deserialize(self, params):
        if params.get("Mainland") is not None:
            self._Mainland = MainlandConfig()
            self._Mainland._deserialize(params.get("Mainland"))
        if params.get("Overseas") is not None:
            self._Overseas = OverseaConfig()
            self._Overseas._deserialize(params.get("Overseas"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartCdnDomainRequest(AbstractModel):
    """StartCdnDomain request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain name
The domain name status should be `Disabled`
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartCdnDomainResponse(AbstractModel):
    """StartCdnDomain response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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


class StatisticItem(AbstractModel):
    """Usage limit configuration

    """

    def __init__(self):
        r"""
        :param _Type: Type of usage limit. `total`: Cumulative usage; `moment`: Instantaneous usage.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Type: str
        :param _UnBlockTime: Unblocking time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UnBlockTime: int
        :param _BpsThreshold: Bandwidth/Traffic threshold
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type BpsThreshold: int
        :param _CounterMeasure: Specifies how to disable CDN service when the threshold is exceeded. `RETURN_404`: Return 404; `RESOLVE_DNS_TO_ORIGIN`: Forward to origin server.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CounterMeasure: str
        :param _AlertPercentage: Threshold (in percentage) that triggers alarms
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type AlertPercentage: int
        :param _AlertSwitch: Whether to enable alerts for cumulative usage limit. Values:
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AlertSwitch: str
        :param _Metric: Metric type. `flux`: Traffic; `bandwidth`: Bandwidth.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Metric: str
        :param _Cycle: 
        :type Cycle: int
        :param _Switch: Whether to enable cumulative usage limit. Values:
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        """
        self._Type = None
        self._UnBlockTime = None
        self._BpsThreshold = None
        self._CounterMeasure = None
        self._AlertPercentage = None
        self._AlertSwitch = None
        self._Metric = None
        self._Cycle = None
        self._Switch = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UnBlockTime(self):
        return self._UnBlockTime

    @UnBlockTime.setter
    def UnBlockTime(self, UnBlockTime):
        self._UnBlockTime = UnBlockTime

    @property
    def BpsThreshold(self):
        return self._BpsThreshold

    @BpsThreshold.setter
    def BpsThreshold(self, BpsThreshold):
        self._BpsThreshold = BpsThreshold

    @property
    def CounterMeasure(self):
        return self._CounterMeasure

    @CounterMeasure.setter
    def CounterMeasure(self, CounterMeasure):
        self._CounterMeasure = CounterMeasure

    @property
    def AlertPercentage(self):
        return self._AlertPercentage

    @AlertPercentage.setter
    def AlertPercentage(self, AlertPercentage):
        self._AlertPercentage = AlertPercentage

    @property
    def AlertSwitch(self):
        return self._AlertSwitch

    @AlertSwitch.setter
    def AlertSwitch(self, AlertSwitch):
        self._AlertSwitch = AlertSwitch

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Cycle(self):
        return self._Cycle

    @Cycle.setter
    def Cycle(self, Cycle):
        self._Cycle = Cycle

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._UnBlockTime = params.get("UnBlockTime")
        self._BpsThreshold = params.get("BpsThreshold")
        self._CounterMeasure = params.get("CounterMeasure")
        self._AlertPercentage = params.get("AlertPercentage")
        self._AlertSwitch = params.get("AlertSwitch")
        self._Metric = params.get("Metric")
        self._Cycle = params.get("Cycle")
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatusCodeCache(AbstractModel):
    """Status code cache expiration configuration. 404 status codes are cached for 10 seconds by default

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable status code caching. Values:
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        :param _CacheRules: Status code cache expiration rules details
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CacheRules: list of StatusCodeCacheRule
        """
        self._Switch = None
        self._CacheRules = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def CacheRules(self):
        return self._CacheRules

    @CacheRules.setter
    def CacheRules(self, CacheRules):
        self._CacheRules = CacheRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("CacheRules") is not None:
            self._CacheRules = []
            for item in params.get("CacheRules"):
                obj = StatusCodeCacheRule()
                obj._deserialize(item)
                self._CacheRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatusCodeCacheRule(AbstractModel):
    """Status code cache expiration time rule configuration

    """

    def __init__(self):
        r"""
        :param _StatusCode: HTTP status code
Supports 403 and 404 status codes
        :type StatusCode: str
        :param _CacheTime: Status code cache expiration time (in seconds)
        :type CacheTime: int
        """
        self._StatusCode = None
        self._CacheTime = None

    @property
    def StatusCode(self):
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def CacheTime(self):
        return self._CacheTime

    @CacheTime.setter
    def CacheTime(self, CacheTime):
        self._CacheTime = CacheTime


    def _deserialize(self, params):
        self._StatusCode = params.get("StatusCode")
        self._CacheTime = params.get("CacheTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopCdnDomainRequest(AbstractModel):
    """StopCdnDomain request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain name
The domain name status should be **Enabled**
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopCdnDomainResponse(AbstractModel):
    """StopCdnDomain response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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


class SummarizedData(AbstractModel):
    """Aggregated value, which is aggregated from all data of each metric. Aggregation methods are used depending on the metric attributes.

    """

    def __init__(self):
        r"""
        :param _Name: Aggregation method, which can be:
`sum`: Aggregate summation
`max`: Maximum value. In bandwidth mode, the peak bandwidth is calculated based on the data aggregated in 5 minutes.
`avg`: Average value
        :type Name: str
        :param _Value: Aggregated value
        :type Value: float
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Domain name tag configuration

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TagKey: str
        :param _TagValue: Tag value
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

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


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimestampData(AbstractModel):
    """Timestamp and its corresponding value

    """

    def __init__(self):
        r"""
        :param _Time: The start point of the sampling period. 
For example, if the time is set to 13:35:00, and `interval` is `5min`, the data returned is collected between 13:35:00 and 13:39:59
        :type Time: str
        :param _Value: Data value
        :type Value: float
        """
        self._Time = None
        self._Value = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopData(AbstractModel):
    """Data structure of sorted data

    """

    def __init__(self):
        r"""
        :param _Resource: Resource name, which is classified as follows based on different query conditions:
A specific domain name: This indicates the details of this domain name
multiDomains: This indicates the aggregate details of multiple domain names
Project ID: This displays the ID of the specifically queried project
all: This indicates the details at the account level
        :type Resource: str
        :param _DetailData: Detailed sorting results
        :type DetailData: list of TopDetailData
        """
        self._Resource = None
        self._DetailData = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def DetailData(self):
        return self._DetailData

    @DetailData.setter
    def DetailData(self, DetailData):
        self._DetailData = DetailData


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        if params.get("DetailData") is not None:
            self._DetailData = []
            for item in params.get("DetailData"):
                obj = TopDetailData()
                obj._deserialize(item)
                self._DetailData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopDetailData(AbstractModel):
    """Data structure of sorted data

    """

    def __init__(self):
        r"""
        :param _Name: Datatype name
        :type Name: str
        :param _Value: Data value
        :type Value: float
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicInfo(AbstractModel):
    """CLS topic information

    """

    def __init__(self):
        r"""
        :param _TopicId: Topic ID
        :type TopicId: str
        :param _TopicName: Topic name
        :type TopicName: str
        :param _Enabled: Whether to enable publishing
        :type Enabled: int
        :param _CreateTime: Creation time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CreateTime: str
        :param _Channel: Either `cdn` or `ecdn`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Channel: str
        :param _Deleted: Whether the logset has been removed from CLS
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Deleted: str
        """
        self._TopicId = None
        self._TopicName = None
        self._Enabled = None
        self._CreateTime = None
        self._Channel = None
        self._Deleted = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Channel(self):
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def Deleted(self):
        return self._Deleted

    @Deleted.setter
    def Deleted(self, Deleted):
        self._Deleted = Deleted


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._Enabled = params.get("Enabled")
        self._CreateTime = params.get("CreateTime")
        self._Channel = params.get("Channel")
        self._Deleted = params.get("Deleted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TpgAdapter(AbstractModel):
    """Image optimization - `TpgAdapter` configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable TpgAdapter for image optimization. Values:
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDomainConfigRequest(AbstractModel):
    """UpdateDomainConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain name
        :type Domain: str
        :param _ProjectId: Project ID
        :type ProjectId: int
        :param _Origin: Origin server configuration
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param _IpFilter: IP blocklist/allowlist configuration
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param _IpFreqLimit: IP access limit configuration
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param _StatusCodeCache: Status code cache configuration
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param _Compression: Smart compression configuration
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param _BandwidthAlert: Bandwidth cap configuration
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param _RangeOriginPull: Range GETs configuration
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param _FollowRedirect: 301/302 origin-pull follow-redirect configuration
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param _ErrorPage: Error code redirect configuration (This feature is in beta and not generally available yet.)
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param _RequestHeader: Origin-pull request header configuration.
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param _ResponseHeader: Response header configuration
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param _DownstreamCapping: Download speed configuration
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param _CacheKey: Node cache key configuration
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param _ResponseHeaderCache: Header cache configuration
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param _VideoSeek: Video dragging configuration
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        :param _Cache: Cache expiration time configuration
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param _OriginPullOptimization: (Disused) Cross-border linkage optimization\
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param _Https: HTTPS acceleration configuration
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param _Authentication: Timestamp hotlink protection configuration
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param _Seo: SEO configuration
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param _ForceRedirect: Protocol redirect configuration
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param _Referer: Referer configuration
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param _MaxAge: Browser cache configuration (This feature is in beta and not generally available yet.)
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param _SpecificConfig: Specific-region special configuration
Applicable to cases where the acceleration domain name configuration differs for regions in and outside the Chinese mainland.
        :type SpecificConfig: :class:`tencentcloud.cdn.v20180606.models.SpecificConfig`
        :param _ServiceType: Domain name service type
`web`: Static acceleration
`download`: Download acceleration
`media`: Streaming media VOD acceleration
        :type ServiceType: str
        :param _Area: Domain name acceleration region
`mainland`: Acceleration inside the Chinese mainland
`overseas`: Acceleration outside the Chinese mainland
`global`: Acceleration over the globe
After switching to global acceleration, configurations of the domain name will be deployed to the region inside or outside the Chinese mainland. The deployment will take some time as this domain name has special settings.
        :type Area: str
        :param _OriginPullTimeout: Origin-pull timeout configuration
        :type OriginPullTimeout: :class:`tencentcloud.cdn.v20180606.models.OriginPullTimeout`
        :param _AwsPrivateAccess: Access authentication for S3 origin
        :type AwsPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`
        :param _UserAgentFilter: UA blocklist/allowlist configuration
        :type UserAgentFilter: :class:`tencentcloud.cdn.v20180606.models.UserAgentFilter`
        :param _AccessControl: Access control
        :type AccessControl: :class:`tencentcloud.cdn.v20180606.models.AccessControl`
        :param _UrlRedirect: URL rewriting configuration
        :type UrlRedirect: :class:`tencentcloud.cdn.v20180606.models.UrlRedirect`
        :param _AccessPort: Access port configuration
        :type AccessPort: list of int
        :param _AdvancedAuthentication: Timestamp hotlink protection advanced configuration (allowlist feature)
        :type AdvancedAuthentication: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthentication`
        :param _OriginAuthentication: Origin-pull authentication advanced configuration (allowlist feature)
        :type OriginAuthentication: :class:`tencentcloud.cdn.v20180606.models.OriginAuthentication`
        :param _Ipv6Access: IPv6 access configuration
        :type Ipv6Access: :class:`tencentcloud.cdn.v20180606.models.Ipv6Access`
        :param _OfflineCache: Offline cache
        :type OfflineCache: :class:`tencentcloud.cdn.v20180606.models.OfflineCache`
        :param _OriginCombine: Merging pull requests
        :type OriginCombine: :class:`tencentcloud.cdn.v20180606.models.OriginCombine`
        :param _PostMaxSize: Post transport configuration
        :type PostMaxSize: :class:`tencentcloud.cdn.v20180606.models.PostSize`
        :param _Quic: QUIC access, which is a paid service. You can check the product document and Billing Overview for more information.
        :type Quic: :class:`tencentcloud.cdn.v20180606.models.Quic`
        :param _OssPrivateAccess: Access authentication for OSS origin
        :type OssPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.OssPrivateAccess`
        :param _WebSocket: WebSocket configuration
        :type WebSocket: :class:`tencentcloud.cdn.v20180606.models.WebSocket`
        :param _RemoteAuthentication: Remote authentication configuration
        :type RemoteAuthentication: :class:`tencentcloud.cdn.v20180606.models.RemoteAuthentication`
        :param _ShareCname: Shared CNAME configuration (only available to beta users)
        :type ShareCname: :class:`tencentcloud.cdn.v20180606.models.ShareCname`
        :param _HwPrivateAccess: Access authentication for Huawei Cloud OBS origin
        :type HwPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.HwPrivateAccess`
        :param _QnPrivateAccess: Access authentication for QiNiu Cloud Kodo origin
        :type QnPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.QnPrivateAccess`
        :param _OthersPrivateAccess: Origin-pull authentication for other origins
        :type OthersPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.OthersPrivateAccess`
        :param _HttpsBilling: HTTPS, which is a paid service. You can check the product document and Billing Overview for more information.
        :type HttpsBilling: :class:`tencentcloud.cdn.v20180606.models.HttpsBilling`
        """
        self._Domain = None
        self._ProjectId = None
        self._Origin = None
        self._IpFilter = None
        self._IpFreqLimit = None
        self._StatusCodeCache = None
        self._Compression = None
        self._BandwidthAlert = None
        self._RangeOriginPull = None
        self._FollowRedirect = None
        self._ErrorPage = None
        self._RequestHeader = None
        self._ResponseHeader = None
        self._DownstreamCapping = None
        self._CacheKey = None
        self._ResponseHeaderCache = None
        self._VideoSeek = None
        self._Cache = None
        self._OriginPullOptimization = None
        self._Https = None
        self._Authentication = None
        self._Seo = None
        self._ForceRedirect = None
        self._Referer = None
        self._MaxAge = None
        self._SpecificConfig = None
        self._ServiceType = None
        self._Area = None
        self._OriginPullTimeout = None
        self._AwsPrivateAccess = None
        self._UserAgentFilter = None
        self._AccessControl = None
        self._UrlRedirect = None
        self._AccessPort = None
        self._AdvancedAuthentication = None
        self._OriginAuthentication = None
        self._Ipv6Access = None
        self._OfflineCache = None
        self._OriginCombine = None
        self._PostMaxSize = None
        self._Quic = None
        self._OssPrivateAccess = None
        self._WebSocket = None
        self._RemoteAuthentication = None
        self._ShareCname = None
        self._HwPrivateAccess = None
        self._QnPrivateAccess = None
        self._OthersPrivateAccess = None
        self._HttpsBilling = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def IpFilter(self):
        return self._IpFilter

    @IpFilter.setter
    def IpFilter(self, IpFilter):
        self._IpFilter = IpFilter

    @property
    def IpFreqLimit(self):
        return self._IpFreqLimit

    @IpFreqLimit.setter
    def IpFreqLimit(self, IpFreqLimit):
        self._IpFreqLimit = IpFreqLimit

    @property
    def StatusCodeCache(self):
        return self._StatusCodeCache

    @StatusCodeCache.setter
    def StatusCodeCache(self, StatusCodeCache):
        self._StatusCodeCache = StatusCodeCache

    @property
    def Compression(self):
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def BandwidthAlert(self):
        return self._BandwidthAlert

    @BandwidthAlert.setter
    def BandwidthAlert(self, BandwidthAlert):
        self._BandwidthAlert = BandwidthAlert

    @property
    def RangeOriginPull(self):
        return self._RangeOriginPull

    @RangeOriginPull.setter
    def RangeOriginPull(self, RangeOriginPull):
        self._RangeOriginPull = RangeOriginPull

    @property
    def FollowRedirect(self):
        return self._FollowRedirect

    @FollowRedirect.setter
    def FollowRedirect(self, FollowRedirect):
        self._FollowRedirect = FollowRedirect

    @property
    def ErrorPage(self):
        return self._ErrorPage

    @ErrorPage.setter
    def ErrorPage(self, ErrorPage):
        self._ErrorPage = ErrorPage

    @property
    def RequestHeader(self):
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader

    @property
    def ResponseHeader(self):
        return self._ResponseHeader

    @ResponseHeader.setter
    def ResponseHeader(self, ResponseHeader):
        self._ResponseHeader = ResponseHeader

    @property
    def DownstreamCapping(self):
        return self._DownstreamCapping

    @DownstreamCapping.setter
    def DownstreamCapping(self, DownstreamCapping):
        self._DownstreamCapping = DownstreamCapping

    @property
    def CacheKey(self):
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def ResponseHeaderCache(self):
        return self._ResponseHeaderCache

    @ResponseHeaderCache.setter
    def ResponseHeaderCache(self, ResponseHeaderCache):
        self._ResponseHeaderCache = ResponseHeaderCache

    @property
    def VideoSeek(self):
        return self._VideoSeek

    @VideoSeek.setter
    def VideoSeek(self, VideoSeek):
        self._VideoSeek = VideoSeek

    @property
    def Cache(self):
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def OriginPullOptimization(self):
        return self._OriginPullOptimization

    @OriginPullOptimization.setter
    def OriginPullOptimization(self, OriginPullOptimization):
        self._OriginPullOptimization = OriginPullOptimization

    @property
    def Https(self):
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def Authentication(self):
        return self._Authentication

    @Authentication.setter
    def Authentication(self, Authentication):
        self._Authentication = Authentication

    @property
    def Seo(self):
        return self._Seo

    @Seo.setter
    def Seo(self, Seo):
        self._Seo = Seo

    @property
    def ForceRedirect(self):
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def Referer(self):
        return self._Referer

    @Referer.setter
    def Referer(self, Referer):
        self._Referer = Referer

    @property
    def MaxAge(self):
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def SpecificConfig(self):
        return self._SpecificConfig

    @SpecificConfig.setter
    def SpecificConfig(self, SpecificConfig):
        self._SpecificConfig = SpecificConfig

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def OriginPullTimeout(self):
        return self._OriginPullTimeout

    @OriginPullTimeout.setter
    def OriginPullTimeout(self, OriginPullTimeout):
        self._OriginPullTimeout = OriginPullTimeout

    @property
    def AwsPrivateAccess(self):
        return self._AwsPrivateAccess

    @AwsPrivateAccess.setter
    def AwsPrivateAccess(self, AwsPrivateAccess):
        self._AwsPrivateAccess = AwsPrivateAccess

    @property
    def UserAgentFilter(self):
        return self._UserAgentFilter

    @UserAgentFilter.setter
    def UserAgentFilter(self, UserAgentFilter):
        self._UserAgentFilter = UserAgentFilter

    @property
    def AccessControl(self):
        return self._AccessControl

    @AccessControl.setter
    def AccessControl(self, AccessControl):
        self._AccessControl = AccessControl

    @property
    def UrlRedirect(self):
        return self._UrlRedirect

    @UrlRedirect.setter
    def UrlRedirect(self, UrlRedirect):
        self._UrlRedirect = UrlRedirect

    @property
    def AccessPort(self):
        return self._AccessPort

    @AccessPort.setter
    def AccessPort(self, AccessPort):
        self._AccessPort = AccessPort

    @property
    def AdvancedAuthentication(self):
        return self._AdvancedAuthentication

    @AdvancedAuthentication.setter
    def AdvancedAuthentication(self, AdvancedAuthentication):
        self._AdvancedAuthentication = AdvancedAuthentication

    @property
    def OriginAuthentication(self):
        return self._OriginAuthentication

    @OriginAuthentication.setter
    def OriginAuthentication(self, OriginAuthentication):
        self._OriginAuthentication = OriginAuthentication

    @property
    def Ipv6Access(self):
        return self._Ipv6Access

    @Ipv6Access.setter
    def Ipv6Access(self, Ipv6Access):
        self._Ipv6Access = Ipv6Access

    @property
    def OfflineCache(self):
        return self._OfflineCache

    @OfflineCache.setter
    def OfflineCache(self, OfflineCache):
        self._OfflineCache = OfflineCache

    @property
    def OriginCombine(self):
        return self._OriginCombine

    @OriginCombine.setter
    def OriginCombine(self, OriginCombine):
        self._OriginCombine = OriginCombine

    @property
    def PostMaxSize(self):
        return self._PostMaxSize

    @PostMaxSize.setter
    def PostMaxSize(self, PostMaxSize):
        self._PostMaxSize = PostMaxSize

    @property
    def Quic(self):
        return self._Quic

    @Quic.setter
    def Quic(self, Quic):
        self._Quic = Quic

    @property
    def OssPrivateAccess(self):
        return self._OssPrivateAccess

    @OssPrivateAccess.setter
    def OssPrivateAccess(self, OssPrivateAccess):
        self._OssPrivateAccess = OssPrivateAccess

    @property
    def WebSocket(self):
        return self._WebSocket

    @WebSocket.setter
    def WebSocket(self, WebSocket):
        self._WebSocket = WebSocket

    @property
    def RemoteAuthentication(self):
        return self._RemoteAuthentication

    @RemoteAuthentication.setter
    def RemoteAuthentication(self, RemoteAuthentication):
        self._RemoteAuthentication = RemoteAuthentication

    @property
    def ShareCname(self):
        return self._ShareCname

    @ShareCname.setter
    def ShareCname(self, ShareCname):
        self._ShareCname = ShareCname

    @property
    def HwPrivateAccess(self):
        return self._HwPrivateAccess

    @HwPrivateAccess.setter
    def HwPrivateAccess(self, HwPrivateAccess):
        self._HwPrivateAccess = HwPrivateAccess

    @property
    def QnPrivateAccess(self):
        return self._QnPrivateAccess

    @QnPrivateAccess.setter
    def QnPrivateAccess(self, QnPrivateAccess):
        self._QnPrivateAccess = QnPrivateAccess

    @property
    def OthersPrivateAccess(self):
        return self._OthersPrivateAccess

    @OthersPrivateAccess.setter
    def OthersPrivateAccess(self, OthersPrivateAccess):
        self._OthersPrivateAccess = OthersPrivateAccess

    @property
    def HttpsBilling(self):
        return self._HttpsBilling

    @HttpsBilling.setter
    def HttpsBilling(self, HttpsBilling):
        self._HttpsBilling = HttpsBilling


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._ProjectId = params.get("ProjectId")
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        if params.get("IpFilter") is not None:
            self._IpFilter = IpFilter()
            self._IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self._IpFreqLimit = IpFreqLimit()
            self._IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("StatusCodeCache") is not None:
            self._StatusCodeCache = StatusCodeCache()
            self._StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("Compression") is not None:
            self._Compression = Compression()
            self._Compression._deserialize(params.get("Compression"))
        if params.get("BandwidthAlert") is not None:
            self._BandwidthAlert = BandwidthAlert()
            self._BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("RangeOriginPull") is not None:
            self._RangeOriginPull = RangeOriginPull()
            self._RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("FollowRedirect") is not None:
            self._FollowRedirect = FollowRedirect()
            self._FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ErrorPage") is not None:
            self._ErrorPage = ErrorPage()
            self._ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("RequestHeader") is not None:
            self._RequestHeader = RequestHeader()
            self._RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self._ResponseHeader = ResponseHeader()
            self._ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("DownstreamCapping") is not None:
            self._DownstreamCapping = DownstreamCapping()
            self._DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("ResponseHeaderCache") is not None:
            self._ResponseHeaderCache = ResponseHeaderCache()
            self._ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("VideoSeek") is not None:
            self._VideoSeek = VideoSeek()
            self._VideoSeek._deserialize(params.get("VideoSeek"))
        if params.get("Cache") is not None:
            self._Cache = Cache()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("OriginPullOptimization") is not None:
            self._OriginPullOptimization = OriginPullOptimization()
            self._OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        if params.get("Authentication") is not None:
            self._Authentication = Authentication()
            self._Authentication._deserialize(params.get("Authentication"))
        if params.get("Seo") is not None:
            self._Seo = Seo()
            self._Seo._deserialize(params.get("Seo"))
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirect()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Referer") is not None:
            self._Referer = Referer()
            self._Referer._deserialize(params.get("Referer"))
        if params.get("MaxAge") is not None:
            self._MaxAge = MaxAge()
            self._MaxAge._deserialize(params.get("MaxAge"))
        if params.get("SpecificConfig") is not None:
            self._SpecificConfig = SpecificConfig()
            self._SpecificConfig._deserialize(params.get("SpecificConfig"))
        self._ServiceType = params.get("ServiceType")
        self._Area = params.get("Area")
        if params.get("OriginPullTimeout") is not None:
            self._OriginPullTimeout = OriginPullTimeout()
            self._OriginPullTimeout._deserialize(params.get("OriginPullTimeout"))
        if params.get("AwsPrivateAccess") is not None:
            self._AwsPrivateAccess = AwsPrivateAccess()
            self._AwsPrivateAccess._deserialize(params.get("AwsPrivateAccess"))
        if params.get("UserAgentFilter") is not None:
            self._UserAgentFilter = UserAgentFilter()
            self._UserAgentFilter._deserialize(params.get("UserAgentFilter"))
        if params.get("AccessControl") is not None:
            self._AccessControl = AccessControl()
            self._AccessControl._deserialize(params.get("AccessControl"))
        if params.get("UrlRedirect") is not None:
            self._UrlRedirect = UrlRedirect()
            self._UrlRedirect._deserialize(params.get("UrlRedirect"))
        self._AccessPort = params.get("AccessPort")
        if params.get("AdvancedAuthentication") is not None:
            self._AdvancedAuthentication = AdvancedAuthentication()
            self._AdvancedAuthentication._deserialize(params.get("AdvancedAuthentication"))
        if params.get("OriginAuthentication") is not None:
            self._OriginAuthentication = OriginAuthentication()
            self._OriginAuthentication._deserialize(params.get("OriginAuthentication"))
        if params.get("Ipv6Access") is not None:
            self._Ipv6Access = Ipv6Access()
            self._Ipv6Access._deserialize(params.get("Ipv6Access"))
        if params.get("OfflineCache") is not None:
            self._OfflineCache = OfflineCache()
            self._OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("OriginCombine") is not None:
            self._OriginCombine = OriginCombine()
            self._OriginCombine._deserialize(params.get("OriginCombine"))
        if params.get("PostMaxSize") is not None:
            self._PostMaxSize = PostSize()
            self._PostMaxSize._deserialize(params.get("PostMaxSize"))
        if params.get("Quic") is not None:
            self._Quic = Quic()
            self._Quic._deserialize(params.get("Quic"))
        if params.get("OssPrivateAccess") is not None:
            self._OssPrivateAccess = OssPrivateAccess()
            self._OssPrivateAccess._deserialize(params.get("OssPrivateAccess"))
        if params.get("WebSocket") is not None:
            self._WebSocket = WebSocket()
            self._WebSocket._deserialize(params.get("WebSocket"))
        if params.get("RemoteAuthentication") is not None:
            self._RemoteAuthentication = RemoteAuthentication()
            self._RemoteAuthentication._deserialize(params.get("RemoteAuthentication"))
        if params.get("ShareCname") is not None:
            self._ShareCname = ShareCname()
            self._ShareCname._deserialize(params.get("ShareCname"))
        if params.get("HwPrivateAccess") is not None:
            self._HwPrivateAccess = HwPrivateAccess()
            self._HwPrivateAccess._deserialize(params.get("HwPrivateAccess"))
        if params.get("QnPrivateAccess") is not None:
            self._QnPrivateAccess = QnPrivateAccess()
            self._QnPrivateAccess._deserialize(params.get("QnPrivateAccess"))
        if params.get("OthersPrivateAccess") is not None:
            self._OthersPrivateAccess = OthersPrivateAccess()
            self._OthersPrivateAccess._deserialize(params.get("OthersPrivateAccess"))
        if params.get("HttpsBilling") is not None:
            self._HttpsBilling = HttpsBilling()
            self._HttpsBilling._deserialize(params.get("HttpsBilling"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDomainConfigResponse(AbstractModel):
    """UpdateDomainConfig response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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


class UpdatePayTypeRequest(AbstractModel):
    """UpdatePayType request structure.

    """

    def __init__(self):
        r"""
        :param _Area: Billing region, which can be `mainland` or `overseas`.
        :type Area: str
        :param _PayType: Billing mode, which can be `flux` or `bandwidth`.
        :type PayType: str
        """
        self._Area = None
        self._PayType = None

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def PayType(self):
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType


    def _deserialize(self, params):
        self._Area = params.get("Area")
        self._PayType = params.get("PayType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePayTypeResponse(AbstractModel):
    """UpdatePayType response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
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


class UpdateScdnDomainRequest(AbstractModel):
    """UpdateScdnDomain request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain name
        :type Domain: str
        :param _Waf: WAF configuration
        :type Waf: :class:`tencentcloud.cdn.v20180606.models.ScdnWafConfig`
        :param _Acl: Custom defense policy configuration
        :type Acl: :class:`tencentcloud.cdn.v20180606.models.ScdnAclConfig`
        :param _CC: CC attack defense configurations. CC attack defense is enabled by default.
        :type CC: :class:`tencentcloud.cdn.v20180606.models.ScdnConfig`
        :param _Ddos: DDoS defense configuration. DDoS defense is enabled by default.
        :type Ddos: :class:`tencentcloud.cdn.v20180606.models.ScdnDdosConfig`
        :param _Bot: Bot defense configuration
        :type Bot: :class:`tencentcloud.cdn.v20180606.models.ScdnBotConfig`
        """
        self._Domain = None
        self._Waf = None
        self._Acl = None
        self._CC = None
        self._Ddos = None
        self._Bot = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Waf(self):
        return self._Waf

    @Waf.setter
    def Waf(self, Waf):
        self._Waf = Waf

    @property
    def Acl(self):
        return self._Acl

    @Acl.setter
    def Acl(self, Acl):
        self._Acl = Acl

    @property
    def CC(self):
        return self._CC

    @CC.setter
    def CC(self, CC):
        self._CC = CC

    @property
    def Ddos(self):
        return self._Ddos

    @Ddos.setter
    def Ddos(self, Ddos):
        self._Ddos = Ddos

    @property
    def Bot(self):
        return self._Bot

    @Bot.setter
    def Bot(self, Bot):
        self._Bot = Bot


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        if params.get("Waf") is not None:
            self._Waf = ScdnWafConfig()
            self._Waf._deserialize(params.get("Waf"))
        if params.get("Acl") is not None:
            self._Acl = ScdnAclConfig()
            self._Acl._deserialize(params.get("Acl"))
        if params.get("CC") is not None:
            self._CC = ScdnConfig()
            self._CC._deserialize(params.get("CC"))
        if params.get("Ddos") is not None:
            self._Ddos = ScdnDdosConfig()
            self._Ddos._deserialize(params.get("Ddos"))
        if params.get("Bot") is not None:
            self._Bot = ScdnBotConfig()
            self._Bot._deserialize(params.get("Bot"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateScdnDomainResponse(AbstractModel):
    """UpdateScdnDomain response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Result of the request. `Success` indicates that the configurations are updated.
        :type Result: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UrlRecord(AbstractModel):
    """Details of the blocked URLs

    """

    def __init__(self):
        r"""
        :param _Status: Status. `disable`: Blocked; `enable`: Unblocked.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Status: str
        :param _RealUrl: Corresponding URL
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RealUrl: str
        :param _CreateTime: Creation time
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type CreateTime: str
        :param _UpdateTime: Update time.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UpdateTime: str
        """
        self._Status = None
        self._RealUrl = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RealUrl(self):
        return self._RealUrl

    @RealUrl.setter
    def RealUrl(self, RealUrl):
        self._RealUrl = RealUrl

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RealUrl = params.get("RealUrl")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UrlRedirect(AbstractModel):
    """Configuration of URL rewriting

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable URL rewriting. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _PathRules: Rule of URL rewriting rule, which is required if `Switch` is `on`. There can be up to 10 rules.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type PathRules: list of UrlRedirectRule
        """
        self._Switch = None
        self._PathRules = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def PathRules(self):
        return self._PathRules

    @PathRules.setter
    def PathRules(self, PathRules):
        self._PathRules = PathRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("PathRules") is not None:
            self._PathRules = []
            for item in params.get("PathRules"):
                obj = UrlRedirectRule()
                obj._deserialize(item)
                self._PathRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UrlRedirectRule(AbstractModel):
    """URL redirect rule configuration

    """

    def __init__(self):
        r"""
        :param _RedirectStatusCode: Redirect status code. Valid values: 301, 302
        :type RedirectStatusCode: int
        :param _Pattern: URL to be matched. Only URLs are supported, while parameters are not. The exact match is used by default. In regex match, up to 5 wildcards `*` are supported. The URL can contain up to 1,024 characters.
        :type Pattern: str
        :param _RedirectUrl: Target URL, starting with `/` and excluding parameters. The path can contain up to 1,024 characters. The wildcards in the matching path can be respectively captured using `$1`, `$2`, `$3`, `$4`, and `$5`. Up to 10 values can be captured.
        :type RedirectUrl: str
        :param _RedirectHost: Target host. It should be a standard domain name starting with `http://` or `https://`. If it is left empty, “http://[current domain name]” will be used by default.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RedirectHost: str
        :param _FullMatch: Whether to use full-path matching or arbitrary matching
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FullMatch: bool
        """
        self._RedirectStatusCode = None
        self._Pattern = None
        self._RedirectUrl = None
        self._RedirectHost = None
        self._FullMatch = None

    @property
    def RedirectStatusCode(self):
        return self._RedirectStatusCode

    @RedirectStatusCode.setter
    def RedirectStatusCode(self, RedirectStatusCode):
        self._RedirectStatusCode = RedirectStatusCode

    @property
    def Pattern(self):
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def RedirectUrl(self):
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl

    @property
    def RedirectHost(self):
        return self._RedirectHost

    @RedirectHost.setter
    def RedirectHost(self, RedirectHost):
        self._RedirectHost = RedirectHost

    @property
    def FullMatch(self):
        return self._FullMatch

    @FullMatch.setter
    def FullMatch(self, FullMatch):
        self._FullMatch = FullMatch


    def _deserialize(self, params):
        self._RedirectStatusCode = params.get("RedirectStatusCode")
        self._Pattern = params.get("Pattern")
        self._RedirectUrl = params.get("RedirectUrl")
        self._RedirectHost = params.get("RedirectHost")
        self._FullMatch = params.get("FullMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserAgentFilter(AbstractModel):
    """`UserAgent` blacklist/whitelist configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable User-Agent blocklist/allowlist. Values:
`on`: Enable
`off`: Disable
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        :param _FilterRules: UA blacklist/whitelist effect rule list
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FilterRules: list of UserAgentFilterRule
        """
        self._Switch = None
        self._FilterRules = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def FilterRules(self):
        return self._FilterRules

    @FilterRules.setter
    def FilterRules(self, FilterRules):
        self._FilterRules = FilterRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("FilterRules") is not None:
            self._FilterRules = []
            for item in params.get("FilterRules"):
                obj = UserAgentFilterRule()
                obj._deserialize(item)
                self._FilterRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserAgentFilterRule(AbstractModel):
    """`UserAgent` blacklist/whitelist rule configuration

    """

    def __init__(self):
        r"""
        :param _RuleType: Effective access path type
`all`: All access paths are effective
`file`: Effective by file extension
`directory`: Effective by directory
`path`: Effective by full access path
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuleType: str
        :param _RulePaths: Effective access paths
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RulePaths: list of str
        :param _UserAgents: `UserAgent` list
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type UserAgents: list of str
        :param _FilterType: Blocklist or allowlist. Valid values: `blacklist`, `whitelist`
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type FilterType: str
        """
        self._RuleType = None
        self._RulePaths = None
        self._UserAgents = None
        self._FilterType = None

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RulePaths(self):
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths

    @property
    def UserAgents(self):
        return self._UserAgents

    @UserAgents.setter
    def UserAgents(self, UserAgents):
        self._UserAgents = UserAgents

    @property
    def FilterType(self):
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._RulePaths = params.get("RulePaths")
        self._UserAgents = params.get("UserAgents")
        self._FilterType = params.get("FilterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoSeek(AbstractModel):
    """Video dragging configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable video dragging. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ViolationUrl(AbstractModel):
    """Details of URLs in violation

    """

    def __init__(self):
        r"""
        :param _Id: ID
        :type Id: int
        :param _RealUrl: Origin access URL of the resource in violation
        :type RealUrl: str
        :param _DownloadUrl: Snapshot path. This is used to display a snapshot of the content in violation on the console.
        :type DownloadUrl: str
        :param _UrlStatus: Current status of non-compliant resource
`forbid`: Blocked
`release`: Unblocked
`delay`: Processing delayed
`reject`: Appeal dismissed. It is still in `forbid` status.
`complain`: Appeal in process
        :type UrlStatus: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _UpdateTime: Update time
        :type UpdateTime: str
        """
        self._Id = None
        self._RealUrl = None
        self._DownloadUrl = None
        self._UrlStatus = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RealUrl(self):
        return self._RealUrl

    @RealUrl.setter
    def RealUrl(self, RealUrl):
        self._RealUrl = RealUrl

    @property
    def DownloadUrl(self):
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def UrlStatus(self):
        return self._UrlStatus

    @UrlStatus.setter
    def UrlStatus(self, UrlStatus):
        self._UrlStatus = UrlStatus

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RealUrl = params.get("RealUrl")
        self._DownloadUrl = params.get("DownloadUrl")
        self._UrlStatus = params.get("UrlStatus")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafSubRuleStatus(AbstractModel):
    """WAF sub-rule switch status

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable WAF sub-rules. Values:
`on`: Enable
`off`: Disable
        :type Switch: str
        :param _SubIds: List of rule IDs
        :type SubIds: list of int
        """
        self._Switch = None
        self._SubIds = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def SubIds(self):
        return self._SubIds

    @SubIds.setter
    def SubIds(self, SubIds):
        self._SubIds = SubIds


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._SubIds = params.get("SubIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebSocket(AbstractModel):
    """WebSocket configuration.
    WebSocket is an ECDN feature. You can enable it in the ECDN domain name configuration.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable WebSocket connection timeout. Values:
`on`: When it's enabled, the connection timeout can be configured.
`off`: When it's disabled, the connection timeout is set to 15 seconds by default.

        :type Switch: str
        :param _Timeout: Sets timeout period in seconds. Maximum value: 300
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Timeout: int
        """
        self._Switch = None
        self._Timeout = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Timeout(self):
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebpAdapter(AbstractModel):
    """Image optimization - `WebpAdapter` configuration

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable WebpAdapter for image optimization. Values:
`on`: Enable
`off`: Disable
Note: This field may return·`null`, indicating that no valid values can be obtained.
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        