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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.captcha.v20190722 import models
from typing import Dict


class CaptchaClient(AbstractClient):
    _apiVersion = '2019-07-22'
    _endpoint = 'captcha.intl.tencentcloudapi.com'
    _service = 'captcha'

    async def CreateCaptchaInfoInternational(
            self,
            request: models.CreateCaptchaInfoInternationalRequest,
            opts: Dict = None,
    ) -> models.CreateCaptchaInfoInternationalResponse:
        """
        Create a captcha: You can create multiple Captcha based on different business needs. Each verification has different client types and security policies. The limit for new Captcha is 50.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCaptchaInfoInternational"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCaptchaInfoInternationalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIpWhiteListInternational(
            self,
            request: models.CreateIpWhiteListInternationalRequest,
            opts: Dict = None,
    ) -> models.CreateIpWhiteListInternationalResponse:
        """
        Create an IP allowlist: You can create an IP allowlist based on different business needs.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIpWhiteListInternational"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIpWhiteListInternationalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIpWhiteListInternational(
            self,
            request: models.DeleteIpWhiteListInternationalRequest,
            opts: Dict = None,
    ) -> models.DeleteIpWhiteListInternationalResponse:
        """
        Delete an IP allowlist: You can delete an IP allowlist based on different business needs.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIpWhiteListInternational"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIpWhiteListInternationalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCaptchaInfoListInternational(
            self,
            request: models.DescribeCaptchaInfoListInternationalRequest,
            opts: Dict = None,
    ) -> models.DescribeCaptchaInfoListInternationalResponse:
        """
        Query the Captcha list to obtain all verification CaptchaAppIds, verification names, and other information internationally.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCaptchaInfoListInternational"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCaptchaInfoListInternationalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCaptchaResult(
            self,
            request: models.DescribeCaptchaResultRequest,
            opts: Dict = None,
    ) -> models.DescribeCaptchaResultResponse:
        """
        This API is used to query the result of CAPTCHA ticket verification (web and app).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCaptchaResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCaptchaResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIpWhiteListInternational(
            self,
            request: models.DescribeIpWhiteListInternationalRequest,
            opts: Dict = None,
    ) -> models.DescribeIpWhiteListInternationalResponse:
        """
        IP allowlist list: You can query the IP whitelist list based on different business needs.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIpWhiteListInternational"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIpWhiteListInternationalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCaptchaInfoInternational(
            self,
            request: models.ModifyCaptchaInfoInternationalRequest,
            opts: Dict = None,
    ) -> models.ModifyCaptchaInfoInternationalResponse:
        """
        Change the captcha configuration, including basic, appearance, and security settings such as captcha name, prompt language, and validation type.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCaptchaInfoInternational"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCaptchaInfoInternationalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIpWhiteListInternational(
            self,
            request: models.ModifyIpWhiteListInternationalRequest,
            opts: Dict = None,
    ) -> models.ModifyIpWhiteListInternationalResponse:
        """
        Edit IP allowlist: You can edit the IP allowlist based on different business needs.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIpWhiteListInternational"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIpWhiteListInternationalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveCaptchaInfoInternational(
            self,
            request: models.RemoveCaptchaInfoInternationalRequest,
            opts: Dict = None,
    ) -> models.RemoveCaptchaInfoInternationalResponse:
        """
        Delete a captcha: once deleted, verification scenarios using this CaptchaAppId will fail to load the verification code on the frontend, and invoice verification will report an error on the backend. Proceed with caution.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveCaptchaInfoInternational"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveCaptchaInfoInternationalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)