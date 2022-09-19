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
from tencentcloud.batch.v20170312 import models


class BatchClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'batch.tencentcloudapi.com'
    _service = 'batch'


    def DescribeAvailableCvmInstanceTypes(self, request):
        """This API is used to view the information of available CVM model configurations.

        :param request: Request instance for DescribeAvailableCvmInstanceTypes.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeAvailableCvmInstanceTypesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeAvailableCvmInstanceTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailableCvmInstanceTypes", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAvailableCvmInstanceTypesResponse()
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


    def DescribeCvmZoneInstanceConfigInfos(self, request):
        """This API is used to get the model configuration information of the availability zone of BatchCompute.

        :param request: Request instance for DescribeCvmZoneInstanceConfigInfos.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeCvmZoneInstanceConfigInfosRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeCvmZoneInstanceConfigInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCvmZoneInstanceConfigInfos", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCvmZoneInstanceConfigInfosResponse()
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


    def DescribeInstanceCategories(self, request):
        """Currently, CVM instance families are classified into different category, and each category contains several instance families. This API is used to query the instance category information.

        :param request: Request instance for DescribeInstanceCategories.
        :type request: :class:`tencentcloud.batch.v20170312.models.DescribeInstanceCategoriesRequest`
        :rtype: :class:`tencentcloud.batch.v20170312.models.DescribeInstanceCategoriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceCategories", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceCategoriesResponse()
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