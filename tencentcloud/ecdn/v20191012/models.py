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
        """
        :param Domain: Domain name.\n        :type Domain: str\n        :param Origin: Origin server configuration.\n        :type Origin: :class:`tencentcloud.ecdn.v20191012.models.Origin`\n        :param Area: Domain name acceleration region. Valid values: mainland (acceleration in Mainland China), overseas (acceleration outside Mainland China), global (global acceleration).\n        :type Area: str\n        :param ProjectId: Project ID. Default value: 0.\n        :type ProjectId: int\n        :param IpFilter: IP block/allowlist configuration.\n        :type IpFilter: :class:`tencentcloud.ecdn.v20191012.models.IpFilter`\n        :param IpFreqLimit: IP access limit configuration.\n        :type IpFreqLimit: :class:`tencentcloud.ecdn.v20191012.models.IpFreqLimit`\n        :param ResponseHeader: Origin server response header configuration.\n        :type ResponseHeader: :class:`tencentcloud.ecdn.v20191012.models.ResponseHeader`\n        :param CacheKey: Node caching configuration.\n        :type CacheKey: :class:`tencentcloud.ecdn.v20191012.models.CacheKey`\n        :param Cache: Caching rule configuration.\n        :type Cache: :class:`tencentcloud.ecdn.v20191012.models.Cache`\n        :param Https: HTTPS configuration.\n        :type Https: :class:`tencentcloud.ecdn.v20191012.models.Https`\n        :param ForceRedirect: Forced access protocol redirection configuration.\n        :type ForceRedirect: :class:`tencentcloud.ecdn.v20191012.models.ForceRedirect`\n        :param Tag: Tag bound to a domain name.\n        :type Tag: list of Tag\n        :param WebSocket: WebSocket configuration.\n        :type WebSocket: :class:`tencentcloud.ecdn.v20191012.models.WebSocket`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddEcdnDomainResponse(AbstractModel):
    """AddEcdnDomain response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Cache(AbstractModel):
    """Simple edition of cache configuration, which does not support setting a caching rule for scenarios where the `max-age` is not returned from the origin server.

    """

    def __init__(self):
        """
        :param CacheRules: Caching configuration rule array.\n        :type CacheRules: list of CacheRule\n        :param FollowOrigin: Whether to follow the `Cache-Control: max-age` configuration on the origin server (this feature is only available to users on the allowlist).
on: enable
off: disable
If it is enabled, resources that do not match `CacheRules` will be cached on node according to the `max-age` value returned by the origin server, while resources that match `CacheRules` will be cached on node according to the cache expiration time set in `CacheRules`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FollowOrigin: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheKey(AbstractModel):
    """Caching configuration.

    """

    def __init__(self):
        """
        :param FullUrlCache: Whether to enable full path cache. Valid values: on, off.\n        :type FullUrlCache: str\n        """
        self.FullUrlCache = None


    def _deserialize(self, params):
        self.FullUrlCache = params.get("FullUrlCache")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheRule(AbstractModel):
    """Caching configuration rule.

    """

    def __init__(self):
        """
        :param CacheType: Cache type. Valid values: all (all files), file (extension type), directory (directory), path (full path), index (homepage).\n        :type CacheType: str\n        :param CacheContents: Cached content list.\n        :type CacheContents: list of str\n        :param CacheTime: Cache time in seconds.\n        :type CacheTime: int\n        """
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
        


class ClientCert(AbstractModel):
    """HTTPS client certificate configuration.

    """

    def __init__(self):
        """
        :param Certificate: Client certificate in PEM format.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Certificate: str\n        :param CertName: Client certificate name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CertName: str\n        :param ExpireTime: Certificate expiration time.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ExpireTime: str\n        :param DeployTime: Certificate issuance time.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DeployTime: str\n        """
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
        


class DeleteEcdnDomainRequest(AbstractModel):
    """DeleteEcdnDomain request structure.

    """

    def __init__(self):
        """
        :param Domain: Domain name to be deleted.\n        :type Domain: str\n        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEcdnDomainResponse(AbstractModel):
    """DeleteEcdnDomain response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDomainsConfigRequest(AbstractModel):
    """DescribeDomainsConfig request structure.

    """

    def __init__(self):
        """
        :param Offset: Pagination offset address. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of domain names per page. Default value: 100.\n        :type Limit: int\n        :param Filters: Query filter.\n        :type Filters: list of DomainFilter\n        :param Sort: Query result sorting rule.\n        :type Sort: :class:`tencentcloud.ecdn.v20191012.models.Sort`\n        """
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
        """
        :param Domains: Domain name list.\n        :type Domains: list of DomainDetailInfo\n        :param TotalCount: Number of matched domain names. This is used for paginated query.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeDomainsRequest(AbstractModel):
    """DescribeDomains request structure.

    """

    def __init__(self):
        """
        :param Offset: Pagination offset address. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of domain names per page. Default value: 100. Maximum value: 1000.\n        :type Limit: int\n        :param Filters: Query filter.\n        :type Filters: list of DomainFilter\n        """
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
        """
        :param Domains: Domain name information list.\n        :type Domains: list of DomainBriefInfo\n        :param TotalCount: Total number of domain names.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeEcdnDomainLogsRequest(AbstractModel):
    """DescribeEcdnDomainLogs request structure.

    """

    def __init__(self):
        """
        :param Domain: Domain name to be queried.\n        :type Domain: str\n        :param StartTime: Log start time, such as 2019-10-01 00:00:00\n        :type StartTime: str\n        :param EndTime: Log end time, such as 2019-10-02 00:00:00. Only logs for the last 30 days can be queried.\n        :type EndTime: str\n        :param Offset: Pagination offset for log link list. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of log links per page. Default value: 100. Maximum value: 1000.\n        :type Limit: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEcdnDomainLogsResponse(AbstractModel):
    """DescribeEcdnDomainLogs response structure.

    """

    def __init__(self):
        """
        :param DomainLogs: Log link list.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DomainLogs: list of DomainLogs\n        :param TotalCount: Total number of log links.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeEcdnDomainStatisticsRequest(AbstractModel):
    """DescribeEcdnDomainStatistics request structure.

    """

    def __init__(self):
        """
        :param StartTime: Query start time, such as 2019-12-13 00:00:00.
The time span cannot exceed 90 days.\n        :type StartTime: str\n        :param EndTime: Query end time, such as 2019-12-13 23:59:59.
The time span cannot exceed 90 days.\n        :type EndTime: str\n        :param Metrics: Statistical metric names:
flux: traffic (in bytes)
bandwidth: bandwidth (in bps)
request: number of requests\n        :type Metrics: list of str\n        :param Domains: Specifies the list of domain names to be queried\n        :type Domains: list of str\n        :param Projects: Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)
If no domain name is entered, the specified project will be queried; otherwise, the domain name will prevail\n        :type Projects: list of int\n        :param Offset: Pagination offset. Default value: 0.\n        :type Offset: int\n        :param Limit: Number of entries per page. Default value: 1000. Maximum value: 3,000.\n        :type Limit: int\n        :param Area: Statistical areas:
mainland: Chinese mainland
oversea: outside the Chinese mainland
global: global
Default value: global\n        :type Area: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEcdnDomainStatisticsResponse(AbstractModel):
    """DescribeEcdnDomainStatistics response structure.

    """

    def __init__(self):
        """
        :param Data: Domain name data\n        :type Data: list of DomainData\n        :param TotalCount: Quantity\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeEcdnStatisticsRequest(AbstractModel):
    """DescribeEcdnStatistics request structure.

    """

    def __init__(self):
        """
        :param StartTime: Query start time, such as 2019-12-13 00:00:00\n        :type StartTime: str\n        :param EndTime: Query end time, such as 2019-12-13 23:59:59\n        :type EndTime: str\n        :param Metrics: Specifies the query metric, which can be:
flux: traffic (in bytes)
bandwidth: bandwidth (in bps)
request: number of requests
2xx: returns the number of 2xx status codes or details of status codes starting with 2
3xx: returns the number of 3xx status codes or details of status codes starting with 3
4xx: returns the number of 4xx status codes or details of status codes starting with 4
5xx: returns the number of 5xx status codes or details of status codes starting with 5\n        :type Metrics: list of str\n        :param Interval: Time granularity, which can be:
1 day	 1, 5, 15, 30, 60, 120, 240, 1440 
2-3 days 15, 30, 60, 120, 240, 1440
4-7 days 30, 60, 120, 240, 1440
8-90 days	 60, 120, 240, 1440\n        :type Interval: int\n        :param Domains: Specifies the list of domain names to be queried

Up to 30 acceleration domain names can be queried at a time.\n        :type Domains: list of str\n        :param Projects: Specifies the project ID to be queried, which can be viewed [here](https://console.cloud.tencent.com/project)
If no domain name is entered, the specified project will be queried; otherwise, the domain name will prevail\n        :type Projects: list of int\n        :param Area: Statistical areas:
mainland: Chinese mainland
oversea: outside the Chinese mainland
global: global
Default value: global\n        :type Area: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEcdnStatisticsResponse(AbstractModel):
    """DescribeEcdnStatistics response structure.

    """

    def __init__(self):
        """
        :param Data: Returned data details of the specified conditional query\n        :type Data: list of ResourceData\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribeIpStatusRequest(AbstractModel):
    """DescribeIpStatus request structure.

    """

    def __init__(self):
        """
        :param Domain: Acceleration domain name\n        :type Domain: str\n        :param Area: Target region of the query:
mainland: nodes in Mainland China
overseas: nodes outside Mainland China
global: global nodes\n        :type Area: str\n        """
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
        


class DescribeIpStatusResponse(AbstractModel):
    """DescribeIpStatus response structure.

    """

    def __init__(self):
        """
        :param Ips: Node list\n        :type Ips: list of IpStatus\n        :param TotalCount: Total number of nodes\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribePurgeQuotaRequest(AbstractModel):
    """DescribePurgeQuota request structure.

    """


class DescribePurgeQuotaResponse(AbstractModel):
    """DescribePurgeQuota response structure.

    """

    def __init__(self):
        """
        :param UrlPurge: URL purge usage and quota.\n        :type UrlPurge: :class:`tencentcloud.ecdn.v20191012.models.Quota`\n        :param PathPurge: Directory purge usage and quota.\n        :type PathPurge: :class:`tencentcloud.ecdn.v20191012.models.Quota`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DescribePurgeTasksRequest(AbstractModel):
    """DescribePurgeTasks request structure.

    """

    def __init__(self):
        """
        :param PurgeType: Purge type to be queried. url: query URL purge records; path: query directory purge records.\n        :type PurgeType: str\n        :param StartTime: Start time, such as 2018-08-08 00:00:00\n        :type StartTime: str\n        :param EndTime: End time, such as 2018-08-08 23:59:59\n        :type EndTime: str\n        :param TaskId: Task ID returned during submission. Either `TaskId` or start time must be specified for a query.\n        :type TaskId: str\n        :param Offset: Pagination offset. Default value: 0 (starting from entry 0).\n        :type Offset: int\n        :param Limit: Pagination limit. Default value: 20.\n        :type Limit: int\n        :param Keyword: Query keyword. Please enter a domain name or full URL beginning with `http(s)://`.\n        :type Keyword: str\n        :param Status: Specified task status to be queried. fail: failed, done: succeeded, process: purging.\n        :type Status: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePurgeTasksResponse(AbstractModel):
    """DescribePurgeTasks response structure.

    """

    def __init__(self):
        """
        :param PurgeLogs: Purge history.\n        :type PurgeLogs: list of PurgeTask\n        :param TotalCount: Total number of tasks, which is used for pagination.\n        :type TotalCount: int\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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


class DetailData(AbstractModel):
    """Data structure of sorted data

    """

    def __init__(self):
        """
        :param Name: Data type name\n        :type Name: str\n        :param Value: Data value\n        :type Value: float\n        """
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
        


class DomainBriefInfo(AbstractModel):
    """Basic information of a CDN domain name.

    """

    def __init__(self):
        """
        :param ResourceId: Domain name ID.\n        :type ResourceId: str\n        :param AppId: Tencent Cloud account ID.\n        :type AppId: int\n        :param Domain: CDN acceleration domain name.\n        :type Domain: str\n        :param Cname: Domain name CNAME.\n        :type Cname: str\n        :param Status: Domain name status. Valid values: pending (reviewing), rejected (rejected), processing (deploying after approval), online (enabled), offline (disabled), deleted (deleted).\n        :type Status: str\n        :param ProjectId: Project ID.\n        :type ProjectId: int\n        :param CreateTime: Domain name creation time.\n        :type CreateTime: str\n        :param UpdateTime: Domain name update time.\n        :type UpdateTime: str\n        :param Origin: Origin server configuration details.\n        :type Origin: :class:`tencentcloud.ecdn.v20191012.models.Origin`\n        :param Disable: Domain name blockage status. Valid values: normal (normal), overdue (service is suspended due to arrears), quota (trial traffic package is used up), malicious (malicious user), ddos (DDoS attack), idle (no traffic), unlicensed (no ICP filing), capping (bandwidth cap reached), readonly (read-only)\n        :type Disable: str\n        :param Area: Acceleration region. Valid values: mainland, oversea, global.\n        :type Area: str\n        :param Readonly: Domain name lock status. normal: not locked; global: globally locked\n        :type Readonly: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainData(AbstractModel):
    """Data structure of sorted data

    """

    def __init__(self):
        """
        :param Resource: Domain name\n        :type Resource: str\n        :param DetailData: Result details.\n        :type DetailData: list of DetailData\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainDetailInfo(AbstractModel):
    """Detailed configuration information of ECDN domain name.

    """

    def __init__(self):
        """
        :param ResourceId: Domain name ID.\n        :type ResourceId: str\n        :param AppId: Tencent Cloud account ID.\n        :type AppId: int\n        :param Domain: Acceleration domain name.\n        :type Domain: str\n        :param Cname: Domain name CNAME.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Cname: str\n        :param Status: Domain name status. Valid values: pending (reviewing), rejected (rejected), processing (deploying after approval), online (enabled), offline (disabled), deleted (deleted).\n        :type Status: str\n        :param ProjectId: Project ID.\n        :type ProjectId: int\n        :param CreateTime: Domain name creation time.\n        :type CreateTime: str\n        :param UpdateTime: Domain name update time.\n        :type UpdateTime: str\n        :param Origin: Origin server configuration.\n        :type Origin: :class:`tencentcloud.ecdn.v20191012.models.Origin`\n        :param IpFilter: IP blocklist/allowlist configuration.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IpFilter: :class:`tencentcloud.ecdn.v20191012.models.IpFilter`\n        :param IpFreqLimit: IP access limit configuration.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IpFreqLimit: :class:`tencentcloud.ecdn.v20191012.models.IpFreqLimit`\n        :param ResponseHeader: Origin server response header configuration.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ResponseHeader: :class:`tencentcloud.ecdn.v20191012.models.ResponseHeader`\n        :param CacheKey: Node caching configuration.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CacheKey: :class:`tencentcloud.ecdn.v20191012.models.CacheKey`\n        :param Cache: Caching rule configuration.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Cache: :class:`tencentcloud.ecdn.v20191012.models.Cache`\n        :param Https: HTTPS configuration.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Https: :class:`tencentcloud.ecdn.v20191012.models.Https`\n        :param Disable: Domain name blockage status. Valid values: normal (normal), overdue (service is suspended due to arrears), quota (trial traffic package is used up), malicious (malicious user), ddos (DDoS attack), idle (no traffic), unlicensed (no ICP filing), capping (bandwidth cap reached), readonly (read-only).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Disable: str\n        :param ForceRedirect: Forced access protocol redirection configuration.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ForceRedirect: :class:`tencentcloud.ecdn.v20191012.models.ForceRedirect`\n        :param Area: Acceleration region. Valid values: mainland, overseas, global.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Area: str\n        :param Readonly: Domain name lock status. normal: not locked; global: globally locked.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Readonly: str\n        :param Tag: Domain name tag
Note: This field may return `null`, indicating that no valid value can be obtained.\n        :type Tag: list of Tag\n        :param WebSocket: WebSocket configuration.
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type WebSocket: :class:`tencentcloud.ecdn.v20191012.models.WebSocket`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
- area: acceleration region. Valid values: mainland, overseas, global.\n        :type Name: str\n        :param Value: Filter field value.\n        :type Value: list of str\n        :param Fuzzy: Whether to enable fuzzy query, which is supported only for filter fields `origin` and `domain`.\n        :type Fuzzy: bool\n        """
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
        


class DomainLogs(AbstractModel):
    """Domain name log information.

    """

    def __init__(self):
        """
        :param StartTime: Log start time.\n        :type StartTime: str\n        :param EndTime: Log end time.\n        :type EndTime: str\n        :param LogPath: Log download path.\n        :type LogPath: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EcdnData(AbstractModel):
    """Detailed access data type

    """

    def __init__(self):
        """
        :param Metrics: Queries the specified metric. Valid values: Bandwidth, Flux, Request, Delay, status code, LogBandwidth, LogFlux, LogRequest\n        :type Metrics: list of str\n        :param DetailData: Detailed data collection\n        :type DetailData: list of TimestampData\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForceRedirect(AbstractModel):
    """Forced access protocol redirection configuration.

    """

    def __init__(self):
        """
        :param Switch: Forced access protocol redirection configuration switch. Valid values: on, off.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Switch: str\n        :param RedirectType: Access protocol type for forced redirection. Valid values: http (forced redirection to HTTP protocol), https (forced redirection to HTTPS protocol).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RedirectType: str\n        :param RedirectStatusCode: HTTP status code returned when forced redirection is enabled. Valid values: 301, 302.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RedirectStatusCode: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Hsts(AbstractModel):
    """HSTS configuration.

    """

    def __init__(self):
        """
        :param Switch: Whether to enable. Valid values: on, off.\n        :type Switch: str\n        :param MaxAge: `MaxAge` value.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MaxAge: int\n        :param IncludeSubDomains: Whether to include subdomain names. Valid values: on, off.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IncludeSubDomains: str\n        """
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
    """Path-specific HTTP header setting rule.

    """

    def __init__(self):
        """
        :param HeaderMode: HTTP header setting method. Valid values: add (add header), set (set header), del (delete header).
Request header currently does not support `set`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type HeaderMode: str\n        :param HeaderName: HTTP header name.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type HeaderName: str\n        :param HeaderValue: HTTP header value, which is optional when it is `del`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type HeaderValue: str\n        :param RuleType: Type of effective URL path rule. Valid values: all (all paths), file (file extension), directory (directory), path (absolute path).
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RuleType: str\n        :param RulePaths: URL path or file type list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RulePaths: list of str\n        """
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
        


class Https(AbstractModel):
    """HTTPS configuration of domain name.

    """

    def __init__(self):
        """
        :param Switch: HTTPS configuration switch. Valid values: on, off. If the domain name with HTTPS configuration enabled is being deployed, this switch will be `off`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Switch: str\n        :param Http2: Whether to enable HTTP2. Valid values: on, off.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Http2: str\n        :param OcspStapling: Whether to enable the OCSP feature. Valid values: on, off.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OcspStapling: str\n        :param VerifyClient: Whether to enable the client certificate verification feature. Valid values: on, off. The client certificate information must be uploaded if this feature is enabled.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VerifyClient: str\n        :param CertInfo: Server certificate configuration information.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CertInfo: :class:`tencentcloud.ecdn.v20191012.models.ServerCert`\n        :param ClientCertInfo: Client certificate configuration information.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ClientCertInfo: :class:`tencentcloud.ecdn.v20191012.models.ClientCert`\n        :param Spdy: Whether to enable SPDY. Valid values: on, off.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Spdy: str\n        :param SslStatus: HTTPS certificate deployment status. Valid values: closed (disabled), deploying (deploying), deployed (deployment succeeded), failed (deployment failed). This parameter cannot be used as an input parameter.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SslStatus: str\n        :param Hsts: HSTS configuration
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Hsts: :class:`tencentcloud.ecdn.v20191012.models.Hsts`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpFilter(AbstractModel):
    """IP blocklist/allowlist.

    """

    def __init__(self):
        """
        :param Switch: IP blocklist/allowlist switch. Valid values: on, off.\n        :type Switch: str\n        :param FilterType: IP blocklist/allowlist type. Valid values: whitelist, blacklist.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FilterType: str\n        :param Filters: IP blocklist/allowlist list.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Filters: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpFreqLimit(AbstractModel):
    """IP access limit configuration.

    """

    def __init__(self):
        """
        :param Switch: IP access limit switch. Valid values: on, off.\n        :type Switch: str\n        :param Qps: Number of requests per second.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Qps: int\n        """
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
        """
        :param Ip: Node IP\n        :type Ip: str\n        :param District: Node region\n        :type District: str\n        :param Isp: Node ISP\n        :type Isp: str\n        :param City: Node city\n        :type City: str\n        :param Status: Node status
online: the node is online and scheduling normally
offline: the node is offline\n        :type Status: str\n        :param CreateTime: Node IP creation time\n        :type CreateTime: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Origin(AbstractModel):
    """Origin server configuration.

    """

    def __init__(self):
        """
        :param Origins: Primary origin server list. IP and the domain name of the origin server cannot be entered at the same time. Configure origin server port in the format of ["origin1:port1", "origin2:port2"]. Configure origin-pull weight in the format of ["origin1::weight1", "origin2::weight2"]. Configure both port and weight in the format of ["origin1:port1:weight1", "origin2:port2:weight2"]. Valid range of weight value: 0 - 100.\n        :type Origins: list of str\n        :param OriginType: Primary origin server type. Valid values: domain (domain name origin server), ip (IP origin server).
This is required when setting `Origins`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type OriginType: str\n        :param ServerName: Host header value during origin-pull.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ServerName: str\n        :param OriginPullProtocol: Origin-pull protocol type. Valid values: http (forced HTTP origin-pull), follow (protocol follow), https (HTTPS origin-pull).
If this parameter is left empty, HTTP origin-pull will be used by default.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type OriginPullProtocol: str\n        :param BackupOrigins: Secondary origin server list.\n        :type BackupOrigins: list of str\n        :param BackupOriginType: Secondary origin server type, which is the same as `OriginType`.
This is required when setting `BackupOrigins`.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type BackupOriginType: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurgePathCacheRequest(AbstractModel):
    """PurgePathCache request structure.

    """

    def __init__(self):
        """
        :param Paths: List of directories to be purged. The protocol header must be included.\n        :type Paths: list of str\n        :param FlushType: Purge type. flush: purges updated resources, delete: purges all resources.\n        :type FlushType: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurgePathCacheResponse(AbstractModel):
    """PurgePathCache response structure.

    """

    def __init__(self):
        """
        :param TaskId: Purge task ID. The first ten digits are the UTC time when the task is submitted.\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class PurgeTask(AbstractModel):
    """Purge task log details.

    """

    def __init__(self):
        """
        :param TaskId: Purge task ID.\n        :type TaskId: str\n        :param Url: Purged URL.\n        :type Url: str\n        :param Status: Purge task status. fail: failed, done: succeeded, process: purging.\n        :type Status: str\n        :param PurgeType: Purge type. url: URL purge; path: directory purge.\n        :type PurgeType: str\n        :param FlushType: Resource purge method. flush: purges updated resources, delete: purges all resources.\n        :type FlushType: str\n        :param CreateTime: Purge task submission time\n        :type CreateTime: str\n        """
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
        """
        :param Urls: List of URLs to be purged. The protocol header must be included.\n        :type Urls: list of str\n        """
        self.Urls = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
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
        """
        :param TaskId: Purge task ID. The first ten digits are the UTC time when the task is submitted.\n        :type TaskId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class Quota(AbstractModel):
    """Purge usage and quota

    """

    def __init__(self):
        """
        :param Batch: Quota limit for one batch submission request.\n        :type Batch: int\n        :param Total: Daily submission quota limit.\n        :type Total: int\n        :param Available: Remaining daily submission quota.\n        :type Available: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceData(AbstractModel):
    """Query object and its access details

    """

    def __init__(self):
        """
        :param Resource: Resource name, which is categorized as follows based on different query conditions:
Specific domain name: indicates the details of the specific domain name
multiDomains: indicates aggregated details of multiple domain names
Project ID: displays the ID of the specified project to be queried
all: details at the account level\n        :type Resource: str\n        :param EcdnData: Data details of resource\n        :type EcdnData: :class:`tencentcloud.ecdn.v20191012.models.EcdnData`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResponseHeader(AbstractModel):
    """Custom response header configuration.

    """

    def __init__(self):
        """
        :param Switch: Custom response header switch. Valid values: on, off.\n        :type Switch: str\n        :param HeaderRules: Custom response header rule array.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type HeaderRules: list of HttpHeaderPathRule\n        """
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
        


class ServerCert(AbstractModel):
    """HTTPS server certificate configuration.

    """

    def __init__(self):
        """
        :param CertId: Server certificate ID, which is required if the certificate is a Tencent Cloud-hosted certificate.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CertId: str\n        :param CertName: Server certificate name, which is required if the certificate is a Tencent Cloud-hosted certificate.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CertName: str\n        :param Certificate: Server certificate information, which is required when uploading your own certificate and must contain complete certificate chain information.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Certificate: str\n        :param PrivateKey: Server key information, which is required when uploading your own certificate.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PrivateKey: str\n        :param ExpireTime: Certificate expiration time.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ExpireTime: str\n        :param DeployTime: Certificate issuance time.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DeployTime: str\n        :param Message: Certificate remarks.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Message: str\n        """
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
        


class Sort(AbstractModel):
    """Sorting criteria for query results.

    """

    def __init__(self):
        """
        :param Key: Sort by field. Valid values:
createTime: domain name creation time
certExpireTime: certificate expiration time\n        :type Key: str\n        :param Sequence: asc/desc. Default value: desc.\n        :type Sequence: str\n        """
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
        


class StartEcdnDomainRequest(AbstractModel):
    """StartEcdnDomain request structure.

    """

    def __init__(self):
        """
        :param Domain: Domain name to be enabled.\n        :type Domain: str\n        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartEcdnDomainResponse(AbstractModel):
    """StartEcdnDomain response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopEcdnDomainRequest(AbstractModel):
    """StopEcdnDomain request structure.

    """

    def __init__(self):
        """
        :param Domain: Domain name to be disabled.\n        :type Domain: str\n        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopEcdnDomainResponse(AbstractModel):
    """StopEcdnDomain response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """Tag key and tag value.

    """

    def __init__(self):
        """
        :param TagKey: Tag key.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type TagKey: str\n        :param TagValue: Tag value.
Note: this field may return `null`, indicating that no valid value is obtained.\n        :type TagValue: str\n        """
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
        """
        :param Time: Statistical time point in forward rounding mode
Taking the 5-minute granularity as an example, 13:35:00 indicates that the statistical interval is between 13:35:00 and 13:39:59\n        :type Time: str\n        :param Value: Data value\n        :type Value: list of float\n        """
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
        


class UpdateDomainConfigRequest(AbstractModel):
    """UpdateDomainConfig request structure.

    """

    def __init__(self):
        """
        :param Domain: Domain name.\n        :type Domain: str\n        :param Origin: Origin server configuration.\n        :type Origin: :class:`tencentcloud.ecdn.v20191012.models.Origin`\n        :param ProjectId: Project ID.\n        :type ProjectId: int\n        :param IpFilter: IP blocklist/allowlist configuration.\n        :type IpFilter: :class:`tencentcloud.ecdn.v20191012.models.IpFilter`\n        :param IpFreqLimit: IP access limit configuration.\n        :type IpFreqLimit: :class:`tencentcloud.ecdn.v20191012.models.IpFreqLimit`\n        :param ResponseHeader: Origin server response header configuration.\n        :type ResponseHeader: :class:`tencentcloud.ecdn.v20191012.models.ResponseHeader`\n        :param CacheKey: Node caching configuration.\n        :type CacheKey: :class:`tencentcloud.ecdn.v20191012.models.CacheKey`\n        :param Cache: Caching rule configuration.\n        :type Cache: :class:`tencentcloud.ecdn.v20191012.models.Cache`\n        :param Https: HTTPS configuration.\n        :type Https: :class:`tencentcloud.ecdn.v20191012.models.Https`\n        :param ForceRedirect: Forced access protocol redirection configuration.\n        :type ForceRedirect: :class:`tencentcloud.ecdn.v20191012.models.ForceRedirect`\n        :param Area: Domain name acceleration region. Valid values: mainland (acceleration in Mainland China), overseas (acceleration outside Mainland China), global (global acceleration).\n        :type Area: str\n        :param WebSocket: WebSocket configuration.\n        :type WebSocket: :class:`tencentcloud.ecdn.v20191012.models.WebSocket`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDomainConfigResponse(AbstractModel):
    """UpdateDomainConfig response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class WebSocket(AbstractModel):
    """WebSocket configuration.

    """

    def __init__(self):
        """
        :param Switch: WebSocket configuration switch, which can be `on` or `off`.\n        :type Switch: str\n        :param Timeout: Sets timeout period in seconds. Maximum value: 65
Note: This field may return `null`, indicating that no valid values can be obtained.\n        :type Timeout: int\n        """
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
        