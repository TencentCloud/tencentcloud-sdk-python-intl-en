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
from tencentcloud.tms.v20201229 import models


class TmsClient(AbstractClient):
    _apiVersion = '2020-12-29'
    _endpoint = 'tms.intl.tencentcloudapi.com'
    _service = 'tms'


    def TextModeration(self, request):
        """This API is used to submit text content for intelligent moderation.

        ### Notes
        - Before invoking this API, be sure you have activated Tencent Cloud Text Moderation System in the [Content Moderation - Text Moderation System](https://console.cloud.tencent.com/cms/text/package) console.
        - This is a paid API. For the billing details, see [Text Moderation System Pricing](https://www.tencentcloud.com/document/product/1121/43752).








        ### Use limits
        - The submitted texts can not be longer than 10,000 unicode characters.
        - English letters, digits and Chinese characters are supported for moderation.
        - The API request frequency limit: **1,000 times/second**.

        :param request: Request instance for TextModeration.
        :type request: :class:`tencentcloud.tms.v20201229.models.TextModerationRequest`
        :rtype: :class:`tencentcloud.tms.v20201229.models.TextModerationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextModeration", params, headers=headers)
            response = json.loads(body)
            model = models.TextModerationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))