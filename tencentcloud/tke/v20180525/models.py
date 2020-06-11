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


class AddExistedInstancesRequest(AbstractModel):
    """AddExistedInstances request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param InstanceIds: Instance list
        :type InstanceIds: list of str
        :param InstanceAdvancedSettings: Additional parameter to be set for the instance
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param EnhancedService: Enhanced services. This parameter is used to specify whether to enable Cloud Security, Cloud Monitoring and other services. If this parameter is not specified, Cloud Monitor and Cloud Security are enabled by default.
        :type EnhancedService: :class:`tencentcloud.tke.v20180525.models.EnhancedService`
        :param LoginSettings: Node login information (currently only supports using Password or single KeyIds)
        :type LoginSettings: :class:`tencentcloud.tke.v20180525.models.LoginSettings`
        :param SecurityGroupIds: Security group to which the instance belongs. This parameter can be obtained from the `sgId` field returned by DescribeSecurityGroups. If this parameter is not specified, the default security group is bound. (Currently, you can only set a single sgId)
        :type SecurityGroupIds: list of str
        :param HostName: 
        :type HostName: str
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.InstanceAdvancedSettings = None
        self.EnhancedService = None
        self.LoginSettings = None
        self.SecurityGroupIds = None
        self.HostName = None


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
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.HostName = params.get("HostName")


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
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.FailedInstanceIds = None
        self.SuccInstanceIds = None
        self.TimeoutInstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailedInstanceIds = params.get("FailedInstanceIds")
        self.SuccInstanceIds = params.get("SuccInstanceIds")
        self.TimeoutInstanceIds = params.get("TimeoutInstanceIds")
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
        :param TagSpecification: 
        :type TagSpecification: list of TagSpecification
        :param ClusterStatus: 
        :type ClusterStatus: str
        :param Property: 
        :type Property: str
        :param ClusterMaterNodeNum: Number of master nodes currently in the cluster
        :type ClusterMaterNodeNum: int
        :param ImageId: ID of the image used by the cluster
Note: this field may return null, indicating that no valid value is obtained.
        :type ImageId: str
        :param OsCustomizeType: OsCustomizeType
Note: this field may return null, indicating that no valid value is obtained.
        :type OsCustomizeType: str
        :param ContainerRuntime: Runtime environment of the cluster. Values can be `docker` or `containerd`.
Note: this field may return null, indicating that no valid value is obtained.
        :type ContainerRuntime: str
        :param CreatedTime: Creation time
Note: this field may return null, indicating that no valid value is obtained.
        :type CreatedTime: str
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
        :param NodeNameType: 
        :type NodeNameType: str
        :param ExtraArgs: Cluster custom parameter
        :type ExtraArgs: :class:`tencentcloud.tke.v20180525.models.ClusterExtraArgs`
        :param NetworkType: Cluster network type, which can be GR (Global Router) or VPC-CNI. The default value is GR.
        :type NetworkType: str
        :param IsNonStaticIpMode: Whether a cluster in VPC-CNI mode uses dynamic IP addresses. The default value is FALSE, which indicates that static IP addresses are used.
        :type IsNonStaticIpMode: bool
        :param DeletionProtection: Indicates whether to enable deletion protection
        :type DeletionProtection: bool
        """
        self.IPVS = None
        self.AsEnabled = None
        self.ContainerRuntime = None
        self.NodeNameType = None
        self.ExtraArgs = None
        self.NetworkType = None
        self.IsNonStaticIpMode = None
        self.DeletionProtection = None


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
        :param TagSpecification: 
        :type TagSpecification: list of TagSpecification
        :param OsCustomizeType: 
        :type OsCustomizeType: str
        :param NeedWorkSecurityGroup: 
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
        :param ClusterCIDR: CIDR used to assign container and service IPs for the cluster. It cannot conflict with the VPC’s CIDR or the CIDRs of other clusters in the same VPC
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
        :param KubeAPIServer: kube-apiserver custom parameter
Note: this field may return null, indicating that no valid value is obtained.
        :type KubeAPIServer: list of str
        :param KubeControllerManager: kube-controller-manager custom parameter
Note: this field may return null, indicating that no valid value is obtained.
        :type KubeControllerManager: list of str
        :param KubeScheduler: kube-scheduler custom parameter
Note: this field may return null, indicating that no valid value is obtained.
        :type KubeScheduler: list of str
        """
        self.KubeAPIServer = None
        self.KubeControllerManager = None
        self.KubeScheduler = None


    def _deserialize(self, params):
        self.KubeAPIServer = params.get("KubeAPIServer")
        self.KubeControllerManager = params.get("KubeControllerManager")
        self.KubeScheduler = params.get("KubeScheduler")


class ClusterNetworkSettings(AbstractModel):
    """Cluster network-related parameters

    """

    def __init__(self):
        """
        :param ClusterCIDR: CIDR used to assign container and service IPs for the cluster. It cannot conflict with the VPC’s CIDR or the CIDRs of other clusters in the same VPC.
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


class CreateClusterAsGroupRequest(AbstractModel):
    """CreateClusterAsGroup request structure.

    """

    def __init__(self):
        """
        :param ClusterId: Cluster ID
        :type ClusterId: str
        :param AutoScalingGroupPara: The pass-through parameters for scaling group creation, in the format of a JSON string. For more information, see the [CreateAutoScalingGroup](https://cloud.tencent.com/document/api/377/20440) API. The **LaunchConfigurationId** is created with the LaunchConfigurePara parameter, which does not support data entry.
        :type AutoScalingGroupPara: str
        :param LaunchConfigurePara: The pass-through parameters for launch configuration creation, in the format of a JSON string. For more information, see the [CreateLaunchConfiguration](https://cloud.tencent.com/document/api/377/20447) API. **ImageId** is not required as it is already included in the cluster dimension. **UserData** is not required as it’s set through the **UserScript**.
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
        :param SubnetId: The ID of the subnet where the cluster’s port is located (only needs to be entered when the non-public network access is enabled, and must be within the subnet of the cluster’s VPC). 
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
        :param SecurityPolicies: Security policy opens single IP or CIDR to the Internet (for example: “192.168.1.0/24”, with “reject all” as the default).
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
        :param RequestFlowId: Request job’s FlowId
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
        :param RunInstancePara: Pass-through parameter for CVM creation in the format of a JSON string. For more information, see the [RunInstances](https://cloud.tencent.com/document/product/213/15730) API.
        :type RunInstancePara: str
        :param InstanceAdvancedSettings: Additional parameter to be set for the instance
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        """
        self.ClusterId = None
        self.RunInstancePara = None
        self.InstanceAdvancedSettings = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RunInstancePara = params.get("RunInstancePara")
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))


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


class CreateClusterRequest(AbstractModel):
    """CreateCluster request structure.

    """

    def __init__(self):
        """
        :param ClusterCIDRSettings: Container networking configuration information for the cluster
        :type ClusterCIDRSettings: :class:`tencentcloud.tke.v20180525.models.ClusterCIDRSettings`
        :param ClusterType: Cluster type. Managed cluster: MANAGED_CLUSTER; self-deployed cluster: INDEPENDENT_CLUSTER.
        :type ClusterType: str
        :param RunInstancesForNode: Pass-through parameter for CVM creation in the format of a JSON string. For more information, see the API for [creating a CVM instance](https://cloud.tencent.com/document/product/213/15730).
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
        """
        self.ClusterCIDRSettings = None
        self.ClusterType = None
        self.RunInstancesForNode = None
        self.ClusterBasicSettings = None
        self.ClusterAdvancedSettings = None
        self.InstanceAdvancedSettings = None
        self.ExistedInstancesForNode = None
        self.InstanceDataDiskMountSettings = None


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
        :param ClusterId: The cluster ID, obtained through the [DescribeClusters](https://cloud.tencent.com/document/api/457/31862) API.
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
        :param ForceDelete: 
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
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
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
        :param InstanceRole: 
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
        """
        self.RouteTableName = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")


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
        :param UserName: Cluster’s account name
        :type UserName: str
        :param Password: Cluster’s password
        :type Password: str
        :param CertificationAuthority: Cluster’s access CA certificate
        :type CertificationAuthority: str
        :param ClusterExternalEndpoint: Cluster’s access address
        :type ClusterExternalEndpoint: str
        :param Domain: Domain name accessed by the cluster
        :type Domain: str
        :param PgwEndpoint: Cluster’s endpoint address
        :type PgwEndpoint: str
        :param SecurityPolicy: Cluster’s access policy group
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
        :param InstanceIds: Query by one or more instance ID(s). Instance ID format: ins-xxxxxxxx. (Refer to section ID.N of the API overview for this parameter’s specific format.) Up to 100 instances are allowed for each request. You cannot specify InstanceIds and Filters at the same time.
        :type InstanceIds: list of str
        :param Filters: Filter condition. For fields and other information, see [the DescribeInstances API](https://cloud.tencent.com/document/api/213/15728). If a ClusterId has been set, then the cluster’s VPC ID will be attached as a query field. In this situation, if a "vpc-id" is specified in Filter, then the specified VPC ID must be consistent with the cluster’s VPC ID.
        :type Filters: list of Filter
        :param VagueIpAddress: Filter by instance IP (Supports both private and public IPs)
        :type VagueIpAddress: str
        :param VagueInstanceName: Filter by instance name
        :type VagueInstanceName: str
        :param Offset: Offset. Default value: 0. For more information on Offset, see the relevant section in the API [Introduction](https://cloud.tencent.com/document/api/213/15688).
        :type Offset: int
        :param Limit: Number of returned results. Default value: 20. Maximum value: 100. For more information on Limit, see the relevant section in the API [Introduction](https://cloud.tencent.com/document/api/213/15688).
        :type Limit: int
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.Filters = None
        self.VagueIpAddress = None
        self.VagueInstanceName = None
        self.Offset = None
        self.Limit = None


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
        :param PrivateIpAddresses: List of private IPs of the instance’s primary ENI.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PrivateIpAddresses: list of str
        :param PublicIpAddresses: List of public IPs of the instance’s primary ENI.
Note: This field may return null, indicating that no valid values can be obtained.
        :type PublicIpAddresses: list of str
        :param CreatedTime: Creation time, which follows the ISO8601 standard and uses UTC time. Format: YYYY-MM-DDThh:mm:ssZ.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CreatedTime: str
        :param CPU: Instance’s number of CPU cores. Unit: cores.
Note: This field may return null, indicating that no valid values can be obtained.
        :type CPU: int
        :param Memory: Instance’s memory capacity. Unit: GB.
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
        :param HostName: 
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


class Filter(AbstractModel):
    """> Key-value pair filters used for conditional queries, such as filtering results by ID, name, and state.
    > * If there are multiple `Filter` parameters, they are evaluated using the logical `AND` operator.
    > * If a `Filter` contains multiple `Values`, they are evaluated using the logical `OR` operator.
    >
    > Take [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) as an example. You can use the following filters to query the instances in availability zone (`zone`) Guangzhou Zone 1 ***and*** whose billing plan (`instance-charge-type`) is pay-as-you-go:
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
    """Cluster’s instance information

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
        :param MountTarget: Data disk mount point. By default, no data disk is mounted. Data disks in ext3, ext4, or XFS file system formats will be mounted directly, while data disks in other file systems and unformatted data disks will automatically be formatted as ext4 and then mounted. Please back up your data in advance. This setting is only applicable to CVMs with a single data disk.
Note: This field may return null, indicating that no valid value was found.
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
        :param DataDisks: Data disk information
Note: This field may return null, indicating that no valid value was found.
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
        :param Kubelet: Kubelet custom parameter
Note: this field may return null, indicating that no valid value is obtained.
        :type Kubelet: list of str
        """
        self.Kubelet = None


    def _deserialize(self, params):
        self.Kubelet = params.get("Kubelet")


class Label(AbstractModel):
    """k8s tags, generally exist as an array

    """

    def __init__(self):
        """
        :param Name: 
        :type Name: str
        :param Value: 
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
        :param KeyIds: List of key IDs. After an instance is associated with a key, you can access the instance with the private key in the key pair. You can call [`DescribeKeyPairs`](https://cloud.tencent.com/document/api/213/15699) to obtain `KeyId`. A key and password cannot be specified at the same time. Windows instances do not support keys. Currently, you can only specify one key when purchasing an instance.
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
        :param SecurityPolicies: Security policy opens single IP or CIDR block to the Internet (for example: “192.168.1.0/24”, with “reject all” as the default).
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
        :param RunInstancesPara: Pass-through parameter for CVM creation in the format of a JSON string. For more information, see the API for [creating a CVM instance](https://cloud.tencent.com/document/product/213/15730). Pass any parameter other than common parameters. ImageId will be replaced with the image corresponding to the TKE cluster operating system.
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
        :param Enabled: Whether to enable [Cloud Monitor](/document/product/248). Valid values: <br><li>TRUE: enable Cloud Monitor <br><li>FALSE: do not enable Cloud Monitor <br><br>Default value: TRUE.
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
        :param Enabled: Whether to enable [Cloud Security](/document/product/296). Valid values: <br><li>TRUE: enable Cloud Security <br><li>FALSE: do not enable Cloud Security <br><br>Default value: TRUE.
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")


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
        :param ResourceType: 
        :type ResourceType: str
        :param Tags: 
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