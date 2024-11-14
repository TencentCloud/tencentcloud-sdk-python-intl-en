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
        :param _Body: Message body
        :type Body: str
        :param _Key: Key of a message
        :type Key: str
        """
        self._Body = None
        self._Key = None

    @property
    def Body(self):
        """Message body
        :rtype: str
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Key(self):
        """Key of a message
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key


    def _deserialize(self, params):
        self._Body = params.get("Body")
        self._Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMessageRequest(AbstractModel):
    """SendMessage request structure.

    """

    def __init__(self):
        r"""
        :param _DataHubId: ID of the integrated resource
        :type DataHubId: str
        :param _Message: A batch of messages
        :type Message: list of BatchContent
        """
        self._DataHubId = None
        self._Message = None

    @property
    def DataHubId(self):
        """ID of the integrated resource
        :rtype: str
        """
        return self._DataHubId

    @DataHubId.setter
    def DataHubId(self, DataHubId):
        self._DataHubId = DataHubId

    @property
    def Message(self):
        """A batch of messages
        :rtype: list of BatchContent
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._DataHubId = params.get("DataHubId")
        if params.get("Message") is not None:
            self._Message = []
            for item in params.get("Message"):
                obj = BatchContent()
                obj._deserialize(item)
                self._Message.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMessageResponse(AbstractModel):
    """SendMessage response structure.

    """

    def __init__(self):
        r"""
        :param _MessageId: Message ID
        :type MessageId: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MessageId = None
        self._RequestId = None

    @property
    def MessageId(self):
        """Message ID
        :rtype: list of str
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