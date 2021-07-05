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
from tencentcloud.cloudaudit.v20190319 import models


class CloudauditClient(AbstractClient):
    _apiVersion = '2019-03-19'
    _endpoint = 'cloudaudit.tencentcloudapi.com'
    _service = 'cloudaudit'


    def CreateRecorder(self, request):
        """This API is used to create resource recorders to detect and record resource configuration changes.

        :param request: Request instance for CreateRecorder.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.CreateRecorderRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.CreateRecorderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRecorder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRecorderResponse()
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


    def DeleteRecorder(self, request):
        """This API is used to delete resource recorders. After deletion, resource configuration changes will not be recorded.

        :param request: Request instance for DeleteRecorder.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.DeleteRecorderRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.DeleteRecorderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRecorder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRecorderResponse()
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


    def DescribeDiscoveredResource(self, request):
        """This API is used to view the basic information of discovered resources.

        :param request: Request instance for DescribeDiscoveredResource.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeDiscoveredResourceRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeDiscoveredResourceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDiscoveredResource", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDiscoveredResourceResponse()
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


    def DescribeRecorder(self, request):
        """This API is used to display current configurations and status of a recorder.

        :param request: Request instance for DescribeRecorder.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeRecorderRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.DescribeRecorderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRecorder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRecorderResponse()
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


    def GetConfigurationItems(self, request):
        """This API is used to get the list of resource configuration items and display resource configuration changes in chronological order.

        :param request: Request instance for GetConfigurationItems.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.GetConfigurationItemsRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.GetConfigurationItemsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetConfigurationItems", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetConfigurationItemsResponse()
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


    def ListDiscoveredResources(self, request):
        """This API is used to view the list of discovered resources.

        :param request: Request instance for ListDiscoveredResources.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.ListDiscoveredResourcesRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.ListDiscoveredResourcesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListDiscoveredResources", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListDiscoveredResourcesResponse()
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


    def ListSupportResourceTypes(self, request):
        """This API is used to query the list of all CFA supported resource types.

        :param request: Request instance for ListSupportResourceTypes.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.ListSupportResourceTypesRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.ListSupportResourceTypesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListSupportResourceTypes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListSupportResourceTypesResponse()
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


    def UpdateRecorder(self, request):
        """This API is used to modify the resources to monitor, recorder name, and other recorder configurations.

        :param request: Request instance for UpdateRecorder.
        :type request: :class:`tencentcloud.cloudaudit.v20190319.models.UpdateRecorderRequest`
        :rtype: :class:`tencentcloud.cloudaudit.v20190319.models.UpdateRecorderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateRecorder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateRecorderResponse()
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