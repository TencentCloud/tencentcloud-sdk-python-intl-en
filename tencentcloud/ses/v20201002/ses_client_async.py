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
from tencentcloud.ses.v20201002 import models
from typing import Dict


class SesClient(AbstractClient):
    _apiVersion = '2020-10-02'
    _endpoint = 'ses.intl.tencentcloudapi.com'
    _service = 'ses'

    async def BatchSendEmail(
            self,
            request: models.BatchSendEmailRequest,
            opts: Dict = None,
    ) -> models.BatchSendEmailResponse:
        """
        This API is used to send a TEXT or HTML email to multiple recipients at a time for marketing or notification purposes. By default, you can send emails using a template only. You need to create a recipient group with email addresses first and then send emails by group ID. SES supports scheduled and recurring email sending tasks. You need to pass in `TimedParam` for a scheduled task and `CycleParam` for a recurring one.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchSendEmail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchSendEmailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAddressUnsubscribeConfig(
            self,
            request: models.CreateAddressUnsubscribeConfigRequest,
            opts: Dict = None,
    ) -> models.CreateAddressUnsubscribeConfigResponse:
        """
        This API is used to create an address-level unsubscribe configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAddressUnsubscribeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAddressUnsubscribeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEmailAddress(
            self,
            request: models.CreateEmailAddressRequest,
            opts: Dict = None,
    ) -> models.CreateEmailAddressResponse:
        """
        After the sender domain is verified, you need a sender address to send emails. For example, if your sender domain is mail.qcloud.com, your sender address can be service@mail.qcloud.com. If you want to display your name (such as "Tencent Cloud") in the inbox list of the recipients, the sender address should be in the format of `Tencent Cloud <email address>`. Please note that there must be a space between your name and the first angle bracket.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEmailAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEmailAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEmailIdentity(
            self,
            request: models.CreateEmailIdentityRequest,
            opts: Dict = None,
    ) -> models.CreateEmailIdentityResponse:
        """
        This API is used to create a sender domain. Before you can send an email using Tencent Cloud SES, you must create a sender domain as your identity. It can be the domain of your website or mobile app. You must verify the domain to prove that you own it and authorize Tencent Cloud SES to use it to send emails.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEmailIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEmailIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEmailTemplate(
            self,
            request: models.CreateEmailTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateEmailTemplateResponse:
        """
        This API is used to create a TEXT or HTML email template. To create an HTML template, ensure that it does not include external CSS files. You can use {{variable name}} to specify a variable in the template.
        Note: Only an approved template can be used to send emails.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEmailTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEmailTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReceiver(
            self,
            request: models.CreateReceiverRequest,
            opts: Dict = None,
    ) -> models.CreateReceiverResponse:
        """
        This API is used to create a recipient group, which is the list of target email addresses for batch sending emails. After creating a group, you need to upload recipient email addresses. Then, you can create a sending task and select the group to batch send emails.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReceiver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReceiverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReceiverDetail(
            self,
            request: models.CreateReceiverDetailRequest,
            opts: Dict = None,
    ) -> models.CreateReceiverDetailResponse:
        """
        This API is used to add recipient email addresses (up to 20,000 at a time) to a recipient group. This will be processed asynchronously. If the data volume is large, it may take some time to upload. You can check the recipient group for the upload status and upload quantity. This API has basically the same feature as that of `CreateReceiverDetailWithData` except that it doesn't support uploading template parameters for email sending. You need to first call the `CreateReceiver` API to create a recipient group, then call this API to pass in recipient addresses, and finally call the `BatchSendEmail` API to batch send emails. This API supports adding more recipient addresses during upload but not address deduplication, so you need to make sure that the recipient addresses are not duplicate by yourself. This API can request up to 20,000 recipient addresses at a time, but the recipient group can contain up to 50,000 addresses currently.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReceiverDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReceiverDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAddressUnsubscribeConfig(
            self,
            request: models.DeleteAddressUnsubscribeConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteAddressUnsubscribeConfigResponse:
        """
        Remove address-level unsubscribe configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAddressUnsubscribeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAddressUnsubscribeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBlackList(
            self,
            request: models.DeleteBlackListRequest,
            opts: Dict = None,
    ) -> models.DeleteBlackListResponse:
        """
        This API is used to unblocklist email addresses. If you confirm that a blocklisted recipient address is valid and active, you can remove it from Tencent Cloud’s address blocklist database.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBlackList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBlackListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEmailAddress(
            self,
            request: models.DeleteEmailAddressRequest,
            opts: Dict = None,
    ) -> models.DeleteEmailAddressResponse:
        """
        This API is used to delete a sender address.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEmailAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEmailAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEmailIdentity(
            self,
            request: models.DeleteEmailIdentityRequest,
            opts: Dict = None,
    ) -> models.DeleteEmailIdentityResponse:
        """
        This API is used to delete a sender domain. After deleted, the sender domain can no longer be used to send emails.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEmailIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEmailIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEmailTemplate(
            self,
            request: models.DeleteEmailTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteEmailTemplateResponse:
        """
        This API is used to delete an email template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEmailTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEmailTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReceiver(
            self,
            request: models.DeleteReceiverRequest,
            opts: Dict = None,
    ) -> models.DeleteReceiverResponse:
        """
        This API is used to delete a recipient group and all recipient email addresses in the group based on the recipient group ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReceiver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReceiverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetEmailIdentity(
            self,
            request: models.GetEmailIdentityRequest,
            opts: Dict = None,
    ) -> models.GetEmailIdentityResponse:
        """
        This API is used to get the configuration details of a sender domain.
        """
        
        kwargs = {}
        kwargs["action"] = "GetEmailIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetEmailIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetEmailTemplate(
            self,
            request: models.GetEmailTemplateRequest,
            opts: Dict = None,
    ) -> models.GetEmailTemplateResponse:
        """
        This API is used to get the details of a template.
        """
        
        kwargs = {}
        kwargs["action"] = "GetEmailTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetEmailTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSendEmailStatus(
            self,
            request: models.GetSendEmailStatusRequest,
            opts: Dict = None,
    ) -> models.GetSendEmailStatusResponse:
        """
        This API is used to get email sending status. Only data within 30 days can be queried.
        Default API request rate limit: 1 request/sec.
        """
        
        kwargs = {}
        kwargs["action"] = "GetSendEmailStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSendEmailStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetStatisticsReport(
            self,
            request: models.GetStatisticsReportRequest,
            opts: Dict = None,
    ) -> models.GetStatisticsReportResponse:
        """
        This API is used to get the email sending statistics over a recent period, including data on sent emails, delivery success rate, open rate, bounce rate, and so on.
        """
        
        kwargs = {}
        kwargs["action"] = "GetStatisticsReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetStatisticsReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAddressUnsubscribeConfig(
            self,
            request: models.ListAddressUnsubscribeConfigRequest,
            opts: Dict = None,
    ) -> models.ListAddressUnsubscribeConfigResponse:
        """
        This API is used to get the address and unsubscribe configuration list.
        """
        
        kwargs = {}
        kwargs["action"] = "ListAddressUnsubscribeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAddressUnsubscribeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListBlackEmailAddress(
            self,
            request: models.ListBlackEmailAddressRequest,
            opts: Dict = None,
    ) -> models.ListBlackEmailAddressResponse:
        """
        The API is used to get blocklisted addresses. In the case of a hard bounce, Tencent Cloud will blocklist the recipient address and do not allow any user to send emails to this address. If you confirm that this is a misjudgment, you can remove it from the blocklist.
        """
        
        kwargs = {}
        kwargs["action"] = "ListBlackEmailAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListBlackEmailAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListEmailAddress(
            self,
            request: models.ListEmailAddressRequest,
            opts: Dict = None,
    ) -> models.ListEmailAddressResponse:
        """
        This API is used to get the list of sender addresses.
        """
        
        kwargs = {}
        kwargs["action"] = "ListEmailAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListEmailAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListEmailIdentities(
            self,
            request: models.ListEmailIdentitiesRequest,
            opts: Dict = None,
    ) -> models.ListEmailIdentitiesResponse:
        """
        This API is used to get the list of sender domains, including verified and unverified domains.
        """
        
        kwargs = {}
        kwargs["action"] = "ListEmailIdentities"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListEmailIdentitiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListEmailTemplates(
            self,
            request: models.ListEmailTemplatesRequest,
            opts: Dict = None,
    ) -> models.ListEmailTemplatesResponse:
        """
        This API is used to get the list of email templates.
        """
        
        kwargs = {}
        kwargs["action"] = "ListEmailTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListEmailTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListReceivers(
            self,
            request: models.ListReceiversRequest,
            opts: Dict = None,
    ) -> models.ListReceiversResponse:
        """
        This API is used to query recipient groups. It supports pagination, fuzzy query, and query by status.
        """
        
        kwargs = {}
        kwargs["action"] = "ListReceivers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListReceiversResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSendTasks(
            self,
            request: models.ListSendTasksRequest,
            opts: Dict = None,
    ) -> models.ListSendTasksResponse:
        """
        This API is used to query batch email sending tasks (including immediate, scheduled, and recurring tasks) by page. You can query task data including the number of emails requested to be sent, the number of sent emails, the number of cached emails, and task status.
        """
        
        kwargs = {}
        kwargs["action"] = "ListSendTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSendTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendEmail(
            self,
            request: models.SendEmailRequest,
            opts: Dict = None,
    ) -> models.SendEmailResponse:
        """
        This API is used to send an HTML or TEXT email triggered for authentication or transaction. By default, you can send emails using a template only.
        """
        
        kwargs = {}
        kwargs["action"] = "SendEmail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendEmailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAddressUnsubscribeConfig(
            self,
            request: models.UpdateAddressUnsubscribeConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateAddressUnsubscribeConfigResponse:
        """
        This API is used to update address-level unsubscribe configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAddressUnsubscribeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAddressUnsubscribeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateEmailIdentity(
            self,
            request: models.UpdateEmailIdentityRequest,
            opts: Dict = None,
    ) -> models.UpdateEmailIdentityResponse:
        """
        This API is used to verify whether your DNS configuration is correct.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateEmailIdentity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateEmailIdentityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateEmailSmtpPassWord(
            self,
            request: models.UpdateEmailSmtpPassWordRequest,
            opts: Dict = None,
    ) -> models.UpdateEmailSmtpPassWordResponse:
        """
        This API is used to set the SMTP password. Initially, no SMTP password is set for your email address, so emails cannot be sent over SMTP. To send emails over SMTP, you must set the SMTP password. The set password can be changed subsequently.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateEmailSmtpPassWord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateEmailSmtpPassWordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateEmailTemplate(
            self,
            request: models.UpdateEmailTemplateRequest,
            opts: Dict = None,
    ) -> models.UpdateEmailTemplateResponse:
        """
        This API is used to update an email template. An updated template must be approved again before it can be used.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateEmailTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateEmailTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)