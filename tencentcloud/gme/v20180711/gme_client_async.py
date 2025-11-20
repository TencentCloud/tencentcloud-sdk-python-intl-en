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
from tencentcloud.gme.v20180711 import models
from typing import Dict


class GmeClient(AbstractClient):
    _apiVersion = '2018-07-11'
    _endpoint = 'gme.intl.tencentcloudapi.com'
    _service = 'gme'

    async def CreateApp(
            self,
            request: models.CreateAppRequest,
            opts: Dict = None,
    ) -> models.CreateAppResponse:
        """
        This API is used to create a GME application.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoomMember(
            self,
            request: models.DeleteRoomMemberRequest,
            opts: Dict = None,
    ) -> models.DeleteRoomMemberResponse:
        """
        This API is used to delete a room or remove members from the room.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoomMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoomMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAppStatistics(
            self,
            request: models.DescribeAppStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeAppStatisticsResponse:
        """
        This API is used to query the usage statistics of a GME application, including those of Voice Chat, Voice Message Service, Voice Analysis, etc. The maximum query period is the past 30 days.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAppStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAppStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationData(
            self,
            request: models.DescribeApplicationDataRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationDataResponse:
        """
        This API is used to query data details for up to the past 90 days.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordInfo(
            self,
            request: models.DescribeRecordInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordInfoResponse:
        """
        This API is used to query a recording task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskInfo(
            self,
            request: models.DescribeTaskInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskInfoResponse:
        """
        This API is used to query the recording task in a room.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAppStatus(
            self,
            request: models.ModifyAppStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAppStatusResponse:
        """
        This API is used to change the status of an application.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAppStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAppStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRecordInfo(
            self,
            request: models.ModifyRecordInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyRecordInfoResponse:
        """
        This API is used to modify recording configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRecordInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRecordInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartRecord(
            self,
            request: models.StartRecordRequest,
            opts: Dict = None,
    ) -> models.StartRecordResponse:
        """
        This API is used to start recording.
        """
        
        kwargs = {}
        kwargs["action"] = "StartRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopRecord(
            self,
            request: models.StopRecordRequest,
            opts: Dict = None,
    ) -> models.StopRecordResponse:
        """
        This API is used to stop recording.
        """
        
        kwargs = {}
        kwargs["action"] = "StopRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)