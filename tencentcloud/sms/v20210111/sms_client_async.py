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
from tencentcloud.sms.v20210111 import models
from typing import Dict


class SmsClient(AbstractClient):
    _apiVersion = '2021-01-11'
    _endpoint = 'sms.intl.tencentcloudapi.com'
    _service = 'sms'

    async def AddSmsSign(
            self,
            request: models.AddSmsSignRequest,
            opts: Dict = None,
    ) -> models.AddSmsSignResponse:
        """
        1. This API is used to add an SMS signature. You need to read the [Tencent Cloud SMS Signature Review Standards](https://intl.cloud.tencent.com/zh/document/product/382/40658) before starting an application.
        2. ⚠️ Note: individual users cannot use this API to apply for SMS signatures. For more information, see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1). If your account identity is individual, you can log in to the console to apply for SMS signatures.
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.
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
        1. This API is used to add an SMS template. You need to read the [Tencent Cloud SMS Body Template Review Standards](https://intl.cloud.tencent.com/zh/document/product/382/40659) before starting an application.
        2. Note: individual users cannot use this API to apply for SMS body templates. For more information, see [Identity Verification Overview](https://intl.cloud.tencent.com/zh/document/product/378/3629). If your account identity is individual, you can log in to the [console](https://console.cloud.tencent.com/smsv2) to apply for SMS body templates.
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.
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
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.
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
        ⚠️ Note: individual users cannot use this API to delete SMS signatures. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1). Please log in to the [console](https://console.cloud.tencent.com/smsv2) to delete SMS signatures.
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.
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
        ⚠️ Note: individual users cannot use this API to delete SMS body templates. Please log in to the [console](https://console.cloud.tencent.com/smsv2) to do so. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1).
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSmsTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSmsTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePhoneNumberInfo(
            self,
            request: models.DescribePhoneNumberInfoRequest,
            opts: Dict = None,
    ) -> models.DescribePhoneNumberInfoResponse:
        """
        This API is used to query the information of a phone number, including country/region code and standardized E.164 format number.
        >- For example, if you query the number +86018845720123, you can get the country/region code 86 and the standardized E.164 number +8618845720123.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePhoneNumberInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePhoneNumberInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSmsSignList(
            self,
            request: models.DescribeSmsSignListRequest,
            opts: Dict = None,
    ) -> models.DescribeSmsSignListResponse:
        """
        ⚠️ Note: individual users cannot use this API to query SMS signatures. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1). If your account identity is individual, you can log in to the [console](https://console.cloud.tencent.com/smsv2) to query SMS signatures.
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.
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
        ⚠️ Note: individual users cannot use this API to query SMS body templates. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1).
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.
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
        1. This API is used to modify an SMS signature. Read the [Tencent Cloud SMS signature review standards](https://intl.cloud.tencent.com/document/product/382/40658) before making a modification.
        2. ⚠️ Note: Individual users cannot use this API to modify SMS signatures. For more information, see [Identity Verification Guide](https://intl.cloud.tencent.com/document/product/378/3629). If your account identity is individual, you can log in to the [console](https://console.cloud.tencent.com/smsv2) to modify SMS signatures.
        3. Modifications can be made only if the signature status is **Pending Review** or **Rejected**. **Approved** signatures cannot be modified.
        >- Note: Because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.
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
        1. This API is used to modify an SMS body template. Please read the [Tencent Cloud SMS Body Template Review Standards](https://intl.cloud.tencent.com/document/product/382/39023?from_cn_redirect=1) before making a modification.
        2. Note: individual users cannot use this API to modify SMS body templates. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1). If your account identity is individual, you can log in to the [console](https://console.cloud.tencent.com/smsv2) to modify SMS body templates.
        3. Modifications can be made only if the body template status is **Pending Review** or **Rejected**. **Approved** body templates cannot be modified.
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2019-07-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.
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
        Currently, you can also [configure the reply callback](https://intl.cloud.tencent.com/document/product/382/42907?from_cn_redirect=1) to get replies.
        >- Note: You need to contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) to activate this API.
        >- Note: Because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.
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
        Currently, you can also [configure the reply callback](https://intl.cloud.tencent.com/document/product/382/42907?from_cn_redirect=1) to get replies.
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.
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
        Currently, you can also [configure the callback](https://intl.cloud.tencent.com/document/product/382/37809?from_cn_redirect=1#.E8.AE.BE.E7.BD.AE.E4.BA.8B.E4.BB.B6.E5.9B.9E.E8.B0.83.E9.85.8D.E7.BD.AE) to get the delivery status.
        >- Note: you need to contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) to activate this API.
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.
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
        Currently, you can also [configure the callback](https://intl.cloud.tencent.com/document/product/382/37809?from_cn_redirect=1#.E8.AE.BE.E7.BD.AE.E4.BA.8B.E4.BB.B6.E5.9B.9E.E8.B0.83.E9.85.8D.E7.BD.AE) to get the delivery status.
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms) to eliminate the need to calculate signatures. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.
        """
        
        kwargs = {}
        kwargs["action"] = "PullSmsSendStatusByPhoneNumber"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PullSmsSendStatusByPhoneNumberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReportConversion(
            self,
            request: models.ReportConversionRequest,
            opts: Dict = None,
    ) -> models.ReportConversionResponse:
        """
        This API is used to report the SMS conversion rate (SMS conversion rate = the number of returned verification codes / the number of verification codes sent) and report the serial numbers of received SMS messages to Tencent Cloud SMS.
        >- Note: To call this API, you need to be added to the allowlist first. If you have any questions, contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81).
        """
        
        kwargs = {}
        kwargs["action"] = "ReportConversion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReportConversionResponse
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
        >- Note: Because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the [SDK](https://intl.cloud.tencent.com/document/product/382/43193?from_cn_redirect=1).
        >- Note: You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.
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
        This API is used to collect statistics on SMS messages sent by users.
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.
        """
        
        kwargs = {}
        kwargs["action"] = "SendStatusStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendStatusStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)