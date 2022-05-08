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


class AcknowledgeMessageRequest(AbstractModel):
    """AcknowledgeMessage request structure.

    """

    def __init__(self):
        r"""
        :param MessageId: Unique ID used to identify the message, which can be obtained from the returned value of `receiveMessage`.
        :type MessageId: str
        :param AckTopic: Topic name, which can be obtained from the returned value of `receiveMessage` and is better to be the full path of the topic, such as `tenant/namespace/topic`. If it is not specified, `public/default` will be used by default.
        :type AckTopic: str
        :param SubName: Subscriber name, which can be obtained from the returned value of `receiveMessage`. Make sure that it is the same as the subscriber name identified in `receiveMessage`; otherwise, the received message cannot be correctly acknowledged.
        :type SubName: str
        """
        self.MessageId = None
        self.AckTopic = None
        self.SubName = None


    def _deserialize(self, params):
        self.MessageId = params.get("MessageId")
        self.AckTopic = params.get("AckTopic")
        self.SubName = params.get("SubName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcknowledgeMessageResponse(AbstractModel):
    """AcknowledgeMessage response structure.

    """

    def __init__(self):
        r"""
        :param ErrorMsg: If it is an empty string, no error occurred.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class ClearCmqQueueRequest(AbstractModel):
    """ClearCmqQueue request structure.

    """

    def __init__(self):
        r"""
        :param QueueName: Queue name, which must be unique under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type QueueName: str
        """
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearCmqQueueResponse(AbstractModel):
    """ClearCmqQueue response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ClearCmqSubscriptionFilterTagsRequest(AbstractModel):
    """ClearCmqSubscriptionFilterTags request structure.

    """

    def __init__(self):
        r"""
        :param TopicName: Topic name, which must be unique in the same topic under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type TopicName: str
        :param SubscriptionName: Subscription name, which must be unique in the same topic under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type SubscriptionName: str
        """
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
        


class ClearCmqSubscriptionFilterTagsResponse(AbstractModel):
    """ClearCmqSubscriptionFilterTags response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Cluster(AbstractModel):
    """Set of cluster information

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID.
        :type ClusterId: str
        :param ClusterName: Cluster name.
        :type ClusterName: str
        :param Remark: Remarks.
        :type Remark: str
        :param EndPointNum: Number of access points
        :type EndPointNum: int
        :param CreateTime: Creation time
        :type CreateTime: str
        :param Healthy: Whether the cluster is healthy. 1: healthy; 0: exceptional
        :type Healthy: int
        :param HealthyInfo: Cluster health information
Note: this field may return null, indicating that no valid values can be obtained.
        :type HealthyInfo: str
        :param Status: Cluster status. 0: creating; 1: normal; 2: terminating; 3: deleted; 4. isolated; 5. creation failed; 6: deletion failed
        :type Status: int
        :param MaxNamespaceNum: Maximum number of namespaces
        :type MaxNamespaceNum: int
        :param MaxTopicNum: Maximum number of topics
        :type MaxTopicNum: int
        :param MaxQps: Maximum QPS
        :type MaxQps: int
        :param MessageRetentionTime: Maximum message retention period in seconds
        :type MessageRetentionTime: int
        :param MaxStorageCapacity: Maximum storage capacity
        :type MaxStorageCapacity: int
        :param Version: Cluster version
Note: this field may return null, indicating that no valid values can be obtained.
        :type Version: str
        :param PublicEndPoint: Public network access point
Note: this field may return null, indicating that no valid values can be obtained.
        :type PublicEndPoint: str
        :param VpcEndPoint: VPC access point
Note: this field may return null, indicating that no valid values can be obtained.
        :type VpcEndPoint: str
        :param NamespaceNum: Number of namespaces
Note: this field may return null, indicating that no valid values can be obtained.
        :type NamespaceNum: int
        :param UsedStorageBudget: Limit of used storage in MB
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsedStorageBudget: int
        :param MaxPublishRateInMessages: Maximum message production rate in messages
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxPublishRateInMessages: int
        :param MaxDispatchRateInMessages: Maximum message push rate in messages
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxDispatchRateInMessages: int
        :param MaxPublishRateInBytes: Maximum message production rate in bytes
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxPublishRateInBytes: int
        :param MaxDispatchRateInBytes: Maximum message push rate in bytes
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxDispatchRateInBytes: int
        :param TopicNum: Number of created topics
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicNum: int
        :param MaxMessageDelayInSeconds: Maximum message delay in seconds
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxMessageDelayInSeconds: int
        :param PublicAccessEnabled: Whether to enable public network access. If this parameter is left empty, the feature will be enabled by default
Note: this field may return null, indicating that no valid values can be obtained.
        :type PublicAccessEnabled: bool
        :param Tags: Tag
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param PayMode: Billing mode:
`0`: Pay-as-you-go
`1`: Monthly subscription
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PayMode: int
        """
        self.ClusterId = None
        self.ClusterName = None
        self.Remark = None
        self.EndPointNum = None
        self.CreateTime = None
        self.Healthy = None
        self.HealthyInfo = None
        self.Status = None
        self.MaxNamespaceNum = None
        self.MaxTopicNum = None
        self.MaxQps = None
        self.MessageRetentionTime = None
        self.MaxStorageCapacity = None
        self.Version = None
        self.PublicEndPoint = None
        self.VpcEndPoint = None
        self.NamespaceNum = None
        self.UsedStorageBudget = None
        self.MaxPublishRateInMessages = None
        self.MaxDispatchRateInMessages = None
        self.MaxPublishRateInBytes = None
        self.MaxDispatchRateInBytes = None
        self.TopicNum = None
        self.MaxMessageDelayInSeconds = None
        self.PublicAccessEnabled = None
        self.Tags = None
        self.PayMode = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Remark = params.get("Remark")
        self.EndPointNum = params.get("EndPointNum")
        self.CreateTime = params.get("CreateTime")
        self.Healthy = params.get("Healthy")
        self.HealthyInfo = params.get("HealthyInfo")
        self.Status = params.get("Status")
        self.MaxNamespaceNum = params.get("MaxNamespaceNum")
        self.MaxTopicNum = params.get("MaxTopicNum")
        self.MaxQps = params.get("MaxQps")
        self.MessageRetentionTime = params.get("MessageRetentionTime")
        self.MaxStorageCapacity = params.get("MaxStorageCapacity")
        self.Version = params.get("Version")
        self.PublicEndPoint = params.get("PublicEndPoint")
        self.VpcEndPoint = params.get("VpcEndPoint")
        self.NamespaceNum = params.get("NamespaceNum")
        self.UsedStorageBudget = params.get("UsedStorageBudget")
        self.MaxPublishRateInMessages = params.get("MaxPublishRateInMessages")
        self.MaxDispatchRateInMessages = params.get("MaxDispatchRateInMessages")
        self.MaxPublishRateInBytes = params.get("MaxPublishRateInBytes")
        self.MaxDispatchRateInBytes = params.get("MaxDispatchRateInBytes")
        self.TopicNum = params.get("TopicNum")
        self.MaxMessageDelayInSeconds = params.get("MaxMessageDelayInSeconds")
        self.PublicAccessEnabled = params.get("PublicAccessEnabled")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmqDeadLetterPolicy(AbstractModel):
    """cmq DeadLetterPolicy

    """

    def __init__(self):
        r"""
        :param DeadLetterQueue: Dead letter queue.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeadLetterQueue: str
        :param Policy: Dead letter queue policy.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Policy: int
        :param MaxTimeToLive: Maximum period in seconds before an unconsumed message expires, which is required if `Policy` is 1. Value range: 300–43200. This value should be smaller than `MsgRetentionSeconds` (maximum message retention period)
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxTimeToLive: int
        :param MaxReceiveCount: Maximum number of receipts.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxReceiveCount: int
        """
        self.DeadLetterQueue = None
        self.Policy = None
        self.MaxTimeToLive = None
        self.MaxReceiveCount = None


    def _deserialize(self, params):
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
        


class CmqDeadLetterSource(AbstractModel):
    """Cmq DeadLetterSource

    """

    def __init__(self):
        r"""
        :param QueueId: Message queue ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type QueueId: str
        :param QueueName: Message queue name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type QueueName: str
        """
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
        


class CmqQueue(AbstractModel):
    """Batch queue attribute information of CMQ

    """

    def __init__(self):
        r"""
        :param QueueId: Message queue ID.
        :type QueueId: str
        :param QueueName: Message queue name.
        :type QueueName: str
        :param Qps: Limit of the number of messages produced per second. The value for consumed messages is 1.1 times this value.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Qps: int
        :param Bps: Bandwidth limit.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Bps: int
        :param MaxDelaySeconds: Maximum retention period for inflight messages.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxDelaySeconds: int
        :param MaxMsgHeapNum: Maximum number of heaped messages. The value range is 1,000,000–10,000,000 during the beta test and can be 1,000,000–1,000,000,000 after the product is officially released. The default value is 10,000,000 during the beta test and will be 100,000,000 after the product is officially released.
        :type MaxMsgHeapNum: int
        :param PollingWaitSeconds: Long polling wait time for message reception. Value range: 0–30 seconds. Default value: 0.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PollingWaitSeconds: int
        :param MsgRetentionSeconds: Message retention period. Value range: 60–1296000 seconds (i.e., 1 minute–15 days). Default value: 345600 (i.e., 4 days).
Note: this field may return null, indicating that no valid values can be obtained.
        :type MsgRetentionSeconds: int
        :param VisibilityTimeout: Message visibility timeout period. Value range: 1–43200 seconds (i.e., 12 hours). Default value: 30.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VisibilityTimeout: int
        :param MaxMsgSize: Maximum message length. Value range: 1024–1048576 bytes (i.e., 1–1024 KB). Default value: 65536.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxMsgSize: int
        :param RewindSeconds: Maximum time range during which a message can be rewound in the queue, which ranges from 0 to 43,200 seconds. 0 indicates that message rewind is disabled.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RewindSeconds: int
        :param CreateTime: Queue creation time. A Unix timestamp accurate down to the millisecond will be returned.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: int
        :param LastModifyTime: Time when the queue attribute is last modified. A Unix timestamp accurate down to the millisecond will be returned.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastModifyTime: int
        :param ActiveMsgNum: Total number of messages in `Active` status (i.e., unconsumed) in the queue, which is an approximate value.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ActiveMsgNum: int
        :param InactiveMsgNum: Total number of messages in `Inactive` status (i.e., being consumed) in the queue, which is an approximate value.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InactiveMsgNum: int
        :param DelayMsgNum: Number of delayed messages.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DelayMsgNum: int
        :param RewindMsgNum: Number of retained messages which have been deleted by the `DelMsg` API but are still within their rewind time range.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RewindMsgNum: int
        :param MinMsgTime: Minimum unconsumed time of message in seconds.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MinMsgTime: int
        :param Transaction: Transaction message queue. true: transaction message type; false: other message types.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Transaction: bool
        :param DeadLetterSource: Dead letter queue.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeadLetterSource: list of CmqDeadLetterSource
        :param DeadLetterPolicy: Dead letter queue policy.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeadLetterPolicy: :class:`tencentcloud.tdmq.v20200217.models.CmqDeadLetterPolicy`
        :param TransactionPolicy: Transaction message policy.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TransactionPolicy: :class:`tencentcloud.tdmq.v20200217.models.CmqTransactionPolicy`
        :param CreateUin: Creator `Uin`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateUin: int
        :param Tags: Associated tag.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param Trace: Message trace. true: enabled; false: not enabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type Trace: bool
        :param TenantId: Tenant ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type TenantId: str
        :param NamespaceName: Namespace name
Note: this field may return null, indicating that no valid values can be obtained.
        :type NamespaceName: str
        :param Status: Cluster status. 0: creating; 1: normal; 2: terminating; 3: deleted; 4. isolated; 5. creation failed; 6: deletion failed
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Status: int
        :param MaxUnackedMsgNum: The maximum number of unacknowledged messages.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MaxUnackedMsgNum: int
        :param MaxMsgBacklogSize: Maximum size of heaped messages in bytes.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MaxMsgBacklogSize: int
        :param RetentionSizeInMB: Queue storage space configured for message rewind. Value range: 1,024-10,240 MB (if message rewind is enabled). The value “0” indicates that message rewind is not enabled.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RetentionSizeInMB: int
        """
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
        self.TenantId = None
        self.NamespaceName = None
        self.Status = None
        self.MaxUnackedMsgNum = None
        self.MaxMsgBacklogSize = None
        self.RetentionSizeInMB = None


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
                obj = CmqDeadLetterSource()
                obj._deserialize(item)
                self.DeadLetterSource.append(obj)
        if params.get("DeadLetterPolicy") is not None:
            self.DeadLetterPolicy = CmqDeadLetterPolicy()
            self.DeadLetterPolicy._deserialize(params.get("DeadLetterPolicy"))
        if params.get("TransactionPolicy") is not None:
            self.TransactionPolicy = CmqTransactionPolicy()
            self.TransactionPolicy._deserialize(params.get("TransactionPolicy"))
        self.CreateUin = params.get("CreateUin")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Trace = params.get("Trace")
        self.TenantId = params.get("TenantId")
        self.NamespaceName = params.get("NamespaceName")
        self.Status = params.get("Status")
        self.MaxUnackedMsgNum = params.get("MaxUnackedMsgNum")
        self.MaxMsgBacklogSize = params.get("MaxMsgBacklogSize")
        self.RetentionSizeInMB = params.get("RetentionSizeInMB")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmqSubscription(AbstractModel):
    """Subscription response parameter in CMQ

    """

    def __init__(self):
        r"""
        :param SubscriptionName: Subscription name, which must be unique in the same topic under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubscriptionName: str
        :param SubscriptionId: Subscription ID, which will be used during monitoring data pull.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubscriptionId: str
        :param TopicOwner: Subscription owner `APPID`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicOwner: int
        :param MsgCount: Number of messages to be delivered in the subscription.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MsgCount: int
        :param LastModifyTime: Time when the subscription attribute is last modified. A Unix timestamp accurate down to the millisecond will be returned.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastModifyTime: int
        :param CreateTime: Subscription creation time. A Unix timestamp accurate down to the millisecond will be returned.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: int
        :param BindingKey: Filtering policy for subscribing to and receiving messages.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BindingKey: list of str
        :param Endpoint: Endpoint that receives notifications, which varies by `protocol`: for HTTP, the endpoint must start with `http://`, and the `host` can be a domain or IP; for `queue`, `queueName` should be entered.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Endpoint: str
        :param FilterTags: Filtering policy selected when a subscription is created:
If `filterType` is 1, `filterTag` will be used for filtering.
If `filterType` is 2, `bindingKey` will be used for filtering.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FilterTags: list of str
        :param Protocol: Subscription protocol. Currently, two protocols are supported: HTTP and queue. To use the HTTP protocol, you need to build your own web server to receive messages. With the queue protocol, messages are automatically pushed to a CMQ queue and you can pull them concurrently.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param NotifyStrategy: CMQ push server retry policy in case an error occurs while pushing a message to the endpoint. Valid values:
(1) BACKOFF_RETRY: backoff retry, which is to retry at a fixed interval, discard the message after a certain number of retries, and continue to push the next message.
(2) EXPONENTIAL_DECAY_RETRY: exponential decay retry, which is to retry at an exponentially increasing interval, such as 1s, 2s, 4s, 8s, and so on. As a message can be retained in a topic for one day, failed messages will be discarded at most after one day of retry. Default value: EXPONENTIAL_DECAY_RETRY.
Note: this field may return null, indicating that no valid values can be obtained.
        :type NotifyStrategy: str
        :param NotifyContentFormat: Push content format. Valid values: 1. JSON; 2. SIMPLIFIED, i.e., the raw format. If `protocol` is `queue`, this value must be `SIMPLIFIED`. If `protocol` is `HTTP`, both values are acceptable, and the default value is `JSON`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type NotifyContentFormat: str
        """
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
        


class CmqTopic(AbstractModel):
    """Display field of the returned CMQ topic information

    """

    def __init__(self):
        r"""
        :param TopicId: Topic ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicId: str
        :param TopicName: Topic name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicName: str
        :param MsgRetentionSeconds: Maximum lifecycle of message in topic. After the period specified by this parameter has elapsed since a message is sent to the topic, the message will be deleted no matter whether it has been successfully pushed to the user. This parameter is measured in seconds and defaulted to one day (86,400 seconds), which cannot be modified.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MsgRetentionSeconds: int
        :param MaxMsgSize: Maximum message size, which ranges from 1,024 to 1,048,576 bytes (i.e., 1–1,024 KB). The default value is 65,536.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxMsgSize: int
        :param Qps: Number of messages published per second.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Qps: int
        :param FilterType: Filtering policy selected when a subscription is created:
If `filterType` is 1, `FilterTag` will be used for filtering.
If `filterType` is 2, `BindingKey` will be used for filtering.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FilterType: int
        :param CreateTime: Topic creation time. A Unix timestamp accurate down to the millisecond will be returned.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: int
        :param LastModifyTime: Time when the topic attribute is last modified. A Unix timestamp accurate down to the millisecond will be returned.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastModifyTime: int
        :param MsgCount: Number of current messages in the topic (number of retained messages).
Note: this field may return null, indicating that no valid values can be obtained.
        :type MsgCount: int
        :param CreateUin: Creator `Uin`. The `resource` field for CAM authentication is composed of this field.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateUin: int
        :param Tags: Associated tag.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param Trace: Message trace. true: enabled; false: not enabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type Trace: bool
        :param TenantId: Tenant ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type TenantId: str
        :param NamespaceName: Namespace name
Note: this field may return null, indicating that no valid values can be obtained.
        :type NamespaceName: str
        :param Status: Cluster status. 0: creating; 1: normal; 2: terminating; 3: deleted; 4. isolated; 5. creation failed; 6: deletion failed
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Status: int
        """
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
        self.TenantId = None
        self.NamespaceName = None
        self.Status = None


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
        self.TenantId = params.get("TenantId")
        self.NamespaceName = params.get("NamespaceName")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmqTransactionPolicy(AbstractModel):
    """cmq TransactionPolicy

    """

    def __init__(self):
        r"""
        :param FirstQueryInterval: First lookback time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FirstQueryInterval: int
        :param MaxQueryCount: Maximum number of queries.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxQueryCount: int
        """
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
        


class CreateClusterRequest(AbstractModel):
    """CreateCluster request structure.

    """

    def __init__(self):
        r"""
        :param ClusterName: Cluster name, which can contain up to 16 letters, digits, hyphens, and underscores.
        :type ClusterName: str
        :param BindClusterId: ID of your dedicated physical cluster. If it is not passed in, cluster resources will be created in a public cluster by default.
        :type BindClusterId: int
        :param Remark: Remarks (up to 128 characters).
        :type Remark: str
        :param Tags: Cluster tag list (deprecated).
        :type Tags: list of Tag
        :param PublicAccessEnabled: Whether to enable public network access. If this parameter is left empty, the feature will be enabled by default
        :type PublicAccessEnabled: bool
        """
        self.ClusterName = None
        self.BindClusterId = None
        self.Remark = None
        self.Tags = None
        self.PublicAccessEnabled = None


    def _deserialize(self, params):
        self.ClusterName = params.get("ClusterName")
        self.BindClusterId = params.get("BindClusterId")
        self.Remark = params.get("Remark")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.PublicAccessEnabled = params.get("PublicAccessEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterResponse(AbstractModel):
    """CreateCluster response structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RequestId = params.get("RequestId")


class CreateCmqQueueRequest(AbstractModel):
    """CreateCmqQueue request structure.

    """

    def __init__(self):
        r"""
        :param QueueName: Queue name, which must be unique under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type QueueName: str
        :param MaxMsgHeapNum: Maximum number of heaped messages. The value range is 1,000,000–10,000,000 during the beta test and can be 1,000,000–1,000,000,000 after the product is officially released. The default value is 10,000,000 during the beta test and will be 100,000,000 after the product is officially released.
        :type MaxMsgHeapNum: int
        :param PollingWaitSeconds: Long polling wait time for message reception. Value range: 0–30 seconds. Default value: 0.
        :type PollingWaitSeconds: int
        :param VisibilityTimeout: Message visibility timeout period. Value range: 1–43200 seconds (i.e., 12 hours). Default value: 30.
        :type VisibilityTimeout: int
        :param MaxMsgSize: Maximum message length. Value range: 1024–65536 bytes (i.e., 1–64 KB). Default value: 65536.
        :type MaxMsgSize: int
        :param MsgRetentionSeconds: The max period during which a message is retained before it is automatically acknowledged. Value range: 30-43,200 seconds (30 seconds to 12 hours). Default value: 3600 seconds (1 hour).
        :type MsgRetentionSeconds: int
        :param RewindSeconds: Rewindable time of messages in the queue. Value range: 0-1,296,000s (if message rewind is enabled). The value “0” indicates that message rewind is not enabled.
        :type RewindSeconds: int
        :param Transaction: 1: transaction queue; 0: general queue
        :type Transaction: int
        :param FirstQueryInterval: First lookback interval
        :type FirstQueryInterval: int
        :param MaxQueryCount: Maximum number of lookbacks
        :type MaxQueryCount: int
        :param DeadLetterQueueName: Dead letter queue name
        :type DeadLetterQueueName: str
        :param Policy: Dead letter policy. 0: message has been consumed multiple times but not deleted; 1: `Time-To-Live` has elapsed
        :type Policy: int
        :param MaxReceiveCount: Maximum receipt times. Value range: 1–1000
        :type MaxReceiveCount: int
        :param MaxTimeToLive: Maximum period in seconds before an unconsumed message expires, which is required if `policy` is 1. Value range: 300–43200. This value should be smaller than `msgRetentionSeconds` (maximum message retention period)
        :type MaxTimeToLive: int
        :param Trace: Whether to enable message trace. true: yes; false: no. If this field is not configured, the feature will not be enabled
        :type Trace: bool
        :param Tags: Tag array.
        :type Tags: list of Tag
        :param RetentionSizeInMB: Queue storage space configured for message rewind. Value range: 1,024-10,240 MB (if message rewind is enabled). The value “0” indicates that message rewind is not enabled.
        :type RetentionSizeInMB: int
        """
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
        self.Tags = None
        self.RetentionSizeInMB = None


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
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RetentionSizeInMB = params.get("RetentionSizeInMB")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCmqQueueResponse(AbstractModel):
    """CreateCmqQueue response structure.

    """

    def __init__(self):
        r"""
        :param QueueId: `queueId` of a successfully created queue
        :type QueueId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.QueueId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.QueueId = params.get("QueueId")
        self.RequestId = params.get("RequestId")


class CreateCmqSubscribeRequest(AbstractModel):
    """CreateCmqSubscribe request structure.

    """

    def __init__(self):
        r"""
        :param TopicName: Topic name, which must be unique in the same topic under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type TopicName: str
        :param SubscriptionName: Subscription name, which must be unique in the same topic under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type SubscriptionName: str
        :param Protocol: Subscription protocol. Currently, two protocols are supported: HTTP and queue. To use the HTTP protocol, you need to build your own web server to receive messages. With the queue protocol, messages are automatically pushed to a CMQ queue and you can pull them concurrently.
        :type Protocol: str
        :param Endpoint: `Endpoint` for notification receipt, which is distinguished by `Protocol`. For `http`, `Endpoint` must begin with `http://` and `host` can be a domain name or IP. For `Queue`, enter `QueueName`. Note that currently the push service cannot push messages to a VPC; therefore, if a VPC domain name or address is entered for `Endpoint`, pushed messages will not be received. Currently, messages can be pushed only to the public network and classic network.
        :type Endpoint: str
        :param NotifyStrategy: CMQ push server retry policy in case an error occurs while pushing a message to `Endpoint`. Valid values: 1. BACKOFF_RETRY: backoff retry, which is to retry at a fixed interval, discard the message after a certain number of retries, and continue to push the next message; 2. EXPONENTIAL_DECAY_RETRY: exponential decay retry, which is to retry at an exponentially increasing interval, such as 1s, 2s, 4s, 8s, and so on. As a message can be retained in a topic for one day, failed messages will be discarded at most after one day of retry. Default value: EXPONENTIAL_DECAY_RETRY.
        :type NotifyStrategy: str
        :param FilterTag: Message body tag (used for message filtering). The number of tags cannot exceed 5, and each tag can contain up to 16 characters. It is used in conjunction with the `MsgTag` parameter of `(Batch)PublishMessage`. Rules: 1. If `FilterTag` is not configured, no matter whether `MsgTag` is configured, the subscription will receive all messages published to the topic; 2. If the array of `FilterTag` values has a value, only when at least one of the values in the array also exists in the array of `MsgTag` values (i.e., `FilterTag` and `MsgTag` have an intersection) can the subscription receive messages published to the topic; 3. If the array of `FilterTag` values has a value, but `MsgTag` is not configured, then no message published to the topic will be received, which can be considered as a special case of rule 2 as `FilterTag` and `MsgTag` do not intersect in this case. The overall design idea of rules is based on the intention of the subscriber.
        :type FilterTag: list of str
        :param BindingKey: The number of `BindingKey` cannot exceed 5, and the length of each `BindingKey` cannot exceed 64 bytes. This field indicates the filtering policy for subscribing to and receiving messages. Each `BindingKey` includes up to 15 dots (namely up to 16 segments).
        :type BindingKey: list of str
        :param NotifyContentFormat: Push content format. Valid values: 1. JSON; 2. SIMPLIFIED, i.e., the raw format. If `Protocol` is `queue`, this value must be `SIMPLIFIED`. If `Protocol` is `http`, both options are acceptable, and the default value is `JSON`.
        :type NotifyContentFormat: str
        """
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
        


class CreateCmqSubscribeResponse(AbstractModel):
    """CreateCmqSubscribe response structure.

    """

    def __init__(self):
        r"""
        :param SubscriptionId: Subscription ID
        :type SubscriptionId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SubscriptionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubscriptionId = params.get("SubscriptionId")
        self.RequestId = params.get("RequestId")


class CreateCmqTopicRequest(AbstractModel):
    """CreateCmqTopic request structure.

    """

    def __init__(self):
        r"""
        :param TopicName: Topic name, which must be unique in the same topic under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type TopicName: str
        :param MaxMsgSize: Maximum message length. Value range: 1024–65536 bytes (i.e., 1–64 KB). Default value: 65536.
        :type MaxMsgSize: int
        :param FilterType: Used to specify the message match policy for the topic. 1: tag match policy (default value); 2: routing match policy.
        :type FilterType: int
        :param MsgRetentionSeconds: Message retention period. Value range: 60–86400 seconds (i.e., 1 minute–1 day). Default value: 86400.
        :type MsgRetentionSeconds: int
        :param Trace: Whether to enable message trace. true: yes; false: no. If this field is left empty, the feature will not be enabled.
        :type Trace: bool
        :param Tags: Tag array.
        :type Tags: list of Tag
        """
        self.TopicName = None
        self.MaxMsgSize = None
        self.FilterType = None
        self.MsgRetentionSeconds = None
        self.Trace = None
        self.Tags = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.MaxMsgSize = params.get("MaxMsgSize")
        self.FilterType = params.get("FilterType")
        self.MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self.Trace = params.get("Trace")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCmqTopicResponse(AbstractModel):
    """CreateCmqTopic response structure.

    """

    def __init__(self):
        r"""
        :param TopicId: Topic ID
        :type TopicId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TopicId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.RequestId = params.get("RequestId")


class CreateEnvironmentRequest(AbstractModel):
    """CreateEnvironment request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment (namespace) name, which can contain up to 16 letters, digits, hyphens, and underscores.
        :type EnvironmentId: str
        :param MsgTTL: Unconsumed message expiration time in seconds. Minimum value: 60; maximum value: 1296000 (15 days).
        :type MsgTTL: int
        :param Remark: Remarks (up to 128 characters).
        :type Remark: str
        :param ClusterId: Pulsar cluster ID
        :type ClusterId: str
        :param RetentionPolicy: Message retention policy
        :type RetentionPolicy: :class:`tencentcloud.tdmq.v20200217.models.RetentionPolicy`
        """
        self.EnvironmentId = None
        self.MsgTTL = None
        self.Remark = None
        self.ClusterId = None
        self.RetentionPolicy = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.MsgTTL = params.get("MsgTTL")
        self.Remark = params.get("Remark")
        self.ClusterId = params.get("ClusterId")
        if params.get("RetentionPolicy") is not None:
            self.RetentionPolicy = RetentionPolicy()
            self.RetentionPolicy._deserialize(params.get("RetentionPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEnvironmentResponse(AbstractModel):
    """CreateEnvironment response structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param MsgTTL: TTL for unconsumed messages in seconds.
        :type MsgTTL: int
        :param Remark: Remarks (up to 128 characters).
Note: this field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param NamespaceId: Namespace ID
        :type NamespaceId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EnvironmentId = None
        self.MsgTTL = None
        self.Remark = None
        self.NamespaceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.MsgTTL = params.get("MsgTTL")
        self.Remark = params.get("Remark")
        self.NamespaceId = params.get("NamespaceId")
        self.RequestId = params.get("RequestId")


class CreateEnvironmentRoleRequest(AbstractModel):
    """CreateEnvironmentRole request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param RoleName: Role name.
        :type RoleName: str
        :param Permissions: Permissions, which is a non-empty string array of `produce` and `consume` at the most.
        :type Permissions: list of str
        :param ClusterId: Cluster ID (required)
        :type ClusterId: str
        """
        self.EnvironmentId = None
        self.RoleName = None
        self.Permissions = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.RoleName = params.get("RoleName")
        self.Permissions = params.get("Permissions")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEnvironmentRoleResponse(AbstractModel):
    """CreateEnvironmentRole response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateRocketMQClusterRequest(AbstractModel):
    """CreateRocketMQCluster request structure.

    """

    def __init__(self):
        r"""
        :param Name: Cluster name, which can contain 3–64 letters, digits, hyphens, and underscores
        :type Name: str
        :param Remark: Cluster description (up to 128 characters)
        :type Remark: str
        """
        self.Name = None
        self.Remark = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRocketMQClusterResponse(AbstractModel):
    """CreateRocketMQCluster response structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RequestId = params.get("RequestId")


class CreateRocketMQGroupRequest(AbstractModel):
    """CreateRocketMQGroup request structure.

    """

    def __init__(self):
        r"""
        :param GroupId: Group name (8–64 characters)
        :type GroupId: str
        :param Namespaces: Namespace. Currently, only one namespace is supported
        :type Namespaces: list of str
        :param ReadEnable: Whether to enable consumption
        :type ReadEnable: bool
        :param BroadcastEnable: Whether to enable broadcast consumption
        :type BroadcastEnable: bool
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param Remark: Remarks (up to 128 characters)
        :type Remark: str
        """
        self.GroupId = None
        self.Namespaces = None
        self.ReadEnable = None
        self.BroadcastEnable = None
        self.ClusterId = None
        self.Remark = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Namespaces = params.get("Namespaces")
        self.ReadEnable = params.get("ReadEnable")
        self.BroadcastEnable = params.get("BroadcastEnable")
        self.ClusterId = params.get("ClusterId")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRocketMQGroupResponse(AbstractModel):
    """CreateRocketMQGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateRocketMQNamespaceRequest(AbstractModel):
    """CreateRocketMQNamespace request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param NamespaceId: Namespace name, which can contain 3–64 letters, digits, hyphens, and underscores
        :type NamespaceId: str
        :param Ttl: Retention time of unconsumed messages in milliseconds. Value range: 60 seconds–15 days
        :type Ttl: int
        :param RetentionTime: Retention time of persisted messages in milliseconds
        :type RetentionTime: int
        :param Remark: Remarks (up to 128 characters)
        :type Remark: str
        """
        self.ClusterId = None
        self.NamespaceId = None
        self.Ttl = None
        self.RetentionTime = None
        self.Remark = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.Ttl = params.get("Ttl")
        self.RetentionTime = params.get("RetentionTime")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRocketMQNamespaceResponse(AbstractModel):
    """CreateRocketMQNamespace response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateRocketMQTopicRequest(AbstractModel):
    """CreateRocketMQTopic request structure.

    """

    def __init__(self):
        r"""
        :param Topic: Topic name, which can contain 3–64 letters, digits, hyphens, and underscores
        :type Topic: str
        :param Namespaces: Topic namespace. Currently, you can create topics only in one single namespace.
        :type Namespaces: list of str
        :param Type: Topic type. Valid values: Normal, GlobalOrder, PartitionedOrder.
        :type Type: str
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param Remark: Topic remarks (up to 128 characters)
        :type Remark: str
        :param PartitionNum: Number of partitions, which doesn't take effect for globally sequential messages
        :type PartitionNum: int
        """
        self.Topic = None
        self.Namespaces = None
        self.Type = None
        self.ClusterId = None
        self.Remark = None
        self.PartitionNum = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Namespaces = params.get("Namespaces")
        self.Type = params.get("Type")
        self.ClusterId = params.get("ClusterId")
        self.Remark = params.get("Remark")
        self.PartitionNum = params.get("PartitionNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRocketMQTopicResponse(AbstractModel):
    """CreateRocketMQTopic response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateRoleRequest(AbstractModel):
    """CreateRole request structure.

    """

    def __init__(self):
        r"""
        :param RoleName: Role name, which can contain up to 32 letters, digits, hyphens, and underscores.
        :type RoleName: str
        :param Remark: Remarks (up to 128 characters).
        :type Remark: str
        :param ClusterId: Cluster ID (required)
        :type ClusterId: str
        """
        self.RoleName = None
        self.Remark = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.RoleName = params.get("RoleName")
        self.Remark = params.get("Remark")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoleResponse(AbstractModel):
    """CreateRole response structure.

    """

    def __init__(self):
        r"""
        :param RoleName: Role name
        :type RoleName: str
        :param Token: Role token
        :type Token: str
        :param Remark: Remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RoleName = None
        self.Token = None
        self.Remark = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoleName = params.get("RoleName")
        self.Token = params.get("Token")
        self.Remark = params.get("Remark")
        self.RequestId = params.get("RequestId")


class CreateSubscriptionRequest(AbstractModel):
    """CreateSubscription request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param TopicName: Topic name.
        :type TopicName: str
        :param SubscriptionName: Subscriber name, which can contain up to 150 letters, digits, hyphens, and underscores.
        :type SubscriptionName: str
        :param IsIdempotent: Whether the creation is idempotent; if not, you cannot create subscriptions with the same name.
        :type IsIdempotent: bool
        :param Remark: Remarks (up to 128 characters).
        :type Remark: str
        :param ClusterId: Pulsar cluster ID
        :type ClusterId: str
        :param AutoCreatePolicyTopic: Whether to automatically create a dead letter topic and a retry letter topic. true: yes (default value); false: no.
        :type AutoCreatePolicyTopic: bool
        :param PostFixPattern: Naming convention for dead letter and retry letter topics. `LEGACY` indicates to use the legacy naming convention, and `COMMUNITY` indicates to use the naming convention in the Pulsar community.
        :type PostFixPattern: str
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.SubscriptionName = None
        self.IsIdempotent = None
        self.Remark = None
        self.ClusterId = None
        self.AutoCreatePolicyTopic = None
        self.PostFixPattern = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.SubscriptionName = params.get("SubscriptionName")
        self.IsIdempotent = params.get("IsIdempotent")
        self.Remark = params.get("Remark")
        self.ClusterId = params.get("ClusterId")
        self.AutoCreatePolicyTopic = params.get("AutoCreatePolicyTopic")
        self.PostFixPattern = params.get("PostFixPattern")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubscriptionResponse(AbstractModel):
    """CreateSubscription response structure.

    """

    def __init__(self):
        r"""
        :param Result: Creation result.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param TopicName: Topic name, which can contain up to 64 letters, digits, hyphens, and underscores.
        :type TopicName: str
        :param Partitions: 0: non-partitioned topic; other values: number of partitions in the partitioned topic (up to 128).
        :type Partitions: int
        :param Remark: Remarks (up to 128 characters).
        :type Remark: str
        :param TopicType: 0: general message;
1: globally sequential message;
2: partitionally sequential message;
3: retry letter queue;
4: dead letter queue.
        :type TopicType: int
        :param ClusterId: Pulsar cluster ID
        :type ClusterId: str
        :param PulsarTopicType: Pulsar topic type.
`0`: Non-persistent and non-partitioned
`1`: Non-persistent and partitioned
`2`: Persistent and non-partitioned
`3`: Persistent and partitioned
        :type PulsarTopicType: int
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.Partitions = None
        self.Remark = None
        self.TopicType = None
        self.ClusterId = None
        self.PulsarTopicType = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.Partitions = params.get("Partitions")
        self.Remark = params.get("Remark")
        self.TopicType = params.get("TopicType")
        self.ClusterId = params.get("ClusterId")
        self.PulsarTopicType = params.get("PulsarTopicType")
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
        r"""
        :param EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param TopicName: Topic name.
        :type TopicName: str
        :param Partitions: 0: non-partitioned topic; other values: number of partitions in the partitioned topic.
        :type Partitions: int
        :param Remark: Remarks (up to 128 characters).
Note: this field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param TopicType: 0: general message;
1: globally sequential message;
2: partitionally sequential message;
3: retry letter queue;
4: dead letter queue;
5: transaction message.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicType: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.Partitions = None
        self.Remark = None
        self.TopicType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.Partitions = params.get("Partitions")
        self.Remark = params.get("Remark")
        self.TopicType = params.get("TopicType")
        self.RequestId = params.get("RequestId")


class DeleteClusterRequest(AbstractModel):
    """DeleteCluster request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster to be deleted.
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterResponse(AbstractModel):
    """DeleteCluster response structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RequestId = params.get("RequestId")


class DeleteCmqQueueRequest(AbstractModel):
    """DeleteCmqQueue request structure.

    """

    def __init__(self):
        r"""
        :param QueueName: Queue name, which must be unique under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type QueueName: str
        """
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCmqQueueResponse(AbstractModel):
    """DeleteCmqQueue response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCmqSubscribeRequest(AbstractModel):
    """DeleteCmqSubscribe request structure.

    """

    def __init__(self):
        r"""
        :param TopicName: Topic name, which must be unique under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type TopicName: str
        :param SubscriptionName: Subscription name, which must be unique in the same topic under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type SubscriptionName: str
        """
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
        


class DeleteCmqSubscribeResponse(AbstractModel):
    """DeleteCmqSubscribe response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCmqTopicRequest(AbstractModel):
    """DeleteCmqTopic request structure.

    """

    def __init__(self):
        r"""
        :param TopicName: Topic name, which must be unique under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type TopicName: str
        """
        self.TopicName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCmqTopicResponse(AbstractModel):
    """DeleteCmqTopic response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEnvironmentRolesRequest(AbstractModel):
    """DeleteEnvironmentRoles request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param RoleNames: Array of role names.
        :type RoleNames: list of str
        :param ClusterId: Cluster ID (required)
        :type ClusterId: str
        """
        self.EnvironmentId = None
        self.RoleNames = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.RoleNames = params.get("RoleNames")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEnvironmentRolesResponse(AbstractModel):
    """DeleteEnvironmentRoles response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEnvironmentsRequest(AbstractModel):
    """DeleteEnvironments request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentIds: Array of environments (namespaces). Up to 20 environments can be deleted at a time.
        :type EnvironmentIds: list of str
        :param ClusterId: Pulsar cluster ID
        :type ClusterId: str
        """
        self.EnvironmentIds = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentIds = params.get("EnvironmentIds")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEnvironmentsResponse(AbstractModel):
    """DeleteEnvironments response structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentIds: Array of environments (namespaces) successfully deleted.
        :type EnvironmentIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EnvironmentIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvironmentIds = params.get("EnvironmentIds")
        self.RequestId = params.get("RequestId")


class DeleteRocketMQClusterRequest(AbstractModel):
    """DeleteRocketMQCluster request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster to be deleted.
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRocketMQClusterResponse(AbstractModel):
    """DeleteRocketMQCluster response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRocketMQGroupRequest(AbstractModel):
    """DeleteRocketMQGroup request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param NamespaceId: Namespace name
        :type NamespaceId: str
        :param GroupId: Consumer group name
        :type GroupId: str
        """
        self.ClusterId = None
        self.NamespaceId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRocketMQGroupResponse(AbstractModel):
    """DeleteRocketMQGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRocketMQNamespaceRequest(AbstractModel):
    """DeleteRocketMQNamespace request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param NamespaceId: Namespace name
        :type NamespaceId: str
        """
        self.ClusterId = None
        self.NamespaceId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRocketMQNamespaceResponse(AbstractModel):
    """DeleteRocketMQNamespace response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRocketMQTopicRequest(AbstractModel):
    """DeleteRocketMQTopic request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param NamespaceId: Namespace name
        :type NamespaceId: str
        :param Topic: Topic name
        :type Topic: str
        """
        self.ClusterId = None
        self.NamespaceId = None
        self.Topic = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.Topic = params.get("Topic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRocketMQTopicResponse(AbstractModel):
    """DeleteRocketMQTopic response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRolesRequest(AbstractModel):
    """DeleteRoles request structure.

    """

    def __init__(self):
        r"""
        :param RoleNames: Array of role names.
        :type RoleNames: list of str
        :param ClusterId: Cluster ID (required)
        :type ClusterId: str
        """
        self.RoleNames = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.RoleNames = params.get("RoleNames")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRolesResponse(AbstractModel):
    """DeleteRoles response structure.

    """

    def __init__(self):
        r"""
        :param RoleNames: Name array of roles successfully deleted.
        :type RoleNames: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RoleNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoleNames = params.get("RoleNames")
        self.RequestId = params.get("RequestId")


class DescribeBindVpcsRequest(AbstractModel):
    """DescribeBindVpcs request structure.

    """

    def __init__(self):
        r"""
        :param Offset: Offset. If this parameter is left empty, 0 will be used by default.
        :type Offset: int
        :param Limit: Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 20.
        :type Limit: int
        :param ClusterId: Pulsar cluster ID
        :type ClusterId: str
        """
        self.Offset = None
        self.Limit = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindVpcsResponse(AbstractModel):
    """DescribeBindVpcs response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of records.
        :type TotalCount: int
        :param VpcSets: Set of VPCs.
        :type VpcSets: list of VpcBindRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.VpcSets = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VpcSets") is not None:
            self.VpcSets = []
            for item in params.get("VpcSets"):
                obj = VpcBindRecord()
                obj._deserialize(item)
                self.VpcSets.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterDetailRequest(AbstractModel):
    """DescribeClusterDetail request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterDetailResponse(AbstractModel):
    """DescribeClusterDetail response structure.

    """

    def __init__(self):
        r"""
        :param ClusterSet: Cluster details
        :type ClusterSet: :class:`tencentcloud.tdmq.v20200217.models.Cluster`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ClusterSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterSet") is not None:
            self.ClusterSet = Cluster()
            self.ClusterSet._deserialize(params.get("ClusterSet"))
        self.RequestId = params.get("RequestId")


class DescribeCmqDeadLetterSourceQueuesRequest(AbstractModel):
    """DescribeCmqDeadLetterSourceQueues request structure.

    """

    def __init__(self):
        r"""
        :param DeadLetterQueueName: Dead letter queue name
        :type DeadLetterQueueName: str
        :param Limit: Starting position of the list of topics to be returned on the current page in case of paginated return. If a value is entered, `limit` is required. If this parameter is left empty, 0 will be used by default.
        :type Limit: int
        :param Offset: Number of topics to be returned per page in case of paginated return. If this parameter is not passed in, 20 will be used by default. Maximum value: 50.
        :type Offset: int
        :param SourceQueueName: Filter by `SourceQueueName`
        :type SourceQueueName: str
        """
        self.DeadLetterQueueName = None
        self.Limit = None
        self.Offset = None
        self.SourceQueueName = None


    def _deserialize(self, params):
        self.DeadLetterQueueName = params.get("DeadLetterQueueName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SourceQueueName = params.get("SourceQueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCmqDeadLetterSourceQueuesResponse(AbstractModel):
    """DescribeCmqDeadLetterSourceQueues response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of eligible queues
        :type TotalCount: int
        :param QueueSet: Source queues of dead letter queue
        :type QueueSet: list of CmqDeadLetterSource
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.QueueSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("QueueSet") is not None:
            self.QueueSet = []
            for item in params.get("QueueSet"):
                obj = CmqDeadLetterSource()
                obj._deserialize(item)
                self.QueueSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCmqQueueDetailRequest(AbstractModel):
    """DescribeCmqQueueDetail request structure.

    """

    def __init__(self):
        r"""
        :param QueueName: Exact match by `QueueName`
        :type QueueName: str
        """
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCmqQueueDetailResponse(AbstractModel):
    """DescribeCmqQueueDetail response structure.

    """

    def __init__(self):
        r"""
        :param QueueDescribe: List of queue details.
        :type QueueDescribe: :class:`tencentcloud.tdmq.v20200217.models.CmqQueue`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.QueueDescribe = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QueueDescribe") is not None:
            self.QueueDescribe = CmqQueue()
            self.QueueDescribe._deserialize(params.get("QueueDescribe"))
        self.RequestId = params.get("RequestId")


class DescribeCmqSubscriptionDetailRequest(AbstractModel):
    """DescribeCmqSubscriptionDetail request structure.

    """

    def __init__(self):
        r"""
        :param TopicName: Topic name, which must be unique in the same topic under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type TopicName: str
        :param Offset: Starting position of the list of topics to be returned on the current page in case of paginated return. If a value is entered, `limit` is required. If this parameter is left empty, 0 will be used by default
        :type Offset: int
        :param Limit: Number of topics to be returned per page in case of paginated return. If this parameter is not passed in, 20 will be used by default. Maximum value: 50.
        :type Limit: int
        :param SubscriptionName: Fuzzy search by `SubscriptionName`
        :type SubscriptionName: str
        """
        self.TopicName = None
        self.Offset = None
        self.Limit = None
        self.SubscriptionName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SubscriptionName = params.get("SubscriptionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCmqSubscriptionDetailResponse(AbstractModel):
    """DescribeCmqSubscriptionDetail response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number
        :type TotalCount: int
        :param SubscriptionSet: Set of subscription attributes
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubscriptionSet: list of CmqSubscription
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.SubscriptionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SubscriptionSet") is not None:
            self.SubscriptionSet = []
            for item in params.get("SubscriptionSet"):
                obj = CmqSubscription()
                obj._deserialize(item)
                self.SubscriptionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCmqTopicDetailRequest(AbstractModel):
    """DescribeCmqTopicDetail request structure.

    """

    def __init__(self):
        r"""
        :param TopicName: Exact match by `TopicName`.
        :type TopicName: str
        """
        self.TopicName = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCmqTopicDetailResponse(AbstractModel):
    """DescribeCmqTopicDetail response structure.

    """

    def __init__(self):
        r"""
        :param TopicDescribe: Topic details
        :type TopicDescribe: :class:`tencentcloud.tdmq.v20200217.models.CmqTopic`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TopicDescribe = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TopicDescribe") is not None:
            self.TopicDescribe = CmqTopic()
            self.TopicDescribe._deserialize(params.get("TopicDescribe"))
        self.RequestId = params.get("RequestId")


class DescribeEnvironmentAttributesRequest(AbstractModel):
    """DescribeEnvironmentAttributes request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param ClusterId: Pulsar cluster ID
        :type ClusterId: str
        """
        self.EnvironmentId = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentAttributesResponse(AbstractModel):
    """DescribeEnvironmentAttributes response structure.

    """

    def __init__(self):
        r"""
        :param MsgTTL: TTL for unconsumed messages in seconds. Maximum value: 1296000 seconds (i.e., 15 days).
        :type MsgTTL: int
        :param RateInByte: Consumption rate limit in bytes/second. 0: unlimited.
        :type RateInByte: int
        :param RateInSize: Consumption rate limit in messages/second. 0: unlimited.
        :type RateInSize: int
        :param RetentionHours: Retention policy for consumed messages in hours. 0: deleted immediately after consumption.
        :type RetentionHours: int
        :param RetentionSize: Retention policy for consumed messages in GB. 0: deleted immediately after consumption.
        :type RetentionSize: int
        :param EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param Replicas: Number of replicas.
        :type Replicas: int
        :param Remark: Remarks.
        :type Remark: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MsgTTL = None
        self.RateInByte = None
        self.RateInSize = None
        self.RetentionHours = None
        self.RetentionSize = None
        self.EnvironmentId = None
        self.Replicas = None
        self.Remark = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MsgTTL = params.get("MsgTTL")
        self.RateInByte = params.get("RateInByte")
        self.RateInSize = params.get("RateInSize")
        self.RetentionHours = params.get("RetentionHours")
        self.RetentionSize = params.get("RetentionSize")
        self.EnvironmentId = params.get("EnvironmentId")
        self.Replicas = params.get("Replicas")
        self.Remark = params.get("Remark")
        self.RequestId = params.get("RequestId")


class DescribePublisherSummaryRequest(AbstractModel):
    """DescribePublisherSummary request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID.
        :type ClusterId: str
        :param Namespace: Namespace name.
        :type Namespace: str
        :param Topic: Topic name.
        :type Topic: str
        """
        self.ClusterId = None
        self.Namespace = None
        self.Topic = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Namespace = params.get("Namespace")
        self.Topic = params.get("Topic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublisherSummaryResponse(AbstractModel):
    """DescribePublisherSummary response structure.

    """

    def __init__(self):
        r"""
        :param MsgRateIn: Production rate (messages/sec).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MsgRateIn: float
        :param MsgThroughputIn: Production rate (byte/sec).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MsgThroughputIn: float
        :param PublisherCount: The number of producers.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type PublisherCount: int
        :param StorageSize: Message storage size in bytes.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type StorageSize: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MsgRateIn = None
        self.MsgThroughputIn = None
        self.PublisherCount = None
        self.StorageSize = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MsgRateIn = params.get("MsgRateIn")
        self.MsgThroughputIn = params.get("MsgThroughputIn")
        self.PublisherCount = params.get("PublisherCount")
        self.StorageSize = params.get("StorageSize")
        self.RequestId = params.get("RequestId")


class DescribePublishersRequest(AbstractModel):
    """DescribePublishers request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID.
        :type ClusterId: str
        :param Namespace: Namespace name.
        :type Namespace: str
        :param Topic: Topic name.
        :type Topic: str
        :param Filters: Parameter filter. The `ProducerName` and `Address` fields are supported.
        :type Filters: list of Filter
        :param Offset: Offset for query. Default value: `0`.
        :type Offset: int
        :param Limit: The number of query results displayed per page. Default value: `20`.
        :type Limit: int
        :param Sort: Sort by field.
        :type Sort: :class:`tencentcloud.tdmq.v20200217.models.Sort`
        """
        self.ClusterId = None
        self.Namespace = None
        self.Topic = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Sort = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Namespace = params.get("Namespace")
        self.Topic = params.get("Topic")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Sort") is not None:
            self.Sort = Sort()
            self.Sort._deserialize(params.get("Sort"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublishersResponse(AbstractModel):
    """DescribePublishers response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of query results.
        :type TotalCount: int
        :param Publishers: List of producer information.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Publishers: list of Publisher
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Publishers = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Publishers") is not None:
            self.Publishers = []
            for item in params.get("Publishers"):
                obj = Publisher()
                obj._deserialize(item)
                self.Publishers.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRocketMQClusterRequest(AbstractModel):
    """DescribeRocketMQCluster request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQClusterResponse(AbstractModel):
    """DescribeRocketMQCluster response structure.

    """

    def __init__(self):
        r"""
        :param ClusterInfo: Cluster information
        :type ClusterInfo: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterInfo`
        :param ClusterConfig: Cluster configuration
        :type ClusterConfig: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterConfig`
        :param ClusterStats: Recent cluster usage
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterStats: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterRecentStats`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ClusterInfo = None
        self.ClusterConfig = None
        self.ClusterStats = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterInfo") is not None:
            self.ClusterInfo = RocketMQClusterInfo()
            self.ClusterInfo._deserialize(params.get("ClusterInfo"))
        if params.get("ClusterConfig") is not None:
            self.ClusterConfig = RocketMQClusterConfig()
            self.ClusterConfig._deserialize(params.get("ClusterConfig"))
        if params.get("ClusterStats") is not None:
            self.ClusterStats = RocketMQClusterRecentStats()
            self.ClusterStats._deserialize(params.get("ClusterStats"))
        self.RequestId = params.get("RequestId")


class DescribeRolesRequest(AbstractModel):
    """DescribeRoles request structure.

    """

    def __init__(self):
        r"""
        :param RoleName: Fuzzy query by role name
        :type RoleName: str
        :param Offset: Offset. If this parameter is left empty, 0 will be used by default.
        :type Offset: int
        :param Limit: Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 20.
        :type Limit: int
        :param ClusterId: Cluster ID (required)
        :type ClusterId: str
        :param Filters: * RoleName
Filter by role name for exact query.
Type: String
Required: no
        :type Filters: list of Filter
        """
        self.RoleName = None
        self.Offset = None
        self.Limit = None
        self.ClusterId = None
        self.Filters = None


    def _deserialize(self, params):
        self.RoleName = params.get("RoleName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ClusterId = params.get("ClusterId")
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
        


class DescribeRolesResponse(AbstractModel):
    """DescribeRoles response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of records.
        :type TotalCount: int
        :param RoleSets: Array of roles.
        :type RoleSets: list of Role
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.RoleSets = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RoleSets") is not None:
            self.RoleSets = []
            for item in params.get("RoleSets"):
                obj = Role()
                obj._deserialize(item)
                self.RoleSets.append(obj)
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """Filter parameter

    """

    def __init__(self):
        r"""
        :param Name: Filter parameter name
        :type Name: str
        :param Values: Value
        :type Values: list of str
        """
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
        


class ModifyClusterRequest(AbstractModel):
    """ModifyCluster request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the Pulsar cluster to be updated.
        :type ClusterId: str
        :param ClusterName: Updated cluster name.
        :type ClusterName: str
        :param Remark: Remarks.
        :type Remark: str
        :param PublicAccessEnabled: Enables public network access, which can only be `true`.
        :type PublicAccessEnabled: bool
        """
        self.ClusterId = None
        self.ClusterName = None
        self.Remark = None
        self.PublicAccessEnabled = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Remark = params.get("Remark")
        self.PublicAccessEnabled = params.get("PublicAccessEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterResponse(AbstractModel):
    """ModifyCluster response structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Pulsar cluster ID
        :type ClusterId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RequestId = params.get("RequestId")


class ModifyCmqQueueAttributeRequest(AbstractModel):
    """ModifyCmqQueueAttribute request structure.

    """

    def __init__(self):
        r"""
        :param QueueName: Queue name, which must be unique under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type QueueName: str
        :param MaxMsgHeapNum: Maximum number of heaped messages. The value range is 1,000,000–10,000,000 during the beta test and can be 1,000,000–1,000,000,000 after the product is officially released. The default value is 10,000,000 during the beta test and will be 100,000,000 after the product is officially released.
        :type MaxMsgHeapNum: int
        :param PollingWaitSeconds: Long polling wait time for message reception. Value range: 0–30 seconds. Default value: 0.
        :type PollingWaitSeconds: int
        :param VisibilityTimeout: Message visibility timeout period. Value range: 1–43200 seconds (i.e., 12 hours). Default value: 30.
        :type VisibilityTimeout: int
        :param MaxMsgSize: Max message size, which defaults to 1,024 KB for the queue of TDMQ for CMQ and cannot be modified.
        :type MaxMsgSize: int
        :param MsgRetentionSeconds: The max period during which a message is retained before it is automatically acknowledged. Value range: 30-43,200 seconds (30 seconds to 12 hours). Default value: 3600 seconds (1 hour).
        :type MsgRetentionSeconds: int
        :param RewindSeconds: Rewindable time of messages in the queue. Value range: 0-1,296,000s (if message rewind is enabled). The value “0” indicates that message rewind is not enabled.
        :type RewindSeconds: int
        :param FirstQueryInterval: First query time
        :type FirstQueryInterval: int
        :param MaxQueryCount: Maximum number of queries
        :type MaxQueryCount: int
        :param DeadLetterQueueName: Dead letter queue name
        :type DeadLetterQueueName: str
        :param MaxTimeToLive: Maximum period in seconds before an unconsumed message expires, which is required if `MaxTimeToLivepolicy` is 1. Value range: 300–43200. This value should be smaller than `MsgRetentionSeconds` (maximum message retention period)
        :type MaxTimeToLive: int
        :param MaxReceiveCount: Maximum number of receipts
        :type MaxReceiveCount: int
        :param Policy: Dead letter queue policy
        :type Policy: int
        :param Trace: Whether to enable message trace. true: yes; false: no. If this field is left empty, the feature will not be enabled.
        :type Trace: bool
        :param Transaction: Whether to enable transaction. 1: yes; 0: no
        :type Transaction: int
        :param RetentionSizeInMB: Queue storage space configured for message rewind. Value range: 1,024-10,240 MB (if message rewind is enabled). The value “0” indicates that message rewind is not enabled.
        :type RetentionSizeInMB: int
        """
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
        self.Transaction = None
        self.RetentionSizeInMB = None


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
        self.Transaction = params.get("Transaction")
        self.RetentionSizeInMB = params.get("RetentionSizeInMB")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCmqQueueAttributeResponse(AbstractModel):
    """ModifyCmqQueueAttribute response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCmqSubscriptionAttributeRequest(AbstractModel):
    """ModifyCmqSubscriptionAttribute request structure.

    """

    def __init__(self):
        r"""
        :param TopicName: Topic name, which must be unique in the same topic under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type TopicName: str
        :param SubscriptionName: Subscription name, which must be unique in the same topic under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type SubscriptionName: str
        :param NotifyStrategy: CMQ push server retry policy in case an error occurs while pushing a message to the endpoint. Valid values:
(1) BACKOFF_RETRY: backoff retry, which is to retry at a fixed interval, discard the message after a certain number of retries, and continue to push the next message.
(2) EXPONENTIAL_DECAY_RETRY: exponential decay retry, which is to retry at an exponentially increasing interval, such as 1s, 2s, 4s, 8s, and so on. As a message can be retained in a topic for one day, failed messages will be discarded at most after one day of retry. Default value: EXPONENTIAL_DECAY_RETRY.
        :type NotifyStrategy: str
        :param NotifyContentFormat: Push content format. Valid values: 1. JSON; 2. SIMPLIFIED, i.e., the raw format. If `Protocol` is `queue`, this value must be `SIMPLIFIED`. If `Protocol` is `HTTP`, both values are acceptable, and the default value is `JSON`.
        :type NotifyContentFormat: str
        :param FilterTags: Message body tag (used for message filtering). The number of tags cannot exceed 5, and each tag can contain up to 16 characters. It is used in conjunction with the `MsgTag` parameter of `(Batch)PublishMessage`. Rules: 1. If `FilterTag` is not configured, no matter whether `MsgTag` is configured, the subscription will receive all messages published to the topic; 2. If the array of `FilterTag` values has a value, only when at least one of the values in the array also exists in the array of `MsgTag` values (i.e., `FilterTag` and `MsgTag` have an intersection) can the subscription receive messages published to the topic; 3. If the array of `FilterTag` values has a value, but `MsgTag` is not configured, then no message published to the topic will be received, which can be considered as a special case of rule 2 as `FilterTag` and `MsgTag` do not intersect in this case. The overall design idea of rules is based on the intention of the subscriber.
        :type FilterTags: list of str
        :param BindingKey: The number of `BindingKey` cannot exceed 5, and the length of each `BindingKey` cannot exceed 64 bytes. This field indicates the filtering policy for subscribing to and receiving messages. Each `BindingKey` includes up to 15 dots (namely up to 16 segments).
        :type BindingKey: list of str
        """
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
        


class ModifyCmqSubscriptionAttributeResponse(AbstractModel):
    """ModifyCmqSubscriptionAttribute response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCmqTopicAttributeRequest(AbstractModel):
    """ModifyCmqTopicAttribute request structure.

    """

    def __init__(self):
        r"""
        :param TopicName: Topic name, which must be unique under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type TopicName: str
        :param MaxMsgSize: Maximum message length. Value range: 1024–65536 bytes (i.e., 1–64 KB). Default value: 65536.
        :type MaxMsgSize: int
        :param MsgRetentionSeconds: Message retention period. Value range: 60–86400 seconds (i.e., 1 minute–1 day). Default value: 86400.
        :type MsgRetentionSeconds: int
        :param Trace: Whether to enable message trace. true: yes; false: no. If this field is left empty, the feature will not be enabled.
        :type Trace: bool
        """
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
        


class ModifyCmqTopicAttributeResponse(AbstractModel):
    """ModifyCmqTopicAttribute response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyEnvironmentAttributesRequest(AbstractModel):
    """ModifyEnvironmentAttributes request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Namespace name.
        :type EnvironmentId: str
        :param MsgTTL: TTL for unconsumed messages in seconds. Maximum value: 1296000 seconds.
        :type MsgTTL: int
        :param Remark: Remarks (up to 128 characters).
        :type Remark: str
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param RetentionPolicy: Message retention policy
        :type RetentionPolicy: :class:`tencentcloud.tdmq.v20200217.models.RetentionPolicy`
        """
        self.EnvironmentId = None
        self.MsgTTL = None
        self.Remark = None
        self.ClusterId = None
        self.RetentionPolicy = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.MsgTTL = params.get("MsgTTL")
        self.Remark = params.get("Remark")
        self.ClusterId = params.get("ClusterId")
        if params.get("RetentionPolicy") is not None:
            self.RetentionPolicy = RetentionPolicy()
            self.RetentionPolicy._deserialize(params.get("RetentionPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEnvironmentAttributesResponse(AbstractModel):
    """ModifyEnvironmentAttributes response structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Namespace name.
        :type EnvironmentId: str
        :param MsgTTL: TTL for unconsumed messages in seconds.
        :type MsgTTL: int
        :param Remark: Remarks (up to 128 characters).
Note: this field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param NamespaceId: Namespace ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type NamespaceId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EnvironmentId = None
        self.MsgTTL = None
        self.Remark = None
        self.NamespaceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.MsgTTL = params.get("MsgTTL")
        self.Remark = params.get("Remark")
        self.NamespaceId = params.get("NamespaceId")
        self.RequestId = params.get("RequestId")


class ModifyEnvironmentRoleRequest(AbstractModel):
    """ModifyEnvironmentRole request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param RoleName: Role name.
        :type RoleName: str
        :param Permissions: Permissions, which is a non-empty string array of `produce` and `consume` at the most.
        :type Permissions: list of str
        :param ClusterId: Cluster ID (required)
        :type ClusterId: str
        """
        self.EnvironmentId = None
        self.RoleName = None
        self.Permissions = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.RoleName = params.get("RoleName")
        self.Permissions = params.get("Permissions")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEnvironmentRoleResponse(AbstractModel):
    """ModifyEnvironmentRole response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRocketMQClusterRequest(AbstractModel):
    """ModifyRocketMQCluster request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: RocketMQ cluster ID
        :type ClusterId: str
        :param ClusterName: 3–64 letters, digits, hyphens, and underscores
        :type ClusterName: str
        :param Remark: Remarks (up to 128 characters)
        :type Remark: str
        """
        self.ClusterId = None
        self.ClusterName = None
        self.Remark = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRocketMQClusterResponse(AbstractModel):
    """ModifyRocketMQCluster response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRocketMQGroupRequest(AbstractModel):
    """ModifyRocketMQGroup request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param NamespaceId: Namespace
        :type NamespaceId: str
        :param GroupId: Consumer group name
        :type GroupId: str
        :param Remark: Remarks (up to 128 characters)
        :type Remark: str
        :param ReadEnable: Whether to enable consumption
        :type ReadEnable: bool
        :param BroadcastEnable: Whether to enable broadcast consumption
        :type BroadcastEnable: bool
        """
        self.ClusterId = None
        self.NamespaceId = None
        self.GroupId = None
        self.Remark = None
        self.ReadEnable = None
        self.BroadcastEnable = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.GroupId = params.get("GroupId")
        self.Remark = params.get("Remark")
        self.ReadEnable = params.get("ReadEnable")
        self.BroadcastEnable = params.get("BroadcastEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRocketMQGroupResponse(AbstractModel):
    """ModifyRocketMQGroup response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRocketMQNamespaceRequest(AbstractModel):
    """ModifyRocketMQNamespace request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param NamespaceId: Namespace name, which can contain 3–64 letters, digits, hyphens, and underscores
        :type NamespaceId: str
        :param Ttl: Retention time of unconsumed messages in milliseconds. Value range: 60 seconds–15 days
        :type Ttl: int
        :param RetentionTime: Retention time for persisted messages in milliseconds
        :type RetentionTime: int
        :param Remark: Remarks (up to 128 characters)
        :type Remark: str
        """
        self.ClusterId = None
        self.NamespaceId = None
        self.Ttl = None
        self.RetentionTime = None
        self.Remark = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.Ttl = params.get("Ttl")
        self.RetentionTime = params.get("RetentionTime")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRocketMQNamespaceResponse(AbstractModel):
    """ModifyRocketMQNamespace response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRocketMQTopicRequest(AbstractModel):
    """ModifyRocketMQTopic request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param NamespaceId: Namespace name
        :type NamespaceId: str
        :param Topic: Topic name
        :type Topic: str
        :param Remark: Remarks (up to 128 characters)
        :type Remark: str
        :param PartitionNum: Number of partitions, which is invalid for globally sequential messages and cannot be less than the current number of partitions.
        :type PartitionNum: int
        """
        self.ClusterId = None
        self.NamespaceId = None
        self.Topic = None
        self.Remark = None
        self.PartitionNum = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.Topic = params.get("Topic")
        self.Remark = params.get("Remark")
        self.PartitionNum = params.get("PartitionNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRocketMQTopicResponse(AbstractModel):
    """ModifyRocketMQTopic response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRoleRequest(AbstractModel):
    """ModifyRole request structure.

    """

    def __init__(self):
        r"""
        :param RoleName: Role name, which can contain up to 32 letters, digits, hyphens, and underscores.
        :type RoleName: str
        :param Remark: Remarks (up to 128 characters).
        :type Remark: str
        :param ClusterId: Cluster ID (required)
        :type ClusterId: str
        """
        self.RoleName = None
        self.Remark = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.RoleName = params.get("RoleName")
        self.Remark = params.get("Remark")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRoleResponse(AbstractModel):
    """ModifyRole response structure.

    """

    def __init__(self):
        r"""
        :param RoleName: Role name
        :type RoleName: str
        :param Remark: Remarks
        :type Remark: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RoleName = None
        self.Remark = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RoleName = params.get("RoleName")
        self.Remark = params.get("Remark")
        self.RequestId = params.get("RequestId")


class ModifyTopicRequest(AbstractModel):
    """ModifyTopic request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param TopicName: Topic name.
        :type TopicName: str
        :param Partitions: Number of partitions, which must be equal to or greater than the original number of partitions. To maintain the original number of partitions, enter the original number. Modifying the number of partitions will take effect only for non-globally sequential messages. There can be up to 128 partitions.
        :type Partitions: int
        :param Remark: Remarks (up to 128 characters).
        :type Remark: str
        :param ClusterId: Pulsar cluster ID
        :type ClusterId: str
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.Partitions = None
        self.Remark = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.Partitions = params.get("Partitions")
        self.Remark = params.get("Remark")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicResponse(AbstractModel):
    """ModifyTopic response structure.

    """

    def __init__(self):
        r"""
        :param Partitions: Number of partitions
        :type Partitions: int
        :param Remark: Remarks (up to 128 characters).
        :type Remark: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Partitions = None
        self.Remark = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Partitions = params.get("Partitions")
        self.Remark = params.get("Remark")
        self.RequestId = params.get("RequestId")


class PublishCmqMsgRequest(AbstractModel):
    """PublishCmqMsg request structure.

    """

    def __init__(self):
        r"""
        :param TopicName: Topic name
        :type TopicName: str
        :param MsgContent: Message content
        :type MsgContent: str
        :param MsgTag: Message tag
        :type MsgTag: list of str
        """
        self.TopicName = None
        self.MsgContent = None
        self.MsgTag = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.MsgContent = params.get("MsgContent")
        self.MsgTag = params.get("MsgTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishCmqMsgResponse(AbstractModel):
    """PublishCmqMsg response structure.

    """

    def __init__(self):
        r"""
        :param Result: `true` indicates that the sending is successful
        :type Result: bool
        :param MsgId: Message ID
        :type MsgId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.MsgId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.MsgId = params.get("MsgId")
        self.RequestId = params.get("RequestId")


class Publisher(AbstractModel):
    """Producer information

    """

    def __init__(self):
        r"""
        :param ProducerId: Producer ID.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ProducerId: int
        :param ProducerName: Producer name.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ProducerName: str
        :param Address: Producer address.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Address: str
        :param ClientVersion: Client version.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ClientVersion: str
        :param MsgRateIn: Message production rate (message/sec).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MsgRateIn: float
        :param MsgThroughputIn: Message production throughput rate (byte/sec).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MsgThroughputIn: float
        :param AverageMsgSize: Average message size in bytes.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AverageMsgSize: float
        :param ConnectedSince: Connection time.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ConnectedSince: str
        :param Partition: Serial number of the topic partition connected to the producer.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Partition: int
        """
        self.ProducerId = None
        self.ProducerName = None
        self.Address = None
        self.ClientVersion = None
        self.MsgRateIn = None
        self.MsgThroughputIn = None
        self.AverageMsgSize = None
        self.ConnectedSince = None
        self.Partition = None


    def _deserialize(self, params):
        self.ProducerId = params.get("ProducerId")
        self.ProducerName = params.get("ProducerName")
        self.Address = params.get("Address")
        self.ClientVersion = params.get("ClientVersion")
        self.MsgRateIn = params.get("MsgRateIn")
        self.MsgThroughputIn = params.get("MsgThroughputIn")
        self.AverageMsgSize = params.get("AverageMsgSize")
        self.ConnectedSince = params.get("ConnectedSince")
        self.Partition = params.get("Partition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReceiveMessageRequest(AbstractModel):
    """ReceiveMessage request structure.

    """

    def __init__(self):
        r"""
        :param Topic: Name of the topic which receives the message. It is better to be the full path of the topic, such as `tenant/namespace/topic`. If it is not specified, `public/default` will be used by default.
        :type Topic: str
        :param SubscriptionName: Subscriber name
        :type SubscriptionName: str
        :param ReceiverQueueSize: Default value: 1000. Messages received by the consumer will first be stored in the `receiverQueueSize` queue to tune the message receiving rate.
        :type ReceiverQueueSize: int
        :param SubInitialPosition: Default value: Latest. It is used to determine the position where the consumer initially receives messages. Valid values: Earliest, Latest.
        :type SubInitialPosition: str
        """
        self.Topic = None
        self.SubscriptionName = None
        self.ReceiverQueueSize = None
        self.SubInitialPosition = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.SubscriptionName = params.get("SubscriptionName")
        self.ReceiverQueueSize = params.get("ReceiverQueueSize")
        self.SubInitialPosition = params.get("SubInitialPosition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReceiveMessageResponse(AbstractModel):
    """ReceiveMessage response structure.

    """

    def __init__(self):
        r"""
        :param MessageID: Unique primary key used to identify the message
        :type MessageID: str
        :param MessagePayload: Content of the received message
        :type MessagePayload: str
        :param AckTopic: Provided to the `Ack` API and used to acknowledge messages in the topic
        :type AckTopic: str
        :param ErrorMsg: Returned error message. If it is an empty string, no error occurred.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param SubName: Returned subscriber name, which will be used when an acknowledgment consumer is created.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubName: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MessageID = None
        self.MessagePayload = None
        self.AckTopic = None
        self.ErrorMsg = None
        self.SubName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MessageID = params.get("MessageID")
        self.MessagePayload = params.get("MessagePayload")
        self.AckTopic = params.get("AckTopic")
        self.ErrorMsg = params.get("ErrorMsg")
        self.SubName = params.get("SubName")
        self.RequestId = params.get("RequestId")


class ResetMsgSubOffsetByTimestampRequest(AbstractModel):
    """ResetMsgSubOffsetByTimestamp request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Namespace name.
        :type EnvironmentId: str
        :param TopicName: Topic name.
        :type TopicName: str
        :param Subscription: Subscriber name.
        :type Subscription: str
        :param ToTimestamp: Timestamp, accurate down to the millisecond.
        :type ToTimestamp: int
        :param ClusterId: Pulsar cluster ID
        :type ClusterId: str
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.Subscription = None
        self.ToTimestamp = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.Subscription = params.get("Subscription")
        self.ToTimestamp = params.get("ToTimestamp")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetMsgSubOffsetByTimestampResponse(AbstractModel):
    """ResetMsgSubOffsetByTimestamp response structure.

    """

    def __init__(self):
        r"""
        :param Result: Result.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ResetRocketMQConsumerOffSetRequest(AbstractModel):
    """ResetRocketMQConsumerOffSet request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID.
        :type ClusterId: str
        :param NamespaceId: Namespace name.
        :type NamespaceId: str
        :param GroupId: Consumer group name.
        :type GroupId: str
        :param Topic: Topic name.
        :type Topic: str
        :param Type: Reset method. 0: Start from the latest offset; 1: Start from specified time point.
        :type Type: int
        :param ResetTimestamp: The specified timestamp that has been reset, in milliseconds. This parameter only takes effect when the value of `Type` is `1`.
        :type ResetTimestamp: int
        """
        self.ClusterId = None
        self.NamespaceId = None
        self.GroupId = None
        self.Topic = None
        self.Type = None
        self.ResetTimestamp = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.GroupId = params.get("GroupId")
        self.Topic = params.get("Topic")
        self.Type = params.get("Type")
        self.ResetTimestamp = params.get("ResetTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetRocketMQConsumerOffSetResponse(AbstractModel):
    """ResetRocketMQConsumerOffSet response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RetentionPolicy(AbstractModel):
    """Message retention policy

    """

    def __init__(self):
        r"""
        :param TimeInMinutes: Message retention period
        :type TimeInMinutes: int
        :param SizeInMB: Message retention size
        :type SizeInMB: int
        """
        self.TimeInMinutes = None
        self.SizeInMB = None


    def _deserialize(self, params):
        self.TimeInMinutes = params.get("TimeInMinutes")
        self.SizeInMB = params.get("SizeInMB")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RewindCmqQueueRequest(AbstractModel):
    """RewindCmqQueue request structure.

    """

    def __init__(self):
        r"""
        :param QueueName: Queue name, which must be unique under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type QueueName: str
        :param StartConsumeTime: After this time is configured, the `(Batch)receiveMessage` API will consume the messages received after this timestamp in the order in which they are produced.
        :type StartConsumeTime: int
        """
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
        


class RewindCmqQueueResponse(AbstractModel):
    """RewindCmqQueue response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RocketMQClusterConfig(AbstractModel):
    """RocketMQ cluster configuration

    """

    def __init__(self):
        r"""
        :param MaxTpsPerNamespace: Maximum TPS per namespace
        :type MaxTpsPerNamespace: int
        :param MaxNamespaceNum: Maximum number of namespaces
        :type MaxNamespaceNum: int
        :param UsedNamespaceNum: Number of used namespaces
        :type UsedNamespaceNum: int
        :param MaxTopicNum: Maximum number of topics
        :type MaxTopicNum: int
        :param UsedTopicNum: Number of used topics
        :type UsedTopicNum: int
        :param MaxGroupNum: Maximum number of groups
        :type MaxGroupNum: int
        :param UsedGroupNum: Number of used groups
        :type UsedGroupNum: int
        :param MaxRetentionTime: Maximum message retention period in milliseconds
        :type MaxRetentionTime: int
        :param MaxLatencyTime: Maximum message delay in milliseconds
        :type MaxLatencyTime: int
        """
        self.MaxTpsPerNamespace = None
        self.MaxNamespaceNum = None
        self.UsedNamespaceNum = None
        self.MaxTopicNum = None
        self.UsedTopicNum = None
        self.MaxGroupNum = None
        self.UsedGroupNum = None
        self.MaxRetentionTime = None
        self.MaxLatencyTime = None


    def _deserialize(self, params):
        self.MaxTpsPerNamespace = params.get("MaxTpsPerNamespace")
        self.MaxNamespaceNum = params.get("MaxNamespaceNum")
        self.UsedNamespaceNum = params.get("UsedNamespaceNum")
        self.MaxTopicNum = params.get("MaxTopicNum")
        self.UsedTopicNum = params.get("UsedTopicNum")
        self.MaxGroupNum = params.get("MaxGroupNum")
        self.UsedGroupNum = params.get("UsedGroupNum")
        self.MaxRetentionTime = params.get("MaxRetentionTime")
        self.MaxLatencyTime = params.get("MaxLatencyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQClusterInfo(AbstractModel):
    """RocketMQ cluster's basic information

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param ClusterName: Cluster name
        :type ClusterName: str
        :param Region: Region information
        :type Region: str
        :param CreateTime: Creation time in milliseconds
        :type CreateTime: int
        :param Remark: Cluster remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param PublicEndPoint: Public network access address
        :type PublicEndPoint: str
        :param VpcEndPoint: VPC access address
        :type VpcEndPoint: str
        :param SupportNamespaceEndpoint: Whether the namespace access point is supported.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SupportNamespaceEndpoint: bool
        """
        self.ClusterId = None
        self.ClusterName = None
        self.Region = None
        self.CreateTime = None
        self.Remark = None
        self.PublicEndPoint = None
        self.VpcEndPoint = None
        self.SupportNamespaceEndpoint = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Region = params.get("Region")
        self.CreateTime = params.get("CreateTime")
        self.Remark = params.get("Remark")
        self.PublicEndPoint = params.get("PublicEndPoint")
        self.VpcEndPoint = params.get("VpcEndPoint")
        self.SupportNamespaceEndpoint = params.get("SupportNamespaceEndpoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQClusterRecentStats(AbstractModel):
    """Recent RocketMQ usage

    """

    def __init__(self):
        r"""
        :param TopicNum: Number of topics
        :type TopicNum: int
        :param ProducedMsgNum: Number of produced messages
        :type ProducedMsgNum: int
        :param ConsumedMsgNum: Number of consumed messages
        :type ConsumedMsgNum: int
        :param AccumulativeMsgNum: Number of retained messages
        :type AccumulativeMsgNum: int
        """
        self.TopicNum = None
        self.ProducedMsgNum = None
        self.ConsumedMsgNum = None
        self.AccumulativeMsgNum = None


    def _deserialize(self, params):
        self.TopicNum = params.get("TopicNum")
        self.ProducedMsgNum = params.get("ProducedMsgNum")
        self.ConsumedMsgNum = params.get("ConsumedMsgNum")
        self.AccumulativeMsgNum = params.get("AccumulativeMsgNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Role(AbstractModel):
    """Role instance

    """

    def __init__(self):
        r"""
        :param RoleName: Role name.
        :type RoleName: str
        :param Token: Value of the role token.
        :type Token: str
        :param Remark: Remarks.
        :type Remark: str
        :param CreateTime: Creation time.
        :type CreateTime: str
        :param UpdateTime: Update time.
        :type UpdateTime: str
        """
        self.RoleName = None
        self.Token = None
        self.Remark = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.RoleName = params.get("RoleName")
        self.Token = params.get("Token")
        self.Remark = params.get("Remark")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendBatchMessagesRequest(AbstractModel):
    """SendBatchMessages request structure.

    """

    def __init__(self):
        r"""
        :param Topic: Name of the topic to which to send the message. It is better to be the full path of the topic, such as `tenant/namespace/topic`. If it is not specified, `public/default` will be used by default.
        :type Topic: str
        :param Payload: Content of the message to be sent
        :type Payload: str
        :param StringToken: String-Type token, which is optional and will be automatically obtained by the system.
        :type StringToken: str
        :param ProducerName: Producer name, which must be globally unique. If it is not configured, the system will automatically generate one.
        :type ProducerName: str
        :param SendTimeout: Message sending timeout period in seconds. Default value: 30s
        :type SendTimeout: int
        :param MaxPendingMessages: Maximum number of produced messages which can be cached in the memory. Default value: 1000
        :type MaxPendingMessages: int
        :param BatchingMaxMessages: Maximum number of messages in each batch. Default value: 1000 messages/batch
        :type BatchingMaxMessages: int
        :param BatchingMaxPublishDelay: Maximum wait time for each batch, after which the batch will be sent no matter whether the specified number or size of messages in the batch is reached. Default value: 10 ms
        :type BatchingMaxPublishDelay: int
        :param BatchingMaxBytes: Maximum allowed size of messages in each batch. Default value: 128 KB
        :type BatchingMaxBytes: int
        """
        self.Topic = None
        self.Payload = None
        self.StringToken = None
        self.ProducerName = None
        self.SendTimeout = None
        self.MaxPendingMessages = None
        self.BatchingMaxMessages = None
        self.BatchingMaxPublishDelay = None
        self.BatchingMaxBytes = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Payload = params.get("Payload")
        self.StringToken = params.get("StringToken")
        self.ProducerName = params.get("ProducerName")
        self.SendTimeout = params.get("SendTimeout")
        self.MaxPendingMessages = params.get("MaxPendingMessages")
        self.BatchingMaxMessages = params.get("BatchingMaxMessages")
        self.BatchingMaxPublishDelay = params.get("BatchingMaxPublishDelay")
        self.BatchingMaxBytes = params.get("BatchingMaxBytes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendBatchMessagesResponse(AbstractModel):
    """SendBatchMessages response structure.

    """

    def __init__(self):
        r"""
        :param MessageId: Unique message ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type MessageId: str
        :param ErrorMsg: Error message. If an empty string is returned, no error occurred.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MessageId = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MessageId = params.get("MessageId")
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class SendCmqMsgRequest(AbstractModel):
    """SendCmqMsg request structure.

    """

    def __init__(self):
        r"""
        :param QueueName: Queue name
        :type QueueName: str
        :param MsgContent: Message content
        :type MsgContent: str
        :param DelaySeconds: Delay time
        :type DelaySeconds: int
        """
        self.QueueName = None
        self.MsgContent = None
        self.DelaySeconds = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        self.MsgContent = params.get("MsgContent")
        self.DelaySeconds = params.get("DelaySeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendCmqMsgResponse(AbstractModel):
    """SendCmqMsg response structure.

    """

    def __init__(self):
        r"""
        :param Result: `true` indicates that the sending is successful
        :type Result: bool
        :param MsgId: Message ID
        :type MsgId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.MsgId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.MsgId = params.get("MsgId")
        self.RequestId = params.get("RequestId")


class SendMessagesRequest(AbstractModel):
    """SendMessages request structure.

    """

    def __init__(self):
        r"""
        :param Topic: Name of the topic to which to send the message. It is better to be the full path of the topic, such as `tenant/namespace/topic`. If it is not specified, `public/default` will be used by default.
        :type Topic: str
        :param Payload: Content of the message to be sent
        :type Payload: str
        :param StringToken: Token used for authentication, which is optional and will be automatically obtained by the system.
        :type StringToken: str
        :param ProducerName: Producer name, which must be globally unique. If it is not configured, the system will randomly generate one.
        :type ProducerName: str
        :param SendTimeout: Message sending timeout period, which is 30s by default.
        :type SendTimeout: int
        :param MaxPendingMessages: Maximum number of produced messages which can be cached in the memory. Default value: 1000
        :type MaxPendingMessages: int
        """
        self.Topic = None
        self.Payload = None
        self.StringToken = None
        self.ProducerName = None
        self.SendTimeout = None
        self.MaxPendingMessages = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Payload = params.get("Payload")
        self.StringToken = params.get("StringToken")
        self.ProducerName = params.get("ProducerName")
        self.SendTimeout = params.get("SendTimeout")
        self.MaxPendingMessages = params.get("MaxPendingMessages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMessagesResponse(AbstractModel):
    """SendMessages response structure.

    """

    def __init__(self):
        r"""
        :param MessageId: messageID, which must be globally unique and is the metadata information used to identify the message.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MessageId: str
        :param ErrorMsg: Returned error message. If an empty string is returned, no error occurred.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.MessageId = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MessageId = params.get("MessageId")
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class SendMsgRequest(AbstractModel):
    """SendMsg request structure.

    """

    def __init__(self):
        r"""
        :param EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param TopicName: Topic name. If the topic is a partitioned topic, you need to specify the partition; otherwise, messages will be sent to partition 0 by default, such as `my_topic-partition-0`.
        :type TopicName: str
        :param MsgContent: Message content, which cannot be empty and can contain up to 5,242,880 bytes.
        :type MsgContent: str
        :param ClusterId: Pulsar cluster ID
        :type ClusterId: str
        """
        self.EnvironmentId = None
        self.TopicName = None
        self.MsgContent = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.EnvironmentId = params.get("EnvironmentId")
        self.TopicName = params.get("TopicName")
        self.MsgContent = params.get("MsgContent")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMsgResponse(AbstractModel):
    """SendMsg response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Sort(AbstractModel):
    """Sort by field

    """

    def __init__(self):
        r"""
        :param Name: Sorting field.
        :type Name: str
        :param Order: Ascending order: `ASC`; descending order: `DESC`.
        :type Order: str
        """
        self.Name = None
        self.Order = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Type of the tag key/value

    """

    def __init__(self):
        r"""
        :param TagKey: Value of the tag key
        :type TagKey: str
        :param TagValue: Value of the tag value
        :type TagValue: str
        """
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
        


class UnbindCmqDeadLetterRequest(AbstractModel):
    """UnbindCmqDeadLetter request structure.

    """

    def __init__(self):
        r"""
        :param SourceQueueName: Source queue name of dead letter policy. Calling this API will clear the dead letter queue policy of this queue.
        :type SourceQueueName: str
        """
        self.SourceQueueName = None


    def _deserialize(self, params):
        self.SourceQueueName = params.get("SourceQueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindCmqDeadLetterResponse(AbstractModel):
    """UnbindCmqDeadLetter response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VpcBindRecord(AbstractModel):
    """VPC binding record

    """

    def __init__(self):
        r"""
        :param UniqueVpcId: Tenant VPC ID
        :type UniqueVpcId: str
        :param UniqueSubnetId: Tenant VPC subnet ID
        :type UniqueSubnetId: str
        :param RouterId: Route ID
        :type RouterId: str
        :param Ip: VPC ID
        :type Ip: str
        :param Port: VPC port
        :type Port: int
        :param Remark: Remarks (up to 128 characters)
Note: this field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        """
        self.UniqueVpcId = None
        self.UniqueSubnetId = None
        self.RouterId = None
        self.Ip = None
        self.Port = None
        self.Remark = None


    def _deserialize(self, params):
        self.UniqueVpcId = params.get("UniqueVpcId")
        self.UniqueSubnetId = params.get("UniqueSubnetId")
        self.RouterId = params.get("RouterId")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        