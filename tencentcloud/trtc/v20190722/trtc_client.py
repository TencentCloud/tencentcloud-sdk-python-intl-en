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
from tencentcloud.trtc.v20190722 import models


class TrtcClient(AbstractClient):
    _apiVersion = '2019-07-22'
    _endpoint = 'trtc.tencentcloudapi.com'
    _service = 'trtc'


    def ControlAIConversation(self, request):
        """Provides server-side control of AI Conversation

        :param request: Request instance for ControlAIConversation.
        :type request: :class:`tencentcloud.trtc.v20190722.models.ControlAIConversationRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.ControlAIConversationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ControlAIConversation", params, headers=headers)
            response = json.loads(body)
            model = models.ControlAIConversationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudRecording(self, request):
        """API description:
        This API is used to start an on-cloud recording task. It records the audio and video streams in a room and saves them to the specified cloud storage. You can use this API to record the streams in a room separately, or you can mix the streams first and then record the mixed stream.

        You can use this API to perform the following operations:
        * Specify the anchors whose streams you want or do not want to record by using the `RecordParams` parameter
        * Specify the storage service you want to save recording files to by using the `StorageParams` parameter. Currently, you can save recording files to Tencent Cloud VOD or COS.
        * Specify transcoding settings for mixed-stream recording, including video resolution, video bitrate, frame rate, and audio quality, by using `MixTranscodeParams`
        * Specify the layout of different videos in mixed-stream recording mode or select an auto-arranged layout template

        Key concepts:
        * Single-stream recording: Record the audio and video of each subscribed user (`UserId`) in a room and save the recording files to the storage you specify.
        Mixed-stream recording: Mix the audios and videos of subscribed users (`UserId`) in a room, record the mixed stream, and save the recording files to the storage you specify. After a recording task ends, you can go to the VOD console (https://console.tencentcloud.com/vod/media) or [COS console](https://console.cloud.tencent.com/cos/bucket) to view the recording files.

        :param request: Request instance for CreateCloudRecording.
        :type request: :class:`tencentcloud.trtc.v20190722.models.CreateCloudRecordingRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.CreateCloudRecordingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudRecording", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudRecordingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudRecording(self, request):
        """This API is used to stop a recording task. If a task is stopped successfully, but the uploading of recording files has not completed, the backend will continue to upload the files and will notify you via a callback when the upload is completed.

        :param request: Request instance for DeleteCloudRecording.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DeleteCloudRecordingRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DeleteCloudRecordingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudRecording", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudRecordingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAIConversation(self, request):
        """Describe the AI conversation task status

        :param request: Request instance for DescribeAIConversation.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeAIConversationRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeAIConversationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAIConversation", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAIConversationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAITranscription(self, request):
        """Describe AI transcription task status

        :param request: Request instance for DescribeAITranscription.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeAITranscriptionRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeAITranscriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAITranscription", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAITranscriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCallDetailInfo(self, request):
        """This API (the old `DescribeCallDetail`) is used to query the user list and call quality data of a specified time range in the last 14 days. If `DataType` is not null, the data of up to six users during a period of up to one hour can be queried (the period can start and end on different days). If `DataType` is null, the data of up to 100 users can be returned per page (the value of `PageSize` cannot exceed 100). Six users are queried by default. The period queried cannot exceed four hours. This API is used to query call quality and is not recommended for billing purposes.
        **Note**:
        1. You can use this API to query historical data or for reconciliation purposes, but we do not recommend you use it for crucial business logic.
        2. If you need to call this API, please upgrade the monitoring dashboard version to "Standard". For more details, please refer to: https://trtc.io/document/54481?product=pricing.

        :param request: Request instance for DescribeCallDetailInfo.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeCallDetailInfoRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeCallDetailInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCallDetailInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCallDetailInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudRecording(self, request):
        """This API is used to query the status of a recording task after it starts. It works only when a task is in progress. If the task has already ended when this API is called, an error will be returned.
        If a recording file is being uploaded to VOD, the response parameter `StorageFileList` will not contain the information of the recording file. Please listen for the recording file callback to get the information.

        :param request: Request instance for DescribeCloudRecording.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeCloudRecordingRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeCloudRecordingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudRecording", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudRecordingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMixTranscodingUsage(self, request):
        """This API is used to query your usage of TRTC’s On-Cloud MixTranscoding service.
        - If the period queried is one day or shorter, the statistics returned are on a five-minute basis. If the period queried is longer than one day, the statistics returned are on a daily basis.
        - The period queried per request cannot be longer than 31 days.
        - If you query the statistics of the current day, the statistics returned may be inaccurate due to the delay in data collection.
        - You can use this API to query your historical usage or to reconcile data, but we do not recommend you use it for crucial business logic.
        - The rate limit of this API is five calls per second.

        :param request: Request instance for DescribeMixTranscodingUsage.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeMixTranscodingUsageRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeMixTranscodingUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMixTranscodingUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMixTranscodingUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordingUsage(self, request):
        """This API is used to query your TRTC recording usage.
        - If the period queried is one day or shorter, the statistics returned are on a five-minute basis. If the period queried is longer than one day, the statistics returned are on a daily basis.
        - The period queried per request cannot be longer than 31 days.
        - If you query the statistics of the current day, the statistics returned may be inaccurate due to the delay in data collection.
        - You can use this API to query your historical usage or to reconcile data, but we do not recommend you use it for crucial business logic.
        - The rate limit of this API is five calls per second.

        :param request: Request instance for DescribeRecordingUsage.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeRecordingUsageRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeRecordingUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordingUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordingUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRelayUsage(self, request):
        """This API is used to query your usage of TRTC’s relay to CDN service.
        - If the period queried is one day or shorter, the statistics returned are on a five-minute basis. If the period queried is longer than one day, the statistics returned are on a daily basis.
        - The period queried per request cannot be longer than 31 days.
        - If you query the statistics of the current day, the statistics returned may be inaccurate due to the delay in data collection.
        - You can use this API to query your historical usage or to reconcile data, but we do not recommend you use it for crucial business logic.
        - The rate limit of this API is five calls per second.

        :param request: Request instance for DescribeRelayUsage.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeRelayUsageRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeRelayUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRelayUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRelayUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoomInfo(self, request):
        """This API (the old `DescribeRoomInformation`) is used to query the rooms of an application (`SDKAppID`) in the last 14 days. Up to 100 records can be returned per call (10 are returned by default).
        **Note**:
        1. You can use this API to query historical data or for reconciliation purposes, but we do not recommend you use it for crucial business logic.
        2. If you need to call this API, please upgrade the monitoring dashboard version to "Standard". For more details, please refer to: https://trtc.io/document/54481

        :param request: Request instance for DescribeRoomInfo.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeRoomInfoRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeRoomInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoomInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoomInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScaleInfo(self, request):
        """This API (the old `DescribeHistoryScale`) is used to query the daily number of rooms and users of an application (`SDKAppID`) in the last 14 days. Data for the current day cannot be queried.

        :param request: Request instance for DescribeScaleInfo.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeScaleInfoRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeScaleInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScaleInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScaleInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStreamIngest(self, request):
        """You can query the status of the Relay task.

        :param request: Request instance for DescribeStreamIngest.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeStreamIngestRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeStreamIngestResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamIngest", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamIngestResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTRTCMarketQualityData(self, request):
        """Query TRTC Monitoring Dashboard - Data Dashboard Quality Metrics (including the following metrics)
        joinSuccessRate: Join channel success rate.
        joinSuccessIn5sRate: Join channel success rate within 5s.
        audioFreezeRate: Audio stutter rate.
        videoFreezeRate: Video stutter rate.
        networkDelay: Lag rate.
        Note:
        1. To call the API, you need to activate the monitoring dashboard Standard Edition and Premium Edition, the monitoring dashboard Free Edition does not support calling. Monitoring dashboard version features and billing overview: https://trtc.io/document/54481.
        2. The query time range depends on the monitoring dashboard function version, premium edition can query the last 30 days.

        :param request: Request instance for DescribeTRTCMarketQualityData.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCMarketQualityDataRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCMarketQualityDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTRTCMarketQualityData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTRTCMarketQualityDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTRTCMarketScaleData(self, request):
        """Query TRTC Monitoring Dashboard - Data Dashboard Scale Metrics (will return userCount, roomCount, peakCurrentUsers, peakCurrentChannels)
        - userCount: number of users in the call,
        - roomCount: number of rooms in the call, counted as one call channel from the time a user joins the channel to the time all users leave the channel.
        - peakCurrentChannels: peak number of channels online at the same time.
        - peakCurrentUsers: peak number of users online at the same time.
        Note:
        1. To call the interface, you need to activate the monitoring dashboard Standard Edition and Premium Edition, the monitoring dashboard Free Edition does not support calling, for monitoring dashboard version features and billing overview: https://trtc.io/document/54481.
        2. The query time range depends on the monitoring dashboard function version, premium edition can query up to 60 days.

        :param request: Request instance for DescribeTRTCMarketScaleData.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCMarketScaleDataRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCMarketScaleDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTRTCMarketScaleData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTRTCMarketScaleDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTRTCRealTimeQualityData(self, request):
        """Query TRTC Monitoring Dashboard - Real-Time Monitoring Quality Metrics (return the following metrics)
         -Video stutter rate
         -Audio stutter rate
         Note:
         1. To call the API, you need to activate the Monitoring Dashboard Standard Edition and Premium Edition. The Monitoring Dashboard Free Edition does not support calling. For monitoring dashboard version features and billing overview, please visit: https://trtc.io/document/54481.
         2. The query time range depends on the monitoring dashboard function version. The premium edition can query up to 1 hours

        :param request: Request instance for DescribeTRTCRealTimeQualityData.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCRealTimeQualityDataRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCRealTimeQualityDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTRTCRealTimeQualityData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTRTCRealTimeQualityDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTRTCRealTimeScaleData(self, request):
        """Query TRTC Monitoring Dashboard - Real-Time Monitoring Scale Metrics (the following metrics will be returned) -userCount (Online users) -roomCount (Online rooms) Note: 1. To call the interface, you need to activate the monitoring dashboard Standard Edition and Premium Edition, the monitoring dashboard Free Edition does not support calling. For monitoring dashboard version features and billing overview, please visit: https://trtc.io/document/54481. 2. The query time range depends on the function version of the monitoring dashboard. The premium edition can query the last 1 hours

        :param request: Request instance for DescribeTRTCRealTimeScaleData.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCRealTimeScaleDataRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeTRTCRealTimeScaleDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTRTCRealTimeScaleData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTRTCRealTimeScaleDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrtcRoomUsage(self, request):
        """This API is used to query usage data grouped by room.
        - The queried period cannot exceed 24 hours. If the period spans two different days, the data returned may not be accurate due to a delay in data collection. You can make multiple calls to query the usage on different days.
        - You can use this API to query your historical usage or to reconcile data, but we do not recommend you use it for crucial business logic.
        - The rate limit of this API is one call every 15 seconds.

        :param request: Request instance for DescribeTrtcRoomUsage.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeTrtcRoomUsageRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeTrtcRoomUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrtcRoomUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrtcRoomUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrtcUsage(self, request):
        """This API is used to query your TRTC audio/video duration.
        - If the period queried is one day or shorter, the statistics returned are on a five-minute basis. If the period queried is longer than one day, the statistics returned are on a daily basis.
        - The period queried per request cannot be longer than 31 days.
        - If you query the statistics of the current day, the statistics returned may be inaccurate due to the delay in data collection.
        - You can use this API to query your historical usage or to reconcile data, but we do not recommend you use it for crucial business logic.
        - The rate limit of this API is five calls per second.

        :param request: Request instance for DescribeTrtcUsage.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeTrtcUsageRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeTrtcUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrtcUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrtcUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUnusualEvent(self, request):
        """This API (the old `DescribeAbnormalEvent`) is used to query up to 20 random abnormal user experiences of an application (`SDKAppID`) in the last 14 days. The start and end time can be on two different days, but they cannot be more than one hour apart.
        For details about the error events, see https://intl.cloud.tencent.com/document/product/647/44916?from_cn_redirect=1
        **Note**:
        1. You can use this API to query historical data or for reconciliation purposes, but we do not recommend you use it for crucial business logic.
        2. If you need to call this API, please upgrade the monitoring dashboard version to "Standard". For more details, please refer to: https://www.tencentcloud.com/document/product/647/54481.

        :param request: Request instance for DescribeUnusualEvent.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeUnusualEventRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeUnusualEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUnusualEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUnusualEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserEvent(self, request):
        """This API (the old `DescribeDetailEvent`) is used to query the events of a call in the last 14 days, including user entry and exit, turning the camera on/off, etc.
        **Note**:
        1. You can use this API to query historical data or for reconciliation purposes, but we do not recommend you use it for crucial business logic.
        2. If you need to call this API, please upgrade the monitoring dashboard version to "Standard". For more details, please refer to: https://trtc.io/document/54481?product=pricing.

        :param request: Request instance for DescribeUserEvent.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeUserEventRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeUserEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserInfo(self, request):
        """This API (the old `DescribeUserInformation`) is used to query the user list of a specified time range (up to four hours) in the last 14 days. The data of up to 100 users can be returned per page (six are returned by default).
        **Note**:
        1. You can use this API to query historical data or for reconciliation purposes, but we do not recommend you use it for crucial business logic.
        2. If you need to call this API, please upgrade the monitoring dashboard version to "Standard". For more details, please refer to: https://trtc.io/document/60214?product=pricing.

        :param request: Request instance for DescribeUserInfo.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DescribeUserInfoRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DescribeUserInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DismissRoom(self, request):
        """This API is used to remove all users from a room and dismiss the room. It supports all platforms. For Android, iOS, Windows, and macOS, the TRTC SDK needs to be upgraded to v6.6 or above.

        :param request: Request instance for DismissRoom.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DismissRoomRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DismissRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DismissRoom", params, headers=headers)
            response = json.loads(body)
            model = models.DismissRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DismissRoomByStrRoomId(self, request):
        """This API is used to remove all users from a room and close the room. It works on all platforms. For Android, iOS, Windows, and macOS, you need to update the TRTC SDK to version 6.6 or above.

        :param request: Request instance for DismissRoomByStrRoomId.
        :type request: :class:`tencentcloud.trtc.v20190722.models.DismissRoomByStrRoomIdRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.DismissRoomByStrRoomIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DismissRoomByStrRoomId", params, headers=headers)
            response = json.loads(body)
            model = models.DismissRoomByStrRoomIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudRecording(self, request):
        """This API is used to modify a recording task. It works only when a task is in progress. If the task has already ended when this API is called, an error will be returned. You need to specify all the parameters for each request instead of just the ones you want to modify.

        :param request: Request instance for ModifyCloudRecording.
        :type request: :class:`tencentcloud.trtc.v20190722.models.ModifyCloudRecordingRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.ModifyCloudRecordingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudRecording", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudRecordingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveUser(self, request):
        """This API is used to remove a user from a room. It is applicable to scenarios where the anchor, room owner, or admin wants to kick out a user. It supports all platforms. For Android, iOS, Windows, and macOS, the TRTC SDK needs to be upgraded to v6.6 or above.

        :param request: Request instance for RemoveUser.
        :type request: :class:`tencentcloud.trtc.v20190722.models.RemoveUserRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.RemoveUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveUser", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveUserByStrRoomId(self, request):
        """This API is used to remove a user from a room. It allows the anchor, room owner, or admin to kick out a user, and works on all platforms. For Android, iOS, Windows, and macOS, you need to update the TRTC SDK to version 6.6 or above.

        :param request: Request instance for RemoveUserByStrRoomId.
        :type request: :class:`tencentcloud.trtc.v20190722.models.RemoveUserByStrRoomIdRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.RemoveUserByStrRoomIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveUserByStrRoomId", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveUserByStrRoomIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetUserBlocked(self, request):
        """This API is used to disable or enable the audio and video of a user. It can be used by an anchor, room owner, or admin to block or unblock a user. It supports platforms including Android, iOS, Windows, macOS, web, and WeChat Mini Program. Use this API if the room ID is a number.

        :param request: Request instance for SetUserBlocked.
        :type request: :class:`tencentcloud.trtc.v20190722.models.SetUserBlockedRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SetUserBlockedResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetUserBlocked", params, headers=headers)
            response = json.loads(body)
            model = models.SetUserBlockedResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetUserBlockedByStrRoomId(self, request):
        """This API allows an anchor, room owner, admin to mute/unmute a user. It can be used on platforms including Android, iOS, Windows, macOS, web, and WeChat Mini Program. Use this API when the room ID is a string.

        :param request: Request instance for SetUserBlockedByStrRoomId.
        :type request: :class:`tencentcloud.trtc.v20190722.models.SetUserBlockedByStrRoomIdRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.SetUserBlockedByStrRoomIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetUserBlockedByStrRoomId", params, headers=headers)
            response = json.loads(body)
            model = models.SetUserBlockedByStrRoomIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartAIConversation(self, request):
        """Initiate AI conversation task, where the AI bot enters the TRTC room to engage in AI conversation with specified members in the room. This is suitable for scenarios such as intelligent customer service and AI language teachers. The TRTC AI conversation feature has built-in speech-to-text capabilities , allowing customers to flexibly specify third-party AI model (LLM) services and text-to-speech (TTS) services. For more [feature details](https://cloud.tencent.com/document/product/647/108901).

        :param request: Request instance for StartAIConversation.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StartAIConversationRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StartAIConversationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartAIConversation", params, headers=headers)
            response = json.loads(body)
            model = models.StartAIConversationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartAITranscription(self, request):
        """Initiate the transcription bot. The backend will pull the stream through the bot to perform real-time speech recognition and deliver subtitles and transcription messages. The transcription bot supports two stream pulling modes, controlled by the `TranscriptionMode` field:
        - Pull the stream of the entire room.
        - Pull the stream of a specific user.

        The server delivers subtitles and transcription messages in real-time through TRTC's custom messages, with `CmdId` fixed at 1. The client only needs to listen for the callback of custom messages. For example, see the [C++ callback](https://cloud.tencent.com/document/product/647/79637#4cd82f4edb24992a15a25187089e1565). Other clients, such as Android, Web, etc., can also be found at the same link.

        :param request: Request instance for StartAITranscription.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StartAITranscriptionRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StartAITranscriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartAITranscription", params, headers=headers)
            response = json.loads(body)
            model = models.StartAITranscriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartPublishCdnStream(self, request):
        """In a TRTC room, there may be multiple audio and video streams concurrently active. You can use the MixTranscoding API to notify Tencent Cloud server to mix multiple video screens from the same room or multiple rooms together, and specify the position of each screen, while mixing multiple audio streams together. The final result is a single audio and video stream, which can be used for recording and live viewing. It also supports pushing this mixed audio and video stream back to the TRTC room.

        The Cloud API MixTranscoding feature includes three interfaces:
        1. StartPublishCdnStream: Start a MixTranscoding task. This interface will initiate a new MixTranscoding task. After the task is successfully started, a unique TaskId will be returned under the sdkappid dimension. You need to save this TaskId, as it will be required for updating and stopping the task later.
        2. UpdatePublishCdnStream: Update the specified MixTranscoding task, including updating the video screen layout, updating the mixing list, updating the list of CDN addresses to be relayed, and updating the list of rooms to be pushed back.
        3. StopPublishCdnStream: Stop the specified MixTranscoding task.

        You can achieve the following goals through this set of interfaces:
        1. Set the final video and audio quality, including video resolution, video frame rate, video bitrate, and audio quality.
        2. Set the layout position of each screen. You only need to set it once. When you specify the MixTranscoding user to enter the room and send audio and video, the layout engine will automatically mix the user's screen to the specified layout position. You can also use the update interface to adjust the layout position.
        3. Set multiple CDN relay target addresses. A single relay task can support up to 10 CDN relay addresses at the same time.
        4. Set multiple room pushback lists. A single relay task can support up to 10 TRTC rooms for mixed stream pushback.

        The following layout templates are currently supported. Dynamic layout templates (floating template, grid template, screen sharing template) only support a single TRTC room, while custom templates support mixing audio and video streams from multiple TRTC rooms. The specific descriptions are as follows:
        1. Floating template: The video screen of the first user entering the room will fill the entire screen, and the video screens of other users will be arranged horizontally from the bottom left corner, displaying as small screens, with up to 4 rows and 4 screens per row. The small screens float above the large screen. It supports up to 1 large screen and 15 small screens. If the user only sends audio, it does not occupy the layout configuration by default, but it can also be set. Each sub-screen is rendered by default using the center cropping method, and the rendering method of the sub-screen can also be set uniformly.
        2. Grid template: The video screens of all users are of the same size, evenly dividing the entire screen. The more people there are, the smaller the size of each user's screen. It supports up to 16 screens. If the user only sends audio, it does not occupy the layout configuration by default, but it can also be set. Each sub-screen is rendered by default using the center cropping method, and the rendering method of the sub-screen can also be set uniformly.
        3. Screen sharing template: Suitable for video conference and online education scenarios. The screen sharing (or the main speaker's camera) always occupies the large screen position on the left side of the screen. You need to explicitly set the MixTranscoding user information that occupies the large screen. Other users are arranged vertically on the right side, with up to two columns and 8 small screens per column. It supports up to 1 large screen and 15 small screens. If the uplink resolution aspect ratio is different from the screen output aspect ratio, the large screen on the left side will be scaled to maintain content integrity, while the small screens on the right side will be cropped. The rendering method of the sub-screen can also be set uniformly.
        4. Custom layout template: Allows you to actively set the layout position according to your business needs. Each preset layout position supports named settings (named settings require specifying the room number and username) and unnamed settings. When a sub-screen is named, the position is reserved for the user, and the user will automatically occupy the position when entering the room and sending audio and video data. Other users will not occupy this position. When the preset layout position is not named, the layout engine will automatically fill in the order of entering the room. When the preset positions are full, no other users' screens and sounds will be mixed. Each sub-screen position supports setting placeholder images (BackgroundImageUrl). When the user does not enter the room or only sends audio data, the screen at this position can display the corresponding placeholder image.

        When using the relay API, you may incur the following costs depending on the usage characteristics:
        For MCU MixTranscoding fees, please refer to the documentation: Billing of MixTranscoding and Relay to CDN | Tencent Cloud.
        For non-Tencent Cloud CDN relay fees, please refer to the documentation: Billing of MixTranscoding and Relay to CDN | Tencent Cloud.

        Instructions for using parameters:
        1. AgentParams: Each relay task will pull a robot user into the TRTC room to pull the stream. You need to set this robot user through the AgentParams.UserId parameter. This robot ID cannot conflict with the normal user ID in the room, otherwise, the relay task will be abnormally terminated due to the robot user being kicked out of the TRTC room. You can avoid this by adding a special prefix. You can control the automatic termination of the relay task by setting AgentParams.MaxIdleTime. When this parameter is set, the relay task will automatically stop when all participating MixTranscoding anchors continuously leave the TRTC room for more than MaxIdleTime duration. Note: The relay task will not automatically stop when the participating MixTranscoding anchor only stops sending audio and video.
        2. WithTranscoding: If you need to mix multiple audio and video streams into one, WithTranscoding must be set to 1.
        3. AudioParams: The audio parameters and video parameters of the relay task are set separately. If you want to mix the audio of specified users, you need to explicitly set AudioParams.SubscribeAudioList. If you do not set AudioParams.SubscribeAudioList, the mixing engine will automatically mix the audio of all users in the TRTC room. If you want to mix the audio of all users in the TRTC room except for specified users, you can set the audio blacklist list through AudioParams.UnSubscribeAudioList.
        4. VideoParams: If you want to mix user videos, you can set it through VideoParams. If you only want to mix audio, you do not need to set VideoParams. You can set the screen layout mode through VideoParams.LayoutParams.MixLayoutMode, including dynamic layout (1: floating layout (default), 2: screen sharing layout, 3: grid layout) and custom layout. The dynamic layout mode is automatically mixed by the layout engine according to a fixed layout, and there is no need to set VideoParams.LayoutParams.MixLayoutList. When using the floating layout and screen sharing layout, you can specify the large screen user by setting VideoParams.LayoutParams.MaxVideoUser. The custom layout mode provides you with the ability to layout screens independently, and you can specify the layout position of each user through VideoParams.LayoutParams.MixLayoutList. In each layout parameter, you can specify the layout position for the specified user by setting the UserMediaStream parameter, or you can not set the UserMediaStream, and the layout engine will automatically fill in the order of users entering the TRTC room. In addition, you can set the rendering method (RenderMode) and cropping method (CustomCrop) for each layout position.
        5. VideoParams.WaterMarkList: If you want to overlay a watermark on the mixed screen, you can set it through VideoParams.WaterMarkList. It supports image watermarks and text watermarks and supports transparent channels.
        6. SingleSubscribeParams: If you want to push a single stream from the TRTC room to the CDN, you can set it using the SingleSubscribeParams parameter. In this case, you need to set the WithTranscoding parameter to 0.
        7. PublishCdnParams.N: If you want to push the stream to the CDN, you can set it using the PublishCdnParams.N parameter. It supports pushing to up to 10 CDN addresses at the same time. If the relay address is Tencent Cloud CDN, please set IsTencentCdn explicitly to 1; if you need to relay to a non-Tencent Cloud CDN, please contact Tencent Cloud Technical Support to enable it. Relaying to non-Tencent Cloud will incur relay fees. For fee information, please refer to the official documentation: On-Cloud Relay Billing Overview.
        8. FeedBackRoomParams.N: If you want to push the mixed audio and video stream back to the TRTC room, you can set it using the FeedBackRoomParams.N parameter. It supports pushing up to 10 streams back to the TRTC room at the same time. You need to specify the TRTC room number and robot ID (UserId) for the pushback. The robot ID cannot conflict with the normal user ID, otherwise, the relay task will be abnormally terminated due to the robot user being kicked out of the TRTC room. You can avoid this by adding a special prefix.
        9. SeiParams: If you want to add SEI information to the mixed audio and video stream, you can set it using the SeiParams parameter. It supports volume layout SEI and overlay relay request SEI. The content of the volume layout SEI is a fixed JSON structure, please see the SEI description in the following section of this chapter. You can set the SEI to follow the keyframe by setting the FollowIdr parameter. The description of the volume layout SEI is as follows:
        If your CDN audience needs to recognize the position of the participating MixTranscoding anchors and the volume information of the participating MixTranscoding anchors, you can use the volume layout SEI. The payload content and parameter description of the volume layout SEI are as follows:
        { "app_data":"", "canvas":{ "w":1080, "h":960 }, "regions":[ { "uid":"65949987242835883c", "zorder":2, "volume":45, "x":270, "y":480, "w":540, "h":480 }, { "uid":"659c9d8d242b328d31", "zorder":2, "volume":0, "x":0, "y":0, "w":540, "h":480 }, { "uid":"64989a82272b308c", "zorder":2, "volume":91, "x":540, "y":0, "w":540, "h":480 } ], "ver":"1.0", "ts":1648544726 }
        canvas: This is the width and height of the VideoEncode setting in the MixTranscoding signaling, that is, the width and height of the entire canvas of the MixTranscoding output.
        regions: Contains the real mixed user ID and the corresponding sub-screen position. If the participating MixTranscoding user does not enter the TRTC room or does not turn on the video uplink, the regions will not include the user.
        uid: Represents the user ID participating in MixTranscoding.
        zorder: The layer of the participating MixTranscoding userid in the MixTranscoding output.
        x/y: The coordinates of the sub-screen of the participating MixTranscoding userid on the canvas.
        w/h: The size of the sub-screen of the participating MixTranscoding userid.
        volume: Represents the volume of the MixTranscoding user, with a value range of 0-100. The larger the value, the greater the volume of the user participating in MixTranscoding.
        ts: The server local second-level timestamp for outputting SEI.
        ver: can be ignored.

        Usage Precautions:
        1. When using the Mixed Relay Interface, you need to call the Start Relay Task Interface (StartPublishCdnStream) first to get the Task ID from the response. Then, use the Task ID to update the relay task (UpdatePublishCdnStream) and stop the relay task (StopPublishCdnStream).
        2. The Relay API does not support initiating Automatic Bypass Tasks configured in the TRTC Console, nor does it support Custom Stream ID bypass tasks set in the TRTC SDK room entry interface.
        3. To ensure the stability of the relay link, the same relay task does not support switching between Audio only, Audio and Video, and Video only.
        4. To ensure the stability of the relay link, updating video parameters (codec) and audio parameters (codec, Sample rate, bitrate, and number of channels) is not supported during the Update Video process.
        5. When initiating a single stream bypass task, filling in both Audio Parameters and Video Parameters means Audio and Video bypass. If only Audio Parameters are filled in, it means Audio only bypass, and switching from Audio only to Audio and Video is not supported during the task progress. For Audio and Video bypass, the Width, Height, Fps, BitRate, and Gop in Video Parameters must be filled in according to the real upstream parameters.
        6. The SequenceNumber parameter must be carried in the update request to prevent request disorder. Customers must ensure that the SequenceNumber parameter increases when updating the same task, otherwise, the mix task update will fail.
        7. When calling the API, choose the region according to the following instructions: If the Application ID is 1400xxx, the region can be Beijing, Shanghai, Guangzhou, or Hong Kong. If your CDN audience is mainly overseas, please choose Hong Kong. If the Application ID is 200xxx or 400xxx, please choose Singapore.
        8. Streams pushed back to the TRTC room will not participate in the mixing of other push back room tasks. If one of the following conditions is met, it can participate in the mixing of other relay CDN tasks: (1) The push stream robot is specified to participate in the mixing in the video parameters of the relay CDN task; (2) The push stream robot is specified to participate in the mixing in the audio parameters of the relay CDN task through the whitelist method; (3) The room number of the mix user participating in the relay CDN task is completely different from the room number of the mix user corresponding to the push back robot.
        9. You can create a relay task before the anchor enters the room. When the relay task is finished, you need to call the stop interface actively. If you do not call the Stop Relay Task Interface, Tencent Cloud will automatically stop the mix relay task when all users participating in the mix have no data uploaded for a period of time exceeding the timeout (AgentParams.MaxIdleTime) set when starting the relay task.

        :param request: Request instance for StartPublishCdnStream.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StartPublishCdnStreamRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StartPublishCdnStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartPublishCdnStream", params, headers=headers)
            response = json.loads(body)
            model = models.StartPublishCdnStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartStreamIngest(self, request):
        """Push an online media stream to the TRTC room.

        :param request: Request instance for StartStreamIngest.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StartStreamIngestRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StartStreamIngestResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartStreamIngest", params, headers=headers)
            response = json.loads(body)
            model = models.StartStreamIngestResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopAIConversation(self, request):
        """Stop AI conversation task

        :param request: Request instance for StopAIConversation.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StopAIConversationRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StopAIConversationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopAIConversation", params, headers=headers)
            response = json.loads(body)
            model = models.StopAIConversationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopAITranscription(self, request):
        """Stop AI Transcription task

        :param request: Request instance for StopAITranscription.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StopAITranscriptionRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StopAITranscriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopAITranscription", params, headers=headers)
            response = json.loads(body)
            model = models.StopAITranscriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopPublishCdnStream(self, request):
        """This API is used to stop a relaying task.

        :param request: Request instance for StopPublishCdnStream.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StopPublishCdnStreamRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StopPublishCdnStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopPublishCdnStream", params, headers=headers)
            response = json.loads(body)
            model = models.StopPublishCdnStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopStreamIngest(self, request):
        """Stop a Pull stream Relay task.

        :param request: Request instance for StopStreamIngest.
        :type request: :class:`tencentcloud.trtc.v20190722.models.StopStreamIngestRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.StopStreamIngestResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopStreamIngest", params, headers=headers)
            response = json.loads(body)
            model = models.StopStreamIngestResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAIConversation(self, request):
        """Update AI conversation task parameters

        :param request: Request instance for UpdateAIConversation.
        :type request: :class:`tencentcloud.trtc.v20190722.models.UpdateAIConversationRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.UpdateAIConversationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAIConversation", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAIConversationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdatePublishCdnStream(self, request):
        """This API is used to change the parameters of a relaying task.
        Note: For details about how to use this API, see the `StartPublishCdnStream` document.

        :param request: Request instance for UpdatePublishCdnStream.
        :type request: :class:`tencentcloud.trtc.v20190722.models.UpdatePublishCdnStreamRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.UpdatePublishCdnStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdatePublishCdnStream", params, headers=headers)
            response = json.loads(body)
            model = models.UpdatePublishCdnStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateStreamIngest(self, request):
        """You can update the StreamUrl of the Relay task.

        :param request: Request instance for UpdateStreamIngest.
        :type request: :class:`tencentcloud.trtc.v20190722.models.UpdateStreamIngestRequest`
        :rtype: :class:`tencentcloud.trtc.v20190722.models.UpdateStreamIngestResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateStreamIngest", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateStreamIngestResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))