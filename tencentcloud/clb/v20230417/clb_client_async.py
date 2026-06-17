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
from tencentcloud.clb.v20230417 import models
from typing import Dict


class ClbClient(AbstractClient):
    _apiVersion = '2023-04-17'
    _endpoint = 'clb.intl.tencentcloudapi.com'
    _service = 'clb'

    async def BatchModifyTargetWeight(
            self,
            request: models.BatchModifyTargetWeightRequest,
            opts: Dict = None,
    ) -> models.BatchModifyTargetWeightResponse:
        """
        The BatchModifyTargetWeight API is used to modify the forwarding weight of backend machines bound to a Cloud Load Balancer listener in batch. The resource limit is 500. This is an async API. After it returns a successful result, call DescribeTaskStatus API with the returned RequestID as input parameter to check whether this task is successful.<br/>This API is supported by layer-4 and layer-7 CLB listeners but not by classic CLB.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchModifyTargetWeight"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchModifyTargetWeightResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloneLoadBalancer(
            self,
            request: models.CloneLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.CloneLoadBalancerResponse:
        """
        This API is used to clone a Cloud Load Balancer instance. Based on the designated CLB instance, it creates a new instance with identical rules and binding relationships. The cloning operation is asynchronous. The cloned data is based on the call to CloneLoadBalancer. If the cloned CLB changes after calling CloneLoadBalancer, the change rules will not be cloned.

        Limitation notes:
        Does not support basic networks, classic CLB, IPv6, or NAT64.
        Unsupported Monthly Subscription CLB
        The listener does not support QUIC or port ranges.
        No support for backend types: target group, Serverless Cloud Function (SCF).
        Personalized configuration, redirection configuration, and security group default allow switch will not be cloned and must be manually configured.

        API calling
        BGP bandwidth package must include bandwidth package ID
        Exclusive cluster cloning must pass corresponding parameters, otherwise shared instance creation is used.
        The feature is in beta test. You can submit a [beta test application](https://www.tencentcloud.com/apply/p/1akuvsmyn0g?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "CloneLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloneLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLoadBalancer(
            self,
            request: models.CreateLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.CreateLoadBalancerResponse:
        """
        This API is used to create a Cloud Load Balancer instance (this interface supports only pay-as-you-go CLB instances. For annual/monthly subscription, proceed to purchase through the console). To use the CLB service, you must purchase one or more CLB instances. After successfully calling the API, the unique ID of the CLB instance will be returned. CLB instances are divided into public network and private network types. For details, refer to the product type in the product description.
        Note: (1) To apply for Cloud Load Balancer (CLB) in a specified availability zone or cross-zone disaster recovery (only supported in Hong Kong (China)), [submit a request](https://console.cloud.tencent.com/workorder/category) if you need to experience the feature. (2) Currently only Beijing, Shanghai, and Guangzhou support IPv6. (3) The default purchase quota for an account in each region is 100 for public network and 100 for private network.
        This is an async API. After the API returns successfully, you can use the DescribeLoadBalancers API to query the status of the Cloud Load Balancer instance (such as creating and normal) to confirm whether the creation is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClassicalLBListeners(
            self,
            request: models.DescribeClassicalLBListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeClassicalLBListenersResponse:
        """
        This API is used to obtain listener information of classic CLB.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClassicalLBListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClassicalLBListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomizedConfigAssociateList(
            self,
            request: models.DescribeCustomizedConfigAssociateListRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomizedConfigAssociateListResponse:
        """
        This API is used to query the locations, servers, or CLB instances bound to a configuration. If there are domains, the result will be filtered by domain.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomizedConfigAssociateList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomizedConfigAssociateListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomizedConfigList(
            self,
            request: models.DescribeCustomizedConfigListRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomizedConfigListResponse:
        """
        Pull the list of custom configurations. The configurations of the specified type under the user's AppId will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomizedConfigList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomizedConfigListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoadBalancerListByCertId(
            self,
            request: models.DescribeLoadBalancerListByCertIdRequest,
            opts: Dict = None,
    ) -> models.DescribeLoadBalancerListByCertIdResponse:
        """
        This API is used to query the list of CLB instances associated with a certificate in a region by certificate ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoadBalancerListByCertId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoadBalancerListByCertIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoadBalancers(
            self,
            request: models.DescribeLoadBalancersRequest,
            opts: Dict = None,
    ) -> models.DescribeLoadBalancersResponse:
        """
        This API is used to query the list of CLB instances in a region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoadBalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoadBalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoadBalancersDetail(
            self,
            request: models.DescribeLoadBalancersDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeLoadBalancersDetailResponse:
        """
        Query the detailed information of Cloud Load Balancer, including listeners, rules, and backend targets.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoadBalancersDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoadBalancersDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTargetHealth(
            self,
            request: models.DescribeTargetHealthRequest,
            opts: Dict = None,
    ) -> models.DescribeTargetHealthResponse:
        """
        This API (DescribeTargetHealth) is used to query the health check result of a real server of a CLB instance. It is not supported by Classic CLB.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTargetHealth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTargetHealthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetCustomizedConfigForLoadBalancer(
            self,
            request: models.SetCustomizedConfigForLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.SetCustomizedConfigForLoadBalancerResponse:
        """
        This API is used to create, delete, modify, bind, and unbind custom CLB configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "SetCustomizedConfigForLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetCustomizedConfigForLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)