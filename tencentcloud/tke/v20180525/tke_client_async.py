# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.tke.v20180525 import models
from typing import Dict


class TkeClient(AbstractClient):
    _apiVersion = '2018-05-25'
    _endpoint = 'tke.intl.tencentcloudapi.com'
    _service = 'tke'

    async def AcquireClusterAdminRole(
            self,
            request: models.AcquireClusterAdminRoleRequest,
            opts: Dict = None,
    ) -> models.AcquireClusterAdminRoleResponse:
        """
        This API can be called to acquire the ClusterRole tke:admin. By setting a CAM policy, you can grant permission of this API to a sub-account that has higher permission in CAM. In this way, this sub-account can call this API directly to acquire the admin role of a Kubernetes cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "AcquireClusterAdminRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AcquireClusterAdminRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddExistedInstances(
            self,
            request: models.AddExistedInstancesRequest,
            opts: Dict = None,
    ) -> models.AddExistedInstancesResponse:
        """
        This API is used to add one or more existing instances to a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "AddExistedInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddExistedInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddNodeToNodePool(
            self,
            request: models.AddNodeToNodePoolRequest,
            opts: Dict = None,
    ) -> models.AddNodeToNodePoolResponse:
        """
        This API is used to move nodes in a cluster to a node pool.
        """
        
        kwargs = {}
        kwargs["action"] = "AddNodeToNodePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddNodeToNodePoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddVpcCniSubnets(
            self,
            request: models.AddVpcCniSubnetsRequest,
            opts: Dict = None,
    ) -> models.AddVpcCniSubnetsResponse:
        """
        This API is used to add subnets in the container network for a VPC-CNI cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "AddVpcCniSubnets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddVpcCniSubnetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckEdgeClusterCIDR(
            self,
            request: models.CheckEdgeClusterCIDRRequest,
            opts: Dict = None,
    ) -> models.CheckEdgeClusterCIDRResponse:
        """
        This API is used to check if the CIDR block of a TKE Edge cluster conflicts with other CIDR blocks.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckEdgeClusterCIDR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckEdgeClusterCIDRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckInstancesUpgradeAble(
            self,
            request: models.CheckInstancesUpgradeAbleRequest,
            opts: Dict = None,
    ) -> models.CheckInstancesUpgradeAbleResponse:
        """
        This API is used to query nodes eligible for an upgrade in the given node list.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckInstancesUpgradeAble"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckInstancesUpgradeAbleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBackupStorageLocation(
            self,
            request: models.CreateBackupStorageLocationRequest,
            opts: Dict = None,
    ) -> models.CreateBackupStorageLocationResponse:
        """
        This API is used to create a backup repository. You can specify the storage type (such as COS), the bucket region and the name. Up to 100 repositories can be created. Note that the settings of this API apply globally. You only need to create one backup repository, and back up TKE clusters in different regions in it.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackupStorageLocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackupStorageLocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCLSLogConfig(
            self,
            request: models.CreateCLSLogConfigRequest,
            opts: Dict = None,
    ) -> models.CreateCLSLogConfigResponse:
        """
        This API is used to create log collection configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCLSLogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCLSLogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCluster(
            self,
            request: models.CreateClusterRequest,
            opts: Dict = None,
    ) -> models.CreateClusterResponse:
        """
        This API is used to create a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterEndpoint(
            self,
            request: models.CreateClusterEndpointRequest,
            opts: Dict = None,
    ) -> models.CreateClusterEndpointResponse:
        """
        This API is used to create a cluster access endpoint.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterEndpointVip(
            self,
            request: models.CreateClusterEndpointVipRequest,
            opts: Dict = None,
    ) -> models.CreateClusterEndpointVipResponse:
        """
        This API is used to create a public network access port for a managed cluster. Note: This API will be disused soon. Please call `CreateClusterEndpoint` instead.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterEndpointVip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterEndpointVipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterInstances(
            self,
            request: models.CreateClusterInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateClusterInstancesResponse:
        """
        This API is used to create one or more nodes in a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterNodePool(
            self,
            request: models.CreateClusterNodePoolRequest,
            opts: Dict = None,
    ) -> models.CreateClusterNodePoolResponse:
        """
        This API is used to create a node pool.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterNodePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterNodePoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterRouteTable(
            self,
            request: models.CreateClusterRouteTableRequest,
            opts: Dict = None,
    ) -> models.CreateClusterRouteTableResponse:
        """
        This API is used to create a cluster route table.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterRouteTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterRouteTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterVirtualNode(
            self,
            request: models.CreateClusterVirtualNodeRequest,
            opts: Dict = None,
    ) -> models.CreateClusterVirtualNodeResponse:
        """
        This API is used to create the Pay-as-you-go Super Node.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterVirtualNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterVirtualNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterVirtualNodePool(
            self,
            request: models.CreateClusterVirtualNodePoolRequest,
            opts: Dict = None,
    ) -> models.CreateClusterVirtualNodePoolResponse:
        """
        This API is used to create the Super Node Pool.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterVirtualNodePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterVirtualNodePoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateECMInstances(
            self,
            request: models.CreateECMInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateECMInstancesResponse:
        """
        This API is used to create an ECM instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateECMInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateECMInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEdgeCVMInstances(
            self,
            request: models.CreateEdgeCVMInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateEdgeCVMInstancesResponse:
        """
        This API is used to create CVM instances in the specified TKE edge cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEdgeCVMInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEdgeCVMInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEdgeLogConfig(
            self,
            request: models.CreateEdgeLogConfigRequest,
            opts: Dict = None,
    ) -> models.CreateEdgeLogConfigResponse:
        """
        This API is used to create log collection configuration for a TKE Edge cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEdgeLogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEdgeLogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEksLogConfig(
            self,
            request: models.CreateEksLogConfigRequest,
            opts: Dict = None,
    ) -> models.CreateEksLogConfigResponse:
        """
        This API is used to create Log Collection Configuration for Elastic Cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEksLogConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEksLogConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrometheusAlertRule(
            self,
            request: models.CreatePrometheusAlertRuleRequest,
            opts: Dict = None,
    ) -> models.CreatePrometheusAlertRuleResponse:
        """
        This API is used to create an alarm rule.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrometheusAlertRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrometheusAlertRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTKEEdgeCluster(
            self,
            request: models.CreateTKEEdgeClusterRequest,
            opts: Dict = None,
    ) -> models.CreateTKEEdgeClusterResponse:
        """
        This API is used to create a TKE Edge cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTKEEdgeCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTKEEdgeClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAddon(
            self,
            request: models.DeleteAddonRequest,
            opts: Dict = None,
    ) -> models.DeleteAddonResponse:
        """
        This API is used to delete an add-on.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAddon"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAddonResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBackupStorageLocation(
            self,
            request: models.DeleteBackupStorageLocationRequest,
            opts: Dict = None,
    ) -> models.DeleteBackupStorageLocationResponse:
        """
        This API is used to delete a backup repository.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBackupStorageLocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBackupStorageLocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCluster(
            self,
            request: models.DeleteClusterRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterResponse:
        """
        This API is used to delete a cluster. (Cloud API v3).
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterAsGroups(
            self,
            request: models.DeleteClusterAsGroupsRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterAsGroupsResponse:
        """
        Delete a cluster scaling group
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterAsGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterAsGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterEndpoint(
            self,
            request: models.DeleteClusterEndpointRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterEndpointResponse:
        """
        This API is used to delete a cluster access endpoint.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterEndpoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterEndpointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterEndpointVip(
            self,
            request: models.DeleteClusterEndpointVipRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterEndpointVipResponse:
        """
        Delete the external network access port of the managed cluster (the old way, only the external network port of the managed cluster is supported)
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterEndpointVip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterEndpointVipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterInstances(
            self,
            request: models.DeleteClusterInstancesRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterInstancesResponse:
        """
        This API is used to delete one or more nodes from a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterNodePool(
            self,
            request: models.DeleteClusterNodePoolRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterNodePoolResponse:
        """
        This API is used to delete a node pool.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterNodePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterNodePoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterRoute(
            self,
            request: models.DeleteClusterRouteRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterRouteResponse:
        """
        This API is used to delete a cluster route.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterRouteTable(
            self,
            request: models.DeleteClusterRouteTableRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterRouteTableResponse:
        """
        This API is used to delete cluster a route table.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterRouteTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterRouteTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterVirtualNode(
            self,
            request: models.DeleteClusterVirtualNodeRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterVirtualNodeResponse:
        """
        This API is used to delete the super node.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterVirtualNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterVirtualNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterVirtualNodePool(
            self,
            request: models.DeleteClusterVirtualNodePoolRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterVirtualNodePoolResponse:
        """
        This API is used to delete the Super Node Pool.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterVirtualNodePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterVirtualNodePoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteECMInstances(
            self,
            request: models.DeleteECMInstancesRequest,
            opts: Dict = None,
    ) -> models.DeleteECMInstancesResponse:
        """
        This API is used to delete one or more ECM instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteECMInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteECMInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEdgeCVMInstances(
            self,
            request: models.DeleteEdgeCVMInstancesRequest,
            opts: Dict = None,
    ) -> models.DeleteEdgeCVMInstancesResponse:
        """
        This API is used to delete one or more edge CVM instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEdgeCVMInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEdgeCVMInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEdgeClusterInstances(
            self,
            request: models.DeleteEdgeClusterInstancesRequest,
            opts: Dict = None,
    ) -> models.DeleteEdgeClusterInstancesResponse:
        """
        This API is used to delete one or more edge compute instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEdgeClusterInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEdgeClusterInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLogConfigs(
            self,
            request: models.DeleteLogConfigsRequest,
            opts: Dict = None,
    ) -> models.DeleteLogConfigsResponse:
        """
        This API is used to delete collection rules within the cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLogConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLogConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrometheusAlertRule(
            self,
            request: models.DeletePrometheusAlertRuleRequest,
            opts: Dict = None,
    ) -> models.DeletePrometheusAlertRuleResponse:
        """
        This API is used to delete an alarm rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrometheusAlertRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrometheusAlertRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTKEEdgeCluster(
            self,
            request: models.DeleteTKEEdgeClusterRequest,
            opts: Dict = None,
    ) -> models.DeleteTKEEdgeClusterResponse:
        """
        This API is used to delete a TKE Edge cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTKEEdgeCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTKEEdgeClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddon(
            self,
            request: models.DescribeAddonRequest,
            opts: Dict = None,
    ) -> models.DescribeAddonResponse:
        """
        This API is used to query the list of add-ons.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddon"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddonResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddonValues(
            self,
            request: models.DescribeAddonValuesRequest,
            opts: Dict = None,
    ) -> models.DescribeAddonValuesResponse:
        """
        This API is used to query parameters of an add-on.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddonValues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddonValuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAvailableClusterVersion(
            self,
            request: models.DescribeAvailableClusterVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeAvailableClusterVersionResponse:
        """
        This API is used to obtain all versions that the cluster can upgrade to.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAvailableClusterVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAvailableClusterVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAvailableTKEEdgeVersion(
            self,
            request: models.DescribeAvailableTKEEdgeVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeAvailableTKEEdgeVersionResponse:
        """
        This API is used to check the edge component versions and K8s versions supported by TKE Edge.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAvailableTKEEdgeVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAvailableTKEEdgeVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupStorageLocations(
            self,
            request: models.DescribeBackupStorageLocationsRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupStorageLocationsResponse:
        """
        This API is used to query backup repositories.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupStorageLocations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupStorageLocationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBatchModifyTagsStatus(
            self,
            request: models.DescribeBatchModifyTagsStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeBatchModifyTagsStatusResponse:
        """
        This API is used to query batch modification Tag status.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBatchModifyTagsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBatchModifyTagsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterAsGroupOption(
            self,
            request: models.DescribeClusterAsGroupOptionRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterAsGroupOptionResponse:
        """
        Cluster auto scaling configuration
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterAsGroupOption"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterAsGroupOptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterAsGroups(
            self,
            request: models.DescribeClusterAsGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterAsGroupsResponse:
        """
        Cluster-associated scaling group list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterAsGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterAsGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterAuthenticationOptions(
            self,
            request: models.DescribeClusterAuthenticationOptionsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterAuthenticationOptionsResponse:
        """
        This API is used to query cluster authentication configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterAuthenticationOptions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterAuthenticationOptionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterCommonNames(
            self,
            request: models.DescribeClusterCommonNamesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterCommonNamesResponse:
        """
        This API is used to obtain the CommonName from the kube-apiserver client certificate that corresponding to the sub-account in RBAC authorization mode.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterCommonNames"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterCommonNamesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterEndpointStatus(
            self,
            request: models.DescribeClusterEndpointStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterEndpointStatusResponse:
        """
        Query cluster access port status (intranet / extranet access is enabled for independent clusters, and intranet access is supported for managed clusters)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterEndpointStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterEndpointStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterEndpointVipStatus(
            self,
            request: models.DescribeClusterEndpointVipStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterEndpointVipStatusResponse:
        """
        Query cluster open port process status (only supports external ports of the managed cluster)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterEndpointVipStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterEndpointVipStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterEndpoints(
            self,
            request: models.DescribeClusterEndpointsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterEndpointsResponse:
        """
        This API is used to query cluster access addresses, including private network address, public network address, public network domain name, and security policy for public network access.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterEndpoints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterEndpointsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterExtraArgs(
            self,
            request: models.DescribeClusterExtraArgsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterExtraArgsResponse:
        """
        This API is used to query custom parameters of a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterExtraArgs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterExtraArgsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterInstances(
            self,
            request: models.DescribeClusterInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterInstancesResponse:
        """
        This API is used to query information of node instances in a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterKubeconfig(
            self,
            request: models.DescribeClusterKubeconfigRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterKubeconfigResponse:
        """
        This API is used to obtain the cluster kubeconfig file. Different sub-accounts have their own kubeconfig files. The kubeconfig file contains the kube-apiserver client certificate of the corresponding sub-account. By default, the client certificate is created when this API is called for the first time, and the certificate is valid for 20 years with no permissions granted. For the cluster owner or primary account, the cluster-admin permission is granted by default.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterKubeconfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterKubeconfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterLevelAttribute(
            self,
            request: models.DescribeClusterLevelAttributeRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterLevelAttributeResponse:
        """
        This API is used to obtain the cluster model.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterLevelAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterLevelAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterLevelChangeRecords(
            self,
            request: models.DescribeClusterLevelChangeRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterLevelChangeRecordsResponse:
        """
        This API is used to query the cluster model adjustment history.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterLevelChangeRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterLevelChangeRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterNodePoolDetail(
            self,
            request: models.DescribeClusterNodePoolDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterNodePoolDetailResponse:
        """
        This API is used to query detailed information of a node pool.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterNodePoolDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterNodePoolDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterNodePools(
            self,
            request: models.DescribeClusterNodePoolsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterNodePoolsResponse:
        """
        This API is used to query the node pool list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterNodePools"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterNodePoolsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterRouteTables(
            self,
            request: models.DescribeClusterRouteTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterRouteTablesResponse:
        """
        This API is used to query one or more cluster route tables.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterRouteTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterRouteTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterRoutes(
            self,
            request: models.DescribeClusterRoutesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterRoutesResponse:
        """
        This API is used to query cluster routes.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterSecurity(
            self,
            request: models.DescribeClusterSecurityRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterSecurityResponse:
        """
        This API is used to query the key information of a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterSecurity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterSecurityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterStatus(
            self,
            request: models.DescribeClusterStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterStatusResponse:
        """
        This API is used to query the information of clusters under the current account.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterVirtualNode(
            self,
            request: models.DescribeClusterVirtualNodeRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterVirtualNodeResponse:
        """
        This API is used to view the Super Node list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterVirtualNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterVirtualNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterVirtualNodePools(
            self,
            request: models.DescribeClusterVirtualNodePoolsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterVirtualNodePoolsResponse:
        """
        This API is used to view the Super Node Pool list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterVirtualNodePools"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterVirtualNodePoolsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusters(
            self,
            request: models.DescribeClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeClustersResponse:
        """
        This API is used to query clusters list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeECMInstances(
            self,
            request: models.DescribeECMInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeECMInstancesResponse:
        """
        This API is used to obtain the ECM instance information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeECMInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeECMInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdgeAvailableExtraArgs(
            self,
            request: models.DescribeEdgeAvailableExtraArgsRequest,
            opts: Dict = None,
    ) -> models.DescribeEdgeAvailableExtraArgsResponse:
        """
        This API is used to query the custom parameters available for an edge cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdgeAvailableExtraArgs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdgeAvailableExtraArgsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdgeCVMInstances(
            self,
            request: models.DescribeEdgeCVMInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeEdgeCVMInstancesResponse:
        """
        This API is used to obtain the edge CVM instance information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdgeCVMInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdgeCVMInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdgeClusterExtraArgs(
            self,
            request: models.DescribeEdgeClusterExtraArgsRequest,
            opts: Dict = None,
    ) -> models.DescribeEdgeClusterExtraArgsResponse:
        """
        This API is used to query custom parameters of an edge cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdgeClusterExtraArgs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdgeClusterExtraArgsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdgeClusterInstances(
            self,
            request: models.DescribeEdgeClusterInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeEdgeClusterInstancesResponse:
        """
        This API is used to query the TKE Edge cluster node information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdgeClusterInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdgeClusterInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdgeClusterUpgradeInfo(
            self,
            request: models.DescribeEdgeClusterUpgradeInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeEdgeClusterUpgradeInfoResponse:
        """
        This API is used to query the upgrade information of an edge cluster, including the upgradeable components, the current upgrade status, and errors occur during the upgrade.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdgeClusterUpgradeInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdgeClusterUpgradeInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdgeLogSwitches(
            self,
            request: models.DescribeEdgeLogSwitchesRequest,
            opts: Dict = None,
    ) -> models.DescribeEdgeLogSwitchesResponse:
        """
        This API is used to query the status of event storage, cluster auditing and logging.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdgeLogSwitches"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdgeLogSwitchesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnableVpcCniProgress(
            self,
            request: models.DescribeEnableVpcCniProgressRequest,
            opts: Dict = None,
    ) -> models.DescribeEnableVpcCniProgressResponse:
        """
        This API is used to query the task progress of enabling VPC-CNI mode.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnableVpcCniProgress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnableVpcCniProgressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEncryptionStatus(
            self,
            request: models.DescribeEncryptionStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeEncryptionStatusResponse:
        """
        This API is used to query the encryption status of etcd data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEncryptionStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEncryptionStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExistedInstances(
            self,
            request: models.DescribeExistedInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeExistedInstancesResponse:
        """
        This API is used to query one or more existing node and determine whether they can be added to a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExistedInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExistedInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExternalNodeSupportConfig(
            self,
            request: models.DescribeExternalNodeSupportConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeExternalNodeSupportConfigResponse:
        """
        This API is used to view third-party node pool configuration information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExternalNodeSupportConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExternalNodeSupportConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIPAMD(
            self,
            request: models.DescribeIPAMDRequest,
            opts: Dict = None,
    ) -> models.DescribeIPAMDResponse:
        """
        This API is used to obtain eniipamd component information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIPAMD"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIPAMDResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImages(
            self,
            request: models.DescribeImagesRequest,
            opts: Dict = None,
    ) -> models.DescribeImagesResponse:
        """
        This API is used to get image information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogConfigs(
            self,
            request: models.DescribeLogConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeLogConfigsResponse:
        """
        This API is used to query the log collection rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogSwitches(
            self,
            request: models.DescribeLogSwitchesRequest,
            opts: Dict = None,
    ) -> models.DescribeLogSwitchesResponse:
        """
        This API is used to query Cluster Log (Auditing, Event, Common Log) Switch List.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogSwitches"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogSwitchesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePodChargeInfo(
            self,
            request: models.DescribePodChargeInfoRequest,
            opts: Dict = None,
    ) -> models.DescribePodChargeInfoResponse:
        """
        This API is used to query the billing information of running Pods. You can query a specific Pod by Namespace and Name or batch query by Pod Uid.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePodChargeInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePodChargeInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrometheusInstance(
            self,
            request: models.DescribePrometheusInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribePrometheusInstanceResponse:
        """
        This API is used to obtain the instance details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrometheusInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrometheusInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegions(
            self,
            request: models.DescribeRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeRegionsResponse:
        """
        This API is used to obtain all regions supported by TKE.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReservedInstanceUtilizationRate(
            self,
            request: models.DescribeReservedInstanceUtilizationRateRequest,
            opts: Dict = None,
    ) -> models.DescribeReservedInstanceUtilizationRateResponse:
        """
        This API is used to query the usage rate of various types of Reserved Coupons.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReservedInstanceUtilizationRate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReservedInstanceUtilizationRateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceUsage(
            self,
            request: models.DescribeResourceUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceUsageResponse:
        """
        This API is used to query the cluster resource usage.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRouteTableConflicts(
            self,
            request: models.DescribeRouteTableConflictsRequest,
            opts: Dict = None,
    ) -> models.DescribeRouteTableConflictsResponse:
        """
        This API is used to query the list of route table conflicts.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRouteTableConflicts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRouteTableConflictsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSupportedRuntime(
            self,
            request: models.DescribeSupportedRuntimeRequest,
            opts: Dict = None,
    ) -> models.DescribeSupportedRuntimeResponse:
        """
        This API is used to retrieve optional runtime versions based on K8S version.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSupportedRuntime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSupportedRuntimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTKEEdgeClusterCredential(
            self,
            request: models.DescribeTKEEdgeClusterCredentialRequest,
            opts: Dict = None,
    ) -> models.DescribeTKEEdgeClusterCredentialResponse:
        """
        This API is used to obtain the authentication information of a TKE Edge cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTKEEdgeClusterCredential"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTKEEdgeClusterCredentialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTKEEdgeClusterStatus(
            self,
            request: models.DescribeTKEEdgeClusterStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTKEEdgeClusterStatusResponse:
        """
        This API is used to query the current status and process information of a TKE Edge cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTKEEdgeClusterStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTKEEdgeClusterStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTKEEdgeClusters(
            self,
            request: models.DescribeTKEEdgeClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeTKEEdgeClustersResponse:
        """
        This API is used to query the list of TKE Edge clusters.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTKEEdgeClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTKEEdgeClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTKEEdgeExternalKubeconfig(
            self,
            request: models.DescribeTKEEdgeExternalKubeconfigRequest,
            opts: Dict = None,
    ) -> models.DescribeTKEEdgeExternalKubeconfigResponse:
        """
        This API is used to obtain the kubeconfig for access to a TKE Edge cluster through the public network.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTKEEdgeExternalKubeconfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTKEEdgeExternalKubeconfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTKEEdgeScript(
            self,
            request: models.DescribeTKEEdgeScriptRequest,
            opts: Dict = None,
    ) -> models.DescribeTKEEdgeScriptResponse:
        """
        This API is used to query the URL of TKE edge script. You can add external nodes to a TKE Edge cluster by downloading the URL.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTKEEdgeScript"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTKEEdgeScriptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVersions(
            self,
            request: models.DescribeVersionsRequest,
            opts: Dict = None,
    ) -> models.DescribeVersionsResponse:
        """
        This API is used to query cluster version information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcCniPodLimits(
            self,
            request: models.DescribeVpcCniPodLimitsRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcCniPodLimitsResponse:
        """
        This API is used to query the maximum number of Pods in the VPC-CNI network mode supported by the models in the specified availability zone of the current user and region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcCniPodLimits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcCniPodLimitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableClusterDeletionProtection(
            self,
            request: models.DisableClusterDeletionProtectionRequest,
            opts: Dict = None,
    ) -> models.DisableClusterDeletionProtectionResponse:
        """
        This API is used to disable cluster deletion protection.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableClusterDeletionProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableClusterDeletionProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableEncryptionProtection(
            self,
            request: models.DisableEncryptionProtectionRequest,
            opts: Dict = None,
    ) -> models.DisableEncryptionProtectionResponse:
        """
        This API is used to disable encryption protection.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableEncryptionProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableEncryptionProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DrainClusterVirtualNode(
            self,
            request: models.DrainClusterVirtualNodeRequest,
            opts: Dict = None,
    ) -> models.DrainClusterVirtualNodeResponse:
        """
        This API is used to evict the Super Node.
        """
        
        kwargs = {}
        kwargs["action"] = "DrainClusterVirtualNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DrainClusterVirtualNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableClusterDeletionProtection(
            self,
            request: models.EnableClusterDeletionProtectionRequest,
            opts: Dict = None,
    ) -> models.EnableClusterDeletionProtectionResponse:
        """
        This API is used to enable cluster deletion protection.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableClusterDeletionProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableClusterDeletionProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableEncryptionProtection(
            self,
            request: models.EnableEncryptionProtectionRequest,
            opts: Dict = None,
    ) -> models.EnableEncryptionProtectionResponse:
        """
        This API is used to enable Encrypted Data Protection, which requires enabling KMS capability and completing KMS authorization.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableEncryptionProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableEncryptionProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableVpcCniNetworkType(
            self,
            request: models.EnableVpcCniNetworkTypeRequest,
            opts: Dict = None,
    ) -> models.EnableVpcCniNetworkTypeResponse:
        """
        This API is used to enable the VPC-CNI network mode for GR clusters.
        """
        
        kwargs = {}
        kwargs["action"] = "EnableVpcCniNetworkType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableVpcCniNetworkTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ForwardTKEEdgeApplicationRequestV3(
            self,
            request: models.ForwardTKEEdgeApplicationRequestV3Request,
            opts: Dict = None,
    ) -> models.ForwardTKEEdgeApplicationRequestV3Response:
        """
        This API is used to work with the add-ons of a TKE Edge cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "ForwardTKEEdgeApplicationRequestV3"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ForwardTKEEdgeApplicationRequestV3Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetClusterLevelPrice(
            self,
            request: models.GetClusterLevelPriceRequest,
            opts: Dict = None,
    ) -> models.GetClusterLevelPriceResponse:
        """
        Obtaining the price of specified cluster model
        """
        
        kwargs = {}
        kwargs["action"] = "GetClusterLevelPrice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetClusterLevelPriceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTkeAppChartList(
            self,
            request: models.GetTkeAppChartListRequest,
            opts: Dict = None,
    ) -> models.GetTkeAppChartListResponse:
        """
        This API is used to retrieve the App List supported by TKE.
        """
        
        kwargs = {}
        kwargs["action"] = "GetTkeAppChartList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTkeAppChartListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetUpgradeInstanceProgress(
            self,
            request: models.GetUpgradeInstanceProgressRequest,
            opts: Dict = None,
    ) -> models.GetUpgradeInstanceProgressResponse:
        """
        This API is used to obtain the current progress of node upgrade. If the cluster is not in node upgrade status, the API will report an error: Task not found.
        """
        
        kwargs = {}
        kwargs["action"] = "GetUpgradeInstanceProgress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetUpgradeInstanceProgressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InstallAddon(
            self,
            request: models.InstallAddonRequest,
            opts: Dict = None,
    ) -> models.InstallAddonResponse:
        """
        This API is used to install an add-on on the target cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "InstallAddon"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InstallAddonResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InstallEdgeLogAgent(
            self,
            request: models.InstallEdgeLogAgentRequest,
            opts: Dict = None,
    ) -> models.InstallEdgeLogAgentResponse:
        """
        This API is used to install the log collection add-on on TKE Edge cluster nodes.
        """
        
        kwargs = {}
        kwargs["action"] = "InstallEdgeLogAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InstallEdgeLogAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterAsGroupAttribute(
            self,
            request: models.ModifyClusterAsGroupAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterAsGroupAttributeResponse:
        """
        Modify cluster scaling group attributes
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterAsGroupAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterAsGroupAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterAsGroupOptionAttribute(
            self,
            request: models.ModifyClusterAsGroupOptionAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterAsGroupOptionAttributeResponse:
        """
        This API is used to modify cluster auto scaling attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterAsGroupOptionAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterAsGroupOptionAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterAttribute(
            self,
            request: models.ModifyClusterAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterAttributeResponse:
        """
        This API is used to modify cluster attributes.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterAuthenticationOptions(
            self,
            request: models.ModifyClusterAuthenticationOptionsRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterAuthenticationOptionsResponse:
        """
        This API is used to modify cluster authentication configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterAuthenticationOptions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterAuthenticationOptionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterEndpointSP(
            self,
            request: models.ModifyClusterEndpointSPRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterEndpointSPResponse:
        """
        Modify the security policy of the external port of the managed cluster (the old way, only the external port of the managed cluster is supported)
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterEndpointSP"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterEndpointSPResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterImage(
            self,
            request: models.ModifyClusterImageRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterImageResponse:
        """
        This API is used to modify the cluster image.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterNodePool(
            self,
            request: models.ModifyClusterNodePoolRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterNodePoolResponse:
        """
        This API is used to edit a node pool.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterNodePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterNodePoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterRuntimeConfig(
            self,
            request: models.ModifyClusterRuntimeConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterRuntimeConfigResponse:
        """
        This API is used to modify the latitude runtime configuration of clusters and node pools.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterRuntimeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterRuntimeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterTags(
            self,
            request: models.ModifyClusterTagsRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterTagsResponse:
        """
        This API is used to modify cluster tags.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterVirtualNodePool(
            self,
            request: models.ModifyClusterVirtualNodePoolRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterVirtualNodePoolResponse:
        """
        This API is used to modify the Super Node Pool.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterVirtualNodePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterVirtualNodePoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNodePoolInstanceTypes(
            self,
            request: models.ModifyNodePoolInstanceTypesRequest,
            opts: Dict = None,
    ) -> models.ModifyNodePoolInstanceTypesResponse:
        """
        This API is used to modify the model of instances in a node pool.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNodePoolInstanceTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNodePoolInstanceTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrometheusAlertRule(
            self,
            request: models.ModifyPrometheusAlertRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyPrometheusAlertRuleResponse:
        """
        This API is used to modify an alert rule.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrometheusAlertRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrometheusAlertRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveNodeFromNodePool(
            self,
            request: models.RemoveNodeFromNodePoolRequest,
            opts: Dict = None,
    ) -> models.RemoveNodeFromNodePoolResponse:
        """
        This API is used to remove a node from a node pool but retain it in the cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveNodeFromNodePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveNodeFromNodePoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetNodePoolNodeProtection(
            self,
            request: models.SetNodePoolNodeProtectionRequest,
            opts: Dict = None,
    ) -> models.SetNodePoolNodeProtectionResponse:
        """
        This API is used to enable removal protection for the nodes automatically created by the scaling group in a node pool.
        """
        
        kwargs = {}
        kwargs["action"] = "SetNodePoolNodeProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetNodePoolNodeProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UninstallEdgeLogAgent(
            self,
            request: models.UninstallEdgeLogAgentRequest,
            opts: Dict = None,
    ) -> models.UninstallEdgeLogAgentResponse:
        """
        This API is used to uninstall the log collection add-on from TKE Edge cluster nodes.
        """
        
        kwargs = {}
        kwargs["action"] = "UninstallEdgeLogAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UninstallEdgeLogAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAddon(
            self,
            request: models.UpdateAddonRequest,
            opts: Dict = None,
    ) -> models.UpdateAddonResponse:
        """
        This API is used to update parameters and version of an add-on.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAddon"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAddonResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateClusterKubeconfig(
            self,
            request: models.UpdateClusterKubeconfigRequest,
            opts: Dict = None,
    ) -> models.UpdateClusterKubeconfigResponse:
        """
        This API is used to update the Kubeconfig information of a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateClusterKubeconfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateClusterKubeconfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateClusterVersion(
            self,
            request: models.UpdateClusterVersionRequest,
            opts: Dict = None,
    ) -> models.UpdateClusterVersionResponse:
        """
        This API is used to upgrade the master component of the cluster to the specified version.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateClusterVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateClusterVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateEdgeClusterVersion(
            self,
            request: models.UpdateEdgeClusterVersionRequest,
            opts: Dict = None,
    ) -> models.UpdateEdgeClusterVersionResponse:
        """
        This API is used to upgrade an edge cluster component to a TKE Edge version.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateEdgeClusterVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateEdgeClusterVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeClusterInstances(
            self,
            request: models.UpgradeClusterInstancesRequest,
            opts: Dict = None,
    ) -> models.UpgradeClusterInstancesResponse:
        """
        This API is used to upgrade work nodes in a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeClusterInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeClusterInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)