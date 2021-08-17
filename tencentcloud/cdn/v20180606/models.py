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
        :param Switch: Whether to enable request header and request URL access control. Valid values: on, off
        :type Switch: str
        :param AccessControlRules: Request header and request URL access rule
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccessControlRules: list of AccessControlRule
        :param ReturnCode: Returned status code
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReturnCode: int
        """
        self.Switch = None
        self.AccessControlRules = None
        self.ReturnCode = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("AccessControlRules") is not None:
            self.AccessControlRules = []
            for item in params.get("AccessControlRules"):
                obj = AccessControlRule()
                obj._deserialize(item)
                self.AccessControlRules.append(obj)
        self.ReturnCode = params.get("ReturnCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessControlRule(AbstractModel):
    """Access control rule

    """

    def __init__(self):
        r"""
        :param RuleType: requestHeader: access control over request header
url: access control over access URL
Note: this field may return null, indicating that no valid values can be obtained.
        :type RuleType: str
        :param RuleContent: Blocked content
Note: this field may return null, indicating that no valid values can be obtained.
        :type RuleContent: str
        :param Regex: on: regular match
off: exact match
Note: this field may return null, indicating that no valid values can be obtained.
        :type Regex: str
        :param RuleHeader: This parameter is required only if `RuleType` is `requestHeader`
Note: this field may return null, indicating that no valid values can be obtained.
        :type RuleHeader: str
        """
        self.RuleType = None
        self.RuleContent = None
        self.Regex = None
        self.RuleHeader = None


    def _deserialize(self, params):
        self.RuleType = params.get("RuleType")
        self.RuleContent = params.get("RuleContent")
        self.Regex = params.get("Regex")
        self.RuleHeader = params.get("RuleHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCdnDomainRequest(AbstractModel):
    """AddCdnDomain request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain name
        :type Domain: str
        :param ServiceType: Acceleration domain name service type
web: static acceleration
download: download acceleration
media: streaming media VOD acceleration
        :type ServiceType: str
        :param Origin: Origin server configuration
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param ProjectId: Project ID. Default value: 0, indicating `Default Project`
        :type ProjectId: int
        :param IpFilter: IP blocklist/allowlist configuration
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param IpFreqLimit: IP access limit configuration
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param StatusCodeCache: Status code cache configuration
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param Compression: Smart compression configuration
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param BandwidthAlert: Bandwidth cap configuration
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param RangeOriginPull: Range GETs configuration
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param FollowRedirect: 301/302 origin-pull follow-redirect configuration
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param ErrorPage: Error code redirect configuration (This feature is in beta and not generally available yet.)
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param RequestHeader: Request header configuration
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param ResponseHeader: Response header configuration
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param DownstreamCapping: Download speed configuration
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param CacheKey: Node cache key configuration
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param ResponseHeaderCache: Header cache configuration
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param VideoSeek: Video dragging configuration
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        :param Cache: Cache expiration time configuration
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param OriginPullOptimization: Cross-border linkage optimization configuration
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param Https: HTTPS acceleration configuration
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param Authentication: Timestamp hotlink protection configuration
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param Seo: SEO configuration
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param ForceRedirect: Access protocol forced redirect configuration
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param Referer: Referer hotlink protection configuration
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param MaxAge: Browser cache configuration (This feature is in beta and not generally available yet.)
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param Ipv6: IPv6 configuration (This feature is in beta and not generally available yet.)
        :type Ipv6: :class:`tencentcloud.cdn.v20180606.models.Ipv6`
        :param SpecificConfig: Specific region configuration
Applicable to cases where the acceleration domain name configuration differs for regions in and outside mainland China.
        :type SpecificConfig: :class:`tencentcloud.cdn.v20180606.models.SpecificConfig`
        :param Area: Domain name acceleration region
mainland: acceleration inside mainland China
overseas: acceleration outside mainland China
global: global acceleration
Overseas acceleration service must be enabled to use overseas acceleration and global acceleration.
        :type Area: str
        :param OriginPullTimeout: Origin-pull timeout configuration
        :type OriginPullTimeout: :class:`tencentcloud.cdn.v20180606.models.OriginPullTimeout`
        :param Tag: Tag configuration
        :type Tag: list of Tag
        :param Ipv6Access: IPv6 access configuration
        :type Ipv6Access: :class:`tencentcloud.cdn.v20180606.models.Ipv6Access`
        :param OfflineCache: Offline cache
        :type OfflineCache: :class:`tencentcloud.cdn.v20180606.models.OfflineCache`
        :param Quic: QUIC is in beta now. Please submit an application to join the beta. For more information, please see QUIC product documents.
        :type Quic: :class:`tencentcloud.cdn.v20180606.models.Quic`
        :param AwsPrivateAccess: Access authentication for S3 origin
        :type AwsPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`
        :param OssPrivateAccess: Access authentication for OSS origin
        :type OssPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.OssPrivateAccess`
        """
        self.Domain = None
        self.ServiceType = None
        self.Origin = None
        self.ProjectId = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.StatusCodeCache = None
        self.Compression = None
        self.BandwidthAlert = None
        self.RangeOriginPull = None
        self.FollowRedirect = None
        self.ErrorPage = None
        self.RequestHeader = None
        self.ResponseHeader = None
        self.DownstreamCapping = None
        self.CacheKey = None
        self.ResponseHeaderCache = None
        self.VideoSeek = None
        self.Cache = None
        self.OriginPullOptimization = None
        self.Https = None
        self.Authentication = None
        self.Seo = None
        self.ForceRedirect = None
        self.Referer = None
        self.MaxAge = None
        self.Ipv6 = None
        self.SpecificConfig = None
        self.Area = None
        self.OriginPullTimeout = None
        self.Tag = None
        self.Ipv6Access = None
        self.OfflineCache = None
        self.Quic = None
        self.AwsPrivateAccess = None
        self.OssPrivateAccess = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.ServiceType = params.get("ServiceType")
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        self.ProjectId = params.get("ProjectId")
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("StatusCodeCache") is not None:
            self.StatusCodeCache = StatusCodeCache()
            self.StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("BandwidthAlert") is not None:
            self.BandwidthAlert = BandwidthAlert()
            self.BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("RangeOriginPull") is not None:
            self.RangeOriginPull = RangeOriginPull()
            self.RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("FollowRedirect") is not None:
            self.FollowRedirect = FollowRedirect()
            self.FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("RequestHeader") is not None:
            self.RequestHeader = RequestHeader()
            self.RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("DownstreamCapping") is not None:
            self.DownstreamCapping = DownstreamCapping()
            self.DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("ResponseHeaderCache") is not None:
            self.ResponseHeaderCache = ResponseHeaderCache()
            self.ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("VideoSeek") is not None:
            self.VideoSeek = VideoSeek()
            self.VideoSeek._deserialize(params.get("VideoSeek"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("OriginPullOptimization") is not None:
            self.OriginPullOptimization = OriginPullOptimization()
            self.OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("Authentication") is not None:
            self.Authentication = Authentication()
            self.Authentication._deserialize(params.get("Authentication"))
        if params.get("Seo") is not None:
            self.Seo = Seo()
            self.Seo._deserialize(params.get("Seo"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Referer") is not None:
            self.Referer = Referer()
            self.Referer._deserialize(params.get("Referer"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        if params.get("SpecificConfig") is not None:
            self.SpecificConfig = SpecificConfig()
            self.SpecificConfig._deserialize(params.get("SpecificConfig"))
        self.Area = params.get("Area")
        if params.get("OriginPullTimeout") is not None:
            self.OriginPullTimeout = OriginPullTimeout()
            self.OriginPullTimeout._deserialize(params.get("OriginPullTimeout"))
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self.Tag.append(obj)
        if params.get("Ipv6Access") is not None:
            self.Ipv6Access = Ipv6Access()
            self.Ipv6Access._deserialize(params.get("Ipv6Access"))
        if params.get("OfflineCache") is not None:
            self.OfflineCache = OfflineCache()
            self.OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("Quic") is not None:
            self.Quic = Quic()
            self.Quic._deserialize(params.get("Quic"))
        if params.get("AwsPrivateAccess") is not None:
            self.AwsPrivateAccess = AwsPrivateAccess()
            self.AwsPrivateAccess._deserialize(params.get("AwsPrivateAccess"))
        if params.get("OssPrivateAccess") is not None:
            self.OssPrivateAccess = OssPrivateAccess()
            self.OssPrivateAccess._deserialize(params.get("OssPrivateAccess"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCdnDomainResponse(AbstractModel):
    """AddCdnDomain response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AdvanceCacheRule(AbstractModel):
    """Advanced cache configuration rules

    """

    def __init__(self):
        r"""
        :param CacheType: Rule types:
`all`: effective for all files
`file`: effective for specified file suffixes
`directory`: effective for specified paths
`path`: effective for specified absolute paths
`default`: the cache rules when the origin server has not returned max-age
Note: this field may return null, indicating that no valid values can be obtained.
        :type CacheType: str
        :param CacheContents: Content for each CacheType:
For `all`, enter an asterisk (*).
For `file`, enter the suffix, such as jpg, txt.
For `directory`, enter the path, such as /xxx/test/.
For `path`, enter the corresponding absolute path, such as /xxx/test.html.
For `default`, enter "no max-age".
Note: this field may return null, indicating that no valid values can be obtained.
        :type CacheContents: list of str
        :param CacheTime: Cache expiration time
Unit: second. The maximum value is 365 days.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CacheTime: int
        """
        self.CacheType = None
        self.CacheContents = None
        self.CacheTime = None


    def _deserialize(self, params):
        self.CacheType = params.get("CacheType")
        self.CacheContents = params.get("CacheContents")
        self.CacheTime = params.get("CacheTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvanceConfig(AbstractModel):
    """Advanced configuration set

    """

    def __init__(self):
        r"""
        :param Name: Advanced configuration name
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Name: str
        :param Value: Whether advanced configuration is supported:
`on`: support
`off`: do not support
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthentication(AbstractModel):
    """Timestamp hotlink protection advanced configuration (allowlist feature)

    """

    def __init__(self):
        r"""
        :param Switch: Hotlink protection configuration switch (which can be on or off). If it is enabled, only one mode can and must be configured, while other modes are null.
        :type Switch: str
        :param TypeA: Timestamp hotlink protection advanced configuration mode A
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TypeA: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeA`
        :param TypeB: Timestamp hotlink protection advanced configuration mode B
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TypeB: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeB`
        :param TypeC: Timestamp hotlink protection advanced configuration mode C
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TypeC: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeC`
        :param TypeD: Timestamp hotlink protection advanced configuration mode D
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TypeD: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeD`
        :param TypeE: Timestamp hotlink protection advanced configuration mode E
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TypeE: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeE`
        :param TypeF: Timestamp hotlink protection advanced configuration mode F
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TypeF: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeF`
        """
        self.Switch = None
        self.TypeA = None
        self.TypeB = None
        self.TypeC = None
        self.TypeD = None
        self.TypeE = None
        self.TypeF = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("TypeA") is not None:
            self.TypeA = AdvancedAuthenticationTypeA()
            self.TypeA._deserialize(params.get("TypeA"))
        if params.get("TypeB") is not None:
            self.TypeB = AdvancedAuthenticationTypeB()
            self.TypeB._deserialize(params.get("TypeB"))
        if params.get("TypeC") is not None:
            self.TypeC = AdvancedAuthenticationTypeC()
            self.TypeC._deserialize(params.get("TypeC"))
        if params.get("TypeD") is not None:
            self.TypeD = AdvancedAuthenticationTypeD()
            self.TypeD._deserialize(params.get("TypeD"))
        if params.get("TypeE") is not None:
            self.TypeE = AdvancedAuthenticationTypeE()
            self.TypeE._deserialize(params.get("TypeE"))
        if params.get("TypeF") is not None:
            self.TypeF = AdvancedAuthenticationTypeF()
            self.TypeF._deserialize(params.get("TypeF"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeA(AbstractModel):
    """Timestamp hotlink protection advanced configuration mode A

    """

    def __init__(self):
        r"""
        :param SecretKey: Key used for signature calculation, allowing 6 to 32 bytes of letters and digits.
        :type SecretKey: str
        :param SignParam: Signature field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
        :type SignParam: str
        :param TimeParam: Time field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
        :type TimeParam: str
        :param ExpireTime: Expiration time in seconds
        :type ExpireTime: int
        :param ExpireTimeRequired: Whether the expiration time parameter is required
        :type ExpireTimeRequired: bool
        :param Format: URL composition, e.g., `${private_key}${schema}${host}${full_uri}`.
        :type Format: str
        :param TimeFormat: Time format. Valid values: dec (decimal), hex (hexadecimal).
        :type TimeFormat: str
        :param FailCode: Status code returned when the authentication failed
        :type FailCode: int
        :param ExpireCode: Status code returned when the URL expired
        :type ExpireCode: int
        :param RulePaths: List of URLs to be authenticated
        :type RulePaths: list of str
        :param Transformation: Reserved field
        :type Transformation: int
        """
        self.SecretKey = None
        self.SignParam = None
        self.TimeParam = None
        self.ExpireTime = None
        self.ExpireTimeRequired = None
        self.Format = None
        self.TimeFormat = None
        self.FailCode = None
        self.ExpireCode = None
        self.RulePaths = None
        self.Transformation = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.SignParam = params.get("SignParam")
        self.TimeParam = params.get("TimeParam")
        self.ExpireTime = params.get("ExpireTime")
        self.ExpireTimeRequired = params.get("ExpireTimeRequired")
        self.Format = params.get("Format")
        self.TimeFormat = params.get("TimeFormat")
        self.FailCode = params.get("FailCode")
        self.ExpireCode = params.get("ExpireCode")
        self.RulePaths = params.get("RulePaths")
        self.Transformation = params.get("Transformation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeB(AbstractModel):
    """Timestamp hotlink protection advanced configuration mode B

    """

    def __init__(self):
        r"""
        :param KeyAlpha: Alpha key name
        :type KeyAlpha: str
        :param KeyBeta: Beta key name
        :type KeyBeta: str
        :param KeyGamma: Gamma key name
        :type KeyGamma: str
        :param SignParam: Signature field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
        :type SignParam: str
        :param TimeParam: Time field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
        :type TimeParam: str
        :param ExpireTime: Expiration time in seconds
        :type ExpireTime: int
        :param TimeFormat: Time format. Valid values: dec (decimal), hex (hexadecimal).
        :type TimeFormat: str
        :param FailCode: Status code returned when the authentication failed
        :type FailCode: int
        :param ExpireCode: Status code returned when the URL expired
        :type ExpireCode: int
        :param RulePaths: List of URLs to be authenticated
        :type RulePaths: list of str
        """
        self.KeyAlpha = None
        self.KeyBeta = None
        self.KeyGamma = None
        self.SignParam = None
        self.TimeParam = None
        self.ExpireTime = None
        self.TimeFormat = None
        self.FailCode = None
        self.ExpireCode = None
        self.RulePaths = None


    def _deserialize(self, params):
        self.KeyAlpha = params.get("KeyAlpha")
        self.KeyBeta = params.get("KeyBeta")
        self.KeyGamma = params.get("KeyGamma")
        self.SignParam = params.get("SignParam")
        self.TimeParam = params.get("TimeParam")
        self.ExpireTime = params.get("ExpireTime")
        self.TimeFormat = params.get("TimeFormat")
        self.FailCode = params.get("FailCode")
        self.ExpireCode = params.get("ExpireCode")
        self.RulePaths = params.get("RulePaths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeC(AbstractModel):
    """Timestamp hotlink protection advanced configuration mode C

    """

    def __init__(self):
        r"""
        :param AccessKey: Access key
        :type AccessKey: str
        :param SecretKey: Authentication key
        :type SecretKey: str
        """
        self.AccessKey = None
        self.SecretKey = None


    def _deserialize(self, params):
        self.AccessKey = params.get("AccessKey")
        self.SecretKey = params.get("SecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeD(AbstractModel):
    """Timestamp hotlink protection advanced configuration mode D

    """

    def __init__(self):
        r"""
        :param SecretKey: Key used for signature calculation, allowing 6 to 32 bytes of letters and digits.
        :type SecretKey: str
        :param BackupSecretKey: Alternative key used for authentication after the authentication key (`SecretKey`) failed
        :type BackupSecretKey: str
        :param SignParam: Signature field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
        :type SignParam: str
        :param TimeParam: Time field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
        :type TimeParam: str
        :param ExpireTime: Expiration time in seconds
        :type ExpireTime: int
        :param TimeFormat: Time format. Valid values: dec (decimal), hex (hexadecimal).
        :type TimeFormat: str
        """
        self.SecretKey = None
        self.BackupSecretKey = None
        self.SignParam = None
        self.TimeParam = None
        self.ExpireTime = None
        self.TimeFormat = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.BackupSecretKey = params.get("BackupSecretKey")
        self.SignParam = params.get("SignParam")
        self.TimeParam = params.get("TimeParam")
        self.ExpireTime = params.get("ExpireTime")
        self.TimeFormat = params.get("TimeFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeE(AbstractModel):
    """Timestamp hotlink protection advanced configuration mode E

    """

    def __init__(self):
        r"""
        :param SecretKey: Key used for signature calculation, allowing 6 to 32 bytes of letters and digits.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SecretKey: str
        :param SignParam: Signature field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SignParam: str
        :param AclSignParam: ACL signature field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AclSignParam: str
        :param StartTimeParam: Start time field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type StartTimeParam: str
        :param ExpireTimeParam: Expiration time field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ExpireTimeParam: str
        :param TimeFormat: Time format (dec)
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TimeFormat: str
        """
        self.SecretKey = None
        self.SignParam = None
        self.AclSignParam = None
        self.StartTimeParam = None
        self.ExpireTimeParam = None
        self.TimeFormat = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.SignParam = params.get("SignParam")
        self.AclSignParam = params.get("AclSignParam")
        self.StartTimeParam = params.get("StartTimeParam")
        self.ExpireTimeParam = params.get("ExpireTimeParam")
        self.TimeFormat = params.get("TimeFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeF(AbstractModel):
    """Timestamp hotlink protection advanced authentication configuration mode F (TypeF)

    """

    def __init__(self):
        r"""
        :param SignParam: Signature field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SignParam: str
        :param TimeParam: Time field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TimeParam: str
        :param TransactionParam: Transaction field name in the URI string, starting with a letter, and consisting of letters, digits, and underscores.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TransactionParam: str
        :param SecretKey: CMK used for signature calculation, allowing 6 to 32 bytes of letters and digits.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SecretKey: str
        :param BackupSecretKey: Alternative key used for signature calculation, which is used after the CMK fails in authentication. It allows 6 to 32 bytes of letters and digits.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type BackupSecretKey: str
        """
        self.SignParam = None
        self.TimeParam = None
        self.TransactionParam = None
        self.SecretKey = None
        self.BackupSecretKey = None


    def _deserialize(self, params):
        self.SignParam = params.get("SignParam")
        self.TimeParam = params.get("TimeParam")
        self.TransactionParam = params.get("TransactionParam")
        self.SecretKey = params.get("SecretKey")
        self.BackupSecretKey = params.get("BackupSecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedCache(AbstractModel):
    """Advanced cache expiration configuration (This feature is in beta and not generally available yet.)
    Note: this version does not support setting homepage cache rules.

    """

    def __init__(self):
        r"""
        :param CacheRules: Cache expiration rule
Note: this field may return null, indicating that no valid values can be obtained.
        :type CacheRules: list of AdvanceCacheRule
        :param IgnoreCacheControl: Forced cache configuration
on: enabled
off: disabled
When this is enabled, if the origin server returns no-cache, no-store headers, node caching will still be performed according to the cache expiration rules.
This is disabled by default
Note: this field may return null, indicating that no valid values can be obtained.
        :type IgnoreCacheControl: str
        :param IgnoreSetCookie: Whether to cache the header and body on cache nodes if the origin server returns the header `Set-Cookie`.
on: Enable; do not cache the header and body.
off: Disable; follow the custom cache rules of cache nodes.
It is disabled by default.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type IgnoreSetCookie: str
        """
        self.CacheRules = None
        self.IgnoreCacheControl = None
        self.IgnoreSetCookie = None


    def _deserialize(self, params):
        if params.get("CacheRules") is not None:
            self.CacheRules = []
            for item in params.get("CacheRules"):
                obj = AdvanceCacheRule()
                obj._deserialize(item)
                self.CacheRules.append(obj)
        self.IgnoreCacheControl = params.get("IgnoreCacheControl")
        self.IgnoreSetCookie = params.get("IgnoreSetCookie")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Authentication(AbstractModel):
    """Timestamp hotlink protection configuration

    """

    def __init__(self):
        r"""
        :param Switch: Hotlink protection configuration switch
on: enabled
off: disabled
When this is enabled, one mode needs to be configured. Other modes need to be set to null.
        :type Switch: str
        :param TypeA: Timestamp hotlink protection mode A configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type TypeA: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeA`
        :param TypeB: Timestamp hotlink protection mode B configuration (mode B is being upgraded and is currently not supported)
Note: this field may return null, indicating that no valid values can be obtained.
        :type TypeB: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeB`
        :param TypeC: Timestamp hotlink protection mode C configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type TypeC: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeC`
        :param TypeD: Timestamp hotlink protection mode D configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type TypeD: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeD`
        """
        self.Switch = None
        self.TypeA = None
        self.TypeB = None
        self.TypeC = None
        self.TypeD = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("TypeA") is not None:
            self.TypeA = AuthenticationTypeA()
            self.TypeA._deserialize(params.get("TypeA"))
        if params.get("TypeB") is not None:
            self.TypeB = AuthenticationTypeB()
            self.TypeB._deserialize(params.get("TypeB"))
        if params.get("TypeC") is not None:
            self.TypeC = AuthenticationTypeC()
            self.TypeC._deserialize(params.get("TypeC"))
        if params.get("TypeD") is not None:
            self.TypeD = AuthenticationTypeD()
            self.TypeD._deserialize(params.get("TypeD"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
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
        :param SecretKey: The key for signature calculation
Only digits, upper and lower-case letters are allowed. Length limit: 6-32 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecretKey: str
        :param SignParam: Signature parameter name
Only upper and lower-case letters, digits, and underscores (_) are allowed. It cannot start with a digit. Length limit: 1-100 characters.
        :type SignParam: str
        :param ExpireTime: Signature expiration time
Unit: second. The maximum value is 630720000.
        :type ExpireTime: int
        :param FileExtensions: File extension list settings determining if authentication should be performed
If it contains an asterisk (*), this indicates all files.
        :type FileExtensions: list of str
        :param FilterType: allowlist: indicates that all file types apart from the FileExtensions list are authenticated
blacklist: indicates that only the file types in the FileExtensions list are authenticated
        :type FilterType: str
        """
        self.SecretKey = None
        self.SignParam = None
        self.ExpireTime = None
        self.FileExtensions = None
        self.FilterType = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.SignParam = params.get("SignParam")
        self.ExpireTime = params.get("ExpireTime")
        self.FileExtensions = params.get("FileExtensions")
        self.FilterType = params.get("FilterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthenticationTypeB(AbstractModel):
    """Timestamp hotlink protection mode B configuration (mode B is being upgraded and is currently not supported)

    """

    def __init__(self):
        r"""
        :param SecretKey: The key for signature calculation
Only digits, upper and lower-case letters are allowed. Length limit: 6-32 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecretKey: str
        :param ExpireTime: Signature expiration time
Unit: second. The maximum value is 630720000.
        :type ExpireTime: int
        :param FileExtensions: File extension list settings determining if authentication should be performed
If it contains an asterisk (*), this indicates all files.
        :type FileExtensions: list of str
        :param FilterType: allowlist: indicates that all file types apart from the FileExtensions list are authenticated
blacklist: indicates that only the file types in the FileExtensions list are authenticated
        :type FilterType: str
        """
        self.SecretKey = None
        self.ExpireTime = None
        self.FileExtensions = None
        self.FilterType = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.ExpireTime = params.get("ExpireTime")
        self.FileExtensions = params.get("FileExtensions")
        self.FilterType = params.get("FilterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthenticationTypeC(AbstractModel):
    """Timestamp hotlink protection mode C configuration
    The access URL format of timestamp hotlink protection mode C is as follows: http://DomainName/md5hash/timestamp/FileName
    Here, timestamp is a hexadecimal timestamp in Unix format;
    md5hash: MD5 (custom key + file path + timestamp)

    """

    def __init__(self):
        r"""
        :param SecretKey: The key for signature calculation
Only digits, upper and lower-case letters are allowed. Length limit: 6-32 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecretKey: str
        :param ExpireTime: Signature expiration time
Unit: second. The maximum value is 630720000.
        :type ExpireTime: int
        :param FileExtensions: File extension list settings determining if authentication should be performed
If it contains an asterisk (*), this indicates all files.
        :type FileExtensions: list of str
        :param FilterType: allowlist: indicates that all file types apart from the FileExtensions list are authenticated
blacklist: indicates that only the file types in the FileExtensions list are authenticated
        :type FilterType: str
        :param TimeFormat: Timestamp settings
dec: decimal
hex: hexadecimal
Note: this field may return `null`, indicating that no valid value is obtained.
        :type TimeFormat: str
        """
        self.SecretKey = None
        self.ExpireTime = None
        self.FileExtensions = None
        self.FilterType = None
        self.TimeFormat = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.ExpireTime = params.get("ExpireTime")
        self.FileExtensions = params.get("FileExtensions")
        self.FilterType = params.get("FilterType")
        self.TimeFormat = params.get("TimeFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthenticationTypeD(AbstractModel):
    """Timestamp hotlink protection mode D configuration
    The access URL format of timestamp hotlink protection mode D is as follows: http://DomainName/FileName?sign=md5hash&t=timestamp
    Here, timestamp is a decimal or hexadecimal timestamp in Unix format;
    md5hash: MD5 (custom key + file path + timestamp)

    """

    def __init__(self):
        r"""
        :param SecretKey: The key for signature calculation
Only digits, upper and lower-case letters are allowed. Length limit: 6-32 characters.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecretKey: str
        :param ExpireTime: Signature expiration time
Unit: second. The maximum value is 630720000.
        :type ExpireTime: int
        :param FileExtensions: File extension list settings determining if authentication should be performed
If it contains an asterisk (*), this indicates all files.
        :type FileExtensions: list of str
        :param FilterType: allowlist: indicates that all file types apart from the FileExtensions list are authenticated
blacklist: indicates that only the file types in the FileExtensions list are authenticated
        :type FilterType: str
        :param SignParam: Signature parameter name
Only upper and lower-case letters, digits, and underscores (_) are allowed. It cannot start with a digit. Length limit: 1-100 characters.
        :type SignParam: str
        :param TimeParam: Timestamp parameter name
Only upper and lower-case letters, digits, and underscores (_) are allowed. It cannot start with a digit. Length limit: 1-100 characters.
        :type TimeParam: str
        :param TimeFormat: Timestamp settings
dec: decimal
hex: hexadecimal
        :type TimeFormat: str
        """
        self.SecretKey = None
        self.ExpireTime = None
        self.FileExtensions = None
        self.FilterType = None
        self.SignParam = None
        self.TimeParam = None
        self.TimeFormat = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.ExpireTime = params.get("ExpireTime")
        self.FileExtensions = params.get("FileExtensions")
        self.FilterType = params.get("FilterType")
        self.SignParam = params.get("SignParam")
        self.TimeParam = params.get("TimeParam")
        self.TimeFormat = params.get("TimeFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AwsPrivateAccess(AbstractModel):
    """Origin access authentication for S3 bucket.

    """

    def __init__(self):
        r"""
        :param Switch: Switch, which can be set to on or off.
        :type Switch: str
        :param AccessKey: Access ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccessKey: str
        :param SecretKey: Key.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SecretKey: str
        """
        self.Switch = None
        self.AccessKey = None
        self.SecretKey = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.AccessKey = params.get("AccessKey")
        self.SecretKey = params.get("SecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BandwidthAlert(AbstractModel):
    """Bandwidth cap configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param Switch: Bandwidth cap configuration switch
on: enabled
off: disabled
        :type Switch: str
        :param BpsThreshold: Bandwidth cap threshold (in bps)
Note: this field may return null, indicating that no valid values can be obtained.
        :type BpsThreshold: int
        :param CounterMeasure: Action taken when threshold is reached
RESOLVE_DNS_TO_ORIGIN: requests will be forwarded to the origin server. This is only supported for domain names of external origin.
RETURN_404: a 404 error will be returned for all requests.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CounterMeasure: str
        :param LastTriggerTime: The last time the bandwidth cap threshold was triggered
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastTriggerTime: str
        """
        self.Switch = None
        self.BpsThreshold = None
        self.CounterMeasure = None
        self.LastTriggerTime = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BpsThreshold = params.get("BpsThreshold")
        self.CounterMeasure = params.get("CounterMeasure")
        self.LastTriggerTime = params.get("LastTriggerTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotCookie(AbstractModel):
    """Bot cookie policy

    """

    def __init__(self):
        r"""
        :param Switch: Valid values: `on` and `off`.
        :type Switch: str
        :param RuleType: Rule type, which can only be `all` currently.
        :type RuleType: str
        :param RuleValue: Rule value. Valid value: `*`.
        :type RuleValue: list of str
        :param Action: Action. Valid values: `monitor`, `intercept`, `redirect`, and `captcha`.
        :type Action: str
        :param RedirectUrl: Redirection target page
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RedirectUrl: str
        :param UpdateTime: Update time
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UpdateTime: str
        """
        self.Switch = None
        self.RuleType = None
        self.RuleValue = None
        self.Action = None
        self.RedirectUrl = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.RuleType = params.get("RuleType")
        self.RuleValue = params.get("RuleValue")
        self.Action = params.get("Action")
        self.RedirectUrl = params.get("RedirectUrl")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotJavaScript(AbstractModel):
    """Bot JS policy

    """

    def __init__(self):
        r"""
        :param Switch: Valid values: `on` and `off`.
        :type Switch: str
        :param RuleType: Rule type, which can only be `file` currently.
        :type RuleType: str
        :param RuleValue: Rule value. Valid values: `html` and `htm`.
        :type RuleValue: list of str
        :param Action: Action. Valid values: `monitor`, `intercept`, `redirect`, and `captcha`.
        :type Action: str
        :param RedirectUrl: Redirection target page
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RedirectUrl: str
        :param UpdateTime: Update time
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UpdateTime: str
        """
        self.Switch = None
        self.RuleType = None
        self.RuleValue = None
        self.Action = None
        self.RedirectUrl = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.RuleType = params.get("RuleType")
        self.RuleValue = params.get("RuleValue")
        self.Action = params.get("Action")
        self.RedirectUrl = params.get("RedirectUrl")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BriefDomain(AbstractModel):
    """Basic domain configuration information, including CNAME, status, service type, acceleration region, creation time, last modified time, and origin server configuration.

    """

    def __init__(self):
        r"""
        :param ResourceId: Domain name ID
        :type ResourceId: str
        :param AppId: Tencent Cloud account ID
        :type AppId: int
        :param Domain: Acceleration domain name
        :type Domain: str
        :param Cname: CNAME address of domain name
        :type Cname: str
        :param Status: Acceleration service status
rejected: the domain name is rejected due to expiration/deregistration of its ICP filing
processing: deploying
online: activated
offline: disabled
        :type Status: str
        :param ProjectId: Project ID, which can be viewed on the Tencent Cloud project management page
        :type ProjectId: int
        :param ServiceType: Domain name service type
web: static acceleration
download: download acceleration
media: streaming VOD acceleration
        :type ServiceType: str
        :param CreateTime: Domain name creation time
        :type CreateTime: str
        :param UpdateTime: Last modified time of domain name
        :type UpdateTime: str
        :param Origin: Origin server configuration details
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param Disable: Domain name block status
normal: normal
overdue: the domain name has been disabled due to account arrears. The acceleration service can be resumed after the account is topped up.
malicious: the acceleration service has been forcibly disabled due to detection of malicious behavior.
ddos: the acceleration service has been disabled due to large-scale DDoS attacks to the domain name
idle: no operations or data has been detected for more than 90 days. The domain name is determined to be inactive which automatically disables the acceleration service. You can restart the service.
unlicensed: the acceleration service has been automatically disabled as the domain name has no ICP filing or its ICP filing is deregistered. Service can be resumed after an ICP filing is obtained.
capping: the configured upper limit for bandwidth has been reached.
readonly: the domain name has a special configuration and has been locked.
        :type Disable: str
        :param Area: Acceleration region
mainland: acceleration in Mainland China
overseas: acceleration outside Mainland China
global: global acceleration
        :type Area: str
        :param Readonly: Domain name lock status
normal: not locked
mainland: locked in Mainland China
overseas: locked outside Mainland China
global: locked globally
        :type Readonly: str
        :param Product: Product of the domain name, either `cdn` or `ecdn`.
        :type Product: str
        """
        self.ResourceId = None
        self.AppId = None
        self.Domain = None
        self.Cname = None
        self.Status = None
        self.ProjectId = None
        self.ServiceType = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Origin = None
        self.Disable = None
        self.Area = None
        self.Readonly = None
        self.Product = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.AppId = params.get("AppId")
        self.Domain = params.get("Domain")
        self.Cname = params.get("Cname")
        self.Status = params.get("Status")
        self.ProjectId = params.get("ProjectId")
        self.ServiceType = params.get("ServiceType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        self.Disable = params.get("Disable")
        self.Area = params.get("Area")
        self.Readonly = params.get("Readonly")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Cache(AbstractModel):
    """Node cache expiration time configuration. There are two types of configuration:
    + Basic cache expiration rules configuration
    + Advanced cache expiration rules configuration

    """

    def __init__(self):
        r"""
        :param SimpleCache: Basic cache expiration time configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type SimpleCache: :class:`tencentcloud.cdn.v20180606.models.SimpleCache`
        :param AdvancedCache: Advanced cache expiration configuration (This feature is in beta and not generally available yet.)
Note: this field may return null, indicating that no valid values can be obtained.
        :type AdvancedCache: :class:`tencentcloud.cdn.v20180606.models.AdvancedCache`
        :param RuleCache: Advanced path cache configuration
Note: this field may return null, indicating that no valid value is obtained.
        :type RuleCache: list of RuleCache
        """
        self.SimpleCache = None
        self.AdvancedCache = None
        self.RuleCache = None


    def _deserialize(self, params):
        if params.get("SimpleCache") is not None:
            self.SimpleCache = SimpleCache()
            self.SimpleCache._deserialize(params.get("SimpleCache"))
        if params.get("AdvancedCache") is not None:
            self.AdvancedCache = AdvancedCache()
            self.AdvancedCache._deserialize(params.get("AdvancedCache"))
        if params.get("RuleCache") is not None:
            self.RuleCache = []
            for item in params.get("RuleCache"):
                obj = RuleCache()
                obj._deserialize(item)
                self.RuleCache.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigCache(AbstractModel):
    """Path cache configuration

    """

    def __init__(self):
        r"""
        :param Switch: Cache configuration switch
on: enable
off: disable
Note: this field may return null, indicating that no valid value is obtained.
        :type Switch: str
        :param CacheTime: Cache expiration time settings
Unit: second. The maximum value is 365 days.
Note: this field may return null, indicating that no valid value is obtained.
        :type CacheTime: int
        :param CompareMaxAge: Advanced cache expiration configuration. If this is enabled, the max-age value returned by the origin server will be compared with the cache expiration time set in CacheRules, and the smallest value will be cached on the node.
on: enable
off: disable
This is disabled by default.
Note: this field may return null, indicating that no valid value is obtained.
        :type CompareMaxAge: str
        :param IgnoreCacheControl: Force cache
on: enable
off: disable
This is disabled by default. If enabled, the `no-store` and `no-cache` resources returned from the origin server will be cached according to `CacheRules` rules.
Note: this field may return null, indicating that no valid value is obtained.
        :type IgnoreCacheControl: str
        :param IgnoreSetCookie: Whether to ignore the header and body on cache nodes if the origin server returns the header `Set-Cookie`.
`on`: Ignore; do not cache the header and body.
`off`: Do not ignore; follow the custom cache rules of cache nodes.
It is disabled by default.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IgnoreSetCookie: str
        """
        self.Switch = None
        self.CacheTime = None
        self.CompareMaxAge = None
        self.IgnoreCacheControl = None
        self.IgnoreSetCookie = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CacheTime = params.get("CacheTime")
        self.CompareMaxAge = params.get("CompareMaxAge")
        self.IgnoreCacheControl = params.get("IgnoreCacheControl")
        self.IgnoreSetCookie = params.get("IgnoreSetCookie")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigFollowOrigin(AbstractModel):
    """Path cache configuration follows the origin server configuration.

    """

    def __init__(self):
        r"""
        :param Switch: Follow origin server switch configuration
on: enable
off: disable
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigNoCache(AbstractModel):
    """Path cache/no cache configuration.

    """

    def __init__(self):
        r"""
        :param Switch: No cache configuration switch
on: enable
off: disable
Note: this field may return null, indicating that no valid value is obtained.
        :type Switch: str
        :param Revalidate: Always forwards to the origin server for verification
on: enable
off: disable
This is disabled by default.
Note: this field may return null, indicating that no valid value is obtained.
        :type Revalidate: str
        """
        self.Switch = None
        self.Revalidate = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Revalidate = params.get("Revalidate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheKey(AbstractModel):
    """Cache key configuration (filter parameter configuration)

    """

    def __init__(self):
        r"""
        :param FullUrlCache: Whether to enable full-path cache
on: enable full-path cache (i.e., disable parameter filter)
off: disable full-path cache (i.e., enable parameter filter)
        :type FullUrlCache: str
        :param IgnoreCase: Whether caches are case insensitive
Note: this field may return null, indicating that no valid values can be obtained.
        :type IgnoreCase: str
        :param QueryString: Request parameter contained in `CacheKey`
Note: this field may return null, indicating that no valid values can be obtained.
        :type QueryString: :class:`tencentcloud.cdn.v20180606.models.QueryStringKey`
        :param Cookie: Cookie contained in `CacheKey`
Note: this field may return null, indicating that no valid values can be obtained.
        :type Cookie: :class:`tencentcloud.cdn.v20180606.models.CookieKey`
        :param Header: Request header contained in `CacheKey`
Note: this field may return null, indicating that no valid values can be obtained.
        :type Header: :class:`tencentcloud.cdn.v20180606.models.HeaderKey`
        :param CacheTag: Custom string contained in `CacheKey`
Note: this field may return null, indicating that no valid values can be obtained.
        :type CacheTag: :class:`tencentcloud.cdn.v20180606.models.CacheTagKey`
        :param Scheme: Request protocol contained in `CacheKey`
Note: this field may return null, indicating that no valid values can be obtained.
        :type Scheme: :class:`tencentcloud.cdn.v20180606.models.SchemeKey`
        :param KeyRules: Path-based cache key configuration
Note: this field may return null, indicating that no valid value is obtained.
        :type KeyRules: list of KeyRule
        """
        self.FullUrlCache = None
        self.IgnoreCase = None
        self.QueryString = None
        self.Cookie = None
        self.Header = None
        self.CacheTag = None
        self.Scheme = None
        self.KeyRules = None


    def _deserialize(self, params):
        self.FullUrlCache = params.get("FullUrlCache")
        self.IgnoreCase = params.get("IgnoreCase")
        if params.get("QueryString") is not None:
            self.QueryString = QueryStringKey()
            self.QueryString._deserialize(params.get("QueryString"))
        if params.get("Cookie") is not None:
            self.Cookie = CookieKey()
            self.Cookie._deserialize(params.get("Cookie"))
        if params.get("Header") is not None:
            self.Header = HeaderKey()
            self.Header._deserialize(params.get("Header"))
        if params.get("CacheTag") is not None:
            self.CacheTag = CacheTagKey()
            self.CacheTag._deserialize(params.get("CacheTag"))
        if params.get("Scheme") is not None:
            self.Scheme = SchemeKey()
            self.Scheme._deserialize(params.get("Scheme"))
        if params.get("KeyRules") is not None:
            self.KeyRules = []
            for item in params.get("KeyRules"):
                obj = KeyRule()
                obj._deserialize(item)
                self.KeyRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheOptResult(AbstractModel):
    """Result of blocking/unblocking URLs

    """

    def __init__(self):
        r"""
        :param SuccessUrls: List of succeeded URLs
Note: This field may return null, indicating that no valid values can be obtained.
        :type SuccessUrls: list of str
        :param FailUrls: List of failed URLs
Note: This field may return null, indicating that no valid values can be obtained.
        :type FailUrls: list of str
        """
        self.SuccessUrls = None
        self.FailUrls = None


    def _deserialize(self, params):
        self.SuccessUrls = params.get("SuccessUrls")
        self.FailUrls = params.get("FailUrls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheTagKey(AbstractModel):
    """A part of `CacheKey`

    """

    def __init__(self):
        r"""
        :param Switch: Whether to use `CacheTag` as part of `CacheKey`
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param Value: Value of custom `CacheTag`
Note: this field may return null, indicating that no valid values can be obtained.
        :type Value: str
        """
        self.Switch = None
        self.Value = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CappingRule(AbstractModel):
    """Downstream speed limit configuration rules. Up to 100 entries can be configured.

    """

    def __init__(self):
        r"""
        :param RuleType: Rule types:
`all`: effective for all files
`file`: effective for specified file suffixes
`directory`: effective for specified paths
`path`: effective for specified absolute paths
        :type RuleType: str
        :param RulePaths: Content for each RuleType: 
For `all`, enter an asterisk (*).
For `file`, enter the suffix, such as jpg, txt.
For `directory`, enter the path, such as /xxx/test/.
For `path`, enter the corresponding absolute path, such as /xxx/test.html.
        :type RulePaths: list of str
        :param KBpsThreshold: Downstream speed value settings (in KB/s)
        :type KBpsThreshold: int
        """
        self.RuleType = None
        self.RulePaths = None
        self.KBpsThreshold = None


    def _deserialize(self, params):
        self.RuleType = params.get("RuleType")
        self.RulePaths = params.get("RulePaths")
        self.KBpsThreshold = params.get("KBpsThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdnData(AbstractModel):
    """Detailed access data

    """

    def __init__(self):
        r"""
        :param Metric: Queries the specified metric:
flux: traffic (in bytes)
bandwidth: bandwidth (in bps)
request: number of requests
fluxHitRate: traffic hit rate (in %)
statusCode: status code. The aggregate data for 2xx, 3xx, 4xx, and 5xx status codes will be returned (in entries)
2XX: Returns the aggregate list of 2xx status codes and the data for status codes starting with 2 (in entries)
3XX: Returns the aggregate list of 3xx status codes and the data for status codes starting with 3 (in entries)
4XX: Returns the aggregate list of 4xx status codes and the data for status codes starting with 4 (in entries)
5XX: Returns the aggregate list of 5xx status codes and the data for status codes starting with 5 (in entries)
Alternatively, you can specify a status code for querying.
        :type Metric: str
        :param DetailData: Detailed data combination
        :type DetailData: list of TimestampData
        :param SummarizedData: Aggregate data combination
        :type SummarizedData: :class:`tencentcloud.cdn.v20180606.models.SummarizedData`
        """
        self.Metric = None
        self.DetailData = None
        self.SummarizedData = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        if params.get("DetailData") is not None:
            self.DetailData = []
            for item in params.get("DetailData"):
                obj = TimestampData()
                obj._deserialize(item)
                self.DetailData.append(obj)
        if params.get("SummarizedData") is not None:
            self.SummarizedData = SummarizedData()
            self.SummarizedData._deserialize(params.get("SummarizedData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdnIp(AbstractModel):
    """IP attribute information

    """

    def __init__(self):
        r"""
        :param Ip: IP to be queried
        :type Ip: str
        :param Platform: IP ownership:
yes: Tencent Cloud CDN node
no: non-Tencent Cloud CDN node
        :type Platform: str
        :param Location: Node district/country
unknown: unknown node location
        :type Location: str
        :param History: Node activation and deactivation history
        :type History: list of CdnIpHistory
        :param Area: Node region
mainland: cache node in Mainland China
overseas: cache node outside Mainland China
unknown: service region unknown
        :type Area: str
        :param City: City where the node resides
Note: this field may return `null`, indicating that no valid value is obtained.
        :type City: str
        """
        self.Ip = None
        self.Platform = None
        self.Location = None
        self.History = None
        self.Area = None
        self.City = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Platform = params.get("Platform")
        self.Location = params.get("Location")
        if params.get("History") is not None:
            self.History = []
            for item in params.get("History"):
                obj = CdnIpHistory()
                obj._deserialize(item)
                self.History.append(obj)
        self.Area = params.get("Area")
        self.City = params.get("City")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdnIpHistory(AbstractModel):
    """CDN node activation and deactivation history

    """

    def __init__(self):
        r"""
        :param Status: Operation type
online: node is online
offline: node is offline
        :type Status: str
        :param Datetime: Operation time corresponding to operation type
If this value is null, there are no status change records
Note: this field may return null, indicating that no valid values can be obtained.
        :type Datetime: str
        """
        self.Status = None
        self.Datetime = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Datetime = params.get("Datetime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClientCert(AbstractModel):
    """HTTPS client certificate configuration

    """

    def __init__(self):
        r"""
        :param Certificate: Client Certificate
PEM format, requires Base64 encoding.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Certificate: str
        :param CertName: Client certificate name
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertName: str
        :param ExpireTime: Certificate expiration time
When this is used as an input parameter, it can be left blank.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param DeployTime: Certificate issuance time
When this is used as an input parameter, it can be left blank.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeployTime: str
        """
        self.Certificate = None
        self.CertName = None
        self.ExpireTime = None
        self.DeployTime = None


    def _deserialize(self, params):
        self.Certificate = params.get("Certificate")
        self.CertName = params.get("CertName")
        self.ExpireTime = params.get("ExpireTime")
        self.DeployTime = params.get("DeployTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClsLogObject(AbstractModel):
    """CLS log search object

    """

    def __init__(self):
        r"""
        :param TopicId: Topic ID
        :type TopicId: str
        :param TopicName: Topic name
        :type TopicName: str
        :param Timestamp: Log time
        :type Timestamp: str
        :param Content: Log content
        :type Content: str
        :param Filename: Capture path
        :type Filename: str
        :param Source: Log source device
        :type Source: str
        """
        self.TopicId = None
        self.TopicName = None
        self.Timestamp = None
        self.Content = None
        self.Filename = None
        self.Source = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.Timestamp = params.get("Timestamp")
        self.Content = params.get("Content")
        self.Filename = params.get("Filename")
        self.Source = params.get("Source")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClsSearchLogs(AbstractModel):
    """CLS log search result

    """

    def __init__(self):
        r"""
        :param Context: Cursor for more search results
        :type Context: str
        :param Listover: Whether all search results have been returned
        :type Listover: bool
        :param Results: Log content information
        :type Results: list of ClsLogObject
        """
        self.Context = None
        self.Listover = None
        self.Results = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        self.Listover = params.get("Listover")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = ClsLogObject()
                obj._deserialize(item)
                self.Results.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Compatibility(AbstractModel):
    """Old configuration compatibility check

    """

    def __init__(self):
        r"""
        :param Code: Compatibility flag status code.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Code: int
        """
        self.Code = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Compression(AbstractModel):
    """Smart compression configuration. By default, Gzip compression is performed for files with js, html, css, xml, json, shtml, and htm suffixes, and with sizes between 256 and 2097152 bytes.

    """

    def __init__(self):
        r"""
        :param Switch: Smart compression configuration switch
on: enabled
off: disabled
        :type Switch: str
        :param CompressionRules: Compression rules array
Note: this field may return null, indicating that no valid values can be obtained.
        :type CompressionRules: list of CompressionRule
        """
        self.Switch = None
        self.CompressionRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("CompressionRules") is not None:
            self.CompressionRules = []
            for item in params.get("CompressionRules"):
                obj = CompressionRule()
                obj._deserialize(item)
                self.CompressionRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompressionRule(AbstractModel):
    """Compression rules configuration. Up to 100 entries can be set.

    """

    def __init__(self):
        r"""
        :param Compress: true: must be set as true, enables compression
Note: this field may return null, indicating that no valid values can be obtained.
        :type Compress: bool
        :param FileExtensions: Compress according to the file suffix type
Such as: jpg, txt
Note: this field may return null, indicating that no valid values can be obtained.
        :type FileExtensions: list of str
        :param MinLength: The minimum file size to trigger compression (in bytes)
Note: this field may return null, indicating that no valid values can be obtained.
        :type MinLength: int
        :param MaxLength: The maximum file size to trigger compression (in bytes)
The maximum value is 30 MB
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxLength: int
        :param Algorithms: File compression algorithm
gzip: specifies Gzip compression
brotli: specifies Brotli compression
Note: this field may return null, indicating that no valid values can be obtained.
        :type Algorithms: list of str
        """
        self.Compress = None
        self.FileExtensions = None
        self.MinLength = None
        self.MaxLength = None
        self.Algorithms = None


    def _deserialize(self, params):
        self.Compress = params.get("Compress")
        self.FileExtensions = params.get("FileExtensions")
        self.MinLength = params.get("MinLength")
        self.MaxLength = params.get("MaxLength")
        self.Algorithms = params.get("Algorithms")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CookieKey(AbstractModel):
    """A part of `CacheKey`

    """

    def __init__(self):
        r"""
        :param Switch: Whether to use `Cookie` as part of `CacheKey`. Valid values: on, off
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param Value: Used cookies (separated by ';')
Note: this field may return null, indicating that no valid values can be obtained.
        :type Value: str
        """
        self.Switch = None
        self.Value = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClsLogTopicRequest(AbstractModel):
    """CreateClsLogTopic request structure.

    """

    def __init__(self):
        r"""
        :param TopicName: Log topic name
        :type TopicName: str
        :param LogsetId: Logset ID
        :type LogsetId: str
        :param Channel: Connection channel. Default value: cdn
        :type Channel: str
        :param DomainAreaConfigs: Domain name region information
        :type DomainAreaConfigs: list of DomainAreaConfig
        """
        self.TopicName = None
        self.LogsetId = None
        self.Channel = None
        self.DomainAreaConfigs = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.LogsetId = params.get("LogsetId")
        self.Channel = params.get("Channel")
        if params.get("DomainAreaConfigs") is not None:
            self.DomainAreaConfigs = []
            for item in params.get("DomainAreaConfigs"):
                obj = DomainAreaConfig()
                obj._deserialize(item)
                self.DomainAreaConfigs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClsLogTopicResponse(AbstractModel):
    """CreateClsLogTopic response structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Topic ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TopicId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TopicId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.RequestId = params.get("RequestId")


class CreateScdnFailedLogTaskRequest(AbstractModel):
    """CreateScdnFailedLogTask request structure.

    """

    def __init__(self):
        r"""
        :param TaskId: ID of the failed task to retry
        :type TaskId: str
        :param Area: Region. Valid values: `mainland` and `overseas`.
        :type Area: str
        """
        self.TaskId = None
        self.Area = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScdnFailedLogTaskResponse(AbstractModel):
    """CreateScdnFailedLogTask response structure.

    """

    def __init__(self):
        r"""
        :param Result: Creation result. 
0: Creation succeeded
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteCdnDomainRequest(AbstractModel):
    """DeleteCdnDomain request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain name
The domain name status should be `Disabled`
        :type Domain: str
        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCdnDomainResponse(AbstractModel):
    """DeleteCdnDomain response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClsLogTopicRequest(AbstractModel):
    """DeleteClsLogTopic request structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Log topic ID
        :type TopicId: str
        :param LogsetId: Logset ID
        :type LogsetId: str
        :param Channel: Connection channel. Default value: cdn
        :type Channel: str
        """
        self.TopicId = None
        self.LogsetId = None
        self.Channel = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.LogsetId = params.get("LogsetId")
        self.Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClsLogTopicResponse(AbstractModel):
    """DeleteClsLogTopic response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeBillingDataRequest(AbstractModel):
    """DescribeBillingData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Query start time, e.g., 2018-09-04 10:40:00. The returned result will be later than or equal to the specified time
The time will be rounded forward based on the granularity parameter `Interval`. For example, if the query start time is 2018-09-04 10:40:00 and the query time granularity is 1-hour, the time for the first returned entry will be 2018-09-04 10:00:00
The range between the start time and end time should be less than or equal to 90 days
        :type StartTime: str
        :param EndTime: Query end time, e.g. 2018-09-04 10:40:00. The returned result will be earlier than or equal to the specified time
The time will be rounded forward based on the granularity parameter `Interval`. For example, if the query end time is 2018-09-04 10:40:00 and the query time granularity is 1-hour, the time for the last returned entry will be 2018-09-04 10:00:00
The range between the start time and end time should be less than or equal to 90 days
        :type EndTime: str
        :param Interval: Time granularity, which can be:
min: 1-minute. The query range should be less than or equal to 24 hours
5min: 5-minute. The query range should be less than or equal to 31 days
hour: 1-hour. The query range should be less than or equal to 31 days
day: 1-day. The query period should be greater than 31 days

Currently, data query at 1-minute granularity is not supported if the `Area` field is `overseas`
        :type Interval: str
        :param Domain: Domain name whose billing data is to be queried
        :type Domain: str
        :param Project: Project ID, which can be viewed [here](https://console.cloud.tencent.com/project)
If the `Domain` parameter is populated with specific domain name information, then the billing data of this domain name instead of the specified project will be returned
        :type Project: int
        :param Area: Acceleration region whose billing data is to be queried:
mainland: in the mainland of China
overseas: outside the mainland of China
If this parameter is left empty, `mainland` will be used by default
        :type Area: str
        :param District: Country/region to be queried if `Area` is `overseas`
For district or country/region codes, please see [District Code Mappings](https://intl.cloud.tencent.com/document/product/228/6316?from_cn_redirect=1#.E7.9C.81.E4.BB.BD.E6.98.A0.E5.B0.84)
If this parameter is left empty, all countries/regions will be queried
        :type District: int
        :param Metric: Billing statistics type
flux: bill-by-traffic
bandwidth: bill-by-bandwidth
Default value: `bandwidth`
        :type Metric: str
        :param Product: Specifies the product to query, either `cdn` (default) or `ecdn`.
        :type Product: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.Domain = None
        self.Project = None
        self.Area = None
        self.District = None
        self.Metric = None
        self.Product = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Interval = params.get("Interval")
        self.Domain = params.get("Domain")
        self.Project = params.get("Project")
        self.Area = params.get("Area")
        self.District = params.get("District")
        self.Metric = params.get("Metric")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillingDataResponse(AbstractModel):
    """DescribeBillingData response structure.

    """

    def __init__(self):
        r"""
        :param Interval: Time granularity, which is specified by the parameter passed in during the query:
min: 1-minute
5min: 5-minute
hour: 1-hour
day: 1-day
        :type Interval: str
        :param Data: Data details
        :type Data: list of ResourceBillingData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Interval = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Interval = params.get("Interval")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ResourceBillingData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCdnDataRequest(AbstractModel):
    """DescribeCdnData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Queries start time, such as 2018-09-04 10:40:00; the returned result is later than or equal to the specified time.
According to the specified time granularity, forward rounding is applied; for example, if the query end time is 2018-09-04 10:40:00 and the query time granularity is 1 hour, the time for the first returned entry will be 2018-09-04 10:00:00.
The gap between the start time and end time should be less than or equal to 90 days.
        :type StartTime: str
        :param EndTime: Queries end time, such as 2018-09-04 10:40:00; the returned result is earlier than or equal to the specified time.
According to the specified time granularity, forward rounding is applied; for example, if the query start time is 2018-09-04 10:40:00 and the query time granularity is 1 hour, the time for the last returned entry will be 2018-09-04 10:00:00.
The gap between the start time and end time should be less than or equal to 90 days.
        :type EndTime: str
        :param Metric: Specifies the metric to query, which can be:
`flux`: traffic (in bytes)
`fluxIn`: upstream traffic (in bytes), only used for the `ecdn` product
`fluxOut`: downstream traffic (in bytes), only used for the `ecdn` product
`bandwidth`: bandwidth (in bps)
`bandwidthIn`: upstream bandwidth (in bps), only used for the `ecdn` product
`bandwidthOut`: downstream bandwidth (in bps), only used for the `ecdn` product
`request`: number of requests
`hitRequest`: number of hit requests
`requestHitRate`: request hit rate (in % with two decimal digits)
`hitFlux`: hit traffic (in bytes)
`fluxHitRate`: traffic hit rate (in % with two decimal digits)
`statusCode`: status code. Number of 2xx, 3xx, 4xx, and 5xx status codes returned during the queried period.
`2xx`: lists the number of all status codes starting with **2** returned during the queried period based on the specified interval (if any)
`3xx`: lists the number of all status codes starting with **3** returned during the queried period based on the specified interval (if any)
`4xx`: lists the number of all status codes starting with **4** returned during the queried period based on the specified interval (if any)
`5xx`: lists the number of all status codes starting with **5** returned during the queried period based on the specified interval (if any)
Specifies the status code to query. The return will be empty if the status code has never been generated.
        :type Metric: str
        :param Domains: Specifies the list of domain names to be queried
Up to 30 domain names can be queried at a time
        :type Domains: list of str
        :param Project: Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)
Please note that if domain names are specified, this parameter will be ignored.
        :type Project: int
        :param Interval: Time granularity; valid values:
`min`: data with 1-minute granularity is returned when the queried period is no longer than 24 hours. This value is not supported if the service region you want to query is outside Mainland China;
`5min`: data with 5-minute granularity is returned when the queried period is no longer than 31 days;
`hour`: data with 1-hour granularity is returned when the queried period is no longer than 31 days;
`day`: data with 1-day granularity is returned when the queried period is longer than 31 days.
        :type Interval: str
        :param Detail: The aggregate data for multiple domain names is returned by default (false) during a multi-domain-name query.
You can set it to true to return the details for each Domain (the statusCode metric is currently not supported)
        :type Detail: bool
        :param Isp: Specifies an ISP when you query the CDN data within Mainland China. If this is left blank, all ISPs will be queried.
To view ISP codes, see [ISP Code Mappings](https://intl.cloud.tencent.com/document/product/228/6316?from_cn_redirect=1#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)
If you have specified an ISP, you cannot specify a province or an IP protocol for the same query.
        :type Isp: int
        :param District: Specifies a province when you query the CDN data within Mainland China. If this is left blank, all provinces will be queried.
Specifies a country/region when you query the CDN data outside Mainland China. If this is left blank, all countries/regions will be queried.
To view codes of provinces or countries/regions, see [Province Code Mappings](https://intl.cloud.tencent.com/document/product/228/6316?from_cn_redirect=1#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)
If you have specified a province for your query on CDN data within mainland China, you cannot specify an ISP or an IP protocol for the same query.
        :type District: int
        :param Protocol: Specifies the protocol to be queried; if you leave it blank, all protocols will be queried.
all: All protocols
http: specifies the HTTP metric to be queried
https: specifies the HTTPS metric to be queried
        :type Protocol: str
        :param DataSource: Specifies the data source to be queried, which can be seen as the allowlist function.
        :type DataSource: str
        :param IpProtocol: Specified IP protocol to be queried. If this parameter is left empty, all protocols will be queried
all: all protocols
ipv4: specifies to query IPv4 metrics
ipv6: specifies to query IPv6 metrics
If the IP protocol to be queried is specified, the district and ISP cannot be specified at the same time
Note: non-IPv6 allowlisted users cannot specify `ipv4` and `ipv6` for query
        :type IpProtocol: str
        :param Area: Specifies a service region. If this value is left blank, CDN data within Mainland China will be queried.
`mainland`: specifies to query CDN data within Mainland China;
`overseas`: specifies to query CDN data outside Mainland China.
        :type Area: str
        :param AreaType: Specifies a region type for your query on CDN data outside Mainland China. If this parameter is left blank, data on the service region will be queried. This parameter is valid only when `Area` is `overseas`.
`server`: specifies to query data on the service region where Tencent Cloud CDN nodes are located;
`client`: specifies to query data on the client region where the request devices are located.
        :type AreaType: str
        :param Product: Specifies the product to query, either `cdn` (default) or `ecdn`.
        :type Product: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Metric = None
        self.Domains = None
        self.Project = None
        self.Interval = None
        self.Detail = None
        self.Isp = None
        self.District = None
        self.Protocol = None
        self.DataSource = None
        self.IpProtocol = None
        self.Area = None
        self.AreaType = None
        self.Product = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metric = params.get("Metric")
        self.Domains = params.get("Domains")
        self.Project = params.get("Project")
        self.Interval = params.get("Interval")
        self.Detail = params.get("Detail")
        self.Isp = params.get("Isp")
        self.District = params.get("District")
        self.Protocol = params.get("Protocol")
        self.DataSource = params.get("DataSource")
        self.IpProtocol = params.get("IpProtocol")
        self.Area = params.get("Area")
        self.AreaType = params.get("AreaType")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCdnDataResponse(AbstractModel):
    """DescribeCdnData response structure.

    """

    def __init__(self):
        r"""
        :param Interval: Time granularity of the returned data. Specify one of the following during querying:
min: 1 minute
5min: 5 minutes
hour: 1 hour
day: 1 day
        :type Interval: str
        :param Data: Returned data details of the specified conditional query
        :type Data: list of ResourceData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Interval = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Interval = params.get("Interval")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ResourceData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCdnDomainLogsRequest(AbstractModel):
    """DescribeCdnDomainLogs request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Specifies a domain name for the query
        :type Domain: str
        :param StartTime: Starting time, such as `2019-09-04 00:00:00`
        :type StartTime: str
        :param EndTime: End time, such as `2019-09-04 12:00:00`
        :type EndTime: str
        :param Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param Limit: Limit on paged queries. Default value: 100. Maximum value: 1,000
        :type Limit: int
        :param Area: Specifies a region for the query.
`mainland`: specifies to return the download link of logs on acceleration within Mainland China;
`overseas`: specifies to return the download link of logs on acceleration outside Mainland China;
`global`: specifies to return a download link of logs on acceleration within Mainland China and a link of logs on acceleration outside Mainland China.
Default value: `mainland`.
        :type Area: str
        :param LogType: The type of log to be downloaded.
access: access logs
        :type LogType: str
        """
        self.Domain = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Area = None
        self.LogType = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Area = params.get("Area")
        self.LogType = params.get("LogType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCdnDomainLogsResponse(AbstractModel):
    """DescribeCdnDomainLogs response structure.

    """

    def __init__(self):
        r"""
        :param DomainLogs: Download link of the log package
        :type DomainLogs: list of DomainLog
        :param TotalCount: Total number of entries obtained
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DomainLogs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainLogs") is not None:
            self.DomainLogs = []
            for item in params.get("DomainLogs"):
                obj = DomainLog()
                obj._deserialize(item)
                self.DomainLogs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCdnIpRequest(AbstractModel):
    """DescribeCdnIp request structure.

    """

    def __init__(self):
        r"""
        :param Ips: List of IPs to be queried
        :type Ips: list of str
        """
        self.Ips = None


    def _deserialize(self, params):
        self.Ips = params.get("Ips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCdnIpResponse(AbstractModel):
    """DescribeCdnIp response structure.

    """

    def __init__(self):
        r"""
        :param Ips: Node ownership details
        :type Ips: list of CdnIp
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Ips = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ips") is not None:
            self.Ips = []
            for item in params.get("Ips"):
                obj = CdnIp()
                obj._deserialize(item)
                self.Ips.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCdnOriginIpRequest(AbstractModel):
    """DescribeCdnOriginIp request structure.

    """


class DescribeCdnOriginIpResponse(AbstractModel):
    """DescribeCdnOriginIp response structure.

    """

    def __init__(self):
        r"""
        :param Ips: Intermediate node IP details
        :type Ips: list of OriginIp
        :param TotalCount: Number of intermediate node IPs
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Ips = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ips") is not None:
            self.Ips = []
            for item in params.get("Ips"):
                obj = OriginIp()
                obj._deserialize(item)
                self.Ips.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCertDomainsRequest(AbstractModel):
    """DescribeCertDomains request structure.

    """

    def __init__(self):
        r"""
        :param Cert: Base64-encoded string of certificate in PEM format
        :type Cert: str
        :param CertId: Managed certificate ID. `Cert` and `CertId` cannot be both empty. If they’re both filled in, `CerID` prevails.
        :type CertId: str
        :param Product: Product of the domain name, either `cdn` (default) or `ecdn`.
        :type Product: str
        """
        self.Cert = None
        self.CertId = None
        self.Product = None


    def _deserialize(self, params):
        self.Cert = params.get("Cert")
        self.CertId = params.get("CertId")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertDomainsResponse(AbstractModel):
    """DescribeCertDomains response structure.

    """

    def __init__(self):
        r"""
        :param Domains: List of domain names connected to CDN
Note: this field may return null, indicating that no valid values can be obtained.
        :type Domains: list of str
        :param CertifiedDomains: List of CDN domain names with certificates configured
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertifiedDomains: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Domains = None
        self.CertifiedDomains = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Domains = params.get("Domains")
        self.CertifiedDomains = params.get("CertifiedDomains")
        self.RequestId = params.get("RequestId")


class DescribeDomainsConfigRequest(AbstractModel):
    """DescribeDomainsConfig request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param Limit: Limit on paginated queries. Default value: 100. Maximum value: 1000.
        :type Limit: int
        :param Filters: Query condition filter, complex type.
        :type Filters: list of DomainFilter
        :param Sort: Sorting rules
        :type Sort: :class:`tencentcloud.cdn.v20180606.models.Sort`
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.Sort = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = DomainFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("Sort") is not None:
            self.Sort = Sort()
            self.Sort._deserialize(params.get("Sort"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainsConfigResponse(AbstractModel):
    """DescribeDomainsConfig response structure.

    """

    def __init__(self):
        r"""
        :param Domains: List of domain names
        :type Domains: list of DetailDomain
        :param TotalNumber: The number of domain names that matched the query conditions
Used for paginated queries
        :type TotalNumber: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Domains = None
        self.TotalNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self.Domains = []
            for item in params.get("Domains"):
                obj = DetailDomain()
                obj._deserialize(item)
                self.Domains.append(obj)
        self.TotalNumber = params.get("TotalNumber")
        self.RequestId = params.get("RequestId")


class DescribeDomainsRequest(AbstractModel):
    """DescribeDomains request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param Limit: Limit on paginated queries. Default value: 100. Maximum value: 1000.
        :type Limit: int
        :param Filters: Query condition filter, complex type.
        :type Filters: list of DomainFilter
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = DomainFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainsResponse(AbstractModel):
    """DescribeDomains response structure.

    """

    def __init__(self):
        r"""
        :param Domains: List of domain names
        :type Domains: list of BriefDomain
        :param TotalNumber: The number of domain names that matched the query conditions
Used for paginated queries
        :type TotalNumber: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Domains = None
        self.TotalNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self.Domains = []
            for item in params.get("Domains"):
                obj = BriefDomain()
                obj._deserialize(item)
                self.Domains.append(obj)
        self.TotalNumber = params.get("TotalNumber")
        self.RequestId = params.get("RequestId")


class DescribeIpStatusRequest(AbstractModel):
    """DescribeIpStatus request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Acceleration domain name
        :type Domain: str
        :param Layer: Node type.
edge: edge server
last: intermediate server
If this parameter is left empty, edge server information will be returned by default
        :type Layer: str
        :param Area: Region to be queried.
mainland: domestic nodes
overseas: overseas nodes
global: global nodes
        :type Area: str
        :param Segment: Whether to return a value as an IP range
        :type Segment: bool
        """
        self.Domain = None
        self.Layer = None
        self.Area = None
        self.Segment = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Layer = params.get("Layer")
        self.Area = params.get("Area")
        self.Segment = params.get("Segment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpStatusResponse(AbstractModel):
    """DescribeIpStatus response structure.

    """

    def __init__(self):
        r"""
        :param Ips: Node list
        :type Ips: list of IpStatus
        :param TotalCount: Total number of nodes
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Ips = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ips") is not None:
            self.Ips = []
            for item in params.get("Ips"):
                obj = IpStatus()
                obj._deserialize(item)
                self.Ips.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeIpVisitRequest(AbstractModel):
    """DescribeIpVisit request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Query start time, such as 2018-09-04 10:40:10; the returned result is later than or equal to the specified time.
According to the specified time granularity, forward rounding is applied; for example, if the query start time is 2018-09-04 10:40:10 and the query time granularity is 5 minutes, the time for the first returned entry will be 2018-09-04 10:40:00.
        :type StartTime: str
        :param EndTime: Query end time, such as 2018-09-04 10:40:10; the returned result is earlier than or equal to the specified time.
According to the specified time granularity, forward rounding is applied; for example, if the query start time is 2018-09-04 10:40:10 and the query time granularity is 5 minutes, the time for the last returned entry will be 2018-09-04 10:40:00.
        :type EndTime: str
        :param Domains: Specifies the list of domain names to be queried; up to 30 domain names can be queried at a time.
        :type Domains: list of str
        :param Project: Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)
Please note that if domain names are specified, this parameter will be ignored.
        :type Project: int
        :param Interval: Time granularity, which can be:
5min: 5 minutes. If the query period is within 24 hours, `5min` will be used by default.
day: 1 day. If the query period is longer than 24 hours, `day` will be used by default.
        :type Interval: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Domains = None
        self.Project = None
        self.Interval = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Domains = params.get("Domains")
        self.Project = params.get("Project")
        self.Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpVisitResponse(AbstractModel):
    """DescribeIpVisit response structure.

    """

    def __init__(self):
        r"""
        :param Interval: Time granularity of data statistics, which supports 5min (5 minutes) and day (1 day).
        :type Interval: str
        :param Data: Origin-pull data details of each resource.
        :type Data: list of ResourceData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Interval = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Interval = params.get("Interval")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ResourceData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMapInfoRequest(AbstractModel):
    """DescribeMapInfo request structure.

    """

    def __init__(self):
        r"""
        :param Name: Query type:
`isp`: queries ISP codes
`district`: queries codes of provinces (Mainland China) or countries/regions (outside Mainland China)
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMapInfoResponse(AbstractModel):
    """DescribeMapInfo response structure.

    """

    def __init__(self):
        r"""
        :param MapInfoList: Array of mappings.
        :type MapInfoList: list of MapInfo
        :param ServerRegionRelation: The relationship between server region ID and sub-region ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ServerRegionRelation: list of RegionMapRelation
        :param ClientRegionRelation: The relationship between client region ID and sub-region ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClientRegionRelation: list of RegionMapRelation
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MapInfoList = None
        self.ServerRegionRelation = None
        self.ClientRegionRelation = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MapInfoList") is not None:
            self.MapInfoList = []
            for item in params.get("MapInfoList"):
                obj = MapInfo()
                obj._deserialize(item)
                self.MapInfoList.append(obj)
        if params.get("ServerRegionRelation") is not None:
            self.ServerRegionRelation = []
            for item in params.get("ServerRegionRelation"):
                obj = RegionMapRelation()
                obj._deserialize(item)
                self.ServerRegionRelation.append(obj)
        if params.get("ClientRegionRelation") is not None:
            self.ClientRegionRelation = []
            for item in params.get("ClientRegionRelation"):
                obj = RegionMapRelation()
                obj._deserialize(item)
                self.ClientRegionRelation.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOriginDataRequest(AbstractModel):
    """DescribeOriginData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Query start time, such as 2018-09-04 10:40:00; the returned result is later than or equal to the specified time.
According to the specified time granularity, forward rounding is applied; for example, if the query end time is 2018-09-04 10:40:00 and the query time granularity is 1 hour, the time for the first returned entry will be 2018-09-04 10:00:00.
The gap between the start time and end time should be less than or equal to 90 days.
        :type StartTime: str
        :param EndTime: Query end time, such as 2018-09-04 10:40:00; the returned result is earlier than or equal to the specified time.
According to the specified time granularity, forward rounding is applied; for example, if the query start time is 2018-09-04 10:40:00 and the query time granularity is 1 hour, the time for the last returned entry will be 2018-09-04 10:00:00.
The gap between the start time and end time should be less than or equal to 90 days.
        :type EndTime: str
        :param Metric: Specifies the query metric, which can be:
flux: origin-pull traffic (in bytes)
bandwidth: origin-pull bandwidth (in bps)
request: number of origin-pull requests
failRequest: number of failed origin-pull requests
failRate: origin-pull failure rate (in %)
statusCode: origin-pull status code. The aggregate data for 2xx, 3xx, 4xx, and 5xx origin-pull status codes will be returned (in entries)
2xx: Returns the aggregate list of 2xx origin-pull status codes and the data for origin-pull status codes starting with 2 (in entries)
3xx: Returns the aggregate list of 3xx origin-pull status codes and the data for origin-pull status codes starting with 3 (in entries)
4xx: Returns the aggregate list of 4xx origin-pull status codes and the data for origin-pull status codes starting with 4 (in entries)
5xx: Returns the aggregate list of 5xx origin-pull status codes and the data for origin-pull status codes starting with 5 (in entries)
It is supported to specify a status code for query. The return will be empty if the status code has never been generated.
        :type Metric: str
        :param Domains: Specifies the list of domain names to be queried; up to 30 domain names can be queried at a time.
        :type Domains: list of str
        :param Project: Project ID, which can be viewed [here](https://console.cloud.tencent.com/project)
If the domain name is not specified, the specified project will be queried. Up to 30 acceleration domain names can be queried at a time
If the domain name information is specified, the domain name will prevail
        :type Project: int
        :param Interval: Time granularity; valid values:
`min`: data with 1-minute granularity is returned when the queried period is no longer than 24 hours. This value is not supported if the service region you want to query is outside Mainland China;
`5min`: data with 5-minute granularity is returned when the queried period is no longer than 31 days;
`hour`: data with 1-hour granularity is returned when the queried period is no longer than 31 days;
`day`: data with 1-day granularity is returned when the queried period is longer than 31 days.
        :type Interval: str
        :param Detail: The aggregate data for multiple domain names is returned by default (false) when multiple `Domains` are passed in.
You can set it to true to return the details for each Domain (the statusCode metric is currently not supported)
        :type Detail: bool
        :param Area: Specifies a service region. If this value is left blank, CDN data within Mainland China will be queried.
`mainland`: specifies to query CDN data within Mainland China;
`overseas`: specifies to query CDN data outside Mainland China.
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Metric = None
        self.Domains = None
        self.Project = None
        self.Interval = None
        self.Detail = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metric = params.get("Metric")
        self.Domains = params.get("Domains")
        self.Project = params.get("Project")
        self.Interval = params.get("Interval")
        self.Detail = params.get("Detail")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOriginDataResponse(AbstractModel):
    """DescribeOriginData response structure.

    """

    def __init__(self):
        r"""
        :param Interval: Time granularity of data statistics, which supports min (1 minute), 5min (5 minutes), hour (1 hour), and day (1 day).
        :type Interval: str
        :param Data: Origin-pull data details of each resource.
        :type Data: list of ResourceOriginData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Interval = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Interval = params.get("Interval")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ResourceOriginData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePayTypeRequest(AbstractModel):
    """DescribePayType request structure.

    """

    def __init__(self):
        r"""
        :param Area: Specifies a service region.
`mainland`: queries billing methods within Mainland China;
`overseas`: queries billing methods outside Mainland China.
Default value: `mainland`.
        :type Area: str
        :param Product: Specifies the product to query, either `cdn` (default) or `ecdn`.
        :type Product: str
        """
        self.Area = None
        self.Product = None


    def _deserialize(self, params):
        self.Area = params.get("Area")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePayTypeResponse(AbstractModel):
    """DescribePayType response structure.

    """

    def __init__(self):
        r"""
        :param PayType: Billing modes:
`flux`: bill-by-traffic
`bandwidth`: bill-by-bandwidth
`request`: bill-by-request
In case the billing mode is changed in the day, if there is bandwidth consumption occurred in the current day, the billing mode returned is the new billing mode for the next day. If no bandwidth consumption occurs, it indicates the current billing mode.
        :type PayType: str
        :param BillingCycle: Billing cycle:
day: daily settlement
month: monthly settlement
        :type BillingCycle: str
        :param StatType: `monthMax`: billed by the monthly average of daily peak traffic (monthly settlement)
`day95`: billed by the daily 95th percentile bandwidth (monthly settlement)
`month95`: billed by the monthly 95th percentile bandwidth (monthly settlement)
`sum`: billed by the total traffic/total requests (daily or monthly settlement)
`max`: billed by the peak bandwidth (daily settlement)
        :type StatType: str
        :param RegionType: Billing method outside Mainland China:
`all`: unified billing for all regions
`multiple`: separate billing for different regions
        :type RegionType: str
        :param CurrentPayType: The current billing mode in effect:
`flux`: bill-by-traffic
`bandwidth`: bill-by-bandwidth
`request`: bill-by-request
        :type CurrentPayType: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PayType = None
        self.BillingCycle = None
        self.StatType = None
        self.RegionType = None
        self.CurrentPayType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PayType = params.get("PayType")
        self.BillingCycle = params.get("BillingCycle")
        self.StatType = params.get("StatType")
        self.RegionType = params.get("RegionType")
        self.CurrentPayType = params.get("CurrentPayType")
        self.RequestId = params.get("RequestId")


class DescribePurgeQuotaRequest(AbstractModel):
    """DescribePurgeQuota request structure.

    """


class DescribePurgeQuotaResponse(AbstractModel):
    """DescribePurgeQuota response structure.

    """

    def __init__(self):
        r"""
        :param UrlPurge: URL purge usage and quota.
        :type UrlPurge: list of Quota
        :param PathPurge: Directory purge usage and quota.
        :type PathPurge: list of Quota
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UrlPurge = None
        self.PathPurge = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UrlPurge") is not None:
            self.UrlPurge = []
            for item in params.get("UrlPurge"):
                obj = Quota()
                obj._deserialize(item)
                self.UrlPurge.append(obj)
        if params.get("PathPurge") is not None:
            self.PathPurge = []
            for item in params.get("PathPurge"):
                obj = Quota()
                obj._deserialize(item)
                self.PathPurge.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePurgeTasksRequest(AbstractModel):
    """DescribePurgeTasks request structure.

    """

    def __init__(self):
        r"""
        :param PurgeType: Specifies a purge type:
`url`: URL purge record
`path`: Directory purge record
        :type PurgeType: str
        :param StartTime: Specifies the starting time of the period you want to query, such as `2018-08-08 00:00:00`
        :type StartTime: str
        :param EndTime: Specifies the end time of the period you want to query, such as 2018-08-08 23:59:59
        :type EndTime: str
        :param TaskId: Specifies a task ID when you want to query by task ID.
You must specify either a task ID or a starting time for your query.
        :type TaskId: str
        :param Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param Limit: Limit on paged queries. Default value: 20
        :type Limit: int
        :param Keyword: You can filter the results by domain name or a complete URL beginning with `http(s)://`
        :type Keyword: str
        :param Status: Specifies a task state for your query:
`fail`: purge failed
`done`: purge succeeded
`process`: purge in progress
        :type Status: str
        :param Area: Specifies a purge region for your query:
`mainland`: within Mainland China
`overseas`: outside Mainland China
`global`: global
        :type Area: str
        """
        self.PurgeType = None
        self.StartTime = None
        self.EndTime = None
        self.TaskId = None
        self.Offset = None
        self.Limit = None
        self.Keyword = None
        self.Status = None
        self.Area = None


    def _deserialize(self, params):
        self.PurgeType = params.get("PurgeType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TaskId = params.get("TaskId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Keyword = params.get("Keyword")
        self.Status = params.get("Status")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePurgeTasksResponse(AbstractModel):
    """DescribePurgeTasks response structure.

    """

    def __init__(self):
        r"""
        :param PurgeLogs: Detailed purge record.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PurgeLogs: list of PurgeTask
        :param TotalCount: Total number of tasks, which is used for pagination.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PurgeLogs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PurgeLogs") is not None:
            self.PurgeLogs = []
            for item in params.get("PurgeLogs"):
                obj = PurgeTask()
                obj._deserialize(item)
                self.PurgeLogs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribePushQuotaRequest(AbstractModel):
    """DescribePushQuota request structure.

    """


class DescribePushQuotaResponse(AbstractModel):
    """DescribePushQuota response structure.

    """

    def __init__(self):
        r"""
        :param UrlPush: URL prefetch usage and quota.
        :type UrlPush: list of Quota
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UrlPush = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UrlPush") is not None:
            self.UrlPush = []
            for item in params.get("UrlPush"):
                obj = Quota()
                obj._deserialize(item)
                self.UrlPush.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePushTasksRequest(AbstractModel):
    """DescribePushTasks request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Starting time, such as `2018-08-08 00:00:00`
        :type StartTime: str
        :param EndTime: End time, such as `2018-08-08 23:59:59`
        :type EndTime: str
        :param TaskId: Specifies a task ID for your query.
You must specify either a task ID or a starting time.
        :type TaskId: str
        :param Keyword: Specifies a keyword for your query. Please enter a domain name or a complete URL beginning with `http(s)://`
        :type Keyword: str
        :param Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param Limit: Limit on paged queries. Default value: 20
        :type Limit: int
        :param Area: Specifies a region for your query:
`mainland`: within Mainland China
`overseas`: outside Mainland China
`global`: global
        :type Area: str
        :param Status: Specifies a task state for your query:
`fail`: prefetch failed
`done`: prefetch succeeded
`process`: prefetch in progress
        :type Status: str
        """
        self.StartTime = None
        self.EndTime = None
        self.TaskId = None
        self.Keyword = None
        self.Offset = None
        self.Limit = None
        self.Area = None
        self.Status = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TaskId = params.get("TaskId")
        self.Keyword = params.get("Keyword")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Area = params.get("Area")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePushTasksResponse(AbstractModel):
    """DescribePushTasks response structure.

    """

    def __init__(self):
        r"""
        :param PushLogs: Prefetch history
Note: This field may return null, indicating that no valid values can be obtained.
        :type PushLogs: list of PushTask
        :param TotalCount: Total number of tasks, which is used for pagination.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.PushLogs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PushLogs") is not None:
            self.PushLogs = []
            for item in params.get("PushLogs"):
                obj = PushTask()
                obj._deserialize(item)
                self.PushLogs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeReportDataRequest(AbstractModel):
    """DescribeReportData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Query the start time in the format of `yyyy-MM-dd`
If the report type is `daily`, the start time and end time must be the same day.
If the report type is `weekly`, the start time must be Monday and the end time must be the Sunday of the same week.
If the report type is `monthly`, the start time must be the first day of the calendar month and the end time must be the last day of the same calendar month.
        :type StartTime: str
        :param EndTime: Query the end time in the format of `yyyy-MM-dd`
If the report type is `daily`, the start time and end time must be of the same day.
If the report type is `weekly`, the start time must be Monday and the end time must be the Sunday of the same week.
If the report type is `monthly`, the start time must be the first day of the calendar month and the end time must be the last day of the same calendar month.
        :type EndTime: str
        :param ReportType: Report type
daily: daily report
weekly: weekly report (Monday to Sunday)
monthly: monthly report (calendar month)
        :type ReportType: str
        :param Area: Domain name acceleration region
mainland: in Mainland China
overseas: outside Mainland China
        :type Area: str
        :param Offset: Offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of data entries. Default value: 1000.
        :type Limit: int
        :param Project: Filters by project ID
        :type Project: int
        """
        self.StartTime = None
        self.EndTime = None
        self.ReportType = None
        self.Area = None
        self.Offset = None
        self.Limit = None
        self.Project = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ReportType = params.get("ReportType")
        self.Area = params.get("Area")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Project = params.get("Project")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReportDataResponse(AbstractModel):
    """DescribeReportData response structure.

    """

    def __init__(self):
        r"""
        :param DomainReport: Domain name-level data details.
        :type DomainReport: list of ReportData
        :param ProjectReport: Project-level data details
        :type ProjectReport: list of ReportData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DomainReport = None
        self.ProjectReport = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainReport") is not None:
            self.DomainReport = []
            for item in params.get("DomainReport"):
                obj = ReportData()
                obj._deserialize(item)
                self.DomainReport.append(obj)
        if params.get("ProjectReport") is not None:
            self.ProjectReport = []
            for item in params.get("ProjectReport"):
                obj = ReportData()
                obj._deserialize(item)
                self.ProjectReport.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUrlViolationsRequest(AbstractModel):
    """DescribeUrlViolations request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param Limit: Limit on paginated queries. Default value: 100.
        :type Limit: int
        :param Domains: Specified domain name query
        :type Domains: list of str
        """
        self.Offset = None
        self.Limit = None
        self.Domains = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUrlViolationsResponse(AbstractModel):
    """DescribeUrlViolations response structure.

    """

    def __init__(self):
        r"""
        :param UrlRecordList: Details of URLs in violation
Note: this field may return null, indicating that no valid values can be obtained.
        :type UrlRecordList: list of ViolationUrl
        :param TotalCount: Total number of records, which is used for pagination.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UrlRecordList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UrlRecordList") is not None:
            self.UrlRecordList = []
            for item in params.get("UrlRecordList"):
                obj = ViolationUrl()
                obj._deserialize(item)
                self.UrlRecordList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DetailDomain(AbstractModel):
    """Complete acceleration domain configuration information

    """

    def __init__(self):
        r"""
        :param ResourceId: Domain name ID
        :type ResourceId: str
        :param AppId: Tencent Cloud account ID
        :type AppId: int
        :param Domain: Acceleration domain name
        :type Domain: str
        :param Cname: CNAME address of domain name
Note: this field may return null, indicating that no valid values can be obtained.
        :type Cname: str
        :param Status: Acceleration service status
rejected: the domain name is rejected due to expiration/deregistration of its ICP filing
processing: deploying
online: activated
offline: disabled
        :type Status: str
        :param ProjectId: Project ID, which can be viewed on the Tencent Cloud project management page
        :type ProjectId: int
        :param ServiceType: Domain name service type
web: static acceleration
download: download acceleration
media: streaming VOD acceleration
        :type ServiceType: str
        :param CreateTime: Domain name creation time
        :type CreateTime: str
        :param UpdateTime: Last modified time of domain name
        :type UpdateTime: str
        :param Origin: Origin server configuration
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param IpFilter: IP blacklist/whitelist configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param IpFreqLimit: IP access frequency limit configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param StatusCodeCache: Status code cache configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param Compression: Smart compression configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param BandwidthAlert: Bandwidth cap configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param RangeOriginPull: Range GETs configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param FollowRedirect: 301/302 origin-pull follow-redirect configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param ErrorPage: Custom error page configuration (in beta)
Note: this field may return null, indicating that no valid values can be obtained.
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param RequestHeader: Custom request header configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param ResponseHeader: Custom response header configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param DownstreamCapping: Single-link downstream speed limit configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param CacheKey: Configuration of cache with/without parameter
Note: this field may return null, indicating that no valid values can be obtained.
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param ResponseHeaderCache: Origin server header cache configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param VideoSeek: Video dragging configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        :param Cache: Node cache expiration rule configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param OriginPullOptimization: Cross-border linkage optimization configuration (in beta)
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param Https: HTTPS acceleration configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param Authentication: Timestamp hotlink protection configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param Seo: SEO configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param Disable: Domain name block status
normal: normal
overdue: the domain name has been disabled due to account arrears. The acceleration service can be resumed after the account is topped up.
malicious: the acceleration service has been forcibly disabled due to detection of malicious behavior.
ddos: the acceleration service has been disabled due to large-scale DDoS attacks to the domain name
idle: no operations or data has been detected for more than 90 days. The domain name is determined to be inactive which automatically disables the acceleration service. You can restart the service.
unlicensed: the acceleration service has been automatically disabled as the domain name has no ICP filing or its ICP filing is deregistered. Service can be resumed after an ICP filing is obtained.
capping: the configured upper limit for bandwidth has been reached.
readonly: the domain name has a special configuration and has been locked.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Disable: str
        :param ForceRedirect: Access protocol forced redirect configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param Referer: Referer hotlink protection configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param MaxAge: Browser cache expiration rule configuration (in beta)
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param Ipv6: IPv6 origin-pull configuration (in beta)
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Ipv6: :class:`tencentcloud.cdn.v20180606.models.Ipv6`
        :param Compatibility: Backwards compatibility configuration (compatibility field for internal use)
Note: this field may return null, indicating that no valid values can be obtained.
        :type Compatibility: :class:`tencentcloud.cdn.v20180606.models.Compatibility`
        :param SpecificConfig: Region-specific configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type SpecificConfig: :class:`tencentcloud.cdn.v20180606.models.SpecificConfig`
        :param Area: Acceleration region
mainland: acceleration in Mainland China
overseas: acceleration outside Mainland China
global: global acceleration
Note: this field may return null, indicating that no valid values can be obtained.
        :type Area: str
        :param Readonly: Domain name lock status
normal: not locked
mainland: locked in Mainland China
overseas: locked outside Mainland China
global: locked globally
Note: this field may return null, indicating that no valid values can be obtained.
        :type Readonly: str
        :param OriginPullTimeout: Origin-pull timeout configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginPullTimeout: :class:`tencentcloud.cdn.v20180606.models.OriginPullTimeout`
        :param AwsPrivateAccess: S3 bucket origin access authentication configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type AwsPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`
        :param SecurityConfig: SCDN configuration
        :type SecurityConfig: :class:`tencentcloud.cdn.v20180606.models.SecurityConfig`
        :param ImageOptimization: Image Optimization configuration
        :type ImageOptimization: :class:`tencentcloud.cdn.v20180606.models.ImageOptimization`
        :param UserAgentFilter: `UA` blocklist/allowlist configuration
        :type UserAgentFilter: :class:`tencentcloud.cdn.v20180606.models.UserAgentFilter`
        :param AccessControl: Access control
        :type AccessControl: :class:`tencentcloud.cdn.v20180606.models.AccessControl`
        :param Advance: Whether to support advanced configuration items
on: supported
off: not supported
Note: this field may return null, indicating that no valid values can be obtained.
        :type Advance: str
        :param UrlRedirect: URL redirect configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type UrlRedirect: :class:`tencentcloud.cdn.v20180606.models.UrlRedirect`
        :param AccessPort: Access port configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type AccessPort: list of int
        :param Tag: Tag configuration
Note: this field may return null, indicating that no valid value is obtained.
        :type Tag: list of Tag
        :param AdvancedAuthentication: Timestamp hotlink protection advanced configuration (allowlist feature)
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AdvancedAuthentication: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthentication`
        :param OriginAuthentication: Origin-pull authentication advanced configuration (allowlist feature)
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type OriginAuthentication: :class:`tencentcloud.cdn.v20180606.models.OriginAuthentication`
        :param Ipv6Access: IPv6 access configuration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Ipv6Access: :class:`tencentcloud.cdn.v20180606.models.Ipv6Access`
        :param AdvanceSet: Advanced configuration set
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AdvanceSet: list of AdvanceConfig
        :param OfflineCache: Offline cache
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type OfflineCache: :class:`tencentcloud.cdn.v20180606.models.OfflineCache`
        :param OriginCombine: Merging pull requests
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type OriginCombine: :class:`tencentcloud.cdn.v20180606.models.OriginCombine`
        :param PostMaxSize: POST request configuration item
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type PostMaxSize: :class:`tencentcloud.cdn.v20180606.models.PostSize`
        :param Quic: QUIC configuration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Quic: :class:`tencentcloud.cdn.v20180606.models.Quic`
        :param OssPrivateAccess: Access authentication for OSS origin
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type OssPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.OssPrivateAccess`
        :param WebSocket: WebSocket configuration.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type WebSocket: :class:`tencentcloud.cdn.v20180606.models.WebSocket`
        """
        self.ResourceId = None
        self.AppId = None
        self.Domain = None
        self.Cname = None
        self.Status = None
        self.ProjectId = None
        self.ServiceType = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Origin = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.StatusCodeCache = None
        self.Compression = None
        self.BandwidthAlert = None
        self.RangeOriginPull = None
        self.FollowRedirect = None
        self.ErrorPage = None
        self.RequestHeader = None
        self.ResponseHeader = None
        self.DownstreamCapping = None
        self.CacheKey = None
        self.ResponseHeaderCache = None
        self.VideoSeek = None
        self.Cache = None
        self.OriginPullOptimization = None
        self.Https = None
        self.Authentication = None
        self.Seo = None
        self.Disable = None
        self.ForceRedirect = None
        self.Referer = None
        self.MaxAge = None
        self.Ipv6 = None
        self.Compatibility = None
        self.SpecificConfig = None
        self.Area = None
        self.Readonly = None
        self.OriginPullTimeout = None
        self.AwsPrivateAccess = None
        self.SecurityConfig = None
        self.ImageOptimization = None
        self.UserAgentFilter = None
        self.AccessControl = None
        self.Advance = None
        self.UrlRedirect = None
        self.AccessPort = None
        self.Tag = None
        self.AdvancedAuthentication = None
        self.OriginAuthentication = None
        self.Ipv6Access = None
        self.AdvanceSet = None
        self.OfflineCache = None
        self.OriginCombine = None
        self.PostMaxSize = None
        self.Quic = None
        self.OssPrivateAccess = None
        self.WebSocket = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.AppId = params.get("AppId")
        self.Domain = params.get("Domain")
        self.Cname = params.get("Cname")
        self.Status = params.get("Status")
        self.ProjectId = params.get("ProjectId")
        self.ServiceType = params.get("ServiceType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("StatusCodeCache") is not None:
            self.StatusCodeCache = StatusCodeCache()
            self.StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("BandwidthAlert") is not None:
            self.BandwidthAlert = BandwidthAlert()
            self.BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("RangeOriginPull") is not None:
            self.RangeOriginPull = RangeOriginPull()
            self.RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("FollowRedirect") is not None:
            self.FollowRedirect = FollowRedirect()
            self.FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("RequestHeader") is not None:
            self.RequestHeader = RequestHeader()
            self.RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("DownstreamCapping") is not None:
            self.DownstreamCapping = DownstreamCapping()
            self.DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("ResponseHeaderCache") is not None:
            self.ResponseHeaderCache = ResponseHeaderCache()
            self.ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("VideoSeek") is not None:
            self.VideoSeek = VideoSeek()
            self.VideoSeek._deserialize(params.get("VideoSeek"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("OriginPullOptimization") is not None:
            self.OriginPullOptimization = OriginPullOptimization()
            self.OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("Authentication") is not None:
            self.Authentication = Authentication()
            self.Authentication._deserialize(params.get("Authentication"))
        if params.get("Seo") is not None:
            self.Seo = Seo()
            self.Seo._deserialize(params.get("Seo"))
        self.Disable = params.get("Disable")
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Referer") is not None:
            self.Referer = Referer()
            self.Referer._deserialize(params.get("Referer"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        if params.get("Compatibility") is not None:
            self.Compatibility = Compatibility()
            self.Compatibility._deserialize(params.get("Compatibility"))
        if params.get("SpecificConfig") is not None:
            self.SpecificConfig = SpecificConfig()
            self.SpecificConfig._deserialize(params.get("SpecificConfig"))
        self.Area = params.get("Area")
        self.Readonly = params.get("Readonly")
        if params.get("OriginPullTimeout") is not None:
            self.OriginPullTimeout = OriginPullTimeout()
            self.OriginPullTimeout._deserialize(params.get("OriginPullTimeout"))
        if params.get("AwsPrivateAccess") is not None:
            self.AwsPrivateAccess = AwsPrivateAccess()
            self.AwsPrivateAccess._deserialize(params.get("AwsPrivateAccess"))
        if params.get("SecurityConfig") is not None:
            self.SecurityConfig = SecurityConfig()
            self.SecurityConfig._deserialize(params.get("SecurityConfig"))
        if params.get("ImageOptimization") is not None:
            self.ImageOptimization = ImageOptimization()
            self.ImageOptimization._deserialize(params.get("ImageOptimization"))
        if params.get("UserAgentFilter") is not None:
            self.UserAgentFilter = UserAgentFilter()
            self.UserAgentFilter._deserialize(params.get("UserAgentFilter"))
        if params.get("AccessControl") is not None:
            self.AccessControl = AccessControl()
            self.AccessControl._deserialize(params.get("AccessControl"))
        self.Advance = params.get("Advance")
        if params.get("UrlRedirect") is not None:
            self.UrlRedirect = UrlRedirect()
            self.UrlRedirect._deserialize(params.get("UrlRedirect"))
        self.AccessPort = params.get("AccessPort")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self.Tag.append(obj)
        if params.get("AdvancedAuthentication") is not None:
            self.AdvancedAuthentication = AdvancedAuthentication()
            self.AdvancedAuthentication._deserialize(params.get("AdvancedAuthentication"))
        if params.get("OriginAuthentication") is not None:
            self.OriginAuthentication = OriginAuthentication()
            self.OriginAuthentication._deserialize(params.get("OriginAuthentication"))
        if params.get("Ipv6Access") is not None:
            self.Ipv6Access = Ipv6Access()
            self.Ipv6Access._deserialize(params.get("Ipv6Access"))
        if params.get("AdvanceSet") is not None:
            self.AdvanceSet = []
            for item in params.get("AdvanceSet"):
                obj = AdvanceConfig()
                obj._deserialize(item)
                self.AdvanceSet.append(obj)
        if params.get("OfflineCache") is not None:
            self.OfflineCache = OfflineCache()
            self.OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("OriginCombine") is not None:
            self.OriginCombine = OriginCombine()
            self.OriginCombine._deserialize(params.get("OriginCombine"))
        if params.get("PostMaxSize") is not None:
            self.PostMaxSize = PostSize()
            self.PostMaxSize._deserialize(params.get("PostMaxSize"))
        if params.get("Quic") is not None:
            self.Quic = Quic()
            self.Quic._deserialize(params.get("Quic"))
        if params.get("OssPrivateAccess") is not None:
            self.OssPrivateAccess = OssPrivateAccess()
            self.OssPrivateAccess._deserialize(params.get("OssPrivateAccess"))
        if params.get("WebSocket") is not None:
            self.WebSocket = WebSocket()
            self.WebSocket._deserialize(params.get("WebSocket"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableCachesRequest(AbstractModel):
    """DisableCaches request structure.

    """

    def __init__(self):
        r"""
        :param Urls: List of URLs to be blocked (URLs must contain `http://` or `https://`).
Up to 100 entries can be submitted at a time and 3,000 entries per day.
        :type Urls: list of str
        """
        self.Urls = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableCachesResponse(AbstractModel):
    """DisableCaches response structure.

    """

    def __init__(self):
        r"""
        :param CacheOptResult: Submission result
Note: This field may return null, indicating that no valid values can be obtained.
        :type CacheOptResult: :class:`tencentcloud.cdn.v20180606.models.CacheOptResult`
        :param TaskId: Task ID.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CacheOptResult = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CacheOptResult") is not None:
            self.CacheOptResult = CacheOptResult()
            self.CacheOptResult._deserialize(params.get("CacheOptResult"))
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DisableClsLogTopicRequest(AbstractModel):
    """DisableClsLogTopic request structure.

    """

    def __init__(self):
        r"""
        :param LogsetId: Logset ID
        :type LogsetId: str
        :param TopicId: Log topic ID
        :type TopicId: str
        :param Channel: Connection channel. Default value: cdn
        :type Channel: str
        """
        self.LogsetId = None
        self.TopicId = None
        self.Channel = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        self.Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableClsLogTopicResponse(AbstractModel):
    """DisableClsLogTopic response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DomainAreaConfig(AbstractModel):
    """Domain name region configuration

    """

    def __init__(self):
        r"""
        :param Domain: Domain name
        :type Domain: str
        :param Area: Region list, where the element can be `mainland/overseas`
        :type Area: list of str
        """
        self.Domain = None
        self.Area = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainFilter(AbstractModel):
    """Filter conditions for domain name query.

    """

    def __init__(self):
        r"""
        :param Name: Filters field name, which includes:
- `origin`: primary origin server.
- `domain`: domain name.
- `resourceId`: domain name ID.
- `status`: domain name status. Valid values: `online`, `offline`, and `processing`.
- `serviceType`: service type. Valid values: `web`, `download`, and `media`.
- projectId: project ID.
- `domainType`: primary origin server type. Valid values: `cname` (external origin), `COS` (COS origin), and `third_party` (3rd-party object storage origin).
- `fullUrlCache`: whether to enable full-path cache, which can be `on` or `off`.
- `https`: whether to configure HTTPS, which can be `on`, `off` or `processing`.
- `originPullProtocol`: origin-pull protocol type, which can be `http`, `follow`, or `https`.
- `tagKey`: tag key.
        :type Name: str
        :param Value: Filter field value.
        :type Value: list of str
        :param Fuzzy: Whether to enable fuzzy query. Only `origin` or `domain` is supported for the filter field name.
When fuzzy query is enabled, the maximum Value length is 1. When fuzzy query is disabled, the maximum Value length is 5.
        :type Fuzzy: bool
        """
        self.Name = None
        self.Value = None
        self.Fuzzy = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainLog(AbstractModel):
    """Details about a log package download link

    """

    def __init__(self):
        r"""
        :param StartTime: Starting time of the log package
        :type StartTime: str
        :param EndTime: End time of the log package
        :type EndTime: str
        :param LogPath: Log package download link
        :type LogPath: str
        :param Area: Acceleration region corresponding to the log package
`mainland`: within Mainland China
`overseas`: outside Mainland China
        :type Area: str
        :param LogName: Log package filename
        :type LogName: str
        """
        self.StartTime = None
        self.EndTime = None
        self.LogPath = None
        self.Area = None
        self.LogName = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.LogPath = params.get("LogPath")
        self.Area = params.get("Area")
        self.LogName = params.get("LogName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownstreamCapping(AbstractModel):
    """Single link downstream speed limit configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param Switch: Downstream speed configuration switch
on: enabled
off: disabled
        :type Switch: str
        :param CappingRules: Downstream speed limiting rules
Note: this field may return null, indicating that no valid values can be obtained.
        :type CappingRules: list of CappingRule
        """
        self.Switch = None
        self.CappingRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("CappingRules") is not None:
            self.CappingRules = []
            for item in params.get("CappingRules"):
                obj = CappingRule()
                obj._deserialize(item)
                self.CappingRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableCachesRequest(AbstractModel):
    """EnableCaches request structure.

    """

    def __init__(self):
        r"""
        :param Urls: List of unblocked URLs
        :type Urls: list of str
        :param Date: URL blocking date
        :type Date: str
        """
        self.Urls = None
        self.Date = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
        self.Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableCachesResponse(AbstractModel):
    """EnableCaches response structure.

    """

    def __init__(self):
        r"""
        :param CacheOptResult: Result list
Note: This field may return null, indicating that no valid values can be obtained.
        :type CacheOptResult: :class:`tencentcloud.cdn.v20180606.models.CacheOptResult`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CacheOptResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CacheOptResult") is not None:
            self.CacheOptResult = CacheOptResult()
            self.CacheOptResult._deserialize(params.get("CacheOptResult"))
        self.RequestId = params.get("RequestId")


class EnableClsLogTopicRequest(AbstractModel):
    """EnableClsLogTopic request structure.

    """

    def __init__(self):
        r"""
        :param LogsetId: Logset ID
        :type LogsetId: str
        :param TopicId: Log topic ID
        :type TopicId: str
        :param Channel: Connection channel. Default value: cdn
        :type Channel: str
        """
        self.LogsetId = None
        self.TopicId = None
        self.Channel = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        self.Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableClsLogTopicResponse(AbstractModel):
    """EnableClsLogTopic response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ErrorPage(AbstractModel):
    """Status code redirect configuration. This is disabled by default. (This feature is in beta and not generally available yet.)

    """

    def __init__(self):
        r"""
        :param Switch: Status code redirect configuration switch
on: enabled
off: disabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param PageRules: Status code redirect rules configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type PageRules: list of ErrorPageRule
        """
        self.Switch = None
        self.PageRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("PageRules") is not None:
            self.PageRules = []
            for item in params.get("PageRules"):
                obj = ErrorPageRule()
                obj._deserialize(item)
                self.PageRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorPageRule(AbstractModel):
    """Status code redirect rules configuration

    """

    def __init__(self):
        r"""
        :param StatusCode: Status code
Supports 400, 403, 404, 500.
        :type StatusCode: int
        :param RedirectCode: Redirect status code settings
Supports 301 or 302.
        :type RedirectCode: int
        :param RedirectUrl: Redirect URL
Requires a full redirect path, such as https://www.test.com/error.html.
        :type RedirectUrl: str
        """
        self.StatusCode = None
        self.RedirectCode = None
        self.RedirectUrl = None


    def _deserialize(self, params):
        self.StatusCode = params.get("StatusCode")
        self.RedirectCode = params.get("RedirectCode")
        self.RedirectUrl = params.get("RedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FollowRedirect(AbstractModel):
    """301/302 automatic origin-pull follow-redirect configuration. It is disabled by default.

    """

    def __init__(self):
        r"""
        :param Switch: Origin-pull follow-redirect switch
on: enabled
off: disabled
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForceRedirect(AbstractModel):
    """Access protocol forced redirect configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param Switch: Access forced redirect configuration switch
on: enabled
off: disabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param RedirectType: Access forced redirect types
http: forced HTTP redirect
https: forced HTTPS redirect
Note: this field may return null, indicating that no valid values can be obtained.
        :type RedirectType: str
        :param RedirectStatusCode: Status code returned for forced redirect 
Supports 301, 302.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RedirectStatusCode: int
        :param CarryHeaders: Whether to return the added header in forced redirection.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CarryHeaders: str
        """
        self.Switch = None
        self.RedirectType = None
        self.RedirectStatusCode = None
        self.CarryHeaders = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.RedirectType = params.get("RedirectType")
        self.RedirectStatusCode = params.get("RedirectStatusCode")
        self.CarryHeaders = params.get("CarryHeaders")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDisableRecordsRequest(AbstractModel):
    """GetDisableRecords request structure.

    """

    def __init__(self):
        r"""
        :param Url: Specifies the URL to be queried
        :type Url: str
        :param StartTime: Starting time, such as `2018-12-12 10:24:00`
        :type StartTime: str
        :param EndTime: End time, such as 2018-12-14 10:24:00
        :type EndTime: str
        :param Status: Current URL status
disable: The URL remains disabled, and accessing it will return an error 403
enable: The URL is enabled (unblocked) and can be normally accessed
        :type Status: str
        :param Offset: Offset for paginated queries. Default value: 0
        :type Offset: int
        :param Limit: Limit on paged queries. Default value: 20
        :type Limit: int
        :param TaskId: Task ID. The task ID and start time cannot be both left empty.
        :type TaskId: str
        """
        self.Url = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.Offset = None
        self.Limit = None
        self.TaskId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDisableRecordsResponse(AbstractModel):
    """GetDisableRecords response structure.

    """

    def __init__(self):
        r"""
        :param UrlRecordList: Blocking history
Note: This field may return null, indicating that no valid values can be obtained.
        :type UrlRecordList: list of UrlRecord
        :param TotalCount: Total number of tasks, which is used for pagination
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UrlRecordList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UrlRecordList") is not None:
            self.UrlRecordList = []
            for item in params.get("UrlRecordList"):
                obj = UrlRecord()
                obj._deserialize(item)
                self.UrlRecordList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class GuetzliAdapter(AbstractModel):
    """Image optimization - `GuetzliAdapter` configuration

    """

    def __init__(self):
        r"""
        :param Switch: Switch. Valid values: on, off
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HeaderKey(AbstractModel):
    """A part of `CacheKey`

    """

    def __init__(self):
        r"""
        :param Switch: Whether to use it as part of `CacheKey`
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param Value: Array of headers that make up the `CacheKey` (separated by ';')
Note: this field may return null, indicating that no valid values can be obtained.
        :type Value: str
        """
        self.Switch = None
        self.Value = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Hsts(AbstractModel):
    """`HSTS` configuration.

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable. Valid values: on, off.
        :type Switch: str
        :param MaxAge: `MaxAge` value.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxAge: int
        :param IncludeSubDomains: Whether to include subdomain names. Valid values: on, off.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IncludeSubDomains: str
        """
        self.Switch = None
        self.MaxAge = None
        self.IncludeSubDomains = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.MaxAge = params.get("MaxAge")
        self.IncludeSubDomains = params.get("IncludeSubDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpHeaderPathRule(AbstractModel):
    """HTTP header setting rules. Up to 100 entries can be set.

    """

    def __init__(self):
        r"""
        :param HeaderMode: HTTP header setting methods
`set`: sets a value for an existing header parameter, a new header parameter, or multiple header parameters. Multiple header parameters will be merged into one.
`del`: deletes a header parameter.
`add`: adds a header parameter. By default, you can repeat the same action to add the same header parameter, which may affect browser response. Please consider the set operation first.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type HeaderMode: str
        :param HeaderName: HTTP header name. Up to 100 characters can be set.
Note: this field may return null, indicating that no valid values can be obtained.
        :type HeaderName: str
        :param HeaderValue: HTTP header value. Up to 1000 characters can be set.
Not required when Mode is del
Required when Mode is add/set
Note: this field may return null, indicating that no valid values can be obtained.
        :type HeaderValue: str
        :param RuleType: Rule types:
`all`: effective for all files
`file`: effective for specified file suffixes
`directory`: effective for specified paths
`path`: effective for specified absolute paths
Note: this field may return null, indicating that no valid values can be obtained.
        :type RuleType: str
        :param RulePaths: Content for each RuleType:
For `all`, enter an asterisk (*).
For `file`, enter the suffix, such as jpg, txt.
For `directory`, enter the path, such as /xxx/test/.
For `path`, enter the corresponding absolute path, such as /xxx/test.html.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RulePaths: list of str
        """
        self.HeaderMode = None
        self.HeaderName = None
        self.HeaderValue = None
        self.RuleType = None
        self.RulePaths = None


    def _deserialize(self, params):
        self.HeaderMode = params.get("HeaderMode")
        self.HeaderName = params.get("HeaderName")
        self.HeaderValue = params.get("HeaderValue")
        self.RuleType = params.get("RuleType")
        self.RulePaths = params.get("RulePaths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpHeaderRule(AbstractModel):
    """HTTP header setting rules.

    """

    def __init__(self):
        r"""
        :param HeaderMode: HTTP header setting method. Valid values: `add` (add header), `set` (set header) or `del` (delete header).
        :type HeaderMode: str
        :param HeaderName: HTTP header name
        :type HeaderName: str
        :param HeaderValue: HTTP header value
        :type HeaderValue: str
        """
        self.HeaderMode = None
        self.HeaderName = None
        self.HeaderValue = None


    def _deserialize(self, params):
        self.HeaderMode = params.get("HeaderMode")
        self.HeaderName = params.get("HeaderName")
        self.HeaderValue = params.get("HeaderValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Https(AbstractModel):
    """Domain name HTTPS acceleration configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param Switch: HTTPS configuration switch
on: enabled
off: disabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param Http2: HTTP2 configuration switch
on: enabled
off: disabled
Enabling HTTPS acceleration for the first time will enable HTTP2 configuration by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Http2: str
        :param OcspStapling: OCSP configuration switch
on: enabled
off: disabled
This is disabled by default
Note: this field may return null, indicating that no valid values can be obtained.
        :type OcspStapling: str
        :param VerifyClient: Client certificate authentication feature
on: enabled
off: disabled
This is disabled by default. The client certificate information is needed when enabled. This is still in beta and not generally available yet.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VerifyClient: str
        :param CertInfo: Server certificate configuration information
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertInfo: :class:`tencentcloud.cdn.v20180606.models.ServerCert`
        :param ClientCertInfo: Client certificate configuration information
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClientCertInfo: :class:`tencentcloud.cdn.v20180606.models.ClientCert`
        :param Spdy: Spdy configuration switch
on: enabled
off: disabled
This is disabled by default
Note: this field may return null, indicating that no valid values can be obtained.
        :type Spdy: str
        :param SslStatus: HTTPS certificate deployment status
closed: already closed
deploying: in deployment
deployed: successfully deployed
failed: deployment failed
Note: this field may return null, indicating that no valid values can be obtained.
        :type SslStatus: str
        :param Hsts: HSTS configuration
        :type Hsts: :class:`tencentcloud.cdn.v20180606.models.Hsts`
        :param TlsVersion: TLS version settings, which only support certain advanced domain names. Valid values: `TLSv1`, `TLSV1.1`, `TLSV1.2`, and `TLSv1.3`. Only consecutive versions can be enabled at the same time.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TlsVersion: list of str
        """
        self.Switch = None
        self.Http2 = None
        self.OcspStapling = None
        self.VerifyClient = None
        self.CertInfo = None
        self.ClientCertInfo = None
        self.Spdy = None
        self.SslStatus = None
        self.Hsts = None
        self.TlsVersion = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Http2 = params.get("Http2")
        self.OcspStapling = params.get("OcspStapling")
        self.VerifyClient = params.get("VerifyClient")
        if params.get("CertInfo") is not None:
            self.CertInfo = ServerCert()
            self.CertInfo._deserialize(params.get("CertInfo"))
        if params.get("ClientCertInfo") is not None:
            self.ClientCertInfo = ClientCert()
            self.ClientCertInfo._deserialize(params.get("ClientCertInfo"))
        self.Spdy = params.get("Spdy")
        self.SslStatus = params.get("SslStatus")
        if params.get("Hsts") is not None:
            self.Hsts = Hsts()
            self.Hsts._deserialize(params.get("Hsts"))
        self.TlsVersion = params.get("TlsVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageOptimization(AbstractModel):
    """`ImageOptimization` configuration

    """

    def __init__(self):
        r"""
        :param WebpAdapter: `WebpAdapter` configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type WebpAdapter: :class:`tencentcloud.cdn.v20180606.models.WebpAdapter`
        :param TpgAdapter: `TpgAdapter` configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type TpgAdapter: :class:`tencentcloud.cdn.v20180606.models.TpgAdapter`
        :param GuetzliAdapter: `GuetzliAdapter` configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type GuetzliAdapter: :class:`tencentcloud.cdn.v20180606.models.GuetzliAdapter`
        """
        self.WebpAdapter = None
        self.TpgAdapter = None
        self.GuetzliAdapter = None


    def _deserialize(self, params):
        if params.get("WebpAdapter") is not None:
            self.WebpAdapter = WebpAdapter()
            self.WebpAdapter._deserialize(params.get("WebpAdapter"))
        if params.get("TpgAdapter") is not None:
            self.TpgAdapter = TpgAdapter()
            self.TpgAdapter._deserialize(params.get("TpgAdapter"))
        if params.get("GuetzliAdapter") is not None:
            self.GuetzliAdapter = GuetzliAdapter()
            self.GuetzliAdapter._deserialize(params.get("GuetzliAdapter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpFilter(AbstractModel):
    """IP blocklist/allowlist configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param Switch: IP blocklist/allowlist configuration switch
on: enabled
off: disabled
        :type Switch: str
        :param FilterType: IP blocklist/allowlist type
whitelist: allowlist
blacklist: blocklist
Note: this field may return null, indicating that no valid values can be obtained.
        :type FilterType: str
        :param Filters: IP blocklist/allowlist list
Supports IPs in X.X.X.X format, or /8, /16, /24 format IP ranges.
Up to 50 allowlists or blocklists can be entered
Note: this field may return null, indicating that no valid values can be obtained.
        :type Filters: list of str
        :param FilterRules: IP blocklist/allowlist path-based configuration. This feature is only available to selected beta customers.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type FilterRules: list of IpFilterPathRule
        """
        self.Switch = None
        self.FilterType = None
        self.Filters = None
        self.FilterRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.FilterType = params.get("FilterType")
        self.Filters = params.get("Filters")
        if params.get("FilterRules") is not None:
            self.FilterRules = []
            for item in params.get("FilterRules"):
                obj = IpFilterPathRule()
                obj._deserialize(item)
                self.FilterRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpFilterPathRule(AbstractModel):
    """IP blocklist/allowlist path-based configuration

    """

    def __init__(self):
        r"""
        :param FilterType: IP blocklist/allowlist type
`whitelist`: allowlist IPs
`blacklist`: blocklist IPs
Note: this field may return `null`, indicating that no valid value is obtained.
        :type FilterType: str
        :param Filters: IP blocklist/allowlist list
Supports IPs in X.X.X.X format, or /8, /16, /24 format IP ranges.
Up to 50 allowlists or blocklists can be entered.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Filters: list of str
        :param RuleType: Rule types:
`all`: effective for all files
`file`: effective for specified file suffixes
`directory`: effective for specified paths
`path`: effective for specified absolute paths
Note: this field may return `null`, indicating that no valid value is obtained.
        :type RuleType: str
        :param RulePaths: Content for each RuleType:
For `all`, enter an asterisk (*).
For `file`, enter the suffix, such as jpg, txt.
For `directory`, enter the path, such as /xxx/test/.
For `path`, enter the corresponding absolute path, such as /xxx/test.html.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type RulePaths: list of str
        """
        self.FilterType = None
        self.Filters = None
        self.RuleType = None
        self.RulePaths = None


    def _deserialize(self, params):
        self.FilterType = params.get("FilterType")
        self.Filters = params.get("Filters")
        self.RuleType = params.get("RuleType")
        self.RulePaths = params.get("RulePaths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpFreqLimit(AbstractModel):
    """Access limit configuration for a single IP of a single node. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param Switch: IP access limit configuration switch
on: enabled
off: disabled
        :type Switch: str
        :param Qps: Sets the limited number of requests per second
514 will be returned for requests that exceed the limit
Note: this field may return null, indicating that no valid values can be obtained.
        :type Qps: int
        """
        self.Switch = None
        self.Qps = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Qps = params.get("Qps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpStatus(AbstractModel):
    """Node IP information

    """

    def __init__(self):
        r"""
        :param Ip: Node IP
        :type Ip: str
        :param District: Node region
        :type District: str
        :param Isp: Node ISP
        :type Isp: str
        :param City: Node city
        :type City: str
        :param Status: Node status
online: the node is online; scheduling service running
offline: the node is offline
        :type Status: str
        """
        self.Ip = None
        self.District = None
        self.Isp = None
        self.City = None
        self.Status = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.District = params.get("District")
        self.Isp = params.get("Isp")
        self.City = params.get("City")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ipv6(AbstractModel):
    """IPv6 activation configurations, which cannot be changed.

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable the IPv6 feature for a domain name. Values include `on` or `off`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ipv6Access(AbstractModel):
    """IPv6 access configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable the IPv6 access feature for a domain name. Valid values: `on` and `off`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyRule(AbstractModel):
    """Path-based cache key configuration

    """

    def __init__(self):
        r"""
        :param RulePaths: Content for each CacheType:
For `file`, enter the suffix, such as jpg, txt.
For `directory`, enter the path, such as /xxx/test/.
For `path`, enter the corresponding absolute path, such as /xxx/test.html.
For `index`, enter a backslash (/).
Note: this field may return null, indicating that no valid value is obtained.
        :type RulePaths: list of str
        :param RuleType: Rule types:
`file`: effective for specified file suffixes
`directory`: effective for specified paths
`path`: effective for specified absolute paths
`index`: home page
Note: this field may return null, indicating that no valid value is obtained.
        :type RuleType: str
        :param FullUrlCache: Whether to enable full-path cache
on: enable full-path cache (i.e., disable parameter filter)
off: disable full-path cache (i.e., enable parameter filter)
Note: this field may return null, indicating that no valid value is obtained.
        :type FullUrlCache: str
        :param IgnoreCase: Whether caches are case insensitive
Note: this field may return null, indicating that no valid value is obtained.
        :type IgnoreCase: str
        :param QueryString: Request parameter contained in `CacheKey`
Note: this field may return null, indicating that no valid value is obtained.
        :type QueryString: :class:`tencentcloud.cdn.v20180606.models.RuleQueryString`
        :param RuleTag: Path cache key tag, the value "user" is passed.
Note: this field may return null, indicating that no valid value is obtained.
        :type RuleTag: str
        """
        self.RulePaths = None
        self.RuleType = None
        self.FullUrlCache = None
        self.IgnoreCase = None
        self.QueryString = None
        self.RuleTag = None


    def _deserialize(self, params):
        self.RulePaths = params.get("RulePaths")
        self.RuleType = params.get("RuleType")
        self.FullUrlCache = params.get("FullUrlCache")
        self.IgnoreCase = params.get("IgnoreCase")
        if params.get("QueryString") is not None:
            self.QueryString = RuleQueryString()
            self.QueryString._deserialize(params.get("QueryString"))
        self.RuleTag = params.get("RuleTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListClsLogTopicsRequest(AbstractModel):
    """ListClsLogTopics request structure.

    """

    def __init__(self):
        r"""
        :param Channel: Connection channel. Default value: cdn
        :type Channel: str
        """
        self.Channel = None


    def _deserialize(self, params):
        self.Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListClsLogTopicsResponse(AbstractModel):
    """ListClsLogTopics response structure.

    """

    def __init__(self):
        r"""
        :param Logset: Logset information
        :type Logset: :class:`tencentcloud.cdn.v20180606.models.LogSetInfo`
        :param Topics: Log topic information list
Note: this field may return null, indicating that no valid values can be obtained.
        :type Topics: list of TopicInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Logset = None
        self.Topics = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Logset") is not None:
            self.Logset = LogSetInfo()
            self.Logset._deserialize(params.get("Logset"))
        if params.get("Topics") is not None:
            self.Topics = []
            for item in params.get("Topics"):
                obj = TopicInfo()
                obj._deserialize(item)
                self.Topics.append(obj)
        self.RequestId = params.get("RequestId")


class ListClsTopicDomainsRequest(AbstractModel):
    """ListClsTopicDomains request structure.

    """

    def __init__(self):
        r"""
        :param LogsetId: Logset ID
        :type LogsetId: str
        :param TopicId: Log topic ID
        :type TopicId: str
        :param Channel: Connection channel. Default value: cdn
        :type Channel: str
        """
        self.LogsetId = None
        self.TopicId = None
        self.Channel = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        self.Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListClsTopicDomainsResponse(AbstractModel):
    """ListClsTopicDomains response structure.

    """

    def __init__(self):
        r"""
        :param AppId: Developer ID
        :type AppId: int
        :param Channel: Channel
        :type Channel: str
        :param LogsetId: Logset ID
        :type LogsetId: str
        :param TopicId: Log topic ID
        :type TopicId: str
        :param DomainAreaConfigs: Domain name region configuration, which may contain deleted domain names. If this is to be used in `ManageClsTopicDomains` API, you need to exclude deleted domain names by using the `ListCdnDomains` API.
        :type DomainAreaConfigs: list of DomainAreaConfig
        :param TopicName: Log topic name
        :type TopicName: str
        :param UpdateTime: Last modified time of log topic
Note: this field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.AppId = None
        self.Channel = None
        self.LogsetId = None
        self.TopicId = None
        self.DomainAreaConfigs = None
        self.TopicName = None
        self.UpdateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.Channel = params.get("Channel")
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        if params.get("DomainAreaConfigs") is not None:
            self.DomainAreaConfigs = []
            for item in params.get("DomainAreaConfigs"):
                obj = DomainAreaConfig()
                obj._deserialize(item)
                self.DomainAreaConfigs.append(obj)
        self.TopicName = params.get("TopicName")
        self.UpdateTime = params.get("UpdateTime")
        self.RequestId = params.get("RequestId")


class ListTopDataRequest(AbstractModel):
    """ListTopData request structure.

    """

    def __init__(self):
        r"""
        :param StartTime: Query start time in the format of `yyyy-MM-dd HH:mm:ss`
Only supports data query at daily granularity. The date in the input parameter is used as the start date.
Data generated after or at 00:00:00 on the start date will be returned
Only data for the last 90 days can be queried
        :type StartTime: str
        :param EndTime: Query end time in the format of `yyyy-MM-dd HH:mm:ss`
Only supports data query at daily granularity. The date in the input parameter is used as the end date.
Data generated before or at 23:59:59 on the end date will be returned
`EndTime` must be later than or equal to `StartTime`
        :type EndTime: str
        :param Metric: Object representing the sort criteria. The following objects are supported:
`url`: sorts by access URL (URLs carrying no parameters). Supported filters are `flux` and `request`.
`district`: sorts by province, country, or region. Supported filters are `flux` and `request`.
`isp`: sorts by ISP. Supported filters are `flux` and `request`.
`host`: sorts by domain name access data. Supported filters are `flux`, `request`, `bandwidth`, `fluxHitRate`, and `statusCode` (2XX, 3XX, 4XX, 5XX).
`originHost`: sorts by domain name origin-pull data. Supported filters are `flux`, `request`, `bandwidth`, and `OriginStatusCode` (origin_2XX, origin_3XX, origin_4XX, origin_5XX).
        :type Metric: str
        :param Filter: Metric name used for sorting:
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
        :param Domains: Specifies the list of domain names to be queried; up to 30 domain names can be queried at a time.
        :type Domains: list of str
        :param Project: Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)
Please note that if domain names are specified, this parameter will be ignored.
        :type Project: int
        :param Detail: Default is `false` for multi-domain name queries, which returns sorted results of all domain names. 
If `Metric` is `url`, `path`, `district`, or `isp` and `Filter` is `flux` or `request`, it can be set to `true` to return the sorted results of each domain.
        :type Detail: bool
        :param Code: When Filter is `statusCode` or `OriginStatusCode`, enter a code to query and sort results.
        :type Code: str
        :param Area: Specifies a service region for the query. If it is left blank, CDN data within Mainland China will be queried.
`mainland`: specifies to query CDN data within Mainland China;
`overseas`: specifies to query CDN data outside Mainland China. Supported metrics are `url`, `district`, `host`, and `originHost`. If `Metric` is `originHost`, supported filters are `flux`, `request`, and `bandwidth`.
        :type Area: str
        :param AreaType: The region type can be specified only when you query CDN data outside Mainland China and `Metric` is `district` or `host`; if you leave it empty, data of the service region will be queried (only applicable when `Area` is `overseas` and `Metric` is `district` or `host`)
server: specifies to query data of service region (where a CDN node is located)
client: specifies to query data of the client region (where a user request device is located). If `Metric` is `host`, `Filter` can only be `flux`, `request`, or `bandwidth`
        :type AreaType: str
        :param Product: Specifies the product to query, either `cdn` (default) or `ecdn`.
        :type Product: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Metric = None
        self.Filter = None
        self.Domains = None
        self.Project = None
        self.Detail = None
        self.Code = None
        self.Area = None
        self.AreaType = None
        self.Product = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metric = params.get("Metric")
        self.Filter = params.get("Filter")
        self.Domains = params.get("Domains")
        self.Project = params.get("Project")
        self.Detail = params.get("Detail")
        self.Code = params.get("Code")
        self.Area = params.get("Area")
        self.AreaType = params.get("AreaType")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTopDataResponse(AbstractModel):
    """ListTopData response structure.

    """

    def __init__(self):
        r"""
        :param Data: Top access data details of each resource
        :type Data: list of TopData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TopData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class LogSetInfo(AbstractModel):
    """Logset information

    """

    def __init__(self):
        r"""
        :param AppId: Developer ID
        :type AppId: int
        :param Channel: Channel
Note: this field may return null, indicating that no valid values can be obtained.
        :type Channel: str
        :param LogsetId: Logset ID
        :type LogsetId: str
        :param LogsetName: Logset name
        :type LogsetName: str
        :param IsDefault: Whether it is the default logset
        :type IsDefault: int
        :param LogsetSavePeriod: Log retention period in days
        :type LogsetSavePeriod: int
        :param CreateTime: Creation date
        :type CreateTime: str
        :param Region: Region
        :type Region: str
        """
        self.AppId = None
        self.Channel = None
        self.LogsetId = None
        self.LogsetName = None
        self.IsDefault = None
        self.LogsetSavePeriod = None
        self.CreateTime = None
        self.Region = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.Channel = params.get("Channel")
        self.LogsetId = params.get("LogsetId")
        self.LogsetName = params.get("LogsetName")
        self.IsDefault = params.get("IsDefault")
        self.LogsetSavePeriod = params.get("LogsetSavePeriod")
        self.CreateTime = params.get("CreateTime")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MainlandConfig(AbstractModel):
    """Specific configuration for domain names in the mainland China by region. UpdateDomainConfig API only supports modification of certain region configurations. A list of differences that may exist for older configurations will be provided for a compatibility check. The supported configuration list is as follows:
    + Authentication
    + BandwidthAlert
    + ErrorPage
    + IpFilter
    + Origin
    + Referer

    """

    def __init__(self):
        r"""
        :param Authentication: Timestamp hotlink protection configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param BandwidthAlert: Bandwidth cap configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param Cache: Cache rules configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param CacheKey: Cache configurations.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param Compression: Smart compression configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param DownstreamCapping: Download speed limit configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param ErrorPage: Error code redirect configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param FollowRedirect: 301 and 302 automatic origin-pull follow-redirect configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param ForceRedirect: Access protocol forced redirect configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param Https: HTTPS configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param IpFilter: IP blocklist/allowlist configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param IpFreqLimit: IP access limit configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param MaxAge: Browser cache rules configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param Origin: Origin server configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param OriginPullOptimization: Cross-border optimization configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param RangeOriginPull: Range GETs configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param Referer: Hotlink protection configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param RequestHeader: Origin-pull request header configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param ResponseHeader: Origin server response header configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param ResponseHeaderCache: Follows origin server cache header configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param Seo: SEO configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param ServiceType: Domain name service type. `web`: static acceleration; `download`: download acceleration; `media`: streaming media acceleration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceType: str
        :param StatusCodeCache: Status code cache configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param VideoSeek: Video dragging configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        """
        self.Authentication = None
        self.BandwidthAlert = None
        self.Cache = None
        self.CacheKey = None
        self.Compression = None
        self.DownstreamCapping = None
        self.ErrorPage = None
        self.FollowRedirect = None
        self.ForceRedirect = None
        self.Https = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.MaxAge = None
        self.Origin = None
        self.OriginPullOptimization = None
        self.RangeOriginPull = None
        self.Referer = None
        self.RequestHeader = None
        self.ResponseHeader = None
        self.ResponseHeaderCache = None
        self.Seo = None
        self.ServiceType = None
        self.StatusCodeCache = None
        self.VideoSeek = None


    def _deserialize(self, params):
        if params.get("Authentication") is not None:
            self.Authentication = Authentication()
            self.Authentication._deserialize(params.get("Authentication"))
        if params.get("BandwidthAlert") is not None:
            self.BandwidthAlert = BandwidthAlert()
            self.BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("DownstreamCapping") is not None:
            self.DownstreamCapping = DownstreamCapping()
            self.DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("FollowRedirect") is not None:
            self.FollowRedirect = FollowRedirect()
            self.FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("OriginPullOptimization") is not None:
            self.OriginPullOptimization = OriginPullOptimization()
            self.OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("RangeOriginPull") is not None:
            self.RangeOriginPull = RangeOriginPull()
            self.RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("Referer") is not None:
            self.Referer = Referer()
            self.Referer._deserialize(params.get("Referer"))
        if params.get("RequestHeader") is not None:
            self.RequestHeader = RequestHeader()
            self.RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("ResponseHeaderCache") is not None:
            self.ResponseHeaderCache = ResponseHeaderCache()
            self.ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("Seo") is not None:
            self.Seo = Seo()
            self.Seo._deserialize(params.get("Seo"))
        self.ServiceType = params.get("ServiceType")
        if params.get("StatusCodeCache") is not None:
            self.StatusCodeCache = StatusCodeCache()
            self.StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("VideoSeek") is not None:
            self.VideoSeek = VideoSeek()
            self.VideoSeek._deserialize(params.get("VideoSeek"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageClsTopicDomainsRequest(AbstractModel):
    """ManageClsTopicDomains request structure.

    """

    def __init__(self):
        r"""
        :param LogsetId: Logset ID
        :type LogsetId: str
        :param TopicId: Log topic ID
        :type TopicId: str
        :param Channel: Connection channel. Default value: cdn
        :type Channel: str
        :param DomainAreaConfigs: Domain name region configuration. Note: if this field is empty, it means to unbind all domain names from the corresponding topic
        :type DomainAreaConfigs: list of DomainAreaConfig
        """
        self.LogsetId = None
        self.TopicId = None
        self.Channel = None
        self.DomainAreaConfigs = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        self.Channel = params.get("Channel")
        if params.get("DomainAreaConfigs") is not None:
            self.DomainAreaConfigs = []
            for item in params.get("DomainAreaConfigs"):
                obj = DomainAreaConfig()
                obj._deserialize(item)
                self.DomainAreaConfigs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageClsTopicDomainsResponse(AbstractModel):
    """ManageClsTopicDomains response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MapInfo(AbstractModel):
    """Mapping between a name and an ID

    """

    def __init__(self):
        r"""
        :param Id: Object ID
        :type Id: int
        :param Name: Object name
        :type Name: str
        """
        self.Id = None
        self.Name = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaxAge(AbstractModel):
    """Browser cache rule configuration. This is used to set the MaxAge default value and is disabled by default. (This feature is in beta and not generally available yet.)

    """

    def __init__(self):
        r"""
        :param Switch: Browser cache configuration switch
on: enabled
off: disabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param MaxAgeRules: MaxAge rule
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxAgeRules: list of MaxAgeRule
        """
        self.Switch = None
        self.MaxAgeRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("MaxAgeRules") is not None:
            self.MaxAgeRules = []
            for item in params.get("MaxAgeRules"):
                obj = MaxAgeRule()
                obj._deserialize(item)
                self.MaxAgeRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaxAgeRule(AbstractModel):
    """MaxAge rules configuration

    """

    def __init__(self):
        r"""
        :param MaxAgeType: Rule types:
`all`: effective for all files.
`file`: effective for specified file suffixes.
`directory`: effective for specified paths.
`path`: effective for specified absolute paths.
`index`: effective for specified homepages.
        :type MaxAgeType: str
        :param MaxAgeContents: Content for each `MaxAgeType`:
For `all`, enter a wildcard `*`.
For `file`, enter a suffix, e.g., `jpg` or `txt`.
For `directory`, enter a path, e.g., `/xxx/test/`.
For `path`, enter an absolute path, e.g., `/xxx/test.html`.
For `index`, enter a forward slash `/`.
Note: the rule `all` cannot be deleted. It follows origin by default and can be modified.
        :type MaxAgeContents: list of str
        :param MaxAgeTime: MaxAge time (in seconds)
Note: the value `0` means not to cache.
        :type MaxAgeTime: int
        :param FollowOrigin: Whether to follow the origin server. Valid values: `on` and `off`. If it's on, `MaxAgeTime` is ignored.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FollowOrigin: str
        """
        self.MaxAgeType = None
        self.MaxAgeContents = None
        self.MaxAgeTime = None
        self.FollowOrigin = None


    def _deserialize(self, params):
        self.MaxAgeType = params.get("MaxAgeType")
        self.MaxAgeContents = params.get("MaxAgeContents")
        self.MaxAgeTime = params.get("MaxAgeTime")
        self.FollowOrigin = params.get("FollowOrigin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineCache(AbstractModel):
    """Whether to enable offline cache

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable offline cache. Valid values: `on` and `off`.
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Origin(AbstractModel):
    """Complex origin server configurations. The following configurations are supported:
    + Origin server specified as a single domain name
    + Origin server specified as multiple IPs. Supported port range: 1-65535; Supported weight range: 1-100. Format: IP:Port:Weight.
    + Origin-pull domain name configuration
    + Cloud Object Storage (COS) specified as origin server
    + Hot backup origin server specified as a single domain name
    + Hot backup origin server specified as multiple IPs. Supported port range: 1-65535. At present, weight configuration is not supported.
    + Hot backup origin server origin-pull domain name configuration

    """

    def __init__(self):
        r"""
        :param Origins: Master origin server list
When modifying the origin server, you need to enter the corresponding OriginType.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Origins: list of str
        :param OriginType: Master origin server type
The following types are supported for input parameters:
domain: domain name type
cos: COS origin
ip: IP list used as origin server
ipv6: origin server list is a single IPv6 address
ip_ipv6: origin server list is multiple IPv4 addresses and an IPv6 address
The following types of output parameters are added:
image: Cloud Infinite origin
ftp: legacy FTP origin, which is no longer maintained.
When modifying `Origins`, you need to enter the corresponding OriginType.
The IPv6 feature is not generally available yet. Please send in a whitelist application to use this feature.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginType: str
        :param ServerName: Host header used when accessing the master origin server. If left empty, the acceleration domain name will be used by default.
If a wildcard domain name is accessed, then the sub-domain name during the access will be used by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServerName: str
        :param CosPrivateAccess: When OriginType is COS, you can specify if access to private buckets is allowed.
Note: to enable this configuration, you need to first grant CDN access to the private bucket.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CosPrivateAccess: str
        :param OriginPullProtocol: Origin-pull protocol configuration
http: forced HTTP origin-pull
follow: protocol follow origin-pull
https: forced HTTPS origin-pull. This only supports origin server port 443 for origin-pull.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginPullProtocol: str
        :param BackupOrigins: Backup origin server list
When modifying the backup origin server, you need to enter the corresponding BackupOriginType.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BackupOrigins: list of str
        :param BackupOriginType: Backup origin server type, which supports the following types:
domain: domain name type
ip: IP list used as origin server
When modifying BackupOrigins, you need to enter the corresponding BackupOriginType.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BackupOriginType: str
        :param BackupServerName: Host header used when accessing the backup origin server. If left empty, the ServerName of master origin server will be used by default.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BackupServerName: str
        :param BasePath: 
        :type BasePath: str
        :param PathRules: Origin URL rewrite rule configuration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type PathRules: list of PathRule
        :param PathBasedOrigin: Path-based origin-pull configurations
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type PathBasedOrigin: list of PathBasedOriginRule
        """
        self.Origins = None
        self.OriginType = None
        self.ServerName = None
        self.CosPrivateAccess = None
        self.OriginPullProtocol = None
        self.BackupOrigins = None
        self.BackupOriginType = None
        self.BackupServerName = None
        self.BasePath = None
        self.PathRules = None
        self.PathBasedOrigin = None


    def _deserialize(self, params):
        self.Origins = params.get("Origins")
        self.OriginType = params.get("OriginType")
        self.ServerName = params.get("ServerName")
        self.CosPrivateAccess = params.get("CosPrivateAccess")
        self.OriginPullProtocol = params.get("OriginPullProtocol")
        self.BackupOrigins = params.get("BackupOrigins")
        self.BackupOriginType = params.get("BackupOriginType")
        self.BackupServerName = params.get("BackupServerName")
        self.BasePath = params.get("BasePath")
        if params.get("PathRules") is not None:
            self.PathRules = []
            for item in params.get("PathRules"):
                obj = PathRule()
                obj._deserialize(item)
                self.PathRules.append(obj)
        if params.get("PathBasedOrigin") is not None:
            self.PathBasedOrigin = []
            for item in params.get("PathBasedOrigin"):
                obj = PathBasedOriginRule()
                obj._deserialize(item)
                self.PathBasedOrigin.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginAuthentication(AbstractModel):
    """Origin-pull authentication advanced configuration

    """

    def __init__(self):
        r"""
        :param Switch: Authentication switch, which can be on or off.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Switch: str
        :param TypeA: Authentication type configuration A
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TypeA: :class:`tencentcloud.cdn.v20180606.models.OriginAuthenticationTypeA`
        """
        self.Switch = None
        self.TypeA = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("TypeA") is not None:
            self.TypeA = OriginAuthenticationTypeA()
            self.TypeA._deserialize(params.get("TypeA"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginAuthenticationTypeA(AbstractModel):
    """Origin-pull authentication advanced configuration TypeA

    """

    def __init__(self):
        r"""
        :param SecretKey: Key used for signature calculation, allowing 6 to 32 bytes of letters and digits.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SecretKey: str
        """
        self.SecretKey = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginCombine(AbstractModel):
    """Merging pull requests configurations

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable the merging pull requests feature. Valid values: `on` and `off`.
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginIp(AbstractModel):
    """IP information of CDN intermediate nodes

    """

    def __init__(self):
        r"""
        :param Ip: Intermediate IP range/intermediate IP. The IP range information is returned by default.
        :type Ip: str
        """
        self.Ip = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginPullOptimization(AbstractModel):
    """Cross-border origin-pull optimization configuration. This is disabled by default. (This feature is in beta and not generally available yet.)

    """

    def __init__(self):
        r"""
        :param Switch: Cross-border origin-pull optimization configuration switch
on: enabled
off: disabled
        :type Switch: str
        :param OptimizationType: Cross-border types
OVToCN: origin-pull from outside mainland China to inside mainland China
CNToOV: origin-pull from inside mainland China to outside mainland China
Note: this field may return null, indicating that no valid values can be obtained.
        :type OptimizationType: str
        """
        self.Switch = None
        self.OptimizationType = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.OptimizationType = params.get("OptimizationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginPullTimeout(AbstractModel):
    """Origin-pull timeout configuration

    """

    def __init__(self):
        r"""
        :param ConnectTimeout: The origin-pull connection timeout (in seconds). Valid range: 5-60.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ConnectTimeout: int
        :param ReceiveTimeout: The origin-pull receipt timeout (in seconds). Valid range: 10-60.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ReceiveTimeout: int
        """
        self.ConnectTimeout = None
        self.ReceiveTimeout = None


    def _deserialize(self, params):
        self.ConnectTimeout = params.get("ConnectTimeout")
        self.ReceiveTimeout = params.get("ReceiveTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OssPrivateAccess(AbstractModel):
    """Access authentication configuration for OSS origin

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable access authentication. Valid values: `on`, `off`.
        :type Switch: str
        :param AccessKey: Access ID.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AccessKey: str
        :param SecretKey: Key.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SecretKey: str
        """
        self.Switch = None
        self.AccessKey = None
        self.SecretKey = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.AccessKey = params.get("AccessKey")
        self.SecretKey = params.get("SecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OverseaConfig(AbstractModel):
    """Specific configuration for domain names outside mainland China. UpdateDomainConfig API only supports modification of some region configurations. A list of differences that may exist for older configurations will be provided for a compatibility check. The supported configuration list is as follows:
    + Authentication
    + BandwidthAlert
    + ErrorPage
    + IpFilter
    + Origin
    + Referer

    """

    def __init__(self):
        r"""
        :param Authentication: Timestamp hotlink protection configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param BandwidthAlert: Bandwidth cap configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param Cache: Cache rules configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param CacheKey: Cache configurations.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param Compression: Smart compression configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param DownstreamCapping: Download speed limit configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param ErrorPage: Error code redirect configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param FollowRedirect: 301 and 302 automatic origin-pull follow-redirect configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param ForceRedirect: Access protocol forced redirect configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param Https: HTTPS configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param IpFilter: IP blocklist/allowlist configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param IpFreqLimit: IP access limit configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param MaxAge: Browser cache rules configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param Origin: Origin server configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param OriginPullOptimization: Cross-border optimization configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param RangeOriginPull: Range GETs configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param Referer: Hotlink protection configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param RequestHeader: Origin-pull request header configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param ResponseHeader: Origin server response header configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param ResponseHeaderCache: Follows origin server cache header configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param Seo: SEO configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param ServiceType: Domain name service type. `web`: static acceleration; `download`: download acceleration; `media`: streaming media acceleration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServiceType: str
        :param StatusCodeCache: Status code cache configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param VideoSeek: Video dragging configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        """
        self.Authentication = None
        self.BandwidthAlert = None
        self.Cache = None
        self.CacheKey = None
        self.Compression = None
        self.DownstreamCapping = None
        self.ErrorPage = None
        self.FollowRedirect = None
        self.ForceRedirect = None
        self.Https = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.MaxAge = None
        self.Origin = None
        self.OriginPullOptimization = None
        self.RangeOriginPull = None
        self.Referer = None
        self.RequestHeader = None
        self.ResponseHeader = None
        self.ResponseHeaderCache = None
        self.Seo = None
        self.ServiceType = None
        self.StatusCodeCache = None
        self.VideoSeek = None


    def _deserialize(self, params):
        if params.get("Authentication") is not None:
            self.Authentication = Authentication()
            self.Authentication._deserialize(params.get("Authentication"))
        if params.get("BandwidthAlert") is not None:
            self.BandwidthAlert = BandwidthAlert()
            self.BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("DownstreamCapping") is not None:
            self.DownstreamCapping = DownstreamCapping()
            self.DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("FollowRedirect") is not None:
            self.FollowRedirect = FollowRedirect()
            self.FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("OriginPullOptimization") is not None:
            self.OriginPullOptimization = OriginPullOptimization()
            self.OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("RangeOriginPull") is not None:
            self.RangeOriginPull = RangeOriginPull()
            self.RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("Referer") is not None:
            self.Referer = Referer()
            self.Referer._deserialize(params.get("Referer"))
        if params.get("RequestHeader") is not None:
            self.RequestHeader = RequestHeader()
            self.RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("ResponseHeaderCache") is not None:
            self.ResponseHeaderCache = ResponseHeaderCache()
            self.ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("Seo") is not None:
            self.Seo = Seo()
            self.Seo._deserialize(params.get("Seo"))
        self.ServiceType = params.get("ServiceType")
        if params.get("StatusCodeCache") is not None:
            self.StatusCodeCache = StatusCodeCache()
            self.StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("VideoSeek") is not None:
            self.VideoSeek = VideoSeek()
            self.VideoSeek._deserialize(params.get("VideoSeek"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PathBasedOriginRule(AbstractModel):
    """Path-based origin-pull rules

    """

    def __init__(self):
        r"""
        :param RuleType: Rule types:
`file`: effective for files with specified suffixes.
`directory`: effective for specified paths.
`path`: effective for specified absolute paths.
`index`: effective for specified homepages.
        :type RuleType: str
        :param RulePaths: Content for each `RuleType`:
For `file`, enter a suffix, e.g., `jpg` or `txt`.
For `directory`, enter a path, e.g., `/xxx/test/`.
For `path`, enter an absolute path, e.g., `/xxx/test.html`.
For `index`, enter a forward slash `/`.
        :type RulePaths: list of str
        :param Origin: Origin server list. Domain names and IPv4 addresses are supported.
        :type Origin: list of str
        """
        self.RuleType = None
        self.RulePaths = None
        self.Origin = None


    def _deserialize(self, params):
        self.RuleType = params.get("RuleType")
        self.RulePaths = params.get("RulePaths")
        self.Origin = params.get("Origin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PathRule(AbstractModel):
    """Path-based origin-pull configuration rules

    """

    def __init__(self):
        r"""
        :param Regex: Whether to enable wildcard match (`*`).
false: disable
true: enable
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Regex: bool
        :param Path: Matched URL. Only URLs are supported, while parameters are not. The exact match is used by default. If wildcard match is enabled, up to 5 wildcards are supported. The URL can contain up to 1,024 characters.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Path: str
        :param Origin: Origin server when the path matches. COS origin with private read/write is not supported. The default origin server will be used by default when this field is left empty.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Origin: str
        :param ServerName: Origin server host header when the path matches. The default `ServerName` will be used by default when this field is left empty.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ServerName: str
        :param OriginArea: Origin server region. Valid values: `CN` and `OV`.
CN: the Chinese mainland
OV: outside the Chinese mainland
Default value: `CN`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type OriginArea: str
        :param ForwardUri: Origin server URI path when the path matches, starting with `/` and excluding parameters. The path can contain up to 1,024 characters. The wildcards in the match path can be respectively captured using `$1`, `$2`, `$3`, `$4`, and `$5`. Up to 10 values can be captured.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ForwardUri: str
        :param RequestHeaders: Origin-pull header setting when the path matches.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type RequestHeaders: list of HttpHeaderRule
        """
        self.Regex = None
        self.Path = None
        self.Origin = None
        self.ServerName = None
        self.OriginArea = None
        self.ForwardUri = None
        self.RequestHeaders = None


    def _deserialize(self, params):
        self.Regex = params.get("Regex")
        self.Path = params.get("Path")
        self.Origin = params.get("Origin")
        self.ServerName = params.get("ServerName")
        self.OriginArea = params.get("OriginArea")
        self.ForwardUri = params.get("ForwardUri")
        if params.get("RequestHeaders") is not None:
            self.RequestHeaders = []
            for item in params.get("RequestHeaders"):
                obj = HttpHeaderRule()
                obj._deserialize(item)
                self.RequestHeaders.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostSize(AbstractModel):
    """Maximum size of the file uploaded for streaming via a POST request

    """

    def __init__(self):
        r"""
        :param Switch: Limit the size of a POST request. The default value is 32 MB.
off: Disable
on: Enable
        :type Switch: str
        :param MaxSize: Maximum size. Value range: 1 MB to 200 MB.
        :type MaxSize: int
        """
        self.Switch = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurgePathCacheRequest(AbstractModel):
    """PurgePathCache request structure.

    """

    def __init__(self):
        r"""
        :param Paths: List of directories. The protocol header such as "http://" or "https://" needs to be included.
        :type Paths: list of str
        :param FlushType: Purge type:
`flush`: purges updated resources
`delete`: purges all resources
        :type FlushType: str
        :param UrlEncode: Whether to encode Chinese characters before purge.
        :type UrlEncode: bool
        """
        self.Paths = None
        self.FlushType = None
        self.UrlEncode = None


    def _deserialize(self, params):
        self.Paths = params.get("Paths")
        self.FlushType = params.get("FlushType")
        self.UrlEncode = params.get("UrlEncode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurgePathCacheResponse(AbstractModel):
    """PurgePathCache response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Purge task ID. Directories submitted in one request share a task ID.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class PurgeTask(AbstractModel):
    """Purge task details.

    """

    def __init__(self):
        r"""
        :param TaskId: Purge task ID
        :type TaskId: str
        :param Url: Purged URL
        :type Url: str
        :param Status: Purge task status
`fail`: purge failed
`done`: purge succeeded
`process`: purge in progress
        :type Status: str
        :param PurgeType: Purge type
`url`: URL purge
`path`: directory purge
        :type PurgeType: str
        :param FlushType: Purge method
`flush`: purges updated resources; this type is available only for directory purges
`delete`: purges all resources
        :type FlushType: str
        :param CreateTime: Purge task submission time
        :type CreateTime: str
        """
        self.TaskId = None
        self.Url = None
        self.Status = None
        self.PurgeType = None
        self.FlushType = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Url = params.get("Url")
        self.Status = params.get("Status")
        self.PurgeType = params.get("PurgeType")
        self.FlushType = params.get("FlushType")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurgeUrlsCacheRequest(AbstractModel):
    """PurgeUrlsCache request structure.

    """

    def __init__(self):
        r"""
        :param Urls: List of URLs. The protocol header such as "http://" or "https://" needs to be included.
        :type Urls: list of str
        :param Area: Purging region
The acceleration region of the acceleration domain name will be purged if this parameter is not passed in
If `mainland` is passed in, only the content cached on nodes in the Chinese mainland will be purged
If `overseas` is passed in, only the content cached on nodes outside the Chinese mainland will be purged
The specified purging region should match the domain name acceleration region
        :type Area: str
        :param UrlEncode: Whether to encode Chinese characters before purge.
        :type UrlEncode: bool
        """
        self.Urls = None
        self.Area = None
        self.UrlEncode = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
        self.Area = params.get("Area")
        self.UrlEncode = params.get("UrlEncode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurgeUrlsCacheResponse(AbstractModel):
    """PurgeUrlsCache response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Purge task ID. URLs submitted in one request share a task ID.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class PushTask(AbstractModel):
    """Prefetch task details.

    """

    def __init__(self):
        r"""
        :param TaskId: Prefetch task ID
        :type TaskId: str
        :param Url: Prefetched URL
        :type Url: str
        :param Status: Prefetch task status
`fail`: prefetch failed
`done`: prefetch succeeded
`process`: prefetch in progress
        :type Status: str
        :param Percent: Prefetch progress in percentage
        :type Percent: int
        :param CreateTime: Prefetch task submission time
        :type CreateTime: str
        :param Area: Prefetch region
`mainland`: within Mainland China
`overseas`: outside Mainland China
`global`: global
        :type Area: str
        :param UpdateTime: Prefetch task update time
Note: this field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        """
        self.TaskId = None
        self.Url = None
        self.Status = None
        self.Percent = None
        self.CreateTime = None
        self.Area = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Url = params.get("Url")
        self.Status = params.get("Status")
        self.Percent = params.get("Percent")
        self.CreateTime = params.get("CreateTime")
        self.Area = params.get("Area")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushUrlsCacheRequest(AbstractModel):
    """PushUrlsCache request structure.

    """

    def __init__(self):
        r"""
        :param Urls: List of URLs. The protocol header such as "http://" or "https://" needs to be included.
        :type Urls: list of str
        :param UserAgent: Specifies the User-Agent header of an HTTP prefetch request when it is forwarded to the origin server
Default value: `TencentCdn`
        :type UserAgent: str
        :param Area: Destination region for the prefetch
`mainland`: prefetches resources to nodes within Mainland China
`overseas`: prefetches resources to nodes outside Mainland China
`global`: prefetches resources to global nodes
Default value: `mainland`. You can prefetch a URL to nodes in a region provided that CDN service has been enabled for the domain name in the URL in the region.
        :type Area: str
        :param Layer: If this parameter is `middle` or left empty, prefetch will be performed onto the intermediate node
        :type Layer: str
        :param ParseM3U8: Whether to recursively resolve the M3U8 index file and prefetch the TS shards in it.
Notes:
1. This feature requires that the M3U8 index file can be directly requested and obtained.
2. In the M3U8 index file, currently only the TS shards at the first to the third level can be recursively resolved.
3. Prefetching the TS shards obtained through recursive resolution consumes the daily prefetch quota. If the usage exceeds the quota, the feature will be disabled and TS shards will not be prefetched.
        :type ParseM3U8: bool
        """
        self.Urls = None
        self.UserAgent = None
        self.Area = None
        self.Layer = None
        self.ParseM3U8 = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
        self.UserAgent = params.get("UserAgent")
        self.Area = params.get("Area")
        self.Layer = params.get("Layer")
        self.ParseM3U8 = params.get("ParseM3U8")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushUrlsCacheResponse(AbstractModel):
    """PushUrlsCache response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: ID of the submitted task
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class QueryStringKey(AbstractModel):
    """A part of `CacheKey`

    """

    def __init__(self):
        r"""
        :param Switch: Whether to use `QueryString` as part of `CacheKey`. Valid values: on, off
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param Reorder: Whether to sort again
Note: this field may return null, indicating that no valid values can be obtained.
        :type Reorder: str
        :param Action: Include/exclude query parameters. Valid values: `includeAll`, `excludeAll`, `includeCustom`, `excludeAll`
Note: this field may return null, indicating that no valid values can be obtained.
        :type Action: str
        :param Value: Array of included/excluded URL parameters (separated by ';')
Note: this field may return null, indicating that no valid values can be obtained.
        :type Value: str
        """
        self.Switch = None
        self.Reorder = None
        self.Action = None
        self.Value = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Reorder = params.get("Reorder")
        self.Action = params.get("Action")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quic(AbstractModel):
    """QUIC configuration item

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable QUIC
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quota(AbstractModel):
    """Purge/Prefetch available usage and quota

    """

    def __init__(self):
        r"""
        :param Batch: Quota limit for one batch submission request.
        :type Batch: int
        :param Total: Daily submission quota limit.
        :type Total: int
        :param Available: Remaining daily submission quota.
        :type Available: int
        :param Area: Quota region.
        :type Area: str
        """
        self.Batch = None
        self.Total = None
        self.Available = None
        self.Area = None


    def _deserialize(self, params):
        self.Batch = params.get("Batch")
        self.Total = params.get("Total")
        self.Available = params.get("Available")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RangeOriginPull(AbstractModel):
    """Range GETs configuration which is enabled by default

    """

    def __init__(self):
        r"""
        :param Switch: Range GETs configuration switch
on: enabled
off: disabled
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Referer(AbstractModel):
    """Referer blocklist/allowlist configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param Switch: Referer blocklist/allowlist configuration switch
on: enabled
off: disabled
        :type Switch: str
        :param RefererRules: Referer blocklist/allowlist configuration rule
Note: this field may return null, indicating that no valid values can be obtained.
        :type RefererRules: list of RefererRule
        """
        self.Switch = None
        self.RefererRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("RefererRules") is not None:
            self.RefererRules = []
            for item in params.get("RefererRules"):
                obj = RefererRule()
                obj._deserialize(item)
                self.RefererRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefererRule(AbstractModel):
    """Referer blocklist/allowlist configuration rules, which is effective for specific resources.

    """

    def __init__(self):
        r"""
        :param RuleType: Rule types:
`all`: effective for all files
`file`: effective for specified file suffixes
`directory`: effective for specified paths
`path`: effective for specified absolute paths
        :type RuleType: str
        :param RulePaths: Content for each RuleType:
For `all`, enter an asterisk (*).
For `file`, enter the suffix, such as jpg, txt.
For `directory`, enter the path, such as /xxx/test/.
For `path`, enter the corresponding absolute path, such as /xxx/test.html.
        :type RulePaths: list of str
        :param RefererType: Referer configuration types
whitelist: allowlist
blacklist: blocklist
        :type RefererType: str
        :param Referers: Referer content list
        :type Referers: list of str
        :param AllowEmpty: Whether to allow empty referer
true: allow empty referer
false: do not allow empty referer
        :type AllowEmpty: bool
        """
        self.RuleType = None
        self.RulePaths = None
        self.RefererType = None
        self.Referers = None
        self.AllowEmpty = None


    def _deserialize(self, params):
        self.RuleType = params.get("RuleType")
        self.RulePaths = params.get("RulePaths")
        self.RefererType = params.get("RefererType")
        self.Referers = params.get("Referers")
        self.AllowEmpty = params.get("AllowEmpty")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionMapRelation(AbstractModel):
    """Association between a region ID and sub-region IDs.

    """

    def __init__(self):
        r"""
        :param RegionId: Region ID
        :type RegionId: int
        :param SubRegionIdList: List of sub-region IDs
        :type SubRegionIdList: list of int
        """
        self.RegionId = None
        self.SubRegionIdList = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.SubRegionIdList = params.get("SubRegionIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportData(AbstractModel):
    """CDN report data

    """

    def __init__(self):
        r"""
        :param ResourceId: Project ID/domain name ID.
        :type ResourceId: str
        :param Resource: Project name/domain name.
        :type Resource: str
        :param Value: Total traffic/max bandwidth in bytes and bps, respectively.
        :type Value: int
        :param Percentage: Percentage of individual resource out of all resources.
        :type Percentage: float
        :param BillingValue: Total billable traffic/max billable bandwidth in bytes and bps, respectively.
        :type BillingValue: int
        :param BillingPercentage: Percentage of billable amount out of total amount.
        :type BillingPercentage: float
        """
        self.ResourceId = None
        self.Resource = None
        self.Value = None
        self.Percentage = None
        self.BillingValue = None
        self.BillingPercentage = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.Resource = params.get("Resource")
        self.Value = params.get("Value")
        self.Percentage = params.get("Percentage")
        self.BillingValue = params.get("BillingValue")
        self.BillingPercentage = params.get("BillingPercentage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestHeader(AbstractModel):
    """Custom request header configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param Switch: Custom request header configuration switch
on: enabled
off: disabled
        :type Switch: str
        :param HeaderRules: Custom request header configuration rules
Note: this field may return null, indicating that no valid values can be obtained.
        :type HeaderRules: list of HttpHeaderPathRule
        """
        self.Switch = None
        self.HeaderRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("HeaderRules") is not None:
            self.HeaderRules = []
            for item in params.get("HeaderRules"):
                obj = HttpHeaderPathRule()
                obj._deserialize(item)
                self.HeaderRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceBillingData(AbstractModel):
    """Billing data details

    """

    def __init__(self):
        r"""
        :param Resource: Resource name, which is categorized as follows based on different query conditions:
Specific domain name: domain name details
multiDomains: aggregated details of multiple domain names
Project ID: displays the ID of the specified project to be queried
all: the details at the account level
        :type Resource: str
        :param BillingData: Billing data details
        :type BillingData: list of CdnData
        """
        self.Resource = None
        self.BillingData = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("BillingData") is not None:
            self.BillingData = []
            for item in params.get("BillingData"):
                obj = CdnData()
                obj._deserialize(item)
                self.BillingData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceData(AbstractModel):
    """This API is used to query an object and its access details

    """

    def __init__(self):
        r"""
        :param Resource: Resource name, which is classified as follows based on different query conditions:
A specific domain name: This indicates the details of this domain name
multiDomains: This indicates the aggregate details of multiple domain names
Project ID: This displays the ID of the specifically queried project
all: This indicates the details at the account level
        :type Resource: str
        :param CdnData: Data details of a resource
        :type CdnData: list of CdnData
        """
        self.Resource = None
        self.CdnData = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("CdnData") is not None:
            self.CdnData = []
            for item in params.get("CdnData"):
                obj = CdnData()
                obj._deserialize(item)
                self.CdnData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceOriginData(AbstractModel):
    """This API is used to query an object and its origin-pull details

    """

    def __init__(self):
        r"""
        :param Resource: Resource name, which is classified as follows based on different query conditions:
A specific domain name: This indicates the details of this domain name
multiDomains: This indicates the aggregate details of multiple domain names
Project ID: This displays the ID of the specifically queried project
all: This indicates the details at the account level
        :type Resource: str
        :param OriginData: Origin-pull data details
        :type OriginData: list of CdnData
        """
        self.Resource = None
        self.OriginData = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("OriginData") is not None:
            self.OriginData = []
            for item in params.get("OriginData"):
                obj = CdnData()
                obj._deserialize(item)
                self.OriginData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResponseHeader(AbstractModel):
    """Custom response header configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param Switch: Custom response header switch
on: enabled
off: disabled
        :type Switch: str
        :param HeaderRules: Custom response header rules
Note: this field may return null, indicating that no valid values can be obtained.
        :type HeaderRules: list of HttpHeaderPathRule
        """
        self.Switch = None
        self.HeaderRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("HeaderRules") is not None:
            self.HeaderRules = []
            for item in params.get("HeaderRules"):
                obj = HttpHeaderPathRule()
                obj._deserialize(item)
                self.HeaderRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResponseHeaderCache(AbstractModel):
    """Origin server header cache configuration. This is enabled by default and caches all the header information.

    """

    def __init__(self):
        r"""
        :param Switch: Origin server header cache switch
on: enabled
off: disabled
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Revalidate(AbstractModel):
    """Whether to forward to the origin server for verification

    """

    def __init__(self):
        r"""
        :param Switch: Whether to always forward to the origin server for verification. Valid values: on, off
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param Path: Forwards to the origin server for verification only for specific request path
Note: this field may return null, indicating that no valid values can be obtained.
        :type Path: str
        """
        self.Switch = None
        self.Path = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleCache(AbstractModel):
    """Path-based cache rule configuration
    The cache expiration time for all files is 30 days by default.
    Static acceleration type domain names .php, .jsp, .asp, and .aspx are not cached by default.

    """

    def __init__(self):
        r"""
        :param RulePaths: Content for each `CacheType`:
For `all`, enter a wildcard `*`.
For `file`, enter the suffix, e.g., `jpg` or `txt`.
For `directory`, enter the path, e.g., `/xxx/test/`.
For `path`, enter the absolute path, e.g., `/xxx/test.html`.
For `index`, enter a forward slash `/`.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RulePaths: list of str
        :param RuleType: Rule types:
`all`: effective for all files.
`file`: effective for specified file suffixes.
`directory`: effective for specified paths.
`path`: effective for specified absolute paths.
`index`: homepage.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RuleType: str
        :param CacheConfig: Cache configuration
Note: this field may return null, indicating that no valid value is obtained.
        :type CacheConfig: :class:`tencentcloud.cdn.v20180606.models.RuleCacheConfig`
        """
        self.RulePaths = None
        self.RuleType = None
        self.CacheConfig = None


    def _deserialize(self, params):
        self.RulePaths = params.get("RulePaths")
        self.RuleType = params.get("RuleType")
        if params.get("CacheConfig") is not None:
            self.CacheConfig = RuleCacheConfig()
            self.CacheConfig._deserialize(params.get("CacheConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleCacheConfig(AbstractModel):
    """Path cache configuration, choose one from the following three cache modes.

    """

    def __init__(self):
        r"""
        :param Cache: Cache configuration
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.CacheConfigCache`
        :param NoCache: No cache configuration
Note: this field may return null, indicating that no valid value is obtained.
        :type NoCache: :class:`tencentcloud.cdn.v20180606.models.CacheConfigNoCache`
        :param FollowOrigin: Follows the origin server configuration
Note: this field may return null, indicating that no valid value is obtained.
        :type FollowOrigin: :class:`tencentcloud.cdn.v20180606.models.CacheConfigFollowOrigin`
        """
        self.Cache = None
        self.NoCache = None
        self.FollowOrigin = None


    def _deserialize(self, params):
        if params.get("Cache") is not None:
            self.Cache = CacheConfigCache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("NoCache") is not None:
            self.NoCache = CacheConfigNoCache()
            self.NoCache._deserialize(params.get("NoCache"))
        if params.get("FollowOrigin") is not None:
            self.FollowOrigin = CacheConfigFollowOrigin()
            self.FollowOrigin._deserialize(params.get("FollowOrigin"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleQueryString(AbstractModel):
    """Configuration to retain query strings for this path

    """

    def __init__(self):
        r"""
        :param Switch: Whether to use `QueryString` as part of `CacheKey`. Valid values: on, off
Note: this field may return null, indicating that no valid value is obtained.
        :type Switch: str
        :param Action: `includeCustom` will retain partial query strings
Note: this field may return null, indicating that no valid value is obtained.
        :type Action: str
        :param Value: Array of included/excluded query strings (separated by ';')
Note: this field may return null, indicating that no valid value is obtained.
        :type Value: str
        """
        self.Switch = None
        self.Action = None
        self.Value = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Action = params.get("Action")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnAclConfig(AbstractModel):
    """SCDN access control

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable. Valid values: `on` and `off`.
        :type Switch: str
        :param ScriptData: ACL rule group, which is required when the access control is on.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ScriptData: list of ScdnAclGroup
        :param ErrorPage: Error page configuration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ScdnErrorPage`
        """
        self.Switch = None
        self.ScriptData = None
        self.ErrorPage = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("ScriptData") is not None:
            self.ScriptData = []
            for item in params.get("ScriptData"):
                obj = ScdnAclGroup()
                obj._deserialize(item)
                self.ScriptData.append(obj)
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ScdnErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnAclGroup(AbstractModel):
    """SCDN precise access control configuration

    """

    def __init__(self):
        r"""
        :param RuleName: Rule name
        :type RuleName: str
        :param Configure: Specific configurations
        :type Configure: list of ScdnAclRule
        :param Result: Rule action, which can be `refuse` or `redirect`.
        :type Result: str
        :param Status: Whether the rule is effective. Valid values: `active` and `inactive`.
        :type Status: str
        :param ErrorPage: Error page configuration.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ScdnErrorPage`
        """
        self.RuleName = None
        self.Configure = None
        self.Result = None
        self.Status = None
        self.ErrorPage = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        if params.get("Configure") is not None:
            self.Configure = []
            for item in params.get("Configure"):
                obj = ScdnAclRule()
                obj._deserialize(item)
                self.Configure.append(obj)
        self.Result = params.get("Result")
        self.Status = params.get("Status")
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ScdnErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnAclRule(AbstractModel):
    """Precise access control match rule

    """

    def __init__(self):
        r"""
        :param MatchKey: Match keywords. Valid values: `params`, `url`, `ip`, `referer`, and `user-agent`.
        :type MatchKey: str
        :param LogiOperator: Logical operator. Valid values: `exclude`, `include`, `notequal`, `equal`, `len-less`, `len-equal`, and `len-more`.
        :type LogiOperator: str
        :param MatchValue: Match value
        :type MatchValue: str
        """
        self.MatchKey = None
        self.LogiOperator = None
        self.MatchValue = None


    def _deserialize(self, params):
        self.MatchKey = params.get("MatchKey")
        self.LogiOperator = params.get("LogiOperator")
        self.MatchValue = params.get("MatchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnBotConfig(AbstractModel):
    """Bot configuration

    """

    def __init__(self):
        r"""
        :param Switch: Valid values: `on` and `off`.
        :type Switch: str
        :param BotCookie: Bot cookie policy
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type BotCookie: list of BotCookie
        :param BotJavaScript: Bot JS policy
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type BotJavaScript: list of BotJavaScript
        """
        self.Switch = None
        self.BotCookie = None
        self.BotJavaScript = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("BotCookie") is not None:
            self.BotCookie = []
            for item in params.get("BotCookie"):
                obj = BotCookie()
                obj._deserialize(item)
                self.BotCookie.append(obj)
        if params.get("BotJavaScript") is not None:
            self.BotJavaScript = []
            for item in params.get("BotJavaScript"):
                obj = BotJavaScript()
                obj._deserialize(item)
                self.BotJavaScript.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnCCRules(AbstractModel):
    """SCDN custom CC rules

    """

    def __init__(self):
        r"""
        :param RuleType: Rule types:
`all`: effective for all files.
`file`: effective for specified file suffixes.
`directory`: effective for specified paths.
`path`: effective for specified absolute paths.
`index`: effective for web homepages and root directories.
        :type RuleType: str
        :param RuleValue: Rule value (blocking condition)
        :type RuleValue: list of str
        :param Qps: IP access limit rule
        :type Qps: int
        :param DetectionTime: Detection granularity
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DetectionTime: int
        :param FrequencyLimit: Frequency threshold
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FrequencyLimit: int
        :param PunishmentSwitch: Whether to block or redirect requests from suspicious IPs. Valid values: `on` and `off`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type PunishmentSwitch: str
        :param PunishmentTime: Suspicious IP restriction duration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type PunishmentTime: int
        :param Action: Action. Valid values: `intercept` and `redirect`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Action: str
        :param RedirectUrl: The redirection target URL used when the `Action` is `redirect`
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RedirectUrl: str
        """
        self.RuleType = None
        self.RuleValue = None
        self.Qps = None
        self.DetectionTime = None
        self.FrequencyLimit = None
        self.PunishmentSwitch = None
        self.PunishmentTime = None
        self.Action = None
        self.RedirectUrl = None


    def _deserialize(self, params):
        self.RuleType = params.get("RuleType")
        self.RuleValue = params.get("RuleValue")
        self.Qps = params.get("Qps")
        self.DetectionTime = params.get("DetectionTime")
        self.FrequencyLimit = params.get("FrequencyLimit")
        self.PunishmentSwitch = params.get("PunishmentSwitch")
        self.PunishmentTime = params.get("PunishmentTime")
        self.Action = params.get("Action")
        self.RedirectUrl = params.get("RedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnConfig(AbstractModel):
    """CC attack defense configuration

    """

    def __init__(self):
        r"""
        :param Switch: Valid values: `on` and `off`.
        :type Switch: str
        :param Rules: Custom CC attack defense rule
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Rules: list of ScdnCCRules
        """
        self.Switch = None
        self.Rules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = ScdnCCRules()
                obj._deserialize(item)
                self.Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnDdosConfig(AbstractModel):
    """DDoS configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable DDoS defense. Valid values: `on` and `off`.
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnErrorPage(AbstractModel):
    """ACL error page

    """

    def __init__(self):
        r"""
        :param RedirectCode: Status code
        :type RedirectCode: int
        :param RedirectUrl: Redirection URL
        :type RedirectUrl: str
        """
        self.RedirectCode = None
        self.RedirectUrl = None


    def _deserialize(self, params):
        self.RedirectCode = params.get("RedirectCode")
        self.RedirectUrl = params.get("RedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnWafConfig(AbstractModel):
    """WAF configuration

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable WAF. Valid values: `on` and `off`.
        :type Switch: str
        :param Mode: WAF protection mode. Valid values: `intercept` and `observe`. Default value: `intercept`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Mode: str
        :param ErrorPage: Redirection error page
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ScdnErrorPage`
        :param WebShellSwitch: Whether to enable Web shell blocking. Valid values: `on` and `off`. Default value: `off`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type WebShellSwitch: str
        :param Rules: Attack blocking rules
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Rules: list of ScdnWafRule
        :param Level: WAF rule level. Valid values: 100, 200, and 300.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Level: int
        :param SubRuleSwitch: WAF sub-rule switch
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SubRuleSwitch: list of WafSubRuleStatus
        """
        self.Switch = None
        self.Mode = None
        self.ErrorPage = None
        self.WebShellSwitch = None
        self.Rules = None
        self.Level = None
        self.SubRuleSwitch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Mode = params.get("Mode")
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ScdnErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        self.WebShellSwitch = params.get("WebShellSwitch")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = ScdnWafRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Level = params.get("Level")
        if params.get("SubRuleSwitch") is not None:
            self.SubRuleSwitch = []
            for item in params.get("SubRuleSwitch"):
                obj = WafSubRuleStatus()
                obj._deserialize(item)
                self.SubRuleSwitch.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnWafRule(AbstractModel):
    """WAF rule information

    """

    def __init__(self):
        r"""
        :param AttackType: Attack type
        :type AttackType: str
        :param Operate: Defense action. Valid value: `observe`.
        :type Operate: str
        """
        self.AttackType = None
        self.Operate = None


    def _deserialize(self, params):
        self.AttackType = params.get("AttackType")
        self.Operate = params.get("Operate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemeKey(AbstractModel):
    """A part of `CacheKey`

    """

    def __init__(self):
        r"""
        :param Switch: Whether to use the scheme as part of the cache key. Valid values: on, off
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchClsLogRequest(AbstractModel):
    """SearchClsLog request structure.

    """

    def __init__(self):
        r"""
        :param LogsetId: ID of logset to be queried
        :type LogsetId: str
        :param TopicIds: List of IDs of log topics to be queried, separated by commas
        :type TopicIds: str
        :param StartTime: Start time of log to be queried in the format of `YYYY-mm-dd HH:MM:SS`
        :type StartTime: str
        :param EndTime: End time of log to be queried in the format of `YYYY-mm-dd HH:MM:SS`
        :type EndTime: str
        :param Limit: Number of logs to be returned at a time. Maximum value: 100
        :type Limit: int
        :param Channel: Connection channel. Default value: cdn
        :type Channel: str
        :param Query: Content to be queried. For more information, please visit https://intl.cloud.tencent.com/document/product/614/16982?from_cn_redirect=1
        :type Query: str
        :param Context: This field is used when loading more results. Pass through the last `context` value returned to get more log content. Up to 10,000 logs can be obtained through the cursor. Please narrow down the time range as much as possible.
        :type Context: str
        :param Sort: Sorting by log time. Valid values: asc (ascending), desc (descending). Default value: desc
        :type Sort: str
        """
        self.LogsetId = None
        self.TopicIds = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Channel = None
        self.Query = None
        self.Context = None
        self.Sort = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicIds = params.get("TopicIds")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Channel = params.get("Channel")
        self.Query = params.get("Query")
        self.Context = params.get("Context")
        self.Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchClsLogResponse(AbstractModel):
    """SearchClsLog response structure.

    """

    def __init__(self):
        r"""
        :param Logs: Query result
        :type Logs: :class:`tencentcloud.cdn.v20180606.models.ClsSearchLogs`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Logs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Logs") is not None:
            self.Logs = ClsSearchLogs()
            self.Logs._deserialize(params.get("Logs"))
        self.RequestId = params.get("RequestId")


class SecurityConfig(AbstractModel):
    """SCDN configuration

    """

    def __init__(self):
        r"""
        :param Switch: on|off
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Seo(AbstractModel):
    """SEO configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param Switch: SEO configuration switch
on: enabled
off: disabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerCert(AbstractModel):
    """HTTPS acceleration server certificate configuration:
    + Supports deployment with certificates that are being hosted by the SSL Certificate Services
    + Supports uploading certificates of PEM format for deployment
    Note: when uploading certificates of PEM format, the Base64 encoding is required.

    """

    def __init__(self):
        r"""
        :param CertId: Server certificate ID
This is auto-generated when the certificate is being hosted by the SSL Certificate Service
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertId: str
        :param CertName: Server certificate name
This is auto-generated when the certificate is being hosted by the SSL Certificate Service
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertName: str
        :param Certificate: Server certificate information
This is required when uploading an external certificate, which should contain the complete certificate chain.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Certificate: str
        :param PrivateKey: Server key information
This is required when uploading an external certificate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateKey: str
        :param ExpireTime: Certificate expiration time
Can be left blank when used as an input parameter
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param DeployTime: Certificate issuance time
Can be left blank when used as an input parameter
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeployTime: str
        :param Message: Certificate remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :type Message: str
        """
        self.CertId = None
        self.CertName = None
        self.Certificate = None
        self.PrivateKey = None
        self.ExpireTime = None
        self.DeployTime = None
        self.Message = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.CertName = params.get("CertName")
        self.Certificate = params.get("Certificate")
        self.PrivateKey = params.get("PrivateKey")
        self.ExpireTime = params.get("ExpireTime")
        self.DeployTime = params.get("DeployTime")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
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
        :param CacheRules: Cache expiration time rules
Note: this field may return null, indicating that no valid values can be obtained.
        :type CacheRules: list of SimpleCacheRule
        :param FollowOrigin: Follows origin server Cache-Control: max-age configurations
on: enabled
off: disabled
If this is enabled, resources that do not match CacheRules rules will be cached by the node according to the max-age value returned by the origin server. Resources that match CacheRules rules will be cached on the node according to the cache expiration time set in CacheRules.
This conflicts with CompareMaxAge. The two cannot be enabled at the same time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FollowOrigin: str
        :param IgnoreCacheControl: Forced cache
on: enable
off: disable
This is disabled by default. If enabled, the `no-store` and `no-cache` resources returned from the origin server will be cached according to `CacheRules` rules.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IgnoreCacheControl: str
        :param IgnoreSetCookie: Ignores the Set-Cookie header of the origin server
on: enabled
off: disabled
This is disabled by default
Note: this field may return null, indicating that no valid values can be obtained.
        :type IgnoreSetCookie: str
        :param CompareMaxAge: Advanced cache expiration configuration. If this is enabled, the max-age value returned by the origin server will be compared with the cache expiration time set in CacheRules, and the smallest value will be cached on the node.
on: enabled
off: disabled
This is disabled by default
Note: this field may return null, indicating that no valid values can be obtained.
        :type CompareMaxAge: str
        :param Revalidate: Always forwards to the origin server for verification
Note: this field may return null, indicating that no valid values can be obtained.
        :type Revalidate: :class:`tencentcloud.cdn.v20180606.models.Revalidate`
        """
        self.CacheRules = None
        self.FollowOrigin = None
        self.IgnoreCacheControl = None
        self.IgnoreSetCookie = None
        self.CompareMaxAge = None
        self.Revalidate = None


    def _deserialize(self, params):
        if params.get("CacheRules") is not None:
            self.CacheRules = []
            for item in params.get("CacheRules"):
                obj = SimpleCacheRule()
                obj._deserialize(item)
                self.CacheRules.append(obj)
        self.FollowOrigin = params.get("FollowOrigin")
        self.IgnoreCacheControl = params.get("IgnoreCacheControl")
        self.IgnoreSetCookie = params.get("IgnoreSetCookie")
        self.CompareMaxAge = params.get("CompareMaxAge")
        if params.get("Revalidate") is not None:
            self.Revalidate = Revalidate()
            self.Revalidate._deserialize(params.get("Revalidate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SimpleCacheRule(AbstractModel):
    """Cache expiration rules configuration

    """

    def __init__(self):
        r"""
        :param CacheType: Rule types:
`all`: effective for all files
`file`: effective for specified file suffixes
`directory`: effective for specified paths
`path`: effective for specified absolute paths
index: home page
        :type CacheType: str
        :param CacheContents: Content for each CacheType:
Enter `*` for `all`
Enter an extension for `file`, such as `jpg` or `txt`
Enter a path for `directory`, such as `/xxx/test`
Enter an absolute path for `path`, such as `/xxx/test.html`
Enter `/` for `index`
        :type CacheContents: list of str
        :param CacheTime: Cache expiration time settings
Unit: second. The maximum value is 365 days.
        :type CacheTime: int
        """
        self.CacheType = None
        self.CacheContents = None
        self.CacheTime = None


    def _deserialize(self, params):
        self.CacheType = params.get("CacheType")
        self.CacheContents = params.get("CacheContents")
        self.CacheTime = params.get("CacheTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Sort(AbstractModel):
    """Sorting conditions for query results.

    """

    def __init__(self):
        r"""
        :param Key: Fields that can be sorted. Currently supports:
`createTime`: domain name creation time.
`certExpireTime`: certificate expiration time.
Default value: createTime.
        :type Key: str
        :param Sequence: `asc` or `desc`. Default: `desc`.
        :type Sequence: str
        """
        self.Key = None
        self.Sequence = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Sequence = params.get("Sequence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecificConfig(AbstractModel):
    """Specific configuration for domain names inside and outside mainland China by regions.

    """

    def __init__(self):
        r"""
        :param Mainland: Specific configuration for domain name inside mainland China.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Mainland: :class:`tencentcloud.cdn.v20180606.models.MainlandConfig`
        :param Overseas: Specific configuration for domain name outside mainland China.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Overseas: :class:`tencentcloud.cdn.v20180606.models.OverseaConfig`
        """
        self.Mainland = None
        self.Overseas = None


    def _deserialize(self, params):
        if params.get("Mainland") is not None:
            self.Mainland = MainlandConfig()
            self.Mainland._deserialize(params.get("Mainland"))
        if params.get("Overseas") is not None:
            self.Overseas = OverseaConfig()
            self.Overseas._deserialize(params.get("Overseas"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartCdnDomainRequest(AbstractModel):
    """StartCdnDomain request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain name
The domain name status should be `Disabled`
        :type Domain: str
        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartCdnDomainResponse(AbstractModel):
    """StartCdnDomain response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StatusCodeCache(AbstractModel):
    """Status code cache expiration configuration. 404 status codes are cached for 10 seconds by default

    """

    def __init__(self):
        r"""
        :param Switch: Status code cache expiration configuration switch
on: enabled
off: disabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param CacheRules: Status code cache expiration rules details
Note: this field may return null, indicating that no valid values can be obtained.
        :type CacheRules: list of StatusCodeCacheRule
        """
        self.Switch = None
        self.CacheRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("CacheRules") is not None:
            self.CacheRules = []
            for item in params.get("CacheRules"):
                obj = StatusCodeCacheRule()
                obj._deserialize(item)
                self.CacheRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatusCodeCacheRule(AbstractModel):
    """Status code cache expiration time rule configuration

    """

    def __init__(self):
        r"""
        :param StatusCode: HTTP status code
Supports 403 and 404 status codes
        :type StatusCode: str
        :param CacheTime: Status code cache expiration time (in seconds)
        :type CacheTime: int
        """
        self.StatusCode = None
        self.CacheTime = None


    def _deserialize(self, params):
        self.StatusCode = params.get("StatusCode")
        self.CacheTime = params.get("CacheTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopCdnDomainRequest(AbstractModel):
    """StopCdnDomain request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain name
The domain name status should be **Enabled**
        :type Domain: str
        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopCdnDomainResponse(AbstractModel):
    """StopCdnDomain response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SummarizedData(AbstractModel):
    """Aggregate values of details; each metric has different aggregation methods based on its characteristics

    """

    def __init__(self):
        r"""
        :param Name: Aggregation method, which can be:
sum: aggregate summation
max: maximum value; in bandwidth mode, the peak bandwidth is calculated based on the aggregate data with 5-minute granularity.
avg: average value
        :type Name: str
        :param Value: Aggregate data value
        :type Value: float
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Domain name tag configuration

    """

    def __init__(self):
        r"""
        :param TagKey: Tag key
Note: this field may return null, indicating that no valid value is obtained.
        :type TagKey: str
        :param TagValue: Tag value.
Note: this field may return null, indicating that no valid value is obtained.
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimestampData(AbstractModel):
    """Timestamp and its corresponding value

    """

    def __init__(self):
        r"""
        :param Time: Statistical point in time in forward rounding mode
Taking the 5-minute granularity as an example, 13:35:00 indicates that the statistical interval is between 13:35:00 and 13:39:59.
        :type Time: str
        :param Value: Data value
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
        


class TopData(AbstractModel):
    """Data structure of sorted data

    """

    def __init__(self):
        r"""
        :param Resource: Resource name, which is classified as follows based on different query conditions:
A specific domain name: This indicates the details of this domain name
multiDomains: This indicates the aggregate details of multiple domain names
Project ID: This displays the ID of the specifically queried project
all: This indicates the details at the account level
        :type Resource: str
        :param DetailData: Detailed sorting results
        :type DetailData: list of TopDetailData
        """
        self.Resource = None
        self.DetailData = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("DetailData") is not None:
            self.DetailData = []
            for item in params.get("DetailData"):
                obj = TopDetailData()
                obj._deserialize(item)
                self.DetailData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopDetailData(AbstractModel):
    """Data structure of sorted data

    """

    def __init__(self):
        r"""
        :param Name: Datatype name
        :type Name: str
        :param Value: Data value
        :type Value: float
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicInfo(AbstractModel):
    """CLS topic information

    """

    def __init__(self):
        r"""
        :param TopicId: Topic ID
        :type TopicId: str
        :param TopicName: Topic name
        :type TopicName: str
        :param Enabled: Whether to enable publishing
        :type Enabled: int
        :param CreateTime: Creation time
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param Channel: Either `cdn` or `ecdn`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Channel: str
        """
        self.TopicId = None
        self.TopicName = None
        self.Enabled = None
        self.CreateTime = None
        self.Channel = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.Enabled = params.get("Enabled")
        self.CreateTime = params.get("CreateTime")
        self.Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TpgAdapter(AbstractModel):
    """Image optimization - `TpgAdapter` configuration

    """

    def __init__(self):
        r"""
        :param Switch: Switch. Valid values: on, off
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDomainConfigRequest(AbstractModel):
    """UpdateDomainConfig request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain name
        :type Domain: str
        :param ProjectId: Project ID
        :type ProjectId: int
        :param Origin: Origin server configuration
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param IpFilter: IP blocklist/allowlist configuration
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param IpFreqLimit: IP access limit configuration
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param StatusCodeCache: Status code cache configuration
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param Compression: Smart compression configuration
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param BandwidthAlert: Bandwidth cap configuration
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param RangeOriginPull: Range GETs configuration
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param FollowRedirect: 301/302 origin-pull follow-redirect configuration
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param ErrorPage: Error code redirect configuration (This feature is in beta and not generally available yet.)
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param RequestHeader: Request header configuration
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param ResponseHeader: Response header configuration
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param DownstreamCapping: Download speed configuration
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param CacheKey: Node cache key configuration
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param ResponseHeaderCache: Header cache configuration
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param VideoSeek: Video dragging configuration
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        :param Cache: Cache expiration time configuration
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param OriginPullOptimization: Cross-border linkage optimization configuration
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param Https: HTTPS acceleration configuration
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param Authentication: Timestamp hotlink protection configuration
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param Seo: SEO configuration
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param ForceRedirect: Access protocol forced redirect configuration
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param Referer: Referer hotlink protection configuration
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param MaxAge: Browser cache configuration (This feature is in beta and not generally available yet.)
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param ServiceType: Domain name service type
web: static acceleration
download: download acceleration
media: streaming media VOD acceleration
        :type ServiceType: str
        :param SpecificConfig: Specific region configuration
Applicable to cases where the acceleration domain name configuration differs for regions in and outside mainland China.
        :type SpecificConfig: :class:`tencentcloud.cdn.v20180606.models.SpecificConfig`
        :param Area: Domain name acceleration region
mainland: acceleration inside mainland China
overseas: acceleration outside mainland China
global: global acceleration
        :type Area: str
        :param OriginPullTimeout: Origin-pull timeout configuration
        :type OriginPullTimeout: :class:`tencentcloud.cdn.v20180606.models.OriginPullTimeout`
        :param AwsPrivateAccess: Origin access authentication for S3 bucket
        :type AwsPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`
        :param UserAgentFilter: UA blocklist/allowlist Configuration
        :type UserAgentFilter: :class:`tencentcloud.cdn.v20180606.models.UserAgentFilter`
        :param AccessControl: Access control
        :type AccessControl: :class:`tencentcloud.cdn.v20180606.models.AccessControl`
        :param UrlRedirect: URL redirect configuration
        :type UrlRedirect: :class:`tencentcloud.cdn.v20180606.models.UrlRedirect`
        :param AccessPort: Access port configuration
        :type AccessPort: list of int
        :param AdvancedAuthentication: Timestamp hotlink protection advanced configuration (allowlist feature)
        :type AdvancedAuthentication: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthentication`
        :param OriginAuthentication: Origin-pull authentication advanced configuration (allowlist feature)
        :type OriginAuthentication: :class:`tencentcloud.cdn.v20180606.models.OriginAuthentication`
        :param Ipv6Access: IPv6 access configuration
        :type Ipv6Access: :class:`tencentcloud.cdn.v20180606.models.Ipv6Access`
        :param OfflineCache: Offline cache
        :type OfflineCache: :class:`tencentcloud.cdn.v20180606.models.OfflineCache`
        :param OriginCombine: Merging pull requests
        :type OriginCombine: :class:`tencentcloud.cdn.v20180606.models.OriginCombine`
        :param Quic: QUIC is in beta now. Please submit an application to join the beta. For more information, please see QUIC product documents.
        :type Quic: :class:`tencentcloud.cdn.v20180606.models.Quic`
        :param OssPrivateAccess: Access authentication for OSS origin
        :type OssPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.OssPrivateAccess`
        :param WebSocket: WebSocket configuration.
        :type WebSocket: :class:`tencentcloud.cdn.v20180606.models.WebSocket`
        """
        self.Domain = None
        self.ProjectId = None
        self.Origin = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.StatusCodeCache = None
        self.Compression = None
        self.BandwidthAlert = None
        self.RangeOriginPull = None
        self.FollowRedirect = None
        self.ErrorPage = None
        self.RequestHeader = None
        self.ResponseHeader = None
        self.DownstreamCapping = None
        self.CacheKey = None
        self.ResponseHeaderCache = None
        self.VideoSeek = None
        self.Cache = None
        self.OriginPullOptimization = None
        self.Https = None
        self.Authentication = None
        self.Seo = None
        self.ForceRedirect = None
        self.Referer = None
        self.MaxAge = None
        self.ServiceType = None
        self.SpecificConfig = None
        self.Area = None
        self.OriginPullTimeout = None
        self.AwsPrivateAccess = None
        self.UserAgentFilter = None
        self.AccessControl = None
        self.UrlRedirect = None
        self.AccessPort = None
        self.AdvancedAuthentication = None
        self.OriginAuthentication = None
        self.Ipv6Access = None
        self.OfflineCache = None
        self.OriginCombine = None
        self.Quic = None
        self.OssPrivateAccess = None
        self.WebSocket = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.ProjectId = params.get("ProjectId")
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("StatusCodeCache") is not None:
            self.StatusCodeCache = StatusCodeCache()
            self.StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("BandwidthAlert") is not None:
            self.BandwidthAlert = BandwidthAlert()
            self.BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("RangeOriginPull") is not None:
            self.RangeOriginPull = RangeOriginPull()
            self.RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("FollowRedirect") is not None:
            self.FollowRedirect = FollowRedirect()
            self.FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("RequestHeader") is not None:
            self.RequestHeader = RequestHeader()
            self.RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("DownstreamCapping") is not None:
            self.DownstreamCapping = DownstreamCapping()
            self.DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("ResponseHeaderCache") is not None:
            self.ResponseHeaderCache = ResponseHeaderCache()
            self.ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("VideoSeek") is not None:
            self.VideoSeek = VideoSeek()
            self.VideoSeek._deserialize(params.get("VideoSeek"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("OriginPullOptimization") is not None:
            self.OriginPullOptimization = OriginPullOptimization()
            self.OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("Authentication") is not None:
            self.Authentication = Authentication()
            self.Authentication._deserialize(params.get("Authentication"))
        if params.get("Seo") is not None:
            self.Seo = Seo()
            self.Seo._deserialize(params.get("Seo"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Referer") is not None:
            self.Referer = Referer()
            self.Referer._deserialize(params.get("Referer"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        self.ServiceType = params.get("ServiceType")
        if params.get("SpecificConfig") is not None:
            self.SpecificConfig = SpecificConfig()
            self.SpecificConfig._deserialize(params.get("SpecificConfig"))
        self.Area = params.get("Area")
        if params.get("OriginPullTimeout") is not None:
            self.OriginPullTimeout = OriginPullTimeout()
            self.OriginPullTimeout._deserialize(params.get("OriginPullTimeout"))
        if params.get("AwsPrivateAccess") is not None:
            self.AwsPrivateAccess = AwsPrivateAccess()
            self.AwsPrivateAccess._deserialize(params.get("AwsPrivateAccess"))
        if params.get("UserAgentFilter") is not None:
            self.UserAgentFilter = UserAgentFilter()
            self.UserAgentFilter._deserialize(params.get("UserAgentFilter"))
        if params.get("AccessControl") is not None:
            self.AccessControl = AccessControl()
            self.AccessControl._deserialize(params.get("AccessControl"))
        if params.get("UrlRedirect") is not None:
            self.UrlRedirect = UrlRedirect()
            self.UrlRedirect._deserialize(params.get("UrlRedirect"))
        self.AccessPort = params.get("AccessPort")
        if params.get("AdvancedAuthentication") is not None:
            self.AdvancedAuthentication = AdvancedAuthentication()
            self.AdvancedAuthentication._deserialize(params.get("AdvancedAuthentication"))
        if params.get("OriginAuthentication") is not None:
            self.OriginAuthentication = OriginAuthentication()
            self.OriginAuthentication._deserialize(params.get("OriginAuthentication"))
        if params.get("Ipv6Access") is not None:
            self.Ipv6Access = Ipv6Access()
            self.Ipv6Access._deserialize(params.get("Ipv6Access"))
        if params.get("OfflineCache") is not None:
            self.OfflineCache = OfflineCache()
            self.OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("OriginCombine") is not None:
            self.OriginCombine = OriginCombine()
            self.OriginCombine._deserialize(params.get("OriginCombine"))
        if params.get("Quic") is not None:
            self.Quic = Quic()
            self.Quic._deserialize(params.get("Quic"))
        if params.get("OssPrivateAccess") is not None:
            self.OssPrivateAccess = OssPrivateAccess()
            self.OssPrivateAccess._deserialize(params.get("OssPrivateAccess"))
        if params.get("WebSocket") is not None:
            self.WebSocket = WebSocket()
            self.WebSocket._deserialize(params.get("WebSocket"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDomainConfigResponse(AbstractModel):
    """UpdateDomainConfig response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdatePayTypeRequest(AbstractModel):
    """UpdatePayType request structure.

    """

    def __init__(self):
        r"""
        :param Area: Billing region, which can be mainland or overseas.
        :type Area: str
        :param PayType: Billing mode, which can be flux or bandwidth.
        :type PayType: str
        """
        self.Area = None
        self.PayType = None


    def _deserialize(self, params):
        self.Area = params.get("Area")
        self.PayType = params.get("PayType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePayTypeResponse(AbstractModel):
    """UpdatePayType response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateScdnDomainRequest(AbstractModel):
    """UpdateScdnDomain request structure.

    """

    def __init__(self):
        r"""
        :param Domain: Domain name
        :type Domain: str
        :param Waf: WAF configuration
        :type Waf: :class:`tencentcloud.cdn.v20180606.models.ScdnWafConfig`
        :param Acl: Custom defense policy configuration
        :type Acl: :class:`tencentcloud.cdn.v20180606.models.ScdnAclConfig`
        :param CC: CC attack defense configurations. CC attack defense is enabled by default.
        :type CC: :class:`tencentcloud.cdn.v20180606.models.ScdnConfig`
        :param Ddos: DDoS defense configuration. DDoS defense is enabled by default.
        :type Ddos: :class:`tencentcloud.cdn.v20180606.models.ScdnDdosConfig`
        :param Bot: Bot defense configuration
        :type Bot: :class:`tencentcloud.cdn.v20180606.models.ScdnBotConfig`
        """
        self.Domain = None
        self.Waf = None
        self.Acl = None
        self.CC = None
        self.Ddos = None
        self.Bot = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("Waf") is not None:
            self.Waf = ScdnWafConfig()
            self.Waf._deserialize(params.get("Waf"))
        if params.get("Acl") is not None:
            self.Acl = ScdnAclConfig()
            self.Acl._deserialize(params.get("Acl"))
        if params.get("CC") is not None:
            self.CC = ScdnConfig()
            self.CC._deserialize(params.get("CC"))
        if params.get("Ddos") is not None:
            self.Ddos = ScdnDdosConfig()
            self.Ddos._deserialize(params.get("Ddos"))
        if params.get("Bot") is not None:
            self.Bot = ScdnBotConfig()
            self.Bot._deserialize(params.get("Bot"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateScdnDomainResponse(AbstractModel):
    """UpdateScdnDomain response structure.

    """

    def __init__(self):
        r"""
        :param Result: Result of the request. `Success` indicates that the configurations are updated.
        :type Result: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UrlRecord(AbstractModel):
    """Details of the blocked URLs

    """

    def __init__(self):
        r"""
        :param Status: Status (disable: blocked; enable: unblocked)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param RealUrl: Corresponding URL
Note: This field may return null, indicating that no valid values can be obtained.
        :type RealUrl: str
        :param CreateTime: Creation time
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param UpdateTime: Update time
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        """
        self.Status = None
        self.RealUrl = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RealUrl = params.get("RealUrl")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UrlRedirect(AbstractModel):
    """URL redirect configuration

    """

    def __init__(self):
        r"""
        :param Switch: URL redirect configuration switch
on: enabled
off: disabled
        :type Switch: str
        :param PathRules: URL redirect rule, which is required if `Switch` is `on`. There can be up to 10 rules.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PathRules: list of UrlRedirectRule
        """
        self.Switch = None
        self.PathRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("PathRules") is not None:
            self.PathRules = []
            for item in params.get("PathRules"):
                obj = UrlRedirectRule()
                obj._deserialize(item)
                self.PathRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UrlRedirectRule(AbstractModel):
    """URL redirect rule configuration

    """

    def __init__(self):
        r"""
        :param RedirectStatusCode: Redirect status code. Valid values: 301, 302
        :type RedirectStatusCode: int
        :param Pattern: URL to be matched. Only URLs are supported, while parameters are not. The exact match is used by default. In regex match, up to 5 wildcards `*` are supported. The URL can contain up to 1,024 characters.
        :type Pattern: str
        :param RedirectUrl: Target URL, starting with `/` and excluding parameters. The path can contain up to 1,024 characters. The wildcards in the matching path can be respectively captured using `$1`, `$2`, `$3`, `$4`, and `$5`. Up to 10 values can be captured.
        :type RedirectUrl: str
        :param RedirectHost: Target host. It should be a standard domain name starting with `http://` or `https://`. If it is left empty, “http://[current domain name]” will be used by default.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RedirectHost: str
        """
        self.RedirectStatusCode = None
        self.Pattern = None
        self.RedirectUrl = None
        self.RedirectHost = None


    def _deserialize(self, params):
        self.RedirectStatusCode = params.get("RedirectStatusCode")
        self.Pattern = params.get("Pattern")
        self.RedirectUrl = params.get("RedirectUrl")
        self.RedirectHost = params.get("RedirectHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserAgentFilter(AbstractModel):
    """`UserAgent` blocklist/allowlist configuration

    """

    def __init__(self):
        r"""
        :param Switch: Switch. Valid values: on, off
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param FilterRules: UA blocklist/allowlist effect rule list
Note: this field may return null, indicating that no valid values can be obtained.
        :type FilterRules: list of UserAgentFilterRule
        """
        self.Switch = None
        self.FilterRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("FilterRules") is not None:
            self.FilterRules = []
            for item in params.get("FilterRules"):
                obj = UserAgentFilterRule()
                obj._deserialize(item)
                self.FilterRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserAgentFilterRule(AbstractModel):
    """`UserAgent` blocklist/allowlist rule configuration

    """

    def __init__(self):
        r"""
        :param RuleType: Effective access path type
all: all access paths are effective
file: effective by file extension
directory: effective by directory
path: effective by full access path
Note: this field may return null, indicating that no valid values can be obtained.
        :type RuleType: str
        :param RulePaths: Effective access paths
Note: this field may return null, indicating that no valid values can be obtained.
        :type RulePaths: list of str
        :param UserAgents: `UserAgent` list
Note: this field may return null, indicating that no valid values can be obtained.
        :type UserAgents: list of str
        :param FilterType: blocklist or allowlist. Valid values: blacklist, whitelist
Note: this field may return null, indicating that no valid values can be obtained.
        :type FilterType: str
        """
        self.RuleType = None
        self.RulePaths = None
        self.UserAgents = None
        self.FilterType = None


    def _deserialize(self, params):
        self.RuleType = params.get("RuleType")
        self.RulePaths = params.get("RulePaths")
        self.UserAgents = params.get("UserAgents")
        self.FilterType = params.get("FilterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VideoSeek(AbstractModel):
    """Video dragging configuration. This is disabled by default.

    """

    def __init__(self):
        r"""
        :param Switch: Video dragging switch
on: enabled
off: disabled
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ViolationUrl(AbstractModel):
    """Details of URLs in violation

    """

    def __init__(self):
        r"""
        :param Id: ID
        :type Id: int
        :param RealUrl: Origin access URL of the resource in violation
        :type RealUrl: str
        :param DownloadUrl: Snapshot path. This is used to display a snapshot of the content in violation on the console.
        :type DownloadUrl: str
        :param UrlStatus: Current status of the resources in violation
forbid: blocked
release: unblocked
delay: processing delayed 
reject: appeal dismissed. The status is still blocked.
complain: appeal in process
        :type UrlStatus: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param UpdateTime: Update time
        :type UpdateTime: str
        """
        self.Id = None
        self.RealUrl = None
        self.DownloadUrl = None
        self.UrlStatus = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RealUrl = params.get("RealUrl")
        self.DownloadUrl = params.get("DownloadUrl")
        self.UrlStatus = params.get("UrlStatus")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafSubRuleStatus(AbstractModel):
    """WAF sub-rule switch status

    """

    def __init__(self):
        r"""
        :param Switch: Sub-rule status. Valid values: `on` and `off`.
        :type Switch: str
        :param SubIds: List of rule IDs
        :type SubIds: list of int
        """
        self.Switch = None
        self.SubIds = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.SubIds = params.get("SubIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebSocket(AbstractModel):
    """WebSocket configuration.

    """

    def __init__(self):
        r"""
        :param Switch: Whether to enable custom WebSocket timeout setting. When it’s `off`: WebSocket connection is supported, and the default timeout period is 15 seconds. To change the timeout period, please set it to `on`.

* WebSocket is now only available for beta users. To use it, please submit a ticket.
        :type Switch: str
        :param Timeout: Sets the timeout period in seconds. Maximum value: 65.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Timeout: int
        """
        self.Switch = None
        self.Timeout = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebpAdapter(AbstractModel):
    """Image optimization - `WebpAdapter` configuration

    """

    def __init__(self):
        r"""
        :param Switch: Switch. Valid values: on, off
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        