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
from tencentcloud.clb.v20180317 import models
from typing import Dict


class ClbClient(AbstractClient):
    _apiVersion = '2018-03-17'
    _endpoint = 'clb.intl.tencentcloudapi.com'
    _service = 'clb'

    async def AssociateTargetGroups(
            self,
            request: models.AssociateTargetGroupsRequest,
            opts: Dict = None,
    ) -> models.AssociateTargetGroupsResponse:
        """
        This API is used to bind target groups to CLB listeners (layer-4 protocol) or forwarding rules (layer-7 protocol).
        This is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateTargetGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateTargetGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AutoRewrite(
            self,
            request: models.AutoRewriteRequest,
            opts: Dict = None,
    ) -> models.AutoRewriteResponse:
        """
        An HTTPS:443 listener needs to be created first, along with a forwarding rule. When this API is called, an HTTP:80 listener will be created automatically if it did not exist and a forwarding rule corresponding to `Domains` (specified in the input parameter) under the HTTPS:443 listener will also be created. After successful creation, access requests to an HTTP:80 address will be redirected to an HTTPS:443 address automatically.
        """
        
        kwargs = {}
        kwargs["action"] = "AutoRewrite"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AutoRewriteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDeregisterTargets(
            self,
            request: models.BatchDeregisterTargetsRequest,
            opts: Dict = None,
    ) -> models.BatchDeregisterTargetsResponse:
        """
        This API is used to batch unbind real servers of the layer-4 and layer-7 VPC-based CLBs. Up to 500 real servers can be unbound in a batch.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeregisterTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeregisterTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchModifyTargetTag(
            self,
            request: models.BatchModifyTargetTagRequest,
            opts: Dict = None,
    ) -> models.BatchModifyTargetTagResponse:
        """
        This API is used to modify the tags of real servers bound to CLB listeners in batches. The maximum number of resources that can be modified in a batch is 500. This is a synchronous API. <br/> It is supported for Layer-4 and Layer-7 listeners of CLB instances, but not for classic CLB instances.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchModifyTargetTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchModifyTargetTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchModifyTargetWeight(
            self,
            request: models.BatchModifyTargetWeightRequest,
            opts: Dict = None,
    ) -> models.BatchModifyTargetWeightResponse:
        """
        This API is used to modify forwarding weights of real servers bound to CLB listeners in batches. Up to 500 servers can be unbound in a batch. As this API is async, you should check whether the task is successful by passing the RequestId returned to the API call `DescribeTaskStatus`.<br/> This API is supported by CLB layer-4 and layer-7 listeners, but not Classis CLB counterparts.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchModifyTargetWeight"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchModifyTargetWeightResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchRegisterTargets(
            self,
            request: models.BatchRegisterTargetsRequest,
            opts: Dict = None,
    ) -> models.BatchRegisterTargetsResponse:
        """
        This API is used to batch bind CVM instances or ENIs. Up to 500 servers can be bound in a batch. It supports cross-region binding, layer-4 and layer-7 (TCP/UDP/HTTP/HTTPS) protocols, and VPC-based CLBs only.
        """
        
        kwargs = {}
        kwargs["action"] = "BatchRegisterTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchRegisterTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloneLoadBalancer(
            self,
            request: models.CloneLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.CloneLoadBalancerResponse:
        """
        This API is used to clone a CLB instance. CLB instance cloning indicates copying a specified CLB instance to create one with the same rules and binding relationships. The operation of this cloning API is asynchronous. The cloned data is based on the state when CloneLoadBalancer is called. If the cloned CLB instance changes after CloneLoadBalancer is called, the changed rules will not be cloned.Note: You can query the instance creation status by calling the [DescribeTaskStatus](https://intl.cloud.tencent.com/document/product/214/30683?from_cn_redirect=1) API with the returned requestId.RestrictionsInstance attribute restrictions:- Instances billed in pay-as-you-go and monthly subscription modes can be cloned. For a new instance cloned from a monthly subscription instance, its network billing mode will switch to billing by hourly bandwidth, but its bandwidth and specifications will remain the same as the settings of the original instance.- CLB instances not associated with any billable items cannot be cloned.- Classic CLB instances and CLB instances with Anti-DDoS Pro cannot be cloned.- Classic network-based instances cannot be cloned.- Anycast instances cannot be cloned.- IPv6 NAT64 instances cannot be cloned.- Blocked or frozen instances cannot be cloned.- Before cloning an instance, make sure that all certificates used on the instance have not expired; otherwise, the cloning will fail.Quota restrictions:- Instances with more than 50 listeners cannot be cloned.- Shared instances with the public network bandwidth cap exceeding 2 Gbps cannot be cloned.API calling restrictions:The bandwidth package ID must be input for BGP bandwidth packages.Corresponding parameters should be input for cloning of an exclusive cluster; otherwise, a shared instance will be created.The feature is in beta test. You can submit a [beta test application](https://intl.cloud.tencent.com/apply/p/1akuvsmyn0g?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "CloneLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloneLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClsLogSet(
            self,
            request: models.CreateClsLogSetRequest,
            opts: Dict = None,
    ) -> models.CreateClsLogSetResponse:
        """
        This API is used to create a CLB exclusive logset for storing CLB logs.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClsLogSet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClsLogSetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateListener(
            self,
            request: models.CreateListenerRequest,
            opts: Dict = None,
    ) -> models.CreateListenerResponse:
        """
        This API is used to create a listener for a CLB instance.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestId as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLoadBalancer(
            self,
            request: models.CreateLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.CreateLoadBalancerResponse:
        """
        This API (CreateLoadBalancer) is used to create a CLB instance. To use the CLB service, you first need to purchase one or more instances. After this API is called successfully, a unique instance ID will be returned. There are two types of instances: public network and private network. For more information, see the product types in the product documentation.
        Note: (1) To apply for a CLB instance in the specified AZ and cross-AZ disaster recovery, please [submit a ticket](https://console.cloud.tencent.com/workorder/category); (2) Currently, IPv6 is supported only in Beijing, Shanghai, and Guangzhou regions.
        This is an async API. After it is returned successfully, you can call the DescribeLoadBalancers API to query the status of the instance (such as creating and normal) to check whether it is successfully created.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLoadBalancerSnatIps(
            self,
            request: models.CreateLoadBalancerSnatIpsRequest,
            opts: Dict = None,
    ) -> models.CreateLoadBalancerSnatIpsResponse:
        """
        This API is used to add an SNAT IP for an SnatPro CLB instance. If SnatPro is not enabled for CLB, it will be automatically enabled after the SNAT IP is added.
        This is an async API. After it is returned successfully, you can check the task result by calling `DescribeTaskStatus` with the returned `RequestID`.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLoadBalancerSnatIps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLoadBalancerSnatIpsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRule(
            self,
            request: models.CreateRuleRequest,
            opts: Dict = None,
    ) -> models.CreateRuleResponse:
        """
        This API (CreateRule) is used to create a forwarding rule under an existing layer-7 CLB listener, where real servers must be bound to the rule instead of the listener.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTargetGroup(
            self,
            request: models.CreateTargetGroupRequest,
            opts: Dict = None,
    ) -> models.CreateTargetGroupResponse:
        """
        This API is used to create a target group. This feature is in beta test, if you want to try it out, please [submit a ticket](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=163&source=0&data_title=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB&step=1).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTargetGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTargetGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTopic(
            self,
            request: models.CreateTopicRequest,
            opts: Dict = None,
    ) -> models.CreateTopicResponse:
        """
        This API is used to create a topic with the full-text index and key-value index enabled by default. The creation will fail if there is no CLB exclusive logset.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTopic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTopicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteListener(
            self,
            request: models.DeleteListenerRequest,
            opts: Dict = None,
    ) -> models.DeleteListenerResponse:
        """
        This API is used to delete a listener from a CLB instance (layer-4 or layer-7).
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLoadBalancer(
            self,
            request: models.DeleteLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.DeleteLoadBalancerResponse:
        """
        This API is used to delete one or more specified CLB instances. After successful deletion, the listeners and forwarding rules under the CLB instance will be deleted together, and the backend service will be unbound.
        This API is asynchronous. After it returns the result successfully, you can call the [DescribeTaskStatus](https://www.tencentcloud.com/document/product/214/30683?from_cn_redirect=1) API with the returned RequestId as an input parameter to query whether the task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLoadBalancerListeners(
            self,
            request: models.DeleteLoadBalancerListenersRequest,
            opts: Dict = None,
    ) -> models.DeleteLoadBalancerListenersResponse:
        """
        This API is used to delete multiple listeners of a CLB instance.
        This is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLoadBalancerListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLoadBalancerListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLoadBalancerSnatIps(
            self,
            request: models.DeleteLoadBalancerSnatIpsRequest,
            opts: Dict = None,
    ) -> models.DeleteLoadBalancerSnatIpsResponse:
        """
        This API is used to delete the SNAT IP for an SnatPro CLB instance.
        This is an async API. After it is returned successfully, you can check the task result by calling `DescribeTaskStatus` with the returned `RequestID`.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLoadBalancerSnatIps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLoadBalancerSnatIpsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRewrite(
            self,
            request: models.DeleteRewriteRequest,
            opts: Dict = None,
    ) -> models.DeleteRewriteResponse:
        """
        This API (DeleteRewrite) is used to delete the redirection relationship between the specified forwarding rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRewrite"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRewriteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRule(
            self,
            request: models.DeleteRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteRuleResponse:
        """
        This API (DeleteRule) is used to delete a forwarding rule under a layer-7 CLB instance listener
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRuleResponse
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
        
    async def DeregisterFunctionTargets(
            self,
            request: models.DeregisterFunctionTargetsRequest,
            opts: Dict = None,
    ) -> models.DeregisterFunctionTargetsResponse:
        """
        This API is used to unbind a SCF function with a CLB forwarding rule. For L7 listeners, you need to specify the forwarding rule by using `LocationId` or `Domain+Url`.
        This is an async API. After it is returned successfully, you can call the [DescribeTaskStatus](https://intl.cloud.tencent.com/document/product/214/30683?from_cn_redirect=1) API with the returned RequestID to check whether this task is successful.
        <br/>Limits:

        - Binding with SCF is only available in Guangzhou, Shenzhen Finance, Shanghai, Shanghai Finance, Beijing, Chengdu, Hong Kong (China), Singapore, Mumbai, Tokyo, and Silicon Valley.
        - SCF functions can only be bound with CLB instances of bill-by-IP accounts but not with bill-by-CVM accounts. If you are using a bill-by-CVM account, we recommend upgrading it to a bill-by-IP account.
        - SCF functions cannot be bound with classic CLB instances.
        - SCF functions cannot be bound with classic network-based CLB instances.
        - SCF functions in the same region can be bound with CLB instances. SCF functions can only be bound across VPCs but not regions.
        - SCF functions can only be bound with IPv4 and IPv6 NAT64 CLB instances, but currently not with IPv6 CLB instances.
        - SCF functions can only be bound with layer-7 HTTP and HTTPS listeners, but not with layer-7 QUIC listeners or layer-4 (TCP, UDP, and TCP SSL) listeners.
        - Only SCF event-triggered functions can be bound with CLB instances.
        """
        
        kwargs = {}
        kwargs["action"] = "DeregisterFunctionTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeregisterFunctionTargetsResponse
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
        This is an async API. After it is returned successfully, you can call the API `DescribeTaskStatus` with the returned RequestId as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "DeregisterTargetGroupInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeregisterTargetGroupInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeregisterTargets(
            self,
            request: models.DeregisterTargetsRequest,
            opts: Dict = None,
    ) -> models.DeregisterTargetsResponse:
        """
        This API (DeregisterTargets) is used to unbind one or more real servers from a CLB listener or forwarding rule. For layer-4 listeners, only the listener ID needs to be specified. For layer-7 listeners, the forwarding rule also needs to be specified through LocationId or Domain+Url.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "DeregisterTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeregisterTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeregisterTargetsFromClassicalLB(
            self,
            request: models.DeregisterTargetsFromClassicalLBRequest,
            opts: Dict = None,
    ) -> models.DeregisterTargetsFromClassicalLBResponse:
        """
        This API is used to unbind a CLB real server. This is an async API. After it is returned successfully, you can call the API `DescribeTaskStatus` with the returned RequestId as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "DeregisterTargetsFromClassicalLB"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeregisterTargetsFromClassicalLBResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBlockIPList(
            self,
            request: models.DescribeBlockIPListRequest,
            opts: Dict = None,
    ) -> models.DescribeBlockIPListResponse:
        """
        This API is used to query the list of blocked IPs (blocklist) of a CLB instance. (This API is in beta test. To use it, please submit a ticket.)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBlockIPList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBlockIPListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBlockIPTask(
            self,
            request: models.DescribeBlockIPTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeBlockIPTaskResponse:
        """
        This API is used to query the execution status of an async IP blocking (blocklisting) task by the async task ID returned by the `ModifyBlockIPList` API. (This API is in beta test. To use it, please submit a ticket.)
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBlockIPTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBlockIPTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClassicalLBByInstanceId(
            self,
            request: models.DescribeClassicalLBByInstanceIdRequest,
            opts: Dict = None,
    ) -> models.DescribeClassicalLBByInstanceIdResponse:
        """
        This API is used to get the list of classic CLB instance IDs through a real server ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClassicalLBByInstanceId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClassicalLBByInstanceIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClassicalLBHealthStatus(
            self,
            request: models.DescribeClassicalLBHealthStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeClassicalLBHealthStatusResponse:
        """
        This API (DescribeClassicalLBHealthStatus) is used to get the real server health status of a classic CLB
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClassicalLBHealthStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClassicalLBHealthStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClassicalLBListeners(
            self,
            request: models.DescribeClassicalLBListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeClassicalLBListenersResponse:
        """
        This API (DescribeClassicalLBListeners) is used to get the listener information of a classic CLB.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClassicalLBListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClassicalLBListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClassicalLBTargets(
            self,
            request: models.DescribeClassicalLBTargetsRequest,
            opts: Dict = None,
    ) -> models.DescribeClassicalLBTargetsResponse:
        """
        This API is used to get the real servers bound to a classic CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClassicalLBTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClassicalLBTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClsLogSet(
            self,
            request: models.DescribeClsLogSetRequest,
            opts: Dict = None,
    ) -> models.DescribeClsLogSetResponse:
        """
        This API is used to get the CLB exclusive logset.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClsLogSet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClsLogSetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCrossTargets(
            self,
            request: models.DescribeCrossTargetsRequest,
            opts: Dict = None,
    ) -> models.DescribeCrossTargetsResponse:
        """
        Queries information of CVMs and ENIs that use cross-region binding 2.0
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCrossTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCrossTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomizedConfigAssociateList(
            self,
            request: models.DescribeCustomizedConfigAssociateListRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomizedConfigAssociateListResponse:
        """
        This API is used to query the configured location, bound server or bound CLB instance. If there are domain names, the result will be filtered by domain name.
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
        This API is used to pull custom configuration lists to return the user configuration of `AppId`.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomizedConfigList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomizedConfigListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIdleLoadBalancers(
            self,
            request: models.DescribeIdleLoadBalancersRequest,
            opts: Dict = None,
    ) -> models.DescribeIdleLoadBalancersResponse:
        """
        Idle CLB instances are pay-as-you-go load balancers that, within seven days after the creation, do not have rules configured or the configured rules are not associated with any servers.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIdleLoadBalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIdleLoadBalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLBListeners(
            self,
            request: models.DescribeLBListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeLBListenersResponse:
        """
        This API is used to query CLB instances bound to the CVM or ENI.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLBListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLBListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListeners(
            self,
            request: models.DescribeListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeListenersResponse:
        """
        This API is used to get the list of listeners by CLB ID, listener protocol, or listener port. If no filter is specified, all listeners for the CLB instance will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListenersResponse
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
        
    async def DescribeLoadBalancerOverview(
            self,
            request: models.DescribeLoadBalancerOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeLoadBalancerOverviewResponse:
        """
        Queries the total number of CLB instances and the number of CLB instances in different status (running, isolated and about to expire).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoadBalancerOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoadBalancerOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoadBalancerTraffic(
            self,
            request: models.DescribeLoadBalancerTrafficRequest,
            opts: Dict = None,
    ) -> models.DescribeLoadBalancerTrafficResponse:
        """
        This API is used to query CLB instances with high traffic under the current account, and return the top 10 results. For queries using a sub-account, only the CLB instances authorized to the sub-account will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoadBalancerTraffic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoadBalancerTrafficResponse
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
        This API is used to query CLB instance details, including listener, rules, and target real servers.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoadBalancersDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoadBalancersDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQuota(
            self,
            request: models.DescribeQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeQuotaResponse:
        """
        This API is used to query various quotas in the current region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResources(
            self,
            request: models.DescribeResourcesRequest,
            opts: Dict = None,
    ) -> models.DescribeResourcesResponse:
        """
        This API is used to query the list of AZs and resources supported for the user in the current region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRewrite(
            self,
            request: models.DescribeRewriteRequest,
            opts: Dict = None,
    ) -> models.DescribeRewriteResponse:
        """
        This API (DescribeRewrite) is used to query the redirection relationship between the forwarding rules of a CLB instance by instance ID. If no listener ID or forwarding rule ID is specified, all redirection relationships in the instance will be returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRewrite"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRewriteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTargetGroupInstances(
            self,
            request: models.DescribeTargetGroupInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeTargetGroupInstancesResponse:
        """
        This API is used to get the information of servers bound to a target group.
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
        This API is used to get the target group list.
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
        This API is used to query the target group information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTargetGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTargetGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTargetHealth(
            self,
            request: models.DescribeTargetHealthRequest,
            opts: Dict = None,
    ) -> models.DescribeTargetHealthResponse:
        """
        This API (DescribeTargetHealth) is used to query the health check result of a real server of a CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTargetHealth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTargetHealthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTargets(
            self,
            request: models.DescribeTargetsRequest,
            opts: Dict = None,
    ) -> models.DescribeTargetsResponse:
        """
        This API (DescribeTargets) is used to query the list of real servers bound to some listeners of a CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskStatus(
            self,
            request: models.DescribeTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskStatusResponse:
        """
        This API is used to query the execution status of an async task. After non-query APIs (used to create/delete CLB instances, listeners, or rules or to bind/unbind real servers) are called successfully, this API needs to be used to query whether the task is successful.
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
        This API is used to unbind target groups from a rule.
        This is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateTargetGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateTargetGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceCreateLoadBalancer(
            self,
            request: models.InquiryPriceCreateLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceCreateLoadBalancerResponse:
        """
        This API is used to query the price of creating a CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceCreateLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceCreateLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceModifyLoadBalancer(
            self,
            request: models.InquiryPriceModifyLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceModifyLoadBalancerResponse:
        """
        This API is used to query the price of adjusting the specification of a CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceModifyLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceModifyLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceRefundLoadBalancer(
            self,
            request: models.InquiryPriceRefundLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceRefundLoadBalancerResponse:
        """
        This API is used to query the refund amount of returning a CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceRefundLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceRefundLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceRenewLoadBalancer(
            self,
            request: models.InquiryPriceRenewLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceRenewLoadBalancerResponse:
        """
        This API is used to query the price of renewing a CLB instance. It's only available to prepaid CLB instances.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceRenewLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceRenewLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ManualRewrite(
            self,
            request: models.ManualRewriteRequest,
            opts: Dict = None,
    ) -> models.ManualRewriteResponse:
        """
        After the original access address and the address to be redirected are configured manually, the system will automatically redirect requests made to the original access address to the target address of the corresponding path. Multiple paths can be configured as a redirection policy under one domain name to achieve automatic redirection between HTTP and HTTPS. A redirection policy should meet the following rules: if A has already been redirected to B, then it cannot be redirected to C (unless the original redirection relationship is deleted and a new one is created), and B cannot be redirected to any other addresses.
        """
        
        kwargs = {}
        kwargs["action"] = "ManualRewrite"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ManualRewriteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MigrateClassicalLoadBalancers(
            self,
            request: models.MigrateClassicalLoadBalancersRequest,
            opts: Dict = None,
    ) -> models.MigrateClassicalLoadBalancersResponse:
        """
        This API is used to upgrade classic CLB instances to application CLB instances.
        This is an async API. After it is returned successfully, you can check the action result by calling `DescribeLoadBalancers`.
        """
        
        kwargs = {}
        kwargs["action"] = "MigrateClassicalLoadBalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MigrateClassicalLoadBalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBlockIPList(
            self,
            request: models.ModifyBlockIPListRequest,
            opts: Dict = None,
    ) -> models.ModifyBlockIPListResponse:
        """
        This API is used to modify the client IP blocklist of a CLB instance. One forwarding rule supports blocking up to 2,000,000 IPs. One blocklist can contain up to 2,000,000 entries.
        (This API is in beta test. To use it, please submit a ticket.)
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBlockIPList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBlockIPListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomain(
            self,
            request: models.ModifyDomainRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainResponse:
        """
        This API (ModifyDomain) is used to modify a domain name under a layer-7 CLB listener.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomainAttributes(
            self,
            request: models.ModifyDomainAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainAttributesResponse:
        """
        This API is used to modify the domain name-level attributes of a layer-7 listener's forwarding rule, such as modifying the domain name, changing the DefaultServer, enabling/disabling HTTP/2, and modifying certificates.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestId as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomainAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFunctionTargets(
            self,
            request: models.ModifyFunctionTargetsRequest,
            opts: Dict = None,
    ) -> models.ModifyFunctionTargetsResponse:
        """
        This API is used to modify the cloud functions associated with a load balancing forwarding rule.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFunctionTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFunctionTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyListener(
            self,
            request: models.ModifyListenerRequest,
            opts: Dict = None,
    ) -> models.ModifyListenerResponse:
        """
        This API (ModifyListener) is used to modify the attributes of a CLB listener, such as listener name, health check parameter, certificate information, and forwarding policy.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoadBalancerAttributes(
            self,
            request: models.ModifyLoadBalancerAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyLoadBalancerAttributesResponse:
        """
        This API is used to modify the attributes of a CLB instance, such as name and cross-region attributes.

        Note: For CLB instances of bill-by-CVM users, cross-region attributes can be set only after a bandwidth package is purchased.This is an asynchronous API. After it returns a result successfully, the obtained RequestID should be used as an input parameter to call the DescribeTaskStatus API, for checking whether this task succeeds.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoadBalancerAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoadBalancerAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoadBalancerSla(
            self,
            request: models.ModifyLoadBalancerSlaRequest,
            opts: Dict = None,
    ) -> models.ModifyLoadBalancerSlaResponse:
        """
        This API is used to upgrade a pay-as-you-go shared CLB instance to an LCU-supported CLB instance. <br/>
        Limits
        - This API can only be used to upgrade pay-as-you-go shared instances. To upgrade monthly-subscribed shared instances, please go to the CLB console.
        - An LCU-supported instance cannot be changed back to a shared instance.
        - Classic CLB instances cannot be upgraded to LCU-supported instances.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoadBalancerSla"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoadBalancerSlaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoadBalancersProject(
            self,
            request: models.ModifyLoadBalancersProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyLoadBalancersProjectResponse:
        """
        This API is used to modify the projects of CLB instances.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoadBalancersProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoadBalancersProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRule(
            self,
            request: models.ModifyRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyRuleResponse:
        """
        This API (ModifyRule) is used to modify the attributes of a forwarding rule under a layer-7 CLB listener, such as forwarding path, health check attribute, and forwarding policy.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTargetGroupAttribute(
            self,
            request: models.ModifyTargetGroupAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyTargetGroupAttributeResponse:
        """
        This API is used to rename a target group or modify its default port attribute.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTargetGroupAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTargetGroupAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTargetGroupInstancesPort(
            self,
            request: models.ModifyTargetGroupInstancesPortRequest,
            opts: Dict = None,
    ) -> models.ModifyTargetGroupInstancesPortResponse:
        """
        This API is used to modify server ports of a target group in batches.
        This is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTargetGroupInstancesPort"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTargetGroupInstancesPortResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTargetGroupInstancesWeight(
            self,
            request: models.ModifyTargetGroupInstancesWeightRequest,
            opts: Dict = None,
    ) -> models.ModifyTargetGroupInstancesWeightResponse:
        """
        This API is used to modify server weights of a target group in batches.
        This is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTargetGroupInstancesWeight"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTargetGroupInstancesWeightResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTargetPort(
            self,
            request: models.ModifyTargetPortRequest,
            opts: Dict = None,
    ) -> models.ModifyTargetPortResponse:
        """
        This API (ModifyTargetPort) is used to modify the port of a real server bound to a listener.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTargetPort"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTargetPortResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTargetWeight(
            self,
            request: models.ModifyTargetWeightRequest,
            opts: Dict = None,
    ) -> models.ModifyTargetWeightResponse:
        """
        This API (ModifyTargetWeight) is used to modify the forwarding weight of a real server bound to a CLB instance.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTargetWeight"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTargetWeightResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterFunctionTargets(
            self,
            request: models.RegisterFunctionTargetsRequest,
            opts: Dict = None,
    ) -> models.RegisterFunctionTargetsResponse:
        """
        This API is used to bind an SCF function with the L7 forwarding rule of a CLB instance. Note that you need to create an L7 listener (HTTP, HTTPS) and forwarding rule first.
        This is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful.<br/>
        **Limits:**
        - Binding with SCF is only available in Guangzhou, Shenzhen Finance, Shanghai, Shanghai Finance, Beijing, Chengdu, Hong Kong (China), Singapore, Mumbai, Tokyo, and Silicon Valley.
        - SCF functions can only be bound with CLB instances of bill-by-IP accounts but not with bill-by-CVM accounts. If you are using a bill-by-CVM account, we recommend upgrading it to a bill-by-IP account.
        - SCF functions cannot be bound with classic CLB instances.
        - SCF functions cannot be bound with classic network-based CLB instances.
        - SCF functions in the same region can be bound with CLB instances. SCF functions can only be bound across VPCs but not regions.
        - SCF functions can only be bound with IPv4 and IPv6 NAT64 CLB instances, but currently not with IPv6 CLB instances.
        - SCF functions can only be bound with layer-7 HTTP and HTTPS listeners, but not with layer-7 QUIC listeners or layer-4 (TCP, UDP, and TCP SSL) listeners.
        - Only SCF event-triggered functions can be bound with CLB instances.
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterFunctionTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterFunctionTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterTargetGroupInstances(
            self,
            request: models.RegisterTargetGroupInstancesRequest,
            opts: Dict = None,
    ) -> models.RegisterTargetGroupInstancesResponse:
        """
        This API is used to register servers to a target group.
        This is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterTargetGroupInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterTargetGroupInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterTargets(
            self,
            request: models.RegisterTargetsRequest,
            opts: Dict = None,
    ) -> models.RegisterTargetsResponse:
        """
        This API (RegisterTargets) is used to bind one or more real servers to a CLB listener or layer-7 forwarding rule. Before using this API, you need to create relevant layer-4 listeners or layer-7 forwarding rules. For the former (TCP/UDP), only the listener ID needs to be specified, while for the latter (HTTP/HTTPS), the forwarding rule also needs to be specified through LocationId or Domain+Url.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterTargetsWithClassicalLB(
            self,
            request: models.RegisterTargetsWithClassicalLBRequest,
            opts: Dict = None,
    ) -> models.RegisterTargetsWithClassicalLBResponse:
        """
        This API is used to bind a real server with a classic CLB instance. This is an async API. After it is returned successfully, you can call the API `DescribeTaskStatus` with the returned RequestId as an input parameter to check whether this task is successful.
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterTargetsWithClassicalLB"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterTargetsWithClassicalLBResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceCertForLoadBalancers(
            self,
            request: models.ReplaceCertForLoadBalancersRequest,
            opts: Dict = None,
    ) -> models.ReplaceCertForLoadBalancersResponse:
        """
        This API (ReplaceCertForLoadBalancers) is used to replace the certificate associated with a CLB instance. A new certificates can be associated with a CLB only after the original certificate is disassociated from it.
        This API supports replacing server certificates and client certificates.
        The new certificate to be used can be specified by passing in the certificate ID. If no certificate ID is specified, relevant information such as certificate content must be passed in to create a new certificate and bind it to the CLB.
        Note: This API can only be called in the Guangzhou region; for other regions, an error will occur due to domain name resolution problems.
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceCertForLoadBalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceCertForLoadBalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetCustomizedConfigForLoadBalancer(
            self,
            request: models.SetCustomizedConfigForLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.SetCustomizedConfigForLoadBalancerResponse:
        """
        This API is used to create or manage a user-defined CLB configuration template.
        """
        
        kwargs = {}
        kwargs["action"] = "SetCustomizedConfigForLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetCustomizedConfigForLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetLoadBalancerClsLog(
            self,
            request: models.SetLoadBalancerClsLogRequest,
            opts: Dict = None,
    ) -> models.SetLoadBalancerClsLogResponse:
        """
        This API is used to add, delete, and update the CLS topic of a CLB instance.
        """
        
        kwargs = {}
        kwargs["action"] = "SetLoadBalancerClsLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetLoadBalancerClsLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetLoadBalancerSecurityGroups(
            self,
            request: models.SetLoadBalancerSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.SetLoadBalancerSecurityGroupsResponse:
        """
        This API is used to configure (bind and unbind) security groups for a public network CLB instance. You can use the DescribeLoadBalancers API to query the security groups currently bound to a CLB instance. This API follows the set semantics.For binding operations, the input parameters should specify all security groups that should be bound (have been bound and will be bound) to the CLB instance.For unbinding operations, the input parameters should specify all security groups bound to a CLB instance after unbinding. If you want to unbind all security groups, you can omit this parameter or input an empty array. Note: After a private network CLB is bound to an EIP, the security groups on the CLB do not take effect for the traffic from the EIP, but take effect for the traffic from the private network CLB.
        """
        
        kwargs = {}
        kwargs["action"] = "SetLoadBalancerSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetLoadBalancerSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetLoadBalancerStartStatus(
            self,
            request: models.SetLoadBalancerStartStatusRequest,
            opts: Dict = None,
    ) -> models.SetLoadBalancerStartStatusResponse:
        """
        This API is used to enable or disable a CLB instance or listener.This is an asynchronous API. After it returns a result successfully, the obtained RequestID should be used as an input parameter to call the DescribeTaskStatus API, for checking whether this task succeeds.This feature is currently in beta test. To use it, submit a [ticket](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=163&source=0&data_title=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB&step=1) for application.
        """
        
        kwargs = {}
        kwargs["action"] = "SetLoadBalancerStartStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetLoadBalancerStartStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetSecurityGroupForLoadbalancers(
            self,
            request: models.SetSecurityGroupForLoadbalancersRequest,
            opts: Dict = None,
    ) -> models.SetSecurityGroupForLoadbalancersResponse:
        """
        This API is used to bind or unbind a security group for multiple public network CLB instances. Note: Private network CLB do not support binding security groups.
        """
        
        kwargs = {}
        kwargs["action"] = "SetSecurityGroupForLoadbalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetSecurityGroupForLoadbalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)