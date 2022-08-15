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


class BatchContent(AbstractModel):
    """A batch of messages

    """

    def __init__(self):
        r"""
        :param Body: Message body
        :type Body: str
        :param Key: Key of a message
        :type Key: str
        """
        self.Body = None
        self.Key = None


    def _deserialize(self, params):
        self.Body = params.get("Body")
        self.Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMessageRequest(AbstractModel):
    """SendMessage request structure.

    """

    def __init__(self):
        r"""
        :param DataHubId: ID of the integrated resource
        :type DataHubId: str
        :param Message: A batch of messages
        :type Message: list of BatchContent
        """
        self.DataHubId = None
        self.Message = None


    def _deserialize(self, params):
        self.DataHubId = params.get("DataHubId")
        if params.get("Message") is not None:
            self.Message = []
            for item in params.get("Message"):
                obj = BatchContent()
                obj._deserialize(item)
                self.Message.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMessageResponse(AbstractModel):
    """SendMessage response structure.

    """

    def __init__(self):
        r"""
        :param MessageId: Message ID
        :type MessageId: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MessageId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MessageId = params.get("MessageId")
        self.RequestId = params.get("RequestId")