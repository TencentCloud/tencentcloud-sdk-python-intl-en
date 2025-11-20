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
from tencentcloud.gwlb.v20240906 import models
from typing import Dict


class GwlbClient(AbstractClient):
    _apiVersion = '2024-09-06'
    _endpoint = 'gwlb.intl.tencentcloudapi.com'
    _service = 'gwlb'

    async def AssociateTargetGroups(
            self,
            request: models.AssociateTargetGroupsRequest,
            opts: Dict = None,
    ) -> models.AssociateTargetGroupsResponse:
        """
        This API is used to bind target groups to a CLB.This is an async API. After the API return succeeds, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateTargetGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateTargetGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGatewayLoadBalancer(
            self,
            request: models.CreateGatewayLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.CreateGatewayLoadBalancerResponse:
        """
        This API is used to create a GWLB instance. To use the GWLB service, you must purchase one or more GWLB instances. After this API is called successfully, a unique ID for the GWLB instance will be returned.Note: The default purchase quota for each account in each region is 10.This is an async API. After the API is called successfully, you can use the DescribeGatewayLoadBalancers API to query the status of the GWLB instance (such as creating and normal) to determine whether the creation is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGatewayLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGatewayLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTargetGroup(
            self,
            request: models.CreateTargetGroupRequest,
            opts: Dict = None,
    ) -> models.CreateTargetGroupResponse:
        """
        This API is used to create a target group. This feature is in beta testing. If you need to use it, please [submit a ticket](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=163&source=0&data_title=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB&step=1).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTargetGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTargetGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGatewayLoadBalancer(
            self,
            request: models.DeleteGatewayLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.DeleteGatewayLoadBalancerResponse:
        """
        This API is used to delete one or more specified GWLB instances. After successful deletion, the GWLB instances will be unbound from the backend service.This is an async API. After the API return succeeds, you can call the DescribeTaskStatus API with the returned RequestId as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGatewayLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGatewayLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTargetGroups(
            self,
            request: models.DeleteTargetGroupsRequest,
            opts: Dict = None,
    ) -> models.DeleteTargetGroupsResponse:
        """
        This API is used to delete a target group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTargetGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTargetGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeregisterTargetGroupInstances(
            self,
            request: models.DeregisterTargetGroupInstancesRequest,
            opts: Dict = None,
    ) -> models.DeregisterTargetGroupInstancesResponse:
        """
        This API is used to unbind a server from a target group.
        This is an async API. After the API return succeeds, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "DeregisterTargetGroupInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeregisterTargetGroupInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatewayLoadBalancers(
            self,
            request: models.DescribeGatewayLoadBalancersRequest,
            opts: Dict = None,
    ) -> models.DescribeGatewayLoadBalancersResponse:
        """
        This API is used to query the list of GWLB instances in a region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatewayLoadBalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatewayLoadBalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTargetGroupInstanceStatus(
            self,
            request: models.DescribeTargetGroupInstanceStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTargetGroupInstanceStatusResponse:
        """
        This API is used to query the backend service status of a target group. Currently, only GWLB type target groups support querying backend service status.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTargetGroupInstanceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTargetGroupInstanceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTargetGroupInstances(
            self,
            request: models.DescribeTargetGroupInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeTargetGroupInstancesResponse:
        """
        This API is used to obtain information on servers bound to a target group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTargetGroupInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTargetGroupInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTargetGroupList(
            self,
            request: models.DescribeTargetGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeTargetGroupListResponse:
        """
        This API is used to obtain a target group list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTargetGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTargetGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTargetGroups(
            self,
            request: models.DescribeTargetGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeTargetGroupsResponse:
        """
        This API is used to query target group information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTargetGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTargetGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskStatus(
            self,
            request: models.DescribeTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskStatusResponse:
        """
        This API is used to query the execution status of an async task. After non-query APIs (for example, used to create/delete CLB instances) are called successfully, this API needs to be used to query whether the task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateTargetGroups(
            self,
            request: models.DisassociateTargetGroupsRequest,
            opts: Dict = None,
    ) -> models.DisassociateTargetGroupsResponse:
        """
        This API is used to disassociate a CLB from a target group.This is an async API. After the API return succeeds, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateTargetGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateTargetGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceCreateGatewayLoadBalancer(
            self,
            request: models.InquirePriceCreateGatewayLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.InquirePriceCreateGatewayLoadBalancerResponse:
        """
        This API is used to query the price for creating a GWLB.
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceCreateGatewayLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceCreateGatewayLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGatewayLoadBalancerAttribute(
            self,
            request: models.ModifyGatewayLoadBalancerAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyGatewayLoadBalancerAttributeResponse:
        """
        This API is used to modify the attributes of a CLB instance. It supports modifying the name and bandwidth cap of the CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGatewayLoadBalancerAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGatewayLoadBalancerAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTargetGroupAttribute(
            self,
            request: models.ModifyTargetGroupAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyTargetGroupAttributeResponse:
        """
        This API is used to modify the name, health check, and other attributes of the target group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTargetGroupAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTargetGroupAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTargetGroupInstancesWeight(
            self,
            request: models.ModifyTargetGroupInstancesWeightRequest,
            opts: Dict = None,
    ) -> models.ModifyTargetGroupInstancesWeightResponse:
        """
        This API is used to modify the server weight of a target group.This is an async API. After the API return succeeds, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTargetGroupInstancesWeight"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTargetGroupInstancesWeightResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterTargetGroupInstances(
            self,
            request: models.RegisterTargetGroupInstancesRequest,
            opts: Dict = None,
    ) -> models.RegisterTargetGroupInstancesResponse:
        """
        This API is used to register servers to a target group.This is an async API. After the API return succeeds, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterTargetGroupInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterTargetGroupInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)