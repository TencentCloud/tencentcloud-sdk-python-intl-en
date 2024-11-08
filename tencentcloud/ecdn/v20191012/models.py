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


class AddEcdnDomainRequest(AbstractModel):
    """AddEcdnDomain request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain name.
        :type Domain: str
        :param _Origin: Origin server configuration.
        :type Origin: :class:`tencentcloud.ecdn.v20191012.models.Origin`
        :param _Area: Domain name acceleration region. Valid values: mainland (acceleration in Mainland China), overseas (acceleration outside Mainland China), global (global acceleration).
        :type Area: str
        :param _ProjectId: Project ID. Default value: 0.
        :type ProjectId: int
        :param _IpFilter: IP block/allowlist configuration.
        :type IpFilter: :class:`tencentcloud.ecdn.v20191012.models.IpFilter`
        :param _IpFreqLimit: IP access limit configuration.
        :type IpFreqLimit: :class:`tencentcloud.ecdn.v20191012.models.IpFreqLimit`
        :param _ResponseHeader: Origin server response header configuration.
        :type ResponseHeader: :class:`tencentcloud.ecdn.v20191012.models.ResponseHeader`
        :param _CacheKey: Node caching configuration.
        :type CacheKey: :class:`tencentcloud.ecdn.v20191012.models.CacheKey`
        :param _Cache: Caching rule configuration.
        :type Cache: :class:`tencentcloud.ecdn.v20191012.models.Cache`
        :param _Https: HTTPS configuration.
        :type Https: :class:`tencentcloud.ecdn.v20191012.models.Https`
        :param _ForceRedirect: Forced access protocol redirection configuration.
        :type ForceRedirect: :class:`tencentcloud.ecdn.v20191012.models.ForceRedirect`
        :param _Tag: Tag bound to a domain name.
        :type Tag: list of Tag
        :param _WebSocket: WebSocket configuration.
        :type WebSocket: :class:`tencentcloud.ecdn.v20191012.models.WebSocket`
        """
        self._Domain = None
        self._Origin = None
        self._Area = None
        self._ProjectId = None
        self._IpFilter = None
        self._IpFreqLimit = None
        self._ResponseHeader = None
        self._CacheKey = None
        self._Cache = None
        self._Https = None
        self._ForceRedirect = None
        self._Tag = None
        self._WebSocket = None

    @property
    def Domain(self):
        """Domain name.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Origin(self):
        """Origin server configuration.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.Origin`
        """
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def Area(self):
        """Domain name acceleration region. Valid values: mainland (acceleration in Mainland China), overseas (acceleration outside Mainland China), global (global acceleration).
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def ProjectId(self):
        """Project ID. Default value: 0.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def IpFilter(self):
        """IP block/allowlist configuration.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.IpFilter`
        """
        return self._IpFilter

    @IpFilter.setter
    def IpFilter(self, IpFilter):
        self._IpFilter = IpFilter

    @property
    def IpFreqLimit(self):
        """IP access limit configuration.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.IpFreqLimit`
        """
        return self._IpFreqLimit

    @IpFreqLimit.setter
    def IpFreqLimit(self, IpFreqLimit):
        self._IpFreqLimit = IpFreqLimit

    @property
    def ResponseHeader(self):
        """Origin server response header configuration.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.ResponseHeader`
        """
        return self._ResponseHeader

    @ResponseHeader.setter
    def ResponseHeader(self, ResponseHeader):
        self._ResponseHeader = ResponseHeader

    @property
    def CacheKey(self):
        """Node caching configuration.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.CacheKey`
        """
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def Cache(self):
        """Caching rule configuration.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.Cache`
        """
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def Https(self):
        """HTTPS configuration.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.Https`
        """
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def ForceRedirect(self):
        """Forced access protocol redirection configuration.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.ForceRedirect`
        """
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def Tag(self):
        """Tag bound to a domain name.
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def WebSocket(self):
        """WebSocket configuration.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.WebSocket`
        """
        return self._WebSocket

    @WebSocket.setter
    def WebSocket(self, WebSocket):
        self._WebSocket = WebSocket


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        self._Area = params.get("Area")
        self._ProjectId = params.get("ProjectId")
        if params.get("IpFilter") is not None:
            self._IpFilter = IpFilter()
            self._IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self._IpFreqLimit = IpFreqLimit()
            self._IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("ResponseHeader") is not None:
            self._ResponseHeader = ResponseHeader()
            self._ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Cache") is not None:
            self._Cache = Cache()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirect()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        if params.get("WebSocket") is not None:
            self._WebSocket = WebSocket()
            self._WebSocket._deserialize(params.get("WebSocket"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddEcdnDomainResponse(AbstractModel):
    """AddEcdnDomain response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AdvanceHttps(AbstractModel):
    """Custom HTTPS configuration for origin-pull

    """

    def __init__(self):
        r"""
        :param _CustomTlsStatus: Custom TLS data switch
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CustomTlsStatus: str
        :param _TlsVersion: TLS version settings. Valid values: `TLSv1`, `TLSV1.1`, `TLSV1.2`, and `TLSv1.3`. Only consecutive versions can be enabled at the same time.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type TlsVersion: list of str
        :param _Cipher: Custom encryption suite
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Cipher: str
        :param _VerifyOriginType: Origin-pull verification status
`off`: Disables origin-pull verification
`oneWay`: Only verify the origin
`twoWay`: Enables two-way origin-pull verification
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type VerifyOriginType: str
        :param _CertInfo: Configuration information of the origin-pull certificate
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CertInfo: :class:`tencentcloud.ecdn.v20191012.models.ServerCert`
        :param _OriginCertInfo: Configuration information of the origin server certificate
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type OriginCertInfo: :class:`tencentcloud.ecdn.v20191012.models.ClientCert`
        """
        self._CustomTlsStatus = None
        self._TlsVersion = None
        self._Cipher = None
        self._VerifyOriginType = None
        self._CertInfo = None
        self._OriginCertInfo = None

    @property
    def CustomTlsStatus(self):
        """Custom TLS data switch
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CustomTlsStatus

    @CustomTlsStatus.setter
    def CustomTlsStatus(self, CustomTlsStatus):
        self._CustomTlsStatus = CustomTlsStatus

    @property
    def TlsVersion(self):
        """TLS version settings. Valid values: `TLSv1`, `TLSV1.1`, `TLSV1.2`, and `TLSv1.3`. Only consecutive versions can be enabled at the same time.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._TlsVersion

    @TlsVersion.setter
    def TlsVersion(self, TlsVersion):
        self._TlsVersion = TlsVersion

    @property
    def Cipher(self):
        """Custom encryption suite
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Cipher

    @Cipher.setter
    def Cipher(self, Cipher):
        self._Cipher = Cipher

    @property
    def VerifyOriginType(self):
        """Origin-pull verification status
`off`: Disables origin-pull verification
`oneWay`: Only verify the origin
`twoWay`: Enables two-way origin-pull verification
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VerifyOriginType

    @VerifyOriginType.setter
    def VerifyOriginType(self, VerifyOriginType):
        self._VerifyOriginType = VerifyOriginType

    @property
    def CertInfo(self):
        """Configuration information of the origin-pull certificate
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.ServerCert`
        """
        return self._CertInfo

    @CertInfo.setter
    def CertInfo(self, CertInfo):
        self._CertInfo = CertInfo

    @property
    def OriginCertInfo(self):
        """Configuration information of the origin server certificate
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.ClientCert`
        """
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
        


class Cache(AbstractModel):
    """Simple edition of cache configuration, which does not support setting a caching rule for scenarios where the `max-age` is not returned from the origin server.

    """

    def __init__(self):
        r"""
        :param _CacheRules: Caching configuration rule array.
        :type CacheRules: list of CacheRule
        :param _FollowOrigin: Whether to follow the `Cache-Control: max-age` configuration on the origin server (this feature is only available to users on the allowlist).
on: enable
off: disable
If it is enabled, resources that do not match `CacheRules` will be cached on node according to the `max-age` value returned by the origin server, while resources that match `CacheRules` will be cached on node according to the cache expiration time set in `CacheRules`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FollowOrigin: str
        """
        self._CacheRules = None
        self._FollowOrigin = None

    @property
    def CacheRules(self):
        """Caching configuration rule array.
        :rtype: list of CacheRule
        """
        return self._CacheRules

    @CacheRules.setter
    def CacheRules(self, CacheRules):
        self._CacheRules = CacheRules

    @property
    def FollowOrigin(self):
        """Whether to follow the `Cache-Control: max-age` configuration on the origin server (this feature is only available to users on the allowlist).
on: enable
off: disable
If it is enabled, resources that do not match `CacheRules` will be cached on node according to the `max-age` value returned by the origin server, while resources that match `CacheRules` will be cached on node according to the cache expiration time set in `CacheRules`.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FollowOrigin

    @FollowOrigin.setter
    def FollowOrigin(self, FollowOrigin):
        self._FollowOrigin = FollowOrigin


    def _deserialize(self, params):
        if params.get("CacheRules") is not None:
            self._CacheRules = []
            for item in params.get("CacheRules"):
                obj = CacheRule()
                obj._deserialize(item)
                self._CacheRules.append(obj)
        self._FollowOrigin = params.get("FollowOrigin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheKey(AbstractModel):
    """Caching configuration.

    """

    def __init__(self):
        r"""
        :param _FullUrlCache: Whether to enable full path cache. Valid values: on, off.
        :type FullUrlCache: str
        """
        self._FullUrlCache = None

    @property
    def FullUrlCache(self):
        """Whether to enable full path cache. Valid values: on, off.
        :rtype: str
        """
        return self._FullUrlCache

    @FullUrlCache.setter
    def FullUrlCache(self, FullUrlCache):
        self._FullUrlCache = FullUrlCache


    def _deserialize(self, params):
        self._FullUrlCache = params.get("FullUrlCache")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheRule(AbstractModel):
    """Caching configuration rule.

    """

    def __init__(self):
        r"""
        :param _CacheType: Cache type. Valid values: all (all files), file (extension type), directory (directory), path (full path), index (homepage).
        :type CacheType: str
        :param _CacheContents: Cached content list.
        :type CacheContents: list of str
        :param _CacheTime: Cache time in seconds.
        :type CacheTime: int
        """
        self._CacheType = None
        self._CacheContents = None
        self._CacheTime = None

    @property
    def CacheType(self):
        """Cache type. Valid values: all (all files), file (extension type), directory (directory), path (full path), index (homepage).
        :rtype: str
        """
        return self._CacheType

    @CacheType.setter
    def CacheType(self, CacheType):
        self._CacheType = CacheType

    @property
    def CacheContents(self):
        """Cached content list.
        :rtype: list of str
        """
        return self._CacheContents

    @CacheContents.setter
    def CacheContents(self, CacheContents):
        self._CacheContents = CacheContents

    @property
    def CacheTime(self):
        """Cache time in seconds.
        :rtype: int
        """
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
        


class ClientCert(AbstractModel):
    """HTTPS client certificate configuration.

    """

    def __init__(self):
        r"""
        :param _Certificate: Client certificate in PEM format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Certificate: str
        :param _CertName: Client certificate name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertName: str
        :param _ExpireTime: Certificate expiration time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _DeployTime: Certificate issuance time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeployTime: str
        """
        self._Certificate = None
        self._CertName = None
        self._ExpireTime = None
        self._DeployTime = None

    @property
    def Certificate(self):
        """Client certificate in PEM format.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def CertName(self):
        """Client certificate name.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def ExpireTime(self):
        """Certificate expiration time.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def DeployTime(self):
        """Certificate issuance time.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
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
        


class DeleteEcdnDomainRequest(AbstractModel):
    """DeleteEcdnDomain request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain name to be deleted.
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        """Domain name to be deleted.
        :rtype: str
        """
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
        


class DeleteEcdnDomainResponse(AbstractModel):
    """DeleteEcdnDomain response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeDomainsConfigRequest(AbstractModel):
    """DescribeDomainsConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Pagination offset address. Default value: 0.
        :type Offset: int
        :param _Limit: Number of domain names per page. Default value: 100.
        :type Limit: int
        :param _Filters: Query filter.
        :type Filters: list of DomainFilter
        :param _Sort: Query result sorting rule.
        :type Sort: :class:`tencentcloud.ecdn.v20191012.models.Sort`
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._Sort = None

    @property
    def Offset(self):
        """Pagination offset address. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of domain names per page. Default value: 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """Query filter.
        :rtype: list of DomainFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Sort(self):
        """Query result sorting rule.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.Sort`
        """
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
        :param _Domains: Domain name list.
        :type Domains: list of DomainDetailInfo
        :param _TotalCount: Number of matched domain names. This is used for paginated query.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Domains = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Domains(self):
        """Domain name list.
        :rtype: list of DomainDetailInfo
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def TotalCount(self):
        """Number of matched domain names. This is used for paginated query.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self._Domains = []
            for item in params.get("Domains"):
                obj = DomainDetailInfo()
                obj._deserialize(item)
                self._Domains.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDomainsRequest(AbstractModel):
    """DescribeDomains request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Pagination offset address. Default value: 0.
        :type Offset: int
        :param _Limit: Number of domain names per page. Default value: 100. Maximum value: 1000.
        :type Limit: int
        :param _Filters: Query filter.
        :type Filters: list of DomainFilter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        """Pagination offset address. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of domain names per page. Default value: 100. Maximum value: 1000.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """Query filter.
        :rtype: list of DomainFilter
        """
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
        :param _Domains: Domain name information list.
        :type Domains: list of DomainBriefInfo
        :param _TotalCount: Total number of domain names.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Domains = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Domains(self):
        """Domain name information list.
        :rtype: list of DomainBriefInfo
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def TotalCount(self):
        """Total number of domain names.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self._Domains = []
            for item in params.get("Domains"):
                obj = DomainBriefInfo()
                obj._deserialize(item)
                self._Domains.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeEcdnDomainLogsRequest(AbstractModel):
    """DescribeEcdnDomainLogs request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain name to be queried.
        :type Domain: str
        :param _StartTime: Log start time, such as 2019-10-01 00:00:00
        :type StartTime: str
        :param _EndTime: Log end time, such as 2019-10-02 00:00:00. Only logs for the last 30 days can be queried.
        :type EndTime: str
        :param _Offset: Pagination offset for log link list. Default value: 0.
        :type Offset: int
        :param _Limit: Number of log links per page. Default value: 100. Maximum value: 1000.
        :type Limit: int
        """
        self._Domain = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def Domain(self):
        """Domain name to be queried.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def StartTime(self):
        """Log start time, such as 2019-10-01 00:00:00
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Log end time, such as 2019-10-02 00:00:00. Only logs for the last 30 days can be queried.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        """Pagination offset for log link list. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of log links per page. Default value: 100. Maximum value: 1000.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEcdnDomainLogsResponse(AbstractModel):
    """DescribeEcdnDomainLogs response structure.

    """

    def __init__(self):
        r"""
        :param _DomainLogs: Log link list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DomainLogs: list of DomainLogs
        :param _TotalCount: Total number of log links.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DomainLogs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DomainLogs(self):
        """Log link list.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of DomainLogs
        """
        return self._DomainLogs

    @DomainLogs.setter
    def DomainLogs(self, DomainLogs):
        self._DomainLogs = DomainLogs

    @property
    def TotalCount(self):
        """Total number of log links.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DomainLogs") is not None:
            self._DomainLogs = []
            for item in params.get("DomainLogs"):
                obj = DomainLogs()
                obj._deserialize(item)
                self._DomainLogs.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeEcdnDomainStatisticsRequest(AbstractModel):
    """DescribeEcdnDomainStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Query start time, such as 2019-12-13 00:00:00.
The time span cannot exceed 90 days.
        :type StartTime: str
        :param _EndTime: Query end time, such as 2019-12-13 23:59:59.
The time span cannot exceed 90 days.
        :type EndTime: str
        :param _Metrics: Statistical metric names:
flux: traffic (in bytes)
bandwidth: bandwidth (in bps)
request: number of requests
        :type Metrics: list of str
        :param _Domains: Specifies the list of domain names to be queried
        :type Domains: list of str
        :param _Projects: Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)
If no domain name is entered, the specified project will be queried; otherwise, the domain name will prevail
        :type Projects: list of int
        :param _Offset: Pagination offset. Default value: 0.
        :type Offset: int
        :param _Limit: Number of entries per page. Default value: 1000. Maximum value: 3,000.
        :type Limit: int
        :param _Area: Statistical areas:
mainland: Chinese mainland
oversea: outside the Chinese mainland
global: global
Default value: global
        :type Area: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Metrics = None
        self._Domains = None
        self._Projects = None
        self._Offset = None
        self._Limit = None
        self._Area = None

    @property
    def StartTime(self):
        """Query start time, such as 2019-12-13 00:00:00.
The time span cannot exceed 90 days.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Query end time, such as 2019-12-13 23:59:59.
The time span cannot exceed 90 days.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Metrics(self):
        """Statistical metric names:
flux: traffic (in bytes)
bandwidth: bandwidth (in bps)
request: number of requests
        :rtype: list of str
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def Domains(self):
        """Specifies the list of domain names to be queried
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Projects(self):
        """Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)
If no domain name is entered, the specified project will be queried; otherwise, the domain name will prevail
        :rtype: list of int
        """
        return self._Projects

    @Projects.setter
    def Projects(self, Projects):
        self._Projects = Projects

    @property
    def Offset(self):
        """Pagination offset. Default value: 0.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of entries per page. Default value: 1000. Maximum value: 3,000.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Area(self):
        """Statistical areas:
mainland: Chinese mainland
oversea: outside the Chinese mainland
global: global
Default value: global
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Metrics = params.get("Metrics")
        self._Domains = params.get("Domains")
        self._Projects = params.get("Projects")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEcdnDomainStatisticsResponse(AbstractModel):
    """DescribeEcdnDomainStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Domain name data
        :type Data: list of DomainData
        :param _TotalCount: Quantity
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Data(self):
        """Domain name data
        :rtype: list of DomainData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        """Quantity
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DomainData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeEcdnStatisticsRequest(AbstractModel):
    """DescribeEcdnStatistics request structure.

    """

    def __init__(self):
        r"""
        :param _StartTime: Query start time, such as 2019-12-13 00:00:00
        :type StartTime: str
        :param _EndTime: Query end time, such as 2019-12-13 23:59:59
        :type EndTime: str
        :param _Metrics: Specifies the query metric, which can be:
flux: traffic (in bytes)
bandwidth: bandwidth (in bps)
request: number of requests
2xx: returns the number of 2xx status codes or details of status codes starting with 2
3xx: returns the number of 3xx status codes or details of status codes starting with 3
4xx: returns the number of 4xx status codes or details of status codes starting with 4
5xx: returns the number of 5xx status codes or details of status codes starting with 5
        :type Metrics: list of str
        :param _Interval: Sampling interval in minutes. The available options vary for different query period. See below: 
1 day: `1`, `5`, `15`, `30`, `60`, `120`, `240`, `1440` 
2 to 3 days: `15`, `30`, `60`, `120`, `240`, `1440`
4 to 7 days: `30`, `60`, `120`, `240`, `1440`
8 to 31 days: `60`, `120`, `240`, `1440`
        :type Interval: int
        :param _Domains: Specifies the list of domain names to be queried

Up to 30 acceleration domain names can be queried at a time.
        :type Domains: list of str
        :param _Projects: Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)
If no domain name is entered, the specified project will be queried; otherwise, the domain name will prevail
        :type Projects: list of int
        :param _Area: Statistical areas:
mainland: Chinese mainland
oversea: outside the Chinese mainland
global: global
Default value: global
        :type Area: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Metrics = None
        self._Interval = None
        self._Domains = None
        self._Projects = None
        self._Area = None

    @property
    def StartTime(self):
        """Query start time, such as 2019-12-13 00:00:00
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Query end time, such as 2019-12-13 23:59:59
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Metrics(self):
        """Specifies the query metric, which can be:
flux: traffic (in bytes)
bandwidth: bandwidth (in bps)
request: number of requests
2xx: returns the number of 2xx status codes or details of status codes starting with 2
3xx: returns the number of 3xx status codes or details of status codes starting with 3
4xx: returns the number of 4xx status codes or details of status codes starting with 4
5xx: returns the number of 5xx status codes or details of status codes starting with 5
        :rtype: list of str
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def Interval(self):
        """Sampling interval in minutes. The available options vary for different query period. See below: 
1 day: `1`, `5`, `15`, `30`, `60`, `120`, `240`, `1440` 
2 to 3 days: `15`, `30`, `60`, `120`, `240`, `1440`
4 to 7 days: `30`, `60`, `120`, `240`, `1440`
8 to 31 days: `60`, `120`, `240`, `1440`
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Domains(self):
        """Specifies the list of domain names to be queried

Up to 30 acceleration domain names can be queried at a time.
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Projects(self):
        """Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)
If no domain name is entered, the specified project will be queried; otherwise, the domain name will prevail
        :rtype: list of int
        """
        return self._Projects

    @Projects.setter
    def Projects(self, Projects):
        self._Projects = Projects

    @property
    def Area(self):
        """Statistical areas:
mainland: Chinese mainland
oversea: outside the Chinese mainland
global: global
Default value: global
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Metrics = params.get("Metrics")
        self._Interval = params.get("Interval")
        self._Domains = params.get("Domains")
        self._Projects = params.get("Projects")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEcdnStatisticsResponse(AbstractModel):
    """DescribeEcdnStatistics response structure.

    """

    def __init__(self):
        r"""
        :param _Data: Returned data details of the specified conditional query
        :type Data: list of ResourceData
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """Returned data details of the specified conditional query
        :rtype: list of ResourceData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ResourceData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIpStatusRequest(AbstractModel):
    """DescribeIpStatus request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Acceleration domain name
        :type Domain: str
        :param _Area: Target region of the query:
mainland: nodes in Mainland China
overseas: nodes outside Mainland China
global: global nodes
        :type Area: str
        """
        self._Domain = None
        self._Area = None

    @property
    def Domain(self):
        """Acceleration domain name
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Area(self):
        """Target region of the query:
mainland: nodes in Mainland China
overseas: nodes outside Mainland China
global: global nodes
        :rtype: str
        """
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
        """Node list
        :rtype: list of IpStatus
        """
        return self._Ips

    @Ips.setter
    def Ips(self, Ips):
        self._Ips = Ips

    @property
    def TotalCount(self):
        """Total number of nodes
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
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


class DescribePurgeQuotaRequest(AbstractModel):
    """DescribePurgeQuota request structure.

    """


class DescribePurgeQuotaResponse(AbstractModel):
    """DescribePurgeQuota response structure.

    """

    def __init__(self):
        r"""
        :param _UrlPurge: URL purge usage and quota.
        :type UrlPurge: :class:`tencentcloud.ecdn.v20191012.models.Quota`
        :param _PathPurge: Directory purge usage and quota.
        :type PathPurge: :class:`tencentcloud.ecdn.v20191012.models.Quota`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._UrlPurge = None
        self._PathPurge = None
        self._RequestId = None

    @property
    def UrlPurge(self):
        """URL purge usage and quota.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.Quota`
        """
        return self._UrlPurge

    @UrlPurge.setter
    def UrlPurge(self, UrlPurge):
        self._UrlPurge = UrlPurge

    @property
    def PathPurge(self):
        """Directory purge usage and quota.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.Quota`
        """
        return self._PathPurge

    @PathPurge.setter
    def PathPurge(self, PathPurge):
        self._PathPurge = PathPurge

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UrlPurge") is not None:
            self._UrlPurge = Quota()
            self._UrlPurge._deserialize(params.get("UrlPurge"))
        if params.get("PathPurge") is not None:
            self._PathPurge = Quota()
            self._PathPurge._deserialize(params.get("PathPurge"))
        self._RequestId = params.get("RequestId")


class DescribePurgeTasksRequest(AbstractModel):
    """DescribePurgeTasks request structure.

    """

    def __init__(self):
        r"""
        :param _PurgeType: Purge type to be queried. url: query URL purge records; path: query directory purge records.
        :type PurgeType: str
        :param _StartTime: Start time, such as 2018-08-08 00:00:00
        :type StartTime: str
        :param _EndTime: End time, such as 2018-08-08 23:59:59
        :type EndTime: str
        :param _TaskId: Task ID returned during submission. Either `TaskId` or start time must be specified for a query.
        :type TaskId: str
        :param _Offset: Pagination offset. Default value: 0 (starting from entry 0).
        :type Offset: int
        :param _Limit: Pagination limit. Default value: 20.
        :type Limit: int
        :param _Keyword: Query keyword. Please enter a domain name or full URL beginning with `http(s)://`.
        :type Keyword: str
        :param _Status: Specified task status to be queried. fail: failed, done: succeeded, process: purging.
        :type Status: str
        """
        self._PurgeType = None
        self._StartTime = None
        self._EndTime = None
        self._TaskId = None
        self._Offset = None
        self._Limit = None
        self._Keyword = None
        self._Status = None

    @property
    def PurgeType(self):
        """Purge type to be queried. url: query URL purge records; path: query directory purge records.
        :rtype: str
        """
        return self._PurgeType

    @PurgeType.setter
    def PurgeType(self, PurgeType):
        self._PurgeType = PurgeType

    @property
    def StartTime(self):
        """Start time, such as 2018-08-08 00:00:00
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """End time, such as 2018-08-08 23:59:59
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TaskId(self):
        """Task ID returned during submission. Either `TaskId` or start time must be specified for a query.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Offset(self):
        """Pagination offset. Default value: 0 (starting from entry 0).
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Pagination limit. Default value: 20.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Keyword(self):
        """Query keyword. Please enter a domain name or full URL beginning with `http(s)://`.
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Status(self):
        """Specified task status to be queried. fail: failed, done: succeeded, process: purging.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._PurgeType = params.get("PurgeType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TaskId = params.get("TaskId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Keyword = params.get("Keyword")
        self._Status = params.get("Status")
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
        :param _PurgeLogs: Purge history.
        :type PurgeLogs: list of PurgeTask
        :param _TotalCount: Total number of tasks, which is used for pagination.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._PurgeLogs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def PurgeLogs(self):
        """Purge history.
        :rtype: list of PurgeTask
        """
        return self._PurgeLogs

    @PurgeLogs.setter
    def PurgeLogs(self, PurgeLogs):
        self._PurgeLogs = PurgeLogs

    @property
    def TotalCount(self):
        """Total number of tasks, which is used for pagination.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
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


class DetailData(AbstractModel):
    """Data structure of sorted data

    """

    def __init__(self):
        r"""
        :param _Name: Data type name
        :type Name: str
        :param _Value: Data value
        :type Value: float
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        """Data type name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """Data value
        :rtype: float
        """
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
        


class DomainBriefInfo(AbstractModel):
    """Basic information of a CDN domain name.

    """

    def __init__(self):
        r"""
        :param _ResourceId: Domain name ID.
        :type ResourceId: str
        :param _AppId: Tencent Cloud account ID.
        :type AppId: int
        :param _Domain: CDN acceleration domain name.
        :type Domain: str
        :param _Cname: Domain name CNAME.
        :type Cname: str
        :param _Status: Domain name status. Valid values: pending (reviewing), rejected (rejected), processing (deploying after approval), online (enabled), offline (disabled), deleted (deleted).
        :type Status: str
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _CreateTime: Domain name creation time.
        :type CreateTime: str
        :param _UpdateTime: Domain name update time.
        :type UpdateTime: str
        :param _Origin: Origin server configuration details.
        :type Origin: :class:`tencentcloud.ecdn.v20191012.models.Origin`
        :param _Disable: Domain name blockage status. Valid values: normal (normal), overdue (service is suspended due to arrears), quota (trial traffic package is used up), malicious (malicious user), ddos (DDoS attack), idle (no traffic), unlicensed (no ICP filing), capping (bandwidth cap reached), readonly (read-only)
        :type Disable: str
        :param _Area: Acceleration region. Valid values: mainland, oversea, global.
        :type Area: str
        :param _Readonly: Domain name lock status. normal: not locked; global: globally locked
        :type Readonly: str
        :param _Tag: Domain name tag
Note: This field may return `null`, indicating that no valid value can be found.
        :type Tag: list of Tag
        """
        self._ResourceId = None
        self._AppId = None
        self._Domain = None
        self._Cname = None
        self._Status = None
        self._ProjectId = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Origin = None
        self._Disable = None
        self._Area = None
        self._Readonly = None
        self._Tag = None

    @property
    def ResourceId(self):
        """Domain name ID.
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def AppId(self):
        """Tencent Cloud account ID.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Domain(self):
        """CDN acceleration domain name.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Cname(self):
        """Domain name CNAME.
        :rtype: str
        """
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def Status(self):
        """Domain name status. Valid values: pending (reviewing), rejected (rejected), processing (deploying after approval), online (enabled), offline (disabled), deleted (deleted).
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ProjectId(self):
        """Project ID.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        """Domain name creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """Domain name update time.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Origin(self):
        """Origin server configuration details.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.Origin`
        """
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def Disable(self):
        """Domain name blockage status. Valid values: normal (normal), overdue (service is suspended due to arrears), quota (trial traffic package is used up), malicious (malicious user), ddos (DDoS attack), idle (no traffic), unlicensed (no ICP filing), capping (bandwidth cap reached), readonly (read-only)
        :rtype: str
        """
        return self._Disable

    @Disable.setter
    def Disable(self, Disable):
        self._Disable = Disable

    @property
    def Area(self):
        """Acceleration region. Valid values: mainland, oversea, global.
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Readonly(self):
        """Domain name lock status. normal: not locked; global: globally locked
        :rtype: str
        """
        return self._Readonly

    @Readonly.setter
    def Readonly(self, Readonly):
        self._Readonly = Readonly

    @property
    def Tag(self):
        """Domain name tag
Note: This field may return `null`, indicating that no valid value can be found.
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._AppId = params.get("AppId")
        self._Domain = params.get("Domain")
        self._Cname = params.get("Cname")
        self._Status = params.get("Status")
        self._ProjectId = params.get("ProjectId")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        self._Disable = params.get("Disable")
        self._Area = params.get("Area")
        self._Readonly = params.get("Readonly")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainData(AbstractModel):
    """Data structure of sorted data

    """

    def __init__(self):
        r"""
        :param _Resource: Domain name
        :type Resource: str
        :param _DetailData: Result details.
        :type DetailData: list of DetailData
        """
        self._Resource = None
        self._DetailData = None

    @property
    def Resource(self):
        """Domain name
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def DetailData(self):
        """Result details.
        :rtype: list of DetailData
        """
        return self._DetailData

    @DetailData.setter
    def DetailData(self, DetailData):
        self._DetailData = DetailData


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        if params.get("DetailData") is not None:
            self._DetailData = []
            for item in params.get("DetailData"):
                obj = DetailData()
                obj._deserialize(item)
                self._DetailData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainDetailInfo(AbstractModel):
    """Detailed configuration information of ECDN domain name.

    """

    def __init__(self):
        r"""
        :param _ResourceId: Domain name ID.
        :type ResourceId: str
        :param _AppId: Tencent Cloud account ID.
        :type AppId: int
        :param _Domain: Acceleration domain name.
        :type Domain: str
        :param _Cname: Domain name CNAME.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Cname: str
        :param _Status: Domain name status. Valid values: pending (reviewing), rejected (rejected), processing (deploying after approval), online (enabled), offline (disabled), deleted (deleted).
        :type Status: str
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _CreateTime: Domain name creation time.
        :type CreateTime: str
        :param _UpdateTime: Domain name update time.
        :type UpdateTime: str
        :param _Origin: Origin server configuration.
        :type Origin: :class:`tencentcloud.ecdn.v20191012.models.Origin`
        :param _IpFilter: IP blocklist/allowlist configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpFilter: :class:`tencentcloud.ecdn.v20191012.models.IpFilter`
        :param _IpFreqLimit: IP access limit configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpFreqLimit: :class:`tencentcloud.ecdn.v20191012.models.IpFreqLimit`
        :param _ResponseHeader: Origin server response header configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseHeader: :class:`tencentcloud.ecdn.v20191012.models.ResponseHeader`
        :param _CacheKey: Node caching configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CacheKey: :class:`tencentcloud.ecdn.v20191012.models.CacheKey`
        :param _Cache: Caching rule configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Cache: :class:`tencentcloud.ecdn.v20191012.models.Cache`
        :param _Https: HTTPS configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Https: :class:`tencentcloud.ecdn.v20191012.models.Https`
        :param _Disable: Domain name blockage status. Valid values: normal (normal), overdue (service is suspended due to arrears), quota (trial traffic package is used up), malicious (malicious user), ddos (DDoS attack), idle (no traffic), unlicensed (no ICP filing), capping (bandwidth cap reached), readonly (read-only).
Note: this field may return null, indicating that no valid values can be obtained.
        :type Disable: str
        :param _ForceRedirect: Forced access protocol redirection configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ForceRedirect: :class:`tencentcloud.ecdn.v20191012.models.ForceRedirect`
        :param _Area: Acceleration region. Valid values: mainland, overseas, global.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Area: str
        :param _Readonly: Domain name lock status. normal: not locked; global: globally locked.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Readonly: str
        :param _Tag: Domain name tag
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Tag: list of Tag
        :param _WebSocket: WebSocket configuration.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type WebSocket: :class:`tencentcloud.ecdn.v20191012.models.WebSocket`
        """
        self._ResourceId = None
        self._AppId = None
        self._Domain = None
        self._Cname = None
        self._Status = None
        self._ProjectId = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Origin = None
        self._IpFilter = None
        self._IpFreqLimit = None
        self._ResponseHeader = None
        self._CacheKey = None
        self._Cache = None
        self._Https = None
        self._Disable = None
        self._ForceRedirect = None
        self._Area = None
        self._Readonly = None
        self._Tag = None
        self._WebSocket = None

    @property
    def ResourceId(self):
        """Domain name ID.
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def AppId(self):
        """Tencent Cloud account ID.
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Domain(self):
        """Acceleration domain name.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Cname(self):
        """Domain name CNAME.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def Status(self):
        """Domain name status. Valid values: pending (reviewing), rejected (rejected), processing (deploying after approval), online (enabled), offline (disabled), deleted (deleted).
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ProjectId(self):
        """Project ID.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        """Domain name creation time.
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """Domain name update time.
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Origin(self):
        """Origin server configuration.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.Origin`
        """
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def IpFilter(self):
        """IP blocklist/allowlist configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.IpFilter`
        """
        return self._IpFilter

    @IpFilter.setter
    def IpFilter(self, IpFilter):
        self._IpFilter = IpFilter

    @property
    def IpFreqLimit(self):
        """IP access limit configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.IpFreqLimit`
        """
        return self._IpFreqLimit

    @IpFreqLimit.setter
    def IpFreqLimit(self, IpFreqLimit):
        self._IpFreqLimit = IpFreqLimit

    @property
    def ResponseHeader(self):
        """Origin server response header configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.ResponseHeader`
        """
        return self._ResponseHeader

    @ResponseHeader.setter
    def ResponseHeader(self, ResponseHeader):
        self._ResponseHeader = ResponseHeader

    @property
    def CacheKey(self):
        """Node caching configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.CacheKey`
        """
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def Cache(self):
        """Caching rule configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.Cache`
        """
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def Https(self):
        """HTTPS configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.Https`
        """
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def Disable(self):
        """Domain name blockage status. Valid values: normal (normal), overdue (service is suspended due to arrears), quota (trial traffic package is used up), malicious (malicious user), ddos (DDoS attack), idle (no traffic), unlicensed (no ICP filing), capping (bandwidth cap reached), readonly (read-only).
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Disable

    @Disable.setter
    def Disable(self, Disable):
        self._Disable = Disable

    @property
    def ForceRedirect(self):
        """Forced access protocol redirection configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.ForceRedirect`
        """
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def Area(self):
        """Acceleration region. Valid values: mainland, overseas, global.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Readonly(self):
        """Domain name lock status. normal: not locked; global: globally locked.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Readonly

    @Readonly.setter
    def Readonly(self, Readonly):
        self._Readonly = Readonly

    @property
    def Tag(self):
        """Domain name tag
Note: This field may return `null`, indicating that no valid value can be obtained.
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def WebSocket(self):
        """WebSocket configuration.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.WebSocket`
        """
        return self._WebSocket

    @WebSocket.setter
    def WebSocket(self, WebSocket):
        self._WebSocket = WebSocket


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._AppId = params.get("AppId")
        self._Domain = params.get("Domain")
        self._Cname = params.get("Cname")
        self._Status = params.get("Status")
        self._ProjectId = params.get("ProjectId")
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
        if params.get("ResponseHeader") is not None:
            self._ResponseHeader = ResponseHeader()
            self._ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Cache") is not None:
            self._Cache = Cache()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        self._Disable = params.get("Disable")
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirect()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        self._Area = params.get("Area")
        self._Readonly = params.get("Readonly")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        if params.get("WebSocket") is not None:
            self._WebSocket = WebSocket()
            self._WebSocket._deserialize(params.get("WebSocket"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainFilter(AbstractModel):
    """Filter for domain name query.

    """

    def __init__(self):
        r"""
        :param _Name: Filters by the field name, which includes:
- `origin`: Primary origin server.
- `domain`: Domain name.
- `resourceId`: Domain name ID.
- `status`: Domain name status. Valid values: `online`, `offline`, and `processing`.
- `disable`: Whether the domain name is blocked. Valid values: `normal`, `unlicensed`.
- `projectId`: Project ID.
- `fullUrlCache`: Whether to enable full-path cache, which can be `on` or `off`.
- `https`: Whether to configure HTTPS, which can be `on`, `off` or `processing`.
- `originPullProtocol`: Origin-pull protocol type, which can be `http`, `follow`, or `https`.
- `area`: Acceleration region, which can be `mainland`，`overseas` or `global`.
- `tagKey`: Tag key.
        :type Name: str
        :param _Value: Filter field value.
        :type Value: list of str
        :param _Fuzzy: Whether to enable fuzzy query, which is supported only for filter fields `origin` and `domain`.
        :type Fuzzy: bool
        """
        self._Name = None
        self._Value = None
        self._Fuzzy = None

    @property
    def Name(self):
        """Filters by the field name, which includes:
- `origin`: Primary origin server.
- `domain`: Domain name.
- `resourceId`: Domain name ID.
- `status`: Domain name status. Valid values: `online`, `offline`, and `processing`.
- `disable`: Whether the domain name is blocked. Valid values: `normal`, `unlicensed`.
- `projectId`: Project ID.
- `fullUrlCache`: Whether to enable full-path cache, which can be `on` or `off`.
- `https`: Whether to configure HTTPS, which can be `on`, `off` or `processing`.
- `originPullProtocol`: Origin-pull protocol type, which can be `http`, `follow`, or `https`.
- `area`: Acceleration region, which can be `mainland`，`overseas` or `global`.
- `tagKey`: Tag key.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """Filter field value.
        :rtype: list of str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Fuzzy(self):
        """Whether to enable fuzzy query, which is supported only for filter fields `origin` and `domain`.
        :rtype: bool
        """
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
        


class DomainLogs(AbstractModel):
    """Domain name log information.

    """

    def __init__(self):
        r"""
        :param _StartTime: Log start time.
        :type StartTime: str
        :param _EndTime: Log end time.
        :type EndTime: str
        :param _LogPath: Log download path.
        :type LogPath: str
        """
        self._StartTime = None
        self._EndTime = None
        self._LogPath = None

    @property
    def StartTime(self):
        """Log start time.
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """Log end time.
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def LogPath(self):
        """Log download path.
        :rtype: str
        """
        return self._LogPath

    @LogPath.setter
    def LogPath(self, LogPath):
        self._LogPath = LogPath


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._LogPath = params.get("LogPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EcdnData(AbstractModel):
    """Detailed access data type

    """

    def __init__(self):
        r"""
        :param _Metrics: Queries the specified metric. Valid values: Bandwidth, Flux, Request, Delay, status code, LogBandwidth, LogFlux, LogRequest
        :type Metrics: list of str
        :param _DetailData: Detailed data collection
        :type DetailData: list of TimestampData
        """
        self._Metrics = None
        self._DetailData = None

    @property
    def Metrics(self):
        """Queries the specified metric. Valid values: Bandwidth, Flux, Request, Delay, status code, LogBandwidth, LogFlux, LogRequest
        :rtype: list of str
        """
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def DetailData(self):
        """Detailed data collection
        :rtype: list of TimestampData
        """
        return self._DetailData

    @DetailData.setter
    def DetailData(self, DetailData):
        self._DetailData = DetailData


    def _deserialize(self, params):
        self._Metrics = params.get("Metrics")
        if params.get("DetailData") is not None:
            self._DetailData = []
            for item in params.get("DetailData"):
                obj = TimestampData()
                obj._deserialize(item)
                self._DetailData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForceRedirect(AbstractModel):
    """Forced access protocol redirection configuration.

    """

    def __init__(self):
        r"""
        :param _Switch: Forced access protocol redirection configuration switch. Valid values: on, off.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param _RedirectType: Access protocol type for forced redirection. Valid values: http (forced redirection to HTTP protocol), https (forced redirection to HTTPS protocol).
Note: this field may return null, indicating that no valid values can be obtained.
        :type RedirectType: str
        :param _RedirectStatusCode: HTTP status code returned when forced redirection is enabled. Valid values: 301, 302.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RedirectStatusCode: int
        """
        self._Switch = None
        self._RedirectType = None
        self._RedirectStatusCode = None

    @property
    def Switch(self):
        """Forced access protocol redirection configuration switch. Valid values: on, off.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RedirectType(self):
        """Access protocol type for forced redirection. Valid values: http (forced redirection to HTTP protocol), https (forced redirection to HTTPS protocol).
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RedirectType

    @RedirectType.setter
    def RedirectType(self, RedirectType):
        self._RedirectType = RedirectType

    @property
    def RedirectStatusCode(self):
        """HTTP status code returned when forced redirection is enabled. Valid values: 301, 302.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._RedirectStatusCode

    @RedirectStatusCode.setter
    def RedirectStatusCode(self, RedirectStatusCode):
        self._RedirectStatusCode = RedirectStatusCode


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._RedirectType = params.get("RedirectType")
        self._RedirectStatusCode = params.get("RedirectStatusCode")
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
        :param _Switch: Whether to enable. Valid values: on, off.
        :type Switch: str
        :param _MaxAge: `MaxAge` value.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxAge: int
        :param _IncludeSubDomains: Whether to include subdomain names. Valid values: on, off.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IncludeSubDomains: str
        """
        self._Switch = None
        self._MaxAge = None
        self._IncludeSubDomains = None

    @property
    def Switch(self):
        """Whether to enable. Valid values: on, off.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def MaxAge(self):
        """`MaxAge` value.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def IncludeSubDomains(self):
        """Whether to include subdomain names. Valid values: on, off.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
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
    """Path-specific HTTP header setting rule.

    """

    def __init__(self):
        r"""
        :param _HeaderMode: HTTP header setting method. Valid values: add (add header), set (set header), del (delete header).
Request header currently does not support `set`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type HeaderMode: str
        :param _HeaderName: HTTP header name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type HeaderName: str
        :param _HeaderValue: HTTP header value, which is optional when it is `del`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type HeaderValue: str
        :param _RuleType: Type of effective URL path rule. Valid values: all (all paths), file (file extension), directory (directory), path (absolute path).
Note: this field may return null, indicating that no valid values can be obtained.
        :type RuleType: str
        :param _RulePaths: URL path or file type list
Note: this field may return null, indicating that no valid values can be obtained.
        :type RulePaths: list of str
        """
        self._HeaderMode = None
        self._HeaderName = None
        self._HeaderValue = None
        self._RuleType = None
        self._RulePaths = None

    @property
    def HeaderMode(self):
        """HTTP header setting method. Valid values: add (add header), set (set header), del (delete header).
Request header currently does not support `set`.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HeaderMode

    @HeaderMode.setter
    def HeaderMode(self, HeaderMode):
        self._HeaderMode = HeaderMode

    @property
    def HeaderName(self):
        """HTTP header name.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HeaderName

    @HeaderName.setter
    def HeaderName(self, HeaderName):
        self._HeaderName = HeaderName

    @property
    def HeaderValue(self):
        """HTTP header value, which is optional when it is `del`.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._HeaderValue

    @HeaderValue.setter
    def HeaderValue(self, HeaderValue):
        self._HeaderValue = HeaderValue

    @property
    def RuleType(self):
        """Type of effective URL path rule. Valid values: all (all paths), file (file extension), directory (directory), path (absolute path).
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RulePaths(self):
        """URL path or file type list
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
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
        


class Https(AbstractModel):
    """HTTPS configuration of domain name.

    """

    def __init__(self):
        r"""
        :param _Switch: HTTPS configuration switch. Valid values: on, off. If the domain name with HTTPS configuration enabled is being deployed, this switch will be `off`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param _Http2: Whether to enable HTTP2. Valid values: on, off.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Http2: str
        :param _OcspStapling: Whether to enable the OCSP feature. Valid values: on, off.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OcspStapling: str
        :param _VerifyClient: Whether to enable the client certificate verification feature. Valid values: on, off. The client certificate information must be uploaded if this feature is enabled.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VerifyClient: str
        :param _CertInfo: Server certificate configuration information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertInfo: :class:`tencentcloud.ecdn.v20191012.models.ServerCert`
        :param _ClientCertInfo: Client certificate configuration information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClientCertInfo: :class:`tencentcloud.ecdn.v20191012.models.ClientCert`
        :param _Spdy: Whether to enable SPDY. Valid values: on, off.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Spdy: str
        :param _SslStatus: HTTPS certificate deployment status. Valid values: closed (disabled), deploying (deploying), deployed (deployment succeeded), failed (deployment failed). This parameter cannot be used as an input parameter.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SslStatus: str
        :param _Hsts: HSTS configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type Hsts: :class:`tencentcloud.ecdn.v20191012.models.Hsts`
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

    @property
    def Switch(self):
        """HTTPS configuration switch. Valid values: on, off. If the domain name with HTTPS configuration enabled is being deployed, this switch will be `off`.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Http2(self):
        """Whether to enable HTTP2. Valid values: on, off.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Http2

    @Http2.setter
    def Http2(self, Http2):
        self._Http2 = Http2

    @property
    def OcspStapling(self):
        """Whether to enable the OCSP feature. Valid values: on, off.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OcspStapling

    @OcspStapling.setter
    def OcspStapling(self, OcspStapling):
        self._OcspStapling = OcspStapling

    @property
    def VerifyClient(self):
        """Whether to enable the client certificate verification feature. Valid values: on, off. The client certificate information must be uploaded if this feature is enabled.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._VerifyClient

    @VerifyClient.setter
    def VerifyClient(self, VerifyClient):
        self._VerifyClient = VerifyClient

    @property
    def CertInfo(self):
        """Server certificate configuration information.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.ServerCert`
        """
        return self._CertInfo

    @CertInfo.setter
    def CertInfo(self, CertInfo):
        self._CertInfo = CertInfo

    @property
    def ClientCertInfo(self):
        """Client certificate configuration information.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.ClientCert`
        """
        return self._ClientCertInfo

    @ClientCertInfo.setter
    def ClientCertInfo(self, ClientCertInfo):
        self._ClientCertInfo = ClientCertInfo

    @property
    def Spdy(self):
        """Whether to enable SPDY. Valid values: on, off.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Spdy

    @Spdy.setter
    def Spdy(self, Spdy):
        self._Spdy = Spdy

    @property
    def SslStatus(self):
        """HTTPS certificate deployment status. Valid values: closed (disabled), deploying (deploying), deployed (deployment succeeded), failed (deployment failed). This parameter cannot be used as an input parameter.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SslStatus

    @SslStatus.setter
    def SslStatus(self, SslStatus):
        self._SslStatus = SslStatus

    @property
    def Hsts(self):
        """HSTS configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.Hsts`
        """
        return self._Hsts

    @Hsts.setter
    def Hsts(self, Hsts):
        self._Hsts = Hsts


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpFilter(AbstractModel):
    """IP blocklist/allowlist.

    """

    def __init__(self):
        r"""
        :param _Switch: IP blocklist/allowlist switch. Valid values: on, off.
        :type Switch: str
        :param _FilterType: IP blocklist/allowlist type. Valid values: whitelist, blacklist.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FilterType: str
        :param _Filters: IP blocklist/allowlist list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Filters: list of str
        """
        self._Switch = None
        self._FilterType = None
        self._Filters = None

    @property
    def Switch(self):
        """IP blocklist/allowlist switch. Valid values: on, off.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def FilterType(self):
        """IP blocklist/allowlist type. Valid values: whitelist, blacklist.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def Filters(self):
        """IP blocklist/allowlist list.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of str
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._FilterType = params.get("FilterType")
        self._Filters = params.get("Filters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpFreqLimit(AbstractModel):
    """IP access limit configuration.

    """

    def __init__(self):
        r"""
        :param _Switch: IP access limit switch. Valid values: on, off.
        :type Switch: str
        :param _Qps: Number of requests per second.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Qps: int
        """
        self._Switch = None
        self._Qps = None

    @property
    def Switch(self):
        """IP access limit switch. Valid values: on, off.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Qps(self):
        """Number of requests per second.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: int
        """
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
        :param _District: Node region
        :type District: str
        :param _Isp: Node ISP
        :type Isp: str
        :param _City: Node city
        :type City: str
        :param _Status: Node status
online: the node is online and scheduling normally
offline: the node is offline
        :type Status: str
        :param _CreateTime: Node IP creation time
        :type CreateTime: str
        """
        self._Ip = None
        self._District = None
        self._Isp = None
        self._City = None
        self._Status = None
        self._CreateTime = None

    @property
    def Ip(self):
        """Node IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def District(self):
        """Node region
        :rtype: str
        """
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def Isp(self):
        """Node ISP
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def City(self):
        """Node city
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Status(self):
        """Node status
online: the node is online and scheduling normally
offline: the node is offline
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """Node IP creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._District = params.get("District")
        self._Isp = params.get("Isp")
        self._City = params.get("City")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Origin(AbstractModel):
    """Origin server configuration.

    """

    def __init__(self):
        r"""
        :param _Origins: Primary origin server list. IP and the domain name of the origin server cannot be entered at the same time. Configure origin server port in the format of ["origin1:port1", "origin2:port2"]. Configure origin-pull weight in the format of ["origin1::weight1", "origin2::weight2"]. Configure both port and weight in the format of ["origin1:port1:weight1", "origin2:port2:weight2"]. Valid range of weight value: 0 - 100.
        :type Origins: list of str
        :param _OriginType: Primary origin server type. Valid values: domain (domain name origin server), ip (IP origin server).
This is required when setting `Origins`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginType: str
        :param _ServerName: Host header value during origin-pull.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServerName: str
        :param _OriginPullProtocol: Origin-pull protocol type. Valid values: http (forced HTTP origin-pull), follow (protocol follow), https (HTTPS origin-pull).
If this parameter is left empty, HTTP origin-pull will be used by default.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type OriginPullProtocol: str
        :param _BackupOrigins: Secondary origin server list.
        :type BackupOrigins: list of str
        :param _BackupOriginType: Secondary origin server type, which is the same as `OriginType`.
This is required when setting `BackupOrigins`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BackupOriginType: str
        :param _AdvanceHttps: HTTPS advanced origin-pull configuration
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AdvanceHttps: :class:`tencentcloud.ecdn.v20191012.models.AdvanceHttps`
        """
        self._Origins = None
        self._OriginType = None
        self._ServerName = None
        self._OriginPullProtocol = None
        self._BackupOrigins = None
        self._BackupOriginType = None
        self._AdvanceHttps = None

    @property
    def Origins(self):
        """Primary origin server list. IP and the domain name of the origin server cannot be entered at the same time. Configure origin server port in the format of ["origin1:port1", "origin2:port2"]. Configure origin-pull weight in the format of ["origin1::weight1", "origin2::weight2"]. Configure both port and weight in the format of ["origin1:port1:weight1", "origin2:port2:weight2"]. Valid range of weight value: 0 - 100.
        :rtype: list of str
        """
        return self._Origins

    @Origins.setter
    def Origins(self, Origins):
        self._Origins = Origins

    @property
    def OriginType(self):
        """Primary origin server type. Valid values: domain (domain name origin server), ip (IP origin server).
This is required when setting `Origins`.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

    @property
    def ServerName(self):
        """Host header value during origin-pull.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def OriginPullProtocol(self):
        """Origin-pull protocol type. Valid values: http (forced HTTP origin-pull), follow (protocol follow), https (HTTPS origin-pull).
If this parameter is left empty, HTTP origin-pull will be used by default.
Note: this field may return `null`, indicating that no valid value is obtained.
        :rtype: str
        """
        return self._OriginPullProtocol

    @OriginPullProtocol.setter
    def OriginPullProtocol(self, OriginPullProtocol):
        self._OriginPullProtocol = OriginPullProtocol

    @property
    def BackupOrigins(self):
        """Secondary origin server list.
        :rtype: list of str
        """
        return self._BackupOrigins

    @BackupOrigins.setter
    def BackupOrigins(self, BackupOrigins):
        self._BackupOrigins = BackupOrigins

    @property
    def BackupOriginType(self):
        """Secondary origin server type, which is the same as `OriginType`.
This is required when setting `BackupOrigins`.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._BackupOriginType

    @BackupOriginType.setter
    def BackupOriginType(self, BackupOriginType):
        self._BackupOriginType = BackupOriginType

    @property
    def AdvanceHttps(self):
        """HTTPS advanced origin-pull configuration
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.AdvanceHttps`
        """
        return self._AdvanceHttps

    @AdvanceHttps.setter
    def AdvanceHttps(self, AdvanceHttps):
        self._AdvanceHttps = AdvanceHttps


    def _deserialize(self, params):
        self._Origins = params.get("Origins")
        self._OriginType = params.get("OriginType")
        self._ServerName = params.get("ServerName")
        self._OriginPullProtocol = params.get("OriginPullProtocol")
        self._BackupOrigins = params.get("BackupOrigins")
        self._BackupOriginType = params.get("BackupOriginType")
        if params.get("AdvanceHttps") is not None:
            self._AdvanceHttps = AdvanceHttps()
            self._AdvanceHttps._deserialize(params.get("AdvanceHttps"))
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
        :param _Paths: List of directories to be purged. The protocol header must be included.
        :type Paths: list of str
        :param _FlushType: Purge type. flush: purges updated resources, delete: purges all resources.
        :type FlushType: str
        """
        self._Paths = None
        self._FlushType = None

    @property
    def Paths(self):
        """List of directories to be purged. The protocol header must be included.
        :rtype: list of str
        """
        return self._Paths

    @Paths.setter
    def Paths(self, Paths):
        self._Paths = Paths

    @property
    def FlushType(self):
        """Purge type. flush: purges updated resources, delete: purges all resources.
        :rtype: str
        """
        return self._FlushType

    @FlushType.setter
    def FlushType(self, FlushType):
        self._FlushType = FlushType


    def _deserialize(self, params):
        self._Paths = params.get("Paths")
        self._FlushType = params.get("FlushType")
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
        :param _TaskId: Purge task ID
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """Purge task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class PurgeTask(AbstractModel):
    """Purge task log details.

    """

    def __init__(self):
        r"""
        :param _TaskId: Purge task ID.
        :type TaskId: str
        :param _Url: Purged URL.
        :type Url: str
        :param _Status: Purge task status. fail: failed, done: succeeded, process: purging.
        :type Status: str
        :param _PurgeType: Purge type. url: URL purge; path: directory purge.
        :type PurgeType: str
        :param _FlushType: Resource purge method. flush: purges updated resources, delete: purges all resources.
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
        """Purge task ID.
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Url(self):
        """Purged URL.
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Status(self):
        """Purge task status. fail: failed, done: succeeded, process: purging.
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PurgeType(self):
        """Purge type. url: URL purge; path: directory purge.
        :rtype: str
        """
        return self._PurgeType

    @PurgeType.setter
    def PurgeType(self, PurgeType):
        self._PurgeType = PurgeType

    @property
    def FlushType(self):
        """Resource purge method. flush: purges updated resources, delete: purges all resources.
        :rtype: str
        """
        return self._FlushType

    @FlushType.setter
    def FlushType(self, FlushType):
        self._FlushType = FlushType

    @property
    def CreateTime(self):
        """Purge task submission time
        :rtype: str
        """
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
        :param _Urls: List of URLs to be purged. The protocol header must be included.
        :type Urls: list of str
        """
        self._Urls = None

    @property
    def Urls(self):
        """List of URLs to be purged. The protocol header must be included.
        :rtype: list of str
        """
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
        


class PurgeUrlsCacheResponse(AbstractModel):
    """PurgeUrlsCache response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Purge task ID
        :type TaskId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """Purge task ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class Quota(AbstractModel):
    """Purge usage and quota

    """

    def __init__(self):
        r"""
        :param _Batch: Quota limit for one batch submission request.
        :type Batch: int
        :param _Total: Daily submission quota limit.
        :type Total: int
        :param _Available: Remaining daily submission quota.
        :type Available: int
        """
        self._Batch = None
        self._Total = None
        self._Available = None

    @property
    def Batch(self):
        """Quota limit for one batch submission request.
        :rtype: int
        """
        return self._Batch

    @Batch.setter
    def Batch(self, Batch):
        self._Batch = Batch

    @property
    def Total(self):
        """Daily submission quota limit.
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Available(self):
        """Remaining daily submission quota.
        :rtype: int
        """
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available


    def _deserialize(self, params):
        self._Batch = params.get("Batch")
        self._Total = params.get("Total")
        self._Available = params.get("Available")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceData(AbstractModel):
    """Query object and its access details

    """

    def __init__(self):
        r"""
        :param _Resource: Resource name, which is categorized as follows based on different query conditions:
Specific domain name: indicates the details of the specific domain name
multiDomains: indicates aggregated details of multiple domain names
Project ID: displays the ID of the specified project to be queried
all: details at the account level
        :type Resource: str
        :param _EcdnData: Data details of resource
        :type EcdnData: :class:`tencentcloud.ecdn.v20191012.models.EcdnData`
        """
        self._Resource = None
        self._EcdnData = None

    @property
    def Resource(self):
        """Resource name, which is categorized as follows based on different query conditions:
Specific domain name: indicates the details of the specific domain name
multiDomains: indicates aggregated details of multiple domain names
Project ID: displays the ID of the specified project to be queried
all: details at the account level
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def EcdnData(self):
        """Data details of resource
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.EcdnData`
        """
        return self._EcdnData

    @EcdnData.setter
    def EcdnData(self, EcdnData):
        self._EcdnData = EcdnData


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        if params.get("EcdnData") is not None:
            self._EcdnData = EcdnData()
            self._EcdnData._deserialize(params.get("EcdnData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResponseHeader(AbstractModel):
    """Custom response header configuration.

    """

    def __init__(self):
        r"""
        :param _Switch: Custom response header switch. Valid values: on, off.
        :type Switch: str
        :param _HeaderRules: Custom response header rule array.
Note: this field may return null, indicating that no valid values can be obtained.
        :type HeaderRules: list of HttpHeaderPathRule
        """
        self._Switch = None
        self._HeaderRules = None

    @property
    def Switch(self):
        """Custom response header switch. Valid values: on, off.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def HeaderRules(self):
        """Custom response header rule array.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: list of HttpHeaderPathRule
        """
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
        


class ServerCert(AbstractModel):
    """HTTPS server certificate configuration.

    """

    def __init__(self):
        r"""
        :param _CertId: Server certificate ID, which is required if the certificate is a Tencent Cloud-hosted certificate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertId: str
        :param _CertName: Server certificate name, which is required if the certificate is a Tencent Cloud-hosted certificate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertName: str
        :param _Certificate: Server certificate information, which is required when uploading your own certificate and must contain complete certificate chain information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Certificate: str
        :param _PrivateKey: Server key information, which is required when uploading your own certificate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateKey: str
        :param _ExpireTime: Certificate expiration time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param _DeployTime: Certificate issuance time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeployTime: str
        :param _Message: Certificate remarks.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Message: str
        """
        self._CertId = None
        self._CertName = None
        self._Certificate = None
        self._PrivateKey = None
        self._ExpireTime = None
        self._DeployTime = None
        self._Message = None

    @property
    def CertId(self):
        """Server certificate ID, which is required if the certificate is a Tencent Cloud-hosted certificate.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertName(self):
        """Server certificate name, which is required if the certificate is a Tencent Cloud-hosted certificate.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def Certificate(self):
        """Server certificate information, which is required when uploading your own certificate and must contain complete certificate chain information.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def PrivateKey(self):
        """Server key information, which is required when uploading your own certificate.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def ExpireTime(self):
        """Certificate expiration time.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def DeployTime(self):
        """Certificate issuance time.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._DeployTime

    @DeployTime.setter
    def DeployTime(self, DeployTime):
        self._DeployTime = DeployTime

    @property
    def Message(self):
        """Certificate remarks.
Note: this field may return null, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._CertName = params.get("CertName")
        self._Certificate = params.get("Certificate")
        self._PrivateKey = params.get("PrivateKey")
        self._ExpireTime = params.get("ExpireTime")
        self._DeployTime = params.get("DeployTime")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Sort(AbstractModel):
    """Sorting criteria for query results.

    """

    def __init__(self):
        r"""
        :param _Key: Sort by field. Valid values:
createTime: domain name creation time
certExpireTime: certificate expiration time
        :type Key: str
        :param _Sequence: asc/desc. Default value: desc.
        :type Sequence: str
        """
        self._Key = None
        self._Sequence = None

    @property
    def Key(self):
        """Sort by field. Valid values:
createTime: domain name creation time
certExpireTime: certificate expiration time
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Sequence(self):
        """asc/desc. Default value: desc.
        :rtype: str
        """
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
        


class StartEcdnDomainRequest(AbstractModel):
    """StartEcdnDomain request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain name to be enabled.
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        """Domain name to be enabled.
        :rtype: str
        """
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
        


class StartEcdnDomainResponse(AbstractModel):
    """StartEcdnDomain response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopEcdnDomainRequest(AbstractModel):
    """StopEcdnDomain request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain name to be disabled.
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        """Domain name to be disabled.
        :rtype: str
        """
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
        


class StopEcdnDomainResponse(AbstractModel):
    """StopEcdnDomain response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """Tag key and tag value.

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type TagKey: str
        :param _TagValue: Tag value.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """Tag key.
Note: this field may return `null`, indicating that no valid value is obtained.
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """Tag value.
Note: this field may return `null`, indicating that no valid value is obtained.
        :rtype: str
        """
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
        :param _Time: Statistical time point in forward rounding mode
Taking the 5-minute granularity as an example, 13:35:00 indicates that the statistical interval is between 13:35:00 and 13:39:59
        :type Time: str
        :param _Value: Data value
        :type Value: list of float
        """
        self._Time = None
        self._Value = None

    @property
    def Time(self):
        """Statistical time point in forward rounding mode
Taking the 5-minute granularity as an example, 13:35:00 indicates that the statistical interval is between 13:35:00 and 13:39:59
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        """Data value
        :rtype: list of float
        """
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
        


class UpdateDomainConfigRequest(AbstractModel):
    """UpdateDomainConfig request structure.

    """

    def __init__(self):
        r"""
        :param _Domain: Domain name.
        :type Domain: str
        :param _Origin: Origin server configuration.
        :type Origin: :class:`tencentcloud.ecdn.v20191012.models.Origin`
        :param _ProjectId: Project ID.
        :type ProjectId: int
        :param _IpFilter: IP blocklist/allowlist configuration.
        :type IpFilter: :class:`tencentcloud.ecdn.v20191012.models.IpFilter`
        :param _IpFreqLimit: IP access limit configuration.
        :type IpFreqLimit: :class:`tencentcloud.ecdn.v20191012.models.IpFreqLimit`
        :param _ResponseHeader: Origin server response header configuration.
        :type ResponseHeader: :class:`tencentcloud.ecdn.v20191012.models.ResponseHeader`
        :param _CacheKey: Node caching configuration.
        :type CacheKey: :class:`tencentcloud.ecdn.v20191012.models.CacheKey`
        :param _Cache: Caching rule configuration.
        :type Cache: :class:`tencentcloud.ecdn.v20191012.models.Cache`
        :param _Https: HTTPS configuration.
        :type Https: :class:`tencentcloud.ecdn.v20191012.models.Https`
        :param _ForceRedirect: Forced access protocol redirection configuration.
        :type ForceRedirect: :class:`tencentcloud.ecdn.v20191012.models.ForceRedirect`
        :param _Area: Domain name acceleration region. Valid values: mainland (acceleration in Mainland China), overseas (acceleration outside Mainland China), global (global acceleration).
        :type Area: str
        :param _WebSocket: WebSocket configuration.
        :type WebSocket: :class:`tencentcloud.ecdn.v20191012.models.WebSocket`
        """
        self._Domain = None
        self._Origin = None
        self._ProjectId = None
        self._IpFilter = None
        self._IpFreqLimit = None
        self._ResponseHeader = None
        self._CacheKey = None
        self._Cache = None
        self._Https = None
        self._ForceRedirect = None
        self._Area = None
        self._WebSocket = None

    @property
    def Domain(self):
        """Domain name.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Origin(self):
        """Origin server configuration.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.Origin`
        """
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def ProjectId(self):
        """Project ID.
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def IpFilter(self):
        """IP blocklist/allowlist configuration.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.IpFilter`
        """
        return self._IpFilter

    @IpFilter.setter
    def IpFilter(self, IpFilter):
        self._IpFilter = IpFilter

    @property
    def IpFreqLimit(self):
        """IP access limit configuration.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.IpFreqLimit`
        """
        return self._IpFreqLimit

    @IpFreqLimit.setter
    def IpFreqLimit(self, IpFreqLimit):
        self._IpFreqLimit = IpFreqLimit

    @property
    def ResponseHeader(self):
        """Origin server response header configuration.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.ResponseHeader`
        """
        return self._ResponseHeader

    @ResponseHeader.setter
    def ResponseHeader(self, ResponseHeader):
        self._ResponseHeader = ResponseHeader

    @property
    def CacheKey(self):
        """Node caching configuration.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.CacheKey`
        """
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def Cache(self):
        """Caching rule configuration.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.Cache`
        """
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def Https(self):
        """HTTPS configuration.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.Https`
        """
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def ForceRedirect(self):
        """Forced access protocol redirection configuration.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.ForceRedirect`
        """
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def Area(self):
        """Domain name acceleration region. Valid values: mainland (acceleration in Mainland China), overseas (acceleration outside Mainland China), global (global acceleration).
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def WebSocket(self):
        """WebSocket configuration.
        :rtype: :class:`tencentcloud.ecdn.v20191012.models.WebSocket`
        """
        return self._WebSocket

    @WebSocket.setter
    def WebSocket(self, WebSocket):
        self._WebSocket = WebSocket


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
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
        if params.get("ResponseHeader") is not None:
            self._ResponseHeader = ResponseHeader()
            self._ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Cache") is not None:
            self._Cache = Cache()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirect()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        self._Area = params.get("Area")
        if params.get("WebSocket") is not None:
            self._WebSocket = WebSocket()
            self._WebSocket._deserialize(params.get("WebSocket"))
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
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class WebSocket(AbstractModel):
    """WebSocket configuration.

    """

    def __init__(self):
        r"""
        :param _Switch: Whether to enable custom WebSocket timeout setting. When it’s `off`: WebSocket connection is supported, and the default timeout period is 15 seconds. To change the timeout period, please set it to `on`.

* WebSocket is now only available for beta users. To use it, please submit a ticket.
        :type Switch: str
        :param _Timeout: Sets timeout period in seconds. Maximum value: 65
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Timeout: int
        """
        self._Switch = None
        self._Timeout = None

    @property
    def Switch(self):
        """Whether to enable custom WebSocket timeout setting. When it’s `off`: WebSocket connection is supported, and the default timeout period is 15 seconds. To change the timeout period, please set it to `on`.

* WebSocket is now only available for beta users. To use it, please submit a ticket.
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Timeout(self):
        """Sets timeout period in seconds. Maximum value: 65
Note: This field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
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
        