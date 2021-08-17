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
        :param FromAddress: Sender
        :type FromAddress: str
        :param ToAddress: Recipient
        :type ToAddress: str
        :param Subject: Email summary
        :type Subject: str
        :param FromName: Sender name
        :type FromName: str
        :param ReplyAddress: Reply-to address
        :type ReplyAddress: str
        :param HtmlContent: The body of an HTML email
        :type HtmlContent: str
        :param TextContent: The body of a plain-text email
        :type TextContent: str
        """
        self.FromAddress = None
        self.ToAddress = None
        self.Subject = None
        self.FromName = None
        self.ReplyAddress = None
        self.HtmlContent = None
        self.TextContent = None


    def _deserialize(self, params):
        self.FromAddress = params.get("FromAddress")
        self.ToAddress = params.get("ToAddress")
        self.Subject = params.get("Subject")
        self.FromName = params.get("FromName")
        self.ReplyAddress = params.get("ReplyAddress")
        self.HtmlContent = params.get("HtmlContent")
        self.TextContent = params.get("TextContent")
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
        :param Result: The result of creating an email task
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class SendTemplatedEmailRequest(AbstractModel):
    """SendTemplatedEmail request structure.

    """

    def __init__(self):
        r"""
        :param FromAddress: Sender address.
        :type FromAddress: str
        :param ToAddress: Recipient address. Up to 100 recipient addresses are supported. Multiple addresses should be separated by semicolons (;).
        :type ToAddress: str
        :param TemplateName: The name of the template created in advance.
        :type TemplateName: str
        :param TemplateValue: Template variable value, which is a JSON string.
        :type TemplateValue: str
        :param FromName: Sender name.
        :type FromName: str
        :param ReplyAddress: Reply-to address.
        :type ReplyAddress: str
        """
        self.FromAddress = None
        self.ToAddress = None
        self.TemplateName = None
        self.TemplateValue = None
        self.FromName = None
        self.ReplyAddress = None


    def _deserialize(self, params):
        self.FromAddress = params.get("FromAddress")
        self.ToAddress = params.get("ToAddress")
        self.TemplateName = params.get("TemplateName")
        self.TemplateValue = params.get("TemplateValue")
        self.FromName = params.get("FromName")
        self.ReplyAddress = params.get("ReplyAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendTemplatedEmailResponse(AbstractModel):
    """SendTemplatedEmail response structure.

    """

    def __init__(self):
        r"""
        :param Result: The result of creating a template email task
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")