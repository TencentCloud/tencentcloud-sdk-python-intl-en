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
from tencentcloud.clb.v20180317 import models


class ClbClient(AbstractClient):
    _apiVersion = '2018-03-17'
    _endpoint = 'clb.tencentcloudapi.com'
    _service = 'clb'


    def AssociateTargetGroups(self, request):
        """This API is used to bind target groups to CLB listeners (layer-4 protocol) or forwarding rules (layer-7 protocol).
        This is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful.

        :param request: Request instance for AssociateTargetGroups.
        :type request: :class:`tencentcloud.clb.v20180317.models.AssociateTargetGroupsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.AssociateTargetGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateTargetGroups", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateTargetGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AutoRewrite(self, request):
        """An HTTPS:443 listener needs to be created first, along with a forwarding rule. When this API is called, an HTTP:80 listener will be created automatically if it did not exist and a forwarding rule corresponding to `Domains` (specified in the input parameter) under the HTTPS:443 listener will also be created. After successful creation, access requests to an HTTP:80 address will be redirected to an HTTPS:443 address automatically.

        :param request: Request instance for AutoRewrite.
        :type request: :class:`tencentcloud.clb.v20180317.models.AutoRewriteRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.AutoRewriteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AutoRewrite", params, headers=headers)
            response = json.loads(body)
            model = models.AutoRewriteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchDeregisterTargets(self, request):
        """This API is used to batch unbind real servers of the layer-4 and layer-7 VPC-based CLBs. Up to 500 real servers can be unbound in a batch.

        :param request: Request instance for BatchDeregisterTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.BatchDeregisterTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.BatchDeregisterTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeregisterTargets", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeregisterTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchModifyTargetWeight(self, request):
        """This API is used to modify forwarding weights of real servers bound to CLB listeners in batches. Up to 500 servers can be unbound in a batch. As this API is async, you should check whether the task is successful by passing the RequestId returned to the API call `DescribeTaskStatus`.<br/> This API is supported by CLB layer-4 and layer-7 listeners, but not Classis CLB counterparts.

        :param request: Request instance for BatchModifyTargetWeight.
        :type request: :class:`tencentcloud.clb.v20180317.models.BatchModifyTargetWeightRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.BatchModifyTargetWeightResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyTargetWeight", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyTargetWeightResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchRegisterTargets(self, request):
        """This API is used to batch bind CVM instances or ENIs. Up to 500 servers can be bound in a batch. It supports cross-region binding, layer-4 and layer-7 (TCP/UDP/HTTP/HTTPS) protocols, and VPC-based CLBs only.

        :param request: Request instance for BatchRegisterTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.BatchRegisterTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.BatchRegisterTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchRegisterTargets", params, headers=headers)
            response = json.loads(body)
            model = models.BatchRegisterTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloneLoadBalancer(self, request):
        """This API is used to create a clone of the source CLB instance with the same forwarding rules and binding relations. Note that this API is asynchronous, which means that changes to the source CLB after invocation of the API are not included in the clone.

        Use limits:
        Unsupported instance types: Classic network CLB, Classic CLB, IPv6 CLB, and NAT64 CLB.
        Monthly subscribed CLB instances are not supported.
        QUIC and port listeners are not supported.
        The CLB backend service cannot be a target group or an SCF function.
        The following settings will not be cloned automatically and require manual configuration: "Custom Configuration", "Redirection Configuration" and "Allow Traffic by Default in Security Group".

        Notes:
        If you are using a BGP bandwidth package, you need to pass the package ID.
        To create a dedicated cluster-based CLB by cloning the source CLB, you need to pass the cluster ID. Otherwise, a normal CLB is created.
        This API is only available for beta users. If you want to try it out, please [submit a ticket](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=163&source=0&data_title=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20CLB&step=1).

        :param request: Request instance for CloneLoadBalancer.
        :type request: :class:`tencentcloud.clb.v20180317.models.CloneLoadBalancerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CloneLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloneLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.CloneLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClsLogSet(self, request):
        """This API is used to create a CLB exclusive logset for storing CLB logs.

        :param request: Request instance for CreateClsLogSet.
        :type request: :class:`tencentcloud.clb.v20180317.models.CreateClsLogSetRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CreateClsLogSetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClsLogSet", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClsLogSetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateListener(self, request):
        """This API is used to create a listener for a CLB instance.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestId as an input parameter to check whether this task is successful.

        :param request: Request instance for CreateListener.
        :type request: :class:`tencentcloud.clb.v20180317.models.CreateListenerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CreateListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateListener", params, headers=headers)
            response = json.loads(body)
            model = models.CreateListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLoadBalancer(self, request):
        """This API (CreateLoadBalancer) is used to create a CLB instance. To use the CLB service, you first need to purchase one or more instances. After this API is called successfully, a unique instance ID will be returned. There are two types of instances: public network and private network. For more information, see the product types in the product documentation.
        Note: (1) To apply for a CLB instance in the specified AZ and cross-AZ disaster recovery, please [submit a ticket](https://console.cloud.tencent.com/workorder/category); (2) Currently, IPv6 is supported only in Beijing, Shanghai, and Guangzhou regions.
        This is an async API. After it is returned successfully, you can call the DescribeLoadBalancers API to query the status of the instance (such as creating and normal) to check whether it is successfully created.

        :param request: Request instance for CreateLoadBalancer.
        :type request: :class:`tencentcloud.clb.v20180317.models.CreateLoadBalancerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CreateLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLoadBalancerSnatIps(self, request):
        """This API is used to add an SNAT IP for an SnatPro CLB instance. If SnatPro is not enabled for CLB, it will be automatically enabled after the SNAT IP is added.
        This is an async API. After it is returned successfully, you can check the task result by calling `DescribeTaskStatus` with the returned `RequestID`.

        :param request: Request instance for CreateLoadBalancerSnatIps.
        :type request: :class:`tencentcloud.clb.v20180317.models.CreateLoadBalancerSnatIpsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CreateLoadBalancerSnatIpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLoadBalancerSnatIps", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLoadBalancerSnatIpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRule(self, request):
        """This API (CreateRule) is used to create a forwarding rule under an existing layer-7 CLB listener, where real servers must be bound to the rule instead of the listener.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for CreateRule.
        :type request: :class:`tencentcloud.clb.v20180317.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CreateRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTargetGroup(self, request):
        """This API is used to create a target group. This feature is in beta test, if you want to try it out, please [submit a ticket](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=163&source=0&data_title=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB&step=1).

        :param request: Request instance for CreateTargetGroup.
        :type request: :class:`tencentcloud.clb.v20180317.models.CreateTargetGroupRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CreateTargetGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTargetGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTargetGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTopic(self, request):
        """This API is used to create a topic with the full-text index and key-value index enabled by default. The creation will fail if there is no CLB exclusive logset.

        :param request: Request instance for CreateTopic.
        :type request: :class:`tencentcloud.clb.v20180317.models.CreateTopicRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CreateTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTopic", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteListener(self, request):
        """This API is used to delete a listener from a CLB instance (layer-4 or layer-7).
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for DeleteListener.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteListenerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteListener", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLoadBalancer(self, request):
        """This API (DeleteLoadBalancer) is used to delete one or more specified CLB instances.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestId as an input parameter to check whether this task is successful.

        :param request: Request instance for DeleteLoadBalancer.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteLoadBalancerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLoadBalancerListeners(self, request):
        """This API is used to delete multiple listeners of a CLB instance.
        This is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful.

        :param request: Request instance for DeleteLoadBalancerListeners.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteLoadBalancerListenersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteLoadBalancerListenersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoadBalancerListeners", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoadBalancerListenersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLoadBalancerSnatIps(self, request):
        """This API is used to delete the SNAT IP for an SnatPro CLB instance.
        This is an async API. After it is returned successfully, you can check the task result by calling `DescribeTaskStatus` with the returned `RequestID`.

        :param request: Request instance for DeleteLoadBalancerSnatIps.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteLoadBalancerSnatIpsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteLoadBalancerSnatIpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoadBalancerSnatIps", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoadBalancerSnatIpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRewrite(self, request):
        """This API (DeleteRewrite) is used to delete the redirection relationship between the specified forwarding rules.

        :param request: Request instance for DeleteRewrite.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteRewriteRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteRewriteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRewrite", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRewriteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRule(self, request):
        """This API (DeleteRule) is used to delete a forwarding rule under a layer-7 CLB instance listener
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for DeleteRule.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteRuleRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTargetGroups(self, request):
        """This API is used to delete a target group.

        :param request: Request instance for DeleteTargetGroups.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteTargetGroupsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteTargetGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTargetGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTargetGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeregisterFunctionTargets(self, request):
        """This API is used to unbind a SCF function with a CLB forwarding rule. For L7 listeners, you need to specify the forwarding rule by using `LocationId` or `Domain+Url`.
        This is an async API. After it is returned successfully, you can call the [DescribeTaskStatus](https://intl.cloud.tencent.com/document/product/214/30683?from_cn_redirect=1) API with the returned RequestID to check whether this task is successful.
        <br/>Limits:

        - Binding with SCF is only available in Guangzhou, Shenzhen Finance, Shanghai, Shanghai Finance, Beijing, Chengdu, Hong Kong (China), Singapore, Mumbai, Tokyo, and Silicon Valley.
        - SCF functions can only be bound with CLB instances of bill-by-IP accounts but not with bill-by-CVM accounts. If you are using a bill-by-CVM account, we recommend upgrading it to a bill-by-IP account. For more information, please see [Checking Account Type](https://intl.cloud.tencent.com/document/product/1199/49090?from_cn_redirect=1).
        - SCF functions cannot be bound with classic CLB instances.
        - SCF functions cannot be bound with classic network-based CLB instances.
        - SCF functions in the same region can be bound with CLB instances. SCF functions can only be bound across VPCs but not regions.
        - SCF functions can only be bound with IPv4 and IPv6 NAT64 CLB instances, but currently not with IPv6 CLB instances.
        - SCF functions can only be bound with layer-7 HTTP and HTTPS listeners, but not with layer-7 QUIC listeners or layer-4 (TCP, UDP, and TCP SSL) listeners.
        - Only SCF event-triggered functions can be bound with CLB instances.

        :param request: Request instance for DeregisterFunctionTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeregisterFunctionTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeregisterFunctionTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeregisterFunctionTargets", params, headers=headers)
            response = json.loads(body)
            model = models.DeregisterFunctionTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeregisterTargetGroupInstances(self, request):
        """This API is used to unbind a server from a target group.
        This is an async API. After it is returned successfully, you can call the API `DescribeTaskStatus` with the returned RequestId as an input parameter to check whether this task is successful.

        :param request: Request instance for DeregisterTargetGroupInstances.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetGroupInstancesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetGroupInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeregisterTargetGroupInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DeregisterTargetGroupInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeregisterTargets(self, request):
        """This API (DeregisterTargets) is used to unbind one or more real servers from a CLB listener or forwarding rule. For layer-4 listeners, only the listener ID needs to be specified. For layer-7 listeners, the forwarding rule also needs to be specified through LocationId or Domain+Url.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for DeregisterTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeregisterTargets", params, headers=headers)
            response = json.loads(body)
            model = models.DeregisterTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeregisterTargetsFromClassicalLB(self, request):
        """This API is used to unbind a CLB real server. This is an async API. After it is returned successfully, you can call the API `DescribeTaskStatus` with the returned RequestId as an input parameter to check whether this task is successful.

        :param request: Request instance for DeregisterTargetsFromClassicalLB.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetsFromClassicalLBRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetsFromClassicalLBResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeregisterTargetsFromClassicalLB", params, headers=headers)
            response = json.loads(body)
            model = models.DeregisterTargetsFromClassicalLBResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBlockIPList(self, request):
        """This API is used to query the list of blocked IPs (blocklist) of a CLB instance. (This API is in beta test. To use it, please submit a ticket.)

        :param request: Request instance for DescribeBlockIPList.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeBlockIPListRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeBlockIPListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBlockIPList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBlockIPListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBlockIPTask(self, request):
        """This API is used to query the execution status of an async IP blocking (blocklisting) task by the async task ID returned by the `ModifyBlockIPList` API. (This API is in beta test. To use it, please submit a ticket.)

        :param request: Request instance for DescribeBlockIPTask.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeBlockIPTaskRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeBlockIPTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBlockIPTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBlockIPTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClassicalLBByInstanceId(self, request):
        """This API is used to get the list of classic CLB instance IDs through a real server ID.

        :param request: Request instance for DescribeClassicalLBByInstanceId.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBByInstanceIdRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBByInstanceIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClassicalLBByInstanceId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClassicalLBByInstanceIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClassicalLBHealthStatus(self, request):
        """This API (DescribeClassicalLBHealthStatus) is used to get the real server health status of a classic CLB

        :param request: Request instance for DescribeClassicalLBHealthStatus.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBHealthStatusRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBHealthStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClassicalLBHealthStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClassicalLBHealthStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClassicalLBListeners(self, request):
        """This API (DescribeClassicalLBListeners) is used to get the listener information of a classic CLB.

        :param request: Request instance for DescribeClassicalLBListeners.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBListenersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBListenersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClassicalLBListeners", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClassicalLBListenersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClassicalLBTargets(self, request):
        """This API is used to get the real servers bound to a classic CLB instance.

        :param request: Request instance for DescribeClassicalLBTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClassicalLBTargets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClassicalLBTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClsLogSet(self, request):
        """This API is used to get the CLB exclusive logset.

        :param request: Request instance for DescribeClsLogSet.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeClsLogSetRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeClsLogSetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClsLogSet", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClsLogSetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCrossTargets(self, request):
        """Queries information of CVMs and ENIs that use cross-region binding 2.0

        :param request: Request instance for DescribeCrossTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeCrossTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeCrossTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCrossTargets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCrossTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomizedConfigAssociateList(self, request):
        """This API is used to query the configured location, bound server or bound CLB instance. If there are domain names, the result will be filtered by domain name.

        :param request: Request instance for DescribeCustomizedConfigAssociateList.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeCustomizedConfigAssociateListRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeCustomizedConfigAssociateListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomizedConfigAssociateList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomizedConfigAssociateListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomizedConfigList(self, request):
        """This API is used to pull custom configuration lists to return the user configuration of `AppId`.

        :param request: Request instance for DescribeCustomizedConfigList.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeCustomizedConfigListRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeCustomizedConfigListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomizedConfigList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomizedConfigListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIdleLoadBalancers(self, request):
        """Idle CLB instances are pay-as-you-go load balancers that, within seven days after the creation, do not have rules configured or the configured rules are not associated with any servers.

        :param request: Request instance for DescribeIdleLoadBalancers.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeIdleLoadBalancersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeIdleLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIdleLoadBalancers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIdleLoadBalancersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLBListeners(self, request):
        """This API is used to query CLB instances bound to the CVM or ENI.

        :param request: Request instance for DescribeLBListeners.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeLBListenersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeLBListenersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLBListeners", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLBListenersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListeners(self, request):
        """This API is used to get the list of listeners by CLB ID, listener protocol, or listener port. If no filter is specified, all listeners for the CLB instance will be returned.

        :param request: Request instance for DescribeListeners.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeListenersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeListenersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListeners", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListenersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoadBalancerListByCertId(self, request):
        """This API is used to query the list of CLB instances associated with a certificate in a region by certificate ID.

        :param request: Request instance for DescribeLoadBalancerListByCertId.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancerListByCertIdRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancerListByCertIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalancerListByCertId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoadBalancerListByCertIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoadBalancerOverview(self, request):
        """Queries the total number of CLB instances and the number of CLB instances in different status (running, isolated and about to expire).

        :param request: Request instance for DescribeLoadBalancerOverview.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancerOverviewRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancerOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalancerOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoadBalancerOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoadBalancerTraffic(self, request):
        """This API is used to query CLB instances with high traffic under the current account, and return the top 10 results. For queries using a sub-account, only the CLB instances authorized to the sub-account will be returned.

        :param request: Request instance for DescribeLoadBalancerTraffic.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancerTrafficRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancerTrafficResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalancerTraffic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoadBalancerTrafficResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoadBalancers(self, request):
        """This API is used to query the list of CLB instances in a region.

        :param request: Request instance for DescribeLoadBalancers.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalancers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoadBalancersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoadBalancersDetail(self, request):
        """This API is used to query CLB instance details, including listener, rules, and target real servers.

        :param request: Request instance for DescribeLoadBalancersDetail.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancersDetailRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancersDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalancersDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoadBalancersDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQuota(self, request):
        """This API is used to query various quotas in the current region.

        :param request: Request instance for DescribeQuota.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeQuotaRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResources(self, request):
        """This API is used to query the list of AZs and resources supported for the user in the current region.

        :param request: Request instance for DescribeResources.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeResourcesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRewrite(self, request):
        """This API (DescribeRewrite) is used to query the redirection relationship between the forwarding rules of a CLB instance by instance ID. If no listener ID or forwarding rule ID is specified, all redirection relationships in the instance will be returned.

        :param request: Request instance for DescribeRewrite.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeRewriteRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeRewriteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRewrite", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRewriteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargetGroupInstances(self, request):
        """This API is used to get the information of servers bound to a target group.

        :param request: Request instance for DescribeTargetGroupInstances.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupInstancesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargetGroupInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetGroupInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargetGroupList(self, request):
        """This API is used to get the target group list.

        :param request: Request instance for DescribeTargetGroupList.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupListRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargetGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargetGroups(self, request):
        """This API is used to query the target group information.

        :param request: Request instance for DescribeTargetGroups.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargetGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargetHealth(self, request):
        """This API (DescribeTargetHealth) is used to query the health check result of a real server of a CLB instance.

        :param request: Request instance for DescribeTargetHealth.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTargetHealthRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTargetHealthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargetHealth", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetHealthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargets(self, request):
        """This API (DescribeTargets) is used to query the list of real servers bound to some listeners of a CLB instance.

        :param request: Request instance for DescribeTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskStatus(self, request):
        """This API is used to query the execution status of an async task. After non-query APIs (used to create/delete CLB instances, listeners, or rules or to bind/unbind real servers) are called successfully, this API needs to be used to query whether the task is successful.

        :param request: Request instance for DescribeTaskStatus.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTaskStatusRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateTargetGroups(self, request):
        """This API is used to unbind target groups from a rule.
        This is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful.

        :param request: Request instance for DisassociateTargetGroups.
        :type request: :class:`tencentcloud.clb.v20180317.models.DisassociateTargetGroupsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DisassociateTargetGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateTargetGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateTargetGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ManualRewrite(self, request):
        """After the original access address and the address to be redirected are configured manually, the system will automatically redirect requests made to the original access address to the target address of the corresponding path. Multiple paths can be configured as a redirection policy under one domain name to achieve automatic redirection between HTTP and HTTPS. A redirection policy should meet the following rules: if A has already been redirected to B, then it cannot be redirected to C (unless the original redirection relationship is deleted and a new one is created), and B cannot be redirected to any other addresses.

        :param request: Request instance for ManualRewrite.
        :type request: :class:`tencentcloud.clb.v20180317.models.ManualRewriteRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ManualRewriteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ManualRewrite", params, headers=headers)
            response = json.loads(body)
            model = models.ManualRewriteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MigrateClassicalLoadBalancers(self, request):
        """This API is used to upgrade classic CLB instances to application CLB instances.
        This is an async API. After it is returned successfully, you can check the action result by calling `DescribeLoadBalancers`.

        :param request: Request instance for MigrateClassicalLoadBalancers.
        :type request: :class:`tencentcloud.clb.v20180317.models.MigrateClassicalLoadBalancersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.MigrateClassicalLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MigrateClassicalLoadBalancers", params, headers=headers)
            response = json.loads(body)
            model = models.MigrateClassicalLoadBalancersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBlockIPList(self, request):
        """This API is used to modify the client IP blocklist of a CLB instance. One forwarding rule supports blocking up to 2,000,000 IPs. One blocklist can contain up to 2,000,000 entries.
        (This API is in beta test. To use it, please submit a ticket.)

        :param request: Request instance for ModifyBlockIPList.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyBlockIPListRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyBlockIPListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBlockIPList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBlockIPListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomain(self, request):
        """This API (ModifyDomain) is used to modify a domain name under a layer-7 CLB listener.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for ModifyDomain.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyDomainRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainAttributes(self, request):
        """This API is used to modify the domain name-level attributes of a layer-7 listener's forwarding rule, such as modifying the domain name, changing the DefaultServer, enabling/disabling HTTP/2, and modifying certificates.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestId as an input parameter to check whether this task is successful.

        :param request: Request instance for ModifyDomainAttributes.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyDomainAttributesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyDomainAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFunctionTargets(self, request):
        """This API is used to modify the cloud functions associated with a load balancing forwarding rule.

        :param request: Request instance for ModifyFunctionTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyFunctionTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyFunctionTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFunctionTargets", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFunctionTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyListener(self, request):
        """This API (ModifyListener) is used to modify the attributes of a CLB listener, such as listener name, health check parameter, certificate information, and forwarding policy.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for ModifyListener.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyListenerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyListener", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoadBalancerAttributes(self, request):
        """This API is used to modify the attributes of a CLB instance such as name and cross-region attributes.
        This is an async API. After it is returned successfully, you can check the task result by calling `DescribeTaskStatus` with the returned `RequestID`.

        :param request: Request instance for ModifyLoadBalancerAttributes.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyLoadBalancerAttributesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyLoadBalancerAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoadBalancerAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoadBalancerAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoadBalancerSla(self, request):
        """This API is used to upgrade a pay-as-you-go shared CLB instance to an LCU-supported CLB instance.<br/>
        Limits
        - This API can be used to upgrade only a pay-as-you-go shared instance. A monthly subscription shared instance must be upgraded in the console.
        - An LCU-supported instance cannot be rolled back to a shared instance.
        - LCU-supported instances are in beta testing. To upgrade to an LCU-supported instance, [submit a ticket](https://intl.cloud.tencent.com/apply/p/hf45esx99lf?from_cn_redirect=1) for application.
        - Classic CLB instances cannot be upgraded to LCU-supported instances.

        :param request: Request instance for ModifyLoadBalancerSla.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyLoadBalancerSlaRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyLoadBalancerSlaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoadBalancerSla", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoadBalancerSlaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRule(self, request):
        """This API (ModifyRule) is used to modify the attributes of a forwarding rule under a layer-7 CLB listener, such as forwarding path, health check attribute, and forwarding policy.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for ModifyRule.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyRuleRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTargetGroupAttribute(self, request):
        """This API is used to rename a target group or modify its default port attribute.

        :param request: Request instance for ModifyTargetGroupAttribute.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupAttributeRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTargetGroupAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTargetGroupAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTargetGroupInstancesPort(self, request):
        """This API is used to modify server ports of a target group in batches.
        This is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful.

        :param request: Request instance for ModifyTargetGroupInstancesPort.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupInstancesPortRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupInstancesPortResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTargetGroupInstancesPort", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTargetGroupInstancesPortResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTargetGroupInstancesWeight(self, request):
        """This API is used to modify server weights of a target group in batches.
        This is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful.

        :param request: Request instance for ModifyTargetGroupInstancesWeight.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupInstancesWeightRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupInstancesWeightResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTargetGroupInstancesWeight", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTargetGroupInstancesWeightResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTargetPort(self, request):
        """This API (ModifyTargetPort) is used to modify the port of a real server bound to a listener.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for ModifyTargetPort.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyTargetPortRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyTargetPortResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTargetPort", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTargetPortResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTargetWeight(self, request):
        """This API (ModifyTargetWeight) is used to modify the forwarding weight of a real server bound to a CLB instance.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for ModifyTargetWeight.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyTargetWeightRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyTargetWeightResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTargetWeight", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTargetWeightResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterFunctionTargets(self, request):
        """This API is used to bind an SCF function with the L7 forwarding rule of a CLB instance. Note that you need to create an L7 listener (HTTP, HTTPS) and forwarding rule first.
        This is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful.<br/>
        **Limits:**
        - Binding with SCF is only available in Guangzhou, Shenzhen Finance, Shanghai, Shanghai Finance, Beijing, Chengdu, Hong Kong (China), Singapore, Mumbai, Tokyo, and Silicon Valley.
        - SCF functions can only be bound with CLB instances of bill-by-IP accounts but not with bill-by-CVM accounts. If you are using a bill-by-CVM account, we recommend upgrading it to a bill-by-IP account. For more information, please see [Checking Account Type](https://intl.cloud.tencent.com/document/product/1199/49090?from_cn_redirect=1).
        - SCF functions cannot be bound with classic CLB instances.
        - SCF functions cannot be bound with classic network-based CLB instances.
        - SCF functions in the same region can be bound with CLB instances. SCF functions can only be bound across VPCs but not regions.
        - SCF functions can only be bound with IPv4 and IPv6 NAT64 CLB instances, but currently not with IPv6 CLB instances.
        - SCF functions can only be bound with layer-7 HTTP and HTTPS listeners, but not with layer-7 QUIC listeners or layer-4 (TCP, UDP, and TCP SSL) listeners.
        - Only SCF event-triggered functions can be bound with CLB instances.

        :param request: Request instance for RegisterFunctionTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.RegisterFunctionTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.RegisterFunctionTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterFunctionTargets", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterFunctionTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterTargetGroupInstances(self, request):
        """This API is used to register servers to a target group.
        This is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful.

        :param request: Request instance for RegisterTargetGroupInstances.
        :type request: :class:`tencentcloud.clb.v20180317.models.RegisterTargetGroupInstancesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.RegisterTargetGroupInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterTargetGroupInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterTargetGroupInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterTargets(self, request):
        """This API (RegisterTargets) is used to bind one or more real servers to a CLB listener or layer-7 forwarding rule. Before using this API, you need to create relevant layer-4 listeners or layer-7 forwarding rules. For the former (TCP/UDP), only the listener ID needs to be specified, while for the latter (HTTP/HTTPS), the forwarding rule also needs to be specified through LocationId or Domain+Url.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for RegisterTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.RegisterTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.RegisterTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterTargets", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RegisterTargetsWithClassicalLB(self, request):
        """This API is used to bind a real server with a classic CLB instance. This is an async API. After it is returned successfully, you can call the API `DescribeTaskStatus` with the returned RequestId as an input parameter to check whether this task is successful.

        :param request: Request instance for RegisterTargetsWithClassicalLB.
        :type request: :class:`tencentcloud.clb.v20180317.models.RegisterTargetsWithClassicalLBRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.RegisterTargetsWithClassicalLBResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterTargetsWithClassicalLB", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterTargetsWithClassicalLBResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplaceCertForLoadBalancers(self, request):
        """This API (ReplaceCertForLoadBalancers) is used to replace the certificate associated with a CLB instance. A new certificates can be associated with a CLB only after the original certificate is disassociated from it.
        This API supports replacing server certificates and client certificates.
        The new certificate to be used can be specified by passing in the certificate ID. If no certificate ID is specified, relevant information such as certificate content must be passed in to create a new certificate and bind it to the CLB.
        Note: This API can only be called in the Guangzhou region; for other regions, an error will occur due to domain name resolution problems.

        :param request: Request instance for ReplaceCertForLoadBalancers.
        :type request: :class:`tencentcloud.clb.v20180317.models.ReplaceCertForLoadBalancersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ReplaceCertForLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceCertForLoadBalancers", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceCertForLoadBalancersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetCustomizedConfigForLoadBalancer(self, request):
        """This API is used to create or manage a user-defined CLB configuration template.

        :param request: Request instance for SetCustomizedConfigForLoadBalancer.
        :type request: :class:`tencentcloud.clb.v20180317.models.SetCustomizedConfigForLoadBalancerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.SetCustomizedConfigForLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetCustomizedConfigForLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.SetCustomizedConfigForLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetLoadBalancerClsLog(self, request):
        """This API is used to add, delete, and update the CLS topic of a CLB instance.

        :param request: Request instance for SetLoadBalancerClsLog.
        :type request: :class:`tencentcloud.clb.v20180317.models.SetLoadBalancerClsLogRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.SetLoadBalancerClsLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetLoadBalancerClsLog", params, headers=headers)
            response = json.loads(body)
            model = models.SetLoadBalancerClsLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetLoadBalancerSecurityGroups(self, request):
        """This API (SetLoadBalancerSecurityGroups) is used to bind/unbind security groups for a public network CLB instance. You can use the DescribeLoadBalancers API to query the security groups bound to a CLB instance. This API uses `set` semantics.
        During a binding operation, the input parameters need to be all security groups to be bound to the CLB instance (including those already bound ones and new ones).
        During an unbinding operation, the input parameters need to be all the security groups still bound to the CLB instance after the unbinding operation. To unbind all security groups, you can leave this parameter empty or pass in an empty array. Note: Private network CLB do not support binding security groups.

        :param request: Request instance for SetLoadBalancerSecurityGroups.
        :type request: :class:`tencentcloud.clb.v20180317.models.SetLoadBalancerSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.SetLoadBalancerSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetLoadBalancerSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.SetLoadBalancerSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetSecurityGroupForLoadbalancers(self, request):
        """This API is used to bind or unbind a security group for multiple public network CLB instances. Note: Private network CLB do not support binding security groups.

        :param request: Request instance for SetSecurityGroupForLoadbalancers.
        :type request: :class:`tencentcloud.clb.v20180317.models.SetSecurityGroupForLoadbalancersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.SetSecurityGroupForLoadbalancersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetSecurityGroupForLoadbalancers", params, headers=headers)
            response = json.loads(body)
            model = models.SetSecurityGroupForLoadbalancersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))