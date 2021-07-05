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
from tencentcloud.ip.v20210409 import models


class IpClient(AbstractClient):
    _apiVersion = '2021-04-09'
    _endpoint = 'ip.tencentcloudapi.com'
    _service = 'ip'


    def CreateAccount(self, request):
        """This API is used to create a Tencent Cloud account in the International Partner platform for a customer. After registration, the customer will be automatically bound to the partner account.

        Notes:<br>
        1. To create the Tencent Cloud account, the partner should enter and verify the customer’s email address and mobile number.<br>
        2. The customer needs to complete personal information after the first login.

        :param request: Request instance for CreateAccount.
        :type request: :class:`tencentcloud.ip.v20210409.models.CreateAccountRequest`
        :rtype: :class:`tencentcloud.ip.v20210409.models.CreateAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAccountResponse()
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


    def GetCountryCodes(self, request):
        """This API is used to obtain country and region codes.

        :param request: Request instance for GetCountryCodes.
        :type request: :class:`tencentcloud.ip.v20210409.models.GetCountryCodesRequest`
        :rtype: :class:`tencentcloud.ip.v20210409.models.GetCountryCodesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetCountryCodes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetCountryCodesResponse()
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