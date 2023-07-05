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


class ClearQueueRequest(AbstractModel):
    """ClearQueue request structure.

    """

    def __init__(self):
        r"""
        :param _QueueName: Queue name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).
        :type QueueName: str
        """
        self._QueueName = None

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearQueueResponse(AbstractModel):
    """ClearQueue response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ClearSubscriptionFilterTagsRequest(AbstractModel):
    """ClearSubscriptionFilterTags request structure.

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).
        :type TopicName: str
        :param _SubscriptionName: Subscription name, which is unique in the same topic under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).
        :type SubscriptionName: str
        """
        self._TopicName = None
        self._SubscriptionName = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def SubscriptionName(self):
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._SubscriptionName = params.get("SubscriptionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearSubscriptionFilterTagsResponse(AbstractModel):
    """ClearSubscriptionFilterTags response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateQueueRequest(AbstractModel):
    """CreateQueue request structure.

    """

    def __init__(self):
        r"""
        :param _QueueName: Queue name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).
        :type QueueName: str
        :param _MaxMsgHeapNum: Maximum number of heaped messages. The value range is 1,000,000–10,000,000 during the beta test and can be 1,000,000–1,000,000,000 after the product is officially released. The default value is 10,000,000 during the beta test and will be 100,000,000 after the product is officially released.
        :type MaxMsgHeapNum: int
        :param _PollingWaitSeconds: Long polling wait time for message reception. Value range: 0–30 seconds. Default value: 0.
        :type PollingWaitSeconds: int
        :param _VisibilityTimeout: Message visibility timeout period. Value range: 1–43200 seconds (i.e., 12 hours). Default value: 30.
        :type VisibilityTimeout: int
        :param _MaxMsgSize: Maximum message length. Value range: 1024–65536 bytes (i.e., 1–64 KB). Default value: 65536.
        :type MaxMsgSize: int
        :param _MsgRetentionSeconds: Message retention period. Value range: 60–1296000 seconds (i.e., 1 minute–15 days). Default value: 345600 (i.e., 4 days).
        :type MsgRetentionSeconds: int
        :param _RewindSeconds: Whether to enable the message rewinding feature for a queue. Value range: 0–msgRetentionSeconds, where 0 means not to enable this feature, while `msgRetentionSeconds` indicates that the maximum rewindable period is the message retention period of the queue.
        :type RewindSeconds: int
        :param _Transaction: 1: transaction queue, 0: general queue
        :type Transaction: int
        :param _FirstQueryInterval: First lookback interval
        :type FirstQueryInterval: int
        :param _MaxQueryCount: Maximum number of lookbacks
        :type MaxQueryCount: int
        :param _DeadLetterQueueName: Dead letter queue name
        :type DeadLetterQueueName: str
        :param _Policy: Dead letter policy. 0: message has been consumed multiple times but not deleted, 1: `Time-To-Live` has elapsed
        :type Policy: int
        :param _MaxReceiveCount: Maximum receipt times. Value range: 1–1000
        :type MaxReceiveCount: int
        :param _MaxTimeToLive: Maximum period in seconds before an unconsumed message expires, which is required if `policy` is 1. Value range: 300–43200. This value should be smaller than `msgRetentionSeconds` (maximum message retention period)
        :type MaxTimeToLive: int
        :param _Trace: Whether to enable message trace. true: yes, false: no. If this field is not set, the feature will not be enabled
        :type Trace: bool
        """
        self._QueueName = None
        self._MaxMsgHeapNum = None
        self._PollingWaitSeconds = None
        self._VisibilityTimeout = None
        self._MaxMsgSize = None
        self._MsgRetentionSeconds = None
        self._RewindSeconds = None
        self._Transaction = None
        self._FirstQueryInterval = None
        self._MaxQueryCount = None
        self._DeadLetterQueueName = None
        self._Policy = None
        self._MaxReceiveCount = None
        self._MaxTimeToLive = None
        self._Trace = None

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def MaxMsgHeapNum(self):
        return self._MaxMsgHeapNum

    @MaxMsgHeapNum.setter
    def MaxMsgHeapNum(self, MaxMsgHeapNum):
        self._MaxMsgHeapNum = MaxMsgHeapNum

    @property
    def PollingWaitSeconds(self):
        return self._PollingWaitSeconds

    @PollingWaitSeconds.setter
    def PollingWaitSeconds(self, PollingWaitSeconds):
        self._PollingWaitSeconds = PollingWaitSeconds

    @property
    def VisibilityTimeout(self):
        return self._VisibilityTimeout

    @VisibilityTimeout.setter
    def VisibilityTimeout(self, VisibilityTimeout):
        self._VisibilityTimeout = VisibilityTimeout

    @property
    def MaxMsgSize(self):
        return self._MaxMsgSize

    @MaxMsgSize.setter
    def MaxMsgSize(self, MaxMsgSize):
        self._MaxMsgSize = MaxMsgSize

    @property
    def MsgRetentionSeconds(self):
        return self._MsgRetentionSeconds

    @MsgRetentionSeconds.setter
    def MsgRetentionSeconds(self, MsgRetentionSeconds):
        self._MsgRetentionSeconds = MsgRetentionSeconds

    @property
    def RewindSeconds(self):
        return self._RewindSeconds

    @RewindSeconds.setter
    def RewindSeconds(self, RewindSeconds):
        self._RewindSeconds = RewindSeconds

    @property
    def Transaction(self):
        return self._Transaction

    @Transaction.setter
    def Transaction(self, Transaction):
        self._Transaction = Transaction

    @property
    def FirstQueryInterval(self):
        return self._FirstQueryInterval

    @FirstQueryInterval.setter
    def FirstQueryInterval(self, FirstQueryInterval):
        self._FirstQueryInterval = FirstQueryInterval

    @property
    def MaxQueryCount(self):
        return self._MaxQueryCount

    @MaxQueryCount.setter
    def MaxQueryCount(self, MaxQueryCount):
        self._MaxQueryCount = MaxQueryCount

    @property
    def DeadLetterQueueName(self):
        return self._DeadLetterQueueName

    @DeadLetterQueueName.setter
    def DeadLetterQueueName(self, DeadLetterQueueName):
        self._DeadLetterQueueName = DeadLetterQueueName

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def MaxReceiveCount(self):
        return self._MaxReceiveCount

    @MaxReceiveCount.setter
    def MaxReceiveCount(self, MaxReceiveCount):
        self._MaxReceiveCount = MaxReceiveCount

    @property
    def MaxTimeToLive(self):
        return self._MaxTimeToLive

    @MaxTimeToLive.setter
    def MaxTimeToLive(self, MaxTimeToLive):
        self._MaxTimeToLive = MaxTimeToLive

    @property
    def Trace(self):
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        self._MaxMsgHeapNum = params.get("MaxMsgHeapNum")
        self._PollingWaitSeconds = params.get("PollingWaitSeconds")
        self._VisibilityTimeout = params.get("VisibilityTimeout")
        self._MaxMsgSize = params.get("MaxMsgSize")
        self._MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self._RewindSeconds = params.get("RewindSeconds")
        self._Transaction = params.get("Transaction")
        self._FirstQueryInterval = params.get("FirstQueryInterval")
        self._MaxQueryCount = params.get("MaxQueryCount")
        self._DeadLetterQueueName = params.get("DeadLetterQueueName")
        self._Policy = params.get("Policy")
        self._MaxReceiveCount = params.get("MaxReceiveCount")
        self._MaxTimeToLive = params.get("MaxTimeToLive")
        self._Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateQueueResponse(AbstractModel):
    """CreateQueue response structure.

    """

    def __init__(self):
        r"""
        :param _QueueId: `queueId` of a successfully created queue
        :type QueueId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._QueueId = None
        self._RequestId = None

    @property
    def QueueId(self):
        return self._QueueId

    @QueueId.setter
    def QueueId(self, QueueId):
        self._QueueId = QueueId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._QueueId = params.get("QueueId")
        self._RequestId = params.get("RequestId")


class CreateSubscribeRequest(AbstractModel):
    """CreateSubscribe request structure.

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).
        :type TopicName: str
        :param _SubscriptionName: Subscription name, which is unique in the same topic under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).
        :type SubscriptionName: str
        :param _Protocol: Subscription protocol. Currently, two protocols are supported: http and queue. To use the `http` protocol, you need to build your own web server to receive messages. With the `queue` protocol, messages are automatically pushed to a CMQ queue and you can pull them concurrently.
        :type Protocol: str
        :param _Endpoint: `Endpoint` for notification receipt, which is distinguished by `Protocol`. For `http`, `Endpoint` must begin with `http://` and `host` can be a domain name or IP. For `Queue`, enter `QueueName`. Please note that currently the push service cannot push messages to a VPC; therefore, if a VPC domain name or address is entered for `Endpoint`, pushed messages will not be received. Currently, messages can be pushed only to the public network and basic network.
        :type Endpoint: str
        :param _NotifyStrategy: CMQ push server retry policy in case an error occurs while pushing a message to `Endpoint`. Valid values: 1. BACKOFF_RETRY: backoff retry, which is to retry at a fixed interval, discard the message after a certain number of retries, and continue to push the next message; 2. EXPONENTIAL_DECAY_RETRY: exponential decay retry, which is to retry at an exponentially increasing interval, such as 1s, 2s, 4s, 8s, and so on. As a message can be retained in a topic for one day, failed messages will be discarded at most after one day of retry. Default value: EXPONENTIAL_DECAY_RETRY.
        :type NotifyStrategy: str
        :param _FilterTag: Message body tag (used for message filtering). The number of tags cannot exceed 5, and each tag can contain up to 16 characters. It is used in conjunction with the `MsgTag` parameter of `(Batch)PublishMessage`. Rules: 1. If `FilterTag` is not set, no matter whether `MsgTag` is set, the subscription will receive all messages published to the topic; 2. If the `FilterTag` array has a value, only when at least one of the values in the array also exists in the `MsgTag` array (i.e., `FilterTag` and `MsgTag` have an intersection) can the subscription receive messages published to the topic; 3. If the `FilterTag` array has a value, but `MsgTag` is not set, then no message published to the topic will be received, which can be considered as a special case of rule 2 as `FilterTag` and `MsgTag` do not intersect in this case. The overall design idea of rules is based on the intention of the subscriber.
        :type FilterTag: list of str
        :param _BindingKey: The number of `BindingKey` cannot exceed 5, and the length of each `BindingKey` cannot exceed 64 bytes. This field indicates the filtering policy for subscribing to and receiving messages. Each `BindingKey` can contain up to 15 `.`, i.e., up to 16 phrases.
        :type BindingKey: list of str
        :param _NotifyContentFormat: Push content format. Valid values: 1. JSON, 2. SIMPLIFIED, i.e., the raw format. If `Protocol` is `queue`, this value must be `SIMPLIFIED`. If `Protocol` is `http`, both options are acceptable, and the default value is `JSON`.
        :type NotifyContentFormat: str
        """
        self._TopicName = None
        self._SubscriptionName = None
        self._Protocol = None
        self._Endpoint = None
        self._NotifyStrategy = None
        self._FilterTag = None
        self._BindingKey = None
        self._NotifyContentFormat = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def SubscriptionName(self):
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def NotifyStrategy(self):
        return self._NotifyStrategy

    @NotifyStrategy.setter
    def NotifyStrategy(self, NotifyStrategy):
        self._NotifyStrategy = NotifyStrategy

    @property
    def FilterTag(self):
        return self._FilterTag

    @FilterTag.setter
    def FilterTag(self, FilterTag):
        self._FilterTag = FilterTag

    @property
    def BindingKey(self):
        return self._BindingKey

    @BindingKey.setter
    def BindingKey(self, BindingKey):
        self._BindingKey = BindingKey

    @property
    def NotifyContentFormat(self):
        return self._NotifyContentFormat

    @NotifyContentFormat.setter
    def NotifyContentFormat(self, NotifyContentFormat):
        self._NotifyContentFormat = NotifyContentFormat


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._SubscriptionName = params.get("SubscriptionName")
        self._Protocol = params.get("Protocol")
        self._Endpoint = params.get("Endpoint")
        self._NotifyStrategy = params.get("NotifyStrategy")
        self._FilterTag = params.get("FilterTag")
        self._BindingKey = params.get("BindingKey")
        self._NotifyContentFormat = params.get("NotifyContentFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubscribeResponse(AbstractModel):
    """CreateSubscribe response structure.

    """

    def __init__(self):
        r"""
        :param _SubscriptionId: SubscriptionId
        :type SubscriptionId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SubscriptionId = None
        self._RequestId = None

    @property
    def SubscriptionId(self):
        return self._SubscriptionId

    @SubscriptionId.setter
    def SubscriptionId(self, SubscriptionId):
        self._SubscriptionId = SubscriptionId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SubscriptionId = params.get("SubscriptionId")
        self._RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic request structure.

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).
        :type TopicName: str
        :param _MaxMsgSize: Maximum message length. Value range: 1024–65536 bytes (i.e., 1–64 KB). Default value: 65536.
        :type MaxMsgSize: int
        :param _FilterType: Message match policy for a specified topic.
        :type FilterType: int
        :param _MsgRetentionSeconds: Message retention period. Value range: 60–86400 seconds (i.e., 1 minute–1 day). Default value: 86400.
        :type MsgRetentionSeconds: int
        :param _Trace: Whether to enable message trace. true: yes, false: no. If this field is left empty, the feature will not be enabled.
        :type Trace: bool
        """
        self._TopicName = None
        self._MaxMsgSize = None
        self._FilterType = None
        self._MsgRetentionSeconds = None
        self._Trace = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def MaxMsgSize(self):
        return self._MaxMsgSize

    @MaxMsgSize.setter
    def MaxMsgSize(self, MaxMsgSize):
        self._MaxMsgSize = MaxMsgSize

    @property
    def FilterType(self):
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def MsgRetentionSeconds(self):
        return self._MsgRetentionSeconds

    @MsgRetentionSeconds.setter
    def MsgRetentionSeconds(self, MsgRetentionSeconds):
        self._MsgRetentionSeconds = MsgRetentionSeconds

    @property
    def Trace(self):
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._MaxMsgSize = params.get("MaxMsgSize")
        self._FilterType = params.get("FilterType")
        self._MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self._Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResponse(AbstractModel):
    """CreateTopic response structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: TopicName
        :type TopicId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TopicId = None
        self._RequestId = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._RequestId = params.get("RequestId")


class DeadLetterPolicy(AbstractModel):
    """DeadLetterPolicy

    """

    def __init__(self):
        r"""
        :param _DeadLetterQueueName: DeadLetterQueueName
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeadLetterQueueName: str
        :param _DeadLetterQueue: DeadLetterQueue
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeadLetterQueue: str
        :param _Policy: Policy
Note: this field may return null, indicating that no valid values can be obtained.
        :type Policy: int
        :param _MaxTimeToLive: MaxTimeToLive
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxTimeToLive: int
        :param _MaxReceiveCount: MaxReceiveCount
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxReceiveCount: int
        """
        self._DeadLetterQueueName = None
        self._DeadLetterQueue = None
        self._Policy = None
        self._MaxTimeToLive = None
        self._MaxReceiveCount = None

    @property
    def DeadLetterQueueName(self):
        return self._DeadLetterQueueName

    @DeadLetterQueueName.setter
    def DeadLetterQueueName(self, DeadLetterQueueName):
        self._DeadLetterQueueName = DeadLetterQueueName

    @property
    def DeadLetterQueue(self):
        return self._DeadLetterQueue

    @DeadLetterQueue.setter
    def DeadLetterQueue(self, DeadLetterQueue):
        self._DeadLetterQueue = DeadLetterQueue

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def MaxTimeToLive(self):
        return self._MaxTimeToLive

    @MaxTimeToLive.setter
    def MaxTimeToLive(self, MaxTimeToLive):
        self._MaxTimeToLive = MaxTimeToLive

    @property
    def MaxReceiveCount(self):
        return self._MaxReceiveCount

    @MaxReceiveCount.setter
    def MaxReceiveCount(self, MaxReceiveCount):
        self._MaxReceiveCount = MaxReceiveCount


    def _deserialize(self, params):
        self._DeadLetterQueueName = params.get("DeadLetterQueueName")
        self._DeadLetterQueue = params.get("DeadLetterQueue")
        self._Policy = params.get("Policy")
        self._MaxTimeToLive = params.get("MaxTimeToLive")
        self._MaxReceiveCount = params.get("MaxReceiveCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeadLetterSource(AbstractModel):
    """DeadLetterSource

    """

    def __init__(self):
        r"""
        :param _QueueId: QueueId
Note: this field may return null, indicating that no valid values can be obtained.
        :type QueueId: str
        :param _QueueName: QueueName
Note: this field may return null, indicating that no valid values can be obtained.
        :type QueueName: str
        """
        self._QueueId = None
        self._QueueName = None

    @property
    def QueueId(self):
        return self._QueueId

    @QueueId.setter
    def QueueId(self, QueueId):
        self._QueueId = QueueId

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._QueueId = params.get("QueueId")
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteQueueRequest(AbstractModel):
    """DeleteQueue request structure.

    """

    def __init__(self):
        r"""
        :param _QueueName: Queue name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).
        :type QueueName: str
        """
        self._QueueName = None

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteQueueResponse(AbstractModel):
    """DeleteQueue response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteSubscribeRequest(AbstractModel):
    """DeleteSubscribe request structure.

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).
        :type TopicName: str
        :param _SubscriptionName: Subscription name, which is unique in the same topic under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).
        :type SubscriptionName: str
        """
        self._TopicName = None
        self._SubscriptionName = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def SubscriptionName(self):
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._SubscriptionName = params.get("SubscriptionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSubscribeResponse(AbstractModel):
    """DeleteSubscribe response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTopicRequest(AbstractModel):
    """DeleteTopic request structure.

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).
        :type TopicName: str
        """
        self._TopicName = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicResponse(AbstractModel):
    """DeleteTopic response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeDeadLetterSourceQueuesRequest(AbstractModel):
    """DescribeDeadLetterSourceQueues request structure.

    """

    def __init__(self):
        r"""
        :param _DeadLetterQueueName: Dead letter queue name
        :type DeadLetterQueueName: str
        :param _Limit: Starting position of topic list to be returned on the current page in case of paginated return. If a value is entered, `limit` is required. If this parameter is left empty, 0 will be used by default.
        :type Limit: int
        :param _Offset: Number of topics to be returned per page in case of paginated return. If this parameter is not passed in, 20 will be used by default. Maximum value: 50.
        :type Offset: int
        :param _Filters: Filters source queue name of dead letter queue. Currently, only filtering by `SourceQueueName` is supported
        :type Filters: list of Filter
        """
        self._DeadLetterQueueName = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def DeadLetterQueueName(self):
        return self._DeadLetterQueueName

    @DeadLetterQueueName.setter
    def DeadLetterQueueName(self, DeadLetterQueueName):
        self._DeadLetterQueueName = DeadLetterQueueName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._DeadLetterQueueName = params.get("DeadLetterQueueName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeadLetterSourceQueuesResponse(AbstractModel):
    """DescribeDeadLetterSourceQueues response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible queues
        :type TotalCount: int
        :param _QueueSet: Source queues of dead letter queue
        :type QueueSet: list of DeadLetterSource
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._QueueSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def QueueSet(self):
        return self._QueueSet

    @QueueSet.setter
    def QueueSet(self, QueueSet):
        self._QueueSet = QueueSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("QueueSet") is not None:
            self._QueueSet = []
            for item in params.get("QueueSet"):
                obj = DeadLetterSource()
                obj._deserialize(item)
                self._QueueSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeQueueDetailRequest(AbstractModel):
    """DescribeQueueDetail request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Starting position of queue list to be returned on the current page in case of paginated return. If a value is entered, `limit` is required. If this parameter is left empty, 0 will be used by default
        :type Offset: int
        :param _Limit: Number of queues to be returned per page in case of paginated return. If this parameter is not passed in, 20 will be used by default. Maximum value: 50.
        :type Limit: int
        :param _Filters: Filter parameter. Currently, filtering by `QueueName` is supported, and only one keyword is allowed
        :type Filters: list of Filter
        :param _TagKey: Tag search
        :type TagKey: str
        :param _QueueName: Exact match by `QueueName`
        :type QueueName: str
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._TagKey = None
        self._QueueName = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._TagKey = params.get("TagKey")
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQueueDetailResponse(AbstractModel):
    """DescribeQueueDetail response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of queues
        :type TotalCount: int
        :param _QueueSet: Queue list
        :type QueueSet: list of QueueSet
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._QueueSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def QueueSet(self):
        return self._QueueSet

    @QueueSet.setter
    def QueueSet(self, QueueSet):
        self._QueueSet = QueueSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("QueueSet") is not None:
            self._QueueSet = []
            for item in params.get("QueueSet"):
                obj = QueueSet()
                obj._deserialize(item)
                self._QueueSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubscriptionDetailRequest(AbstractModel):
    """DescribeSubscriptionDetail request structure.

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).
        :type TopicName: str
        :param _Offset: Starting position of topic list to be returned on the current page in case of paginated return. If a value is entered, `limit` is required. If this parameter is left empty, 0 will be used by default
        :type Offset: int
        :param _Limit: Number of topics to be returned per page in case of paginated return. If this parameter is not passed in, 20 will be used by default. Maximum value: 50.
        :type Limit: int
        :param _Filters: Filter parameter. Currently, only filtering by `SubscriptionName` is supported, and only one keyword is allowed.
        :type Filters: list of Filter
        """
        self._TopicName = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubscriptionDetailResponse(AbstractModel):
    """DescribeSubscriptionDetail response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _SubscriptionSet: Subscription attribute set
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubscriptionSet: list of Subscription
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._SubscriptionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SubscriptionSet(self):
        return self._SubscriptionSet

    @SubscriptionSet.setter
    def SubscriptionSet(self, SubscriptionSet):
        self._SubscriptionSet = SubscriptionSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SubscriptionSet") is not None:
            self._SubscriptionSet = []
            for item in params.get("SubscriptionSet"):
                obj = Subscription()
                obj._deserialize(item)
                self._SubscriptionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopicDetailRequest(AbstractModel):
    """DescribeTopicDetail request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Starting position of queue list to be returned on the current page in case of paginated return. If a value is entered, `limit` is required. If this parameter is left empty, 0 will be used by default.
        :type Offset: int
        :param _Limit: Number of queues to be returned per page in case of paginated return. If this parameter is not passed in, 20 will be used by default. Maximum value: 50.
        :type Limit: int
        :param _Filters: Currently, only filtering by `TopicName` is supported, and only one filter value can be entered
        :type Filters: list of Filter
        :param _TagKey: Tag match
        :type TagKey: str
        :param _TopicName: Exact match by `TopicName`
        :type TopicName: str
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._TagKey = None
        self._TopicName = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._TagKey = params.get("TagKey")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicDetailResponse(AbstractModel):
    """DescribeTopicDetail response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: TotalCount
        :type TotalCount: int
        :param _TopicSet: TopicSet
        :type TopicSet: list of TopicSet
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._TopicSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TopicSet(self):
        return self._TopicSet

    @TopicSet.setter
    def TopicSet(self, TopicSet):
        self._TopicSet = TopicSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TopicSet") is not None:
            self._TopicSet = []
            for item in params.get("TopicSet"):
                obj = TopicSet()
                obj._deserialize(item)
                self._TopicSet.append(obj)
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """Filter parameter

    """

    def __init__(self):
        r"""
        :param _Name: Filter parameter name
        :type Name: str
        :param _Values: Value
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyQueueAttributeRequest(AbstractModel):
    """ModifyQueueAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _QueueName: Queue name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).
        :type QueueName: str
        :param _MaxMsgHeapNum: Maximum number of heaped messages. The value range is 1,000,000–10,000,000 during the beta test and can be 1,000,000–1,000,000,000 after the product is officially released. The default value is 10,000,000 during the beta test and will be 100,000,000 after the product is officially released.
        :type MaxMsgHeapNum: int
        :param _PollingWaitSeconds: Long polling wait time for message reception. Value range: 0–30 seconds. Default value: 0.
        :type PollingWaitSeconds: int
        :param _VisibilityTimeout: Message visibility timeout period. Value range: 1–43200 seconds (i.e., 12 hours). Default value: 30.
        :type VisibilityTimeout: int
        :param _MaxMsgSize: Maximum message length. Value range: 1024–65536 bytes (i.e., 1–64 KB). Default value: 65536.
        :type MaxMsgSize: int
        :param _MsgRetentionSeconds: Message retention period. Value range: 60–1296000 seconds (i.e., 1 minute–15 days). Default value: 345600 (i.e., 4 days).
        :type MsgRetentionSeconds: int
        :param _RewindSeconds: Maximum message rewindable period. Value range: 0–msgRetentionSeconds (maximum message retention period of a queue). 0 means not to enable message rewinding.
        :type RewindSeconds: int
        :param _FirstQueryInterval: First query time
        :type FirstQueryInterval: int
        :param _MaxQueryCount: Maximum number of queries
        :type MaxQueryCount: int
        :param _DeadLetterQueueName: Dead letter queue name
        :type DeadLetterQueueName: str
        :param _MaxTimeToLive: Maximum period in seconds before an unconsumed message expires, which is required if `MaxTimeToLivepolicy` is 1. Value range: 300–43200. This value should be smaller than `MsgRetentionSeconds` (maximum message retention period)
        :type MaxTimeToLive: int
        :param _MaxReceiveCount: Maximum number of receipts
        :type MaxReceiveCount: int
        :param _Policy: Dead letter queue policy
        :type Policy: int
        :param _Trace: Whether to enable message trace. true: yes, false: no. If this field is left empty, the feature will not be enabled.
        :type Trace: bool
        """
        self._QueueName = None
        self._MaxMsgHeapNum = None
        self._PollingWaitSeconds = None
        self._VisibilityTimeout = None
        self._MaxMsgSize = None
        self._MsgRetentionSeconds = None
        self._RewindSeconds = None
        self._FirstQueryInterval = None
        self._MaxQueryCount = None
        self._DeadLetterQueueName = None
        self._MaxTimeToLive = None
        self._MaxReceiveCount = None
        self._Policy = None
        self._Trace = None

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def MaxMsgHeapNum(self):
        return self._MaxMsgHeapNum

    @MaxMsgHeapNum.setter
    def MaxMsgHeapNum(self, MaxMsgHeapNum):
        self._MaxMsgHeapNum = MaxMsgHeapNum

    @property
    def PollingWaitSeconds(self):
        return self._PollingWaitSeconds

    @PollingWaitSeconds.setter
    def PollingWaitSeconds(self, PollingWaitSeconds):
        self._PollingWaitSeconds = PollingWaitSeconds

    @property
    def VisibilityTimeout(self):
        return self._VisibilityTimeout

    @VisibilityTimeout.setter
    def VisibilityTimeout(self, VisibilityTimeout):
        self._VisibilityTimeout = VisibilityTimeout

    @property
    def MaxMsgSize(self):
        return self._MaxMsgSize

    @MaxMsgSize.setter
    def MaxMsgSize(self, MaxMsgSize):
        self._MaxMsgSize = MaxMsgSize

    @property
    def MsgRetentionSeconds(self):
        return self._MsgRetentionSeconds

    @MsgRetentionSeconds.setter
    def MsgRetentionSeconds(self, MsgRetentionSeconds):
        self._MsgRetentionSeconds = MsgRetentionSeconds

    @property
    def RewindSeconds(self):
        return self._RewindSeconds

    @RewindSeconds.setter
    def RewindSeconds(self, RewindSeconds):
        self._RewindSeconds = RewindSeconds

    @property
    def FirstQueryInterval(self):
        return self._FirstQueryInterval

    @FirstQueryInterval.setter
    def FirstQueryInterval(self, FirstQueryInterval):
        self._FirstQueryInterval = FirstQueryInterval

    @property
    def MaxQueryCount(self):
        return self._MaxQueryCount

    @MaxQueryCount.setter
    def MaxQueryCount(self, MaxQueryCount):
        self._MaxQueryCount = MaxQueryCount

    @property
    def DeadLetterQueueName(self):
        return self._DeadLetterQueueName

    @DeadLetterQueueName.setter
    def DeadLetterQueueName(self, DeadLetterQueueName):
        self._DeadLetterQueueName = DeadLetterQueueName

    @property
    def MaxTimeToLive(self):
        return self._MaxTimeToLive

    @MaxTimeToLive.setter
    def MaxTimeToLive(self, MaxTimeToLive):
        self._MaxTimeToLive = MaxTimeToLive

    @property
    def MaxReceiveCount(self):
        return self._MaxReceiveCount

    @MaxReceiveCount.setter
    def MaxReceiveCount(self, MaxReceiveCount):
        self._MaxReceiveCount = MaxReceiveCount

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def Trace(self):
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        self._MaxMsgHeapNum = params.get("MaxMsgHeapNum")
        self._PollingWaitSeconds = params.get("PollingWaitSeconds")
        self._VisibilityTimeout = params.get("VisibilityTimeout")
        self._MaxMsgSize = params.get("MaxMsgSize")
        self._MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self._RewindSeconds = params.get("RewindSeconds")
        self._FirstQueryInterval = params.get("FirstQueryInterval")
        self._MaxQueryCount = params.get("MaxQueryCount")
        self._DeadLetterQueueName = params.get("DeadLetterQueueName")
        self._MaxTimeToLive = params.get("MaxTimeToLive")
        self._MaxReceiveCount = params.get("MaxReceiveCount")
        self._Policy = params.get("Policy")
        self._Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyQueueAttributeResponse(AbstractModel):
    """ModifyQueueAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySubscriptionAttributeRequest(AbstractModel):
    """ModifySubscriptionAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).
        :type TopicName: str
        :param _SubscriptionName: Subscription name, which is unique in the same topic under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).
        :type SubscriptionName: str
        :param _NotifyStrategy: CMQ push server retry policy in case an error occurs while pushing a message to `Endpoint`. Valid values:
1. BACKOFF_RETRY: backoff retry, which is to retry at a fixed interval, discard the message after a certain number of retries, and continue to push the next message.
2. EXPONENTIAL_DECAY_RETRY: exponential decay retry, which is to retry at an exponentially increasing interval, such as 1s, 2s, 4s, 8s, and so on. As a message can be retained in a topic for one day, failed messages will be discarded at most after one day of retry. Default value: EXPONENTIAL_DECAY_RETRY.
        :type NotifyStrategy: str
        :param _NotifyContentFormat: Push content format. Valid values: 1. JSON, 2. SIMPLIFIED, i.e., the raw format. If `Protocol` is `queue`, this value must be `SIMPLIFIED`. If `Protocol` is `HTTP`, both options are acceptable, and the default value is `JSON`.
        :type NotifyContentFormat: str
        :param _FilterTags: Message body tag (used for message filtering). The number of tags cannot exceed 5, and each tag can contain up to 16 characters. It is used in conjunction with the `MsgTag` parameter of `(Batch)PublishMessage`. Rules: 1. If `FilterTag` is not set, no matter whether `MsgTag` is set, the subscription will receive all messages published to the topic; 2. If the `FilterTag` array has a value, only when at least one of the values in the array also exists in the `MsgTag` array (i.e., `FilterTag` and `MsgTag` have an intersection) can the subscription receive messages published to the topic; 3. If the `FilterTag` array has a value, but `MsgTag` is not set, then no message published to the topic will be received, which can be considered as a special case of rule 2 as `FilterTag` and `MsgTag` do not intersect in this case. The overall design idea of rules is based on the intention of the subscriber.
        :type FilterTags: list of str
        :param _BindingKey: The number of `BindingKey` cannot exceed 5, and the length of each `BindingKey` cannot exceed 64 bytes. This field indicates the filtering policy for subscribing to and receiving messages. Each `BindingKey` can contain up to 15 `.`, i.e., up to 16 phrases.
        :type BindingKey: list of str
        """
        self._TopicName = None
        self._SubscriptionName = None
        self._NotifyStrategy = None
        self._NotifyContentFormat = None
        self._FilterTags = None
        self._BindingKey = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def SubscriptionName(self):
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName

    @property
    def NotifyStrategy(self):
        return self._NotifyStrategy

    @NotifyStrategy.setter
    def NotifyStrategy(self, NotifyStrategy):
        self._NotifyStrategy = NotifyStrategy

    @property
    def NotifyContentFormat(self):
        return self._NotifyContentFormat

    @NotifyContentFormat.setter
    def NotifyContentFormat(self, NotifyContentFormat):
        self._NotifyContentFormat = NotifyContentFormat

    @property
    def FilterTags(self):
        return self._FilterTags

    @FilterTags.setter
    def FilterTags(self, FilterTags):
        self._FilterTags = FilterTags

    @property
    def BindingKey(self):
        return self._BindingKey

    @BindingKey.setter
    def BindingKey(self, BindingKey):
        self._BindingKey = BindingKey


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._SubscriptionName = params.get("SubscriptionName")
        self._NotifyStrategy = params.get("NotifyStrategy")
        self._NotifyContentFormat = params.get("NotifyContentFormat")
        self._FilterTags = params.get("FilterTags")
        self._BindingKey = params.get("BindingKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscriptionAttributeResponse(AbstractModel):
    """ModifySubscriptionAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyTopicAttributeRequest(AbstractModel):
    """ModifyTopicAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).
        :type TopicName: str
        :param _MaxMsgSize: Maximum message length. Value range: 1024–65536 bytes (i.e., 1–64 KB). Default value: 65536.
        :type MaxMsgSize: int
        :param _MsgRetentionSeconds: Message retention period. Value range: 60–86400 seconds (i.e., 1 minute–1 day). Default value: 86400.
        :type MsgRetentionSeconds: int
        :param _Trace: Whether to enable message trace. true: yes, false: no. If this field is left empty, the feature will not be enabled.
        :type Trace: bool
        """
        self._TopicName = None
        self._MaxMsgSize = None
        self._MsgRetentionSeconds = None
        self._Trace = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def MaxMsgSize(self):
        return self._MaxMsgSize

    @MaxMsgSize.setter
    def MaxMsgSize(self, MaxMsgSize):
        self._MaxMsgSize = MaxMsgSize

    @property
    def MsgRetentionSeconds(self):
        return self._MsgRetentionSeconds

    @MsgRetentionSeconds.setter
    def MsgRetentionSeconds(self, MsgRetentionSeconds):
        self._MsgRetentionSeconds = MsgRetentionSeconds

    @property
    def Trace(self):
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._MaxMsgSize = params.get("MaxMsgSize")
        self._MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self._Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicAttributeResponse(AbstractModel):
    """ModifyTopicAttribute response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class QueueSet(AbstractModel):
    """Batch queue attribute information

    """

    def __init__(self):
        r"""
        :param _QueueId: QueueId
        :type QueueId: str
        :param _QueueName: QueueName
        :type QueueName: str
        :param _Qps: Qps
Note: this field may return null, indicating that no valid values can be obtained.
        :type Qps: int
        :param _Bps: Bps
Note: this field may return null, indicating that no valid values can be obtained.
        :type Bps: int
        :param _MaxDelaySeconds: MaxDelaySeconds
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxDelaySeconds: int
        :param _MaxMsgHeapNum: MaxMsgHeapNum
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxMsgHeapNum: int
        :param _PollingWaitSeconds: PollingWaitSeconds
Note: this field may return null, indicating that no valid values can be obtained.
        :type PollingWaitSeconds: int
        :param _MsgRetentionSeconds: MsgRetentionSeconds
Note: this field may return null, indicating that no valid values can be obtained.
        :type MsgRetentionSeconds: int
        :param _VisibilityTimeout: VisibilityTimeout
Note: this field may return null, indicating that no valid values can be obtained.
        :type VisibilityTimeout: int
        :param _MaxMsgSize: MaxMsgSize
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxMsgSize: int
        :param _RewindSeconds: RewindSeconds
Note: this field may return null, indicating that no valid values can be obtained.
        :type RewindSeconds: int
        :param _CreateTime: CreateTime
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: int
        :param _LastModifyTime: LastModifyTime
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastModifyTime: int
        :param _ActiveMsgNum: ActiveMsgNum
Note: this field may return null, indicating that no valid values can be obtained.
        :type ActiveMsgNum: int
        :param _InactiveMsgNum: InactiveMsgNum
Note: this field may return null, indicating that no valid values can be obtained.
        :type InactiveMsgNum: int
        :param _DelayMsgNum: DelayMsgNum
Note: this field may return null, indicating that no valid values can be obtained.
        :type DelayMsgNum: int
        :param _RewindMsgNum: RewindMsgNum
Note: this field may return null, indicating that no valid values can be obtained.
        :type RewindMsgNum: int
        :param _MinMsgTime: MinMsgTime
Note: this field may return null, indicating that no valid values can be obtained.
        :type MinMsgTime: int
        :param _Transaction: Transaction
Note: this field may return null, indicating that no valid values can be obtained.
        :type Transaction: bool
        :param _DeadLetterSource: DeadLetterSource
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeadLetterSource: list of DeadLetterSource
        :param _DeadLetterPolicy: DeadLetterPolicy
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeadLetterPolicy: :class:`tencentcloud.cmq.v20190304.models.DeadLetterPolicy`
        :param _TransactionPolicy: TransactionPolicy
Note: this field may return null, indicating that no valid values can be obtained.
        :type TransactionPolicy: :class:`tencentcloud.cmq.v20190304.models.TransactionPolicy`
        :param _CreateUin: Creator `uin`
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateUin: int
        :param _Tags: Tag
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _Trace: Message trace flag. true: enabled, false: not enabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type Trace: bool
        """
        self._QueueId = None
        self._QueueName = None
        self._Qps = None
        self._Bps = None
        self._MaxDelaySeconds = None
        self._MaxMsgHeapNum = None
        self._PollingWaitSeconds = None
        self._MsgRetentionSeconds = None
        self._VisibilityTimeout = None
        self._MaxMsgSize = None
        self._RewindSeconds = None
        self._CreateTime = None
        self._LastModifyTime = None
        self._ActiveMsgNum = None
        self._InactiveMsgNum = None
        self._DelayMsgNum = None
        self._RewindMsgNum = None
        self._MinMsgTime = None
        self._Transaction = None
        self._DeadLetterSource = None
        self._DeadLetterPolicy = None
        self._TransactionPolicy = None
        self._CreateUin = None
        self._Tags = None
        self._Trace = None

    @property
    def QueueId(self):
        return self._QueueId

    @QueueId.setter
    def QueueId(self, QueueId):
        self._QueueId = QueueId

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def Qps(self):
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def Bps(self):
        return self._Bps

    @Bps.setter
    def Bps(self, Bps):
        self._Bps = Bps

    @property
    def MaxDelaySeconds(self):
        return self._MaxDelaySeconds

    @MaxDelaySeconds.setter
    def MaxDelaySeconds(self, MaxDelaySeconds):
        self._MaxDelaySeconds = MaxDelaySeconds

    @property
    def MaxMsgHeapNum(self):
        return self._MaxMsgHeapNum

    @MaxMsgHeapNum.setter
    def MaxMsgHeapNum(self, MaxMsgHeapNum):
        self._MaxMsgHeapNum = MaxMsgHeapNum

    @property
    def PollingWaitSeconds(self):
        return self._PollingWaitSeconds

    @PollingWaitSeconds.setter
    def PollingWaitSeconds(self, PollingWaitSeconds):
        self._PollingWaitSeconds = PollingWaitSeconds

    @property
    def MsgRetentionSeconds(self):
        return self._MsgRetentionSeconds

    @MsgRetentionSeconds.setter
    def MsgRetentionSeconds(self, MsgRetentionSeconds):
        self._MsgRetentionSeconds = MsgRetentionSeconds

    @property
    def VisibilityTimeout(self):
        return self._VisibilityTimeout

    @VisibilityTimeout.setter
    def VisibilityTimeout(self, VisibilityTimeout):
        self._VisibilityTimeout = VisibilityTimeout

    @property
    def MaxMsgSize(self):
        return self._MaxMsgSize

    @MaxMsgSize.setter
    def MaxMsgSize(self, MaxMsgSize):
        self._MaxMsgSize = MaxMsgSize

    @property
    def RewindSeconds(self):
        return self._RewindSeconds

    @RewindSeconds.setter
    def RewindSeconds(self, RewindSeconds):
        self._RewindSeconds = RewindSeconds

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastModifyTime(self):
        return self._LastModifyTime

    @LastModifyTime.setter
    def LastModifyTime(self, LastModifyTime):
        self._LastModifyTime = LastModifyTime

    @property
    def ActiveMsgNum(self):
        return self._ActiveMsgNum

    @ActiveMsgNum.setter
    def ActiveMsgNum(self, ActiveMsgNum):
        self._ActiveMsgNum = ActiveMsgNum

    @property
    def InactiveMsgNum(self):
        return self._InactiveMsgNum

    @InactiveMsgNum.setter
    def InactiveMsgNum(self, InactiveMsgNum):
        self._InactiveMsgNum = InactiveMsgNum

    @property
    def DelayMsgNum(self):
        return self._DelayMsgNum

    @DelayMsgNum.setter
    def DelayMsgNum(self, DelayMsgNum):
        self._DelayMsgNum = DelayMsgNum

    @property
    def RewindMsgNum(self):
        return self._RewindMsgNum

    @RewindMsgNum.setter
    def RewindMsgNum(self, RewindMsgNum):
        self._RewindMsgNum = RewindMsgNum

    @property
    def MinMsgTime(self):
        return self._MinMsgTime

    @MinMsgTime.setter
    def MinMsgTime(self, MinMsgTime):
        self._MinMsgTime = MinMsgTime

    @property
    def Transaction(self):
        return self._Transaction

    @Transaction.setter
    def Transaction(self, Transaction):
        self._Transaction = Transaction

    @property
    def DeadLetterSource(self):
        return self._DeadLetterSource

    @DeadLetterSource.setter
    def DeadLetterSource(self, DeadLetterSource):
        self._DeadLetterSource = DeadLetterSource

    @property
    def DeadLetterPolicy(self):
        return self._DeadLetterPolicy

    @DeadLetterPolicy.setter
    def DeadLetterPolicy(self, DeadLetterPolicy):
        self._DeadLetterPolicy = DeadLetterPolicy

    @property
    def TransactionPolicy(self):
        return self._TransactionPolicy

    @TransactionPolicy.setter
    def TransactionPolicy(self, TransactionPolicy):
        self._TransactionPolicy = TransactionPolicy

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Trace(self):
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace


    def _deserialize(self, params):
        self._QueueId = params.get("QueueId")
        self._QueueName = params.get("QueueName")
        self._Qps = params.get("Qps")
        self._Bps = params.get("Bps")
        self._MaxDelaySeconds = params.get("MaxDelaySeconds")
        self._MaxMsgHeapNum = params.get("MaxMsgHeapNum")
        self._PollingWaitSeconds = params.get("PollingWaitSeconds")
        self._MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self._VisibilityTimeout = params.get("VisibilityTimeout")
        self._MaxMsgSize = params.get("MaxMsgSize")
        self._RewindSeconds = params.get("RewindSeconds")
        self._CreateTime = params.get("CreateTime")
        self._LastModifyTime = params.get("LastModifyTime")
        self._ActiveMsgNum = params.get("ActiveMsgNum")
        self._InactiveMsgNum = params.get("InactiveMsgNum")
        self._DelayMsgNum = params.get("DelayMsgNum")
        self._RewindMsgNum = params.get("RewindMsgNum")
        self._MinMsgTime = params.get("MinMsgTime")
        self._Transaction = params.get("Transaction")
        if params.get("DeadLetterSource") is not None:
            self._DeadLetterSource = []
            for item in params.get("DeadLetterSource"):
                obj = DeadLetterSource()
                obj._deserialize(item)
                self._DeadLetterSource.append(obj)
        if params.get("DeadLetterPolicy") is not None:
            self._DeadLetterPolicy = DeadLetterPolicy()
            self._DeadLetterPolicy._deserialize(params.get("DeadLetterPolicy"))
        if params.get("TransactionPolicy") is not None:
            self._TransactionPolicy = TransactionPolicy()
            self._TransactionPolicy._deserialize(params.get("TransactionPolicy"))
        self._CreateUin = params.get("CreateUin")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RewindQueueRequest(AbstractModel):
    """RewindQueue request structure.

    """

    def __init__(self):
        r"""
        :param _QueueName: Queue name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).
        :type QueueName: str
        :param _StartConsumeTime: After this time is set, the `(Batch)receiveMessage` API will consume the messages received after this timestamp in the order in which they are produced.
        :type StartConsumeTime: int
        """
        self._QueueName = None
        self._StartConsumeTime = None

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def StartConsumeTime(self):
        return self._StartConsumeTime

    @StartConsumeTime.setter
    def StartConsumeTime(self, StartConsumeTime):
        self._StartConsumeTime = StartConsumeTime


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        self._StartConsumeTime = params.get("StartConsumeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RewindQueueResponse(AbstractModel):
    """RewindQueue response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Subscription(AbstractModel):
    """Subscription response parameter

    """

    def __init__(self):
        r"""
        :param _SubscriptionName: SubscriptionName
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubscriptionName: str
        :param _SubscriptionId: SubscriptionId
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubscriptionId: str
        :param _TopicOwner: TopicOwner
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicOwner: int
        :param _MsgCount: MsgCount
Note: this field may return null, indicating that no valid values can be obtained.
        :type MsgCount: int
        :param _LastModifyTime: LastModifyTime
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastModifyTime: int
        :param _CreateTime: CreateTime
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: int
        :param _BindingKey: BindingKey
Note: this field may return null, indicating that no valid values can be obtained.
        :type BindingKey: list of str
        :param _Endpoint: Endpoint
Note: this field may return null, indicating that no valid values can be obtained.
        :type Endpoint: str
        :param _FilterTags: FilterTags
Note: this field may return null, indicating that no valid values can be obtained.
        :type FilterTags: list of str
        :param _Protocol: Protocol
Note: this field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param _NotifyStrategy: NotifyStrategy
Note: this field may return null, indicating that no valid values can be obtained.
        :type NotifyStrategy: str
        :param _NotifyContentFormat: NotifyContentFormat
Note: this field may return null, indicating that no valid values can be obtained.
        :type NotifyContentFormat: str
        """
        self._SubscriptionName = None
        self._SubscriptionId = None
        self._TopicOwner = None
        self._MsgCount = None
        self._LastModifyTime = None
        self._CreateTime = None
        self._BindingKey = None
        self._Endpoint = None
        self._FilterTags = None
        self._Protocol = None
        self._NotifyStrategy = None
        self._NotifyContentFormat = None

    @property
    def SubscriptionName(self):
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName

    @property
    def SubscriptionId(self):
        return self._SubscriptionId

    @SubscriptionId.setter
    def SubscriptionId(self, SubscriptionId):
        self._SubscriptionId = SubscriptionId

    @property
    def TopicOwner(self):
        return self._TopicOwner

    @TopicOwner.setter
    def TopicOwner(self, TopicOwner):
        self._TopicOwner = TopicOwner

    @property
    def MsgCount(self):
        return self._MsgCount

    @MsgCount.setter
    def MsgCount(self, MsgCount):
        self._MsgCount = MsgCount

    @property
    def LastModifyTime(self):
        return self._LastModifyTime

    @LastModifyTime.setter
    def LastModifyTime(self, LastModifyTime):
        self._LastModifyTime = LastModifyTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def BindingKey(self):
        return self._BindingKey

    @BindingKey.setter
    def BindingKey(self, BindingKey):
        self._BindingKey = BindingKey

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def FilterTags(self):
        return self._FilterTags

    @FilterTags.setter
    def FilterTags(self, FilterTags):
        self._FilterTags = FilterTags

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def NotifyStrategy(self):
        return self._NotifyStrategy

    @NotifyStrategy.setter
    def NotifyStrategy(self, NotifyStrategy):
        self._NotifyStrategy = NotifyStrategy

    @property
    def NotifyContentFormat(self):
        return self._NotifyContentFormat

    @NotifyContentFormat.setter
    def NotifyContentFormat(self, NotifyContentFormat):
        self._NotifyContentFormat = NotifyContentFormat


    def _deserialize(self, params):
        self._SubscriptionName = params.get("SubscriptionName")
        self._SubscriptionId = params.get("SubscriptionId")
        self._TopicOwner = params.get("TopicOwner")
        self._MsgCount = params.get("MsgCount")
        self._LastModifyTime = params.get("LastModifyTime")
        self._CreateTime = params.get("CreateTime")
        self._BindingKey = params.get("BindingKey")
        self._Endpoint = params.get("Endpoint")
        self._FilterTags = params.get("FilterTags")
        self._Protocol = params.get("Protocol")
        self._NotifyStrategy = params.get("NotifyStrategy")
        self._NotifyContentFormat = params.get("NotifyContentFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag

    """

    def __init__(self):
        r"""
        :param _TagKey: Tag key
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagKey: str
        :param _TagValue: Tag value
Note: this field may return null, indicating that no valid values can be obtained.
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicSet(AbstractModel):
    """Field for displaying returned topic information

    """

    def __init__(self):
        r"""
        :param _TopicId: TopicId
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicId: str
        :param _TopicName: TopicName
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicName: str
        :param _MsgRetentionSeconds: MsgRetentionSeconds
Note: this field may return null, indicating that no valid values can be obtained.
        :type MsgRetentionSeconds: int
        :param _MaxMsgSize: MaxMsgSize
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxMsgSize: int
        :param _Qps: Qps
Note: this field may return null, indicating that no valid values can be obtained.
        :type Qps: int
        :param _FilterType: FilterType
Note: this field may return null, indicating that no valid values can be obtained.
        :type FilterType: int
        :param _CreateTime: CreateTime
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: int
        :param _LastModifyTime: LastModifyTime
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastModifyTime: int
        :param _MsgCount: MsgCount
Note: this field may return null, indicating that no valid values can be obtained.
        :type MsgCount: int
        :param _CreateUin: CreateUin
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateUin: int
        :param _Tags: Tags
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _Trace: Whether to enable message trace for a topic. true: yes, false: no
Note: this field may return null, indicating that no valid values can be obtained.
        :type Trace: bool
        """
        self._TopicId = None
        self._TopicName = None
        self._MsgRetentionSeconds = None
        self._MaxMsgSize = None
        self._Qps = None
        self._FilterType = None
        self._CreateTime = None
        self._LastModifyTime = None
        self._MsgCount = None
        self._CreateUin = None
        self._Tags = None
        self._Trace = None

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def MsgRetentionSeconds(self):
        return self._MsgRetentionSeconds

    @MsgRetentionSeconds.setter
    def MsgRetentionSeconds(self, MsgRetentionSeconds):
        self._MsgRetentionSeconds = MsgRetentionSeconds

    @property
    def MaxMsgSize(self):
        return self._MaxMsgSize

    @MaxMsgSize.setter
    def MaxMsgSize(self, MaxMsgSize):
        self._MaxMsgSize = MaxMsgSize

    @property
    def Qps(self):
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def FilterType(self):
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastModifyTime(self):
        return self._LastModifyTime

    @LastModifyTime.setter
    def LastModifyTime(self, LastModifyTime):
        self._LastModifyTime = LastModifyTime

    @property
    def MsgCount(self):
        return self._MsgCount

    @MsgCount.setter
    def MsgCount(self, MsgCount):
        self._MsgCount = MsgCount

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Trace(self):
        return self._Trace

    @Trace.setter
    def Trace(self, Trace):
        self._Trace = Trace


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self._MaxMsgSize = params.get("MaxMsgSize")
        self._Qps = params.get("Qps")
        self._FilterType = params.get("FilterType")
        self._CreateTime = params.get("CreateTime")
        self._LastModifyTime = params.get("LastModifyTime")
        self._MsgCount = params.get("MsgCount")
        self._CreateUin = params.get("CreateUin")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransactionPolicy(AbstractModel):
    """TransactionPolicy

    """

    def __init__(self):
        r"""
        :param _FirstQueryInterval: FirstQueryInterval
Note: this field may return null, indicating that no valid values can be obtained.
        :type FirstQueryInterval: int
        :param _MaxQueryCount: MaxQueryCount
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxQueryCount: int
        """
        self._FirstQueryInterval = None
        self._MaxQueryCount = None

    @property
    def FirstQueryInterval(self):
        return self._FirstQueryInterval

    @FirstQueryInterval.setter
    def FirstQueryInterval(self, FirstQueryInterval):
        self._FirstQueryInterval = FirstQueryInterval

    @property
    def MaxQueryCount(self):
        return self._MaxQueryCount

    @MaxQueryCount.setter
    def MaxQueryCount(self, MaxQueryCount):
        self._MaxQueryCount = MaxQueryCount


    def _deserialize(self, params):
        self._FirstQueryInterval = params.get("FirstQueryInterval")
        self._MaxQueryCount = params.get("MaxQueryCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindDeadLetterRequest(AbstractModel):
    """UnbindDeadLetter request structure.

    """

    def __init__(self):
        r"""
        :param _QueueName: Source queue name of dead letter policy. Calling this API will clear the dead letter queue policy of this queue.
        :type QueueName: str
        """
        self._QueueName = None

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindDeadLetterResponse(AbstractModel):
    """UnbindDeadLetter response structure.

    """

    def __init__(self):
        r"""
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")