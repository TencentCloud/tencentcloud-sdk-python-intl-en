# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.cdn.v20180606 import models
from typing import Dict


class CdnClient(AbstractClient):
    _apiVersion = '2018-06-06'
    _endpoint = 'cdn.intl.tencentcloudapi.com'
    _service = 'cdn'

    async def AddCLSTopicDomains(
            self,
            request: models.AddCLSTopicDomainsRequest,
            opts: Dict = None,
    ) -> models.AddCLSTopicDomainsResponse:
        """
        This API is used to add one or more domains to a specified log topic.
        """
        
        kwargs = {}
        kwargs["action"] = "AddCLSTopicDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCLSTopicDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddCdnDomain(
            self,
            request: models.AddCdnDomainRequest,
            opts: Dict = None,
    ) -> models.AddCdnDomainResponse:
        """
        This API is used to add a CDN acceleration domain name. Up to 100 domain names can be added per minute.
        """
        
        kwargs = {}
        kwargs["action"] = "AddCdnDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCdnDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClsLogTopic(
            self,
            request: models.CreateClsLogTopicRequest,
            opts: Dict = None,
    ) -> models.CreateClsLogTopicResponse:
        """
        This API is used to create a log topic. Up to 10 log topics can be created under one logset.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClsLogTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClsLogTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateScdnFailedLogTask(
            self,
            request: models.CreateScdnFailedLogTaskRequest,
            opts: Dict = None,
    ) -> models.CreateScdnFailedLogTaskResponse:
        """
        This API is used to recreate a failed event log task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateScdnFailedLogTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateScdnFailedLogTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCdnDomain(
            self,
            request: models.DeleteCdnDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteCdnDomainResponse:
        """
        This API is used to delete a specified acceleration domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCdnDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCdnDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClsLogTopic(
            self,
            request: models.DeleteClsLogTopicRequest,
            opts: Dict = None,
    ) -> models.DeleteClsLogTopicResponse:
        """
        This API is used to delete a log topic. Note: when a log topic is deleted, all logs of the domain names bound to it will no longer be published to the topic, and the logs previously published to the topic will be deleted. This action will take effect within 5–15 minutes.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClsLogTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClsLogTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillingData(
            self,
            request: models.DescribeBillingDataRequest,
            opts: Dict = None,
    ) -> models.DescribeBillingDataResponse:
        """
        This API is used to query billing data details.
        Notes:
        Due to the impact of the billing and settlement methods, the data returned by the DescribeBillingData  has a certain delay. For hourly-billed customers, the expected delay is 3 to 5 hours. For monthly-billed customers, the expected delay is 4 to 28 hours. Before 4:00 AM  (UTC+8, excluding 4:00 AM), only data from two days prior can be queried; after 4:00 AM (including 4:00 AM), data from the previous day can be queried.
        If you have a strong requirement for data timeliness, it is recommended to use the DescribeCdnData.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillingData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillingDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCdnData(
            self,
            request: models.DescribeCdnDataRequest,
            opts: Dict = None,
    ) -> models.DescribeCdnDataResponse:
        """
        This API is used to query CDN real-time access monitoring data and supports the following metrics:

        + Traffic (in bytes)
        + Bandwidth (in bps)
        + Number of requests
        + Number of hit requests
        + Request hit rate (in %)
        + Hit traffic (in bytes)
        + Traffic hit rate (in %)
        + Aggregate list of 2xx status codes and the details of status codes starting with 2 (in entries)
        + Aggregate list of 3xx status codes and the details of status codes starting with 3 (in entries)
        + Aggregate list of 4xx status codes and the details of status codes starting with 4 (in entries)
        + Aggregate list of 5xx status codes and the details of status codes starting with 5 (in entries)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCdnData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCdnDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCdnDomainLogs(
            self,
            request: models.DescribeCdnDomainLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeCdnDomainLogsResponse:
        """
        This API is used to query the download link of an access log. You can use this API for access logs in the last 30 days either within or outside Mainland China.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCdnDomainLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCdnDomainLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCdnIp(
            self,
            request: models.DescribeCdnIpRequest,
            opts: Dict = None,
    ) -> models.DescribeCdnIpResponse:
        """
        This API is used to query CDN IP ownership.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCdnIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCdnIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCdnOriginIp(
            self,
            request: models.DescribeCdnOriginIpRequest,
            opts: Dict = None,
    ) -> models.DescribeCdnOriginIpResponse:
        """
        This API is used to query the IP information of CDN intermediate nodes. Note: this API will be deactivated soon and no longer be maintained. Please call `DescribeIpStatus` instead.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCdnOriginIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCdnOriginIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCertDomains(
            self,
            request: models.DescribeCertDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeCertDomainsResponse:
        """
        This API is used to verify a SSL certificate and obtain its domain names.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCertDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCertDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomains(
            self,
            request: models.DescribeDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainsResponse:
        """
        This API is used to query the basic configuration information of CDN acceleration domain names (inside and outside mainland China), including the project ID, service status, service type, creation time, and update time, etc.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainsConfig(
            self,
            request: models.DescribeDomainsConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainsConfigResponse:
        """
        This API is used to query the complete configuration information of CDN acceleration domain names (inside and outside mainland China).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainsConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainsConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIpStatus(
            self,
            request: models.DescribeIpStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeIpStatusResponse:
        """
        This API is used to query the IP details of edge nodes (available soon) and intermediate nodes. Note that there is a certain delay in data availability.

        >? If you have migrated your ECDN service to CDN, you can use the <a href="https://intl.cloud.tencent.com/document/api/228/41954?from_cn_redirect=1">corresponding CDN API</a>.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIpStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIpStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIpVisit(
            self,
            request: models.DescribeIpVisitRequest,
            opts: Dict = None,
    ) -> models.DescribeIpVisitResponse:
        """
        This API (DescribeIpVisit) is used to query the number of users who remain active for 5 minutes and the detailed number of daily active users.

        + Number of users who remain active for 5 minutes: Collects deduplicated statistics based on client IP addresses in the log with the 5-minute granularity.
        + Number of daily active users: Collects deduplicated statistics based on client IP addresses in the log with the 1-day granularity.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIpVisit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIpVisitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMapInfo(
            self,
            request: models.DescribeMapInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeMapInfoResponse:
        """
        This API (DescribeMapInfo) is used to query the IDs of districts or ISPs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMapInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMapInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOriginData(
            self,
            request: models.DescribeOriginDataRequest,
            opts: Dict = None,
    ) -> models.DescribeOriginDataResponse:
        """
        This API is used to query CDN real-time origin-pull monitoring data and supports the following metrics:

        + Origin-pull traffic (in bytes)
        + Origin-pull bandwidth (in bps)
        + Number of origin-pull requests
        + Number of failed origin-pull requests
        + Origin-pull failure rate (in % with two decimal digits)
        + Aggregate list of 2xx origin-pull status codes and the details of origin-pull status codes starting with 2 (in entries)
        + Aggregate list of 3xx origin-pull status codes and the details of origin-pull status codes starting with 3 (in entries)
        + Aggregate list of 4xx origin-pull status codes and the details of origin-pull status codes starting with 4 (in entries)
        + Aggregate list of 5xx origin-pull status codes and the details of origin-pull status codes starting with 5 (in entries)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOriginData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOriginDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePayType(
            self,
            request: models.DescribePayTypeRequest,
            opts: Dict = None,
    ) -> models.DescribePayTypeResponse:
        """
        This API (DescribePayType) is used to query billing information of the current account, such as billing mode and billing cycle.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePayType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePayTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePurgeQuota(
            self,
            request: models.DescribePurgeQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribePurgeQuotaResponse:
        """
        This API is used to query the purge usage quota and daily available usage for an account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePurgeQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePurgeQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePurgeTasks(
            self,
            request: models.DescribePurgeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribePurgeTasksResponse:
        """
        This API is used to query the record and progress of URL or directory purge tasks submitted via the `PurgePathCache` or `PurgeUrlsCache` APIs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePurgeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePurgeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePushQuota(
            self,
            request: models.DescribePushQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribePushQuotaResponse:
        """
        This API is used to query the prefetch quota and daily available usage.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePushQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePushQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePushTasks(
            self,
            request: models.DescribePushTasksRequest,
            opts: Dict = None,
    ) -> models.DescribePushTasksResponse:
        """
        This API is used to query the submission record and progress of prefetch tasks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePushTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePushTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReportData(
            self,
            request: models.DescribeReportDataRequest,
            opts: Dict = None,
    ) -> models.DescribeReportDataResponse:
        """
        This API is used to query the daily/weekly/monthly report data at domain name/project levels.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReportData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReportDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUrlViolations(
            self,
            request: models.DescribeUrlViolationsRequest,
            opts: Dict = None,
    ) -> models.DescribeUrlViolationsResponse:
        """
        This API is used to query the list of domain name URLs containing regulation-violating content scanned and detected by the CDN system, and the current status of the URLs.
        It corresponds to the **Pornography Detection** page on the CDN Console.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUrlViolations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUrlViolationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableCaches(
            self,
            request: models.DisableCachesRequest,
            opts: Dict = None,
    ) -> models.DisableCachesResponse:
        """
        This API is used to block access to a specific URL on CDN. When a URL is blocked, error 403 will be returned for requests from the Chinese mainland. URL blocking is not permanent. Note that this API is only available to beta users now.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableCaches"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableCachesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableClsLogTopic(
            self,
            request: models.DisableClsLogTopicRequest,
            opts: Dict = None,
    ) -> models.DisableClsLogTopicResponse:
        """
        This API is used to stop publishing to a log topic. Note: after a log topic is disabled, all logs of the domain names bound to it will no longer be published to the topic, and the logs that have already been published will be retained. This action will take effect within 5–15 minutes.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableClsLogTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableClsLogTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableCaches(
            self,
            request: models.EnableCachesRequest,
            opts: Dict = None,
    ) -> models.EnableCachesResponse:
        """
        This API (EnableCaches) is used to unblock manually blocked URLs. After a URL is successfully unblocked, it takes about 5 to 10 minutes to take effect across the entire network. (This API is during beta test and not fully available now.)
        """
        
        kwargs = {}
        kwargs["action"] = "EnableCaches"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableCachesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableClsLogTopic(
            self,
            request: models.EnableClsLogTopicRequest,
            opts: Dict = None,
    ) -> models.EnableClsLogTopicResponse:
        """
        This API is used to start publishing to a log topic. Note: after a log topic is enabled, all logs of the domain names bound to the topic will be published to it. This action will take effect within 5–15 minutes.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableClsLogTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableClsLogTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDisableRecords(
            self,
            request: models.GetDisableRecordsRequest,
            opts: Dict = None,
    ) -> models.GetDisableRecordsResponse:
        """
        This API is used to query the resource blocking history and the current URL status. (This API is in beta test and not generally available yet.)
        """
        
        kwargs = {}
        kwargs["action"] = "GetDisableRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDisableRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListClsLogTopics(
            self,
            request: models.ListClsLogTopicsRequest,
            opts: Dict = None,
    ) -> models.ListClsLogTopicsResponse:
        """
        This API is used to display the list of log topics. Note: a logset can contain up to 10 log topics.
        """
        
        kwargs = {}
        kwargs["action"] = "ListClsLogTopics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListClsLogTopicsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListClsTopicDomains(
            self,
            request: models.ListClsTopicDomainsRequest,
            opts: Dict = None,
    ) -> models.ListClsTopicDomainsResponse:
        """
        This API is used to get the list of domain names bound to a log topic.
        """
        
        kwargs = {}
        kwargs["action"] = "ListClsTopicDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListClsTopicDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTopData(
            self,
            request: models.ListTopDataRequest,
            opts: Dict = None,
    ) -> models.ListTopDataResponse:
        """
        This API is used to list data sorted the following ways by using different combinations of the Metric and Filter input parameters:

        + It sorts access URLs by total traffic and total requests, and returns the top 1,000 URLs in descending order.
        + It sorts client districts by total traffic and total requests, and returns the list of districts in descending order.
        + It sorts client ISPs by total traffic and total requests, and returns the list of ISPs in descending order.
        + It sorts domain names by total traffic, peak bandwidth, total requests, average hit rate, and 2XX/3XX/4XX/5XX status codes, and returns the list of domain names in descending order.
        + It sorts domain names by total origin-pull traffic, peak origin-pull bandwidth, total origin-pull requests, average origin-pull failure rate, and 2XX/3XX/4XX/5XX origin-pull status codes, and returns the list of domain names in descending order.

        Note: only data from the last 90 days will be queried.
        """
        
        kwargs = {}
        kwargs["action"] = "ListTopData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTopDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ManageClsTopicDomains(
            self,
            request: models.ManageClsTopicDomainsRequest,
            opts: Dict = None,
    ) -> models.ManageClsTopicDomainsResponse:
        """
        This API is used to manage the list of domain names bound to a log topic.
        """
        
        kwargs = {}
        kwargs["action"] = "ManageClsTopicDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ManageClsTopicDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainConfig(
            self,
            request: models.ModifyDomainConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainConfigResponse:
        """
        This API is used to modify the configuration of a CDN acceleration domain name in a finer manner than `UpdateDomainConfig`.
        Notes:
        In `Route`, separate values by dots (.). The last value is called a leaf node. For non-leaf nodes, keep the configuration unchanged.
        The Value field is serialized to a JSON string {key:value}, where **key** is fixed to `update` and **value** is used to specify the value of the configuration parameter. To specify configurations with complex types, see https://intl.cloud.tencent.com/document/product/228/41116.?from_cn_redirect=1
        The input parameters of this API are not reported to CloudAudit as it may contain sensitive data, such as keys and secrets.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PurgePathCache(
            self,
            request: models.PurgePathCacheRequest,
            opts: Dict = None,
    ) -> models.PurgePathCacheResponse:
        """
        This API is used to submit multiple directory purge tasks, which are carried out according to the acceleration region of the domain names.
        By default, a maximum of 100 directories can be purged per day for acceleration regions either within or outside the Chinese mainland, and up to 500 tasks can be submitted at a time.
        """
        
        kwargs = {}
        kwargs["action"] = "PurgePathCache"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PurgePathCacheResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PurgeUrlsCache(
            self,
            request: models.PurgeUrlsCacheRequest,
            opts: Dict = None,
    ) -> models.PurgeUrlsCacheResponse:
        """
        This API is used to submit multiple URL purge tasks, which are carried out according to the current acceleration region of the domain names in the URLs.
        By default, a maximum of 10,000 URLs can be purged per day for acceleration regions either within or outside Mainland China, and up to 1,000 tasks can be submitted at a time.
        """
        
        kwargs = {}
        kwargs["action"] = "PurgeUrlsCache"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PurgeUrlsCacheResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PushUrlsCache(
            self,
            request: models.PushUrlsCacheRequest,
            opts: Dict = None,
    ) -> models.PushUrlsCacheResponse:
        """
        This API is used to cache specified URL resources to CDN nodes. You can specify acceleration regions for the prefetch.
        By default, a maximum of 1000 URLs can be prefetched per day for regions either within or outside the Chinese mainland, and up to 500 tasks can be submitted at a time. Note that resources prefetched outside the Chinese mainland will be cached to CDN nodes outside the Chinese mainland and the traffic generated will incur costs.
        """
        
        kwargs = {}
        kwargs["action"] = "PushUrlsCache"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PushUrlsCacheResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchClsLog(
            self,
            request: models.SearchClsLogRequest,
            opts: Dict = None,
    ) -> models.SearchClsLogResponse:
        """
        This API is used to search for CLS logs. Search filters can be set to today, 24 hours (one of the last 7 days), and the last 7 days.
        """
        
        kwargs = {}
        kwargs["action"] = "SearchClsLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchClsLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartCdnDomain(
            self,
            request: models.StartCdnDomainRequest,
            opts: Dict = None,
    ) -> models.StartCdnDomainResponse:
        """
        This API is used to enable the acceleration service for a disabled domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "StartCdnDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartCdnDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopCdnDomain(
            self,
            request: models.StopCdnDomainRequest,
            opts: Dict = None,
    ) -> models.StopCdnDomainResponse:
        """
        This API is used to suspend the acceleration service for a domain name.
        Note: after the acceleration service has been suspended, requests to the cache node will return a 404 error. In order to avoid impact to your business, please move the domain name to another service before suspending the acceleration service.
        """
        
        kwargs = {}
        kwargs["action"] = "StopCdnDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopCdnDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDomainConfig(
            self,
            request: models.UpdateDomainConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateDomainConfigResponse:
        """
        This API is used to modify the configuration of CDN acceleration domain names.
        Note: To update complex configuration items, all attributes of the object must be specified, or the default values are used. We recommend calling the querying API to get attributes before modifying and passing them to this API.
        The input parameters of this API are not reported to CloudAudit as it may contain sensitive data, such as keys and secrets.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDomainConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDomainConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdatePayType(
            self,
            request: models.UpdatePayTypeRequest,
            opts: Dict = None,
    ) -> models.UpdatePayTypeResponse:
        """
        This API is used to modify the billing mode of an account. At present, the billing mode of accounts on a monthly billing cycle and sub-accounts cannot be modified.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdatePayType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdatePayTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateScdnDomain(
            self,
            request: models.UpdateScdnDomainRequest,
            opts: Dict = None,
    ) -> models.UpdateScdnDomainResponse:
        """
        This API is used to modify security configurations of SCDN acceleration domain names.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateScdnDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateScdnDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)