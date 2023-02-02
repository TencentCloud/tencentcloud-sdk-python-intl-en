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
from tencentcloud.dms.v20200819 import models


class DmsClient(AbstractClient):
    _apiVersion = '2020-08-19'
    _endpoint = 'dms.tencentcloudapi.com'
    _service = 'dms'


    def SendEmail(self, request):
        """This API is used to send regular emails.

        :param request: Request instance for SendEmail.
        :type request: :class:`tencentcloud.dms.v20200819.models.SendEmailRequest`
        :rtype: :class:`tencentcloud.dms.v20200819.models.SendEmailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendEmail", params, headers=headers)
            response = json.loads(body)
            model = models.SendEmailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SendTemplatedEmail(self, request):
        """This API is used to send template emails.

        :param request: Request instance for SendTemplatedEmail.
        :type request: :class:`tencentcloud.dms.v20200819.models.SendTemplatedEmailRequest`
        :rtype: :class:`tencentcloud.dms.v20200819.models.SendTemplatedEmailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendTemplatedEmail", params, headers=headers)
            response = json.loads(body)
            model = models.SendTemplatedEmailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)