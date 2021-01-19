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

from tencentcloud.common.abstract_model import AbstractModel


class Attachment(AbstractModel):
    """

    """

    def __init__(self):
        """
        :param FileName: 
        :type FileName: str
        :param Content: 
        :type Content: str
        """
        self.FileName = None
        self.Content = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.Content = params.get("Content")


class BlackEmailAddress(AbstractModel):
    """Email address blocklist structure, including the blocklisted address and the time when it is blocklisted.

    """

    def __init__(self):
        """
        :param BounceTime: Time when the email address is blocklisted.
        :type BounceTime: str
        :param EmailAddress: Blocklisted email address.
        :type EmailAddress: str
        """
        self.BounceTime = None
        self.EmailAddress = None


    def _deserialize(self, params):
        self.BounceTime = params.get("BounceTime")
        self.EmailAddress = params.get("EmailAddress")


class CreateEmailAddressRequest(AbstractModel):
    """CreateEmailAddress request structure.

    """

    def __init__(self):
        """
        :param EmailAddress: Your sender address. You can create up to 10 sender addresses for each domain.
        :type EmailAddress: str
        :param EmailSenderName: Sender name.
        :type EmailSenderName: str
        """
        self.EmailAddress = None
        self.EmailSenderName = None


    def _deserialize(self, params):
        self.EmailAddress = params.get("EmailAddress")
        self.EmailSenderName = params.get("EmailSenderName")


class CreateEmailAddressResponse(AbstractModel):
    """CreateEmailAddress response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateEmailIdentityRequest(AbstractModel):
    """CreateEmailIdentity request structure.

    """

    def __init__(self):
        """
        :param EmailIdentity: Your sender domain. You are advised to use a third-level domain, for example, mail.qcloud.com.
        :type EmailIdentity: str
        """
        self.EmailIdentity = None


    def _deserialize(self, params):
        self.EmailIdentity = params.get("EmailIdentity")


class CreateEmailIdentityResponse(AbstractModel):
    """CreateEmailIdentity response structure.

    """

    def __init__(self):
        """
        :param IdentityType: Verification type. The value is fixed to `DOMAIN`.
        :type IdentityType: str
        :param VerifiedForSendingStatus: Verification passed or not.
        :type VerifiedForSendingStatus: bool
        :param Attributes: DNS information that needs to be configured.
        :type Attributes: list of DNSAttributes
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IdentityType = None
        self.VerifiedForSendingStatus = None
        self.Attributes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IdentityType = params.get("IdentityType")
        self.VerifiedForSendingStatus = params.get("VerifiedForSendingStatus")
        if params.get("Attributes") is not None:
            self.Attributes = []
            for item in params.get("Attributes"):
                obj = DNSAttributes()
                obj._deserialize(item)
                self.Attributes.append(obj)
        self.RequestId = params.get("RequestId")


class CreateEmailTemplateRequest(AbstractModel):
    """CreateEmailTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateName: Template name.
        :type TemplateName: str
        :param TemplateContent: Template content.
        :type TemplateContent: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        """
        self.TemplateName = None
        self.TemplateContent = None


    def _deserialize(self, params):
        self.TemplateName = params.get("TemplateName")
        if params.get("TemplateContent") is not None:
            self.TemplateContent = TemplateContent()
            self.TemplateContent._deserialize(params.get("TemplateContent"))


class CreateEmailTemplateResponse(AbstractModel):
    """CreateEmailTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DNSAttributes(AbstractModel):
    """Describes the domain name, record type, expected value, and currently configured value of DNS records.

    """

    def __init__(self):
        """
        :param Type: Record types: CNAME, A, TXT, and MX.
        :type Type: str
        :param SendDomain: Domain name.
        :type SendDomain: str
        :param ExpectedValue: Expected value.
        :type ExpectedValue: str
        :param CurrentValue: Currently configured value.
        :type CurrentValue: str
        :param Status: Approved or not. The default value is `false`.
        :type Status: bool
        """
        self.Type = None
        self.SendDomain = None
        self.ExpectedValue = None
        self.CurrentValue = None
        self.Status = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.SendDomain = params.get("SendDomain")
        self.ExpectedValue = params.get("ExpectedValue")
        self.CurrentValue = params.get("CurrentValue")
        self.Status = params.get("Status")


class DeleteBlackListRequest(AbstractModel):
    """DeleteBlackList request structure.

    """

    def __init__(self):
        """
        :param EmailAddressList: List of email addresses to be unblocklisted. Enter at least one address.
        :type EmailAddressList: list of str
        """
        self.EmailAddressList = None


    def _deserialize(self, params):
        self.EmailAddressList = params.get("EmailAddressList")


class DeleteBlackListResponse(AbstractModel):
    """DeleteBlackList response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEmailAddressRequest(AbstractModel):
    """DeleteEmailAddress request structure.

    """

    def __init__(self):
        """
        :param EmailAddress: Sender address.
        :type EmailAddress: str
        """
        self.EmailAddress = None


    def _deserialize(self, params):
        self.EmailAddress = params.get("EmailAddress")


class DeleteEmailAddressResponse(AbstractModel):
    """DeleteEmailAddress response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEmailIdentityRequest(AbstractModel):
    """DeleteEmailIdentity request structure.

    """

    def __init__(self):
        """
        :param EmailIdentity: Sender domain.
        :type EmailIdentity: str
        """
        self.EmailIdentity = None


    def _deserialize(self, params):
        self.EmailIdentity = params.get("EmailIdentity")


class DeleteEmailIdentityResponse(AbstractModel):
    """DeleteEmailIdentity response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEmailTemplateRequest(AbstractModel):
    """DeleteEmailTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateID: Email template to be deleted.
        :type TemplateID: int
        """
        self.TemplateID = None


    def _deserialize(self, params):
        self.TemplateID = params.get("TemplateID")


class DeleteEmailTemplateResponse(AbstractModel):
    """DeleteEmailTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EmailIdentity(AbstractModel):
    """Sender domain verification list structure

    """

    def __init__(self):
        """
        :param IdentityName: Sender domain.
        :type IdentityName: str
        :param IdentityType: Verification type. The value is fixed to `DOMAIN`.
        :type IdentityType: str
        :param SendingEnabled: Verification passed or not.
        :type SendingEnabled: bool
        """
        self.IdentityName = None
        self.IdentityType = None
        self.SendingEnabled = None


    def _deserialize(self, params):
        self.IdentityName = params.get("IdentityName")
        self.IdentityType = params.get("IdentityType")
        self.SendingEnabled = params.get("SendingEnabled")


class EmailSender(AbstractModel):
    """Describes sender information.

    """

    def __init__(self):
        """
        :param EmailAddress: Sender address.
        :type EmailAddress: str
        :param EmailSenderName: Sender name.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type EmailSenderName: str
        :param CreatedTimestamp: Creation time.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CreatedTimestamp: int
        """
        self.EmailAddress = None
        self.EmailSenderName = None
        self.CreatedTimestamp = None


    def _deserialize(self, params):
        self.EmailAddress = params.get("EmailAddress")
        self.EmailSenderName = params.get("EmailSenderName")
        self.CreatedTimestamp = params.get("CreatedTimestamp")


class GetEmailIdentityRequest(AbstractModel):
    """GetEmailIdentity request structure.

    """

    def __init__(self):
        """
        :param EmailIdentity: Sender domain.
        :type EmailIdentity: str
        """
        self.EmailIdentity = None


    def _deserialize(self, params):
        self.EmailIdentity = params.get("EmailIdentity")


class GetEmailIdentityResponse(AbstractModel):
    """GetEmailIdentity response structure.

    """

    def __init__(self):
        """
        :param IdentityType: Verification type. The value is fixed to `DOMAIN`.
        :type IdentityType: str
        :param VerifiedForSendingStatus: Verification passed or not.
        :type VerifiedForSendingStatus: bool
        :param Attributes: DNS configuration details.
        :type Attributes: list of DNSAttributes
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IdentityType = None
        self.VerifiedForSendingStatus = None
        self.Attributes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IdentityType = params.get("IdentityType")
        self.VerifiedForSendingStatus = params.get("VerifiedForSendingStatus")
        if params.get("Attributes") is not None:
            self.Attributes = []
            for item in params.get("Attributes"):
                obj = DNSAttributes()
                obj._deserialize(item)
                self.Attributes.append(obj)
        self.RequestId = params.get("RequestId")


class GetEmailTemplateRequest(AbstractModel):
    """GetEmailTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateID: Template ID.
        :type TemplateID: int
        """
        self.TemplateID = None


    def _deserialize(self, params):
        self.TemplateID = params.get("TemplateID")


class GetEmailTemplateResponse(AbstractModel):
    """GetEmailTemplate response structure.

    """

    def __init__(self):
        """
        :param TemplateContent: Template content.
        :type TemplateContent: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TemplateContent = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TemplateContent") is not None:
            self.TemplateContent = TemplateContent()
            self.TemplateContent._deserialize(params.get("TemplateContent"))
        self.RequestId = params.get("RequestId")


class GetStatisticsReportRequest(AbstractModel):
    """GetStatisticsReport request structure.

    """

    def __init__(self):
        """
        :param StartDate: Start date.
        :type StartDate: str
        :param EndDate: End date.
        :type EndDate: str
        :param Domain: Sender domain.
        :type Domain: str
        :param ReceivingMailboxType: Recipient address type, for example, gmail.com.
        :type ReceivingMailboxType: str
        """
        self.StartDate = None
        self.EndDate = None
        self.Domain = None
        self.ReceivingMailboxType = None


    def _deserialize(self, params):
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Domain = params.get("Domain")
        self.ReceivingMailboxType = params.get("ReceivingMailboxType")


class GetStatisticsReportResponse(AbstractModel):
    """GetStatisticsReport response structure.

    """

    def __init__(self):
        """
        :param DailyVolumes: Daily email sending statistics.
        :type DailyVolumes: list of Volume
        :param OverallVolume: Overall email sending statistics.
        :type OverallVolume: :class:`tencentcloud.ses.v20201002.models.Volume`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.DailyVolumes = None
        self.OverallVolume = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DailyVolumes") is not None:
            self.DailyVolumes = []
            for item in params.get("DailyVolumes"):
                obj = Volume()
                obj._deserialize(item)
                self.DailyVolumes.append(obj)
        if params.get("OverallVolume") is not None:
            self.OverallVolume = Volume()
            self.OverallVolume._deserialize(params.get("OverallVolume"))
        self.RequestId = params.get("RequestId")


class ListBlackEmailAddressRequest(AbstractModel):
    """ListBlackEmailAddress request structure.

    """

    def __init__(self):
        """
        :param StartDate: Start date.
        :type StartDate: str
        :param EndDate: End date.
        :type EndDate: str
        :param Limit: Common parameter. It must be used with `Offset`.
        :type Limit: int
        :param Offset: Common parameter. It must be used with `Limit`.
        :type Offset: int
        :param EmailAddress: You can specify an email address to query.
        :type EmailAddress: str
        :param TaskID: You can specify a task ID to query.
        :type TaskID: str
        """
        self.StartDate = None
        self.EndDate = None
        self.Limit = None
        self.Offset = None
        self.EmailAddress = None
        self.TaskID = None


    def _deserialize(self, params):
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.EmailAddress = params.get("EmailAddress")
        self.TaskID = params.get("TaskID")


class ListBlackEmailAddressResponse(AbstractModel):
    """ListBlackEmailAddress response structure.

    """

    def __init__(self):
        """
        :param BlackList: List of blocklisted addresses.
        :type BlackList: list of BlackEmailAddress
        :param TotalCount: Total number of blocklisted addresses.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.BlackList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BlackList") is not None:
            self.BlackList = []
            for item in params.get("BlackList"):
                obj = BlackEmailAddress()
                obj._deserialize(item)
                self.BlackList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListEmailAddressRequest(AbstractModel):
    """ListEmailAddress request structure.

    """


class ListEmailAddressResponse(AbstractModel):
    """ListEmailAddress response structure.

    """

    def __init__(self):
        """
        :param EmailSenders: Details of sender addresses.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type EmailSenders: list of EmailSender
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EmailSenders = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EmailSenders") is not None:
            self.EmailSenders = []
            for item in params.get("EmailSenders"):
                obj = EmailSender()
                obj._deserialize(item)
                self.EmailSenders.append(obj)
        self.RequestId = params.get("RequestId")


class ListEmailIdentitiesRequest(AbstractModel):
    """ListEmailIdentities request structure.

    """


class ListEmailIdentitiesResponse(AbstractModel):
    """ListEmailIdentities response structure.

    """

    def __init__(self):
        """
        :param EmailIdentities: List of sender domains.
        :type EmailIdentities: list of EmailIdentity
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EmailIdentities = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EmailIdentities") is not None:
            self.EmailIdentities = []
            for item in params.get("EmailIdentities"):
                obj = EmailIdentity()
                obj._deserialize(item)
                self.EmailIdentities.append(obj)
        self.RequestId = params.get("RequestId")


class ListEmailTemplatesRequest(AbstractModel):
    """ListEmailTemplates request structure.

    """

    def __init__(self):
        """
        :param Limit: Number of templates to get. This parameter is used for pagination.
        :type Limit: int
        :param Offset: Template offset to get. This parameter is used for pagination.
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class ListEmailTemplatesResponse(AbstractModel):
    """ListEmailTemplates response structure.

    """

    def __init__(self):
        """
        :param TemplatesMetadata: List of email templates.
        :type TemplatesMetadata: list of TemplatesMetadata
        :param TotalCount: Total number of templates.
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TemplatesMetadata = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TemplatesMetadata") is not None:
            self.TemplatesMetadata = []
            for item in params.get("TemplatesMetadata"):
                obj = TemplatesMetadata()
                obj._deserialize(item)
                self.TemplatesMetadata.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class SendEmailRequest(AbstractModel):
    """SendEmail request structure.

    """

    def __init__(self):
        """
        :param FromEmailAddress: Sender address. Enter a sender address, for example, noreply@mail.qcloud.com. To display the sender name, enter the address in the following format:  
sender &lt;email address&gt;. For example: 
Tencent Cloud team &lt;noreply@mail.qcloud.com&gt;
        :type FromEmailAddress: str
        :param Destination: Recipient address.
        :type Destination: list of str
        :param Subject: Email subject.
        :type Subject: str
        :param ReplyToAddresses: Reply-to address. You can enter a valid personal email address that can receive emails. If this field is left empty, reply emails will be sent to Tencent Cloud. Note: the email content will display all recipient addresses. To send one-to-one emails to several recipients, please call the API multiple times to send the emails.
        :type ReplyToAddresses: str
        :param Template: Template when sending emails using a template.
        :type Template: :class:`tencentcloud.ses.v20201002.models.Template`
        :param Simple: Email content when sending emails by calling the API.
        :type Simple: :class:`tencentcloud.ses.v20201002.models.Simple`
        :param Attachments: 
        :type Attachments: list of Attachment
        """
        self.FromEmailAddress = None
        self.Destination = None
        self.Subject = None
        self.ReplyToAddresses = None
        self.Template = None
        self.Simple = None
        self.Attachments = None


    def _deserialize(self, params):
        self.FromEmailAddress = params.get("FromEmailAddress")
        self.Destination = params.get("Destination")
        self.Subject = params.get("Subject")
        self.ReplyToAddresses = params.get("ReplyToAddresses")
        if params.get("Template") is not None:
            self.Template = Template()
            self.Template._deserialize(params.get("Template"))
        if params.get("Simple") is not None:
            self.Simple = Simple()
            self.Simple._deserialize(params.get("Simple"))
        if params.get("Attachments") is not None:
            self.Attachments = []
            for item in params.get("Attachments"):
                obj = Attachment()
                obj._deserialize(item)
                self.Attachments.append(obj)


class SendEmailResponse(AbstractModel):
    """SendEmail response structure.

    """

    def __init__(self):
        """
        :param MessageId: Unique ID generated when receiving the message.
        :type MessageId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MessageId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MessageId = params.get("MessageId")
        self.RequestId = params.get("RequestId")


class Simple(AbstractModel):
    """Email content, which can be plain text (TEXT), pure code (HTML), or a combination of TEXT and HTML (recommended).

    """

    def __init__(self):
        """
        :param Html: HTML code after base64 encoding. To ensure correct display, this parameter should include all code information and cannot contain external CSS.
        :type Html: str
        :param Text: Plain text content after base64 encoding. If HTML is not involved, the plain text will be displayed in the email. Otherwise, this parameter represents the plain text style of the email.
        :type Text: str
        """
        self.Html = None
        self.Text = None


    def _deserialize(self, params):
        self.Html = params.get("Html")
        self.Text = params.get("Text")


class Template(AbstractModel):
    """Template information, including template ID, template variable parameters, etc.

    """

    def __init__(self):
        """
        :param TemplateID: Template ID. If you don’t have any template, please create one.
        :type TemplateID: int
        :param TemplateData: Variable parameters in the template. Please use `json.dump` to format the JSON object into a string type. The object is a set of key-value pairs. Each key denotes a variable, which is represented by {{key}}. The key will be replaced with the corresponding value (represented by {{value}}) when sending the email.
        :type TemplateData: str
        """
        self.TemplateID = None
        self.TemplateData = None


    def _deserialize(self, params):
        self.TemplateID = params.get("TemplateID")
        self.TemplateData = params.get("TemplateData")


class TemplateContent(AbstractModel):
    """Template content, which must include at least one of TEXT and HTML. A combination of TEXT and HTML is recommended.

    """

    def __init__(self):
        """
        :param Html: HTML code after base64 encoding.
        :type Html: str
        :param Text: Text content after base64 encoding.
        :type Text: str
        """
        self.Html = None
        self.Text = None


    def _deserialize(self, params):
        self.Html = params.get("Html")
        self.Text = params.get("Text")


class TemplatesMetadata(AbstractModel):
    """Template list structure.

    """

    def __init__(self):
        """
        :param CreatedTimestamp: Creation time.
        :type CreatedTimestamp: int
        :param TemplateName: Template name.
        :type TemplateName: str
        :param TemplateStatus: Template status. 1: under review; 0: approved; 2: rejected; other values: unavailable.
        :type TemplateStatus: int
        :param TemplateID: Template ID.
        :type TemplateID: int
        :param ReviewReason: Review reply
        :type ReviewReason: str
        """
        self.CreatedTimestamp = None
        self.TemplateName = None
        self.TemplateStatus = None
        self.TemplateID = None
        self.ReviewReason = None


    def _deserialize(self, params):
        self.CreatedTimestamp = params.get("CreatedTimestamp")
        self.TemplateName = params.get("TemplateName")
        self.TemplateStatus = params.get("TemplateStatus")
        self.TemplateID = params.get("TemplateID")
        self.ReviewReason = params.get("ReviewReason")


class UpdateEmailIdentityRequest(AbstractModel):
    """UpdateEmailIdentity request structure.

    """

    def __init__(self):
        """
        :param EmailIdentity: Domain to be verified.
        :type EmailIdentity: str
        """
        self.EmailIdentity = None


    def _deserialize(self, params):
        self.EmailIdentity = params.get("EmailIdentity")


class UpdateEmailIdentityResponse(AbstractModel):
    """UpdateEmailIdentity response structure.

    """

    def __init__(self):
        """
        :param IdentityType: Verification type. The value is fixed to `DOMAIN`.
        :type IdentityType: str
        :param VerifiedForSendingStatus: Verification passed or not.
        :type VerifiedForSendingStatus: bool
        :param Attributes: DNS information that needs to be configured.
        :type Attributes: list of DNSAttributes
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.IdentityType = None
        self.VerifiedForSendingStatus = None
        self.Attributes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IdentityType = params.get("IdentityType")
        self.VerifiedForSendingStatus = params.get("VerifiedForSendingStatus")
        if params.get("Attributes") is not None:
            self.Attributes = []
            for item in params.get("Attributes"):
                obj = DNSAttributes()
                obj._deserialize(item)
                self.Attributes.append(obj)
        self.RequestId = params.get("RequestId")


class UpdateEmailTemplateRequest(AbstractModel):
    """UpdateEmailTemplate request structure.

    """

    def __init__(self):
        """
        :param TemplateContent: Template content.
        :type TemplateContent: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        :param TemplateID: Template ID.
        :type TemplateID: int
        :param TemplateName: Template name.
        :type TemplateName: str
        """
        self.TemplateContent = None
        self.TemplateID = None
        self.TemplateName = None


    def _deserialize(self, params):
        if params.get("TemplateContent") is not None:
            self.TemplateContent = TemplateContent()
            self.TemplateContent._deserialize(params.get("TemplateContent"))
        self.TemplateID = params.get("TemplateID")
        self.TemplateName = params.get("TemplateName")


class UpdateEmailTemplateResponse(AbstractModel):
    """UpdateEmailTemplate response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Volume(AbstractModel):
    """Statistics structure.

    """

    def __init__(self):
        """
        :param SendDate: Date
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SendDate: str
        :param RequestCount: Number of email requests.
        :type RequestCount: int
        :param AcceptedCount: Number of email requests accepted by Tencent Cloud.
        :type AcceptedCount: int
        :param DeliveredCount: Number of delivered emails.
        :type DeliveredCount: int
        :param OpenedCount: Number of users (deduplicated) who opened emails.
        :type OpenedCount: int
        :param ClickedCount: Number of recipients who clicked on links in emails.
        :type ClickedCount: int
        :param BounceCount: Number of bounced emails.
        :type BounceCount: int
        :param UnsubscribeCount: Number of users who canceled subscriptions.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnsubscribeCount: int
        """
        self.SendDate = None
        self.RequestCount = None
        self.AcceptedCount = None
        self.DeliveredCount = None
        self.OpenedCount = None
        self.ClickedCount = None
        self.BounceCount = None
        self.UnsubscribeCount = None


    def _deserialize(self, params):
        self.SendDate = params.get("SendDate")
        self.RequestCount = params.get("RequestCount")
        self.AcceptedCount = params.get("AcceptedCount")
        self.DeliveredCount = params.get("DeliveredCount")
        self.OpenedCount = params.get("OpenedCount")
        self.ClickedCount = params.get("ClickedCount")
        self.BounceCount = params.get("BounceCount")
        self.UnsubscribeCount = params.get("UnsubscribeCount")