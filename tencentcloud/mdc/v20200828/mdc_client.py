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
            headers = request.headers
            body = self.call("CreateStreamLinkFlow", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStreamLinkFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStreamLinkInput(self, request):
        """Create an input configuration for the StreamLink.

        :param request: Request instance for CreateStreamLinkInput.
        :type request: :class:`tencentcloud.mdc.v20200828.models.CreateStreamLinkInputRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateStreamLinkInputResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStreamLinkInput", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStreamLinkInputResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStreamLinkOutputInfo(self, request):
        """This API is used to create a StreamLink output.

        :param request: Request instance for CreateStreamLinkOutputInfo.
        :type request: :class:`tencentcloud.mdc.v20200828.models.CreateStreamLinkOutputInfoRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.CreateStreamLinkOutputInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStreamLinkOutputInfo", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStreamLinkOutputInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStreamLinkFlow(self, request):
        """This API is used to delete a StreamLink flow.

        :param request: Request instance for DeleteStreamLinkFlow.
        :type request: :class:`tencentcloud.mdc.v20200828.models.DeleteStreamLinkFlowRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DeleteStreamLinkFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStreamLinkFlow", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStreamLinkFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStreamLinkOutput(self, request):
        """This API is used to delete an output of a StreamLink flow.

        :param request: Request instance for DeleteStreamLinkOutput.
        :type request: :class:`tencentcloud.mdc.v20200828.models.DeleteStreamLinkOutputRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DeleteStreamLinkOutputResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStreamLinkOutput", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStreamLinkOutputResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamLinkFlow(self, request):
        """This API is used to query the configuration information of a StreamLink flow.

        :param request: Request instance for DescribeStreamLinkFlow.
        :type request: :class:`tencentcloud.mdc.v20200828.models.DescribeStreamLinkFlowRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeStreamLinkFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLinkFlow", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLinkFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamLinkFlowLogs(self, request):
        """This API is used to query the logs of a StreamLink flow.

        :param request: Request instance for DescribeStreamLinkFlowLogs.
        :type request: :class:`tencentcloud.mdc.v20200828.models.DescribeStreamLinkFlowLogsRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeStreamLinkFlowLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLinkFlowLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLinkFlowLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamLinkFlowMediaStatistics(self, request):
        """This API is used to query the media quality of a StreamLink flow.

        :param request: Request instance for DescribeStreamLinkFlowMediaStatistics.
        :type request: :class:`tencentcloud.mdc.v20200828.models.DescribeStreamLinkFlowMediaStatisticsRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeStreamLinkFlowMediaStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLinkFlowMediaStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLinkFlowMediaStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamLinkFlowRealtimeStatus(self, request):
        """This API is used to query the current status of a flow.

        :param request: Request instance for DescribeStreamLinkFlowRealtimeStatus.
        :type request: :class:`tencentcloud.mdc.v20200828.models.DescribeStreamLinkFlowRealtimeStatusRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeStreamLinkFlowRealtimeStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLinkFlowRealtimeStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLinkFlowRealtimeStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamLinkFlowSRTStatistics(self, request):
        """This API is used to query the SRT streaming performance of a StreamLink flow.

        :param request: Request instance for DescribeStreamLinkFlowSRTStatistics.
        :type request: :class:`tencentcloud.mdc.v20200828.models.DescribeStreamLinkFlowSRTStatisticsRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeStreamLinkFlowSRTStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLinkFlowSRTStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLinkFlowSRTStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamLinkFlowStatistics(self, request):
        """This API is used to query the media quality of a StreamLink flow.

        :param request: Request instance for DescribeStreamLinkFlowStatistics.
        :type request: :class:`tencentcloud.mdc.v20200828.models.DescribeStreamLinkFlowStatisticsRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeStreamLinkFlowStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLinkFlowStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLinkFlowStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamLinkFlows(self, request):
        """This API is used to query the configuration information of multiple StreamLink flows in batches.

        :param request: Request instance for DescribeStreamLinkFlows.
        :type request: :class:`tencentcloud.mdc.v20200828.models.DescribeStreamLinkFlowsRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeStreamLinkFlowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLinkFlows", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLinkFlowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamLinkRegions(self, request):
        """This API is used to query all StreamLink regions.

        :param request: Request instance for DescribeStreamLinkRegions.
        :type request: :class:`tencentcloud.mdc.v20200828.models.DescribeStreamLinkRegionsRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.DescribeStreamLinkRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLinkRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLinkRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStreamLinkFlow(self, request):
        """This API is used to modify the configuration information of a StreamLink flow.

        :param request: Request instance for ModifyStreamLinkFlow.
        :type request: :class:`tencentcloud.mdc.v20200828.models.ModifyStreamLinkFlowRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.ModifyStreamLinkFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStreamLinkFlow", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStreamLinkFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStreamLinkInput(self, request):
        """This API is used to modify an input of a StreamLink flow.

        :param request: Request instance for ModifyStreamLinkInput.
        :type request: :class:`tencentcloud.mdc.v20200828.models.ModifyStreamLinkInputRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.ModifyStreamLinkInputResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStreamLinkInput", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStreamLinkInputResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStreamLinkOutputInfo(self, request):
        """This API is used to modify an output of a StreamLink flow.

        :param request: Request instance for ModifyStreamLinkOutputInfo.
        :type request: :class:`tencentcloud.mdc.v20200828.models.ModifyStreamLinkOutputInfoRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.ModifyStreamLinkOutputInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStreamLinkOutputInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStreamLinkOutputInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartStreamLinkFlow(self, request):
        """This API is used to start a StreamLink flow.

        :param request: Request instance for StartStreamLinkFlow.
        :type request: :class:`tencentcloud.mdc.v20200828.models.StartStreamLinkFlowRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.StartStreamLinkFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartStreamLinkFlow", params, headers=headers)
            response = json.loads(body)
            model = models.StartStreamLinkFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopStreamLinkFlow(self, request):
        """This API is used to stop a StreamLink flow.

        :param request: Request instance for StopStreamLinkFlow.
        :type request: :class:`tencentcloud.mdc.v20200828.models.StopStreamLinkFlowRequest`
        :rtype: :class:`tencentcloud.mdc.v20200828.models.StopStreamLinkFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopStreamLinkFlow", params, headers=headers)
            response = json.loads(body)
            model = models.StopStreamLinkFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))