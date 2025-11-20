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
from tencentcloud.tiw.v20190919 import models
from typing import Dict


class TiwClient(AbstractClient):
    _apiVersion = '2019-09-19'
    _endpoint = 'tiw.intl.tencentcloudapi.com'
    _service = 'tiw'

    async def ApplyTiwTrial(
            self,
            request: models.ApplyTiwTrialRequest,
            opts: Dict = None,
    ) -> models.ApplyTiwTrialResponse:
        """
        This API is used to apply for a Tencent Interactive Whiteboard trial (15-day by default).
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyTiwTrial"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyTiwTrialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplication(
            self,
            request: models.CreateApplicationRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationResponse:
        """
        This API is used to create a whiteboard application.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSnapshotTask(
            self,
            request: models.CreateSnapshotTaskRequest,
            opts: Dict = None,
    ) -> models.CreateSnapshotTaskResponse:
        """
        This API is used to create a whiteboard snapshot task. If a callback URL is provided, the whiteboard snapshot result is sent to the callback URL after the task is complete.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSnapshotTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSnapshotTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTranscode(
            self,
            request: models.CreateTranscodeRequest,
            opts: Dict = None,
    ) -> models.CreateTranscodeResponse:
        """
        This API is used to create a document transcoding task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTranscode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTranscodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVideoGenerationTask(
            self,
            request: models.CreateVideoGenerationTaskRequest,
            opts: Dict = None,
    ) -> models.CreateVideoGenerationTaskResponse:
        """
        This API is used to create a recording video generation task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVideoGenerationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVideoGenerationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAPIService(
            self,
            request: models.DescribeAPIServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeAPIServiceResponse:
        """
        This API is used to query the information about other cloud products by using the service role.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAPIService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAPIServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationInfos(
            self,
            request: models.DescribeApplicationInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationInfosResponse:
        """
        This API is used to query the details of a whiteboard application.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationUsage(
            self,
            request: models.DescribeApplicationUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationUsageResponse:
        """
        This API is used to query the subproduct usage of Tencent Interactive Whiteboard.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBoardSDKLog(
            self,
            request: models.DescribeBoardSDKLogRequest,
            opts: Dict = None,
    ) -> models.DescribeBoardSDKLogResponse:
        """
        This API is used to query the logs of a whiteboard application on a client.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBoardSDKLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBoardSDKLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIMApplications(
            self,
            request: models.DescribeIMApplicationsRequest,
            opts: Dict = None,
    ) -> models.DescribeIMApplicationsResponse:
        """
        This API is used to query the instant messaging (IM) applications that are available for creating a whiteboard application.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIMApplications"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIMApplicationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOnlineRecord(
            self,
            request: models.DescribeOnlineRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeOnlineRecordResponse:
        """
        This API is used to query the status and result of a real-time recording task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOnlineRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOnlineRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOnlineRecordCallback(
            self,
            request: models.DescribeOnlineRecordCallbackRequest,
            opts: Dict = None,
    ) -> models.DescribeOnlineRecordCallbackResponse:
        """
        This API is used to query the real-time recording callback address.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOnlineRecordCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOnlineRecordCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePostpaidUsage(
            self,
            request: models.DescribePostpaidUsageRequest,
            opts: Dict = None,
    ) -> models.DescribePostpaidUsageResponse:
        """
        This API is used to query the pay-as-you-go usage of a user.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePostpaidUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePostpaidUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQualityMetrics(
            self,
            request: models.DescribeQualityMetricsRequest,
            opts: Dict = None,
    ) -> models.DescribeQualityMetricsResponse:
        """
        This API is used to query the quality data of a whiteboard application.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQualityMetrics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQualityMetricsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordSearch(
            self,
            request: models.DescribeRecordSearchRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordSearchResponse:
        """
        This API is used to query real-time recording tasks by room ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordSearch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordSearchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoomList(
            self,
            request: models.DescribeRoomListRequest,
            opts: Dict = None,
    ) -> models.DescribeRoomListResponse:
        """
        This API is used to query the rooms of a whiteboard application.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoomList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoomListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotTask(
            self,
            request: models.DescribeSnapshotTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotTaskResponse:
        """
        This API is used to query the information about a whiteboard snapshot task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTIWDailyUsage(
            self,
            request: models.DescribeTIWDailyUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeTIWDailyUsageResponse:
        """
        This API is used to query the daily billable usage of a whiteboard application.
        1. The period queried per request cannot be longer than 31 days.
        2. Due to statistics delays and other reasons, you cannot query the usage data of the current day. You can query today's usage after 7:00 tomorrow.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTIWDailyUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTIWDailyUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTIWRoomDailyUsage(
            self,
            request: models.DescribeTIWRoomDailyUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeTIWRoomDailyUsageResponse:
        """
        This API is used to query the daily billable usage by each room of a whiteboard application.
        1. The period queried per request cannot be longer than 31 days.
        2. Due to statistics delays and other reasons, you cannot query the usage data of the current day. You can query today's usage after 7:00 tomorrow.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTIWRoomDailyUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTIWRoomDailyUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTranscode(
            self,
            request: models.DescribeTranscodeRequest,
            opts: Dict = None,
    ) -> models.DescribeTranscodeResponse:
        """
        This API is used to query the progress and result of a document transcoding task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTranscode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTranscodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTranscodeCallback(
            self,
            request: models.DescribeTranscodeCallbackRequest,
            opts: Dict = None,
    ) -> models.DescribeTranscodeCallbackResponse:
        """
        This API is used to query the document transcoding callback address.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTranscodeCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTranscodeCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTranscodeSearch(
            self,
            request: models.DescribeTranscodeSearchRequest,
            opts: Dict = None,
    ) -> models.DescribeTranscodeSearchResponse:
        """
        This API is used to query transcoding tasks by document name.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTranscodeSearch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTranscodeSearchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsageSummary(
            self,
            request: models.DescribeUsageSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeUsageSummaryResponse:
        """
        This API is used to query the summary of subproduct usage within a specified period of time.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsageSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsageSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserList(
            self,
            request: models.DescribeUserListRequest,
            opts: Dict = None,
    ) -> models.DescribeUserListResponse:
        """
        This API is used to query the users of a whiteboard application.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserResources(
            self,
            request: models.DescribeUserResourcesRequest,
            opts: Dict = None,
    ) -> models.DescribeUserResourcesResponse:
        """
        This API is used to query user resources.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserStatus(
            self,
            request: models.DescribeUserStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeUserStatusResponse:
        """
        This API is used to query the Tencent Interactive Whiteboard service status of a user, including the activation status and validity period.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoGenerationTask(
            self,
            request: models.DescribeVideoGenerationTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoGenerationTaskResponse:
        """
        This API is used to query the status and result of a recording video generation task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoGenerationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoGenerationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVideoGenerationTaskCallback(
            self,
            request: models.DescribeVideoGenerationTaskCallbackRequest,
            opts: Dict = None,
    ) -> models.DescribeVideoGenerationTaskCallbackResponse:
        """
        This API is used to query the callback URL for recording video generation.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVideoGenerationTaskCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVideoGenerationTaskCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWhiteboardApplicationConfig(
            self,
            request: models.DescribeWhiteboardApplicationConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeWhiteboardApplicationConfigResponse:
        """
        This API is used to query the task-related configurations of a whiteboard application, including the bucket and callback URL.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWhiteboardApplicationConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWhiteboardApplicationConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWhiteboardBucketConfig(
            self,
            request: models.DescribeWhiteboardBucketConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeWhiteboardBucketConfigResponse:
        """
        This API is used to query the bucket configurations for document transcoding and real-time recording.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWhiteboardBucketConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWhiteboardBucketConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWhiteboardPush(
            self,
            request: models.DescribeWhiteboardPushRequest,
            opts: Dict = None,
    ) -> models.DescribeWhiteboardPushResponse:
        """
        This API is used to query the status and result of a whiteboard push task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWhiteboardPush"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWhiteboardPushResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWhiteboardPushCallback(
            self,
            request: models.DescribeWhiteboardPushCallbackRequest,
            opts: Dict = None,
    ) -> models.DescribeWhiteboardPushCallbackResponse:
        """
        This API is used to query the whiteboard push callback URL.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWhiteboardPushCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWhiteboardPushCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWhiteboardPushSearch(
            self,
            request: models.DescribeWhiteboardPushSearchRequest,
            opts: Dict = None,
    ) -> models.DescribeWhiteboardPushSearchResponse:
        """
        This API is used to query whiteboard push tasks by room ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWhiteboardPushSearch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWhiteboardPushSearchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplication(
            self,
            request: models.ModifyApplicationRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationResponse:
        """
        This API is used to modify a whiteboard application.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoRenewFlag(
            self,
            request: models.ModifyAutoRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoRenewFlagResponse:
        """
        This API is used to set auto-renewal for a Tencent Interactive Whiteboard monthly feature package.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWhiteboardApplicationConfig(
            self,
            request: models.ModifyWhiteboardApplicationConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyWhiteboardApplicationConfigResponse:
        """
        This API is used to modify the task-related configurations of a whiteboard application, including the bucket and callback URL.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWhiteboardApplicationConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWhiteboardApplicationConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWhiteboardBucketConfig(
            self,
            request: models.ModifyWhiteboardBucketConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyWhiteboardBucketConfigResponse:
        """
        This API is used to modify the bucket configurations for document transcoding and real-time recording.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWhiteboardBucketConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWhiteboardBucketConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PauseOnlineRecord(
            self,
            request: models.PauseOnlineRecordRequest,
            opts: Dict = None,
    ) -> models.PauseOnlineRecordResponse:
        """
        This API is used to pause real-time recording.
        """
        
        kwargs = {}
        kwargs["action"] = "PauseOnlineRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PauseOnlineRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeOnlineRecord(
            self,
            request: models.ResumeOnlineRecordRequest,
            opts: Dict = None,
    ) -> models.ResumeOnlineRecordResponse:
        """
        This API is used to resume real-time recording.
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeOnlineRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeOnlineRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetOnlineRecordCallback(
            self,
            request: models.SetOnlineRecordCallbackRequest,
            opts: Dict = None,
    ) -> models.SetOnlineRecordCallbackResponse:
        """
        This API is used to set the real-time recording callback address. For the callback format, please [see here](https://www.tencentcloud.com/document/product/1176/55569).
        """
        
        kwargs = {}
        kwargs["action"] = "SetOnlineRecordCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetOnlineRecordCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetOnlineRecordCallbackKey(
            self,
            request: models.SetOnlineRecordCallbackKeyRequest,
            opts: Dict = None,
    ) -> models.SetOnlineRecordCallbackKeyResponse:
        """
        This API is used to set the callback authentication key for real-time recording. For more information, see [Event Notification](https://www.tencentcloud.com/document/product/1176/55569).
        """
        
        kwargs = {}
        kwargs["action"] = "SetOnlineRecordCallbackKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetOnlineRecordCallbackKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetTranscodeCallback(
            self,
            request: models.SetTranscodeCallbackRequest,
            opts: Dict = None,
    ) -> models.SetTranscodeCallbackResponse:
        """
        This API is used to set the callback address for document transcoding. For the callback format, please [see here](https://www.tencentcloud.com/document/product/1176/55569).
        """
        
        kwargs = {}
        kwargs["action"] = "SetTranscodeCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetTranscodeCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetTranscodeCallbackKey(
            self,
            request: models.SetTranscodeCallbackKeyRequest,
            opts: Dict = None,
    ) -> models.SetTranscodeCallbackKeyResponse:
        """
        This API is used to set the callback authentication key for document transcoding. For more information, see [Event Notification](https://www.tencentcloud.com/document/product/1176/55569).
        """
        
        kwargs = {}
        kwargs["action"] = "SetTranscodeCallbackKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetTranscodeCallbackKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetVideoGenerationTaskCallback(
            self,
            request: models.SetVideoGenerationTaskCallbackRequest,
            opts: Dict = None,
    ) -> models.SetVideoGenerationTaskCallbackResponse:
        """
        This API is used to set the callback URL for recording video generation.
        """
        
        kwargs = {}
        kwargs["action"] = "SetVideoGenerationTaskCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetVideoGenerationTaskCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetVideoGenerationTaskCallbackKey(
            self,
            request: models.SetVideoGenerationTaskCallbackKeyRequest,
            opts: Dict = None,
    ) -> models.SetVideoGenerationTaskCallbackKeyResponse:
        """
        This API is used to set the callback authentication key for recording video generation.
        """
        
        kwargs = {}
        kwargs["action"] = "SetVideoGenerationTaskCallbackKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetVideoGenerationTaskCallbackKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetWhiteboardPushCallback(
            self,
            request: models.SetWhiteboardPushCallbackRequest,
            opts: Dict = None,
    ) -> models.SetWhiteboardPushCallbackResponse:
        """
        This API is used to set the whiteboard push callback URL. For more information, see [Event Notification](https://www.tencentcloud.com/document/product/1176/55569).
        """
        
        kwargs = {}
        kwargs["action"] = "SetWhiteboardPushCallback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetWhiteboardPushCallbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetWhiteboardPushCallbackKey(
            self,
            request: models.SetWhiteboardPushCallbackKeyRequest,
            opts: Dict = None,
    ) -> models.SetWhiteboardPushCallbackKeyResponse:
        """
        This API is used to set the callback authentication key for whiteboard push. For more information, see [Event Notification](https://www.tencentcloud.com/document/product/1176/55569).
        """
        
        kwargs = {}
        kwargs["action"] = "SetWhiteboardPushCallbackKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetWhiteboardPushCallbackKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartOnlineRecord(
            self,
            request: models.StartOnlineRecordRequest,
            opts: Dict = None,
    ) -> models.StartOnlineRecordResponse:
        """
        This API is used to start a real-time recording task.
        """
        
        kwargs = {}
        kwargs["action"] = "StartOnlineRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartOnlineRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartWhiteboardPush(
            self,
            request: models.StartWhiteboardPushRequest,
            opts: Dict = None,
    ) -> models.StartWhiteboardPushResponse:
        """
        This API is used to start a whiteboard push task.
        """
        
        kwargs = {}
        kwargs["action"] = "StartWhiteboardPush"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartWhiteboardPushResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopOnlineRecord(
            self,
            request: models.StopOnlineRecordRequest,
            opts: Dict = None,
    ) -> models.StopOnlineRecordResponse:
        """
        This API is used to stop real-time recording.
        """
        
        kwargs = {}
        kwargs["action"] = "StopOnlineRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopOnlineRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopWhiteboardPush(
            self,
            request: models.StopWhiteboardPushRequest,
            opts: Dict = None,
    ) -> models.StopWhiteboardPushResponse:
        """
        This API is used to stop a whiteboard push task.
        """
        
        kwargs = {}
        kwargs["action"] = "StopWhiteboardPush"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopWhiteboardPushResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)