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
from tencentcloud.cdc.v20201214 import models
from typing import Dict


class CdcClient(AbstractClient):
    _apiVersion = '2020-12-14'
    _endpoint = 'cdc.intl.tencentcloudapi.com'
    _service = 'cdc'

    async def CreateDedicatedCluster(
            self,
            request: models.CreateDedicatedClusterRequest,
            opts: Dict = None,
    ) -> models.CreateDedicatedClusterResponse:
        """
        This API is used to create a CDC.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDedicatedCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDedicatedClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDedicatedClusterOrder(
            self,
            request: models.CreateDedicatedClusterOrderRequest,
            opts: Dict = None,
    ) -> models.CreateDedicatedClusterOrderResponse:
        """
        This API is used to create a CDC order.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDedicatedClusterOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDedicatedClusterOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSite(
            self,
            request: models.CreateSiteRequest,
            opts: Dict = None,
    ) -> models.CreateSiteResponse:
        """
        This API is used to create a site.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSite"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSiteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDedicatedClusters(
            self,
            request: models.DeleteDedicatedClustersRequest,
            opts: Dict = None,
    ) -> models.DeleteDedicatedClustersResponse:
        """
        This API is used to delete a CDC.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDedicatedClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDedicatedClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSites(
            self,
            request: models.DeleteSitesRequest,
            opts: Dict = None,
    ) -> models.DeleteSitesResponse:
        """
        This API is used to delete a site.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSites"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSitesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDedicatedClusterCosCapacity(
            self,
            request: models.DescribeDedicatedClusterCosCapacityRequest,
            opts: Dict = None,
    ) -> models.DescribeDedicatedClusterCosCapacityResponse:
        """
        This API is used to query the Cloud Object Storage (COS) capacity of the CDC.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDedicatedClusterCosCapacity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDedicatedClusterCosCapacityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDedicatedClusterHostStatistics(
            self,
            request: models.DescribeDedicatedClusterHostStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeDedicatedClusterHostStatisticsResponse:
        """
        This API is used to query the statistic information of the host in the CDC.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDedicatedClusterHostStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDedicatedClusterHostStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDedicatedClusterHosts(
            self,
            request: models.DescribeDedicatedClusterHostsRequest,
            opts: Dict = None,
    ) -> models.DescribeDedicatedClusterHostsResponse:
        """
        This API is used to query host information of the CDC
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDedicatedClusterHosts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDedicatedClusterHostsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDedicatedClusterInstanceTypes(
            self,
            request: models.DescribeDedicatedClusterInstanceTypesRequest,
            opts: Dict = None,
    ) -> models.DescribeDedicatedClusterInstanceTypesResponse:
        """
        This API is used to query instance types supported by the CDC.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDedicatedClusterInstanceTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDedicatedClusterInstanceTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDedicatedClusterOrders(
            self,
            request: models.DescribeDedicatedClusterOrdersRequest,
            opts: Dict = None,
    ) -> models.DescribeDedicatedClusterOrdersResponse:
        """
        This API is used to query the list of CDC orders.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDedicatedClusterOrders"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDedicatedClusterOrdersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDedicatedClusterOverview(
            self,
            request: models.DescribeDedicatedClusterOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeDedicatedClusterOverviewResponse:
        """
        This API is used to query the overview of the CDC
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDedicatedClusterOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDedicatedClusterOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDedicatedClusterTypes(
            self,
            request: models.DescribeDedicatedClusterTypesRequest,
            opts: Dict = None,
    ) -> models.DescribeDedicatedClusterTypesResponse:
        """
        This API is used to query the configuration list of the CDC.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDedicatedClusterTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDedicatedClusterTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDedicatedClusters(
            self,
            request: models.DescribeDedicatedClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeDedicatedClustersResponse:
        """
        This API is used to query the CDC list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDedicatedClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDedicatedClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDedicatedSupportedZones(
            self,
            request: models.DescribeDedicatedSupportedZonesRequest,
            opts: Dict = None,
    ) -> models.DescribeDedicatedSupportedZonesResponse:
        """
        This API is used to query the list of AZs supported by the CDC.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDedicatedSupportedZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDedicatedSupportedZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSites(
            self,
            request: models.DescribeSitesRequest,
            opts: Dict = None,
    ) -> models.DescribeSitesResponse:
        """
        This API is used to query the site list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSites"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSitesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSitesDetail(
            self,
            request: models.DescribeSitesDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeSitesDetailResponse:
        """
        This API is used to query site details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSitesDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSitesDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDedicatedClusterInfo(
            self,
            request: models.ModifyDedicatedClusterInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyDedicatedClusterInfoResponse:
        """
        This API is used to modify the CDC information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDedicatedClusterInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDedicatedClusterInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOrderStatus(
            self,
            request: models.ModifyOrderStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyOrderStatusResponse:
        """
        This API is used to modify the status of large and small orders.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOrderStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOrderStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySiteDeviceInfo(
            self,
            request: models.ModifySiteDeviceInfoRequest,
            opts: Dict = None,
    ) -> models.ModifySiteDeviceInfoResponse:
        """
        This API is used to modify the information about devices in the equipment room.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySiteDeviceInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySiteDeviceInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySiteInfo(
            self,
            request: models.ModifySiteInfoRequest,
            opts: Dict = None,
    ) -> models.ModifySiteInfoResponse:
        """
        This API is used to modify the equipment room information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySiteInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySiteInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)