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
from tencentcloud.captcha.v20190722 import models


class CaptchaClient(AbstractClient):
    _apiVersion = '2019-07-22'
    _endpoint = 'captcha.intl.tencentcloudapi.com'
    _service = 'captcha'


    def CreateCaptchaInfoInternational(self, request):
        r"""Create a captcha: You can create multiple Captcha based on different business needs. Each verification has different client types and security policies. The limit for new Captcha is 50.

        :param request: Request instance for CreateCaptchaInfoInternational.
        :type request: :class:`tencentcloud.captcha.v20190722.models.CreateCaptchaInfoInternationalRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.CreateCaptchaInfoInternationalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCaptchaInfoInternational", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCaptchaInfoInternationalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIpWhiteListInternational(self, request):
        r"""Create an IP allowlist: You can create an IP allowlist based on different business needs.

        :param request: Request instance for CreateIpWhiteListInternational.
        :type request: :class:`tencentcloud.captcha.v20190722.models.CreateIpWhiteListInternationalRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.CreateIpWhiteListInternationalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIpWhiteListInternational", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIpWhiteListInternationalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIpWhiteListInternational(self, request):
        r"""Delete an IP allowlist: You can delete an IP allowlist based on different business needs.

        :param request: Request instance for DeleteIpWhiteListInternational.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DeleteIpWhiteListInternationalRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DeleteIpWhiteListInternationalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIpWhiteListInternational", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIpWhiteListInternationalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCaptchaInfoListInternational(self, request):
        r"""Query the Captcha list to obtain all verification CaptchaAppIds, verification names, and other information internationally.

        :param request: Request instance for DescribeCaptchaInfoListInternational.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaInfoListInternationalRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeCaptchaInfoListInternationalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCaptchaInfoListInternational", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCaptchaInfoListInternationalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCaptchaResult(self, request):
        r"""This API is used to query the result of CAPTCHA ticket verification (web and app).

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIpWhiteListInternational(self, request):
        r"""IP allowlist list: You can query the IP whitelist list based on different business needs.

        :param request: Request instance for DescribeIpWhiteListInternational.
        :type request: :class:`tencentcloud.captcha.v20190722.models.DescribeIpWhiteListInternationalRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.DescribeIpWhiteListInternationalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIpWhiteListInternational", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIpWhiteListInternationalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCaptchaInfoInternational(self, request):
        r"""Change the captcha configuration, including basic, appearance, and security settings such as captcha name, prompt language, and validation type.

        :param request: Request instance for ModifyCaptchaInfoInternational.
        :type request: :class:`tencentcloud.captcha.v20190722.models.ModifyCaptchaInfoInternationalRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.ModifyCaptchaInfoInternationalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCaptchaInfoInternational", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCaptchaInfoInternationalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIpWhiteListInternational(self, request):
        r"""Edit IP allowlist: You can edit the IP allowlist based on different business needs.

        :param request: Request instance for ModifyIpWhiteListInternational.
        :type request: :class:`tencentcloud.captcha.v20190722.models.ModifyIpWhiteListInternationalRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.ModifyIpWhiteListInternationalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIpWhiteListInternational", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIpWhiteListInternationalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveCaptchaInfoInternational(self, request):
        r"""Delete a captcha: once deleted, verification scenarios using this CaptchaAppId will fail to load the verification code on the frontend, and invoice verification will report an error on the backend. Proceed with caution.

        :param request: Request instance for RemoveCaptchaInfoInternational.
        :type request: :class:`tencentcloud.captcha.v20190722.models.RemoveCaptchaInfoInternationalRequest`
        :rtype: :class:`tencentcloud.captcha.v20190722.models.RemoveCaptchaInfoInternationalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveCaptchaInfoInternational", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveCaptchaInfoInternationalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))