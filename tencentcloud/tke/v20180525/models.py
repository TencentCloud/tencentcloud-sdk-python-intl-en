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


class AcquireClusterAdminRoleRequest(AbstractModel):
    """AcquireClusterAdminRole request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")


class AcquireClusterAdminRoleResponse(AbstractModel):
    """AcquireClusterAdminRole response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddExistedInstancesRequest(AbstractModel):
    """AddExistedInstances request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param InstanceIds: Instance list. Spot instance is not supported.
        :type InstanceIds: list of str
        :param InstanceAdvancedSettings: Detailed information of the instance
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param EnhancedService: Enhanced services. This parameter is used to specify whether to enable Cloud Security, Cloud Monitoring and other services. If this parameter is not specified, Cloud Monitor and Cloud Security are enabled by default.
        :type EnhancedService: :class:`tencentcloud.tke.v20180525.models.EnhancedService`
        :param LoginSettings: Node login information (currently only supports using Password or single KeyIds)
        :type LoginSettings: :class:`tencentcloud.tke.v20180525.models.LoginSettings`
        :param HostName: When reinstalling the system, you can specify the HostName of the modified instance (when the cluster is in HostName mode, this parameter is required, and the rule name is the same as the [Create CVM Instance](https://intl.cloud.tencent.com/document/product/213/15730?from_cn_redirect=1) API HostName except for uppercase letters not being supported.
        :type HostName: str
        :param SecurityGroupIds: Security group to which the instance belongs. This parameter can be obtained from the `sgId` field returned by DescribeSecurityGroups. If this parameter is not specified, the default security group is bound. (Currently, you can only set a single sgId)
        :type SecurityGroupIds: list of str
        :param NodePool: Node pool options
        :type NodePool: :class:`tencentcloud.tke.v20180525.models.NodePoolOption`
        :param SkipValidateOptions: Skips the specified verification. Valid values: GlobalRouteCIDRCheck, VpcCniCIDRCheck
        :type SkipValidateOptions: list of str
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.InstanceAdvancedSettings = None
        self.EnhancedService = None
        self.LoginSettings = None
        self.HostName = None
        self.SecurityGroupIds = None
        self.NodePool = None
        self.SkipValidateOptions = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.HostName = params.get("HostName")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("NodePool") is not None:
            self.NodePool = NodePoolOption()
            self.NodePool._deserialize(params.get("NodePool"))
        self.SkipValidateOptions = params.get("SkipValidateOptions")


class AddExistedInstancesResponse(AbstractModel):
    """AddExistedInstances response structure.

    """

    def __init__(self):
        """
        :param FailedInstanceIds: IDs of failed nodes
Note: This field may return null, indicating that no valid value was found.
        :type FailedInstanceIds: list of str
        :param SuccInstanceIds: IDs of successful nodes
Note: This field may return null, indicating that no valid value was found.
        :type SuccInstanceIds: list of str
        :param TimeoutInstanceIds: IDs of (successful or failed) nodes that timed out
Note: This field may return null, indicating that no valid value was found.
        :type TimeoutInstanceIds: list of str
        :param FailedReasons: Causes of the failure to add a node to a cluster
Note: this field may return `null`, indicating that no valid value is obtained.
        :type FailedReasons: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FailedInstanceIds = None
        self.SuccInstanceIds = None
        self.TimeoutInstanceIds = None
        self.FailedReasons = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailedInstanceIds = params.get("FailedInstanceIds")
        self.SuccInstanceIds = params.get("SuccInstanceIds")
        self.TimeoutInstanceIds = params.get("TimeoutInstanceIds")
        self.FailedReasons = params.get("FailedReasons")
        self.RequestId = params.get("RequestId")


class AddNodeToNodePoolRequest(AbstractModel):
    """AddNodeToNodePool request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param NodePoolId: Node pool ID
        :type NodePoolId: str
        :param InstanceIds: Node ID
        :type InstanceIds: list of str
        """
        self.ClusterId = None
        self.NodePoolId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NodePoolId = params.get("NodePoolId")
        self.InstanceIds = params.get("InstanceIds")


class AddNodeToNodePoolResponse(AbstractModel):
    """AddNodeToNodePool response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AutoScalingGroupRange(AbstractModel):
    """Maximum and minimum number of pods in cluster-associated scaling groups

    """

    def __init__(self):
        """
        :param MinSize: Minimum number of pods in a scaling group
        :type MinSize: int
        :param MaxSize: Maximum number of pods in a scaling group
        :type MaxSize: int
        """
        self.MinSize = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.MinSize = params.get("MinSize")
        self.MaxSize = params.get("MaxSize")


class AutoscalingAdded(AbstractModel):
    """Nodes that are added in scale-out

    """

    def __init__(self):
        """
        :param Joining: Number of nodes that are being added
        :type Joining: int
        :param Initializing: Number of nodes that are being initialized
        :type Initializing: int
        :param Normal: Number of normal nodes
        :type Normal: int
        :param Total: Total number of nodes
        :type Total: int
        """
        self.Joining = None
        self.Initializing = None
        self.Normal = None
        self.Total = None


    def _deserialize(self, params):
        self.Joining = params.get("Joining")
        self.Initializing = params.get("Initializing")
        self.Normal = params.get("Normal")
        self.Total = params.get("Total")


class CheckInstancesUpgradeAbleRequest(AbstractModel):
    """CheckInstancesUpgradeAble request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param InstanceIds: Specify the node list to check. If it’s not passed in, all nodes of the cluster will be checked.
        :type InstanceIds: list of str
        :param UpgradeType: Upgrade type
        :type UpgradeType: str
        :param Offset: Pagination offset
        :type Offset: int
        :param Limit: Pagination limit
        :type Limit: int
        :param Filter: Filtering
        :type Filter: list of Filter
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.UpgradeType = None
        self.Offset = None
        self.Limit = None
        self.Filter = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIds = params.get("InstanceIds")
        self.UpgradeType = params.get("UpgradeType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filter") is not None:
            self.Filter = []
            for item in params.get("Filter"):
                obj = Filter()
                obj._deserialize(item)
                self.Filter.append(obj)


class CheckInstancesUpgradeAbleResponse(AbstractModel):
    """CheckInstancesUpgradeAble response structure.

    """

    def __init__(self):
        """
        :param ClusterVersion: The current minor version of cluster Master
        :type ClusterVersion: str
        :param LatestVersion: The latest minor version of cluster Master corresponding major version
        :type LatestVersion: str
        :param UpgradeAbleInstances: List of nodes that can be upgraded
Note: this field may return `null`, indicating that no valid value is obtained.
        :type UpgradeAbleInstances: list of UpgradeAbleInstancesItem
        :param Total: Total number
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Total: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ClusterVersion = None
        self.LatestVersion = None
        self.UpgradeAbleInstances = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterVersion = params.get("ClusterVersion")
        self.LatestVersion = params.get("LatestVersion")
        if params.get("UpgradeAbleInstances") is not None:
            self.UpgradeAbleInstances = []
            for item in params.get("UpgradeAbleInstances"):
                obj = UpgradeAbleInstancesItem()
                obj._deserialize(item)
                self.UpgradeAbleInstances.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class Cluster(AbstractModel):
    """Cluster information struct

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param ClusterName: Cluster name
        :type ClusterName: str
        :param ClusterDescription: Cluster description
        :type ClusterDescription: str
        :param ClusterVersion: Cluster version. The default value is 1.10.5.
        :type ClusterVersion: str
        :param ClusterOs: Cluster operating system. centOS 7.2x86_64 or ubuntu 16.04.1 LTSx86_64. Default value: ubuntu 16.04.1 LTSx86_64
        :type ClusterOs: str
        :param ClusterType: Cluster type. Managed cluster: MANAGED_CLUSTER; Self-deployed cluster: INDEPENDENT_CLUSTER.
        :type ClusterType: str
        :param ClusterNetworkSettings: Cluster network-related parameters
        :type ClusterNetworkSettings: :class:`tencentcloud.tke.v20180525.models.ClusterNetworkSettings`
        :param ClusterNodeNum: Current number of nodes in the cluster
        :type ClusterNodeNum: int
        :param ProjectId: ID of the project to which the cluster belongs
        :type ProjectId: int
        :param TagSpecification: Tag description list.
        :type TagSpecification: list of TagSpecification
        :param ClusterStatus: Cluster status (Running, Creating, or Abnormal)
        :type ClusterStatus: str
        :param Property: Cluster attributes (including a map of different cluster attributes, with attribute fields including NodeNameType (lan-ip mode and hostname mode, with lan-ip mode as default))
        :type Property: str
        :param ClusterMaterNodeNum: Number of primary nodes currently in the cluster
        :type ClusterMaterNodeNum: int
        :param ImageId: ID of the image used by the cluster
Note: this field may return null, indicating that no valid value is obtained.
        :type ImageId: str
        :param OsCustomizeType: Container image tag
Note: This field may return null, indicating that no valid value was found.
        :type OsCustomizeType: str
        :param ContainerRuntime: Runtime environment of the cluster. Values can be `docker` or `containerd`.
Note: this field may return null, indicating that no valid value is obtained.
        :type ContainerRuntime: str
        :param CreatedTime: Creation time
Note: this field may return null, indicating that no valid value is obtained.
        :type CreatedTime: str
        :param DeletionProtection: Whether Deletion Protection is enabled
Note: this field may return null, indicating that no valid value is obtained.
        :type DeletionProtection: bool
        """
        self.ClusterId = None
        self.ClusterName = None
        self.ClusterDescription = None
        self.ClusterVersion = None
        self.ClusterOs = None
        self.ClusterType = None
        self.ClusterNetworkSettings = None
        self.ClusterNodeNum = None
        self.ProjectId = None
        self.TagSpecification = None
        self.ClusterStatus = None
        self.Property = None
        self.ClusterMaterNodeNum = None
        self.ImageId = None
        self.OsCustomizeType = None
        self.ContainerRuntime = None
        self.CreatedTime = None
        self.DeletionProtection = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterDescription = params.get("ClusterDescription")
        self.ClusterVersion = params.get("ClusterVersion")
        self.ClusterOs = params.get("ClusterOs")
        self.ClusterType = params.get("ClusterType")
        if params.get("ClusterNetworkSettings") is not None:
            self.ClusterNetworkSettings = ClusterNetworkSettings()
            self.ClusterNetworkSettings._deserialize(params.get("ClusterNetworkSettings"))
        self.ClusterNodeNum = params.get("ClusterNodeNum")
        self.ProjectId = params.get("ProjectId")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        self.ClusterStatus = params.get("ClusterStatus")
        self.Property = params.get("Property")
        self.ClusterMaterNodeNum = params.get("ClusterMaterNodeNum")
        self.ImageId = params.get("ImageId")
        self.OsCustomizeType = params.get("OsCustomizeType")
        self.ContainerRuntime = params.get("ContainerRuntime")
        self.CreatedTime = params.get("CreatedTime")
        self.DeletionProtection = params.get("DeletionProtection")


class ClusterAdvancedSettings(AbstractModel):
    """Cluster advanced configurations

    """

    def __init__(self):
        """
        :param IPVS: Whether IPVS is enabled
        :type IPVS: bool
        :param AsEnabled: Whether auto-scaling is enabled for nodes in the cluster (Enabling this function is not supported when you create a cluster)
        :type AsEnabled: bool
        :param ContainerRuntime: Type of runtime component used by the cluster. The types include "docker" and "containerd". Default value: docker
        :type ContainerRuntime: str
        :param NodeNameType: NodeName type for a node in a cluster (This includes the two forms of **hostname** and **lan-ip**, with the default as **lan-ip**. If **hostname** is used, you need to set the HostName parameter when creating a node, and the InstanceName needs to be the same as the HostName.)
        :type NodeNameType: str
        :param ExtraArgs: Cluster custom parameter
        :type ExtraArgs: :class:`tencentcloud.tke.v20180525.models.ClusterExtraArgs`
        :param NetworkType: Cluster network type, which can be GR (Global Router) or VPC-CNI. The default value is GR.
        :type NetworkType: str
        :param IsNonStaticIpMode: Whether a cluster in VPC-CNI mode uses dynamic IP addresses. The default value is FALSE, which indicates that static IP addresses are used.
        :type IsNonStaticIpMode: bool
        :param DeletionProtection: Indicates whether to enable cluster deletion protection.
        :type DeletionProtection: bool
        :param KubeProxyMode: Cluster network proxy model, which is only used when ipvs-bpf mode is used. At present, TKE cluster supports three network proxy modes including `iptables`, `ipvs` and `ipvs-bpf` and their parameter setting relationships are as follows:
`iptables`: do not set IPVS and KubeProxyMode.
`ipvs`: set IPVS to `true` and do not set KubeProxyMode.
`ipvs-bpf`: set KubeProxyMode to `kube-proxy-bpf`.
The following conditions are required to use ipvs-bpf network mode:
1. The cluster version must be v1.14 or later.
2. The system image must be Tencent Linux 2.4.
        :type KubeProxyMode: str
        :param AuditEnabled: Indicates whether to enable auditing
        :type AuditEnabled: bool
        :param AuditLogsetId: Specifies the ID of logset to which the audit logs are uploaded.
        :type AuditLogsetId: str
        :param AuditLogTopicId: Specifies the ID of topic to which the audit logs are uploaded.
        :type AuditLogTopicId: str
        :param VpcCniType: Specifies whether the VPC CNI type is multi-IP ENI or or independent ENI.
        :type VpcCniType: str
        :param RuntimeVersion: Runtime version
        :type RuntimeVersion: str
        :param EnableCustomizedPodCIDR: Indicates whether to enable the custom mode for the node’s pod CIDR range
        :type EnableCustomizedPodCIDR: bool
        :param BasePodNumber: The basic number of Pods in custom mode
        :type BasePodNumber: int
        """
        self.IPVS = None
        self.AsEnabled = None
        self.ContainerRuntime = None
        self.NodeNameType = None
        self.ExtraArgs = None
        self.NetworkType = None
        self.IsNonStaticIpMode = None
        self.DeletionProtection = None
        self.KubeProxyMode = None
        self.AuditEnabled = None
        self.AuditLogsetId = None
        self.AuditLogTopicId = None
        self.VpcCniType = None
        self.RuntimeVersion = None
        self.EnableCustomizedPodCIDR = None
        self.BasePodNumber = None


    def _deserialize(self, params):
        self.IPVS = params.get("IPVS")
        self.AsEnabled = params.get("AsEnabled")
        self.ContainerRuntime = params.get("ContainerRuntime")
        self.NodeNameType = params.get("NodeNameType")
        if params.get("ExtraArgs") is not None:
            self.ExtraArgs = ClusterExtraArgs()
            self.ExtraArgs._deserialize(params.get("ExtraArgs"))
        self.NetworkType = params.get("NetworkType")
        self.IsNonStaticIpMode = params.get("IsNonStaticIpMode")
        self.DeletionProtection = params.get("DeletionProtection")
        self.KubeProxyMode = params.get("KubeProxyMode")
        self.AuditEnabled = params.get("AuditEnabled")
        self.AuditLogsetId = params.get("AuditLogsetId")
        self.AuditLogTopicId = params.get("AuditLogTopicId")
        self.VpcCniType = params.get("VpcCniType")
        self.RuntimeVersion = params.get("RuntimeVersion")
        self.EnableCustomizedPodCIDR = params.get("EnableCustomizedPodCIDR")
        self.BasePodNumber = params.get("BasePodNumber")


class ClusterAsGroup(AbstractModel):
    """Cluster-associated scaling group information

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: Scaling group ID
        :type AutoScalingGroupId: str
        :param Status: Scaling group status (`enabled`, `enabling`, `disabled`, `disabling`, `updating`, `deleting`, `scaleDownEnabling`, `scaleDownDisabling`)
        :type Status: str
        :param IsUnschedulable: Whether the node is set to unschedulable
Note: this field may return null, indicating that no valid value was found.
        :type IsUnschedulable: bool
        :param Labels: Scaling group label list
Note: this field may return null, indicating that no valid value was found.
        :type Labels: list of Label
        :param CreatedTime: Creation time
        :type CreatedTime: str
        """
        self.AutoScalingGroupId = None
        self.Status = None
        self.IsUnschedulable = None
        self.Labels = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.Status = params.get("Status")
        self.IsUnschedulable = params.get("IsUnschedulable")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        self.CreatedTime = params.get("CreatedTime")


class ClusterAsGroupAttribute(AbstractModel):
    """Cluster scaling group attributes

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: Scaling group ID
        :type AutoScalingGroupId: str
        :param AutoScalingGroupEnabled: Whether it is enabled
        :type AutoScalingGroupEnabled: bool
        :param AutoScalingGroupRange: Maximum and minimum number of pods in a scaling group
        :type AutoScalingGroupRange: :class:`tencentcloud.tke.v20180525.models.AutoScalingGroupRange`
        """
        self.AutoScalingGroupId = None
        self.AutoScalingGroupEnabled = None
        self.AutoScalingGroupRange = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.AutoScalingGroupEnabled = params.get("AutoScalingGroupEnabled")
        if params.get("AutoScalingGroupRange") is not None:
            self.AutoScalingGroupRange = AutoScalingGroupRange()
            self.AutoScalingGroupRange._deserialize(params.get("AutoScalingGroupRange"))


class ClusterAsGroupOption(AbstractModel):
    """Cluster auto scaling configuration

    """

    def __init__(self):
        """
        :param IsScaleDownEnabled: Whether to enable scale-in
Note: this field may return null, indicating that no valid value was found.
        :type IsScaleDownEnabled: bool
        :param Expander: The scale-out method when there are multiple scaling groups. `random`: select a random scaling group. `most-pods`: choose the scaling group that can schedule the most pods. `least-waste`: select the scaling group that can ensure the fewest remaining resources after Pod scheduling.. The default value is `random`.)
Note: this field may return null, indicating that no valid value was found.
        :type Expander: str
        :param MaxEmptyBulkDelete: Max concurrent scale-in volume
Note: this field may return null, indicating that no valid value was found.
        :type MaxEmptyBulkDelete: int
        :param ScaleDownDelay: Number of minutes after cluster scale-out when the system starts judging whether to perform scale-in
Note: this field may return null, indicating that no valid value was found.
        :type ScaleDownDelay: int
        :param ScaleDownUnneededTime: Number of consecutive minutes of idleness after which the node is subject to scale-in (default value: 10)
Note: this field may return null, indicating that no valid value was found.
        :type ScaleDownUnneededTime: int
        :param ScaleDownUtilizationThreshold: Percentage of node resource usage below which the node is considered to be idle (default value: 50)
Note: this field may return null, indicating that no valid value was found.
        :type ScaleDownUtilizationThreshold: int
        :param SkipNodesWithLocalStorage: During scale-in, ignore nodes with local storage pods (default value: False)
Note: this field may return null, indicating that no valid value was found.
        :type SkipNodesWithLocalStorage: bool
        :param SkipNodesWithSystemPods: During scale-in, ignore nodes with pods in the kube-system namespace that are not managed by DaemonSet (default value: False)
Note: this field may return null, indicating that no valid value was found.
        :type SkipNodesWithSystemPods: bool
        :param IgnoreDaemonSetsUtilization: Whether to ignore DaemonSet pods by default when calculating resource usage (default value: False: do not ignore)
Note: this field may return null, indicating that no valid value was found.
        :type IgnoreDaemonSetsUtilization: bool
        :param OkTotalUnreadyCount: Number at which CA health detection is triggered (default value: 3). After the number specified in OkTotalUnreadyCount is exceeded, CA will perform health detection.
Note: this field may return null, indicating that no valid value was found.
        :type OkTotalUnreadyCount: int
        :param MaxTotalUnreadyPercentage: Max percentage of unready nodes. After the max percentage is exceeded, CA will stop operation.
Note: this field may return null, indicating that no valid value was found.
        :type MaxTotalUnreadyPercentage: int
        :param ScaleDownUnreadyTime: Amount of time before unready nodes become eligible for scale-in
Note: this field may return null, indicating that no valid value was found.
        :type ScaleDownUnreadyTime: int
        :param UnregisteredNodeRemovalTime: Waiting time before CA deletes nodes that are not registered in Kubernetes
Note: this field may return null, indicating that no valid value was found.
        :type UnregisteredNodeRemovalTime: int
        """
        self.IsScaleDownEnabled = None
        self.Expander = None
        self.MaxEmptyBulkDelete = None
        self.ScaleDownDelay = None
        self.ScaleDownUnneededTime = None
        self.ScaleDownUtilizationThreshold = None
        self.SkipNodesWithLocalStorage = None
        self.SkipNodesWithSystemPods = None
        self.IgnoreDaemonSetsUtilization = None
        self.OkTotalUnreadyCount = None
        self.MaxTotalUnreadyPercentage = None
        self.ScaleDownUnreadyTime = None
        self.UnregisteredNodeRemovalTime = None


    def _deserialize(self, params):
        self.IsScaleDownEnabled = params.get("IsScaleDownEnabled")
        self.Expander = params.get("Expander")
        self.MaxEmptyBulkDelete = params.get("MaxEmptyBulkDelete")
        self.ScaleDownDelay = params.get("ScaleDownDelay")
        self.ScaleDownUnneededTime = params.get("ScaleDownUnneededTime")
        self.ScaleDownUtilizationThreshold = params.get("ScaleDownUtilizationThreshold")
        self.SkipNodesWithLocalStorage = params.get("SkipNodesWithLocalStorage")
        self.SkipNodesWithSystemPods = params.get("SkipNodesWithSystemPods")
        self.IgnoreDaemonSetsUtilization = params.get("IgnoreDaemonSetsUtilization")
        self.OkTotalUnreadyCount = params.get("OkTotalUnreadyCount")
        self.MaxTotalUnreadyPercentage = params.get("MaxTotalUnreadyPercentage")
        self.ScaleDownUnreadyTime = params.get("ScaleDownUnreadyTime")
        self.UnregisteredNodeRemovalTime = params.get("UnregisteredNodeRemovalTime")


class ClusterBasicSettings(AbstractModel):
    """Describes the basic configuration information of a cluster

    """

    def __init__(self):
        """
        :param ClusterOs: Cluster operating system. CentOS 7.2x86_64 or Ubuntu 16.04.1 LTSx86_64. Default value: Ubuntu 16.04.1 LTSx86_64
        :type ClusterOs: str
        :param ClusterVersion: Cluster version. The default value is 1.10.5.
        :type ClusterVersion: str
        :param ClusterName: Cluster name
        :type ClusterName: str
        :param ClusterDescription: Cluster description
        :type ClusterDescription: str
        :param VpcId: VPC ID, in the format of vpc-xxx, which is required when you create an empty managed cluster.
        :type VpcId: str
        :param ProjectId: ID of the project to which the new resources in the cluster belong.
        :type ProjectId: int
        :param TagSpecification: Tag description list. This parameter is used to bind a tag to a resource instance. Currently, a tag can only be bound to cluster instances.
        :type TagSpecification: list of TagSpecification
        :param OsCustomizeType: Container image tag, `DOCKER_CUSTOMIZE` (container customized tag), `GENERAL` (general tag, default value)
        :type OsCustomizeType: str
        :param NeedWorkSecurityGroup: Whether to enable the node’s default security group (default: `No`, Aphla feature)
        :type NeedWorkSecurityGroup: bool
        """
        self.ClusterOs = None
        self.ClusterVersion = None
        self.ClusterName = None
        self.ClusterDescription = None
        self.VpcId = None
        self.ProjectId = None
        self.TagSpecification = None
        self.OsCustomizeType = None
        self.NeedWorkSecurityGroup = None


    def _deserialize(self, params):
        self.ClusterOs = params.get("ClusterOs")
        self.ClusterVersion = params.get("ClusterVersion")
        self.ClusterName = params.get("ClusterName")
        self.ClusterDescription = params.get("ClusterDescription")
        self.VpcId = params.get("VpcId")
        self.ProjectId = params.get("ProjectId")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        self.OsCustomizeType = params.get("OsCustomizeType")
        self.NeedWorkSecurityGroup = params.get("NeedWorkSecurityGroup")


class ClusterCIDRSettings(AbstractModel):
    """Container networking parameters for the cluster

    """

    def __init__(self):
        """
        :param ClusterCIDR: CIDR used to assign container and service IPs for the cluster. It cannot conflict with the VPC's CIDR or the CIDRs of other clusters in the same VPC
        :type ClusterCIDR: str
        :param IgnoreClusterCIDRConflict: Whether to ignore ClusterCIDR conflict errors, which are not ignored by default
        :type IgnoreClusterCIDRConflict: bool
        :param MaxNodePodNum: Maximum number of pods on each node in the cluster
        :type MaxNodePodNum: int
        :param MaxClusterServiceNum: Maximum number of cluster services
        :type MaxClusterServiceNum: int
        :param ServiceCIDR: The CIDR block used to assign cluster service IP addresses. It must conflict with neither the VPC CIDR block nor with CIDR blocks of other clusters in the same VPC instance. The IP range must be within the private network IP range, such as 10.1.0.0/14, 192.168.0.1/18, and 172.16.0.0/16.
        :type ServiceCIDR: str
        :param EniSubnetIds: Subnet ID of the ENI in VPC-CNI network mode
        :type EniSubnetIds: list of str
        :param ClaimExpiredSeconds: Repossession time of ENI IP addresses in VPC-CNI network mode, whose range is [300,15768000)
        :type ClaimExpiredSeconds: int
        """
        self.ClusterCIDR = None
        self.IgnoreClusterCIDRConflict = None
        self.MaxNodePodNum = None
        self.MaxClusterServiceNum = None
        self.ServiceCIDR = None
        self.EniSubnetIds = None
        self.ClaimExpiredSeconds = None


    def _deserialize(self, params):
        self.ClusterCIDR = params.get("ClusterCIDR")
        self.IgnoreClusterCIDRConflict = params.get("IgnoreClusterCIDRConflict")
        self.MaxNodePodNum = params.get("MaxNodePodNum")
        self.MaxClusterServiceNum = params.get("MaxClusterServiceNum")
        self.ServiceCIDR = params.get("ServiceCIDR")
        self.EniSubnetIds = params.get("EniSubnetIds")
        self.ClaimExpiredSeconds = params.get("ClaimExpiredSeconds")


class ClusterExtraArgs(AbstractModel):
    """Cluster master custom parameter

    """

    def __init__(self):
        """
        :param KubeAPIServer: kube-apiserver custom parameter, in the format of ["k1=v1", "k1=v2"], for example: ["max-requests-inflight=500","feature-gates=PodShareProcessNamespace=true,DynamicKubeletConfig=true"].
Note: this field may return `null`, indicating that no valid value is obtained.
        :type KubeAPIServer: list of str
        :param KubeControllerManager: kube-controller-manager custom parameter
Note: this field may return null, indicating that no valid value is obtained.
        :type KubeControllerManager: list of str
        :param KubeScheduler: kube-scheduler custom parameter
Note: this field may return null, indicating that no valid value is obtained.
        :type KubeScheduler: list of str
        :param Etcd: etcd custom parameter, which is only effective for self-deployed cluster.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Etcd: list of str
        """
        self.KubeAPIServer = None
        self.KubeControllerManager = None
        self.KubeScheduler = None
        self.Etcd = None


    def _deserialize(self, params):
        self.KubeAPIServer = params.get("KubeAPIServer")
        self.KubeControllerManager = params.get("KubeControllerManager")
        self.KubeScheduler = params.get("KubeScheduler")
        self.Etcd = params.get("Etcd")


class ClusterNetworkSettings(AbstractModel):
    """Cluster network-related parameters

    """

    def __init__(self):
        """
        :param ClusterCIDR: CIDR used to assign container and service IPs for the cluster. It cannot conflict with the VPC's CIDR or the CIDRs of other clusters in the same VPC.
        :type ClusterCIDR: str
        :param IgnoreClusterCIDRConflict: Whether to ignore ClusterCIDR conflict errors. It defaults to not ignore.
        :type IgnoreClusterCIDRConflict: bool
        :param MaxNodePodNum: Maximum number of pods on each node in the cluster. Default value: 256
        :type MaxNodePodNum: int
        :param MaxClusterServiceNum: Maximum number of cluster services. Default value: 256
        :type MaxClusterServiceNum: int
        :param Ipvs: Whether IPVS is enabled. Default value: disabled
        :type Ipvs: bool
        :param VpcId: Cluster VPC ID, which is required when you create an empty cluster; otherwise, it is automatically set to be consistent with that of the nodes in the cluster
        :type VpcId: str
        :param Cni: Whether CNI is enabled for network plugin(s). Default value: enabled
        :type Cni: bool
        """
        self.ClusterCIDR = None
        self.IgnoreClusterCIDRConflict = None
        self.MaxNodePodNum = None
        self.MaxClusterServiceNum = None
        self.Ipvs = None
        self.VpcId = None
        self.Cni = None


    def _deserialize(self, params):
        self.ClusterCIDR = params.get("ClusterCIDR")
        self.IgnoreClusterCIDRConflict = params.get("IgnoreClusterCIDRConflict")
        self.MaxNodePodNum = params.get("MaxNodePodNum")
        self.MaxClusterServiceNum = params.get("MaxClusterServiceNum")
        self.Ipvs = params.get("Ipvs")
        self.VpcId = params.get("VpcId")
        self.Cni = params.get("Cni")


class ClusterVersion(AbstractModel):
    """Cluster version information

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param Versions: The list of cluster major version, such as 1.18.4
        :type Versions: list of str
        """
        self.ClusterId = None
        self.Versions = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Versions = params.get("Versions")


class CreateClusterAsGroupRequest(AbstractModel):
    """CreateClusterAsGroup request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param AutoScalingGroupPara: The pass-through parameters for scaling group creation, in the format of a JSON string. For more information, see the [CreateAutoScalingGroup](https://intl.cloud.tencent.com/document/api/377/20440?from_cn_redirect=1) API. The **LaunchConfigurationId** is created with the LaunchConfigurePara parameter, which does not support data entry.
        :type AutoScalingGroupPara: str
        :param LaunchConfigurePara: The pass-through parameters for launch configuration creation, in the format of a JSON string. For more information, see the [CreateLaunchConfiguration](https://intl.cloud.tencent.com/document/api/377/20447?from_cn_redirect=1) API. **ImageId** is not required as it is already included in the cluster dimension. **UserData** is not required as it's set through the **UserScript**.
        :type LaunchConfigurePara: str
        :param InstanceAdvancedSettings: Advanced configuration information of the node
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param Labels: Node label array
        :type Labels: list of Label
        """
        self.ClusterId = None
        self.AutoScalingGroupPara = None
        self.LaunchConfigurePara = None
        self.InstanceAdvancedSettings = None
        self.Labels = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.AutoScalingGroupPara = params.get("AutoScalingGroupPara")
        self.LaunchConfigurePara = params.get("LaunchConfigurePara")
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)


class CreateClusterAsGroupResponse(AbstractModel):
    """CreateClusterAsGroup response structure.

    """

    def __init__(self):
        """
        :param LaunchConfigurationId: Launch configuration ID
        :type LaunchConfigurationId: str
        :param AutoScalingGroupId: Scaling group ID
        :type AutoScalingGroupId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.LaunchConfigurationId = None
        self.AutoScalingGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.RequestId = params.get("RequestId")


class CreateClusterEndpointRequest(AbstractModel):
    """CreateClusterEndpoint request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param SubnetId: The ID of the subnet where the cluster's port is located (only needs to be entered when the non-public network access is enabled, and must be within the subnet of the cluster's VPC). 
        :type SubnetId: str
        :param IsExtranet: Whether public network access is enabled or not (True = public network access, FALSE = private network access, with the default value as FALSE).
        :type IsExtranet: bool
        """
        self.ClusterId = None
        self.SubnetId = None
        self.IsExtranet = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SubnetId = params.get("SubnetId")
        self.IsExtranet = params.get("IsExtranet")


class CreateClusterEndpointResponse(AbstractModel):
    """CreateClusterEndpoint response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateClusterEndpointVipRequest(AbstractModel):
    """CreateClusterEndpointVip request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param SecurityPolicies: Security policy opens single IP or CIDR to the Internet (for example: '192.168.1.0/24', with 'reject all' as the default).
        :type SecurityPolicies: list of str
        """
        self.ClusterId = None
        self.SecurityPolicies = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SecurityPolicies = params.get("SecurityPolicies")


class CreateClusterEndpointVipResponse(AbstractModel):
    """CreateClusterEndpointVip response structure.

    """

    def __init__(self):
        """
        :param RequestFlowId: Request job's FlowId
        :type RequestFlowId: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestFlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestFlowId = params.get("RequestFlowId")
        self.RequestId = params.get("RequestId")


class CreateClusterInstancesRequest(AbstractModel):
    """CreateClusterInstances request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID. Enter the ClusterId field returned by the DescribeClusters API
        :type ClusterId: str
        :param RunInstancePara: Pass-through parameter for CVM creation in the format of a JSON string. To ensure the idempotence of requests for adding cluster nodes, you need to add the ClientToken field in this parameter. For more information, see the documentation for [RunInstances](https://intl.cloud.tencent.com/document/product/213/15730?from_cn_redirect=1) API.
        :type RunInstancePara: str
        :param InstanceAdvancedSettings: Additional parameter to be set for the instance
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param SkipValidateOptions: Skips the specified verification. Valid values: GlobalRouteCIDRCheck, VpcCniCIDRCheck
        :type SkipValidateOptions: list of str
        """
        self.ClusterId = None
        self.RunInstancePara = None
        self.InstanceAdvancedSettings = None
        self.SkipValidateOptions = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RunInstancePara = params.get("RunInstancePara")
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        self.SkipValidateOptions = params.get("SkipValidateOptions")


class CreateClusterInstancesResponse(AbstractModel):
    """CreateClusterInstances response structure.

    """

    def __init__(self):
        """
        :param InstanceIdSet: Instance ID
        :type InstanceIdSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.RequestId = params.get("RequestId")


class CreateClusterNodePoolFromExistingAsgRequest(AbstractModel):
    """CreateClusterNodePoolFromExistingAsg request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param AutoscalingGroupId: Scaling group ID
        :type AutoscalingGroupId: str
        """
        self.ClusterId = None
        self.AutoscalingGroupId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.AutoscalingGroupId = params.get("AutoscalingGroupId")


class CreateClusterNodePoolFromExistingAsgResponse(AbstractModel):
    """CreateClusterNodePoolFromExistingAsg response structure.

    """

    def __init__(self):
        """
        :param NodePoolId: Node pool ID
        :type NodePoolId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NodePoolId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NodePoolId = params.get("NodePoolId")
        self.RequestId = params.get("RequestId")


class CreateClusterNodePoolRequest(AbstractModel):
    """CreateClusterNodePool request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param AutoScalingGroupPara: AS group parameters
        :type AutoScalingGroupPara: str
        :param LaunchConfigurePara: Running parameters
        :type LaunchConfigurePara: str
        :param InstanceAdvancedSettings: Sample parameters
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param EnableAutoscale: Indicates whether to enable auto scaling
        :type EnableAutoscale: bool
        :param Name: Node pool name
        :type Name: str
        :param Labels: Labels
        :type Labels: list of Label
        :param Taints: Taints
        :type Taints: list of Taint
        :param NodePoolOs: Operating system of the node pool
        :type NodePoolOs: str
        :param OsCustomizeType: Container image tag, `DOCKER_CUSTOMIZE` (container customized tag), `GENERAL` (general tag, default value)
        :type OsCustomizeType: str
        """
        self.ClusterId = None
        self.AutoScalingGroupPara = None
        self.LaunchConfigurePara = None
        self.InstanceAdvancedSettings = None
        self.EnableAutoscale = None
        self.Name = None
        self.Labels = None
        self.Taints = None
        self.NodePoolOs = None
        self.OsCustomizeType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.AutoScalingGroupPara = params.get("AutoScalingGroupPara")
        self.LaunchConfigurePara = params.get("LaunchConfigurePara")
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        self.EnableAutoscale = params.get("EnableAutoscale")
        self.Name = params.get("Name")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("Taints") is not None:
            self.Taints = []
            for item in params.get("Taints"):
                obj = Taint()
                obj._deserialize(item)
                self.Taints.append(obj)
        self.NodePoolOs = params.get("NodePoolOs")
        self.OsCustomizeType = params.get("OsCustomizeType")


class CreateClusterNodePoolResponse(AbstractModel):
    """CreateClusterNodePool response structure.

    """

    def __init__(self):
        """
        :param NodePoolId: Node pool ID
        :type NodePoolId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NodePoolId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NodePoolId = params.get("NodePoolId")
        self.RequestId = params.get("RequestId")


class CreateClusterRequest(AbstractModel):
    """CreateCluster request structure.

    """

    def __init__(self):
        """
        :param ClusterCIDRSettings: Container networking configuration information for the cluster
        :type ClusterCIDRSettings: :class:`tencentcloud.tke.v20180525.models.ClusterCIDRSettings`
        :param ClusterType: Cluster type. Managed cluster: MANAGED_CLUSTER; self-deployed cluster: INDEPENDENT_CLUSTER.
        :type ClusterType: str
        :param RunInstancesForNode: Pass-through parameter for CVM creation in the format of a JSON string. For more information, see the API for [creating a CVM instance](https://intl.cloud.tencent.com/document/product/213/15730?from_cn_redirect=1).
        :type RunInstancesForNode: list of RunInstancesForNode
        :param ClusterBasicSettings: Basic configuration information of the cluster
        :type ClusterBasicSettings: :class:`tencentcloud.tke.v20180525.models.ClusterBasicSettings`
        :param ClusterAdvancedSettings: Advanced configuration information of the cluster
        :type ClusterAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.ClusterAdvancedSettings`
        :param InstanceAdvancedSettings: Advanced configuration information of the node
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param ExistedInstancesForNode: Configuration information of an existing instance
        :type ExistedInstancesForNode: list of ExistedInstancesForNode
        :param InstanceDataDiskMountSettings: CVM type and the corresponding data disk mounting configuration information.
        :type InstanceDataDiskMountSettings: list of InstanceDataDiskMountSetting
        :param ExtensionAddons: Information of the add-on to be installed
        :type ExtensionAddons: list of ExtensionAddon
        """
        self.ClusterCIDRSettings = None
        self.ClusterType = None
        self.RunInstancesForNode = None
        self.ClusterBasicSettings = None
        self.ClusterAdvancedSettings = None
        self.InstanceAdvancedSettings = None
        self.ExistedInstancesForNode = None
        self.InstanceDataDiskMountSettings = None
        self.ExtensionAddons = None


    def _deserialize(self, params):
        if params.get("ClusterCIDRSettings") is not None:
            self.ClusterCIDRSettings = ClusterCIDRSettings()
            self.ClusterCIDRSettings._deserialize(params.get("ClusterCIDRSettings"))
        self.ClusterType = params.get("ClusterType")
        if params.get("RunInstancesForNode") is not None:
            self.RunInstancesForNode = []
            for item in params.get("RunInstancesForNode"):
                obj = RunInstancesForNode()
                obj._deserialize(item)
                self.RunInstancesForNode.append(obj)
        if params.get("ClusterBasicSettings") is not None:
            self.ClusterBasicSettings = ClusterBasicSettings()
            self.ClusterBasicSettings._deserialize(params.get("ClusterBasicSettings"))
        if params.get("ClusterAdvancedSettings") is not None:
            self.ClusterAdvancedSettings = ClusterAdvancedSettings()
            self.ClusterAdvancedSettings._deserialize(params.get("ClusterAdvancedSettings"))
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        if params.get("ExistedInstancesForNode") is not None:
            self.ExistedInstancesForNode = []
            for item in params.get("ExistedInstancesForNode"):
                obj = ExistedInstancesForNode()
                obj._deserialize(item)
                self.ExistedInstancesForNode.append(obj)
        if params.get("InstanceDataDiskMountSettings") is not None:
            self.InstanceDataDiskMountSettings = []
            for item in params.get("InstanceDataDiskMountSettings"):
                obj = InstanceDataDiskMountSetting()
                obj._deserialize(item)
                self.InstanceDataDiskMountSettings.append(obj)
        if params.get("ExtensionAddons") is not None:
            self.ExtensionAddons = []
            for item in params.get("ExtensionAddons"):
                obj = ExtensionAddon()
                obj._deserialize(item)
                self.ExtensionAddons.append(obj)


class CreateClusterResponse(AbstractModel):
    """CreateCluster response structure.

    """

    def __init__(self):
        """
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


class CreateClusterRouteTableRequest(AbstractModel):
    """CreateClusterRouteTable request structure.

    """

    def __init__(self):
        """
        :param RouteTableName: Route table name
        :type RouteTableName: str
        :param RouteTableCidrBlock: Route table CIDR
        :type RouteTableCidrBlock: str
        :param VpcId: VPC bound to the route table
        :type VpcId: str
        :param IgnoreClusterCidrConflict: Whether to ignore CIDR conflicts
        :type IgnoreClusterCidrConflict: int
        """
        self.RouteTableName = None
        self.RouteTableCidrBlock = None
        self.VpcId = None
        self.IgnoreClusterCidrConflict = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")
        self.RouteTableCidrBlock = params.get("RouteTableCidrBlock")
        self.VpcId = params.get("VpcId")
        self.IgnoreClusterCidrConflict = params.get("IgnoreClusterCidrConflict")


class CreateClusterRouteTableResponse(AbstractModel):
    """CreateClusterRouteTable response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """Described the configuration and information of k8s node data disk.

    """

    def __init__(self):
        """
        :param DiskType: Disk type
Note: this field may return null, indicating that no valid values can be obtained.
        :type DiskType: str
        :param FileSystem: File system (ext3/ext4/xfs)
Note: This field may return null, indicating that no valid value was found.
        :type FileSystem: str
        :param DiskSize: Disk size (G)
Note: This field may return null, indicating that no valid value was found.
        :type DiskSize: int
        :param AutoFormatAndMount: Whether the disk is auto-formatted and mounted
Note: this field may return `null`, indicating that no valid value is obtained.
        :type AutoFormatAndMount: bool
        :param MountTarget: Mounting directory
Note: This field may return null, indicating that no valid value was found.
        :type MountTarget: str
        """
        self.DiskType = None
        self.FileSystem = None
        self.DiskSize = None
        self.AutoFormatAndMount = None
        self.MountTarget = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.FileSystem = params.get("FileSystem")
        self.DiskSize = params.get("DiskSize")
        self.AutoFormatAndMount = params.get("AutoFormatAndMount")
        self.MountTarget = params.get("MountTarget")


class DeleteClusterAsGroupsRequest(AbstractModel):
    """DeleteClusterAsGroups request structure.

    """

    def __init__(self):
        """
        :param ClusterId: The cluster ID, obtained through the [DescribeClusters](https://intl.cloud.tencent.com/document/api/457/31862?from_cn_redirect=1) API.
        :type ClusterId: str
        :param AutoScalingGroupIds: Cluster scaling group ID list
        :type AutoScalingGroupIds: list of str
        :param KeepInstance: Whether to keep nodes in the scaling group. Default to **false** (not keep)
        :type KeepInstance: bool
        """
        self.ClusterId = None
        self.AutoScalingGroupIds = None
        self.KeepInstance = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.AutoScalingGroupIds = params.get("AutoScalingGroupIds")
        self.KeepInstance = params.get("KeepInstance")


class DeleteClusterAsGroupsResponse(AbstractModel):
    """DeleteClusterAsGroups response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterEndpointRequest(AbstractModel):
    """DeleteClusterEndpoint request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param IsExtranet: Whether public network access is enabled or not (True = public network access, FALSE = private network access, with the default value as FALSE).
        :type IsExtranet: bool
        """
        self.ClusterId = None
        self.IsExtranet = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.IsExtranet = params.get("IsExtranet")


class DeleteClusterEndpointResponse(AbstractModel):
    """DeleteClusterEndpoint response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterEndpointVipRequest(AbstractModel):
    """DeleteClusterEndpointVip request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")


class DeleteClusterEndpointVipResponse(AbstractModel):
    """DeleteClusterEndpointVip response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterInstancesRequest(AbstractModel):
    """DeleteClusterInstances request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param InstanceIds: List of Instance IDs
        :type InstanceIds: list of str
        :param InstanceDeleteMode: Policy used to delete an instance in the cluster: `terminate` (terminates the instance. Only available for pay-as-you-go CVMs); `retain` (only removes it from the cluster. The instance will be retained.)
        :type InstanceDeleteMode: str
        :param ForceDelete: Whether or not there is forced deletion (when a node is initialized, the parameters can be specified as TRUE)
        :type ForceDelete: bool
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.InstanceDeleteMode = None
        self.ForceDelete = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceDeleteMode = params.get("InstanceDeleteMode")
        self.ForceDelete = params.get("ForceDelete")


class DeleteClusterInstancesResponse(AbstractModel):
    """DeleteClusterInstances response structure.

    """

    def __init__(self):
        """
        :param SuccInstanceIds: IDs of deleted instances
        :type SuccInstanceIds: list of str
        :param FailedInstanceIds: IDs of instances failed to be deleted
        :type FailedInstanceIds: list of str
        :param NotFoundInstanceIds: IDs of instances that cannot be found
        :type NotFoundInstanceIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SuccInstanceIds = None
        self.FailedInstanceIds = None
        self.NotFoundInstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccInstanceIds = params.get("SuccInstanceIds")
        self.FailedInstanceIds = params.get("FailedInstanceIds")
        self.NotFoundInstanceIds = params.get("NotFoundInstanceIds")
        self.RequestId = params.get("RequestId")


class DeleteClusterNodePoolRequest(AbstractModel):
    """DeleteClusterNodePool request structure.

    """

    def __init__(self):
        """
        :param ClusterId: ClusterId of a node pool
        :type ClusterId: str
        :param NodePoolIds: IDs of node pools to delete
        :type NodePoolIds: list of str
        :param KeepInstance: Indicates whether nodes in a node pool are retained when the node pool is deleted. (The nodes are removed from the cluster. However, the corresponding instances will not be terminated.)
        :type KeepInstance: bool
        """
        self.ClusterId = None
        self.NodePoolIds = None
        self.KeepInstance = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NodePoolIds = params.get("NodePoolIds")
        self.KeepInstance = params.get("KeepInstance")


class DeleteClusterNodePoolResponse(AbstractModel):
    """DeleteClusterNodePool response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterRequest(AbstractModel):
    """DeleteCluster request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param InstanceDeleteMode: Policy used to delete an instance in the cluster: terminate (terminates the instance. Only available for instances on pay-as-you-go CVMs); retain (only removes it from the cluster. The instance will be retained.)
        :type InstanceDeleteMode: str
        :param ResourceDeleteOptions: Specifies the policy to deal with resources in the cluster when the cluster is deleted. It only supports CBS now. The default policy is to retain CBS disks.
        :type ResourceDeleteOptions: list of ResourceDeleteOption
        """
        self.ClusterId = None
        self.InstanceDeleteMode = None
        self.ResourceDeleteOptions = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceDeleteMode = params.get("InstanceDeleteMode")
        if params.get("ResourceDeleteOptions") is not None:
            self.ResourceDeleteOptions = []
            for item in params.get("ResourceDeleteOptions"):
                obj = ResourceDeleteOption()
                obj._deserialize(item)
                self.ResourceDeleteOptions.append(obj)


class DeleteClusterResponse(AbstractModel):
    """DeleteCluster response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterRouteRequest(AbstractModel):
    """DeleteClusterRoute request structure.

    """

    def __init__(self):
        """
        :param RouteTableName: Route table name.
        :type RouteTableName: str
        :param GatewayIp: Next hop address.
        :type GatewayIp: str
        :param DestinationCidrBlock: Destination CIDR.
        :type DestinationCidrBlock: str
        """
        self.RouteTableName = None
        self.GatewayIp = None
        self.DestinationCidrBlock = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")
        self.GatewayIp = params.get("GatewayIp")
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")


class DeleteClusterRouteResponse(AbstractModel):
    """DeleteClusterRoute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterRouteTableRequest(AbstractModel):
    """DeleteClusterRouteTable request structure.

    """

    def __init__(self):
        """
        :param RouteTableName: Route table name
        :type RouteTableName: str
        """
        self.RouteTableName = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")


class DeleteClusterRouteTableResponse(AbstractModel):
    """DeleteClusterRouteTable response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAvailableClusterVersionRequest(AbstractModel):
    """DescribeAvailableClusterVersion request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param ClusterIds: List of cluster IDs
        :type ClusterIds: list of str
        """
        self.ClusterId = None
        self.ClusterIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterIds = params.get("ClusterIds")


class DescribeAvailableClusterVersionResponse(AbstractModel):
    """DescribeAvailableClusterVersion response structure.

    """

    def __init__(self):
        """
        :param Versions: Upgradable cluster version
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Versions: list of str
        :param Clusters: Cluster information
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Clusters: list of ClusterVersion
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Versions = None
        self.Clusters = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Versions = params.get("Versions")
        if params.get("Clusters") is not None:
            self.Clusters = []
            for item in params.get("Clusters"):
                obj = ClusterVersion()
                obj._deserialize(item)
                self.Clusters.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterAsGroupOptionRequest(AbstractModel):
    """DescribeClusterAsGroupOption request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")


class DescribeClusterAsGroupOptionResponse(AbstractModel):
    """DescribeClusterAsGroupOption response structure.

    """

    def __init__(self):
        """
        :param ClusterAsGroupOption: Cluster auto scaling attributes
Note: this field may return null, indicating that no valid value was found.
        :type ClusterAsGroupOption: :class:`tencentcloud.tke.v20180525.models.ClusterAsGroupOption`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ClusterAsGroupOption = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterAsGroupOption") is not None:
            self.ClusterAsGroupOption = ClusterAsGroupOption()
            self.ClusterAsGroupOption._deserialize(params.get("ClusterAsGroupOption"))
        self.RequestId = params.get("RequestId")


class DescribeClusterAsGroupsRequest(AbstractModel):
    """DescribeClusterAsGroups request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param AutoScalingGroupIds: Scaling group ID list. If this value is null, it indicates that all cluster-associated scaling groups are pulled.
        :type AutoScalingGroupIds: list of str
        :param Offset: Offset. This value defaults to 0. For more information on Offset, see the relevant sections in API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param Limit: Number of returned results. This value defaults to 20. The maximum is 100. For more information on Limit, see the relevant sections in API [Overview](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        """
        self.ClusterId = None
        self.AutoScalingGroupIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.AutoScalingGroupIds = params.get("AutoScalingGroupIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeClusterAsGroupsResponse(AbstractModel):
    """DescribeClusterAsGroups response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of scaling groups associated with the cluster
        :type TotalCount: int
        :param ClusterAsGroupSet: Cluster-associated scaling group list
        :type ClusterAsGroupSet: list of ClusterAsGroup
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ClusterAsGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ClusterAsGroupSet") is not None:
            self.ClusterAsGroupSet = []
            for item in params.get("ClusterAsGroupSet"):
                obj = ClusterAsGroup()
                obj._deserialize(item)
                self.ClusterAsGroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterEndpointStatusRequest(AbstractModel):
    """DescribeClusterEndpointStatus request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param IsExtranet: Whether public network access is enabled or not (True = public network access, FALSE = private network access, with the default value as FALSE).
        :type IsExtranet: bool
        """
        self.ClusterId = None
        self.IsExtranet = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.IsExtranet = params.get("IsExtranet")


class DescribeClusterEndpointStatusResponse(AbstractModel):
    """DescribeClusterEndpointStatus response structure.

    """

    def __init__(self):
        """
        :param Status: Queries cluster access port status (Created = successfully enabled; Creating = in the process of being enabled; NotFound = not enabled).
        :type Status: str
        :param ErrorMsg: Details of the error occurred while opening the access port
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ErrorMsg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class DescribeClusterEndpointVipStatusRequest(AbstractModel):
    """DescribeClusterEndpointVipStatus request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")


class DescribeClusterEndpointVipStatusResponse(AbstractModel):
    """DescribeClusterEndpointVipStatus response structure.

    """

    def __init__(self):
        """
        :param Status: Port operation status (Creating = in the process of creation; CreateFailed = creation has failed; Created = creation completed; Deleting = in the process of deletion; DeletedFailed = deletion has failed; Deleted = deletion completed; NotFound = operation not found)
        :type Status: str
        :param ErrorMsg: Reason for operation failure
        :type ErrorMsg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class DescribeClusterInstancesRequest(AbstractModel):
    """DescribeClusterInstances request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param Offset: Offset. Default value: 0
        :type Offset: int
        :param Limit: Maximum number of output entries. Default value: 20
        :type Limit: int
        :param InstanceIds: List of instance IDs to be obtained. This parameter is empty by default, which indicates that all instances in the cluster will be pulled.
        :type InstanceIds: list of str
        :param InstanceRole: Node role. Valid values are MASTER, WORKER, ETCD, MASTER_ETCD, and ALL. Default value: WORKER.
        :type InstanceRole: str
        """
        self.ClusterId = None
        self.Offset = None
        self.Limit = None
        self.InstanceIds = None
        self.InstanceRole = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceRole = params.get("InstanceRole")


class DescribeClusterInstancesResponse(AbstractModel):
    """DescribeClusterInstances response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of instances in the cluster
        :type TotalCount: int
        :param InstanceSet: List of instances in the cluster
        :type InstanceSet: list of Instance
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterKubeconfigRequest(AbstractModel):
    """DescribeClusterKubeconfig request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")


class DescribeClusterKubeconfigResponse(AbstractModel):
    """DescribeClusterKubeconfig response structure.

    """

    def __init__(self):
        """
        :param Kubeconfig: Sub-account kubeconfig file, used to access the cluster kube-apiserver directly
        :type Kubeconfig: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Kubeconfig = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Kubeconfig = params.get("Kubeconfig")
        self.RequestId = params.get("RequestId")


class DescribeClusterNodePoolDetailRequest(AbstractModel):
    """DescribeClusterNodePoolDetail request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param NodePoolId: Node pool ID
        :type NodePoolId: str
        """
        self.ClusterId = None
        self.NodePoolId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NodePoolId = params.get("NodePoolId")


class DescribeClusterNodePoolDetailResponse(AbstractModel):
    """DescribeClusterNodePoolDetail response structure.

    """

    def __init__(self):
        """
        :param NodePool: Node pool details
        :type NodePool: :class:`tencentcloud.tke.v20180525.models.NodePool`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NodePool = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NodePool") is not None:
            self.NodePool = NodePool()
            self.NodePool._deserialize(params.get("NodePool"))
        self.RequestId = params.get("RequestId")


class DescribeClusterNodePoolsRequest(AbstractModel):
    """DescribeClusterNodePools request structure.

    """

    def __init__(self):
        """
        :param ClusterId: ClusterId (cluster ID)
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")


class DescribeClusterNodePoolsResponse(AbstractModel):
    """DescribeClusterNodePools response structure.

    """

    def __init__(self):
        """
        :param NodePoolSet: NodePools (node pool list)
Note: this field may return `null`, indicating that no valid value is obtained.
        :type NodePoolSet: list of NodePool
        :param TotalCount: Total resources
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.NodePoolSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NodePoolSet") is not None:
            self.NodePoolSet = []
            for item in params.get("NodePoolSet"):
                obj = NodePool()
                obj._deserialize(item)
                self.NodePoolSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeClusterRouteTablesRequest(AbstractModel):
    """DescribeClusterRouteTables request structure.

    """


class DescribeClusterRouteTablesResponse(AbstractModel):
    """DescribeClusterRouteTables response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of instances that match the filter condition(s).
        :type TotalCount: int
        :param RouteTableSet: Object of cluster route table.
        :type RouteTableSet: list of RouteTableInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.RouteTableSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RouteTableSet") is not None:
            self.RouteTableSet = []
            for item in params.get("RouteTableSet"):
                obj = RouteTableInfo()
                obj._deserialize(item)
                self.RouteTableSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterRoutesRequest(AbstractModel):
    """DescribeClusterRoutes request structure.

    """

    def __init__(self):
        """
        :param RouteTableName: Route table name.
        :type RouteTableName: str
        :param Filters: Filtering conditions, which are optional. Currently, only filtering by GatewayIP is supported.
        :type Filters: list of Filter
        """
        self.RouteTableName = None
        self.Filters = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeClusterRoutesResponse(AbstractModel):
    """DescribeClusterRoutes response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of instances that match the filter condition(s).
        :type TotalCount: int
        :param RouteSet: Object of cluster route.
        :type RouteSet: list of RouteInfo
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.RouteSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RouteSet") is not None:
            self.RouteSet = []
            for item in params.get("RouteSet"):
                obj = RouteInfo()
                obj._deserialize(item)
                self.RouteSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterSecurityRequest(AbstractModel):
    """DescribeClusterSecurity request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID. Enter the ClusterId field returned by the DescribeClusters API
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")


class DescribeClusterSecurityResponse(AbstractModel):
    """DescribeClusterSecurity response structure.

    """

    def __init__(self):
        """
        :param UserName: Cluster's account name
        :type UserName: str
        :param Password: Cluster's password
        :type Password: str
        :param CertificationAuthority: Cluster's access CA certificate
        :type CertificationAuthority: str
        :param ClusterExternalEndpoint: Cluster's access address
        :type ClusterExternalEndpoint: str
        :param Domain: Domain name accessed by the cluster
        :type Domain: str
        :param PgwEndpoint: Cluster's endpoint address
        :type PgwEndpoint: str
        :param SecurityPolicy: Cluster's access policy group
Note: This field may return null, indicating that no valid value was found.
        :type SecurityPolicy: list of str
        :param Kubeconfig: Cluster Kubeconfig file
Note: This field may return null, indicating that no valid value was found.
        :type Kubeconfig: str
        :param JnsGwEndpoint: Access address of the cluster JnsGw
Note: This field may return null, indicating that no valid value was found.
        :type JnsGwEndpoint: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.UserName = None
        self.Password = None
        self.CertificationAuthority = None
        self.ClusterExternalEndpoint = None
        self.Domain = None
        self.PgwEndpoint = None
        self.SecurityPolicy = None
        self.Kubeconfig = None
        self.JnsGwEndpoint = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        self.CertificationAuthority = params.get("CertificationAuthority")
        self.ClusterExternalEndpoint = params.get("ClusterExternalEndpoint")
        self.Domain = params.get("Domain")
        self.PgwEndpoint = params.get("PgwEndpoint")
        self.SecurityPolicy = params.get("SecurityPolicy")
        self.Kubeconfig = params.get("Kubeconfig")
        self.JnsGwEndpoint = params.get("JnsGwEndpoint")
        self.RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters request structure.

    """

    def __init__(self):
        """
        :param ClusterIds: Cluster ID list (When it is empty,
all clusters under the account will be obtained)
        :type ClusterIds: list of str
        :param Offset: Offset. Default value: 0
        :type Offset: int
        :param Limit: Maximum number of output entries. Default value: 20
        :type Limit: int
        :param Filters: Filter condition. Currently, only filtering by a single ClusterName is supported
        :type Filters: list of Filter
        """
        self.ClusterIds = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.ClusterIds = params.get("ClusterIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Total number of clusters
        :type TotalCount: int
        :param Clusters: Cluster information list
        :type Clusters: list of Cluster
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Clusters = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Clusters") is not None:
            self.Clusters = []
            for item in params.get("Clusters"):
                obj = Cluster()
                obj._deserialize(item)
                self.Clusters.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeExistedInstancesRequest(AbstractModel):
    """DescribeExistedInstances request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID. Enter the `ClusterId` field returned when you call the DescribeClusters API (Only VPC ID obtained through `ClusterId` need filtering conditions. When comparing statuses, the nodes on all clusters in this region will be used for comparison. You cannot specify `InstanceIds` and `ClusterId` at the same time.)
        :type ClusterId: str
        :param InstanceIds: Query by one or more instance ID(s). Instance ID format: ins-xxxxxxxx. (Refer to section ID.N of the API overview for this parameter's specific format.) Up to 100 instances are allowed for each request. You cannot specify InstanceIds and Filters at the same time.
        :type InstanceIds: list of str
        :param Filters: Filter condition. For fields and other information, see [the DescribeInstances API](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1). If a ClusterId has been set, then the cluster's VPC ID will be attached as a query field. In this situation, if a "vpc-id" is specified in Filter, then the specified VPC ID must be consistent with the cluster's VPC ID.
        :type Filters: list of Filter
        :param VagueIpAddress: Filter by instance IP (Supports both private and public IPs)
        :type VagueIpAddress: str
        :param VagueInstanceName: Filter by instance name
        :type VagueInstanceName: str
        :param Offset: Offset. Default value: 0. For more information on Offset, see the relevant section in the API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on Limit, see the relevant section in the API [Introduction](https://intl.cloud.tencent.com/document/api/213/15688?from_cn_redirect=1).
        :type Limit: int
        :param IpAddresses: Filter by multiple instance IPs
        :type IpAddresses: list of str
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.Filters = None
        self.VagueIpAddress = None
        self.VagueInstanceName = None
        self.Offset = None
        self.Limit = None
        self.IpAddresses = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.VagueIpAddress = params.get("VagueIpAddress")
        self.VagueInstanceName = params.get("VagueInstanceName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.IpAddresses = params.get("IpAddresses")


class DescribeExistedInstancesResponse(AbstractModel):
    """DescribeExistedInstances response structure.

    """

    def __init__(self):
        """
        :param ExistedInstanceSet: Array of existing instance information.
Note: This field may return null, indicating that no valid values can be obtained.
        :type ExistedInstanceSet: list of ExistedInstance
        :param TotalCount: Number of instances that match the filter condition(s).
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ExistedInstanceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ExistedInstanceSet") is not None:
            self.ExistedInstanceSet = []
            for item in params.get("ExistedInstanceSet"):
                obj = ExistedInstance()
                obj._deserialize(item)
                self.ExistedInstanceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages request structure.

    """


class DescribeImagesResponse(AbstractModel):
    """DescribeImages response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of images
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param ImageInstanceSet: Image information list
Note: this field may return null, indicating that no valid values can be obtained.
        :type ImageInstanceSet: list of ImageInstance
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.ImageInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ImageInstanceSet") is not None:
            self.ImageInstanceSet = []
            for item in params.get("ImageInstanceSet"):
                obj = ImageInstance()
                obj._deserialize(item)
                self.ImageInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions request structure.

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions response structure.

    """

    def __init__(self):
        """
        :param TotalCount: Number of regions
Note: this field may return null, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param RegionInstanceSet: ## Region List
Note: this field may return null, indicating that no valid values can be obtained.
        :type RegionInstanceSet: list of RegionInstance
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.RegionInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RegionInstanceSet") is not None:
            self.RegionInstanceSet = []
            for item in params.get("RegionInstanceSet"):
                obj = RegionInstance()
                obj._deserialize(item)
                self.RegionInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRouteTableConflictsRequest(AbstractModel):
    """DescribeRouteTableConflicts request structure.

    """

    def __init__(self):
        """
        :param RouteTableCidrBlock: Route table CIDR
        :type RouteTableCidrBlock: str
        :param VpcId: VPC bound to the route table
        :type VpcId: str
        """
        self.RouteTableCidrBlock = None
        self.VpcId = None


    def _deserialize(self, params):
        self.RouteTableCidrBlock = params.get("RouteTableCidrBlock")
        self.VpcId = params.get("VpcId")


class DescribeRouteTableConflictsResponse(AbstractModel):
    """DescribeRouteTableConflicts response structure.

    """

    def __init__(self):
        """
        :param HasConflict: Whether there is a conflict in the route table.
        :type HasConflict: bool
        :param RouteTableConflictSet: Route table conflict list.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RouteTableConflictSet: list of RouteTableConflict
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.HasConflict = None
        self.RouteTableConflictSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.HasConflict = params.get("HasConflict")
        if params.get("RouteTableConflictSet") is not None:
            self.RouteTableConflictSet = []
            for item in params.get("RouteTableConflictSet"):
                obj = RouteTableConflict()
                obj._deserialize(item)
                self.RouteTableConflictSet.append(obj)
        self.RequestId = params.get("RequestId")


class EnhancedService(AbstractModel):
    """Describes the configuration of enhanced services, such as Cloud Security and Cloud Monitor.

    """

    def __init__(self):
        """
        :param SecurityService: Enables cloud security service. If this parameter is not specified, the cloud security service will be enabled by default.
        :type SecurityService: :class:`tencentcloud.tke.v20180525.models.RunSecurityServiceEnabled`
        :param MonitorService: Enables cloud monitor service. If this parameter is not specified, the cloud monitor service will be enabled by default.
        :type MonitorService: :class:`tencentcloud.tke.v20180525.models.RunMonitorServiceEnabled`
        """
        self.SecurityService = None
        self.MonitorService = None


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self.SecurityService = RunSecurityServiceEnabled()
            self.SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self.MonitorService = RunMonitorServiceEnabled()
            self.MonitorService._deserialize(params.get("MonitorService"))


class ExistedInstance(AbstractModel):
    """Information of existing instances

    """

    def __init__(self):
        """
        :param Usable: Whether the instance supports being added to the cluster (TRUE: support; FALSE: not support).
Note: This field may return null, indicating that no valid values can be obtained.
        :type Usable: bool
        :param UnusableReason: Reason that the instance does not support being added.
Note: This field may return null, indicating that no valid values can be obtained.
        :type UnusableReason: str
        :param AlreadyInCluster: ID of the cluster in which the instance currently resides.
Note: This field may return null, indicating that no valid values can be obtained.
        :type AlreadyInCluster: str
        :param InstanceId: Instance ID, in the format of ins-xxxxxxxx.
        :type InstanceId: str
        :param InstanceName: Instance name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceName: str
        :param PrivateIpAddresses: List of private IPs of the instance's primary ENI.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrivateIpAddresses: list of str
        :param PublicIpAddresses: List of public IPs of the instance's primary ENI.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PublicIpAddresses: list of str
        :param CreatedTime: Creation time, which follows the ISO8601 standard and uses UTC time. Format: YYYY-MM-DDThh:mm:ssZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param CPU: Instance's number of CPU cores. Unit: cores.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CPU: int
        :param Memory: Instance's memory capacity. Unit: GB.
Note: This field may return null, indicating that no valid values can be obtained.
        :type Memory: int
        :param OsName: Operating system name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type OsName: str
        :param InstanceType: Instance model.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceType: str
        :param AutoscalingGroupId: Auto scaling group ID
Note: This field may return null, indicating that no valid value was found.
        :type AutoscalingGroupId: str
        :param InstanceChargeType: Instance billing method. Valid values: POSTPAID_BY_HOUR (pay-as-you-go hourly); CDHPAID (billed based on CDH, i.e., only CDH is billed but not the instances on CDH)
Note: This field may return null, indicating that no valid value was found.
        :type InstanceChargeType: str
        """
        self.Usable = None
        self.UnusableReason = None
        self.AlreadyInCluster = None
        self.InstanceId = None
        self.InstanceName = None
        self.PrivateIpAddresses = None
        self.PublicIpAddresses = None
        self.CreatedTime = None
        self.CPU = None
        self.Memory = None
        self.OsName = None
        self.InstanceType = None
        self.AutoscalingGroupId = None
        self.InstanceChargeType = None


    def _deserialize(self, params):
        self.Usable = params.get("Usable")
        self.UnusableReason = params.get("UnusableReason")
        self.AlreadyInCluster = params.get("AlreadyInCluster")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.CreatedTime = params.get("CreatedTime")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.OsName = params.get("OsName")
        self.InstanceType = params.get("InstanceType")
        self.AutoscalingGroupId = params.get("AutoscalingGroupId")
        self.InstanceChargeType = params.get("InstanceChargeType")


class ExistedInstancesForNode(AbstractModel):
    """Configuration parameters of existing nodes in different roles

    """

    def __init__(self):
        """
        :param NodeRole: Node role. Values: MASTER_ETCD, WORKER. You only need to specify MASTER_ETCD when creating a self-deployed cluster (INDEPENDENT_CLUSTER).
        :type NodeRole: str
        :param ExistedInstancesPara: Reinstallation parameter of existing instances
        :type ExistedInstancesPara: :class:`tencentcloud.tke.v20180525.models.ExistedInstancesPara`
        :param InstanceAdvancedSettingsOverride: Advanced node setting, which overrides the InstanceAdvancedSettings item set at the cluster level (currently valid for the ExtraArgs node custom parameter only)
        :type InstanceAdvancedSettingsOverride: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        """
        self.NodeRole = None
        self.ExistedInstancesPara = None
        self.InstanceAdvancedSettingsOverride = None


    def _deserialize(self, params):
        self.NodeRole = params.get("NodeRole")
        if params.get("ExistedInstancesPara") is not None:
            self.ExistedInstancesPara = ExistedInstancesPara()
            self.ExistedInstancesPara._deserialize(params.get("ExistedInstancesPara"))
        if params.get("InstanceAdvancedSettingsOverride") is not None:
            self.InstanceAdvancedSettingsOverride = InstanceAdvancedSettings()
            self.InstanceAdvancedSettingsOverride._deserialize(params.get("InstanceAdvancedSettingsOverride"))


class ExistedInstancesPara(AbstractModel):
    """Reinstallation parameter of existing instances

    """

    def __init__(self):
        """
        :param InstanceIds: Cluster ID
        :type InstanceIds: list of str
        :param InstanceAdvancedSettings: Additional parameter to be set for the instance
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param EnhancedService: Enhanced services. This parameter is used to specify whether to enable Cloud Security, Cloud Monitor and other services. If this parameter is not specified, Cloud Monitor and Cloud Security are enabled by default.
        :type EnhancedService: :class:`tencentcloud.tke.v20180525.models.EnhancedService`
        :param LoginSettings: Node login information (currently only supports using Password or single KeyIds)
        :type LoginSettings: :class:`tencentcloud.tke.v20180525.models.LoginSettings`
        :param SecurityGroupIds: Security group to which the instance belongs. This parameter can be obtained from the sgId field in the returned values of DescribeSecurityGroups. If this parameter is not specified, the default security group is bound. (Currently, you can only set a single sgId)
        :type SecurityGroupIds: list of str
        :param HostName: When reinstalling the system, you can specify the HostName of the modified instance (when the cluster is in HostName mode, this parameter is required, and the rule name is the same as the [Create CVM Instance](https://intl.cloud.tencent.com/document/product/213/15730?from_cn_redirect=1) API HostName except for uppercase letters not being supported.
        :type HostName: str
        """
        self.InstanceIds = None
        self.InstanceAdvancedSettings = None
        self.EnhancedService = None
        self.LoginSettings = None
        self.SecurityGroupIds = None
        self.HostName = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.HostName = params.get("HostName")


class ExtensionAddon(AbstractModel):
    """Information of the add-on selected for installation during cluster creation

    """

    def __init__(self):
        """
        :param AddonName: Add-on name
        :type AddonName: str
        :param AddonParam: Add-on information (description of the add-on resource object in JSON string format)
        :type AddonParam: str
        """
        self.AddonName = None
        self.AddonParam = None


    def _deserialize(self, params):
        self.AddonName = params.get("AddonName")
        self.AddonParam = params.get("AddonParam")


class Filter(AbstractModel):
    """> Key-value pair filters used for conditional queries, such as filtering results by ID, name, and state.
    > * If there are multiple `Filter` parameters, they are evaluated using the logical `AND` operator.
    > * If a `Filter` contains multiple `Values`, they are evaluated using the logical `OR` operator.
    >
    > Take [DescribeInstances](https://intl.cloud.tencent.com/document/api/213/15728?from_cn_redirect=1) as an example. You can use the following filters to query the instances in availability zone (`zone`) Guangzhou Zone 1 ***and*** whose billing plan (`instance-charge-type`) is pay-as-you-go:
    ```
    Filters.0.Name=zone
    &Filters.0.Values.0=ap-guangzhou-1
    &Filters.1.Name=instance-charge-type
    &Filters.1.Values.0=POSTPAID_BY_HOUR
    ```

    """

    def __init__(self):
        """
        :param Name: Filters.
        :type Name: str
        :param Values: Filter values.
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class GetUpgradeInstanceProgressRequest(AbstractModel):
    """GetUpgradeInstanceProgress request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param Limit: Maximum number of nodes to be queried
        :type Limit: int
        :param Offset: The starting node for the query
        :type Offset: int
        """
        self.ClusterId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class GetUpgradeInstanceProgressResponse(AbstractModel):
    """GetUpgradeInstanceProgress response structure.

    """

    def __init__(self):
        """
        :param Total: Total nodes to upgrade
        :type Total: int
        :param Done: Total upgraded nodes
        :type Done: int
        :param LifeState: The lifecycle of the upgrade task
process: running
paused: stopped
pausing: stopping
done: completed
timeout: timed out
aborted: canceled
        :type LifeState: str
        :param Instances: Details of upgrade progress of each node
        :type Instances: list of InstanceUpgradeProgressItem
        :param ClusterStatus: Current cluster status
        :type ClusterStatus: :class:`tencentcloud.tke.v20180525.models.InstanceUpgradeClusterStatus`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Total = None
        self.Done = None
        self.LifeState = None
        self.Instances = None
        self.ClusterStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.Done = params.get("Done")
        self.LifeState = params.get("LifeState")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = InstanceUpgradeProgressItem()
                obj._deserialize(item)
                self.Instances.append(obj)
        if params.get("ClusterStatus") is not None:
            self.ClusterStatus = InstanceUpgradeClusterStatus()
            self.ClusterStatus._deserialize(params.get("ClusterStatus"))
        self.RequestId = params.get("RequestId")


class ImageInstance(AbstractModel):
    """Image details

    """

    def __init__(self):
        """
        :param Alias: Image alias
Note: this field may return null, indicating that no valid values can be obtained.
        :type Alias: str
        :param OsName: Operating system name
Note: this field may return null, indicating that no valid values can be obtained.
        :type OsName: str
        :param ImageId: Image ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type ImageId: str
        :param OsCustomizeType: Container image tag, **DOCKER_CUSTOMIZE** (container customized tag), **GENERAL** (general tag, default value)
Note: this field may return null, indicating that no valid values can be obtained.
        :type OsCustomizeType: str
        """
        self.Alias = None
        self.OsName = None
        self.ImageId = None
        self.OsCustomizeType = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.OsName = params.get("OsName")
        self.ImageId = params.get("ImageId")
        self.OsCustomizeType = params.get("OsCustomizeType")


class Instance(AbstractModel):
    """Cluster's instance information

    """

    def __init__(self):
        """
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param InstanceRole: Node role: MASTER, WORKER, ETCD, MASTER_ETCD, and ALL. Default value: WORKER
        :type InstanceRole: str
        :param FailedReason: Reason for instance exception (or initialization)
        :type FailedReason: str
        :param InstanceState: Instance status (running, initializing, or failed)
        :type InstanceState: str
        :param DrainStatus: Whether the instance is drained
Note: this field may return null, indicating that no valid value is obtained.
        :type DrainStatus: str
        :param InstanceAdvancedSettings: Node settings
Note: this field may return null, indicating that no valid value is obtained.
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param CreatedTime: Creation time
        :type CreatedTime: str
        :param LanIP: Node private IP
Note: this field may return null, indicating that no valid values can be obtained.
        :type LanIP: str
        :param NodePoolId: Resource pool ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type NodePoolId: str
        :param AutoscalingGroupId: ID of the auto-scaling group
Note: this field may return null, indicating that no valid value is obtained.
        :type AutoscalingGroupId: str
        """
        self.InstanceId = None
        self.InstanceRole = None
        self.FailedReason = None
        self.InstanceState = None
        self.DrainStatus = None
        self.InstanceAdvancedSettings = None
        self.CreatedTime = None
        self.LanIP = None
        self.NodePoolId = None
        self.AutoscalingGroupId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceRole = params.get("InstanceRole")
        self.FailedReason = params.get("FailedReason")
        self.InstanceState = params.get("InstanceState")
        self.DrainStatus = params.get("DrainStatus")
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        self.CreatedTime = params.get("CreatedTime")
        self.LanIP = params.get("LanIP")
        self.NodePoolId = params.get("NodePoolId")
        self.AutoscalingGroupId = params.get("AutoscalingGroupId")


class InstanceAdvancedSettings(AbstractModel):
    """Describes K8s cluster configuration and related information.

    """

    def __init__(self):
        """
        :param MountTarget: Data disk mount point. By default, no data disk is mounted. Data disks in ext3, ext4, or XFS file system formats will be mounted directly, while data disks in other file systems and unformatted data disks will automatically be formatted as ext4 (xfs for tlinux system) and then mounted. Please back up your data in advance. This setting is only applicable to CVMs with a single data disk.
Note: in multi-disk scenarios, use the DataDisks data structure below to set the corresponding information, such as cloud disk type, cloud disk size, mount path, and whether to perform formatting.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type MountTarget: str
        :param DockerGraphPath: Specified value of dockerd --graph. Default value: /var/lib/docker
Note: This field may return null, indicating that no valid value was found.
        :type DockerGraphPath: str
        :param UserScript: Base64-encoded user script, which will be executed after the K8s component starts running. You need to ensure the reentrant and retry logic of the script. The script and its log files can be viewed at the node path: /data/ccs_userscript/. If you want to initialize nodes before adding them to the scheduling list, you can use this parameter together with the unschedulable parameter. After the final initialization of userScript is completed, add the kubectl uncordon nodename --kubeconfig=/root/.kube/config command to enable the node for scheduling.
Note: This field may return null, indicating that no valid value was found.
        :type UserScript: str
        :param Unschedulable: Sets whether the added node is schedulable. 0 (default): schedulable; other values: unschedulable. After node initialization is completed, you can run kubectl uncordon nodename to enable this node for scheduling.
        :type Unschedulable: int
        :param Labels: Node label array
Note: This field may return null, indicating that no valid value was found.
        :type Labels: list of Label
        :param DataDisks: Mounting information of multiple data disks. Ensure that the CVM purchase parameter specifies the information required for the purchase of multiple data disks, for example `DataDisks` under `RunInstancesPara` of the `CreateClusterInstances` API. You can refer to the example of adding a cluster node with multiple data disks in the CreateClusterInstances API. This parameter does not take effect when the AddExistedInstances API is called.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DataDisks: list of DataDisk
        :param ExtraArgs: Information about node custom parameters
Note: This field may return null, indicating that no valid value was found.
        :type ExtraArgs: :class:`tencentcloud.tke.v20180525.models.InstanceExtraArgs`
        """
        self.MountTarget = None
        self.DockerGraphPath = None
        self.UserScript = None
        self.Unschedulable = None
        self.Labels = None
        self.DataDisks = None
        self.ExtraArgs = None


    def _deserialize(self, params):
        self.MountTarget = params.get("MountTarget")
        self.DockerGraphPath = params.get("DockerGraphPath")
        self.UserScript = params.get("UserScript")
        self.Unschedulable = params.get("Unschedulable")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("ExtraArgs") is not None:
            self.ExtraArgs = InstanceExtraArgs()
            self.ExtraArgs._deserialize(params.get("ExtraArgs"))


class InstanceDataDiskMountSetting(AbstractModel):
    """Mounting configuration of the CVM instance data disk

    """

    def __init__(self):
        """
        :param InstanceType: CVM instance type
        :type InstanceType: str
        :param DataDisks: Data disk mounting information
        :type DataDisks: list of DataDisk
        :param Zone: Availability zone where the CVM instance is located
        :type Zone: str
        """
        self.InstanceType = None
        self.DataDisks = None
        self.Zone = None


    def _deserialize(self, params):
        self.InstanceType = params.get("InstanceType")
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        self.Zone = params.get("Zone")


class InstanceExtraArgs(AbstractModel):
    """Node custom parameter

    """

    def __init__(self):
        """
        :param Kubelet: Kubelet custom parameter, in the format of ["k1=v1", "k1=v2"], for example: ["root-dir=/var/lib/kubelet","feature-gates=PodShareProcessNamespace=true,DynamicKubeletConfig=true"].
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Kubelet: list of str
        """
        self.Kubelet = None


    def _deserialize(self, params):
        self.Kubelet = params.get("Kubelet")


class InstanceUpgradeClusterStatus(AbstractModel):
    """Current status of the cluster during node upgrade

    """

    def __init__(self):
        """
        :param PodTotal: Total Pods
        :type PodTotal: int
        :param NotReadyPod: Total number of NotReady Pods
        :type NotReadyPod: int
        """
        self.PodTotal = None
        self.NotReadyPod = None


    def _deserialize(self, params):
        self.PodTotal = params.get("PodTotal")
        self.NotReadyPod = params.get("NotReadyPod")


class InstanceUpgradePreCheckResult(AbstractModel):
    """Pre-upgrade check result of a node

    """

    def __init__(self):
        """
        :param CheckPass: Whether the check is passed
        :type CheckPass: bool
        :param Items: Array of check items
        :type Items: list of InstanceUpgradePreCheckResultItem
        :param SinglePods: List of independent pods on this node
        :type SinglePods: list of str
        """
        self.CheckPass = None
        self.Items = None
        self.SinglePods = None


    def _deserialize(self, params):
        self.CheckPass = params.get("CheckPass")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = InstanceUpgradePreCheckResultItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.SinglePods = params.get("SinglePods")


class InstanceUpgradePreCheckResultItem(AbstractModel):
    """Check result for node upgrade

    """

    def __init__(self):
        """
        :param Namespace: The namespace of the workload
        :type Namespace: str
        :param WorkLoadKind: Workload type
        :type WorkLoadKind: str
        :param WorkLoadName: Workload name
        :type WorkLoadName: str
        :param Before: The number of running pods in the workload before draining the node
        :type Before: int
        :param After: The number of running pods in the workload after draining the node
        :type After: int
        :param Pods: The pod list of the workload on this node
        :type Pods: list of str
        """
        self.Namespace = None
        self.WorkLoadKind = None
        self.WorkLoadName = None
        self.Before = None
        self.After = None
        self.Pods = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.WorkLoadKind = params.get("WorkLoadKind")
        self.WorkLoadName = params.get("WorkLoadName")
        self.Before = params.get("Before")
        self.After = params.get("After")
        self.Pods = params.get("Pods")


class InstanceUpgradeProgressItem(AbstractModel):
    """Upgrade progress of a node

    """

    def __init__(self):
        """
        :param InstanceID: Node instance ID
        :type InstanceID: str
        :param LifeState: Task lifecycle
process: running
paused: stopped
pausing: stopping
done: completed
timeout: timed out
aborted: canceled
pending: not started
        :type LifeState: str
        :param StartAt: Upgrade start time
Note: this field may return `null`, indicating that no valid value is obtained.
        :type StartAt: str
        :param EndAt: Upgrade end time
Note: this field may return `null`, indicating that no valid value is obtained.
        :type EndAt: str
        :param CheckResult: Check result before upgrading
        :type CheckResult: :class:`tencentcloud.tke.v20180525.models.InstanceUpgradePreCheckResult`
        :param Detail: Upgrade steps details
        :type Detail: list of TaskStepInfo
        """
        self.InstanceID = None
        self.LifeState = None
        self.StartAt = None
        self.EndAt = None
        self.CheckResult = None
        self.Detail = None


    def _deserialize(self, params):
        self.InstanceID = params.get("InstanceID")
        self.LifeState = params.get("LifeState")
        self.StartAt = params.get("StartAt")
        self.EndAt = params.get("EndAt")
        if params.get("CheckResult") is not None:
            self.CheckResult = InstanceUpgradePreCheckResult()
            self.CheckResult._deserialize(params.get("CheckResult"))
        if params.get("Detail") is not None:
            self.Detail = []
            for item in params.get("Detail"):
                obj = TaskStepInfo()
                obj._deserialize(item)
                self.Detail.append(obj)


class Label(AbstractModel):
    """k8s tags, generally exist as an array

    """

    def __init__(self):
        """
        :param Name: Name in map list
        :type Name: str
        :param Value: Value in map list
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class LoginSettings(AbstractModel):
    """Describes login settings of an instance.

    """

    def __init__(self):
        """
        :param Password: Login password of the instance. The password requirements vary among different operating systems: <br><li>For Linux instances, the password must be 8-30 characters long and contain at least two of the following types: [a-z], [A-Z], [0-9] and [( ) \` ~ ! @ # $ % ^ & *  - + = | { } [ ] : ; ' , . ? / ]. <br><li>For Windows instances, the password must be 12-30 characters long and contain at least three of the following categories: [a-z], [A-Z], [0-9] and [( ) \` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? /]. <br><br>If this parameter is not specified, a random password will be generated and sent to you via the Message Center.
Note: this field may return null, indicating that no valid value is obtained.
        :type Password: str
        :param KeyIds: List of key IDs. After an instance is associated with a key, you can access the instance with the private key in the key pair. You can call [`DescribeKeyPairs`](https://intl.cloud.tencent.com/document/api/213/15699?from_cn_redirect=1) to obtain `KeyId`. A key and password cannot be specified at the same time. Windows instances do not support keys. Currently, you can only specify one key when purchasing an instance.
Note: this field may return null, indicating that no valid value is obtained.
        :type KeyIds: list of str
        :param KeepImageLogin: Whether to keep the original settings of an image. You cannot specify this parameter and `Password` or `KeyIds.N` at the same time. You can specify this parameter as `TRUE` only when you create an instance using a custom image, a shared image, or an imported image. Valid values: <br><li>TRUE: keep the login settings of the image <br><li>FALSE: do not keep the login settings of the image <br><br>Default value: FALSE.
Note: This field may return null, indicating that no valid value is found.
        :type KeepImageLogin: str
        """
        self.Password = None
        self.KeyIds = None
        self.KeepImageLogin = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        self.KeyIds = params.get("KeyIds")
        self.KeepImageLogin = params.get("KeepImageLogin")


class ManuallyAdded(AbstractModel):
    """Nodes that are manually added

    """

    def __init__(self):
        """
        :param Joining: Number of nodes that are being added
        :type Joining: int
        :param Initializing: Number of nodes that are being initialized
        :type Initializing: int
        :param Normal: Number of normal nodes
        :type Normal: int
        :param Total: Total number of nodes
        :type Total: int
        """
        self.Joining = None
        self.Initializing = None
        self.Normal = None
        self.Total = None


    def _deserialize(self, params):
        self.Joining = params.get("Joining")
        self.Initializing = params.get("Initializing")
        self.Normal = params.get("Normal")
        self.Total = params.get("Total")


class ModifyClusterAsGroupAttributeRequest(AbstractModel):
    """ModifyClusterAsGroupAttribute request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param ClusterAsGroupAttribute: Cluster-associated scaling group attributes
        :type ClusterAsGroupAttribute: :class:`tencentcloud.tke.v20180525.models.ClusterAsGroupAttribute`
        """
        self.ClusterId = None
        self.ClusterAsGroupAttribute = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("ClusterAsGroupAttribute") is not None:
            self.ClusterAsGroupAttribute = ClusterAsGroupAttribute()
            self.ClusterAsGroupAttribute._deserialize(params.get("ClusterAsGroupAttribute"))


class ModifyClusterAsGroupAttributeResponse(AbstractModel):
    """ModifyClusterAsGroupAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterAsGroupOptionAttributeRequest(AbstractModel):
    """ModifyClusterAsGroupOptionAttribute request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param ClusterAsGroupOption: Cluster auto scaling attributes
        :type ClusterAsGroupOption: :class:`tencentcloud.tke.v20180525.models.ClusterAsGroupOption`
        """
        self.ClusterId = None
        self.ClusterAsGroupOption = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("ClusterAsGroupOption") is not None:
            self.ClusterAsGroupOption = ClusterAsGroupOption()
            self.ClusterAsGroupOption._deserialize(params.get("ClusterAsGroupOption"))


class ModifyClusterAsGroupOptionAttributeResponse(AbstractModel):
    """ModifyClusterAsGroupOptionAttribute response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterAttributeRequest(AbstractModel):
    """ModifyClusterAttribute request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param ProjectId: Project of the Cluster
        :type ProjectId: int
        :param ClusterName: Cluster name
        :type ClusterName: str
        :param ClusterDesc: Cluster description
        :type ClusterDesc: str
        """
        self.ClusterId = None
        self.ProjectId = None
        self.ClusterName = None
        self.ClusterDesc = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ProjectId = params.get("ProjectId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterDesc = params.get("ClusterDesc")


class ModifyClusterAttributeResponse(AbstractModel):
    """ModifyClusterAttribute response structure.

    """

    def __init__(self):
        """
        :param ProjectId: Project of the Cluster
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectId: int
        :param ClusterName: Cluster name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterName: str
        :param ClusterDesc: Cluster description
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterDesc: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ProjectId = None
        self.ClusterName = None
        self.ClusterDesc = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterDesc = params.get("ClusterDesc")
        self.RequestId = params.get("RequestId")


class ModifyClusterEndpointSPRequest(AbstractModel):
    """ModifyClusterEndpointSP request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param SecurityPolicies: Security policy opens single IP or CIDR block to the Internet (for example: '192.168.1.0/24', with 'reject all' as the default).
        :type SecurityPolicies: list of str
        """
        self.ClusterId = None
        self.SecurityPolicies = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SecurityPolicies = params.get("SecurityPolicies")


class ModifyClusterEndpointSPResponse(AbstractModel):
    """ModifyClusterEndpointSP response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterNodePoolRequest(AbstractModel):
    """ModifyClusterNodePool request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param NodePoolId: Node pool ID
        :type NodePoolId: str
        :param Name: Name
        :type Name: str
        :param MaxNodesNum: Maximum number of nodes
        :type MaxNodesNum: int
        :param MinNodesNum: Minimum number of nodes
        :type MinNodesNum: int
        :param Labels: Labels
        :type Labels: list of Label
        :param Taints: Taints
        :type Taints: list of Taint
        :param EnableAutoscale: Indicates whether auto scaling is enabled.
        :type EnableAutoscale: bool
        :param OsName: Operating system name
        :type OsName: str
        :param OsCustomizeType: Image tag, `DOCKER_CUSTOMIZE` (container customized tag), `GENERAL` (general tag, default value)
        :type OsCustomizeType: str
        """
        self.ClusterId = None
        self.NodePoolId = None
        self.Name = None
        self.MaxNodesNum = None
        self.MinNodesNum = None
        self.Labels = None
        self.Taints = None
        self.EnableAutoscale = None
        self.OsName = None
        self.OsCustomizeType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NodePoolId = params.get("NodePoolId")
        self.Name = params.get("Name")
        self.MaxNodesNum = params.get("MaxNodesNum")
        self.MinNodesNum = params.get("MinNodesNum")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("Taints") is not None:
            self.Taints = []
            for item in params.get("Taints"):
                obj = Taint()
                obj._deserialize(item)
                self.Taints.append(obj)
        self.EnableAutoscale = params.get("EnableAutoscale")
        self.OsName = params.get("OsName")
        self.OsCustomizeType = params.get("OsCustomizeType")


class ModifyClusterNodePoolResponse(AbstractModel):
    """ModifyClusterNodePool response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NodeCountSummary(AbstractModel):
    """Node statistics list

    """

    def __init__(self):
        """
        :param ManuallyAdded: Nodes that are manually managed
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ManuallyAdded: :class:`tencentcloud.tke.v20180525.models.ManuallyAdded`
        :param AutoscalingAdded: Nodes that are automatically managed
Note: this field may return `null`, indicating that no valid value is obtained.
        :type AutoscalingAdded: :class:`tencentcloud.tke.v20180525.models.AutoscalingAdded`
        """
        self.ManuallyAdded = None
        self.AutoscalingAdded = None


    def _deserialize(self, params):
        if params.get("ManuallyAdded") is not None:
            self.ManuallyAdded = ManuallyAdded()
            self.ManuallyAdded._deserialize(params.get("ManuallyAdded"))
        if params.get("AutoscalingAdded") is not None:
            self.AutoscalingAdded = AutoscalingAdded()
            self.AutoscalingAdded._deserialize(params.get("AutoscalingAdded"))


class NodePool(AbstractModel):
    """Node pool description

    """

    def __init__(self):
        """
        :param NodePoolId: Node pool ID
        :type NodePoolId: str
        :param Name: Node pool name
        :type Name: str
        :param ClusterInstanceId: Cluster instance ID
        :type ClusterInstanceId: str
        :param LifeState: The lifecycle state of the current node pool. Valid values: `creating`, `normal`, `updating`, `deleting`, and `deleted`.
        :type LifeState: str
        :param LaunchConfigurationId: Launch configuration ID
        :type LaunchConfigurationId: str
        :param AutoscalingGroupId: Auto-scaling group ID
        :type AutoscalingGroupId: str
        :param Labels: Labels
        :type Labels: list of Label
        :param Taints: Array of taint
        :type Taints: list of Taint
        :param NodeCountSummary: Node list
        :type NodeCountSummary: :class:`tencentcloud.tke.v20180525.models.NodeCountSummary`
        :param AutoscalingGroupStatus: 
        :type AutoscalingGroupStatus: str
        :param MaxNodesNum: Maximum number of nodes
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MaxNodesNum: int
        :param MinNodesNum: Minimum number of nodes
Note: this field may return `null`, indicating that no valid value is obtained.
        :type MinNodesNum: int
        :param DesiredNodesNum: Desired number of nodes
Note: this field may return `null`, indicating that no valid value is obtained.
        :type DesiredNodesNum: int
        :param NodePoolOs: The operating system of the node pool
Note: this field may return `null`, indicating that no valid value is obtained.
        :type NodePoolOs: str
        :param OsCustomizeType: Container image tag, `DOCKER_CUSTOMIZE` (container customized tag), `GENERAL` (general tag, default value)
Note: this field may return `null`, indicating that no valid value is obtained.
        :type OsCustomizeType: str
        :param ImageId: Image ID
Note: this field may return `null`, indicating that no valid value is obtained.
        :type ImageId: str
        :param DesiredPodNum: This parameter is required when the custom PodCIDR mode is enabled for the cluster.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type DesiredPodNum: int
        :param UserScript: Custom script
Note: this field may return `null`, indicating that no valid value is obtained.
        :type UserScript: str
        """
        self.NodePoolId = None
        self.Name = None
        self.ClusterInstanceId = None
        self.LifeState = None
        self.LaunchConfigurationId = None
        self.AutoscalingGroupId = None
        self.Labels = None
        self.Taints = None
        self.NodeCountSummary = None
        self.AutoscalingGroupStatus = None
        self.MaxNodesNum = None
        self.MinNodesNum = None
        self.DesiredNodesNum = None
        self.NodePoolOs = None
        self.OsCustomizeType = None
        self.ImageId = None
        self.DesiredPodNum = None
        self.UserScript = None


    def _deserialize(self, params):
        self.NodePoolId = params.get("NodePoolId")
        self.Name = params.get("Name")
        self.ClusterInstanceId = params.get("ClusterInstanceId")
        self.LifeState = params.get("LifeState")
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.AutoscalingGroupId = params.get("AutoscalingGroupId")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("Taints") is not None:
            self.Taints = []
            for item in params.get("Taints"):
                obj = Taint()
                obj._deserialize(item)
                self.Taints.append(obj)
        if params.get("NodeCountSummary") is not None:
            self.NodeCountSummary = NodeCountSummary()
            self.NodeCountSummary._deserialize(params.get("NodeCountSummary"))
        self.AutoscalingGroupStatus = params.get("AutoscalingGroupStatus")
        self.MaxNodesNum = params.get("MaxNodesNum")
        self.MinNodesNum = params.get("MinNodesNum")
        self.DesiredNodesNum = params.get("DesiredNodesNum")
        self.NodePoolOs = params.get("NodePoolOs")
        self.OsCustomizeType = params.get("OsCustomizeType")
        self.ImageId = params.get("ImageId")
        self.DesiredPodNum = params.get("DesiredPodNum")
        self.UserScript = params.get("UserScript")


class NodePoolOption(AbstractModel):
    """The options for adding the existing node to the node pool

    """

    def __init__(self):
        """
        :param AddToNodePool: Whether to add to the node pool.
        :type AddToNodePool: bool
        :param NodePoolId: Node pool ID
        :type NodePoolId: str
        :param InheritConfigurationFromNodePool: Whether to inherit the node pool configuration.
        :type InheritConfigurationFromNodePool: bool
        """
        self.AddToNodePool = None
        self.NodePoolId = None
        self.InheritConfigurationFromNodePool = None


    def _deserialize(self, params):
        self.AddToNodePool = params.get("AddToNodePool")
        self.NodePoolId = params.get("NodePoolId")
        self.InheritConfigurationFromNodePool = params.get("InheritConfigurationFromNodePool")


class RegionInstance(AbstractModel):
    """Region information

    """

    def __init__(self):
        """
        :param RegionName: Region name
Note: this field may return null, indicating that no valid values can be obtained.
        :type RegionName: str
        :param RegionId: Region ID
Note: this field may return null, indicating that no valid values can be obtained.
        :type RegionId: int
        :param Status: Region status
Note: this field may return null, indicating that no valid values can be obtained.
        :type Status: str
        :param FeatureGates: Status of region-related features (return all attributes in JSON format)
Note: this field may return null, indicating that no valid values can be obtained.
        :type FeatureGates: str
        :param Alias: Region abbreviation
Note: this field may return null, indicating that no valid values can be obtained.
        :type Alias: str
        :param Remark: Whitelisted location
Note: this field may return null, indicating that no valid values can be obtained.
        :type Remark: str
        """
        self.RegionName = None
        self.RegionId = None
        self.Status = None
        self.FeatureGates = None
        self.Alias = None
        self.Remark = None


    def _deserialize(self, params):
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        self.Status = params.get("Status")
        self.FeatureGates = params.get("FeatureGates")
        self.Alias = params.get("Alias")
        self.Remark = params.get("Remark")


class RemoveNodeFromNodePoolRequest(AbstractModel):
    """RemoveNodeFromNodePool request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param NodePoolId: Node pool ID
        :type NodePoolId: str
        :param InstanceIds: Node ID list
        :type InstanceIds: list of str
        """
        self.ClusterId = None
        self.NodePoolId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NodePoolId = params.get("NodePoolId")
        self.InstanceIds = params.get("InstanceIds")


class RemoveNodeFromNodePoolResponse(AbstractModel):
    """RemoveNodeFromNodePool response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResourceDeleteOption(AbstractModel):
    """The policy to deal with resources in the cluster when the cluster is deleted.

    """

    def __init__(self):
        """
        :param ResourceType: Resource type, for example `CBS`
        :type ResourceType: str
        :param DeleteMode: Specifies the policy to deal with resources in the cluster when the cluster is deleted. It can be `terminate` or `retain`.
        :type DeleteMode: str
        """
        self.ResourceType = None
        self.DeleteMode = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.DeleteMode = params.get("DeleteMode")


class RouteInfo(AbstractModel):
    """Object of cluster route

    """

    def __init__(self):
        """
        :param RouteTableName: Route table name.
        :type RouteTableName: str
        :param DestinationCidrBlock: Destination CIDR.
        :type DestinationCidrBlock: str
        :param GatewayIp: Next hop address.
        :type GatewayIp: str
        """
        self.RouteTableName = None
        self.DestinationCidrBlock = None
        self.GatewayIp = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.GatewayIp = params.get("GatewayIp")


class RouteTableConflict(AbstractModel):
    """Object of route table conflict

    """

    def __init__(self):
        """
        :param RouteTableType: Route table type.
        :type RouteTableType: str
        :param RouteTableCidrBlock: Route table CIDR.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RouteTableCidrBlock: str
        :param RouteTableName: Route table name.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RouteTableName: str
        :param RouteTableId: Route table ID.
Note: This field may return null, indicating that no valid values can be obtained.
        :type RouteTableId: str
        """
        self.RouteTableType = None
        self.RouteTableCidrBlock = None
        self.RouteTableName = None
        self.RouteTableId = None


    def _deserialize(self, params):
        self.RouteTableType = params.get("RouteTableType")
        self.RouteTableCidrBlock = params.get("RouteTableCidrBlock")
        self.RouteTableName = params.get("RouteTableName")
        self.RouteTableId = params.get("RouteTableId")


class RouteTableInfo(AbstractModel):
    """Object of cluster route table

    """

    def __init__(self):
        """
        :param RouteTableName: Route table name.
        :type RouteTableName: str
        :param RouteTableCidrBlock: Route table CIDR.
        :type RouteTableCidrBlock: str
        :param VpcId: VPC instance ID.
        :type VpcId: str
        """
        self.RouteTableName = None
        self.RouteTableCidrBlock = None
        self.VpcId = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")
        self.RouteTableCidrBlock = params.get("RouteTableCidrBlock")
        self.VpcId = params.get("VpcId")


class RunInstancesForNode(AbstractModel):
    """Node configuration parameters of different roles

    """

    def __init__(self):
        """
        :param NodeRole: Node role. Values: MASTER_ETCD, WORKER. You only need to specify MASTER_ETCD when creating a self-deployed cluster (INDEPENDENT_CLUSTER).
        :type NodeRole: str
        :param RunInstancesPara: Pass-through parameter for CVM creation in the format of a JSON string. For more information, see the API for [creating a CVM instance](https://intl.cloud.tencent.com/document/product/213/15730?from_cn_redirect=1). Pass any parameter other than common parameters. ImageId will be replaced with the image corresponding to the TKE cluster operating system.
        :type RunInstancesPara: list of str
        :param InstanceAdvancedSettingsOverrides: An advanced node setting. This parameter overrides the InstanceAdvancedSettings item set at the cluster level and corresponds to RunInstancesPara in a one-to-one sequential manner (currently valid for the ExtraArgs node custom parameter only).
        :type InstanceAdvancedSettingsOverrides: list of InstanceAdvancedSettings
        """
        self.NodeRole = None
        self.RunInstancesPara = None
        self.InstanceAdvancedSettingsOverrides = None


    def _deserialize(self, params):
        self.NodeRole = params.get("NodeRole")
        self.RunInstancesPara = params.get("RunInstancesPara")
        if params.get("InstanceAdvancedSettingsOverrides") is not None:
            self.InstanceAdvancedSettingsOverrides = []
            for item in params.get("InstanceAdvancedSettingsOverrides"):
                obj = InstanceAdvancedSettings()
                obj._deserialize(item)
                self.InstanceAdvancedSettingsOverrides.append(obj)


class RunMonitorServiceEnabled(AbstractModel):
    """Describes information related to the Cloud Monitor service.

    """

    def __init__(self):
        """
        :param Enabled: Whether to enable [Cloud Monitor](https://intl.cloud.tencent.com/document/product/248?from_cn_redirect=1). Valid values: <br><li>TRUE: enable Cloud Monitor <br><li>FALSE: do not enable Cloud Monitor <br><br>Default value: TRUE.
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")


class RunSecurityServiceEnabled(AbstractModel):
    """Describes information related to the Cloud Security service.

    """

    def __init__(self):
        """
        :param Enabled: Whether to enable [Cloud Security](https://intl.cloud.tencent.com/document/product/296?from_cn_redirect=1). Valid values: <br><li>TRUE: enable Cloud Security <br><li>FALSE: do not enable Cloud Security <br><br>Default value: TRUE.
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")


class SetNodePoolNodeProtectionRequest(AbstractModel):
    """SetNodePoolNodeProtection request structure.

    """


class SetNodePoolNodeProtectionResponse(AbstractModel):
    """SetNodePoolNodeProtection response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """The type of resource the label is bound to. Type currently supported is **cluster**.

    """

    def __init__(self):
        """
        :param Key: Tag key.
        :type Key: str
        :param Value: Tag value.
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")


class TagSpecification(AbstractModel):
    """List of tag descriptions. By specifying this parameter, you can bind tags to corresponding resource instances at the same time. Currently, only tags are bound to cloud host instances.

    """

    def __init__(self):
        """
        :param ResourceType: The type of resource that the tag is bound to. The type currently supported is `cluster`.
        :type ResourceType: str
        :param Tags: List of tag pairs
        :type Tags: list of Tag
        """
        self.ResourceType = None
        self.Tags = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class Taint(AbstractModel):
    """Kubernetes Taint

    """

    def __init__(self):
        """
        :param Key: Key of the taint
        :type Key: str
        :param Value: Value of the taint
        :type Value: str
        :param Effect: Effect of the taint
        :type Effect: str
        """
        self.Key = None
        self.Value = None
        self.Effect = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        self.Effect = params.get("Effect")


class TaskStepInfo(AbstractModel):
    """Task step information

    """

    def __init__(self):
        """
        :param Step: Step name
        :type Step: str
        :param LifeState: Lifecycle
pending: the step is not started
running: the step is in progress
success: the step is completed
failed: the step failed
        :type LifeState: str
        :param StartAt: Step start time
Note: this field may return `null`, indicating that no valid value is obtained.
        :type StartAt: str
        :param EndAt: Step end time
Note: this field may return `null`, indicating that no valid value is obtained.
        :type EndAt: str
        :param FailedMsg: If the lifecycle of the step is failed, this field will display the error information.
Note: this field may return `null`, indicating that no valid value is obtained.
        :type FailedMsg: str
        """
        self.Step = None
        self.LifeState = None
        self.StartAt = None
        self.EndAt = None
        self.FailedMsg = None


    def _deserialize(self, params):
        self.Step = params.get("Step")
        self.LifeState = params.get("LifeState")
        self.StartAt = params.get("StartAt")
        self.EndAt = params.get("EndAt")
        self.FailedMsg = params.get("FailedMsg")


class UpdateClusterVersionRequest(AbstractModel):
    """UpdateClusterVersion request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param DstVersion: The version that needs to upgrade to
        :type DstVersion: str
        :param ExtraArgs: Cluster custom parameter
        :type ExtraArgs: :class:`tencentcloud.tke.v20180525.models.ClusterExtraArgs`
        :param MaxNotReadyPercent: The maximum tolerable number of unavailable pods
        :type MaxNotReadyPercent: float
        :param SkipPreCheck: Whether to skip the precheck
        :type SkipPreCheck: bool
        """
        self.ClusterId = None
        self.DstVersion = None
        self.ExtraArgs = None
        self.MaxNotReadyPercent = None
        self.SkipPreCheck = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.DstVersion = params.get("DstVersion")
        if params.get("ExtraArgs") is not None:
            self.ExtraArgs = ClusterExtraArgs()
            self.ExtraArgs._deserialize(params.get("ExtraArgs"))
        self.MaxNotReadyPercent = params.get("MaxNotReadyPercent")
        self.SkipPreCheck = params.get("SkipPreCheck")


class UpdateClusterVersionResponse(AbstractModel):
    """UpdateClusterVersion response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeAbleInstancesItem(AbstractModel):
    """Upgradeable node information

    """

    def __init__(self):
        """
        :param InstanceId: Node ID
        :type InstanceId: str
        :param Version: The current version of the node
        :type Version: str
        :param LatestVersion: The latest minor version of the current version
Note: this field may return `null`, indicating that no valid value is obtained.
        :type LatestVersion: str
        """
        self.InstanceId = None
        self.Version = None
        self.LatestVersion = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Version = params.get("Version")
        self.LatestVersion = params.get("LatestVersion")


class UpgradeClusterInstancesRequest(AbstractModel):
    """UpgradeClusterInstances request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param Operation: create: starting an upgrade task
pause: pausing the task
resume: continuing the task
abort: stopping the task
        :type Operation: str
        :param UpgradeType: Upgrade type. It’s only required when `Operation` is set as `create`.
reset: the reinstallation and upgrade of major version
hot: the hot upgrade of minor version
major: in-place upgrade of major version
        :type UpgradeType: str
        :param InstanceIds: List of nodes that need to upgrade
        :type InstanceIds: list of str
        :param ResetParam: This parameter is used when the node joins the cluster again. Refer to the API of creating one or more cluster nodes.
        :type ResetParam: :class:`tencentcloud.tke.v20180525.models.UpgradeNodeResetParam`
        :param SkipPreCheck: Whether to skip the pre-upgrade check of the node
        :type SkipPreCheck: bool
        :param MaxNotReadyPercent: The maximum tolerable proportion of unavailable pods
        :type MaxNotReadyPercent: float
        """
        self.ClusterId = None
        self.Operation = None
        self.UpgradeType = None
        self.InstanceIds = None
        self.ResetParam = None
        self.SkipPreCheck = None
        self.MaxNotReadyPercent = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Operation = params.get("Operation")
        self.UpgradeType = params.get("UpgradeType")
        self.InstanceIds = params.get("InstanceIds")
        if params.get("ResetParam") is not None:
            self.ResetParam = UpgradeNodeResetParam()
            self.ResetParam._deserialize(params.get("ResetParam"))
        self.SkipPreCheck = params.get("SkipPreCheck")
        self.MaxNotReadyPercent = params.get("MaxNotReadyPercent")


class UpgradeClusterInstancesResponse(AbstractModel):
    """UpgradeClusterInstances response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeNodeResetParam(AbstractModel):
    """Node upgrade and reinstallation parameters

    """

    def __init__(self):
        """
        :param InstanceAdvancedSettings: Additional parameters set for the instance
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param EnhancedService: Enhanced services. You can use this parameter to specify whether to enable services such as Cloud Security and Cloud Monitor. If this parameter is not specified, Cloud Monitor and Cloud Security will be enabled by default.
        :type EnhancedService: :class:`tencentcloud.tke.v20180525.models.EnhancedService`
        :param LoginSettings: Node login information. For now, it only supports Password or a single KeyIds
        :type LoginSettings: :class:`tencentcloud.tke.v20180525.models.LoginSettings`
        :param SecurityGroupIds: Security group to which the instance belongs. This parameter can be obtained from the `sgId` field in the response of `DescribeSecurityGroups`. If this parameter is not specified, the default security group is bound. (Currently, you can only set a single sgId.)
        :type SecurityGroupIds: list of str
        """
        self.InstanceAdvancedSettings = None
        self.EnhancedService = None
        self.LoginSettings = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")