# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.mdl.v20200326 import models
from typing import Dict


class MdlClient(AbstractClient):
    _apiVersion = '2020-03-26'
    _endpoint = 'mdl.intl.tencentcloudapi.com'
    _service = 'mdl'

    async def CreateStreamLiveChannel(
            self,
            request: models.CreateStreamLiveChannelRequest,
            opts: Dict = None,
    ) -> models.CreateStreamLiveChannelResponse:
        """
        This API is used to create a StreamLive channel.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStreamLiveChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStreamLiveChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStreamLiveInput(
            self,
            request: models.CreateStreamLiveInputRequest,
            opts: Dict = None,
    ) -> models.CreateStreamLiveInputResponse:
        """
        This API is used to create a StreamLive input.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStreamLiveInput"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStreamLiveInputResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStreamLiveInputSecurityGroup(
            self,
            request: models.CreateStreamLiveInputSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.CreateStreamLiveInputSecurityGroupResponse:
        """
        This API is used to create an input security group. Up to 5 security groups are allowed.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStreamLiveInputSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStreamLiveInputSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStreamLivePlan(
            self,
            request: models.CreateStreamLivePlanRequest,
            opts: Dict = None,
    ) -> models.CreateStreamLivePlanResponse:
        """
        This API is used to create an event in the plan.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStreamLivePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStreamLivePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStreamLiveWatermark(
            self,
            request: models.CreateStreamLiveWatermarkRequest,
            opts: Dict = None,
    ) -> models.CreateStreamLiveWatermarkResponse:
        """
        This API is used to add a watermark.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStreamLiveWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStreamLiveWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWatermarkDetection(
            self,
            request: models.CreateWatermarkDetectionRequest,
            opts: Dict = None,
    ) -> models.CreateWatermarkDetectionResponse:
        """
        Create a watermark detection task
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWatermarkDetection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWatermarkDetectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamLiveChannel(
            self,
            request: models.DeleteStreamLiveChannelRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamLiveChannelResponse:
        """
        This API is used to delete a StreamLive channel.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamLiveChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamLiveChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamLiveInput(
            self,
            request: models.DeleteStreamLiveInputRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamLiveInputResponse:
        """
        This API is used to delete a StreamLive input.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamLiveInput"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamLiveInputResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamLiveInputSecurityGroup(
            self,
            request: models.DeleteStreamLiveInputSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamLiveInputSecurityGroupResponse:
        """
        This API is used to delete an input security group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamLiveInputSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamLiveInputSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamLivePlan(
            self,
            request: models.DeleteStreamLivePlanRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamLivePlanResponse:
        """
        This API is used to delete a StreamLive event.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamLivePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamLivePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamLiveWatermark(
            self,
            request: models.DeleteStreamLiveWatermarkRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamLiveWatermarkResponse:
        """
        This API is used to delete a watermark.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamLiveWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamLiveWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLiveChannel(
            self,
            request: models.DescribeStreamLiveChannelRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLiveChannelResponse:
        """
        This API is used to query a StreamLive channel.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLiveChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLiveChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLiveChannelAlerts(
            self,
            request: models.DescribeStreamLiveChannelAlertsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLiveChannelAlertsResponse:
        """
        This API is used to query the alarm information of a StreamLive channel.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLiveChannelAlerts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLiveChannelAlertsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLiveChannelInputStatistics(
            self,
            request: models.DescribeStreamLiveChannelInputStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLiveChannelInputStatisticsResponse:
        """
        This API is used to query input statistics.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLiveChannelInputStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLiveChannelInputStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLiveChannelLogs(
            self,
            request: models.DescribeStreamLiveChannelLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLiveChannelLogsResponse:
        """
        This API is used to query StreamLive channel logs, such as push event logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLiveChannelLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLiveChannelLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLiveChannelOutputStatistics(
            self,
            request: models.DescribeStreamLiveChannelOutputStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLiveChannelOutputStatisticsResponse:
        """
        This API is used to query the output statistics of a StreamLive channel.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLiveChannelOutputStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLiveChannelOutputStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLiveChannels(
            self,
            request: models.DescribeStreamLiveChannelsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLiveChannelsResponse:
        """
        This API is used to query StreamLive channels in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLiveChannels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLiveChannelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLiveInput(
            self,
            request: models.DescribeStreamLiveInputRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLiveInputResponse:
        """
        This API is used to query a StreamLive input.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLiveInput"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLiveInputResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLiveInputSecurityGroup(
            self,
            request: models.DescribeStreamLiveInputSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLiveInputSecurityGroupResponse:
        """
        This API is used to query an input security group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLiveInputSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLiveInputSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLiveInputSecurityGroups(
            self,
            request: models.DescribeStreamLiveInputSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLiveInputSecurityGroupsResponse:
        """
        This API is used to query input security groups in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLiveInputSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLiveInputSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLiveInputs(
            self,
            request: models.DescribeStreamLiveInputsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLiveInputsResponse:
        """
        This API is used to query StreamLive inputs in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLiveInputs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLiveInputsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLivePlans(
            self,
            request: models.DescribeStreamLivePlansRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLivePlansResponse:
        """
        This API is used to query the events in the plan in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLivePlans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLivePlansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLiveRegions(
            self,
            request: models.DescribeStreamLiveRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLiveRegionsResponse:
        """
        This API is used to query all StreamLive regions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLiveRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLiveRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLiveTranscodeDetail(
            self,
            request: models.DescribeStreamLiveTranscodeDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLiveTranscodeDetailResponse:
        """
        This API is used to query the transcoding information of StreamLive streams.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLiveTranscodeDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLiveTranscodeDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLiveWatermark(
            self,
            request: models.DescribeStreamLiveWatermarkRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLiveWatermarkResponse:
        """
        This API is used to query a watermark.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLiveWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLiveWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLiveWatermarks(
            self,
            request: models.DescribeStreamLiveWatermarksRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLiveWatermarksResponse:
        """
        This API is used to query multiple watermarks at a time.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLiveWatermarks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLiveWatermarksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWatermarkDetection(
            self,
            request: models.DescribeWatermarkDetectionRequest,
            opts: Dict = None,
    ) -> models.DescribeWatermarkDetectionResponse:
        """
        Describe watermark detection task
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWatermarkDetection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWatermarkDetectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWatermarkDetections(
            self,
            request: models.DescribeWatermarkDetectionsRequest,
            opts: Dict = None,
    ) -> models.DescribeWatermarkDetectionsResponse:
        """
        Batch Describe watermark detection task
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWatermarkDetections"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWatermarkDetectionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAbWatermarkPlayUrl(
            self,
            request: models.GetAbWatermarkPlayUrlRequest,
            opts: Dict = None,
    ) -> models.GetAbWatermarkPlayUrlResponse:
        """
        Get AB watermark play url.
        """
        
        kwargs = {}
        kwargs["action"] = "GetAbWatermarkPlayUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAbWatermarkPlayUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStreamLiveChannel(
            self,
            request: models.ModifyStreamLiveChannelRequest,
            opts: Dict = None,
    ) -> models.ModifyStreamLiveChannelResponse:
        """
        This API is used to modify a StreamLive channel.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStreamLiveChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStreamLiveChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStreamLiveInput(
            self,
            request: models.ModifyStreamLiveInputRequest,
            opts: Dict = None,
    ) -> models.ModifyStreamLiveInputResponse:
        """
        This API is used to modify a StreamLive input.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStreamLiveInput"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStreamLiveInputResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStreamLiveInputSecurityGroup(
            self,
            request: models.ModifyStreamLiveInputSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyStreamLiveInputSecurityGroupResponse:
        """
        This API is used to modify an input security group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStreamLiveInputSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStreamLiveInputSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStreamLiveWatermark(
            self,
            request: models.ModifyStreamLiveWatermarkRequest,
            opts: Dict = None,
    ) -> models.ModifyStreamLiveWatermarkResponse:
        """
        This API is used to modify a watermark.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStreamLiveWatermark"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStreamLiveWatermarkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryInputStreamState(
            self,
            request: models.QueryInputStreamStateRequest,
            opts: Dict = None,
    ) -> models.QueryInputStreamStateResponse:
        """
        This API is used to query the stream status of a StreamLive input.
        """
        
        kwargs = {}
        kwargs["action"] = "QueryInputStreamState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryInputStreamStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartStreamLiveChannel(
            self,
            request: models.StartStreamLiveChannelRequest,
            opts: Dict = None,
    ) -> models.StartStreamLiveChannelResponse:
        """
        This API is used to start a StreamLive channel.
        """
        
        kwargs = {}
        kwargs["action"] = "StartStreamLiveChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartStreamLiveChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopStreamLiveChannel(
            self,
            request: models.StopStreamLiveChannelRequest,
            opts: Dict = None,
    ) -> models.StopStreamLiveChannelResponse:
        """
        This API is used to stop a StreamLive channel.
        """
        
        kwargs = {}
        kwargs["action"] = "StopStreamLiveChannel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopStreamLiveChannelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)