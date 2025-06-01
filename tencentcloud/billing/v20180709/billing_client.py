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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.billing.v20180709 import models


class BillingClient(AbstractClient):
    _apiVersion = '2018-07-09'
    _endpoint = 'billing.intl.tencentcloudapi.com'
    _service = 'billing'


    def CreateAllocationRule(self, request):
        """Create a sharing rule.

        :param request: Request instance for CreateAllocationRule.
        :type request: :class:`tencentcloud.billing.v20180709.models.CreateAllocationRuleRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.CreateAllocationRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAllocationRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAllocationRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAllocationTag(self, request):
        """This API is used to batch set cost allocation tags.

        :param request: Request instance for CreateAllocationTag.
        :type request: :class:`tencentcloud.billing.v20180709.models.CreateAllocationTagRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.CreateAllocationTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAllocationTag", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAllocationTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAllocationUnit(self, request):
        """This API is used to create allocation units.

        :param request: Request instance for CreateAllocationUnit.
        :type request: :class:`tencentcloud.billing.v20180709.models.CreateAllocationUnitRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.CreateAllocationUnitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAllocationUnit", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAllocationUnitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGatherRule(self, request):
        """Create a collection rule.

        :param request: Request instance for CreateGatherRule.
        :type request: :class:`tencentcloud.billing.v20180709.models.CreateGatherRuleRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.CreateGatherRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGatherRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGatherRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAllocationRule(self, request):
        """Delete sharing rule interface.

        :param request: Request instance for DeleteAllocationRule.
        :type request: :class:`tencentcloud.billing.v20180709.models.DeleteAllocationRuleRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DeleteAllocationRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAllocationRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAllocationRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAllocationTag(self, request):
        """u200cThis API is used to batch cancel cost allocation tags.

        :param request: Request instance for DeleteAllocationTag.
        :type request: :class:`tencentcloud.billing.v20180709.models.DeleteAllocationTagRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DeleteAllocationTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAllocationTag", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAllocationTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAllocationUnit(self, request):
        """Delete a cost allocation unit.

        :param request: Request instance for DeleteAllocationUnit.
        :type request: :class:`tencentcloud.billing.v20180709.models.DeleteAllocationUnitRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DeleteAllocationUnitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAllocationUnit", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAllocationUnitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGatherRule(self, request):
        """Delete a collection rule.

        :param request: Request instance for DeleteGatherRule.
        :type request: :class:`tencentcloud.billing.v20180709.models.DeleteGatherRuleRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DeleteGatherRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGatherRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGatherRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountBalance(self, request):
        """This API is used to check the Tencent Cloud account balance.

        :param request: Request instance for DescribeAccountBalance.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeAccountBalanceRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeAccountBalanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountBalance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountBalanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllocationRuleDetail(self, request):
        """This API is used to query sharing rule details.

        :param request: Request instance for DescribeAllocationRuleDetail.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationRuleDetailRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationRuleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllocationRuleDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllocationRuleDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllocationRuleSummary(self, request):
        """This API is used to query all sharing rule overviews.

        :param request: Request instance for DescribeAllocationRuleSummary.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationRuleSummaryRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationRuleSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllocationRuleSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllocationRuleSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllocationTree(self, request):
        """This API is used to query the cost tree.

        :param request: Request instance for DescribeAllocationTree.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationTreeRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationTreeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllocationTree", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllocationTreeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllocationUnitDetail(self, request):
        """Query the details of a cost allocation unit.

        :param request: Request instance for DescribeAllocationUnitDetail.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationUnitDetailRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeAllocationUnitDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllocationUnitDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllocationUnitDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillAdjustInfo(self, request):
        """This API is used to check whether the current UIN has any adjustment, enabling customers to proactively obtain the adjustment status faster.

        :param request: Request instance for DescribeBillAdjustInfo.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillAdjustInfoRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillAdjustInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillAdjustInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillAdjustInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillDetail(self, request):
        """u200cThis API is used to get bill details.
        Note:
        1. The API request may fail due to network instability or other exceptions. In this case, we recommend you manually retry the request when the API request fails.
        2.If the volume of your bill data is high (for example, if over 200 thousand bill entries are generated for a month), bill data query via APIs may be slow. We recommend you enable bill storage so that you can obtain bill files from COS buckets for analysis. For details, see [Saving Bills to COS](https://intl.cloud.tencent.com/document/product/555/61275?from_cn_redirect=1).

        :param request: Request instance for DescribeBillDetail.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillDetailRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillDetailForOrganization(self, request):
        """This API is used to get pay-on-behalf bills of the admin account (bill details).
        Note: The API request may fail due to network instability or other exceptions. In this case, we recommend you manually retry the request when the API request fails.

        :param request: Request instance for DescribeBillDetailForOrganization.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillDetailForOrganizationRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillDetailForOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillDetailForOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillDetailForOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillDownloadUrl(self, request):
        """This API is used to get bill download URLs for L0, L1, L2, and L3 bills and bill packs.

        :param request: Request instance for DescribeBillDownloadUrl.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillDownloadUrlRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillDownloadUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillDownloadUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillResourceSummary(self, request):
        """This API is used to get the bill summarized by instance.

        :param request: Request instance for DescribeBillResourceSummary.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillResourceSummaryRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillResourceSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillResourceSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillResourceSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillResourceSummaryForOrganization(self, request):
        """This API is used to get pay-on-behalf bills of the admin account (bills by instance).

        :param request: Request instance for DescribeBillResourceSummaryForOrganization.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillResourceSummaryForOrganizationRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillResourceSummaryForOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillResourceSummaryForOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillResourceSummaryForOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillSummary(self, request):
        """This API is used to get bill details by product, project, region, billing mode, and tag by passing in parameters.

        :param request: Request instance for DescribeBillSummary.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillSummaryByPayMode(self, request):
        """This API is used to get the bill summarized by billing mode.

        :param request: Request instance for DescribeBillSummaryByPayMode.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByPayModeRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByPayModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillSummaryByPayMode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillSummaryByPayModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillSummaryByProduct(self, request):
        """Gets the bill summarized according to product

        :param request: Request instance for DescribeBillSummaryByProduct.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByProductRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillSummaryByProduct", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillSummaryByProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillSummaryByProject(self, request):
        """Gets the bill summarized according to project

        :param request: Request instance for DescribeBillSummaryByProject.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByProjectRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillSummaryByProject", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillSummaryByProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillSummaryByRegion(self, request):
        """Gets the bill summarized according to region

        :param request: Request instance for DescribeBillSummaryByRegion.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByRegionRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillSummaryByRegion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillSummaryByRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillSummaryByTag(self, request):
        """This API is used to get the cost distribution over different tags.

        :param request: Request instance for DescribeBillSummaryByTag.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByTagRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillSummaryByTag", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillSummaryByTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBillSummaryForOrganization(self, request):
        """This API is used to get bills summarized by product, project, region, billing mode, and tag by passing in parameters.

        :param request: Request instance for DescribeBillSummaryForOrganization.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryForOrganizationRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryForOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillSummaryForOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillSummaryForOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCostDetail(self, request):
        """This API is used to query consumption details.

        :param request: Request instance for DescribeCostDetail.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeCostDetailRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeCostDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCostDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCostDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCostExplorerSummary(self, request):
        """This API is used to view cost analysis details.

        :param request: Request instance for DescribeCostExplorerSummary.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeCostExplorerSummaryRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeCostExplorerSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCostExplorerSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCostExplorerSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCostSummaryByProduct(self, request):
        """This API is used to obtain consumption details summarized by product.

        :param request: Request instance for DescribeCostSummaryByProduct.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByProductRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCostSummaryByProduct", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCostSummaryByProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCostSummaryByProject(self, request):
        """This API is used to obtain consumption details summarized by project.

        :param request: Request instance for DescribeCostSummaryByProject.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByProjectRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCostSummaryByProject", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCostSummaryByProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCostSummaryByRegion(self, request):
        """This API is used to obtain consumption details summarized by region.

        :param request: Request instance for DescribeCostSummaryByRegion.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByRegionRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCostSummaryByRegion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCostSummaryByRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCostSummaryByResource(self, request):
        """This API is used to obtain consumption details summarized by resource.

        :param request: Request instance for DescribeCostSummaryByResource.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByResourceRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeCostSummaryByResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCostSummaryByResource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCostSummaryByResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDealsByCond(self, request):
        """Querying orders

        :param request: Request instance for DescribeDealsByCond.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeDealsByCondRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeDealsByCondResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDealsByCond", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDealsByCondResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDosageCosDetailByDate(self, request):
        """This API is used to query COS usage details.

        :param request: Request instance for DescribeDosageCosDetailByDate.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeDosageCosDetailByDateRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeDosageCosDetailByDateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDosageCosDetailByDate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDosageCosDetailByDateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGatherRuleDetail(self, request):
        """This API is used to query the collection rule details.

        :param request: Request instance for DescribeGatherRuleDetail.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeGatherRuleDetailRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeGatherRuleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatherRuleDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatherRuleDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTagList(self, request):
        """This API is used to get cost allocation tags.

        :param request: Request instance for DescribeTagList.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeTagListRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeTagListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTagList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVoucherInfo(self, request):
        """This API is used to query vouchers.

        :param request: Request instance for DescribeVoucherInfo.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeVoucherInfoRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeVoucherInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVoucherInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVoucherInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVoucherUsageDetails(self, request):
        """This API is used to query voucher usage details.

        :param request: Request instance for DescribeVoucherUsageDetails.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeVoucherUsageDetailsRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeVoucherUsageDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVoucherUsageDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVoucherUsageDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAllocationRule(self, request):
        """Edit sharing rules.

        :param request: Request instance for ModifyAllocationRule.
        :type request: :class:`tencentcloud.billing.v20180709.models.ModifyAllocationRuleRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.ModifyAllocationRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAllocationRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAllocationRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAllocationUnit(self, request):
        """This API is used to modify cost allocation unit information.

        :param request: Request instance for ModifyAllocationUnit.
        :type request: :class:`tencentcloud.billing.v20180709.models.ModifyAllocationUnitRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.ModifyAllocationUnitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAllocationUnit", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAllocationUnitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGatherRule(self, request):
        """Edit a collection rule.

        :param request: Request instance for ModifyGatherRule.
        :type request: :class:`tencentcloud.billing.v20180709.models.ModifyGatherRuleRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.ModifyGatherRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGatherRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGatherRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))