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
from tencentcloud.mdc.v20200828 import models


class MdcClient(AbstractClient):
    _apiVersion = '2020-08-28'
    _endpoint = 'mdc.tencentcloudapi.com'


    def CreateMediaConnectFlow(self, request):
        """This API is used to create the configuration of a MediaConnect flow.

        :param request: Request instance for CreateMediaConnectFlow.
        :type request: :class:`tencentcloud.mdc.v20200828.models.CreateMediaConnectFlowRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateMediaConnectFlowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMediaConnectFlow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMediaConnectFlowResponse()
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


    def CreateMediaConnectOutput(self, request):
        """This API is used to create the output information of a MediaConnect flow.

        :param request: Request instance for CreateMediaConnectOutput.
        :type request: :class:`tencentcloud.mdc.v20200828.models.CreateMediaConnectOutputRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateMediaConnectOutputResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMediaConnectOutput", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMediaConnectOutputResponse()
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


    def DeleteMediaConnectFlow(self, request):
        """This API is used to delete the configuration of a MediaConnect flow.

        :param request: Request instance for DeleteMediaConnectFlow.
        :type request: :class:`tencentcloud.mdc.v20200828.models.DeleteMediaConnectFlowRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DeleteMediaConnectFlowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMediaConnectFlow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMediaConnectFlowResponse()
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


    def DeleteMediaConnectOutput(self, request):
        """This API is used to delete the output configuration of a MediaConnect flow.

        :param request: Request instance for DeleteMediaConnectOutput.
        :type request: :class:`tencentcloud.mdc.v20200828.models.DeleteMediaConnectOutputRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DeleteMediaConnectOutputResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMediaConnectOutput", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMediaConnectOutputResponse()
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


    def DescribeMediaConnectFlow(self, request):
        """This API is used to query the configuration information of a MediaConnect flow.

        :param request: Request instance for DescribeMediaConnectFlow.
        :type request: :class:`tencentcloud.mdc.v20200828.models.DescribeMediaConnectFlowRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeMediaConnectFlowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMediaConnectFlow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediaConnectFlowResponse()
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


    def DescribeMediaConnectFlows(self, request):
        """This API is used to query the configuration information of multiple MediaConnect flows in batches.

        :param request: Request instance for DescribeMediaConnectFlows.
        :type request: :class:`tencentcloud.mdc.v20200828.models.DescribeMediaConnectFlowsRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeMediaConnectFlowsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMediaConnectFlows", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediaConnectFlowsResponse()
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


    def ModifyMediaConnectFlow(self, request):
        """This API is used to modify the configuration information of a MediaConnect flow.

        :param request: Request instance for ModifyMediaConnectFlow.
        :type request: :class:`tencentcloud.mdc.v20200828.models.ModifyMediaConnectFlowRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.ModifyMediaConnectFlowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMediaConnectFlow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMediaConnectFlowResponse()
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


    def ModifyMediaConnectInput(self, request):
        """This API is used to modify the input information of a MediaConnect flow.

        :param request: Request instance for ModifyMediaConnectInput.
        :type request: :class:`tencentcloud.mdc.v20200828.models.ModifyMediaConnectInputRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.ModifyMediaConnectInputResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMediaConnectInput", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMediaConnectInputResponse()
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


    def ModifyMediaConnectOutput(self, request):
        """This API is used to modify the output configuration of a MediaConnect flow.

        :param request: Request instance for ModifyMediaConnectOutput.
        :type request: :class:`tencentcloud.mdc.v20200828.models.ModifyMediaConnectOutputRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.ModifyMediaConnectOutputResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMediaConnectOutput", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMediaConnectOutputResponse()
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


    def StartMediaConnectFlow(self, request):
        """This API is used to start a MediaConnect flow.

        :param request: Request instance for StartMediaConnectFlow.
        :type request: :class:`tencentcloud.mdc.v20200828.models.StartMediaConnectFlowRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.StartMediaConnectFlowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartMediaConnectFlow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartMediaConnectFlowResponse()
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


    def StopMediaConnectFlow(self, request):
        """This API is used to stop a MediaConnect flow.

        :param request: Request instance for StopMediaConnectFlow.
        :type request: :class:`tencentcloud.mdc.v20200828.models.StopMediaConnectFlowRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.StopMediaConnectFlowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopMediaConnectFlow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopMediaConnectFlowResponse()
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