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
from tencentcloud.trtc.v20190722 import models
from typing import Dict


class TrtcClient(AbstractClient):
    _apiVersion = '2019-07-22'
    _endpoint = 'trtc.intl.tencentcloudapi.com'
    _service = 'trtc'

    async def ControlAIConversation(
            self,
            request: models.ControlAIConversationRequest,
            opts: Dict = None,
    ) -> models.ControlAIConversationResponse:
        """
        Provides server-side control of AI Conversation
        """
        
        kwargs = {}
        kwargs["action"] = "ControlAIConversation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ControlAIConversationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudModeration(
            self,
            request: models.CreateCloudModerationRequest,
            opts: Dict = None,
    ) -> models.CreateCloudModerationResponse:
        """
        API description:
        This API is used to enable the cloud moderation feature to complete audio and video slicing, video frame extraction, and audio stream recording in the room, and submit them to the specified moderation supplier for completing the moderation.

        This API is used to achieve the following goals:
        * This API is used to specify the moderation parameters (ModerationParams) to specify the detailed parameters required for moderation.
        * This API is used to specify the storage parameter (SliceStorageParams) to specify the cloud storage you want to upload the file complying with the moderation policy to. Currently, Tencent Cloud Object Storage (COS) and third-party AWS are supported.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudModeration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudModerationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudRecording(
            self,
            request: models.CreateCloudRecordingRequest,
            opts: Dict = None,
    ) -> models.CreateCloudRecordingResponse:
        """
        API description:
        This API is used to start an on-cloud recording task. It records the audio and video streams in a room and saves them to the specified cloud storage. You can use this API to record the streams in a room separately, or you can mix the streams first and then record the mixed stream.

        You can use this API to perform the following operations:
        * Specify the anchors whose streams you want or do not want to record by using the `RecordParams` parameter
        * Specify the storage service you want to save recording files to by using the `StorageParams` parameter. Currently, you can save recording files to Tencent Cloud VOD or COS.
        * Specify transcoding settings for mixed-stream recording, including video resolution, video bitrate, frame rate, and audio quality, by using `MixTranscodeParams`
        * Specify the layout of different videos in mixed-stream recording mode or select an auto-arranged layout template

        Key concepts:
        * Single-stream recording: Record the audio and video of each subscribed user (`UserId`) in a room and save the recording files to the storage you specify.
        Mixed-stream recording: Mix the audios and videos of subscribed users (`UserId`) in a room, record the mixed stream, and save the recording files to the storage you specify. After a recording task ends, you can go to the VOD console (https://console.tencentcloud.com/vod/media) or [COS console](https://console.cloud.tencent.com/cos/bucket) to view the recording files.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudRecording"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudRecordingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudSliceTask(
            self,
            request: models.CreateCloudSliceTaskRequest,
            opts: Dict = None,
    ) -> models.CreateCloudSliceTaskResponse:
        """
        API description:
        This API is used to enable the cloud slicing feature, completing audio and video slicing tasks in the room, and uploading them to the specified cloud storage.
        This API is used to achieve the following goals:
        * This API is used to specify the slicing parameter (SliceParams) to define the blocklist or allowlist of the anchors that require slicing.
        * This API is used to specify the storage parameter (SliceStorageParams) to specify the cloud storage you want to upload to. Currently, Tencent Cloud Object Storage (COS) and third-party AWS are supported.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudSliceTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudSliceTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudModeration(
            self,
            request: models.DeleteCloudModerationRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudModerationResponse:
        """
        This API is used to stop submission for moderation after the cloud moderation task is successfully started.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudModeration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudModerationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudRecording(
            self,
            request: models.DeleteCloudRecordingRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudRecordingResponse:
        """
        This API is used to stop a recording task. If a task is stopped successfully, but the uploading of recording files has not completed, the backend will continue to upload the files and will notify you via a callback when the upload is completed.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudRecording"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudRecordingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudSliceTask(
            self,
            request: models.DeleteCloudSliceTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudSliceTaskResponse:
        """
        This API is used to stop the slicing task after it is started. Successfully stopping the slicing does not mean that all files are fully transmitted; if the transmission is not completed, the backend will continue to upload files. After the upload is successful, a notification is sent to the customer, prompting that all files have been transmitted, through the event callback.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudSliceTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudSliceTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIConversation(
            self,
            request: models.DescribeAIConversationRequest,
            opts: Dict = None,
    ) -> models.DescribeAIConversationResponse:
        """
        Describe the AI conversation task status
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIConversation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIConversationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAITranscription(
            self,
            request: models.DescribeAITranscriptionRequest,
            opts: Dict = None,
    ) -> models.DescribeAITranscriptionResponse:
        """
        Describe AI transcription task status
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAITranscription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAITranscriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCallDetailInfo(
            self,
            request: models.DescribeCallDetailInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeCallDetailInfoResponse:
        """
        This API (the old `DescribeCallDetail`) is used to query the user list and call quality data of a specified time range in the last 14 days. If `DataType` is not null, the data of up to six users during a period of up to one hour can be queried (the period can start and end on different days). If `DataType` is null, the data of up to 100 users can be returned per page (the value of `PageSize` cannot exceed 100). Six users are queried by default. The period queried cannot exceed four hours. This API is used to query call quality and is not recommended for billing purposes.
        **Note**:
        1. You can use this API to query historical data or for reconciliation purposes, but we do not recommend you use it for crucial business logic.
        2. If you need to call this API, please upgrade the monitoring dashboard version to "Standard". For more details, please refer to: https://trtc.io/document/54481?product=pricing.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCallDetailInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCallDetailInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudModeration(
            self,
            request: models.DescribeCloudModerationRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudModerationResponse:
        """
        This API is used to query the status of the moderation task and information about the subscription blocklist and allowlist after the task is started, which is valid only when the task is in progress. An error will be returned if the task is exited.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudModeration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudModerationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudRecording(
            self,
            request: models.DescribeCloudRecordingRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudRecordingResponse:
        """
        This API is used to query the status of a recording task after it starts. It works only when a task is in progress. If the task has already ended when this API is called, an error will be returned.
        If a recording file is being uploaded to VOD, the response parameter `StorageFileList` will not contain the information of the recording file. Please listen for the recording file callback to get the information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudRecording"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudRecordingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudSliceTask(
            self,
            request: models.DescribeCloudSliceTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudSliceTaskResponse:
        """
        This API is used to query the status of the slicing task after it is started, which is valid only when the task is in progress. An error will be returned if the task is exited.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudSliceTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudSliceTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMixTranscodingUsage(
            self,
            request: models.DescribeMixTranscodingUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeMixTranscodingUsageResponse:
        """
        This API is used to query your usage of TRTC’s On-Cloud MixTranscoding service.
        - If the period queried is one day or shorter, the statistics returned are on a five-minute basis. If the period queried is longer than one day, the statistics returned are on a daily basis.
        - The period queried per request cannot be longer than 31 days.
        - If you query the statistics of the current day, the statistics returned may be inaccurate due to the delay in data collection.
        - You can use this API to query your historical usage or to reconcile data, but we do not recommend you use it for crucial business logic.
        - The rate limit of this API is five calls per second.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMixTranscodingUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMixTranscodingUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRecordingUsage(
            self,
            request: models.DescribeRecordingUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeRecordingUsageResponse:
        """
        This API is used to query your TRTC recording usage.
        - If the period queried is one day or shorter, the statistics returned are on a five-minute basis. If the period queried is longer than one day, the statistics returned are on a daily basis.
        - The period queried per request cannot be longer than 31 days.
        - If you query the statistics of the current day, the statistics returned may be inaccurate due to the delay in data collection.
        - You can use this API to query your historical usage or to reconcile data, but we do not recommend you use it for crucial business logic.
        - The rate limit of this API is five calls per second.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRecordingUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRecordingUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRelayUsage(
            self,
            request: models.DescribeRelayUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeRelayUsageResponse:
        """
        This API is used to query your usage of TRTC’s relay to CDN service.
        - If the period queried is one day or shorter, the statistics returned are on a five-minute basis. If the period queried is longer than one day, the statistics returned are on a daily basis.
        - The period queried per request cannot be longer than 31 days.
        - If you query the statistics of the current day, the statistics returned may be inaccurate due to the delay in data collection.
        - You can use this API to query your historical usage or to reconcile data, but we do not recommend you use it for crucial business logic.
        - The rate limit of this API is five calls per second.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRelayUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRelayUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoomInfo(
            self,
            request: models.DescribeRoomInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeRoomInfoResponse:
        """
        This API (the old `DescribeRoomInformation`) is used to query the rooms of an application (`SDKAppID`) in the last 14 days. Up to 100 records can be returned per call (10 are returned by default).
        **Note**:
        1. You can use this API to query historical data or for reconciliation purposes, but we do not recommend you use it for crucial business logic.
        2. If you need to call this API, please upgrade the monitoring dashboard version to "Standard". For more details, please refer to: https://trtc.io/document/54481
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoomInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoomInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScaleInfo(
            self,
            request: models.DescribeScaleInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeScaleInfoResponse:
        """
        This API (the old `DescribeHistoryScale`) is used to query the daily number of rooms and users of an application (`SDKAppID`) in the last 14 days. Data for the current day cannot be queried.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScaleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScaleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamIngest(
            self,
            request: models.DescribeStreamIngestRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamIngestResponse:
        """
        You can query the status of the Relay task.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamIngest"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamIngestResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTRTCMarketQualityData(
            self,
            request: models.DescribeTRTCMarketQualityDataRequest,
            opts: Dict = None,
    ) -> models.DescribeTRTCMarketQualityDataResponse:
        """
        Query TRTC Monitoring Dashboard - Data Dashboard Quality Metrics (including the following metrics)
        joinSuccessRate: Join channel success rate.
        joinSuccessIn5sRate: Join channel success rate within 5s.
        audioFreezeRate: Audio stutter rate.
        videoFreezeRate: Video stutter rate.
        networkDelay: Lag rate.
        Note:
        1. To call the API, you need to activate the monitoring dashboard Standard Edition and Premium Edition, the monitoring dashboard Free Edition does not support calling. Monitoring dashboard version features and billing overview: https://trtc.io/document/54481.
        2. The query time range depends on the monitoring dashboard function version, premium edition can query the last 30 days.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTRTCMarketQualityData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTRTCMarketQualityDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTRTCMarketScaleData(
            self,
            request: models.DescribeTRTCMarketScaleDataRequest,
            opts: Dict = None,
    ) -> models.DescribeTRTCMarketScaleDataResponse:
        """
        Query TRTC Monitoring Dashboard - Data Dashboard Scale Metrics (will return userCount, roomCount, peakCurrentUsers, peakCurrentChannels)
        - userCount: number of users in the call,
        - roomCount: number of rooms in the call, counted as one call channel from the time a user joins the channel to the time all users leave the channel.
        - peakCurrentChannels: peak number of channels online at the same time.
        - peakCurrentUsers: peak number of users online at the same time.
        Note:
        1. To call the interface, you need to activate the monitoring dashboard Standard Edition and Premium Edition, the monitoring dashboard Free Edition does not support calling, for monitoring dashboard version features and billing overview: https://trtc.io/document/54481.
        2. The query time range depends on the monitoring dashboard function version, premium edition can query up to 60 days.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTRTCMarketScaleData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTRTCMarketScaleDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTRTCRealTimeQualityData(
            self,
            request: models.DescribeTRTCRealTimeQualityDataRequest,
            opts: Dict = None,
    ) -> models.DescribeTRTCRealTimeQualityDataResponse:
        """
        Query TRTC Monitoring Dashboard - Real-Time Monitoring Quality Metrics (return the following metrics)
         -Video stutter rate
         -Audio stutter rate
         Note:
         1. To call the API, you need to activate the Monitoring Dashboard Standard Edition and Premium Edition. The Monitoring Dashboard Free Edition does not support calling. For monitoring dashboard version features and billing overview, please visit: https://trtc.io/document/54481.
         2. The query time range depends on the monitoring dashboard function version. The premium edition can query up to 1 hours
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTRTCRealTimeQualityData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTRTCRealTimeQualityDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTRTCRealTimeScaleData(
            self,
            request: models.DescribeTRTCRealTimeScaleDataRequest,
            opts: Dict = None,
    ) -> models.DescribeTRTCRealTimeScaleDataResponse:
        """
        Query TRTC Monitoring Dashboard - Real-Time Monitoring Scale Metrics (the following metrics will be returned) -userCount (Online users) -roomCount (Online rooms) Note: 1. To call the interface, you need to activate the monitoring dashboard Standard Edition and Premium Edition, the monitoring dashboard Free Edition does not support calling. For monitoring dashboard version features and billing overview, please visit: https://trtc.io/document/54481. 2. The query time range depends on the function version of the monitoring dashboard. The premium edition can query the last 1 hours
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTRTCRealTimeScaleData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTRTCRealTimeScaleDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrtcRoomUsage(
            self,
            request: models.DescribeTrtcRoomUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeTrtcRoomUsageResponse:
        """
        This API is used to query usage data grouped by room.
        - The queried period cannot exceed 24 hours. If the period spans two different days, the data returned may not be accurate due to a delay in data collection. You can make multiple calls to query the usage on different days.
        - You can use this API to query your historical usage or to reconcile data, but we do not recommend you use it for crucial business logic.
        - The rate limit of this API is one call every 15 seconds.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrtcRoomUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrtcRoomUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrtcUsage(
            self,
            request: models.DescribeTrtcUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeTrtcUsageResponse:
        """
        This API is used to query your TRTC audio/video duration.
        - If the period queried is one day or shorter, the statistics returned are on a five-minute basis. If the period queried is longer than one day, the statistics returned are on a daily basis.
        - The period queried per request cannot be longer than 31 days.
        - If you query the statistics of the current day, the statistics returned may be inaccurate due to the delay in data collection.
        - You can use this API to query your historical usage or to reconcile data, but we do not recommend you use it for crucial business logic.
        - The rate limit of this API is five calls per second.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrtcUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrtcUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUnusualEvent(
            self,
            request: models.DescribeUnusualEventRequest,
            opts: Dict = None,
    ) -> models.DescribeUnusualEventResponse:
        """
        This API (the old `DescribeAbnormalEvent`) is used to query up to 20 random abnormal user experiences of an application (`SDKAppID`) in the last 14 days. The start and end time can be on two different days, but they cannot be more than one hour apart.
        For details about the error events, see https://intl.cloud.tencent.com/document/product/647/44916?from_cn_redirect=1
        **Note**:
        1. You can use this API to query historical data or for reconciliation purposes, but we do not recommend you use it for crucial business logic.
        2. If you need to call this API, please upgrade the monitoring dashboard version to "Standard". For more details, please refer to: https://www.tencentcloud.com/document/product/647/54481.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUnusualEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUnusualEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserEvent(
            self,
            request: models.DescribeUserEventRequest,
            opts: Dict = None,
    ) -> models.DescribeUserEventResponse:
        """
        This API (the old `DescribeDetailEvent`) is used to query the events of a call in the last 14 days, including user entry and exit, turning the camera on/off, etc.
        **Note**:
        1. You can use this API to query historical data or for reconciliation purposes, but we do not recommend you use it for crucial business logic.
        2. If you need to call this API, please upgrade the monitoring dashboard version to "Standard". For more details, please refer to: https://trtc.io/document/54481?product=pricing.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserInfo(
            self,
            request: models.DescribeUserInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeUserInfoResponse:
        """
        This API (the old `DescribeUserInformation`) is used to query the user list of a specified time range (up to four hours) in the last 14 days. The data of up to 100 users can be returned per page (six are returned by default).
        **Note**:
        1. You can use this API to query historical data or for reconciliation purposes, but we do not recommend you use it for crucial business logic.
        2. If you need to call this API, please upgrade the monitoring dashboard version to "Standard". For more details, please refer to: https://trtc.io/document/60214?product=pricing.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebRecord(
            self,
            request: models.DescribeWebRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeWebRecordResponse:
        """
        Queries the status of a web-page recording task
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DismissRoom(
            self,
            request: models.DismissRoomRequest,
            opts: Dict = None,
    ) -> models.DismissRoomResponse:
        """
        This API is used to remove all users from a room and dismiss the room. It supports all platforms. For Android, iOS, Windows, and macOS, the TRTC SDK needs to be upgraded to v6.6 or above.
        """
        
        kwargs = {}
        kwargs["action"] = "DismissRoom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DismissRoomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DismissRoomByStrRoomId(
            self,
            request: models.DismissRoomByStrRoomIdRequest,
            opts: Dict = None,
    ) -> models.DismissRoomByStrRoomIdResponse:
        """
        This API is used to remove all users from a room and close the room. It works on all platforms. For Android, iOS, Windows, and macOS, you need to update the TRTC SDK to version 6.6 or above.
        """
        
        kwargs = {}
        kwargs["action"] = "DismissRoomByStrRoomId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DismissRoomByStrRoomIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudModeration(
            self,
            request: models.ModifyCloudModerationRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudModerationResponse:
        """
        This API is used to update the subscription blocklist and allowlist after the cloud moderation task is successfully started.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudModeration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudModerationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudRecording(
            self,
            request: models.ModifyCloudRecordingRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudRecordingResponse:
        """
        This API is used to modify a recording task. It works only when a task is in progress. If the task has already ended when this API is called, an error will be returned. You need to specify all the parameters for each request instead of just the ones you want to modify.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudRecording"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudRecordingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudSliceTask(
            self,
            request: models.ModifyCloudSliceTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudSliceTaskResponse:
        """
        This API is used to update the slicing task after it is started. It can be used to update the allowlist or blocklist for the specified subscription stream.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudSliceTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudSliceTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveUser(
            self,
            request: models.RemoveUserRequest,
            opts: Dict = None,
    ) -> models.RemoveUserResponse:
        """
        This API is used to remove a user from a room. It is applicable to scenarios where the anchor, room owner, or admin wants to kick out a user. It supports all platforms. For Android, iOS, Windows, and macOS, the TRTC SDK needs to be upgraded to v6.6 or above.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveUserByStrRoomId(
            self,
            request: models.RemoveUserByStrRoomIdRequest,
            opts: Dict = None,
    ) -> models.RemoveUserByStrRoomIdResponse:
        """
        This API is used to remove a user from a room. It allows the anchor, room owner, or admin to kick out a user, and works on all platforms. For Android, iOS, Windows, and macOS, you need to update the TRTC SDK to version 6.6 or above.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveUserByStrRoomId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveUserByStrRoomIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetUserBlocked(
            self,
            request: models.SetUserBlockedRequest,
            opts: Dict = None,
    ) -> models.SetUserBlockedResponse:
        """
        This API is used to disable or enable the audio and video of a user. It can be used by an anchor, room owner, or admin to block or unblock a user. It supports platforms including Android, iOS, Windows, macOS, web, and WeChat Mini Program. Use this API if the room ID is a number.
        """
        
        kwargs = {}
        kwargs["action"] = "SetUserBlocked"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetUserBlockedResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetUserBlockedByStrRoomId(
            self,
            request: models.SetUserBlockedByStrRoomIdRequest,
            opts: Dict = None,
    ) -> models.SetUserBlockedByStrRoomIdResponse:
        """
        This API allows an anchor, room owner, admin to mute/unmute a user. It can be used on platforms including Android, iOS, Windows, macOS, web, and WeChat Mini Program. Use this API when the room ID is a string.
        """
        
        kwargs = {}
        kwargs["action"] = "SetUserBlockedByStrRoomId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetUserBlockedByStrRoomIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartAIConversation(
            self,
            request: models.StartAIConversationRequest,
            opts: Dict = None,
    ) -> models.StartAIConversationResponse:
        """
        Initiate AI conversation task, where the AI bot enters the TRTC room to engage in AI conversation with specified members in the room. This is suitable for scenarios such as intelligent customer service and AI language teachers. The TRTC AI conversation feature has built-in speech-to-text capabilities , allowing customers to flexibly specify third-party AI model (LLM) services and text-to-speech (TTS) services. For more [feature details](https://cloud.tencent.com/document/product/647/108901).
        """
        
        kwargs = {}
        kwargs["action"] = "StartAIConversation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartAIConversationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartAITranscription(
            self,
            request: models.StartAITranscriptionRequest,
            opts: Dict = None,
    ) -> models.StartAITranscriptionResponse:
        """
        Initiate the transcription bot. The backend will pull the stream through the bot to perform real-time speech recognition and deliver subtitles and transcription messages. The transcription bot supports two stream pulling modes, controlled by the `TranscriptionMode` field:
        - Pull the stream of the entire room.
        - Pull the stream of a specific user.

        The server delivers subtitles and transcription messages in real-time through TRTC's custom messages, with `CmdId` fixed at 1. The client only needs to listen for the callback of custom messages. For example, see the [C++ callback](https://cloud.tencent.com/document/product/647/79637#4cd82f4edb24992a15a25187089e1565). Other clients, such as Android, Web, etc., can also be found at the same link.
        """
        
        kwargs = {}
        kwargs["action"] = "StartAITranscription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartAITranscriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartPublishCdnStream(
            self,
            request: models.StartPublishCdnStreamRequest,
            opts: Dict = None,
    ) -> models.StartPublishCdnStreamResponse:
        """
        **API Description**

        This API starts a stream mixing and relaying task. This API mixes multiple audio/video streams from a TRTC room into a single stream, encodes it, and then pushes it to CDN server or publishs it into the TRTC room. It also supports relaying a single stream from a TRTC room directly without transcoding.

        After success, the API returns a globally unique TaskID. You will need this TaskId in later operations such as updating or stopping the task.

        For more details, refer to the document:  [Feature Description](https://trtc.io/zh/document/47858?product=rtcengine ) and [FAQs](https://trtc.io/zh/document/36058?product=rtcengine&menulabel=core%20sdk&platform=web) .

        Note: You can enable the relay to CDN in the console to monitor events under the CDN relay status. For callback details, see: [Relay to CDN Callback Description](https://trtc.io/zh/document/54913?product=rtcengine&menulabel=core%20sdk&platform=web ) .

        Starting a relay task may incur the following fees:
        MCU stream mixing and transcoding fees: [See Cloud Stream Mixing and Transcoding Pricing](https://trtc.io/zh/document/47631 ) .
        """
        
        kwargs = {}
        kwargs["action"] = "StartPublishCdnStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartPublishCdnStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartStreamIngest(
            self,
            request: models.StartStreamIngestRequest,
            opts: Dict = None,
    ) -> models.StartStreamIngestResponse:
        """
        Push an online media stream to the TRTC room.
        """
        
        kwargs = {}
        kwargs["action"] = "StartStreamIngest"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartStreamIngestResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartWebRecord(
            self,
            request: models.StartWebRecordRequest,
            opts: Dict = None,
    ) -> models.StartWebRecordResponse:
        """
        This interface can be used to initiate a web-page recording task. In the interface parameters, specify the recording URL, recording resolution, recording result storage and other parameters. If there are parameter or API logic problems, the result will be returned immediately. If there are page problems, such as the page cannot be accessed, the result will be returned in the callback. Please pay attention.
        """
        
        kwargs = {}
        kwargs["action"] = "StartWebRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartWebRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopAIConversation(
            self,
            request: models.StopAIConversationRequest,
            opts: Dict = None,
    ) -> models.StopAIConversationResponse:
        """
        Stop AI conversation task
        """
        
        kwargs = {}
        kwargs["action"] = "StopAIConversation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopAIConversationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopAITranscription(
            self,
            request: models.StopAITranscriptionRequest,
            opts: Dict = None,
    ) -> models.StopAITranscriptionResponse:
        """
        Stop AI Transcription task
        """
        
        kwargs = {}
        kwargs["action"] = "StopAITranscription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopAITranscriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopPublishCdnStream(
            self,
            request: models.StopPublishCdnStreamRequest,
            opts: Dict = None,
    ) -> models.StopPublishCdnStreamResponse:
        """
        This API is used to stop a relaying task.
        You can create a relay task before the anchor enters the room. When the relay task is finished, you need to call the stop interface actively. If you do not call the Stop Relay Task Interface, Tencent Cloud will automatically stop the mix relay task when all users participating in the mix have no data uploaded for a period of time exceeding the timeout (AgentParams.MaxIdleTime) set when starting the relay task.
        """
        
        kwargs = {}
        kwargs["action"] = "StopPublishCdnStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopPublishCdnStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopStreamIngest(
            self,
            request: models.StopStreamIngestRequest,
            opts: Dict = None,
    ) -> models.StopStreamIngestResponse:
        """
        Stop a Pull stream Relay task.
        """
        
        kwargs = {}
        kwargs["action"] = "StopStreamIngest"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopStreamIngestResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopWebRecord(
            self,
            request: models.StopWebRecordRequest,
            opts: Dict = None,
    ) -> models.StopWebRecordResponse:
        """
        Stop an web-page recording task
        """
        
        kwargs = {}
        kwargs["action"] = "StopWebRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopWebRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAIConversation(
            self,
            request: models.UpdateAIConversationRequest,
            opts: Dict = None,
    ) -> models.UpdateAIConversationResponse:
        """
        Update AI conversation task parameters
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAIConversation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAIConversationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdatePublishCdnStream(
            self,
            request: models.UpdatePublishCdnStreamRequest,
            opts: Dict = None,
    ) -> models.UpdatePublishCdnStreamResponse:
        """
        This API is used to change the parameters of a relaying task.
        Note: For details about how to use this API, see the `StartPublishCdnStream` document.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdatePublishCdnStream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdatePublishCdnStreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateStreamIngest(
            self,
            request: models.UpdateStreamIngestRequest,
            opts: Dict = None,
    ) -> models.UpdateStreamIngestResponse:
        """
        You can update the StreamUrl of the Relay task.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateStreamIngest"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateStreamIngestResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)