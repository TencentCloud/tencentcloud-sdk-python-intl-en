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
from tencentcloud.bi.v20220105 import models


class BiClient(AbstractClient):
    _apiVersion = '2022-01-05'
    _endpoint = 'bi.intl.tencentcloudapi.com'
    _service = 'bi'


    def ApplyEmbedInterval(self, request):
        """This API is used to extend the available time of a token with strong authentication.

        :param request: Request instance for ApplyEmbedInterval.
        :type request: :class:`tencentcloud.bi.v20220105.models.ApplyEmbedIntervalRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.ApplyEmbedIntervalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyEmbedInterval", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyEmbedIntervalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDatasource(self, request):
        """This API is used to create a data source.

        :param request: Request instance for CreateDatasource.
        :type request: :class:`tencentcloud.bi.v20220105.models.CreateDatasourceRequest`
        :rtype: :class:`tencentcloud.bi.v20220105.models.CreateDatasourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDatasource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDatasourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))