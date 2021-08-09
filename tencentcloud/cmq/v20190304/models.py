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
        """
        :param QueueName: Queue name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).\n        :type QueueName: str\n        """
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearQueueResponse(AbstractModel):
    """ClearQueue response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ClearSubscriptionFilterTagsRequest(AbstractModel):
    """ClearSubscriptionFilterTags request structure.

    """

    def __init__(self):
        """
        :param TopicName: Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).\n        :type TopicName: str\n        :param SubscriptionName: Subscription name, which is unique in the same topic under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).\n        :type SubscriptionName: str\n        """
        self.TopicName = None
        self.SubscriptionName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearSubscriptionFilterTagsResponse(AbstractModel):
    """ClearSubscriptionFilterTags response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateQueueRequest(AbstractModel):
    """CreateQueue request structure.

    """

    def __init__(self):
        """
        :param QueueName: Queue name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).\n        :type QueueName: str\n        :param MaxMsgHeapNum: Maximum number of heaped messages. The value range is 1,000,000–10,000,000 during the beta test and can be 1,000,000–1,000,000,000 after the product is officially released. The default value is 10,000,000 during the beta test and will be 100,000,000 after the product is officially released.\n        :type MaxMsgHeapNum: int\n        :param PollingWaitSeconds: Long polling wait time for message reception. Value range: 0–30 seconds. Default value: 0.\n        :type PollingWaitSeconds: int\n        :param VisibilityTimeout: Message visibility timeout period. Value range: 1–43200 seconds (i.e., 12 hours). Default value: 30.\n        :type VisibilityTimeout: int\n        :param MaxMsgSize: Maximum message length. Value range: 1024–65536 bytes (i.e., 1–64 KB). Default value: 65536.\n        :type MaxMsgSize: int\n        :param MsgRetentionSeconds: Message retention period. Value range: 60–1296000 seconds (i.e., 1 minute–15 days). Default value: 345600 (i.e., 4 days).\n        :type MsgRetentionSeconds: int\n        :param RewindSeconds: Whether to enable the message rewinding feature for a queue. Value range: 0–msgRetentionSeconds, where 0 means not to enable this feature, while `msgRetentionSeconds` indicates that the maximum rewindable period is the message retention period of the queue.\n        :type RewindSeconds: int\n        :param Transaction: 1: transaction queue, 0: general queue\n        :type Transaction: int\n        :param FirstQueryInterval: First lookback interval\n        :type FirstQueryInterval: int\n        :param MaxQueryCount: Maximum number of lookbacks\n        :type MaxQueryCount: int\n        :param DeadLetterQueueName: Dead letter queue name\n        :type DeadLetterQueueName: str\n        :param Policy: Dead letter policy. 0: message has been consumed multiple times but not deleted, 1: `Time-To-Live` has elapsed\n        :type Policy: int\n        :param MaxReceiveCount: Maximum receipt times. Value range: 1–1000\n        :type MaxReceiveCount: int\n        :param MaxTimeToLive: Maximum period in seconds before an unconsumed message expires, which is required if `policy` is 1. Value range: 300–43200. This value should be smaller than `msgRetentionSeconds` (maximum message retention period)\n        :type MaxTimeToLive: int\n        :param Trace: Whether to enable message trace. true: yes, false: no. If this field is not set, the feature will not be enabled\n        :type Trace: bool\n        """
        self.QueueName = None
        self.MaxMsgHeapNum = None
        self.PollingWaitSeconds = None
        self.VisibilityTimeout = None
        self.MaxMsgSize = None
        self.MsgRetentionSeconds = None
        self.RewindSeconds = None
        self.Transaction = None
        self.FirstQueryInterval = None
        self.MaxQueryCount = None
        self.DeadLetterQueueName = None
        self.Policy = None
        self.MaxReceiveCount = None
        self.MaxTimeToLive = None
        self.Trace = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        self.MaxMsgHeapNum = params.get("MaxMsgHeapNum")
        self.PollingWaitSeconds = params.get("PollingWaitSeconds")
        self.VisibilityTimeout = params.get("VisibilityTimeout")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.RewindSeconds = params.get("RewindSeconds")
        self.Transaction = params.get("Transaction")
        self.FirstQueryInterval = params.get("FirstQueryInterval")
        self.MaxQueryCount = params.get("MaxQueryCount")
        self.DeadLetterQueueName = params.get("DeadLetterQueueName")
        self.Policy = params.get("Policy")
        self.MaxReceiveCount = params.get("MaxReceiveCount")
        self.MaxTimeToLive = params.get("MaxTimeToLive")
        self.Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateQueueResponse(AbstractModel):
    """CreateQueue response structure.

    """

    def __init__(self):
        """
        :param QueueId: `queueId` of a successfully created queue\n        :type QueueId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.QueueId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.QueueId = params.get("QueueId")
        self.RequestId = params.get("RequestId")


class CreateSubscribeRequest(AbstractModel):
    """CreateSubscribe request structure.

    """

    def __init__(self):
        """
        :param TopicName: Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).\n        :type TopicName: str\n        :param SubscriptionName: Subscription name, which is unique in the same topic under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).\n        :type SubscriptionName: str\n        :param Protocol: Subscription protocol. Currently, two protocols are supported: http and queue. To use the `http` protocol, you need to build your own web server to receive messages. With the `queue` protocol, messages are automatically pushed to a CMQ queue and you can pull them concurrently.\n        :type Protocol: str\n        :param Endpoint: `Endpoint` for notification receipt, which is distinguished by `Protocol`. For `http`, `Endpoint` must begin with `http://` and `host` can be a domain name or IP. For `Queue`, enter `QueueName`. Please note that currently the push service cannot push messages to a VPC; therefore, if a VPC domain name or address is entered for `Endpoint`, pushed messages will not be received. Currently, messages can be pushed only to the public network and basic network.\n        :type Endpoint: str\n        :param NotifyStrategy: CMQ push server retry policy in case an error occurs while pushing a message to `Endpoint`. Valid values: 1. BACKOFF_RETRY: backoff retry, which is to retry at a fixed interval, discard the message after a certain number of retries, and continue to push the next message; 2. EXPONENTIAL_DECAY_RETRY: exponential decay retry, which is to retry at an exponentially increasing interval, such as 1s, 2s, 4s, 8s, and so on. As a message can be retained in a topic for one day, failed messages will be discarded at most after one day of retry. Default value: EXPONENTIAL_DECAY_RETRY.\n        :type NotifyStrategy: str\n        :param FilterTag: Message body tag (used for message filtering). The number of tags cannot exceed 5, and each tag can contain up to 16 characters. It is used in conjunction with the `MsgTag` parameter of `(Batch)PublishMessage`. Rules: 1. If `FilterTag` is not set, no matter whether `MsgTag` is set, the subscription will receive all messages published to the topic; 2. If the `FilterTag` array has a value, only when at least one of the values in the array also exists in the `MsgTag` array (i.e., `FilterTag` and `MsgTag` have an intersection) can the subscription receive messages published to the topic; 3. If the `FilterTag` array has a value, but `MsgTag` is not set, then no message published to the topic will be received, which can be considered as a special case of rule 2 as `FilterTag` and `MsgTag` do not intersect in this case. The overall design idea of rules is based on the intention of the subscriber.\n        :type FilterTag: list of str\n        :param BindingKey: The number of `BindingKey` cannot exceed 5, and the length of each `BindingKey` cannot exceed 64 bytes. This field indicates the filtering policy for subscribing to and receiving messages. Each `BindingKey` can contain up to 15 `.`, i.e., up to 16 phrases.\n        :type BindingKey: list of str\n        :param NotifyContentFormat: Push content format. Valid values: 1. JSON, 2. SIMPLIFIED, i.e., the raw format. If `Protocol` is `queue`, this value must be `SIMPLIFIED`. If `Protocol` is `http`, both options are acceptable, and the default value is `JSON`.\n        :type NotifyContentFormat: str\n        """
        self.TopicName = None
        self.SubscriptionName = None
        self.Protocol = None
        self.Endpoint = None
        self.NotifyStrategy = None
        self.FilterTag = None
        self.BindingKey = None
        self.NotifyContentFormat = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")
        self.Protocol = params.get("Protocol")
        self.Endpoint = params.get("Endpoint")
        self.NotifyStrategy = params.get("NotifyStrategy")
        self.FilterTag = params.get("FilterTag")
        self.BindingKey = params.get("BindingKey")
        self.NotifyContentFormat = params.get("NotifyContentFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubscribeResponse(AbstractModel):
    """CreateSubscribe response structure.

    """

    def __init__(self):
        """
        :param SubscriptionId: SubscriptionId\n        :type SubscriptionId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.SubscriptionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubscriptionId = params.get("SubscriptionId")
        self.RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic request structure.

    """

    def __init__(self):
        """
        :param TopicName: Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).\n        :type TopicName: str\n        :param MaxMsgSize: Maximum message length. Value range: 1024–65536 bytes (i.e., 1–64 KB). Default value: 65536.\n        :type MaxMsgSize: int\n        :param FilterType: Message match policy for a specified topic.\n        :type FilterType: int\n        :param MsgRetentionSeconds: Message retention period. Value range: 60–86400 seconds (i.e., 1 minute–1 day). Default value: 86400.\n        :type MsgRetentionSeconds: int\n        :param Trace: Whether to enable message trace. true: yes, false: no. If this field is left empty, the feature will not be enabled.\n        :type Trace: bool\n        """
        self.TopicName = None
        self.MaxMsgSize = None
        self.FilterType = None
        self.MsgRetentionSeconds = None
        self.Trace = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.FilterType = params.get("FilterType")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResponse(AbstractModel):
    """CreateTopic response structure.

    """

    def __init__(self):
        """
        :param TopicId: TopicName\n        :type TopicId: str\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TopicId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.RequestId = params.get("RequestId")


class DeadLetterPolicy(AbstractModel):
    """DeadLetterPolicy

    """

    def __init__(self):
        """
        :param DeadLetterQueueName: DeadLetterQueueName
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DeadLetterQueueName: str\n        :param DeadLetterQueue: DeadLetterQueue
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DeadLetterQueue: str\n        :param Policy: Policy
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Policy: int\n        :param MaxTimeToLive: MaxTimeToLive
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MaxTimeToLive: int\n        :param MaxReceiveCount: MaxReceiveCount
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MaxReceiveCount: int\n        """
        self.DeadLetterQueueName = None
        self.DeadLetterQueue = None
        self.Policy = None
        self.MaxTimeToLive = None
        self.MaxReceiveCount = None


    def _deserialize(self, params):
        self.DeadLetterQueueName = params.get("DeadLetterQueueName")
        self.DeadLetterQueue = params.get("DeadLetterQueue")
        self.Policy = params.get("Policy")
        self.MaxTimeToLive = params.get("MaxTimeToLive")
        self.MaxReceiveCount = params.get("MaxReceiveCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeadLetterSource(AbstractModel):
    """DeadLetterSource

    """

    def __init__(self):
        """
        :param QueueId: QueueId
Note: this field may return null, indicating that no valid values can be obtained.\n        :type QueueId: str\n        :param QueueName: QueueName
Note: this field may return null, indicating that no valid values can be obtained.\n        :type QueueName: str\n        """
        self.QueueId = None
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueId = params.get("QueueId")
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteQueueRequest(AbstractModel):
    """DeleteQueue request structure.

    """

    def __init__(self):
        """
        :param QueueName: Queue name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).\n        :type QueueName: str\n        """
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteQueueResponse(AbstractModel):
    """DeleteQueue response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSubscribeRequest(AbstractModel):
    """DeleteSubscribe request structure.

    """

    def __init__(self):
        """
        :param TopicName: Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).\n        :type TopicName: str\n        :param SubscriptionName: Subscription name, which is unique in the same topic under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).\n        :type SubscriptionName: str\n        """
        self.TopicName = None
        self.SubscriptionName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSubscribeResponse(AbstractModel):
    """DeleteSubscribe response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTopicRequest(AbstractModel):
    """DeleteTopic request structure.

    """

    def __init__(self):
        """
        :param TopicName: Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).\n        :type TopicName: str\n        """
        self.TopicName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicResponse(AbstractModel):
    """DeleteTopic response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDeadLetterSourceQueuesRequest(AbstractModel):
    """DescribeDeadLetterSourceQueues request structure.

    """

    def __init__(self):
        """
        :param DeadLetterQueueName: Dead letter queue name\n        :type DeadLetterQueueName: str\n        :param Limit: Starting position of topic list to be returned on the current page in case of paginated return. If a value is entered, `limit` is required. If this parameter is left empty, 0 will be used by default.\n        :type Limit: int\n        :param Offset: Number of topics to be returned per page in case of paginated return. If this parameter is not passed in, 20 will be used by default. Maximum value: 50.\n        :type Offset: int\n        :param Filters: Filters source queue name of dead letter queue. Currently, only filtering by `SourceQueueName` is supported\n        :type Filters: list of Filter\n        """
        self.DeadLetterQueueName = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.DeadLetterQueueName = params.get("DeadLetterQueueName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeadLetterSourceQueuesResponse(AbstractModel):
    """DescribeDeadLetterSourceQueues response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible queues\n        :type TotalCount: int\n        :param QueueSet: Source queues of dead letter queue\n        :type QueueSet: list of DeadLetterSource\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.QueueSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("QueueSet") is not None:
            self.QueueSet = []
            for item in params.get("QueueSet"):
                obj = DeadLetterSource()
                obj._deserialize(item)
                self.QueueSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeQueueDetailRequest(AbstractModel):
    """DescribeQueueDetail request structure.

    """

    def __init__(self):
        """
        :param Offset: Starting position of queue list to be returned on the current page in case of paginated return. If a value is entered, `limit` is required. If this parameter is left empty, 0 will be used by default\n        :type Offset: int\n        :param Limit: Number of queues to be returned per page in case of paginated return. If this parameter is not passed in, 20 will be used by default. Maximum value: 50.\n        :type Limit: int\n        :param Filters: Filter parameter. Currently, filtering by `QueueName` is supported, and only one keyword is allowed\n        :type Filters: list of Filter\n        :param TagKey: Tag search\n        :type TagKey: str\n        :param QueueName: Exact match by `QueueName`\n        :type QueueName: str\n        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.TagKey = None
        self.QueueName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.TagKey = params.get("TagKey")
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQueueDetailResponse(AbstractModel):
    """DescribeQueueDetail response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of queues\n        :type TotalCount: int\n        :param QueueSet: Queue list\n        :type QueueSet: list of QueueSet\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.QueueSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("QueueSet") is not None:
            self.QueueSet = []
            for item in params.get("QueueSet"):
                obj = QueueSet()
                obj._deserialize(item)
                self.QueueSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubscriptionDetailRequest(AbstractModel):
    """DescribeSubscriptionDetail request structure.

    """

    def __init__(self):
        """
        :param TopicName: Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).\n        :type TopicName: str\n        :param Offset: Starting position of topic list to be returned on the current page in case of paginated return. If a value is entered, `limit` is required. If this parameter is left empty, 0 will be used by default\n        :type Offset: int\n        :param Limit: Number of topics to be returned per page in case of paginated return. If this parameter is not passed in, 20 will be used by default. Maximum value: 50.\n        :type Limit: int\n        :param Filters: Filter parameter. Currently, only filtering by `SubscriptionName` is supported, and only one keyword is allowed.\n        :type Filters: list of Filter\n        """
        self.TopicName = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubscriptionDetailResponse(AbstractModel):
    """DescribeSubscriptionDetail response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number\n        :type TotalCount: int\n        :param SubscriptionSet: Subscription attribute set
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SubscriptionSet: list of Subscription\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.SubscriptionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SubscriptionSet") is not None:
            self.SubscriptionSet = []
            for item in params.get("SubscriptionSet"):
                obj = Subscription()
                obj._deserialize(item)
                self.SubscriptionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTopicDetailRequest(AbstractModel):
    """DescribeTopicDetail request structure.

    """

    def __init__(self):
        """
        :param Offset: Starting position of queue list to be returned on the current page in case of paginated return. If a value is entered, `limit` is required. If this parameter is left empty, 0 will be used by default.\n        :type Offset: int\n        :param Limit: Number of queues to be returned per page in case of paginated return. If this parameter is not passed in, 20 will be used by default. Maximum value: 50.\n        :type Limit: int\n        :param Filters: Currently, only filtering by `TopicName` is supported, and only one filter value can be entered\n        :type Filters: list of Filter\n        :param TagKey: Tag match\n        :type TagKey: str\n        :param TopicName: Exact match by `TopicName`\n        :type TopicName: str\n        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.TagKey = None
        self.TopicName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.TagKey = params.get("TagKey")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicDetailResponse(AbstractModel):
    """DescribeTopicDetail response structure.

    """

    def __init__(self):
        """
        :param TotalCount: TotalCount\n        :type TotalCount: int\n        :param TopicSet: TopicSet\n        :type TopicSet: list of TopicSet\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.TopicSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TopicSet") is not None:
            self.TopicSet = []
            for item in params.get("TopicSet"):
                obj = TopicSet()
                obj._deserialize(item)
                self.TopicSet.append(obj)
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """Filter parameter

    """

    def __init__(self):
        """
        :param Name: Filter parameter name\n        :type Name: str\n        :param Values: Value\n        :type Values: list of str\n        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyQueueAttributeRequest(AbstractModel):
    """ModifyQueueAttribute request structure.

    """

    def __init__(self):
        """
        :param QueueName: Queue name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).\n        :type QueueName: str\n        :param MaxMsgHeapNum: Maximum number of heaped messages. The value range is 1,000,000–10,000,000 during the beta test and can be 1,000,000–1,000,000,000 after the product is officially released. The default value is 10,000,000 during the beta test and will be 100,000,000 after the product is officially released.\n        :type MaxMsgHeapNum: int\n        :param PollingWaitSeconds: Long polling wait time for message reception. Value range: 0–30 seconds. Default value: 0.\n        :type PollingWaitSeconds: int\n        :param VisibilityTimeout: Message visibility timeout period. Value range: 1–43200 seconds (i.e., 12 hours). Default value: 30.\n        :type VisibilityTimeout: int\n        :param MaxMsgSize: Maximum message length. Value range: 1024–65536 bytes (i.e., 1–64 KB). Default value: 65536.\n        :type MaxMsgSize: int\n        :param MsgRetentionSeconds: Message retention period. Value range: 60–1296000 seconds (i.e., 1 minute–15 days). Default value: 345600 (i.e., 4 days).\n        :type MsgRetentionSeconds: int\n        :param RewindSeconds: Maximum message rewindable period. Value range: 0–msgRetentionSeconds (maximum message retention period of a queue). 0 means not to enable message rewinding.\n        :type RewindSeconds: int\n        :param FirstQueryInterval: First query time\n        :type FirstQueryInterval: int\n        :param MaxQueryCount: Maximum number of queries\n        :type MaxQueryCount: int\n        :param DeadLetterQueueName: Dead letter queue name\n        :type DeadLetterQueueName: str\n        :param MaxTimeToLive: Maximum period in seconds before an unconsumed message expires, which is required if `MaxTimeToLivepolicy` is 1. Value range: 300–43200. This value should be smaller than `MsgRetentionSeconds` (maximum message retention period)\n        :type MaxTimeToLive: int\n        :param MaxReceiveCount: Maximum number of receipts\n        :type MaxReceiveCount: int\n        :param Policy: Dead letter queue policy\n        :type Policy: int\n        :param Trace: Whether to enable message trace. true: yes, false: no. If this field is left empty, the feature will not be enabled.\n        :type Trace: bool\n        """
        self.QueueName = None
        self.MaxMsgHeapNum = None
        self.PollingWaitSeconds = None
        self.VisibilityTimeout = None
        self.MaxMsgSize = None
        self.MsgRetentionSeconds = None
        self.RewindSeconds = None
        self.FirstQueryInterval = None
        self.MaxQueryCount = None
        self.DeadLetterQueueName = None
        self.MaxTimeToLive = None
        self.MaxReceiveCount = None
        self.Policy = None
        self.Trace = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        self.MaxMsgHeapNum = params.get("MaxMsgHeapNum")
        self.PollingWaitSeconds = params.get("PollingWaitSeconds")
        self.VisibilityTimeout = params.get("VisibilityTimeout")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.RewindSeconds = params.get("RewindSeconds")
        self.FirstQueryInterval = params.get("FirstQueryInterval")
        self.MaxQueryCount = params.get("MaxQueryCount")
        self.DeadLetterQueueName = params.get("DeadLetterQueueName")
        self.MaxTimeToLive = params.get("MaxTimeToLive")
        self.MaxReceiveCount = params.get("MaxReceiveCount")
        self.Policy = params.get("Policy")
        self.Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyQueueAttributeResponse(AbstractModel):
    """ModifyQueueAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubscriptionAttributeRequest(AbstractModel):
    """ModifySubscriptionAttribute request structure.

    """

    def __init__(self):
        """
        :param TopicName: Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).\n        :type TopicName: str\n        :param SubscriptionName: Subscription name, which is unique in the same topic under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).\n        :type SubscriptionName: str\n        :param NotifyStrategy: CMQ push server retry policy in case an error occurs while pushing a message to `Endpoint`. Valid values:
1. BACKOFF_RETRY: backoff retry, which is to retry at a fixed interval, discard the message after a certain number of retries, and continue to push the next message.
2. EXPONENTIAL_DECAY_RETRY: exponential decay retry, which is to retry at an exponentially increasing interval, such as 1s, 2s, 4s, 8s, and so on. As a message can be retained in a topic for one day, failed messages will be discarded at most after one day of retry. Default value: EXPONENTIAL_DECAY_RETRY.\n        :type NotifyStrategy: str\n        :param NotifyContentFormat: Push content format. Valid values: 1. JSON, 2. SIMPLIFIED, i.e., the raw format. If `Protocol` is `queue`, this value must be `SIMPLIFIED`. If `Protocol` is `HTTP`, both options are acceptable, and the default value is `JSON`.\n        :type NotifyContentFormat: str\n        :param FilterTags: Message body tag (used for message filtering). The number of tags cannot exceed 5, and each tag can contain up to 16 characters. It is used in conjunction with the `MsgTag` parameter of `(Batch)PublishMessage`. Rules: 1. If `FilterTag` is not set, no matter whether `MsgTag` is set, the subscription will receive all messages published to the topic; 2. If the `FilterTag` array has a value, only when at least one of the values in the array also exists in the `MsgTag` array (i.e., `FilterTag` and `MsgTag` have an intersection) can the subscription receive messages published to the topic; 3. If the `FilterTag` array has a value, but `MsgTag` is not set, then no message published to the topic will be received, which can be considered as a special case of rule 2 as `FilterTag` and `MsgTag` do not intersect in this case. The overall design idea of rules is based on the intention of the subscriber.\n        :type FilterTags: list of str\n        :param BindingKey: The number of `BindingKey` cannot exceed 5, and the length of each `BindingKey` cannot exceed 64 bytes. This field indicates the filtering policy for subscribing to and receiving messages. Each `BindingKey` can contain up to 15 `.`, i.e., up to 16 phrases.\n        :type BindingKey: list of str\n        """
        self.TopicName = None
        self.SubscriptionName = None
        self.NotifyStrategy = None
        self.NotifyContentFormat = None
        self.FilterTags = None
        self.BindingKey = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")
        self.NotifyStrategy = params.get("NotifyStrategy")
        self.NotifyContentFormat = params.get("NotifyContentFormat")
        self.FilterTags = params.get("FilterTags")
        self.BindingKey = params.get("BindingKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubscriptionAttributeResponse(AbstractModel):
    """ModifySubscriptionAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTopicAttributeRequest(AbstractModel):
    """ModifyTopicAttribute request structure.

    """

    def __init__(self):
        """
        :param TopicName: Topic name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).\n        :type TopicName: str\n        :param MaxMsgSize: Maximum message length. Value range: 1024–65536 bytes (i.e., 1–64 KB). Default value: 65536.\n        :type MaxMsgSize: int\n        :param MsgRetentionSeconds: Message retention period. Value range: 60–86400 seconds (i.e., 1 minute–1 day). Default value: 86400.\n        :type MsgRetentionSeconds: int\n        :param Trace: Whether to enable message trace. true: yes, false: no. If this field is left empty, the feature will not be enabled.\n        :type Trace: bool\n        """
        self.TopicName = None
        self.MaxMsgSize = None
        self.MsgRetentionSeconds = None
        self.Trace = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicAttributeResponse(AbstractModel):
    """ModifyTopicAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class QueueSet(AbstractModel):
    """Batch queue attribute information

    """

    def __init__(self):
        """
        :param QueueId: QueueId\n        :type QueueId: str\n        :param QueueName: QueueName\n        :type QueueName: str\n        :param Qps: Qps
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Qps: int\n        :param Bps: Bps
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Bps: int\n        :param MaxDelaySeconds: MaxDelaySeconds
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MaxDelaySeconds: int\n        :param MaxMsgHeapNum: MaxMsgHeapNum
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MaxMsgHeapNum: int\n        :param PollingWaitSeconds: PollingWaitSeconds
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PollingWaitSeconds: int\n        :param MsgRetentionSeconds: MsgRetentionSeconds
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MsgRetentionSeconds: int\n        :param VisibilityTimeout: VisibilityTimeout
Note: this field may return null, indicating that no valid values can be obtained.\n        :type VisibilityTimeout: int\n        :param MaxMsgSize: MaxMsgSize
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MaxMsgSize: int\n        :param RewindSeconds: RewindSeconds
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RewindSeconds: int\n        :param CreateTime: CreateTime
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CreateTime: int\n        :param LastModifyTime: LastModifyTime
Note: this field may return null, indicating that no valid values can be obtained.\n        :type LastModifyTime: int\n        :param ActiveMsgNum: ActiveMsgNum
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ActiveMsgNum: int\n        :param InactiveMsgNum: InactiveMsgNum
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InactiveMsgNum: int\n        :param DelayMsgNum: DelayMsgNum
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DelayMsgNum: int\n        :param RewindMsgNum: RewindMsgNum
Note: this field may return null, indicating that no valid values can be obtained.\n        :type RewindMsgNum: int\n        :param MinMsgTime: MinMsgTime
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MinMsgTime: int\n        :param Transaction: Transaction
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Transaction: bool\n        :param DeadLetterSource: DeadLetterSource
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DeadLetterSource: list of DeadLetterSource\n        :param DeadLetterPolicy: DeadLetterPolicy
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DeadLetterPolicy: :class:`tencentcloud.cmq.v20190304.models.DeadLetterPolicy`\n        :param TransactionPolicy: TransactionPolicy
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TransactionPolicy: :class:`tencentcloud.cmq.v20190304.models.TransactionPolicy`\n        :param CreateUin: Creator `uin`
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CreateUin: int\n        :param Tags: Tag
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Tags: list of Tag\n        :param Trace: Message trace flag. true: enabled, false: not enabled
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Trace: bool\n        """
        self.QueueId = None
        self.QueueName = None
        self.Qps = None
        self.Bps = None
        self.MaxDelaySeconds = None
        self.MaxMsgHeapNum = None
        self.PollingWaitSeconds = None
        self.MsgRetentionSeconds = None
        self.VisibilityTimeout = None
        self.MaxMsgSize = None
        self.RewindSeconds = None
        self.CreateTime = None
        self.LastModifyTime = None
        self.ActiveMsgNum = None
        self.InactiveMsgNum = None
        self.DelayMsgNum = None
        self.RewindMsgNum = None
        self.MinMsgTime = None
        self.Transaction = None
        self.DeadLetterSource = None
        self.DeadLetterPolicy = None
        self.TransactionPolicy = None
        self.CreateUin = None
        self.Tags = None
        self.Trace = None


    def _deserialize(self, params):
        self.QueueId = params.get("QueueId")
        self.QueueName = params.get("QueueName")
        self.Qps = params.get("Qps")
        self.Bps = params.get("Bps")
        self.MaxDelaySeconds = params.get("MaxDelaySeconds")
        self.MaxMsgHeapNum = params.get("MaxMsgHeapNum")
        self.PollingWaitSeconds = params.get("PollingWaitSeconds")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.VisibilityTimeout = params.get("VisibilityTimeout")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.RewindSeconds = params.get("RewindSeconds")
        self.CreateTime = params.get("CreateTime")
        self.LastModifyTime = params.get("LastModifyTime")
        self.ActiveMsgNum = params.get("ActiveMsgNum")
        self.InactiveMsgNum = params.get("InactiveMsgNum")
        self.DelayMsgNum = params.get("DelayMsgNum")
        self.RewindMsgNum = params.get("RewindMsgNum")
        self.MinMsgTime = params.get("MinMsgTime")
        self.Transaction = params.get("Transaction")
        if params.get("DeadLetterSource") is not None:
            self.DeadLetterSource = []
            for item in params.get("DeadLetterSource"):
                obj = DeadLetterSource()
                obj._deserialize(item)
                self.DeadLetterSource.append(obj)
        if params.get("DeadLetterPolicy") is not None:
            self.DeadLetterPolicy = DeadLetterPolicy()
            self.DeadLetterPolicy._deserialize(params.get("DeadLetterPolicy"))
        if params.get("TransactionPolicy") is not None:
            self.TransactionPolicy = TransactionPolicy()
            self.TransactionPolicy._deserialize(params.get("TransactionPolicy"))
        self.CreateUin = params.get("CreateUin")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RewindQueueRequest(AbstractModel):
    """RewindQueue request structure.

    """

    def __init__(self):
        """
        :param QueueName: Queue name, which is unique under the same account in an individual region. It is a string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).\n        :type QueueName: str\n        :param StartConsumeTime: After this time is set, the `(Batch)receiveMessage` API will consume the messages received after this timestamp in the order in which they are produced.\n        :type StartConsumeTime: int\n        """
        self.QueueName = None
        self.StartConsumeTime = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        self.StartConsumeTime = params.get("StartConsumeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RewindQueueResponse(AbstractModel):
    """RewindQueue response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Subscription(AbstractModel):
    """Subscription response parameter

    """

    def __init__(self):
        """
        :param SubscriptionName: SubscriptionName
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SubscriptionName: str\n        :param SubscriptionId: SubscriptionId
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SubscriptionId: str\n        :param TopicOwner: TopicOwner
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TopicOwner: int\n        :param MsgCount: MsgCount
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MsgCount: int\n        :param LastModifyTime: LastModifyTime
Note: this field may return null, indicating that no valid values can be obtained.\n        :type LastModifyTime: int\n        :param CreateTime: CreateTime
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CreateTime: int\n        :param BindingKey: BindingKey
Note: this field may return null, indicating that no valid values can be obtained.\n        :type BindingKey: list of str\n        :param Endpoint: Endpoint
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Endpoint: str\n        :param FilterTags: FilterTags
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FilterTags: list of str\n        :param Protocol: Protocol
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Protocol: str\n        :param NotifyStrategy: NotifyStrategy
Note: this field may return null, indicating that no valid values can be obtained.\n        :type NotifyStrategy: str\n        :param NotifyContentFormat: NotifyContentFormat
Note: this field may return null, indicating that no valid values can be obtained.\n        :type NotifyContentFormat: str\n        """
        self.SubscriptionName = None
        self.SubscriptionId = None
        self.TopicOwner = None
        self.MsgCount = None
        self.LastModifyTime = None
        self.CreateTime = None
        self.BindingKey = None
        self.Endpoint = None
        self.FilterTags = None
        self.Protocol = None
        self.NotifyStrategy = None
        self.NotifyContentFormat = None


    def _deserialize(self, params):
        self.SubscriptionName = params.get("SubscriptionName")
        self.SubscriptionId = params.get("SubscriptionId")
        self.TopicOwner = params.get("TopicOwner")
        self.MsgCount = params.get("MsgCount")
        self.LastModifyTime = params.get("LastModifyTime")
        self.CreateTime = params.get("CreateTime")
        self.BindingKey = params.get("BindingKey")
        self.Endpoint = params.get("Endpoint")
        self.FilterTags = params.get("FilterTags")
        self.Protocol = params.get("Protocol")
        self.NotifyStrategy = params.get("NotifyStrategy")
        self.NotifyContentFormat = params.get("NotifyContentFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag

    """

    def __init__(self):
        """
        :param TagKey: Tag key
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TagKey: str\n        :param TagValue: Tag value
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TagValue: str\n        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicSet(AbstractModel):
    """Field for displaying returned topic information

    """

    def __init__(self):
        """
        :param TopicId: TopicId
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TopicId: str\n        :param TopicName: TopicName
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TopicName: str\n        :param MsgRetentionSeconds: MsgRetentionSeconds
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MsgRetentionSeconds: int\n        :param MaxMsgSize: MaxMsgSize
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MaxMsgSize: int\n        :param Qps: Qps
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Qps: int\n        :param FilterType: FilterType
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FilterType: int\n        :param CreateTime: CreateTime
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CreateTime: int\n        :param LastModifyTime: LastModifyTime
Note: this field may return null, indicating that no valid values can be obtained.\n        :type LastModifyTime: int\n        :param MsgCount: MsgCount
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MsgCount: int\n        :param CreateUin: CreateUin
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CreateUin: int\n        :param Tags: Tags
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Tags: list of Tag\n        :param Trace: Whether to enable message trace for a topic. true: yes, false: no
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Trace: bool\n        """
        self.TopicId = None
        self.TopicName = None
        self.MsgRetentionSeconds = None
        self.MaxMsgSize = None
        self.Qps = None
        self.FilterType = None
        self.CreateTime = None
        self.LastModifyTime = None
        self.MsgCount = None
        self.CreateUin = None
        self.Tags = None
        self.Trace = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.Qps = params.get("Qps")
        self.FilterType = params.get("FilterType")
        self.CreateTime = params.get("CreateTime")
        self.LastModifyTime = params.get("LastModifyTime")
        self.MsgCount = params.get("MsgCount")
        self.CreateUin = params.get("CreateUin")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Trace = params.get("Trace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransactionPolicy(AbstractModel):
    """TransactionPolicy

    """

    def __init__(self):
        """
        :param FirstQueryInterval: FirstQueryInterval
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FirstQueryInterval: int\n        :param MaxQueryCount: MaxQueryCount
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MaxQueryCount: int\n        """
        self.FirstQueryInterval = None
        self.MaxQueryCount = None


    def _deserialize(self, params):
        self.FirstQueryInterval = params.get("FirstQueryInterval")
        self.MaxQueryCount = params.get("MaxQueryCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindDeadLetterRequest(AbstractModel):
    """UnbindDeadLetter request structure.

    """

    def __init__(self):
        """
        :param QueueName: Source queue name of dead letter policy. Calling this API will clear the dead letter queue policy of this queue.\n        :type QueueName: str\n        """
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindDeadLetterResponse(AbstractModel):
    """UnbindDeadLetter response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")