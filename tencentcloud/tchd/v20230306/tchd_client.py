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
from tencentcloud.tchd.v20230306 import models


class TchdClient(AbstractClient):
    _apiVersion = '2023-03-06'
    _endpoint = 'tchd.intl.tencentcloudapi.com'
    _service = 'tchd'


    def DescribeEvents(self, request):
        """This API is used to query the availability event list of tencent cloud services. It can be filtered by product, region, or event occurrence date.

        :param request: Request instance for DescribeEvents.
        :type request: :class:`tencentcloud.tchd.v20230306.models.DescribeEventsRequest`
        :rtype: :class:`tencentcloud.tchd.v20230306.models.DescribeEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))