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
from tencentcloud.ses.v20201002 import models


class SesClient(AbstractClient):
    _apiVersion = '2020-10-02'
    _endpoint = 'ses.intl.tencentcloudapi.com'
    _service = 'ses'


    def BatchSendEmail(self, request):
        """This API is used to send a TEXT or HTML email to multiple recipients at a time for marketing or notification purposes. By default, you can send emails using a template only. You need to create a recipient group with email addresses first and then send emails by group ID. SES supports scheduled and recurring email sending tasks. You need to pass in `TimedParam` for a scheduled task and `CycleParam` for a recurring one.

        :param request: Request instance for BatchSendEmail.
        :type request: :class:`tencentcloud.ses.v20201002.models.BatchSendEmailRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.BatchSendEmailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchSendEmail", params, headers=headers)
            response = json.loads(body)
            model = models.BatchSendEmailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAddressUnsubscribeConfig(self, request):
        """This API is used to create an address-level unsubscribe configuration.

        :param request: Request instance for CreateAddressUnsubscribeConfig.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateAddressUnsubscribeConfigRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateAddressUnsubscribeConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAddressUnsubscribeConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAddressUnsubscribeConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEmailAddress(self, request):
        """After the sender domain is verified, you need a sender address to send emails. For example, if your sender domain is mail.qcloud.com, your sender address can be service@mail.qcloud.com. If you want to display your name (such as "Tencent Cloud") in the inbox list of the recipients, the sender address should be in the format of `Tencent Cloud <email address>`. Please note that there must be a space between your name and the first angle bracket.

        :param request: Request instance for CreateEmailAddress.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateEmailAddressRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateEmailAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEmailAddress", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEmailAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEmailIdentity(self, request):
        """This API is used to create a sender domain. Before you can send an email using Tencent Cloud SES, you must create a sender domain as your identity. It can be the domain of your website or mobile app. You must verify the domain to prove that you own it and authorize Tencent Cloud SES to use it to send emails.

        :param request: Request instance for CreateEmailIdentity.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateEmailIdentityRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateEmailIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEmailIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEmailIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEmailTemplate(self, request):
        """This API is used to create a TEXT or HTML email template. To create an HTML template, ensure that it does not include external CSS files. You can use {{variable name}} to specify a variable in the template.
        Note: Only an approved template can be used to send emails.

        :param request: Request instance for CreateEmailTemplate.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateEmailTemplateRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateEmailTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEmailTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEmailTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReceiver(self, request):
        """This API is used to create a recipient group, which is the list of target email addresses for batch sending emails. After creating a group, you need to upload recipient email addresses. Then, you can create a sending task and select the group to batch send emails.

        :param request: Request instance for CreateReceiver.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateReceiverRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateReceiverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReceiver", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReceiverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReceiverDetail(self, request):
        """This API is used to add recipient email addresses (up to 20,000 at a time) to a recipient group. This will be processed asynchronously. If the data volume is large, it may take some time to upload. You can check the recipient group for the upload status and upload quantity. This API has basically the same feature as that of `CreateReceiverDetailWithData` except that it doesn't support uploading template parameters for email sending. You need to first call the `CreateReceiver` API to create a recipient group, then call this API to pass in recipient addresses, and finally call the `BatchSendEmail` API to batch send emails. This API supports adding more recipient addresses during upload but not address deduplication, so you need to make sure that the recipient addresses are not duplicate by yourself. This API can request up to 20,000 recipient addresses at a time, but the recipient group can contain up to 50,000 addresses currently.

        :param request: Request instance for CreateReceiverDetail.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateReceiverDetailRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateReceiverDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReceiverDetail", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReceiverDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAddressUnsubscribeConfig(self, request):
        """Remove address-level unsubscribe configuration.

        :param request: Request instance for DeleteAddressUnsubscribeConfig.
        :type request: :class:`tencentcloud.ses.v20201002.models.DeleteAddressUnsubscribeConfigRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.DeleteAddressUnsubscribeConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAddressUnsubscribeConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAddressUnsubscribeConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBlackList(self, request):
        """This API is used to unblocklist email addresses. If you confirm that a blocklisted recipient address is valid and active, you can remove it from Tencent Cloud’s address blocklist database.

        :param request: Request instance for DeleteBlackList.
        :type request: :class:`tencentcloud.ses.v20201002.models.DeleteBlackListRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.DeleteBlackListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBlackList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBlackListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEmailAddress(self, request):
        """This API is used to delete a sender address.

        :param request: Request instance for DeleteEmailAddress.
        :type request: :class:`tencentcloud.ses.v20201002.models.DeleteEmailAddressRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.DeleteEmailAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEmailAddress", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEmailAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEmailIdentity(self, request):
        """This API is used to delete a sender domain. After deleted, the sender domain can no longer be used to send emails.

        :param request: Request instance for DeleteEmailIdentity.
        :type request: :class:`tencentcloud.ses.v20201002.models.DeleteEmailIdentityRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.DeleteEmailIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEmailIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEmailIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEmailTemplate(self, request):
        """This API is used to delete an email template.

        :param request: Request instance for DeleteEmailTemplate.
        :type request: :class:`tencentcloud.ses.v20201002.models.DeleteEmailTemplateRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.DeleteEmailTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEmailTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEmailTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReceiver(self, request):
        """This API is used to delete a recipient group and all recipient email addresses in the group based on the recipient group ID.

        :param request: Request instance for DeleteReceiver.
        :type request: :class:`tencentcloud.ses.v20201002.models.DeleteReceiverRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.DeleteReceiverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReceiver", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReceiverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetEmailIdentity(self, request):
        """This API is used to get the configuration details of a sender domain.

        :param request: Request instance for GetEmailIdentity.
        :type request: :class:`tencentcloud.ses.v20201002.models.GetEmailIdentityRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.GetEmailIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetEmailIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.GetEmailIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetEmailTemplate(self, request):
        """This API is used to get the details of a template.

        :param request: Request instance for GetEmailTemplate.
        :type request: :class:`tencentcloud.ses.v20201002.models.GetEmailTemplateRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.GetEmailTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetEmailTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.GetEmailTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetSendEmailStatus(self, request):
        """This API is used to get email sending status. Only data within 30 days can be queried.
        Default API request rate limit: 1 request/sec.

        :param request: Request instance for GetSendEmailStatus.
        :type request: :class:`tencentcloud.ses.v20201002.models.GetSendEmailStatusRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.GetSendEmailStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetSendEmailStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetSendEmailStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetStatisticsReport(self, request):
        """This API is used to get the email sending statistics over a recent period, including data on sent emails, delivery success rate, open rate, bounce rate, and so on.

        :param request: Request instance for GetStatisticsReport.
        :type request: :class:`tencentcloud.ses.v20201002.models.GetStatisticsReportRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.GetStatisticsReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetStatisticsReport", params, headers=headers)
            response = json.loads(body)
            model = models.GetStatisticsReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAddressUnsubscribeConfig(self, request):
        """This API is used to get the address and unsubscribe configuration list.

        :param request: Request instance for ListAddressUnsubscribeConfig.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListAddressUnsubscribeConfigRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListAddressUnsubscribeConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAddressUnsubscribeConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ListAddressUnsubscribeConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListBlackEmailAddress(self, request):
        """The API is used to get blocklisted addresses. In the case of a hard bounce, Tencent Cloud will blocklist the recipient address and do not allow any user to send emails to this address. If you confirm that this is a misjudgment, you can remove it from the blocklist.

        :param request: Request instance for ListBlackEmailAddress.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListBlackEmailAddressRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListBlackEmailAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListBlackEmailAddress", params, headers=headers)
            response = json.loads(body)
            model = models.ListBlackEmailAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListEmailAddress(self, request):
        """This API is used to get the list of sender addresses.

        :param request: Request instance for ListEmailAddress.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListEmailAddressRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListEmailAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListEmailAddress", params, headers=headers)
            response = json.loads(body)
            model = models.ListEmailAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListEmailIdentities(self, request):
        """This API is used to get the list of sender domains, including verified and unverified domains.

        :param request: Request instance for ListEmailIdentities.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListEmailIdentitiesRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListEmailIdentitiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListEmailIdentities", params, headers=headers)
            response = json.loads(body)
            model = models.ListEmailIdentitiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListEmailTemplates(self, request):
        """This API is used to get the list of email templates.

        :param request: Request instance for ListEmailTemplates.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListEmailTemplatesRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListEmailTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListEmailTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.ListEmailTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListReceivers(self, request):
        """This API is used to query recipient groups. It supports pagination, fuzzy query, and query by status.

        :param request: Request instance for ListReceivers.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListReceiversRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListReceiversResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListReceivers", params, headers=headers)
            response = json.loads(body)
            model = models.ListReceiversResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListSendTasks(self, request):
        """This API is used to query batch email sending tasks (including immediate, scheduled, and recurring tasks) by page. You can query task data including the number of emails requested to be sent, the number of sent emails, the number of cached emails, and task status.

        :param request: Request instance for ListSendTasks.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListSendTasksRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListSendTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListSendTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListSendTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendEmail(self, request):
        """This API is used to send an HTML or TEXT email triggered for authentication or transaction. By default, you can send emails using a template only.

        :param request: Request instance for SendEmail.
        :type request: :class:`tencentcloud.ses.v20201002.models.SendEmailRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.SendEmailResponse`

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAddressUnsubscribeConfig(self, request):
        """This API is used to update address-level unsubscribe configurations.

        :param request: Request instance for UpdateAddressUnsubscribeConfig.
        :type request: :class:`tencentcloud.ses.v20201002.models.UpdateAddressUnsubscribeConfigRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.UpdateAddressUnsubscribeConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAddressUnsubscribeConfig", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAddressUnsubscribeConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateEmailIdentity(self, request):
        """This API is used to verify whether your DNS configuration is correct.

        :param request: Request instance for UpdateEmailIdentity.
        :type request: :class:`tencentcloud.ses.v20201002.models.UpdateEmailIdentityRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.UpdateEmailIdentityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateEmailIdentity", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateEmailIdentityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateEmailSmtpPassWord(self, request):
        """This API is used to set the SMTP password. Initially, no SMTP password is set for your email address, so emails cannot be sent over SMTP. To send emails over SMTP, you must set the SMTP password. The set password can be changed subsequently.

        :param request: Request instance for UpdateEmailSmtpPassWord.
        :type request: :class:`tencentcloud.ses.v20201002.models.UpdateEmailSmtpPassWordRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.UpdateEmailSmtpPassWordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateEmailSmtpPassWord", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateEmailSmtpPassWordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateEmailTemplate(self, request):
        """This API is used to update an email template. An updated template must be approved again before it can be used.

        :param request: Request instance for UpdateEmailTemplate.
        :type request: :class:`tencentcloud.ses.v20201002.models.UpdateEmailTemplateRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.UpdateEmailTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateEmailTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateEmailTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))