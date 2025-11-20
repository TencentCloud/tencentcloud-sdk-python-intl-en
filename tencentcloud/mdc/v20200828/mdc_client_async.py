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
from tencentcloud.mdc.v20200828 import models
from typing import Dict


class MdcClient(AbstractClient):
    _apiVersion = '2020-08-28'
    _endpoint = 'mdc.intl.tencentcloudapi.com'
    _service = 'mdc'

    async def CreateStreamLinkFlow(
            self,
            request: models.CreateStreamLinkFlowRequest,
            opts: Dict = None,
    ) -> models.CreateStreamLinkFlowResponse:
        """
        This API is used to create a StreamLink flow.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStreamLinkFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStreamLinkFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStreamLinkInput(
            self,
            request: models.CreateStreamLinkInputRequest,
            opts: Dict = None,
    ) -> models.CreateStreamLinkInputResponse:
        """
        Create an input configuration for the StreamLink.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStreamLinkInput"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStreamLinkInputResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStreamLinkOutputInfo(
            self,
            request: models.CreateStreamLinkOutputInfoRequest,
            opts: Dict = None,
    ) -> models.CreateStreamLinkOutputInfoResponse:
        """
        This API is used to create a StreamLink output.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStreamLinkOutputInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStreamLinkOutputInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamLinkFlow(
            self,
            request: models.DeleteStreamLinkFlowRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamLinkFlowResponse:
        """
        This API is used to delete a StreamLink flow.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamLinkFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamLinkFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStreamLinkOutput(
            self,
            request: models.DeleteStreamLinkOutputRequest,
            opts: Dict = None,
    ) -> models.DeleteStreamLinkOutputResponse:
        """
        This API is used to delete an output of a StreamLink flow.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStreamLinkOutput"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStreamLinkOutputResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLinkFlow(
            self,
            request: models.DescribeStreamLinkFlowRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLinkFlowResponse:
        """
        This API is used to query the configuration information of a StreamLink flow.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLinkFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLinkFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLinkFlowLogs(
            self,
            request: models.DescribeStreamLinkFlowLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLinkFlowLogsResponse:
        """
        This API is used to query the logs of a StreamLink flow.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLinkFlowLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLinkFlowLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLinkFlowMediaStatistics(
            self,
            request: models.DescribeStreamLinkFlowMediaStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLinkFlowMediaStatisticsResponse:
        """
        This API is used to query the media quality of a StreamLink flow.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLinkFlowMediaStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLinkFlowMediaStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLinkFlowRealtimeStatus(
            self,
            request: models.DescribeStreamLinkFlowRealtimeStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLinkFlowRealtimeStatusResponse:
        """
        This API is used to query the current status of a flow.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLinkFlowRealtimeStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLinkFlowRealtimeStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLinkFlowSRTStatistics(
            self,
            request: models.DescribeStreamLinkFlowSRTStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLinkFlowSRTStatisticsResponse:
        """
        This API is used to query the SRT streaming performance of a StreamLink flow.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLinkFlowSRTStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLinkFlowSRTStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLinkFlowStatistics(
            self,
            request: models.DescribeStreamLinkFlowStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLinkFlowStatisticsResponse:
        """
        This API is used to query the media quality of a StreamLink flow.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLinkFlowStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLinkFlowStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLinkFlows(
            self,
            request: models.DescribeStreamLinkFlowsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLinkFlowsResponse:
        """
        This API is used to query the configuration information of multiple StreamLink flows in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLinkFlows"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLinkFlowsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamLinkRegions(
            self,
            request: models.DescribeStreamLinkRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamLinkRegionsResponse:
        """
        This API is used to query all StreamLink regions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamLinkRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamLinkRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStreamLinkFlow(
            self,
            request: models.ModifyStreamLinkFlowRequest,
            opts: Dict = None,
    ) -> models.ModifyStreamLinkFlowResponse:
        """
        This API is used to modify the configuration information of a StreamLink flow.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStreamLinkFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStreamLinkFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStreamLinkInput(
            self,
            request: models.ModifyStreamLinkInputRequest,
            opts: Dict = None,
    ) -> models.ModifyStreamLinkInputResponse:
        """
        This API is used to modify an input of a StreamLink flow.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStreamLinkInput"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStreamLinkInputResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyStreamLinkOutputInfo(
            self,
            request: models.ModifyStreamLinkOutputInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyStreamLinkOutputInfoResponse:
        """
        This API is used to modify an output of a StreamLink flow.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyStreamLinkOutputInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyStreamLinkOutputInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartStreamLinkFlow(
            self,
            request: models.StartStreamLinkFlowRequest,
            opts: Dict = None,
    ) -> models.StartStreamLinkFlowResponse:
        """
        This API is used to start a StreamLink flow.
        """
        
        kwargs = {}
        kwargs["action"] = "StartStreamLinkFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartStreamLinkFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopStreamLinkFlow(
            self,
            request: models.StopStreamLinkFlowRequest,
            opts: Dict = None,
    ) -> models.StopStreamLinkFlowResponse:
        """
        This API is used to stop a StreamLink flow.
        """
        
        kwargs = {}
        kwargs["action"] = "StopStreamLinkFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopStreamLinkFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)