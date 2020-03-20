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
        :type FailedInstanceIds: list of str
        :param SuccInstanceIds: IDs of successful nodes
        :type SuccInstanceIds: list of str
        :param TimeoutInstanceIds: IDs of (successful or failed) nodes that timed out
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
        """
        self.IPVS = None
        self.AsEnabled = None
        self.ContainerRuntime = None
        self.NodeNameType = None


    def _deserialize(self, params):
        self.IPVS = params.get("IPVS")
        self.AsEnabled = params.get("AsEnabled")
        self.ContainerRuntime = params.get("ContainerRuntime")
        self.NodeNameType = params.get("NodeNameType")


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
        """
        self.ClusterCIDR = None
        self.IgnoreClusterCIDRConflict = None
        self.MaxNodePodNum = None
        self.MaxClusterServiceNum = None


    def _deserialize(self, params):
        self.ClusterCIDR = params.get("ClusterCIDR")
        self.IgnoreClusterCIDRConflict = params.get("IgnoreClusterCIDRConflict")
        self.MaxNodePodNum = params.get("MaxNodePodNum")
        self.MaxClusterServiceNum = params.get("MaxClusterServiceNum")


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


class CreateClusterAsGroupResponse(AbstractModel):
    """CreateClusterAsGroup response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateClusterEndpointRequest(AbstractModel):
    """CreateClusterEndpoint request structure.

    """


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


class CreateClusterEndpointVipResponse(AbstractModel):
    """CreateClusterEndpointVip response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
        :param InstanceDataDiskMountSettings: 
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


class DeleteClusterAsGroupsRequest(AbstractModel):
    """DeleteClusterAsGroups request structure.

    """


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
        """
        self.ClusterId = None
        self.InstanceDeleteMode = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceDeleteMode = params.get("InstanceDeleteMode")


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


class DescribeClusterEndpointStatusResponse(AbstractModel):
    """DescribeClusterEndpointStatus response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeClusterEndpointVipStatusRequest(AbstractModel):
    """DescribeClusterEndpointVipStatus request structure.

    """


class DescribeClusterEndpointVipStatusResponse(AbstractModel):
    """DescribeClusterEndpointVipStatus response structure.

    """

    def __init__(self):
        """
        :param RequestId: The unique request ID, which is returned for each request. RequestId is required for locating a problem.
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
        :type SecurityPolicy: list of str
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
        self.RequestId = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        self.CertificationAuthority = params.get("CertificationAuthority")
        self.ClusterExternalEndpoint = params.get("ClusterExternalEndpoint")
        self.Domain = params.get("Domain")
        self.PgwEndpoint = params.get("PgwEndpoint")
        self.SecurityPolicy = params.get("SecurityPolicy")
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
        :param InstanceChargeType: Instance’s billing mode. Value range:
PREPAID: Prepaid (Monthly Subscription)
POSTPAID_BY_HOUR: Postpaid (Pay-as-you-go)
CDHPAID: CDH-paid. Only CDH is charged and instances on the CDH do not incur fees.
Note: This field may return null, indicating that no valid values can be obtained.
        :type InstanceChargeType: str
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
        """
        self.Usable = None
        self.UnusableReason = None
        self.AlreadyInCluster = None
        self.InstanceId = None
        self.InstanceName = None
        self.PrivateIpAddresses = None
        self.PublicIpAddresses = None
        self.CreatedTime = None
        self.InstanceChargeType = None
        self.CPU = None
        self.Memory = None
        self.OsName = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.Usable = params.get("Usable")
        self.UnusableReason = params.get("UnusableReason")
        self.AlreadyInCluster = params.get("AlreadyInCluster")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.CreatedTime = params.get("CreatedTime")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.OsName = params.get("OsName")
        self.InstanceType = params.get("InstanceType")


class ExistedInstancesForNode(AbstractModel):
    """Configuration parameters of existing nodes in different roles

    """

    def __init__(self):
        """
        :param NodeRole: Node role. Values: MASTER_ETCD, WORKER. You only need to specify MASTER_ETCD when creating a self-deployed cluster (INDEPENDENT_CLUSTER).
        :type NodeRole: str
        :param ExistedInstancesPara: Reinstallation parameter of existing instances
        :type ExistedInstancesPara: :class:`tencentcloud.tke.v20180525.models.ExistedInstancesPara`
        """
        self.NodeRole = None
        self.ExistedInstancesPara = None


    def _deserialize(self, params):
        self.NodeRole = params.get("NodeRole")
        if params.get("ExistedInstancesPara") is not None:
            self.ExistedInstancesPara = ExistedInstancesPara()
            self.ExistedInstancesPara._deserialize(params.get("ExistedInstancesPara"))


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
    """Filter

    """

    def __init__(self):
        """
        :param Name: Attribute name. If more than one Filter exists, the logical relationship between these Filters is AND.
        :type Name: str
        :param Values: Attribute value. If there are multiple Values for one Filter, the logical relationship between the Values under the same Filter is OR.
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


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
        """
        self.InstanceId = None
        self.InstanceRole = None
        self.FailedReason = None
        self.InstanceState = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceRole = params.get("InstanceRole")
        self.FailedReason = params.get("FailedReason")
        self.InstanceState = params.get("InstanceState")


class InstanceAdvancedSettings(AbstractModel):
    """Describes K8s cluster configuration and related information.

    """

    def __init__(self):
        """
        :param MountTarget: Data disk mount point. By default, no data disk is mounted. Data disks in ext3, ext4, or XFS file system formats will be mounted directly, while data disks in other file systems and unformatted data disks will automatically be formatted as ext4 and then mounted. Please back up your data in advance. This setting is only applicable to CVMs with a single data disk.
        :type MountTarget: str
        :param DockerGraphPath: Specified value of dockerd --graph. Default value: /var/lib/docker
        :type DockerGraphPath: str
        :param UserScript: Base64-encoded user script, which will be executed after the K8s component starts running. You need to ensure the reentrant and retry logic of the script. The script and its log files can be viewed at the node path: /data/ccs_userscript/. If you want to initialize nodes before adding them to the scheduling list, you can use this parameter together with the unschedulable parameter. After the final initialization of userScript is completed, add the kubectl uncordon nodename --kubeconfig=/root/.kube/config command to enable the node for scheduling.
        :type UserScript: str
        :param Unschedulable: Sets whether the added node is schedulable. 0 (default): schedulable; other values: unschedulable. After node initialization is completed, you can run kubectl uncordon nodename to enable this node for scheduling.
        :type Unschedulable: int
        :param Labels: 
        :type Labels: list of Label
        :param DataDisks: 
        :type DataDisks: list of DataDisk
        """
        self.MountTarget = None
        self.DockerGraphPath = None
        self.UserScript = None
        self.Unschedulable = None
        self.Labels = None
        self.DataDisks = None


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


class InstanceDataDiskMountSetting(AbstractModel):
    """CVM instance data disk mount configuration

    """


class Label(AbstractModel):
    """k8s tags, generally exist as an array

    """


class LoginSettings(AbstractModel):
    """Describes login settings of an instance.

    """

    def __init__(self):
        """
        :param Password: Login password of the instance. The password requirements vary among different operating systems: <br><li>For Linux instances, the password must be 8-16 characters long and contain at least one character from two of the following categories: [a-z, A-Z], [0-9] and [( ) ` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? / ]. <br><li>For Windows instances, the password must be 12-16 characters long and contain at least one character from three of the following categories: [a-z], [A-Z], [0-9] and [( ) ` ~ ! @ # $ % ^ & * - + = { } [ ] : ; ' , . ? /]. <br><br>If this parameter is not specified, a random password will be generated and sent to you via the Message Center.
Note: This field may return null, indicating that no valid value is found.
        :type Password: str
        :param KeyIds: List of key IDs. After an instance is associated with a key, you can access the instance with the private key in the key pair. You can call `DescribeKeyPairs` to obtain `KeyId`. Key and password cannot be specified at the same time. Windows instances do not support keys. Currently, you can only specify one key when purchasing an instance.
Note: This field may return null, indicating that no valid value is found.
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


class ModifyClusterEndpointSPRequest(AbstractModel):
    """ModifyClusterEndpointSP request structure.

    """


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
        """
        self.NodeRole = None
        self.RunInstancesPara = None


    def _deserialize(self, params):
        self.NodeRole = params.get("NodeRole")
        self.RunInstancesPara = params.get("RunInstancesPara")


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


class TagSpecification(AbstractModel):
    """List of tag descriptions. By specifying this parameter, you can bind tags to corresponding resource instances at the same time. Currently, only tags are bound to cloud host instances.

    """