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
from tencentcloud.mdl.v20200326 import models


class MdlClient(AbstractClient):
    _apiVersion = '2020-03-26'
    _endpoint = 'mdl.tencentcloudapi.com'
    _service = 'mdl'


    def CreateStreamLiveChannel(self, request):
        """This API is used to create a StreamLive channel.

        :param request: Request instance for CreateStreamLiveChannel.
        :type request: :class:`tencentcloud.mdl.v20200326.models.CreateStreamLiveChannelRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.CreateStreamLiveChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStreamLiveChannel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStreamLiveChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateStreamLiveInput(self, request):
        """This API is used to create a StreamLive input.

        :param request: Request instance for CreateStreamLiveInput.
        :type request: :class:`tencentcloud.mdl.v20200326.models.CreateStreamLiveInputRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.CreateStreamLiveInputResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStreamLiveInput", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStreamLiveInputResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateStreamLiveInputSecurityGroup(self, request):
        """This API is used to create an input security group. Up to 5 security groups are allowed.

        :param request: Request instance for CreateStreamLiveInputSecurityGroup.
        :type request: :class:`tencentcloud.mdl.v20200326.models.CreateStreamLiveInputSecurityGroupRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.CreateStreamLiveInputSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStreamLiveInputSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStreamLiveInputSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateStreamLivePlan(self, request):
        """This API is used to create an event in the plan.

        :param request: Request instance for CreateStreamLivePlan.
        :type request: :class:`tencentcloud.mdl.v20200326.models.CreateStreamLivePlanRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.CreateStreamLivePlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStreamLivePlan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStreamLivePlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateStreamLiveWatermark(self, request):
        """This API is used to add a watermark.

        :param request: Request instance for CreateStreamLiveWatermark.
        :type request: :class:`tencentcloud.mdl.v20200326.models.CreateStreamLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.CreateStreamLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStreamLiveWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStreamLiveWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteStreamLiveChannel(self, request):
        """This API is used to delete a StreamLive channel.

        :param request: Request instance for DeleteStreamLiveChannel.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DeleteStreamLiveChannelRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DeleteStreamLiveChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStreamLiveChannel", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStreamLiveChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteStreamLiveInput(self, request):
        """This API is used to delete a StreamLive input.

        :param request: Request instance for DeleteStreamLiveInput.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DeleteStreamLiveInputRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DeleteStreamLiveInputResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStreamLiveInput", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStreamLiveInputResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteStreamLiveInputSecurityGroup(self, request):
        """This API is used to delete an input security group.

        :param request: Request instance for DeleteStreamLiveInputSecurityGroup.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DeleteStreamLiveInputSecurityGroupRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DeleteStreamLiveInputSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStreamLiveInputSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStreamLiveInputSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteStreamLivePlan(self, request):
        """This API is used to delete a StreamLive event.

        :param request: Request instance for DeleteStreamLivePlan.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DeleteStreamLivePlanRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DeleteStreamLivePlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStreamLivePlan", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStreamLivePlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteStreamLiveWatermark(self, request):
        """This API is used to delete a watermark.

        :param request: Request instance for DeleteStreamLiveWatermark.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DeleteStreamLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DeleteStreamLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStreamLiveWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStreamLiveWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStreamLiveChannel(self, request):
        """This API is used to query a StreamLive channel.

        :param request: Request instance for DescribeStreamLiveChannel.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveChannelRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLiveChannel", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLiveChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStreamLiveChannelAlerts(self, request):
        """This API is used to query the alarm information of a StreamLive channel.

        :param request: Request instance for DescribeStreamLiveChannelAlerts.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveChannelAlertsRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveChannelAlertsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLiveChannelAlerts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLiveChannelAlertsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStreamLiveChannelInputStatistics(self, request):
        """This API is used to query input statistics.

        :param request: Request instance for DescribeStreamLiveChannelInputStatistics.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveChannelInputStatisticsRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveChannelInputStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLiveChannelInputStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLiveChannelInputStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStreamLiveChannelLogs(self, request):
        """This API is used to query StreamLive channel logs, such as push event logs.

        :param request: Request instance for DescribeStreamLiveChannelLogs.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveChannelLogsRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveChannelLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLiveChannelLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLiveChannelLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStreamLiveChannelOutputStatistics(self, request):
        """This API is used to query the output statistics of a StreamLive channel.

        :param request: Request instance for DescribeStreamLiveChannelOutputStatistics.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveChannelOutputStatisticsRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveChannelOutputStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLiveChannelOutputStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLiveChannelOutputStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStreamLiveChannels(self, request):
        """This API is used to query StreamLive channels in batches.

        :param request: Request instance for DescribeStreamLiveChannels.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveChannelsRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveChannelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLiveChannels", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLiveChannelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStreamLiveInput(self, request):
        """This API is used to query a StreamLive input.

        :param request: Request instance for DescribeStreamLiveInput.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveInputRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveInputResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLiveInput", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLiveInputResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStreamLiveInputSecurityGroup(self, request):
        """This API is used to query an input security group.

        :param request: Request instance for DescribeStreamLiveInputSecurityGroup.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveInputSecurityGroupRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveInputSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLiveInputSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLiveInputSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStreamLiveInputSecurityGroups(self, request):
        """This API is used to query input security groups in batches.

        :param request: Request instance for DescribeStreamLiveInputSecurityGroups.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveInputSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveInputSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLiveInputSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLiveInputSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStreamLiveInputs(self, request):
        """This API is used to query StreamLive inputs in batches.

        :param request: Request instance for DescribeStreamLiveInputs.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveInputsRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveInputsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLiveInputs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLiveInputsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStreamLivePlans(self, request):
        """This API is used to query the events in the plan in batches.

        :param request: Request instance for DescribeStreamLivePlans.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLivePlansRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLivePlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLivePlans", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLivePlansResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStreamLiveRegions(self, request):
        """This API is used to query all StreamLive regions.

        :param request: Request instance for DescribeStreamLiveRegions.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveRegionsRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLiveRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLiveRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStreamLiveTranscodeDetail(self, request):
        """This API is used to query the transcoding information of StreamLive streams.

        :param request: Request instance for DescribeStreamLiveTranscodeDetail.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveTranscodeDetailRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveTranscodeDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLiveTranscodeDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLiveTranscodeDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStreamLiveWatermark(self, request):
        """This API is used to query a watermark.

        :param request: Request instance for DescribeStreamLiveWatermark.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLiveWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLiveWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStreamLiveWatermarks(self, request):
        """This API is used to query multiple watermarks at a time.

        :param request: Request instance for DescribeStreamLiveWatermarks.
        :type request: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveWatermarksRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.DescribeStreamLiveWatermarksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamLiveWatermarks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamLiveWatermarksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyStreamLiveChannel(self, request):
        """This API is used to modify a StreamLive channel.

        :param request: Request instance for ModifyStreamLiveChannel.
        :type request: :class:`tencentcloud.mdl.v20200326.models.ModifyStreamLiveChannelRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.ModifyStreamLiveChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStreamLiveChannel", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStreamLiveChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyStreamLiveInput(self, request):
        """This API is used to modify a StreamLive input.

        :param request: Request instance for ModifyStreamLiveInput.
        :type request: :class:`tencentcloud.mdl.v20200326.models.ModifyStreamLiveInputRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.ModifyStreamLiveInputResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStreamLiveInput", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStreamLiveInputResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyStreamLiveInputSecurityGroup(self, request):
        """This API is used to modify an input security group.

        :param request: Request instance for ModifyStreamLiveInputSecurityGroup.
        :type request: :class:`tencentcloud.mdl.v20200326.models.ModifyStreamLiveInputSecurityGroupRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.ModifyStreamLiveInputSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStreamLiveInputSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStreamLiveInputSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyStreamLiveWatermark(self, request):
        """This API is used to modify a watermark.

        :param request: Request instance for ModifyStreamLiveWatermark.
        :type request: :class:`tencentcloud.mdl.v20200326.models.ModifyStreamLiveWatermarkRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.ModifyStreamLiveWatermarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStreamLiveWatermark", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStreamLiveWatermarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartStreamLiveChannel(self, request):
        """This API is used to start a StreamLive channel.

        :param request: Request instance for StartStreamLiveChannel.
        :type request: :class:`tencentcloud.mdl.v20200326.models.StartStreamLiveChannelRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.StartStreamLiveChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartStreamLiveChannel", params, headers=headers)
            response = json.loads(body)
            model = models.StartStreamLiveChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopStreamLiveChannel(self, request):
        """This API is used to stop a StreamLive channel.

        :param request: Request instance for StopStreamLiveChannel.
        :type request: :class:`tencentcloud.mdl.v20200326.models.StopStreamLiveChannelRequest`
        :rtype: :class:`tencentcloud.mdl.v20200326.models.StopStreamLiveChannelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopStreamLiveChannel", params, headers=headers)
            response = json.loads(body)
            model = models.StopStreamLiveChannelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)