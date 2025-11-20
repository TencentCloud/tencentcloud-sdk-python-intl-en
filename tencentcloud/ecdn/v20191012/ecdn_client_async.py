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
from tencentcloud.ecdn.v20191012 import models
from typing import Dict


class EcdnClient(AbstractClient):
    _apiVersion = '2019-10-12'
    _endpoint = 'ecdn.intl.tencentcloudapi.com'
    _service = 'ecdn'

    async def AddEcdnDomain(
            self,
            request: models.AddEcdnDomainRequest,
            opts: Dict = None,
    ) -> models.AddEcdnDomainResponse:
        """
        This API is used to create an acceleration domain name.

        >? If you have migrated your ECDN service to CDN, you can use the <a href="https://intl.cloud.tencent.com/document/api/228/41123?from_cn_redirect=1">corresponding CDN API</a>.
        """
        
        kwargs = {}
        kwargs["action"] = "AddEcdnDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddEcdnDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEcdnDomain(
            self,
            request: models.DeleteEcdnDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteEcdnDomainResponse:
        """
        This API is used to delete a specified acceleration domain name. The acceleration domain name to be deleted must be in disabled status.

        >? If you have migrated your ECDN service to CDN, you can use the <a href="https://intl.cloud.tencent.com/document/api/570/42471?from_cn_redirect=1">corresponding CDN API</a>.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEcdnDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEcdnDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomains(
            self,
            request: models.DescribeDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainsResponse:
        """
        This API is used to query the basic information of a CDN domain name, including the project ID, status, business type, creation time, update time, etc.

        >? If you have migrated your ECDN service to CDN, you can use the <a href="https://intl.cloud.tencent.com/document/api/228/41118?from_cn_redirect=1">corresponding CDN API</a>.
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
        This API is used to query the detailed configuration information of a CDN acceleration domain name.

        >? If you have migrated your ECDN service to CDN, you can use the <a href="https://intl.cloud.tencent.com/document/api/228/41117?from_cn_redirect=1">corresponding CDN API</a>.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainsConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainsConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEcdnDomainLogs(
            self,
            request: models.DescribeEcdnDomainLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeEcdnDomainLogsResponse:
        """
        This API is used to query the access log download link of a domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEcdnDomainLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEcdnDomainLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEcdnDomainStatistics(
            self,
            request: models.DescribeEcdnDomainStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeEcdnDomainStatisticsResponse:
        """
        This API is used to query the statistical metrics of domain name access within a specified time period.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEcdnDomainStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEcdnDomainStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEcdnStatistics(
            self,
            request: models.DescribeEcdnStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeEcdnStatisticsResponse:
        """
        This API is used to query ECDN real-time access monitoring data and supports the following metrics:

        + Traffic (in bytes)
        + Bandwidth (in bps)
        + Number of requests
        + Number of 2xx status codes and details of status codes starting with 2
        + Number of 3xx status codes and details of status codes starting with 3
        + Number of 4xx status codes and details of status codes starting with 4
        + Number of 5xx status codes and details of status codes starting with 5
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEcdnStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEcdnStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIpStatus(
            self,
            request: models.DescribeIpStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeIpStatusResponse:
        """
        This API is used to query ECDN node IPs. This API is only available to beta users. Please submit a ticket to use it.

        If you need to add the node IPs to your origin allowlist, keep querying the updating the IPs regularly to ensure the success of origin forwarding.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIpStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIpStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePurgeQuota(
            self,
            request: models.DescribePurgeQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribePurgeQuotaResponse:
        """
        This API is used to query the usage quota of the purge API.

        >? If you have migrated your ECDN service to CDN, you can use the <a href="https://intl.cloud.tencent.com/document/api/228/41956?from_cn_redirect=1">corresponding CDN API</a>.
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
        This API is used to query the submission record and progress of purge tasks.

        >? If you have migrated your ECDN service to CDN, you can use the <a href="https://intl.cloud.tencent.com/document/api/228/37873?from_cn_redirect=1">corresponding CDN API</a>.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePurgeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePurgeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PurgePathCache(
            self,
            request: models.PurgePathCacheRequest,
            opts: Dict = None,
    ) -> models.PurgePathCacheResponse:
        """
        This API is used to purge cache directories in batches. One purge task ID will be returned for each submission.

        >? If you have migrated your ECDN service to CDN, you can use the <a href="https://intl.cloud.tencent.com/document/api/570/42475?from_cn_redirect=1">corresponding CDN API</a>.
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
        This API is used to batch purge URLs. One purge task ID will be returned for each submission.

        >? If you have migrated your ECDN service to CDN, you can use the <a href="https://intl.cloud.tencent.com/document/api/228/37870?from_cn_redirect=1">corresponding CDN API</a>.
        """
        
        kwargs = {}
        kwargs["action"] = "PurgeUrlsCache"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PurgeUrlsCacheResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartEcdnDomain(
            self,
            request: models.StartEcdnDomainRequest,
            opts: Dict = None,
    ) -> models.StartEcdnDomainResponse:
        """
        This API is used to enable an acceleration domain name. The domain name to be enabled must be in deactivated status.

        >? If you have migrated your ECDN service to CDN, you can use the <a href="https://intl.cloud.tencent.com/document/product/228/41121?from_cn_redirect=1">corresponding CDN API</a>.
        """
        
        kwargs = {}
        kwargs["action"] = "StartEcdnDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartEcdnDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopEcdnDomain(
            self,
            request: models.StopEcdnDomainRequest,
            opts: Dict = None,
    ) -> models.StopEcdnDomainResponse:
        """
        This API is used to disable an acceleration domain name. The domain name to be disabled must be in enabled or deploying status.

        >? If you have migrated your ECDN service to CDN, you can use the <a href="https://intl.cloud.tencent.com/document/product/228/41120?from_cn_redirect=1">corresponding CDN API</a>.
        """
        
        kwargs = {}
        kwargs["action"] = "StopEcdnDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopEcdnDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDomainConfig(
            self,
            request: models.UpdateDomainConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateDomainConfigResponse:
        """
        This API is used to update the configuration information of an ECDN acceleration domain name.
        Note: if you need to update complex configuration items, you must pass all the attributes of the entire object. The default value will be used for attributes that are not passed. We recommend calling the querying API to obtain the configuration attributes first. You can then modify and pass the attributes to the API. The certificate and key fields do not need to be passed for HTTPS configuration.

        >?  If your application has been migrated to Tencent Cloud CDN, you can use <a href="https://intl.cloud.tencent.com/document/product/228/41116?from_cn_redirect=1">CDN APIs</a>.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDomainConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDomainConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)