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


    def CreateReceiver(self, request):
        """This API is used to create a recipient group, which is the list of target email addresses for batch sending emails. After creating a group, you need to upload recipient email addresses. Then, you can create a sending task and select the group to batch send emails.

        :param request: Request instance for CreateReceiver.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateReceiverRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateReceiverResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateReceiver", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateReceiverResponse()
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


    def CreateReceiverDetail(self, request):
        """This API is used to add recipient email addresses (up to 100,000 at a time) to a recipient group. This will be processed asynchronously. You can upload recipient email addresses only once. If the data volume is large, it may take some time to upload. You can check the recipient group to learn the upload status and upload quantity.

        :param request: Request instance for CreateReceiverDetail.
        :type request: :class:`tencentcloud.ses.v20201002.models.CreateReceiverDetailRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.CreateReceiverDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateReceiverDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateReceiverDetailResponse()
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


    def DeleteReceiver(self, request):
        """This API is used to delete a recipient group and all recipient email addresses in the group based on the recipient group ID.

        :param request: Request instance for DeleteReceiver.
        :type request: :class:`tencentcloud.ses.v20201002.models.DeleteReceiverRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.DeleteReceiverResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteReceiver", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteReceiverResponse()
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
        """This API is used to get the email sending statistics over a recent period, including data on sent emails, delivery success rate, open rate, bounce rate, and so on.

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


    def ListReceivers(self, request):
        """This API is used to query recipient groups. It supports pagination, fuzzy query, and query by status.

        :param request: Request instance for ListReceivers.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListReceiversRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListReceiversResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListReceivers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListReceiversResponse()
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


    def ListSendTasks(self, request):
        """This API is used to query batch email sending tasks (including immediate, scheduled, and recurring tasks) by page. You can query task data including the number of emails requested to be sent, the number of sent emails, the number of cached emails, and task status.

        :param request: Request instance for ListSendTasks.
        :type request: :class:`tencentcloud.ses.v20201002.models.ListSendTasksRequest`
        :rtype: :class:`tencentcloud.ses.v20201002.models.ListSendTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListSendTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListSendTasksResponse()
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
        """This API is used to send a TEXT or HTML email triggered for authentication or transaction. By default, you can send emails using a template only. To send custom content, please contact your sales rep to enable this feature.

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