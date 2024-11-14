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
from tencentcloud.aiart.v20221229 import models


class AiartClient(AbstractClient):
    _apiVersion = '2022-12-29'
    _endpoint = 'aiart.tencentcloudapi.com'
    _service = 'aiart'


    def ImageToImage(self, request):
        """This API is used to transfer the image style based on the image to image technology. Images with small figures, complex gestures or too many figures are not recommended.
        It supports 3 concurrency by default, which means that up to 3 submitted tasks can be processed simultaneously. Subsequent tasks can be processed only after ongoing ones are completed.

        :param request: Request instance for ImageToImage.
        :type request: :class:`tencentcloud.aiart.v20221229.models.ImageToImageRequest`
        :rtype: :class:`tencentcloud.aiart.v20221229.models.ImageToImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImageToImage", params, headers=headers)
            response = json.loads(body)
            model = models.ImageToImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))