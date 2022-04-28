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
`min`: 1-minute granularity. The query period cannot exceed 24 hours.
`5min`: 5-minute granularity. The query range cannot exceed 31 days.
`hour`: 1-hour granularity. The query period cannot exceed 31 days.
`day`: 1-day granularity. The query period cannot exceed 31 days.

Querying 1-minute granularity data is not supported if the `Area` field is `overseas`.
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
        :param Domains: Queries the information of specified domain names
Specifies a domain name to query
Specifies multiple domain names to query (30 at most at a time)
Queries all Specifies an account to query all domain names
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
        :param Layer: If this parameter is `middle` or left empty, prefetch will be performed onto the intermediate node.
Note: resources prefetched outside the Chinese mainland will be cached to CDN nodes outside the Chinese mainland and the traffic generated will incur costs.
        :type Layer: str
        :param ParseM3U8: Whether to recursively resolve the M3U8 index file and prefetch the TS shards in it.
Notes:
1. This feature requires that the M3U8 index file can be directly requested and obtained.
2. In the M3U8 index file, currently only the TS shards at the first to the third level can be recursively resolved.
3. Prefetching the TS shards obtained through recursive resolution consumes the daily prefetch quota. If the usage exceeds the quota, the feature will be disabled and TS shards will not be prefetched.
        :type ParseM3U8: bool
        :param DisableRange: Specifies whether to disable Range GETs.
Notes:
This feature is in beta test.
        :type DisableRange: bool
        """
        self.Urls = None
        self.UserAgent = None
        self.Area = None
        self.Layer = None
        self.ParseM3U8 = None
        self.DisableRange = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
        self.UserAgent = params.get("UserAgent")
        self.Area = params.get("Area")
        self.Layer = params.get("Layer")
        self.ParseM3U8 = params.get("ParseM3U8")
        self.DisableRange = params.get("DisableRange")
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
        :param Resource: Resource name, which is classified as follows based on different query filters:
A single domain name: queries domain name details by a domain name. The details of the domain name will be displayed when the passed parameter `detail` is `true` (the `detail` parameter defaults to `false`).
Multiple domain names: queries domain name details by multiple domain names. The aggregated details of the domain names will be displayed.
Project ID: queries domain name details by a project ID. The aggregated details of the domain names of the project will be displayed.
`all`: account-level data, which is aggregated details of all domain names of an account.
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
        