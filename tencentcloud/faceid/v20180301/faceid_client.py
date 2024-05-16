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
from tencentcloud.faceid.v20180301 import models


class FaceidClient(AbstractClient):
    _apiVersion = '2018-03-01'
    _endpoint = 'faceid.tencentcloudapi.com'
    _service = 'faceid'


    def ApplySdkVerificationToken(self, request):
        """This API is used to apply for a token before calling the Identity Verification SDK service each time. This token is required for initiating the verification process and getting the result after the verification is completed.

        :param request: Request instance for ApplySdkVerificationToken.
        :type request: :class:`tencentcloud.faceid.v20180301.models.ApplySdkVerificationTokenRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.ApplySdkVerificationTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplySdkVerificationToken", params, headers=headers)
            response = json.loads(body)
            model = models.ApplySdkVerificationTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetSdkVerificationResult(self, request):
        """This API is used to get the verification result with the corresponding token after the SDK-based verification is completed. The token is valid for three days after issuance and can be called multiple times.

        :param request: Request instance for GetSdkVerificationResult.
        :type request: :class:`tencentcloud.faceid.v20180301.models.GetSdkVerificationResultRequest`
        :rtype: :class:`tencentcloud.faceid.v20180301.models.GetSdkVerificationResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetSdkVerificationResult", params, headers=headers)
            response = json.loads(body)
            model = models.GetSdkVerificationResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))