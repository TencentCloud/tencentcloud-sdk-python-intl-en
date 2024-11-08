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
        :param _FileName: Attachment name, which cannot exceed 255 characters. Some attachment types are not supported. For details, see [Attachment Types](https://intl.cloud.tencent.com/document/product/1288/51951?from_cn_redirect=1).
        :type FileName: str
        :param _Content: Base64-encoded attachment content. You can send attachments of up to 4 MB in the total size. Note: The TencentCloud API supports a request packet of up to 8 MB in size, and the size of the attachment content will increase by 1.5 times after Base64 encoding. Therefore, you need to keep the total size of all attachments below 4 MB. If the entire request exceeds 8 MB, the API will return an error.
        :type Content: str
        """
        self._FileName = None
        self._Content = None

    @property
    def FileName(self):
        """Attachment name, which cannot exceed 255 characters. Some attachment types are not supported. For details, see [Attachment Types](https://intl.cloud.tencent.com/document/product/1288/51951?from_cn_redirect=1).
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Content(self):
        """Base64-encoded attachment content. You can send attachments of up to 4 MB in the total size. Note: The TencentCloud API supports a request packet of up to 8 MB in size, and the size of the attachment content will increase by 1.5 times after Base64 encoding. Therefore, you need to keep the total size of all attachments below 4 MB. If the entire request exceeds 8 MB, the API will return an error.
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._FileName = params.get("FileName")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchSendEmailRequest(AbstractModel):
    """BatchSendEmail request structure.

    """

    def __init__(self):
        r"""
        :param _FromEmailAddress: Sender address. Enter a sender address such as `noreply@mail.qcloud.com`. To display the sender name, enter the address in the following format:
sender &lt;email address&gt;. For example:
Tencent Cloud team &lt;noreply@mail.qcloud.com&gt;
        :type FromEmailAddress: str
        :param _ReceiverId: Recipient group ID
        :type ReceiverId: int
        :param _Subject: Email subject
        :type Subject: str
        :param _TaskType: Task type. `1`: immediate; `2`: scheduled; `3`: recurring
        :type TaskType: int
        :param _ReplyToAddresses: Reply-to address. You can enter a valid personal email address that can receive emails. If this parameter is left empty, reply emails will fail to be sent.
        :type ReplyToAddresses: str
        :param _Template: Template when emails are sent using a template
        :type Template: :class:`tencentcloud.ses.v20201002.models.Template`
        :param _Simple: Disused
        :type Simple: :class:`tencentcloud.ses.v20201002.models.Simple`
        :param _Attachments: Attachment parameters to set when you need to send attachments. This parameter is currently unavailable.
        :type Attachments: list of Attachment
        :param _CycleParam: Parameter required for a recurring sending task
        :type CycleParam: :class:`tencentcloud.ses.v20201002.models.CycleEmailParam`
        :param _TimedParam: Parameter required for a scheduled sending task
        :type TimedParam: :class:`tencentcloud.ses.v20201002.models.TimedEmailParam`
        :param _Unsubscribe: Unsubscribe link option. `0`: Do not add unsubscribe link; `1`: English `2`: Simplified Chinese; `3`: Traditional Chinese; `4`: Spanish; `5`: French; `6`: German; `7`: Japanese; `8`: Korean; `9`: Arabic; `10`: Thai
        :type Unsubscribe: str
        :param _ADLocation: Whether to add an ad tag. `0`: Add no tag; `1`: Add before the subject; `2`: Add after the subject.
        :type ADLocation: int
        """
        self._FromEmailAddress = None
        self._ReceiverId = None
        self._Subject = None
        self._TaskType = None
        self._ReplyToAddresses = None
        self._Template = None
        self._Simple = None
        self._Attachments = None
        self._CycleParam = None
        self._TimedParam = None
        self._Unsubscribe = None
        self._ADLocation = None

    @property
    def FromEmailAddress(self):
        """Sender address. Enter a sender address such as `noreply@mail.qcloud.com`. To display the sender name, enter the address in the following format:
sender &lt;email address&gt;. For example:
Tencent Cloud team &lt;noreply@mail.qcloud.com&gt;
        :rtype: str
        """
        return self._FromEmailAddress

    @FromEmailAddress.setter
    def FromEmailAddress(self, FromEmailAddress):
        self._FromEmailAddress = FromEmailAddress

    @property
    def ReceiverId(self):
        """Recipient group ID
        :rtype: int
        """
        return self._ReceiverId

    @ReceiverId.setter
    def ReceiverId(self, ReceiverId):
        self._ReceiverId = ReceiverId

    @property
    def Subject(self):
        """Email subject
        :rtype: str
        """
        return self._Subject

    @Subject.setter
    def Subject(self, Subject):
        self._Subject = Subject

    @property
    def TaskType(self):
        """Task type. `1`: immediate; `2`: scheduled; `3`: recurring
        :rtype: int
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def ReplyToAddresses(self):
        """Reply-to address. You can enter a valid personal email address that can receive emails. If this parameter is left empty, reply emails will fail to be sent.
        :rtype: str
        """
        return self._ReplyToAddresses

    @ReplyToAddresses.setter
    def ReplyToAddresses(self, ReplyToAddresses):
        self._ReplyToAddresses = ReplyToAddresses

    @property
    def Template(self):
        """Template when emails are sent using a template
        :rtype: :class:`tencentcloud.ses.v20201002.models.Template`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def Simple(self):
        """Disused
        :rtype: :class:`tencentcloud.ses.v20201002.models.Simple`
        """
        return self._Simple

    @Simple.setter
    def Simple(self, Simple):
        self._Simple = Simple

    @property
    def Attachments(self):
        """Attachment parameters to set when you need to send attachments. This parameter is currently unavailable.
        :rtype: list of Attachment
        """
        return self._Attachments

    @Attachments.setter
    def Attachments(self, Attachments):
        self._Attachments = Attachments

    @property
    def CycleParam(self):
        """Parameter required for a recurring sending task
        :rtype: :class:`tencentcloud.ses.v20201002.models.CycleEmailParam`
        """
        return self._CycleParam

    @CycleParam.setter
    def CycleParam(self, CycleParam):
        self._CycleParam = CycleParam

    @property
    def TimedParam(self):
        """Parameter required for a scheduled sending task
        :rtype: :class:`tencentcloud.ses.v20201002.models.TimedEmailParam`
        """
        return self._TimedParam

    @TimedParam.setter
    def TimedParam(self, TimedParam):
        self._TimedParam = TimedParam

    @property
    def Unsubscribe(self):
        """Unsubscribe link option. `0`: Do not add unsubscribe link; `1`: English `2`: Simplified Chinese; `3`: Traditional Chinese; `4`: Spanish; `5`: French; `6`: German; `7`: Japanese; `8`: Korean; `9`: Arabic; `10`: Thai
        :rtype: str
        """
        return self._Unsubscribe

    @Unsubscribe.setter
    def Unsubscribe(self, Unsubscribe):
        self._Unsubscribe = Unsubscribe

    @property
    def ADLocation(self):
        """Whether to add an ad tag. `0`: Add no tag; `1`: Add before the subject; `2`: Add after the subject.
        :rtype: int
        """
        return self._ADLocation

    @ADLocation.setter
    def ADLocation(self, ADLocation):
        self._ADLocation = ADLocation


    def _deserialize(self, params):
        self._FromEmailAddress = params.get("FromEmailAddress")
        self._ReceiverId = params.get("ReceiverId")
        self._Subject = params.get("Subject")
        self._TaskType = params.get("TaskType")
        self._ReplyToAddresses = params.get("ReplyToAddresses")
        if params.get("Template") is not None:
            self._Template = Template()
            self._Template._deserialize(params.get("Template"))
        if params.get("Simple") is not None:
            self._Simple = Simple()
            self._Simple._deserialize(params.get("Simple"))
        if params.get("Attachments") is not None:
            self._Attachments = []
            for item in params.get("Attachments"):
                obj = Attachment()
                obj._deserialize(item)
                self._Attachments.append(obj)
        if params.get("CycleParam") is not None:
            self._CycleParam = CycleEmailParam()
            self._CycleParam._deserialize(params.get("CycleParam"))
        if params.get("TimedParam") is not None:
            self._TimedParam = TimedEmailParam()
            self._TimedParam._deserialize(params.get("TimedParam"))
        self._Unsubscribe = params.get("Unsubscribe")
        self._ADLocation = params.get("ADLocation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchSendEmailResponse(AbstractModel):
    """BatchSendEmail response structure.

    """

    def __init__(self):
        r"""
        :param _TaskId: Sending task ID
        :type TaskId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """Sending task ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class BlackEmailAddress(AbstractModel):
    """Email address blocklist structure, including the blocklisted address and the time when it is blocklisted.

    """

    def __init__(self):
        r"""
        :param _BounceTime: Time when the email address is blocklisted.
        :type BounceTime: str
        :param _EmailAddress: Blocklisted email address.
        :type EmailAddress: str
        """
        self._BounceTime = None
        self._EmailAddress = None

    @property
    def BounceTime(self):
        """Time when the email address is blocklisted.
        :rtype: str
        """
        return self._BounceTime

    @BounceTime.setter
    def BounceTime(self, BounceTime):
        self._BounceTime = BounceTime

    @property
    def EmailAddress(self):
        """Blocklisted email address.
        :rtype: str
        """
        return self._EmailAddress

    @EmailAddress.setter
    def EmailAddress(self, EmailAddress):
        self._EmailAddress = EmailAddress


    def _deserialize(self, params):
        self._BounceTime = params.get("BounceTime")
        self._EmailAddress = params.get("EmailAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmailAddressRequest(AbstractModel):
    """CreateEmailAddress request structure.

    """

    def __init__(self):
        r"""
        :param _EmailAddress: Your sender address. (You can create up to 10 sender addresses for each domain.)
        :type EmailAddress: str
        :param _EmailSenderName: Sender name.
        :type EmailSenderName: str
        """
        self._EmailAddress = None
        self._EmailSenderName = None

    @property
    def EmailAddress(self):
        """Your sender address. (You can create up to 10 sender addresses for each domain.)
        :rtype: str
        """
        return self._EmailAddress

    @EmailAddress.setter
    def EmailAddress(self, EmailAddress):
        self._EmailAddress = EmailAddress

    @property
    def EmailSenderName(self):
        """Sender name.
        :rtype: str
        """
        return self._EmailSenderName

    @EmailSenderName.setter
    def EmailSenderName(self, EmailSenderName):
        self._EmailSenderName = EmailSenderName


    def _deserialize(self, params):
        self._EmailAddress = params.get("EmailAddress")
        self._EmailSenderName = params.get("EmailSenderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmailAddressResponse(AbstractModel):
    """CreateEmailAddress response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateEmailIdentityRequest(AbstractModel):
    """CreateEmailIdentity request structure.

    """

    def __init__(self):
        r"""
        :param _EmailIdentity: Your sender domain. You are advised to use a third-level domain, for example, mail.qcloud.com.
        :type EmailIdentity: str
        """
        self._EmailIdentity = None

    @property
    def EmailIdentity(self):
        """Your sender domain. You are advised to use a third-level domain, for example, mail.qcloud.com.
        :rtype: str
        """
        return self._EmailIdentity

    @EmailIdentity.setter
    def EmailIdentity(self, EmailIdentity):
        self._EmailIdentity = EmailIdentity


    def _deserialize(self, params):
        self._EmailIdentity = params.get("EmailIdentity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmailIdentityResponse(AbstractModel):
    """CreateEmailIdentity response structure.

    """

    def __init__(self):
        r"""
        :param _IdentityType: Verification type. The value is fixed to `DOMAIN`.
        :type IdentityType: str
        :param _VerifiedForSendingStatus: Verification passed or not.
        :type VerifiedForSendingStatus: bool
        :param _Attributes: DNS information that needs to be configured.
        :type Attributes: list of DNSAttributes
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IdentityType = None
        self._VerifiedForSendingStatus = None
        self._Attributes = None
        self._RequestId = None

    @property
    def IdentityType(self):
        """Verification type. The value is fixed to `DOMAIN`.
        :rtype: str
        """
        return self._IdentityType

    @IdentityType.setter
    def IdentityType(self, IdentityType):
        self._IdentityType = IdentityType

    @property
    def VerifiedForSendingStatus(self):
        """Verification passed or not.
        :rtype: bool
        """
        return self._VerifiedForSendingStatus

    @VerifiedForSendingStatus.setter
    def VerifiedForSendingStatus(self, VerifiedForSendingStatus):
        self._VerifiedForSendingStatus = VerifiedForSendingStatus

    @property
    def Attributes(self):
        """DNS information that needs to be configured.
        :rtype: list of DNSAttributes
        """
        return self._Attributes

    @Attributes.setter
    def Attributes(self, Attributes):
        self._Attributes = Attributes

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IdentityType = params.get("IdentityType")
        self._VerifiedForSendingStatus = params.get("VerifiedForSendingStatus")
        if params.get("Attributes") is not None:
            self._Attributes = []
            for item in params.get("Attributes"):
                obj = DNSAttributes()
                obj._deserialize(item)
                self._Attributes.append(obj)
        self._RequestId = params.get("RequestId")


class CreateEmailTemplateRequest(AbstractModel):
    """CreateEmailTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateName: Template name.
        :type TemplateName: str
        :param _TemplateContent: Template content.
        :type TemplateContent: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        """
        self._TemplateName = None
        self._TemplateContent = None

    @property
    def TemplateName(self):
        """Template name.
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateContent(self):
        """Template content.
        :rtype: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        """
        return self._TemplateContent

    @TemplateContent.setter
    def TemplateContent(self, TemplateContent):
        self._TemplateContent = TemplateContent


    def _deserialize(self, params):
        self._TemplateName = params.get("TemplateName")
        if params.get("TemplateContent") is not None:
            self._TemplateContent = TemplateContent()
            self._TemplateContent._deserialize(params.get("TemplateContent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEmailTemplateResponse(AbstractModel):
    """CreateEmailTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _TemplateID: Template ID
        :type TemplateID: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TemplateID = None
        self._RequestId = None

    @property
    def TemplateID(self):
        """Template ID
        :rtype: int
        """
        return self._TemplateID

    @TemplateID.setter
    def TemplateID(self, TemplateID):
        self._TemplateID = TemplateID

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TemplateID = params.get("TemplateID")
        self._RequestId = params.get("RequestId")


class CreateReceiverDetailRequest(AbstractModel):
    """CreateReceiverDetail request structure.

    """

    def __init__(self):
        r"""
        :param _ReceiverId: Recipient group ID
        :type ReceiverId: int
        :param _Emails: Email address
        :type Emails: list of str
        """
        self._ReceiverId = None
        self._Emails = None

    @property
    def ReceiverId(self):
        """Recipient group ID
        :rtype: int
        """
        return self._ReceiverId

    @ReceiverId.setter
    def ReceiverId(self, ReceiverId):
        self._ReceiverId = ReceiverId

    @property
    def Emails(self):
        """Email address
        :rtype: list of str
        """
        return self._Emails

    @Emails.setter
    def Emails(self, Emails):
        self._Emails = Emails


    def _deserialize(self, params):
        self._ReceiverId = params.get("ReceiverId")
        self._Emails = params.get("Emails")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReceiverDetailResponse(AbstractModel):
    """CreateReceiverDetail response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateReceiverRequest(AbstractModel):
    """CreateReceiver request structure.

    """

    def __init__(self):
        r"""
        :param _ReceiversName: Recipient group name
        :type ReceiversName: str
        :param _Desc: Recipient group description
        :type Desc: str
        """
        self._ReceiversName = None
        self._Desc = None

    @property
    def ReceiversName(self):
        """Recipient group name
        :rtype: str
        """
        return self._ReceiversName

    @ReceiversName.setter
    def ReceiversName(self, ReceiversName):
        self._ReceiversName = ReceiversName

    @property
    def Desc(self):
        """Recipient group description
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._ReceiversName = params.get("ReceiversName")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReceiverResponse(AbstractModel):
    """CreateReceiver response structure.

    """

    def __init__(self):
        r"""
        :param _ReceiverId: Recipient group ID, by which recipient email addresses are uploaded
        :type ReceiverId: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ReceiverId = None
        self._RequestId = None

    @property
    def ReceiverId(self):
        """Recipient group ID, by which recipient email addresses are uploaded
        :rtype: int
        """
        return self._ReceiverId

    @ReceiverId.setter
    def ReceiverId(self, ReceiverId):
        self._ReceiverId = ReceiverId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReceiverId = params.get("ReceiverId")
        self._RequestId = params.get("RequestId")


class CycleEmailParam(AbstractModel):
    """Parameter required to create a recurring sending task

    """

    def __init__(self):
        r"""
        :param _BeginTime: Start time of the task
        :type BeginTime: str
        :param _IntervalTime: Task recurrence in hours
        :type IntervalTime: int
        :param _TermCycle: Specifies whether to end the cycle. This parameter is used to update the task. Valid values: 0: No; 1: Yes.
        :type TermCycle: int
        """
        self._BeginTime = None
        self._IntervalTime = None
        self._TermCycle = None

    @property
    def BeginTime(self):
        """Start time of the task
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def IntervalTime(self):
        """Task recurrence in hours
        :rtype: int
        """
        return self._IntervalTime

    @IntervalTime.setter
    def IntervalTime(self, IntervalTime):
        self._IntervalTime = IntervalTime

    @property
    def TermCycle(self):
        """Specifies whether to end the cycle. This parameter is used to update the task. Valid values: 0: No; 1: Yes.
        :rtype: int
        """
        return self._TermCycle

    @TermCycle.setter
    def TermCycle(self, TermCycle):
        self._TermCycle = TermCycle


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        self._IntervalTime = params.get("IntervalTime")
        self._TermCycle = params.get("TermCycle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DNSAttributes(AbstractModel):
    """Describes the domain name, record type, expected value, and currently configured value of DNS records.

    """

    def __init__(self):
        r"""
        :param _Type: Record types: CNAME, A, TXT, and MX.
        :type Type: str
        :param _SendDomain: Domain name.
        :type SendDomain: str
        :param _ExpectedValue: Expected value.
        :type ExpectedValue: str
        :param _CurrentValue: Currently configured value.
        :type CurrentValue: str
        :param _Status: Approved or not. The default value is `false`.
        :type Status: bool
        """
        self._Type = None
        self._SendDomain = None
        self._ExpectedValue = None
        self._CurrentValue = None
        self._Status = None

    @property
    def Type(self):
        """Record types: CNAME, A, TXT, and MX.
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SendDomain(self):
        """Domain name.
        :rtype: str
        """
        return self._SendDomain

    @SendDomain.setter
    def SendDomain(self, SendDomain):
        self._SendDomain = SendDomain

    @property
    def ExpectedValue(self):
        """Expected value.
        :rtype: str
        """
        return self._ExpectedValue

    @ExpectedValue.setter
    def ExpectedValue(self, ExpectedValue):
        self._ExpectedValue = ExpectedValue

    @property
    def CurrentValue(self):
        """Currently configured value.
        :rtype: str
        """
        return self._CurrentValue

    @CurrentValue.setter
    def CurrentValue(self, CurrentValue):
        self._CurrentValue = CurrentValue

    @property
    def Status(self):
        """Approved or not. The default value is `false`.
        :rtype: bool
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._SendDomain = params.get("SendDomain")
        self._ExpectedValue = params.get("ExpectedValue")
        self._CurrentValue = params.get("CurrentValue")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBlackListRequest(AbstractModel):
    """DeleteBlackList request structure.

    """

    def __init__(self):
        r"""
        :param _EmailAddressList: List of email addresses to be unblocklisted. Enter at least one address.
        :type EmailAddressList: list of str
        """
        self._EmailAddressList = None

    @property
    def EmailAddressList(self):
        """List of email addresses to be unblocklisted. Enter at least one address.
        :rtype: list of str
        """
        return self._EmailAddressList

    @EmailAddressList.setter
    def EmailAddressList(self, EmailAddressList):
        self._EmailAddressList = EmailAddressList


    def _deserialize(self, params):
        self._EmailAddressList = params.get("EmailAddressList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBlackListResponse(AbstractModel):
    """DeleteBlackList response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteEmailAddressRequest(AbstractModel):
    """DeleteEmailAddress request structure.

    """

    def __init__(self):
        r"""
        :param _EmailAddress: Sender address.
        :type EmailAddress: str
        """
        self._EmailAddress = None

    @property
    def EmailAddress(self):
        """Sender address.
        :rtype: str
        """
        return self._EmailAddress

    @EmailAddress.setter
    def EmailAddress(self, EmailAddress):
        self._EmailAddress = EmailAddress


    def _deserialize(self, params):
        self._EmailAddress = params.get("EmailAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEmailAddressResponse(AbstractModel):
    """DeleteEmailAddress response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteEmailIdentityRequest(AbstractModel):
    """DeleteEmailIdentity request structure.

    """

    def __init__(self):
        r"""
        :param _EmailIdentity: Sender domain.
        :type EmailIdentity: str
        """
        self._EmailIdentity = None

    @property
    def EmailIdentity(self):
        """Sender domain.
        :rtype: str
        """
        return self._EmailIdentity

    @EmailIdentity.setter
    def EmailIdentity(self, EmailIdentity):
        self._EmailIdentity = EmailIdentity


    def _deserialize(self, params):
        self._EmailIdentity = params.get("EmailIdentity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEmailIdentityResponse(AbstractModel):
    """DeleteEmailIdentity response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteEmailTemplateRequest(AbstractModel):
    """DeleteEmailTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateID: Template ID
        :type TemplateID: int
        """
        self._TemplateID = None

    @property
    def TemplateID(self):
        """Template ID
        :rtype: int
        """
        return self._TemplateID

    @TemplateID.setter
    def TemplateID(self, TemplateID):
        self._TemplateID = TemplateID


    def _deserialize(self, params):
        self._TemplateID = params.get("TemplateID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEmailTemplateResponse(AbstractModel):
    """DeleteEmailTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteReceiverRequest(AbstractModel):
    """DeleteReceiver request structure.

    """

    def __init__(self):
        r"""
        :param _ReceiverId: Recipient group ID, which is returned when a recipient group is created.
        :type ReceiverId: int
        """
        self._ReceiverId = None

    @property
    def ReceiverId(self):
        """Recipient group ID, which is returned when a recipient group is created.
        :rtype: int
        """
        return self._ReceiverId

    @ReceiverId.setter
    def ReceiverId(self, ReceiverId):
        self._ReceiverId = ReceiverId


    def _deserialize(self, params):
        self._ReceiverId = params.get("ReceiverId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteReceiverResponse(AbstractModel):
    """DeleteReceiver response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EmailIdentity(AbstractModel):
    """Sender domain verification list structure

    """

    def __init__(self):
        r"""
        :param _IdentityName: Sender domain.
        :type IdentityName: str
        :param _IdentityType: Verification type. The value is fixed to `DOMAIN`.
        :type IdentityType: str
        :param _SendingEnabled: Verification passed or not.
        :type SendingEnabled: bool
        :param _CurrentReputationLevel: Current reputation level
        :type CurrentReputationLevel: int
        :param _DailyQuota: Maximum number of messages sent per day
        :type DailyQuota: int
        """
        self._IdentityName = None
        self._IdentityType = None
        self._SendingEnabled = None
        self._CurrentReputationLevel = None
        self._DailyQuota = None

    @property
    def IdentityName(self):
        """Sender domain.
        :rtype: str
        """
        return self._IdentityName

    @IdentityName.setter
    def IdentityName(self, IdentityName):
        self._IdentityName = IdentityName

    @property
    def IdentityType(self):
        """Verification type. The value is fixed to `DOMAIN`.
        :rtype: str
        """
        return self._IdentityType

    @IdentityType.setter
    def IdentityType(self, IdentityType):
        self._IdentityType = IdentityType

    @property
    def SendingEnabled(self):
        """Verification passed or not.
        :rtype: bool
        """
        return self._SendingEnabled

    @SendingEnabled.setter
    def SendingEnabled(self, SendingEnabled):
        self._SendingEnabled = SendingEnabled

    @property
    def CurrentReputationLevel(self):
        """Current reputation level
        :rtype: int
        """
        return self._CurrentReputationLevel

    @CurrentReputationLevel.setter
    def CurrentReputationLevel(self, CurrentReputationLevel):
        self._CurrentReputationLevel = CurrentReputationLevel

    @property
    def DailyQuota(self):
        """Maximum number of messages sent per day
        :rtype: int
        """
        return self._DailyQuota

    @DailyQuota.setter
    def DailyQuota(self, DailyQuota):
        self._DailyQuota = DailyQuota


    def _deserialize(self, params):
        self._IdentityName = params.get("IdentityName")
        self._IdentityType = params.get("IdentityType")
        self._SendingEnabled = params.get("SendingEnabled")
        self._CurrentReputationLevel = params.get("CurrentReputationLevel")
        self._DailyQuota = params.get("DailyQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmailSender(AbstractModel):
    """Describes sender information.

    """

    def __init__(self):
        r"""
        :param _EmailAddress: Sender address.
        :type EmailAddress: str
        :param _EmailSenderName: Sender name.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type EmailSenderName: str
        :param _CreatedTimestamp: Creation time.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type CreatedTimestamp: int
        """
        self._EmailAddress = None
        self._EmailSenderName = None
        self._CreatedTimestamp = None

    @property
    def EmailAddress(self):
        """Sender address.
        :rtype: str
        """
        return self._EmailAddress

    @EmailAddress.setter
    def EmailAddress(self, EmailAddress):
        self._EmailAddress = EmailAddress

    @property
    def EmailSenderName(self):
        """Sender name.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._EmailSenderName

    @EmailSenderName.setter
    def EmailSenderName(self, EmailSenderName):
        self._EmailSenderName = EmailSenderName

    @property
    def CreatedTimestamp(self):
        """Creation time.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._CreatedTimestamp

    @CreatedTimestamp.setter
    def CreatedTimestamp(self, CreatedTimestamp):
        self._CreatedTimestamp = CreatedTimestamp


    def _deserialize(self, params):
        self._EmailAddress = params.get("EmailAddress")
        self._EmailSenderName = params.get("EmailSenderName")
        self._CreatedTimestamp = params.get("CreatedTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEmailIdentityRequest(AbstractModel):
    """GetEmailIdentity request structure.

    """

    def __init__(self):
        r"""
        :param _EmailIdentity: Sender domain.
        :type EmailIdentity: str
        """
        self._EmailIdentity = None

    @property
    def EmailIdentity(self):
        """Sender domain.
        :rtype: str
        """
        return self._EmailIdentity

    @EmailIdentity.setter
    def EmailIdentity(self, EmailIdentity):
        self._EmailIdentity = EmailIdentity


    def _deserialize(self, params):
        self._EmailIdentity = params.get("EmailIdentity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEmailIdentityResponse(AbstractModel):
    """GetEmailIdentity response structure.

    """

    def __init__(self):
        r"""
        :param _IdentityType: Verification type. The value is fixed to `DOMAIN`.
        :type IdentityType: str
        :param _VerifiedForSendingStatus: Verification passed or not.
        :type VerifiedForSendingStatus: bool
        :param _Attributes: DNS configuration details.
        :type Attributes: list of DNSAttributes
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IdentityType = None
        self._VerifiedForSendingStatus = None
        self._Attributes = None
        self._RequestId = None

    @property
    def IdentityType(self):
        """Verification type. The value is fixed to `DOMAIN`.
        :rtype: str
        """
        return self._IdentityType

    @IdentityType.setter
    def IdentityType(self, IdentityType):
        self._IdentityType = IdentityType

    @property
    def VerifiedForSendingStatus(self):
        """Verification passed or not.
        :rtype: bool
        """
        return self._VerifiedForSendingStatus

    @VerifiedForSendingStatus.setter
    def VerifiedForSendingStatus(self, VerifiedForSendingStatus):
        self._VerifiedForSendingStatus = VerifiedForSendingStatus

    @property
    def Attributes(self):
        """DNS configuration details.
        :rtype: list of DNSAttributes
        """
        return self._Attributes

    @Attributes.setter
    def Attributes(self, Attributes):
        self._Attributes = Attributes

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IdentityType = params.get("IdentityType")
        self._VerifiedForSendingStatus = params.get("VerifiedForSendingStatus")
        if params.get("Attributes") is not None:
            self._Attributes = []
            for item in params.get("Attributes"):
                obj = DNSAttributes()
                obj._deserialize(item)
                self._Attributes.append(obj)
        self._RequestId = params.get("RequestId")


class GetEmailTemplateRequest(AbstractModel):
    """GetEmailTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateID: Template ID.
        :type TemplateID: int
        """
        self._TemplateID = None

    @property
    def TemplateID(self):
        """Template ID.
        :rtype: int
        """
        return self._TemplateID

    @TemplateID.setter
    def TemplateID(self, TemplateID):
        self._TemplateID = TemplateID


    def _deserialize(self, params):
        self._TemplateID = params.get("TemplateID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEmailTemplateResponse(AbstractModel):
    """GetEmailTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _TemplateContent: Template content.
        :type TemplateContent: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        :param _TemplateStatus: Template status. Valid values: `0` (approved); `1` (pending approval); `2` (rejected).
        :type TemplateStatus: int
        :param _TemplateName: Template name
        :type TemplateName: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TemplateContent = None
        self._TemplateStatus = None
        self._TemplateName = None
        self._RequestId = None

    @property
    def TemplateContent(self):
        """Template content.
        :rtype: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        """
        return self._TemplateContent

    @TemplateContent.setter
    def TemplateContent(self, TemplateContent):
        self._TemplateContent = TemplateContent

    @property
    def TemplateStatus(self):
        """Template status. Valid values: `0` (approved); `1` (pending approval); `2` (rejected).
        :rtype: int
        """
        return self._TemplateStatus

    @TemplateStatus.setter
    def TemplateStatus(self, TemplateStatus):
        self._TemplateStatus = TemplateStatus

    @property
    def TemplateName(self):
        """Template name
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TemplateContent") is not None:
            self._TemplateContent = TemplateContent()
            self._TemplateContent._deserialize(params.get("TemplateContent"))
        self._TemplateStatus = params.get("TemplateStatus")
        self._TemplateName = params.get("TemplateName")
        self._RequestId = params.get("RequestId")


class GetSendEmailStatusRequest(AbstractModel):
    """GetSendEmailStatus request structure.

    """

    def __init__(self):
        r"""
        :param _RequestDate: Date sent. This parameter is required. You can only query the sending status for a single date at a time.
        :type RequestDate: str
        :param _Offset: Offset. Default value: `0`.
        :type Offset: int
        :param _Limit: Maximum number of pulled entries. Maximum value: `100`.
        :type Limit: int
        :param _MessageId: The `MessageId` field returned by the `SendMail` API.
        :type MessageId: str
        :param _ToEmailAddress: Recipient email address.
        :type ToEmailAddress: str
        """
        self._RequestDate = None
        self._Offset = None
        self._Limit = None
        self._MessageId = None
        self._ToEmailAddress = None

    @property
    def RequestDate(self):
        """Date sent. This parameter is required. You can only query the sending status for a single date at a time.
        :rtype: str
        """
        return self._RequestDate

    @RequestDate.setter
    def RequestDate(self, RequestDate):
        self._RequestDate = RequestDate

    @property
    def Offset(self):
        """Offset. Default value: `0`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Maximum number of pulled entries. Maximum value: `100`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def MessageId(self):
        """The `MessageId` field returned by the `SendMail` API.
        :rtype: str
        """
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

    @property
    def ToEmailAddress(self):
        """Recipient email address.
        :rtype: str
        """
        return self._ToEmailAddress

    @ToEmailAddress.setter
    def ToEmailAddress(self, ToEmailAddress):
        self._ToEmailAddress = ToEmailAddress


    def _deserialize(self, params):
        self._RequestDate = params.get("RequestDate")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._MessageId = params.get("MessageId")
        self._ToEmailAddress = params.get("ToEmailAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSendEmailStatusResponse(AbstractModel):
    """GetSendEmailStatus response structure.

    """

    def __init__(self):
        r"""
        :param _EmailStatusList: Status of sent emails
        :type EmailStatusList: list of SendEmailStatus
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EmailStatusList = None
        self._RequestId = None

    @property
    def EmailStatusList(self):
        """Status of sent emails
        :rtype: list of SendEmailStatus
        """
        return self._EmailStatusList

    @EmailStatusList.setter
    def EmailStatusList(self, EmailStatusList):
        self._EmailStatusList = EmailStatusList

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EmailStatusList") is not None:
            self._EmailStatusList = []
            for item in params.get("EmailStatusList"):
                obj = SendEmailStatus()
                obj._deserialize(item)
                self._EmailStatusList.append(obj)
        self._RequestId = params.get("RequestId")


class GetStatisticsReportRequest(AbstractModel):
    """GetStatisticsReport request structure.

    """

    def __init__(self):
        r"""
        :param _StartDate: Start date.
        :type StartDate: str
        :param _EndDate: End date.
        :type EndDate: str
        :param _Domain: Sender domain.
        :type Domain: str
        :param _ReceivingMailboxType: Recipient address type, for example, gmail.com.
        :type ReceivingMailboxType: str
        """
        self._StartDate = None
        self._EndDate = None
        self._Domain = None
        self._ReceivingMailboxType = None

    @property
    def StartDate(self):
        """Start date.
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """End date.
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Domain(self):
        """Sender domain.
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ReceivingMailboxType(self):
        """Recipient address type, for example, gmail.com.
        :rtype: str
        """
        return self._ReceivingMailboxType

    @ReceivingMailboxType.setter
    def ReceivingMailboxType(self, ReceivingMailboxType):
        self._ReceivingMailboxType = ReceivingMailboxType


    def _deserialize(self, params):
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Domain = params.get("Domain")
        self._ReceivingMailboxType = params.get("ReceivingMailboxType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetStatisticsReportResponse(AbstractModel):
    """GetStatisticsReport response structure.

    """

    def __init__(self):
        r"""
        :param _DailyVolumes: Daily email sending statistics.
        :type DailyVolumes: list of Volume
        :param _OverallVolume: Overall email sending statistics.
        :type OverallVolume: :class:`tencentcloud.ses.v20201002.models.Volume`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._DailyVolumes = None
        self._OverallVolume = None
        self._RequestId = None

    @property
    def DailyVolumes(self):
        """Daily email sending statistics.
        :rtype: list of Volume
        """
        return self._DailyVolumes

    @DailyVolumes.setter
    def DailyVolumes(self, DailyVolumes):
        self._DailyVolumes = DailyVolumes

    @property
    def OverallVolume(self):
        """Overall email sending statistics.
        :rtype: :class:`tencentcloud.ses.v20201002.models.Volume`
        """
        return self._OverallVolume

    @OverallVolume.setter
    def OverallVolume(self, OverallVolume):
        self._OverallVolume = OverallVolume

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DailyVolumes") is not None:
            self._DailyVolumes = []
            for item in params.get("DailyVolumes"):
                obj = Volume()
                obj._deserialize(item)
                self._DailyVolumes.append(obj)
        if params.get("OverallVolume") is not None:
            self._OverallVolume = Volume()
            self._OverallVolume._deserialize(params.get("OverallVolume"))
        self._RequestId = params.get("RequestId")


class ListBlackEmailAddressRequest(AbstractModel):
    """ListBlackEmailAddress request structure.

    """

    def __init__(self):
        r"""
        :param _StartDate: Start date in the format of `YYYY-MM-DD`
        :type StartDate: str
        :param _EndDate: End date in the format of `YYYY-MM-DD`
        :type EndDate: str
        :param _Limit: Common parameter. It must be used with `Offset`.
        :type Limit: int
        :param _Offset: Common parameter. It must be used with `Limit`. Maximum value of `Limit`: `100`.
        :type Offset: int
        :param _EmailAddress: You can specify an email address to query.
        :type EmailAddress: str
        :param _TaskID: You can specify a task ID to query.
        :type TaskID: str
        """
        self._StartDate = None
        self._EndDate = None
        self._Limit = None
        self._Offset = None
        self._EmailAddress = None
        self._TaskID = None

    @property
    def StartDate(self):
        """Start date in the format of `YYYY-MM-DD`
        :rtype: str
        """
        return self._StartDate

    @StartDate.setter
    def StartDate(self, StartDate):
        self._StartDate = StartDate

    @property
    def EndDate(self):
        """End date in the format of `YYYY-MM-DD`
        :rtype: str
        """
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Limit(self):
        """Common parameter. It must be used with `Offset`.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Common parameter. It must be used with `Limit`. Maximum value of `Limit`: `100`.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EmailAddress(self):
        """You can specify an email address to query.
        :rtype: str
        """
        return self._EmailAddress

    @EmailAddress.setter
    def EmailAddress(self, EmailAddress):
        self._EmailAddress = EmailAddress

    @property
    def TaskID(self):
        """You can specify a task ID to query.
        :rtype: str
        """
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID


    def _deserialize(self, params):
        self._StartDate = params.get("StartDate")
        self._EndDate = params.get("EndDate")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EmailAddress = params.get("EmailAddress")
        self._TaskID = params.get("TaskID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListBlackEmailAddressResponse(AbstractModel):
    """ListBlackEmailAddress response structure.

    """

    def __init__(self):
        r"""
        :param _BlackList: List of blocklisted addresses.
        :type BlackList: list of BlackEmailAddress
        :param _TotalCount: Total number of blocklisted addresses.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._BlackList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def BlackList(self):
        """List of blocklisted addresses.
        :rtype: list of BlackEmailAddress
        """
        return self._BlackList

    @BlackList.setter
    def BlackList(self, BlackList):
        self._BlackList = BlackList

    @property
    def TotalCount(self):
        """Total number of blocklisted addresses.
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BlackList") is not None:
            self._BlackList = []
            for item in params.get("BlackList"):
                obj = BlackEmailAddress()
                obj._deserialize(item)
                self._BlackList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListEmailAddressRequest(AbstractModel):
    """ListEmailAddress request structure.

    """


class ListEmailAddressResponse(AbstractModel):
    """ListEmailAddress response structure.

    """

    def __init__(self):
        r"""
        :param _EmailSenders: Details of sender addresses.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type EmailSenders: list of EmailSender
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EmailSenders = None
        self._RequestId = None

    @property
    def EmailSenders(self):
        """Details of sender addresses.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: list of EmailSender
        """
        return self._EmailSenders

    @EmailSenders.setter
    def EmailSenders(self, EmailSenders):
        self._EmailSenders = EmailSenders

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EmailSenders") is not None:
            self._EmailSenders = []
            for item in params.get("EmailSenders"):
                obj = EmailSender()
                obj._deserialize(item)
                self._EmailSenders.append(obj)
        self._RequestId = params.get("RequestId")


class ListEmailIdentitiesRequest(AbstractModel):
    """ListEmailIdentities request structure.

    """


class ListEmailIdentitiesResponse(AbstractModel):
    """ListEmailIdentities response structure.

    """

    def __init__(self):
        r"""
        :param _EmailIdentities: List of sender domains.
        :type EmailIdentities: list of EmailIdentity
        :param _MaxReputationLevel: Maximum reputation level
        :type MaxReputationLevel: int
        :param _MaxDailyQuota: Maximum number of emails sent per domain name
        :type MaxDailyQuota: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EmailIdentities = None
        self._MaxReputationLevel = None
        self._MaxDailyQuota = None
        self._RequestId = None

    @property
    def EmailIdentities(self):
        """List of sender domains.
        :rtype: list of EmailIdentity
        """
        return self._EmailIdentities

    @EmailIdentities.setter
    def EmailIdentities(self, EmailIdentities):
        self._EmailIdentities = EmailIdentities

    @property
    def MaxReputationLevel(self):
        """Maximum reputation level
        :rtype: int
        """
        return self._MaxReputationLevel

    @MaxReputationLevel.setter
    def MaxReputationLevel(self, MaxReputationLevel):
        self._MaxReputationLevel = MaxReputationLevel

    @property
    def MaxDailyQuota(self):
        """Maximum number of emails sent per domain name
        :rtype: int
        """
        return self._MaxDailyQuota

    @MaxDailyQuota.setter
    def MaxDailyQuota(self, MaxDailyQuota):
        self._MaxDailyQuota = MaxDailyQuota

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EmailIdentities") is not None:
            self._EmailIdentities = []
            for item in params.get("EmailIdentities"):
                obj = EmailIdentity()
                obj._deserialize(item)
                self._EmailIdentities.append(obj)
        self._MaxReputationLevel = params.get("MaxReputationLevel")
        self._MaxDailyQuota = params.get("MaxDailyQuota")
        self._RequestId = params.get("RequestId")


class ListEmailTemplatesRequest(AbstractModel):
    """ListEmailTemplates request structure.

    """

    def __init__(self):
        r"""
        :param _Limit: Number of templates to get. This parameter is used for pagination.
        :type Limit: int
        :param _Offset: Template offset to get. This parameter is used for pagination.
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        """Number of templates to get. This parameter is used for pagination.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """Template offset to get. This parameter is used for pagination.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListEmailTemplatesResponse(AbstractModel):
    """ListEmailTemplates response structure.

    """

    def __init__(self):
        r"""
        :param _TemplatesMetadata: List of email templates.
        :type TemplatesMetadata: list of TemplatesMetadata
        :param _TotalCount: Total number of templates
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TemplatesMetadata = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TemplatesMetadata(self):
        """List of email templates.
        :rtype: list of TemplatesMetadata
        """
        return self._TemplatesMetadata

    @TemplatesMetadata.setter
    def TemplatesMetadata(self, TemplatesMetadata):
        self._TemplatesMetadata = TemplatesMetadata

    @property
    def TotalCount(self):
        """Total number of templates
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TemplatesMetadata") is not None:
            self._TemplatesMetadata = []
            for item in params.get("TemplatesMetadata"):
                obj = TemplatesMetadata()
                obj._deserialize(item)
                self._TemplatesMetadata.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListReceiversRequest(AbstractModel):
    """ListReceivers request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset, starting from 0. The value is an integer.
        :type Offset: int
        :param _Limit: Number of records to query. The value is an integer not exceeding 100.
        :type Limit: int
        :param _Status: Group status (`1`: to be uploaded; `2` uploading; `3` uploaded). To query groups in all states, do not pass in this parameter.
        :type Status: int
        :param _KeyWord: Group name keyword for fuzzy query
        :type KeyWord: str
        """
        self._Offset = None
        self._Limit = None
        self._Status = None
        self._KeyWord = None

    @property
    def Offset(self):
        """Offset, starting from 0. The value is an integer.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of records to query. The value is an integer not exceeding 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Status(self):
        """Group status (`1`: to be uploaded; `2` uploading; `3` uploaded). To query groups in all states, do not pass in this parameter.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def KeyWord(self):
        """Group name keyword for fuzzy query
        :rtype: str
        """
        return self._KeyWord

    @KeyWord.setter
    def KeyWord(self, KeyWord):
        self._KeyWord = KeyWord


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Status = params.get("Status")
        self._KeyWord = params.get("KeyWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListReceiversResponse(AbstractModel):
    """ListReceivers response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _Data: Data record
        :type Data: list of ReceiverData
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        """Data record
        :rtype: list of ReceiverData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ReceiverData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListSendTasksRequest(AbstractModel):
    """ListSendTasks request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset, starting from 0. The value is an integer. `0` means to skip 0 entries.
        :type Offset: int
        :param _Limit: Number of records to query. The value is an integer not exceeding 100.
        :type Limit: int
        :param _Status: Task status. `1`: to start; `5`: sending; `6`: sending suspended today; `7`: sending error; `10`: sent. To query tasks in all states, do not pass in this parameter.
        :type Status: int
        :param _ReceiverId: Recipient group ID
        :type ReceiverId: int
        :param _TaskType: Task type. `1`: immediate; `2`: scheduled; `3`: recurring. To query tasks of all types, do not pass in this parameter.
        :type TaskType: int
        """
        self._Offset = None
        self._Limit = None
        self._Status = None
        self._ReceiverId = None
        self._TaskType = None

    @property
    def Offset(self):
        """Offset, starting from 0. The value is an integer. `0` means to skip 0 entries.
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """Number of records to query. The value is an integer not exceeding 100.
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Status(self):
        """Task status. `1`: to start; `5`: sending; `6`: sending suspended today; `7`: sending error; `10`: sent. To query tasks in all states, do not pass in this parameter.
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ReceiverId(self):
        """Recipient group ID
        :rtype: int
        """
        return self._ReceiverId

    @ReceiverId.setter
    def ReceiverId(self, ReceiverId):
        self._ReceiverId = ReceiverId

    @property
    def TaskType(self):
        """Task type. `1`: immediate; `2`: scheduled; `3`: recurring. To query tasks of all types, do not pass in this parameter.
        :rtype: int
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Status = params.get("Status")
        self._ReceiverId = params.get("ReceiverId")
        self._TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSendTasksResponse(AbstractModel):
    """ListSendTasks response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _Data: Data record
        :type Data: list of SendTaskData
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """Total number
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        """Data record
        :rtype: list of SendTaskData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = SendTaskData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ReceiverData(AbstractModel):
    """Recipient group data type

    """

    def __init__(self):
        r"""
        :param _ReceiverId: Recipient group ID
        :type ReceiverId: int
        :param _ReceiversName: Recipient group name
        :type ReceiversName: str
        :param _Count: Total number of recipient email addresses
        :type Count: int
        :param _Desc: Recipient group description
Note: This field may return `null`, indicating that no valid value can be found.
        :type Desc: str
        :param _ReceiversStatus: Group status (`1`: to be uploaded; `2` uploading; `3` uploaded)
Note: This field may return `null`, indicating that no valid value can be found.
        :type ReceiversStatus: int
        :param _CreateTime: Creation time, such as 2021-09-28 16:40:35
        :type CreateTime: str
        """
        self._ReceiverId = None
        self._ReceiversName = None
        self._Count = None
        self._Desc = None
        self._ReceiversStatus = None
        self._CreateTime = None

    @property
    def ReceiverId(self):
        """Recipient group ID
        :rtype: int
        """
        return self._ReceiverId

    @ReceiverId.setter
    def ReceiverId(self, ReceiverId):
        self._ReceiverId = ReceiverId

    @property
    def ReceiversName(self):
        """Recipient group name
        :rtype: str
        """
        return self._ReceiversName

    @ReceiversName.setter
    def ReceiversName(self, ReceiversName):
        self._ReceiversName = ReceiversName

    @property
    def Count(self):
        """Total number of recipient email addresses
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Desc(self):
        """Recipient group description
Note: This field may return `null`, indicating that no valid value can be found.
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def ReceiversStatus(self):
        """Group status (`1`: to be uploaded; `2` uploading; `3` uploaded)
Note: This field may return `null`, indicating that no valid value can be found.
        :rtype: int
        """
        return self._ReceiversStatus

    @ReceiversStatus.setter
    def ReceiversStatus(self, ReceiversStatus):
        self._ReceiversStatus = ReceiversStatus

    @property
    def CreateTime(self):
        """Creation time, such as 2021-09-28 16:40:35
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ReceiverId = params.get("ReceiverId")
        self._ReceiversName = params.get("ReceiversName")
        self._Count = params.get("Count")
        self._Desc = params.get("Desc")
        self._ReceiversStatus = params.get("ReceiversStatus")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendEmailRequest(AbstractModel):
    """SendEmail request structure.

    """

    def __init__(self):
        r"""
        :param _FromEmailAddress: Sender address. Enter a sender address, for example, noreply@mail.qcloud.com.
To display the sender name, enter the address in the following format: 
Sender <email address>
        :type FromEmailAddress: str
        :param _Destination: Recipient email addresses. You can send an email to up to 50 recipients at a time. Note: the email content will display all recipient addresses. To send one-to-one emails to several recipients, please call the API multiple times to send the emails.
        :type Destination: list of str
        :param _Subject: Email subject.
        :type Subject: str
        :param _ReplyToAddresses: Reply-to address. You can enter a valid personal email address that can receive emails. If this parameter is left empty, reply emails will fail to be sent.
        :type ReplyToAddresses: str
        :param _Cc: 
        :type Cc: list of str
        :param _Bcc: 
        :type Bcc: list of str
        :param _Template: Template parameters for template-based sending. As `Simple` has been disused, `Template` is required.
        :type Template: :class:`tencentcloud.ses.v20201002.models.Template`
        :param _Simple: Disused
        :type Simple: :class:`tencentcloud.ses.v20201002.models.Simple`
        :param _Attachments: Parameters for the attachments to be sent. The TencentCloud API supports a request packet of up to 8 MB in size, and the size of the attachment content will increase by 1.5 times after Base64 encoding. Therefore, you need to keep the total size of all attachments below 4 MB. If the entire request exceeds 8 MB, the API will return an error.
        :type Attachments: list of Attachment
        :param _Unsubscribe: Unsubscribe link option. `0`: Do not add unsubscribe link; `1`: English `2`: Simplified Chinese; `3`: Traditional Chinese; `4`: Spanish; `5`: French; `6`: German; `7`: Japanese; `8`: Korean; `9`: Arabic; `10`: Thai
        :type Unsubscribe: str
        :param _TriggerType: Email triggering type. `0` (default): non-trigger-based, suitable for marketing emails and non-immediate emails; `1`: trigger-based, suitable for immediate emails such as emails containing verification codes. If the size of an email exceeds a specified value, the system will automatically choose the non-trigger-based type.
        :type TriggerType: int
        """
        self._FromEmailAddress = None
        self._Destination = None
        self._Subject = None
        self._ReplyToAddresses = None
        self._Cc = None
        self._Bcc = None
        self._Template = None
        self._Simple = None
        self._Attachments = None
        self._Unsubscribe = None
        self._TriggerType = None

    @property
    def FromEmailAddress(self):
        """Sender address. Enter a sender address, for example, noreply@mail.qcloud.com.
To display the sender name, enter the address in the following format: 
Sender <email address>
        :rtype: str
        """
        return self._FromEmailAddress

    @FromEmailAddress.setter
    def FromEmailAddress(self, FromEmailAddress):
        self._FromEmailAddress = FromEmailAddress

    @property
    def Destination(self):
        """Recipient email addresses. You can send an email to up to 50 recipients at a time. Note: the email content will display all recipient addresses. To send one-to-one emails to several recipients, please call the API multiple times to send the emails.
        :rtype: list of str
        """
        return self._Destination

    @Destination.setter
    def Destination(self, Destination):
        self._Destination = Destination

    @property
    def Subject(self):
        """Email subject.
        :rtype: str
        """
        return self._Subject

    @Subject.setter
    def Subject(self, Subject):
        self._Subject = Subject

    @property
    def ReplyToAddresses(self):
        """Reply-to address. You can enter a valid personal email address that can receive emails. If this parameter is left empty, reply emails will fail to be sent.
        :rtype: str
        """
        return self._ReplyToAddresses

    @ReplyToAddresses.setter
    def ReplyToAddresses(self, ReplyToAddresses):
        self._ReplyToAddresses = ReplyToAddresses

    @property
    def Cc(self):
        """
        :rtype: list of str
        """
        return self._Cc

    @Cc.setter
    def Cc(self, Cc):
        self._Cc = Cc

    @property
    def Bcc(self):
        """
        :rtype: list of str
        """
        return self._Bcc

    @Bcc.setter
    def Bcc(self, Bcc):
        self._Bcc = Bcc

    @property
    def Template(self):
        """Template parameters for template-based sending. As `Simple` has been disused, `Template` is required.
        :rtype: :class:`tencentcloud.ses.v20201002.models.Template`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def Simple(self):
        """Disused
        :rtype: :class:`tencentcloud.ses.v20201002.models.Simple`
        """
        return self._Simple

    @Simple.setter
    def Simple(self, Simple):
        self._Simple = Simple

    @property
    def Attachments(self):
        """Parameters for the attachments to be sent. The TencentCloud API supports a request packet of up to 8 MB in size, and the size of the attachment content will increase by 1.5 times after Base64 encoding. Therefore, you need to keep the total size of all attachments below 4 MB. If the entire request exceeds 8 MB, the API will return an error.
        :rtype: list of Attachment
        """
        return self._Attachments

    @Attachments.setter
    def Attachments(self, Attachments):
        self._Attachments = Attachments

    @property
    def Unsubscribe(self):
        """Unsubscribe link option. `0`: Do not add unsubscribe link; `1`: English `2`: Simplified Chinese; `3`: Traditional Chinese; `4`: Spanish; `5`: French; `6`: German; `7`: Japanese; `8`: Korean; `9`: Arabic; `10`: Thai
        :rtype: str
        """
        return self._Unsubscribe

    @Unsubscribe.setter
    def Unsubscribe(self, Unsubscribe):
        self._Unsubscribe = Unsubscribe

    @property
    def TriggerType(self):
        """Email triggering type. `0` (default): non-trigger-based, suitable for marketing emails and non-immediate emails; `1`: trigger-based, suitable for immediate emails such as emails containing verification codes. If the size of an email exceeds a specified value, the system will automatically choose the non-trigger-based type.
        :rtype: int
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType


    def _deserialize(self, params):
        self._FromEmailAddress = params.get("FromEmailAddress")
        self._Destination = params.get("Destination")
        self._Subject = params.get("Subject")
        self._ReplyToAddresses = params.get("ReplyToAddresses")
        self._Cc = params.get("Cc")
        self._Bcc = params.get("Bcc")
        if params.get("Template") is not None:
            self._Template = Template()
            self._Template._deserialize(params.get("Template"))
        if params.get("Simple") is not None:
            self._Simple = Simple()
            self._Simple._deserialize(params.get("Simple"))
        if params.get("Attachments") is not None:
            self._Attachments = []
            for item in params.get("Attachments"):
                obj = Attachment()
                obj._deserialize(item)
                self._Attachments.append(obj)
        self._Unsubscribe = params.get("Unsubscribe")
        self._TriggerType = params.get("TriggerType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendEmailResponse(AbstractModel):
    """SendEmail response structure.

    """

    def __init__(self):
        r"""
        :param _MessageId: Unique ID generated when receiving the message
        :type MessageId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MessageId = None
        self._RequestId = None

    @property
    def MessageId(self):
        """Unique ID generated when receiving the message
        :rtype: str
        """
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MessageId = params.get("MessageId")
        self._RequestId = params.get("RequestId")


class SendEmailStatus(AbstractModel):
    """Describes the email sending status

    """

    def __init__(self):
        r"""
        :param _MessageId: The `MessageId` field returned by the `SendEmail` API
        :type MessageId: str
        :param _ToEmailAddress: Recipient email address
        :type ToEmailAddress: str
        :param _FromEmailAddress: Sender email address
        :type FromEmailAddress: str
        :param _SendStatus: Tencent Cloud processing status
0: Successful.
1001: Internal system exception.
1002: Internal system exception.
1003: Internal system exception.
1003: Internal system exception.
1004: Email sending timed out.
1005: Internal system exception.
1006: You have sent too many emails to the same address in a short period.
1007: The email address is in the blocklist.
1008: The sender domain is rejected by the recipient.
1009: Internal system exception.
1010: The daily email sending limit is exceeded.
1011: You have no permission to send custom content. Use a template.
1013: The sender domain is unsubscribed from by the recipient.
2001: No results were found.
3007: The template ID is invalid or the template is unavailable.
3008: The sender domain is temporarily blocked by the recipient domain.
3009: You have no permission to use this template.
3010: The format of the `TemplateData` field is incorrect. 
3014: The email cannot be sent because the sender domain is not verified.
3020: The recipient email address is in the blocklist.
3024: Failed to precheck the email address format.
3030: Email sending is restricted temporarily due to a high bounce rate.
3033: The account has insufficient balance or overdue payment.
        :type SendStatus: int
        :param _DeliverStatus: Recipient processing status
0: Tencent Cloud has accepted the request and added it to the send queue.
1: The email is delivered successfully. `DeliverTime` indicates the time when the email is delivered successfully.
2: The email is discarded. `DeliverMessage` indicates the reason for discarding.
3: The recipient's ESP rejects the email, probably because the email address does not exist or due to other reasons.
8: The email is delayed by the ESP. `DeliverMessage` indicates the reason for delay.
        :type DeliverStatus: int
        :param _DeliverMessage: Description of the recipient processing status
        :type DeliverMessage: str
        :param _RequestTime: Timestamp when the request arrives at Tencent Cloud
        :type RequestTime: int
        :param _DeliverTime: Timestamp when Tencent Cloud delivers the email
        :type DeliverTime: int
        :param _UserOpened: Whether the recipient has opened the email
        :type UserOpened: bool
        :param _UserClicked: Whether the recipient has clicked the links in the email
        :type UserClicked: bool
        :param _UserUnsubscribed: Whether the recipient has unsubscribed from the email sent by the sender
        :type UserUnsubscribed: bool
        :param _UserComplainted: Whether the recipient has reported the sender
        :type UserComplainted: bool
        """
        self._MessageId = None
        self._ToEmailAddress = None
        self._FromEmailAddress = None
        self._SendStatus = None
        self._DeliverStatus = None
        self._DeliverMessage = None
        self._RequestTime = None
        self._DeliverTime = None
        self._UserOpened = None
        self._UserClicked = None
        self._UserUnsubscribed = None
        self._UserComplainted = None

    @property
    def MessageId(self):
        """The `MessageId` field returned by the `SendEmail` API
        :rtype: str
        """
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

    @property
    def ToEmailAddress(self):
        """Recipient email address
        :rtype: str
        """
        return self._ToEmailAddress

    @ToEmailAddress.setter
    def ToEmailAddress(self, ToEmailAddress):
        self._ToEmailAddress = ToEmailAddress

    @property
    def FromEmailAddress(self):
        """Sender email address
        :rtype: str
        """
        return self._FromEmailAddress

    @FromEmailAddress.setter
    def FromEmailAddress(self, FromEmailAddress):
        self._FromEmailAddress = FromEmailAddress

    @property
    def SendStatus(self):
        """Tencent Cloud processing status
0: Successful.
1001: Internal system exception.
1002: Internal system exception.
1003: Internal system exception.
1003: Internal system exception.
1004: Email sending timed out.
1005: Internal system exception.
1006: You have sent too many emails to the same address in a short period.
1007: The email address is in the blocklist.
1008: The sender domain is rejected by the recipient.
1009: Internal system exception.
1010: The daily email sending limit is exceeded.
1011: You have no permission to send custom content. Use a template.
1013: The sender domain is unsubscribed from by the recipient.
2001: No results were found.
3007: The template ID is invalid or the template is unavailable.
3008: The sender domain is temporarily blocked by the recipient domain.
3009: You have no permission to use this template.
3010: The format of the `TemplateData` field is incorrect. 
3014: The email cannot be sent because the sender domain is not verified.
3020: The recipient email address is in the blocklist.
3024: Failed to precheck the email address format.
3030: Email sending is restricted temporarily due to a high bounce rate.
3033: The account has insufficient balance or overdue payment.
        :rtype: int
        """
        return self._SendStatus

    @SendStatus.setter
    def SendStatus(self, SendStatus):
        self._SendStatus = SendStatus

    @property
    def DeliverStatus(self):
        """Recipient processing status
0: Tencent Cloud has accepted the request and added it to the send queue.
1: The email is delivered successfully. `DeliverTime` indicates the time when the email is delivered successfully.
2: The email is discarded. `DeliverMessage` indicates the reason for discarding.
3: The recipient's ESP rejects the email, probably because the email address does not exist or due to other reasons.
8: The email is delayed by the ESP. `DeliverMessage` indicates the reason for delay.
        :rtype: int
        """
        return self._DeliverStatus

    @DeliverStatus.setter
    def DeliverStatus(self, DeliverStatus):
        self._DeliverStatus = DeliverStatus

    @property
    def DeliverMessage(self):
        """Description of the recipient processing status
        :rtype: str
        """
        return self._DeliverMessage

    @DeliverMessage.setter
    def DeliverMessage(self, DeliverMessage):
        self._DeliverMessage = DeliverMessage

    @property
    def RequestTime(self):
        """Timestamp when the request arrives at Tencent Cloud
        :rtype: int
        """
        return self._RequestTime

    @RequestTime.setter
    def RequestTime(self, RequestTime):
        self._RequestTime = RequestTime

    @property
    def DeliverTime(self):
        """Timestamp when Tencent Cloud delivers the email
        :rtype: int
        """
        return self._DeliverTime

    @DeliverTime.setter
    def DeliverTime(self, DeliverTime):
        self._DeliverTime = DeliverTime

    @property
    def UserOpened(self):
        """Whether the recipient has opened the email
        :rtype: bool
        """
        return self._UserOpened

    @UserOpened.setter
    def UserOpened(self, UserOpened):
        self._UserOpened = UserOpened

    @property
    def UserClicked(self):
        """Whether the recipient has clicked the links in the email
        :rtype: bool
        """
        return self._UserClicked

    @UserClicked.setter
    def UserClicked(self, UserClicked):
        self._UserClicked = UserClicked

    @property
    def UserUnsubscribed(self):
        """Whether the recipient has unsubscribed from the email sent by the sender
        :rtype: bool
        """
        return self._UserUnsubscribed

    @UserUnsubscribed.setter
    def UserUnsubscribed(self, UserUnsubscribed):
        self._UserUnsubscribed = UserUnsubscribed

    @property
    def UserComplainted(self):
        """Whether the recipient has reported the sender
        :rtype: bool
        """
        return self._UserComplainted

    @UserComplainted.setter
    def UserComplainted(self, UserComplainted):
        self._UserComplainted = UserComplainted


    def _deserialize(self, params):
        self._MessageId = params.get("MessageId")
        self._ToEmailAddress = params.get("ToEmailAddress")
        self._FromEmailAddress = params.get("FromEmailAddress")
        self._SendStatus = params.get("SendStatus")
        self._DeliverStatus = params.get("DeliverStatus")
        self._DeliverMessage = params.get("DeliverMessage")
        self._RequestTime = params.get("RequestTime")
        self._DeliverTime = params.get("DeliverTime")
        self._UserOpened = params.get("UserOpened")
        self._UserClicked = params.get("UserClicked")
        self._UserUnsubscribed = params.get("UserUnsubscribed")
        self._UserComplainted = params.get("UserComplainted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendTaskData(AbstractModel):
    """Email sending task data

    """

    def __init__(self):
        r"""
        :param _TaskId: Task ID
        :type TaskId: int
        :param _FromEmailAddress: Sender address
        :type FromEmailAddress: str
        :param _ReceiverId: Recipient group ID
        :type ReceiverId: int
        :param _TaskStatus: Task status. `1`: to start; `5`: sending; `6`: sending suspended today; `7`: sending error; `10`: sent
        :type TaskStatus: int
        :param _TaskType: Task type. `1`: immediate; `2`: scheduled; `3`: recurring
        :type TaskType: int
        :param _RequestCount: Number of emails requested to be sent
        :type RequestCount: int
        :param _SendCount: Number of emails sent
        :type SendCount: int
        :param _CacheCount: Number of emails cached
        :type CacheCount: int
        :param _CreateTime: Task creation time
        :type CreateTime: str
        :param _UpdateTime: Task update time
        :type UpdateTime: str
        :param _Subject: Email subject
        :type Subject: str
        :param _Template: Template and template data
Note: This field may return `null`, indicating that no valid value can be found.
        :type Template: :class:`tencentcloud.ses.v20201002.models.Template`
        :param _CycleParam: Parameters of a recurring task
Note: This field may return `null`, indicating that no valid value can be found.
        :type CycleParam: :class:`tencentcloud.ses.v20201002.models.CycleEmailParam`
        :param _TimedParam: Parameters of a scheduled task
Note: This field may return `null`, indicating that no valid value can be found.
        :type TimedParam: :class:`tencentcloud.ses.v20201002.models.TimedEmailParam`
        :param _ErrMsg: Task exception information
Note: This field may return `null`, indicating that no valid value can be found.
        :type ErrMsg: str
        :param _ReceiversName: Recipient group name
        :type ReceiversName: str
        """
        self._TaskId = None
        self._FromEmailAddress = None
        self._ReceiverId = None
        self._TaskStatus = None
        self._TaskType = None
        self._RequestCount = None
        self._SendCount = None
        self._CacheCount = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Subject = None
        self._Template = None
        self._CycleParam = None
        self._TimedParam = None
        self._ErrMsg = None
        self._ReceiversName = None

    @property
    def TaskId(self):
        """Task ID
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def FromEmailAddress(self):
        """Sender address
        :rtype: str
        """
        return self._FromEmailAddress

    @FromEmailAddress.setter
    def FromEmailAddress(self, FromEmailAddress):
        self._FromEmailAddress = FromEmailAddress

    @property
    def ReceiverId(self):
        """Recipient group ID
        :rtype: int
        """
        return self._ReceiverId

    @ReceiverId.setter
    def ReceiverId(self, ReceiverId):
        self._ReceiverId = ReceiverId

    @property
    def TaskStatus(self):
        """Task status. `1`: to start; `5`: sending; `6`: sending suspended today; `7`: sending error; `10`: sent
        :rtype: int
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def TaskType(self):
        """Task type. `1`: immediate; `2`: scheduled; `3`: recurring
        :rtype: int
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def RequestCount(self):
        """Number of emails requested to be sent
        :rtype: int
        """
        return self._RequestCount

    @RequestCount.setter
    def RequestCount(self, RequestCount):
        self._RequestCount = RequestCount

    @property
    def SendCount(self):
        """Number of emails sent
        :rtype: int
        """
        return self._SendCount

    @SendCount.setter
    def SendCount(self, SendCount):
        self._SendCount = SendCount

    @property
    def CacheCount(self):
        """Number of emails cached
        :rtype: int
        """
        return self._CacheCount

    @CacheCount.setter
    def CacheCount(self, CacheCount):
        self._CacheCount = CacheCount

    @property
    def CreateTime(self):
        """Task creation time
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """Task update time
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Subject(self):
        """Email subject
        :rtype: str
        """
        return self._Subject

    @Subject.setter
    def Subject(self, Subject):
        self._Subject = Subject

    @property
    def Template(self):
        """Template and template data
Note: This field may return `null`, indicating that no valid value can be found.
        :rtype: :class:`tencentcloud.ses.v20201002.models.Template`
        """
        return self._Template

    @Template.setter
    def Template(self, Template):
        self._Template = Template

    @property
    def CycleParam(self):
        """Parameters of a recurring task
Note: This field may return `null`, indicating that no valid value can be found.
        :rtype: :class:`tencentcloud.ses.v20201002.models.CycleEmailParam`
        """
        return self._CycleParam

    @CycleParam.setter
    def CycleParam(self, CycleParam):
        self._CycleParam = CycleParam

    @property
    def TimedParam(self):
        """Parameters of a scheduled task
Note: This field may return `null`, indicating that no valid value can be found.
        :rtype: :class:`tencentcloud.ses.v20201002.models.TimedEmailParam`
        """
        return self._TimedParam

    @TimedParam.setter
    def TimedParam(self, TimedParam):
        self._TimedParam = TimedParam

    @property
    def ErrMsg(self):
        """Task exception information
Note: This field may return `null`, indicating that no valid value can be found.
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def ReceiversName(self):
        """Recipient group name
        :rtype: str
        """
        return self._ReceiversName

    @ReceiversName.setter
    def ReceiversName(self, ReceiversName):
        self._ReceiversName = ReceiversName


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._FromEmailAddress = params.get("FromEmailAddress")
        self._ReceiverId = params.get("ReceiverId")
        self._TaskStatus = params.get("TaskStatus")
        self._TaskType = params.get("TaskType")
        self._RequestCount = params.get("RequestCount")
        self._SendCount = params.get("SendCount")
        self._CacheCount = params.get("CacheCount")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Subject = params.get("Subject")
        if params.get("Template") is not None:
            self._Template = Template()
            self._Template._deserialize(params.get("Template"))
        if params.get("CycleParam") is not None:
            self._CycleParam = CycleEmailParam()
            self._CycleParam._deserialize(params.get("CycleParam"))
        if params.get("TimedParam") is not None:
            self._TimedParam = TimedEmailParam()
            self._TimedParam._deserialize(params.get("TimedParam"))
        self._ErrMsg = params.get("ErrMsg")
        self._ReceiversName = params.get("ReceiversName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Simple(AbstractModel):
    """Email content, which can be plain text (TEXT), pure code (HTML), or a combination of TEXT and HTML (recommended).

    """

    def __init__(self):
        r"""
        :param _Html: HTML code after base64 encoding. To ensure correct display, this parameter should include all code information and cannot contain external CSS.
        :type Html: str
        :param _Text: Plain text content after base64 encoding. If HTML is not involved, the plain text will be displayed in the email. Otherwise, this parameter represents the plain text style of the email.
        :type Text: str
        """
        self._Html = None
        self._Text = None

    @property
    def Html(self):
        """HTML code after base64 encoding. To ensure correct display, this parameter should include all code information and cannot contain external CSS.
        :rtype: str
        """
        return self._Html

    @Html.setter
    def Html(self, Html):
        self._Html = Html

    @property
    def Text(self):
        """Plain text content after base64 encoding. If HTML is not involved, the plain text will be displayed in the email. Otherwise, this parameter represents the plain text style of the email.
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Html = params.get("Html")
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Template(AbstractModel):
    """Template information, including template ID, template variable parameters, etc.

    """

    def __init__(self):
        r"""
        :param _TemplateID: Template ID. If you don’t have any template, please create one.
        :type TemplateID: int
        :param _TemplateData: Variable parameters in the template. Please use `json.dump` to format the JSON object into a string type. The object is a set of key-value pairs. Each key denotes a variable, which is represented by {{key}}. The key will be replaced with the corresponding value (represented by {{value}}) when sending the email.
Note: The parameter value cannot be data of a complex type such as HTML.
Example: {"name":"xxx","age":"xx"}
        :type TemplateData: str
        """
        self._TemplateID = None
        self._TemplateData = None

    @property
    def TemplateID(self):
        """Template ID. If you don’t have any template, please create one.
        :rtype: int
        """
        return self._TemplateID

    @TemplateID.setter
    def TemplateID(self, TemplateID):
        self._TemplateID = TemplateID

    @property
    def TemplateData(self):
        """Variable parameters in the template. Please use `json.dump` to format the JSON object into a string type. The object is a set of key-value pairs. Each key denotes a variable, which is represented by {{key}}. The key will be replaced with the corresponding value (represented by {{value}}) when sending the email.
Note: The parameter value cannot be data of a complex type such as HTML.
Example: {"name":"xxx","age":"xx"}
        :rtype: str
        """
        return self._TemplateData

    @TemplateData.setter
    def TemplateData(self, TemplateData):
        self._TemplateData = TemplateData


    def _deserialize(self, params):
        self._TemplateID = params.get("TemplateID")
        self._TemplateData = params.get("TemplateData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateContent(AbstractModel):
    """Template content, which must include at least one of TEXT and HTML. A combination of TEXT and HTML is recommended.

    """

    def __init__(self):
        r"""
        :param _Html: HTML code after base64 encoding.
        :type Html: str
        :param _Text: Text content after base64 encoding.
        :type Text: str
        """
        self._Html = None
        self._Text = None

    @property
    def Html(self):
        """HTML code after base64 encoding.
        :rtype: str
        """
        return self._Html

    @Html.setter
    def Html(self, Html):
        self._Html = Html

    @property
    def Text(self):
        """Text content after base64 encoding.
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Html = params.get("Html")
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplatesMetadata(AbstractModel):
    """Template list structure.

    """

    def __init__(self):
        r"""
        :param _CreatedTimestamp: Creation time.
        :type CreatedTimestamp: int
        :param _TemplateName: Template name.
        :type TemplateName: str
        :param _TemplateStatus: Template status. 1: under review; 0: approved; 2: rejected; other values: unavailable.
        :type TemplateStatus: int
        :param _TemplateID: Template ID.
        :type TemplateID: int
        :param _ReviewReason: Review reply
        :type ReviewReason: str
        """
        self._CreatedTimestamp = None
        self._TemplateName = None
        self._TemplateStatus = None
        self._TemplateID = None
        self._ReviewReason = None

    @property
    def CreatedTimestamp(self):
        """Creation time.
        :rtype: int
        """
        return self._CreatedTimestamp

    @CreatedTimestamp.setter
    def CreatedTimestamp(self, CreatedTimestamp):
        self._CreatedTimestamp = CreatedTimestamp

    @property
    def TemplateName(self):
        """Template name.
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateStatus(self):
        """Template status. 1: under review; 0: approved; 2: rejected; other values: unavailable.
        :rtype: int
        """
        return self._TemplateStatus

    @TemplateStatus.setter
    def TemplateStatus(self, TemplateStatus):
        self._TemplateStatus = TemplateStatus

    @property
    def TemplateID(self):
        """Template ID.
        :rtype: int
        """
        return self._TemplateID

    @TemplateID.setter
    def TemplateID(self, TemplateID):
        self._TemplateID = TemplateID

    @property
    def ReviewReason(self):
        """Review reply
        :rtype: str
        """
        return self._ReviewReason

    @ReviewReason.setter
    def ReviewReason(self, ReviewReason):
        self._ReviewReason = ReviewReason


    def _deserialize(self, params):
        self._CreatedTimestamp = params.get("CreatedTimestamp")
        self._TemplateName = params.get("TemplateName")
        self._TemplateStatus = params.get("TemplateStatus")
        self._TemplateID = params.get("TemplateID")
        self._ReviewReason = params.get("ReviewReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimedEmailParam(AbstractModel):
    """Time parameter required to create a scheduled sending task, such as the start time

    """

    def __init__(self):
        r"""
        :param _BeginTime: Start time of a scheduled sending task
        :type BeginTime: str
        """
        self._BeginTime = None

    @property
    def BeginTime(self):
        """Start time of a scheduled sending task
        :rtype: str
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime


    def _deserialize(self, params):
        self._BeginTime = params.get("BeginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEmailIdentityRequest(AbstractModel):
    """UpdateEmailIdentity request structure.

    """

    def __init__(self):
        r"""
        :param _EmailIdentity: Domain to be verified.
        :type EmailIdentity: str
        """
        self._EmailIdentity = None

    @property
    def EmailIdentity(self):
        """Domain to be verified.
        :rtype: str
        """
        return self._EmailIdentity

    @EmailIdentity.setter
    def EmailIdentity(self, EmailIdentity):
        self._EmailIdentity = EmailIdentity


    def _deserialize(self, params):
        self._EmailIdentity = params.get("EmailIdentity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEmailIdentityResponse(AbstractModel):
    """UpdateEmailIdentity response structure.

    """

    def __init__(self):
        r"""
        :param _IdentityType: Verification type. The value is fixed to `DOMAIN`.
        :type IdentityType: str
        :param _VerifiedForSendingStatus: Verification passed or not.
        :type VerifiedForSendingStatus: bool
        :param _Attributes: DNS information that needs to be configured.
        :type Attributes: list of DNSAttributes
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._IdentityType = None
        self._VerifiedForSendingStatus = None
        self._Attributes = None
        self._RequestId = None

    @property
    def IdentityType(self):
        """Verification type. The value is fixed to `DOMAIN`.
        :rtype: str
        """
        return self._IdentityType

    @IdentityType.setter
    def IdentityType(self, IdentityType):
        self._IdentityType = IdentityType

    @property
    def VerifiedForSendingStatus(self):
        """Verification passed or not.
        :rtype: bool
        """
        return self._VerifiedForSendingStatus

    @VerifiedForSendingStatus.setter
    def VerifiedForSendingStatus(self, VerifiedForSendingStatus):
        self._VerifiedForSendingStatus = VerifiedForSendingStatus

    @property
    def Attributes(self):
        """DNS information that needs to be configured.
        :rtype: list of DNSAttributes
        """
        return self._Attributes

    @Attributes.setter
    def Attributes(self, Attributes):
        self._Attributes = Attributes

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IdentityType = params.get("IdentityType")
        self._VerifiedForSendingStatus = params.get("VerifiedForSendingStatus")
        if params.get("Attributes") is not None:
            self._Attributes = []
            for item in params.get("Attributes"):
                obj = DNSAttributes()
                obj._deserialize(item)
                self._Attributes.append(obj)
        self._RequestId = params.get("RequestId")


class UpdateEmailSmtpPassWordRequest(AbstractModel):
    """UpdateEmailSmtpPassWord request structure.

    """

    def __init__(self):
        r"""
        :param _Password: SMTP password. Length limit: 64.
        :type Password: str
        :param _EmailAddress: Email address. Length limit: 128.
        :type EmailAddress: str
        """
        self._Password = None
        self._EmailAddress = None

    @property
    def Password(self):
        """SMTP password. Length limit: 64.
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def EmailAddress(self):
        """Email address. Length limit: 128.
        :rtype: str
        """
        return self._EmailAddress

    @EmailAddress.setter
    def EmailAddress(self, EmailAddress):
        self._EmailAddress = EmailAddress


    def _deserialize(self, params):
        self._Password = params.get("Password")
        self._EmailAddress = params.get("EmailAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEmailSmtpPassWordResponse(AbstractModel):
    """UpdateEmailSmtpPassWord response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateEmailTemplateRequest(AbstractModel):
    """UpdateEmailTemplate request structure.

    """

    def __init__(self):
        r"""
        :param _TemplateContent: Template content.
        :type TemplateContent: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        :param _TemplateID: Template ID.
        :type TemplateID: int
        :param _TemplateName: Template name
        :type TemplateName: str
        """
        self._TemplateContent = None
        self._TemplateID = None
        self._TemplateName = None

    @property
    def TemplateContent(self):
        """Template content.
        :rtype: :class:`tencentcloud.ses.v20201002.models.TemplateContent`
        """
        return self._TemplateContent

    @TemplateContent.setter
    def TemplateContent(self, TemplateContent):
        self._TemplateContent = TemplateContent

    @property
    def TemplateID(self):
        """Template ID.
        :rtype: int
        """
        return self._TemplateID

    @TemplateID.setter
    def TemplateID(self, TemplateID):
        self._TemplateID = TemplateID

    @property
    def TemplateName(self):
        """Template name
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName


    def _deserialize(self, params):
        if params.get("TemplateContent") is not None:
            self._TemplateContent = TemplateContent()
            self._TemplateContent._deserialize(params.get("TemplateContent"))
        self._TemplateID = params.get("TemplateID")
        self._TemplateName = params.get("TemplateName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEmailTemplateResponse(AbstractModel):
    """UpdateEmailTemplate response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Volume(AbstractModel):
    """Statistics structure.

    """

    def __init__(self):
        r"""
        :param _SendDate: Date
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SendDate: str
        :param _RequestCount: Number of email requests.
        :type RequestCount: int
        :param _AcceptedCount: Number of email requests accepted by Tencent Cloud.
        :type AcceptedCount: int
        :param _DeliveredCount: Number of delivered emails.
        :type DeliveredCount: int
        :param _OpenedCount: Number of users (deduplicated) who opened emails.
        :type OpenedCount: int
        :param _ClickedCount: Number of recipients who clicked on links in emails.
        :type ClickedCount: int
        :param _BounceCount: Number of bounced emails.
        :type BounceCount: int
        :param _UnsubscribeCount: Number of users who canceled subscriptions.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type UnsubscribeCount: int
        """
        self._SendDate = None
        self._RequestCount = None
        self._AcceptedCount = None
        self._DeliveredCount = None
        self._OpenedCount = None
        self._ClickedCount = None
        self._BounceCount = None
        self._UnsubscribeCount = None

    @property
    def SendDate(self):
        """Date
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: str
        """
        return self._SendDate

    @SendDate.setter
    def SendDate(self, SendDate):
        self._SendDate = SendDate

    @property
    def RequestCount(self):
        """Number of email requests.
        :rtype: int
        """
        return self._RequestCount

    @RequestCount.setter
    def RequestCount(self, RequestCount):
        self._RequestCount = RequestCount

    @property
    def AcceptedCount(self):
        """Number of email requests accepted by Tencent Cloud.
        :rtype: int
        """
        return self._AcceptedCount

    @AcceptedCount.setter
    def AcceptedCount(self, AcceptedCount):
        self._AcceptedCount = AcceptedCount

    @property
    def DeliveredCount(self):
        """Number of delivered emails.
        :rtype: int
        """
        return self._DeliveredCount

    @DeliveredCount.setter
    def DeliveredCount(self, DeliveredCount):
        self._DeliveredCount = DeliveredCount

    @property
    def OpenedCount(self):
        """Number of users (deduplicated) who opened emails.
        :rtype: int
        """
        return self._OpenedCount

    @OpenedCount.setter
    def OpenedCount(self, OpenedCount):
        self._OpenedCount = OpenedCount

    @property
    def ClickedCount(self):
        """Number of recipients who clicked on links in emails.
        :rtype: int
        """
        return self._ClickedCount

    @ClickedCount.setter
    def ClickedCount(self, ClickedCount):
        self._ClickedCount = ClickedCount

    @property
    def BounceCount(self):
        """Number of bounced emails.
        :rtype: int
        """
        return self._BounceCount

    @BounceCount.setter
    def BounceCount(self, BounceCount):
        self._BounceCount = BounceCount

    @property
    def UnsubscribeCount(self):
        """Number of users who canceled subscriptions.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :rtype: int
        """
        return self._UnsubscribeCount

    @UnsubscribeCount.setter
    def UnsubscribeCount(self, UnsubscribeCount):
        self._UnsubscribeCount = UnsubscribeCount


    def _deserialize(self, params):
        self._SendDate = params.get("SendDate")
        self._RequestCount = params.get("RequestCount")
        self._AcceptedCount = params.get("AcceptedCount")
        self._DeliveredCount = params.get("DeliveredCount")
        self._OpenedCount = params.get("OpenedCount")
        self._ClickedCount = params.get("ClickedCount")
        self._BounceCount = params.get("BounceCount")
        self._UnsubscribeCount = params.get("UnsubscribeCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        