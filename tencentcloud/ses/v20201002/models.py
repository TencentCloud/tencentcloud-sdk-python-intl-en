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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class Attachment(AbstractModel):
    """Attachment structure, including attachment name and Base64-encoded attachment content

    """

    def __init__(self):
        r"""
        :param FileName: Attachment name, which cannot exceed 255 characters. Some attachment types are not supported. For details, see [Attachment Types](https://intl.cloud.tencent.com/document/product/1288/51951?from_cn_redirect=1).
        :type FileName: str
        :param Content: Attachment content after Base64 encoding. A single attachment cannot exceed 4 MB. Note: Tencent Cloud APIs require that a request packet should not exceed 8 MB. If you are sending multiple attachments, the total size of these attachments cannot exceed 8 MB.
        :type Content: str
        """
        self.FileName = None
        self.Content = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchSendEmailRequest(AbstractModel):
    """BatchSendEmail request structure.

    """

    def __init__(self):
        r"""
        :param FromEmailAddress: Sender address. Enter a sender address, for example, noreply@mail.qcloud.com. To display the sender name, enter the address in the following format:
Sender <email address>, for example:
Tencent Cloud team <noreply@mail.qcloud.com>
        :type FromEmailAddress: str
        :param ReceiverId: Recipient group ID
        :type ReceiverId: int
        :param Subject: Email subject
        :type Subject: str
        :param TaskType: Task type. `1`: immediate; `2`: scheduled; `3`: recurring
        :type TaskType: int
        :param ReplyToAddresses: Reply-to address. You can enter a valid personal email address that can receive emails. If this parameter is left empty, reply emails will fail to be sent.
        :type ReplyToAddresses: str
        :param Template: Template when emails are sent using a template
        :type Template: :class:`tencentcloud.ses.v20201002.models.Template`
        :param Simple: Disused
        :type Simple: :class:`tencentcloud.ses.v20201002.models.Simple`
        :param Attachments: Attachment parameters to set when you need to send attachments. This parameter is currently unavailable.
        :type Attachments: list of Attachment
        :param CycleParam: Parameter required for a recurring sending task
        :type CycleParam: :class:`tencentcloud.ses.v20201002.models.CycleEmailParam`
        :param TimedParam: Parameter required for a scheduled sending task
        :type TimedParam: :class:`tencentcloud.ses.v20201002.models.TimedEmailParam`
        :param Unsubscribe: Unsubscribe option. `1`: provides an unsubscribe link; `0`: does not provide an unsubscribe link
        :type Unsubscribe: str
        :param ADLocation: Whether to add an ad tag. `0`: Add no tag; `1`: Add before the subject; `2`: Add after the subject.
        :type ADLocation: int
        """
        self.FromEmailAddress = None
        self.ReceiverId = None
        self.Subject = None
        self.TaskType = None
        self.ReplyToAddresses = None
        self.Template = None
        self.Simple = None
        self.Attachments = None
        self.CycleParam = None
        self.TimedParam = None
        self.Unsubscribe = None
        self.ADLocation = None


    def _deserialize(self, params):
        self.FromEmailAddress = params.get("FromEmailAddress")
        self.ReceiverId = params.get("ReceiverId")
        self.Subject = params.get("Subject")
        self.TaskType = params.get("TaskType")
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
        if params.get("CycleParam") is not None:
            self.CycleParam = CycleEmailParam()
            self.CycleParam._deserialize(params.get("CycleParam"))
        if params.get("TimedParam") is not None:
            self.TimedParam = TimedEmailParam()
            self.TimedParam._deserialize(params.get("TimedParam"))
        self.Unsubscribe = params.get("Unsubscribe")
        self.ADLocation = params.get("ADLocation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchSendEmailResponse(AbstractModel):
    """BatchSendEmail response structure.

    """

    def __init__(self):
        r"""
        :param TaskId: Sending task ID
        :type TaskId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class BlackEmailAddress(AbstractModel):
    """Email address blocklist structure, including the blocklisted address and the time when it is blocklisted.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmailAddressRequest(AbstractModel):
    """CreateEmailAddress request structure.

    """

    def __init__(self):
        r"""
        :param EmailAddress: Your sender address. (You can create up to 10 sender addresses for each domain.)
        :type EmailAddress: str
        :param EmailSenderName: Sender name.
        :type EmailSenderName: str
        """
        self.EmailAddress = None
        self.EmailSenderName = None


    def _deserialize(self, params):
        self.EmailAddress = params.get("EmailAddress")
        self.EmailSenderName = params.get("EmailSenderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmailAddressResponse(AbstractModel):
    """CreateEmailAddress response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param EmailIdentity: Your sender domain. You are advised to use a third-level domain, for example, mail.qcloud.com.
        :type EmailIdentity: str
        """
        self.EmailIdentity = None


    def _deserialize(self, params):
        self.EmailIdentity = params.get("EmailIdentity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmailIdentityResponse(AbstractModel):
    """CreateEmailIdentity response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmailTemplateResponse(AbstractModel):
    """CreateEmailTemplate response structure.

    """

    def __init__(self):
        r"""
        :param TemplateID: Template ID
        :type TemplateID: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TemplateID = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateID = params.get("TemplateID")
        self.RequestId = params.get("RequestId")


class CreateReceiverDetailRequest(AbstractModel):
    """CreateReceiverDetail request structure.

    """

    def __init__(self):
        r"""
        :param ReceiverId: Recipient group ID
        :type ReceiverId: int
        :param Emails: Email address
        :type Emails: list of str
        """
        self.ReceiverId = None
        self.Emails = None


    def _deserialize(self, params):
        self.ReceiverId = params.get("ReceiverId")
        self.Emails = params.get("Emails")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReceiverDetailResponse(AbstractModel):
    """CreateReceiverDetail response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateReceiverRequest(AbstractModel):
    """CreateReceiver request structure.

    """

    def __init__(self):
        r"""
        :param ReceiversName: Recipient group name
        :type ReceiversName: str
        :param Desc: Recipient group description
        :type Desc: str
        """
        self.ReceiversName = None
        self.Desc = None


    def _deserialize(self, params):
        self.ReceiversName = params.get("ReceiversName")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReceiverResponse(AbstractModel):
    """CreateReceiver response structure.

    """

    def __init__(self):
        r"""
        :param ReceiverId: Recipient group ID, by which recipient email addresses are uploaded
        :type ReceiverId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ReceiverId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReceiverId = params.get("ReceiverId")
        self.RequestId = params.get("RequestId")


class CycleEmailParam(AbstractModel):
    """Parameter required to create a recurring sending task

    """

    def __init__(self):
        r"""
        :param BeginTime: Start time of the task
        :type BeginTime: str
        :param IntervalTime: Task recurrence in hours
        :type IntervalTime: int
        """
        self.BeginTime = None
        self.IntervalTime = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.IntervalTime = params.get("IntervalTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DNSAttributes(AbstractModel):
    """Describes the domain name, record type, expected value, and currently configured value of DNS records.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBlackListRequest(AbstractModel):
    """DeleteBlackList request structure.

    """

    def __init__(self):
        r"""
        :param EmailAddressList: List of email addresses to be unblocklisted. Enter at least one address.
        :type EmailAddressList: list of str
        """
        self.EmailAddressList = None


    def _deserialize(self, params):
        self.EmailAddressList = params.get("EmailAddressList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBlackListResponse(AbstractModel):
    """DeleteBlackList response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param EmailAddress: Sender address.
        :type EmailAddress: str
        """
        self.EmailAddress = None


    def _deserialize(self, params):
        self.EmailAddress = params.get("EmailAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEmailAddressResponse(AbstractModel):
    """DeleteEmailAddress response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param EmailIdentity: Sender domain.
        :type EmailIdentity: str
        """
        self.EmailIdentity = None


    def _deserialize(self, params):
        self.EmailIdentity = params.get("EmailIdentity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEmailIdentityResponse(AbstractModel):
    """DeleteEmailIdentity response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param TemplateID: Template ID
        :type TemplateID: int
        """
        self.TemplateID = None


    def _deserialize(self, params):
        self.TemplateID = params.get("TemplateID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEmailTemplateResponse(AbstractModel):
    """DeleteEmailTemplate response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteReceiverRequest(AbstractModel):
    """DeleteReceiver request structure.

    """

    def __init__(self):
        r"""
        :param ReceiverId: Recipient group ID, which is returned when a recipient group is created.
        :type ReceiverId: int
        """
        self.ReceiverId = None


    def _deserialize(self, params):
        self.ReceiverId = params.get("ReceiverId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReceiverResponse(AbstractModel):
    """DeleteReceiver response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param IdentityName: Sender domain.
        :type IdentityName: str
        :param IdentityType: Verification type. The value is fixed to `DOMAIN`.
        :type IdentityType: str
        :param SendingEnabled: Verification passed or not.
        :type SendingEnabled: bool
        :param CurrentReputationLevel: Current reputation level
        :type CurrentReputationLevel: int
        :param DailyQuota: Maximum number of messages sent per day
        :type DailyQuota: int
        """
        self.IdentityName = None
        self.IdentityType = None
        self.SendingEnabled = None
        self.CurrentReputationLevel = None
        self.DailyQuota = None


    def _deserialize(self, params):
        self.IdentityName = params.get("IdentityName")
        self.IdentityType = params.get("IdentityType")
        self.SendingEnabled = params.get("SendingEnabled")
        self.CurrentReputationLevel = params.get("CurrentReputationLevel")
        self.DailyQuota = params.get("DailyQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmailSender(AbstractModel):
    """Describes sender information.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEmailIdentityRequest(AbstractModel):
    """GetEmailIdentity request structure.

    """

    def __init__(self):
        r"""
        :param EmailIdentity: Sender domain.
        :type EmailIdentity: str
        """
        self.EmailIdentity = None


    def _deserialize(self, params):
        self.EmailIdentity = params.get("EmailIdentity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEmailIdentityResponse(AbstractModel):
    """GetEmailIdentity response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param TemplateID: Template ID.
        :type TemplateID: int
        """
        self.TemplateID = None


    def _deserialize(self, params):
        self.TemplateID = params.get("TemplateID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEmailTemplateResponse(AbstractModel):
    """GetEmailTemplate response structure.

    """

    def __init__(self):
        r"""
        :param TemplateContent: Template content.
        :type TemplateContent: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        :param TemplateStatus: Template status. Valid values: `0` (approved); `1` (pending approval); `2` (rejected).
        :type TemplateStatus: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TemplateContent = None
        self.TemplateStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TemplateContent") is not None:
            self.TemplateContent = TemplateContent()
            self.TemplateContent._deserialize(params.get("TemplateContent"))
        self.TemplateStatus = params.get("TemplateStatus")
        self.RequestId = params.get("RequestId")


class GetSendEmailStatusRequest(AbstractModel):
    """GetSendEmailStatus request structure.

    """

    def __init__(self):
        r"""
        :param RequestDate: Date sent. This parameter is required. You can only query the sending status for a single date at a time.
        :type RequestDate: str
        :param Offset: Offset. Default value: `0`.
        :type Offset: int
        :param Limit: Maximum number of pulled entries. Maximum value: `100`.
        :type Limit: int
        :param MessageId: The `MessageId` field returned by the `SendMail` API.
        :type MessageId: str
        :param ToEmailAddress: Recipient email address.
        :type ToEmailAddress: str
        """
        self.RequestDate = None
        self.Offset = None
        self.Limit = None
        self.MessageId = None
        self.ToEmailAddress = None


    def _deserialize(self, params):
        self.RequestDate = params.get("RequestDate")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.MessageId = params.get("MessageId")
        self.ToEmailAddress = params.get("ToEmailAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSendEmailStatusResponse(AbstractModel):
    """GetSendEmailStatus response structure.

    """

    def __init__(self):
        r"""
        :param EmailStatusList: Status of sent emails
        :type EmailStatusList: list of SendEmailStatus
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EmailStatusList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EmailStatusList") is not None:
            self.EmailStatusList = []
            for item in params.get("EmailStatusList"):
                obj = SendEmailStatus()
                obj._deserialize(item)
                self.EmailStatusList.append(obj)
        self.RequestId = params.get("RequestId")


class GetStatisticsReportRequest(AbstractModel):
    """GetStatisticsReport request structure.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetStatisticsReportResponse(AbstractModel):
    """GetStatisticsReport response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param StartDate: Start date in the format of `YYYY-MM-DD`
        :type StartDate: str
        :param EndDate: End date in the format of `YYYY-MM-DD`
        :type EndDate: str
        :param Limit: Common parameter. It must be used with `Offset`.
        :type Limit: int
        :param Offset: Common parameter. It must be used with `Limit`. Maximum value of `Limit`: `100`.
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListBlackEmailAddressResponse(AbstractModel):
    """ListBlackEmailAddress response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
        :param EmailIdentities: List of sender domains.
        :type EmailIdentities: list of EmailIdentity
        :param MaxReputationLevel: Maximum reputation level
        :type MaxReputationLevel: int
        :param MaxDailyQuota: Maximum number of emails sent per domain name
        :type MaxDailyQuota: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EmailIdentities = None
        self.MaxReputationLevel = None
        self.MaxDailyQuota = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EmailIdentities") is not None:
            self.EmailIdentities = []
            for item in params.get("EmailIdentities"):
                obj = EmailIdentity()
                obj._deserialize(item)
                self.EmailIdentities.append(obj)
        self.MaxReputationLevel = params.get("MaxReputationLevel")
        self.MaxDailyQuota = params.get("MaxDailyQuota")
        self.RequestId = params.get("RequestId")


class ListEmailTemplatesRequest(AbstractModel):
    """ListEmailTemplates request structure.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEmailTemplatesResponse(AbstractModel):
    """ListEmailTemplates response structure.

    """

    def __init__(self):
        r"""
        :param TemplatesMetadata: List of email templates.
        :type TemplatesMetadata: list of TemplatesMetadata
        :param TotalCount: Total number of templates
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


class ListReceiversRequest(AbstractModel):
    """ListReceivers request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Offset, starting from 0. The value is an integer.
        :type Offset: int
        :param Limit: Number of records to query. The value is an integer not exceeding 100.
        :type Limit: int
        :param Status: Group status (`1`: to be uploaded; `2` uploading; `3` uploaded). To query groups in all states, do not pass in this parameter.
        :type Status: int
        :param KeyWord: Group name keyword for fuzzy query
        :type KeyWord: str
        """
        self.Offset = None
        self.Limit = None
        self.Status = None
        self.KeyWord = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Status = params.get("Status")
        self.KeyWord = params.get("KeyWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListReceiversResponse(AbstractModel):
    """ListReceivers response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number
        :type TotalCount: int
        :param Data: Data record
        :type Data: list of ReceiverData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ReceiverData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class ListSendTasksRequest(AbstractModel):
    """ListSendTasks request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Offset, starting from 0. The value is an integer. `0` means to skip 0 entries.
        :type Offset: int
        :param Limit: Number of records to query. The value is an integer not exceeding 100.
        :type Limit: int
        :param Status: Task status. `1`: to start; `5`: sending; `6`: sending suspended today; `7`: sending error; `10`: sent. To query tasks in all states, do not pass in this parameter.
        :type Status: int
        :param ReceiverId: Recipient group ID
        :type ReceiverId: int
        :param TaskType: Task type. `1`: immediate; `2`: scheduled; `3`: recurring. To query tasks of all types, do not pass in this parameter.
        :type TaskType: int
        """
        self.Offset = None
        self.Limit = None
        self.Status = None
        self.ReceiverId = None
        self.TaskType = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Status = params.get("Status")
        self.ReceiverId = params.get("ReceiverId")
        self.TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSendTasksResponse(AbstractModel):
    """ListSendTasks response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number
        :type TotalCount: int
        :param Data: Data record
        :type Data: list of SendTaskData
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SendTaskData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class ReceiverData(AbstractModel):
    """Recipient group data type

    """

    def __init__(self):
        r"""
        :param ReceiverId: Recipient group ID
        :type ReceiverId: int
        :param ReceiversName: Recipient group name
        :type ReceiversName: str
        :param Count: Total number of recipient email addresses
        :type Count: int
        :param Desc: Recipient group description
Note: This field may return `null`, indicating that no valid value can be found.
        :type Desc: str
        :param ReceiversStatus: Group status (`1`: to be uploaded; `2` uploading; `3` uploaded)
Note: This field may return `null`, indicating that no valid value can be found.
        :type ReceiversStatus: int
        :param CreateTime: Creation time, such as 2021-09-28 16:40:35
        :type CreateTime: str
        """
        self.ReceiverId = None
        self.ReceiversName = None
        self.Count = None
        self.Desc = None
        self.ReceiversStatus = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ReceiverId = params.get("ReceiverId")
        self.ReceiversName = params.get("ReceiversName")
        self.Count = params.get("Count")
        self.Desc = params.get("Desc")
        self.ReceiversStatus = params.get("ReceiversStatus")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendEmailRequest(AbstractModel):
    """SendEmail request structure.

    """

    def __init__(self):
        r"""
        :param FromEmailAddress: Sender address. Enter a sender address, for example, noreply@mail.qcloud.com.
To display the sender name, enter the address in the following format: 
Sender <email address>
        :type FromEmailAddress: str
        :param Destination: Recipient email addresses. You can send an email to up to 50 recipients at a time. Note: the email content will display all recipient addresses. To send one-to-one emails to several recipients, please call the API multiple times to send the emails.
        :type Destination: list of str
        :param Subject: Email subject.
        :type Subject: str
        :param ReplyToAddresses: Reply-to address. You can enter a valid personal email address that can receive emails. If this parameter is left empty, reply emails will fail to be sent.
        :type ReplyToAddresses: str
        :param Template: Template when sending emails using a template.
        :type Template: :class:`tencentcloud.ses.v20201002.models.Template`
        :param Simple: Disused
        :type Simple: :class:`tencentcloud.ses.v20201002.models.Simple`
        :param Attachments: Email attachments
        :type Attachments: list of Attachment
        :param Unsubscribe: Unsubscribe option. `1`: provides an unsubscribe link; `0`: does not provide an unsubscribe link
        :type Unsubscribe: str
        :param TriggerType: Email triggering type. `0` (default): non-trigger-based, suitable for marketing emails and non-immediate emails; `1`: trigger-based, suitable for immediate emails such as emails containing verification codes. If the size of an email exceeds a specified value, the system will automatically choose the non-trigger-based type.
        :type TriggerType: int
        """
        self.FromEmailAddress = None
        self.Destination = None
        self.Subject = None
        self.ReplyToAddresses = None
        self.Template = None
        self.Simple = None
        self.Attachments = None
        self.Unsubscribe = None
        self.TriggerType = None


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
        self.Unsubscribe = params.get("Unsubscribe")
        self.TriggerType = params.get("TriggerType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendEmailResponse(AbstractModel):
    """SendEmail response structure.

    """

    def __init__(self):
        r"""
        :param MessageId: Unique ID generated when receiving the message
        :type MessageId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MessageId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MessageId = params.get("MessageId")
        self.RequestId = params.get("RequestId")


class SendEmailStatus(AbstractModel):
    """Describes the email sending status

    """

    def __init__(self):
        r"""
        :param MessageId: The `MessageId` field returned by the `SendEmail` API
        :type MessageId: str
        :param ToEmailAddress: Recipient email address
        :type ToEmailAddress: str
        :param FromEmailAddress: Sender email address
        :type FromEmailAddress: str
        :param SendStatus: Tencent Cloud processing status
0: Successful.
1001: Internal system exception.
1002: Internal system exception.
1003: Internal system exception.
1003: Internal system exception.
1004: Email sending timed out.
1005: Internal system exception.
1006: You have sent too many emails to the same address in a short period.
1007: The email address is in the blocklist.
1009: Internal system exception.
1010: The daily email sending limit is exceeded.
1011: You have no permission to send custom content. Use a template.
2001: No results were found.
3007: The template ID is invalid or the template is unavailable.
3008: Template status exception.
3009: You have no permission to use this template.
3010: The format of the `TemplateData` field is incorrect. 
3014: The email cannot be sent because the sender domain is not verified.
3020: The recipient email address is in the blocklist.
3024: Failed to precheck the email address format.
3030: Email sending is restricted temporarily due to high bounce rate.
3033: The account has insufficient balance or overdue payment.
        :type SendStatus: int
        :param DeliverStatus: Recipient processing status
0: Tencent Cloud has accepted the request and added it to the send queue.
1: The email is delivered successfully. `DeliverTime` indicates the time when the email is delivered successfully.
2: The email is discarded. `DeliverMessage` indicates the reason for discarding.
3: The recipient's ESP rejects the email, probably because the email address does not exist or due to other reasons.
8: The email is delayed by the ESP. `DeliverMessage` indicates the reason for delay.
        :type DeliverStatus: int
        :param DeliverMessage: Description of the recipient processing status
        :type DeliverMessage: str
        :param RequestTime: Timestamp when the request arrives at Tencent Cloud
        :type RequestTime: int
        :param DeliverTime: Timestamp when Tencent Cloud delivers the email
        :type DeliverTime: int
        :param UserOpened: Whether the recipient has opened the email
        :type UserOpened: bool
        :param UserClicked: Whether the recipient has clicked the links in the email
        :type UserClicked: bool
        :param UserUnsubscribed: Whether the recipient has unsubscribed from the email sent by the sender
        :type UserUnsubscribed: bool
        :param UserComplainted: Whether the recipient has reported the sender
        :type UserComplainted: bool
        """
        self.MessageId = None
        self.ToEmailAddress = None
        self.FromEmailAddress = None
        self.SendStatus = None
        self.DeliverStatus = None
        self.DeliverMessage = None
        self.RequestTime = None
        self.DeliverTime = None
        self.UserOpened = None
        self.UserClicked = None
        self.UserUnsubscribed = None
        self.UserComplainted = None


    def _deserialize(self, params):
        self.MessageId = params.get("MessageId")
        self.ToEmailAddress = params.get("ToEmailAddress")
        self.FromEmailAddress = params.get("FromEmailAddress")
        self.SendStatus = params.get("SendStatus")
        self.DeliverStatus = params.get("DeliverStatus")
        self.DeliverMessage = params.get("DeliverMessage")
        self.RequestTime = params.get("RequestTime")
        self.DeliverTime = params.get("DeliverTime")
        self.UserOpened = params.get("UserOpened")
        self.UserClicked = params.get("UserClicked")
        self.UserUnsubscribed = params.get("UserUnsubscribed")
        self.UserComplainted = params.get("UserComplainted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendTaskData(AbstractModel):
    """Email sending task data

    """

    def __init__(self):
        r"""
        :param TaskId: Task ID
        :type TaskId: int
        :param FromEmailAddress: Sender address
        :type FromEmailAddress: str
        :param ReceiverId: Recipient group ID
        :type ReceiverId: int
        :param TaskStatus: Task status. `1`: to start; `5`: sending; `6`: sending suspended today; `7`: sending error; `10`: sent
        :type TaskStatus: int
        :param TaskType: Task type. `1`: immediate; `2`: scheduled; `3`: recurring
        :type TaskType: int
        :param RequestCount: Number of emails requested to be sent
        :type RequestCount: int
        :param SendCount: Number of emails sent
        :type SendCount: int
        :param CacheCount: Number of emails cached
        :type CacheCount: int
        :param CreateTime: Task creation time
        :type CreateTime: str
        :param UpdateTime: Task update time
        :type UpdateTime: str
        :param Subject: Email subject
        :type Subject: str
        :param Template: Template and template data
Note: This field may return `null`, indicating that no valid value can be found.
        :type Template: :class:`tencentcloud.ses.v20201002.models.Template`
        :param CycleParam: Parameters of a recurring task
Note: This field may return `null`, indicating that no valid value can be found.
        :type CycleParam: :class:`tencentcloud.ses.v20201002.models.CycleEmailParam`
        :param TimedParam: Parameters of a scheduled task
Note: This field may return `null`, indicating that no valid value can be found.
        :type TimedParam: :class:`tencentcloud.ses.v20201002.models.TimedEmailParam`
        :param ErrMsg: Task exception information
Note: This field may return `null`, indicating that no valid value can be found.
        :type ErrMsg: str
        :param ReceiversName: Recipient group name
        :type ReceiversName: str
        """
        self.TaskId = None
        self.FromEmailAddress = None
        self.ReceiverId = None
        self.TaskStatus = None
        self.TaskType = None
        self.RequestCount = None
        self.SendCount = None
        self.CacheCount = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Subject = None
        self.Template = None
        self.CycleParam = None
        self.TimedParam = None
        self.ErrMsg = None
        self.ReceiversName = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.FromEmailAddress = params.get("FromEmailAddress")
        self.ReceiverId = params.get("ReceiverId")
        self.TaskStatus = params.get("TaskStatus")
        self.TaskType = params.get("TaskType")
        self.RequestCount = params.get("RequestCount")
        self.SendCount = params.get("SendCount")
        self.CacheCount = params.get("CacheCount")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Subject = params.get("Subject")
        if params.get("Template") is not None:
            self.Template = Template()
            self.Template._deserialize(params.get("Template"))
        if params.get("CycleParam") is not None:
            self.CycleParam = CycleEmailParam()
            self.CycleParam._deserialize(params.get("CycleParam"))
        if params.get("TimedParam") is not None:
            self.TimedParam = TimedEmailParam()
            self.TimedParam._deserialize(params.get("TimedParam"))
        self.ErrMsg = params.get("ErrMsg")
        self.ReceiversName = params.get("ReceiversName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Simple(AbstractModel):
    """Email content, which can be plain text (TEXT), pure code (HTML), or a combination of TEXT and HTML (recommended).

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Template(AbstractModel):
    """Template information, including template ID, template variable parameters, etc.

    """

    def __init__(self):
        r"""
        :param TemplateID: Template ID. If you don’t have any template, please create one.
        :type TemplateID: int
        :param TemplateData: Variable parameters in the template. Please use `json.dump` to format the JSON object into a string type. The object is a set of key-value pairs. Each key denotes a variable, which is represented by {{key}}. The key will be replaced with the corresponding value (represented by {{value}}) when sending the email.
Note: The parameter value cannot be data of a complex type such as HTML.
Example: {"name":"xxx","age":"xx"}
        :type TemplateData: str
        """
        self.TemplateID = None
        self.TemplateData = None


    def _deserialize(self, params):
        self.TemplateID = params.get("TemplateID")
        self.TemplateData = params.get("TemplateData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateContent(AbstractModel):
    """Template content, which must include at least one of TEXT and HTML. A combination of TEXT and HTML is recommended.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplatesMetadata(AbstractModel):
    """Template list structure.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimedEmailParam(AbstractModel):
    """Time parameter required to create a scheduled sending task, such as the start time

    """

    def __init__(self):
        r"""
        :param BeginTime: Start time of a scheduled sending task
        :type BeginTime: str
        """
        self.BeginTime = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEmailIdentityRequest(AbstractModel):
    """UpdateEmailIdentity request structure.

    """

    def __init__(self):
        r"""
        :param EmailIdentity: Domain to be verified.
        :type EmailIdentity: str
        """
        self.EmailIdentity = None


    def _deserialize(self, params):
        self.EmailIdentity = params.get("EmailIdentity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEmailIdentityResponse(AbstractModel):
    """UpdateEmailIdentity response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param TemplateContent: Template content.
        :type TemplateContent: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        :param TemplateID: Template ID.
        :type TemplateID: int
        :param TemplateName: Template name
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEmailTemplateResponse(AbstractModel):
    """UpdateEmailTemplate response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        