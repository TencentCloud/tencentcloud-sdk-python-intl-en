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
        :param _MessageId: Unique ID used to identify the message, which can be obtained from the returned value of `receiveMessage`.
        :type MessageId: str
        :param _AckTopic: Topic name, which can be obtained from the returned value of `receiveMessage` and is better to be the full path of the topic, such as `tenant/namespace/topic`. If it is not specified, `public/default` will be used by default.
        :type AckTopic: str
        :param _SubName: Subscriber name, which can be obtained from the returned value of `receiveMessage`. Make sure that it is the same as the subscriber name identified in `receiveMessage`; otherwise, the received message cannot be correctly acknowledged.
        :type SubName: str
        """
        self._MessageId = None
        self._AckTopic = None
        self._SubName = None

    @property
    def MessageId(self):
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

    @property
    def AckTopic(self):
        return self._AckTopic

    @AckTopic.setter
    def AckTopic(self, AckTopic):
        self._AckTopic = AckTopic

    @property
    def SubName(self):
        return self._SubName

    @SubName.setter
    def SubName(self, SubName):
        self._SubName = SubName


    def _deserialize(self, params):
        self._MessageId = params.get("MessageId")
        self._AckTopic = params.get("AckTopic")
        self._SubName = params.get("SubName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcknowledgeMessageResponse(AbstractModel):
    """AcknowledgeMessage response structure.

    """

    def __init__(self):
        r"""
        :param _ErrorMsg: If it is an empty string, no error occurred.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class BindCluster(AbstractModel):
    """Information of dedicated clusters

    """

    def __init__(self):
        r"""
        :param _ClusterName: Name of a physical cluster.
        :type ClusterName: str
        """
        self._ClusterName = None

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName


    def _deserialize(self, params):
        self._ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearCmqQueueRequest(AbstractModel):
    """ClearCmqQueue request structure.

    """

    def __init__(self):
        r"""
        :param _QueueName: Queue name, which must be unique under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
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
        


class ClearCmqQueueResponse(AbstractModel):
    """ClearCmqQueue response structure.

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


class ClearCmqSubscriptionFilterTagsRequest(AbstractModel):
    """ClearCmqSubscriptionFilterTags request structure.

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name, which must be unique in the same topic under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type TopicName: str
        :param _SubscriptionName: Subscription name, which must be unique in the same topic under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
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
        


class ClearCmqSubscriptionFilterTagsResponse(AbstractModel):
    """ClearCmqSubscriptionFilterTags response structure.

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


class Cluster(AbstractModel):
    """Set of cluster information

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID.
        :type ClusterId: str
        :param _ClusterName: Cluster name.
        :type ClusterName: str
        :param _Remark: Remarks.
        :type Remark: str
        :param _EndPointNum: Number of access points
        :type EndPointNum: int
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _Healthy: Whether the cluster is healthy. 1: healthy; 0: exceptional
        :type Healthy: int
        :param _HealthyInfo: Cluster health information
Note: this field may return null, indicating that no valid values can be obtained.
        :type HealthyInfo: str
        :param _Status: Cluster status. 0: creating; 1: normal; 2: terminating; 3: deleted; 4. isolated; 5. creation failed; 6: deletion failed
        :type Status: int
        :param _MaxNamespaceNum: Maximum number of namespaces
        :type MaxNamespaceNum: int
        :param _MaxTopicNum: Maximum number of topics
        :type MaxTopicNum: int
        :param _MaxQps: Maximum QPS
        :type MaxQps: int
        :param _MessageRetentionTime: Maximum message retention period in seconds
        :type MessageRetentionTime: int
        :param _MaxStorageCapacity: Maximum storage capacity
        :type MaxStorageCapacity: int
        :param _Version: Cluster version
Note: this field may return null, indicating that no valid values can be obtained.
        :type Version: str
        :param _PublicEndPoint: Public network access point
Note: this field may return null, indicating that no valid values can be obtained.
        :type PublicEndPoint: str
        :param _VpcEndPoint: VPC access point
Note: this field may return null, indicating that no valid values can be obtained.
        :type VpcEndPoint: str
        :param _NamespaceNum: Number of namespaces
Note: this field may return null, indicating that no valid values can be obtained.
        :type NamespaceNum: int
        :param _UsedStorageBudget: Limit of used storage in MB
Note: this field may return null, indicating that no valid values can be obtained.
        :type UsedStorageBudget: int
        :param _MaxPublishRateInMessages: Maximum message production rate in messages
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxPublishRateInMessages: int
        :param _MaxDispatchRateInMessages: Maximum message push rate in messages
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxDispatchRateInMessages: int
        :param _MaxPublishRateInBytes: Maximum message production rate in bytes
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxPublishRateInBytes: int
        :param _MaxDispatchRateInBytes: Maximum message push rate in bytes
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxDispatchRateInBytes: int
        :param _TopicNum: Number of created topics
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicNum: int
        :param _MaxMessageDelayInSeconds: Maximum message delay in seconds
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxMessageDelayInSeconds: int
        :param _PublicAccessEnabled: Whether to enable public network access. If this parameter is left empty, the feature will be enabled by default
Note: this field may return null, indicating that no valid values can be obtained.
        :type PublicAccessEnabled: bool
        :param _Tags: Tag
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _PayMode: Billing mode:
`0`: Pay-as-you-go
`1`: Monthly subscription
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type PayMode: int
        """
        self._ClusterId = None
        self._ClusterName = None
        self._Remark = None
        self._EndPointNum = None
        self._CreateTime = None
        self._Healthy = None
        self._HealthyInfo = None
        self._Status = None
        self._MaxNamespaceNum = None
        self._MaxTopicNum = None
        self._MaxQps = None
        self._MessageRetentionTime = None
        self._MaxStorageCapacity = None
        self._Version = None
        self._PublicEndPoint = None
        self._VpcEndPoint = None
        self._NamespaceNum = None
        self._UsedStorageBudget = None
        self._MaxPublishRateInMessages = None
        self._MaxDispatchRateInMessages = None
        self._MaxPublishRateInBytes = None
        self._MaxDispatchRateInBytes = None
        self._TopicNum = None
        self._MaxMessageDelayInSeconds = None
        self._PublicAccessEnabled = None
        self._Tags = None
        self._PayMode = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def EndPointNum(self):
        return self._EndPointNum

    @EndPointNum.setter
    def EndPointNum(self, EndPointNum):
        self._EndPointNum = EndPointNum

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Healthy(self):
        return self._Healthy

    @Healthy.setter
    def Healthy(self, Healthy):
        self._Healthy = Healthy

    @property
    def HealthyInfo(self):
        return self._HealthyInfo

    @HealthyInfo.setter
    def HealthyInfo(self, HealthyInfo):
        self._HealthyInfo = HealthyInfo

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MaxNamespaceNum(self):
        return self._MaxNamespaceNum

    @MaxNamespaceNum.setter
    def MaxNamespaceNum(self, MaxNamespaceNum):
        self._MaxNamespaceNum = MaxNamespaceNum

    @property
    def MaxTopicNum(self):
        return self._MaxTopicNum

    @MaxTopicNum.setter
    def MaxTopicNum(self, MaxTopicNum):
        self._MaxTopicNum = MaxTopicNum

    @property
    def MaxQps(self):
        return self._MaxQps

    @MaxQps.setter
    def MaxQps(self, MaxQps):
        self._MaxQps = MaxQps

    @property
    def MessageRetentionTime(self):
        return self._MessageRetentionTime

    @MessageRetentionTime.setter
    def MessageRetentionTime(self, MessageRetentionTime):
        self._MessageRetentionTime = MessageRetentionTime

    @property
    def MaxStorageCapacity(self):
        return self._MaxStorageCapacity

    @MaxStorageCapacity.setter
    def MaxStorageCapacity(self, MaxStorageCapacity):
        self._MaxStorageCapacity = MaxStorageCapacity

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def PublicEndPoint(self):
        return self._PublicEndPoint

    @PublicEndPoint.setter
    def PublicEndPoint(self, PublicEndPoint):
        self._PublicEndPoint = PublicEndPoint

    @property
    def VpcEndPoint(self):
        return self._VpcEndPoint

    @VpcEndPoint.setter
    def VpcEndPoint(self, VpcEndPoint):
        self._VpcEndPoint = VpcEndPoint

    @property
    def NamespaceNum(self):
        return self._NamespaceNum

    @NamespaceNum.setter
    def NamespaceNum(self, NamespaceNum):
        self._NamespaceNum = NamespaceNum

    @property
    def UsedStorageBudget(self):
        return self._UsedStorageBudget

    @UsedStorageBudget.setter
    def UsedStorageBudget(self, UsedStorageBudget):
        self._UsedStorageBudget = UsedStorageBudget

    @property
    def MaxPublishRateInMessages(self):
        return self._MaxPublishRateInMessages

    @MaxPublishRateInMessages.setter
    def MaxPublishRateInMessages(self, MaxPublishRateInMessages):
        self._MaxPublishRateInMessages = MaxPublishRateInMessages

    @property
    def MaxDispatchRateInMessages(self):
        return self._MaxDispatchRateInMessages

    @MaxDispatchRateInMessages.setter
    def MaxDispatchRateInMessages(self, MaxDispatchRateInMessages):
        self._MaxDispatchRateInMessages = MaxDispatchRateInMessages

    @property
    def MaxPublishRateInBytes(self):
        return self._MaxPublishRateInBytes

    @MaxPublishRateInBytes.setter
    def MaxPublishRateInBytes(self, MaxPublishRateInBytes):
        self._MaxPublishRateInBytes = MaxPublishRateInBytes

    @property
    def MaxDispatchRateInBytes(self):
        return self._MaxDispatchRateInBytes

    @MaxDispatchRateInBytes.setter
    def MaxDispatchRateInBytes(self, MaxDispatchRateInBytes):
        self._MaxDispatchRateInBytes = MaxDispatchRateInBytes

    @property
    def TopicNum(self):
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def MaxMessageDelayInSeconds(self):
        return self._MaxMessageDelayInSeconds

    @MaxMessageDelayInSeconds.setter
    def MaxMessageDelayInSeconds(self, MaxMessageDelayInSeconds):
        self._MaxMessageDelayInSeconds = MaxMessageDelayInSeconds

    @property
    def PublicAccessEnabled(self):
        return self._PublicAccessEnabled

    @PublicAccessEnabled.setter
    def PublicAccessEnabled(self, PublicAccessEnabled):
        self._PublicAccessEnabled = PublicAccessEnabled

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Remark = params.get("Remark")
        self._EndPointNum = params.get("EndPointNum")
        self._CreateTime = params.get("CreateTime")
        self._Healthy = params.get("Healthy")
        self._HealthyInfo = params.get("HealthyInfo")
        self._Status = params.get("Status")
        self._MaxNamespaceNum = params.get("MaxNamespaceNum")
        self._MaxTopicNum = params.get("MaxTopicNum")
        self._MaxQps = params.get("MaxQps")
        self._MessageRetentionTime = params.get("MessageRetentionTime")
        self._MaxStorageCapacity = params.get("MaxStorageCapacity")
        self._Version = params.get("Version")
        self._PublicEndPoint = params.get("PublicEndPoint")
        self._VpcEndPoint = params.get("VpcEndPoint")
        self._NamespaceNum = params.get("NamespaceNum")
        self._UsedStorageBudget = params.get("UsedStorageBudget")
        self._MaxPublishRateInMessages = params.get("MaxPublishRateInMessages")
        self._MaxDispatchRateInMessages = params.get("MaxDispatchRateInMessages")
        self._MaxPublishRateInBytes = params.get("MaxPublishRateInBytes")
        self._MaxDispatchRateInBytes = params.get("MaxDispatchRateInBytes")
        self._TopicNum = params.get("TopicNum")
        self._MaxMessageDelayInSeconds = params.get("MaxMessageDelayInSeconds")
        self._PublicAccessEnabled = params.get("PublicAccessEnabled")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmqDeadLetterPolicy(AbstractModel):
    """cmq DeadLetterPolicy

    """

    def __init__(self):
        r"""
        :param _DeadLetterQueue: Dead letter queue.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeadLetterQueue: str
        :param _Policy: Dead letter queue policy.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Policy: int
        :param _MaxTimeToLive: Maximum period in seconds before an unconsumed message expires, which is required if `Policy` is 1. Value range: 300–43200. This value should be smaller than `MsgRetentionSeconds` (maximum message retention period)
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxTimeToLive: int
        :param _MaxReceiveCount: Maximum number of receipts.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxReceiveCount: int
        """
        self._DeadLetterQueue = None
        self._Policy = None
        self._MaxTimeToLive = None
        self._MaxReceiveCount = None

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
        


class CmqDeadLetterSource(AbstractModel):
    """Cmq DeadLetterSource

    """

    def __init__(self):
        r"""
        :param _QueueId: Message queue ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type QueueId: str
        :param _QueueName: Message queue name.
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
        


class CmqQueue(AbstractModel):
    """Batch queue attribute information of CMQ

    """

    def __init__(self):
        r"""
        :param _QueueId: Message queue ID.
        :type QueueId: str
        :param _QueueName: Message queue name.
        :type QueueName: str
        :param _Qps: Limit of the number of messages produced per second. The value for consumed messages is 1.1 times this value.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Qps: int
        :param _Bps: Bandwidth limit.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Bps: int
        :param _MaxDelaySeconds: Maximum retention period for inflight messages.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxDelaySeconds: int
        :param _MaxMsgHeapNum: Maximum number of heaped messages. The value range is 1,000,000–10,000,000 during the beta test and can be 1,000,000–1,000,000,000 after the product is officially released. The default value is 10,000,000 during the beta test and will be 100,000,000 after the product is officially released.
        :type MaxMsgHeapNum: int
        :param _PollingWaitSeconds: Long polling wait time for message reception. Value range: 0–30 seconds. Default value: 0.
Note: this field may return null, indicating that no valid values can be obtained.
        :type PollingWaitSeconds: int
        :param _MsgRetentionSeconds: Message retention period. Value range: 60–1296000 seconds (i.e., 1 minute–15 days). Default value: 345600 (i.e., 4 days).
Note: this field may return null, indicating that no valid values can be obtained.
        :type MsgRetentionSeconds: int
        :param _VisibilityTimeout: Message visibility timeout period. Value range: 1–43200 seconds (i.e., 12 hours). Default value: 30.
Note: this field may return null, indicating that no valid values can be obtained.
        :type VisibilityTimeout: int
        :param _MaxMsgSize: Maximum message length. Value range: 1024–1048576 bytes (i.e., 1–1024 KB). Default value: 65536.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxMsgSize: int
        :param _RewindSeconds: Maximum time range during which a message can be rewound in the queue, which ranges from 0 to 43,200 seconds. 0 indicates that message rewind is disabled.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RewindSeconds: int
        :param _CreateTime: Queue creation time. A Unix timestamp accurate down to the millisecond will be returned.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: int
        :param _LastModifyTime: Time when the queue attribute is last modified. A Unix timestamp accurate down to the millisecond will be returned.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastModifyTime: int
        :param _ActiveMsgNum: Total number of messages in `Active` status (i.e., unconsumed) in the queue, which is an approximate value.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ActiveMsgNum: int
        :param _InactiveMsgNum: Total number of messages in `Inactive` status (i.e., being consumed) in the queue, which is an approximate value.
Note: this field may return null, indicating that no valid values can be obtained.
        :type InactiveMsgNum: int
        :param _DelayMsgNum: Number of delayed messages.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DelayMsgNum: int
        :param _RewindMsgNum: Number of retained messages which have been deleted by the `DelMsg` API but are still within their rewind time range.
Note: this field may return null, indicating that no valid values can be obtained.
        :type RewindMsgNum: int
        :param _MinMsgTime: Minimum unconsumed time of message in seconds.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MinMsgTime: int
        :param _Transaction: Transaction message queue. true: transaction message type; false: other message types.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Transaction: bool
        :param _DeadLetterSource: Dead letter queue.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeadLetterSource: list of CmqDeadLetterSource
        :param _DeadLetterPolicy: Dead letter queue policy.
Note: this field may return null, indicating that no valid values can be obtained.
        :type DeadLetterPolicy: :class:`tencentcloud.tdmq.v20200217.models.CmqDeadLetterPolicy`
        :param _TransactionPolicy: Transaction message policy.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TransactionPolicy: :class:`tencentcloud.tdmq.v20200217.models.CmqTransactionPolicy`
        :param _CreateUin: Creator `Uin`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateUin: int
        :param _Tags: Associated tag.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _Trace: Message trace. true: enabled; false: not enabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type Trace: bool
        :param _TenantId: Tenant ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type TenantId: str
        :param _NamespaceName: Namespace name
Note: this field may return null, indicating that no valid values can be obtained.
        :type NamespaceName: str
        :param _Status: Cluster status. 0: creating; 1: normal; 2: terminating; 3: deleted; 4. isolated; 5. creation failed; 6: deletion failed
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Status: int
        :param _MaxUnackedMsgNum: The maximum number of unacknowledged messages.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MaxUnackedMsgNum: int
        :param _MaxMsgBacklogSize: Maximum size of heaped messages in bytes.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MaxMsgBacklogSize: int
        :param _RetentionSizeInMB: Queue storage space configured for message rewind. Value range: 1,024-10,240 MB (if message rewind is enabled). The value “0” indicates that message rewind is not enabled.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type RetentionSizeInMB: int
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
        self._TenantId = None
        self._NamespaceName = None
        self._Status = None
        self._MaxUnackedMsgNum = None
        self._MaxMsgBacklogSize = None
        self._RetentionSizeInMB = None

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

    @property
    def TenantId(self):
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MaxUnackedMsgNum(self):
        return self._MaxUnackedMsgNum

    @MaxUnackedMsgNum.setter
    def MaxUnackedMsgNum(self, MaxUnackedMsgNum):
        self._MaxUnackedMsgNum = MaxUnackedMsgNum

    @property
    def MaxMsgBacklogSize(self):
        return self._MaxMsgBacklogSize

    @MaxMsgBacklogSize.setter
    def MaxMsgBacklogSize(self, MaxMsgBacklogSize):
        self._MaxMsgBacklogSize = MaxMsgBacklogSize

    @property
    def RetentionSizeInMB(self):
        return self._RetentionSizeInMB

    @RetentionSizeInMB.setter
    def RetentionSizeInMB(self, RetentionSizeInMB):
        self._RetentionSizeInMB = RetentionSizeInMB


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
                obj = CmqDeadLetterSource()
                obj._deserialize(item)
                self._DeadLetterSource.append(obj)
        if params.get("DeadLetterPolicy") is not None:
            self._DeadLetterPolicy = CmqDeadLetterPolicy()
            self._DeadLetterPolicy._deserialize(params.get("DeadLetterPolicy"))
        if params.get("TransactionPolicy") is not None:
            self._TransactionPolicy = CmqTransactionPolicy()
            self._TransactionPolicy._deserialize(params.get("TransactionPolicy"))
        self._CreateUin = params.get("CreateUin")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Trace = params.get("Trace")
        self._TenantId = params.get("TenantId")
        self._NamespaceName = params.get("NamespaceName")
        self._Status = params.get("Status")
        self._MaxUnackedMsgNum = params.get("MaxUnackedMsgNum")
        self._MaxMsgBacklogSize = params.get("MaxMsgBacklogSize")
        self._RetentionSizeInMB = params.get("RetentionSizeInMB")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmqSubscription(AbstractModel):
    """Subscription response parameter in CMQ

    """

    def __init__(self):
        r"""
        :param _SubscriptionName: Subscription name, which must be unique in the same topic under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubscriptionName: str
        :param _SubscriptionId: Subscription ID, which will be used during monitoring data pull.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubscriptionId: str
        :param _TopicOwner: Subscription owner `APPID`.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicOwner: int
        :param _MsgCount: Number of messages to be delivered in the subscription.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MsgCount: int
        :param _LastModifyTime: Time when the subscription attribute is last modified. A Unix timestamp accurate down to the millisecond will be returned.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastModifyTime: int
        :param _CreateTime: Subscription creation time. A Unix timestamp accurate down to the millisecond will be returned.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: int
        :param _BindingKey: Filtering policy for subscribing to and receiving messages.
Note: this field may return null, indicating that no valid values can be obtained.
        :type BindingKey: list of str
        :param _Endpoint: Endpoint that receives notifications, which varies by `protocol`: for HTTP, the endpoint must start with `http://`, and the `host` can be a domain or IP; for `queue`, `queueName` should be entered.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Endpoint: str
        :param _FilterTags: Filtering policy selected when a subscription is created:
If `filterType` is 1, `filterTag` will be used for filtering.
If `filterType` is 2, `bindingKey` will be used for filtering.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FilterTags: list of str
        :param _Protocol: Subscription protocol. Currently, two protocols are supported: HTTP and queue. To use the HTTP protocol, you need to build your own web server to receive messages. With the queue protocol, messages are automatically pushed to a CMQ queue and you can pull them concurrently.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Protocol: str
        :param _NotifyStrategy: CMQ push server retry policy in case an error occurs while pushing a message to the endpoint. Valid values:
(1) BACKOFF_RETRY: backoff retry, which is to retry at a fixed interval, discard the message after a certain number of retries, and continue to push the next message.
(2) EXPONENTIAL_DECAY_RETRY: exponential decay retry, which is to retry at an exponentially increasing interval, such as 1s, 2s, 4s, 8s, and so on. As a message can be retained in a topic for one day, failed messages will be discarded at most after one day of retry. Default value: EXPONENTIAL_DECAY_RETRY.
Note: this field may return null, indicating that no valid values can be obtained.
        :type NotifyStrategy: str
        :param _NotifyContentFormat: Push content format. Valid values: 1. JSON; 2. SIMPLIFIED, i.e., the raw format. If `protocol` is `queue`, this value must be `SIMPLIFIED`. If `protocol` is `HTTP`, both values are acceptable, and the default value is `JSON`.
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
        


class CmqTopic(AbstractModel):
    """Display field of the returned CMQ topic information

    """

    def __init__(self):
        r"""
        :param _TopicId: Topic ID.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicId: str
        :param _TopicName: Topic name.
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicName: str
        :param _MsgRetentionSeconds: Maximum lifecycle of message in topic. After the period specified by this parameter has elapsed since a message is sent to the topic, the message will be deleted no matter whether it has been successfully pushed to the user. This parameter is measured in seconds and defaulted to one day (86,400 seconds), which cannot be modified.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MsgRetentionSeconds: int
        :param _MaxMsgSize: Maximum message size, which ranges from 1,024 to 1,048,576 bytes (i.e., 1–1,024 KB). The default value is 65,536.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxMsgSize: int
        :param _Qps: Number of messages published per second.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Qps: int
        :param _FilterType: Filtering policy selected when a subscription is created:
If `filterType` is 1, `FilterTag` will be used for filtering.
If `filterType` is 2, `BindingKey` will be used for filtering.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FilterType: int
        :param _CreateTime: Topic creation time. A Unix timestamp accurate down to the millisecond will be returned.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateTime: int
        :param _LastModifyTime: Time when the topic attribute is last modified. A Unix timestamp accurate down to the millisecond will be returned.
Note: this field may return null, indicating that no valid values can be obtained.
        :type LastModifyTime: int
        :param _MsgCount: Number of current messages in the topic (number of retained messages).
Note: this field may return null, indicating that no valid values can be obtained.
        :type MsgCount: int
        :param _CreateUin: Creator `Uin`. The `resource` field for CAM authentication is composed of this field.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CreateUin: int
        :param _Tags: Associated tag.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param _Trace: Message trace. true: enabled; false: not enabled
Note: this field may return null, indicating that no valid values can be obtained.
        :type Trace: bool
        :param _TenantId: Tenant ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type TenantId: str
        :param _NamespaceName: Namespace name
Note: this field may return null, indicating that no valid values can be obtained.
        :type NamespaceName: str
        :param _Status: Cluster status. 0: creating; 1: normal; 2: terminating; 3: deleted; 4. isolated; 5. creation failed; 6: deletion failed
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Status: int
        :param _BrokerType: Valid values: `0` (Pulsar), `1` (RocketMQ).
Note: This field may return null, indicating that no valid values can be obtained.
        :type BrokerType: int
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
        self._TenantId = None
        self._NamespaceName = None
        self._Status = None
        self._BrokerType = None

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

    @property
    def TenantId(self):
        return self._TenantId

    @TenantId.setter
    def TenantId(self, TenantId):
        self._TenantId = TenantId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BrokerType(self):
        return self._BrokerType

    @BrokerType.setter
    def BrokerType(self, BrokerType):
        self._BrokerType = BrokerType


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
        self._TenantId = params.get("TenantId")
        self._NamespaceName = params.get("NamespaceName")
        self._Status = params.get("Status")
        self._BrokerType = params.get("BrokerType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CmqTransactionPolicy(AbstractModel):
    """cmq TransactionPolicy

    """

    def __init__(self):
        r"""
        :param _FirstQueryInterval: First lookback time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type FirstQueryInterval: int
        :param _MaxQueryCount: Maximum number of queries.
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
        


class Consumer(AbstractModel):
    """Consumer

    """

    def __init__(self):
        r"""
        :param _ConnectedSince: The time when the consumer started connecting.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConnectedSince: str
        :param _ConsumerAddr: Consumer address.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConsumerAddr: str
        :param _ConsumerName: Consumer name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConsumerName: str
        :param _ClientVersion: Consumer version.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClientVersion: str
        :param _Partition: Serial number of the topic partition connected to the consumer.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Partition: int
        """
        self._ConnectedSince = None
        self._ConsumerAddr = None
        self._ConsumerName = None
        self._ClientVersion = None
        self._Partition = None

    @property
    def ConnectedSince(self):
        return self._ConnectedSince

    @ConnectedSince.setter
    def ConnectedSince(self, ConnectedSince):
        self._ConnectedSince = ConnectedSince

    @property
    def ConsumerAddr(self):
        return self._ConsumerAddr

    @ConsumerAddr.setter
    def ConsumerAddr(self, ConsumerAddr):
        self._ConsumerAddr = ConsumerAddr

    @property
    def ConsumerName(self):
        return self._ConsumerName

    @ConsumerName.setter
    def ConsumerName(self, ConsumerName):
        self._ConsumerName = ConsumerName

    @property
    def ClientVersion(self):
        return self._ClientVersion

    @ClientVersion.setter
    def ClientVersion(self, ClientVersion):
        self._ClientVersion = ClientVersion

    @property
    def Partition(self):
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition


    def _deserialize(self, params):
        self._ConnectedSince = params.get("ConnectedSince")
        self._ConsumerAddr = params.get("ConsumerAddr")
        self._ConsumerName = params.get("ConsumerName")
        self._ClientVersion = params.get("ClientVersion")
        self._Partition = params.get("Partition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumersSchedule(AbstractModel):
    """Consumption progress details

    """

    def __init__(self):
        r"""
        :param _Partitions: ID of the current partition.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Partitions: int
        :param _NumberOfEntries: The number of messages.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NumberOfEntries: int
        :param _MsgBacklog: The number of heaped messages.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MsgBacklog: int
        :param _MsgRateOut: The total number of messages delivered by the consumer per second.
        :type MsgRateOut: str
        :param _MsgThroughputOut: The size (in bytes) of messages consumed by the consumer per second.
        :type MsgThroughputOut: str
        :param _MsgRateExpired: Percentage of messages discarded due to timeout.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MsgRateExpired: str
        """
        self._Partitions = None
        self._NumberOfEntries = None
        self._MsgBacklog = None
        self._MsgRateOut = None
        self._MsgThroughputOut = None
        self._MsgRateExpired = None

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def NumberOfEntries(self):
        return self._NumberOfEntries

    @NumberOfEntries.setter
    def NumberOfEntries(self, NumberOfEntries):
        self._NumberOfEntries = NumberOfEntries

    @property
    def MsgBacklog(self):
        return self._MsgBacklog

    @MsgBacklog.setter
    def MsgBacklog(self, MsgBacklog):
        self._MsgBacklog = MsgBacklog

    @property
    def MsgRateOut(self):
        return self._MsgRateOut

    @MsgRateOut.setter
    def MsgRateOut(self, MsgRateOut):
        self._MsgRateOut = MsgRateOut

    @property
    def MsgThroughputOut(self):
        return self._MsgThroughputOut

    @MsgThroughputOut.setter
    def MsgThroughputOut(self, MsgThroughputOut):
        self._MsgThroughputOut = MsgThroughputOut

    @property
    def MsgRateExpired(self):
        return self._MsgRateExpired

    @MsgRateExpired.setter
    def MsgRateExpired(self, MsgRateExpired):
        self._MsgRateExpired = MsgRateExpired


    def _deserialize(self, params):
        self._Partitions = params.get("Partitions")
        self._NumberOfEntries = params.get("NumberOfEntries")
        self._MsgBacklog = params.get("MsgBacklog")
        self._MsgRateOut = params.get("MsgRateOut")
        self._MsgThroughputOut = params.get("MsgThroughputOut")
        self._MsgRateExpired = params.get("MsgRateExpired")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterRequest(AbstractModel):
    """CreateCluster request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterName: Cluster name, which can contain up to 16 letters, digits, hyphens, and underscores.
        :type ClusterName: str
        :param _BindClusterId: ID of your dedicated physical cluster. If it is not passed in, cluster resources will be created in a public cluster by default.
        :type BindClusterId: int
        :param _Remark: Remarks (up to 128 characters).
        :type Remark: str
        :param _Tags: Cluster tag list (deprecated).
        :type Tags: list of Tag
        :param _PublicAccessEnabled: Whether to enable public network access. If this parameter is left empty, the feature will be enabled by default
        :type PublicAccessEnabled: bool
        """
        self._ClusterName = None
        self._BindClusterId = None
        self._Remark = None
        self._Tags = None
        self._PublicAccessEnabled = None

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def BindClusterId(self):
        return self._BindClusterId

    @BindClusterId.setter
    def BindClusterId(self, BindClusterId):
        self._BindClusterId = BindClusterId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def PublicAccessEnabled(self):
        return self._PublicAccessEnabled

    @PublicAccessEnabled.setter
    def PublicAccessEnabled(self, PublicAccessEnabled):
        self._PublicAccessEnabled = PublicAccessEnabled


    def _deserialize(self, params):
        self._ClusterName = params.get("ClusterName")
        self._BindClusterId = params.get("BindClusterId")
        self._Remark = params.get("Remark")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._PublicAccessEnabled = params.get("PublicAccessEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterResponse(AbstractModel):
    """CreateCluster response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterId = None
        self._RequestId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._RequestId = params.get("RequestId")


class CreateCmqQueueRequest(AbstractModel):
    """CreateCmqQueue request structure.

    """

    def __init__(self):
        r"""
        :param _QueueName: Queue name, which must be unique under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type QueueName: str
        :param _MaxMsgHeapNum: Maximum number of heaped messages. The value range is 1,000,000–10,000,000 during the beta test and can be 1,000,000–1,000,000,000 after the product is officially released. The default value is 10,000,000 during the beta test and will be 100,000,000 after the product is officially released.
        :type MaxMsgHeapNum: int
        :param _PollingWaitSeconds: Long polling wait time for message reception. Value range: 0–30 seconds. Default value: 0.
        :type PollingWaitSeconds: int
        :param _VisibilityTimeout: Message visibility timeout period. Value range: 1–43200 seconds (i.e., 12 hours). Default value: 30.
        :type VisibilityTimeout: int
        :param _MaxMsgSize: Maximum message length. Value range: 1024–65536 bytes (i.e., 1–64 KB). Default value: 65536.
        :type MaxMsgSize: int
        :param _MsgRetentionSeconds: The max period during which a message is retained before it is automatically acknowledged. Value range: 30-43,200 seconds (30 seconds to 12 hours). Default value: 3600 seconds (1 hour).
        :type MsgRetentionSeconds: int
        :param _RewindSeconds: Rewindable time of messages in the queue. Value range: 0-1,296,000s (if message rewind is enabled). The value “0” indicates that message rewind is not enabled.
        :type RewindSeconds: int
        :param _Transaction: 1: transaction queue; 0: general queue
        :type Transaction: int
        :param _FirstQueryInterval: First lookback interval
        :type FirstQueryInterval: int
        :param _MaxQueryCount: Maximum number of lookbacks
        :type MaxQueryCount: int
        :param _DeadLetterQueueName: Dead letter queue name
        :type DeadLetterQueueName: str
        :param _Policy: Dead letter policy. 0: message has been consumed multiple times but not deleted; 1: `Time-To-Live` has elapsed
        :type Policy: int
        :param _MaxReceiveCount: Maximum receipt times. Value range: 1–1000
        :type MaxReceiveCount: int
        :param _MaxTimeToLive: Maximum period in seconds before an unconsumed message expires, which is required if `policy` is 1. Value range: 300–43200. This value should be smaller than `msgRetentionSeconds` (maximum message retention period)
        :type MaxTimeToLive: int
        :param _Trace: Whether to enable message trace. true: yes; false: no. If this field is not configured, the feature will not be enabled
        :type Trace: bool
        :param _Tags: Tag array.
        :type Tags: list of Tag
        :param _RetentionSizeInMB: Queue storage space configured for message rewind. Value range: 10,240-512,000 MB (if message rewind is enabled). The value “0” indicates that message rewind is not enabled.
        :type RetentionSizeInMB: int
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
        self._Tags = None
        self._RetentionSizeInMB = None

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

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RetentionSizeInMB(self):
        return self._RetentionSizeInMB

    @RetentionSizeInMB.setter
    def RetentionSizeInMB(self, RetentionSizeInMB):
        self._RetentionSizeInMB = RetentionSizeInMB


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
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RetentionSizeInMB = params.get("RetentionSizeInMB")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCmqQueueResponse(AbstractModel):
    """CreateCmqQueue response structure.

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


class CreateCmqSubscribeRequest(AbstractModel):
    """CreateCmqSubscribe request structure.

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name, which must be unique in the same topic under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type TopicName: str
        :param _SubscriptionName: Subscription name, which must be unique in the same topic under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type SubscriptionName: str
        :param _Protocol: Subscription protocol. Currently, two protocols are supported: HTTP and queue. To use the HTTP protocol, you need to build your own web server to receive messages. With the queue protocol, messages are automatically pushed to a CMQ queue and you can pull them concurrently.
        :type Protocol: str
        :param _Endpoint: `Endpoint` for notification receipt, which is distinguished by `Protocol`. For `http`, `Endpoint` must begin with `http://` and `host` can be a domain name or IP. For `Queue`, enter `QueueName`. Note that currently the push service cannot push messages to a VPC; therefore, if a VPC domain name or address is entered for `Endpoint`, pushed messages will not be received. Currently, messages can be pushed only to the public network and classic network.
        :type Endpoint: str
        :param _NotifyStrategy: CMQ push server retry policy in case an error occurs while pushing a message to `Endpoint`. Valid values: 1. BACKOFF_RETRY: backoff retry, which is to retry at a fixed interval, discard the message after a certain number of retries, and continue to push the next message; 2. EXPONENTIAL_DECAY_RETRY: exponential decay retry, which is to retry at an exponentially increasing interval, such as 1s, 2s, 4s, 8s, and so on. As a message can be retained in a topic for one day, failed messages will be discarded at most after one day of retry. Default value: EXPONENTIAL_DECAY_RETRY.
        :type NotifyStrategy: str
        :param _FilterTag: Message body tag (used for message filtering). The number of tags cannot exceed 5, and each tag can contain up to 16 characters. It is used in conjunction with the `MsgTag` parameter of `(Batch)PublishMessage`. Rules: 1. If `FilterTag` is not configured, no matter whether `MsgTag` is configured, the subscription will receive all messages published to the topic; 2. If the array of `FilterTag` values has a value, only when at least one of the values in the array also exists in the array of `MsgTag` values (i.e., `FilterTag` and `MsgTag` have an intersection) can the subscription receive messages published to the topic; 3. If the array of `FilterTag` values has a value, but `MsgTag` is not configured, then no message published to the topic will be received, which can be considered as a special case of rule 2 as `FilterTag` and `MsgTag` do not intersect in this case. The overall design idea of rules is based on the intention of the subscriber.
        :type FilterTag: list of str
        :param _BindingKey: The number of `BindingKey` cannot exceed 5, and the length of each `BindingKey` cannot exceed 64 bytes. This field indicates the filtering policy for subscribing to and receiving messages. Each `BindingKey` includes up to 15 dots (namely up to 16 segments).
        :type BindingKey: list of str
        :param _NotifyContentFormat: Push content format. Valid values: 1. JSON; 2. SIMPLIFIED, i.e., the raw format. If `Protocol` is `queue`, this value must be `SIMPLIFIED`. If `Protocol` is `http`, both options are acceptable, and the default value is `JSON`.
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
        


class CreateCmqSubscribeResponse(AbstractModel):
    """CreateCmqSubscribe response structure.

    """

    def __init__(self):
        r"""
        :param _SubscriptionId: Subscription ID
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


class CreateCmqTopicRequest(AbstractModel):
    """CreateCmqTopic request structure.

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name, which must be unique in the same topic under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type TopicName: str
        :param _MaxMsgSize: Maximum message length. Value range: 1024–65536 bytes (i.e., 1–64 KB). Default value: 65536.
        :type MaxMsgSize: int
        :param _FilterType: Used to specify the message match policy for the topic. 1: tag match policy (default value); 2: routing match policy.
        :type FilterType: int
        :param _MsgRetentionSeconds: Message retention period. Value range: 60–86400 seconds (i.e., 1 minute–1 day). Default value: 86400.
        :type MsgRetentionSeconds: int
        :param _Trace: Whether to enable message trace. true: yes; false: no. If this field is left empty, the feature will not be enabled.
        :type Trace: bool
        :param _Tags: Tag array.
        :type Tags: list of Tag
        """
        self._TopicName = None
        self._MaxMsgSize = None
        self._FilterType = None
        self._MsgRetentionSeconds = None
        self._Trace = None
        self._Tags = None

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

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._MaxMsgSize = params.get("MaxMsgSize")
        self._FilterType = params.get("FilterType")
        self._MsgRetentionSeconds = params.get("MsgRetentionSeconds")
        self._Trace = params.get("Trace")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCmqTopicResponse(AbstractModel):
    """CreateCmqTopic response structure.

    """

    def __init__(self):
        r"""
        :param _TopicId: Topic ID
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


class CreateEnvironmentRequest(AbstractModel):
    """CreateEnvironment request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment (namespace) name, which can contain up to 16 letters, digits, hyphens, and underscores.
        :type EnvironmentId: str
        :param _MsgTTL: Retention period for unconsumed messages in seconds. Value range: 60s to 1,296,000s (or 15 days).
        :type MsgTTL: int
        :param _Remark: Remarks (up to 128 characters).
        :type Remark: str
        :param _ClusterId: Pulsar cluster ID
        :type ClusterId: str
        :param _RetentionPolicy: Message retention policy
        :type RetentionPolicy: :class:`tencentcloud.tdmq.v20200217.models.RetentionPolicy`
        """
        self._EnvironmentId = None
        self._MsgTTL = None
        self._Remark = None
        self._ClusterId = None
        self._RetentionPolicy = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def MsgTTL(self):
        return self._MsgTTL

    @MsgTTL.setter
    def MsgTTL(self, MsgTTL):
        self._MsgTTL = MsgTTL

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RetentionPolicy(self):
        return self._RetentionPolicy

    @RetentionPolicy.setter
    def RetentionPolicy(self, RetentionPolicy):
        self._RetentionPolicy = RetentionPolicy


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._MsgTTL = params.get("MsgTTL")
        self._Remark = params.get("Remark")
        self._ClusterId = params.get("ClusterId")
        if params.get("RetentionPolicy") is not None:
            self._RetentionPolicy = RetentionPolicy()
            self._RetentionPolicy._deserialize(params.get("RetentionPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEnvironmentResponse(AbstractModel):
    """CreateEnvironment response structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param _MsgTTL: TTL for unconsumed messages in seconds.
        :type MsgTTL: int
        :param _Remark: Remarks (up to 128 characters).
Note: this field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param _NamespaceId: Namespace ID
        :type NamespaceId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EnvironmentId = None
        self._MsgTTL = None
        self._Remark = None
        self._NamespaceId = None
        self._RequestId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def MsgTTL(self):
        return self._MsgTTL

    @MsgTTL.setter
    def MsgTTL(self, MsgTTL):
        self._MsgTTL = MsgTTL

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._MsgTTL = params.get("MsgTTL")
        self._Remark = params.get("Remark")
        self._NamespaceId = params.get("NamespaceId")
        self._RequestId = params.get("RequestId")


class CreateEnvironmentRoleRequest(AbstractModel):
    """CreateEnvironmentRole request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param _RoleName: Role name.
        :type RoleName: str
        :param _Permissions: Permissions, which is a non-empty string array of `produce` and `consume` at the most.
        :type Permissions: list of str
        :param _ClusterId: Cluster ID (required)
        :type ClusterId: str
        """
        self._EnvironmentId = None
        self._RoleName = None
        self._Permissions = None
        self._ClusterId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Permissions(self):
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._RoleName = params.get("RoleName")
        self._Permissions = params.get("Permissions")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEnvironmentRoleResponse(AbstractModel):
    """CreateEnvironmentRole response structure.

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


class CreateRabbitMQVipInstanceRequest(AbstractModel):
    """CreateRabbitMQVipInstance request structure.

    """

    def __init__(self):
        r"""
        :param _ZoneIds: AZ
        :type ZoneIds: list of int
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: VPC subnet ID
        :type SubnetId: str
        :param _ClusterName: Cluster name
        :type ClusterName: str
        :param _NodeSpec: Node specification (`rabbit-vip-basic-1`: Basic; `rabbit-vip-basic-2`: Standard; `rabbit-vip-basic-3`: Advanced I; `rabbit-vip-basic-4`: Advanced II). If this parameter is left empty, the default value is `rabbit-vip-basic-1`.
        :type NodeSpec: str
        :param _NodeNum: Number of nodes, which is at least three for multi-AZ deployment. If this parameter is left empty, the value will be set to 1 for single-AZ deployment and 3 for multi-AZ deployment by default.
        :type NodeNum: int
        :param _StorageSize: Storage capacity of a single node, which is 200 GB by default.
        :type StorageSize: int
        :param _EnableCreateDefaultHaMirrorQueue: Whether to enable mirrored queue. Default value: `false`.
        :type EnableCreateDefaultHaMirrorQueue: bool
        :param _AutoRenewFlag: Whether to enable auto-renewal. Default value: `true`.
        :type AutoRenewFlag: bool
        :param _TimeSpan: Validity period, which is one month by default.
        :type TimeSpan: int
        """
        self._ZoneIds = None
        self._VpcId = None
        self._SubnetId = None
        self._ClusterName = None
        self._NodeSpec = None
        self._NodeNum = None
        self._StorageSize = None
        self._EnableCreateDefaultHaMirrorQueue = None
        self._AutoRenewFlag = None
        self._TimeSpan = None

    @property
    def ZoneIds(self):
        return self._ZoneIds

    @ZoneIds.setter
    def ZoneIds(self, ZoneIds):
        self._ZoneIds = ZoneIds

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def NodeSpec(self):
        return self._NodeSpec

    @NodeSpec.setter
    def NodeSpec(self, NodeSpec):
        self._NodeSpec = NodeSpec

    @property
    def NodeNum(self):
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def StorageSize(self):
        return self._StorageSize

    @StorageSize.setter
    def StorageSize(self, StorageSize):
        self._StorageSize = StorageSize

    @property
    def EnableCreateDefaultHaMirrorQueue(self):
        return self._EnableCreateDefaultHaMirrorQueue

    @EnableCreateDefaultHaMirrorQueue.setter
    def EnableCreateDefaultHaMirrorQueue(self, EnableCreateDefaultHaMirrorQueue):
        self._EnableCreateDefaultHaMirrorQueue = EnableCreateDefaultHaMirrorQueue

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan


    def _deserialize(self, params):
        self._ZoneIds = params.get("ZoneIds")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ClusterName = params.get("ClusterName")
        self._NodeSpec = params.get("NodeSpec")
        self._NodeNum = params.get("NodeNum")
        self._StorageSize = params.get("StorageSize")
        self._EnableCreateDefaultHaMirrorQueue = params.get("EnableCreateDefaultHaMirrorQueue")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._TimeSpan = params.get("TimeSpan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRabbitMQVipInstanceResponse(AbstractModel):
    """CreateRabbitMQVipInstance response structure.

    """

    def __init__(self):
        r"""
        :param _TranId: Order ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type TranId: str
        :param _InstanceId: Instance ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TranId = None
        self._InstanceId = None
        self._RequestId = None

    @property
    def TranId(self):
        return self._TranId

    @TranId.setter
    def TranId(self, TranId):
        self._TranId = TranId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TranId = params.get("TranId")
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class CreateRocketMQClusterRequest(AbstractModel):
    """CreateRocketMQCluster request structure.

    """

    def __init__(self):
        r"""
        :param _Name: Cluster name, which can contain 3–64 letters, digits, hyphens, and underscores
        :type Name: str
        :param _Remark: Cluster description (up to 128 characters)
        :type Remark: str
        """
        self._Name = None
        self._Remark = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRocketMQClusterResponse(AbstractModel):
    """CreateRocketMQCluster response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterId = None
        self._RequestId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._RequestId = params.get("RequestId")


class CreateRocketMQGroupRequest(AbstractModel):
    """CreateRocketMQGroup request structure.

    """

    def __init__(self):
        r"""
        :param _GroupId: Group name (8–64 characters)
        :type GroupId: str
        :param _Namespaces: Namespace. Currently, only one namespace is supported
        :type Namespaces: list of str
        :param _ReadEnable: Whether to enable consumption
        :type ReadEnable: bool
        :param _BroadcastEnable: Whether to enable broadcast consumption
        :type BroadcastEnable: bool
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Remark: Remarks (up to 128 characters)
        :type Remark: str
        :param _GroupType: Group type (`TCP`, `HTTP`)
        :type GroupType: str
        :param _RetryMaxTimes: The maximum number of retries for a group
        :type RetryMaxTimes: int
        """
        self._GroupId = None
        self._Namespaces = None
        self._ReadEnable = None
        self._BroadcastEnable = None
        self._ClusterId = None
        self._Remark = None
        self._GroupType = None
        self._RetryMaxTimes = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Namespaces(self):
        return self._Namespaces

    @Namespaces.setter
    def Namespaces(self, Namespaces):
        self._Namespaces = Namespaces

    @property
    def ReadEnable(self):
        return self._ReadEnable

    @ReadEnable.setter
    def ReadEnable(self, ReadEnable):
        self._ReadEnable = ReadEnable

    @property
    def BroadcastEnable(self):
        return self._BroadcastEnable

    @BroadcastEnable.setter
    def BroadcastEnable(self, BroadcastEnable):
        self._BroadcastEnable = BroadcastEnable

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def GroupType(self):
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def RetryMaxTimes(self):
        return self._RetryMaxTimes

    @RetryMaxTimes.setter
    def RetryMaxTimes(self, RetryMaxTimes):
        self._RetryMaxTimes = RetryMaxTimes


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Namespaces = params.get("Namespaces")
        self._ReadEnable = params.get("ReadEnable")
        self._BroadcastEnable = params.get("BroadcastEnable")
        self._ClusterId = params.get("ClusterId")
        self._Remark = params.get("Remark")
        self._GroupType = params.get("GroupType")
        self._RetryMaxTimes = params.get("RetryMaxTimes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRocketMQGroupResponse(AbstractModel):
    """CreateRocketMQGroup response structure.

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


class CreateRocketMQNamespaceRequest(AbstractModel):
    """CreateRocketMQNamespace request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _NamespaceId: Namespace name, which can contain 3–64 letters, digits, hyphens, and underscores
        :type NamespaceId: str
        :param _Ttl: Retention time of unconsumed messages in milliseconds. Value range: 60 seconds–15 days
        :type Ttl: int
        :param _RetentionTime: Retention time of persisted messages in milliseconds
        :type RetentionTime: int
        :param _Remark: Remarks (up to 128 characters)
        :type Remark: str
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._Ttl = None
        self._RetentionTime = None
        self._Remark = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def Ttl(self):
        return self._Ttl

    @Ttl.setter
    def Ttl(self, Ttl):
        self._Ttl = Ttl

    @property
    def RetentionTime(self):
        return self._RetentionTime

    @RetentionTime.setter
    def RetentionTime(self, RetentionTime):
        self._RetentionTime = RetentionTime

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._Ttl = params.get("Ttl")
        self._RetentionTime = params.get("RetentionTime")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRocketMQNamespaceResponse(AbstractModel):
    """CreateRocketMQNamespace response structure.

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


class CreateRocketMQTopicRequest(AbstractModel):
    """CreateRocketMQTopic request structure.

    """

    def __init__(self):
        r"""
        :param _Topic: Topic name, which can contain 3–64 letters, digits, hyphens, and underscores
        :type Topic: str
        :param _Namespaces: Topic namespace. Currently, you can create topics only in one single namespace.
        :type Namespaces: list of str
        :param _Type: Topic type. Valid values: `Normal`, `PartitionedOrder`, `Transaction`, `DelayScheduled`.
        :type Type: str
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _Remark: Topic remarks (up to 128 characters)
        :type Remark: str
        :param _PartitionNum: Number of partitions, which doesn't take effect for globally sequential messages
        :type PartitionNum: int
        """
        self._Topic = None
        self._Namespaces = None
        self._Type = None
        self._ClusterId = None
        self._Remark = None
        self._PartitionNum = None

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Namespaces(self):
        return self._Namespaces

    @Namespaces.setter
    def Namespaces(self, Namespaces):
        self._Namespaces = Namespaces

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PartitionNum(self):
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum


    def _deserialize(self, params):
        self._Topic = params.get("Topic")
        self._Namespaces = params.get("Namespaces")
        self._Type = params.get("Type")
        self._ClusterId = params.get("ClusterId")
        self._Remark = params.get("Remark")
        self._PartitionNum = params.get("PartitionNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRocketMQTopicResponse(AbstractModel):
    """CreateRocketMQTopic response structure.

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


class CreateRoleRequest(AbstractModel):
    """CreateRole request structure.

    """

    def __init__(self):
        r"""
        :param _RoleName: Role name, which can contain up to 32 letters, digits, hyphens, and underscores.
        :type RoleName: str
        :param _Remark: Remarks (up to 128 characters).
        :type Remark: str
        :param _ClusterId: Cluster ID (required)
        :type ClusterId: str
        """
        self._RoleName = None
        self._Remark = None
        self._ClusterId = None

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._Remark = params.get("Remark")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoleResponse(AbstractModel):
    """CreateRole response structure.

    """

    def __init__(self):
        r"""
        :param _RoleName: Role name
        :type RoleName: str
        :param _Token: Role token
        :type Token: str
        :param _Remark: Remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RoleName = None
        self._Token = None
        self._Remark = None
        self._RequestId = None

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._Token = params.get("Token")
        self._Remark = params.get("Remark")
        self._RequestId = params.get("RequestId")


class CreateSubscriptionRequest(AbstractModel):
    """CreateSubscription request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param _TopicName: Topic name.
        :type TopicName: str
        :param _SubscriptionName: Subscriber name, which can contain up to 128 characters.
        :type SubscriptionName: str
        :param _IsIdempotent: Whether the creation is idempotent; if not, you cannot create subscriptions with the same name.
        :type IsIdempotent: bool
        :param _Remark: Remarks (up to 128 characters).
        :type Remark: str
        :param _ClusterId: Pulsar cluster ID
        :type ClusterId: str
        :param _AutoCreatePolicyTopic: Whether to automatically create a dead letter topic and a retry letter topic. true: yes (default value); false: no.
        :type AutoCreatePolicyTopic: bool
        :param _PostFixPattern: Naming convention for dead letter and retry letter topics. `LEGACY` indicates to use the legacy naming convention, and `COMMUNITY` indicates to use the naming convention in the Pulsar community.
        :type PostFixPattern: str
        """
        self._EnvironmentId = None
        self._TopicName = None
        self._SubscriptionName = None
        self._IsIdempotent = None
        self._Remark = None
        self._ClusterId = None
        self._AutoCreatePolicyTopic = None
        self._PostFixPattern = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

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
    def IsIdempotent(self):
        return self._IsIdempotent

    @IsIdempotent.setter
    def IsIdempotent(self, IsIdempotent):
        self._IsIdempotent = IsIdempotent

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def AutoCreatePolicyTopic(self):
        return self._AutoCreatePolicyTopic

    @AutoCreatePolicyTopic.setter
    def AutoCreatePolicyTopic(self, AutoCreatePolicyTopic):
        self._AutoCreatePolicyTopic = AutoCreatePolicyTopic

    @property
    def PostFixPattern(self):
        return self._PostFixPattern

    @PostFixPattern.setter
    def PostFixPattern(self, PostFixPattern):
        self._PostFixPattern = PostFixPattern


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._SubscriptionName = params.get("SubscriptionName")
        self._IsIdempotent = params.get("IsIdempotent")
        self._Remark = params.get("Remark")
        self._ClusterId = params.get("ClusterId")
        self._AutoCreatePolicyTopic = params.get("AutoCreatePolicyTopic")
        self._PostFixPattern = params.get("PostFixPattern")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubscriptionResponse(AbstractModel):
    """CreateSubscription response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Creation result.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param _TopicName: Topic name, which can contain up to 64 letters, digits, hyphens, and underscores.
        :type TopicName: str
        :param _Partitions: The value “1” indicates a non-partitioned topic (a topic with no partitions) will be created. A value between 1 (exclusive) and 128 (inclusive) indicates the partition count of a partitioned topic.
        :type Partitions: int
        :param _Remark: Remarks (up to 128 characters).
        :type Remark: str
        :param _TopicType: This input parameter will be disused soon. You can use `PulsarTopicType` instead.
0: General message;
1: Globally sequential message;
2: Partitionally sequential message;
3: Retry letter topic;
4: Dead letter topic.
        :type TopicType: int
        :param _ClusterId: Pulsar cluster ID
        :type ClusterId: str
        :param _PulsarTopicType: Pulsar topic type.
`0`: Non-persistent and non-partitioned
`1`: Non-persistent and partitioned
`2`: Persistent and non-partitioned
`3`: Persistent and partitioned
        :type PulsarTopicType: int
        """
        self._EnvironmentId = None
        self._TopicName = None
        self._Partitions = None
        self._Remark = None
        self._TopicType = None
        self._ClusterId = None
        self._PulsarTopicType = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TopicType(self):
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def PulsarTopicType(self):
        return self._PulsarTopicType

    @PulsarTopicType.setter
    def PulsarTopicType(self, PulsarTopicType):
        self._PulsarTopicType = PulsarTopicType


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._Partitions = params.get("Partitions")
        self._Remark = params.get("Remark")
        self._TopicType = params.get("TopicType")
        self._ClusterId = params.get("ClusterId")
        self._PulsarTopicType = params.get("PulsarTopicType")
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
        :param _EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param _TopicName: Topic name.
        :type TopicName: str
        :param _Partitions: Valid value: 0 or 1. Non-partitioned topic: No partitions. A value greater than 1: The partition count of a partitioned topic. `0` is returned for existing non-partitioned topics, and `1` is returned for incremental non-partitioned topics.
        :type Partitions: int
        :param _Remark: Remarks (up to 128 characters).
Note: this field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param _TopicType: 0: General message;
1: Globally sequential message;
2: Partitionally sequential message;
3: Retry letter topic;
4: Dead letter topic.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TopicType: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EnvironmentId = None
        self._TopicName = None
        self._Partitions = None
        self._Remark = None
        self._TopicType = None
        self._RequestId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TopicType(self):
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._Partitions = params.get("Partitions")
        self._Remark = params.get("Remark")
        self._TopicType = params.get("TopicType")
        self._RequestId = params.get("RequestId")


class DeleteClusterRequest(AbstractModel):
    """DeleteCluster request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster to be deleted.
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterResponse(AbstractModel):
    """DeleteCluster response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterId = None
        self._RequestId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._RequestId = params.get("RequestId")


class DeleteCmqQueueRequest(AbstractModel):
    """DeleteCmqQueue request structure.

    """

    def __init__(self):
        r"""
        :param _QueueName: Queue name, which must be unique under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
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
        


class DeleteCmqQueueResponse(AbstractModel):
    """DeleteCmqQueue response structure.

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


class DeleteCmqSubscribeRequest(AbstractModel):
    """DeleteCmqSubscribe request structure.

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name, which must be unique under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type TopicName: str
        :param _SubscriptionName: Subscription name, which must be unique in the same topic under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
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
        


class DeleteCmqSubscribeResponse(AbstractModel):
    """DeleteCmqSubscribe response structure.

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


class DeleteCmqTopicRequest(AbstractModel):
    """DeleteCmqTopic request structure.

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name, which must be unique under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
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
        


class DeleteCmqTopicResponse(AbstractModel):
    """DeleteCmqTopic response structure.

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


class DeleteEnvironmentRolesRequest(AbstractModel):
    """DeleteEnvironmentRoles request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param _RoleNames: Array of role names.
        :type RoleNames: list of str
        :param _ClusterId: Cluster ID (required)
        :type ClusterId: str
        """
        self._EnvironmentId = None
        self._RoleNames = None
        self._ClusterId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def RoleNames(self):
        return self._RoleNames

    @RoleNames.setter
    def RoleNames(self, RoleNames):
        self._RoleNames = RoleNames

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._RoleNames = params.get("RoleNames")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEnvironmentRolesResponse(AbstractModel):
    """DeleteEnvironmentRoles response structure.

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


class DeleteEnvironmentsRequest(AbstractModel):
    """DeleteEnvironments request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentIds: Array of environments (namespaces). Up to 20 environments can be deleted at a time.
        :type EnvironmentIds: list of str
        :param _ClusterId: Pulsar cluster ID
        :type ClusterId: str
        """
        self._EnvironmentIds = None
        self._ClusterId = None

    @property
    def EnvironmentIds(self):
        return self._EnvironmentIds

    @EnvironmentIds.setter
    def EnvironmentIds(self, EnvironmentIds):
        self._EnvironmentIds = EnvironmentIds

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._EnvironmentIds = params.get("EnvironmentIds")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEnvironmentsResponse(AbstractModel):
    """DeleteEnvironments response structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentIds: Array of environments (namespaces) successfully deleted.
        :type EnvironmentIds: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EnvironmentIds = None
        self._RequestId = None

    @property
    def EnvironmentIds(self):
        return self._EnvironmentIds

    @EnvironmentIds.setter
    def EnvironmentIds(self, EnvironmentIds):
        self._EnvironmentIds = EnvironmentIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EnvironmentIds = params.get("EnvironmentIds")
        self._RequestId = params.get("RequestId")


class DeleteRocketMQClusterRequest(AbstractModel):
    """DeleteRocketMQCluster request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the cluster to be deleted.
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRocketMQClusterResponse(AbstractModel):
    """DeleteRocketMQCluster response structure.

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


class DeleteRocketMQGroupRequest(AbstractModel):
    """DeleteRocketMQGroup request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _NamespaceId: Namespace name
        :type NamespaceId: str
        :param _GroupId: Consumer group name
        :type GroupId: str
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._GroupId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRocketMQGroupResponse(AbstractModel):
    """DeleteRocketMQGroup response structure.

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


class DeleteRocketMQNamespaceRequest(AbstractModel):
    """DeleteRocketMQNamespace request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _NamespaceId: Namespace name
        :type NamespaceId: str
        """
        self._ClusterId = None
        self._NamespaceId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRocketMQNamespaceResponse(AbstractModel):
    """DeleteRocketMQNamespace response structure.

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


class DeleteRocketMQTopicRequest(AbstractModel):
    """DeleteRocketMQTopic request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _NamespaceId: Namespace name
        :type NamespaceId: str
        :param _Topic: Topic name
        :type Topic: str
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._Topic = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._Topic = params.get("Topic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRocketMQTopicResponse(AbstractModel):
    """DeleteRocketMQTopic response structure.

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


class DeleteRolesRequest(AbstractModel):
    """DeleteRoles request structure.

    """

    def __init__(self):
        r"""
        :param _RoleNames: Array of role names.
        :type RoleNames: list of str
        :param _ClusterId: Cluster ID (required)
        :type ClusterId: str
        """
        self._RoleNames = None
        self._ClusterId = None

    @property
    def RoleNames(self):
        return self._RoleNames

    @RoleNames.setter
    def RoleNames(self, RoleNames):
        self._RoleNames = RoleNames

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._RoleNames = params.get("RoleNames")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRolesResponse(AbstractModel):
    """DeleteRoles response structure.

    """

    def __init__(self):
        r"""
        :param _RoleNames: Name array of roles successfully deleted.
        :type RoleNames: list of str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RoleNames = None
        self._RequestId = None

    @property
    def RoleNames(self):
        return self._RoleNames

    @RoleNames.setter
    def RoleNames(self, RoleNames):
        self._RoleNames = RoleNames

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoleNames = params.get("RoleNames")
        self._RequestId = params.get("RequestId")


class DeleteSubscriptionsRequest(AbstractModel):
    """DeleteSubscriptions request structure.

    """

    def __init__(self):
        r"""
        :param _SubscriptionTopicSets: Subscription set. Up to 20 subscriptions can be deleted at a time.
        :type SubscriptionTopicSets: list of SubscriptionTopic
        :param _ClusterId: Pulsar cluster ID.
        :type ClusterId: str
        :param _EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param _Force: Whether to forcibly delete a subscription. Default value: `false`.
        :type Force: bool
        """
        self._SubscriptionTopicSets = None
        self._ClusterId = None
        self._EnvironmentId = None
        self._Force = None

    @property
    def SubscriptionTopicSets(self):
        return self._SubscriptionTopicSets

    @SubscriptionTopicSets.setter
    def SubscriptionTopicSets(self, SubscriptionTopicSets):
        self._SubscriptionTopicSets = SubscriptionTopicSets

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        if params.get("SubscriptionTopicSets") is not None:
            self._SubscriptionTopicSets = []
            for item in params.get("SubscriptionTopicSets"):
                obj = SubscriptionTopic()
                obj._deserialize(item)
                self._SubscriptionTopicSets.append(obj)
        self._ClusterId = params.get("ClusterId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSubscriptionsResponse(AbstractModel):
    """DeleteSubscriptions response structure.

    """

    def __init__(self):
        r"""
        :param _SubscriptionTopicSets: Array of successfully deleted subscriptions.
        :type SubscriptionTopicSets: list of SubscriptionTopic
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SubscriptionTopicSets = None
        self._RequestId = None

    @property
    def SubscriptionTopicSets(self):
        return self._SubscriptionTopicSets

    @SubscriptionTopicSets.setter
    def SubscriptionTopicSets(self, SubscriptionTopicSets):
        self._SubscriptionTopicSets = SubscriptionTopicSets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SubscriptionTopicSets") is not None:
            self._SubscriptionTopicSets = []
            for item in params.get("SubscriptionTopicSets"):
                obj = SubscriptionTopic()
                obj._deserialize(item)
                self._SubscriptionTopicSets.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteTopicsRequest(AbstractModel):
    """DeleteTopics request structure.

    """

    def __init__(self):
        r"""
        :param _TopicSets: Topic set. Up to 20 topics can be deleted at a time.
        :type TopicSets: list of TopicRecord
        :param _ClusterId: Pulsar cluster ID.
        :type ClusterId: str
        :param _EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param _Force: Whether to forcibly delete a topic. Default value: `false`.
        :type Force: bool
        """
        self._TopicSets = None
        self._ClusterId = None
        self._EnvironmentId = None
        self._Force = None

    @property
    def TopicSets(self):
        return self._TopicSets

    @TopicSets.setter
    def TopicSets(self, TopicSets):
        self._TopicSets = TopicSets

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        if params.get("TopicSets") is not None:
            self._TopicSets = []
            for item in params.get("TopicSets"):
                obj = TopicRecord()
                obj._deserialize(item)
                self._TopicSets.append(obj)
        self._ClusterId = params.get("ClusterId")
        self._EnvironmentId = params.get("EnvironmentId")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicsResponse(AbstractModel):
    """DeleteTopics response structure.

    """

    def __init__(self):
        r"""
        :param _TopicSets: Array of deleted topics.
        :type TopicSets: list of TopicRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TopicSets = None
        self._RequestId = None

    @property
    def TopicSets(self):
        return self._TopicSets

    @TopicSets.setter
    def TopicSets(self, TopicSets):
        self._TopicSets = TopicSets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TopicSets") is not None:
            self._TopicSets = []
            for item in params.get("TopicSets"):
                obj = TopicRecord()
                obj._deserialize(item)
                self._TopicSets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBindClustersRequest(AbstractModel):
    """DescribeBindClusters request structure.

    """


class DescribeBindClustersResponse(AbstractModel):
    """DescribeBindClusters response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of dedicated clusters
        :type TotalCount: int
        :param _ClusterSet: List of dedicated clusters
        :type ClusterSet: list of BindCluster
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ClusterSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ClusterSet(self):
        return self._ClusterSet

    @ClusterSet.setter
    def ClusterSet(self, ClusterSet):
        self._ClusterSet = ClusterSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ClusterSet") is not None:
            self._ClusterSet = []
            for item in params.get("ClusterSet"):
                obj = BindCluster()
                obj._deserialize(item)
                self._ClusterSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBindVpcsRequest(AbstractModel):
    """DescribeBindVpcs request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset. If this parameter is left empty, 0 will be used by default.
        :type Offset: int
        :param _Limit: Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 20.
        :type Limit: int
        :param _ClusterId: Pulsar cluster ID
        :type ClusterId: str
        """
        self._Offset = None
        self._Limit = None
        self._ClusterId = None

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
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBindVpcsResponse(AbstractModel):
    """DescribeBindVpcs response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of records.
        :type TotalCount: int
        :param _VpcSets: Set of VPCs.
        :type VpcSets: list of VpcBindRecord
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._VpcSets = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VpcSets(self):
        return self._VpcSets

    @VpcSets.setter
    def VpcSets(self, VpcSets):
        self._VpcSets = VpcSets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("VpcSets") is not None:
            self._VpcSets = []
            for item in params.get("VpcSets"):
                obj = VpcBindRecord()
                obj._deserialize(item)
                self._VpcSets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterDetailRequest(AbstractModel):
    """DescribeClusterDetail request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterDetailResponse(AbstractModel):
    """DescribeClusterDetail response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterSet: Cluster details
        :type ClusterSet: :class:`tencentcloud.tdmq.v20200217.models.Cluster`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterSet = None
        self._RequestId = None

    @property
    def ClusterSet(self):
        return self._ClusterSet

    @ClusterSet.setter
    def ClusterSet(self, ClusterSet):
        self._ClusterSet = ClusterSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ClusterSet") is not None:
            self._ClusterSet = Cluster()
            self._ClusterSet._deserialize(params.get("ClusterSet"))
        self._RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Start offset, which defaults to 0 if left empty.
        :type Offset: int
        :param _Limit: The number of results to be returned, which defaults to 10 if left empty. The maximum value is 20.
        :type Limit: int
        :param _ClusterIdList: Filter by cluster ID.
        :type ClusterIdList: list of str
        :param _IsTagFilter: Whether to filter by tag.
        :type IsTagFilter: bool
        :param _Filters: Filter. Currently, you can filter by tag.
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._ClusterIdList = None
        self._IsTagFilter = None
        self._Filters = None

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
    def ClusterIdList(self):
        return self._ClusterIdList

    @ClusterIdList.setter
    def ClusterIdList(self, ClusterIdList):
        self._ClusterIdList = ClusterIdList

    @property
    def IsTagFilter(self):
        return self._IsTagFilter

    @IsTagFilter.setter
    def IsTagFilter(self, IsTagFilter):
        self._IsTagFilter = IsTagFilter

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ClusterIdList = params.get("ClusterIdList")
        self._IsTagFilter = params.get("IsTagFilter")
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
        


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of clusters.
        :type TotalCount: int
        :param _ClusterSet: Cluster information list
        :type ClusterSet: list of Cluster
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._ClusterSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ClusterSet(self):
        return self._ClusterSet

    @ClusterSet.setter
    def ClusterSet(self, ClusterSet):
        self._ClusterSet = ClusterSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ClusterSet") is not None:
            self._ClusterSet = []
            for item in params.get("ClusterSet"):
                obj = Cluster()
                obj._deserialize(item)
                self._ClusterSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCmqDeadLetterSourceQueuesRequest(AbstractModel):
    """DescribeCmqDeadLetterSourceQueues request structure.

    """

    def __init__(self):
        r"""
        :param _DeadLetterQueueName: Dead letter queue name
        :type DeadLetterQueueName: str
        :param _Limit: Starting position of the list of topics to be returned on the current page in case of paginated return. If a value is entered, `limit` is required. If this parameter is left empty, 0 will be used by default.
        :type Limit: int
        :param _Offset: Number of topics to be returned per page in case of paginated return. If this parameter is not passed in, 20 will be used by default. Maximum value: 50.
        :type Offset: int
        :param _SourceQueueName: Filter by `SourceQueueName`
        :type SourceQueueName: str
        """
        self._DeadLetterQueueName = None
        self._Limit = None
        self._Offset = None
        self._SourceQueueName = None

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
    def SourceQueueName(self):
        return self._SourceQueueName

    @SourceQueueName.setter
    def SourceQueueName(self, SourceQueueName):
        self._SourceQueueName = SourceQueueName


    def _deserialize(self, params):
        self._DeadLetterQueueName = params.get("DeadLetterQueueName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._SourceQueueName = params.get("SourceQueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCmqDeadLetterSourceQueuesResponse(AbstractModel):
    """DescribeCmqDeadLetterSourceQueues response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of eligible queues
        :type TotalCount: int
        :param _QueueSet: Source queues of dead letter queue
        :type QueueSet: list of CmqDeadLetterSource
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
                obj = CmqDeadLetterSource()
                obj._deserialize(item)
                self._QueueSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCmqQueueDetailRequest(AbstractModel):
    """DescribeCmqQueueDetail request structure.

    """

    def __init__(self):
        r"""
        :param _QueueName: Exact match by `QueueName`
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
        


class DescribeCmqQueueDetailResponse(AbstractModel):
    """DescribeCmqQueueDetail response structure.

    """

    def __init__(self):
        r"""
        :param _QueueDescribe: List of queue details.
        :type QueueDescribe: :class:`tencentcloud.tdmq.v20200217.models.CmqQueue`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._QueueDescribe = None
        self._RequestId = None

    @property
    def QueueDescribe(self):
        return self._QueueDescribe

    @QueueDescribe.setter
    def QueueDescribe(self, QueueDescribe):
        self._QueueDescribe = QueueDescribe

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("QueueDescribe") is not None:
            self._QueueDescribe = CmqQueue()
            self._QueueDescribe._deserialize(params.get("QueueDescribe"))
        self._RequestId = params.get("RequestId")


class DescribeCmqQueuesRequest(AbstractModel):
    """DescribeCmqQueues request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Starting position of a queue list to be returned on the current page in case of paginated return. If a value is entered, `limit` must be specified. If this parameter is left empty, 0 will be used by default.
        :type Offset: int
        :param _Limit: The number of queues to be returned per page in case of paginated return. If this parameter is not passed in, 20 will be used by default. Maximum value: 50.
        :type Limit: int
        :param _QueueName: Filter by `QueueName`
        :type QueueName: str
        :param _QueueNameList: Filter by CMQ queue name.
        :type QueueNameList: list of str
        :param _IsTagFilter: For filtering by tag, this parameter must be set to `true`.
        :type IsTagFilter: bool
        :param _Filters: Filter. Currently, you can filter by tag. The tag name must be prefixed with “tag:”, such as “tag: owner”, “tag: environment”, or “tag: business”.
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._QueueName = None
        self._QueueNameList = None
        self._IsTagFilter = None
        self._Filters = None

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
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def QueueNameList(self):
        return self._QueueNameList

    @QueueNameList.setter
    def QueueNameList(self, QueueNameList):
        self._QueueNameList = QueueNameList

    @property
    def IsTagFilter(self):
        return self._IsTagFilter

    @IsTagFilter.setter
    def IsTagFilter(self, IsTagFilter):
        self._IsTagFilter = IsTagFilter

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._QueueName = params.get("QueueName")
        self._QueueNameList = params.get("QueueNameList")
        self._IsTagFilter = params.get("IsTagFilter")
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
        


class DescribeCmqQueuesResponse(AbstractModel):
    """DescribeCmqQueues response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of queues.
        :type TotalCount: int
        :param _QueueList: Queue list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type QueueList: list of CmqQueue
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._QueueList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def QueueList(self):
        return self._QueueList

    @QueueList.setter
    def QueueList(self, QueueList):
        self._QueueList = QueueList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("QueueList") is not None:
            self._QueueList = []
            for item in params.get("QueueList"):
                obj = CmqQueue()
                obj._deserialize(item)
                self._QueueList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCmqSubscriptionDetailRequest(AbstractModel):
    """DescribeCmqSubscriptionDetail request structure.

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name, which must be unique in the same topic under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type TopicName: str
        :param _Offset: Starting position of the list of topics to be returned on the current page in case of paginated return. If a value is entered, `limit` is required. If this parameter is left empty, 0 will be used by default
        :type Offset: int
        :param _Limit: Number of topics to be returned per page in case of paginated return. If this parameter is not passed in, 20 will be used by default. Maximum value: 50.
        :type Limit: int
        :param _SubscriptionName: Fuzzy search by `SubscriptionName`
        :type SubscriptionName: str
        """
        self._TopicName = None
        self._Offset = None
        self._Limit = None
        self._SubscriptionName = None

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
    def SubscriptionName(self):
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SubscriptionName = params.get("SubscriptionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCmqSubscriptionDetailResponse(AbstractModel):
    """DescribeCmqSubscriptionDetail response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number
        :type TotalCount: int
        :param _SubscriptionSet: Set of subscription attributes
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubscriptionSet: list of CmqSubscription
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
                obj = CmqSubscription()
                obj._deserialize(item)
                self._SubscriptionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCmqTopicDetailRequest(AbstractModel):
    """DescribeCmqTopicDetail request structure.

    """

    def __init__(self):
        r"""
        :param _TopicName: Exact match by `TopicName`.
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
        


class DescribeCmqTopicDetailResponse(AbstractModel):
    """DescribeCmqTopicDetail response structure.

    """

    def __init__(self):
        r"""
        :param _TopicDescribe: Topic details
        :type TopicDescribe: :class:`tencentcloud.tdmq.v20200217.models.CmqTopic`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TopicDescribe = None
        self._RequestId = None

    @property
    def TopicDescribe(self):
        return self._TopicDescribe

    @TopicDescribe.setter
    def TopicDescribe(self, TopicDescribe):
        self._TopicDescribe = TopicDescribe

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TopicDescribe") is not None:
            self._TopicDescribe = CmqTopic()
            self._TopicDescribe._deserialize(params.get("TopicDescribe"))
        self._RequestId = params.get("RequestId")


class DescribeCmqTopicsRequest(AbstractModel):
    """DescribeCmqTopics request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Starting position of a queue list to be returned on the current page in case of paginated return. If a value is entered, `limit` must be specified. If this parameter is left empty, 0 will be used by default.
        :type Offset: int
        :param _Limit: The number of queues to be returned per page in case of paginated return. If this parameter is not passed in, 20 will be used by default. Maximum value: 50.
        :type Limit: int
        :param _TopicName: Fuzzy search by `TopicName`
        :type TopicName: str
        :param _TopicNameList: Filter by CMQ topic name.
        :type TopicNameList: list of str
        :param _IsTagFilter: For filtering by tag, this parameter must be set to `true`.
        :type IsTagFilter: bool
        :param _Filters: Filter. Currently, you can filter by tag. The tag name must be prefixed with “tag:”, such as “tag: owner”, “tag: environment”, or “tag: business”.
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._TopicName = None
        self._TopicNameList = None
        self._IsTagFilter = None
        self._Filters = None

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
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def TopicNameList(self):
        return self._TopicNameList

    @TopicNameList.setter
    def TopicNameList(self, TopicNameList):
        self._TopicNameList = TopicNameList

    @property
    def IsTagFilter(self):
        return self._IsTagFilter

    @IsTagFilter.setter
    def IsTagFilter(self, IsTagFilter):
        self._IsTagFilter = IsTagFilter

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TopicName = params.get("TopicName")
        self._TopicNameList = params.get("TopicNameList")
        self._IsTagFilter = params.get("IsTagFilter")
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
        


class DescribeCmqTopicsResponse(AbstractModel):
    """DescribeCmqTopics response structure.

    """

    def __init__(self):
        r"""
        :param _TopicList: Topic list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TopicList: list of CmqTopic
        :param _TotalCount: The total number of topics.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TopicList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TopicList(self):
        return self._TopicList

    @TopicList.setter
    def TopicList(self, TopicList):
        self._TopicList = TopicList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TopicList") is not None:
            self._TopicList = []
            for item in params.get("TopicList"):
                obj = CmqTopic()
                obj._deserialize(item)
                self._TopicList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeEnvironmentAttributesRequest(AbstractModel):
    """DescribeEnvironmentAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param _ClusterId: Pulsar cluster ID
        :type ClusterId: str
        """
        self._EnvironmentId = None
        self._ClusterId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnvironmentAttributesResponse(AbstractModel):
    """DescribeEnvironmentAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _MsgTTL: TTL for unconsumed messages in seconds. Maximum value: 1296000 seconds (i.e., 15 days).
        :type MsgTTL: int
        :param _RateInByte: Consumption rate limit in bytes/second. 0: unlimited.
        :type RateInByte: int
        :param _RateInSize: Consumption rate limit in messages/second. 0: unlimited.
        :type RateInSize: int
        :param _RetentionHours: Retention policy for consumed messages in hours. 0: deleted immediately after consumption.
        :type RetentionHours: int
        :param _RetentionSize: Retention policy for consumed messages in GB. 0: deleted immediately after consumption.
        :type RetentionSize: int
        :param _EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param _Replicas: Number of replicas.
        :type Replicas: int
        :param _Remark: Remarks.
        :type Remark: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MsgTTL = None
        self._RateInByte = None
        self._RateInSize = None
        self._RetentionHours = None
        self._RetentionSize = None
        self._EnvironmentId = None
        self._Replicas = None
        self._Remark = None
        self._RequestId = None

    @property
    def MsgTTL(self):
        return self._MsgTTL

    @MsgTTL.setter
    def MsgTTL(self, MsgTTL):
        self._MsgTTL = MsgTTL

    @property
    def RateInByte(self):
        return self._RateInByte

    @RateInByte.setter
    def RateInByte(self, RateInByte):
        self._RateInByte = RateInByte

    @property
    def RateInSize(self):
        return self._RateInSize

    @RateInSize.setter
    def RateInSize(self, RateInSize):
        self._RateInSize = RateInSize

    @property
    def RetentionHours(self):
        return self._RetentionHours

    @RetentionHours.setter
    def RetentionHours(self, RetentionHours):
        self._RetentionHours = RetentionHours

    @property
    def RetentionSize(self):
        return self._RetentionSize

    @RetentionSize.setter
    def RetentionSize(self, RetentionSize):
        self._RetentionSize = RetentionSize

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Replicas(self):
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MsgTTL = params.get("MsgTTL")
        self._RateInByte = params.get("RateInByte")
        self._RateInSize = params.get("RateInSize")
        self._RetentionHours = params.get("RetentionHours")
        self._RetentionSize = params.get("RetentionSize")
        self._EnvironmentId = params.get("EnvironmentId")
        self._Replicas = params.get("Replicas")
        self._Remark = params.get("Remark")
        self._RequestId = params.get("RequestId")


class DescribeEnvironmentRolesRequest(AbstractModel):
    """DescribeEnvironmentRoles request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment/namespace name (required).
        :type EnvironmentId: str
        :param _Offset: Offset, which defaults to 0 if left empty.
        :type Offset: int
        :param _Limit: The number of results to be returned, which defaults to 10 if left empty. The maximum value is 20.
        :type Limit: int
        :param _ClusterId: Pulsar cluster ID (required).
        :type ClusterId: str
        :param _RoleName: Role name.
        :type RoleName: str
        :param _Filters: * RoleName
Filter by role name for exact query.
Type: String
Required: No
        :type Filters: list of Filter
        """
        self._EnvironmentId = None
        self._Offset = None
        self._Limit = None
        self._ClusterId = None
        self._RoleName = None
        self._Filters = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

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
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ClusterId = params.get("ClusterId")
        self._RoleName = params.get("RoleName")
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
        


class DescribeEnvironmentRolesResponse(AbstractModel):
    """DescribeEnvironmentRoles response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of records.
        :type TotalCount: int
        :param _EnvironmentRoleSets: Namespace role set.
        :type EnvironmentRoleSets: list of EnvironmentRole
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._EnvironmentRoleSets = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def EnvironmentRoleSets(self):
        return self._EnvironmentRoleSets

    @EnvironmentRoleSets.setter
    def EnvironmentRoleSets(self, EnvironmentRoleSets):
        self._EnvironmentRoleSets = EnvironmentRoleSets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("EnvironmentRoleSets") is not None:
            self._EnvironmentRoleSets = []
            for item in params.get("EnvironmentRoleSets"):
                obj = EnvironmentRole()
                obj._deserialize(item)
                self._EnvironmentRoleSets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeEnvironmentsRequest(AbstractModel):
    """DescribeEnvironments request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Fuzzy search by namespace name.
        :type EnvironmentId: str
        :param _Offset: Offset, which defaults to 0 if left empty.
        :type Offset: int
        :param _Limit: The number of results to be returned, which defaults to 10 if left empty. The maximum value is 20.
        :type Limit: int
        :param _ClusterId: Pulsar cluster ID
        :type ClusterId: str
        :param _Filters: * EnvironmentId
Filter by namespace for exact query.
Type: String
Required: No
        :type Filters: list of Filter
        """
        self._EnvironmentId = None
        self._Offset = None
        self._Limit = None
        self._ClusterId = None
        self._Filters = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

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
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ClusterId = params.get("ClusterId")
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
        


class DescribeEnvironmentsResponse(AbstractModel):
    """DescribeEnvironments response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of namespaces.
        :type TotalCount: int
        :param _EnvironmentSet: Array of namespace sets.
        :type EnvironmentSet: list of Environment
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._EnvironmentSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def EnvironmentSet(self):
        return self._EnvironmentSet

    @EnvironmentSet.setter
    def EnvironmentSet(self, EnvironmentSet):
        self._EnvironmentSet = EnvironmentSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("EnvironmentSet") is not None:
            self._EnvironmentSet = []
            for item in params.get("EnvironmentSet"):
                obj = Environment()
                obj._deserialize(item)
                self._EnvironmentSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePublisherSummaryRequest(AbstractModel):
    """DescribePublisherSummary request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID.
        :type ClusterId: str
        :param _Namespace: Namespace name.
        :type Namespace: str
        :param _Topic: Topic name.
        :type Topic: str
        """
        self._ClusterId = None
        self._Namespace = None
        self._Topic = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Namespace = params.get("Namespace")
        self._Topic = params.get("Topic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublisherSummaryResponse(AbstractModel):
    """DescribePublisherSummary response structure.

    """

    def __init__(self):
        r"""
        :param _MsgRateIn: Production rate (messages/sec).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MsgRateIn: float
        :param _MsgThroughputIn: Production rate (byte/sec).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MsgThroughputIn: float
        :param _PublisherCount: The number of producers.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type PublisherCount: int
        :param _StorageSize: Message storage size in bytes.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type StorageSize: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MsgRateIn = None
        self._MsgThroughputIn = None
        self._PublisherCount = None
        self._StorageSize = None
        self._RequestId = None

    @property
    def MsgRateIn(self):
        return self._MsgRateIn

    @MsgRateIn.setter
    def MsgRateIn(self, MsgRateIn):
        self._MsgRateIn = MsgRateIn

    @property
    def MsgThroughputIn(self):
        return self._MsgThroughputIn

    @MsgThroughputIn.setter
    def MsgThroughputIn(self, MsgThroughputIn):
        self._MsgThroughputIn = MsgThroughputIn

    @property
    def PublisherCount(self):
        return self._PublisherCount

    @PublisherCount.setter
    def PublisherCount(self, PublisherCount):
        self._PublisherCount = PublisherCount

    @property
    def StorageSize(self):
        return self._StorageSize

    @StorageSize.setter
    def StorageSize(self, StorageSize):
        self._StorageSize = StorageSize

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MsgRateIn = params.get("MsgRateIn")
        self._MsgThroughputIn = params.get("MsgThroughputIn")
        self._PublisherCount = params.get("PublisherCount")
        self._StorageSize = params.get("StorageSize")
        self._RequestId = params.get("RequestId")


class DescribePublishersRequest(AbstractModel):
    """DescribePublishers request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID.
        :type ClusterId: str
        :param _Namespace: Namespace name.
        :type Namespace: str
        :param _Topic: Topic name.
        :type Topic: str
        :param _Filters: Parameter filter. The `ProducerName` and `Address` fields are supported.
        :type Filters: list of Filter
        :param _Offset: Offset for query. Default value: `0`.
        :type Offset: int
        :param _Limit: The number of query results displayed per page. Default value: `20`.
        :type Limit: int
        :param _Sort: Sort by field.
        :type Sort: :class:`tencentcloud.tdmq.v20200217.models.Sort`
        """
        self._ClusterId = None
        self._Namespace = None
        self._Topic = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Sort = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Namespace = params.get("Namespace")
        self._Topic = params.get("Topic")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Sort") is not None:
            self._Sort = Sort()
            self._Sort._deserialize(params.get("Sort"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublishersResponse(AbstractModel):
    """DescribePublishers response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Total number of query results.
        :type TotalCount: int
        :param _Publishers: List of producer information.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Publishers: list of Publisher
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Publishers = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Publishers(self):
        return self._Publishers

    @Publishers.setter
    def Publishers(self, Publishers):
        self._Publishers = Publishers

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Publishers") is not None:
            self._Publishers = []
            for item in params.get("Publishers"):
                obj = Publisher()
                obj._deserialize(item)
                self._Publishers.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePulsarProInstanceDetailRequest(AbstractModel):
    """DescribePulsarProInstanceDetail request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePulsarProInstanceDetailResponse(AbstractModel):
    """DescribePulsarProInstanceDetail response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterInfo: Cluster information
        :type ClusterInfo: :class:`tencentcloud.tdmq.v20200217.models.PulsarProClusterInfo`
        :param _NetworkAccessPointInfos: Cluster network access point information
Note: This field may return null, indicating that no valid values can be obtained.
        :type NetworkAccessPointInfos: list of PulsarNetworkAccessPointInfo
        :param _ClusterSpecInfo: Cluster specification information
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterSpecInfo: :class:`tencentcloud.tdmq.v20200217.models.PulsarProClusterSpecInfo`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterInfo = None
        self._NetworkAccessPointInfos = None
        self._ClusterSpecInfo = None
        self._RequestId = None

    @property
    def ClusterInfo(self):
        return self._ClusterInfo

    @ClusterInfo.setter
    def ClusterInfo(self, ClusterInfo):
        self._ClusterInfo = ClusterInfo

    @property
    def NetworkAccessPointInfos(self):
        return self._NetworkAccessPointInfos

    @NetworkAccessPointInfos.setter
    def NetworkAccessPointInfos(self, NetworkAccessPointInfos):
        self._NetworkAccessPointInfos = NetworkAccessPointInfos

    @property
    def ClusterSpecInfo(self):
        return self._ClusterSpecInfo

    @ClusterSpecInfo.setter
    def ClusterSpecInfo(self, ClusterSpecInfo):
        self._ClusterSpecInfo = ClusterSpecInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ClusterInfo") is not None:
            self._ClusterInfo = PulsarProClusterInfo()
            self._ClusterInfo._deserialize(params.get("ClusterInfo"))
        if params.get("NetworkAccessPointInfos") is not None:
            self._NetworkAccessPointInfos = []
            for item in params.get("NetworkAccessPointInfos"):
                obj = PulsarNetworkAccessPointInfo()
                obj._deserialize(item)
                self._NetworkAccessPointInfos.append(obj)
        if params.get("ClusterSpecInfo") is not None:
            self._ClusterSpecInfo = PulsarProClusterSpecInfo()
            self._ClusterSpecInfo._deserialize(params.get("ClusterSpecInfo"))
        self._RequestId = params.get("RequestId")


class DescribePulsarProInstancesRequest(AbstractModel):
    """DescribePulsarProInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Query condition filter
        :type Filters: list of Filter
        :param _Limit: The maximum number of queried items, which defaults to `20`.
        :type Limit: int
        :param _Offset: Start offset for query
        :type Offset: int
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePulsarProInstancesResponse(AbstractModel):
    """DescribePulsarProInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The total number of unpaginated items
        :type TotalCount: int
        :param _Instances: Instance information list
        :type Instances: list of PulsarProInstance
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Instances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = PulsarProInstance()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQNodeListRequest(AbstractModel):
    """DescribeRabbitMQNodeList request structure.

    """

    def __init__(self):
        r"""
        :param _InstanceId: TDMQ for RabbitMQ cluster ID
        :type InstanceId: str
        :param _Offset: Offset
        :type Offset: int
        :param _Limit: The maximum entries per page
        :type Limit: int
        :param _NodeName: Node name for fuzzy search
        :type NodeName: str
        :param _Filters: Name and value of a filter.
Currently, only the `nodeStatus` filter is supported.
Valid values: `running`, `down`.
It is an array type and can contain multiple filters.

        :type Filters: list of Filter
        :param _SortElement: Sorting by a specified element.
Valid values: `cpuUsage`, `diskUsage`.
        :type SortElement: str
        :param _SortOrder: Sorting order.
Valid values: `ascend`, `descend`.
        :type SortOrder: str
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._NodeName = None
        self._Filters = None
        self._SortElement = None
        self._SortOrder = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
    def NodeName(self):
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SortElement(self):
        return self._SortElement

    @SortElement.setter
    def SortElement(self, SortElement):
        self._SortElement = SortElement

    @property
    def SortOrder(self):
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._NodeName = params.get("NodeName")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._SortElement = params.get("SortElement")
        self._SortOrder = params.get("SortOrder")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQNodeListResponse(AbstractModel):
    """DescribeRabbitMQNodeList response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The number of clusters
        :type TotalCount: int
        :param _NodeList: Cluster list
Note: This field may return null, indicating that no valid value can be obtained.
        :type NodeList: list of RabbitMQPrivateNode
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._NodeList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NodeList(self):
        return self._NodeList

    @NodeList.setter
    def NodeList(self, NodeList):
        self._NodeList = NodeList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("NodeList") is not None:
            self._NodeList = []
            for item in params.get("NodeList"):
                obj = RabbitMQPrivateNode()
                obj._deserialize(item)
                self._NodeList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRabbitMQVipInstancesRequest(AbstractModel):
    """DescribeRabbitMQVipInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Query condition filter
        :type Filters: list of Filter
        :param _Limit: The maximum number of queried items, which defaults to 20.
        :type Limit: int
        :param _Offset: Start offset for query
        :type Offset: int
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRabbitMQVipInstancesResponse(AbstractModel):
    """DescribeRabbitMQVipInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The total number of unpaginated items
        :type TotalCount: int
        :param _Instances: Instance information list
        :type Instances: list of RabbitMQVipInstance
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Instances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = RabbitMQVipInstance()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRocketMQClusterRequest(AbstractModel):
    """DescribeRocketMQCluster request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQClusterResponse(AbstractModel):
    """DescribeRocketMQCluster response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterInfo: Cluster information
        :type ClusterInfo: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterInfo`
        :param _ClusterConfig: Cluster configuration
        :type ClusterConfig: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterConfig`
        :param _ClusterStats: Recent cluster usage
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterStats: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterRecentStats`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterInfo = None
        self._ClusterConfig = None
        self._ClusterStats = None
        self._RequestId = None

    @property
    def ClusterInfo(self):
        return self._ClusterInfo

    @ClusterInfo.setter
    def ClusterInfo(self, ClusterInfo):
        self._ClusterInfo = ClusterInfo

    @property
    def ClusterConfig(self):
        return self._ClusterConfig

    @ClusterConfig.setter
    def ClusterConfig(self, ClusterConfig):
        self._ClusterConfig = ClusterConfig

    @property
    def ClusterStats(self):
        return self._ClusterStats

    @ClusterStats.setter
    def ClusterStats(self, ClusterStats):
        self._ClusterStats = ClusterStats

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ClusterInfo") is not None:
            self._ClusterInfo = RocketMQClusterInfo()
            self._ClusterInfo._deserialize(params.get("ClusterInfo"))
        if params.get("ClusterConfig") is not None:
            self._ClusterConfig = RocketMQClusterConfig()
            self._ClusterConfig._deserialize(params.get("ClusterConfig"))
        if params.get("ClusterStats") is not None:
            self._ClusterStats = RocketMQClusterRecentStats()
            self._ClusterStats._deserialize(params.get("ClusterStats"))
        self._RequestId = params.get("RequestId")


class DescribeRocketMQClustersRequest(AbstractModel):
    """DescribeRocketMQClusters request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset.
        :type Offset: int
        :param _Limit: The max number of returned results.
        :type Limit: int
        :param _IdKeyword: Search by cluster ID.
        :type IdKeyword: str
        :param _NameKeyword: Search by cluster name.
        :type NameKeyword: str
        :param _ClusterIdList: Filter by cluster ID.
        :type ClusterIdList: list of str
        :param _IsTagFilter: For filtering by tag, this parameter must be set to `true`.
        :type IsTagFilter: bool
        :param _Filters: Filter. Currently, you can filter only by tag.
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._IdKeyword = None
        self._NameKeyword = None
        self._ClusterIdList = None
        self._IsTagFilter = None
        self._Filters = None

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
    def IdKeyword(self):
        return self._IdKeyword

    @IdKeyword.setter
    def IdKeyword(self, IdKeyword):
        self._IdKeyword = IdKeyword

    @property
    def NameKeyword(self):
        return self._NameKeyword

    @NameKeyword.setter
    def NameKeyword(self, NameKeyword):
        self._NameKeyword = NameKeyword

    @property
    def ClusterIdList(self):
        return self._ClusterIdList

    @ClusterIdList.setter
    def ClusterIdList(self, ClusterIdList):
        self._ClusterIdList = ClusterIdList

    @property
    def IsTagFilter(self):
        return self._IsTagFilter

    @IsTagFilter.setter
    def IsTagFilter(self, IsTagFilter):
        self._IsTagFilter = IsTagFilter

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._IdKeyword = params.get("IdKeyword")
        self._NameKeyword = params.get("NameKeyword")
        self._ClusterIdList = params.get("ClusterIdList")
        self._IsTagFilter = params.get("IsTagFilter")
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
        


class DescribeRocketMQClustersResponse(AbstractModel):
    """DescribeRocketMQClusters response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterList: Cluster information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ClusterList: list of RocketMQClusterDetail
        :param _TotalCount: The total number of returned results.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ClusterList(self):
        return self._ClusterList

    @ClusterList.setter
    def ClusterList(self, ClusterList):
        self._ClusterList = ClusterList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ClusterList") is not None:
            self._ClusterList = []
            for item in params.get("ClusterList"):
                obj = RocketMQClusterDetail()
                obj._deserialize(item)
                self._ClusterList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRocketMQGroupsRequest(AbstractModel):
    """DescribeRocketMQGroups request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID.
        :type ClusterId: str
        :param _NamespaceId: Namespace.
        :type NamespaceId: str
        :param _Offset: Offset.
        :type Offset: int
        :param _Limit: The max number of returned results.
        :type Limit: int
        :param _FilterTopic: Topic name, which can be used to query all subscription groups under the topic
        :type FilterTopic: str
        :param _FilterGroup: Consumer group query by consumer group name. Fuzzy query is supported
        :type FilterGroup: str
        :param _SortedBy: Sort by specified field. Valid values: `tps`, `accumulative`.
        :type SortedBy: str
        :param _SortOrder: Sort in ascending or descending order. Valid values: `asc`, `desc`.
        :type SortOrder: str
        :param _FilterOneGroup: Subscription group name. After it is specified, the information of only this subscription group will be returned.
        :type FilterOneGroup: str
        :param _Types: Group type
        :type Types: list of str
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._Offset = None
        self._Limit = None
        self._FilterTopic = None
        self._FilterGroup = None
        self._SortedBy = None
        self._SortOrder = None
        self._FilterOneGroup = None
        self._Types = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

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
    def FilterTopic(self):
        return self._FilterTopic

    @FilterTopic.setter
    def FilterTopic(self, FilterTopic):
        self._FilterTopic = FilterTopic

    @property
    def FilterGroup(self):
        return self._FilterGroup

    @FilterGroup.setter
    def FilterGroup(self, FilterGroup):
        self._FilterGroup = FilterGroup

    @property
    def SortedBy(self):
        return self._SortedBy

    @SortedBy.setter
    def SortedBy(self, SortedBy):
        self._SortedBy = SortedBy

    @property
    def SortOrder(self):
        return self._SortOrder

    @SortOrder.setter
    def SortOrder(self, SortOrder):
        self._SortOrder = SortOrder

    @property
    def FilterOneGroup(self):
        return self._FilterOneGroup

    @FilterOneGroup.setter
    def FilterOneGroup(self, FilterOneGroup):
        self._FilterOneGroup = FilterOneGroup

    @property
    def Types(self):
        return self._Types

    @Types.setter
    def Types(self, Types):
        self._Types = Types


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterTopic = params.get("FilterTopic")
        self._FilterGroup = params.get("FilterGroup")
        self._SortedBy = params.get("SortedBy")
        self._SortOrder = params.get("SortOrder")
        self._FilterOneGroup = params.get("FilterOneGroup")
        self._Types = params.get("Types")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQGroupsResponse(AbstractModel):
    """DescribeRocketMQGroups response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The total number of subscription groups.
        :type TotalCount: int
        :param _Groups: List of subscription groups
        :type Groups: list of RocketMQGroup
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Groups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Groups(self):
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = RocketMQGroup()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRocketMQNamespacesRequest(AbstractModel):
    """DescribeRocketMQNamespaces request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID.
        :type ClusterId: str
        :param _Offset: Offset.
        :type Offset: int
        :param _Limit: The max number of returned results.
        :type Limit: int
        :param _NameKeyword: Search by name.
        :type NameKeyword: str
        """
        self._ClusterId = None
        self._Offset = None
        self._Limit = None
        self._NameKeyword = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

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
    def NameKeyword(self):
        return self._NameKeyword

    @NameKeyword.setter
    def NameKeyword(self, NameKeyword):
        self._NameKeyword = NameKeyword


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._NameKeyword = params.get("NameKeyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQNamespacesResponse(AbstractModel):
    """DescribeRocketMQNamespaces response structure.

    """

    def __init__(self):
        r"""
        :param _Namespaces: List of namespaces
        :type Namespaces: list of RocketMQNamespace
        :param _TotalCount: The total number of returned results.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Namespaces = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Namespaces(self):
        return self._Namespaces

    @Namespaces.setter
    def Namespaces(self, Namespaces):
        self._Namespaces = Namespaces

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Namespaces") is not None:
            self._Namespaces = []
            for item in params.get("Namespaces"):
                obj = RocketMQNamespace()
                obj._deserialize(item)
                self._Namespaces.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRocketMQTopicsRequest(AbstractModel):
    """DescribeRocketMQTopics request structure.

    """

    def __init__(self):
        r"""
        :param _Offset: Offset for query.
        :type Offset: int
        :param _Limit: Query limit.
        :type Limit: int
        :param _ClusterId: Cluster ID.
        :type ClusterId: str
        :param _NamespaceId: Namespace.
        :type NamespaceId: str
        :param _FilterType: Filter by topic type. Valid values: `Normal`, `GlobalOrder`, `PartitionedOrder`, `Transaction`.
        :type FilterType: list of str
        :param _FilterName: Search by topic name. Fuzzy query is supported.
        :type FilterName: str
        """
        self._Offset = None
        self._Limit = None
        self._ClusterId = None
        self._NamespaceId = None
        self._FilterType = None
        self._FilterName = None

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
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def FilterType(self):
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def FilterName(self):
        return self._FilterName

    @FilterName.setter
    def FilterName(self, FilterName):
        self._FilterName = FilterName


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._FilterType = params.get("FilterType")
        self._FilterName = params.get("FilterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQTopicsResponse(AbstractModel):
    """DescribeRocketMQTopics response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The total number of query records.
        :type TotalCount: int
        :param _Topics: List of topic information
        :type Topics: list of RocketMQTopic
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Topics = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Topics(self):
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Topics") is not None:
            self._Topics = []
            for item in params.get("Topics"):
                obj = RocketMQTopic()
                obj._deserialize(item)
                self._Topics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRocketMQVipInstanceDetailRequest(AbstractModel):
    """DescribeRocketMQVipInstanceDetail request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQVipInstanceDetailResponse(AbstractModel):
    """DescribeRocketMQVipInstanceDetail response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterInfo: Cluster information
        :type ClusterInfo: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterInfo`
        :param _InstanceConfig: Cluster configuration
        :type InstanceConfig: :class:`tencentcloud.tdmq.v20200217.models.RocketMQInstanceConfig`
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterInfo = None
        self._InstanceConfig = None
        self._RequestId = None

    @property
    def ClusterInfo(self):
        return self._ClusterInfo

    @ClusterInfo.setter
    def ClusterInfo(self, ClusterInfo):
        self._ClusterInfo = ClusterInfo

    @property
    def InstanceConfig(self):
        return self._InstanceConfig

    @InstanceConfig.setter
    def InstanceConfig(self, InstanceConfig):
        self._InstanceConfig = InstanceConfig

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ClusterInfo") is not None:
            self._ClusterInfo = RocketMQClusterInfo()
            self._ClusterInfo._deserialize(params.get("ClusterInfo"))
        if params.get("InstanceConfig") is not None:
            self._InstanceConfig = RocketMQInstanceConfig()
            self._InstanceConfig._deserialize(params.get("InstanceConfig"))
        self._RequestId = params.get("RequestId")


class DescribeRocketMQVipInstancesRequest(AbstractModel):
    """DescribeRocketMQVipInstances request structure.

    """

    def __init__(self):
        r"""
        :param _Filters: Query condition filter
        :type Filters: list of Filter
        :param _Limit: The maximum number of queried items, which defaults to 20.
        :type Limit: int
        :param _Offset: Start offset for query
        :type Offset: int
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRocketMQVipInstancesResponse(AbstractModel):
    """DescribeRocketMQVipInstances response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: The total number of unpaginated items
        :type TotalCount: int
        :param _Instances: Instance information list
        :type Instances: list of RocketMQVipInstance
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._Instances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Instances(self):
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = RocketMQVipInstance()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRolesRequest(AbstractModel):
    """DescribeRoles request structure.

    """

    def __init__(self):
        r"""
        :param _RoleName: Fuzzy query by role name
        :type RoleName: str
        :param _Offset: Offset. If this parameter is left empty, 0 will be used by default.
        :type Offset: int
        :param _Limit: Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 20.
        :type Limit: int
        :param _ClusterId: Cluster ID (required)
        :type ClusterId: str
        :param _Filters: * RoleName
Filter by role name for exact query.
Type: String
Required: no
        :type Filters: list of Filter
        """
        self._RoleName = None
        self._Offset = None
        self._Limit = None
        self._ClusterId = None
        self._Filters = None

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

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
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ClusterId = params.get("ClusterId")
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
        


class DescribeRolesResponse(AbstractModel):
    """DescribeRoles response structure.

    """

    def __init__(self):
        r"""
        :param _TotalCount: Number of records.
        :type TotalCount: int
        :param _RoleSets: Array of roles.
        :type RoleSets: list of Role
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TotalCount = None
        self._RoleSets = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RoleSets(self):
        return self._RoleSets

    @RoleSets.setter
    def RoleSets(self, RoleSets):
        self._RoleSets = RoleSets

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RoleSets") is not None:
            self._RoleSets = []
            for item in params.get("RoleSets"):
                obj = Role()
                obj._deserialize(item)
                self._RoleSets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubscriptionsRequest(AbstractModel):
    """DescribeSubscriptions request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param _TopicName: Topic name.
        :type TopicName: str
        :param _Offset: Offset, which defaults to 0 if left empty.
        :type Offset: int
        :param _Limit: The number of results to be returned, which defaults to 10 if left empty. The maximum value is 20.
        :type Limit: int
        :param _SubscriptionName: Fuzzy match by subscriber name.
        :type SubscriptionName: str
        :param _Filters: Data filter.
        :type Filters: list of FilterSubscription
        :param _ClusterId: Pulsar cluster ID
        :type ClusterId: str
        """
        self._EnvironmentId = None
        self._TopicName = None
        self._Offset = None
        self._Limit = None
        self._SubscriptionName = None
        self._Filters = None
        self._ClusterId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

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
    def SubscriptionName(self):
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SubscriptionName = params.get("SubscriptionName")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = FilterSubscription()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubscriptionsResponse(AbstractModel):
    """DescribeSubscriptions response structure.

    """

    def __init__(self):
        r"""
        :param _SubscriptionSets: Array of subscriber sets.
        :type SubscriptionSets: list of Subscription
        :param _TotalCount: The total number of returned results.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._SubscriptionSets = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SubscriptionSets(self):
        return self._SubscriptionSets

    @SubscriptionSets.setter
    def SubscriptionSets(self, SubscriptionSets):
        self._SubscriptionSets = SubscriptionSets

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SubscriptionSets") is not None:
            self._SubscriptionSets = []
            for item in params.get("SubscriptionSets"):
                obj = Subscription()
                obj._deserialize(item)
                self._SubscriptionSets.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTopicsRequest(AbstractModel):
    """DescribeTopics request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param _TopicName: Fuzzy match by topic name.
        :type TopicName: str
        :param _Offset: Offset, which defaults to 0 if left empty.
        :type Offset: int
        :param _Limit: The number of results to be returned, which defaults to 10 if left empty. The maximum value is 20.
        :type Limit: int
        :param _TopicType: Topic type description:
0: Non-persistent and non-partitioned topic;
1: Non-persistent and partitioned topic;
2: Persistent and non-partitioned topic;
3: Persistent and partitioned topic.
        :type TopicType: int
        :param _ClusterId: Pulsar cluster ID.
        :type ClusterId: str
        :param _Filters: * TopicName
Query by topic name for exact search.
Type: String
Required: No
        :type Filters: list of Filter
        :param _TopicCreator: Topic creator:
1: User
2: System
        :type TopicCreator: int
        """
        self._EnvironmentId = None
        self._TopicName = None
        self._Offset = None
        self._Limit = None
        self._TopicType = None
        self._ClusterId = None
        self._Filters = None
        self._TopicCreator = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

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
    def TopicType(self):
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TopicCreator(self):
        return self._TopicCreator

    @TopicCreator.setter
    def TopicCreator(self, TopicCreator):
        self._TopicCreator = TopicCreator


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TopicType = params.get("TopicType")
        self._ClusterId = params.get("ClusterId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._TopicCreator = params.get("TopicCreator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicsResponse(AbstractModel):
    """DescribeTopics response structure.

    """

    def __init__(self):
        r"""
        :param _TopicSets: Array of topic sets.
        :type TopicSets: list of Topic
        :param _TotalCount: The number of topics.
        :type TotalCount: int
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._TopicSets = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TopicSets(self):
        return self._TopicSets

    @TopicSets.setter
    def TopicSets(self, TopicSets):
        self._TopicSets = TopicSets

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TopicSets") is not None:
            self._TopicSets = []
            for item in params.get("TopicSets"):
                obj = Topic()
                obj._deserialize(item)
                self._TopicSets.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class Environment(AbstractModel):
    """Namespace information

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Namespace name.
        :type EnvironmentId: str
        :param _Remark: Description.
        :type Remark: str
        :param _MsgTTL: Retention period for unconsumed messages in seconds. Maximum value: 1,296,000 seconds (15 days).
        :type MsgTTL: int
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _UpdateTime: Last modified.
        :type UpdateTime: str
        :param _NamespaceId: Namespace ID.
        :type NamespaceId: str
        :param _NamespaceName: Namespace name.
        :type NamespaceName: str
        :param _TopicNum: The number of topics.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TopicNum: int
        :param _RetentionPolicy: Message retention policy.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RetentionPolicy: :class:`tencentcloud.tdmq.v20200217.models.RetentionPolicy`
        """
        self._EnvironmentId = None
        self._Remark = None
        self._MsgTTL = None
        self._CreateTime = None
        self._UpdateTime = None
        self._NamespaceId = None
        self._NamespaceName = None
        self._TopicNum = None
        self._RetentionPolicy = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def MsgTTL(self):
        return self._MsgTTL

    @MsgTTL.setter
    def MsgTTL(self, MsgTTL):
        self._MsgTTL = MsgTTL

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def NamespaceName(self):
        return self._NamespaceName

    @NamespaceName.setter
    def NamespaceName(self, NamespaceName):
        self._NamespaceName = NamespaceName

    @property
    def TopicNum(self):
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def RetentionPolicy(self):
        return self._RetentionPolicy

    @RetentionPolicy.setter
    def RetentionPolicy(self, RetentionPolicy):
        self._RetentionPolicy = RetentionPolicy


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._Remark = params.get("Remark")
        self._MsgTTL = params.get("MsgTTL")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._NamespaceId = params.get("NamespaceId")
        self._NamespaceName = params.get("NamespaceName")
        self._TopicNum = params.get("TopicNum")
        if params.get("RetentionPolicy") is not None:
            self._RetentionPolicy = RetentionPolicy()
            self._RetentionPolicy._deserialize(params.get("RetentionPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvironmentRole(AbstractModel):
    """Set of environment roles

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment (namespace).
        :type EnvironmentId: str
        :param _RoleName: Role name.
        :type RoleName: str
        :param _Permissions: Permissions, which is a non-empty string array of `produce` and `consume` at the most.
        :type Permissions: list of str
        :param _RoleDescribe: Role description.
        :type RoleDescribe: str
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _UpdateTime: Update time.
        :type UpdateTime: str
        """
        self._EnvironmentId = None
        self._RoleName = None
        self._Permissions = None
        self._RoleDescribe = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Permissions(self):
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions

    @property
    def RoleDescribe(self):
        return self._RoleDescribe

    @RoleDescribe.setter
    def RoleDescribe(self, RoleDescribe):
        self._RoleDescribe = RoleDescribe

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._RoleName = params.get("RoleName")
        self._Permissions = params.get("Permissions")
        self._RoleDescribe = params.get("RoleDescribe")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        


class FilterSubscription(AbstractModel):
    """Filter subscriptions

    """

    def __init__(self):
        r"""
        :param _ConsumerHasCount: Whether to only display subscriptions that include real consumers.
        :type ConsumerHasCount: bool
        :param _ConsumerHasBacklog: Whether to only display subscriptions with heaped messages.
        :type ConsumerHasBacklog: bool
        :param _ConsumerHasExpired: Whether to only display subscriptions with messages discarded after expiration.
        :type ConsumerHasExpired: bool
        :param _SubscriptionNames: Filter by subscription name for exact query.
        :type SubscriptionNames: list of str
        """
        self._ConsumerHasCount = None
        self._ConsumerHasBacklog = None
        self._ConsumerHasExpired = None
        self._SubscriptionNames = None

    @property
    def ConsumerHasCount(self):
        return self._ConsumerHasCount

    @ConsumerHasCount.setter
    def ConsumerHasCount(self, ConsumerHasCount):
        self._ConsumerHasCount = ConsumerHasCount

    @property
    def ConsumerHasBacklog(self):
        return self._ConsumerHasBacklog

    @ConsumerHasBacklog.setter
    def ConsumerHasBacklog(self, ConsumerHasBacklog):
        self._ConsumerHasBacklog = ConsumerHasBacklog

    @property
    def ConsumerHasExpired(self):
        return self._ConsumerHasExpired

    @ConsumerHasExpired.setter
    def ConsumerHasExpired(self, ConsumerHasExpired):
        self._ConsumerHasExpired = ConsumerHasExpired

    @property
    def SubscriptionNames(self):
        return self._SubscriptionNames

    @SubscriptionNames.setter
    def SubscriptionNames(self, SubscriptionNames):
        self._SubscriptionNames = SubscriptionNames


    def _deserialize(self, params):
        self._ConsumerHasCount = params.get("ConsumerHasCount")
        self._ConsumerHasBacklog = params.get("ConsumerHasBacklog")
        self._ConsumerHasExpired = params.get("ConsumerHasExpired")
        self._SubscriptionNames = params.get("SubscriptionNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNodeDistribution(AbstractModel):
    """Information of instance node distribution

    """

    def __init__(self):
        r"""
        :param _ZoneName: AZ
        :type ZoneName: str
        :param _ZoneId: AZ ID
        :type ZoneId: str
        :param _NodeCount: Number of nodes
        :type NodeCount: int
        """
        self._ZoneName = None
        self._ZoneId = None
        self._NodeCount = None

    @property
    def ZoneName(self):
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def NodeCount(self):
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount


    def _deserialize(self, params):
        self._ZoneName = params.get("ZoneName")
        self._ZoneId = params.get("ZoneId")
        self._NodeCount = params.get("NodeCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterRequest(AbstractModel):
    """ModifyCluster request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: ID of the Pulsar cluster to be updated.
        :type ClusterId: str
        :param _ClusterName: Updated cluster name.
        :type ClusterName: str
        :param _Remark: Remarks.
        :type Remark: str
        :param _PublicAccessEnabled: Enables public network access, which can only be `true`.
        :type PublicAccessEnabled: bool
        """
        self._ClusterId = None
        self._ClusterName = None
        self._Remark = None
        self._PublicAccessEnabled = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PublicAccessEnabled(self):
        return self._PublicAccessEnabled

    @PublicAccessEnabled.setter
    def PublicAccessEnabled(self, PublicAccessEnabled):
        self._PublicAccessEnabled = PublicAccessEnabled


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Remark = params.get("Remark")
        self._PublicAccessEnabled = params.get("PublicAccessEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterResponse(AbstractModel):
    """ModifyCluster response structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Pulsar cluster ID
        :type ClusterId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._ClusterId = None
        self._RequestId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._RequestId = params.get("RequestId")


class ModifyCmqQueueAttributeRequest(AbstractModel):
    """ModifyCmqQueueAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _QueueName: Queue name, which must be unique under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type QueueName: str
        :param _MaxMsgHeapNum: Maximum number of heaped messages. The value range is 1,000,000–10,000,000 during the beta test and can be 1,000,000–1,000,000,000 after the product is officially released. The default value is 10,000,000 during the beta test and will be 100,000,000 after the product is officially released.
        :type MaxMsgHeapNum: int
        :param _PollingWaitSeconds: Long polling wait time for message reception. Value range: 0–30 seconds. Default value: 0.
        :type PollingWaitSeconds: int
        :param _VisibilityTimeout: Message visibility timeout period. Value range: 1–43200 seconds (i.e., 12 hours). Default value: 30.
        :type VisibilityTimeout: int
        :param _MaxMsgSize: Max message size, which defaults to 1,024 KB for the queue of TDMQ for CMQ and cannot be modified.
        :type MaxMsgSize: int
        :param _MsgRetentionSeconds: The max period during which a message is retained before it is automatically acknowledged. Value range: 30-43,200 seconds (30 seconds to 12 hours). Default value: 3600 seconds (1 hour).
        :type MsgRetentionSeconds: int
        :param _RewindSeconds: Rewindable time of messages in the queue. Value range: 0-1,296,000s (if message rewind is enabled). The value “0” indicates that message rewind is not enabled.
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
        :param _Trace: Whether to enable message trace. true: yes; false: no. If this field is left empty, the feature will not be enabled.
        :type Trace: bool
        :param _Transaction: Whether to enable transaction. 1: yes; 0: no
        :type Transaction: int
        :param _RetentionSizeInMB: Queue storage space configured for message rewind. Value range: 10,240-512,000 MB (if message rewind is enabled). The value “0” indicates that message rewind is not enabled.
        :type RetentionSizeInMB: int
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
        self._Transaction = None
        self._RetentionSizeInMB = None

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

    @property
    def Transaction(self):
        return self._Transaction

    @Transaction.setter
    def Transaction(self, Transaction):
        self._Transaction = Transaction

    @property
    def RetentionSizeInMB(self):
        return self._RetentionSizeInMB

    @RetentionSizeInMB.setter
    def RetentionSizeInMB(self, RetentionSizeInMB):
        self._RetentionSizeInMB = RetentionSizeInMB


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
        self._Transaction = params.get("Transaction")
        self._RetentionSizeInMB = params.get("RetentionSizeInMB")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCmqQueueAttributeResponse(AbstractModel):
    """ModifyCmqQueueAttribute response structure.

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


class ModifyCmqSubscriptionAttributeRequest(AbstractModel):
    """ModifyCmqSubscriptionAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name, which must be unique in the same topic under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type TopicName: str
        :param _SubscriptionName: Subscription name, which must be unique in the same topic under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type SubscriptionName: str
        :param _NotifyStrategy: CMQ push server retry policy in case an error occurs while pushing a message to the endpoint. Valid values:
(1) BACKOFF_RETRY: backoff retry, which is to retry at a fixed interval, discard the message after a certain number of retries, and continue to push the next message.
(2) EXPONENTIAL_DECAY_RETRY: exponential decay retry, which is to retry at an exponentially increasing interval, such as 1s, 2s, 4s, 8s, and so on. As a message can be retained in a topic for one day, failed messages will be discarded at most after one day of retry. Default value: EXPONENTIAL_DECAY_RETRY.
        :type NotifyStrategy: str
        :param _NotifyContentFormat: Push content format. Valid values: 1. JSON; 2. SIMPLIFIED, i.e., the raw format. If `Protocol` is `queue`, this value must be `SIMPLIFIED`. If `Protocol` is `HTTP`, both values are acceptable, and the default value is `JSON`.
        :type NotifyContentFormat: str
        :param _FilterTags: Message body tag (used for message filtering). The number of tags cannot exceed 5, and each tag can contain up to 16 characters. It is used in conjunction with the `MsgTag` parameter of `(Batch)PublishMessage`. Rules: 1. If `FilterTag` is not configured, no matter whether `MsgTag` is configured, the subscription will receive all messages published to the topic; 2. If the array of `FilterTag` values has a value, only when at least one of the values in the array also exists in the array of `MsgTag` values (i.e., `FilterTag` and `MsgTag` have an intersection) can the subscription receive messages published to the topic; 3. If the array of `FilterTag` values has a value, but `MsgTag` is not configured, then no message published to the topic will be received, which can be considered as a special case of rule 2 as `FilterTag` and `MsgTag` do not intersect in this case. The overall design idea of rules is based on the intention of the subscriber.
        :type FilterTags: list of str
        :param _BindingKey: The number of `BindingKey` cannot exceed 5, and the length of each `BindingKey` cannot exceed 64 bytes. This field indicates the filtering policy for subscribing to and receiving messages. Each `BindingKey` includes up to 15 dots (namely up to 16 segments).
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
        


class ModifyCmqSubscriptionAttributeResponse(AbstractModel):
    """ModifyCmqSubscriptionAttribute response structure.

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


class ModifyCmqTopicAttributeRequest(AbstractModel):
    """ModifyCmqTopicAttribute request structure.

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name, which must be unique under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type TopicName: str
        :param _MaxMsgSize: Maximum message length. Value range: 1024–65536 bytes (i.e., 1–64 KB). Default value: 65536.
        :type MaxMsgSize: int
        :param _MsgRetentionSeconds: Message retention period. Value range: 60–86400 seconds (i.e., 1 minute–1 day). Default value: 86400.
        :type MsgRetentionSeconds: int
        :param _Trace: Whether to enable message trace. true: yes; false: no. If this field is left empty, the feature will not be enabled.
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
        


class ModifyCmqTopicAttributeResponse(AbstractModel):
    """ModifyCmqTopicAttribute response structure.

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


class ModifyEnvironmentAttributesRequest(AbstractModel):
    """ModifyEnvironmentAttributes request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Namespace name.
        :type EnvironmentId: str
        :param _MsgTTL: Retention period for unconsumed messages in seconds. Value range: 60s to 1,296,000s (or 15 days).
        :type MsgTTL: int
        :param _Remark: Remarks (up to 128 characters).
        :type Remark: str
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _RetentionPolicy: Message retention policy
        :type RetentionPolicy: :class:`tencentcloud.tdmq.v20200217.models.RetentionPolicy`
        """
        self._EnvironmentId = None
        self._MsgTTL = None
        self._Remark = None
        self._ClusterId = None
        self._RetentionPolicy = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def MsgTTL(self):
        return self._MsgTTL

    @MsgTTL.setter
    def MsgTTL(self, MsgTTL):
        self._MsgTTL = MsgTTL

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RetentionPolicy(self):
        return self._RetentionPolicy

    @RetentionPolicy.setter
    def RetentionPolicy(self, RetentionPolicy):
        self._RetentionPolicy = RetentionPolicy


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._MsgTTL = params.get("MsgTTL")
        self._Remark = params.get("Remark")
        self._ClusterId = params.get("ClusterId")
        if params.get("RetentionPolicy") is not None:
            self._RetentionPolicy = RetentionPolicy()
            self._RetentionPolicy._deserialize(params.get("RetentionPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEnvironmentAttributesResponse(AbstractModel):
    """ModifyEnvironmentAttributes response structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Namespace name.
        :type EnvironmentId: str
        :param _MsgTTL: TTL for unconsumed messages in seconds.
        :type MsgTTL: int
        :param _Remark: Remarks (up to 128 characters).
Note: this field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param _NamespaceId: Namespace ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type NamespaceId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._EnvironmentId = None
        self._MsgTTL = None
        self._Remark = None
        self._NamespaceId = None
        self._RequestId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def MsgTTL(self):
        return self._MsgTTL

    @MsgTTL.setter
    def MsgTTL(self, MsgTTL):
        self._MsgTTL = MsgTTL

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._MsgTTL = params.get("MsgTTL")
        self._Remark = params.get("Remark")
        self._NamespaceId = params.get("NamespaceId")
        self._RequestId = params.get("RequestId")


class ModifyEnvironmentRoleRequest(AbstractModel):
    """ModifyEnvironmentRole request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param _RoleName: Role name.
        :type RoleName: str
        :param _Permissions: Permissions, which is a non-empty string array of `produce` and `consume` at the most.
        :type Permissions: list of str
        :param _ClusterId: Cluster ID (required)
        :type ClusterId: str
        """
        self._EnvironmentId = None
        self._RoleName = None
        self._Permissions = None
        self._ClusterId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Permissions(self):
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._RoleName = params.get("RoleName")
        self._Permissions = params.get("Permissions")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEnvironmentRoleResponse(AbstractModel):
    """ModifyEnvironmentRole response structure.

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


class ModifyRocketMQClusterRequest(AbstractModel):
    """ModifyRocketMQCluster request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: RocketMQ cluster ID
        :type ClusterId: str
        :param _ClusterName: 3–64 letters, digits, hyphens, and underscores
        :type ClusterName: str
        :param _Remark: Remarks (up to 128 characters)
        :type Remark: str
        """
        self._ClusterId = None
        self._ClusterName = None
        self._Remark = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRocketMQClusterResponse(AbstractModel):
    """ModifyRocketMQCluster response structure.

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


class ModifyRocketMQGroupRequest(AbstractModel):
    """ModifyRocketMQGroup request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _NamespaceId: Namespace
        :type NamespaceId: str
        :param _GroupId: Consumer group name
        :type GroupId: str
        :param _Remark: Remarks (up to 128 characters)
        :type Remark: str
        :param _ReadEnable: Whether to enable consumption
        :type ReadEnable: bool
        :param _BroadcastEnable: Whether to enable broadcast consumption
        :type BroadcastEnable: bool
        :param _RetryMaxTimes: The maximum number of retries
        :type RetryMaxTimes: int
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._GroupId = None
        self._Remark = None
        self._ReadEnable = None
        self._BroadcastEnable = None
        self._RetryMaxTimes = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ReadEnable(self):
        return self._ReadEnable

    @ReadEnable.setter
    def ReadEnable(self, ReadEnable):
        self._ReadEnable = ReadEnable

    @property
    def BroadcastEnable(self):
        return self._BroadcastEnable

    @BroadcastEnable.setter
    def BroadcastEnable(self, BroadcastEnable):
        self._BroadcastEnable = BroadcastEnable

    @property
    def RetryMaxTimes(self):
        return self._RetryMaxTimes

    @RetryMaxTimes.setter
    def RetryMaxTimes(self, RetryMaxTimes):
        self._RetryMaxTimes = RetryMaxTimes


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._GroupId = params.get("GroupId")
        self._Remark = params.get("Remark")
        self._ReadEnable = params.get("ReadEnable")
        self._BroadcastEnable = params.get("BroadcastEnable")
        self._RetryMaxTimes = params.get("RetryMaxTimes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRocketMQGroupResponse(AbstractModel):
    """ModifyRocketMQGroup response structure.

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


class ModifyRocketMQNamespaceRequest(AbstractModel):
    """ModifyRocketMQNamespace request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _NamespaceId: Namespace name, which can contain 3–64 letters, digits, hyphens, and underscores
        :type NamespaceId: str
        :param _Ttl: Retention time of unconsumed messages in milliseconds. Value range: 60 seconds–15 days
        :type Ttl: int
        :param _RetentionTime: Retention time for persisted messages in milliseconds
        :type RetentionTime: int
        :param _Remark: Remarks (up to 128 characters)
        :type Remark: str
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._Ttl = None
        self._RetentionTime = None
        self._Remark = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def Ttl(self):
        return self._Ttl

    @Ttl.setter
    def Ttl(self, Ttl):
        self._Ttl = Ttl

    @property
    def RetentionTime(self):
        return self._RetentionTime

    @RetentionTime.setter
    def RetentionTime(self, RetentionTime):
        self._RetentionTime = RetentionTime

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._Ttl = params.get("Ttl")
        self._RetentionTime = params.get("RetentionTime")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRocketMQNamespaceResponse(AbstractModel):
    """ModifyRocketMQNamespace response structure.

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


class ModifyRocketMQTopicRequest(AbstractModel):
    """ModifyRocketMQTopic request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _NamespaceId: Namespace name
        :type NamespaceId: str
        :param _Topic: Topic name
        :type Topic: str
        :param _Remark: Remarks (up to 128 characters)
        :type Remark: str
        :param _PartitionNum: Number of partitions, which is invalid for globally sequential messages and cannot be less than the current number of partitions.
        :type PartitionNum: int
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._Topic = None
        self._Remark = None
        self._PartitionNum = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PartitionNum(self):
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._Topic = params.get("Topic")
        self._Remark = params.get("Remark")
        self._PartitionNum = params.get("PartitionNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRocketMQTopicResponse(AbstractModel):
    """ModifyRocketMQTopic response structure.

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


class ModifyRoleRequest(AbstractModel):
    """ModifyRole request structure.

    """

    def __init__(self):
        r"""
        :param _RoleName: Role name, which can contain up to 32 letters, digits, hyphens, and underscores.
        :type RoleName: str
        :param _Remark: Remarks (up to 128 characters).
        :type Remark: str
        :param _ClusterId: Cluster ID (required)
        :type ClusterId: str
        """
        self._RoleName = None
        self._Remark = None
        self._ClusterId = None

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._Remark = params.get("Remark")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRoleResponse(AbstractModel):
    """ModifyRole response structure.

    """

    def __init__(self):
        r"""
        :param _RoleName: Role name
        :type RoleName: str
        :param _Remark: Remarks
        :type Remark: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._RoleName = None
        self._Remark = None
        self._RequestId = None

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._Remark = params.get("Remark")
        self._RequestId = params.get("RequestId")


class ModifyTopicRequest(AbstractModel):
    """ModifyTopic request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param _TopicName: Topic name.
        :type TopicName: str
        :param _Partitions: Number of partitions, which must be equal to or greater than the original number of partitions. To maintain the original number of partitions, enter the original number. Modifying the number of partitions will take effect only for non-globally sequential messages. There can be up to 128 partitions.
        :type Partitions: int
        :param _Remark: Remarks (up to 128 characters).
        :type Remark: str
        :param _ClusterId: Pulsar cluster ID
        :type ClusterId: str
        """
        self._EnvironmentId = None
        self._TopicName = None
        self._Partitions = None
        self._Remark = None
        self._ClusterId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._Partitions = params.get("Partitions")
        self._Remark = params.get("Remark")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicResponse(AbstractModel):
    """ModifyTopic response structure.

    """

    def __init__(self):
        r"""
        :param _Partitions: Number of partitions
        :type Partitions: int
        :param _Remark: Remarks (up to 128 characters).
        :type Remark: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Partitions = None
        self._Remark = None
        self._RequestId = None

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Partitions = params.get("Partitions")
        self._Remark = params.get("Remark")
        self._RequestId = params.get("RequestId")


class PartitionsTopic(AbstractModel):
    """Partitioned topic

    """

    def __init__(self):
        r"""
        :param _AverageMsgSize: Average size of the messages published in the last interval in bytes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AverageMsgSize: str
        :param _ConsumerCount: The number of consumers.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConsumerCount: str
        :param _LastConfirmedEntry: The total number of recorded messages.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastConfirmedEntry: str
        :param _LastLedgerCreatedTimestamp: Time when the last ledger was created.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastLedgerCreatedTimestamp: str
        :param _MsgRateIn: The number of messages published by local and replicated publishers per second.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MsgRateIn: str
        :param _MsgRateOut: The total number of messages delivered by local and replicated consumers per second.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MsgRateOut: str
        :param _MsgThroughputIn: The size (in bytes) of messages published by local and replicated publishers per second.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MsgThroughputIn: str
        :param _MsgThroughputOut: The size (in bytes) of messages delivered by local and replicated consumers per second.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MsgThroughputOut: str
        :param _NumberOfEntries: The total number of recorded messages.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NumberOfEntries: str
        :param _Partitions: Subpartition ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Partitions: int
        :param _ProducerCount: The number of producers.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProducerCount: str
        :param _TotalSize: Total size of all stored messages in bytes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: str
        :param _TopicType: Topic type description.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TopicType: int
        """
        self._AverageMsgSize = None
        self._ConsumerCount = None
        self._LastConfirmedEntry = None
        self._LastLedgerCreatedTimestamp = None
        self._MsgRateIn = None
        self._MsgRateOut = None
        self._MsgThroughputIn = None
        self._MsgThroughputOut = None
        self._NumberOfEntries = None
        self._Partitions = None
        self._ProducerCount = None
        self._TotalSize = None
        self._TopicType = None

    @property
    def AverageMsgSize(self):
        return self._AverageMsgSize

    @AverageMsgSize.setter
    def AverageMsgSize(self, AverageMsgSize):
        self._AverageMsgSize = AverageMsgSize

    @property
    def ConsumerCount(self):
        return self._ConsumerCount

    @ConsumerCount.setter
    def ConsumerCount(self, ConsumerCount):
        self._ConsumerCount = ConsumerCount

    @property
    def LastConfirmedEntry(self):
        return self._LastConfirmedEntry

    @LastConfirmedEntry.setter
    def LastConfirmedEntry(self, LastConfirmedEntry):
        self._LastConfirmedEntry = LastConfirmedEntry

    @property
    def LastLedgerCreatedTimestamp(self):
        return self._LastLedgerCreatedTimestamp

    @LastLedgerCreatedTimestamp.setter
    def LastLedgerCreatedTimestamp(self, LastLedgerCreatedTimestamp):
        self._LastLedgerCreatedTimestamp = LastLedgerCreatedTimestamp

    @property
    def MsgRateIn(self):
        return self._MsgRateIn

    @MsgRateIn.setter
    def MsgRateIn(self, MsgRateIn):
        self._MsgRateIn = MsgRateIn

    @property
    def MsgRateOut(self):
        return self._MsgRateOut

    @MsgRateOut.setter
    def MsgRateOut(self, MsgRateOut):
        self._MsgRateOut = MsgRateOut

    @property
    def MsgThroughputIn(self):
        return self._MsgThroughputIn

    @MsgThroughputIn.setter
    def MsgThroughputIn(self, MsgThroughputIn):
        self._MsgThroughputIn = MsgThroughputIn

    @property
    def MsgThroughputOut(self):
        return self._MsgThroughputOut

    @MsgThroughputOut.setter
    def MsgThroughputOut(self, MsgThroughputOut):
        self._MsgThroughputOut = MsgThroughputOut

    @property
    def NumberOfEntries(self):
        return self._NumberOfEntries

    @NumberOfEntries.setter
    def NumberOfEntries(self, NumberOfEntries):
        self._NumberOfEntries = NumberOfEntries

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def ProducerCount(self):
        return self._ProducerCount

    @ProducerCount.setter
    def ProducerCount(self, ProducerCount):
        self._ProducerCount = ProducerCount

    @property
    def TotalSize(self):
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def TopicType(self):
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType


    def _deserialize(self, params):
        self._AverageMsgSize = params.get("AverageMsgSize")
        self._ConsumerCount = params.get("ConsumerCount")
        self._LastConfirmedEntry = params.get("LastConfirmedEntry")
        self._LastLedgerCreatedTimestamp = params.get("LastLedgerCreatedTimestamp")
        self._MsgRateIn = params.get("MsgRateIn")
        self._MsgRateOut = params.get("MsgRateOut")
        self._MsgThroughputIn = params.get("MsgThroughputIn")
        self._MsgThroughputOut = params.get("MsgThroughputOut")
        self._NumberOfEntries = params.get("NumberOfEntries")
        self._Partitions = params.get("Partitions")
        self._ProducerCount = params.get("ProducerCount")
        self._TotalSize = params.get("TotalSize")
        self._TopicType = params.get("TopicType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishCmqMsgRequest(AbstractModel):
    """PublishCmqMsg request structure.

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name
        :type TopicName: str
        :param _MsgContent: Message content. The total message size is up to 1,024 KB.
        :type MsgContent: str
        :param _MsgTag: Message tag. You can pass in multiple tags or a single route. Each tag or route can contain up to 64 characters.
        :type MsgTag: list of str
        """
        self._TopicName = None
        self._MsgContent = None
        self._MsgTag = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def MsgContent(self):
        return self._MsgContent

    @MsgContent.setter
    def MsgContent(self, MsgContent):
        self._MsgContent = MsgContent

    @property
    def MsgTag(self):
        return self._MsgTag

    @MsgTag.setter
    def MsgTag(self, MsgTag):
        self._MsgTag = MsgTag


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._MsgContent = params.get("MsgContent")
        self._MsgTag = params.get("MsgTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishCmqMsgResponse(AbstractModel):
    """PublishCmqMsg response structure.

    """

    def __init__(self):
        r"""
        :param _Result: `true` indicates that the sending is successful
        :type Result: bool
        :param _MsgId: Message ID
        :type MsgId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._MsgId = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def MsgId(self):
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._MsgId = params.get("MsgId")
        self._RequestId = params.get("RequestId")


class Publisher(AbstractModel):
    """Producer information

    """

    def __init__(self):
        r"""
        :param _ProducerId: Producer ID.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ProducerId: int
        :param _ProducerName: Producer name.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ProducerName: str
        :param _Address: Producer address.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Address: str
        :param _ClientVersion: Client version.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ClientVersion: str
        :param _MsgRateIn: Message production rate (message/sec).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MsgRateIn: float
        :param _MsgThroughputIn: Message production throughput rate (byte/sec).
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MsgThroughputIn: float
        :param _AverageMsgSize: Average message size in bytes.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AverageMsgSize: float
        :param _ConnectedSince: Connection time.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ConnectedSince: str
        :param _Partition: Serial number of the topic partition connected to the producer.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Partition: int
        """
        self._ProducerId = None
        self._ProducerName = None
        self._Address = None
        self._ClientVersion = None
        self._MsgRateIn = None
        self._MsgThroughputIn = None
        self._AverageMsgSize = None
        self._ConnectedSince = None
        self._Partition = None

    @property
    def ProducerId(self):
        return self._ProducerId

    @ProducerId.setter
    def ProducerId(self, ProducerId):
        self._ProducerId = ProducerId

    @property
    def ProducerName(self):
        return self._ProducerName

    @ProducerName.setter
    def ProducerName(self, ProducerName):
        self._ProducerName = ProducerName

    @property
    def Address(self):
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def ClientVersion(self):
        return self._ClientVersion

    @ClientVersion.setter
    def ClientVersion(self, ClientVersion):
        self._ClientVersion = ClientVersion

    @property
    def MsgRateIn(self):
        return self._MsgRateIn

    @MsgRateIn.setter
    def MsgRateIn(self, MsgRateIn):
        self._MsgRateIn = MsgRateIn

    @property
    def MsgThroughputIn(self):
        return self._MsgThroughputIn

    @MsgThroughputIn.setter
    def MsgThroughputIn(self, MsgThroughputIn):
        self._MsgThroughputIn = MsgThroughputIn

    @property
    def AverageMsgSize(self):
        return self._AverageMsgSize

    @AverageMsgSize.setter
    def AverageMsgSize(self, AverageMsgSize):
        self._AverageMsgSize = AverageMsgSize

    @property
    def ConnectedSince(self):
        return self._ConnectedSince

    @ConnectedSince.setter
    def ConnectedSince(self, ConnectedSince):
        self._ConnectedSince = ConnectedSince

    @property
    def Partition(self):
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        self._Partition = Partition


    def _deserialize(self, params):
        self._ProducerId = params.get("ProducerId")
        self._ProducerName = params.get("ProducerName")
        self._Address = params.get("Address")
        self._ClientVersion = params.get("ClientVersion")
        self._MsgRateIn = params.get("MsgRateIn")
        self._MsgThroughputIn = params.get("MsgThroughputIn")
        self._AverageMsgSize = params.get("AverageMsgSize")
        self._ConnectedSince = params.get("ConnectedSince")
        self._Partition = params.get("Partition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PulsarNetworkAccessPointInfo(AbstractModel):
    """TDMQ for Pulsar network access point information

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC ID. This field is left empty for supporting network and public network access points.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _SubnetId: Subnet ID. This field is left empty for supporting network and public network access points.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _Endpoint: Access address
        :type Endpoint: str
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _RouteType: Access point type: 
`0`: Supporting network access point 
`1`: VPC access point 
`2`: Public network access point
        :type RouteType: int
        """
        self._VpcId = None
        self._SubnetId = None
        self._Endpoint = None
        self._InstanceId = None
        self._RouteType = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RouteType(self):
        return self._RouteType

    @RouteType.setter
    def RouteType(self, RouteType):
        self._RouteType = RouteType


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Endpoint = params.get("Endpoint")
        self._InstanceId = params.get("InstanceId")
        self._RouteType = params.get("RouteType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PulsarProClusterInfo(AbstractModel):
    """TDMQ for Pulsar pro cluster information

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ClusterName: Cluster name
        :type ClusterName: str
        :param _Remark: Description
        :type Remark: str
        :param _CreateTime: Creation time
        :type CreateTime: str
        :param _Status: Cluster status. Valid values: `0` (Creating), `1` (Normal), `2` (Isolated).
        :type Status: int
        :param _Version: Cluster version
        :type Version: str
        :param _NodeDistribution: Node distribution
Note: This field may return null, indicating that no valid values can be obtained.
        :type NodeDistribution: list of InstanceNodeDistribution
        :param _MaxStorage: Max storage capacity in MB
        :type MaxStorage: int
        """
        self._ClusterId = None
        self._ClusterName = None
        self._Remark = None
        self._CreateTime = None
        self._Status = None
        self._Version = None
        self._NodeDistribution = None
        self._MaxStorage = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def NodeDistribution(self):
        return self._NodeDistribution

    @NodeDistribution.setter
    def NodeDistribution(self, NodeDistribution):
        self._NodeDistribution = NodeDistribution

    @property
    def MaxStorage(self):
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        self._Version = params.get("Version")
        if params.get("NodeDistribution") is not None:
            self._NodeDistribution = []
            for item in params.get("NodeDistribution"):
                obj = InstanceNodeDistribution()
                obj._deserialize(item)
                self._NodeDistribution.append(obj)
        self._MaxStorage = params.get("MaxStorage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PulsarProClusterSpecInfo(AbstractModel):
    """TDMQ for Pulsar pro cluster specification information

    """

    def __init__(self):
        r"""
        :param _SpecName: Cluster specification name
        :type SpecName: str
        :param _MaxTps: Peak TPS
        :type MaxTps: int
        :param _MaxBandWidth: Peak bandwidth in Mbps
        :type MaxBandWidth: int
        :param _MaxNamespaces: Maximum number of namespaces
        :type MaxNamespaces: int
        :param _MaxTopics: Maximum number of topic partitions
        :type MaxTopics: int
        :param _ScalableTps: Elastic TPS beyond the specification
Note: This field may return null, indicating that no valid values can be obtained.
        :type ScalableTps: int
        """
        self._SpecName = None
        self._MaxTps = None
        self._MaxBandWidth = None
        self._MaxNamespaces = None
        self._MaxTopics = None
        self._ScalableTps = None

    @property
    def SpecName(self):
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def MaxTps(self):
        return self._MaxTps

    @MaxTps.setter
    def MaxTps(self, MaxTps):
        self._MaxTps = MaxTps

    @property
    def MaxBandWidth(self):
        return self._MaxBandWidth

    @MaxBandWidth.setter
    def MaxBandWidth(self, MaxBandWidth):
        self._MaxBandWidth = MaxBandWidth

    @property
    def MaxNamespaces(self):
        return self._MaxNamespaces

    @MaxNamespaces.setter
    def MaxNamespaces(self, MaxNamespaces):
        self._MaxNamespaces = MaxNamespaces

    @property
    def MaxTopics(self):
        return self._MaxTopics

    @MaxTopics.setter
    def MaxTopics(self, MaxTopics):
        self._MaxTopics = MaxTopics

    @property
    def ScalableTps(self):
        return self._ScalableTps

    @ScalableTps.setter
    def ScalableTps(self, ScalableTps):
        self._ScalableTps = ScalableTps


    def _deserialize(self, params):
        self._SpecName = params.get("SpecName")
        self._MaxTps = params.get("MaxTps")
        self._MaxBandWidth = params.get("MaxBandWidth")
        self._MaxNamespaces = params.get("MaxNamespaces")
        self._MaxTopics = params.get("MaxTopics")
        self._ScalableTps = params.get("ScalableTps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PulsarProInstance(AbstractModel):
    """TDMQ for Pulsar pro instance information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _InstanceVersion: Instance version
        :type InstanceVersion: str
        :param _Status: Instance status. Valid values: `0` (Creating), `1` (Normal), `2` (Isolated), `3` (Terminated), `4` (Abnormal), `5` (Delivery failed), `6` (Adjusting configuration), `7` (Configuration adjustment failed).
        :type Status: int
        :param _ConfigDisplay: Instance specification name
        :type ConfigDisplay: str
        :param _MaxTps: Peak TPS
        :type MaxTps: int
        :param _MaxStorage: Storage capacity in GB
        :type MaxStorage: int
        :param _ExpireTime: Instance expiration time in milliseconds
        :type ExpireTime: int
        :param _AutoRenewFlag: Renewal mode. Valid values: `0` (Manual renewal, which is the default mode), `1` (Auto-renewal), `2` (Manual renewal, which is specified by users).
        :type AutoRenewFlag: int
        :param _PayMode: Payment mode. Valid values: `0` (Pay-as-you-go), `1` (Monthly subscription).
        :type PayMode: int
        :param _Remark: Remarks
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param _SpecName: Instance specification ID
        :type SpecName: str
        :param _ScalableTps: Elastic TPS beyond the specification
Note: This field may return null, indicating that no valid values can be obtained.
        :type ScalableTps: int
        :param _VpcId: VPC ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcId: str
        :param _SubnetId: Subnet ID
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubnetId: str
        :param _MaxBandWidth: Peak bandwidth in Mbps
        :type MaxBandWidth: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceVersion = None
        self._Status = None
        self._ConfigDisplay = None
        self._MaxTps = None
        self._MaxStorage = None
        self._ExpireTime = None
        self._AutoRenewFlag = None
        self._PayMode = None
        self._Remark = None
        self._SpecName = None
        self._ScalableTps = None
        self._VpcId = None
        self._SubnetId = None
        self._MaxBandWidth = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceVersion(self):
        return self._InstanceVersion

    @InstanceVersion.setter
    def InstanceVersion(self, InstanceVersion):
        self._InstanceVersion = InstanceVersion

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ConfigDisplay(self):
        return self._ConfigDisplay

    @ConfigDisplay.setter
    def ConfigDisplay(self, ConfigDisplay):
        self._ConfigDisplay = ConfigDisplay

    @property
    def MaxTps(self):
        return self._MaxTps

    @MaxTps.setter
    def MaxTps(self, MaxTps):
        self._MaxTps = MaxTps

    @property
    def MaxStorage(self):
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def SpecName(self):
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def ScalableTps(self):
        return self._ScalableTps

    @ScalableTps.setter
    def ScalableTps(self, ScalableTps):
        self._ScalableTps = ScalableTps

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def MaxBandWidth(self):
        return self._MaxBandWidth

    @MaxBandWidth.setter
    def MaxBandWidth(self, MaxBandWidth):
        self._MaxBandWidth = MaxBandWidth


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceVersion = params.get("InstanceVersion")
        self._Status = params.get("Status")
        self._ConfigDisplay = params.get("ConfigDisplay")
        self._MaxTps = params.get("MaxTps")
        self._MaxStorage = params.get("MaxStorage")
        self._ExpireTime = params.get("ExpireTime")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._PayMode = params.get("PayMode")
        self._Remark = params.get("Remark")
        self._SpecName = params.get("SpecName")
        self._ScalableTps = params.get("ScalableTps")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._MaxBandWidth = params.get("MaxBandWidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQPrivateNode(AbstractModel):
    """TDMQ for RabbitMQ node information

    """

    def __init__(self):
        r"""
        :param _NodeName: Node name
Note: This field may return null, indicating that no valid value can be obtained.
        :type NodeName: str
        :param _NodeStatus: Node status
Note: This field may return null, indicating that no valid value can be obtained.
        :type NodeStatus: str
        :param _CPUUsage: CPU utilization
Note: This field may return null, indicating that no valid values can be obtained.
        :type CPUUsage: str
        :param _Memory: Memory usage in MB
Note: This field may return null, indicating that no valid values can be obtained.
        :type Memory: int
        :param _DiskUsage: Disk utilization
Note: This field may return null, indicating that no valid values can be obtained.
        :type DiskUsage: str
        :param _ProcessNumber: The number of RabbitMQ Erlang processes
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProcessNumber: int
        """
        self._NodeName = None
        self._NodeStatus = None
        self._CPUUsage = None
        self._Memory = None
        self._DiskUsage = None
        self._ProcessNumber = None

    @property
    def NodeName(self):
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def NodeStatus(self):
        return self._NodeStatus

    @NodeStatus.setter
    def NodeStatus(self, NodeStatus):
        self._NodeStatus = NodeStatus

    @property
    def CPUUsage(self):
        return self._CPUUsage

    @CPUUsage.setter
    def CPUUsage(self, CPUUsage):
        self._CPUUsage = CPUUsage

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def DiskUsage(self):
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def ProcessNumber(self):
        return self._ProcessNumber

    @ProcessNumber.setter
    def ProcessNumber(self, ProcessNumber):
        self._ProcessNumber = ProcessNumber


    def _deserialize(self, params):
        self._NodeName = params.get("NodeName")
        self._NodeStatus = params.get("NodeStatus")
        self._CPUUsage = params.get("CPUUsage")
        self._Memory = params.get("Memory")
        self._DiskUsage = params.get("DiskUsage")
        self._ProcessNumber = params.get("ProcessNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RabbitMQVipInstance(AbstractModel):
    """TDMQ for RabbitMQ exclusive instance information

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _InstanceVersion: Instance version
Note: This field may return null, indicating that no valid value can be obtained.
        :type InstanceVersion: str
        :param _Status: Instance status. Valid values: `0` (Creating), `1` (Normal), `2` (Isolated), `3` (Terminated), `4` (Abnormal), `5` (Delivery failed).
        :type Status: int
        :param _NodeCount: Number of nodes
        :type NodeCount: int
        :param _ConfigDisplay: Instance specification name
        :type ConfigDisplay: str
        :param _MaxTps: Peak TPS
        :type MaxTps: int
        :param _MaxBandWidth: Peak bandwidth in Mbps
        :type MaxBandWidth: int
        :param _MaxStorage: Storage capacity in GB
        :type MaxStorage: int
        :param _ExpireTime: Instance expiration time in milliseconds
        :type ExpireTime: int
        :param _AutoRenewFlag: Renewal mode. Valid values: `0` (Manual renewal, which is the default mode), `1` (Auto-renewal), `2` (Manual renewal, which is specified by users).
        :type AutoRenewFlag: int
        :param _PayMode: Payment mode. `0`: Postpaid; `1`: Prepaid.
        :type PayMode: int
        :param _Remark: Remarks
Note: This field may return null, indicating that no valid value can be obtained.
        :type Remark: str
        :param _SpecName: Instance specification ID
        :type SpecName: str
        :param _ExceptionInformation: Cluster exception
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExceptionInformation: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceVersion = None
        self._Status = None
        self._NodeCount = None
        self._ConfigDisplay = None
        self._MaxTps = None
        self._MaxBandWidth = None
        self._MaxStorage = None
        self._ExpireTime = None
        self._AutoRenewFlag = None
        self._PayMode = None
        self._Remark = None
        self._SpecName = None
        self._ExceptionInformation = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceVersion(self):
        return self._InstanceVersion

    @InstanceVersion.setter
    def InstanceVersion(self, InstanceVersion):
        self._InstanceVersion = InstanceVersion

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NodeCount(self):
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def ConfigDisplay(self):
        return self._ConfigDisplay

    @ConfigDisplay.setter
    def ConfigDisplay(self, ConfigDisplay):
        self._ConfigDisplay = ConfigDisplay

    @property
    def MaxTps(self):
        return self._MaxTps

    @MaxTps.setter
    def MaxTps(self, MaxTps):
        self._MaxTps = MaxTps

    @property
    def MaxBandWidth(self):
        return self._MaxBandWidth

    @MaxBandWidth.setter
    def MaxBandWidth(self, MaxBandWidth):
        self._MaxBandWidth = MaxBandWidth

    @property
    def MaxStorage(self):
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def SpecName(self):
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName

    @property
    def ExceptionInformation(self):
        return self._ExceptionInformation

    @ExceptionInformation.setter
    def ExceptionInformation(self, ExceptionInformation):
        self._ExceptionInformation = ExceptionInformation


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceVersion = params.get("InstanceVersion")
        self._Status = params.get("Status")
        self._NodeCount = params.get("NodeCount")
        self._ConfigDisplay = params.get("ConfigDisplay")
        self._MaxTps = params.get("MaxTps")
        self._MaxBandWidth = params.get("MaxBandWidth")
        self._MaxStorage = params.get("MaxStorage")
        self._ExpireTime = params.get("ExpireTime")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._PayMode = params.get("PayMode")
        self._Remark = params.get("Remark")
        self._SpecName = params.get("SpecName")
        self._ExceptionInformation = params.get("ExceptionInformation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReceiveMessageRequest(AbstractModel):
    """ReceiveMessage request structure.

    """

    def __init__(self):
        r"""
        :param _Topic: Name of the topic which receives the message. It is better to be the full path of the topic, such as `tenant/namespace/topic`. If it is not specified, `public/default` will be used by default.
        :type Topic: str
        :param _SubscriptionName: Subscriber name
        :type SubscriptionName: str
        :param _ReceiverQueueSize: Default value: 1000. Messages received by the consumer will first be stored in the `receiverQueueSize` queue to tune the message receiving rate.
        :type ReceiverQueueSize: int
        :param _SubInitialPosition: A parameter used to determine the position where the consumer initially receives messages. Valid values: `Earliest` (default), `Latest`.
        :type SubInitialPosition: str
        :param _MaxNumMessages: This parameter is used to specify the maximum number of received messages in a batch for `BatchReceivePolicy`. The default value is 0, indicating that `BatchReceivePolicy` is disabled.
        :type MaxNumMessages: int
        :param _MaxNumBytes: This parameter is used to specify the maximum body size (in bytes) of received messages in a batch for `BatchReceivePolicy`. The default value is 0, indicating that `BatchReceivePolicy` is disabled.
        :type MaxNumBytes: int
        :param _Timeout: This parameter is used to specify the maximum wait timeout (in milliseconds) for receiving a batch of messages for `BatchReceivePolicy`. The default value is 0, indicating that `BatchReceivePolicy` is disabled.
        :type Timeout: int
        """
        self._Topic = None
        self._SubscriptionName = None
        self._ReceiverQueueSize = None
        self._SubInitialPosition = None
        self._MaxNumMessages = None
        self._MaxNumBytes = None
        self._Timeout = None

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def SubscriptionName(self):
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName

    @property
    def ReceiverQueueSize(self):
        return self._ReceiverQueueSize

    @ReceiverQueueSize.setter
    def ReceiverQueueSize(self, ReceiverQueueSize):
        self._ReceiverQueueSize = ReceiverQueueSize

    @property
    def SubInitialPosition(self):
        return self._SubInitialPosition

    @SubInitialPosition.setter
    def SubInitialPosition(self, SubInitialPosition):
        self._SubInitialPosition = SubInitialPosition

    @property
    def MaxNumMessages(self):
        return self._MaxNumMessages

    @MaxNumMessages.setter
    def MaxNumMessages(self, MaxNumMessages):
        self._MaxNumMessages = MaxNumMessages

    @property
    def MaxNumBytes(self):
        return self._MaxNumBytes

    @MaxNumBytes.setter
    def MaxNumBytes(self, MaxNumBytes):
        self._MaxNumBytes = MaxNumBytes

    @property
    def Timeout(self):
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout


    def _deserialize(self, params):
        self._Topic = params.get("Topic")
        self._SubscriptionName = params.get("SubscriptionName")
        self._ReceiverQueueSize = params.get("ReceiverQueueSize")
        self._SubInitialPosition = params.get("SubInitialPosition")
        self._MaxNumMessages = params.get("MaxNumMessages")
        self._MaxNumBytes = params.get("MaxNumBytes")
        self._Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReceiveMessageResponse(AbstractModel):
    """ReceiveMessage response structure.

    """

    def __init__(self):
        r"""
        :param _MessageID: Unique primary key used to identify the message
        :type MessageID: str
        :param _MessagePayload: Content of the received message
        :type MessagePayload: str
        :param _AckTopic: Provided to the `Ack` API and used to acknowledge messages in the topic
        :type AckTopic: str
        :param _ErrorMsg: Returned error message. If it is an empty string, no error occurred.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _SubName: Returned subscriber name, which will be used when an acknowledgment consumer is created.
Note: this field may return null, indicating that no valid values can be obtained.
        :type SubName: str
        :param _MessageIDList: MessageIDs returned by `BatchReceivePolicy` at a time, which are separated by “###”.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MessageIDList: str
        :param _MessagesPayload: Message contents returned by `BatchReceivePolicy` at a time, which are separated by “###”.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MessagesPayload: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MessageID = None
        self._MessagePayload = None
        self._AckTopic = None
        self._ErrorMsg = None
        self._SubName = None
        self._MessageIDList = None
        self._MessagesPayload = None
        self._RequestId = None

    @property
    def MessageID(self):
        return self._MessageID

    @MessageID.setter
    def MessageID(self, MessageID):
        self._MessageID = MessageID

    @property
    def MessagePayload(self):
        return self._MessagePayload

    @MessagePayload.setter
    def MessagePayload(self, MessagePayload):
        self._MessagePayload = MessagePayload

    @property
    def AckTopic(self):
        return self._AckTopic

    @AckTopic.setter
    def AckTopic(self, AckTopic):
        self._AckTopic = AckTopic

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def SubName(self):
        return self._SubName

    @SubName.setter
    def SubName(self, SubName):
        self._SubName = SubName

    @property
    def MessageIDList(self):
        return self._MessageIDList

    @MessageIDList.setter
    def MessageIDList(self, MessageIDList):
        self._MessageIDList = MessageIDList

    @property
    def MessagesPayload(self):
        return self._MessagesPayload

    @MessagesPayload.setter
    def MessagesPayload(self, MessagesPayload):
        self._MessagesPayload = MessagesPayload

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MessageID = params.get("MessageID")
        self._MessagePayload = params.get("MessagePayload")
        self._AckTopic = params.get("AckTopic")
        self._ErrorMsg = params.get("ErrorMsg")
        self._SubName = params.get("SubName")
        self._MessageIDList = params.get("MessageIDList")
        self._MessagesPayload = params.get("MessagesPayload")
        self._RequestId = params.get("RequestId")


class ResetMsgSubOffsetByTimestampRequest(AbstractModel):
    """ResetMsgSubOffsetByTimestamp request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Namespace name.
        :type EnvironmentId: str
        :param _TopicName: Topic name.
        :type TopicName: str
        :param _Subscription: Subscriber name.
        :type Subscription: str
        :param _ToTimestamp: Timestamp, accurate down to the millisecond.
        :type ToTimestamp: int
        :param _ClusterId: Pulsar cluster ID
        :type ClusterId: str
        """
        self._EnvironmentId = None
        self._TopicName = None
        self._Subscription = None
        self._ToTimestamp = None
        self._ClusterId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Subscription(self):
        return self._Subscription

    @Subscription.setter
    def Subscription(self, Subscription):
        self._Subscription = Subscription

    @property
    def ToTimestamp(self):
        return self._ToTimestamp

    @ToTimestamp.setter
    def ToTimestamp(self, ToTimestamp):
        self._ToTimestamp = ToTimestamp

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._Subscription = params.get("Subscription")
        self._ToTimestamp = params.get("ToTimestamp")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetMsgSubOffsetByTimestampResponse(AbstractModel):
    """ResetMsgSubOffsetByTimestamp response structure.

    """

    def __init__(self):
        r"""
        :param _Result: Result.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: bool
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ResetRocketMQConsumerOffSetRequest(AbstractModel):
    """ResetRocketMQConsumerOffSet request structure.

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID.
        :type ClusterId: str
        :param _NamespaceId: Namespace name.
        :type NamespaceId: str
        :param _GroupId: Consumer group name.
        :type GroupId: str
        :param _Topic: Topic name.
        :type Topic: str
        :param _Type: Reset method. 0: Start from the latest offset; 1: Start from specified time point.
        :type Type: int
        :param _ResetTimestamp: The specified timestamp that has been reset, in milliseconds. This parameter only takes effect when the value of `Type` is `1`.
        :type ResetTimestamp: int
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._GroupId = None
        self._Topic = None
        self._Type = None
        self._ResetTimestamp = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ResetTimestamp(self):
        return self._ResetTimestamp

    @ResetTimestamp.setter
    def ResetTimestamp(self, ResetTimestamp):
        self._ResetTimestamp = ResetTimestamp


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._GroupId = params.get("GroupId")
        self._Topic = params.get("Topic")
        self._Type = params.get("Type")
        self._ResetTimestamp = params.get("ResetTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetRocketMQConsumerOffSetResponse(AbstractModel):
    """ResetRocketMQConsumerOffSet response structure.

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


class RetentionPolicy(AbstractModel):
    """Message retention policy

    """

    def __init__(self):
        r"""
        :param _TimeInMinutes: Message retention period
        :type TimeInMinutes: int
        :param _SizeInMB: Message retention size
        :type SizeInMB: int
        """
        self._TimeInMinutes = None
        self._SizeInMB = None

    @property
    def TimeInMinutes(self):
        return self._TimeInMinutes

    @TimeInMinutes.setter
    def TimeInMinutes(self, TimeInMinutes):
        self._TimeInMinutes = TimeInMinutes

    @property
    def SizeInMB(self):
        return self._SizeInMB

    @SizeInMB.setter
    def SizeInMB(self, SizeInMB):
        self._SizeInMB = SizeInMB


    def _deserialize(self, params):
        self._TimeInMinutes = params.get("TimeInMinutes")
        self._SizeInMB = params.get("SizeInMB")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RewindCmqQueueRequest(AbstractModel):
    """RewindCmqQueue request structure.

    """

    def __init__(self):
        r"""
        :param _QueueName: Queue name, which must be unique under the same account in the same region. It can contain up to 64 letters, digits, and hyphens and must begin with a letter.
        :type QueueName: str
        :param _StartConsumeTime: After this time is configured, the `(Batch)receiveMessage` API will consume the messages received after this timestamp in the order in which they are produced.
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
        


class RewindCmqQueueResponse(AbstractModel):
    """RewindCmqQueue response structure.

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


class RocketMQClusterConfig(AbstractModel):
    """RocketMQ cluster configuration

    """

    def __init__(self):
        r"""
        :param _MaxTpsPerNamespace: Maximum TPS per namespace
        :type MaxTpsPerNamespace: int
        :param _MaxNamespaceNum: Maximum number of namespaces
        :type MaxNamespaceNum: int
        :param _UsedNamespaceNum: Number of used namespaces
        :type UsedNamespaceNum: int
        :param _MaxTopicNum: Maximum number of topics
        :type MaxTopicNum: int
        :param _UsedTopicNum: Number of used topics
        :type UsedTopicNum: int
        :param _MaxGroupNum: Maximum number of groups
        :type MaxGroupNum: int
        :param _UsedGroupNum: Number of used groups
        :type UsedGroupNum: int
        :param _MaxRetentionTime: Maximum message retention period in milliseconds
        :type MaxRetentionTime: int
        :param _MaxLatencyTime: Maximum message delay in milliseconds
        :type MaxLatencyTime: int
        :param _MaxQueuesPerTopic: The maximum number of queues in a single topic
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxQueuesPerTopic: int
        """
        self._MaxTpsPerNamespace = None
        self._MaxNamespaceNum = None
        self._UsedNamespaceNum = None
        self._MaxTopicNum = None
        self._UsedTopicNum = None
        self._MaxGroupNum = None
        self._UsedGroupNum = None
        self._MaxRetentionTime = None
        self._MaxLatencyTime = None
        self._MaxQueuesPerTopic = None

    @property
    def MaxTpsPerNamespace(self):
        return self._MaxTpsPerNamespace

    @MaxTpsPerNamespace.setter
    def MaxTpsPerNamespace(self, MaxTpsPerNamespace):
        self._MaxTpsPerNamespace = MaxTpsPerNamespace

    @property
    def MaxNamespaceNum(self):
        return self._MaxNamespaceNum

    @MaxNamespaceNum.setter
    def MaxNamespaceNum(self, MaxNamespaceNum):
        self._MaxNamespaceNum = MaxNamespaceNum

    @property
    def UsedNamespaceNum(self):
        return self._UsedNamespaceNum

    @UsedNamespaceNum.setter
    def UsedNamespaceNum(self, UsedNamespaceNum):
        self._UsedNamespaceNum = UsedNamespaceNum

    @property
    def MaxTopicNum(self):
        return self._MaxTopicNum

    @MaxTopicNum.setter
    def MaxTopicNum(self, MaxTopicNum):
        self._MaxTopicNum = MaxTopicNum

    @property
    def UsedTopicNum(self):
        return self._UsedTopicNum

    @UsedTopicNum.setter
    def UsedTopicNum(self, UsedTopicNum):
        self._UsedTopicNum = UsedTopicNum

    @property
    def MaxGroupNum(self):
        return self._MaxGroupNum

    @MaxGroupNum.setter
    def MaxGroupNum(self, MaxGroupNum):
        self._MaxGroupNum = MaxGroupNum

    @property
    def UsedGroupNum(self):
        return self._UsedGroupNum

    @UsedGroupNum.setter
    def UsedGroupNum(self, UsedGroupNum):
        self._UsedGroupNum = UsedGroupNum

    @property
    def MaxRetentionTime(self):
        return self._MaxRetentionTime

    @MaxRetentionTime.setter
    def MaxRetentionTime(self, MaxRetentionTime):
        self._MaxRetentionTime = MaxRetentionTime

    @property
    def MaxLatencyTime(self):
        return self._MaxLatencyTime

    @MaxLatencyTime.setter
    def MaxLatencyTime(self, MaxLatencyTime):
        self._MaxLatencyTime = MaxLatencyTime

    @property
    def MaxQueuesPerTopic(self):
        return self._MaxQueuesPerTopic

    @MaxQueuesPerTopic.setter
    def MaxQueuesPerTopic(self, MaxQueuesPerTopic):
        self._MaxQueuesPerTopic = MaxQueuesPerTopic


    def _deserialize(self, params):
        self._MaxTpsPerNamespace = params.get("MaxTpsPerNamespace")
        self._MaxNamespaceNum = params.get("MaxNamespaceNum")
        self._UsedNamespaceNum = params.get("UsedNamespaceNum")
        self._MaxTopicNum = params.get("MaxTopicNum")
        self._UsedTopicNum = params.get("UsedTopicNum")
        self._MaxGroupNum = params.get("MaxGroupNum")
        self._UsedGroupNum = params.get("UsedGroupNum")
        self._MaxRetentionTime = params.get("MaxRetentionTime")
        self._MaxLatencyTime = params.get("MaxLatencyTime")
        self._MaxQueuesPerTopic = params.get("MaxQueuesPerTopic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQClusterDetail(AbstractModel):
    """Details of the tenant’s RocketMQ cluster

    """

    def __init__(self):
        r"""
        :param _Info: Basic cluster information.
        :type Info: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterInfo`
        :param _Config: Cluster configuration information.
        :type Config: :class:`tencentcloud.tdmq.v20200217.models.RocketMQClusterConfig`
        :param _Status: Cluster status. 0: Creating; 1: Normal; 2: Terminating; 3: Deleted; 4. Isolated; 5. Creation failed; 6: Deletion failed.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        """
        self._Info = None
        self._Config = None
        self._Status = None

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        if params.get("Info") is not None:
            self._Info = RocketMQClusterInfo()
            self._Info._deserialize(params.get("Info"))
        if params.get("Config") is not None:
            self._Config = RocketMQClusterConfig()
            self._Config._deserialize(params.get("Config"))
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQClusterInfo(AbstractModel):
    """RocketMQ cluster's basic information

    """

    def __init__(self):
        r"""
        :param _ClusterId: Cluster ID
        :type ClusterId: str
        :param _ClusterName: Cluster name
        :type ClusterName: str
        :param _Region: Region information
        :type Region: str
        :param _CreateTime: Creation time in milliseconds
        :type CreateTime: int
        :param _Remark: Cluster remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param _PublicEndPoint: Public network access address
        :type PublicEndPoint: str
        :param _VpcEndPoint: VPC access address
        :type VpcEndPoint: str
        :param _SupportNamespaceEndpoint: Whether the namespace access point is supported.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SupportNamespaceEndpoint: bool
        :param _Vpcs: VPC Information
Note: This field may return null, indicating that no valid values can be obtained.
        :type Vpcs: list of VpcConfig
        :param _IsVip: Whether it is an exclusive instance
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsVip: bool
        :param _RocketMQFlag: TDMQ for RocketMQ cluster type flag
Note: This field may return null, indicating that no valid values can be obtained.
        :type RocketMQFlag: bool
        :param _Status: Billing status (`1`: Normal; `2`: Service suspended; `3`: Terminated)
Note: This field may return null, indicating that no valid values can be obtained.
        :type Status: int
        :param _IsolateTime: Service suspension time in milliseconds
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsolateTime: int
        :param _HttpPublicEndpoint: HTTP-based public network access address
Note: This field may return null, indicating that no valid values can be obtained.
        :type HttpPublicEndpoint: str
        :param _HttpVpcEndpoint: HTTP-based VPC access address
Note: This field may return null, indicating that no valid values can be obtained.
        :type HttpVpcEndpoint: str
        """
        self._ClusterId = None
        self._ClusterName = None
        self._Region = None
        self._CreateTime = None
        self._Remark = None
        self._PublicEndPoint = None
        self._VpcEndPoint = None
        self._SupportNamespaceEndpoint = None
        self._Vpcs = None
        self._IsVip = None
        self._RocketMQFlag = None
        self._Status = None
        self._IsolateTime = None
        self._HttpPublicEndpoint = None
        self._HttpVpcEndpoint = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PublicEndPoint(self):
        return self._PublicEndPoint

    @PublicEndPoint.setter
    def PublicEndPoint(self, PublicEndPoint):
        self._PublicEndPoint = PublicEndPoint

    @property
    def VpcEndPoint(self):
        return self._VpcEndPoint

    @VpcEndPoint.setter
    def VpcEndPoint(self, VpcEndPoint):
        self._VpcEndPoint = VpcEndPoint

    @property
    def SupportNamespaceEndpoint(self):
        return self._SupportNamespaceEndpoint

    @SupportNamespaceEndpoint.setter
    def SupportNamespaceEndpoint(self, SupportNamespaceEndpoint):
        self._SupportNamespaceEndpoint = SupportNamespaceEndpoint

    @property
    def Vpcs(self):
        return self._Vpcs

    @Vpcs.setter
    def Vpcs(self, Vpcs):
        self._Vpcs = Vpcs

    @property
    def IsVip(self):
        return self._IsVip

    @IsVip.setter
    def IsVip(self, IsVip):
        self._IsVip = IsVip

    @property
    def RocketMQFlag(self):
        return self._RocketMQFlag

    @RocketMQFlag.setter
    def RocketMQFlag(self, RocketMQFlag):
        self._RocketMQFlag = RocketMQFlag

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def IsolateTime(self):
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def HttpPublicEndpoint(self):
        return self._HttpPublicEndpoint

    @HttpPublicEndpoint.setter
    def HttpPublicEndpoint(self, HttpPublicEndpoint):
        self._HttpPublicEndpoint = HttpPublicEndpoint

    @property
    def HttpVpcEndpoint(self):
        return self._HttpVpcEndpoint

    @HttpVpcEndpoint.setter
    def HttpVpcEndpoint(self, HttpVpcEndpoint):
        self._HttpVpcEndpoint = HttpVpcEndpoint


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        self._Region = params.get("Region")
        self._CreateTime = params.get("CreateTime")
        self._Remark = params.get("Remark")
        self._PublicEndPoint = params.get("PublicEndPoint")
        self._VpcEndPoint = params.get("VpcEndPoint")
        self._SupportNamespaceEndpoint = params.get("SupportNamespaceEndpoint")
        if params.get("Vpcs") is not None:
            self._Vpcs = []
            for item in params.get("Vpcs"):
                obj = VpcConfig()
                obj._deserialize(item)
                self._Vpcs.append(obj)
        self._IsVip = params.get("IsVip")
        self._RocketMQFlag = params.get("RocketMQFlag")
        self._Status = params.get("Status")
        self._IsolateTime = params.get("IsolateTime")
        self._HttpPublicEndpoint = params.get("HttpPublicEndpoint")
        self._HttpVpcEndpoint = params.get("HttpVpcEndpoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQClusterRecentStats(AbstractModel):
    """Recent RocketMQ usage

    """

    def __init__(self):
        r"""
        :param _TopicNum: Number of topics
        :type TopicNum: int
        :param _ProducedMsgNum: Number of produced messages
        :type ProducedMsgNum: int
        :param _ConsumedMsgNum: Number of consumed messages
        :type ConsumedMsgNum: int
        :param _AccumulativeMsgNum: Number of retained messages
        :type AccumulativeMsgNum: int
        """
        self._TopicNum = None
        self._ProducedMsgNum = None
        self._ConsumedMsgNum = None
        self._AccumulativeMsgNum = None

    @property
    def TopicNum(self):
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def ProducedMsgNum(self):
        return self._ProducedMsgNum

    @ProducedMsgNum.setter
    def ProducedMsgNum(self, ProducedMsgNum):
        self._ProducedMsgNum = ProducedMsgNum

    @property
    def ConsumedMsgNum(self):
        return self._ConsumedMsgNum

    @ConsumedMsgNum.setter
    def ConsumedMsgNum(self, ConsumedMsgNum):
        self._ConsumedMsgNum = ConsumedMsgNum

    @property
    def AccumulativeMsgNum(self):
        return self._AccumulativeMsgNum

    @AccumulativeMsgNum.setter
    def AccumulativeMsgNum(self, AccumulativeMsgNum):
        self._AccumulativeMsgNum = AccumulativeMsgNum


    def _deserialize(self, params):
        self._TopicNum = params.get("TopicNum")
        self._ProducedMsgNum = params.get("ProducedMsgNum")
        self._ConsumedMsgNum = params.get("ConsumedMsgNum")
        self._AccumulativeMsgNum = params.get("AccumulativeMsgNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQGroup(AbstractModel):
    """RocketMQ consumer group information

    """

    def __init__(self):
        r"""
        :param _Name: Consumer group name.
        :type Name: str
        :param _ConsumerNum: The number of online consumers.
        :type ConsumerNum: int
        :param _TPS: Consumption TPS.
        :type TPS: int
        :param _TotalAccumulative: The total number of heaped messages.
        :type TotalAccumulative: int
        :param _ConsumptionMode: 0: Cluster consumption mode; 1: Broadcast consumption mode; -1: Unknown.
        :type ConsumptionMode: int
        :param _ReadEnabled: Whether to allow consumption.
        :type ReadEnabled: bool
        :param _RetryPartitionNum: The number of partitions in a retry topic.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RetryPartitionNum: int
        :param _CreateTime: Creation time in milliseconds.
        :type CreateTime: int
        :param _UpdateTime: Modification time in milliseconds.
        :type UpdateTime: int
        :param _ClientProtocol: Client protocol.
        :type ClientProtocol: str
        :param _Remark: Description.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param _ConsumerType: Consumer type. Enumerated values: `ACTIVELY` or `PASSIVELY`.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConsumerType: str
        :param _BroadcastEnabled: Whether to enable broadcast consumption.
        :type BroadcastEnabled: bool
        :param _GroupType: Group type
Note: This field may return null, indicating that no valid values can be obtained.
        :type GroupType: str
        :param _RetryMaxTimes: The number of retries
Note: This field may return null, indicating that no valid values can be obtained.
        :type RetryMaxTimes: int
        """
        self._Name = None
        self._ConsumerNum = None
        self._TPS = None
        self._TotalAccumulative = None
        self._ConsumptionMode = None
        self._ReadEnabled = None
        self._RetryPartitionNum = None
        self._CreateTime = None
        self._UpdateTime = None
        self._ClientProtocol = None
        self._Remark = None
        self._ConsumerType = None
        self._BroadcastEnabled = None
        self._GroupType = None
        self._RetryMaxTimes = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ConsumerNum(self):
        return self._ConsumerNum

    @ConsumerNum.setter
    def ConsumerNum(self, ConsumerNum):
        self._ConsumerNum = ConsumerNum

    @property
    def TPS(self):
        return self._TPS

    @TPS.setter
    def TPS(self, TPS):
        self._TPS = TPS

    @property
    def TotalAccumulative(self):
        return self._TotalAccumulative

    @TotalAccumulative.setter
    def TotalAccumulative(self, TotalAccumulative):
        self._TotalAccumulative = TotalAccumulative

    @property
    def ConsumptionMode(self):
        return self._ConsumptionMode

    @ConsumptionMode.setter
    def ConsumptionMode(self, ConsumptionMode):
        self._ConsumptionMode = ConsumptionMode

    @property
    def ReadEnabled(self):
        return self._ReadEnabled

    @ReadEnabled.setter
    def ReadEnabled(self, ReadEnabled):
        self._ReadEnabled = ReadEnabled

    @property
    def RetryPartitionNum(self):
        return self._RetryPartitionNum

    @RetryPartitionNum.setter
    def RetryPartitionNum(self, RetryPartitionNum):
        self._RetryPartitionNum = RetryPartitionNum

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ClientProtocol(self):
        return self._ClientProtocol

    @ClientProtocol.setter
    def ClientProtocol(self, ClientProtocol):
        self._ClientProtocol = ClientProtocol

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ConsumerType(self):
        return self._ConsumerType

    @ConsumerType.setter
    def ConsumerType(self, ConsumerType):
        self._ConsumerType = ConsumerType

    @property
    def BroadcastEnabled(self):
        return self._BroadcastEnabled

    @BroadcastEnabled.setter
    def BroadcastEnabled(self, BroadcastEnabled):
        self._BroadcastEnabled = BroadcastEnabled

    @property
    def GroupType(self):
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def RetryMaxTimes(self):
        return self._RetryMaxTimes

    @RetryMaxTimes.setter
    def RetryMaxTimes(self, RetryMaxTimes):
        self._RetryMaxTimes = RetryMaxTimes


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ConsumerNum = params.get("ConsumerNum")
        self._TPS = params.get("TPS")
        self._TotalAccumulative = params.get("TotalAccumulative")
        self._ConsumptionMode = params.get("ConsumptionMode")
        self._ReadEnabled = params.get("ReadEnabled")
        self._RetryPartitionNum = params.get("RetryPartitionNum")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ClientProtocol = params.get("ClientProtocol")
        self._Remark = params.get("Remark")
        self._ConsumerType = params.get("ConsumerType")
        self._BroadcastEnabled = params.get("BroadcastEnabled")
        self._GroupType = params.get("GroupType")
        self._RetryMaxTimes = params.get("RetryMaxTimes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQInstanceConfig(AbstractModel):
    """Instance configurations of a TDMQ for RocketMQ exclusive cluster

    """

    def __init__(self):
        r"""
        :param _MaxTpsPerNamespace: Maximum TPS per namespace
        :type MaxTpsPerNamespace: int
        :param _MaxNamespaceNum: Maximum number of namespaces
        :type MaxNamespaceNum: int
        :param _UsedNamespaceNum: Number of used namespaces
        :type UsedNamespaceNum: int
        :param _MaxTopicNum: Maximum number of topics
        :type MaxTopicNum: int
        :param _UsedTopicNum: Number of used topics
        :type UsedTopicNum: int
        :param _MaxGroupNum: Maximum number of groups
        :type MaxGroupNum: int
        :param _UsedGroupNum: Number of used groups
        :type UsedGroupNum: int
        :param _ConfigDisplay: Cluster type
        :type ConfigDisplay: str
        :param _NodeCount: Number of nodes in the cluster
        :type NodeCount: int
        :param _NodeDistribution: Node distribution
        :type NodeDistribution: list of InstanceNodeDistribution
        :param _TopicDistribution: Topic distribution
        :type TopicDistribution: list of RocketMQTopicDistribution
        :param _MaxQueuesPerTopic: 
        :type MaxQueuesPerTopic: int
        """
        self._MaxTpsPerNamespace = None
        self._MaxNamespaceNum = None
        self._UsedNamespaceNum = None
        self._MaxTopicNum = None
        self._UsedTopicNum = None
        self._MaxGroupNum = None
        self._UsedGroupNum = None
        self._ConfigDisplay = None
        self._NodeCount = None
        self._NodeDistribution = None
        self._TopicDistribution = None
        self._MaxQueuesPerTopic = None

    @property
    def MaxTpsPerNamespace(self):
        return self._MaxTpsPerNamespace

    @MaxTpsPerNamespace.setter
    def MaxTpsPerNamespace(self, MaxTpsPerNamespace):
        self._MaxTpsPerNamespace = MaxTpsPerNamespace

    @property
    def MaxNamespaceNum(self):
        return self._MaxNamespaceNum

    @MaxNamespaceNum.setter
    def MaxNamespaceNum(self, MaxNamespaceNum):
        self._MaxNamespaceNum = MaxNamespaceNum

    @property
    def UsedNamespaceNum(self):
        return self._UsedNamespaceNum

    @UsedNamespaceNum.setter
    def UsedNamespaceNum(self, UsedNamespaceNum):
        self._UsedNamespaceNum = UsedNamespaceNum

    @property
    def MaxTopicNum(self):
        return self._MaxTopicNum

    @MaxTopicNum.setter
    def MaxTopicNum(self, MaxTopicNum):
        self._MaxTopicNum = MaxTopicNum

    @property
    def UsedTopicNum(self):
        return self._UsedTopicNum

    @UsedTopicNum.setter
    def UsedTopicNum(self, UsedTopicNum):
        self._UsedTopicNum = UsedTopicNum

    @property
    def MaxGroupNum(self):
        return self._MaxGroupNum

    @MaxGroupNum.setter
    def MaxGroupNum(self, MaxGroupNum):
        self._MaxGroupNum = MaxGroupNum

    @property
    def UsedGroupNum(self):
        return self._UsedGroupNum

    @UsedGroupNum.setter
    def UsedGroupNum(self, UsedGroupNum):
        self._UsedGroupNum = UsedGroupNum

    @property
    def ConfigDisplay(self):
        return self._ConfigDisplay

    @ConfigDisplay.setter
    def ConfigDisplay(self, ConfigDisplay):
        self._ConfigDisplay = ConfigDisplay

    @property
    def NodeCount(self):
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def NodeDistribution(self):
        return self._NodeDistribution

    @NodeDistribution.setter
    def NodeDistribution(self, NodeDistribution):
        self._NodeDistribution = NodeDistribution

    @property
    def TopicDistribution(self):
        return self._TopicDistribution

    @TopicDistribution.setter
    def TopicDistribution(self, TopicDistribution):
        self._TopicDistribution = TopicDistribution

    @property
    def MaxQueuesPerTopic(self):
        return self._MaxQueuesPerTopic

    @MaxQueuesPerTopic.setter
    def MaxQueuesPerTopic(self, MaxQueuesPerTopic):
        self._MaxQueuesPerTopic = MaxQueuesPerTopic


    def _deserialize(self, params):
        self._MaxTpsPerNamespace = params.get("MaxTpsPerNamespace")
        self._MaxNamespaceNum = params.get("MaxNamespaceNum")
        self._UsedNamespaceNum = params.get("UsedNamespaceNum")
        self._MaxTopicNum = params.get("MaxTopicNum")
        self._UsedTopicNum = params.get("UsedTopicNum")
        self._MaxGroupNum = params.get("MaxGroupNum")
        self._UsedGroupNum = params.get("UsedGroupNum")
        self._ConfigDisplay = params.get("ConfigDisplay")
        self._NodeCount = params.get("NodeCount")
        if params.get("NodeDistribution") is not None:
            self._NodeDistribution = []
            for item in params.get("NodeDistribution"):
                obj = InstanceNodeDistribution()
                obj._deserialize(item)
                self._NodeDistribution.append(obj)
        if params.get("TopicDistribution") is not None:
            self._TopicDistribution = []
            for item in params.get("TopicDistribution"):
                obj = RocketMQTopicDistribution()
                obj._deserialize(item)
                self._TopicDistribution.append(obj)
        self._MaxQueuesPerTopic = params.get("MaxQueuesPerTopic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQNamespace(AbstractModel):
    """RocketMQ namespace information

    """

    def __init__(self):
        r"""
        :param _NamespaceId: Namespace name, which can contain 3–64 letters, digits, hyphens, and underscores.
        :type NamespaceId: str
        :param _Ttl: Retention period for unconsumed messages in milliseconds. Valid range: 60 seconds–15 days.
        :type Ttl: int
        :param _RetentionTime: Retention period for persistently stored messages in milliseconds.
        :type RetentionTime: int
        :param _Remark: Description.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param _PublicEndpoint: Public network access point address.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PublicEndpoint: str
        :param _VpcEndpoint: VPC access point address.
Note: This field may return null, indicating that no valid values can be obtained.
        :type VpcEndpoint: str
        """
        self._NamespaceId = None
        self._Ttl = None
        self._RetentionTime = None
        self._Remark = None
        self._PublicEndpoint = None
        self._VpcEndpoint = None

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def Ttl(self):
        return self._Ttl

    @Ttl.setter
    def Ttl(self, Ttl):
        self._Ttl = Ttl

    @property
    def RetentionTime(self):
        return self._RetentionTime

    @RetentionTime.setter
    def RetentionTime(self, RetentionTime):
        self._RetentionTime = RetentionTime

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PublicEndpoint(self):
        return self._PublicEndpoint

    @PublicEndpoint.setter
    def PublicEndpoint(self, PublicEndpoint):
        self._PublicEndpoint = PublicEndpoint

    @property
    def VpcEndpoint(self):
        return self._VpcEndpoint

    @VpcEndpoint.setter
    def VpcEndpoint(self, VpcEndpoint):
        self._VpcEndpoint = VpcEndpoint


    def _deserialize(self, params):
        self._NamespaceId = params.get("NamespaceId")
        self._Ttl = params.get("Ttl")
        self._RetentionTime = params.get("RetentionTime")
        self._Remark = params.get("Remark")
        self._PublicEndpoint = params.get("PublicEndpoint")
        self._VpcEndpoint = params.get("VpcEndpoint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQTopic(AbstractModel):
    """RocketMQ topic information

    """

    def __init__(self):
        r"""
        :param _Name: Topic name.
        :type Name: str
        :param _Type: Topic type. Enumerated values: `Normal`, `GlobalOrder`, `PartitionedOrder`, `Transaction`, `Retry`, and `DeadLetter`.
        :type Type: str
        :param _GroupNum: The number of subscription groups
        :type GroupNum: int
        :param _Remark: Description.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param _PartitionNum: The number of read/write partitions.
        :type PartitionNum: int
        :param _CreateTime: Creation time in milliseconds.
        :type CreateTime: int
        :param _UpdateTime: Creation time in milliseconds.
        :type UpdateTime: int
        """
        self._Name = None
        self._Type = None
        self._GroupNum = None
        self._Remark = None
        self._PartitionNum = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def GroupNum(self):
        return self._GroupNum

    @GroupNum.setter
    def GroupNum(self, GroupNum):
        self._GroupNum = GroupNum

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PartitionNum(self):
        return self._PartitionNum

    @PartitionNum.setter
    def PartitionNum(self, PartitionNum):
        self._PartitionNum = PartitionNum

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._GroupNum = params.get("GroupNum")
        self._Remark = params.get("Remark")
        self._PartitionNum = params.get("PartitionNum")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQTopicDistribution(AbstractModel):
    """TDMQ for RocketMQ topic distribution

    """

    def __init__(self):
        r"""
        :param _TopicType: Topic type
        :type TopicType: str
        :param _Count: Number of topics
        :type Count: int
        """
        self._TopicType = None
        self._Count = None

    @property
    def TopicType(self):
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._TopicType = params.get("TopicType")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RocketMQVipInstance(AbstractModel):
    """Information of TDMQ for RocketMQ exclusive instances

    """

    def __init__(self):
        r"""
        :param _InstanceId: Instance ID
        :type InstanceId: str
        :param _InstanceName: Instance name
        :type InstanceName: str
        :param _InstanceVersion: Instance version
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceVersion: str
        :param _Status: Instance status. Valid values: `0` (Creating), `1` (Normal), `2` (Isolated), `3` (Terminated), `4` (Abnormal), `5` (Delivery failed).
        :type Status: int
        :param _NodeCount: Number of nodes
        :type NodeCount: int
        :param _ConfigDisplay: Instance specification name
        :type ConfigDisplay: str
        :param _MaxTps: Peak TPS
        :type MaxTps: int
        :param _MaxBandWidth: Peak bandwidth in Mbps
        :type MaxBandWidth: int
        :param _MaxStorage: Storage capacity in GB
        :type MaxStorage: int
        :param _ExpireTime: Instance expiration time in milliseconds
        :type ExpireTime: int
        :param _AutoRenewFlag: Renewal mode. Valid values: `0` (Manual renewal, which is the default mode), `1` (Auto-renewal), `2` (Manual renewal, which is specified by users).
        :type AutoRenewFlag: int
        :param _PayMode: Payment mode. 0: Postpaid; 1: Prepaid.
        :type PayMode: int
        :param _Remark: Remarks
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param _SpecName: Instance specification ID
        :type SpecName: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceVersion = None
        self._Status = None
        self._NodeCount = None
        self._ConfigDisplay = None
        self._MaxTps = None
        self._MaxBandWidth = None
        self._MaxStorage = None
        self._ExpireTime = None
        self._AutoRenewFlag = None
        self._PayMode = None
        self._Remark = None
        self._SpecName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceVersion(self):
        return self._InstanceVersion

    @InstanceVersion.setter
    def InstanceVersion(self, InstanceVersion):
        self._InstanceVersion = InstanceVersion

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def NodeCount(self):
        return self._NodeCount

    @NodeCount.setter
    def NodeCount(self, NodeCount):
        self._NodeCount = NodeCount

    @property
    def ConfigDisplay(self):
        return self._ConfigDisplay

    @ConfigDisplay.setter
    def ConfigDisplay(self, ConfigDisplay):
        self._ConfigDisplay = ConfigDisplay

    @property
    def MaxTps(self):
        return self._MaxTps

    @MaxTps.setter
    def MaxTps(self, MaxTps):
        self._MaxTps = MaxTps

    @property
    def MaxBandWidth(self):
        return self._MaxBandWidth

    @MaxBandWidth.setter
    def MaxBandWidth(self, MaxBandWidth):
        self._MaxBandWidth = MaxBandWidth

    @property
    def MaxStorage(self):
        return self._MaxStorage

    @MaxStorage.setter
    def MaxStorage(self, MaxStorage):
        self._MaxStorage = MaxStorage

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def SpecName(self):
        return self._SpecName

    @SpecName.setter
    def SpecName(self, SpecName):
        self._SpecName = SpecName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceVersion = params.get("InstanceVersion")
        self._Status = params.get("Status")
        self._NodeCount = params.get("NodeCount")
        self._ConfigDisplay = params.get("ConfigDisplay")
        self._MaxTps = params.get("MaxTps")
        self._MaxBandWidth = params.get("MaxBandWidth")
        self._MaxStorage = params.get("MaxStorage")
        self._ExpireTime = params.get("ExpireTime")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._PayMode = params.get("PayMode")
        self._Remark = params.get("Remark")
        self._SpecName = params.get("SpecName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Role(AbstractModel):
    """Role instance

    """

    def __init__(self):
        r"""
        :param _RoleName: Role name.
        :type RoleName: str
        :param _Token: Value of the role token.
        :type Token: str
        :param _Remark: Remarks.
        :type Remark: str
        :param _CreateTime: Creation time.
        :type CreateTime: str
        :param _UpdateTime: Update time.
        :type UpdateTime: str
        """
        self._RoleName = None
        self._Token = None
        self._Remark = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def RoleName(self):
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._Token = params.get("Token")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendBatchMessagesRequest(AbstractModel):
    """SendBatchMessages request structure.

    """

    def __init__(self):
        r"""
        :param _Topic: Name of the topic to which to send the message. It is better to be the full path of the topic, such as `tenant/namespace/topic`. If it is not specified, `public/default` will be used by default.
        :type Topic: str
        :param _Payload: Content of the message to be sent
        :type Payload: str
        :param _StringToken: String-Type token, which is optional and will be automatically obtained by the system.
        :type StringToken: str
        :param _ProducerName: Producer name, which must be globally unique. If it is not configured, the system will automatically generate one.
        :type ProducerName: str
        :param _SendTimeout: Message sending timeout period in seconds. Default value: 30s
        :type SendTimeout: int
        :param _MaxPendingMessages: Maximum number of produced messages which can be cached in the memory. Default value: 1000
        :type MaxPendingMessages: int
        :param _BatchingMaxMessages: Maximum number of messages in each batch. Default value: 1000 messages/batch
        :type BatchingMaxMessages: int
        :param _BatchingMaxPublishDelay: Maximum wait time for each batch, after which the batch will be sent no matter whether the specified number or size of messages in the batch is reached. Default value: 10 ms
        :type BatchingMaxPublishDelay: int
        :param _BatchingMaxBytes: Maximum allowed size of messages in each batch. Default value: 128 KB
        :type BatchingMaxBytes: int
        """
        self._Topic = None
        self._Payload = None
        self._StringToken = None
        self._ProducerName = None
        self._SendTimeout = None
        self._MaxPendingMessages = None
        self._BatchingMaxMessages = None
        self._BatchingMaxPublishDelay = None
        self._BatchingMaxBytes = None

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Payload(self):
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def StringToken(self):
        return self._StringToken

    @StringToken.setter
    def StringToken(self, StringToken):
        self._StringToken = StringToken

    @property
    def ProducerName(self):
        return self._ProducerName

    @ProducerName.setter
    def ProducerName(self, ProducerName):
        self._ProducerName = ProducerName

    @property
    def SendTimeout(self):
        return self._SendTimeout

    @SendTimeout.setter
    def SendTimeout(self, SendTimeout):
        self._SendTimeout = SendTimeout

    @property
    def MaxPendingMessages(self):
        return self._MaxPendingMessages

    @MaxPendingMessages.setter
    def MaxPendingMessages(self, MaxPendingMessages):
        self._MaxPendingMessages = MaxPendingMessages

    @property
    def BatchingMaxMessages(self):
        return self._BatchingMaxMessages

    @BatchingMaxMessages.setter
    def BatchingMaxMessages(self, BatchingMaxMessages):
        self._BatchingMaxMessages = BatchingMaxMessages

    @property
    def BatchingMaxPublishDelay(self):
        return self._BatchingMaxPublishDelay

    @BatchingMaxPublishDelay.setter
    def BatchingMaxPublishDelay(self, BatchingMaxPublishDelay):
        self._BatchingMaxPublishDelay = BatchingMaxPublishDelay

    @property
    def BatchingMaxBytes(self):
        return self._BatchingMaxBytes

    @BatchingMaxBytes.setter
    def BatchingMaxBytes(self, BatchingMaxBytes):
        self._BatchingMaxBytes = BatchingMaxBytes


    def _deserialize(self, params):
        self._Topic = params.get("Topic")
        self._Payload = params.get("Payload")
        self._StringToken = params.get("StringToken")
        self._ProducerName = params.get("ProducerName")
        self._SendTimeout = params.get("SendTimeout")
        self._MaxPendingMessages = params.get("MaxPendingMessages")
        self._BatchingMaxMessages = params.get("BatchingMaxMessages")
        self._BatchingMaxPublishDelay = params.get("BatchingMaxPublishDelay")
        self._BatchingMaxBytes = params.get("BatchingMaxBytes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendBatchMessagesResponse(AbstractModel):
    """SendBatchMessages response structure.

    """

    def __init__(self):
        r"""
        :param _MessageId: Unique message ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type MessageId: str
        :param _ErrorMsg: Error message. If an empty string is returned, no error occurred.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MessageId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def MessageId(self):
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MessageId = params.get("MessageId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class SendCmqMsgRequest(AbstractModel):
    """SendCmqMsg request structure.

    """

    def __init__(self):
        r"""
        :param _QueueName: Queue name
        :type QueueName: str
        :param _MsgContent: Message content
        :type MsgContent: str
        :param _DelaySeconds: Delay time
        :type DelaySeconds: int
        """
        self._QueueName = None
        self._MsgContent = None
        self._DelaySeconds = None

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def MsgContent(self):
        return self._MsgContent

    @MsgContent.setter
    def MsgContent(self, MsgContent):
        self._MsgContent = MsgContent

    @property
    def DelaySeconds(self):
        return self._DelaySeconds

    @DelaySeconds.setter
    def DelaySeconds(self, DelaySeconds):
        self._DelaySeconds = DelaySeconds


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        self._MsgContent = params.get("MsgContent")
        self._DelaySeconds = params.get("DelaySeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendCmqMsgResponse(AbstractModel):
    """SendCmqMsg response structure.

    """

    def __init__(self):
        r"""
        :param _Result: `true` indicates that the sending is successful
        :type Result: bool
        :param _MsgId: Message ID
        :type MsgId: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._Result = None
        self._MsgId = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def MsgId(self):
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._MsgId = params.get("MsgId")
        self._RequestId = params.get("RequestId")


class SendMessagesRequest(AbstractModel):
    """SendMessages request structure.

    """

    def __init__(self):
        r"""
        :param _Topic: Name of the topic to which to send the message. It is better to be the full path of the topic, such as `tenant/namespace/topic`. If it is not specified, `public/default` will be used by default.
        :type Topic: str
        :param _Payload: Content of the message to be sent
        :type Payload: str
        :param _StringToken: Token used for authentication, which is optional and will be automatically obtained by the system.
        :type StringToken: str
        :param _ProducerName: Producer name, which is randomly generated and must be globally unique. If you set the producer name manually, the producer may fail to be created, causing message sending failure.
This parameter is used only when a specific producer is allowed to produce messages. It won’t be used in most cases.
        :type ProducerName: str
        :param _SendTimeout: Message sending timeout period, which is 30s by default.
        :type SendTimeout: int
        :param _MaxPendingMessages: Maximum number of produced messages which can be cached in the memory. Default value: 1000
        :type MaxPendingMessages: int
        """
        self._Topic = None
        self._Payload = None
        self._StringToken = None
        self._ProducerName = None
        self._SendTimeout = None
        self._MaxPendingMessages = None

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Payload(self):
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def StringToken(self):
        return self._StringToken

    @StringToken.setter
    def StringToken(self, StringToken):
        self._StringToken = StringToken

    @property
    def ProducerName(self):
        return self._ProducerName

    @ProducerName.setter
    def ProducerName(self, ProducerName):
        self._ProducerName = ProducerName

    @property
    def SendTimeout(self):
        return self._SendTimeout

    @SendTimeout.setter
    def SendTimeout(self, SendTimeout):
        self._SendTimeout = SendTimeout

    @property
    def MaxPendingMessages(self):
        return self._MaxPendingMessages

    @MaxPendingMessages.setter
    def MaxPendingMessages(self, MaxPendingMessages):
        self._MaxPendingMessages = MaxPendingMessages


    def _deserialize(self, params):
        self._Topic = params.get("Topic")
        self._Payload = params.get("Payload")
        self._StringToken = params.get("StringToken")
        self._ProducerName = params.get("ProducerName")
        self._SendTimeout = params.get("SendTimeout")
        self._MaxPendingMessages = params.get("MaxPendingMessages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMessagesResponse(AbstractModel):
    """SendMessages response structure.

    """

    def __init__(self):
        r"""
        :param _MessageId: messageID, which must be globally unique and is the metadata information used to identify the message.
Note: this field may return null, indicating that no valid values can be obtained.
        :type MessageId: str
        :param _ErrorMsg: Returned error message. If an empty string is returned, no error occurred.
Note: this field may return null, indicating that no valid values can be obtained.
        :type ErrorMsg: str
        :param _RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self._MessageId = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def MessageId(self):
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MessageId = params.get("MessageId")
        self._ErrorMsg = params.get("ErrorMsg")
        self._RequestId = params.get("RequestId")


class SendMsgRequest(AbstractModel):
    """SendMsg request structure.

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param _TopicName: Topic name. If the topic is a partitioned topic, you need to specify the partition; otherwise, messages will be sent to partition 0 by default, such as `my_topic-partition-0`.
        :type TopicName: str
        :param _MsgContent: Message content, which cannot be empty and can contain up to 5,242,880 bytes.
        :type MsgContent: str
        :param _ClusterId: Pulsar cluster ID
        :type ClusterId: str
        """
        self._EnvironmentId = None
        self._TopicName = None
        self._MsgContent = None
        self._ClusterId = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def MsgContent(self):
        return self._MsgContent

    @MsgContent.setter
    def MsgContent(self, MsgContent):
        self._MsgContent = MsgContent

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._MsgContent = params.get("MsgContent")
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMsgResponse(AbstractModel):
    """SendMsg response structure.

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


class Sort(AbstractModel):
    """Sort by field

    """

    def __init__(self):
        r"""
        :param _Name: Sorting field.
        :type Name: str
        :param _Order: Ascending order: `ASC`; descending order: `DESC`.
        :type Order: str
        """
        self._Name = None
        self._Order = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Subscription(AbstractModel):
    """Subscriber

    """

    def __init__(self):
        r"""
        :param _TopicName: Topic name.
        :type TopicName: str
        :param _EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param _ConnectedSince: The time when the consumer started connecting.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ConnectedSince: str
        :param _ConsumerAddr: Consumer address.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConsumerAddr: str
        :param _ConsumerCount: The number of consumers.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConsumerCount: str
        :param _ConsumerName: Consumer name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConsumerName: str
        :param _MsgBacklog: The number of heaped messages.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MsgBacklog: str
        :param _MsgRateExpired: Percentage of messages under this subscription that were discarded but not sent after TTL.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MsgRateExpired: str
        :param _MsgRateOut: The total number of messages delivered by the consumer per second.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MsgRateOut: str
        :param _MsgThroughputOut: The size (in bytes) of messages consumed by the consumer per second.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MsgThroughputOut: str
        :param _SubscriptionName: Subscription name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubscriptionName: str
        :param _ConsumerSets: Set of consumers.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConsumerSets: list of Consumer
        :param _IsOnline: Whether the consumer is online.
Note: This field may return null, indicating that no valid values can be obtained.
        :type IsOnline: bool
        :param _ConsumersScheduleSets: Set of consumption progress information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConsumersScheduleSets: list of ConsumersSchedule
        :param _Remark: Remarks.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param _CreateTime: Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _UpdateTime: Last modified.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param _SubType: Subscription type. Valid values: `Exclusive`, `Shared`, `Failover`, and `Key_Shared`. An empty string or `NULL`: Unknown.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubType: str
        :param _BlockedSubscriptionOnUnackedMsgs: Whether messages are blocked as the limit of unacknowledged messages has been reached.
Note: This field may return null, indicating that no valid values can be obtained.
        :type BlockedSubscriptionOnUnackedMsgs: bool
        :param _MaxUnackedMsgNum: The maximum number of unacknowledged messages.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MaxUnackedMsgNum: int
        """
        self._TopicName = None
        self._EnvironmentId = None
        self._ConnectedSince = None
        self._ConsumerAddr = None
        self._ConsumerCount = None
        self._ConsumerName = None
        self._MsgBacklog = None
        self._MsgRateExpired = None
        self._MsgRateOut = None
        self._MsgThroughputOut = None
        self._SubscriptionName = None
        self._ConsumerSets = None
        self._IsOnline = None
        self._ConsumersScheduleSets = None
        self._Remark = None
        self._CreateTime = None
        self._UpdateTime = None
        self._SubType = None
        self._BlockedSubscriptionOnUnackedMsgs = None
        self._MaxUnackedMsgNum = None

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def ConnectedSince(self):
        return self._ConnectedSince

    @ConnectedSince.setter
    def ConnectedSince(self, ConnectedSince):
        self._ConnectedSince = ConnectedSince

    @property
    def ConsumerAddr(self):
        return self._ConsumerAddr

    @ConsumerAddr.setter
    def ConsumerAddr(self, ConsumerAddr):
        self._ConsumerAddr = ConsumerAddr

    @property
    def ConsumerCount(self):
        return self._ConsumerCount

    @ConsumerCount.setter
    def ConsumerCount(self, ConsumerCount):
        self._ConsumerCount = ConsumerCount

    @property
    def ConsumerName(self):
        return self._ConsumerName

    @ConsumerName.setter
    def ConsumerName(self, ConsumerName):
        self._ConsumerName = ConsumerName

    @property
    def MsgBacklog(self):
        return self._MsgBacklog

    @MsgBacklog.setter
    def MsgBacklog(self, MsgBacklog):
        self._MsgBacklog = MsgBacklog

    @property
    def MsgRateExpired(self):
        return self._MsgRateExpired

    @MsgRateExpired.setter
    def MsgRateExpired(self, MsgRateExpired):
        self._MsgRateExpired = MsgRateExpired

    @property
    def MsgRateOut(self):
        return self._MsgRateOut

    @MsgRateOut.setter
    def MsgRateOut(self, MsgRateOut):
        self._MsgRateOut = MsgRateOut

    @property
    def MsgThroughputOut(self):
        return self._MsgThroughputOut

    @MsgThroughputOut.setter
    def MsgThroughputOut(self, MsgThroughputOut):
        self._MsgThroughputOut = MsgThroughputOut

    @property
    def SubscriptionName(self):
        return self._SubscriptionName

    @SubscriptionName.setter
    def SubscriptionName(self, SubscriptionName):
        self._SubscriptionName = SubscriptionName

    @property
    def ConsumerSets(self):
        return self._ConsumerSets

    @ConsumerSets.setter
    def ConsumerSets(self, ConsumerSets):
        self._ConsumerSets = ConsumerSets

    @property
    def IsOnline(self):
        return self._IsOnline

    @IsOnline.setter
    def IsOnline(self, IsOnline):
        self._IsOnline = IsOnline

    @property
    def ConsumersScheduleSets(self):
        return self._ConsumersScheduleSets

    @ConsumersScheduleSets.setter
    def ConsumersScheduleSets(self, ConsumersScheduleSets):
        self._ConsumersScheduleSets = ConsumersScheduleSets

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def SubType(self):
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def BlockedSubscriptionOnUnackedMsgs(self):
        return self._BlockedSubscriptionOnUnackedMsgs

    @BlockedSubscriptionOnUnackedMsgs.setter
    def BlockedSubscriptionOnUnackedMsgs(self, BlockedSubscriptionOnUnackedMsgs):
        self._BlockedSubscriptionOnUnackedMsgs = BlockedSubscriptionOnUnackedMsgs

    @property
    def MaxUnackedMsgNum(self):
        return self._MaxUnackedMsgNum

    @MaxUnackedMsgNum.setter
    def MaxUnackedMsgNum(self, MaxUnackedMsgNum):
        self._MaxUnackedMsgNum = MaxUnackedMsgNum


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._EnvironmentId = params.get("EnvironmentId")
        self._ConnectedSince = params.get("ConnectedSince")
        self._ConsumerAddr = params.get("ConsumerAddr")
        self._ConsumerCount = params.get("ConsumerCount")
        self._ConsumerName = params.get("ConsumerName")
        self._MsgBacklog = params.get("MsgBacklog")
        self._MsgRateExpired = params.get("MsgRateExpired")
        self._MsgRateOut = params.get("MsgRateOut")
        self._MsgThroughputOut = params.get("MsgThroughputOut")
        self._SubscriptionName = params.get("SubscriptionName")
        if params.get("ConsumerSets") is not None:
            self._ConsumerSets = []
            for item in params.get("ConsumerSets"):
                obj = Consumer()
                obj._deserialize(item)
                self._ConsumerSets.append(obj)
        self._IsOnline = params.get("IsOnline")
        if params.get("ConsumersScheduleSets") is not None:
            self._ConsumersScheduleSets = []
            for item in params.get("ConsumersScheduleSets"):
                obj = ConsumersSchedule()
                obj._deserialize(item)
                self._ConsumersScheduleSets.append(obj)
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._SubType = params.get("SubType")
        self._BlockedSubscriptionOnUnackedMsgs = params.get("BlockedSubscriptionOnUnackedMsgs")
        self._MaxUnackedMsgNum = params.get("MaxUnackedMsgNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscriptionTopic(AbstractModel):
    """Subscription

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param _TopicName: Topic name.
        :type TopicName: str
        :param _SubscriptionName: Subscription name.
        :type SubscriptionName: str
        """
        self._EnvironmentId = None
        self._TopicName = None
        self._SubscriptionName = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

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
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._SubscriptionName = params.get("SubscriptionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Type of the tag key/value

    """

    def __init__(self):
        r"""
        :param _TagKey: Value of the tag key
        :type TagKey: str
        :param _TagValue: Value of the tag value
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
        


class Topic(AbstractModel):
    """Topic instance

    """

    def __init__(self):
        r"""
        :param _AverageMsgSize: Average size of the messages published in the last interval in bytes.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AverageMsgSize: str
        :param _ConsumerCount: The number of consumers.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConsumerCount: str
        :param _LastConfirmedEntry: The total number of recorded messages.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastConfirmedEntry: str
        :param _LastLedgerCreatedTimestamp: Time when the last ledger was created.
Note: This field may return null, indicating that no valid values can be obtained.
        :type LastLedgerCreatedTimestamp: str
        :param _MsgRateIn: The number of messages published by local and replicated publishers per second.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MsgRateIn: str
        :param _MsgRateOut: The total number of messages delivered by local and replicated consumers per second.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MsgRateOut: str
        :param _MsgThroughputIn: The size (in bytes) of messages published by local and replicated publishers per second.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MsgThroughputIn: str
        :param _MsgThroughputOut: The size (in bytes) of messages delivered by local and replicated consumers per second.
Note: This field may return null, indicating that no valid values can be obtained.
        :type MsgThroughputOut: str
        :param _NumberOfEntries: The total number of recorded messages.
Note: This field may return null, indicating that no valid values can be obtained.
        :type NumberOfEntries: str
        :param _Partitions: Partition count ≤ 0: there are no subpartitions in the topic.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Partitions: int
        :param _ProducerCount: The number of producers.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProducerCount: str
        :param _TotalSize: The size of all stored messages in bytes.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TotalSize: str
        :param _SubTopicSets: Subpartitions in a partitioned topic.
Note: This field may return null, indicating that no valid values can be obtained.
        :type SubTopicSets: list of PartitionsTopic
        :param _TopicType: Topic type description:
0: General message;
1: Globally sequential message;
2: Partitionally sequential message;
3: Retry letter topic;
4: Dead letter topic;
5: Transaction message.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TopicType: int
        :param _EnvironmentId: Environment (namespace) name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type EnvironmentId: str
        :param _TopicName: Topic name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type TopicName: str
        :param _Remark: Remarks (up to 128 characters).
Note: This field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        :param _CreateTime: Creation time.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreateTime: str
        :param _UpdateTime: Last modified.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UpdateTime: str
        :param _ProducerLimit: The maximum number of producers.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ProducerLimit: str
        :param _ConsumerLimit: The maximum number of consumers.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ConsumerLimit: str
        :param _PulsarTopicType: `0`: Non-persistent and non-partitioned
`1`: Non-persistent and partitioned
`2`: Persistent and non-partitioned
`3`: Persistent and partitioned
Note: This field may return null, indicating that no valid values can be obtained.
        :type PulsarTopicType: int
        """
        self._AverageMsgSize = None
        self._ConsumerCount = None
        self._LastConfirmedEntry = None
        self._LastLedgerCreatedTimestamp = None
        self._MsgRateIn = None
        self._MsgRateOut = None
        self._MsgThroughputIn = None
        self._MsgThroughputOut = None
        self._NumberOfEntries = None
        self._Partitions = None
        self._ProducerCount = None
        self._TotalSize = None
        self._SubTopicSets = None
        self._TopicType = None
        self._EnvironmentId = None
        self._TopicName = None
        self._Remark = None
        self._CreateTime = None
        self._UpdateTime = None
        self._ProducerLimit = None
        self._ConsumerLimit = None
        self._PulsarTopicType = None

    @property
    def AverageMsgSize(self):
        return self._AverageMsgSize

    @AverageMsgSize.setter
    def AverageMsgSize(self, AverageMsgSize):
        self._AverageMsgSize = AverageMsgSize

    @property
    def ConsumerCount(self):
        return self._ConsumerCount

    @ConsumerCount.setter
    def ConsumerCount(self, ConsumerCount):
        self._ConsumerCount = ConsumerCount

    @property
    def LastConfirmedEntry(self):
        return self._LastConfirmedEntry

    @LastConfirmedEntry.setter
    def LastConfirmedEntry(self, LastConfirmedEntry):
        self._LastConfirmedEntry = LastConfirmedEntry

    @property
    def LastLedgerCreatedTimestamp(self):
        return self._LastLedgerCreatedTimestamp

    @LastLedgerCreatedTimestamp.setter
    def LastLedgerCreatedTimestamp(self, LastLedgerCreatedTimestamp):
        self._LastLedgerCreatedTimestamp = LastLedgerCreatedTimestamp

    @property
    def MsgRateIn(self):
        return self._MsgRateIn

    @MsgRateIn.setter
    def MsgRateIn(self, MsgRateIn):
        self._MsgRateIn = MsgRateIn

    @property
    def MsgRateOut(self):
        return self._MsgRateOut

    @MsgRateOut.setter
    def MsgRateOut(self, MsgRateOut):
        self._MsgRateOut = MsgRateOut

    @property
    def MsgThroughputIn(self):
        return self._MsgThroughputIn

    @MsgThroughputIn.setter
    def MsgThroughputIn(self, MsgThroughputIn):
        self._MsgThroughputIn = MsgThroughputIn

    @property
    def MsgThroughputOut(self):
        return self._MsgThroughputOut

    @MsgThroughputOut.setter
    def MsgThroughputOut(self, MsgThroughputOut):
        self._MsgThroughputOut = MsgThroughputOut

    @property
    def NumberOfEntries(self):
        return self._NumberOfEntries

    @NumberOfEntries.setter
    def NumberOfEntries(self, NumberOfEntries):
        self._NumberOfEntries = NumberOfEntries

    @property
    def Partitions(self):
        return self._Partitions

    @Partitions.setter
    def Partitions(self, Partitions):
        self._Partitions = Partitions

    @property
    def ProducerCount(self):
        return self._ProducerCount

    @ProducerCount.setter
    def ProducerCount(self, ProducerCount):
        self._ProducerCount = ProducerCount

    @property
    def TotalSize(self):
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize

    @property
    def SubTopicSets(self):
        return self._SubTopicSets

    @SubTopicSets.setter
    def SubTopicSets(self, SubTopicSets):
        self._SubTopicSets = SubTopicSets

    @property
    def TopicType(self):
        return self._TopicType

    @TopicType.setter
    def TopicType(self, TopicType):
        self._TopicType = TopicType

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ProducerLimit(self):
        return self._ProducerLimit

    @ProducerLimit.setter
    def ProducerLimit(self, ProducerLimit):
        self._ProducerLimit = ProducerLimit

    @property
    def ConsumerLimit(self):
        return self._ConsumerLimit

    @ConsumerLimit.setter
    def ConsumerLimit(self, ConsumerLimit):
        self._ConsumerLimit = ConsumerLimit

    @property
    def PulsarTopicType(self):
        return self._PulsarTopicType

    @PulsarTopicType.setter
    def PulsarTopicType(self, PulsarTopicType):
        self._PulsarTopicType = PulsarTopicType


    def _deserialize(self, params):
        self._AverageMsgSize = params.get("AverageMsgSize")
        self._ConsumerCount = params.get("ConsumerCount")
        self._LastConfirmedEntry = params.get("LastConfirmedEntry")
        self._LastLedgerCreatedTimestamp = params.get("LastLedgerCreatedTimestamp")
        self._MsgRateIn = params.get("MsgRateIn")
        self._MsgRateOut = params.get("MsgRateOut")
        self._MsgThroughputIn = params.get("MsgThroughputIn")
        self._MsgThroughputOut = params.get("MsgThroughputOut")
        self._NumberOfEntries = params.get("NumberOfEntries")
        self._Partitions = params.get("Partitions")
        self._ProducerCount = params.get("ProducerCount")
        self._TotalSize = params.get("TotalSize")
        if params.get("SubTopicSets") is not None:
            self._SubTopicSets = []
            for item in params.get("SubTopicSets"):
                obj = PartitionsTopic()
                obj._deserialize(item)
                self._SubTopicSets.append(obj)
        self._TopicType = params.get("TopicType")
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ProducerLimit = params.get("ProducerLimit")
        self._ConsumerLimit = params.get("ConsumerLimit")
        self._PulsarTopicType = params.get("PulsarTopicType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicRecord(AbstractModel):
    """Topic's key information

    """

    def __init__(self):
        r"""
        :param _EnvironmentId: Environment (namespace) name.
        :type EnvironmentId: str
        :param _TopicName: Topic name.
        :type TopicName: str
        """
        self._EnvironmentId = None
        self._TopicName = None

    @property
    def EnvironmentId(self):
        return self._EnvironmentId

    @EnvironmentId.setter
    def EnvironmentId(self, EnvironmentId):
        self._EnvironmentId = EnvironmentId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._EnvironmentId = params.get("EnvironmentId")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindCmqDeadLetterRequest(AbstractModel):
    """UnbindCmqDeadLetter request structure.

    """

    def __init__(self):
        r"""
        :param _SourceQueueName: Source queue name of dead letter policy. Calling this API will clear the dead letter queue policy of this queue.
        :type SourceQueueName: str
        """
        self._SourceQueueName = None

    @property
    def SourceQueueName(self):
        return self._SourceQueueName

    @SourceQueueName.setter
    def SourceQueueName(self, SourceQueueName):
        self._SourceQueueName = SourceQueueName


    def _deserialize(self, params):
        self._SourceQueueName = params.get("SourceQueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindCmqDeadLetterResponse(AbstractModel):
    """UnbindCmqDeadLetter response structure.

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


class VpcBindRecord(AbstractModel):
    """VPC binding record

    """

    def __init__(self):
        r"""
        :param _UniqueVpcId: Tenant VPC ID
        :type UniqueVpcId: str
        :param _UniqueSubnetId: Tenant VPC subnet ID
        :type UniqueSubnetId: str
        :param _RouterId: Route ID
        :type RouterId: str
        :param _Ip: VPC ID
        :type Ip: str
        :param _Port: VPC port
        :type Port: int
        :param _Remark: Remarks (up to 128 characters)
Note: this field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        """
        self._UniqueVpcId = None
        self._UniqueSubnetId = None
        self._RouterId = None
        self._Ip = None
        self._Port = None
        self._Remark = None

    @property
    def UniqueVpcId(self):
        return self._UniqueVpcId

    @UniqueVpcId.setter
    def UniqueVpcId(self, UniqueVpcId):
        self._UniqueVpcId = UniqueVpcId

    @property
    def UniqueSubnetId(self):
        return self._UniqueSubnetId

    @UniqueSubnetId.setter
    def UniqueSubnetId(self, UniqueSubnetId):
        self._UniqueSubnetId = UniqueSubnetId

    @property
    def RouterId(self):
        return self._RouterId

    @RouterId.setter
    def RouterId(self, RouterId):
        self._RouterId = RouterId

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._UniqueVpcId = params.get("UniqueVpcId")
        self._UniqueSubnetId = params.get("UniqueSubnetId")
        self._RouterId = params.get("RouterId")
        self._Ip = params.get("Ip")
        self._Port = params.get("Port")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcConfig(AbstractModel):
    """VPC configuration information

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: Subnet ID
        :type SubnetId: str
        """
        self._VpcId = None
        self._SubnetId = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        