# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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


    def CreateApp(self, request):
        """This API is used to create a GME application.

        :param request: Request instance for CreateApp.
        :type request: :class:`tencentcloud.gme.v20180711.models.CreateAppRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.CreateAppResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateApp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAppResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAppStatistics(self, request):
        """This API is used to get the usage statistics of a GME application, including those of voice chat, voice messaging and speech-to-text, phrase analysis, etc. The maximum query period is the past 30 days.

        :param request: Request instance for DescribeAppStatistics.
        :type request: :class:`tencentcloud.gme.v20180711.models.DescribeAppStatisticsRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeAppStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAppStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAppStatisticsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAppStatus(self, request):
        """This API is used to change the status of an application's master switch.

        :param request: Request instance for ModifyAppStatus.
        :type request: :class:`tencentcloud.gme.v20180711.models.ModifyAppStatusRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.ModifyAppStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAppStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAppStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)