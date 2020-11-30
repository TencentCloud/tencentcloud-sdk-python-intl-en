# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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


    def DescribeBillDetail(self, request):
        """This API is used to query bill details.

        :param request: Request instance for DescribeBillDetail.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillDetailRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBillDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBillDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBillResourceSummary(self, request):
        """This API is used to query bill resources summary.

        :param request: Request instance for DescribeBillResourceSummary.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillResourceSummaryRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillResourceSummaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBillResourceSummary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBillResourceSummaryResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBillSummaryByPayMode(self, request):
        """Gets the bill summarized according to billing mode

        :param request: Request instance for DescribeBillSummaryByPayMode.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByPayModeRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByPayModeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBillSummaryByPayMode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBillSummaryByPayModeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBillSummaryByProduct(self, request):
        """Gets the bill summarized according to product

        :param request: Request instance for DescribeBillSummaryByProduct.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByProductRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBillSummaryByProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBillSummaryByProductResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBillSummaryByProject(self, request):
        """Gets the bill summarized according to project

        :param request: Request instance for DescribeBillSummaryByProject.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByProjectRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBillSummaryByProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBillSummaryByProjectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBillSummaryByRegion(self, request):
        """Gets the bill summarized according to region

        :param request: Request instance for DescribeBillSummaryByRegion.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByRegionRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByRegionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBillSummaryByRegion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBillSummaryByRegionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBillSummaryByTag(self, request):
        """This API is used to get the cost distribution over different tags.

        :param request: Request instance for DescribeBillSummaryByTag.
        :type request: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByTagRequest`
        :rtype: :class:`tencentcloud.billing.v20180709.models.DescribeBillSummaryByTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBillSummaryByTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBillSummaryByTagResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)