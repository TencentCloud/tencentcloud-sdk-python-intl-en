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
    _endpoint = 'billing.tencentcloudapi.com'
    _service = 'billing'


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


    def DescribeBillDetail(self, request):
        """This API is used to get bill details.
        Notes: 1. The API request may fail due to network instability or other network exceptions. In this case, we recommend you manually retry the request when the API request fails. 2. If the volume of your bill data is high (for example, if over 200 thousand bill entries are generated for a month), querying bill data via APIs may be slow. We recommend you enable bill storage so that you can obtain bill files from COS buckets for analysis. For details, see [Saving Bills to COS](https://intl.cloud.tencent.com/document/product/555/61275?from_cn_redirect=1).

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


    def DescribeBillResourceSummary(self, request):
        """This API is used to query bill resources summary.

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