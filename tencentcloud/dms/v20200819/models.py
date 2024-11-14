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


class SendEmailRequest(AbstractModel):
    """SendEmail request structure.

    """

    def __init__(self):
        r"""
        :param _FromAddress: Sender
        :type FromAddress: str
        :param _ToAddress: Recipient
        :type ToAddress: str
        :param _Subject: Email summary
        :type Subject: str
        :param _FromName: Sender name
        :type FromName: str
        :param _ReplyAddress: Reply-to address
        :type ReplyAddress: str
        :param _HtmlContent: The body of an HTML email
        :type HtmlContent: str
        :param _TextContent: The body of a plain-text email
        :type TextContent: str
        """
        self._FromAddress = None
        self._ToAddress = None
        self._Subject = None
        self._FromName = None
        self._ReplyAddress = None
        self._HtmlContent = None
        self._TextContent = None

    @property
    def FromAddress(self):
        """Sender
        :rtype: str
        """
        return self._FromAddress

    @FromAddress.setter
    def FromAddress(self, FromAddress):
        self._FromAddress = FromAddress

    @property
    def ToAddress(self):
        """Recipient
        :rtype: str
        """
        return self._ToAddress

    @ToAddress.setter
    def ToAddress(self, ToAddress):
        self._ToAddress = ToAddress

    @property
    def Subject(self):
        """Email summary
        :rtype: str
        """
        return self._Subject

    @Subject.setter
    def Subject(self, Subject):
        self._Subject = Subject

    @property
    def FromName(self):
        """Sender name
        :rtype: str
        """
        return self._FromName

    @FromName.setter
    def FromName(self, FromName):
        self._FromName = FromName

    @property
    def ReplyAddress(self):
        """Reply-to address
        :rtype: str
        """
        return self._ReplyAddress

    @ReplyAddress.setter
    def ReplyAddress(self, ReplyAddress):
        self._ReplyAddress = ReplyAddress

    @property
    def HtmlContent(self):
        """The body of an HTML email
        :rtype: str
        """
        return self._HtmlContent

    @HtmlContent.setter
    def HtmlContent(self, HtmlContent):
        self._HtmlContent = HtmlContent

    @property
    def TextContent(self):
        """The body of a plain-text email
        :rtype: str
        """
        return self._TextContent

    @TextContent.setter
    def TextContent(self, TextContent):
        self._TextContent = TextContent


    def _deserialize(self, params):
        self._FromAddress = params.get("FromAddress")
        self._ToAddress = params.get("ToAddress")
        self._Subject = params.get("Subject")
        self._FromName = params.get("FromName")
        self._ReplyAddress = params.get("ReplyAddress")
        self._HtmlContent = params.get("HtmlContent")
        self._TextContent = params.get("TextContent")
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
        :param _Result: The result of creating an email task
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """The result of creating an email task
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class SendTemplatedEmailRequest(AbstractModel):
    """SendTemplatedEmail request structure.

    """

    def __init__(self):
        r"""
        :param _FromAddress: Sender address.
        :type FromAddress: str
        :param _ToAddress: Recipient address. Up to 100 recipient addresses are supported. Multiple addresses should be separated by semicolons (;).
        :type ToAddress: str
        :param _TemplateName: The name of the template created in advance.
        :type TemplateName: str
        :param _TemplateValue: Template variable value, which is a JSON string.
        :type TemplateValue: str
        :param _FromName: Sender name.
        :type FromName: str
        :param _ReplyAddress: Reply-to address.
        :type ReplyAddress: str
        """
        self._FromAddress = None
        self._ToAddress = None
        self._TemplateName = None
        self._TemplateValue = None
        self._FromName = None
        self._ReplyAddress = None

    @property
    def FromAddress(self):
        """Sender address.
        :rtype: str
        """
        return self._FromAddress

    @FromAddress.setter
    def FromAddress(self, FromAddress):
        self._FromAddress = FromAddress

    @property
    def ToAddress(self):
        """Recipient address. Up to 100 recipient addresses are supported. Multiple addresses should be separated by semicolons (;).
        :rtype: str
        """
        return self._ToAddress

    @ToAddress.setter
    def ToAddress(self, ToAddress):
        self._ToAddress = ToAddress

    @property
    def TemplateName(self):
        """The name of the template created in advance.
        :rtype: str
        """
        return self._TemplateName

    @TemplateName.setter
    def TemplateName(self, TemplateName):
        self._TemplateName = TemplateName

    @property
    def TemplateValue(self):
        """Template variable value, which is a JSON string.
        :rtype: str
        """
        return self._TemplateValue

    @TemplateValue.setter
    def TemplateValue(self, TemplateValue):
        self._TemplateValue = TemplateValue

    @property
    def FromName(self):
        """Sender name.
        :rtype: str
        """
        return self._FromName

    @FromName.setter
    def FromName(self, FromName):
        self._FromName = FromName

    @property
    def ReplyAddress(self):
        """Reply-to address.
        :rtype: str
        """
        return self._ReplyAddress

    @ReplyAddress.setter
    def ReplyAddress(self, ReplyAddress):
        self._ReplyAddress = ReplyAddress


    def _deserialize(self, params):
        self._FromAddress = params.get("FromAddress")
        self._ToAddress = params.get("ToAddress")
        self._TemplateName = params.get("TemplateName")
        self._TemplateValue = params.get("TemplateValue")
        self._FromName = params.get("FromName")
        self._ReplyAddress = params.get("ReplyAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendTemplatedEmailResponse(AbstractModel):
    """SendTemplatedEmail response structure.

    """

    def __init__(self):
        r"""
        :param _Result: The result of creating a template email task
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """The result of creating a template email task
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

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
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")