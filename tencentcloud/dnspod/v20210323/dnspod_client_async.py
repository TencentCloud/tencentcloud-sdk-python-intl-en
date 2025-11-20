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
from tencentcloud.dnspod.v20210323 import models
from typing import Dict


class DnspodClient(AbstractClient):
    _apiVersion = '2021-03-23'
    _endpoint = 'dnspod.intl.tencentcloudapi.com'
    _service = 'dnspod'

    async def CreateDomain(
            self,
            request: models.CreateDomainRequest,
            opts: Dict = None,
    ) -> models.CreateDomainResponse:
        """
        This API is used to add a domain.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDomainAlias(
            self,
            request: models.CreateDomainAliasRequest,
            opts: Dict = None,
    ) -> models.CreateDomainAliasResponse:
        """
        This API is used to create a domain alias.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomainAlias"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainAliasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDomainBatch(
            self,
            request: models.CreateDomainBatchRequest,
            opts: Dict = None,
    ) -> models.CreateDomainBatchResponse:
        """
        This API is used to bulk add domains.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomainBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDomainGroup(
            self,
            request: models.CreateDomainGroupRequest,
            opts: Dict = None,
    ) -> models.CreateDomainGroupResponse:
        """
        This API is used to create a domain group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomainGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePackageOrder(
            self,
            request: models.CreatePackageOrderRequest,
            opts: Dict = None,
    ) -> models.CreatePackageOrderResponse:
        """
        This API is used to enable a paid plan on the international website.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePackageOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePackageOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRecord(
            self,
            request: models.CreateRecordRequest,
            opts: Dict = None,
    ) -> models.CreateRecordResponse:
        """
        This API is used to add a record.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRecordBatch(
            self,
            request: models.CreateRecordBatchRequest,
            opts: Dict = None,
    ) -> models.CreateRecordBatchResponse:
        """
        This API is used to bulk add records.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRecordBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRecordBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRecordGroup(
            self,
            request: models.CreateRecordGroupRequest,
            opts: Dict = None,
    ) -> models.CreateRecordGroupResponse:
        """
        This API is used to add a record group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRecordGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRecordGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDomain(
            self,
            request: models.DeleteDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteDomainResponse:
        """
        This API is used to delete a domain.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDomainAlias(
            self,
            request: models.DeleteDomainAliasRequest,
            opts: Dict = None,
    ) -> models.DeleteDomainAliasResponse:
        """
        This API is used to delete a domain alias.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDomainAlias"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDomainAliasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDomainBatch(
            self,
            request: models.DeleteDomainBatchRequest,
            opts: Dict = None,
    ) -> models.DeleteDomainBatchResponse:
        """
        This API is used to batch delete domains.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDomainBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDomainBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePackageOrder(
            self,
            request: models.DeletePackageOrderRequest,
            opts: Dict = None,
    ) -> models.DeletePackageOrderResponse:
        """
        This API is used to disable the paid plan on the international website.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePackageOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePackageOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecord(
            self,
            request: models.DeleteRecordRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordResponse:
        """
        This API is used to delete a record.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRecordGroup(
            self,
            request: models.DeleteRecordGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteRecordGroupResponse:
        """
        This API is used to delete a record group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRecordGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRecordGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteShareDomain(
            self,
            request: models.DeleteShareDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteShareDomainResponse:
        """
        This API is used to unshare a domain.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteShareDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteShareDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomain(
            self,
            request: models.DescribeDomainRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainResponse:
        """
        This API is used to get the information of a domain.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainAliasList(
            self,
            request: models.DescribeDomainAliasListRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainAliasListResponse:
        """
        This API is used to get the list of domain aliases.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainAliasList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainAliasListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainGroupList(
            self,
            request: models.DescribeDomainGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainGroupListResponse:
        """
        This API is used to get the list of domain groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainList(
            self,
            request: models.DescribeDomainListRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainListResponse:
        """
        This API is used to get the list of domains.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainLogList(
            self,
            request: models.DescribeDomainLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainLogListResponse:
        """
        This API is used to get the log of a domain.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainPurview(
            self,
            request: models.DescribeDomainPurviewRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainPurviewResponse:
        """
        This API is used to get the permissions of a domain.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainPurview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainPurviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainShareInfo(
            self,
            request: models.DescribeDomainShareInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainShareInfoResponse:
        """
        This API is used to get the domain sharing information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainShareInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainShareInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecord(
            self,
            request: models.DescribeRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordResponse:
        """
        This API is used to get the information of a record.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordGroupList(
            self,
            request: models.DescribeRecordGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordGroupListResponse:
        """
        This API is used to query the list of DNS record groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordLineCategoryList(
            self,
            request: models.DescribeRecordLineCategoryListRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordLineCategoryListResponse:
        """
        This API is used to return a line list by category.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordLineCategoryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordLineCategoryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordLineList(
            self,
            request: models.DescribeRecordLineListRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordLineListResponse:
        """
        This API is used to get the split zones allowed by the domain level.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordLineList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordLineListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordList(
            self,
            request: models.DescribeRecordListRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordListResponse:
        """
        This API is used to get the DNS records of a domain.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordType(
            self,
            request: models.DescribeRecordTypeRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordTypeResponse:
        """
        This API is used to get the record type allowed by the domain level.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubdomainAnalytics(
            self,
            request: models.DescribeSubdomainAnalyticsRequest,
            opts: Dict = None,
    ) -> models.DescribeSubdomainAnalyticsResponse:
        """
        This API is used to collect statistics on the DNS query volume of a subdomain. It helps you understand the traffic and time period distribution and allows you to view statistics in the last three months. It is available only for domains under a paid plan.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubdomainAnalytics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubdomainAnalyticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainLock(
            self,
            request: models.ModifyDomainLockRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainLockResponse:
        """
        This API is used to lock a domain.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainLock"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainLockResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainOwner(
            self,
            request: models.ModifyDomainOwnerRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainOwnerResponse:
        """
        This API is used to transfer ownership of a domain.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainOwner"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainOwnerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainRemark(
            self,
            request: models.ModifyDomainRemarkRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainRemarkResponse:
        """
        This API is used to set the remarks of a domain.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainRemark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainRemarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainStatus(
            self,
            request: models.ModifyDomainStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainStatusResponse:
        """
        This API is used to modify the status of a domain.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainUnlock(
            self,
            request: models.ModifyDomainUnlockRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainUnlockResponse:
        """
        This API is used to unlock a domain.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainUnlock"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainUnlockResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRecord(
            self,
            request: models.ModifyRecordRequest,
            opts: Dict = None,
    ) -> models.ModifyRecordResponse:
        """
        This API is used to modify a record.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRecordBatch(
            self,
            request: models.ModifyRecordBatchRequest,
            opts: Dict = None,
    ) -> models.ModifyRecordBatchResponse:
        """
        This API is used to bulk modify records.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRecordBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRecordBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRecordGroup(
            self,
            request: models.ModifyRecordGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyRecordGroupResponse:
        """
        This API is used to modify a record group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRecordGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRecordGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRecordRemark(
            self,
            request: models.ModifyRecordRemarkRequest,
            opts: Dict = None,
    ) -> models.ModifyRecordRemarkResponse:
        """
        This API is used to set the remarks of a record.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRecordRemark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRecordRemarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRecordStatus(
            self,
            request: models.ModifyRecordStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyRecordStatusResponse:
        """
        This API is used to modify the DNS record status.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRecordStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRecordStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRecordToGroup(
            self,
            request: models.ModifyRecordToGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyRecordToGroupResponse:
        """
        This API is used to add a record to a group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRecordToGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRecordToGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)