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
from tencentcloud.privatedns.v20201028 import models
from typing import Dict


class PrivatednsClient(AbstractClient):
    _apiVersion = '2020-10-28'
    _endpoint = 'privatedns.intl.tencentcloudapi.com'
    _service = 'privatedns'

    async def CreateEndPoint(
            self,
            request: models.CreateEndPointRequest,
            opts: Dict = None,
    ) -> models.CreateEndPointResponse:
        """
        This API is used to create an endpoint.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEndPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEndPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEndPointAndEndPointService(
            self,
            request: models.CreateEndPointAndEndPointServiceRequest,
            opts: Dict = None,
    ) -> models.CreateEndPointAndEndPointServiceResponse:
        """
        This API is used to create an endpoint and an endpoint service simultaneously.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEndPointAndEndPointService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEndPointAndEndPointServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateExtendEndpoint(
            self,
            request: models.CreateExtendEndpointRequest,
            opts: Dict = None,
    ) -> models.CreateExtendEndpointResponse:
        """
        This API is used to create an endpoint.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateExtendEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateExtendEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateForwardRule(
            self,
            request: models.CreateForwardRuleRequest,
            opts: Dict = None,
    ) -> models.CreateForwardRuleResponse:
        """
        This API is used to create a custom forwarding rule.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateForwardRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateForwardRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrivateDNSAccount(
            self,
            request: models.CreatePrivateDNSAccountRequest,
            opts: Dict = None,
    ) -> models.CreatePrivateDNSAccountResponse:
        """
        This API is used to create a Private DNS account.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrivateDNSAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrivateDNSAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrivateZone(
            self,
            request: models.CreatePrivateZoneRequest,
            opts: Dict = None,
    ) -> models.CreatePrivateZoneResponse:
        """
        This API is used to create a private domain.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrivateZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrivateZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrivateZoneRecord(
            self,
            request: models.CreatePrivateZoneRecordRequest,
            opts: Dict = None,
    ) -> models.CreatePrivateZoneRecordResponse:
        """
        This API is used to add a DNS record for a private domain.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrivateZoneRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrivateZoneRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEndPoint(
            self,
            request: models.DeleteEndPointRequest,
            opts: Dict = None,
    ) -> models.DeleteEndPointResponse:
        """
        Deletes an endpoint
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEndPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEndPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteForwardRule(
            self,
            request: models.DeleteForwardRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteForwardRuleResponse:
        """
        This API is used to delete a forwarding rule and stop forwarding.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteForwardRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteForwardRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrivateZoneRecord(
            self,
            request: models.DeletePrivateZoneRecordRequest,
            opts: Dict = None,
    ) -> models.DeletePrivateZoneRecordResponse:
        """
        This API is used to delete a DNS record for a private domain.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrivateZoneRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrivateZoneRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountVpcList(
            self,
            request: models.DescribeAccountVpcListRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountVpcListResponse:
        """
        This API is used to get the VPC list of a Private DNS account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountVpcList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountVpcListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuditLog(
            self,
            request: models.DescribeAuditLogRequest,
            opts: Dict = None,
    ) -> models.DescribeAuditLogResponse:
        """
        This API is used to get the list of operation logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuditLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuditLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDashboard(
            self,
            request: models.DescribeDashboardRequest,
            opts: Dict = None,
    ) -> models.DescribeDashboardResponse:
        """
        This API is used to get the overview of private DNS records.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDashboard"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDashboardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEndPointList(
            self,
            request: models.DescribeEndPointListRequest,
            opts: Dict = None,
    ) -> models.DescribeEndPointListResponse:
        """
        This API is used to obtain the endpoint list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEndPointList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEndPointListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEndPointRegion(
            self,
            request: models.DescribeEndPointRegionRequest,
            opts: Dict = None,
    ) -> models.DescribeEndPointRegionResponse:
        """
        This API is used to query the regions where the endpoint is enabled.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEndPointRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEndPointRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExtendEndpointList(
            self,
            request: models.DescribeExtendEndpointListRequest,
            opts: Dict = None,
    ) -> models.DescribeExtendEndpointListResponse:
        """
        This API is used to obtain the endpoint list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExtendEndpointList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExtendEndpointListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeForwardRule(
            self,
            request: models.DescribeForwardRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeForwardRuleResponse:
        """
        This API is used to query forwarding rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeForwardRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeForwardRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeForwardRuleList(
            self,
            request: models.DescribeForwardRuleListRequest,
            opts: Dict = None,
    ) -> models.DescribeForwardRuleListResponse:
        """
        This API is used to query the forwarding rule list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeForwardRuleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeForwardRuleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivateDNSAccountList(
            self,
            request: models.DescribePrivateDNSAccountListRequest,
            opts: Dict = None,
    ) -> models.DescribePrivateDNSAccountListResponse:
        """
        This API is used to get the list of Private DNS accounts.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivateDNSAccountList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivateDNSAccountListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivateZoneList(
            self,
            request: models.DescribePrivateZoneListRequest,
            opts: Dict = None,
    ) -> models.DescribePrivateZoneListResponse:
        """
        This API is used to obtain the private domain list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivateZoneList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivateZoneListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivateZoneRecordList(
            self,
            request: models.DescribePrivateZoneRecordListRequest,
            opts: Dict = None,
    ) -> models.DescribePrivateZoneRecordListResponse:
        """
        This API is used to get the list of records for a private domain.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivateZoneRecordList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivateZoneRecordListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivateZoneService(
            self,
            request: models.DescribePrivateZoneServiceRequest,
            opts: Dict = None,
    ) -> models.DescribePrivateZoneServiceResponse:
        """
        This API is used to query the Private DNS activation status.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivateZoneService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivateZoneServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQuotaUsage(
            self,
            request: models.DescribeQuotaUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeQuotaUsageResponse:
        """
        This API is used to query quota usage.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQuotaUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQuotaUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecord(
            self,
            request: models.DescribeRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordResponse:
        """
        This API is used to obtain the private domain records.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRequestData(
            self,
            request: models.DescribeRequestDataRequest,
            opts: Dict = None,
    ) -> models.DescribeRequestDataResponse:
        """
        This API is used to get the DNS request volume of a private domain.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRequestData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRequestDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyForwardRule(
            self,
            request: models.ModifyForwardRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyForwardRuleResponse:
        """
        This API is used to modify a forwarding rule.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyForwardRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyForwardRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrivateZone(
            self,
            request: models.ModifyPrivateZoneRequest,
            opts: Dict = None,
    ) -> models.ModifyPrivateZoneResponse:
        """
        This API is used to modify a private domain.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrivateZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrivateZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrivateZoneRecord(
            self,
            request: models.ModifyPrivateZoneRecordRequest,
            opts: Dict = None,
    ) -> models.ModifyPrivateZoneRecordResponse:
        """
        This API is used to modify a DNS record for a private domain.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrivateZoneRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrivateZoneRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrivateZoneVpc(
            self,
            request: models.ModifyPrivateZoneVpcRequest,
            opts: Dict = None,
    ) -> models.ModifyPrivateZoneVpcResponse:
        """
        This API is used to modify the VPC associated with a private domain.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrivateZoneVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrivateZoneVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRecordsStatus(
            self,
            request: models.ModifyRecordsStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyRecordsStatusResponse:
        """
        This API is used to modify the DNS record status.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRecordsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRecordsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubscribePrivateZoneService(
            self,
            request: models.SubscribePrivateZoneServiceRequest,
            opts: Dict = None,
    ) -> models.SubscribePrivateZoneServiceResponse:
        """
        This API is used to activate the Private DNS service.
        """
        
        kwargs = {}
        kwargs["action"] = "SubscribePrivateZoneService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubscribePrivateZoneServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)