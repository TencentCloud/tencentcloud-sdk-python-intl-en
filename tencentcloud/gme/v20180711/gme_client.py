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
from tencentcloud.gme.v20180711 import models


class GmeClient(AbstractClient):
    _apiVersion = '2018-07-11'
    _endpoint = 'gme.tencentcloudapi.com'
    _service = 'gme'


    def CreateApp(self, request):
        """This API is used to create a GME application.

        :param request: Request instance for CreateApp.
        :type request: :class:`tencentcloud.gme.v20180711.models.CreateAppRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.CreateAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRoomMember(self, request):
        """This API is used to delete a room or remove members from the room.

        :param request: Request instance for DeleteRoomMember.
        :type request: :class:`tencentcloud.gme.v20180711.models.DeleteRoomMemberRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DeleteRoomMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRoomMember", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRoomMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAppStatistics(self, request):
        """This API is used to query the usage statistics of a GME application, including those of Voice Chat, Voice Message Service, Voice Analysis, etc. The maximum query period is the past 30 days.

        :param request: Request instance for DescribeAppStatistics.
        :type request: :class:`tencentcloud.gme.v20180711.models.DescribeAppStatisticsRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeAppStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAppStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplicationData(self, request):
        """This API is used to query data details for up to the past 90 days.

        :param request: Request instance for DescribeApplicationData.
        :type request: :class:`tencentcloud.gme.v20180711.models.DescribeApplicationDataRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeApplicationDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecordInfo(self, request):
        """This API is used to query a recording task.

        :param request: Request instance for DescribeRecordInfo.
        :type request: :class:`tencentcloud.gme.v20180711.models.DescribeRecordInfoRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeRecordInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecordInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskInfo(self, request):
        """This API is used to query the recording task in a room.

        :param request: Request instance for DescribeTaskInfo.
        :type request: :class:`tencentcloud.gme.v20180711.models.DescribeTaskInfoRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeTaskInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAppStatus(self, request):
        """This API is used to change the status of an application.

        :param request: Request instance for ModifyAppStatus.
        :type request: :class:`tencentcloud.gme.v20180711.models.ModifyAppStatusRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.ModifyAppStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAppStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAppStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRecordInfo(self, request):
        """This API is used to modify recording configurations.

        :param request: Request instance for ModifyRecordInfo.
        :type request: :class:`tencentcloud.gme.v20180711.models.ModifyRecordInfoRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.ModifyRecordInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRecordInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRecordInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartRecord(self, request):
        """This API is used to start recording.

        :param request: Request instance for StartRecord.
        :type request: :class:`tencentcloud.gme.v20180711.models.StartRecordRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.StartRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartRecord", params, headers=headers)
            response = json.loads(body)
            model = models.StartRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopRecord(self, request):
        """This API is used to stop recording.

        :param request: Request instance for StopRecord.
        :type request: :class:`tencentcloud.gme.v20180711.models.StopRecordRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.StopRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopRecord", params, headers=headers)
            response = json.loads(body)
            model = models.StopRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))