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


class AcquireClusterAdminRoleRequest(AbstractModel):
    """AcquireClusterAdminRole request structure.

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
        


class AcquireClusterAdminRoleResponse(AbstractModel):
    """AcquireClusterAdminRole response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        :param InstanceAdvancedSettingsOverrides: This parameter is used to customize the configuration of an instance, which corresponds to the `InstanceIds` one-to-one in sequence. If this parameter is passed in, the default parameter `InstanceAdvancedSettings` will be overwritten and will not take effect. If this parameter is not passed in, the `InstanceAdvancedSettings` will take effect for each instance.

The array length of `InstanceAdvancedSettingsOverride` should be the same as the array length of `InstanceIds`. If its array length is greater than the `InstanceIds` array length, an error will be reported. If its array length is less than the `InstanceIds` array length, the instance without corresponding configuration will use the default configuration.
        :type InstanceAdvancedSettingsOverrides: list of InstanceAdvancedSettings
        :param ImageId: Node image (it is required when creating a node)
        :type ImageId: str
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
        self.InstanceAdvancedSettingsOverrides = None
        self.ImageId = None


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
        if params.get("InstanceAdvancedSettingsOverrides") is not None:
            self.InstanceAdvancedSettingsOverrides = []
            for item in params.get("InstanceAdvancedSettingsOverrides"):
                obj = InstanceAdvancedSettings()
                obj._deserialize(item)
                self.InstanceAdvancedSettingsOverrides.append(obj)
        self.ImageId = params.get("ImageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddExistedInstancesResponse(AbstractModel):
    """AddExistedInstances response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddNodeToNodePoolResponse(AbstractModel):
    """AddNodeToNodePool response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddVpcCniSubnetsRequest(AbstractModel):
    """AddVpcCniSubnets request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param SubnetIds: The subnets added for the cluster container network
        :type SubnetIds: list of str
        :param VpcId: ID of the VPC where the cluster resides
        :type VpcId: str
        """
        self.ClusterId = None
        self.SubnetIds = None
        self.VpcId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SubnetIds = params.get("SubnetIds")
        self.VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddVpcCniSubnetsResponse(AbstractModel):
    """AddVpcCniSubnets response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoUpgradeClusterLevel(AbstractModel):
    """Auto-upgrades cluster specification

    """

    def __init__(self):
        r"""
        :param IsAutoUpgrade: Whether to enable Auto Cluster Upgrade
        :type IsAutoUpgrade: bool
        """
        self.IsAutoUpgrade = None


    def _deserialize(self, params):
        self.IsAutoUpgrade = params.get("IsAutoUpgrade")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoscalingAdded(AbstractModel):
    """Nodes that are added in scale-out

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CUDNN(AbstractModel):
    """cuDNN version information

    """

    def __init__(self):
        r"""
        :param Version: cuDNN version
        :type Version: str
        :param Name: cuDNN name
        :type Name: str
        :param DocName: Doc name of cuDNN
        :type DocName: str
        :param DevName: Dev name of cuDNN
        :type DevName: str
        """
        self.Version = None
        self.Name = None
        self.DocName = None
        self.DevName = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.Name = params.get("Name")
        self.DocName = params.get("DocName")
        self.DevName = params.get("DevName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckEdgeClusterCIDRRequest(AbstractModel):
    """CheckEdgeClusterCIDR request structure.

    """

    def __init__(self):
        r"""
        :param VpcId: Cluster VPC ID
        :type VpcId: str
        :param PodCIDR: Cluster Pod CIDR block
        :type PodCIDR: str
        :param ServiceCIDR: Cluster service CIDR block
        :type ServiceCIDR: str
        """
        self.VpcId = None
        self.PodCIDR = None
        self.ServiceCIDR = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.PodCIDR = params.get("PodCIDR")
        self.ServiceCIDR = params.get("ServiceCIDR")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckEdgeClusterCIDRResponse(AbstractModel):
    """CheckEdgeClusterCIDR response structure.

    """

    def __init__(self):
        r"""
        :param ConflictCode: Return code. Valid values:
-1: Internal error
0: No conflict
1: Conflict between VPC and serviceCIDR
2: Conflict between VPC and podCIDR
3: Conflict between serviceCIDR and podCIDR
        :type ConflictCode: int
        :param ConflictMsg: CIDR block conflict description
        :type ConflictMsg: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ConflictCode = None
        self.ConflictMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ConflictCode = params.get("ConflictCode")
        self.ConflictMsg = params.get("ConflictMsg")
        self.RequestId = params.get("RequestId")


class CheckInstancesUpgradeAbleRequest(AbstractModel):
    """CheckInstancesUpgradeAble request structure.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckInstancesUpgradeAbleResponse(AbstractModel):
    """CheckInstancesUpgradeAble response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        :param ClusterStatus: Cluster status (`Running`, `Creating`, `Idling` or `Abnormal`)
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
        :param EnableExternalNode: Specifies whether the cluster supports external nodes.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type EnableExternalNode: bool
        :param ClusterLevel: Cluster models. It’s valid for managed clusters.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterLevel: str
        :param AutoUpgradeClusterLevel: The target cluster model for auto-upgrade
Note: this field may return null, indicating that no valid value is obtained.
        :type AutoUpgradeClusterLevel: bool
        :param QGPUShareEnable: Whether to enable qGPU Sharing
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type QGPUShareEnable: bool
        :param RuntimeVersion: Runtime version
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type RuntimeVersion: str
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
        self.EnableExternalNode = None
        self.ClusterLevel = None
        self.AutoUpgradeClusterLevel = None
        self.QGPUShareEnable = None
        self.RuntimeVersion = None


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
        self.EnableExternalNode = params.get("EnableExternalNode")
        self.ClusterLevel = params.get("ClusterLevel")
        self.AutoUpgradeClusterLevel = params.get("AutoUpgradeClusterLevel")
        self.QGPUShareEnable = params.get("QGPUShareEnable")
        self.RuntimeVersion = params.get("RuntimeVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterAdvancedSettings(AbstractModel):
    """Cluster advanced configurations

    """

    def __init__(self):
        r"""
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
        :param VpcCniType: Specifies the ENI type. Values: `tke-route-eni` (multi-IP shared ENI); `tke-direct-eni` (independent ENI). It defaults to `tke-route-eni`.
        :type VpcCniType: str
        :param RuntimeVersion: Runtime version
        :type RuntimeVersion: str
        :param EnableCustomizedPodCIDR: Indicates whether to enable the custom mode for the node’s pod CIDR range
        :type EnableCustomizedPodCIDR: bool
        :param BasePodNumber: The basic number of Pods in custom mode
        :type BasePodNumber: int
        :param CiliumMode: Specifies whether to enable Cilium. If it’s left empty, Cilium is not enabled. If `clusterIP` is passed in, it means to enable Cilium to support the clusterIP service type.
        :type CiliumMode: str
        :param IsDualStack: Whether it is a dual-stack cluster in VPC-CNI mode. Default value: `false`, which indicates it is not a dual-stack cluster.
        :type IsDualStack: bool
        :param QGPUShareEnable: Whether to enable qGPU Sharing
        :type QGPUShareEnable: bool
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
        self.CiliumMode = None
        self.IsDualStack = None
        self.QGPUShareEnable = None


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
        self.CiliumMode = params.get("CiliumMode")
        self.IsDualStack = params.get("IsDualStack")
        self.QGPUShareEnable = params.get("QGPUShareEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterAsGroup(AbstractModel):
    """Cluster-associated scaling group information

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterAsGroupAttribute(AbstractModel):
    """Cluster scaling group attributes

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterAsGroupOption(AbstractModel):
    """Cluster auto scaling configuration

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterBasicSettings(AbstractModel):
    """Describes the basic configuration information of a cluster

    """

    def __init__(self):
        r"""
        :param ClusterOs: Cluster operating system. Public image (enter the image ID) and custom image (enter the image name) are supported. For details, see https://intl.cloud.tencent.com/document/product/457/68289?from_cn_redirect=1
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
        :param NeedWorkSecurityGroup: Whether to enable the node’s default security group (default: `No`, Alpha feature)
        :type NeedWorkSecurityGroup: bool
        :param SubnetId: When the Cilium Overlay add-on is selected, TKE will take two IPs from the subnet to create the private network CLB.
        :type SubnetId: str
        :param ClusterLevel: Cluster specifications available for managed clusters
        :type ClusterLevel: str
        :param AutoUpgradeClusterLevel: Auto cluster upgrade for managed clusters
        :type AutoUpgradeClusterLevel: :class:`tencentcloud.tke.v20180525.models.AutoUpgradeClusterLevel`
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
        self.SubnetId = None
        self.ClusterLevel = None
        self.AutoUpgradeClusterLevel = None


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
        self.SubnetId = params.get("SubnetId")
        self.ClusterLevel = params.get("ClusterLevel")
        if params.get("AutoUpgradeClusterLevel") is not None:
            self.AutoUpgradeClusterLevel = AutoUpgradeClusterLevel()
            self.AutoUpgradeClusterLevel._deserialize(params.get("AutoUpgradeClusterLevel"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterCIDRSettings(AbstractModel):
    """Container networking parameters for the cluster

    """

    def __init__(self):
        r"""
        :param ClusterCIDR: CIDR used to assign container and service IPs for the cluster. It cannot conflict with the VPC's CIDR or the CIDRs of other clusters in the same VPC
        :type ClusterCIDR: str
        :param IgnoreClusterCIDRConflict: Whether to ignore ClusterCIDR conflict errors, which are not ignored by default
        :type IgnoreClusterCIDRConflict: bool
        :param MaxNodePodNum: Maximum number of Pods on each node. Value range: 16 to 256. When its power is not 2, it will round upward to the closest power of 2.
        :type MaxNodePodNum: int
        :param MaxClusterServiceNum: The maximum number of services in a cluster. The range is from 32 to 32768. When its power is not 2, it will round upward to the closest power of 2. Default value is 256.
        :type MaxClusterServiceNum: int
        :param ServiceCIDR: The CIDR block used to assign cluster service IP addresses. It must conflict with neither the VPC CIDR block nor with CIDR blocks of other clusters in the same VPC instance. The IP range must be within the private network IP range, such as 10.1.0.0/14, 192.168.0.1/18, and 172.16.0.0/16.
        :type ServiceCIDR: str
        :param EniSubnetIds: Subnet ID of the ENI in VPC-CNI network mode
        :type EniSubnetIds: list of str
        :param ClaimExpiredSeconds: Repossession time of ENI IP addresses in VPC-CNI network mode, whose range is [300,15768000)
        :type ClaimExpiredSeconds: int
        :param IgnoreServiceCIDRConflict: Whether to ignore ServiceCIDR conflict errors. It is only valid in VPC-CNI mode. Default value: `false`.
        :type IgnoreServiceCIDRConflict: bool
        """
        self.ClusterCIDR = None
        self.IgnoreClusterCIDRConflict = None
        self.MaxNodePodNum = None
        self.MaxClusterServiceNum = None
        self.ServiceCIDR = None
        self.EniSubnetIds = None
        self.ClaimExpiredSeconds = None
        self.IgnoreServiceCIDRConflict = None


    def _deserialize(self, params):
        self.ClusterCIDR = params.get("ClusterCIDR")
        self.IgnoreClusterCIDRConflict = params.get("IgnoreClusterCIDRConflict")
        self.MaxNodePodNum = params.get("MaxNodePodNum")
        self.MaxClusterServiceNum = params.get("MaxClusterServiceNum")
        self.ServiceCIDR = params.get("ServiceCIDR")
        self.EniSubnetIds = params.get("EniSubnetIds")
        self.ClaimExpiredSeconds = params.get("ClaimExpiredSeconds")
        self.IgnoreServiceCIDRConflict = params.get("IgnoreServiceCIDRConflict")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterCondition(AbstractModel):
    """Cluster creation process

    """

    def __init__(self):
        r"""
        :param Type: Process type
        :type Type: str
        :param Status: Process status
        :type Status: str
        :param LastProbeTime: Last time when the status is probed
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LastProbeTime: str
        :param LastTransitionTime: Last time when transiting to the process
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type LastTransitionTime: str
        :param Reason: Reasons for transiting to the process
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Reason: str
        :param Message: More information on transition
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Message: str
        """
        self.Type = None
        self.Status = None
        self.LastProbeTime = None
        self.LastTransitionTime = None
        self.Reason = None
        self.Message = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.LastProbeTime = params.get("LastProbeTime")
        self.LastTransitionTime = params.get("LastTransitionTime")
        self.Reason = params.get("Reason")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterCredential(AbstractModel):
    """Authentication information for accessing K8s

    """

    def __init__(self):
        r"""
        :param CACert: CA root certificate
        :type CACert: str
        :param Token: Token for authentication
        :type Token: str
        """
        self.CACert = None
        self.Token = None


    def _deserialize(self, params):
        self.CACert = params.get("CACert")
        self.Token = params.get("Token")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterExtraArgs(AbstractModel):
    """Cluster master custom parameter

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterLevelAttribute(AbstractModel):
    """Information of the managed cluster model

    """

    def __init__(self):
        r"""
        :param Name: Cluster model
        :type Name: str
        :param Alias: Model name
        :type Alias: str
        :param NodeCount: Number of nodes
        :type NodeCount: int
        :param PodCount: Number of Pods
        :type PodCount: int
        :param ConfigMapCount: Number of ConfigMap
        :type ConfigMapCount: int
        :param CRDCount: Number of CRDs
        :type CRDCount: int
        :param Enable: Whether it is enabled
        :type Enable: bool
        :param OtherCount: Number of other resources
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type OtherCount: int
        """
        self.Name = None
        self.Alias = None
        self.NodeCount = None
        self.PodCount = None
        self.ConfigMapCount = None
        self.CRDCount = None
        self.Enable = None
        self.OtherCount = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Alias = params.get("Alias")
        self.NodeCount = params.get("NodeCount")
        self.PodCount = params.get("PodCount")
        self.ConfigMapCount = params.get("ConfigMapCount")
        self.CRDCount = params.get("CRDCount")
        self.Enable = params.get("Enable")
        self.OtherCount = params.get("OtherCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterLevelChangeRecord(AbstractModel):
    """Cluster model adjustment history

    """

    def __init__(self):
        r"""
        :param ID: Record ID
        :type ID: str
        :param ClusterID: Cluster ID
        :type ClusterID: str
        :param Status: Status (valid values: `trading`, `upgrading`, `success`, `failed`)
        :type Status: str
        :param Message: Status description
        :type Message: str
        :param OldLevel: Original model
        :type OldLevel: str
        :param NewLevel: New model
        :type NewLevel: str
        :param TriggerType: Trigger type (valid values: `manual`, `auto`)
        :type TriggerType: str
        :param StartedAt: Start time
        :type StartedAt: str
        :param EndedAt: End time
        :type EndedAt: str
        """
        self.ID = None
        self.ClusterID = None
        self.Status = None
        self.Message = None
        self.OldLevel = None
        self.NewLevel = None
        self.TriggerType = None
        self.StartedAt = None
        self.EndedAt = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.ClusterID = params.get("ClusterID")
        self.Status = params.get("Status")
        self.Message = params.get("Message")
        self.OldLevel = params.get("OldLevel")
        self.NewLevel = params.get("NewLevel")
        self.TriggerType = params.get("TriggerType")
        self.StartedAt = params.get("StartedAt")
        self.EndedAt = params.get("EndedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterNetworkSettings(AbstractModel):
    """Cluster network-related parameters

    """

    def __init__(self):
        r"""
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
        :param KubeProxyMode: The network mode of service. This parameter is only applicable to ipvs+bpf mode.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type KubeProxyMode: str
        :param ServiceCIDR: The IP range for service assignment. It cannot conflict with the VPC’s CIDR block nor the CIDR blocks of other clusters in the same VPC.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type ServiceCIDR: str
        :param Subnets: The container subnet associated with the cluster
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Subnets: list of str
        :param IgnoreServiceCIDRConflict: Whether to ignore ServiceCIDR conflict errors. It is only valid in VPC-CNI mode. Default value: `false`.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IgnoreServiceCIDRConflict: bool
        :param IsDualStack: Whether it is a dual-stack cluster in VPC-CNI mode. Default value: `false`, which indicates it is not a dual-stack cluster.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type IsDualStack: bool
        :param Ipv6ServiceCIDR: It is used to automatically assign the IP ranges for the service.
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Ipv6ServiceCIDR: str
        """
        self.ClusterCIDR = None
        self.IgnoreClusterCIDRConflict = None
        self.MaxNodePodNum = None
        self.MaxClusterServiceNum = None
        self.Ipvs = None
        self.VpcId = None
        self.Cni = None
        self.KubeProxyMode = None
        self.ServiceCIDR = None
        self.Subnets = None
        self.IgnoreServiceCIDRConflict = None
        self.IsDualStack = None
        self.Ipv6ServiceCIDR = None


    def _deserialize(self, params):
        self.ClusterCIDR = params.get("ClusterCIDR")
        self.IgnoreClusterCIDRConflict = params.get("IgnoreClusterCIDRConflict")
        self.MaxNodePodNum = params.get("MaxNodePodNum")
        self.MaxClusterServiceNum = params.get("MaxClusterServiceNum")
        self.Ipvs = params.get("Ipvs")
        self.VpcId = params.get("VpcId")
        self.Cni = params.get("Cni")
        self.KubeProxyMode = params.get("KubeProxyMode")
        self.ServiceCIDR = params.get("ServiceCIDR")
        self.Subnets = params.get("Subnets")
        self.IgnoreServiceCIDRConflict = params.get("IgnoreServiceCIDRConflict")
        self.IsDualStack = params.get("IsDualStack")
        self.Ipv6ServiceCIDR = params.get("Ipv6ServiceCIDR")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterStatus(AbstractModel):
    """Cluster status information

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param ClusterState: Cluster status
        :type ClusterState: str
        :param ClusterInstanceState: Status of nodes in the cluster
        :type ClusterInstanceState: str
        :param ClusterBMonitor: Indicates whether the monitoring service is enabled for the cluster
        :type ClusterBMonitor: bool
        :param ClusterInitNodeNum: Number of cluster nodes being created. "-1" indicates that the request to obtain the node status timed out. "-2" indicates that the request failed.
        :type ClusterInitNodeNum: int
        :param ClusterRunningNodeNum: Number of running nodes in the cluster. "-1" indicates that the request to obtain the node status timed out. "-2" indicates that the request failed.
        :type ClusterRunningNodeNum: int
        :param ClusterFailedNodeNum: Number of abnormal nodes in the cluster.  "-1" indicates that the request to obtain the node status timed out. "-2" indicates that the request failed.
        :type ClusterFailedNodeNum: int
        :param ClusterClosedNodeNum: Number of shutdown nodes in the cluster.  "-1" indicates that the request to obtain the node status timed out. "-2" indicates that the request failed.
Note: this field may return `null`, indicating that no valid value can be found.
        :type ClusterClosedNodeNum: int
        :param ClusterClosingNodeNum: Number of nodes being shut down in the cluster.  "-1" indicates that the request to obtain the node status timed out. "-2" indicates that the request failed.
Note: this field may return `null`, indicating that no valid value can be found.
        :type ClusterClosingNodeNum: int
        :param ClusterDeletionProtection: Indicates whether to enable cluster deletion protection
Note: this field may return `null`, indicating that no valid value can be found.
        :type ClusterDeletionProtection: bool
        :param ClusterAuditEnabled: Indicates whether the cluster is auditable
Note: this field may return `null`, indicating that no valid value can be found.
        :type ClusterAuditEnabled: bool
        """
        self.ClusterId = None
        self.ClusterState = None
        self.ClusterInstanceState = None
        self.ClusterBMonitor = None
        self.ClusterInitNodeNum = None
        self.ClusterRunningNodeNum = None
        self.ClusterFailedNodeNum = None
        self.ClusterClosedNodeNum = None
        self.ClusterClosingNodeNum = None
        self.ClusterDeletionProtection = None
        self.ClusterAuditEnabled = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterState = params.get("ClusterState")
        self.ClusterInstanceState = params.get("ClusterInstanceState")
        self.ClusterBMonitor = params.get("ClusterBMonitor")
        self.ClusterInitNodeNum = params.get("ClusterInitNodeNum")
        self.ClusterRunningNodeNum = params.get("ClusterRunningNodeNum")
        self.ClusterFailedNodeNum = params.get("ClusterFailedNodeNum")
        self.ClusterClosedNodeNum = params.get("ClusterClosedNodeNum")
        self.ClusterClosingNodeNum = params.get("ClusterClosingNodeNum")
        self.ClusterDeletionProtection = params.get("ClusterDeletionProtection")
        self.ClusterAuditEnabled = params.get("ClusterAuditEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterVersion(AbstractModel):
    """Cluster version information

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonName(AbstractModel):
    """The CommonName in the certificate of the client corresponding to the user UIN

    """

    def __init__(self):
        r"""
        :param SubaccountUin: User UIN
        :type SubaccountUin: str
        :param CN: The CommonName in the certificate of the client corresponding to the sub-account
        :type CN: str
        """
        self.SubaccountUin = None
        self.CN = None


    def _deserialize(self, params):
        self.SubaccountUin = params.get("SubaccountUin")
        self.CN = params.get("CN")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterEndpointRequest(AbstractModel):
    """CreateClusterEndpoint request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param SubnetId: The ID of the subnet where the cluster's port is located (only needs to be entered when the non-public network access is enabled, and must be within the subnet of the cluster's VPC). 
        :type SubnetId: str
        :param IsExtranet: Whether public network access is enabled or not (True = public network access, FALSE = private network access, with the default value as FALSE).
        :type IsExtranet: bool
        :param Domain: The domain name
        :type Domain: str
        :param SecurityGroup: The security group in use, which must be passed in when public access is enabled.
        :type SecurityGroup: str
        :param ExtensiveParameters: The LB parameter. Required only for public network access.
        :type ExtensiveParameters: str
        """
        self.ClusterId = None
        self.SubnetId = None
        self.IsExtranet = None
        self.Domain = None
        self.SecurityGroup = None
        self.ExtensiveParameters = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SubnetId = params.get("SubnetId")
        self.IsExtranet = params.get("IsExtranet")
        self.Domain = params.get("Domain")
        self.SecurityGroup = params.get("SecurityGroup")
        self.ExtensiveParameters = params.get("ExtensiveParameters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterEndpointResponse(AbstractModel):
    """CreateClusterEndpoint response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterEndpointVipResponse(AbstractModel):
    """CreateClusterEndpointVip response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterInstancesResponse(AbstractModel):
    """CreateClusterInstances response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterNodePoolFromExistingAsgResponse(AbstractModel):
    """CreateClusterNodePoolFromExistingAsg response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        :param ContainerRuntime: Node pool runtime type and version
        :type ContainerRuntime: str
        :param RuntimeVersion: Runtime version
        :type RuntimeVersion: str
        :param NodePoolOs: Node pool operating system (enter the image ID for a custom image, and enter the OS name for a public image)
        :type NodePoolOs: str
        :param OsCustomizeType: Container image tag, `DOCKER_CUSTOMIZE` (container customized tag), `GENERAL` (general tag, default value)
        :type OsCustomizeType: str
        :param Tags: Resource tag
        :type Tags: list of Tag
        :param DeletionProtection: Whether Deletion Protection is enabled
        :type DeletionProtection: bool
        """
        self.ClusterId = None
        self.AutoScalingGroupPara = None
        self.LaunchConfigurePara = None
        self.InstanceAdvancedSettings = None
        self.EnableAutoscale = None
        self.Name = None
        self.Labels = None
        self.Taints = None
        self.ContainerRuntime = None
        self.RuntimeVersion = None
        self.NodePoolOs = None
        self.OsCustomizeType = None
        self.Tags = None
        self.DeletionProtection = None


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
        self.ContainerRuntime = params.get("ContainerRuntime")
        self.RuntimeVersion = params.get("RuntimeVersion")
        self.NodePoolOs = params.get("NodePoolOs")
        self.OsCustomizeType = params.get("OsCustomizeType")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.DeletionProtection = params.get("DeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterNodePoolResponse(AbstractModel):
    """CreateClusterNodePool response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        :param ExistedInstancesForNode: The configuration information for existing instances. All instances must be in the same VPC. Up to 100 instances are allowed in one VPC. Spot instances are not supported.
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


class CreateClusterRouteTableRequest(AbstractModel):
    """CreateClusterRouteTable request structure.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterRouteTableResponse(AbstractModel):
    """CreateClusterRouteTable response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateECMInstancesRequest(AbstractModel):
    """CreateECMInstances request structure.

    """

    def __init__(self):
        r"""
        :param ClusterID: Cluster ID
        :type ClusterID: str
        :param ModuleId: Module ID
        :type ModuleId: str
        :param ZoneInstanceCountISPSet: Instance AZ, number of instances and ISP
        :type ZoneInstanceCountISPSet: list of ECMZoneInstanceCountISP
        :param Password: Password
        :type Password: str
        :param InternetMaxBandwidthOut: Public network bandwidth
        :type InternetMaxBandwidthOut: int
        :param ImageId: Image ID
        :type ImageId: str
        :param InstanceName: Instance name
        :type InstanceName: str
        :param HostName: Host name
        :type HostName: str
        :param EnhancedService: Enhanced service (including CWP and Cloud Monitoring)
        :type EnhancedService: :class:`tencentcloud.tke.v20180525.models.ECMEnhancedService`
        :param UserData: Custom script
        :type UserData: str
        :param External: Instance extension information
        :type External: str
        :param SecurityGroupIds: Security group of the instance
        :type SecurityGroupIds: list of str
        """
        self.ClusterID = None
        self.ModuleId = None
        self.ZoneInstanceCountISPSet = None
        self.Password = None
        self.InternetMaxBandwidthOut = None
        self.ImageId = None
        self.InstanceName = None
        self.HostName = None
        self.EnhancedService = None
        self.UserData = None
        self.External = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.ClusterID = params.get("ClusterID")
        self.ModuleId = params.get("ModuleId")
        if params.get("ZoneInstanceCountISPSet") is not None:
            self.ZoneInstanceCountISPSet = []
            for item in params.get("ZoneInstanceCountISPSet"):
                obj = ECMZoneInstanceCountISP()
                obj._deserialize(item)
                self.ZoneInstanceCountISPSet.append(obj)
        self.Password = params.get("Password")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.ImageId = params.get("ImageId")
        self.InstanceName = params.get("InstanceName")
        self.HostName = params.get("HostName")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = ECMEnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.UserData = params.get("UserData")
        self.External = params.get("External")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateECMInstancesResponse(AbstractModel):
    """CreateECMInstances response structure.

    """

    def __init__(self):
        r"""
        :param EcmIdSet: ECM ID list
        :type EcmIdSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.EcmIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EcmIdSet = params.get("EcmIdSet")
        self.RequestId = params.get("RequestId")


class CreateEdgeCVMInstancesRequest(AbstractModel):
    """CreateEdgeCVMInstances request structure.

    """

    def __init__(self):
        r"""
        :param ClusterID: Cluster ID
        :type ClusterID: str
        :param RunInstancePara: Pass-through parameter for CVM creation in the format of a JSON string. To ensure the idempotency of requests for adding cluster nodes, you need to add the `ClientToken` field in this parameter. For more information, see the documentation for [RunInstances](https://intl.cloud.tencent.com/document/product/213/15730?from_cn_redirect=1) API.
        :type RunInstancePara: str
        :param CvmRegion: Region of the CVM instances to create
        :type CvmRegion: str
        :param CvmCount: Quantity of CVM instances to create
        :type CvmCount: int
        :param External: Instance extension information
        :type External: str
        :param UserScript: Custom script
        :type UserScript: str
        :param EnableEni: Whether to enable ENI
        :type EnableEni: bool
        """
        self.ClusterID = None
        self.RunInstancePara = None
        self.CvmRegion = None
        self.CvmCount = None
        self.External = None
        self.UserScript = None
        self.EnableEni = None


    def _deserialize(self, params):
        self.ClusterID = params.get("ClusterID")
        self.RunInstancePara = params.get("RunInstancePara")
        self.CvmRegion = params.get("CvmRegion")
        self.CvmCount = params.get("CvmCount")
        self.External = params.get("External")
        self.UserScript = params.get("UserScript")
        self.EnableEni = params.get("EnableEni")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgeCVMInstancesResponse(AbstractModel):
    """CreateEdgeCVMInstances response structure.

    """

    def __init__(self):
        r"""
        :param CvmIdSet: List of CVM IDs
        :type CvmIdSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CvmIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CvmIdSet = params.get("CvmIdSet")
        self.RequestId = params.get("RequestId")


class CreateEdgeLogConfigRequest(AbstractModel):
    """CreateEdgeLogConfig request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param LogConfig: Log collection configuration in json form
        :type LogConfig: str
        :param LogsetId: CLS logset ID
        :type LogsetId: str
        """
        self.ClusterId = None
        self.LogConfig = None
        self.LogsetId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.LogConfig = params.get("LogConfig")
        self.LogsetId = params.get("LogsetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgeLogConfigResponse(AbstractModel):
    """CreateEdgeLogConfig response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreatePrometheusAlertRuleRequest(AbstractModel):
    """CreatePrometheusAlertRule request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param AlertRule: Alarm configurations
        :type AlertRule: :class:`tencentcloud.tke.v20180525.models.PrometheusAlertRuleDetail`
        """
        self.InstanceId = None
        self.AlertRule = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("AlertRule") is not None:
            self.AlertRule = PrometheusAlertRuleDetail()
            self.AlertRule._deserialize(params.get("AlertRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusAlertRuleResponse(AbstractModel):
    """CreatePrometheusAlertRule response structure.

    """

    def __init__(self):
        r"""
        :param Id: Alarm ID
        :type Id: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class CreateTKEEdgeClusterRequest(AbstractModel):
    """CreateTKEEdgeCluster request structure.

    """

    def __init__(self):
        r"""
        :param K8SVersion: 
        :type K8SVersion: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param ClusterName: Cluster name
        :type ClusterName: str
        :param PodCIDR: Cluster Pod CIDR block
        :type PodCIDR: str
        :param ServiceCIDR: Cluster service CIDR block
        :type ServiceCIDR: str
        :param ClusterDesc: Cluster description
        :type ClusterDesc: str
        :param ClusterAdvancedSettings: Cluster advanced settings
        :type ClusterAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.EdgeClusterAdvancedSettings`
        :param MaxNodePodNum: Maximum number of Pods on the node
        :type MaxNodePodNum: int
        :param PublicLB: Public LB of the TKE Edge cluster
        :type PublicLB: :class:`tencentcloud.tke.v20180525.models.EdgeClusterPublicLB`
        :param ClusterLevel: Cluster specification level
        :type ClusterLevel: str
        :param AutoUpgradeClusterLevel: Whether auto upgrade is supported
        :type AutoUpgradeClusterLevel: bool
        :param ChargeType: Cluster billing mode
        :type ChargeType: str
        :param EdgeVersion: Edge cluster version. It is the set of versions of all cluster components.
        :type EdgeVersion: str
        :param RegistryPrefix: Prefix of the image registry of an edge component
        :type RegistryPrefix: str
        """
        self.K8SVersion = None
        self.VpcId = None
        self.ClusterName = None
        self.PodCIDR = None
        self.ServiceCIDR = None
        self.ClusterDesc = None
        self.ClusterAdvancedSettings = None
        self.MaxNodePodNum = None
        self.PublicLB = None
        self.ClusterLevel = None
        self.AutoUpgradeClusterLevel = None
        self.ChargeType = None
        self.EdgeVersion = None
        self.RegistryPrefix = None


    def _deserialize(self, params):
        self.K8SVersion = params.get("K8SVersion")
        self.VpcId = params.get("VpcId")
        self.ClusterName = params.get("ClusterName")
        self.PodCIDR = params.get("PodCIDR")
        self.ServiceCIDR = params.get("ServiceCIDR")
        self.ClusterDesc = params.get("ClusterDesc")
        if params.get("ClusterAdvancedSettings") is not None:
            self.ClusterAdvancedSettings = EdgeClusterAdvancedSettings()
            self.ClusterAdvancedSettings._deserialize(params.get("ClusterAdvancedSettings"))
        self.MaxNodePodNum = params.get("MaxNodePodNum")
        if params.get("PublicLB") is not None:
            self.PublicLB = EdgeClusterPublicLB()
            self.PublicLB._deserialize(params.get("PublicLB"))
        self.ClusterLevel = params.get("ClusterLevel")
        self.AutoUpgradeClusterLevel = params.get("AutoUpgradeClusterLevel")
        self.ChargeType = params.get("ChargeType")
        self.EdgeVersion = params.get("EdgeVersion")
        self.RegistryPrefix = params.get("RegistryPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTKEEdgeClusterResponse(AbstractModel):
    """CreateTKEEdgeCluster response structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: TKE Edge cluster ID
        :type ClusterId: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RequestId = params.get("RequestId")


class CustomDriver(AbstractModel):
    """Custom driver information

    """

    def __init__(self):
        r"""
        :param Address: URL of custom GPU driver address
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Address: str
        """
        self.Address = None


    def _deserialize(self, params):
        self.Address = params.get("Address")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataDisk(AbstractModel):
    """Described the configuration and information of k8s node data disk.

    """

    def __init__(self):
        r"""
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
        :param DiskPartition: Mounted device name or partition name (only required when adding an existing node)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type DiskPartition: str
        """
        self.DiskType = None
        self.FileSystem = None
        self.DiskSize = None
        self.AutoFormatAndMount = None
        self.MountTarget = None
        self.DiskPartition = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.FileSystem = params.get("FileSystem")
        self.DiskSize = params.get("DiskSize")
        self.AutoFormatAndMount = params.get("AutoFormatAndMount")
        self.MountTarget = params.get("MountTarget")
        self.DiskPartition = params.get("DiskPartition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterAsGroupsRequest(AbstractModel):
    """DeleteClusterAsGroups request structure.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterAsGroupsResponse(AbstractModel):
    """DeleteClusterAsGroups response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterEndpointResponse(AbstractModel):
    """DeleteClusterEndpoint response structure.

    """

    def __init__(self):
        r"""
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
        


class DeleteClusterEndpointVipResponse(AbstractModel):
    """DeleteClusterEndpointVip response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterInstancesResponse(AbstractModel):
    """DeleteClusterInstances response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterNodePoolResponse(AbstractModel):
    """DeleteClusterNodePool response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterRouteResponse(AbstractModel):
    """DeleteClusterRoute response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param RouteTableName: Route table name
        :type RouteTableName: str
        """
        self.RouteTableName = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterRouteTableResponse(AbstractModel):
    """DeleteClusterRouteTable response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteECMInstancesRequest(AbstractModel):
    """DeleteECMInstances request structure.

    """

    def __init__(self):
        r"""
        :param ClusterID: Cluster ID
        :type ClusterID: str
        :param EcmIdSet: IDs of ECMs to be deleted
        :type EcmIdSet: list of str
        """
        self.ClusterID = None
        self.EcmIdSet = None


    def _deserialize(self, params):
        self.ClusterID = params.get("ClusterID")
        self.EcmIdSet = params.get("EcmIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteECMInstancesResponse(AbstractModel):
    """DeleteECMInstances response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEdgeCVMInstancesRequest(AbstractModel):
    """DeleteEdgeCVMInstances request structure.

    """

    def __init__(self):
        r"""
        :param ClusterID: Cluster ID
        :type ClusterID: str
        :param CvmIdSet: IDs of CVMs to be deleted
        :type CvmIdSet: list of str
        """
        self.ClusterID = None
        self.CvmIdSet = None


    def _deserialize(self, params):
        self.ClusterID = params.get("ClusterID")
        self.CvmIdSet = params.get("CvmIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEdgeCVMInstancesResponse(AbstractModel):
    """DeleteEdgeCVMInstances response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEdgeClusterInstancesRequest(AbstractModel):
    """DeleteEdgeClusterInstances request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param InstanceIds: Array of instance IDs to be deleted
        :type InstanceIds: list of str
        """
        self.ClusterId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEdgeClusterInstancesResponse(AbstractModel):
    """DeleteEdgeClusterInstances response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrometheusAlertRuleRequest(AbstractModel):
    """DeletePrometheusAlertRule request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param AlertIds: The ID list of alarm rules
        :type AlertIds: list of str
        """
        self.InstanceId = None
        self.AlertIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AlertIds = params.get("AlertIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusAlertRuleResponse(AbstractModel):
    """DeletePrometheusAlertRule response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTKEEdgeClusterRequest(AbstractModel):
    """DeleteTKEEdgeCluster request structure.

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
        


class DeleteTKEEdgeClusterResponse(AbstractModel):
    """DeleteTKEEdgeCluster response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAvailableClusterVersionResponse(AbstractModel):
    """DescribeAvailableClusterVersion response structure.

    """

    def __init__(self):
        r"""
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


class DescribeAvailableTKEEdgeVersionRequest(AbstractModel):
    """DescribeAvailableTKEEdgeVersion request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: You can enter the `ClusterId` to query the current and latest versions of all cluster components.
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
        


class DescribeAvailableTKEEdgeVersionResponse(AbstractModel):
    """DescribeAvailableTKEEdgeVersion response structure.

    """

    def __init__(self):
        r"""
        :param Versions: Version list
        :type Versions: list of str
        :param EdgeVersionLatest: Latest version of the edge cluster
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type EdgeVersionLatest: str
        :param EdgeVersionCurrent: Current version of the edge cluster
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type EdgeVersionCurrent: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Versions = None
        self.EdgeVersionLatest = None
        self.EdgeVersionCurrent = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Versions = params.get("Versions")
        self.EdgeVersionLatest = params.get("EdgeVersionLatest")
        self.EdgeVersionCurrent = params.get("EdgeVersionCurrent")
        self.RequestId = params.get("RequestId")


class DescribeClusterAsGroupOptionRequest(AbstractModel):
    """DescribeClusterAsGroupOption request structure.

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
        


class DescribeClusterAsGroupOptionResponse(AbstractModel):
    """DescribeClusterAsGroupOption response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterAsGroupsResponse(AbstractModel):
    """DescribeClusterAsGroups response structure.

    """

    def __init__(self):
        r"""
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


class DescribeClusterAuthenticationOptionsRequest(AbstractModel):
    """DescribeClusterAuthenticationOptions request structure.

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
        


class DescribeClusterAuthenticationOptionsResponse(AbstractModel):
    """DescribeClusterAuthenticationOptions response structure.

    """

    def __init__(self):
        r"""
        :param ServiceAccounts: ServiceAccount authentication configuration
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ServiceAccounts: :class:`tencentcloud.tke.v20180525.models.ServiceAccountAuthenticationOptions`
        :param LatestOperationState: Result of the last modification. Values: `Updating`, `Success`, `Failed` or `TimeOut`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type LatestOperationState: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ServiceAccounts = None
        self.LatestOperationState = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceAccounts") is not None:
            self.ServiceAccounts = ServiceAccountAuthenticationOptions()
            self.ServiceAccounts._deserialize(params.get("ServiceAccounts"))
        self.LatestOperationState = params.get("LatestOperationState")
        self.RequestId = params.get("RequestId")


class DescribeClusterCommonNamesRequest(AbstractModel):
    """DescribeClusterCommonNames request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param SubaccountUins: Sub-account. Up to 50 sub-accounts can be passed in at a time.
        :type SubaccountUins: list of str
        :param RoleIds: Role ID. Up to 50 role IDs can be passed in at a time.
        :type RoleIds: list of str
        """
        self.ClusterId = None
        self.SubaccountUins = None
        self.RoleIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SubaccountUins = params.get("SubaccountUins")
        self.RoleIds = params.get("RoleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterCommonNamesResponse(AbstractModel):
    """DescribeClusterCommonNames response structure.

    """

    def __init__(self):
        r"""
        :param CommonNames: The CommonName in the certificate of the client corresponding to the sub-account UIN
        :type CommonNames: list of CommonName
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CommonNames = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CommonNames") is not None:
            self.CommonNames = []
            for item in params.get("CommonNames"):
                obj = CommonName()
                obj._deserialize(item)
                self.CommonNames.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterEndpointStatusRequest(AbstractModel):
    """DescribeClusterEndpointStatus request structure.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterEndpointStatusResponse(AbstractModel):
    """DescribeClusterEndpointStatus response structure.

    """

    def __init__(self):
        r"""
        :param Status: The status of cluster access port. It can be `Created` (enabled); `Creating` (enabling) and `NotFound` (not enabled)
Note: this field may return `null`, indicating that no valid value is obtained.
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
        


class DescribeClusterEndpointVipStatusResponse(AbstractModel):
    """DescribeClusterEndpointVipStatus response structure.

    """

    def __init__(self):
        r"""
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


class DescribeClusterEndpointsRequest(AbstractModel):
    """DescribeClusterEndpoints request structure.

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
        


class DescribeClusterEndpointsResponse(AbstractModel):
    """DescribeClusterEndpoints response structure.

    """

    def __init__(self):
        r"""
        :param CertificationAuthority: CA certificate of cluster APIServer
        :type CertificationAuthority: str
        :param ClusterExternalEndpoint: Public network access address of cluster APIServer
        :type ClusterExternalEndpoint: str
        :param ClusterIntranetEndpoint: Private network access address of cluster APIServer
        :type ClusterIntranetEndpoint: str
        :param ClusterDomain: Domain name of cluster APIServer
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterDomain: str
        :param ClusterExternalACL: Public network access ACL of cluster APIServer
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterExternalACL: list of str
        :param ClusterExternalDomain: Public network domain name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterExternalDomain: str
        :param ClusterIntranetDomain: Private network domain name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterIntranetDomain: str
        :param SecurityGroup: Public network security group
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SecurityGroup: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CertificationAuthority = None
        self.ClusterExternalEndpoint = None
        self.ClusterIntranetEndpoint = None
        self.ClusterDomain = None
        self.ClusterExternalACL = None
        self.ClusterExternalDomain = None
        self.ClusterIntranetDomain = None
        self.SecurityGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificationAuthority = params.get("CertificationAuthority")
        self.ClusterExternalEndpoint = params.get("ClusterExternalEndpoint")
        self.ClusterIntranetEndpoint = params.get("ClusterIntranetEndpoint")
        self.ClusterDomain = params.get("ClusterDomain")
        self.ClusterExternalACL = params.get("ClusterExternalACL")
        self.ClusterExternalDomain = params.get("ClusterExternalDomain")
        self.ClusterIntranetDomain = params.get("ClusterIntranetDomain")
        self.SecurityGroup = params.get("SecurityGroup")
        self.RequestId = params.get("RequestId")


class DescribeClusterInstancesRequest(AbstractModel):
    """DescribeClusterInstances request structure.

    """

    def __init__(self):
        r"""
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
        :param Filters: Filters include `nodepool-id` and `nodepool-instance-type` (how the instance is added to the pool). For `nodepool-instance-type`, the values can be `MANUALLY_ADDED`, `AUTOSCALING_ADDED` and `ALL`.
        :type Filters: list of Filter
        """
        self.ClusterId = None
        self.Offset = None
        self.Limit = None
        self.InstanceIds = None
        self.InstanceRole = None
        self.Filters = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceRole = params.get("InstanceRole")
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
        


class DescribeClusterInstancesResponse(AbstractModel):
    """DescribeClusterInstances response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param IsExtranet: Defaults to `false`, which means to obtain the kubeconfig of private network
        :type IsExtranet: bool
        """
        self.ClusterId = None
        self.IsExtranet = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.IsExtranet = params.get("IsExtranet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterKubeconfigResponse(AbstractModel):
    """DescribeClusterKubeconfig response structure.

    """

    def __init__(self):
        r"""
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


class DescribeClusterLevelAttributeRequest(AbstractModel):
    """DescribeClusterLevelAttribute request structure.

    """

    def __init__(self):
        r"""
        :param ClusterID: Cluster ID (available for cluster model adjustment)
        :type ClusterID: str
        """
        self.ClusterID = None


    def _deserialize(self, params):
        self.ClusterID = params.get("ClusterID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterLevelAttributeResponse(AbstractModel):
    """DescribeClusterLevelAttribute response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number
        :type TotalCount: int
        :param Items: Cluster model
        :type Items: list of ClusterLevelAttribute
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ClusterLevelAttribute()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterLevelChangeRecordsRequest(AbstractModel):
    """DescribeClusterLevelChangeRecords request structure.

    """

    def __init__(self):
        r"""
        :param ClusterID: Cluster ID
        :type ClusterID: str
        :param StartAt: Start time
        :type StartAt: str
        :param EndAt: End time
        :type EndAt: str
        :param Offset: Offset. Default value: `0`
        :type Offset: int
        :param Limit: Maximum number of output entries. Default value: `20`
        :type Limit: int
        """
        self.ClusterID = None
        self.StartAt = None
        self.EndAt = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterID = params.get("ClusterID")
        self.StartAt = params.get("StartAt")
        self.EndAt = params.get("EndAt")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterLevelChangeRecordsResponse(AbstractModel):
    """DescribeClusterLevelChangeRecords response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number
        :type TotalCount: int
        :param Items: Cluster model
        :type Items: list of ClusterLevelChangeRecord
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ClusterLevelChangeRecord()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterNodePoolDetailRequest(AbstractModel):
    """DescribeClusterNodePoolDetail request structure.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterNodePoolDetailResponse(AbstractModel):
    """DescribeClusterNodePoolDetail response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param ClusterId: ClusterId (cluster ID)
        :type ClusterId: str
        :param Filters: ·  NodePoolsName
    Filters by the node pool name
    Type: String
    Required: No

·  NodePoolsId
    Filters by the node pool ID
    Type: String
    Required: No

·  tags
    Filters by key-value pairs of tags
    Type: String
    Required: No

·  tag:tag-key
    Filters by key-value pairs of tags
    Type: String
    Required: No
        :type Filters: list of Filter
        """
        self.ClusterId = None
        self.Filters = None


    def _deserialize(self, params):
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
        


class DescribeClusterNodePoolsResponse(AbstractModel):
    """DescribeClusterNodePools response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterRoutesResponse(AbstractModel):
    """DescribeClusterRoutes response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param ClusterId: Cluster ID. Enter the ClusterId field returned by the DescribeClusters API
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
        


class DescribeClusterSecurityResponse(AbstractModel):
    """DescribeClusterSecurity response structure.

    """

    def __init__(self):
        r"""
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


class DescribeClusterStatusRequest(AbstractModel):
    """DescribeClusterStatus request structure.

    """

    def __init__(self):
        r"""
        :param ClusterIds: Cluster ID list. All clusters are pulled if it is left empty.
        :type ClusterIds: list of str
        """
        self.ClusterIds = None


    def _deserialize(self, params):
        self.ClusterIds = params.get("ClusterIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterStatusResponse(AbstractModel):
    """DescribeClusterStatus response structure.

    """

    def __init__(self):
        r"""
        :param ClusterStatusSet: Cluster status list
        :type ClusterStatusSet: list of ClusterStatus
        :param TotalCount: Number of clusters
        :type TotalCount: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ClusterStatusSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterStatusSet") is not None:
            self.ClusterStatusSet = []
            for item in params.get("ClusterStatusSet"):
                obj = ClusterStatus()
                obj._deserialize(item)
                self.ClusterStatusSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters request structure.

    """

    def __init__(self):
        r"""
        :param ClusterIds: Cluster ID list (When it is empty,
all clusters under the account will be obtained)
        :type ClusterIds: list of str
        :param Offset: Offset. Default value: 0
        :type Offset: int
        :param Limit: Maximum number of output entries. Default value: 20
        :type Limit: int
        :param Filters: ·  ClusterName
    Filters by the cluster name
    Type: String
    Required: No

·  ClusterType
    Filters by the cluster type
    Type: String
    Required: No

·  ClusterStatus
    Filters by the cluster status
    Type: String
    Required: No

·  Tags
    Filters by key-value pairs of tags
    Type: String
    Required: No

·  vpc-id
    Filters by the VPC ID
    Type: String
    Required: No

·  tag-key
    Filters by the tag key
    Type: String
    Required: No

·  tag-value
    Filters by the tag value
    Type: String
    Required: No

·  tag:tag-key
    Filters by key-value pairs of tags
    Type: String
    Required: No
        :type Filters: list of Filter
        :param ClusterType: Cluster type, such as `MANAGED_CLUSTER`
        :type ClusterType: str
        """
        self.ClusterIds = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.ClusterType = None


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
        self.ClusterType = params.get("ClusterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters response structure.

    """

    def __init__(self):
        r"""
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


class DescribeECMInstancesRequest(AbstractModel):
    """DescribeECMInstances request structure.

    """

    def __init__(self):
        r"""
        :param ClusterID: Cluster ID
        :type ClusterID: str
        :param Filters: Filter condition
Only filtering by an ECM ID is supported
        :type Filters: list of Filter
        """
        self.ClusterID = None
        self.Filters = None


    def _deserialize(self, params):
        self.ClusterID = params.get("ClusterID")
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
        


class DescribeECMInstancesResponse(AbstractModel):
    """DescribeECMInstances response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of instances matched the condition
        :type TotalCount: int
        :param InstanceInfoSet: List of the returned instance information
        :type InstanceInfoSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.InstanceInfoSet = params.get("InstanceInfoSet")
        self.RequestId = params.get("RequestId")


class DescribeEdgeAvailableExtraArgsRequest(AbstractModel):
    """DescribeEdgeAvailableExtraArgs request structure.

    """

    def __init__(self):
        r"""
        :param ClusterVersion: Cluster version
        :type ClusterVersion: str
        """
        self.ClusterVersion = None


    def _deserialize(self, params):
        self.ClusterVersion = params.get("ClusterVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeAvailableExtraArgsResponse(AbstractModel):
    """DescribeEdgeAvailableExtraArgs response structure.

    """

    def __init__(self):
        r"""
        :param ClusterVersion: Cluster version
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterVersion: str
        :param AvailableExtraArgs: Available custom parameters
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AvailableExtraArgs: :class:`tencentcloud.tke.v20180525.models.EdgeAvailableExtraArgs`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ClusterVersion = None
        self.AvailableExtraArgs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterVersion = params.get("ClusterVersion")
        if params.get("AvailableExtraArgs") is not None:
            self.AvailableExtraArgs = EdgeAvailableExtraArgs()
            self.AvailableExtraArgs._deserialize(params.get("AvailableExtraArgs"))
        self.RequestId = params.get("RequestId")


class DescribeEdgeCVMInstancesRequest(AbstractModel):
    """DescribeEdgeCVMInstances request structure.

    """

    def __init__(self):
        r"""
        :param ClusterID: Cluster ID
        :type ClusterID: str
        :param Filters: Filter condition
Only `cvm-id` is supported.
        :type Filters: list of Filter
        """
        self.ClusterID = None
        self.Filters = None


    def _deserialize(self, params):
        self.ClusterID = params.get("ClusterID")
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
        


class DescribeEdgeCVMInstancesResponse(AbstractModel):
    """DescribeEdgeCVMInstances response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of instances matched the condition
        :type TotalCount: int
        :param InstanceInfoSet: List of the returned instance information
        :type InstanceInfoSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.InstanceInfoSet = params.get("InstanceInfoSet")
        self.RequestId = params.get("RequestId")


class DescribeEdgeClusterExtraArgsRequest(AbstractModel):
    """DescribeEdgeClusterExtraArgs request structure.

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
        


class DescribeEdgeClusterExtraArgsResponse(AbstractModel):
    """DescribeEdgeClusterExtraArgs response structure.

    """

    def __init__(self):
        r"""
        :param ClusterExtraArgs: Custom parameters of the cluster
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterExtraArgs: :class:`tencentcloud.tke.v20180525.models.EdgeClusterExtraArgs`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ClusterExtraArgs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterExtraArgs") is not None:
            self.ClusterExtraArgs = EdgeClusterExtraArgs()
            self.ClusterExtraArgs._deserialize(params.get("ClusterExtraArgs"))
        self.RequestId = params.get("RequestId")


class DescribeEdgeClusterInstancesRequest(AbstractModel):
    """DescribeEdgeClusterInstances request structure.

    """

    def __init__(self):
        r"""
        :param ClusterID: Cluster ID
        :type ClusterID: str
        :param Limit: Max number of returned entries
        :type Limit: int
        :param Offset: Offset
        :type Offset: int
        :param Filters: Filter condition. Only `NodeName` is supported.
        :type Filters: list of Filter
        """
        self.ClusterID = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.ClusterID = params.get("ClusterID")
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
        


class DescribeEdgeClusterInstancesResponse(AbstractModel):
    """DescribeEdgeClusterInstances response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of nodes in the cluster
        :type TotalCount: int
        :param InstanceInfoSet: Array of node information
        :type InstanceInfoSet: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.InstanceInfoSet = params.get("InstanceInfoSet")
        self.RequestId = params.get("RequestId")


class DescribeEdgeLogSwitchesRequest(AbstractModel):
    """DescribeEdgeLogSwitches request structure.

    """

    def __init__(self):
        r"""
        :param ClusterIds: List of cluster IDs
        :type ClusterIds: list of str
        """
        self.ClusterIds = None


    def _deserialize(self, params):
        self.ClusterIds = params.get("ClusterIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeLogSwitchesResponse(AbstractModel):
    """DescribeEdgeLogSwitches response structure.

    """

    def __init__(self):
        r"""
        :param SwitchSet: Array of TKE Edge cluster log switches
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SwitchSet: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SwitchSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SwitchSet = params.get("SwitchSet")
        self.RequestId = params.get("RequestId")


class DescribeEnableVpcCniProgressRequest(AbstractModel):
    """DescribeEnableVpcCniProgress request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: ID of the cluster for which you want to enable the VPC-CNI mode
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
        


class DescribeEnableVpcCniProgressResponse(AbstractModel):
    """DescribeEnableVpcCniProgress response structure.

    """

    def __init__(self):
        r"""
        :param Status: Task status, which can be `Running`, `Succeed`, or `Failed`.
        :type Status: str
        :param ErrorMessage: The description for the task status when the task status is “Failed”, for example, failed to install the IPAMD component.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type ErrorMessage: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.ErrorMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrorMessage = params.get("ErrorMessage")
        self.RequestId = params.get("RequestId")


class DescribeExistedInstancesRequest(AbstractModel):
    """DescribeExistedInstances request structure.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExistedInstancesResponse(AbstractModel):
    """DescribeExistedInstances response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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


class DescribePrometheusInstanceRequest(AbstractModel):
    """DescribePrometheusInstance request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusInstanceResponse(AbstractModel):
    """DescribePrometheusInstance response structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param Name: Instance name
        :type Name: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: Subnet ID
        :type SubnetId: str
        :param COSBucket: COS bucket name
        :type COSBucket: str
        :param QueryAddress: Data query address
        :type QueryAddress: str
        :param Grafana: The grafana related information in the instance
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Grafana: :class:`tencentcloud.tke.v20180525.models.PrometheusGrafanaInfo`
        :param AlertManagerUrl: Custom alertmanager
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type AlertManagerUrl: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.InstanceId = None
        self.Name = None
        self.VpcId = None
        self.SubnetId = None
        self.COSBucket = None
        self.QueryAddress = None
        self.Grafana = None
        self.AlertManagerUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.COSBucket = params.get("COSBucket")
        self.QueryAddress = params.get("QueryAddress")
        if params.get("Grafana") is not None:
            self.Grafana = PrometheusGrafanaInfo()
            self.Grafana._deserialize(params.get("Grafana"))
        self.AlertManagerUrl = params.get("AlertManagerUrl")
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions request structure.

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions response structure.

    """

    def __init__(self):
        r"""
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


class DescribeResourceUsageRequest(AbstractModel):
    """DescribeResourceUsage request structure.

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
        


class DescribeResourceUsageResponse(AbstractModel):
    """DescribeResourceUsage response structure.

    """

    def __init__(self):
        r"""
        :param CRDUsage: CRD usage
        :type CRDUsage: :class:`tencentcloud.tke.v20180525.models.ResourceUsage`
        :param PodUsage: Pod usage
        :type PodUsage: int
        :param ConfigMapUsage: ConfigMap usage
        :type ConfigMapUsage: int
        :param OtherUsage: Other resource usage
        :type OtherUsage: :class:`tencentcloud.tke.v20180525.models.ResourceUsage`
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.CRDUsage = None
        self.PodUsage = None
        self.ConfigMapUsage = None
        self.OtherUsage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CRDUsage") is not None:
            self.CRDUsage = ResourceUsage()
            self.CRDUsage._deserialize(params.get("CRDUsage"))
        self.PodUsage = params.get("PodUsage")
        self.ConfigMapUsage = params.get("ConfigMapUsage")
        if params.get("OtherUsage") is not None:
            self.OtherUsage = ResourceUsage()
            self.OtherUsage._deserialize(params.get("OtherUsage"))
        self.RequestId = params.get("RequestId")


class DescribeRouteTableConflictsRequest(AbstractModel):
    """DescribeRouteTableConflicts request structure.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRouteTableConflictsResponse(AbstractModel):
    """DescribeRouteTableConflicts response structure.

    """

    def __init__(self):
        r"""
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


class DescribeTKEEdgeClusterCredentialRequest(AbstractModel):
    """DescribeTKEEdgeClusterCredential request structure.

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
        


class DescribeTKEEdgeClusterCredentialResponse(AbstractModel):
    """DescribeTKEEdgeClusterCredential response structure.

    """

    def __init__(self):
        r"""
        :param Addresses: Access address of the cluster
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Addresses: list of IPAddress
        :param Credential: Cluster authentication information
        :type Credential: :class:`tencentcloud.tke.v20180525.models.ClusterCredential`
        :param PublicLB: Public network access information of the cluster
        :type PublicLB: :class:`tencentcloud.tke.v20180525.models.EdgeClusterPublicLB`
        :param InternalLB: Private network access information of the cluster
        :type InternalLB: :class:`tencentcloud.tke.v20180525.models.EdgeClusterInternalLB`
        :param CoreDns: CoreDns deployment information of the cluster
        :type CoreDns: str
        :param HealthRegion: Multi-region health check deployment information of the cluster
        :type HealthRegion: str
        :param Health: Health check deployment information of the cluster
        :type Health: str
        :param GridDaemon: Whether to deploy GridDaemon to support headless service
        :type GridDaemon: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Addresses = None
        self.Credential = None
        self.PublicLB = None
        self.InternalLB = None
        self.CoreDns = None
        self.HealthRegion = None
        self.Health = None
        self.GridDaemon = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Addresses") is not None:
            self.Addresses = []
            for item in params.get("Addresses"):
                obj = IPAddress()
                obj._deserialize(item)
                self.Addresses.append(obj)
        if params.get("Credential") is not None:
            self.Credential = ClusterCredential()
            self.Credential._deserialize(params.get("Credential"))
        if params.get("PublicLB") is not None:
            self.PublicLB = EdgeClusterPublicLB()
            self.PublicLB._deserialize(params.get("PublicLB"))
        if params.get("InternalLB") is not None:
            self.InternalLB = EdgeClusterInternalLB()
            self.InternalLB._deserialize(params.get("InternalLB"))
        self.CoreDns = params.get("CoreDns")
        self.HealthRegion = params.get("HealthRegion")
        self.Health = params.get("Health")
        self.GridDaemon = params.get("GridDaemon")
        self.RequestId = params.get("RequestId")


class DescribeTKEEdgeClusterStatusRequest(AbstractModel):
    """DescribeTKEEdgeClusterStatus request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Edge compute cluster ID
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
        


class DescribeTKEEdgeClusterStatusResponse(AbstractModel):
    """DescribeTKEEdgeClusterStatus response structure.

    """

    def __init__(self):
        r"""
        :param Phase: Current cluster status
        :type Phase: str
        :param Conditions: Array of cluster processes
        :type Conditions: list of ClusterCondition
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Phase = None
        self.Conditions = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Phase = params.get("Phase")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = ClusterCondition()
                obj._deserialize(item)
                self.Conditions.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTKEEdgeClustersRequest(AbstractModel):
    """DescribeTKEEdgeClusters request structure.

    """

    def __init__(self):
        r"""
        :param ClusterIds: Cluster ID list (when it is empty,
all clusters under the account are obtained)
        :type ClusterIds: list of str
        :param Offset: Offset. Default value: `0`
        :type Offset: int
        :param Limit: Maximum number of output entries. Default value: `20`
        :type Limit: int
        :param Filters: Filter condition (only filtering by a single ClusterName is supported)
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTKEEdgeClustersResponse(AbstractModel):
    """DescribeTKEEdgeClusters response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Total number of clusters
        :type TotalCount: int
        :param Clusters: Cluster information list
        :type Clusters: list of EdgeCluster
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
                obj = EdgeCluster()
                obj._deserialize(item)
                self.Clusters.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTKEEdgeExternalKubeconfigRequest(AbstractModel):
    """DescribeTKEEdgeExternalKubeconfig request structure.

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
        


class DescribeTKEEdgeExternalKubeconfigResponse(AbstractModel):
    """DescribeTKEEdgeExternalKubeconfig response structure.

    """

    def __init__(self):
        r"""
        :param Kubeconfig: Kubeconfig file content
        :type Kubeconfig: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Kubeconfig = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Kubeconfig = params.get("Kubeconfig")
        self.RequestId = params.get("RequestId")


class DescribeTKEEdgeScriptRequest(AbstractModel):
    """DescribeTKEEdgeScript request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param Interface: ENI
        :type Interface: str
        :param NodeName: Name of the name
        :type NodeName: str
        :param Config: Node configuration in JSON format 
        :type Config: str
        :param ScriptVersion: A legacy version of edgectl script can be downloaded. The latest version is downloaded by default. The version information can be checked in the script.
        :type ScriptVersion: str
        """
        self.ClusterId = None
        self.Interface = None
        self.NodeName = None
        self.Config = None
        self.ScriptVersion = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Interface = params.get("Interface")
        self.NodeName = params.get("NodeName")
        self.Config = params.get("Config")
        self.ScriptVersion = params.get("ScriptVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTKEEdgeScriptResponse(AbstractModel):
    """DescribeTKEEdgeScript response structure.

    """

    def __init__(self):
        r"""
        :param Link: Whether to download the link
        :type Link: str
        :param Token: Whether to download the desired token
        :type Token: str
        :param Command: Whether to download the command
        :type Command: str
        :param ScriptVersion: Version of edgectl script. The latest version is obtained by default.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ScriptVersion: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Link = None
        self.Token = None
        self.Command = None
        self.ScriptVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Link = params.get("Link")
        self.Token = params.get("Token")
        self.Command = params.get("Command")
        self.ScriptVersion = params.get("ScriptVersion")
        self.RequestId = params.get("RequestId")


class DescribeVersionsRequest(AbstractModel):
    """DescribeVersions request structure.

    """


class DescribeVersionsResponse(AbstractModel):
    """DescribeVersions response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: Number of versions
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type TotalCount: int
        :param VersionInstanceSet: Version list
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type VersionInstanceSet: list of VersionInstance
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.VersionInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VersionInstanceSet") is not None:
            self.VersionInstanceSet = []
            for item in params.get("VersionInstanceSet"):
                obj = VersionInstance()
                obj._deserialize(item)
                self.VersionInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpcCniPodLimitsRequest(AbstractModel):
    """DescribeVpcCniPodLimits request structure.

    """

    def __init__(self):
        r"""
        :param Zone: The availability zone of the model to query, for example, `ap-guangzhou-3`. This field is left empty by default, that is, do not filter by the availability zone.
        :type Zone: str
        :param InstanceFamily: The instance family to query, for example, `S5`. This field is left empty by default, that is, do not filter by the instance family.
        :type InstanceFamily: str
        :param InstanceType: The instance model to query, for example, `S5.LARGE8`. This field is empty by default, that is, do not filter by instance type.
        :type InstanceType: str
        """
        self.Zone = None
        self.InstanceFamily = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceFamily = params.get("InstanceFamily")
        self.InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcCniPodLimitsResponse(AbstractModel):
    """DescribeVpcCniPodLimits response structure.

    """

    def __init__(self):
        r"""
        :param TotalCount: The number of the models
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type TotalCount: int
        :param PodLimitsInstanceSet: The model information and the maximum supported number of Pods in the VPC-CNI mode
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type PodLimitsInstanceSet: list of PodLimitsInstance
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.TotalCount = None
        self.PodLimitsInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PodLimitsInstanceSet") is not None:
            self.PodLimitsInstanceSet = []
            for item in params.get("PodLimitsInstanceSet"):
                obj = PodLimitsInstance()
                obj._deserialize(item)
                self.PodLimitsInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DisableClusterDeletionProtectionRequest(AbstractModel):
    """DisableClusterDeletionProtection request structure.

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
        


class DisableClusterDeletionProtectionResponse(AbstractModel):
    """DisableClusterDeletionProtection response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DriverVersion(AbstractModel):
    """Version information of GPU driver and CUDA

    """

    def __init__(self):
        r"""
        :param Version: Version of GPU driver or CUDA
        :type Version: str
        :param Name: Name of GPU driver or CUDA
        :type Name: str
        """
        self.Version = None
        self.Name = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ECMEnhancedService(AbstractModel):
    """ECM enhanced services

    """

    def __init__(self):
        r"""
        :param SecurityService: Whether Cloud Monitoring is enabled
        :type SecurityService: :class:`tencentcloud.tke.v20180525.models.ECMRunMonitorServiceEnabled`
        :param MonitorService: Whether Cloud Workload Protection is enabled
        :type MonitorService: :class:`tencentcloud.tke.v20180525.models.ECMRunSecurityServiceEnabled`
        """
        self.SecurityService = None
        self.MonitorService = None


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self.SecurityService = ECMRunMonitorServiceEnabled()
            self.SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self.MonitorService = ECMRunSecurityServiceEnabled()
            self.MonitorService._deserialize(params.get("MonitorService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ECMRunMonitorServiceEnabled(AbstractModel):
    """ECM Cloud Monitoring

    """

    def __init__(self):
        r"""
        :param Enabled: Whether it is enabled
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ECMRunSecurityServiceEnabled(AbstractModel):
    """ECM Cloud Workload Protection

    """

    def __init__(self):
        r"""
        :param Enabled: Whether it is enabled
        :type Enabled: bool
        :param Version: CWP version. Valid values: `0` (CWP Pro), `1` (CWP Pro)
        :type Version: int
        """
        self.Enabled = None
        self.Version = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ECMZoneInstanceCountISP(AbstractModel):
    """Combination of the ECM instance AZ, number of instances, and ISP

    """

    def __init__(self):
        r"""
        :param Zone: Instance AZ
        :type Zone: str
        :param InstanceCount: Number of instances to be created in the current AZ
        :type InstanceCount: int
        :param ISP: ISP
        :type ISP: str
        """
        self.Zone = None
        self.InstanceCount = None
        self.ISP = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceCount = params.get("InstanceCount")
        self.ISP = params.get("ISP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeArgsFlag(AbstractModel):
    """Edge cluster parameters

    """

    def __init__(self):
        r"""
        :param Name: Parameter name
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Name: str
        :param Type: Parameter type
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Type: str
        :param Usage: Parameter description
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Usage: str
        :param Default: Default value of the parameter
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Default: str
        :param Constraint: Valid value or range. Options: `[]` (it indicates a range, for example, “[1, 5]” indicates the parameter must be equal or larger than 1, and be equal or smaller than 5), and `()` (it indicates a valid value, for example, “('aa', 'bb')” indicates the parameter must be “aa” or “bb”. If it is left empty, the verification can be skipped.)
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Constraint: str
        """
        self.Name = None
        self.Type = None
        self.Usage = None
        self.Default = None
        self.Constraint = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Usage = params.get("Usage")
        self.Default = params.get("Default")
        self.Constraint = params.get("Constraint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeAvailableExtraArgs(AbstractModel):
    """Custom parameters available for the edge cluster

    """

    def __init__(self):
        r"""
        :param KubeAPIServer: kube-apiserver custom parameter
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type KubeAPIServer: list of EdgeArgsFlag
        :param KubeControllerManager: kube-controller-manager custom parameter
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type KubeControllerManager: list of EdgeArgsFlag
        :param KubeScheduler: kube-scheduler custom parameter
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type KubeScheduler: list of EdgeArgsFlag
        :param Kubelet: kubelet custom parameter
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Kubelet: list of EdgeArgsFlag
        """
        self.KubeAPIServer = None
        self.KubeControllerManager = None
        self.KubeScheduler = None
        self.Kubelet = None


    def _deserialize(self, params):
        if params.get("KubeAPIServer") is not None:
            self.KubeAPIServer = []
            for item in params.get("KubeAPIServer"):
                obj = EdgeArgsFlag()
                obj._deserialize(item)
                self.KubeAPIServer.append(obj)
        if params.get("KubeControllerManager") is not None:
            self.KubeControllerManager = []
            for item in params.get("KubeControllerManager"):
                obj = EdgeArgsFlag()
                obj._deserialize(item)
                self.KubeControllerManager.append(obj)
        if params.get("KubeScheduler") is not None:
            self.KubeScheduler = []
            for item in params.get("KubeScheduler"):
                obj = EdgeArgsFlag()
                obj._deserialize(item)
                self.KubeScheduler.append(obj)
        if params.get("Kubelet") is not None:
            self.Kubelet = []
            for item in params.get("Kubelet"):
                obj = EdgeArgsFlag()
                obj._deserialize(item)
                self.Kubelet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeCluster(AbstractModel):
    """Edge compute cluster information

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param ClusterName: Cluster name
        :type ClusterName: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param PodCIDR: Cluster Pod CIDR block
        :type PodCIDR: str
        :param ServiceCIDR: Cluster service CIDR block
        :type ServiceCIDR: str
        :param K8SVersion: 
        :type K8SVersion: str
        :param Status: Cluster status
        :type Status: str
        :param ClusterDesc: Cluster description
        :type ClusterDesc: str
        :param CreatedTime: Cluster creation time
        :type CreatedTime: str
        :param EdgeClusterVersion: Edge cluster version
        :type EdgeClusterVersion: str
        :param MaxNodePodNum: Maximum number of Pods on the node
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type MaxNodePodNum: int
        :param ClusterAdvancedSettings: Cluster advanced settings
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.EdgeClusterAdvancedSettings`
        """
        self.ClusterId = None
        self.ClusterName = None
        self.VpcId = None
        self.PodCIDR = None
        self.ServiceCIDR = None
        self.K8SVersion = None
        self.Status = None
        self.ClusterDesc = None
        self.CreatedTime = None
        self.EdgeClusterVersion = None
        self.MaxNodePodNum = None
        self.ClusterAdvancedSettings = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.VpcId = params.get("VpcId")
        self.PodCIDR = params.get("PodCIDR")
        self.ServiceCIDR = params.get("ServiceCIDR")
        self.K8SVersion = params.get("K8SVersion")
        self.Status = params.get("Status")
        self.ClusterDesc = params.get("ClusterDesc")
        self.CreatedTime = params.get("CreatedTime")
        self.EdgeClusterVersion = params.get("EdgeClusterVersion")
        self.MaxNodePodNum = params.get("MaxNodePodNum")
        if params.get("ClusterAdvancedSettings") is not None:
            self.ClusterAdvancedSettings = EdgeClusterAdvancedSettings()
            self.ClusterAdvancedSettings._deserialize(params.get("ClusterAdvancedSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeClusterAdvancedSettings(AbstractModel):
    """Edge cluster advanced settings

    """

    def __init__(self):
        r"""
        :param ExtraArgs: Custom parameters of the cluster
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ExtraArgs: :class:`tencentcloud.tke.v20180525.models.EdgeClusterExtraArgs`
        :param Runtime: Runtime type. Valid values: "docker" (default), "containerd".
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Runtime: str
        :param ProxyMode: Forwarding mode of kube-proxy. Valid values: "iptables" (default), "ipvs".
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ProxyMode: str
        """
        self.ExtraArgs = None
        self.Runtime = None
        self.ProxyMode = None


    def _deserialize(self, params):
        if params.get("ExtraArgs") is not None:
            self.ExtraArgs = EdgeClusterExtraArgs()
            self.ExtraArgs._deserialize(params.get("ExtraArgs"))
        self.Runtime = params.get("Runtime")
        self.ProxyMode = params.get("ProxyMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeClusterExtraArgs(AbstractModel):
    """Edge cluster master custom parameters

    """

    def __init__(self):
        r"""
        :param KubeAPIServer: kube-apiserver custom parameter, in the format of ["k1=v1", "k1=v2"], for example: ["max-requests-inflight=500","feature-gates=PodShareProcessNamespace=true,DynamicKubeletConfig=true"]
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type KubeAPIServer: list of str
        :param KubeControllerManager: kube-controller-manager custom parameter
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type KubeControllerManager: list of str
        :param KubeScheduler: kube-scheduler custom parameter
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type KubeScheduler: list of str
        """
        self.KubeAPIServer = None
        self.KubeControllerManager = None
        self.KubeScheduler = None


    def _deserialize(self, params):
        self.KubeAPIServer = params.get("KubeAPIServer")
        self.KubeControllerManager = params.get("KubeControllerManager")
        self.KubeScheduler = params.get("KubeScheduler")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeClusterInternalLB(AbstractModel):
    """Edge compute cluster private LB information

    """

    def __init__(self):
        r"""
        :param Enabled: Whether the private LB is enabled
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Enabled: bool
        :param SubnetId: ID of the subnet associated with the private LB
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type SubnetId: list of str
        """
        self.Enabled = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeClusterPublicLB(AbstractModel):
    """Edge compute cluster public LB information

    """

    def __init__(self):
        r"""
        :param Enabled: Whether the public LB is enabled
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type Enabled: bool
        :param AllowFromCidrs: Public network CIDR block allowed to access
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AllowFromCidrs: list of str
        """
        self.Enabled = None
        self.AllowFromCidrs = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.AllowFromCidrs = params.get("AllowFromCidrs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableClusterDeletionProtectionRequest(AbstractModel):
    """EnableClusterDeletionProtection request structure.

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
        


class EnableClusterDeletionProtectionResponse(AbstractModel):
    """EnableClusterDeletionProtection response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableVpcCniNetworkTypeRequest(AbstractModel):
    """EnableVpcCniNetworkType request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param VpcCniType: The VPC-CNI mode. `tke-route-eni`: Multi-IP ENI, `tke-direct-eni`: Independent ENI
        :type VpcCniType: str
        :param EnableStaticIp: Whether to enable static IP address
        :type EnableStaticIp: bool
        :param Subnets: The container subnet being used
        :type Subnets: list of str
        :param ExpiredSeconds: Specifies when to release the IP after the Pod termination in static IP mode. It must be longer than 300 seconds. If this parameter is left empty, the IP address will never be released.
        :type ExpiredSeconds: int
        """
        self.ClusterId = None
        self.VpcCniType = None
        self.EnableStaticIp = None
        self.Subnets = None
        self.ExpiredSeconds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.VpcCniType = params.get("VpcCniType")
        self.EnableStaticIp = params.get("EnableStaticIp")
        self.Subnets = params.get("Subnets")
        self.ExpiredSeconds = params.get("ExpiredSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableVpcCniNetworkTypeResponse(AbstractModel):
    """EnableVpcCniNetworkType response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnhancedService(AbstractModel):
    """Describes the configuration of enhanced services, such as Cloud Security and Cloud Monitor.

    """

    def __init__(self):
        r"""
        :param SecurityService: Enables cloud security service. If this parameter is not specified, the cloud security service will be enabled by default.
        :type SecurityService: :class:`tencentcloud.tke.v20180525.models.RunSecurityServiceEnabled`
        :param MonitorService: Enables cloud monitor service. If this parameter is not specified, the cloud monitor service will be enabled by default.
        :type MonitorService: :class:`tencentcloud.tke.v20180525.models.RunMonitorServiceEnabled`
        :param AutomationService: Enables the TAT service. If this parameter is not specified, the TAT service will not be enabled.
        :type AutomationService: :class:`tencentcloud.tke.v20180525.models.RunAutomationServiceEnabled`
        """
        self.SecurityService = None
        self.MonitorService = None
        self.AutomationService = None


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self.SecurityService = RunSecurityServiceEnabled()
            self.SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self.MonitorService = RunMonitorServiceEnabled()
            self.MonitorService._deserialize(params.get("MonitorService"))
        if params.get("AutomationService") is not None:
            self.AutomationService = RunAutomationServiceEnabled()
            self.AutomationService._deserialize(params.get("AutomationService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExistedInstance(AbstractModel):
    """Information of existing instances

    """

    def __init__(self):
        r"""
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
        :param IPv6Addresses: IPv6 address of the instance
Note: This field may return `null`, indicating that no valid values can be obtained.
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type IPv6Addresses: list of str
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
        self.IPv6Addresses = None


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
        self.IPv6Addresses = params.get("IPv6Addresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExistedInstancesForNode(AbstractModel):
    """Configuration parameters of existing nodes in different roles

    """

    def __init__(self):
        r"""
        :param NodeRole: Node role. Values: MASTER_ETCD, WORKER. You only need to specify MASTER_ETCD when creating a self-deployed cluster (INDEPENDENT_CLUSTER).
        :type NodeRole: str
        :param ExistedInstancesPara: Reinstallation parameter of existing instances
        :type ExistedInstancesPara: :class:`tencentcloud.tke.v20180525.models.ExistedInstancesPara`
        :param InstanceAdvancedSettingsOverride: Advanced node setting, which overrides the InstanceAdvancedSettings item set at the cluster level (currently valid for the ExtraArgs node custom parameter only)
        :type InstanceAdvancedSettingsOverride: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param DesiredPodNumbers: When the custom PodCIDR mode is enabled for the cluster, you can specify the maximum number of pods per node.
        :type DesiredPodNumbers: list of int
        """
        self.NodeRole = None
        self.ExistedInstancesPara = None
        self.InstanceAdvancedSettingsOverride = None
        self.DesiredPodNumbers = None


    def _deserialize(self, params):
        self.NodeRole = params.get("NodeRole")
        if params.get("ExistedInstancesPara") is not None:
            self.ExistedInstancesPara = ExistedInstancesPara()
            self.ExistedInstancesPara._deserialize(params.get("ExistedInstancesPara"))
        if params.get("InstanceAdvancedSettingsOverride") is not None:
            self.InstanceAdvancedSettingsOverride = InstanceAdvancedSettings()
            self.InstanceAdvancedSettingsOverride._deserialize(params.get("InstanceAdvancedSettingsOverride"))
        self.DesiredPodNumbers = params.get("DesiredPodNumbers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExistedInstancesPara(AbstractModel):
    """Reinstallation parameter of existing instances

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtensionAddon(AbstractModel):
    """Information of the add-on selected for installation during cluster creation

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForwardTKEEdgeApplicationRequestV3Request(AbstractModel):
    """ForwardTKEEdgeApplicationRequestV3 request structure.

    """

    def __init__(self):
        r"""
        :param Method: Access to request the cluster add-on
        :type Method: str
        :param Path: Path to request the cluster add-on
        :type Path: str
        :param Accept: Data format allowed to receive the requested cluster add-on
        :type Accept: str
        :param ContentType: Data format for requesting the cluster add-on
        :type ContentType: str
        :param RequestBody: Data sent to request the cluster add-on
        :type RequestBody: str
        :param ClusterName: Cluster name (for example, `cls-1234abcd`)
        :type ClusterName: str
        :param EncodedBody: Whether to encode the request content
        :type EncodedBody: str
        """
        self.Method = None
        self.Path = None
        self.Accept = None
        self.ContentType = None
        self.RequestBody = None
        self.ClusterName = None
        self.EncodedBody = None


    def _deserialize(self, params):
        self.Method = params.get("Method")
        self.Path = params.get("Path")
        self.Accept = params.get("Accept")
        self.ContentType = params.get("ContentType")
        self.RequestBody = params.get("RequestBody")
        self.ClusterName = params.get("ClusterName")
        self.EncodedBody = params.get("EncodedBody")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForwardTKEEdgeApplicationRequestV3Response(AbstractModel):
    """ForwardTKEEdgeApplicationRequestV3 response structure.

    """

    def __init__(self):
        r"""
        :param ResponseBody: Data returned after requesting the cluster add-on
        :type ResponseBody: str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ResponseBody = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResponseBody = params.get("ResponseBody")
        self.RequestId = params.get("RequestId")


class GPUArgs(AbstractModel):
    """GPU parameters, including GPU driver version, CDUA version, cuDNN version and whether to enable MIG.

    """

    def __init__(self):
        r"""
        :param MIGEnable: Whether to enable MIG
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type MIGEnable: bool
        :param Driver: GPU driver version
        :type Driver: :class:`tencentcloud.tke.v20180525.models.DriverVersion`
        :param CUDA: CUDA version
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CUDA: :class:`tencentcloud.tke.v20180525.models.DriverVersion`
        :param CUDNN: cuDNN version
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CUDNN: :class:`tencentcloud.tke.v20180525.models.CUDNN`
        :param CustomDriver: Custom GPU driver
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type CustomDriver: :class:`tencentcloud.tke.v20180525.models.CustomDriver`
        """
        self.MIGEnable = None
        self.Driver = None
        self.CUDA = None
        self.CUDNN = None
        self.CustomDriver = None


    def _deserialize(self, params):
        self.MIGEnable = params.get("MIGEnable")
        if params.get("Driver") is not None:
            self.Driver = DriverVersion()
            self.Driver._deserialize(params.get("Driver"))
        if params.get("CUDA") is not None:
            self.CUDA = DriverVersion()
            self.CUDA._deserialize(params.get("CUDA"))
        if params.get("CUDNN") is not None:
            self.CUDNN = CUDNN()
            self.CUDNN._deserialize(params.get("CUDNN"))
        if params.get("CustomDriver") is not None:
            self.CustomDriver = CustomDriver()
            self.CustomDriver._deserialize(params.get("CustomDriver"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetClusterLevelPriceRequest(AbstractModel):
    """GetClusterLevelPrice request structure.

    """

    def __init__(self):
        r"""
        :param ClusterLevel: The cluster model. It’s used for price query.
        :type ClusterLevel: str
        """
        self.ClusterLevel = None


    def _deserialize(self, params):
        self.ClusterLevel = params.get("ClusterLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetClusterLevelPriceResponse(AbstractModel):
    """GetClusterLevelPrice response structure.

    """

    def __init__(self):
        r"""
        :param Cost: Discount price (unit: US cent)
        :type Cost: int
        :param TotalCost: Original price (unit: US cent)
        :type TotalCost: int
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Cost = None
        self.TotalCost = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Cost = params.get("Cost")
        self.TotalCost = params.get("TotalCost")
        self.RequestId = params.get("RequestId")


class GetUpgradeInstanceProgressRequest(AbstractModel):
    """GetUpgradeInstanceProgress request structure.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetUpgradeInstanceProgressResponse(AbstractModel):
    """GetUpgradeInstanceProgress response structure.

    """

    def __init__(self):
        r"""
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


class IPAddress(AbstractModel):
    """IP Address

    """

    def __init__(self):
        r"""
        :param Type: Type. Valid values: `advertise`, `public`, and others
        :type Type: str
        :param Ip: IP Address
        :type Ip: str
        :param Port: Network port
        :type Port: int
        """
        self.Type = None
        self.Ip = None
        self.Port = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageInstance(AbstractModel):
    """Image details

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstallEdgeLogAgentRequest(AbstractModel):
    """InstallEdgeLogAgent request structure.

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
        


class InstallEdgeLogAgentResponse(AbstractModel):
    """InstallEdgeLogAgent response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """Cluster's instance information

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceAdvancedSettings(AbstractModel):
    """Describes K8s cluster configuration and related information.

    """

    def __init__(self):
        r"""
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
        :param DataDisks: Mounting information of multiple data disks. When you create a node, ensure that the CVM purchase parameter specifies the information required for the purchase of multiple data disks. For example, the `DataDisks` under `RunInstancesPara` of the `CreateClusterInstances` API should be configured accordingly (Referto document of CreateClusterInstances API). When you add an existing node, ensure that the specified partition exists in the node.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DataDisks: list of DataDisk
        :param ExtraArgs: Information about node custom parameters
Note: This field may return null, indicating that no valid value was found.
        :type ExtraArgs: :class:`tencentcloud.tke.v20180525.models.InstanceExtraArgs`
        :param DesiredPodNumber: When the custom PodCIDR mode is enabled for the cluster, you can specify the maximum number of pods per node.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DesiredPodNumber: int
        :param GPUArgs: GPU driver parameters
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type GPUArgs: :class:`tencentcloud.tke.v20180525.models.GPUArgs`
        :param PreStartUserScript: Specifies the base64-encoded custom script to be executed before initialization of the node. It’s only valid for adding existing nodes for now.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type PreStartUserScript: str
        :param Taints: Node taint
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type Taints: list of Taint
        """
        self.MountTarget = None
        self.DockerGraphPath = None
        self.UserScript = None
        self.Unschedulable = None
        self.Labels = None
        self.DataDisks = None
        self.ExtraArgs = None
        self.DesiredPodNumber = None
        self.GPUArgs = None
        self.PreStartUserScript = None
        self.Taints = None


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
        self.DesiredPodNumber = params.get("DesiredPodNumber")
        if params.get("GPUArgs") is not None:
            self.GPUArgs = GPUArgs()
            self.GPUArgs._deserialize(params.get("GPUArgs"))
        self.PreStartUserScript = params.get("PreStartUserScript")
        if params.get("Taints") is not None:
            self.Taints = []
            for item in params.get("Taints"):
                obj = Taint()
                obj._deserialize(item)
                self.Taints.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDataDiskMountSetting(AbstractModel):
    """Mounting configuration of the CVM instance data disk

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceExtraArgs(AbstractModel):
    """Node custom parameter

    """

    def __init__(self):
        r"""
        :param Kubelet: Kubelet custom parameter, in the format of ["k1=v1", "k1=v2"], for example: ["root-dir=/var/lib/kubelet","feature-gates=PodShareProcessNamespace=true,DynamicKubeletConfig=true"].
Note: this field may return `null`, indicating that no valid value is obtained.
        :type Kubelet: list of str
        """
        self.Kubelet = None


    def _deserialize(self, params):
        self.Kubelet = params.get("Kubelet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceUpgradeClusterStatus(AbstractModel):
    """Current status of the cluster during node upgrade

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceUpgradePreCheckResult(AbstractModel):
    """Pre-upgrade check result of a node

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceUpgradePreCheckResultItem(AbstractModel):
    """Check result for node upgrade

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceUpgradeProgressItem(AbstractModel):
    """Upgrade progress of a node

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Label(AbstractModel):
    """k8s tags, generally exist as an array

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginSettings(AbstractModel):
    """Describes login settings of an instance.

    """

    def __init__(self):
        r"""
        :param Password: Login password of the instance. <br><li>For Linux instances, the password must include 8-30 characters, and contain at least two of the following character sets: [a-z], [A-Z], [0-9] and [()\`~!@#$%^&*-+=|{}[]:;',.?/]. <br><li>For Windows instances, the password must include 12-30 characters, and contain at least three of the following character sets: [a-z], [A-Z], [0-9] and [()\`~!@#$%^&*-+=|{}[]:;',.?/]. <br><br>If it's not specified, the user needs to set the login password using the **Reset password** option in the CVM console or calling the API `ResetInstancesPassword` to complete the creation of the CVM instance(s).
Note: This field may return `null`, indicating that no valid values can be obtained.
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManuallyAdded(AbstractModel):
    """Nodes that are manually added

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterAsGroupAttributeRequest(AbstractModel):
    """ModifyClusterAsGroupAttribute request structure.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterAsGroupAttributeResponse(AbstractModel):
    """ModifyClusterAsGroupAttribute response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterAsGroupOptionAttributeResponse(AbstractModel):
    """ModifyClusterAsGroupOptionAttribute response structure.

    """

    def __init__(self):
        r"""
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
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param ProjectId: Project of the Cluster
        :type ProjectId: int
        :param ClusterName: Cluster name
        :type ClusterName: str
        :param ClusterDesc: Cluster description
        :type ClusterDesc: str
        :param ClusterLevel: Cluster specification
        :type ClusterLevel: str
        :param AutoUpgradeClusterLevel: Auto-upgrades cluster specification
        :type AutoUpgradeClusterLevel: :class:`tencentcloud.tke.v20180525.models.AutoUpgradeClusterLevel`
        :param QGPUShareEnable: Whether to enable qGPU Sharing
        :type QGPUShareEnable: bool
        """
        self.ClusterId = None
        self.ProjectId = None
        self.ClusterName = None
        self.ClusterDesc = None
        self.ClusterLevel = None
        self.AutoUpgradeClusterLevel = None
        self.QGPUShareEnable = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ProjectId = params.get("ProjectId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterDesc = params.get("ClusterDesc")
        self.ClusterLevel = params.get("ClusterLevel")
        if params.get("AutoUpgradeClusterLevel") is not None:
            self.AutoUpgradeClusterLevel = AutoUpgradeClusterLevel()
            self.AutoUpgradeClusterLevel._deserialize(params.get("AutoUpgradeClusterLevel"))
        self.QGPUShareEnable = params.get("QGPUShareEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterAttributeResponse(AbstractModel):
    """ModifyClusterAttribute response structure.

    """

    def __init__(self):
        r"""
        :param ProjectId: Project of the Cluster
Note: this field may return null, indicating that no valid values can be obtained.
        :type ProjectId: int
        :param ClusterName: Cluster name
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterName: str
        :param ClusterDesc: Cluster description
Note: this field may return null, indicating that no valid values can be obtained.
        :type ClusterDesc: str
        :param ClusterLevel: Cluster specification
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type ClusterLevel: str
        :param AutoUpgradeClusterLevel: Auto-upgrades cluster specification
Note: This field may return `null`, indicating that no valid values can be obtained.
        :type AutoUpgradeClusterLevel: :class:`tencentcloud.tke.v20180525.models.AutoUpgradeClusterLevel`
        :param QGPUShareEnable: Whether to enable qGPU Sharing
Note: This field may return `null`, indicating that no valid value can be obtained.
        :type QGPUShareEnable: bool
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.ProjectId = None
        self.ClusterName = None
        self.ClusterDesc = None
        self.ClusterLevel = None
        self.AutoUpgradeClusterLevel = None
        self.QGPUShareEnable = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterDesc = params.get("ClusterDesc")
        self.ClusterLevel = params.get("ClusterLevel")
        if params.get("AutoUpgradeClusterLevel") is not None:
            self.AutoUpgradeClusterLevel = AutoUpgradeClusterLevel()
            self.AutoUpgradeClusterLevel._deserialize(params.get("AutoUpgradeClusterLevel"))
        self.QGPUShareEnable = params.get("QGPUShareEnable")
        self.RequestId = params.get("RequestId")


class ModifyClusterAuthenticationOptionsRequest(AbstractModel):
    """ModifyClusterAuthenticationOptions request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param ServiceAccounts: ServiceAccount authentication configuration
        :type ServiceAccounts: :class:`tencentcloud.tke.v20180525.models.ServiceAccountAuthenticationOptions`
        """
        self.ClusterId = None
        self.ServiceAccounts = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("ServiceAccounts") is not None:
            self.ServiceAccounts = ServiceAccountAuthenticationOptions()
            self.ServiceAccounts._deserialize(params.get("ServiceAccounts"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterAuthenticationOptionsResponse(AbstractModel):
    """ModifyClusterAuthenticationOptions response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterEndpointSPRequest(AbstractModel):
    """ModifyClusterEndpointSP request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param SecurityPolicies: Security policy opens single IP or CIDR block to the Internet (for example: '192.168.1.0/24', with 'reject all' as the default).
        :type SecurityPolicies: list of str
        :param SecurityGroup: Modify public network security group
        :type SecurityGroup: str
        """
        self.ClusterId = None
        self.SecurityPolicies = None
        self.SecurityGroup = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SecurityPolicies = params.get("SecurityPolicies")
        self.SecurityGroup = params.get("SecurityGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterEndpointSPResponse(AbstractModel):
    """ModifyClusterEndpointSP response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        :param ExtraArgs: Node custom parameter
        :type ExtraArgs: :class:`tencentcloud.tke.v20180525.models.InstanceExtraArgs`
        :param Tags: Resource tag
        :type Tags: list of Tag
        :param Unschedulable: Sets whether the added node is schedulable. 0 (default): schedulable; other values: unschedulable. After node initialization is completed, you can run `kubectl uncordon nodename` to enable this node for scheduling.
        :type Unschedulable: int
        :param DeletionProtection: Whether Deletion Protection is enabled
        :type DeletionProtection: bool
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
        self.ExtraArgs = None
        self.Tags = None
        self.Unschedulable = None
        self.DeletionProtection = None


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
        if params.get("ExtraArgs") is not None:
            self.ExtraArgs = InstanceExtraArgs()
            self.ExtraArgs._deserialize(params.get("ExtraArgs"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Unschedulable = params.get("Unschedulable")
        self.DeletionProtection = params.get("DeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterNodePoolResponse(AbstractModel):
    """ModifyClusterNodePool response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNodePoolInstanceTypesRequest(AbstractModel):
    """ModifyNodePoolInstanceTypes request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param NodePoolId: Node pool ID
        :type NodePoolId: str
        :param InstanceTypes: List of instance types
        :type InstanceTypes: list of str
        """
        self.ClusterId = None
        self.NodePoolId = None
        self.InstanceTypes = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NodePoolId = params.get("NodePoolId")
        self.InstanceTypes = params.get("InstanceTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNodePoolInstanceTypesResponse(AbstractModel):
    """ModifyNodePoolInstanceTypes response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPrometheusAlertRuleRequest(AbstractModel):
    """ModifyPrometheusAlertRule request structure.

    """

    def __init__(self):
        r"""
        :param InstanceId: Instance ID
        :type InstanceId: str
        :param AlertRule: Alarm configurations
        :type AlertRule: :class:`tencentcloud.tke.v20180525.models.PrometheusAlertRuleDetail`
        """
        self.InstanceId = None
        self.AlertRule = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("AlertRule") is not None:
            self.AlertRule = PrometheusAlertRuleDetail()
            self.AlertRule._deserialize(params.get("AlertRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusAlertRuleResponse(AbstractModel):
    """ModifyPrometheusAlertRule response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodePool(AbstractModel):
    """Node pool description

    """

    def __init__(self):
        r"""
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
        :param Tags: Resource tag
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Tags: list of Tag
        :param DeletionProtection: Whether Deletion Protection is enabled
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type DeletionProtection: bool
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
        self.Tags = None
        self.DeletionProtection = None


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
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.DeletionProtection = params.get("DeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodePoolOption(AbstractModel):
    """The options for adding the existing node to the node pool

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodLimitsByType(AbstractModel):
    """The maximum number of Pods in VPC-CNI mode supported by a model

    """

    def __init__(self):
        r"""
        :param TKERouteENINonStaticIP: The number of Pods supported by a TKE shared ENI in non-static IP address mode
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type TKERouteENINonStaticIP: int
        :param TKERouteENIStaticIP: The number of Pods supported by a TKE shared ENI in static IP address mode
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type TKERouteENIStaticIP: int
        :param TKEDirectENI: The number of Pods supported by TKE independent ENI mode
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type TKEDirectENI: int
        """
        self.TKERouteENINonStaticIP = None
        self.TKERouteENIStaticIP = None
        self.TKEDirectENI = None


    def _deserialize(self, params):
        self.TKERouteENINonStaticIP = params.get("TKERouteENINonStaticIP")
        self.TKERouteENIStaticIP = params.get("TKERouteENIStaticIP")
        self.TKEDirectENI = params.get("TKEDirectENI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodLimitsInstance(AbstractModel):
    """The model information and the maximum supported number of Pods in the VPC-CNI mode

    """

    def __init__(self):
        r"""
        :param Zone: The availability zone where the model is located
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Zone: str
        :param InstanceFamily: The instance family to which the model belongs
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type InstanceFamily: str
        :param InstanceType: Instance type
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type InstanceType: str
        :param PodLimits: The maximum number of Pods in the VPC-CNI mode supported by the model
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type PodLimits: :class:`tencentcloud.tke.v20180525.models.PodLimitsByType`
        """
        self.Zone = None
        self.InstanceFamily = None
        self.InstanceType = None
        self.PodLimits = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceFamily = params.get("InstanceFamily")
        self.InstanceType = params.get("InstanceType")
        if params.get("PodLimits") is not None:
            self.PodLimits = PodLimitsByType()
            self.PodLimits._deserialize(params.get("PodLimits"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAlertRule(AbstractModel):
    """PROM instance alarm rule

    """

    def __init__(self):
        r"""
        :param Name: Rule name
        :type Name: str
        :param Rule: PromQL contents
        :type Rule: str
        :param Labels: Additional labels
        :type Labels: list of Label
        :param Template: Alarm delivery template
        :type Template: str
        :param For: Duration
        :type For: str
        :param Describe: Rule description
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Describe: str
        :param Annotations: Refer to annotations in prometheus rule
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Annotations: list of Label
        :param RuleState: Alarm rule status
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type RuleState: int
        """
        self.Name = None
        self.Rule = None
        self.Labels = None
        self.Template = None
        self.For = None
        self.Describe = None
        self.Annotations = None
        self.RuleState = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Rule = params.get("Rule")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        self.Template = params.get("Template")
        self.For = params.get("For")
        self.Describe = params.get("Describe")
        if params.get("Annotations") is not None:
            self.Annotations = []
            for item in params.get("Annotations"):
                obj = Label()
                obj._deserialize(item)
                self.Annotations.append(obj)
        self.RuleState = params.get("RuleState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAlertRuleDetail(AbstractModel):
    """The alarm configuration

    """

    def __init__(self):
        r"""
        :param Name: Rule name
        :type Name: str
        :param Rules: Rule list
        :type Rules: list of PrometheusAlertRule
        :param UpdatedAt: Last modification time
        :type UpdatedAt: str
        :param Notification: Alarm delivery methods
        :type Notification: :class:`tencentcloud.tke.v20180525.models.PrometheusNotification`
        :param Id: Alarm rule ID
        :type Id: str
        :param TemplateId: If the alarm is delivered via a template, the TemplateId is the template ID.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type TemplateId: str
        :param Interval: Alarm interval
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Interval: str
        """
        self.Name = None
        self.Rules = None
        self.UpdatedAt = None
        self.Notification = None
        self.Id = None
        self.TemplateId = None
        self.Interval = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = PrometheusAlertRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.UpdatedAt = params.get("UpdatedAt")
        if params.get("Notification") is not None:
            self.Notification = PrometheusNotification()
            self.Notification._deserialize(params.get("Notification"))
        self.Id = params.get("Id")
        self.TemplateId = params.get("TemplateId")
        self.Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusGrafanaInfo(AbstractModel):
    """The grafana information in the managed PROM instance

    """

    def __init__(self):
        r"""
        :param Enabled: Whether it is enabled
        :type Enabled: bool
        :param Domain: Domain name. It will be effective only when the public network access is enabled.
        :type Domain: str
        :param Address: The private network or public network address
        :type Address: str
        :param Internet: Whether the public network access is enabled.
`close`: the public network access is not enabled
`opening`: the public network access is being enabled
`open`: the public network access is enabled
        :type Internet: str
        :param AdminUser: The user name of the grafana admin
        :type AdminUser: str
        """
        self.Enabled = None
        self.Domain = None
        self.Address = None
        self.Internet = None
        self.AdminUser = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.Domain = params.get("Domain")
        self.Address = params.get("Address")
        self.Internet = params.get("Internet")
        self.AdminUser = params.get("AdminUser")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusNotification(AbstractModel):
    """amp alarm channel configuration

    """

    def __init__(self):
        r"""
        :param Enabled: Whether it is enabled
        :type Enabled: bool
        :param RepeatInterval: Convergence time
        :type RepeatInterval: str
        :param TimeRangeStart: Start time
        :type TimeRangeStart: str
        :param TimeRangeEnd: End time
        :type TimeRangeEnd: str
        :param NotifyWay: Alarm delivery method. Valid values: `SMS`, `EMAIL`, `CALL`, and `WECHAT`
It respectively represents SMS, email, phone calls, and WeChat.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type NotifyWay: list of str
        :param ReceiverGroups: The alarm recipient group (user group)
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type ReceiverGroups: list of int non-negative
        :param PhoneNotifyOrder: The alarm sequence of phone calls
This parameter is used when you specify `CALL` for `NotifyWay`.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type PhoneNotifyOrder: list of int non-negative
        :param PhoneCircleTimes: The number of phone call alarms
This parameter is used when you specify `CALL` for `NotifyWay`.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type PhoneCircleTimes: int
        :param PhoneInnerInterval: Dialing interval in seconds within one polling
This parameter is used when you specify `CALL` for `NotifyWay`.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type PhoneInnerInterval: int
        :param PhoneCircleInterval: Polling interval in seconds
This parameter is used when you specify `CALL` for `NotifyWay`.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type PhoneCircleInterval: int
        :param PhoneArriveNotice: Phone call alarm arrival notification
This parameter is used when you specify `CALL` for `NotifyWay`.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type PhoneArriveNotice: bool
        :param Type: Channel type. Default value: `amp`. The following channels are supported:
amp
webhook
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type Type: str
        :param WebHook: This parameter is required if `Type` is `webhook`.
Note: this field may return `null`, indicating that no valid value can be obtained.
        :type WebHook: str
        """
        self.Enabled = None
        self.RepeatInterval = None
        self.TimeRangeStart = None
        self.TimeRangeEnd = None
        self.NotifyWay = None
        self.ReceiverGroups = None
        self.PhoneNotifyOrder = None
        self.PhoneCircleTimes = None
        self.PhoneInnerInterval = None
        self.PhoneCircleInterval = None
        self.PhoneArriveNotice = None
        self.Type = None
        self.WebHook = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.RepeatInterval = params.get("RepeatInterval")
        self.TimeRangeStart = params.get("TimeRangeStart")
        self.TimeRangeEnd = params.get("TimeRangeEnd")
        self.NotifyWay = params.get("NotifyWay")
        self.ReceiverGroups = params.get("ReceiverGroups")
        self.PhoneNotifyOrder = params.get("PhoneNotifyOrder")
        self.PhoneCircleTimes = params.get("PhoneCircleTimes")
        self.PhoneInnerInterval = params.get("PhoneInnerInterval")
        self.PhoneCircleInterval = params.get("PhoneCircleInterval")
        self.PhoneArriveNotice = params.get("PhoneArriveNotice")
        self.Type = params.get("Type")
        self.WebHook = params.get("WebHook")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionInstance(AbstractModel):
    """Region information

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveNodeFromNodePoolRequest(AbstractModel):
    """RemoveNodeFromNodePool request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param NodePoolId: Node pool ID
        :type NodePoolId: str
        :param InstanceIds: The node ID list. Up to 100 nodes can be removed at a time.
        :type InstanceIds: list of str
        """
        self.ClusterId = None
        self.NodePoolId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NodePoolId = params.get("NodePoolId")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveNodeFromNodePoolResponse(AbstractModel):
    """RemoveNodeFromNodePool response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceUsage(AbstractModel):
    """Cluster resource usage

    """

    def __init__(self):
        r"""
        :param Name: Resource type
        :type Name: str
        :param Usage: Resource usage
        :type Usage: int
        :param Details: Resource usage details
        :type Details: list of ResourceUsageDetail
        """
        self.Name = None
        self.Usage = None
        self.Details = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Usage = params.get("Usage")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = ResourceUsageDetail()
                obj._deserialize(item)
                self.Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceUsageDetail(AbstractModel):
    """Resource usage details

    """

    def __init__(self):
        r"""
        :param Name: Resource name
        :type Name: str
        :param Usage: Resource usage
        :type Usage: int
        """
        self.Name = None
        self.Usage = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Usage = params.get("Usage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteInfo(AbstractModel):
    """Object of cluster route

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteTableConflict(AbstractModel):
    """Object of route table conflict

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteTableInfo(AbstractModel):
    """Object of cluster route table

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunAutomationServiceEnabled(AbstractModel):
    """Describes the TAT service information.

    """

    def __init__(self):
        r"""
        :param Enabled: Whether to enable the TAT service. Valid values: <br><li>`TRUE`: yes;<br><li>`FALSE`: no<br><br>Default: `FALSE`.
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesForNode(AbstractModel):
    """Node configuration parameters of different roles

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunMonitorServiceEnabled(AbstractModel):
    """Describes information related to the Cloud Monitor service.

    """

    def __init__(self):
        r"""
        :param Enabled: Whether to enable [Cloud Monitor](https://intl.cloud.tencent.com/document/product/248?from_cn_redirect=1). Valid values: <br><li>TRUE: enable Cloud Monitor <br><li>FALSE: do not enable Cloud Monitor <br><br>Default value: TRUE.
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunSecurityServiceEnabled(AbstractModel):
    """Describes information related to the Cloud Security service.

    """

    def __init__(self):
        r"""
        :param Enabled: Whether to enable [Cloud Security](https://intl.cloud.tencent.com/document/product/296?from_cn_redirect=1). Valid values: <br><li>TRUE: enable Cloud Security <br><li>FALSE: do not enable Cloud Security <br><br>Default value: TRUE.
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceAccountAuthenticationOptions(AbstractModel):
    """ServiceAccount authentication configuration

    """

    def __init__(self):
        r"""
        :param Issuer: service-account-issuer
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Issuer: str
        :param JWKSURI: service-account-jwks-uri
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type JWKSURI: str
        :param AutoCreateDiscoveryAnonymousAuth: If it is set to `true`, a RABC rule is automatically created to allow anonymous users to access `/.well-known/openid-configuration` and `/openid/v1/jwks`.
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type AutoCreateDiscoveryAnonymousAuth: bool
        """
        self.Issuer = None
        self.JWKSURI = None
        self.AutoCreateDiscoveryAnonymousAuth = None


    def _deserialize(self, params):
        self.Issuer = params.get("Issuer")
        self.JWKSURI = params.get("JWKSURI")
        self.AutoCreateDiscoveryAnonymousAuth = params.get("AutoCreateDiscoveryAnonymousAuth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetNodePoolNodeProtectionRequest(AbstractModel):
    """SetNodePoolNodeProtection request structure.

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param NodePoolId: Node pool ID
        :type NodePoolId: str
        :param InstanceIds: Node ID
        :type InstanceIds: list of str
        :param ProtectedFromScaleIn: Whether the node needs removal protection
        :type ProtectedFromScaleIn: bool
        """
        self.ClusterId = None
        self.NodePoolId = None
        self.InstanceIds = None
        self.ProtectedFromScaleIn = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NodePoolId = params.get("NodePoolId")
        self.InstanceIds = params.get("InstanceIds")
        self.ProtectedFromScaleIn = params.get("ProtectedFromScaleIn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetNodePoolNodeProtectionResponse(AbstractModel):
    """SetNodePoolNodeProtection response structure.

    """

    def __init__(self):
        r"""
        :param SucceedInstanceIds: ID of the node that has successfully set the removal protection
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type SucceedInstanceIds: list of str
        :param FailedInstanceIds: ID of the node that fails to set the removal protection
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type FailedInstanceIds: list of str
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.SucceedInstanceIds = None
        self.FailedInstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SucceedInstanceIds = params.get("SucceedInstanceIds")
        self.FailedInstanceIds = params.get("FailedInstanceIds")
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """The type of resource the label is bound to. Type currently supported is **cluster**.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagSpecification(AbstractModel):
    """List of tag descriptions. By specifying this parameter, you can bind tags to corresponding resource instances at the same time. Currently, only tags are bound to cloud host instances.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Taint(AbstractModel):
    """Kubernetes Taint

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskStepInfo(AbstractModel):
    """Task step information

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UninstallEdgeLogAgentRequest(AbstractModel):
    """UninstallEdgeLogAgent request structure.

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
        


class UninstallEdgeLogAgentResponse(AbstractModel):
    """UninstallEdgeLogAgent response structure.

    """

    def __init__(self):
        r"""
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateClusterVersionRequest(AbstractModel):
    """UpdateClusterVersion request structure.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateClusterVersionResponse(AbstractModel):
    """UpdateClusterVersion response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeClusterInstancesRequest(AbstractModel):
    """UpgradeClusterInstances request structure.

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeClusterInstancesResponse(AbstractModel):
    """UpgradeClusterInstances response structure.

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VersionInstance(AbstractModel):
    """Version Info

    """

    def __init__(self):
        r"""
        :param Name: Version name
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Name: str
        :param Version: Version Info
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Version: str
        :param Remark: Remark
Note: this field may return `null`, indicating that no valid values can be obtained.
        :type Remark: str
        """
        self.Name = None
        self.Version = None
        self.Remark = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Version = params.get("Version")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        