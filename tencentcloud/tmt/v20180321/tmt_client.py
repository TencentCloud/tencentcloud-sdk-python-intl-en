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
from tencentcloud.tmt.v20180321 import models


class TmtClient(AbstractClient):
    _apiVersion = '2018-03-21'
    _endpoint = 'tmt.tencentcloudapi.com'
    _service = 'tmt'


    def TextTranslate(self, request):
        """This API is used to translate text in multiple language pairs, such as Chinese-English.<br />
        Note: We recommend that you simplify your development with the SDK integration mode. For how to use the SDK, see Section 5 "Developer Resources".

        :param request: Request instance for TextTranslate.
        :type request: :class:`tencentcloud.tmt.v20180321.models.TextTranslateRequest`
        :rtype: :class:`tencentcloud.tmt.v20180321.models.TextTranslateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextTranslate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextTranslateResponse()
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