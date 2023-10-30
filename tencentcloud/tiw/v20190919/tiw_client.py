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
from tencentcloud.tiw.v20190919 import models


class TiwClient(AbstractClient):
    _apiVersion = '2019-09-19'
    _endpoint = 'tiw.tencentcloudapi.com'
    _service = 'tiw'


    def ApplyTiwTrial(self, request):
        """This API is used to apply for a Tencent Interactive Whiteboard trial (15-day by default).

        :param request: Request instance for ApplyTiwTrial.
        :type request: :class:`tencentcloud.tiw.v20190919.models.ApplyTiwTrialRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.ApplyTiwTrialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyTiwTrial", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyTiwTrialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApplication(self, request):
        """This API is used to create a whiteboard application.

        :param request: Request instance for CreateApplication.
        :type request: :class:`tencentcloud.tiw.v20190919.models.CreateApplicationRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.CreateApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplication", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOfflineRecord(self, request):
        """课后录制服务已下线

        This API is used to create an offline recording task.

        :param request: Request instance for CreateOfflineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.CreateOfflineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.CreateOfflineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOfflineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOfflineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSnapshotTask(self, request):
        """This API is used to create a whiteboard snapshot task. If a callback URL is provided, the whiteboard snapshot result is sent to the callback URL after the task is complete.

        :param request: Request instance for CreateSnapshotTask.
        :type request: :class:`tencentcloud.tiw.v20190919.models.CreateSnapshotTaskRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.CreateSnapshotTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSnapshotTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSnapshotTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTranscode(self, request):
        """This API is used to create a document transcoding task.

        :param request: Request instance for CreateTranscode.
        :type request: :class:`tencentcloud.tiw.v20190919.models.CreateTranscodeRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.CreateTranscodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTranscode", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTranscodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVideoGenerationTask(self, request):
        """This API is used to create a recording video generation task.

        :param request: Request instance for CreateVideoGenerationTask.
        :type request: :class:`tencentcloud.tiw.v20190919.models.CreateVideoGenerationTaskRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.CreateVideoGenerationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVideoGenerationTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVideoGenerationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAPIService(self, request):
        """This API is used to query the information about other cloud products by using the service role.

        :param request: Request instance for DescribeAPIService.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeAPIServiceRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeAPIServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAPIService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAPIServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationInfos(self, request):
        """This API is used to query the details of a whiteboard application.

        :param request: Request instance for DescribeApplicationInfos.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeApplicationInfosRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeApplicationInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationUsage(self, request):
        """This API is used to query the subproduct usage of Tencent Interactive Whiteboard.

        :param request: Request instance for DescribeApplicationUsage.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeApplicationUsageRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeApplicationUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBoardSDKLog(self, request):
        """This API is used to query the logs of a whiteboard application on a client.

        :param request: Request instance for DescribeBoardSDKLog.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeBoardSDKLogRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeBoardSDKLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBoardSDKLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBoardSDKLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIMApplications(self, request):
        """This API is used to query the instant messaging (IM) applications that are available for creating a whiteboard application.

        :param request: Request instance for DescribeIMApplications.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeIMApplicationsRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeIMApplicationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIMApplications", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIMApplicationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOfflineRecord(self, request):
        """课后录制服务已下线

        This API is used to query the information about an offline recording task, including the recording progress and recording result.

        :param request: Request instance for DescribeOfflineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeOfflineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeOfflineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOfflineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOfflineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOfflineRecordCallback(self, request):
        """课后录制服务已下线

        This API is used to query the offline recording callback URL.

        :param request: Request instance for DescribeOfflineRecordCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeOfflineRecordCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeOfflineRecordCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOfflineRecordCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOfflineRecordCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOnlineRecord(self, request):
        """This API is used to query the status and result of a real-time recording task.

        :param request: Request instance for DescribeOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOnlineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOnlineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOnlineRecordCallback(self, request):
        """This API is used to query the real-time recording callback address.

        :param request: Request instance for DescribeOnlineRecordCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeOnlineRecordCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeOnlineRecordCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOnlineRecordCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOnlineRecordCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePostpaidUsage(self, request):
        """This API is used to query the pay-as-you-go usage of a user.

        :param request: Request instance for DescribePostpaidUsage.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribePostpaidUsageRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribePostpaidUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePostpaidUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePostpaidUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQualityMetrics(self, request):
        """This API is used to query the quality data of a whiteboard application.

        :param request: Request instance for DescribeQualityMetrics.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeQualityMetricsRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeQualityMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQualityMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQualityMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordSearch(self, request):
        """This API is used to query real-time recording tasks by room ID.

        :param request: Request instance for DescribeRecordSearch.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeRecordSearchRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeRecordSearchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordSearch", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordSearchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoomList(self, request):
        """This API is used to query the rooms of a whiteboard application.

        :param request: Request instance for DescribeRoomList.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeRoomListRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeRoomListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoomList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoomListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshotTask(self, request):
        """This API is used to query the information about a whiteboard snapshot task.

        :param request: Request instance for DescribeSnapshotTask.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeSnapshotTaskRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeSnapshotTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTIWDailyUsage(self, request):
        """This API is used to query the daily billable usage of a whiteboard application.
        1. The period queried per request cannot be longer than 31 days.
        2. Due to statistics delays and other reasons, you cannot query the usage data of the current day. You can query today's usage after 7:00 tomorrow.

        :param request: Request instance for DescribeTIWDailyUsage.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeTIWDailyUsageRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeTIWDailyUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTIWDailyUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTIWDailyUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTIWRoomDailyUsage(self, request):
        """This API is used to query the daily billable usage by each room of a whiteboard application.
        1. The period queried per request cannot be longer than 31 days.
        2. Due to statistics delays and other reasons, you cannot query the usage data of the current day. You can query today's usage after 7:00 tomorrow.

        :param request: Request instance for DescribeTIWRoomDailyUsage.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeTIWRoomDailyUsageRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeTIWRoomDailyUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTIWRoomDailyUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTIWRoomDailyUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTranscode(self, request):
        """This API is used to query the progress and result of a document transcoding task.

        :param request: Request instance for DescribeTranscode.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTranscode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTranscodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTranscodeCallback(self, request):
        """This API is used to query the document transcoding callback address.

        :param request: Request instance for DescribeTranscodeCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTranscodeCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTranscodeCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTranscodeSearch(self, request):
        """This API is used to query transcoding tasks by document name.

        :param request: Request instance for DescribeTranscodeSearch.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeSearchRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeTranscodeSearchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTranscodeSearch", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTranscodeSearchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsageSummary(self, request):
        """This API is used to query the summary of subproduct usage within a specified period of time.

        :param request: Request instance for DescribeUsageSummary.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeUsageSummaryRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeUsageSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsageSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsageSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserList(self, request):
        """This API is used to query the users of a whiteboard application.

        :param request: Request instance for DescribeUserList.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeUserListRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeUserListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserResources(self, request):
        """This API is used to query user resources.

        :param request: Request instance for DescribeUserResources.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeUserResourcesRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeUserResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserResources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserStatus(self, request):
        """This API is used to query the Tencent Interactive Whiteboard service status of a user, including the activation status and validity period.

        :param request: Request instance for DescribeUserStatus.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeUserStatusRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeUserStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVideoGenerationTask(self, request):
        """This API is used to query the status and result of a recording video generation task.

        :param request: Request instance for DescribeVideoGenerationTask.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeVideoGenerationTaskRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeVideoGenerationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoGenerationTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoGenerationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVideoGenerationTaskCallback(self, request):
        """This API is used to query the callback URL for recording video generation.

        :param request: Request instance for DescribeVideoGenerationTaskCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeVideoGenerationTaskCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeVideoGenerationTaskCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoGenerationTaskCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoGenerationTaskCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWhiteboardApplicationConfig(self, request):
        """This API is used to query the task-related configurations of a whiteboard application, including the bucket and callback URL.

        :param request: Request instance for DescribeWhiteboardApplicationConfig.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardApplicationConfigRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardApplicationConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWhiteboardApplicationConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWhiteboardApplicationConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWhiteboardBucketConfig(self, request):
        """This API is used to query the bucket configurations for document transcoding and real-time recording.

        :param request: Request instance for DescribeWhiteboardBucketConfig.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardBucketConfigRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardBucketConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWhiteboardBucketConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWhiteboardBucketConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWhiteboardPush(self, request):
        """This API is used to query the status and result of a whiteboard push task.

        :param request: Request instance for DescribeWhiteboardPush.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardPushRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardPushResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWhiteboardPush", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWhiteboardPushResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWhiteboardPushCallback(self, request):
        """This API is used to query the whiteboard push callback URL.

        :param request: Request instance for DescribeWhiteboardPushCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardPushCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardPushCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWhiteboardPushCallback", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWhiteboardPushCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWhiteboardPushSearch(self, request):
        """This API is used to query whiteboard push tasks by room ID.

        :param request: Request instance for DescribeWhiteboardPushSearch.
        :type request: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardPushSearchRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.DescribeWhiteboardPushSearchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWhiteboardPushSearch", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWhiteboardPushSearchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyApplication(self, request):
        """This API is used to modify a whiteboard application.

        :param request: Request instance for ModifyApplication.
        :type request: :class:`tencentcloud.tiw.v20190919.models.ModifyApplicationRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.ModifyApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplication", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAutoRenewFlag(self, request):
        """This API is used to set auto-renewal for a Tencent Interactive Whiteboard monthly feature package.

        :param request: Request instance for ModifyAutoRenewFlag.
        :type request: :class:`tencentcloud.tiw.v20190919.models.ModifyAutoRenewFlagRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.ModifyAutoRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAutoRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAutoRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWhiteboardApplicationConfig(self, request):
        """This API is used to modify the task-related configurations of a whiteboard application, including the bucket and callback URL.

        :param request: Request instance for ModifyWhiteboardApplicationConfig.
        :type request: :class:`tencentcloud.tiw.v20190919.models.ModifyWhiteboardApplicationConfigRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.ModifyWhiteboardApplicationConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWhiteboardApplicationConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWhiteboardApplicationConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWhiteboardBucketConfig(self, request):
        """This API is used to modify the bucket configurations for document transcoding and real-time recording.

        :param request: Request instance for ModifyWhiteboardBucketConfig.
        :type request: :class:`tencentcloud.tiw.v20190919.models.ModifyWhiteboardBucketConfigRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.ModifyWhiteboardBucketConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWhiteboardBucketConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWhiteboardBucketConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PauseOnlineRecord(self, request):
        """This API is used to pause real-time recording.

        :param request: Request instance for PauseOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.PauseOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.PauseOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PauseOnlineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.PauseOnlineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeOnlineRecord(self, request):
        """This API is used to resume real-time recording.

        :param request: Request instance for ResumeOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.ResumeOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.ResumeOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeOnlineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeOnlineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetOfflineRecordCallback(self, request):
        """课后录制服务已下线

        This API is used to set the offline recording callback URL.

        :param request: Request instance for SetOfflineRecordCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetOfflineRecordCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetOfflineRecordCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetOfflineRecordCallback", params, headers=headers)
            response = json.loads(body)
            model = models.SetOfflineRecordCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetOnlineRecordCallback(self, request):
        """This API is used to set the real-time recording callback address. For the callback format, please [see here](https://intl.cloud.tencent.com/document/product/1137/40258?from_cn_redirect=1).

        :param request: Request instance for SetOnlineRecordCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetOnlineRecordCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetOnlineRecordCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetOnlineRecordCallback", params, headers=headers)
            response = json.loads(body)
            model = models.SetOnlineRecordCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetOnlineRecordCallbackKey(self, request):
        """This API is used to set the callback authentication key for real-time recording. For more information, see [Event Notification](https://intl.cloud.tencent.com/document/product/1137/40257?from_cn_redirect=1).

        :param request: Request instance for SetOnlineRecordCallbackKey.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetOnlineRecordCallbackKeyRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetOnlineRecordCallbackKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetOnlineRecordCallbackKey", params, headers=headers)
            response = json.loads(body)
            model = models.SetOnlineRecordCallbackKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetTranscodeCallback(self, request):
        """This API is used to set the callback address for document transcoding. For the callback format, please [see here](https://intl.cloud.tencent.com/document/product/1137/40260?from_cn_redirect=1).

        :param request: Request instance for SetTranscodeCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetTranscodeCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetTranscodeCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetTranscodeCallback", params, headers=headers)
            response = json.loads(body)
            model = models.SetTranscodeCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetTranscodeCallbackKey(self, request):
        """This API is used to set the callback authentication key for document transcoding. For more information, see [Event Notification](https://intl.cloud.tencent.com/document/product/1137/40257?from_cn_redirect=1).

        :param request: Request instance for SetTranscodeCallbackKey.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetTranscodeCallbackKeyRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetTranscodeCallbackKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetTranscodeCallbackKey", params, headers=headers)
            response = json.loads(body)
            model = models.SetTranscodeCallbackKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetVideoGenerationTaskCallback(self, request):
        """This API is used to set the callback URL for recording video generation.

        :param request: Request instance for SetVideoGenerationTaskCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetVideoGenerationTaskCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetVideoGenerationTaskCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetVideoGenerationTaskCallback", params, headers=headers)
            response = json.loads(body)
            model = models.SetVideoGenerationTaskCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetVideoGenerationTaskCallbackKey(self, request):
        """This API is used to set the callback authentication key for recording video generation.

        :param request: Request instance for SetVideoGenerationTaskCallbackKey.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetVideoGenerationTaskCallbackKeyRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetVideoGenerationTaskCallbackKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetVideoGenerationTaskCallbackKey", params, headers=headers)
            response = json.loads(body)
            model = models.SetVideoGenerationTaskCallbackKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetWhiteboardPushCallback(self, request):
        """This API is used to set the whiteboard push callback URL. For more information, see [Event Notification](https://intl.cloud.tencent.com/document/product/1137/40257?from_cn_redirect=1).

        :param request: Request instance for SetWhiteboardPushCallback.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetWhiteboardPushCallbackRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetWhiteboardPushCallbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetWhiteboardPushCallback", params, headers=headers)
            response = json.loads(body)
            model = models.SetWhiteboardPushCallbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetWhiteboardPushCallbackKey(self, request):
        """This API is used to set the callback authentication key for whiteboard push. For more information, see [Event Notification](https://intl.cloud.tencent.com/document/product/1137/40257?from_cn_redirect=1).

        :param request: Request instance for SetWhiteboardPushCallbackKey.
        :type request: :class:`tencentcloud.tiw.v20190919.models.SetWhiteboardPushCallbackKeyRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.SetWhiteboardPushCallbackKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetWhiteboardPushCallbackKey", params, headers=headers)
            response = json.loads(body)
            model = models.SetWhiteboardPushCallbackKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartOnlineRecord(self, request):
        """This API is used to start a real-time recording task.

        :param request: Request instance for StartOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.StartOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.StartOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartOnlineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.StartOnlineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartWhiteboardPush(self, request):
        """This API is used to start a whiteboard push task.

        :param request: Request instance for StartWhiteboardPush.
        :type request: :class:`tencentcloud.tiw.v20190919.models.StartWhiteboardPushRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.StartWhiteboardPushResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartWhiteboardPush", params, headers=headers)
            response = json.loads(body)
            model = models.StartWhiteboardPushResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopOnlineRecord(self, request):
        """This API is used to stop real-time recording.

        :param request: Request instance for StopOnlineRecord.
        :type request: :class:`tencentcloud.tiw.v20190919.models.StopOnlineRecordRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.StopOnlineRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopOnlineRecord", params, headers=headers)
            response = json.loads(body)
            model = models.StopOnlineRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopWhiteboardPush(self, request):
        """This API is used to stop a whiteboard push task.

        :param request: Request instance for StopWhiteboardPush.
        :type request: :class:`tencentcloud.tiw.v20190919.models.StopWhiteboardPushRequest`
        :rtype: :class:`tencentcloud.tiw.v20190919.models.StopWhiteboardPushResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopWhiteboardPush", params, headers=headers)
            response = json.loads(body)
            model = models.StopWhiteboardPushResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))