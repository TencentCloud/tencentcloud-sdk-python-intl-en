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
from tencentcloud.captcha.v20190722 import models


class CaptchaClient(AbstractClient):
    _apiVersion = '2019-07-22'
    _endpoint = 'captcha.tencentcloudapi.com'
    _service = 'captcha'


    def DescribeCaptchaResult(self, request):
        """This API is used to query the result of CAPTCHA ticket verification (web and app).

        :param request: Request instance for DescribeCaptchaResult.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaResultRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCaptchaResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCaptchaResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)