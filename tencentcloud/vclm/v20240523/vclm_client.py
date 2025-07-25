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
from tencentcloud.vclm.v20240523 import models


class VclmClient(AbstractClient):
    _apiVersion = '2024-05-23'
    _endpoint = 'vclm.intl.tencentcloudapi.com'
    _service = 'vclm'


    def DescribeImageAnimateJob(self, request):
        """This API is used to query image animation tasks. The image animation feature supports generating videos based on dance movements and images to meet the needs of scenarios such as social entertainment and interactive marketing.

        :param request: Request instance for DescribeImageAnimateJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.DescribeImageAnimateJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.DescribeImageAnimateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageAnimateJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageAnimateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitImageAnimateJob(self, request):
        """This API is used to submit image animation tasks. The image animation feature supports generating videos based on dance movements and images to meet the needs of scenarios such as social entertainment and interactive marketing.

        :param request: Request instance for SubmitImageAnimateJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.SubmitImageAnimateJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.SubmitImageAnimateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitImageAnimateJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitImageAnimateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))