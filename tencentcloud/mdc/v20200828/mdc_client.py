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
from tencentcloud.mdc.v20200828 import models


class MdcClient(AbstractClient):
    _apiVersion = '2020-08-28'
    _endpoint = 'mdc.tencentcloudapi.com'
    _service = 'mdc'


    def CreateStreamLinkFlow(self, request):
        """This API is used to create a StreamLink flow.

        :param request: Request instance for CreateStreamLinkFlow.
        :type request: :class:`tencentcloud.mdc.v20200828.models.CreateStreamLinkFlowRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateStreamLinkFlowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateStreamLinkFlow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateStreamLinkFlowResponse()
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


    def DeleteStreamLinkFlow(self, request):
        """This API is used to delete a StreamLink flow.

        :param request: Request instance for DeleteStreamLinkFlow.
        :type request: :class:`tencentcloud.mdc.v20200828.models.DeleteStreamLinkFlowRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DeleteStreamLinkFlowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteStreamLinkFlow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteStreamLinkFlowResponse()
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


    def DeleteStreamLinkOutput(self, request):
        """This API is used to delete an output of a StreamLink flow.

        :param request: Request instance for DeleteStreamLinkOutput.
        :type request: :class:`tencentcloud.mdc.v20200828.models.DeleteStreamLinkOutputRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DeleteStreamLinkOutputResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteStreamLinkOutput", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteStreamLinkOutputResponse()
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


    def DescribeStreamLinkFlow(self, request):
        """This API is used to query the configuration information of a StreamLink flow.

        :param request: Request instance for DescribeStreamLinkFlow.
        :type request: :class:`tencentcloud.mdc.v20200828.models.DescribeStreamLinkFlowRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeStreamLinkFlowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStreamLinkFlow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStreamLinkFlowResponse()
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


    def DescribeStreamLinkFlows(self, request):
        """This API is used to query the configuration information of multiple StreamLink flows in batches.

        :param request: Request instance for DescribeStreamLinkFlows.
        :type request: :class:`tencentcloud.mdc.v20200828.models.DescribeStreamLinkFlowsRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeStreamLinkFlowsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStreamLinkFlows", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStreamLinkFlowsResponse()
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


    def DescribeStreamLinkRegions(self, request):
        """This API is used to query all StreamLink regions.

        :param request: Request instance for DescribeStreamLinkRegions.
        :type request: :class:`tencentcloud.mdc.v20200828.models.DescribeStreamLinkRegionsRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeStreamLinkRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStreamLinkRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStreamLinkRegionsResponse()
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


    def ModifyStreamLinkFlow(self, request):
        """This API is used to modify the configuration information of a StreamLink flow.

        :param request: Request instance for ModifyStreamLinkFlow.
        :type request: :class:`tencentcloud.mdc.v20200828.models.ModifyStreamLinkFlowRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.ModifyStreamLinkFlowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyStreamLinkFlow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyStreamLinkFlowResponse()
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


    def StartStreamLinkFlow(self, request):
        """This API is used to start a StreamLink flow.

        :param request: Request instance for StartStreamLinkFlow.
        :type request: :class:`tencentcloud.mdc.v20200828.models.StartStreamLinkFlowRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.StartStreamLinkFlowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartStreamLinkFlow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartStreamLinkFlowResponse()
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


    def StopStreamLinkFlow(self, request):
        """This API is used to stop a StreamLink flow.

        :param request: Request instance for StopStreamLinkFlow.
        :type request: :class:`tencentcloud.mdc.v20200828.models.StopStreamLinkFlowRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.StopStreamLinkFlowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopStreamLinkFlow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopStreamLinkFlowResponse()
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