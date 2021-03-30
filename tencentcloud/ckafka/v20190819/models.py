# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class Acl(AbstractModel):
    """ACL object entity

    """

    def __init__(self):
        """
        :param ResourceType: ACL resource type. 0: UNKNOWN, 1: ANY, 2: TOPIC, 3: GROUP, 4: CLUSTER, 5: TRANSACTIONAL_ID. Currently, only `TOPIC` is available,
        :type ResourceType: int
        :param ResourceName: Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name
        :type ResourceName: str
        :param Principal: User list. The default value is `User:*`, which means that any user can access. The current user can only be one included in the user list
Note: this field may return null, indicating that no valid values can be obtained.
        :type Principal: str
        :param Host: The default value is `*`, which means that any host can access. Currently, CKafka does not support the host as `*`, but the future product based on the open-source Kafka will directly support this
Note: this field may return null, indicating that no valid values can be obtained.
        :type Host: str
        :param Operation: ACL operation mode. 0: UNKNOWN, 1: ANY, 2: ALL, 3: READ, 4: WRITE, 5: CREATE, 6: DELETE, 7: ALTER, 8: DESCRIBE, 9: CLUSTER_ACTION, 10: DESCRIBE_CONFIGS, 11: ALTER_CONFIGS, 12: IDEMPOTEN_WRITE
        :type Operation: int
        :param PermissionType: Permission type. 0: UNKNOWN, 1: ANY, 2: DENY, 3: ALLOW
        :type PermissionType: int
        """
        self.ResourceType = None
        self.ResourceName = None
        self.Principal = None
        self.Host = None
        self.Operation = None
        self.PermissionType = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.ResourceName = params.get("ResourceName")
        self.Principal = params.get("Principal")
        self.Host = params.get("Host")
        self.Operation = params.get("Operation")
        self.PermissionType = params.get("PermissionType")


class AclResponse(AbstractModel):
    """Set of returned ACL results

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible data entries
        :type TotalCount: int
        :param AclList: ACL list
Note: this field may return null, indicating that no valid values can be obtained.
        :type AclList: list of Acl
        """
        self.TotalCount = None
        self.AclList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AclList") is not None:
            self.AclList = []
            for item in params.get("AclList"):
                obj = Acl()
                obj._deserialize(item)
                self.AclList.append(obj)


class AppIdResponse(AbstractModel):
    """`AppId` query result

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible `AppId`
        :type TotalCount: int
        :param AppIdList: List of eligible `AppId`
Note: this field may return null, indicating that no valid values can be obtained.
        :type AppIdList: list of int
        """
        self.TotalCount = None
        self.AppIdList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.AppIdList = params.get("AppIdList")


class Assignment(AbstractModel):
    """Stores the information of partition assigned to this consumer

    """

    def __init__(self):
        """
        :param Version: Assignment version information
        :type Version: int
        :param Topics: Topic information list
Note: this field may return null, indicating that no valid values can be obtained.
        :type Topics: list of GroupInfoTopics
        """
        self.Version = None
        self.Topics = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        if params.get("Topics") is not None:
            self.Topics = []
            for item in params.get("Topics"):
                obj = GroupInfoTopics()
                obj._deserialize(item)
                self.Topics.append(obj)


class Config(AbstractModel):
    """Advanced configuration object

    """

    def __init__(self):
        """
        :param Retention: Message retention period
Note: this field may return null, indicating that no valid values can be obtained.
        :type Retention: int
        :param MinInsyncReplicas: Minimum number of sync replications
Note: this field may return null, indicating that no valid values can be obtained.
        :type MinInsyncReplicas: int
        :param CleanUpPolicy: Log cleanup mode. Default value: delete.
delete: logs will be deleted by save time; compact: logs will be compressed by key; compact, delete: logs will be compressed by key and deleted by save time.
Note: this field may return null, indicating that no valid values can be obtained.
        :type CleanUpPolicy: str
        :param SegmentMs: Segment rolling duration
Note: this field may return null, indicating that no valid values can be obtained.
        :type SegmentMs: int
        :param UncleanLeaderElectionEnable: 0: false, 1: true.
Note: this field may return null, indicating that no valid values can be obtained.
        :type UncleanLeaderElectionEnable: int
        :param SegmentBytes: Number of bytes for segment rolling
Note: this field may return null, indicating that no valid values can be obtained.
        :type SegmentBytes: int
        :param MaxMessageBytes: Maximum number of message bytes
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxMessageBytes: int
        """
        self.Retention = None
        self.MinInsyncReplicas = None
        self.CleanUpPolicy = None
        self.SegmentMs = None
        self.UncleanLeaderElectionEnable = None
        self.SegmentBytes = None
        self.MaxMessageBytes = None


    def _deserialize(self, params):
        self.Retention = params.get("Retention")
        self.MinInsyncReplicas = params.get("MinInsyncReplicas")
        self.CleanUpPolicy = params.get("CleanUpPolicy")
        self.SegmentMs = params.get("SegmentMs")
        self.UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self.SegmentBytes = params.get("SegmentBytes")
        self.MaxMessageBytes = params.get("MaxMessageBytes")


class ConsumerGroup(AbstractModel):
    """User group entity

    """

    def __init__(self):
        """
        :param ConsumerGroupName: User group name
        :type ConsumerGroupName: str
        :param SubscribedInfo: Subscribed message entity
        :type SubscribedInfo: list of SubscribedInfo
        """
        self.ConsumerGroupName = None
        self.SubscribedInfo = None


    def _deserialize(self, params):
        self.ConsumerGroupName = params.get("ConsumerGroupName")
        if params.get("SubscribedInfo") is not None:
            self.SubscribedInfo = []
            for item in params.get("SubscribedInfo"):
                obj = SubscribedInfo()
                obj._deserialize(item)
                self.SubscribedInfo.append(obj)


class ConsumerGroupResponse(AbstractModel):
    """Returned consumer group result entity

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible consumer groups
        :type TotalCount: int
        :param TopicList: Topic list
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicList: list of ConsumerGroupTopic
        :param GroupList: Consumer group list
Note: this field may return null, indicating that no valid values can be obtained.
        :type GroupList: list of ConsumerGroup
        :param TotalPartition: Total number of partitions
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalPartition: int
        :param PartitionListForMonitor: List of monitored partitions
Note: this field may return null, indicating that no valid values can be obtained.
        :type PartitionListForMonitor: list of Partition
        :param TotalTopic: Total number of topics
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalTopic: int
        :param TopicListForMonitor: List of monitored topics
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicListForMonitor: list of ConsumerGroupTopic
        :param GroupListForMonitor: List of monitored groups
Note: this field may return null, indicating that no valid values can be obtained.
        :type GroupListForMonitor: list of Group
        """
        self.TotalCount = None
        self.TopicList = None
        self.GroupList = None
        self.TotalPartition = None
        self.PartitionListForMonitor = None
        self.TotalTopic = None
        self.TopicListForMonitor = None
        self.GroupListForMonitor = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TopicList") is not None:
            self.TopicList = []
            for item in params.get("TopicList"):
                obj = ConsumerGroupTopic()
                obj._deserialize(item)
                self.TopicList.append(obj)
        if params.get("GroupList") is not None:
            self.GroupList = []
            for item in params.get("GroupList"):
                obj = ConsumerGroup()
                obj._deserialize(item)
                self.GroupList.append(obj)
        self.TotalPartition = params.get("TotalPartition")
        if params.get("PartitionListForMonitor") is not None:
            self.PartitionListForMonitor = []
            for item in params.get("PartitionListForMonitor"):
                obj = Partition()
                obj._deserialize(item)
                self.PartitionListForMonitor.append(obj)
        self.TotalTopic = params.get("TotalTopic")
        if params.get("TopicListForMonitor") is not None:
            self.TopicListForMonitor = []
            for item in params.get("TopicListForMonitor"):
                obj = ConsumerGroupTopic()
                obj._deserialize(item)
                self.TopicListForMonitor.append(obj)
        if params.get("GroupListForMonitor") is not None:
            self.GroupListForMonitor = []
            for item in params.get("GroupListForMonitor"):
                obj = Group()
                obj._deserialize(item)
                self.GroupListForMonitor.append(obj)


class ConsumerGroupTopic(AbstractModel):
    """Consumer group topic object

    """

    def __init__(self):
        """
        :param TopicId: Topic ID
        :type TopicId: str
        :param TopicName: Topic name
        :type TopicName: str
        """
        self.TopicId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")


class CreateAclRequest(AbstractModel):
    """CreateAcl request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID information
        :type InstanceId: str
        :param ResourceType: ACL resource type. 0: UNKNOWN, 1: ANY, 2: TOPIC, 3: GROUP, 4: CLUSTER, 5: TRANSACTIONAL_ID. Currently, only `TOPIC` is available, and other fields will be used for future ACLs compatible with open-source Kafka
        :type ResourceType: int
        :param ResourceName: Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name
        :type ResourceName: str
        :param Operation: ACL operation mode. 0: UNKNOWN, 1: ANY, 2: ALL, 3: READ, 4: WRITE, 5: CREATE, 6: DELETE, 7: ALTER, 8: DESCRIBE, 9: CLUSTER_ACTION, 10: DESCRIBE_CONFIGS, 11: ALTER_CONFIGS
        :type Operation: int
        :param PermissionType: Permission type. 0: UNKNOWN, 1: ANY, 2: DENY, 3: ALLOW. Currently, CKafka supports `ALLOW` (equivalent to allowlist), and other fields will be used for future ACLs compatible with open-source Kafka
        :type PermissionType: int
        :param Host: The default value is `*`, which means that any host can access. Currently, CKafka does not support the host as `*`, but the future product based on the open-source Kafka will directly support this
        :type Host: str
        :param Principal: User list. The default value is `*`, which means that any user can access. The current user can only be one included in the user list
        :type Principal: str
        """
        self.InstanceId = None
        self.ResourceType = None
        self.ResourceName = None
        self.Operation = None
        self.PermissionType = None
        self.Host = None
        self.Principal = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceType = params.get("ResourceType")
        self.ResourceName = params.get("ResourceName")
        self.Operation = params.get("Operation")
        self.PermissionType = params.get("PermissionType")
        self.Host = params.get("Host")
        self.Principal = params.get("Principal")


class CreateAclResponse(AbstractModel):
    """CreateAcl response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreatePartitionRequest(AbstractModel):
    """CreatePartition request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param TopicName: Topic name
        :type TopicName: str
        :param PartitionNum: Number of topic partitions
        :type PartitionNum: int
        """
        self.InstanceId = None
        self.TopicName = None
        self.PartitionNum = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.PartitionNum = params.get("PartitionNum")


class CreatePartitionResponse(AbstractModel):
    """CreatePartition response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result set
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateTopicIpWhiteListRequest(AbstractModel):
    """CreateTopicIpWhiteList request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param TopicName: Topic name
        :type TopicName: str
        :param IpWhiteList: IP allowlist list
        :type IpWhiteList: list of str
        """
        self.InstanceId = None
        self.TopicName = None
        self.IpWhiteList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.IpWhiteList = params.get("IpWhiteList")


class CreateTopicIpWhiteListResponse(AbstractModel):
    """CreateTopicIpWhiteList response structure.

    """

    def __init__(self):
        """
        :param Result: Result of deleting topic IP allowlist
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateTopicRequest(AbstractModel):
    """CreateTopic request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param TopicName: Topic name string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)
        :type TopicName: str
        :param PartitionNum: Number of partitions, which should be greater than 0
        :type PartitionNum: int
        :param ReplicaNum: Number of replicas, which cannot be higher than the number of brokers. Maximum value: 3
        :type ReplicaNum: int
        :param EnableWhiteList: IP allowlist switch. 1: enabled, 0: disabled. Default value: 0
        :type EnableWhiteList: int
        :param IpWhiteList: IP allowlist list for quota limit, which is required if `enableWhileList` is 1
        :type IpWhiteList: list of str
        :param CleanUpPolicy: Log cleanup policy, which is `delete` by default. `delete`: logs will be deleted by save time; `compact`: logs will be compressed by key; `compact, delete`: logs will be compressed by key and deleted by save time.
        :type CleanUpPolicy: str
        :param Note: Topic remarks string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)
        :type Note: str
        :param MinInsyncReplicas: Default value: 1
        :type MinInsyncReplicas: int
        :param UncleanLeaderElectionEnable: Whether to allow an unsynced replica to be elected as leader. false: no, true: yes. Default value: false
        :type UncleanLeaderElectionEnable: int
        :param RetentionMs: Message retention period in ms, which is optional. The current minimum value is 60,000 ms
        :type RetentionMs: int
        :param SegmentMs: Segment rolling duration in ms. The current minimum value is 3,600,000 ms
        :type SegmentMs: int
        """
        self.InstanceId = None
        self.TopicName = None
        self.PartitionNum = None
        self.ReplicaNum = None
        self.EnableWhiteList = None
        self.IpWhiteList = None
        self.CleanUpPolicy = None
        self.Note = None
        self.MinInsyncReplicas = None
        self.UncleanLeaderElectionEnable = None
        self.RetentionMs = None
        self.SegmentMs = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.PartitionNum = params.get("PartitionNum")
        self.ReplicaNum = params.get("ReplicaNum")
        self.EnableWhiteList = params.get("EnableWhiteList")
        self.IpWhiteList = params.get("IpWhiteList")
        self.CleanUpPolicy = params.get("CleanUpPolicy")
        self.Note = params.get("Note")
        self.MinInsyncReplicas = params.get("MinInsyncReplicas")
        self.UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self.RetentionMs = params.get("RetentionMs")
        self.SegmentMs = params.get("SegmentMs")


class CreateTopicResp(AbstractModel):
    """Return for topic creation

    """

    def __init__(self):
        """
        :param TopicId: Topic ID
        :type TopicId: str
        """
        self.TopicId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")


class CreateTopicResponse(AbstractModel):
    """CreateTopic response structure.

    """

    def __init__(self):
        """
        :param Result: Returned creation result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicResp`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateTopicResp()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    """CreateUser request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Name: Username
        :type Name: str
        :param Password: User password
        :type Password: str
        """
        self.InstanceId = None
        self.Name = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.Password = params.get("Password")


class CreateUserResponse(AbstractModel):
    """CreateUser response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteAclRequest(AbstractModel):
    """DeleteAcl request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID information
        :type InstanceId: str
        :param ResourceType: ACL resource type. 0: UNKNOWN, 1: ANY, 2: TOPIC, 3: GROUP, 4: CLUSTER, 5: TRANSACTIONAL_ID. Currently, only `TOPIC` is available, and other fields will be used for future ACLs compatible with open-source Kafka
        :type ResourceType: int
        :param ResourceName: Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name
        :type ResourceName: str
        :param Operation: ACL operation mode. 0: UNKNOWN, 1: ANY, 2: ALL, 3: READ, 4: WRITE, 5: CREATE, 6: DELETE, 7: ALTER, 8: DESCRIBE, 9: CLUSTER_ACTION, 10: DESCRIBE_CONFIGS, 11: ALTER_CONFIGS, 12: IDEMPOTEN_WRITE. Currently, CKafka only supports `READ` and `WRITE`, and other values will be used for future ACLs compatible with open-source Kafka
        :type Operation: int
        :param PermissionType: Permission type. 0: UNKNOWN, 1: ANY, 2: DENY, 3: ALLOW. Currently, CKafka supports `ALLOW` (equivalent to allowlist), and other fields will be used for future ACLs compatible with open-source Kafka
        :type PermissionType: int
        :param Host: The default value is `*`, which means that any host can access. Currently, CKafka does not support the host as `*`, but the future product based on the open-source Kafka will directly support this
        :type Host: str
        :param Principal: User list. The default value is `*`, which means that any user can access. The current user can only be one included in the user list
        :type Principal: str
        """
        self.InstanceId = None
        self.ResourceType = None
        self.ResourceName = None
        self.Operation = None
        self.PermissionType = None
        self.Host = None
        self.Principal = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceType = params.get("ResourceType")
        self.ResourceName = params.get("ResourceName")
        self.Operation = params.get("Operation")
        self.PermissionType = params.get("PermissionType")
        self.Host = params.get("Host")
        self.Principal = params.get("Principal")


class DeleteAclResponse(AbstractModel):
    """DeleteAcl response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteTopicIpWhiteListRequest(AbstractModel):
    """DeleteTopicIpWhiteList request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param TopicName: Topic name
        :type TopicName: str
        :param IpWhiteList: IP allowlist list
        :type IpWhiteList: list of str
        """
        self.InstanceId = None
        self.TopicName = None
        self.IpWhiteList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.IpWhiteList = params.get("IpWhiteList")


class DeleteTopicIpWhiteListResponse(AbstractModel):
    """DeleteTopicIpWhiteList response structure.

    """

    def __init__(self):
        """
        :param Result: Result of deleting topic IP allowlist
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteTopicRequest(AbstractModel):
    """DeleteTopic request structure.

    """

    def __init__(self):
        """
        :param InstanceId: CKafka instance ID
        :type InstanceId: str
        :param TopicName: CKafka topic name
        :type TopicName: str
        """
        self.InstanceId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")


class DeleteTopicResponse(AbstractModel):
    """DeleteTopic response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result set
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteUserRequest(AbstractModel):
    """DeleteUser request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Name: Username
        :type Name: str
        """
        self.InstanceId = None
        self.Name = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")


class DeleteUserResponse(AbstractModel):
    """DeleteUser response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeACLRequest(AbstractModel):
    """DescribeACL request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param ResourceType: ACL resource type. 0: UNKNOWN, 1: ANY, 2: TOPIC, 3: GROUP, 4: CLUSTER, 5: TRANSACTIONAL_ID. Currently, only `TOPIC` is available, and other fields will be used for future ACLs compatible with open-source Kafka
        :type ResourceType: int
        :param ResourceName: Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name
        :type ResourceName: str
        :param Offset: Offset position
        :type Offset: int
        :param Limit: Quantity limit
        :type Limit: int
        :param SearchWord: Keyword match
        :type SearchWord: str
        """
        self.InstanceId = None
        self.ResourceType = None
        self.ResourceName = None
        self.Offset = None
        self.Limit = None
        self.SearchWord = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceType = params.get("ResourceType")
        self.ResourceName = params.get("ResourceName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchWord = params.get("SearchWord")


class DescribeACLResponse(AbstractModel):
    """DescribeACL response structure.

    """

    def __init__(self):
        """
        :param Result: Returned ACL result set object
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.AclResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = AclResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeAppInfoRequest(AbstractModel):
    """DescribeAppInfo request structure.

    """

    def __init__(self):
        """
        :param Offset: Offset position
        :type Offset: int
        :param Limit: Maximum number of users to be queried in this request. Maximum value: 50. Default value: 50
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAppInfoResponse(AbstractModel):
    """DescribeAppInfo response structure.

    """

    def __init__(self):
        """
        :param Result: Returned list of eligible `AppId`
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.AppIdResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = AppIdResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeConsumerGroupRequest(AbstractModel):
    """DescribeConsumerGroup request structure.

    """

    def __init__(self):
        """
        :param InstanceId: CKafka instance ID.
        :type InstanceId: str
        :param GroupName: Name of the group to be queried, which is optional.
        :type GroupName: str
        :param TopicName: Name of the corresponding topic in the group to be queried, which is optional. If this parameter is specified but `group` is not specified, this parameter will be ignored.
        :type TopicName: str
        :param Limit: Number of results to be returned in this request
        :type Limit: int
        :param Offset: Offset position
        :type Offset: int
        """
        self.InstanceId = None
        self.GroupName = None
        self.TopicName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.GroupName = params.get("GroupName")
        self.TopicName = params.get("TopicName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeConsumerGroupResponse(AbstractModel):
    """DescribeConsumerGroup response structure.

    """

    def __init__(self):
        """
        :param Result: Returned consumer group information
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ConsumerGroupResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ConsumerGroupResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeGroup(AbstractModel):
    """`DescribeGroup` response entity

    """

    def __init__(self):
        """
        :param Group: groupId
        :type Group: str
        :param Protocol: Protocol used by the group.
        :type Protocol: str
        """
        self.Group = None
        self.Protocol = None


    def _deserialize(self, params):
        self.Group = params.get("Group")
        self.Protocol = params.get("Protocol")


class DescribeGroupInfoRequest(AbstractModel):
    """DescribeGroupInfo request structure.

    """

    def __init__(self):
        """
        :param InstanceId: (Filter) filter by instance ID.
        :type InstanceId: str
        :param GroupList: Kafka consumer group (`Consumer-group`), which is an array in the format of `GroupList.0=xxx&GroupList.1=yyy`.
        :type GroupList: list of str
        """
        self.InstanceId = None
        self.GroupList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.GroupList = params.get("GroupList")


class DescribeGroupInfoResponse(AbstractModel):
    """DescribeGroupInfo response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: list of GroupInfoResponse
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = GroupInfoResponse()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeGroupOffsetsRequest(AbstractModel):
    """DescribeGroupOffsets request structure.

    """

    def __init__(self):
        """
        :param InstanceId: (Filter) filter by instance ID
        :type InstanceId: str
        :param Group: Kafka consumer group
        :type Group: str
        :param Topics: Array of the names of topics subscribed to by a group. If there is no such array, this parameter means the information of all topics in the specified group
        :type Topics: list of str
        :param SearchWord: Fuzzy match by `topicName`
        :type SearchWord: str
        :param Offset: Offset position of this query. Default value: 0
        :type Offset: int
        :param Limit: Maximum number of results to be returned in this request. Default value: 50. Maximum value: 50
        :type Limit: int
        """
        self.InstanceId = None
        self.Group = None
        self.Topics = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Group = params.get("Group")
        self.Topics = params.get("Topics")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeGroupOffsetsResponse(AbstractModel):
    """DescribeGroupOffsets response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result object
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.GroupOffsetResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = GroupOffsetResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeGroupRequest(AbstractModel):
    """DescribeGroup request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param SearchWord: Search keyword
        :type SearchWord: str
        :param Offset: Offset
        :type Offset: int
        :param Limit: Maximum number of results to be returned
        :type Limit: int
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeGroupResponse(AbstractModel):
    """DescribeGroup response structure.

    """

    def __init__(self):
        """
        :param Result: List of returned results
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.GroupResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = GroupResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeInstanceAttributesRequest(AbstractModel):
    """DescribeInstanceAttributes request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeInstanceAttributesResponse(AbstractModel):
    """DescribeInstanceAttributes response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result object of instance attributes
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceAttributesResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = InstanceAttributesResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeInstancesDetailRequest(AbstractModel):
    """DescribeInstancesDetail request structure.

    """

    def __init__(self):
        """
        :param InstanceId: (Filter) filter by instance ID
        :type InstanceId: str
        :param SearchWord: (Filter) filter by instance name. Fuzzy search is supported
        :type SearchWord: str
        :param Status: (Filter) instance status. 0: creating, 1: running, 2: deleting. If this parameter is left empty, all instances will be returned by default
        :type Status: list of int
        :param Offset: Offset. If this parameter is left empty, 0 will be used by default
        :type Offset: int
        :param Limit: Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 20
        :type Limit: int
        :param TagKey: Tag key match.
        :type TagKey: str
        :param Filters: Filter
        :type Filters: list of Filter
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Status = None
        self.Offset = None
        self.Limit = None
        self.TagKey = None
        self.Filters = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TagKey = params.get("TagKey")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeInstancesDetailResponse(AbstractModel):
    """DescribeInstancesDetail response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result object of instance details
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceDetailResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = InstanceDetailResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances request structure.

    """

    def __init__(self):
        """
        :param InstanceId: (Filter) filter by instance ID
        :type InstanceId: str
        :param SearchWord: (Filter) filter by instance name. Fuzzy search is supported
        :type SearchWord: str
        :param Status: (Filter) instance status. 0: creating, 1: running, 2: deleting. If this parameter is left empty, all instances will be returned by default
        :type Status: list of int
        :param Offset: Offset. If this parameter is left empty, 0 will be used by default
        :type Offset: int
        :param Limit: Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 100.
        :type Limit: int
        :param TagKey: Tag key match.
        :type TagKey: str
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Status = None
        self.Offset = None
        self.Limit = None
        self.TagKey = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TagKey = params.get("TagKey")


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = InstanceResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeRouteRequest(AbstractModel):
    """DescribeRoute request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Unique instance ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeRouteResponse(AbstractModel):
    """DescribeRoute response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result set of route information
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.RouteResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = RouteResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeTopicAttributesRequest(AbstractModel):
    """DescribeTopicAttributes request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param TopicName: Topic name
        :type TopicName: str
        """
        self.InstanceId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")


class DescribeTopicAttributesResponse(AbstractModel):
    """DescribeTopicAttributes response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result object
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicAttributesResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TopicAttributesResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeTopicDetailRequest(AbstractModel):
    """DescribeTopicDetail request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param SearchWord: (Filter) filter by `topicName`. Fuzzy search is supported
        :type SearchWord: str
        :param Offset: Offset. If this parameter is left empty, 0 will be used by default
        :type Offset: int
        :param Limit: Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 20. This value must be greater than 0
        :type Limit: int
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTopicDetailResponse(AbstractModel):
    """DescribeTopicDetail response structure.

    """

    def __init__(self):
        """
        :param Result: Returned entity of topic details
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicDetailResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TopicDetailResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeTopicRequest(AbstractModel):
    """DescribeTopic request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param SearchWord: Filter by `topicName`. Fuzzy search is supported
        :type SearchWord: str
        :param Offset: Offset. If this parameter is left empty, 0 will be used by default
        :type Offset: int
        :param Limit: Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 20
        :type Limit: int
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTopicResponse(AbstractModel):
    """DescribeTopic response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result
Note: this field may return null, indicating that no valid values can be obtained.
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicResult`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = TopicResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUserRequest(AbstractModel):
    """DescribeUser request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param SearchWord: Filter by name
        :type SearchWord: str
        :param Offset: Offset
        :type Offset: int
        :param Limit: Number of results to be returned in this request
        :type Limit: int
        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeUserResponse(AbstractModel):
    """DescribeUser response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result list
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.UserResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UserResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DynamicRetentionTime(AbstractModel):
    """Dynamic message retention time configuration

    """

    def __init__(self):
        """
        :param Enable: Whether the dynamic message retention time configuration is enabled. 0: disabled; 1: enabled
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Enable: int
        :param DiskQuotaPercentage: Disk quota threshold (in percentage) for triggering the message retention time change event
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type DiskQuotaPercentage: int
        :param StepForwardPercentage: Percentage by which the message retention time is shortened each time
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type StepForwardPercentage: int
        :param BottomRetention: Minimum retention time, in minutes
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type BottomRetention: int
        """
        self.Enable = None
        self.DiskQuotaPercentage = None
        self.StepForwardPercentage = None
        self.BottomRetention = None


    def _deserialize(self, params):
        self.Enable = params.get("Enable")
        self.DiskQuotaPercentage = params.get("DiskQuotaPercentage")
        self.StepForwardPercentage = params.get("StepForwardPercentage")
        self.BottomRetention = params.get("BottomRetention")


class Filter(AbstractModel):
    """Query filter
    >Key-value pair filters for conditional filtering queries, such as filter ID, name, and status
    > * If there are multiple `Filter`, the relationship among them is logical `AND`.
    > * If there are multiple `Values` in the same `Filter`, the relationship among them is logical `OR`.
    >

    """

    def __init__(self):
        """
        :param Name: Field to be filtered.
        :type Name: str
        :param Values: Filter value of field.
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class Group(AbstractModel):
    """Group entity

    """

    def __init__(self):
        """
        :param GroupName: Group name
        :type GroupName: str
        """
        self.GroupName = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")


class GroupInfoMember(AbstractModel):
    """Consumer information

    """

    def __init__(self):
        """
        :param MemberId: Unique ID generated for consumer in consumer group by coordinator
        :type MemberId: str
        :param ClientId: `client.id` information by the client consumer SDK
        :type ClientId: str
        :param ClientHost: Generally stores client IP address
        :type ClientHost: str
        :param Assignment: Stores the information of partition assigned to this consumer
        :type Assignment: :class:`tencentcloud.ckafka.v20190819.models.Assignment`
        """
        self.MemberId = None
        self.ClientId = None
        self.ClientHost = None
        self.Assignment = None


    def _deserialize(self, params):
        self.MemberId = params.get("MemberId")
        self.ClientId = params.get("ClientId")
        self.ClientHost = params.get("ClientHost")
        if params.get("Assignment") is not None:
            self.Assignment = Assignment()
            self.Assignment._deserialize(params.get("Assignment"))


class GroupInfoResponse(AbstractModel):
    """`GroupInfo` response data entity

    """

    def __init__(self):
        """
        :param ErrorCode: Error code. 0: success
        :type ErrorCode: str
        :param State: Group status description (common valid values: Empty, Stable, Dead):
Dead: the consumer group does not exist
Empty: there are currently no consumer subscriptions in the consumer group
PreparingRebalance: the consumer group is currently in `rebalance` state
CompletingRebalance: the consumer group is currently in `rebalance` state
Stable: each consumer in the consumer group has joined and is in stable state
        :type State: str
        :param ProtocolType: The type of protocol selected by the consumer group, which is `consumer` for common consumers. However, some systems use their own protocols; for example, the protocol used by kafka-connect is `connect`. Only with the standard `consumer` protocol can this API get to know the specific assigning method and parse the specific partition assignment
        :type ProtocolType: str
        :param Protocol: Consumer partition assignment algorithm, such as `range` (which is the default value for the Kafka consumer SDK), `roundrobin`, and `sticky`
        :type Protocol: str
        :param Members: This array contains information only if `state` is `Stable` and `protocol_type` is `consumer`
        :type Members: list of GroupInfoMember
        :param Group: Kafka consumer group
        :type Group: str
        """
        self.ErrorCode = None
        self.State = None
        self.ProtocolType = None
        self.Protocol = None
        self.Members = None
        self.Group = None


    def _deserialize(self, params):
        self.ErrorCode = params.get("ErrorCode")
        self.State = params.get("State")
        self.ProtocolType = params.get("ProtocolType")
        self.Protocol = params.get("Protocol")
        if params.get("Members") is not None:
            self.Members = []
            for item in params.get("Members"):
                obj = GroupInfoMember()
                obj._deserialize(item)
                self.Members.append(obj)
        self.Group = params.get("Group")


class GroupInfoTopics(AbstractModel):
    """Internal topic object of `GroupInfo`

    """

    def __init__(self):
        """
        :param Topic: Name of assigned topics
        :type Topic: str
        :param Partitions: Information of assigned partition
Note: this field may return null, indicating that no valid values can be obtained.
        :type Partitions: list of int
        """
        self.Topic = None
        self.Partitions = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Partitions = params.get("Partitions")


class GroupOffsetPartition(AbstractModel):
    """Group offset partition object

    """

    def __init__(self):
        """
        :param Partition: Topic `partitionId`
        :type Partition: int
        :param Offset: Offset position submitted by consumer
        :type Offset: int
        :param Metadata: Metadata can be passed in for other purposes when the consumer submits messages. Currently, this parameter is usually an empty string
Note: this field may return null, indicating that no valid values can be obtained.
        :type Metadata: str
        :param ErrorCode: Error code
        :type ErrorCode: int
        :param LogEndOffset: Latest offset of current partition
        :type LogEndOffset: int
        :param Lag: Number of unconsumed messages
        :type Lag: int
        """
        self.Partition = None
        self.Offset = None
        self.Metadata = None
        self.ErrorCode = None
        self.LogEndOffset = None
        self.Lag = None


    def _deserialize(self, params):
        self.Partition = params.get("Partition")
        self.Offset = params.get("Offset")
        self.Metadata = params.get("Metadata")
        self.ErrorCode = params.get("ErrorCode")
        self.LogEndOffset = params.get("LogEndOffset")
        self.Lag = params.get("Lag")


class GroupOffsetResponse(AbstractModel):
    """Returned result of consumer group offset

    """

    def __init__(self):
        """
        :param TotalCount: Total number of eligible results
        :type TotalCount: int
        :param TopicList: Array of partitions in the topic, where each element is a JSON object
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicList: list of GroupOffsetTopic
        """
        self.TotalCount = None
        self.TopicList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TopicList") is not None:
            self.TopicList = []
            for item in params.get("TopicList"):
                obj = GroupOffsetTopic()
                obj._deserialize(item)
                self.TopicList.append(obj)


class GroupOffsetTopic(AbstractModel):
    """Consumer group topic object

    """

    def __init__(self):
        """
        :param Topic: Topic name
        :type Topic: str
        :param Partitions: Array of partitions in the topic, where each element is a JSON object
Note: this field may return null, indicating that no valid values can be obtained.
        :type Partitions: list of GroupOffsetPartition
        """
        self.Topic = None
        self.Partitions = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = GroupOffsetPartition()
                obj._deserialize(item)
                self.Partitions.append(obj)


class GroupResponse(AbstractModel):
    """`DescribeGroup` response

    """

    def __init__(self):
        """
        :param TotalCount: Count
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param GroupList: GroupList
Note: this field may return null, indicating that no valid values can be obtained.
        :type GroupList: list of DescribeGroup
        """
        self.TotalCount = None
        self.GroupList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("GroupList") is not None:
            self.GroupList = []
            for item in params.get("GroupList"):
                obj = DescribeGroup()
                obj._deserialize(item)
                self.GroupList.append(obj)


class Instance(AbstractModel):
    """Instance object

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param InstanceName: Instance name
        :type InstanceName: str
        :param Status: Instance status. 0: creating, 1: running, 2: deleting, 5: isolated, -1: creation failed
        :type Status: int
        :param IfCommunity: Whether it is an open-source instance. true: yes, false: no
Note: this field may return null, indicating that no valid values can be obtained.
        :type IfCommunity: bool
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Status = None
        self.IfCommunity = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Status = params.get("Status")
        self.IfCommunity = params.get("IfCommunity")


class InstanceAttributesResponse(AbstractModel):
    """Returned result object of instance attributes

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param InstanceName: Instance name
        :type InstanceName: str
        :param VipList: VIP list information of access point
        :type VipList: list of VipEntity
        :param Vip: Virtual IP
        :type Vip: str
        :param Vport: Virtual port
        :type Vport: str
        :param Status: Instance status. 0: creating, 1: running, 2: deleting
        :type Status: int
        :param Bandwidth: Instance bandwidth in Mbps
        :type Bandwidth: int
        :param DiskSize: Instance storage capacity in GB
        :type DiskSize: int
        :param ZoneId: AZ
        :type ZoneId: int
        :param VpcId: VPC ID. If this parameter is empty, it means the basic network
        :type VpcId: str
        :param SubnetId: Subnet ID. If this parameter is empty, it means the basic network
        :type SubnetId: str
        :param Healthy: Instance health status. 1: healthy, 2: alarmed, 3: exceptional
        :type Healthy: int
        :param HealthyMessage: Instance health information. Currently, the disk utilization is displayed with a maximum length of 256
        :type HealthyMessage: str
        :param CreateTime: Creation time
        :type CreateTime: int
        :param MsgRetentionTime: Message retention period in minutes
        :type MsgRetentionTime: int
        :param Config: Configuration for automatic topic creation. If this field is empty, it means that automatic creation is not enabled
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.InstanceConfigDO`
        :param RemainderPartitions: Number of remaining creatable partitions
        :type RemainderPartitions: int
        :param RemainderTopics: Number of remaining creatable topics
        :type RemainderTopics: int
        :param CreatedPartitions: Number of partitions already created
        :type CreatedPartitions: int
        :param CreatedTopics: Number of topics already created
        :type CreatedTopics: int
        :param Tags: Tag array
Note: this field may return null, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param ExpireTime: Expiration time
Note: this field may return null, indicating that no valid values can be obtained.
        :type ExpireTime: int
        :param ZoneIds: Cross-AZ
Note: this field may return null, indicating that no valid values can be obtained.
        :type ZoneIds: list of int
        :param Version: Kafka version information
Note: this field may return null, indicating that no valid values can be obtained.
        :type Version: str
        :param MaxGroupNum: Maximum number of groups
Note: this field may return null, indicating that no valid values can be obtained.
        :type MaxGroupNum: int
        :param Cvm: Offering type. `0`: Standard Edition; `1`: Professional Edition
Note: this field may return `null`, indicating that no valid value was found.
        :type Cvm: int
        :param InstanceType: Type.
Note: this field may return `null`, indicating that no valid value was found.
        :type InstanceType: str
        :param Features: Features supported by the instance. `FEATURE_SUBNET_ACL` indicates that the ACL policy supports setting subnets. 
Note: this field may return null, indicating that no valid values can be obtained.
        :type Features: list of str
        :param RetentionTimeConfig: Dynamic message retention policy
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type RetentionTimeConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`
        """
        self.InstanceId = None
        self.InstanceName = None
        self.VipList = None
        self.Vip = None
        self.Vport = None
        self.Status = None
        self.Bandwidth = None
        self.DiskSize = None
        self.ZoneId = None
        self.VpcId = None
        self.SubnetId = None
        self.Healthy = None
        self.HealthyMessage = None
        self.CreateTime = None
        self.MsgRetentionTime = None
        self.Config = None
        self.RemainderPartitions = None
        self.RemainderTopics = None
        self.CreatedPartitions = None
        self.CreatedTopics = None
        self.Tags = None
        self.ExpireTime = None
        self.ZoneIds = None
        self.Version = None
        self.MaxGroupNum = None
        self.Cvm = None
        self.InstanceType = None
        self.Features = None
        self.RetentionTimeConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        if params.get("VipList") is not None:
            self.VipList = []
            for item in params.get("VipList"):
                obj = VipEntity()
                obj._deserialize(item)
                self.VipList.append(obj)
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.Status = params.get("Status")
        self.Bandwidth = params.get("Bandwidth")
        self.DiskSize = params.get("DiskSize")
        self.ZoneId = params.get("ZoneId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Healthy = params.get("Healthy")
        self.HealthyMessage = params.get("HealthyMessage")
        self.CreateTime = params.get("CreateTime")
        self.MsgRetentionTime = params.get("MsgRetentionTime")
        if params.get("Config") is not None:
            self.Config = InstanceConfigDO()
            self.Config._deserialize(params.get("Config"))
        self.RemainderPartitions = params.get("RemainderPartitions")
        self.RemainderTopics = params.get("RemainderTopics")
        self.CreatedPartitions = params.get("CreatedPartitions")
        self.CreatedTopics = params.get("CreatedTopics")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.ExpireTime = params.get("ExpireTime")
        self.ZoneIds = params.get("ZoneIds")
        self.Version = params.get("Version")
        self.MaxGroupNum = params.get("MaxGroupNum")
        self.Cvm = params.get("Cvm")
        self.InstanceType = params.get("InstanceType")
        self.Features = params.get("Features")
        if params.get("RetentionTimeConfig") is not None:
            self.RetentionTimeConfig = DynamicRetentionTime()
            self.RetentionTimeConfig._deserialize(params.get("RetentionTimeConfig"))


class InstanceConfigDO(AbstractModel):
    """Instance configuration entity

    """

    def __init__(self):
        """
        :param AutoCreateTopicsEnable: Whether to create topics automatically
        :type AutoCreateTopicsEnable: bool
        :param DefaultNumPartitions: Number of partitions
        :type DefaultNumPartitions: int
        :param DefaultReplicationFactor: Default replication factor
        :type DefaultReplicationFactor: int
        """
        self.AutoCreateTopicsEnable = None
        self.DefaultNumPartitions = None
        self.DefaultReplicationFactor = None


    def _deserialize(self, params):
        self.AutoCreateTopicsEnable = params.get("AutoCreateTopicsEnable")
        self.DefaultNumPartitions = params.get("DefaultNumPartitions")
        self.DefaultReplicationFactor = params.get("DefaultReplicationFactor")


class InstanceDetail(AbstractModel):
    """Instance details

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param InstanceName: Instance name
        :type InstanceName: str
        :param Vip: Instance VIP information
        :type Vip: str
        :param Vport: Instance port information
        :type Vport: str
        :param VipList: Virtual IP list
        :type VipList: list of VipEntity
        :param Status: Instance status. 0: creating, 1: running, 2: deleting, 5: isolated, -1: creation failed
        :type Status: int
        :param Bandwidth: Instance bandwidth in Mbps
        :type Bandwidth: int
        :param DiskSize: Instance storage capacity in GB
        :type DiskSize: int
        :param ZoneId: AZ ID
        :type ZoneId: int
        :param VpcId: vpcId. If this parameter is empty, it means the basic network
        :type VpcId: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        :param RenewFlag: Whether to renew the instance automatically, which is an int-type enumerated value. 1: yes, 2: no
        :type RenewFlag: int
        :param Healthy: Instance status, which is an int-type value. 0: healthy, 1: alarmed, 2: exceptional
        :type Healthy: int
        :param HealthyMessage: Instance status information
        :type HealthyMessage: str
        :param CreateTime: Instance creation time
        :type CreateTime: int
        :param ExpireTime: Instance expiration time
        :type ExpireTime: int
        :param IsInternal: Whether it is an internal customer. 1: yes
        :type IsInternal: int
        :param TopicNum: Number of topics
        :type TopicNum: int
        :param Tags: Tag
        :type Tags: list of Tag
        :param Version: Kafka version information
Note: this field may return null, indicating that no valid values can be obtained.
        :type Version: str
        :param ZoneIds: Cross-AZ
Note: this field may return null, indicating that no valid values can be obtained.
        :type ZoneIds: list of int
        :param Cvm: CKafka sale type
Note: this field may return null, indicating that no valid values can be obtained.
        :type Cvm: int
        :param InstanceType: CKafka instance type
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type InstanceType: str
        :param DiskType: Disk type
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type DiskType: str
        :param MaxTopicNumber: Maximum number of topics for the current instance
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type MaxTopicNumber: int
        :param MaxPartitionNumber: Maximum number of partitions for the current instance
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type MaxPartitionNumber: int
        :param RebalanceTime: Time of scheduled upgrade
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type RebalanceTime: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Vip = None
        self.Vport = None
        self.VipList = None
        self.Status = None
        self.Bandwidth = None
        self.DiskSize = None
        self.ZoneId = None
        self.VpcId = None
        self.SubnetId = None
        self.RenewFlag = None
        self.Healthy = None
        self.HealthyMessage = None
        self.CreateTime = None
        self.ExpireTime = None
        self.IsInternal = None
        self.TopicNum = None
        self.Tags = None
        self.Version = None
        self.ZoneIds = None
        self.Cvm = None
        self.InstanceType = None
        self.DiskType = None
        self.MaxTopicNumber = None
        self.MaxPartitionNumber = None
        self.RebalanceTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        if params.get("VipList") is not None:
            self.VipList = []
            for item in params.get("VipList"):
                obj = VipEntity()
                obj._deserialize(item)
                self.VipList.append(obj)
        self.Status = params.get("Status")
        self.Bandwidth = params.get("Bandwidth")
        self.DiskSize = params.get("DiskSize")
        self.ZoneId = params.get("ZoneId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.RenewFlag = params.get("RenewFlag")
        self.Healthy = params.get("Healthy")
        self.HealthyMessage = params.get("HealthyMessage")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.IsInternal = params.get("IsInternal")
        self.TopicNum = params.get("TopicNum")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Version = params.get("Version")
        self.ZoneIds = params.get("ZoneIds")
        self.Cvm = params.get("Cvm")
        self.InstanceType = params.get("InstanceType")
        self.DiskType = params.get("DiskType")
        self.MaxTopicNumber = params.get("MaxTopicNumber")
        self.MaxPartitionNumber = params.get("MaxPartitionNumber")
        self.RebalanceTime = params.get("RebalanceTime")


class InstanceDetailResponse(AbstractModel):
    """Returned result of instance details

    """

    def __init__(self):
        """
        :param TotalCount: Total number of eligible instances
        :type TotalCount: int
        :param InstanceList: List of eligible instance details
        :type InstanceList: list of InstanceDetail
        """
        self.TotalCount = None
        self.InstanceList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = InstanceDetail()
                obj._deserialize(item)
                self.InstanceList.append(obj)


class InstanceResponse(AbstractModel):
    """Aggregated returned result of instance status

    """

    def __init__(self):
        """
        :param InstanceList: List of eligible instances
Note: this field may return null, indicating that no valid values can be obtained.
        :type InstanceList: list of Instance
        :param TotalCount: Total number of eligible results
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        """
        self.InstanceList = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = Instance()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.TotalCount = params.get("TotalCount")


class JgwOperateResponse(AbstractModel):
    """Returned result value of operation

    """

    def __init__(self):
        """
        :param ReturnCode: Returned code. 0: normal, other values: error
        :type ReturnCode: str
        :param ReturnMessage: Success message
        :type ReturnMessage: str
        :param Data: Data returned by an operation, which may contain `flowId`, etc.
Note: this field may return null, indicating that no valid values can be obtained.
        :type Data: :class:`tencentcloud.ckafka.v20190819.models.OperateResponseData`
        """
        self.ReturnCode = None
        self.ReturnMessage = None
        self.Data = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.ReturnMessage = params.get("ReturnMessage")
        if params.get("Data") is not None:
            self.Data = OperateResponseData()
            self.Data._deserialize(params.get("Data"))


class ModifyGroupOffsetsRequest(AbstractModel):
    """ModifyGroupOffsets request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Kafka instance ID
        :type InstanceId: str
        :param Group: Kafka consumer group
        :type Group: str
        :param Strategy: Offset resetting policy. Meanings of the input parameters: 0: equivalent to the `shift-by` parameter, which indicates to shift the offset forward or backward by the value of the `shift`. 1: equivalent to `by-duration`, `to-datetime`, `to-earliest`, or `to-latest`, which indicates to move the offset to the specified timestamp. 2: equivalent to `to-offset`, which indicates to move the offset to the specified offset position
        :type Strategy: int
        :param Topics: Indicates the topics to be reset. If this parameter is left empty, all topics will be reset
        :type Topics: list of str
        :param Shift: When `strategy` is 0, this field is required. If it is above zero, the offset will be shifted backward by the value of the `shift`. If it is below zero, the offset will be shifted forward by the value of the `shift`. After a correct reset, the new offset should be (old_offset + shift). Note that if the new offset is smaller than the `earliest` parameter of the partition, it will be set to `earliest`, and if it is greater than the `latest` parameter of the partition, it will be set to `latest`
        :type Shift: int
        :param ShiftTimestamp: Unit: ms. When `strategy` is 1, this field is required, where -2 indicates to reset the offset to the initial position, -1 indicates to reset to the latest position (equivalent to emptying), and other values represent the specified time, i.e., the offset of the topic at the specified time will be obtained and then reset. Note that if there is no message at the specified time, the last offset will be obtained
        :type ShiftTimestamp: int
        :param Offset: Position of the offset that needs to be reset. When `strategy` is 2, this field is required
        :type Offset: int
        :param Partitions: List of partitions that need to be reset. If the topics parameter is not specified, reset partitions in the corresponding partition list of all topics. If the topics parameter is specified, reset partitions of the corresponding partition list of the specified topic list.
        :type Partitions: list of int
        """
        self.InstanceId = None
        self.Group = None
        self.Strategy = None
        self.Topics = None
        self.Shift = None
        self.ShiftTimestamp = None
        self.Offset = None
        self.Partitions = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Group = params.get("Group")
        self.Strategy = params.get("Strategy")
        self.Topics = params.get("Topics")
        self.Shift = params.get("Shift")
        self.ShiftTimestamp = params.get("ShiftTimestamp")
        self.Offset = params.get("Offset")
        self.Partitions = params.get("Partitions")


class ModifyGroupOffsetsResponse(AbstractModel):
    """ModifyGroupOffsets response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ModifyInstanceAttributesConfig(AbstractModel):
    """Configuration object for modifying instance attributes

    """

    def __init__(self):
        """
        :param AutoCreateTopicEnable: Automatic creation. true: enabled, false: not enabled
        :type AutoCreateTopicEnable: bool
        :param DefaultNumPartitions: Optional. If `auto.create.topic.enable` is set to `true` and this value is not set, 3 will be used by default
        :type DefaultNumPartitions: int
        :param DefaultReplicationFactor: If `auto.create.topic.enable` is set to `true` but this value is not set, 2 will be used by default
        :type DefaultReplicationFactor: int
        """
        self.AutoCreateTopicEnable = None
        self.DefaultNumPartitions = None
        self.DefaultReplicationFactor = None


    def _deserialize(self, params):
        self.AutoCreateTopicEnable = params.get("AutoCreateTopicEnable")
        self.DefaultNumPartitions = params.get("DefaultNumPartitions")
        self.DefaultReplicationFactor = params.get("DefaultReplicationFactor")


class ModifyInstanceAttributesRequest(AbstractModel):
    """ModifyInstanceAttributes request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param MsgRetentionTime: Maximum retention period in minutes for instance log, which can be up to 30 days. 0 indicates not to enable the log retention period policy
        :type MsgRetentionTime: int
        :param InstanceName: Instance name string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)
        :type InstanceName: str
        :param Config: Instance configuration
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstanceAttributesConfig`
        :param DynamicRetentionConfig: Dynamic message retention policy configuration
        :type DynamicRetentionConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`
        :param RebalanceTime: Modification of the rebalancing time after upgrade
        :type RebalanceTime: int
        """
        self.InstanceId = None
        self.MsgRetentionTime = None
        self.InstanceName = None
        self.Config = None
        self.DynamicRetentionConfig = None
        self.RebalanceTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.MsgRetentionTime = params.get("MsgRetentionTime")
        self.InstanceName = params.get("InstanceName")
        if params.get("Config") is not None:
            self.Config = ModifyInstanceAttributesConfig()
            self.Config._deserialize(params.get("Config"))
        if params.get("DynamicRetentionConfig") is not None:
            self.DynamicRetentionConfig = DynamicRetentionTime()
            self.DynamicRetentionConfig._deserialize(params.get("DynamicRetentionConfig"))
        self.RebalanceTime = params.get("RebalanceTime")


class ModifyInstanceAttributesResponse(AbstractModel):
    """ModifyInstanceAttributes response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ModifyPasswordRequest(AbstractModel):
    """ModifyPassword request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Name: Username
        :type Name: str
        :param Password: Current user password
        :type Password: str
        :param PasswordNew: New user password
        :type PasswordNew: str
        """
        self.InstanceId = None
        self.Name = None
        self.Password = None
        self.PasswordNew = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.Password = params.get("Password")
        self.PasswordNew = params.get("PasswordNew")


class ModifyPasswordResponse(AbstractModel):
    """ModifyPassword response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ModifyTopicAttributesRequest(AbstractModel):
    """ModifyTopicAttributes request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID.
        :type InstanceId: str
        :param TopicName: Topic name.
        :type TopicName: str
        :param Note: Topic remarks string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).
        :type Note: str
        :param EnableWhiteList: IP allowlist switch. 1: enabled, 0: disabled.
        :type EnableWhiteList: int
        :param MinInsyncReplicas: Default value: 1.
        :type MinInsyncReplicas: int
        :param UncleanLeaderElectionEnable: 0: false, 1: true. Default value: 0.
        :type UncleanLeaderElectionEnable: int
        :param RetentionMs: Message retention period in ms. The current minimum value is 60,000 ms.
        :type RetentionMs: int
        :param SegmentMs: Segment rolling duration in ms. The current minimum value is 86,400,000 ms.
        :type SegmentMs: int
        :param MaxMessageBytes: Maximum topic message length in bytes. The maximum value is 8,388,608 bytes (i.e., 8 MB).
        :type MaxMessageBytes: int
        :param CleanUpPolicy: Message deletion policy. Valid values: delete, compact
        :type CleanUpPolicy: str
        """
        self.InstanceId = None
        self.TopicName = None
        self.Note = None
        self.EnableWhiteList = None
        self.MinInsyncReplicas = None
        self.UncleanLeaderElectionEnable = None
        self.RetentionMs = None
        self.SegmentMs = None
        self.MaxMessageBytes = None
        self.CleanUpPolicy = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.Note = params.get("Note")
        self.EnableWhiteList = params.get("EnableWhiteList")
        self.MinInsyncReplicas = params.get("MinInsyncReplicas")
        self.UncleanLeaderElectionEnable = params.get("UncleanLeaderElectionEnable")
        self.RetentionMs = params.get("RetentionMs")
        self.SegmentMs = params.get("SegmentMs")
        self.MaxMessageBytes = params.get("MaxMessageBytes")
        self.CleanUpPolicy = params.get("CleanUpPolicy")


class ModifyTopicAttributesResponse(AbstractModel):
    """ModifyTopicAttributes response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result set
        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = JgwOperateResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class OperateResponseData(AbstractModel):
    """Data structure returned by operation

    """

    def __init__(self):
        """
        :param FlowId: FlowId
Note: this field may return null, indicating that no valid values can be obtained.
        :type FlowId: int
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")


class Partition(AbstractModel):
    """Partition entity

    """

    def __init__(self):
        """
        :param PartitionId: Partition ID
        :type PartitionId: int
        """
        self.PartitionId = None


    def _deserialize(self, params):
        self.PartitionId = params.get("PartitionId")


class PartitionOffset(AbstractModel):
    """Partition and offset

    """

    def __init__(self):
        """
        :param Partition: Partition, such as "0" or "1"
Note: this field may return null, indicating that no valid values can be obtained.
        :type Partition: str
        :param Offset: Offset, such as 100
Note: this field may return null, indicating that no valid values can be obtained.
        :type Offset: int
        """
        self.Partition = None
        self.Offset = None


    def _deserialize(self, params):
        self.Partition = params.get("Partition")
        self.Offset = params.get("Offset")


class Route(AbstractModel):
    """Route entity object

    """

    def __init__(self):
        """
        :param AccessType: Instance connection method
0: PLAINTEXT (plaintext method, which does not carry user information and is supported for legacy versions and Community Edition)
1: SASL_PLAINTEXT (plaintext method, which authenticates the login through SASL before data start and is supported only for Community Edition)
2: SSL (SSL-encrypted communication, which does not carry user information and is supported for legacy versions and Community Edition)
3: SASL_SSL (SSL-encrypted communication, which authenticates the login through SASL before data start and is supported only for Community Edition)
        :type AccessType: int
        :param RouteId: Route ID
        :type RouteId: int
        :param VipType: VIP network type (1: public network TGW; 2: classic network; 3: VPC; 4: Tencent Cloud-supported environment (generally used for internal instances); 5: SSL public network access; 6: BM VPC)
        :type VipType: int
        :param VipList: Virtual IP list
        :type VipList: list of VipEntity
        :param Domain: Domain name
Note: this field may return null, indicating that no valid values can be obtained.
        :type Domain: str
        :param DomainPort: Domain name port
Note: this field may return null, indicating that no valid values can be obtained.
        :type DomainPort: int
        """
        self.AccessType = None
        self.RouteId = None
        self.VipType = None
        self.VipList = None
        self.Domain = None
        self.DomainPort = None


    def _deserialize(self, params):
        self.AccessType = params.get("AccessType")
        self.RouteId = params.get("RouteId")
        self.VipType = params.get("VipType")
        if params.get("VipList") is not None:
            self.VipList = []
            for item in params.get("VipList"):
                obj = VipEntity()
                obj._deserialize(item)
                self.VipList.append(obj)
        self.Domain = params.get("Domain")
        self.DomainPort = params.get("DomainPort")


class RouteResponse(AbstractModel):
    """Returned object for route information

    """

    def __init__(self):
        """
        :param Routers: Route information list
Note: this field may return null, indicating that no valid values can be obtained.
        :type Routers: list of Route
        """
        self.Routers = None


    def _deserialize(self, params):
        if params.get("Routers") is not None:
            self.Routers = []
            for item in params.get("Routers"):
                obj = Route()
                obj._deserialize(item)
                self.Routers.append(obj)


class SubscribedInfo(AbstractModel):
    """Subscribed message entity

    """

    def __init__(self):
        """
        :param TopicName: Subscribed topic name
        :type TopicName: str
        :param Partition: Subscribed partition
Note: this field may return null, indicating that no valid values can be obtained.
        :type Partition: list of int
        :param PartitionOffset: Partition offset information
Note: this field may return null, indicating that no valid values can be obtained.
        :type PartitionOffset: list of PartitionOffset
        :param TopicId: ID of the subscribed topic. 
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicId: str
        """
        self.TopicName = None
        self.Partition = None
        self.PartitionOffset = None
        self.TopicId = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.Partition = params.get("Partition")
        if params.get("PartitionOffset") is not None:
            self.PartitionOffset = []
            for item in params.get("PartitionOffset"):
                obj = PartitionOffset()
                obj._deserialize(item)
                self.PartitionOffset.append(obj)
        self.TopicId = params.get("TopicId")


class Tag(AbstractModel):
    """Tag object in instance details

    """

    def __init__(self):
        """
        :param TagKey: Tag key
        :type TagKey: str
        :param TagValue: Tag value
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class Topic(AbstractModel):
    """Returned topic object

    """

    def __init__(self):
        """
        :param TopicId: Topic ID
        :type TopicId: str
        :param TopicName: Topic name
        :type TopicName: str
        :param Note: Remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :type Note: str
        """
        self.TopicId = None
        self.TopicName = None
        self.Note = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.Note = params.get("Note")


class TopicAttributesResponse(AbstractModel):
    """Returned topic attributes result entity

    """

    def __init__(self):
        """
        :param TopicId: Topic ID
        :type TopicId: str
        :param CreateTime: Creation time
        :type CreateTime: int
        :param Note: Topic remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :type Note: str
        :param PartitionNum: Number of partitions
        :type PartitionNum: int
        :param EnableWhiteList: IP allowlist switch. 1: enabled, 0: disabled
        :type EnableWhiteList: int
        :param IpWhiteList: IP allowlist list
        :type IpWhiteList: list of str
        :param Config: Topic configuration array
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.Config`
        :param Partitions: Partition details
        :type Partitions: list of TopicPartitionDO
        """
        self.TopicId = None
        self.CreateTime = None
        self.Note = None
        self.PartitionNum = None
        self.EnableWhiteList = None
        self.IpWhiteList = None
        self.Config = None
        self.Partitions = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.CreateTime = params.get("CreateTime")
        self.Note = params.get("Note")
        self.PartitionNum = params.get("PartitionNum")
        self.EnableWhiteList = params.get("EnableWhiteList")
        self.IpWhiteList = params.get("IpWhiteList")
        if params.get("Config") is not None:
            self.Config = Config()
            self.Config._deserialize(params.get("Config"))
        if params.get("Partitions") is not None:
            self.Partitions = []
            for item in params.get("Partitions"):
                obj = TopicPartitionDO()
                obj._deserialize(item)
                self.Partitions.append(obj)


class TopicDetail(AbstractModel):
    """Topic details

    """

    def __init__(self):
        """
        :param TopicName: Topic name
        :type TopicName: str
        :param TopicId: Topic ID
        :type TopicId: str
        :param PartitionNum: Number of partitions
        :type PartitionNum: int
        :param ReplicaNum: Number of replicas
        :type ReplicaNum: int
        :param Note: Remarks
Note: this field may return null, indicating that no valid values can be obtained.
        :type Note: str
        :param CreateTime: Creation time
        :type CreateTime: int
        :param EnableWhiteList: Whether to enable IP authentication allowlist. true: yes, false: no
        :type EnableWhiteList: bool
        :param IpWhiteListCount: Number of IPs in IP allowlist
        :type IpWhiteListCount: int
        :param ForwardCosBucket: COS bucket for data backup: address of the destination COS bucket
Note: this field may return null, indicating that no valid values can be obtained.
        :type ForwardCosBucket: str
        :param ForwardStatus: Status of data backup to COS. 1: not enabled, 0: enabled
        :type ForwardStatus: int
        :param ForwardInterval: Frequency of data backup to COS
        :type ForwardInterval: int
        :param Config: Advanced configuration
Note: this field may return null, indicating that no valid values can be obtained.
        :type Config: :class:`tencentcloud.ckafka.v20190819.models.Config`
        :param RetentionTimeConfig: Message retention time configuration (for recording the latest retention time)
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type RetentionTimeConfig: :class:`tencentcloud.ckafka.v20190819.models.TopicRetentionTimeConfigRsp`
        """
        self.TopicName = None
        self.TopicId = None
        self.PartitionNum = None
        self.ReplicaNum = None
        self.Note = None
        self.CreateTime = None
        self.EnableWhiteList = None
        self.IpWhiteListCount = None
        self.ForwardCosBucket = None
        self.ForwardStatus = None
        self.ForwardInterval = None
        self.Config = None
        self.RetentionTimeConfig = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.TopicId = params.get("TopicId")
        self.PartitionNum = params.get("PartitionNum")
        self.ReplicaNum = params.get("ReplicaNum")
        self.Note = params.get("Note")
        self.CreateTime = params.get("CreateTime")
        self.EnableWhiteList = params.get("EnableWhiteList")
        self.IpWhiteListCount = params.get("IpWhiteListCount")
        self.ForwardCosBucket = params.get("ForwardCosBucket")
        self.ForwardStatus = params.get("ForwardStatus")
        self.ForwardInterval = params.get("ForwardInterval")
        if params.get("Config") is not None:
            self.Config = Config()
            self.Config._deserialize(params.get("Config"))
        if params.get("RetentionTimeConfig") is not None:
            self.RetentionTimeConfig = TopicRetentionTimeConfigRsp()
            self.RetentionTimeConfig._deserialize(params.get("RetentionTimeConfig"))


class TopicDetailResponse(AbstractModel):
    """Returned topic details entity

    """

    def __init__(self):
        """
        :param TopicList: List of returned topic details
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicList: list of TopicDetail
        :param TotalCount: Number of all eligible topic details
        :type TotalCount: int
        """
        self.TopicList = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("TopicList") is not None:
            self.TopicList = []
            for item in params.get("TopicList"):
                obj = TopicDetail()
                obj._deserialize(item)
                self.TopicList.append(obj)
        self.TotalCount = params.get("TotalCount")


class TopicPartitionDO(AbstractModel):
    """Partition details

    """

    def __init__(self):
        """
        :param Partition: Partition ID
        :type Partition: int
        :param LeaderStatus: Leader running status
        :type LeaderStatus: int
        :param IsrNum: ISR quantity
        :type IsrNum: int
        :param ReplicaNum: Number of replicas
        :type ReplicaNum: int
        """
        self.Partition = None
        self.LeaderStatus = None
        self.IsrNum = None
        self.ReplicaNum = None


    def _deserialize(self, params):
        self.Partition = params.get("Partition")
        self.LeaderStatus = params.get("LeaderStatus")
        self.IsrNum = params.get("IsrNum")
        self.ReplicaNum = params.get("ReplicaNum")


class TopicResult(AbstractModel):
    """`TopicResponse` returned uniformly

    """

    def __init__(self):
        """
        :param TopicList: List of returned topic information
Note: this field may return null, indicating that no valid values can be obtained.
        :type TopicList: list of Topic
        :param TotalCount: Number of eligible topics
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        """
        self.TopicList = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("TopicList") is not None:
            self.TopicList = []
            for item in params.get("TopicList"):
                obj = Topic()
                obj._deserialize(item)
                self.TopicList.append(obj)
        self.TotalCount = params.get("TotalCount")


class TopicRetentionTimeConfigRsp(AbstractModel):
    """Information returned for topic message retention time configuration

    """

    def __init__(self):
        """
        :param Expect: Expected value, i.e., the topic message retention time (min) configured
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Expect: int
        :param Current: Current value (min), i.e., the retention time currently in effect, which may be dynamically adjusted
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type Current: int
        :param ModTimeStamp: Last modified time
Note: `null` may be returned for this field, indicating that no valid values can be obtained.
        :type ModTimeStamp: int
        """
        self.Expect = None
        self.Current = None
        self.ModTimeStamp = None


    def _deserialize(self, params):
        self.Expect = params.get("Expect")
        self.Current = params.get("Current")
        self.ModTimeStamp = params.get("ModTimeStamp")


class User(AbstractModel):
    """User entity

    """

    def __init__(self):
        """
        :param UserId: User ID
        :type UserId: int
        :param Name: Username
        :type Name: str
        :param CreateTime: Creation time
        :type CreateTime: str
        :param UpdateTime: Last updated time
        :type UpdateTime: str
        """
        self.UserId = None
        self.Name = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Name = params.get("Name")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class UserResponse(AbstractModel):
    """Returned user entity

    """

    def __init__(self):
        """
        :param Users: List of eligible users
Note: this field may return null, indicating that no valid values can be obtained.
        :type Users: list of User
        :param TotalCount: Total number of eligible users
        :type TotalCount: int
        """
        self.Users = None
        self.TotalCount = None


    def _deserialize(self, params):
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = User()
                obj._deserialize(item)
                self.Users.append(obj)
        self.TotalCount = params.get("TotalCount")


class VipEntity(AbstractModel):
    """Virtual IP entity

    """

    def __init__(self):
        """
        :param Vip: Virtual IP
        :type Vip: str
        :param Vport: Virtual port
        :type Vport: str
        """
        self.Vip = None
        self.Vport = None


    def _deserialize(self, params):
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")