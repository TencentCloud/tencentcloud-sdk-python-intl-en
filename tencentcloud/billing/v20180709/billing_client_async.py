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
from tencentcloud.billing.v20180709 import models
from typing import Dict


class BillingClient(AbstractClient):
    _apiVersion = '2018-07-09'
    _endpoint = 'billing.intl.tencentcloudapi.com'
    _service = 'billing'

    async def CreateAllocationRule(
            self,
            request: models.CreateAllocationRuleRequest,
            opts: Dict = None,
    ) -> models.CreateAllocationRuleResponse:
        """
        Create a sharing rule.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAllocationRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAllocationRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAllocationTag(
            self,
            request: models.CreateAllocationTagRequest,
            opts: Dict = None,
    ) -> models.CreateAllocationTagResponse:
        """
        This API is used to batch set cost allocation tags.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAllocationTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAllocationTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAllocationUnit(
            self,
            request: models.CreateAllocationUnitRequest,
            opts: Dict = None,
    ) -> models.CreateAllocationUnitResponse:
        """
        This API is used to create allocation units.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAllocationUnit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAllocationUnitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGatherRule(
            self,
            request: models.CreateGatherRuleRequest,
            opts: Dict = None,
    ) -> models.CreateGatherRuleResponse:
        """
        Create a collection rule.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGatherRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGatherRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAllocationRule(
            self,
            request: models.DeleteAllocationRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteAllocationRuleResponse:
        """
        Delete sharing rule interface.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAllocationRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAllocationRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAllocationTag(
            self,
            request: models.DeleteAllocationTagRequest,
            opts: Dict = None,
    ) -> models.DeleteAllocationTagResponse:
        """
        u200cThis API is used to batch cancel cost allocation tags.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAllocationTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAllocationTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAllocationUnit(
            self,
            request: models.DeleteAllocationUnitRequest,
            opts: Dict = None,
    ) -> models.DeleteAllocationUnitResponse:
        """
        Delete a cost allocation unit.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAllocationUnit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAllocationUnitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGatherRule(
            self,
            request: models.DeleteGatherRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteGatherRuleResponse:
        """
        Delete a collection rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGatherRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGatherRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountBalance(
            self,
            request: models.DescribeAccountBalanceRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountBalanceResponse:
        """
        This API is used to check the Tencent Cloud account balance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountBalance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountBalanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllocationRuleDetail(
            self,
            request: models.DescribeAllocationRuleDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAllocationRuleDetailResponse:
        """
        This API is used to query sharing rule details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllocationRuleDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllocationRuleDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllocationRuleSummary(
            self,
            request: models.DescribeAllocationRuleSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeAllocationRuleSummaryResponse:
        """
        This API is used to query all sharing rule overviews.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllocationRuleSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllocationRuleSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllocationTree(
            self,
            request: models.DescribeAllocationTreeRequest,
            opts: Dict = None,
    ) -> models.DescribeAllocationTreeResponse:
        """
        This API is used to query the cost tree.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllocationTree"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllocationTreeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllocationUnitDetail(
            self,
            request: models.DescribeAllocationUnitDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAllocationUnitDetailResponse:
        """
        Query the details of a cost allocation unit.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllocationUnitDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllocationUnitDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillAdjustInfo(
            self,
            request: models.DescribeBillAdjustInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeBillAdjustInfoResponse:
        """
        This API is used to check whether the current UIN has any adjustment, enabling customers to proactively obtain the adjustment status faster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillAdjustInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillAdjustInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillDetail(
            self,
            request: models.DescribeBillDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeBillDetailResponse:
        """
        u200cThis API is used to get bill details.
        Note:
        1. The API request may fail due to network instability or other exceptions. In this case, we recommend you manually retry the request when the API request fails.
        2.If the volume of your bill data is high (for example, if over 200 thousand bill entries are generated for a month), bill data query via APIs may be slow. We recommend you enable bill storage so that you can obtain bill files from COS buckets for analysis. For details, see [Saving Bills to COS](https://intl.cloud.tencent.com/document/product/555/61275?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillDetailForOrganization(
            self,
            request: models.DescribeBillDetailForOrganizationRequest,
            opts: Dict = None,
    ) -> models.DescribeBillDetailForOrganizationResponse:
        """
        This API is used to get pay-on-behalf bills of the admin account (bill details).
        Note: The API request may fail due to network instability or other exceptions. In this case, we recommend you manually retry the request when the API request fails.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillDetailForOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillDetailForOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillDownloadUrl(
            self,
            request: models.DescribeBillDownloadUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeBillDownloadUrlResponse:
        """
        This API is used to get bill download URLs for L0, L1, L2, and L3 bills and bill packs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillDownloadUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillDownloadUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillResourceSummary(
            self,
            request: models.DescribeBillResourceSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeBillResourceSummaryResponse:
        """
        This API is used to get the bill summarized by instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillResourceSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillResourceSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillResourceSummaryForOrganization(
            self,
            request: models.DescribeBillResourceSummaryForOrganizationRequest,
            opts: Dict = None,
    ) -> models.DescribeBillResourceSummaryForOrganizationResponse:
        """
        This API is used to get pay-on-behalf bills of the admin account (bills by instance).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillResourceSummaryForOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillResourceSummaryForOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillSummary(
            self,
            request: models.DescribeBillSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeBillSummaryResponse:
        """
        This API is used to get bill details by product, project, region, billing mode, and tag by passing in parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillSummaryByPayMode(
            self,
            request: models.DescribeBillSummaryByPayModeRequest,
            opts: Dict = None,
    ) -> models.DescribeBillSummaryByPayModeResponse:
        """
        This API is used to get the bill summarized by billing mode.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillSummaryByPayMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillSummaryByPayModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillSummaryByProduct(
            self,
            request: models.DescribeBillSummaryByProductRequest,
            opts: Dict = None,
    ) -> models.DescribeBillSummaryByProductResponse:
        """
        Gets the bill summarized according to product
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillSummaryByProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillSummaryByProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillSummaryByProject(
            self,
            request: models.DescribeBillSummaryByProjectRequest,
            opts: Dict = None,
    ) -> models.DescribeBillSummaryByProjectResponse:
        """
        Gets the bill summarized according to project
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillSummaryByProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillSummaryByProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillSummaryByRegion(
            self,
            request: models.DescribeBillSummaryByRegionRequest,
            opts: Dict = None,
    ) -> models.DescribeBillSummaryByRegionResponse:
        """
        Gets the bill summarized according to region
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillSummaryByRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillSummaryByRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillSummaryByTag(
            self,
            request: models.DescribeBillSummaryByTagRequest,
            opts: Dict = None,
    ) -> models.DescribeBillSummaryByTagResponse:
        """
        This API is used to get the cost distribution over different tags.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillSummaryByTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillSummaryByTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillSummaryForOrganization(
            self,
            request: models.DescribeBillSummaryForOrganizationRequest,
            opts: Dict = None,
    ) -> models.DescribeBillSummaryForOrganizationResponse:
        """
        This API is used to get bills summarized by product, project, region, billing mode, and tag by passing in parameters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillSummaryForOrganization"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillSummaryForOrganizationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCostDetail(
            self,
            request: models.DescribeCostDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCostDetailResponse:
        """
        This API is used to query consumption details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCostDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCostDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCostExplorerSummary(
            self,
            request: models.DescribeCostExplorerSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeCostExplorerSummaryResponse:
        """
        This API is used to view cost analysis details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCostExplorerSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCostExplorerSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCostSummaryByProduct(
            self,
            request: models.DescribeCostSummaryByProductRequest,
            opts: Dict = None,
    ) -> models.DescribeCostSummaryByProductResponse:
        """
        This API is used to obtain consumption details summarized by product.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCostSummaryByProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCostSummaryByProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCostSummaryByProject(
            self,
            request: models.DescribeCostSummaryByProjectRequest,
            opts: Dict = None,
    ) -> models.DescribeCostSummaryByProjectResponse:
        """
        This API is used to obtain consumption details summarized by project.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCostSummaryByProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCostSummaryByProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCostSummaryByRegion(
            self,
            request: models.DescribeCostSummaryByRegionRequest,
            opts: Dict = None,
    ) -> models.DescribeCostSummaryByRegionResponse:
        """
        This API is used to obtain consumption details summarized by region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCostSummaryByRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCostSummaryByRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCostSummaryByResource(
            self,
            request: models.DescribeCostSummaryByResourceRequest,
            opts: Dict = None,
    ) -> models.DescribeCostSummaryByResourceResponse:
        """
        This API is used to obtain consumption details summarized by resource.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCostSummaryByResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCostSummaryByResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDealsByCond(
            self,
            request: models.DescribeDealsByCondRequest,
            opts: Dict = None,
    ) -> models.DescribeDealsByCondResponse:
        """
        Querying orders
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDealsByCond"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDealsByCondResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDosageCosDetailByDate(
            self,
            request: models.DescribeDosageCosDetailByDateRequest,
            opts: Dict = None,
    ) -> models.DescribeDosageCosDetailByDateResponse:
        """
        This API is used to query COS usage details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDosageCosDetailByDate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDosageCosDetailByDateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatherRuleDetail(
            self,
            request: models.DescribeGatherRuleDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeGatherRuleDetailResponse:
        """
        This API is used to query the collection rule details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatherRuleDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatherRuleDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagList(
            self,
            request: models.DescribeTagListRequest,
            opts: Dict = None,
    ) -> models.DescribeTagListResponse:
        """
        This API is used to get cost allocation tags.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVoucherInfo(
            self,
            request: models.DescribeVoucherInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeVoucherInfoResponse:
        """
        This API is used to query vouchers.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVoucherInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVoucherInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVoucherUsageDetails(
            self,
            request: models.DescribeVoucherUsageDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeVoucherUsageDetailsResponse:
        """
        This API is used to query voucher usage details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVoucherUsageDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVoucherUsageDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAllocationRule(
            self,
            request: models.ModifyAllocationRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyAllocationRuleResponse:
        """
        Edit sharing rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAllocationRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAllocationRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAllocationUnit(
            self,
            request: models.ModifyAllocationUnitRequest,
            opts: Dict = None,
    ) -> models.ModifyAllocationUnitResponse:
        """
        This API is used to modify cost allocation unit information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAllocationUnit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAllocationUnitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGatherRule(
            self,
            request: models.ModifyGatherRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyGatherRuleResponse:
        """
        Edit a collection rule.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGatherRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGatherRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PayDeals(
            self,
            request: models.PayDealsRequest,
            opts: Dict = None,
    ) -> models.PayDealsResponse:
        """
        This API is used to pay for an order.
        """
        
        kwargs = {}
        kwargs["action"] = "PayDeals"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PayDealsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)