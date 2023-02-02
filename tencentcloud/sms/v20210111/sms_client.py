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
from tencentcloud.sms.v20210111 import models


class SmsClient(AbstractClient):
    _apiVersion = '2021-01-11'
    _endpoint = 'sms.tencentcloudapi.com'
    _service = 'sms'


    def AddSmsSign(self, request):
        """1. This API is used to add an SMS signature. You need to read the [Tencent Cloud SMS Signature Review Standards](https://intl.cloud.tencent.com/zh/document/product/382/40658) before starting an application.
        2. ⚠️ Note: individual users cannot use this API to apply for SMS signatures. For more information, see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1). If your account identity is individual, you can log in to the console to apply for SMS signatures.
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.

        :param request: Request instance for AddSmsSign.
        :type request: :class:`tencentcloud.sms.v20210111.models.AddSmsSignRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.AddSmsSignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddSmsSign", params, headers=headers)
            response = json.loads(body)
            model = models.AddSmsSignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddSmsTemplate(self, request):
        """1. This API is used to add an SMS template. You need to read the [Tencent Cloud SMS Body Template Review Standards](https://intl.cloud.tencent.com/zh/document/product/382/40659) before starting an application.
        2. ⚠️ Note: individual users cannot use this API to apply for SMS body templates. For more information, see [Identity Verification Overview](https://intl.cloud.tencent.com/zh/document/product/378/3629). If your account identity is individual, you can log in to the [console](https://console.cloud.tencent.com/smsv2) to apply for SMS body templates.
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.

        :param request: Request instance for AddSmsTemplate.
        :type request: :class:`tencentcloud.sms.v20210111.models.AddSmsTemplateRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.AddSmsTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddSmsTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.AddSmsTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CallbackStatusStatistics(self, request):
        """This API is used to collect statistics on user receipts.
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.

        :param request: Request instance for CallbackStatusStatistics.
        :type request: :class:`tencentcloud.sms.v20210111.models.CallbackStatusStatisticsRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.CallbackStatusStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CallbackStatusStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.CallbackStatusStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSmsSign(self, request):
        """⚠️ Note: individual users cannot use this API to delete SMS signatures. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1). Please log in to the [console](https://console.cloud.tencent.com/smsv2) to delete SMS signatures.
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.

        :param request: Request instance for DeleteSmsSign.
        :type request: :class:`tencentcloud.sms.v20210111.models.DeleteSmsSignRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.DeleteSmsSignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSmsSign", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSmsSignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSmsTemplate(self, request):
        """⚠️ Note: individual users cannot use this API to delete SMS body templates. Please log in to the [console](https://console.cloud.tencent.com/smsv2) to do so. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1).
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.

        :param request: Request instance for DeleteSmsTemplate.
        :type request: :class:`tencentcloud.sms.v20210111.models.DeleteSmsTemplateRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.DeleteSmsTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSmsTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSmsTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePhoneNumberInfo(self, request):
        """This API is used to query the information of a phone number, including country/region code and standardized E.164 format number.
        >- For example, if you query the number +86018845720123, you can get the country/region code 86 and the standardized E.164 number +8618845720123.

        :param request: Request instance for DescribePhoneNumberInfo.
        :type request: :class:`tencentcloud.sms.v20210111.models.DescribePhoneNumberInfoRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.DescribePhoneNumberInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePhoneNumberInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePhoneNumberInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSmsSignList(self, request):
        """⚠️ Note: individual users cannot use this API to query SMS signatures. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1). If your account identity is individual, you can log in to the [console](https://console.cloud.tencent.com/smsv2) to query SMS signatures.
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.

        :param request: Request instance for DescribeSmsSignList.
        :type request: :class:`tencentcloud.sms.v20210111.models.DescribeSmsSignListRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.DescribeSmsSignListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSmsSignList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSmsSignListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSmsTemplateList(self, request):
        """⚠️ Note: individual users cannot use this API to query SMS body templates. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1).
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.

        :param request: Request instance for DescribeSmsTemplateList.
        :type request: :class:`tencentcloud.sms.v20210111.models.DescribeSmsTemplateListRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.DescribeSmsTemplateListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSmsTemplateList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSmsTemplateListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySmsSign(self, request):
        """1. This API is used to modify an SMS signature. Read the [Tencent Cloud SMS signature review standards](https://intl.cloud.tencent.com/document/product/382/40658) before making a modification.
        2. ⚠️ Note: Individual users cannot use this API to modify SMS signatures. For more information, see [Identity Verification Guide](https://intl.cloud.tencent.com/document/product/378/3629). If your account identity is individual, you can log in to the [console](https://console.cloud.tencent.com/smsv2) to modify SMS signatures.
        3. Modifications can be made only if the signature status is **Pending Review** or **Rejected**. **Approved** signatures cannot be modified.
        >- Note: Because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.

        :param request: Request instance for ModifySmsSign.
        :type request: :class:`tencentcloud.sms.v20210111.models.ModifySmsSignRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.ModifySmsSignResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySmsSign", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySmsSignResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySmsTemplate(self, request):
        """1. This API is used to modify an SMS body template. Please read the [Tencent Cloud SMS Body Template Review Standards](https://intl.cloud.tencent.com/document/product/382/39023?from_cn_redirect=1) before making a modification.
        2. ⚠️ Note: individual users cannot use this API to modify SMS body templates. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1). If your account identity is individual, you can log in to the [console](https://console.cloud.tencent.com/smsv2) to modify SMS body templates.
        3. Modifications can be made only if the body template status is **Pending Review** or **Rejected**. **Approved** body templates cannot be modified.
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2019-07-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.

        :param request: Request instance for ModifySmsTemplate.
        :type request: :class:`tencentcloud.sms.v20210111.models.ModifySmsTemplateRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.ModifySmsTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySmsTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySmsTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PullSmsReplyStatus(self, request):
        """This API is used to pull SMS reply status.
        Currently, you can also [configure the reply callback](https://intl.cloud.tencent.com/document/product/382/42907?from_cn_redirect=1) to get replies.
        >- Note: You need to contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) to activate this API.
        >- Note: Because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.

        :param request: Request instance for PullSmsReplyStatus.
        :type request: :class:`tencentcloud.sms.v20210111.models.PullSmsReplyStatusRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.PullSmsReplyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PullSmsReplyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.PullSmsReplyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PullSmsReplyStatusByPhoneNumber(self, request):
        """This API is used to pull SMS reply status for one single number.
        Currently, you can also [configure the reply callback](https://intl.cloud.tencent.com/document/product/382/42907?from_cn_redirect=1) to get replies.
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.

        :param request: Request instance for PullSmsReplyStatusByPhoneNumber.
        :type request: :class:`tencentcloud.sms.v20210111.models.PullSmsReplyStatusByPhoneNumberRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.PullSmsReplyStatusByPhoneNumberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PullSmsReplyStatusByPhoneNumber", params, headers=headers)
            response = json.loads(body)
            model = models.PullSmsReplyStatusByPhoneNumberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PullSmsSendStatus(self, request):
        """This API is used to pull SMS delivery status.
        Currently, you can also [configure the callback](https://intl.cloud.tencent.com/document/product/382/37809?from_cn_redirect=1#.E8.AE.BE.E7.BD.AE.E4.BA.8B.E4.BB.B6.E5.9B.9E.E8.B0.83.E9.85.8D.E7.BD.AE) to get the delivery status.
        >- Note: you need to contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81) to activate this API.
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.

        :param request: Request instance for PullSmsSendStatus.
        :type request: :class:`tencentcloud.sms.v20210111.models.PullSmsSendStatusRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.PullSmsSendStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PullSmsSendStatus", params, headers=headers)
            response = json.loads(body)
            model = models.PullSmsSendStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PullSmsSendStatusByPhoneNumber(self, request):
        """This API is used to pull SMS delivery status for one single number.
        Currently, you can also [configure the callback](https://intl.cloud.tencent.com/document/product/382/37809?from_cn_redirect=1#.E8.AE.BE.E7.BD.AE.E4.BA.8B.E4.BB.B6.E5.9B.9E.E8.B0.83.E9.85.8D.E7.BD.AE) to get the delivery status.
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms) to eliminate the need to calculate signatures. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.

        :param request: Request instance for PullSmsSendStatusByPhoneNumber.
        :type request: :class:`tencentcloud.sms.v20210111.models.PullSmsSendStatusByPhoneNumberRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.PullSmsSendStatusByPhoneNumberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PullSmsSendStatusByPhoneNumber", params, headers=headers)
            response = json.loads(body)
            model = models.PullSmsSendStatusByPhoneNumberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReportConversion(self, request):
        """This API is used to report the SMS conversion rate (SMS conversion rate = the number of returned verification codes / the number of verification codes sent) and report the serial numbers of received SMS messages to Tencent Cloud SMS.
        >- Note: To call this API, you need to be added to the allowlist first. If you have any questions, contact [SMS Helper](https://intl.cloud.tencent.com/document/product/382/3773?from_cn_redirect=1#.E6.8A.80.E6.9C.AF.E4.BA.A4.E6.B5.81).

        :param request: Request instance for ReportConversion.
        :type request: :class:`tencentcloud.sms.v20210111.models.ReportConversionRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.ReportConversionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportConversion", params, headers=headers)
            response = json.loads(body)
            model = models.ReportConversionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SendSms(self, request):
        """This API is used to send SMS verification codes, notification, or marketing messages to users.
        >- Note: Because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the [SDK](https://intl.cloud.tencent.com/document/product/382/43193?from_cn_redirect=1).
        >- Note: You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.
        >- Note: This API is currently on the 2021-01-11 version. If you are still using the [2019-07-11 version](https://intl.cloud.tencent.com/document/product/382/38778?from_cn_redirect=1), we recommend you use this latest version. For version differences, see [Version description](https://intl.cloud.tencent.com/document/product/382/63195?from_cn_redirect=1#.E7.89.88.E6.9C.AC.E6.8F.8F.E8.BF.B0).

        :param request: Request instance for SendSms.
        :type request: :class:`tencentcloud.sms.v20210111.models.SendSmsRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.SendSmsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendSms", params, headers=headers)
            response = json.loads(body)
            model = models.SendSmsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SendStatusStatistics(self, request):
        """This API is used to collect statistics on SMS messages sent by users.
        >- Note: because of the improved security of **TencentCloud API 3.0**, **API authentication** is more complicated. We recommend you use the Tencent Cloud SMS service with the SDK.
        >- You can run this API directly in [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=sms&Version=2021-01-11&Action=SendSms), which eliminates the signature calculation steps. After it is executed successfully, API Explorer can **automatically generate** SDK code samples.

        :param request: Request instance for SendStatusStatistics.
        :type request: :class:`tencentcloud.sms.v20210111.models.SendStatusStatisticsRequest`
        :rtype: :class:`tencentcloud.sms.v20210111.models.SendStatusStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendStatusStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.SendStatusStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)