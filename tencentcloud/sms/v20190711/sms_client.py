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
from tencentcloud.sms.v20190711 import models


class SmsClient(AbstractClient):
    _apiVersion = '2019-07-11'
    _endpoint = 'sms.tencentcloudapi.com'
    _service = 'sms'


    def AddSmsSign(self, request):
        """This API is used to add an SMS signature. Please read the [Tencent Cloud SMS Signature Review Standards](https://intl.cloud.tencent.com/document/product/382/39022?from_cn_redirect=1) before starting an application.
        > Note: individual users cannot use this API to apply for SMS signatures. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1). If your account identity is individual, please log in to the console to apply for SMS signatures. For detailed directions, please see [Creating SMS Signatures](https://intl.cloud.tencent.com/document/product/382/36136?from_cn_redirect=1#Sign).

        :param request: Request instance for AddSmsSign.
        :type request: :class:`tencentcloud.sms.v20190711.models.AddSmsSignRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.AddSmsSignResponse`

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
        """This API is used to add an SMS template. Please read the [Tencent Cloud SMS Body Template Review Standards](https://intl.cloud.tencent.com/document/product/382/39023?from_cn_redirect=1) before starting an application.
        > Note: individual users cannot use this API to apply for SMS body templates. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1). If your account identity is individual, please log in to the console to apply for SMS body templates. For detailed directions, please see [Creating SMS Body Templates](https://intl.cloud.tencent.com/document/product/382/36136?from_cn_redirect=1#Template).

        :param request: Request instance for AddSmsTemplate.
        :type request: :class:`tencentcloud.sms.v20190711.models.AddSmsTemplateRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.AddSmsTemplateResponse`

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

        :param request: Request instance for CallbackStatusStatistics.
        :type request: :class:`tencentcloud.sms.v20190711.models.CallbackStatusStatisticsRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.CallbackStatusStatisticsResponse`

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
        """> Note: individual users cannot use this API to delete SMS signatures. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1). You can log in to the console to delete SMS signatures. For detailed directions, please see the notes on deleting SMS signatures in [SMS Signature Operations](https://intl.cloud.tencent.com/document/product/382/36136?from_cn_redirect=1#Sign).

        :param request: Request instance for DeleteSmsSign.
        :type request: :class:`tencentcloud.sms.v20190711.models.DeleteSmsSignRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.DeleteSmsSignResponse`

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
        """> Note: individual users cannot use this API to delete SMS body templates. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1). You can log in to the console to delete SMS body templates. For detailed directions, please see the notes on deleting SMS body templates in [SMS Body Template Operations](https://intl.cloud.tencent.com/document/product/382/36136?from_cn_redirect=1#Template).

        :param request: Request instance for DeleteSmsTemplate.
        :type request: :class:`tencentcloud.sms.v20190711.models.DeleteSmsTemplateRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.DeleteSmsTemplateResponse`

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


    def DescribeSmsSignList(self, request):
        """> Note: individual users cannot use this API to query SMS signatures. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1).

        :param request: Request instance for DescribeSmsSignList.
        :type request: :class:`tencentcloud.sms.v20190711.models.DescribeSmsSignListRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.DescribeSmsSignListResponse`

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
        """> Note: individual users cannot use this API to query SMS body templates. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1).

        :param request: Request instance for DescribeSmsTemplateList.
        :type request: :class:`tencentcloud.sms.v20190711.models.DescribeSmsTemplateListRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.DescribeSmsTemplateListResponse`

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
        """This API is used to modify an SMS signature. Please read the [Tencent Cloud SMS Signature Review Standards](https://intl.cloud.tencent.com/document/product/382/39022?from_cn_redirect=1) before making a modification.
        >-  Note: individual users cannot use this API to modify SMS signatures. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1). If your account identity is individual, you can log in to the console to modify SMS signatures.
        >- Modifications can be made only if the signature status is **pending review** or **rejected**. **Approved** signatures cannot be modified.

        :param request: Request instance for ModifySmsSign.
        :type request: :class:`tencentcloud.sms.v20190711.models.ModifySmsSignRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.ModifySmsSignResponse`

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
        """This API is used to modify an SMS body template. Please read the [Tencent Cloud SMS Body Template Review Standards](https://intl.cloud.tencent.com/document/product/382/39023?from_cn_redirect=1) before making a modification.
        >-  Note: individual users cannot use this API to modify SMS body templates. For more information, please see [Identity Verification Overview](https://intl.cloud.tencent.com/document/product/378/3629?from_cn_redirect=1). If your account identity is individual, you can log in to the console to modify SMS body templates.
        >- Modifications can be made only if the body template status is **pending review** or **rejected**. **Approved** body templates cannot be modified.

        :param request: Request instance for ModifySmsTemplate.
        :type request: :class:`tencentcloud.sms.v20190711.models.ModifySmsTemplateRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.ModifySmsTemplateResponse`

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

        :param request: Request instance for PullSmsReplyStatus.
        :type request: :class:`tencentcloud.sms.v20190711.models.PullSmsReplyStatusRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.PullSmsReplyStatusResponse`

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

        :param request: Request instance for PullSmsReplyStatusByPhoneNumber.
        :type request: :class:`tencentcloud.sms.v20190711.models.PullSmsReplyStatusByPhoneNumberRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.PullSmsReplyStatusByPhoneNumberResponse`

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

        :param request: Request instance for PullSmsSendStatus.
        :type request: :class:`tencentcloud.sms.v20190711.models.PullSmsSendStatusRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.PullSmsSendStatusResponse`

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

        :param request: Request instance for PullSmsSendStatusByPhoneNumber.
        :type request: :class:`tencentcloud.sms.v20190711.models.PullSmsSendStatusByPhoneNumberRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.PullSmsSendStatusByPhoneNumberResponse`

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


    def SendSms(self, request):
        """This API is used to send SMS verification codes, notification, or marketing messages to users.


        :param request: Request instance for SendSms.
        :type request: :class:`tencentcloud.sms.v20190711.models.SendSmsRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.SendSmsResponse`

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
        """This API is used to collect statistics on SMS sent by users.

        :param request: Request instance for SendStatusStatistics.
        :type request: :class:`tencentcloud.sms.v20190711.models.SendStatusStatisticsRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.SendStatusStatisticsResponse`

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


    def SmsPackagesStatistics(self, request):
        """This API is used to collect statistics on user's packages.

        :param request: Request instance for SmsPackagesStatistics.
        :type request: :class:`tencentcloud.sms.v20190711.models.SmsPackagesStatisticsRequest`
        :rtype: :class:`tencentcloud.sms.v20190711.models.SmsPackagesStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SmsPackagesStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.SmsPackagesStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)