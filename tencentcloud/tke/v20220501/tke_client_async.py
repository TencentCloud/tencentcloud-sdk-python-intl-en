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
from tencentcloud.tke.v20220501 import models
from typing import Dict


class TkeClient(AbstractClient):
    _apiVersion = '2022-05-01'
    _endpoint = 'tke.intl.tencentcloudapi.com'
    _service = 'tke'

    async def CreateHealthCheckPolicy(
            self,
            request: models.CreateHealthCheckPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateHealthCheckPolicyResponse:
        """
        This API is used to create a health check policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHealthCheckPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHealthCheckPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNodePool(
            self,
            request: models.CreateNodePoolRequest,
            opts: Dict = None,
    ) -> models.CreateNodePoolResponse:
        """
        This API is used to create a TKE node pool
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNodePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNodePoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteHealthCheckPolicy(
            self,
            request: models.DeleteHealthCheckPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteHealthCheckPolicyResponse:
        """
        This API is used to delete a health check policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteHealthCheckPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteHealthCheckPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNodePool(
            self,
            request: models.DeleteNodePoolRequest,
            opts: Dict = None,
    ) -> models.DeleteNodePoolResponse:
        """
        This API is used to delete a TKE node pool.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNodePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNodePoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterInstances(
            self,
            request: models.DescribeClusterInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterInstancesResponse:
        """
        This API is used to query the information of node instances in a cluster.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHealthCheckPolicies(
            self,
            request: models.DescribeHealthCheckPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeHealthCheckPoliciesResponse:
        """
        This API is used to query a health check policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHealthCheckPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHealthCheckPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHealthCheckPolicyBindings(
            self,
            request: models.DescribeHealthCheckPolicyBindingsRequest,
            opts: Dict = None,
    ) -> models.DescribeHealthCheckPolicyBindingsResponse:
        """
        This API is used to query a health check policy binding relationship.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHealthCheckPolicyBindings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHealthCheckPolicyBindingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHealthCheckTemplate(
            self,
            request: models.DescribeHealthCheckTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeHealthCheckTemplateResponse:
        """
        This API is used to query a health check policy template.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHealthCheckTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHealthCheckTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNodePools(
            self,
            request: models.DescribeNodePoolsRequest,
            opts: Dict = None,
    ) -> models.DescribeNodePoolsResponse:
        """
        This API is used to query a TKE node pool list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNodePools"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNodePoolsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHealthCheckPolicy(
            self,
            request: models.ModifyHealthCheckPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyHealthCheckPolicyResponse:
        """
        This API is used to modify a health check policy.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHealthCheckPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHealthCheckPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNodePool(
            self,
            request: models.ModifyNodePoolRequest,
            opts: Dict = None,
    ) -> models.ModifyNodePoolResponse:
        """
        This API is used to update a TKE node pool.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNodePool"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNodePoolResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)