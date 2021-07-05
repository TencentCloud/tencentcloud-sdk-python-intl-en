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
from tencentcloud.emr.v20190103 import models


class EmrClient(AbstractClient):
    _apiVersion = '2019-01-03'
    _endpoint = 'emr.tencentcloudapi.com'
    _service = 'emr'


    def CreateInstance(self, request):
        """This API is used to create EMR instance.

        :param request: Request instance for CreateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.CreateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.CreateInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateInstanceResponse()
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


    def DescribeClusterNodes(self, request):
        """This API is used to query the information of a hardware node.

        :param request: Request instance for DescribeClusterNodes.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeClusterNodesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeClusterNodesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusterNodes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterNodesResponse()
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


    def DescribeInstances(self, request):
        """This API is used to query EMR instances.

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesResponse()
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


    def InquiryPriceCreateInstance(self, request):
        """This API is used to query price of instance creation.

        :param request: Request instance for InquiryPriceCreateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceCreateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceCreateInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceCreateInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceCreateInstanceResponse()
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


    def InquiryPriceRenewInstance(self, request):
        """This API is used to query the price for renewal.

        :param request: Request instance for InquiryPriceRenewInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceRenewInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceRenewInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceRenewInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceRenewInstanceResponse()
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


    def InquiryPriceScaleOutInstance(self, request):
        """This API is used to query price of scale-out.

        :param request: Request instance for InquiryPriceScaleOutInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceScaleOutInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceScaleOutInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceScaleOutInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceScaleOutInstanceResponse()
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


    def InquiryPriceUpdateInstance(self, request):
        """This API is used to query price of scaling.

        :param request: Request instance for InquiryPriceUpdateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceUpdateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceUpdateInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceUpdateInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceUpdateInstanceResponse()
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


    def ScaleOutInstance(self, request):
        """This API is used to scale out instance.

        :param request: Request instance for ScaleOutInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.ScaleOutInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ScaleOutInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ScaleOutInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScaleOutInstanceResponse()
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


    def TerminateInstance(self, request):
        """This API is used to terminate an EMR instance. It is only supported in the official paid edition of EMR.

        :param request: Request instance for TerminateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.TerminateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.TerminateInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateInstanceResponse()
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


    def TerminateTasks(self, request):
        """This API is used to terminate a task node.

        :param request: Request instance for TerminateTasks.
        :type request: :class:`tencentcloud.emr.v20190103.models.TerminateTasksRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.TerminateTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateTasksResponse()
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