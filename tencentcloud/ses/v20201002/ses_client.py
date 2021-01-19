# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.ses.v20201002 import models


class SesClient(AbstractClient):
    _apiVersion = '2020-10-02'
    _endpoint = 'ses.tencentcloudapi.com'
    _service = 'ses'


    def CreateEmailAddress(self, request):
        """After the sender domain is verified, you need a sender address to send emails. For example, if your sender domain is mail.qcloud.com, your sender address can be service@mail.qcloud.com. If you want to display your name (such as "Tencent Cloud") in the inbox list of the recipients, the sender address should be in the format of `Tencent Cloud <email address>`. Please note that there must be a space between your name and the first angle bracket.

        :param request: Request instance for CreateEmailAddress.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateEmailAddressRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateEmailAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateEmailAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEmailAddressResponse()
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


    def CreateEmailIdentity(self, request):
        """This API is used to create a sender domain. Before you can send an email using Tencent Cloud SES, you must create a sender domain as your identity. It can be the domain of your website or mobile app. You must verify the domain to prove that you own it and authorize Tencent Cloud SES to use it to send emails.

        :param request: Request instance for CreateEmailIdentity.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateEmailIdentityRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateEmailIdentityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateEmailIdentity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEmailIdentityResponse()
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


    def CreateEmailTemplate(self, request):
        """This API is used to create a TEXT or HTML email template. To create an HTML template, ensure that it does not include external CSS files. You can use {{variable name}} to specify a variable in the template.
        Note: only an approved template can be used to send emails.

        :param request: Request instance for CreateEmailTemplate.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateEmailTemplateRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateEmailTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateEmailTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEmailTemplateResponse()
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


    def DeleteBlackList(self, request):
        """This API is used to unblocklist email addresses. If you confirm that a blocklisted recipient address is valid and active, you can remove it from Tencent Cloud’s address blocklist database.

        :param request: Request instance for DeleteBlackList.
        :type request: :class:`tencentcloud.ses.v20201002.models.DeleteBlackListRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.DeleteBlackListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteBlackList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteBlackListResponse()
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


    def DeleteEmailAddress(self, request):
        """This API is used to delete a sender address.

        :param request: Request instance for DeleteEmailAddress.
        :type request: :class:`tencentcloud.ses.v20201002.models.DeleteEmailAddressRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.DeleteEmailAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteEmailAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEmailAddressResponse()
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


    def DeleteEmailIdentity(self, request):
        """This API is used to delete a sender domain. After deleted, the sender domain can no longer be used to send emails.

        :param request: Request instance for DeleteEmailIdentity.
        :type request: :class:`tencentcloud.ses.v20201002.models.DeleteEmailIdentityRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.DeleteEmailIdentityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteEmailIdentity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEmailIdentityResponse()
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


    def DeleteEmailTemplate(self, request):
        """This API is used to delete an email template.

        :param request: Request instance for DeleteEmailTemplate.
        :type request: :class:`tencentcloud.ses.v20201002.models.DeleteEmailTemplateRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.DeleteEmailTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteEmailTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEmailTemplateResponse()
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


    def GetEmailIdentity(self, request):
        """This API is used to get the configuration details of a sender domain.

        :param request: Request instance for GetEmailIdentity.
        :type request: :class:`tencentcloud.ses.v20201002.models.GetEmailIdentityRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.GetEmailIdentityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetEmailIdentity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetEmailIdentityResponse()
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


    def GetEmailTemplate(self, request):
        """This API is used to get the details of a template.

        :param request: Request instance for GetEmailTemplate.
        :type request: :class:`tencentcloud.ses.v20201002.models.GetEmailTemplateRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.GetEmailTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetEmailTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetEmailTemplateResponse()
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


    def GetStatisticsReport(self, request):
        """This API is used to get the email sending statistics over a recent period, including data on sent emails, delivery success rate, open rate, bounce rate, and so on. The maximum time span is 14 days.

        :param request: Request instance for GetStatisticsReport.
        :type request: :class:`tencentcloud.ses.v20201002.models.GetStatisticsReportRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.GetStatisticsReportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetStatisticsReport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetStatisticsReportResponse()
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


    def ListBlackEmailAddress(self, request):
        """The API is used to get blocklisted addresses. In the case of a hard bounce, Tencent Cloud will blocklist the recipient address and do not allow any user to send emails to this address. If you confirm that this is a misjudgment, you can remove it from the blocklist.

        :param request: Request instance for ListBlackEmailAddress.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListBlackEmailAddressRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListBlackEmailAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListBlackEmailAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListBlackEmailAddressResponse()
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


    def ListEmailAddress(self, request):
        """This API is used to get the list of sender addresses.

        :param request: Request instance for ListEmailAddress.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListEmailAddressRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListEmailAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListEmailAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListEmailAddressResponse()
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


    def ListEmailIdentities(self, request):
        """This API is used to get the list of sender domains, including verified and unverified domains.

        :param request: Request instance for ListEmailIdentities.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListEmailIdentitiesRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListEmailIdentitiesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListEmailIdentities", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListEmailIdentitiesResponse()
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


    def ListEmailTemplates(self, request):
        """This API is used to get the list of email templates.

        :param request: Request instance for ListEmailTemplates.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListEmailTemplatesRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListEmailTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListEmailTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListEmailTemplatesResponse()
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


    def SendEmail(self, request):
        """This API is used to send a TEXT or HTML email. By default, you can only send emails using a template. To send custom content, please contact your sales rep to enable this feature.

        :param request: Request instance for SendEmail.
        :type request: :class:`tencentcloud.ses.v20201002.models.SendEmailRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.SendEmailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SendEmail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendEmailResponse()
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


    def UpdateEmailIdentity(self, request):
        """This API is used to verify whether your DNS configuration is correct.

        :param request: Request instance for UpdateEmailIdentity.
        :type request: :class:`tencentcloud.ses.v20201002.models.UpdateEmailIdentityRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.UpdateEmailIdentityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateEmailIdentity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateEmailIdentityResponse()
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


    def UpdateEmailTemplate(self, request):
        """This API is used to update an email template. An updated template must be approved again before it can be used.

        :param request: Request instance for UpdateEmailTemplate.
        :type request: :class:`tencentcloud.ses.v20201002.models.UpdateEmailTemplateRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.UpdateEmailTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateEmailTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateEmailTemplateResponse()
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