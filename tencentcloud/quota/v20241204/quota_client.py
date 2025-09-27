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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.quota.v20241204 import models


class QuotaClient(AbstractClient):
    _apiVersion = '2024-12-04'
    _endpoint = 'quota.intl.tencentcloudapi.com'
    _service = 'quota'


    def CreateAlarm(self, request):
        r"""Add alarm rules

        :param request: Request instance for CreateAlarm.
        :type request: :class:`tencentcloud.quota.v20241204.models.CreateAlarmRequest`
        :rtype: :class:`tencentcloud.quota.v20241204.models.CreateAlarmResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAlarm", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAlarmResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAlarm(self, request):
        r"""Deletes alarm rules

        :param request: Request instance for DeleteAlarm.
        :type request: :class:`tencentcloud.quota.v20241204.models.DeleteAlarmRequest`
        :rtype: :class:`tencentcloud.quota.v20241204.models.DeleteAlarmResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAlarm", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAlarmResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarms(self, request):
        r"""This API is used to query the alarm rule list.

        :param request: Request instance for DescribeAlarms.
        :type request: :class:`tencentcloud.quota.v20241204.models.DescribeAlarmsRequest`
        :rtype: :class:`tencentcloud.quota.v20241204.models.DescribeAlarmsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarms", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableAlarm(self, request):
        r"""This API is used to enable alarm rules.

        :param request: Request instance for EnableAlarm.
        :type request: :class:`tencentcloud.quota.v20241204.models.EnableAlarmRequest`
        :rtype: :class:`tencentcloud.quota.v20241204.models.EnableAlarmResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableAlarm", params, headers=headers)
            response = json.loads(body)
            model = models.EnableAlarmResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAlarm(self, request):
        r"""Modifies alarm rules

        :param request: Request instance for UpdateAlarm.
        :type request: :class:`tencentcloud.quota.v20241204.models.UpdateAlarmRequest`
        :rtype: :class:`tencentcloud.quota.v20241204.models.UpdateAlarmResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAlarm", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAlarmResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))