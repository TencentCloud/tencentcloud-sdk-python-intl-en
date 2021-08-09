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


class Acl(AbstractModel):
    """ACL object entity

    """

    def __init__(self):
        """
        :param ResourceType: ACL resource type. 0: UNKNOWN, 1: ANY, 2: TOPIC, 3: GROUP, 4: CLUSTER, 5: TRANSACTIONAL_ID. Currently, only `TOPIC` is available,\n        :type ResourceType: int\n        :param ResourceName: Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name\n        :type ResourceName: str\n        :param Principal: User list. The default value is `User:*`, which means that any user can access. The current user can only be one included in the user list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Principal: str\n        :param Host: The default value is `*`, which means that any host can access. Currently, CKafka does not support the host as `*`, but the future product based on the open-source Kafka will directly support this
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Host: str\n        :param Operation: ACL operation mode. 0: UNKNOWN, 1: ANY, 2: ALL, 3: READ, 4: WRITE, 5: CREATE, 6: DELETE, 7: ALTER, 8: DESCRIBE, 9: CLUSTER_ACTION, 10: DESCRIBE_CONFIGS, 11: ALTER_CONFIGS, 12: IDEMPOTEN_WRITE\n        :type Operation: int\n        :param PermissionType: Permission type. 0: UNKNOWN, 1: ANY, 2: DENY, 3: ALLOW\n        :type PermissionType: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclResponse(AbstractModel):
    """Set of returned ACL results

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible data entries\n        :type TotalCount: int\n        :param AclList: ACL list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AclList: list of Acl\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppIdResponse(AbstractModel):
    """`AppId` query result

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible `AppId`\n        :type TotalCount: int\n        :param AppIdList: List of eligible `AppId`
Note: this field may return null, indicating that no valid values can be obtained.\n        :type AppIdList: list of int\n        """
        self.TotalCount = None
        self.AppIdList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.AppIdList = params.get("AppIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Assignment(AbstractModel):
    """Stores the information of partition assigned to this consumer

    """

    def __init__(self):
        """
        :param Version: Assignment version information\n        :type Version: int\n        :param Topics: Topic information list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Topics: list of GroupInfoTopics\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterInfo(AbstractModel):
    """Cluster information entity

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID\n        :type ClusterId: int\n        :param ClusterName: Cluster name\n        :type ClusterName: str\n        :param MaxDiskSize: The cluster’s maximum disk capacity in GB
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type MaxDiskSize: int\n        :param MaxBandWidth: The cluster’s maximum bandwidth in MB/s
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type MaxBandWidth: int\n        :param AvailableDiskSize: The cluster’s available disk capacity in GB
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type AvailableDiskSize: int\n        :param AvailableBandWidth: The cluster’s available bandwidth in MB/s
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type AvailableBandWidth: int\n        :param ZoneId: The AZ where the cluster resides
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type ZoneId: int\n        :param ZoneIds: The AZ where the cluster nodes reside. If the cluster is a multi-AZ cluster, this field means multiple AZs where the cluster nodes reside.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type ZoneIds: list of int\n        """
        self.ClusterId = None
        self.ClusterName = None
        self.MaxDiskSize = None
        self.MaxBandWidth = None
        self.AvailableDiskSize = None
        self.AvailableBandWidth = None
        self.ZoneId = None
        self.ZoneIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.MaxDiskSize = params.get("MaxDiskSize")
        self.MaxBandWidth = params.get("MaxBandWidth")
        self.AvailableDiskSize = params.get("AvailableDiskSize")
        self.AvailableBandWidth = params.get("AvailableBandWidth")
        self.ZoneId = params.get("ZoneId")
        self.ZoneIds = params.get("ZoneIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Config(AbstractModel):
    """Advanced configuration object

    """

    def __init__(self):
        """
        :param Retention: Message retention period
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Retention: int\n        :param MinInsyncReplicas: Minimum number of sync replications
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MinInsyncReplicas: int\n        :param CleanUpPolicy: Log cleanup mode. Default value: delete.
delete: logs will be deleted by save time; compact: logs will be compressed by key; compact, delete: logs will be compressed by key and deleted by save time.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type CleanUpPolicy: str\n        :param SegmentMs: Segment rolling duration
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SegmentMs: int\n        :param UncleanLeaderElectionEnable: 0: false, 1: true.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type UncleanLeaderElectionEnable: int\n        :param SegmentBytes: Number of bytes for segment rolling
Note: this field may return null, indicating that no valid values can be obtained.\n        :type SegmentBytes: int\n        :param MaxMessageBytes: Maximum number of message bytes
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MaxMessageBytes: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerGroup(AbstractModel):
    """User group entity

    """

    def __init__(self):
        """
        :param ConsumerGroupName: User group name\n        :type ConsumerGroupName: str\n        :param SubscribedInfo: Subscribed message entity\n        :type SubscribedInfo: list of SubscribedInfo\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerGroupResponse(AbstractModel):
    """Returned consumer group result entity

    """

    def __init__(self):
        """
        :param TotalCount: Number of eligible consumer groups\n        :type TotalCount: int\n        :param TopicList: Topic list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TopicList: list of ConsumerGroupTopic\n        :param GroupList: Consumer group list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type GroupList: list of ConsumerGroup\n        :param TotalPartition: Total number of partitions
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalPartition: int\n        :param PartitionListForMonitor: List of monitored partitions
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PartitionListForMonitor: list of Partition\n        :param TotalTopic: Total number of topics
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalTopic: int\n        :param TopicListForMonitor: List of monitored topics
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TopicListForMonitor: list of ConsumerGroupTopic\n        :param GroupListForMonitor: List of monitored groups
Note: this field may return null, indicating that no valid values can be obtained.\n        :type GroupListForMonitor: list of Group\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumerGroupTopic(AbstractModel):
    """Consumer group topic object

    """

    def __init__(self):
        """
        :param TopicId: Topic ID\n        :type TopicId: str\n        :param TopicName: Topic name\n        :type TopicName: str\n        """
        self.TopicId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAclRequest(AbstractModel):
    """CreateAcl request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID information\n        :type InstanceId: str\n        :param ResourceType: ACL resource type. 0: UNKNOWN, 1: ANY, 2: TOPIC, 3: GROUP, 4: CLUSTER, 5: TRANSACTIONAL_ID. Currently, only `TOPIC` is available, and other fields will be used for future ACLs compatible with open-source Kafka\n        :type ResourceType: int\n        :param Operation: ACL operation mode. 0: UNKNOWN, 1: ANY, 2: ALL, 3: READ, 4: WRITE, 5: CREATE, 6: DELETE, 7: ALTER, 8: DESCRIBE, 9: CLUSTER_ACTION, 10: DESCRIBE_CONFIGS, 11: ALTER_CONFIGS\n        :type Operation: int\n        :param PermissionType: Permission type. 0: UNKNOWN, 1: ANY, 2: DENY, 3: ALLOW. Currently, CKafka supports `ALLOW` (equivalent to allowlist), and other fields will be used for future ACLs compatible with open-source Kafka\n        :type PermissionType: int\n        :param ResourceName: Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name\n        :type ResourceName: str\n        :param Host: The default value is `*`, which means that any host can access. Currently, CKafka does not support the host as `*`, but the future product based on the open-source Kafka will directly support this\n        :type Host: str\n        :param Principal: The list of users allowed to access the topic. Default: User:*, meaning all users. The current user must be in the user list. Add `User:` before the user name (`User:A` for example).\n        :type Principal: str\n        """
        self.InstanceId = None
        self.ResourceType = None
        self.Operation = None
        self.PermissionType = None
        self.ResourceName = None
        self.Host = None
        self.Principal = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ResourceType = params.get("ResourceType")
        self.Operation = params.get("Operation")
        self.PermissionType = params.get("PermissionType")
        self.ResourceName = params.get("ResourceName")
        self.Host = params.get("Host")
        self.Principal = params.get("Principal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAclResponse(AbstractModel):
    """CreateAcl response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param TopicName: Topic name\n        :type TopicName: str\n        :param PartitionNum: Number of topic partitions\n        :type PartitionNum: int\n        """
        self.InstanceId = None
        self.TopicName = None
        self.PartitionNum = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.PartitionNum = params.get("PartitionNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePartitionResponse(AbstractModel):
    """CreatePartition response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result set\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param TopicName: Topic name\n        :type TopicName: str\n        :param IpWhiteList: IP allowlist list\n        :type IpWhiteList: list of str\n        """
        self.InstanceId = None
        self.TopicName = None
        self.IpWhiteList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.IpWhiteList = params.get("IpWhiteList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicIpWhiteListResponse(AbstractModel):
    """CreateTopicIpWhiteList response structure.

    """

    def __init__(self):
        """
        :param Result: Result of deleting topic IP allowlist\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param TopicName: Topic name string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)\n        :type TopicName: str\n        :param PartitionNum: Number of partitions, which should be greater than 0\n        :type PartitionNum: int\n        :param ReplicaNum: Number of replicas, which cannot be higher than the number of brokers. Maximum value: 3\n        :type ReplicaNum: int\n        :param EnableWhiteList: IP allowlist switch. 1: enabled, 0: disabled. Default value: 0\n        :type EnableWhiteList: int\n        :param IpWhiteList: IP allowlist list for quota limit, which is required if `enableWhileList` is 1\n        :type IpWhiteList: list of str\n        :param CleanUpPolicy: Log cleanup policy, which is `delete` by default. `delete`: logs will be deleted by save time; `compact`: logs will be compressed by key; `compact, delete`: logs will be compressed by key and deleted by save time.\n        :type CleanUpPolicy: str\n        :param Note: Topic remarks string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)\n        :type Note: str\n        :param MinInsyncReplicas: Default value: 1\n        :type MinInsyncReplicas: int\n        :param UncleanLeaderElectionEnable: Whether to allow an unsynced replica to be elected as leader. false: no, true: yes. Default value: false\n        :type UncleanLeaderElectionEnable: int\n        :param RetentionMs: Message retention period in ms, which is optional. The current minimum value is 60,000 ms\n        :type RetentionMs: int\n        :param SegmentMs: Segment rolling duration in ms. The current minimum value is 3,600,000 ms\n        :type SegmentMs: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResp(AbstractModel):
    """Return for topic creation

    """

    def __init__(self):
        """
        :param TopicId: Topic ID\n        :type TopicId: str\n        """
        self.TopicId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
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
        :param Result: Returned creation result\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicResp`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param Name: Username\n        :type Name: str\n        :param Password: User password\n        :type Password: str\n        """
        self.InstanceId = None
        self.Name = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserResponse(AbstractModel):
    """CreateUser response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID information\n        :type InstanceId: str\n        :param ResourceType: ACL resource type. 0: UNKNOWN, 1: ANY, 2: TOPIC, 3: GROUP, 4: CLUSTER, 5: TRANSACTIONAL_ID. Currently, only `TOPIC` is available, and other fields will be used for future ACLs compatible with open-source Kafka\n        :type ResourceType: int\n        :param ResourceName: Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name\n        :type ResourceName: str\n        :param Operation: ACL operation mode. 0: UNKNOWN, 1: ANY, 2: ALL, 3: READ, 4: WRITE, 5: CREATE, 6: DELETE, 7: ALTER, 8: DESCRIBE, 9: CLUSTER_ACTION, 10: DESCRIBE_CONFIGS, 11: ALTER_CONFIGS, 12: IDEMPOTEN_WRITE. Currently, CKafka only supports `READ` and `WRITE`, and other values will be used for future ACLs compatible with open-source Kafka\n        :type Operation: int\n        :param PermissionType: Permission type. 0: UNKNOWN, 1: ANY, 2: DENY, 3: ALLOW. Currently, CKafka supports `ALLOW` (equivalent to allowlist), and other fields will be used for future ACLs compatible with open-source Kafka\n        :type PermissionType: int\n        :param Host: The default value is `*`, which means that any host can access. Currently, CKafka does not support the host as `*`, but the future product based on the open-source Kafka will directly support this\n        :type Host: str\n        :param Principal: User list. The default value is `*`, which means that any user can access. The current user can only be one included in the user list\n        :type Principal: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAclResponse(AbstractModel):
    """DeleteAcl response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param TopicName: Topic name\n        :type TopicName: str\n        :param IpWhiteList: IP allowlist list\n        :type IpWhiteList: list of str\n        """
        self.InstanceId = None
        self.TopicName = None
        self.IpWhiteList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        self.IpWhiteList = params.get("IpWhiteList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicIpWhiteListResponse(AbstractModel):
    """DeleteTopicIpWhiteList response structure.

    """

    def __init__(self):
        """
        :param Result: Result of deleting topic IP allowlist\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: CKafka instance ID\n        :type InstanceId: str\n        :param TopicName: CKafka topic name\n        :type TopicName: str\n        """
        self.InstanceId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
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
        :param Result: Returned result set\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param Name: Username\n        :type Name: str\n        """
        self.InstanceId = None
        self.Name = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserResponse(AbstractModel):
    """DeleteUser response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param ResourceType: ACL resource type. 0: UNKNOWN, 1: ANY, 2: TOPIC, 3: GROUP, 4: CLUSTER, 5: TRANSACTIONAL_ID. Currently, only `TOPIC` is available, and other fields will be used for future ACLs compatible with open-source Kafka\n        :type ResourceType: int\n        :param ResourceName: Resource name, which is related to `resourceType`. For example, if `resourceType` is `TOPIC`, this field indicates the topic name; if `resourceType` is `GROUP`, this field indicates the group name\n        :type ResourceName: str\n        :param Offset: Offset position\n        :type Offset: int\n        :param Limit: Quantity limit\n        :type Limit: int\n        :param SearchWord: Keyword match\n        :type SearchWord: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeACLResponse(AbstractModel):
    """DescribeACL response structure.

    """

    def __init__(self):
        """
        :param Result: Returned ACL result set object\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.AclResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Offset: Offset position\n        :type Offset: int\n        :param Limit: Maximum number of users to be queried in this request. Maximum value: 50. Default value: 50\n        :type Limit: int\n        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppInfoResponse(AbstractModel):
    """DescribeAppInfo response structure.

    """

    def __init__(self):
        """
        :param Result: Returned list of eligible `AppId`\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.AppIdResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = AppIdResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeCkafkaZoneRequest(AbstractModel):
    """DescribeCkafkaZone request structure.

    """


class DescribeCkafkaZoneResponse(AbstractModel):
    """DescribeCkafkaZone response structure.

    """

    def __init__(self):
        """
        :param Result: Returned results for the query\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ZoneResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ZoneResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeConsumerGroupRequest(AbstractModel):
    """DescribeConsumerGroup request structure.

    """

    def __init__(self):
        """
        :param InstanceId: CKafka instance ID.\n        :type InstanceId: str\n        :param GroupName: Name of the group to be queried, which is optional.\n        :type GroupName: str\n        :param TopicName: Name of the corresponding topic in the group to be queried, which is optional. If this parameter is specified but `group` is not specified, this parameter will be ignored.\n        :type TopicName: str\n        :param Limit: Number of results to be returned in this request\n        :type Limit: int\n        :param Offset: Offset position\n        :type Offset: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConsumerGroupResponse(AbstractModel):
    """DescribeConsumerGroup response structure.

    """

    def __init__(self):
        """
        :param Result: Returned consumer group information\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.ConsumerGroupResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param Group: groupId\n        :type Group: str\n        :param Protocol: Protocol used by the group.\n        :type Protocol: str\n        """
        self.Group = None
        self.Protocol = None


    def _deserialize(self, params):
        self.Group = params.get("Group")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupInfoRequest(AbstractModel):
    """DescribeGroupInfo request structure.

    """

    def __init__(self):
        """
        :param InstanceId: (Filter) filter by instance ID.\n        :type InstanceId: str\n        :param GroupList: Kafka consumer group (`Consumer-group`), which is an array in the format of `GroupList.0=xxx&GroupList.1=yyy`.\n        :type GroupList: list of str\n        """
        self.InstanceId = None
        self.GroupList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.GroupList = params.get("GroupList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupInfoResponse(AbstractModel):
    """DescribeGroupInfo response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: list of GroupInfoResponse\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: (Filter) filter by instance ID\n        :type InstanceId: str\n        :param Group: Kafka consumer group\n        :type Group: str\n        :param Topics: Array of the names of topics subscribed to by a group. If there is no such array, this parameter means the information of all topics in the specified group\n        :type Topics: list of str\n        :param SearchWord: Fuzzy match by `topicName`\n        :type SearchWord: str\n        :param Offset: Offset position of this query. Default value: 0\n        :type Offset: int\n        :param Limit: Maximum number of results to be returned in this request. Default value: 50. Maximum value: 50\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupOffsetsResponse(AbstractModel):
    """DescribeGroupOffsets response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result object\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.GroupOffsetResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param SearchWord: Search keyword\n        :type SearchWord: str\n        :param Offset: Offset\n        :type Offset: int\n        :param Limit: Maximum number of results to be returned\n        :type Limit: int\n        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupResponse(AbstractModel):
    """DescribeGroup response structure.

    """

    def __init__(self):
        """
        :param Result: List of returned results\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.GroupResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceAttributesResponse(AbstractModel):
    """DescribeInstanceAttributes response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result object of instance attributes\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceAttributesResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: (Filter) filter by instance ID\n        :type InstanceId: str\n        :param SearchWord: (Filter) filter by instance name. Fuzzy search is supported\n        :type SearchWord: str\n        :param Status: (Filter) instance status. 0: creating, 1: running, 2: deleting. If this parameter is left empty, all instances will be returned by default\n        :type Status: list of int\n        :param Offset: Offset. If this parameter is left empty, 0 will be used by default\n        :type Offset: int\n        :param Limit: Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 20\n        :type Limit: int\n        :param TagKey: Tag key match.\n        :type TagKey: str\n        :param Filters: Filter\n        :type Filters: list of Filter\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesDetailResponse(AbstractModel):
    """DescribeInstancesDetail response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result object of instance details\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceDetailResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: (Filter) filter by instance ID\n        :type InstanceId: str\n        :param SearchWord: (Filter) filter by instance name. Fuzzy search is supported\n        :type SearchWord: str\n        :param Status: (Filter) instance status. 0: creating, 1: running, 2: deleting. If this parameter is left empty, all instances will be returned by default\n        :type Status: list of int\n        :param Offset: Offset. If this parameter is left empty, 0 will be used by default\n        :type Offset: int\n        :param Limit: Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 100.\n        :type Limit: int\n        :param TagKey: Tag key match.\n        :type TagKey: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.InstanceResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = InstanceResponse()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeRegionRequest(AbstractModel):
    """DescribeRegion request structure.

    """

    def __init__(self):
        """
        :param Offset: The offset value\n        :type Offset: int\n        :param Limit: The maximum number of results returned\n        :type Limit: int\n        :param Business: Business field, which can be ignored.\n        :type Business: str\n        """
        self.Offset = None
        self.Limit = None
        self.Business = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Business = params.get("Business")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegionResponse(AbstractModel):
    """DescribeRegion response structure.

    """

    def __init__(self):
        """
        :param Result: List of the returned results of enumerated regions
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type Result: list of Region\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = Region()
                obj._deserialize(item)
                self.Result.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRouteRequest(AbstractModel):
    """DescribeRoute request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Unique instance ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRouteResponse(AbstractModel):
    """DescribeRoute response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result set of route information\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.RouteResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param TopicName: Topic name\n        :type TopicName: str\n        """
        self.InstanceId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicAttributesResponse(AbstractModel):
    """DescribeTopicAttributes response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result object\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicAttributesResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param SearchWord: (Filter) filter by `topicName`. Fuzzy search is supported\n        :type SearchWord: str\n        :param Offset: Offset. If this parameter is left empty, 0 will be used by default\n        :type Offset: int\n        :param Limit: Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 20. This value must be greater than 0\n        :type Limit: int\n        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
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
        :param Result: Returned entity of topic details\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicDetailResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param SearchWord: Filter by `topicName`. Fuzzy search is supported\n        :type SearchWord: str\n        :param Offset: Offset. If this parameter is left empty, 0 will be used by default\n        :type Offset: int\n        :param Limit: Number of results to be returned. If this parameter is left empty, 10 will be used by default. The maximum value is 20\n        :type Limit: int\n        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicResponse(AbstractModel):
    """DescribeTopic response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.TopicResult`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param SearchWord: Filter by name\n        :type SearchWord: str\n        :param Offset: Offset\n        :type Offset: int\n        :param Limit: Number of results to be returned in this request\n        :type Limit: int\n        """
        self.InstanceId = None
        self.SearchWord = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SearchWord = params.get("SearchWord")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserResponse(AbstractModel):
    """DescribeUser response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result list\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.UserResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type Enable: int\n        :param DiskQuotaPercentage: Disk quota threshold (in percentage) for triggering the message retention time change event
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type DiskQuotaPercentage: int\n        :param StepForwardPercentage: Percentage by which the message retention time is shortened each time
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type StepForwardPercentage: int\n        :param BottomRetention: Minimum retention time, in minutes
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type BottomRetention: int\n        """
        self.Enable = None
        self.DiskQuotaPercentage = None
        self.StepForwardPercentage = None
        self.BottomRetention = None


    def _deserialize(self, params):
        self.Enable = params.get("Enable")
        self.DiskQuotaPercentage = params.get("DiskQuotaPercentage")
        self.StepForwardPercentage = params.get("StepForwardPercentage")
        self.BottomRetention = params.get("BottomRetention")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Query filter
    >Key-value pair filters for conditional filtering queries, such as filter ID, name, and status
    > * If there are multiple `Filter`, the relationship among them is logical `AND`.
    > * If there are multiple `Values` in the same `Filter`, the relationship among them is logical `OR`.
    >

    """

    def __init__(self):
        """
        :param Name: Field to be filtered.\n        :type Name: str\n        :param Values: Filter value of field.\n        :type Values: list of str\n        """
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
        


class Group(AbstractModel):
    """Group entity

    """

    def __init__(self):
        """
        :param GroupName: Group name\n        :type GroupName: str\n        """
        self.GroupName = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfoMember(AbstractModel):
    """Consumer information

    """

    def __init__(self):
        """
        :param MemberId: Unique ID generated for consumer in consumer group by coordinator\n        :type MemberId: str\n        :param ClientId: `client.id` information by the client consumer SDK\n        :type ClientId: str\n        :param ClientHost: Generally stores client IP address\n        :type ClientHost: str\n        :param Assignment: Stores the information of partition assigned to this consumer\n        :type Assignment: :class:`tencentcloud.ckafka.v20190819.models.Assignment`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfoResponse(AbstractModel):
    """`GroupInfo` response data entity

    """

    def __init__(self):
        """
        :param ErrorCode: Error code. 0: success\n        :type ErrorCode: str\n        :param State: Group status description (common valid values: Empty, Stable, Dead):
Dead: the consumer group does not exist
Empty: there are currently no consumer subscriptions in the consumer group
PreparingRebalance: the consumer group is currently in `rebalance` state
CompletingRebalance: the consumer group is currently in `rebalance` state
Stable: each consumer in the consumer group has joined and is in stable state\n        :type State: str\n        :param ProtocolType: The type of protocol selected by the consumer group, which is `consumer` for common consumers. However, some systems use their own protocols; for example, the protocol used by kafka-connect is `connect`. Only with the standard `consumer` protocol can this API get to know the specific assigning method and parse the specific partition assignment\n        :type ProtocolType: str\n        :param Protocol: Consumer partition assignment algorithm, such as `range` (which is the default value for the Kafka consumer SDK), `roundrobin`, and `sticky`\n        :type Protocol: str\n        :param Members: This array contains information only if `state` is `Stable` and `protocol_type` is `consumer`\n        :type Members: list of GroupInfoMember\n        :param Group: Kafka consumer group\n        :type Group: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupInfoTopics(AbstractModel):
    """Internal topic object of `GroupInfo`

    """

    def __init__(self):
        """
        :param Topic: Name of assigned topics\n        :type Topic: str\n        :param Partitions: Information of assigned partition
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Partitions: list of int\n        """
        self.Topic = None
        self.Partitions = None


    def _deserialize(self, params):
        self.Topic = params.get("Topic")
        self.Partitions = params.get("Partitions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupOffsetPartition(AbstractModel):
    """Group offset partition object

    """

    def __init__(self):
        """
        :param Partition: Topic `partitionId`\n        :type Partition: int\n        :param Offset: Offset position submitted by consumer\n        :type Offset: int\n        :param Metadata: Metadata can be passed in for other purposes when the consumer submits messages. Currently, this parameter is usually an empty string
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Metadata: str\n        :param ErrorCode: Error code\n        :type ErrorCode: int\n        :param LogEndOffset: Latest offset of current partition\n        :type LogEndOffset: int\n        :param Lag: Number of unconsumed messages\n        :type Lag: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupOffsetResponse(AbstractModel):
    """Returned result of consumer group offset

    """

    def __init__(self):
        """
        :param TotalCount: Total number of eligible results\n        :type TotalCount: int\n        :param TopicList: Array of partitions in the topic, where each element is a JSON object
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TopicList: list of GroupOffsetTopic\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupOffsetTopic(AbstractModel):
    """Consumer group topic object

    """

    def __init__(self):
        """
        :param Topic: Topic name\n        :type Topic: str\n        :param Partitions: Array of partitions in the topic, where each element is a JSON object
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Partitions: list of GroupOffsetPartition\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupResponse(AbstractModel):
    """`DescribeGroup` response

    """

    def __init__(self):
        """
        :param TotalCount: Count
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        :param GroupList: GroupList
Note: this field may return null, indicating that no valid values can be obtained.\n        :type GroupList: list of DescribeGroup\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    """Instance object

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param InstanceName: Instance name\n        :type InstanceName: str\n        :param Status: Instance status. 0: creating, 1: running, 2: deleting, 5: isolated, -1: creation failed\n        :type Status: int\n        :param IfCommunity: Whether it is an open-source instance. true: yes, false: no
Note: this field may return null, indicating that no valid values can be obtained.\n        :type IfCommunity: bool\n        """
        self.InstanceId = None
        self.InstanceName = None
        self.Status = None
        self.IfCommunity = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Status = params.get("Status")
        self.IfCommunity = params.get("IfCommunity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceAttributesResponse(AbstractModel):
    """Returned result object of instance attributes

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param InstanceName: Instance name\n        :type InstanceName: str\n        :param VipList: VIP list information of access point\n        :type VipList: list of VipEntity\n        :param Vip: Virtual IP\n        :type Vip: str\n        :param Vport: Virtual port\n        :type Vport: str\n        :param Status: Instance status. 0: creating, 1: running, 2: deleting\n        :type Status: int\n        :param Bandwidth: Instance bandwidth in Mbps\n        :type Bandwidth: int\n        :param DiskSize: Instance storage capacity in GB\n        :type DiskSize: int\n        :param ZoneId: AZ\n        :type ZoneId: int\n        :param VpcId: VPC ID. If this parameter is empty, it means the basic network\n        :type VpcId: str\n        :param SubnetId: Subnet ID. If this parameter is empty, it means the basic network\n        :type SubnetId: str\n        :param Healthy: Instance health status. 1: healthy, 2: alarmed, 3: exceptional\n        :type Healthy: int\n        :param HealthyMessage: Instance health information. Currently, the disk utilization is displayed with a maximum length of 256\n        :type HealthyMessage: str\n        :param CreateTime: Creation time\n        :type CreateTime: int\n        :param MsgRetentionTime: Message retention period in minutes\n        :type MsgRetentionTime: int\n        :param Config: Configuration for automatic topic creation. If this field is empty, it means that automatic creation is not enabled\n        :type Config: :class:`tencentcloud.ckafka.v20190819.models.InstanceConfigDO`\n        :param RemainderPartitions: Number of remaining creatable partitions\n        :type RemainderPartitions: int\n        :param RemainderTopics: Number of remaining creatable topics\n        :type RemainderTopics: int\n        :param CreatedPartitions: Number of partitions already created\n        :type CreatedPartitions: int\n        :param CreatedTopics: Number of topics already created\n        :type CreatedTopics: int\n        :param Tags: Tag array
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Tags: list of Tag\n        :param ExpireTime: Expiration time
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ExpireTime: int\n        :param ZoneIds: Cross-AZ
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ZoneIds: list of int\n        :param Version: Kafka version information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Version: str\n        :param MaxGroupNum: Maximum number of groups
Note: this field may return null, indicating that no valid values can be obtained.\n        :type MaxGroupNum: int\n        :param Cvm: Offering type. `0`: Standard Edition; `1`: Professional Edition
Note: this field may return `null`, indicating that no valid value was found.\n        :type Cvm: int\n        :param InstanceType: Type.
Note: this field may return `null`, indicating that no valid value was found.\n        :type InstanceType: str\n        :param Features: Features supported by the instance. `FEATURE_SUBNET_ACL` indicates that the ACL policy supports setting subnets. 
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Features: list of str\n        :param RetentionTimeConfig: Dynamic message retention policy
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type RetentionTimeConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceConfigDO(AbstractModel):
    """Instance configuration entity

    """

    def __init__(self):
        """
        :param AutoCreateTopicsEnable: Whether to create topics automatically\n        :type AutoCreateTopicsEnable: bool\n        :param DefaultNumPartitions: Number of partitions\n        :type DefaultNumPartitions: int\n        :param DefaultReplicationFactor: Default replication factor\n        :type DefaultReplicationFactor: int\n        """
        self.AutoCreateTopicsEnable = None
        self.DefaultNumPartitions = None
        self.DefaultReplicationFactor = None


    def _deserialize(self, params):
        self.AutoCreateTopicsEnable = params.get("AutoCreateTopicsEnable")
        self.DefaultNumPartitions = params.get("DefaultNumPartitions")
        self.DefaultReplicationFactor = params.get("DefaultReplicationFactor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDetail(AbstractModel):
    """Instance details

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param InstanceName: Instance name\n        :type InstanceName: str\n        :param Vip: Instance VIP information\n        :type Vip: str\n        :param Vport: Instance port information\n        :type Vport: str\n        :param VipList: Virtual IP list\n        :type VipList: list of VipEntity\n        :param Status: Instance status. 0: creating, 1: running, 2: deleting, 5: isolated, -1: creation failed\n        :type Status: int\n        :param Bandwidth: Instance bandwidth in Mbps\n        :type Bandwidth: int\n        :param DiskSize: Instance storage capacity in GB\n        :type DiskSize: int\n        :param ZoneId: AZ ID\n        :type ZoneId: int\n        :param VpcId: vpcId. If this parameter is empty, it means the basic network\n        :type VpcId: str\n        :param SubnetId: Subnet ID\n        :type SubnetId: str\n        :param RenewFlag: Whether to renew the instance automatically, which is an int-type enumerated value. 1: yes, 2: no\n        :type RenewFlag: int\n        :param Healthy: Instance status, which is an int-type value. 0: healthy, 1: alarmed, 2: exceptional\n        :type Healthy: int\n        :param HealthyMessage: Instance status information\n        :type HealthyMessage: str\n        :param CreateTime: Instance creation time\n        :type CreateTime: int\n        :param ExpireTime: Instance expiration time\n        :type ExpireTime: int\n        :param IsInternal: Whether it is an internal customer. 1: yes\n        :type IsInternal: int\n        :param TopicNum: Number of topics\n        :type TopicNum: int\n        :param Tags: Tag\n        :type Tags: list of Tag\n        :param Version: Kafka version information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Version: str\n        :param ZoneIds: Cross-AZ
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ZoneIds: list of int\n        :param Cvm: CKafka sale type
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Cvm: int\n        :param InstanceType: CKafka instance type
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type InstanceType: str\n        :param DiskType: Disk type
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type DiskType: str\n        :param MaxTopicNumber: Maximum number of topics for the current instance
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type MaxTopicNumber: int\n        :param MaxPartitionNumber: Maximum number of partitions for the current instance
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type MaxPartitionNumber: int\n        :param RebalanceTime: Time of scheduled upgrade
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type RebalanceTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDetailResponse(AbstractModel):
    """Returned result of instance details

    """

    def __init__(self):
        """
        :param TotalCount: Total number of eligible instances\n        :type TotalCount: int\n        :param InstanceList: List of eligible instance details\n        :type InstanceList: list of InstanceDetail\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceResponse(AbstractModel):
    """Aggregated returned result of instance status

    """

    def __init__(self):
        """
        :param InstanceList: List of eligible instances
Note: this field may return null, indicating that no valid values can be obtained.\n        :type InstanceList: list of Instance\n        :param TotalCount: Total number of eligible results
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JgwOperateResponse(AbstractModel):
    """Returned result value of operation

    """

    def __init__(self):
        """
        :param ReturnCode: Returned code. 0: normal, other values: error\n        :type ReturnCode: str\n        :param ReturnMessage: Success message\n        :type ReturnMessage: str\n        :param Data: Data returned by an operation, which may contain `flowId`, etc.
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Data: :class:`tencentcloud.ckafka.v20190819.models.OperateResponseData`\n        """
        self.ReturnCode = None
        self.ReturnMessage = None
        self.Data = None


    def _deserialize(self, params):
        self.ReturnCode = params.get("ReturnCode")
        self.ReturnMessage = params.get("ReturnMessage")
        if params.get("Data") is not None:
            self.Data = OperateResponseData()
            self.Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGroupOffsetsRequest(AbstractModel):
    """ModifyGroupOffsets request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Kafka instance ID\n        :type InstanceId: str\n        :param Group: Kafka consumer group\n        :type Group: str\n        :param Strategy: Offset resetting policy. Meanings of the input parameters: 0: equivalent to the `shift-by` parameter, which indicates to shift the offset forward or backward by the value of the `shift`. 1: equivalent to `by-duration`, `to-datetime`, `to-earliest`, or `to-latest`, which indicates to move the offset to the specified timestamp. 2: equivalent to `to-offset`, which indicates to move the offset to the specified offset position\n        :type Strategy: int\n        :param Topics: Indicates the topics to be reset. If this parameter is left empty, all topics will be reset\n        :type Topics: list of str\n        :param Shift: When `strategy` is 0, this field is required. If it is above zero, the offset will be shifted backward by the value of the `shift`. If it is below zero, the offset will be shifted forward by the value of the `shift`. After a correct reset, the new offset should be (old_offset + shift). Note that if the new offset is smaller than the `earliest` parameter of the partition, it will be set to `earliest`, and if it is greater than the `latest` parameter of the partition, it will be set to `latest`\n        :type Shift: int\n        :param ShiftTimestamp: Unit: ms. When `strategy` is 1, this field is required, where -2 indicates to reset the offset to the initial position, -1 indicates to reset to the latest position (equivalent to emptying), and other values represent the specified time, i.e., the offset of the topic at the specified time will be obtained and then reset. Note that if there is no message at the specified time, the last offset will be obtained\n        :type ShiftTimestamp: int\n        :param Offset: Position of the offset that needs to be reset. When `strategy` is 2, this field is required\n        :type Offset: int\n        :param Partitions: List of partitions that need to be reset. If the topics parameter is not specified, reset partitions in the corresponding partition list of all topics. If the topics parameter is specified, reset partitions of the corresponding partition list of the specified topic list.\n        :type Partitions: list of int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGroupOffsetsResponse(AbstractModel):
    """ModifyGroupOffsets response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param AutoCreateTopicEnable: Automatic creation. true: enabled, false: not enabled\n        :type AutoCreateTopicEnable: bool\n        :param DefaultNumPartitions: Optional. If `auto.create.topic.enable` is set to `true` and this value is not set, 3 will be used by default\n        :type DefaultNumPartitions: int\n        :param DefaultReplicationFactor: If `auto.create.topic.enable` is set to `true` but this value is not set, 2 will be used by default\n        :type DefaultReplicationFactor: int\n        """
        self.AutoCreateTopicEnable = None
        self.DefaultNumPartitions = None
        self.DefaultReplicationFactor = None


    def _deserialize(self, params):
        self.AutoCreateTopicEnable = params.get("AutoCreateTopicEnable")
        self.DefaultNumPartitions = params.get("DefaultNumPartitions")
        self.DefaultReplicationFactor = params.get("DefaultReplicationFactor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceAttributesRequest(AbstractModel):
    """ModifyInstanceAttributes request structure.

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param MsgRetentionTime: Maximum retention period in minutes for instance log, which can be up to 30 days. 0 indicates not to enable the log retention period policy\n        :type MsgRetentionTime: int\n        :param InstanceName: Instance name string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`)\n        :type InstanceName: str\n        :param Config: Instance configuration\n        :type Config: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstanceAttributesConfig`\n        :param DynamicRetentionConfig: Dynamic message retention policy configuration\n        :type DynamicRetentionConfig: :class:`tencentcloud.ckafka.v20190819.models.DynamicRetentionTime`\n        :param RebalanceTime: Modification of the rebalancing time after upgrade\n        :type RebalanceTime: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceAttributesResponse(AbstractModel):
    """ModifyInstanceAttributes response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID\n        :type InstanceId: str\n        :param Name: Username\n        :type Name: str\n        :param Password: Current user password\n        :type Password: str\n        :param PasswordNew: New user password\n        :type PasswordNew: str\n        """
        self.InstanceId = None
        self.Name = None
        self.Password = None
        self.PasswordNew = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.Password = params.get("Password")
        self.PasswordNew = params.get("PasswordNew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPasswordResponse(AbstractModel):
    """ModifyPassword response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
        :param InstanceId: Instance ID.\n        :type InstanceId: str\n        :param TopicName: Topic name.\n        :type TopicName: str\n        :param Note: Topic remarks string of up to 64 characters, which must begin with a letter and can contain letters, digits, and dashes (`-`).\n        :type Note: str\n        :param EnableWhiteList: IP allowlist switch. 1: enabled, 0: disabled.\n        :type EnableWhiteList: int\n        :param MinInsyncReplicas: Default value: 1.\n        :type MinInsyncReplicas: int\n        :param UncleanLeaderElectionEnable: 0: false, 1: true. Default value: 0.\n        :type UncleanLeaderElectionEnable: int\n        :param RetentionMs: Message retention period in ms. The current minimum value is 60,000 ms.\n        :type RetentionMs: int\n        :param SegmentMs: Segment rolling duration in ms. The current minimum value is 86,400,000 ms.\n        :type SegmentMs: int\n        :param MaxMessageBytes: Maximum topic message length in bytes. The maximum value is 8,388,608 bytes (i.e., 8 MB).\n        :type MaxMessageBytes: int\n        :param CleanUpPolicy: Message deletion policy. Valid values: delete, compact\n        :type CleanUpPolicy: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicAttributesResponse(AbstractModel):
    """ModifyTopicAttributes response structure.

    """

    def __init__(self):
        """
        :param Result: Returned result set\n        :type Result: :class:`tencentcloud.ckafka.v20190819.models.JgwOperateResponse`\n        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.\n        :type RequestId: str\n        """
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
Note: this field may return null, indicating that no valid values can be obtained.\n        :type FlowId: int\n        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Partition(AbstractModel):
    """Partition entity

    """

    def __init__(self):
        """
        :param PartitionId: Partition ID\n        :type PartitionId: int\n        """
        self.PartitionId = None


    def _deserialize(self, params):
        self.PartitionId = params.get("PartitionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PartitionOffset(AbstractModel):
    """Partition and offset

    """

    def __init__(self):
        """
        :param Partition: Partition, such as "0" or "1"
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Partition: str\n        :param Offset: Offset, such as 100
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Offset: int\n        """
        self.Partition = None
        self.Offset = None


    def _deserialize(self, params):
        self.Partition = params.get("Partition")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Price(AbstractModel):
    """Message price entity

    """

    def __init__(self):
        """
        :param RealTotalCost: Discounted price\n        :type RealTotalCost: float\n        :param TotalCost: Original price\n        :type TotalCost: float\n        """
        self.RealTotalCost = None
        self.TotalCost = None


    def _deserialize(self, params):
        self.RealTotalCost = params.get("RealTotalCost")
        self.TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Region(AbstractModel):
    """Region entity object

    """

    def __init__(self):
        """
        :param RegionId: Region ID\n        :type RegionId: int\n        :param RegionName: Region name\n        :type RegionName: str\n        :param AreaName: Area name\n        :type AreaName: str\n        :param RegionCode: Region code
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type RegionCode: str\n        :param RegionCodeV3: Region code (v3)
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type RegionCodeV3: str\n        :param Support: NONE: no special models are supported by default.\nCVM: the CVM type is supported.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type Support: str\n        :param Ipv6: Whether IPv6 is supported. `0` indicates no, and `1` indicates yes.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type Ipv6: int\n        :param MultiZone: Whether cross-AZ clusters are supported.`0` indicates no, and `1` indicates yes.
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type MultiZone: int\n        """
        self.RegionId = None
        self.RegionName = None
        self.AreaName = None
        self.RegionCode = None
        self.RegionCodeV3 = None
        self.Support = None
        self.Ipv6 = None
        self.MultiZone = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.AreaName = params.get("AreaName")
        self.RegionCode = params.get("RegionCode")
        self.RegionCodeV3 = params.get("RegionCodeV3")
        self.Support = params.get("Support")
        self.Ipv6 = params.get("Ipv6")
        self.MultiZone = params.get("MultiZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Route(AbstractModel):
    """Route entity object

    """

    def __init__(self):
        """
        :param AccessType: Instance connection method
0: PLAINTEXT (plaintext method, which does not carry user information and is supported for legacy versions and Community Edition)
1: SASL_PLAINTEXT (plaintext method, which authenticates the login through SASL before data start and is supported only for Community Edition)
2: SSL (SSL-encrypted communication, which does not carry user information and is supported for legacy versions and Community Edition)
3: SASL_SSL (SSL-encrypted communication, which authenticates the login through SASL before data start and is supported only for Community Edition)\n        :type AccessType: int\n        :param RouteId: Route ID\n        :type RouteId: int\n        :param VipType: VIP network type (1: public network TGW; 2: classic network; 3: VPC; 4: Tencent Cloud-supported environment (generally used for internal instances); 5: SSL public network access; 6: BM VPC)\n        :type VipType: int\n        :param VipList: Virtual IP list\n        :type VipList: list of VipEntity\n        :param Domain: Domain name
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Domain: str\n        :param DomainPort: Domain name port
Note: this field may return null, indicating that no valid values can be obtained.\n        :type DomainPort: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteResponse(AbstractModel):
    """Returned object for route information

    """

    def __init__(self):
        """
        :param Routers: Route information list
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Routers: list of Route\n        """
        self.Routers = None


    def _deserialize(self, params):
        if params.get("Routers") is not None:
            self.Routers = []
            for item in params.get("Routers"):
                obj = Route()
                obj._deserialize(item)
                self.Routers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribedInfo(AbstractModel):
    """Subscribed message entity

    """

    def __init__(self):
        """
        :param TopicName: Subscribed topic name\n        :type TopicName: str\n        :param Partition: Subscribed partition
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Partition: list of int\n        :param PartitionOffset: Partition offset information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type PartitionOffset: list of PartitionOffset\n        :param TopicId: ID of the subscribed topic. 
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TopicId: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """Tag object in instance details

    """

    def __init__(self):
        """
        :param TagKey: Tag key\n        :type TagKey: str\n        :param TagValue: Tag value\n        :type TagValue: str\n        """
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
        


class Topic(AbstractModel):
    """Returned topic object

    """

    def __init__(self):
        """
        :param TopicId: Topic ID\n        :type TopicId: str\n        :param TopicName: Topic name\n        :type TopicName: str\n        :param Note: Remarks
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Note: str\n        """
        self.TopicId = None
        self.TopicName = None
        self.Note = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.Note = params.get("Note")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicAttributesResponse(AbstractModel):
    """Returned topic attributes result entity

    """

    def __init__(self):
        """
        :param TopicId: Topic ID\n        :type TopicId: str\n        :param CreateTime: Creation time\n        :type CreateTime: int\n        :param Note: Topic remarks
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Note: str\n        :param PartitionNum: Number of partitions\n        :type PartitionNum: int\n        :param EnableWhiteList: IP allowlist switch. 1: enabled, 0: disabled\n        :type EnableWhiteList: int\n        :param IpWhiteList: IP allowlist list\n        :type IpWhiteList: list of str\n        :param Config: Topic configuration array\n        :type Config: :class:`tencentcloud.ckafka.v20190819.models.Config`\n        :param Partitions: Partition details\n        :type Partitions: list of TopicPartitionDO\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicDetail(AbstractModel):
    """Topic details

    """

    def __init__(self):
        """
        :param TopicName: Topic name\n        :type TopicName: str\n        :param TopicId: Topic ID\n        :type TopicId: str\n        :param PartitionNum: Number of partitions\n        :type PartitionNum: int\n        :param ReplicaNum: Number of replicas\n        :type ReplicaNum: int\n        :param Note: Remarks
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Note: str\n        :param CreateTime: Creation time\n        :type CreateTime: int\n        :param EnableWhiteList: Whether to enable IP authentication allowlist. true: yes, false: no\n        :type EnableWhiteList: bool\n        :param IpWhiteListCount: Number of IPs in IP allowlist\n        :type IpWhiteListCount: int\n        :param ForwardCosBucket: COS bucket for data backup: address of the destination COS bucket
Note: this field may return null, indicating that no valid values can be obtained.\n        :type ForwardCosBucket: str\n        :param ForwardStatus: Status of data backup to COS. 1: not enabled, 0: enabled\n        :type ForwardStatus: int\n        :param ForwardInterval: Frequency of data backup to COS\n        :type ForwardInterval: int\n        :param Config: Advanced configuration
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Config: :class:`tencentcloud.ckafka.v20190819.models.Config`\n        :param RetentionTimeConfig: Message retention time configuration (for recording the latest retention time)
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type RetentionTimeConfig: :class:`tencentcloud.ckafka.v20190819.models.TopicRetentionTimeConfigRsp`\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicDetailResponse(AbstractModel):
    """Returned topic details entity

    """

    def __init__(self):
        """
        :param TopicList: List of returned topic details
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TopicList: list of TopicDetail\n        :param TotalCount: Number of all eligible topic details\n        :type TotalCount: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicPartitionDO(AbstractModel):
    """Partition details

    """

    def __init__(self):
        """
        :param Partition: Partition ID\n        :type Partition: int\n        :param LeaderStatus: Leader running status\n        :type LeaderStatus: int\n        :param IsrNum: ISR quantity\n        :type IsrNum: int\n        :param ReplicaNum: Number of replicas\n        :type ReplicaNum: int\n        """
        self.Partition = None
        self.LeaderStatus = None
        self.IsrNum = None
        self.ReplicaNum = None


    def _deserialize(self, params):
        self.Partition = params.get("Partition")
        self.LeaderStatus = params.get("LeaderStatus")
        self.IsrNum = params.get("IsrNum")
        self.ReplicaNum = params.get("ReplicaNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicResult(AbstractModel):
    """`TopicResponse` returned uniformly

    """

    def __init__(self):
        """
        :param TopicList: List of returned topic information
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TopicList: list of Topic\n        :param TotalCount: Number of eligible topics
Note: this field may return null, indicating that no valid values can be obtained.\n        :type TotalCount: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicRetentionTimeConfigRsp(AbstractModel):
    """Information returned for topic message retention time configuration

    """

    def __init__(self):
        """
        :param Expect: Expected value, i.e., the topic message retention time (min) configured
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type Expect: int\n        :param Current: Current value (min), i.e., the retention time currently in effect, which may be dynamically adjusted
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type Current: int\n        :param ModTimeStamp: Last modified time
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type ModTimeStamp: int\n        """
        self.Expect = None
        self.Current = None
        self.ModTimeStamp = None


    def _deserialize(self, params):
        self.Expect = params.get("Expect")
        self.Current = params.get("Current")
        self.ModTimeStamp = params.get("ModTimeStamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class User(AbstractModel):
    """User entity

    """

    def __init__(self):
        """
        :param UserId: User ID\n        :type UserId: int\n        :param Name: Username\n        :type Name: str\n        :param CreateTime: Creation time\n        :type CreateTime: str\n        :param UpdateTime: Last updated time\n        :type UpdateTime: str\n        """
        self.UserId = None
        self.Name = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Name = params.get("Name")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserResponse(AbstractModel):
    """Returned user entity

    """

    def __init__(self):
        """
        :param Users: List of eligible users
Note: this field may return null, indicating that no valid values can be obtained.\n        :type Users: list of User\n        :param TotalCount: Total number of eligible users\n        :type TotalCount: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VipEntity(AbstractModel):
    """Virtual IP entity

    """

    def __init__(self):
        """
        :param Vip: Virtual IP\n        :type Vip: str\n        :param Vport: Virtual port\n        :type Vport: str\n        """
        self.Vip = None
        self.Vport = None


    def _deserialize(self, params):
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """Zone information entity

    """

    def __init__(self):
        """
        :param ZoneId: Zone ID\n        :type ZoneId: str\n        :param IsInternalApp: Whether it is an internal application.\n        :type IsInternalApp: int\n        :param AppId: Application ID\n        :type AppId: int\n        :param Flag: Flag\n        :type Flag: bool\n        :param ZoneName: Zone name\n        :type ZoneName: str\n        :param ZoneStatus: Zone status\n        :type ZoneStatus: int\n        :param Exflag: Extra flag\n        :type Exflag: str\n        :param SoldOut: JSON object. The key is the model. The value `true` means “sold out”, and `false` means “not sold out”.\n        :type SoldOut: str\n        """
        self.ZoneId = None
        self.IsInternalApp = None
        self.AppId = None
        self.Flag = None
        self.ZoneName = None
        self.ZoneStatus = None
        self.Exflag = None
        self.SoldOut = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.IsInternalApp = params.get("IsInternalApp")
        self.AppId = params.get("AppId")
        self.Flag = params.get("Flag")
        self.ZoneName = params.get("ZoneName")
        self.ZoneStatus = params.get("ZoneStatus")
        self.Exflag = params.get("Exflag")
        self.SoldOut = params.get("SoldOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneResponse(AbstractModel):
    """The entity returned for the query of Kafka’s zone information

    """

    def __init__(self):
        """
        :param ZoneList: Zone list\n        :type ZoneList: list of ZoneInfo\n        :param MaxBuyInstanceNum: Maximum number of instances to be purchased\n        :type MaxBuyInstanceNum: int\n        :param MaxBandwidth: Maximum bandwidth in MB/S\n        :type MaxBandwidth: int\n        :param UnitPrice: Pay-as-you-go unit price\n        :type UnitPrice: :class:`tencentcloud.ckafka.v20190819.models.Price`\n        :param MessagePrice: Pay-as-you-go unit message price\n        :type MessagePrice: :class:`tencentcloud.ckafka.v20190819.models.Price`\n        :param ClusterInfo: Cluster information dedicated to a user
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type ClusterInfo: list of ClusterInfo\n        :param Standard: Purchase of Standard Edition configurations
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type Standard: str\n        :param StandardS2: Purchase of Standard S2 Edition configurations
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type StandardS2: str\n        :param Profession: Purchase of Pro Edition configurations
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type Profession: str\n        :param Physical: Purchase of Physical Dedicated Edition configurations
Note: `null` may be returned for this field, indicating that no valid values can be obtained.\n        :type Physical: str\n        """
        self.ZoneList = None
        self.MaxBuyInstanceNum = None
        self.MaxBandwidth = None
        self.UnitPrice = None
        self.MessagePrice = None
        self.ClusterInfo = None
        self.Standard = None
        self.StandardS2 = None
        self.Profession = None
        self.Physical = None


    def _deserialize(self, params):
        if params.get("ZoneList") is not None:
            self.ZoneList = []
            for item in params.get("ZoneList"):
                obj = ZoneInfo()
                obj._deserialize(item)
                self.ZoneList.append(obj)
        self.MaxBuyInstanceNum = params.get("MaxBuyInstanceNum")
        self.MaxBandwidth = params.get("MaxBandwidth")
        if params.get("UnitPrice") is not None:
            self.UnitPrice = Price()
            self.UnitPrice._deserialize(params.get("UnitPrice"))
        if params.get("MessagePrice") is not None:
            self.MessagePrice = Price()
            self.MessagePrice._deserialize(params.get("MessagePrice"))
        if params.get("ClusterInfo") is not None:
            self.ClusterInfo = []
            for item in params.get("ClusterInfo"):
                obj = ClusterInfo()
                obj._deserialize(item)
                self.ClusterInfo.append(obj)
        self.Standard = params.get("Standard")
        self.StandardS2 = params.get("StandardS2")
        self.Profession = params.get("Profession")
        self.Physical = params.get("Physical")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        