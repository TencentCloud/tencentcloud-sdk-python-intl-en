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
from tencentcloud.tmt.v20180321 import models


class TmtClient(AbstractClient):
    _apiVersion = '2018-03-21'
    _endpoint = 'tmt.intl.tencentcloudapi.com'
    _service = 'tmt'


    def ImageTranslateLLM(self, request):
        r"""This API is used to provide translation service for images in 18 languages. It can automatically recognize text content in images and translate it into the target language. The recognized text is translated line by line, and a version that supports paragraph translation will be offered subsequently.

        -Input image format: png, jpg, jpeg and other common image formats. gif animation is not supported.
        -Output image format: jpg.

        Notification: For general developers, we recommend prioritizing SDK integration to simplify development. For SDK usage introduction, directly view the 5. Developer Resources part.

        :param request: Request instance for ImageTranslateLLM.
        :type request: :class:`tencentcloud.tmt.v20180321.models.ImageTranslateLLMRequest`
        :rtype: :class:`tencentcloud.tmt.v20180321.models.ImageTranslateLLMResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImageTranslateLLM", params, headers=headers)
            response = json.loads(body)
            model = models.ImageTranslateLLMResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))