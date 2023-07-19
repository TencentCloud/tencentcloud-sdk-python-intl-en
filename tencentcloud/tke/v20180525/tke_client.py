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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.tke.v20180525 import models


class TkeClient(AbstractClient):
    _apiVersion = '2018-05-25'
    _endpoint = 'tke.tencentcloudapi.com'
    _service = 'tke'


    def AcquireClusterAdminRole(self, request):
        """This API can be called to acquire the ClusterRole tke:admin. By setting a CAM policy, you can grant permission of this API to a sub-account that has higher permission in CAM. In this way, this sub-account can call this API directly to acquire the admin role of a Kubernetes cluster.

        :param request: Request instance for AcquireClusterAdminRole.
        :type request: :class:`tencentcloud.tke.v20180525.models.AcquireClusterAdminRoleRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.AcquireClusterAdminRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AcquireClusterAdminRole", params, headers=headers)
            response = json.loads(body)
            model = models.AcquireClusterAdminRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddExistedInstances(self, request):
        """This API is used to add one or more existing instances to a cluster.

        :param request: Request instance for AddExistedInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.AddExistedInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.AddExistedInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddExistedInstances", params, headers=headers)
            response = json.loads(body)
            model = models.AddExistedInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddNodeToNodePool(self, request):
        """This API is used to move nodes in a cluster to a node pool.

        :param request: Request instance for AddNodeToNodePool.
        :type request: :class:`tencentcloud.tke.v20180525.models.AddNodeToNodePoolRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.AddNodeToNodePoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddNodeToNodePool", params, headers=headers)
            response = json.loads(body)
            model = models.AddNodeToNodePoolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddVpcCniSubnets(self, request):
        """This API is used to add subnets in the container network for a VPC-CNI cluster.

        :param request: Request instance for AddVpcCniSubnets.
        :type request: :class:`tencentcloud.tke.v20180525.models.AddVpcCniSubnetsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.AddVpcCniSubnetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddVpcCniSubnets", params, headers=headers)
            response = json.loads(body)
            model = models.AddVpcCniSubnetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckEdgeClusterCIDR(self, request):
        """This API is used to check if the CIDR block of a TKE Edge cluster conflicts with other CIDR blocks.

        :param request: Request instance for CheckEdgeClusterCIDR.
        :type request: :class:`tencentcloud.tke.v20180525.models.CheckEdgeClusterCIDRRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CheckEdgeClusterCIDRResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckEdgeClusterCIDR", params, headers=headers)
            response = json.loads(body)
            model = models.CheckEdgeClusterCIDRResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckInstancesUpgradeAble(self, request):
        """This API is used to query nodes eligible for an upgrade in the given node list.

        :param request: Request instance for CheckInstancesUpgradeAble.
        :type request: :class:`tencentcloud.tke.v20180525.models.CheckInstancesUpgradeAbleRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CheckInstancesUpgradeAbleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckInstancesUpgradeAble", params, headers=headers)
            response = json.loads(body)
            model = models.CheckInstancesUpgradeAbleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBackupStorageLocation(self, request):
        """This API is used to create a backup repository. You can specify the storage type (such as COS), the bucket region and the name. Up to 100 repositories can be created. Note that the settings of this API apply globally. You only need to create one backup repository, and back up TKE clusters in different regions in it.

        :param request: Request instance for CreateBackupStorageLocation.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateBackupStorageLocationRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateBackupStorageLocationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBackupStorageLocation", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBackupStorageLocationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCluster(self, request):
        """This API is used to create a cluster.

        :param request: Request instance for CreateCluster.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCluster", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusterEndpoint(self, request):
        """This API is used to create a cluster access endpoint.

        :param request: Request instance for CreateClusterEndpoint.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterEndpointRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterEndpointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterEndpoint", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterEndpointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusterEndpointVip(self, request):
        """Create an external network access port for the managed cluster (the old way, only the external network port for the managed cluster is supported)

        :param request: Request instance for CreateClusterEndpointVip.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterEndpointVipRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterEndpointVipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterEndpointVip", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterEndpointVipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusterInstances(self, request):
        """This API is used to create one or more nodes in a cluster.

        :param request: Request instance for CreateClusterInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusterNodePool(self, request):
        """This API is used to create a node pool.

        :param request: Request instance for CreateClusterNodePool.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterNodePoolRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterNodePoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterNodePool", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterNodePoolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusterRouteTable(self, request):
        """This API is used to create a cluster route table.

        :param request: Request instance for CreateClusterRouteTable.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterRouteTableRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterRouteTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterRouteTable", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterRouteTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusterVirtualNode(self, request):
        """This API is used to create a virtual node.

        :param request: Request instance for CreateClusterVirtualNode.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterVirtualNodeRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterVirtualNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterVirtualNode", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterVirtualNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusterVirtualNodePool(self, request):
        """This API is used to create a virtual node pool.

        :param request: Request instance for CreateClusterVirtualNodePool.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateClusterVirtualNodePoolRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateClusterVirtualNodePoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterVirtualNodePool", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterVirtualNodePoolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateECMInstances(self, request):
        """This API is used to create an ECM instance.

        :param request: Request instance for CreateECMInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateECMInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateECMInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateECMInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateECMInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEdgeCVMInstances(self, request):
        """This API is used to create CVM instances in the specified TKE edge cluster.

        :param request: Request instance for CreateEdgeCVMInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateEdgeCVMInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateEdgeCVMInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEdgeCVMInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEdgeCVMInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEdgeLogConfig(self, request):
        """This API is used to create log collection configuration for a TKE Edge cluster.

        :param request: Request instance for CreateEdgeLogConfig.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateEdgeLogConfigRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateEdgeLogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEdgeLogConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEdgeLogConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePrometheusAlertRule(self, request):
        """This API is used to create an alarm rule.

        :param request: Request instance for CreatePrometheusAlertRule.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusAlertRuleRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreatePrometheusAlertRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheusAlertRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrometheusAlertRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTKEEdgeCluster(self, request):
        """This API is used to create a TKE Edge cluster.

        :param request: Request instance for CreateTKEEdgeCluster.
        :type request: :class:`tencentcloud.tke.v20180525.models.CreateTKEEdgeClusterRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.CreateTKEEdgeClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTKEEdgeCluster", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTKEEdgeClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBackupStorageLocation(self, request):
        """This API is used to delete a backup repository.

        :param request: Request instance for DeleteBackupStorageLocation.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteBackupStorageLocationRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteBackupStorageLocationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBackupStorageLocation", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBackupStorageLocationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCluster(self, request):
        """This API is used to delete a cluster. (Cloud API v3).

        :param request: Request instance for DeleteCluster.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCluster", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteClusterAsGroups(self, request):
        """Delete a cluster scaling group

        :param request: Request instance for DeleteClusterAsGroups.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterAsGroupsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterAsGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClusterAsGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClusterAsGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteClusterEndpoint(self, request):
        """This API is used to delete a cluster access endpoint.

        :param request: Request instance for DeleteClusterEndpoint.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterEndpointRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterEndpointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClusterEndpoint", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClusterEndpointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteClusterEndpointVip(self, request):
        """Delete the external network access port of the managed cluster (the old way, only the external network port of the managed cluster is supported)

        :param request: Request instance for DeleteClusterEndpointVip.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterEndpointVipRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterEndpointVipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClusterEndpointVip", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClusterEndpointVipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteClusterInstances(self, request):
        """This API is used to delete one or more nodes from a cluster.

        :param request: Request instance for DeleteClusterInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClusterInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClusterInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteClusterNodePool(self, request):
        """This API is used to delete a node pool.

        :param request: Request instance for DeleteClusterNodePool.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterNodePoolRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterNodePoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClusterNodePool", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClusterNodePoolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteClusterRoute(self, request):
        """This API is used to delete a cluster route.

        :param request: Request instance for DeleteClusterRoute.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterRouteRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClusterRoute", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClusterRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteClusterRouteTable(self, request):
        """This API is used to delete cluster a route table.

        :param request: Request instance for DeleteClusterRouteTable.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterRouteTableRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterRouteTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClusterRouteTable", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClusterRouteTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteClusterVirtualNode(self, request):
        """This API is used to delete a virtual node.

        :param request: Request instance for DeleteClusterVirtualNode.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterVirtualNodeRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterVirtualNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClusterVirtualNode", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClusterVirtualNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteClusterVirtualNodePool(self, request):
        """This API is used to delete a virtual node pool.

        :param request: Request instance for DeleteClusterVirtualNodePool.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteClusterVirtualNodePoolRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteClusterVirtualNodePoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClusterVirtualNodePool", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClusterVirtualNodePoolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteECMInstances(self, request):
        """This API is used to delete one or more ECM instances.

        :param request: Request instance for DeleteECMInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteECMInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteECMInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteECMInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteECMInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEdgeCVMInstances(self, request):
        """This API is used to delete one or more edge CVM instances.

        :param request: Request instance for DeleteEdgeCVMInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteEdgeCVMInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteEdgeCVMInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEdgeCVMInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEdgeCVMInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEdgeClusterInstances(self, request):
        """This API is used to delete one or more edge compute instances.

        :param request: Request instance for DeleteEdgeClusterInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteEdgeClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteEdgeClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEdgeClusterInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEdgeClusterInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePrometheusAlertRule(self, request):
        """This API is used to delete an alarm rule.

        :param request: Request instance for DeletePrometheusAlertRule.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusAlertRuleRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeletePrometheusAlertRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrometheusAlertRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrometheusAlertRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTKEEdgeCluster(self, request):
        """This API is used to delete a TKE Edge cluster.

        :param request: Request instance for DeleteTKEEdgeCluster.
        :type request: :class:`tencentcloud.tke.v20180525.models.DeleteTKEEdgeClusterRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DeleteTKEEdgeClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTKEEdgeCluster", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTKEEdgeClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAvailableClusterVersion(self, request):
        """This API is used to obtain all versions that the cluster can upgrade to.

        :param request: Request instance for DescribeAvailableClusterVersion.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeAvailableClusterVersionRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeAvailableClusterVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailableClusterVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAvailableClusterVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAvailableTKEEdgeVersion(self, request):
        """This API is used to check the edge component versions and K8s versions supported by TKE Edge.

        :param request: Request instance for DescribeAvailableTKEEdgeVersion.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeAvailableTKEEdgeVersionRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeAvailableTKEEdgeVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailableTKEEdgeVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAvailableTKEEdgeVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupStorageLocations(self, request):
        """This API is used to query backup repositories.

        :param request: Request instance for DescribeBackupStorageLocations.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeBackupStorageLocationsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeBackupStorageLocationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupStorageLocations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupStorageLocationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterAsGroupOption(self, request):
        """Cluster auto scaling configuration

        :param request: Request instance for DescribeClusterAsGroupOption.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterAsGroupOptionRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterAsGroupOptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterAsGroupOption", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterAsGroupOptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterAsGroups(self, request):
        """Cluster-associated scaling group list

        :param request: Request instance for DescribeClusterAsGroups.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterAsGroupsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterAsGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterAsGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterAsGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterAuthenticationOptions(self, request):
        """This API is used to query cluster authentication configuration.

        :param request: Request instance for DescribeClusterAuthenticationOptions.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterAuthenticationOptionsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterAuthenticationOptionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterAuthenticationOptions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterAuthenticationOptionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterCommonNames(self, request):
        """This API is used to obtain the CommonName from the kube-apiserver client certificate that corresponding to the sub-account in RBAC authorization mode.

        :param request: Request instance for DescribeClusterCommonNames.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterCommonNamesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterCommonNamesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterCommonNames", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterCommonNamesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterEndpointStatus(self, request):
        """Query cluster access port status (intranet / extranet access is enabled for independent clusters, and intranet access is supported for managed clusters)

        :param request: Request instance for DescribeClusterEndpointStatus.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterEndpointStatusRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterEndpointStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterEndpointStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterEndpointStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterEndpointVipStatus(self, request):
        """Query cluster open port process status (only supports external ports of the managed cluster)

        :param request: Request instance for DescribeClusterEndpointVipStatus.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterEndpointVipStatusRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterEndpointVipStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterEndpointVipStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterEndpointVipStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterEndpoints(self, request):
        """This API is used to query cluster access addresses, including private network address, public network address, public network domain name, and security policy for public network access.

        :param request: Request instance for DescribeClusterEndpoints.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterEndpointsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterEndpointsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterEndpoints", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterEndpointsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterInstances(self, request):
        """This API is used to query information of node instances in a cluster.

        :param request: Request instance for DescribeClusterInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterKubeconfig(self, request):
        """This API is used to obtain the cluster kubeconfig file. Different sub-accounts have their own kubeconfig files. The kubeconfig file contains the kube-apiserver client certificate of the corresponding sub-account. By default, the client certificate is created when this API is called for the first time, and the certificate is valid for 20 years with no permissions granted. For the cluster owner or primary account, the cluster-admin permission is granted by default.

        :param request: Request instance for DescribeClusterKubeconfig.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterKubeconfigRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterKubeconfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterKubeconfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterKubeconfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterLevelAttribute(self, request):
        """This API is used to obtain the cluster model.

        :param request: Request instance for DescribeClusterLevelAttribute.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterLevelAttributeRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterLevelAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterLevelAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterLevelAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterLevelChangeRecords(self, request):
        """This API is used to query the cluster model adjustment history.

        :param request: Request instance for DescribeClusterLevelChangeRecords.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterLevelChangeRecordsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterLevelChangeRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterLevelChangeRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterLevelChangeRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterNodePoolDetail(self, request):
        """This API is used to query detailed information of a node pool.

        :param request: Request instance for DescribeClusterNodePoolDetail.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterNodePoolDetailRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterNodePoolDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterNodePoolDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterNodePoolDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterNodePools(self, request):
        """This API is used to query the node pool list

        :param request: Request instance for DescribeClusterNodePools.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterNodePoolsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterNodePoolsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterNodePools", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterNodePoolsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterRouteTables(self, request):
        """This API is used to query one or more cluster route tables.

        :param request: Request instance for DescribeClusterRouteTables.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterRouteTablesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterRouteTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterRouteTables", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterRouteTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterRoutes(self, request):
        """This API is used to query cluster routes.

        :param request: Request instance for DescribeClusterRoutes.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterRoutesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterSecurity(self, request):
        """This API is used to query the key information of a cluster.

        :param request: Request instance for DescribeClusterSecurity.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterSecurityRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterSecurityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterSecurity", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterSecurityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterStatus(self, request):
        """This API is used to query the information of clusters under the current account.

        :param request: Request instance for DescribeClusterStatus.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterStatusRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterVirtualNode(self, request):
        """This API is used to query the list of virtual nodes.

        :param request: Request instance for DescribeClusterVirtualNode.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterVirtualNodeRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterVirtualNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterVirtualNode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterVirtualNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterVirtualNodePools(self, request):
        """This API is used to query the list of virtual node pools.

        :param request: Request instance for DescribeClusterVirtualNodePools.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClusterVirtualNodePoolsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClusterVirtualNodePoolsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterVirtualNodePools", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterVirtualNodePoolsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusters(self, request):
        """This API is used to query clusters list.

        :param request: Request instance for DescribeClusters.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeClustersRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeECMInstances(self, request):
        """This API is used to obtain the ECM instance information.

        :param request: Request instance for DescribeECMInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeECMInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeECMInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeECMInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeECMInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeAvailableExtraArgs(self, request):
        """This API is used to query the custom parameters available for an edge cluster.

        :param request: Request instance for DescribeEdgeAvailableExtraArgs.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeAvailableExtraArgsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeAvailableExtraArgsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeAvailableExtraArgs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeAvailableExtraArgsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeCVMInstances(self, request):
        """This API is used to obtain the edge CVM instance information.

        :param request: Request instance for DescribeEdgeCVMInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeCVMInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeCVMInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeCVMInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeCVMInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeClusterExtraArgs(self, request):
        """This API is used to query custom parameters of an edge cluster.

        :param request: Request instance for DescribeEdgeClusterExtraArgs.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeClusterExtraArgsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeClusterExtraArgsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeClusterExtraArgs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeClusterExtraArgsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeClusterInstances(self, request):
        """This API is used to query the TKE Edge cluster node information.

        :param request: Request instance for DescribeEdgeClusterInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeClusterInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeClusterInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeClusterUpgradeInfo(self, request):
        """This API is used to query the upgrade information of an edge cluster, including the upgradeable components, the current upgrade status, and errors occur during the upgrade.

        :param request: Request instance for DescribeEdgeClusterUpgradeInfo.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeClusterUpgradeInfoRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeClusterUpgradeInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeClusterUpgradeInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeClusterUpgradeInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEdgeLogSwitches(self, request):
        """This API is used to query the status of event storage, cluster auditing and logging.

        :param request: Request instance for DescribeEdgeLogSwitches.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeLogSwitchesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeEdgeLogSwitchesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEdgeLogSwitches", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEdgeLogSwitchesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnableVpcCniProgress(self, request):
        """This API is used to query the task progress of enabling VPC-CNI mode.

        :param request: Request instance for DescribeEnableVpcCniProgress.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeEnableVpcCniProgressRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeEnableVpcCniProgressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnableVpcCniProgress", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnableVpcCniProgressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExistedInstances(self, request):
        """This API is used to query one or more existing node and determine whether they can be added to a cluster.

        :param request: Request instance for DescribeExistedInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeExistedInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeExistedInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExistedInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExistedInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImages(self, request):
        """This API is used to get image information.

        :param request: Request instance for DescribeImages.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeImagesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrometheusInstance(self, request):
        """This API is used to obtain the instance details.

        :param request: Request instance for DescribePrometheusInstance.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusInstanceRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribePrometheusInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheusInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrometheusInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegions(self, request):
        """This API is used to obtain all regions supported by TKE.

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceUsage(self, request):
        """This API is used to query the cluster resource usage.

        :param request: Request instance for DescribeResourceUsage.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeResourceUsageRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeResourceUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRouteTableConflicts(self, request):
        """This API is used to query the list of route table conflicts.

        :param request: Request instance for DescribeRouteTableConflicts.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeRouteTableConflictsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeRouteTableConflictsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRouteTableConflicts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRouteTableConflictsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTKEEdgeClusterCredential(self, request):
        """This API is used to obtain the authentication information of a TKE Edge cluster.

        :param request: Request instance for DescribeTKEEdgeClusterCredential.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeTKEEdgeClusterCredentialRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeTKEEdgeClusterCredentialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTKEEdgeClusterCredential", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTKEEdgeClusterCredentialResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTKEEdgeClusterStatus(self, request):
        """This API is used to query the current status and process information of a TKE Edge cluster.

        :param request: Request instance for DescribeTKEEdgeClusterStatus.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeTKEEdgeClusterStatusRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeTKEEdgeClusterStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTKEEdgeClusterStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTKEEdgeClusterStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTKEEdgeClusters(self, request):
        """This API is used to query the list of TKE Edge clusters.

        :param request: Request instance for DescribeTKEEdgeClusters.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeTKEEdgeClustersRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeTKEEdgeClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTKEEdgeClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTKEEdgeClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTKEEdgeExternalKubeconfig(self, request):
        """This API is used to obtain the kubeconfig for access to a TKE Edge cluster through the public network.

        :param request: Request instance for DescribeTKEEdgeExternalKubeconfig.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeTKEEdgeExternalKubeconfigRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeTKEEdgeExternalKubeconfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTKEEdgeExternalKubeconfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTKEEdgeExternalKubeconfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTKEEdgeScript(self, request):
        """This API is used to query the URL of TKE edge script. You can add external nodes to a TKE Edge cluster by downloading the URL.

        :param request: Request instance for DescribeTKEEdgeScript.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeTKEEdgeScriptRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeTKEEdgeScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTKEEdgeScript", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTKEEdgeScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVersions(self, request):
        """This API is used to query cluster version information.

        :param request: Request instance for DescribeVersions.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeVersionsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcCniPodLimits(self, request):
        """This API is used to query the maximum number of Pods in the VPC-CNI network mode supported by the models in the specified availability zone of the current user and region.

        :param request: Request instance for DescribeVpcCniPodLimits.
        :type request: :class:`tencentcloud.tke.v20180525.models.DescribeVpcCniPodLimitsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DescribeVpcCniPodLimitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcCniPodLimits", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcCniPodLimitsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableClusterDeletionProtection(self, request):
        """This API is used to disable cluster deletion protection.

        :param request: Request instance for DisableClusterDeletionProtection.
        :type request: :class:`tencentcloud.tke.v20180525.models.DisableClusterDeletionProtectionRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DisableClusterDeletionProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableClusterDeletionProtection", params, headers=headers)
            response = json.loads(body)
            model = models.DisableClusterDeletionProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DrainClusterVirtualNode(self, request):
        """This API is used to drain a virtual node.

        :param request: Request instance for DrainClusterVirtualNode.
        :type request: :class:`tencentcloud.tke.v20180525.models.DrainClusterVirtualNodeRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.DrainClusterVirtualNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DrainClusterVirtualNode", params, headers=headers)
            response = json.loads(body)
            model = models.DrainClusterVirtualNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableClusterDeletionProtection(self, request):
        """This API is used to enable cluster deletion protection.

        :param request: Request instance for EnableClusterDeletionProtection.
        :type request: :class:`tencentcloud.tke.v20180525.models.EnableClusterDeletionProtectionRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.EnableClusterDeletionProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableClusterDeletionProtection", params, headers=headers)
            response = json.loads(body)
            model = models.EnableClusterDeletionProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableVpcCniNetworkType(self, request):
        """This API is used to enable the VPC-CNI network mode for GR clusters.

        :param request: Request instance for EnableVpcCniNetworkType.
        :type request: :class:`tencentcloud.tke.v20180525.models.EnableVpcCniNetworkTypeRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.EnableVpcCniNetworkTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableVpcCniNetworkType", params, headers=headers)
            response = json.loads(body)
            model = models.EnableVpcCniNetworkTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ForwardTKEEdgeApplicationRequestV3(self, request):
        """This API is used to work with the add-ons of a TKE Edge cluster.

        :param request: Request instance for ForwardTKEEdgeApplicationRequestV3.
        :type request: :class:`tencentcloud.tke.v20180525.models.ForwardTKEEdgeApplicationRequestV3Request`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ForwardTKEEdgeApplicationRequestV3Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ForwardTKEEdgeApplicationRequestV3", params, headers=headers)
            response = json.loads(body)
            model = models.ForwardTKEEdgeApplicationRequestV3Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetClusterLevelPrice(self, request):
        """Obtaining the price of specified cluster model

        :param request: Request instance for GetClusterLevelPrice.
        :type request: :class:`tencentcloud.tke.v20180525.models.GetClusterLevelPriceRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.GetClusterLevelPriceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetClusterLevelPrice", params, headers=headers)
            response = json.loads(body)
            model = models.GetClusterLevelPriceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetUpgradeInstanceProgress(self, request):
        """This API is used to obtain the current progress of the node upgrade.

        :param request: Request instance for GetUpgradeInstanceProgress.
        :type request: :class:`tencentcloud.tke.v20180525.models.GetUpgradeInstanceProgressRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.GetUpgradeInstanceProgressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetUpgradeInstanceProgress", params, headers=headers)
            response = json.loads(body)
            model = models.GetUpgradeInstanceProgressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InstallEdgeLogAgent(self, request):
        """This API is used to install the log collection add-on on TKE Edge cluster nodes.

        :param request: Request instance for InstallEdgeLogAgent.
        :type request: :class:`tencentcloud.tke.v20180525.models.InstallEdgeLogAgentRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.InstallEdgeLogAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InstallEdgeLogAgent", params, headers=headers)
            response = json.loads(body)
            model = models.InstallEdgeLogAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterAsGroupAttribute(self, request):
        """Modify cluster scaling group attributes

        :param request: Request instance for ModifyClusterAsGroupAttribute.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyClusterAsGroupAttributeRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyClusterAsGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterAsGroupAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterAsGroupAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterAsGroupOptionAttribute(self, request):
        """This API is used to modify cluster auto scaling attributes.

        :param request: Request instance for ModifyClusterAsGroupOptionAttribute.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyClusterAsGroupOptionAttributeRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyClusterAsGroupOptionAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterAsGroupOptionAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterAsGroupOptionAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterAttribute(self, request):
        """This API is used to modify cluster attributes.

        :param request: Request instance for ModifyClusterAttribute.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyClusterAttributeRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyClusterAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterAuthenticationOptions(self, request):
        """This API is used to modify cluster authentication configuration.

        :param request: Request instance for ModifyClusterAuthenticationOptions.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyClusterAuthenticationOptionsRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyClusterAuthenticationOptionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterAuthenticationOptions", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterAuthenticationOptionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterEndpointSP(self, request):
        """Modify the security policy of the external port of the managed cluster (the old way, only the external port of the managed cluster is supported)

        :param request: Request instance for ModifyClusterEndpointSP.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyClusterEndpointSPRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyClusterEndpointSPResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterEndpointSP", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterEndpointSPResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterNodePool(self, request):
        """This API is used to edit a node pool.

        :param request: Request instance for ModifyClusterNodePool.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyClusterNodePoolRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyClusterNodePoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterNodePool", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterNodePoolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterVirtualNodePool(self, request):
        """This API is used to modify a virtual node pool.

        :param request: Request instance for ModifyClusterVirtualNodePool.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyClusterVirtualNodePoolRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyClusterVirtualNodePoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterVirtualNodePool", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterVirtualNodePoolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNodePoolInstanceTypes(self, request):
        """This API is used to modify the model of instances in a node pool.

        :param request: Request instance for ModifyNodePoolInstanceTypes.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyNodePoolInstanceTypesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyNodePoolInstanceTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNodePoolInstanceTypes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNodePoolInstanceTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPrometheusAlertRule(self, request):
        """This API is used to modify an alert rule.

        :param request: Request instance for ModifyPrometheusAlertRule.
        :type request: :class:`tencentcloud.tke.v20180525.models.ModifyPrometheusAlertRuleRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.ModifyPrometheusAlertRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrometheusAlertRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrometheusAlertRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveNodeFromNodePool(self, request):
        """This API is used to remove a node from a node pool but retain it in the cluster.

        :param request: Request instance for RemoveNodeFromNodePool.
        :type request: :class:`tencentcloud.tke.v20180525.models.RemoveNodeFromNodePoolRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.RemoveNodeFromNodePoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveNodeFromNodePool", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveNodeFromNodePoolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetNodePoolNodeProtection(self, request):
        """This API is used to enable removal protection for the nodes automatically created by the scaling group in a node pool.

        :param request: Request instance for SetNodePoolNodeProtection.
        :type request: :class:`tencentcloud.tke.v20180525.models.SetNodePoolNodeProtectionRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.SetNodePoolNodeProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetNodePoolNodeProtection", params, headers=headers)
            response = json.loads(body)
            model = models.SetNodePoolNodeProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UninstallEdgeLogAgent(self, request):
        """This API is used to uninstall the log collection add-on from TKE Edge cluster nodes.

        :param request: Request instance for UninstallEdgeLogAgent.
        :type request: :class:`tencentcloud.tke.v20180525.models.UninstallEdgeLogAgentRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.UninstallEdgeLogAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UninstallEdgeLogAgent", params, headers=headers)
            response = json.loads(body)
            model = models.UninstallEdgeLogAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateClusterKubeconfig(self, request):
        """This API is used to update the Kubeconfig information of a cluster.

        :param request: Request instance for UpdateClusterKubeconfig.
        :type request: :class:`tencentcloud.tke.v20180525.models.UpdateClusterKubeconfigRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.UpdateClusterKubeconfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateClusterKubeconfig", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateClusterKubeconfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateClusterVersion(self, request):
        """This API is used to upgrade the master component of the cluster to the specified version.

        :param request: Request instance for UpdateClusterVersion.
        :type request: :class:`tencentcloud.tke.v20180525.models.UpdateClusterVersionRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.UpdateClusterVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateClusterVersion", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateClusterVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateEdgeClusterVersion(self, request):
        """This API is used to upgrade an edge cluster component to a TKE Edge version.

        :param request: Request instance for UpdateEdgeClusterVersion.
        :type request: :class:`tencentcloud.tke.v20180525.models.UpdateEdgeClusterVersionRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.UpdateEdgeClusterVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateEdgeClusterVersion", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateEdgeClusterVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeClusterInstances(self, request):
        """This API is used to upgrade work nodes in a cluster.

        :param request: Request instance for UpgradeClusterInstances.
        :type request: :class:`tencentcloud.tke.v20180525.models.UpgradeClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tke.v20180525.models.UpgradeClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeClusterInstances", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeClusterInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))