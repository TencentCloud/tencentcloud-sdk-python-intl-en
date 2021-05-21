# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
        """
        :param Domain: Domain name.
        :type Domain: str
        :param Origin: Origin server configuration.
        :type Origin: :class:`tencentcloud.ecdn.v20191012.models.Origin`
        :param Area: Domain name acceleration region. Valid values: mainland (acceleration in Mainland China), overseas (acceleration outside Mainland China), global (global acceleration).
        :type Area: str
        :param ProjectId: Project ID. Default value: 0.
        :type ProjectId: int
        :param IpFilter: IP block/allowlist configuration.
        :type IpFilter: :class:`tencentcloud.ecdn.v20191012.models.IpFilter`
        :param IpFreqLimit: IP access limit configuration.
        :type IpFreqLimit: :class:`tencentcloud.ecdn.v20191012.models.IpFreqLimit`
        :param ResponseHeader: Origin server response header configuration.
        :type ResponseHeader: :class:`tencentcloud.ecdn.v20191012.models.ResponseHeader`
        :param CacheKey: Node caching configuration.
        :type CacheKey: :class:`tencentcloud.ecdn.v20191012.models.CacheKey`
        :param Cache: Caching rule configuration.
        :type Cache: :class:`tencentcloud.ecdn.v20191012.models.Cache`
        :param Https: HTTPS configuration.
        :type Https: :class:`tencentcloud.ecdn.v20191012.models.Https`
        :param ForceRedirect: Forced access protocol redirection configuration.
        :type ForceRedirect: :class:`tencentcloud.ecdn.v20191012.models.ForceRedirect`
        :param Tag: Tag bound to a domain name.
        :type Tag: list of Tag
        :param WebSocket: WebSocket configuration.
        :type WebSocket: :class:`tencentcloud.ecdn.v20191012.models.WebSocket`
        """
        self.Domain = None
        self.Origin = None
        self.Area = None
        self.ProjectId = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.ResponseHeader = None
        self.CacheKey = None
        self.Cache = None
        self.Https = None
        self.ForceRedirect = None
        self.Tag = None
        self.WebSocket = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        self.Area = params.get("Area")
        self.ProjectId = params.get("ProjectId")
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self.Tag.append(obj)
        if params.get("WebSocket") is not None:
            self.WebSocket = WebSocket()
            self.WebSocket._deserialize(params.get("WebSocket"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddEcdnDomainResponse(AbstractModel):
    """AddEcdnDomain response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Cache(AbstractModel):
    """Simple edition of cache configuration, which does not support setting a caching rule for scenarios where the `max-age` is not returned from the origin server.

    """

    def __init__(self):
        """
        :param CacheRules: Caching configuration rule array.
        :type CacheRules: list of CacheRule
        :param FollowOrigin: Whether to follow the `Cache-Control: max-age` configuration on the origin server (this feature is only available to users on the allowlist).
on: enable
off: disable
If it is enabled, resources that do not match `CacheRules` will be cached on node according to the `max-age` value returned by the origin server, while resources that match `CacheRules` will be cached on node according to the cache expiration time set in `CacheRules`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FollowOrigin: str
        """
        self.CacheRules = None
        self.FollowOrigin = None


    def _deserialize(self, params):
        if params.get("CacheRules") is not None:
            self.CacheRules = []
            for item in params.get("CacheRules"):
                obj = CacheRule()
                obj._deserialize(item)
                self.CacheRules.append(obj)
        self.FollowOrigin = params.get("FollowOrigin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CacheKey(AbstractModel):
    """Caching configuration.

    """

    def __init__(self):
        """
        :param FullUrlCache: Whether to enable full path cache. Valid values: on, off.
        :type FullUrlCache: str
        """
        self.FullUrlCache = None


    def _deserialize(self, params):
        self.FullUrlCache = params.get("FullUrlCache")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CacheRule(AbstractModel):
    """Caching configuration rule.

    """

    def __init__(self):
        """
        :param CacheType: Cache type. Valid values: all (all files), file (extension type), directory (directory), path (full path), index (homepage).
        :type CacheType: str
        :param CacheContents: Cached content list.
        :type CacheContents: list of str
        :param CacheTime: Cache time in seconds.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClientCert(AbstractModel):
    """HTTPS client certificate configuration.

    """

    def __init__(self):
        """
        :param Certificate: Client certificate in PEM format.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Certificate: str
        :param CertName: Client certificate name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertName: str
        :param ExpireTime: Certificate expiration time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param DeployTime: Certificate issuance time.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteEcdnDomainRequest(AbstractModel):
    """DeleteEcdnDomain request structure.

    """

    def __init__(self):
        """
        :param Domain: Domain name to be deleted.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteEcdnDomainResponse(AbstractModel):
    """DeleteEcdnDomain response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDomainsConfigRequest(AbstractModel):
    """DescribeDomainsConfig request structure.

    """

    def __init__(self):
        """
        :param Offset: Pagination offset address. Default value: 0.
        :type Offset: int
        :param Limit: Number of domain names per page. Default value: 100.
        :type Limit: int
        :param Filters: Query filter.
        :type Filters: list of DomainFilter
        :param Sort: Query result sorting rule.
        :type Sort: :class:`tencentcloud.ecdn.v20191012.models.Sort`
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDomainsConfigResponse(AbstractModel):
    """DescribeDomainsConfig response structure.

    """

    def __init__(self):
        """
        :param Domains: Domain name list.
        :type Domains: list of DomainDetailInfo
        :param TotalCount: Number of matched domain names. This is used for paginated query.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Domains = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self.Domains = []
            for item in params.get("Domains"):
                obj = DomainDetailInfo()
                obj._deserialize(item)
                self.Domains.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDomainsRequest(AbstractModel):
    """DescribeDomains request structure.

    """

    def __init__(self):
        """
        :param Offset: Pagination offset address. Default value: 0.
        :type Offset: int
        :param Limit: Number of domain names per page. Default value: 100. Maximum value: 1000.
        :type Limit: int
        :param Filters: Query filter.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDomainsResponse(AbstractModel):
    """DescribeDomains response structure.

    """

    def __init__(self):
        """
        :param Domains: Domain name information list.
        :type Domains: list of DomainBriefInfo
        :param TotalCount: Total number of domain names.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Domains = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self.Domains = []
            for item in params.get("Domains"):
                obj = DomainBriefInfo()
                obj._deserialize(item)
                self.Domains.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeEcdnDomainLogsRequest(AbstractModel):
    """DescribeEcdnDomainLogs request structure.

    """

    def __init__(self):
        """
        :param Domain: Domain name to be queried.
        :type Domain: str
        :param StartTime: Log start time, such as 2019-10-01 00:00:00
        :type StartTime: str
        :param EndTime: Log end time, such as 2019-10-02 00:00:00. Only logs for the last 30 days can be queried.
        :type EndTime: str
        :param Offset: Pagination offset for log link list. Default value: 0.
        :type Offset: int
        :param Limit: Number of log links per page. Default value: 100. Maximum value: 1000.
        :type Limit: int
        """
        self.Domain = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeEcdnDomainLogsResponse(AbstractModel):
    """DescribeEcdnDomainLogs response structure.

    """

    def __init__(self):
        """
        :param DomainLogs: Log link list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DomainLogs: list of DomainLogs
        :param TotalCount: Total number of log links.
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
                obj = DomainLogs()
                obj._deserialize(item)
                self.DomainLogs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeEcdnDomainStatisticsRequest(AbstractModel):
    """DescribeEcdnDomainStatistics request structure.

    """

    def __init__(self):
        """
        :param StartTime: Query start time, such as 2019-12-13 00:00:00.
The time span cannot exceed 90 days.
        :type StartTime: str
        :param EndTime: Query end time, such as 2019-12-13 23:59:59.
The time span cannot exceed 90 days.
        :type EndTime: str
        :param Metrics: Statistical metric names:
flux: traffic (in bytes)
bandwidth: bandwidth (in bps)
request: number of requests
        :type Metrics: list of str
        :param Domains: Specifies the list of domain names to be queried
        :type Domains: list of str
        :param Projects: Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)
If no domain name is entered, the specified project will be queried; otherwise, the domain name will prevail
        :type Projects: list of int
        :param Offset: Pagination offset. Default value: 0.
        :type Offset: int
        :param Limit: Number of entries per page. Default value: 1000. Maximum value: 3,000.
        :type Limit: int
        :param Area: Statistical areas:
mainland: Chinese mainland
oversea: outside the Chinese mainland
global: global
Default value: global
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Metrics = None
        self.Domains = None
        self.Projects = None
        self.Offset = None
        self.Limit = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metrics = params.get("Metrics")
        self.Domains = params.get("Domains")
        self.Projects = params.get("Projects")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeEcdnDomainStatisticsResponse(AbstractModel):
    """DescribeEcdnDomainStatistics response structure.

    """

    def __init__(self):
        """
        :param Data: Domain name data
        :type Data: list of DomainData
        :param TotalCount: Quantity
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DomainData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeEcdnStatisticsRequest(AbstractModel):
    """DescribeEcdnStatistics request structure.

    """

    def __init__(self):
        """
        :param StartTime: Query start time, such as 2019-12-13 00:00:00
        :type StartTime: str
        :param EndTime: Query end time, such as 2019-12-13 23:59:59
        :type EndTime: str
        :param Metrics: Specifies the query metric, which can be:
flux: traffic (in bytes)
bandwidth: bandwidth (in bps)
request: number of requests
2xx: returns the number of 2xx status codes or details of status codes starting with 2
3xx: returns the number of 3xx status codes or details of status codes starting with 3
4xx: returns the number of 4xx status codes or details of status codes starting with 4
5xx: returns the number of 5xx status codes or details of status codes starting with 5
        :type Metrics: list of str
        :param Interval: Time granularity, which can be:
1 day	 1, 5, 15, 30, 60, 120, 240, 1440 
2-3 days 15, 30, 60, 120, 240, 1440
4-7 days 30, 60, 120, 240, 1440
8-90 days	 60, 120, 240, 1440
        :type Interval: int
        :param Domains: Specifies the list of domain names to be queried

Up to 30 acceleration domain names can be queried at a time.
        :type Domains: list of str
        :param Projects: Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)
If no domain name is entered, the specified project will be queried; otherwise, the domain name will prevail
        :type Projects: list of int
        :param Area: Statistical areas:
mainland: Chinese mainland
oversea: outside the Chinese mainland
global: global
Default value: global
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Metrics = None
        self.Interval = None
        self.Domains = None
        self.Projects = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metrics = params.get("Metrics")
        self.Interval = params.get("Interval")
        self.Domains = params.get("Domains")
        self.Projects = params.get("Projects")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeEcdnStatisticsResponse(AbstractModel):
    """DescribeEcdnStatistics response structure.

    """

    def __init__(self):
        """
        :param Data: Returned data details of the specified conditional query
        :type Data: list of ResourceData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ResourceData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeIpStatusRequest(AbstractModel):
    """DescribeIpStatus request structure.

    """

    def __init__(self):
        """
        :param Domain: Acceleration domain name
        :type Domain: str
        :param Area: Target region of the query:
mainland: nodes in Mainland China
overseas: nodes outside Mainland China
global: global nodes
        :type Area: str
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeIpStatusResponse(AbstractModel):
    """DescribeIpStatus response structure.

    """

    def __init__(self):
        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePurgeQuotaRequest(AbstractModel):
    """DescribePurgeQuota request structure.

    """


class DescribePurgeQuotaResponse(AbstractModel):
    """DescribePurgeQuota response structure.

    """

    def __init__(self):
        """
        :param UrlPurge: URL purge usage and quota.
        :type UrlPurge: :class:`tencentcloud.ecdn.v20191012.models.Quota`
        :param PathPurge: Directory purge usage and quota.
        :type PathPurge: :class:`tencentcloud.ecdn.v20191012.models.Quota`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UrlPurge = None
        self.PathPurge = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UrlPurge") is not None:
            self.UrlPurge = Quota()
            self.UrlPurge._deserialize(params.get("UrlPurge"))
        if params.get("PathPurge") is not None:
            self.PathPurge = Quota()
            self.PathPurge._deserialize(params.get("PathPurge"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePurgeTasksRequest(AbstractModel):
    """DescribePurgeTasks request structure.

    """

    def __init__(self):
        """
        :param PurgeType: Purge type to be queried. url: query URL purge records; path: query directory purge records.
        :type PurgeType: str
        :param StartTime: Start time, such as 2018-08-08 00:00:00
        :type StartTime: str
        :param EndTime: End time, such as 2018-08-08 23:59:59
        :type EndTime: str
        :param TaskId: Task ID returned during submission. Either `TaskId` or start time must be specified for a query.
        :type TaskId: str
        :param Offset: Pagination offset. Default value: 0 (starting from entry 0).
        :type Offset: int
        :param Limit: Pagination limit. Default value: 20.
        :type Limit: int
        :param Keyword: Query keyword. Please enter a domain name or full URL beginning with `http(s)://`.
        :type Keyword: str
        :param Status: Specified task status to be queried. fail: failed, done: succeeded, process: purging.
        :type Status: str
        """
        self.PurgeType = None
        self.StartTime = None
        self.EndTime = None
        self.TaskId = None
        self.Offset = None
        self.Limit = None
        self.Keyword = None
        self.Status = None


    def _deserialize(self, params):
        self.PurgeType = params.get("PurgeType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TaskId = params.get("TaskId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Keyword = params.get("Keyword")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePurgeTasksResponse(AbstractModel):
    """DescribePurgeTasks response structure.

    """

    def __init__(self):
        """
        :param PurgeLogs: Purge history.
        :type PurgeLogs: list of PurgeTask
        :param TotalCount: Total number of tasks, which is used for pagination.
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DetailData(AbstractModel):
    """Data structure of sorted data

    """

    def __init__(self):
        """
        :param Name: Data type name
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DomainBriefInfo(AbstractModel):
    """Basic information of a CDN domain name.

    """

    def __init__(self):
        """
        :param ResourceId: Domain name ID.
        :type ResourceId: str
        :param AppId: Tencent Cloud account ID.
        :type AppId: int
        :param Domain: CDN acceleration domain name.
        :type Domain: str
        :param Cname: Domain name CNAME.
        :type Cname: str
        :param Status: Domain name status. Valid values: pending (reviewing), rejected (rejected), processing (deploying after approval), online (enabled), offline (disabled), deleted (deleted).
        :type Status: str
        :param ProjectId: Project ID.
        :type ProjectId: int
        :param CreateTime: Domain name creation time.
        :type CreateTime: str
        :param UpdateTime: Domain name update time.
        :type UpdateTime: str
        :param Origin: Origin server configuration details.
        :type Origin: :class:`tencentcloud.ecdn.v20191012.models.Origin`
        :param Disable: Domain name blockage status. Valid values: normal (normal), overdue (service is suspended due to arrears), quota (trial traffic package is used up), malicious (malicious user), ddos (DDoS attack), idle (no traffic), unlicensed (no ICP filing), capping (bandwidth cap reached), readonly (read-only)
        :type Disable: str
        :param Area: Acceleration region. Valid values: mainland, oversea, global.
        :type Area: str
        :param Readonly: Domain name lock status. normal: not locked; global: globally locked
        :type Readonly: str
        """
        self.ResourceId = None
        self.AppId = None
        self.Domain = None
        self.Cname = None
        self.Status = None
        self.ProjectId = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Origin = None
        self.Disable = None
        self.Area = None
        self.Readonly = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.AppId = params.get("AppId")
        self.Domain = params.get("Domain")
        self.Cname = params.get("Cname")
        self.Status = params.get("Status")
        self.ProjectId = params.get("ProjectId")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        self.Disable = params.get("Disable")
        self.Area = params.get("Area")
        self.Readonly = params.get("Readonly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DomainData(AbstractModel):
    """Data structure of sorted data

    """

    def __init__(self):
        """
        :param Resource: Domain name
        :type Resource: str
        :param DetailData: Result details.
        :type DetailData: list of DetailData
        """
        self.Resource = None
        self.DetailData = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("DetailData") is not None:
            self.DetailData = []
            for item in params.get("DetailData"):
                obj = DetailData()
                obj._deserialize(item)
                self.DetailData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DomainDetailInfo(AbstractModel):
    """Detailed configuration information of ECDN domain name.

    """

    def __init__(self):
        """
        :param ResourceId: Domain name ID.
        :type ResourceId: str
        :param AppId: Tencent Cloud account ID.
        :type AppId: int
        :param Domain: Acceleration domain name.
        :type Domain: str
        :param Cname: Domain name CNAME.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Cname: str
        :param Status: Domain name status. Valid values: pending (reviewing), rejected (rejected), processing (deploying after approval), online (enabled), offline (disabled), deleted (deleted).
        :type Status: str
        :param ProjectId: Project ID.
        :type ProjectId: int
        :param CreateTime: Domain name creation time.
        :type CreateTime: str
        :param UpdateTime: Domain name update time.
        :type UpdateTime: str
        :param Origin: Origin server configuration.
        :type Origin: :class:`tencentcloud.ecdn.v20191012.models.Origin`
        :param IpFilter: IP blocklist/allowlist configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpFilter: :class:`tencentcloud.ecdn.v20191012.models.IpFilter`
        :param IpFreqLimit: IP access limit configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type IpFreqLimit: :class:`tencentcloud.ecdn.v20191012.models.IpFreqLimit`
        :param ResponseHeader: Origin server response header configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ResponseHeader: :class:`tencentcloud.ecdn.v20191012.models.ResponseHeader`
        :param CacheKey: Node caching configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CacheKey: :class:`tencentcloud.ecdn.v20191012.models.CacheKey`
        :param Cache: Caching rule configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Cache: :class:`tencentcloud.ecdn.v20191012.models.Cache`
        :param Https: HTTPS configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Https: :class:`tencentcloud.ecdn.v20191012.models.Https`
        :param Disable: Domain name blockage status. Valid values: normal (normal), overdue (service is suspended due to arrears), quota (trial traffic package is used up), malicious (malicious user), ddos (DDoS attack), idle (no traffic), unlicensed (no ICP filing), capping (bandwidth cap reached), readonly (read-only).
Note: this field may return null, indicating that no valid values can be obtained.
        :type Disable: str
        :param ForceRedirect: Forced access protocol redirection configuration.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ForceRedirect: :class:`tencentcloud.ecdn.v20191012.models.ForceRedirect`
        :param Area: Acceleration region. Valid values: mainland, overseas, global.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Area: str
        :param Readonly: Domain name lock status. normal: not locked; global: globally locked.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Readonly: str
        :param Tag: Domain name tag
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Tag: list of Tag
        :param WebSocket: WebSocket configuration.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type WebSocket: :class:`tencentcloud.ecdn.v20191012.models.WebSocket`
        """
        self.ResourceId = None
        self.AppId = None
        self.Domain = None
        self.Cname = None
        self.Status = None
        self.ProjectId = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Origin = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.ResponseHeader = None
        self.CacheKey = None
        self.Cache = None
        self.Https = None
        self.Disable = None
        self.ForceRedirect = None
        self.Area = None
        self.Readonly = None
        self.Tag = None
        self.WebSocket = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.AppId = params.get("AppId")
        self.Domain = params.get("Domain")
        self.Cname = params.get("Cname")
        self.Status = params.get("Status")
        self.ProjectId = params.get("ProjectId")
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
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        self.Disable = params.get("Disable")
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        self.Area = params.get("Area")
        self.Readonly = params.get("Readonly")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self.Tag.append(obj)
        if params.get("WebSocket") is not None:
            self.WebSocket = WebSocket()
            self.WebSocket._deserialize(params.get("WebSocket"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DomainFilter(AbstractModel):
    """Filter for domain name query.

    """

    def __init__(self):
        """
        :param Name: Filter field name, which can be:
- origin: primary origin server.
- domain: domain name.
- resourceId: domain name ID.
- status: domain name status. Valid values: online, offline, processing.
- disable: domain name blockage status. Valid values: normal, unlicensed.
- projectId: project ID.
- fullUrlCache: full path cache. Valid values: on, off.
- https: whether to configure HTTPS. Valid values: on, off, processing.
- originPullProtocol: origin-pull protocol type. Valid values: http, follow, https.
- area: acceleration region. Valid values: mainland, overseas, global.
        :type Name: str
        :param Value: Filter field value.
        :type Value: list of str
        :param Fuzzy: Whether to enable fuzzy query, which is supported only for filter fields `origin` and `domain`.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DomainLogs(AbstractModel):
    """Domain name log information.

    """

    def __init__(self):
        """
        :param StartTime: Log start time.
        :type StartTime: str
        :param EndTime: Log end time.
        :type EndTime: str
        :param LogPath: Log download path.
        :type LogPath: str
        """
        self.StartTime = None
        self.EndTime = None
        self.LogPath = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.LogPath = params.get("LogPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EcdnData(AbstractModel):
    """Detailed access data type

    """

    def __init__(self):
        """
        :param Metrics: Queries the specified metric. Valid values: Bandwidth, Flux, Request, Delay, status code, LogBandwidth, LogFlux, LogRequest
        :type Metrics: list of str
        :param DetailData: Detailed data collection
        :type DetailData: list of TimestampData
        """
        self.Metrics = None
        self.DetailData = None


    def _deserialize(self, params):
        self.Metrics = params.get("Metrics")
        if params.get("DetailData") is not None:
            self.DetailData = []
            for item in params.get("DetailData"):
                obj = TimestampData()
                obj._deserialize(item)
                self.DetailData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ForceRedirect(AbstractModel):
    """Forced access protocol redirection configuration.

    """

    def __init__(self):
        """
        :param Switch: Forced access protocol redirection configuration switch. Valid values: on, off.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param RedirectType: Access protocol type for forced redirection. Valid values: http (forced redirection to HTTP protocol), https (forced redirection to HTTPS protocol).
Note: this field may return null, indicating that no valid values can be obtained.
        :type RedirectType: str
        :param RedirectStatusCode: HTTP status code returned when forced redirection is enabled. Valid values: 301, 302.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RedirectStatusCode: int
        """
        self.Switch = None
        self.RedirectType = None
        self.RedirectStatusCode = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.RedirectType = params.get("RedirectType")
        self.RedirectStatusCode = params.get("RedirectStatusCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Hsts(AbstractModel):
    """HSTS configuration.

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class HttpHeaderPathRule(AbstractModel):
    """Path-specific HTTP header setting rule.

    """

    def __init__(self):
        """
        :param HeaderMode: HTTP header setting method. Valid values: add (add header), set (set header), del (delete header).
Request header currently does not support `set`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type HeaderMode: str
        :param HeaderName: HTTP header name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type HeaderName: str
        :param HeaderValue: HTTP header value, which is optional when it is `del`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type HeaderValue: str
        :param RuleType: Type of effective URL path rule. Valid values: all (all paths), file (file extension), directory (directory), path (absolute path).
Note: this field may return null, indicating that no valid values can be obtained.
        :type RuleType: str
        :param RulePaths: URL path or file type list
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Https(AbstractModel):
    """HTTPS configuration of domain name.

    """

    def __init__(self):
        """
        :param Switch: HTTPS configuration switch. Valid values: on, off. If the domain name with HTTPS configuration enabled is being deployed, this switch will be `off`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Switch: str
        :param Http2: Whether to enable HTTP2. Valid values: on, off.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Http2: str
        :param OcspStapling: Whether to enable the OCSP feature. Valid values: on, off.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OcspStapling: str
        :param VerifyClient: Whether to enable the client certificate verification feature. Valid values: on, off. The client certificate information must be uploaded if this feature is enabled.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VerifyClient: str
        :param CertInfo: Server certificate configuration information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertInfo: :class:`tencentcloud.ecdn.v20191012.models.ServerCert`
        :param ClientCertInfo: Client certificate configuration information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClientCertInfo: :class:`tencentcloud.ecdn.v20191012.models.ClientCert`
        :param Spdy: Whether to enable SPDY. Valid values: on, off.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Spdy: str
        :param SslStatus: HTTPS certificate deployment status. Valid values: closed (disabled), deploying (deploying), deployed (deployment succeeded), failed (deployment failed). This parameter cannot be used as an input parameter.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SslStatus: str
        :param Hsts: HSTS configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type Hsts: :class:`tencentcloud.ecdn.v20191012.models.Hsts`
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class IpFilter(AbstractModel):
    """IP blocklist/allowlist.

    """

    def __init__(self):
        """
        :param Switch: IP blocklist/allowlist switch. Valid values: on, off.
        :type Switch: str
        :param FilterType: IP blocklist/allowlist type. Valid values: whitelist, blacklist.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FilterType: str
        :param Filters: IP blocklist/allowlist list.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Filters: list of str
        """
        self.Switch = None
        self.FilterType = None
        self.Filters = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.FilterType = params.get("FilterType")
        self.Filters = params.get("Filters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class IpFreqLimit(AbstractModel):
    """IP access limit configuration.

    """

    def __init__(self):
        """
        :param Switch: IP access limit switch. Valid values: on, off.
        :type Switch: str
        :param Qps: Number of requests per second.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class IpStatus(AbstractModel):
    """Node IP information

    """

    def __init__(self):
        """
        :param Ip: Node IP
        :type Ip: str
        :param District: Node region
        :type District: str
        :param Isp: Node ISP
        :type Isp: str
        :param City: Node city
        :type City: str
        :param Status: Node status
online: the node is online and scheduling normally
offline: the node is offline
        :type Status: str
        :param CreateTime: Node IP creation time
        :type CreateTime: str
        """
        self.Ip = None
        self.District = None
        self.Isp = None
        self.City = None
        self.Status = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.District = params.get("District")
        self.Isp = params.get("Isp")
        self.City = params.get("City")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Origin(AbstractModel):
    """Origin server configuration.

    """

    def __init__(self):
        """
        :param Origins: Primary origin server list. IP and the domain name of the origin server cannot be entered at the same time. Configure origin server port in the format of ["origin1:port1", "origin2:port2"]. Configure origin-pull weight in the format of ["origin1::weight1", "origin2::weight2"]. Configure both port and weight in the format of ["origin1:port1:weight1", "origin2:port2:weight2"]. Valid range of weight value: 0 - 100.
        :type Origins: list of str
        :param OriginType: Primary origin server type. Valid values: domain (domain name origin server), ip (IP origin server).
This is required when setting `Origins`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type OriginType: str
        :param ServerName: Host header value during origin-pull.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ServerName: str
        :param OriginPullProtocol: Origin-pull protocol type. Valid values: http (forced HTTP origin-pull), follow (protocol follow), https (HTTPS origin-pull).
If this parameter is left empty, HTTP origin-pull will be used by default.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type OriginPullProtocol: str
        :param BackupOrigins: Secondary origin server list.
        :type BackupOrigins: list of str
        :param BackupOriginType: Secondary origin server type, which is the same as `OriginType`.
This is required when setting `BackupOrigins`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BackupOriginType: str
        """
        self.Origins = None
        self.OriginType = None
        self.ServerName = None
        self.OriginPullProtocol = None
        self.BackupOrigins = None
        self.BackupOriginType = None


    def _deserialize(self, params):
        self.Origins = params.get("Origins")
        self.OriginType = params.get("OriginType")
        self.ServerName = params.get("ServerName")
        self.OriginPullProtocol = params.get("OriginPullProtocol")
        self.BackupOrigins = params.get("BackupOrigins")
        self.BackupOriginType = params.get("BackupOriginType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PurgePathCacheRequest(AbstractModel):
    """PurgePathCache request structure.

    """

    def __init__(self):
        """
        :param Paths: List of directories to be purged. The protocol header must be included.
        :type Paths: list of str
        :param FlushType: Purge type. flush: purges updated resources, delete: purges all resources.
        :type FlushType: str
        """
        self.Paths = None
        self.FlushType = None


    def _deserialize(self, params):
        self.Paths = params.get("Paths")
        self.FlushType = params.get("FlushType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PurgePathCacheResponse(AbstractModel):
    """PurgePathCache response structure.

    """

    def __init__(self):
        """
        :param TaskId: Purge task ID. The first ten digits are the UTC time when the task is submitted.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PurgeTask(AbstractModel):
    """Purge task log details.

    """

    def __init__(self):
        """
        :param TaskId: Purge task ID.
        :type TaskId: str
        :param Url: Purged URL.
        :type Url: str
        :param Status: Purge task status. fail: failed, done: succeeded, process: purging.
        :type Status: str
        :param PurgeType: Purge type. url: URL purge; path: directory purge.
        :type PurgeType: str
        :param FlushType: Resource purge method. flush: purges updated resources, delete: purges all resources.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PurgeUrlsCacheRequest(AbstractModel):
    """PurgeUrlsCache request structure.

    """

    def __init__(self):
        """
        :param Urls: List of URLs to be purged. The protocol header must be included.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PurgeUrlsCacheResponse(AbstractModel):
    """PurgeUrlsCache response structure.

    """

    def __init__(self):
        """
        :param TaskId: Purge task ID. The first ten digits are the UTC time when the task is submitted.
        :type TaskId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Quota(AbstractModel):
    """Purge usage and quota

    """

    def __init__(self):
        """
        :param Batch: Quota limit for one batch submission request.
        :type Batch: int
        :param Total: Daily submission quota limit.
        :type Total: int
        :param Available: Remaining daily submission quota.
        :type Available: int
        """
        self.Batch = None
        self.Total = None
        self.Available = None


    def _deserialize(self, params):
        self.Batch = params.get("Batch")
        self.Total = params.get("Total")
        self.Available = params.get("Available")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResourceData(AbstractModel):
    """Query object and its access details

    """

    def __init__(self):
        """
        :param Resource: Resource name, which is categorized as follows based on different query conditions:
Specific domain name: indicates the details of the specific domain name
multiDomains: indicates aggregated details of multiple domain names
Project ID: displays the ID of the specified project to be queried
all: details at the account level
        :type Resource: str
        :param EcdnData: Data details of resource
        :type EcdnData: :class:`tencentcloud.ecdn.v20191012.models.EcdnData`
        """
        self.Resource = None
        self.EcdnData = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("EcdnData") is not None:
            self.EcdnData = EcdnData()
            self.EcdnData._deserialize(params.get("EcdnData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResponseHeader(AbstractModel):
    """Custom response header configuration.

    """

    def __init__(self):
        """
        :param Switch: Custom response header switch. Valid values: on, off.
        :type Switch: str
        :param HeaderRules: Custom response header rule array.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ServerCert(AbstractModel):
    """HTTPS server certificate configuration.

    """

    def __init__(self):
        """
        :param CertId: Server certificate ID, which is required if the certificate is a Tencent Cloud-hosted certificate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertId: str
        :param CertName: Server certificate name, which is required if the certificate is a Tencent Cloud-hosted certificate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CertName: str
        :param Certificate: Server certificate information, which is required when uploading your own certificate and must contain complete certificate chain information.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Certificate: str
        :param PrivateKey: Server key information, which is required when uploading your own certificate.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PrivateKey: str
        :param ExpireTime: Certificate expiration time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: str
        :param DeployTime: Certificate issuance time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeployTime: str
        :param Message: Certificate remarks.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Sort(AbstractModel):
    """Sorting criteria for query results.

    """

    def __init__(self):
        """
        :param Key: Sort by field. Valid values:
createTime: domain name creation time
certExpireTime: certificate expiration time
        :type Key: str
        :param Sequence: asc/desc. Default value: desc.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StartEcdnDomainRequest(AbstractModel):
    """StartEcdnDomain request structure.

    """

    def __init__(self):
        """
        :param Domain: Domain name to be enabled.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StartEcdnDomainResponse(AbstractModel):
    """StartEcdnDomain response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StopEcdnDomainRequest(AbstractModel):
    """StopEcdnDomain request structure.

    """

    def __init__(self):
        """
        :param Domain: Domain name to be disabled.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StopEcdnDomainResponse(AbstractModel):
    """StopEcdnDomain response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Tag(AbstractModel):
    """Tag key and tag value.

    """

    def __init__(self):
        """
        :param TagKey: Tag key.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type TagKey: str
        :param TagValue: Tag value.
Note: this field may return `null`, indicating that no valid value is obtained.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TimestampData(AbstractModel):
    """Timestamp and its corresponding value

    """

    def __init__(self):
        """
        :param Time: Statistical time point in forward rounding mode
Taking the 5-minute granularity as an example, 13:35:00 indicates that the statistical interval is between 13:35:00 and 13:39:59
        :type Time: str
        :param Value: Data value
        :type Value: list of float
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateDomainConfigRequest(AbstractModel):
    """UpdateDomainConfig request structure.

    """

    def __init__(self):
        """
        :param Domain: Domain name.
        :type Domain: str
        :param Origin: Origin server configuration.
        :type Origin: :class:`tencentcloud.ecdn.v20191012.models.Origin`
        :param ProjectId: Project ID.
        :type ProjectId: int
        :param IpFilter: IP blocklist/allowlist configuration.
        :type IpFilter: :class:`tencentcloud.ecdn.v20191012.models.IpFilter`
        :param IpFreqLimit: IP access limit configuration.
        :type IpFreqLimit: :class:`tencentcloud.ecdn.v20191012.models.IpFreqLimit`
        :param ResponseHeader: Origin server response header configuration.
        :type ResponseHeader: :class:`tencentcloud.ecdn.v20191012.models.ResponseHeader`
        :param CacheKey: Node caching configuration.
        :type CacheKey: :class:`tencentcloud.ecdn.v20191012.models.CacheKey`
        :param Cache: Caching rule configuration.
        :type Cache: :class:`tencentcloud.ecdn.v20191012.models.Cache`
        :param Https: HTTPS configuration.
        :type Https: :class:`tencentcloud.ecdn.v20191012.models.Https`
        :param ForceRedirect: Forced access protocol redirection configuration.
        :type ForceRedirect: :class:`tencentcloud.ecdn.v20191012.models.ForceRedirect`
        :param Area: Domain name acceleration region. Valid values: mainland (acceleration in Mainland China), overseas (acceleration outside Mainland China), global (global acceleration).
        :type Area: str
        :param WebSocket: WebSocket configuration.
        :type WebSocket: :class:`tencentcloud.ecdn.v20191012.models.WebSocket`
        """
        self.Domain = None
        self.Origin = None
        self.ProjectId = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.ResponseHeader = None
        self.CacheKey = None
        self.Cache = None
        self.Https = None
        self.ForceRedirect = None
        self.Area = None
        self.WebSocket = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
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
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        self.Area = params.get("Area")
        if params.get("WebSocket") is not None:
            self.WebSocket = WebSocket()
            self.WebSocket._deserialize(params.get("WebSocket"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateDomainConfigResponse(AbstractModel):
    """UpdateDomainConfig response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class WebSocket(AbstractModel):
    """WebSocket configuration.

    """

    def __init__(self):
        """
        :param Switch: WebSocket configuration switch, which can be `on` or `off`.
        :type Switch: str
        :param Timeout: Sets timeout period in seconds. Maximum value: 65
Note: This field may return `null`, indicating that no valid values can be obtained.
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        