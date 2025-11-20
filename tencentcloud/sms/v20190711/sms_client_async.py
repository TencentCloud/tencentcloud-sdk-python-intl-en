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
from tencentcloud.sms.v20190711 import models
from typing import Dict


class SmsClient(AbstractClient):
    _apiVersion = '2019-07-11'
    _endpoint = 'sms.intl.tencentcloudapi.com'
    _service = 'sms'

    async def AddSmsSign(
            self,
            request: models.AddSmsSignRequest,
            opts: Dict = None,
    ) -> models.AddSmsSignResponse:
        """
        This API is used to add an SMS signature. Please read the [Tencent Cloud SMS Signature Review Standards](https://intl.cloud.tencent.com/document/product/382/39022?from_cn_redirect=1) before starting an application.
        > Note: individual users cannot use this API to apply for SMS signatures. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1). If your account identity is individual, please log in to the console to apply for SMS signatures. For detailed directions, please see [Creating SMS Signatures](https://intl.cloud.tencent.com/document/product/382/36136?from_cn_redirect=1#Sign).
        """
        
        kwargs = {}
        kwargs["action"] = "AddSmsSign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddSmsSignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddSmsTemplate(
            self,
            request: models.AddSmsTemplateRequest,
            opts: Dict = None,
    ) -> models.AddSmsTemplateResponse:
        """
        This API is used to add an SMS template. Please read the [Tencent Cloud SMS Body Template Review Standards](https://intl.cloud.tencent.com/document/product/382/39023?from_cn_redirect=1) before starting an application.
        > Note: individual users cannot use this API to apply for SMS body templates. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1). If your account identity is individual, please log in to the console to apply for SMS body templates. For detailed directions, please see [Creating SMS Body Templates](https://intl.cloud.tencent.com/document/product/382/36136?from_cn_redirect=1#Template).
        """
        
        kwargs = {}
        kwargs["action"] = "AddSmsTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddSmsTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CallbackStatusStatistics(
            self,
            request: models.CallbackStatusStatisticsRequest,
            opts: Dict = None,
    ) -> models.CallbackStatusStatisticsResponse:
        """
        This API is used to collect statistics on user receipts.
        """
        
        kwargs = {}
        kwargs["action"] = "CallbackStatusStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CallbackStatusStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSmsSign(
            self,
            request: models.DeleteSmsSignRequest,
            opts: Dict = None,
    ) -> models.DeleteSmsSignResponse:
        """
        > Note: individual users cannot use this API to delete SMS signatures. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1). You can log in to the console to delete SMS signatures. For detailed directions, please see the notes on deleting SMS signatures in [SMS Signature Operations](https://intl.cloud.tencent.com/document/product/382/36136?from_cn_redirect=1#Sign).
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSmsSign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSmsSignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSmsTemplate(
            self,
            request: models.DeleteSmsTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteSmsTemplateResponse:
        """
        > Note: individual users cannot use this API to delete SMS body templates. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1). You can log in to the console to delete SMS body templates. For detailed directions, please see the notes on deleting SMS body templates in [SMS Body Template Operations](https://intl.cloud.tencent.com/document/product/382/36136?from_cn_redirect=1#Template).
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSmsTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSmsTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSmsSignList(
            self,
            request: models.DescribeSmsSignListRequest,
            opts: Dict = None,
    ) -> models.DescribeSmsSignListResponse:
        """
        > Note: individual users cannot use this API to query SMS signatures. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSmsSignList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSmsSignListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSmsTemplateList(
            self,
            request: models.DescribeSmsTemplateListRequest,
            opts: Dict = None,
    ) -> models.DescribeSmsTemplateListResponse:
        """
        > Note: individual users cannot use this API to query SMS body templates. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSmsTemplateList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSmsTemplateListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySmsSign(
            self,
            request: models.ModifySmsSignRequest,
            opts: Dict = None,
    ) -> models.ModifySmsSignResponse:
        """
        This API is used to modify an SMS signature. Please read the [Tencent Cloud SMS Signature Review Standards](https://intl.cloud.tencent.com/document/product/382/39022?from_cn_redirect=1) before making a modification.
        >-  Note: individual users cannot use this API to modify SMS signatures. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1). If your account identity is individual, you can log in to the console to modify SMS signatures.
        >- Modifications can be made only if the signature status is **pending review** or **rejected**. **Approved** signatures cannot be modified.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySmsSign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySmsSignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySmsTemplate(
            self,
            request: models.ModifySmsTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifySmsTemplateResponse:
        """
        This API is used to modify an SMS body template. Please read the [Tencent Cloud SMS Body Template Review Standards](https://intl.cloud.tencent.com/document/product/382/39023?from_cn_redirect=1) before making a modification.
        >-  Note: individual users cannot use this API to modify SMS body templates. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1). If your account identity is individual, you can log in to the console to modify SMS body templates.
        >- Modifications can be made only if the body template status is **pending review** or **rejected**. **Approved** body templates cannot be modified.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySmsTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySmsTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PullSmsReplyStatus(
            self,
            request: models.PullSmsReplyStatusRequest,
            opts: Dict = None,
    ) -> models.PullSmsReplyStatusResponse:
        """
        This API is used to pull SMS reply status.
        """
        
        kwargs = {}
        kwargs["action"] = "PullSmsReplyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PullSmsReplyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PullSmsReplyStatusByPhoneNumber(
            self,
            request: models.PullSmsReplyStatusByPhoneNumberRequest,
            opts: Dict = None,
    ) -> models.PullSmsReplyStatusByPhoneNumberResponse:
        """
        This API is used to pull SMS reply status for one single number.
        """
        
        kwargs = {}
        kwargs["action"] = "PullSmsReplyStatusByPhoneNumber"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PullSmsReplyStatusByPhoneNumberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PullSmsSendStatus(
            self,
            request: models.PullSmsSendStatusRequest,
            opts: Dict = None,
    ) -> models.PullSmsSendStatusResponse:
        """
        This API is used to pull SMS delivery status.
        """
        
        kwargs = {}
        kwargs["action"] = "PullSmsSendStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PullSmsSendStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PullSmsSendStatusByPhoneNumber(
            self,
            request: models.PullSmsSendStatusByPhoneNumberRequest,
            opts: Dict = None,
    ) -> models.PullSmsSendStatusByPhoneNumberResponse:
        """
        This API is used to pull SMS delivery status for one single number.
        """
        
        kwargs = {}
        kwargs["action"] = "PullSmsSendStatusByPhoneNumber"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PullSmsSendStatusByPhoneNumberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendSms(
            self,
            request: models.SendSmsRequest,
            opts: Dict = None,
    ) -> models.SendSmsResponse:
        """
        This API is used to send SMS verification codes, notification, or marketing messages to users.

        """
        
        kwargs = {}
        kwargs["action"] = "SendSms"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendSmsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendStatusStatistics(
            self,
            request: models.SendStatusStatisticsRequest,
            opts: Dict = None,
    ) -> models.SendStatusStatisticsResponse:
        """
        This API is used to collect statistics on SMS sent by users.
        """
        
        kwargs = {}
        kwargs["action"] = "SendStatusStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendStatusStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SmsPackagesStatistics(
            self,
            request: models.SmsPackagesStatisticsRequest,
            opts: Dict = None,
    ) -> models.SmsPackagesStatisticsResponse:
        """
        This API is used to collect statistics on user's packages.
        """
        
        kwargs = {}
        kwargs["action"] = "SmsPackagesStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SmsPackagesStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)