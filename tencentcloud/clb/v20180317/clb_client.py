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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.clb.v20180317 import models


class ClbClient(AbstractClient):
    _apiVersion = '2018-03-17'
    _endpoint = 'clb.tencentcloudapi.com'


    def AssociateTargetGroups(self, request):
        """This API is used to bind target groups to CLB listeners (layer-4 protocol) or forwarding rules (layer-7 protocol).
        This is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful.

        :param request: Request instance for AssociateTargetGroups.
        :type request: :class:`tencentcloud.clb.v20180317.models.AssociateTargetGroupsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.AssociateTargetGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateTargetGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateTargetGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AutoRewrite(self, request):
        """An HTTPS:443 listener needs to be created first, along with a forwarding rule. When this API is called, an HTTP:80 listener will be created automatically if it did not exist and a forwarding rule corresponding to `Domains` (specified in the input parameter) under the HTTPS:443 listener will also be created. After successful creation, access requests to an HTTP:80 address will be redirected to an HTTPS:443 address automatically.

        :param request: Request instance for AutoRewrite.
        :type request: :class:`tencentcloud.clb.v20180317.models.AutoRewriteRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.AutoRewriteResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AutoRewrite", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AutoRewriteResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchDeregisterTargets(self, request):
        """This API is used to unbind layer-4/layer-7 real servers in batches.

        :param request: Request instance for BatchDeregisterTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.BatchDeregisterTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.BatchDeregisterTargetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BatchDeregisterTargets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BatchDeregisterTargetsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchModifyTargetWeight(self, request):
        """This API is used to modify the forwarding weights of real servers bound to a CLB listener in batches. It supports layer-4 and layer-7 CLB listeners but not Classic CLB.
        This is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful.

        :param request: Request instance for BatchModifyTargetWeight.
        :type request: :class:`tencentcloud.clb.v20180317.models.BatchModifyTargetWeightRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.BatchModifyTargetWeightResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BatchModifyTargetWeight", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BatchModifyTargetWeightResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchRegisterTargets(self, request):
        """This API is used to bind CVM instances or ENIs in batches. It supports cross-region binding and layer-4 and layer-7 (TCP, UDP, HTTP, HTTPS) protocols.

        :param request: Request instance for BatchRegisterTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.BatchRegisterTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.BatchRegisterTargetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BatchRegisterTargets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BatchRegisterTargetsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateListener(self, request):
        """This API is used to create a listener for a CLB instance.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestId as an input parameter to check whether this task is successful.

        :param request: Request instance for CreateListener.
        :type request: :class:`tencentcloud.clb.v20180317.models.CreateListenerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CreateListenerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateListener", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateListenerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("CreateLoadBalancer", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLoadBalancerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRule(self, request):
        """This API (CreateRule) is used to create a forwarding rule under an existing layer-7 CLB listener, where real servers must be bound to the rule instead of the listener.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for CreateRule.
        :type request: :class:`tencentcloud.clb.v20180317.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CreateRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTargetGroup(self, request):
        """This API is used to create a target group. This feature is in beta test, if you want to try it out, please [submit a ticket](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=163&source=0&data_title=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB&step=1).

        :param request: Request instance for CreateTargetGroup.
        :type request: :class:`tencentcloud.clb.v20180317.models.CreateTargetGroupRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.CreateTargetGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTargetGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTargetGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteListener(self, request):
        """This API is used to delete a listener from a CLB instance (layer-4 or layer-7).
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for DeleteListener.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteListenerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteListenerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteListener", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteListenerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLoadBalancer(self, request):
        """This API (DeleteLoadBalancer) is used to delete one or more specified CLB instances.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestId as an input parameter to check whether this task is successful.

        :param request: Request instance for DeleteLoadBalancer.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteLoadBalancerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLoadBalancer", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLoadBalancerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRewrite(self, request):
        """This API (DeleteRewrite) is used to delete the redirection relationship between the specified forwarding rules.

        :param request: Request instance for DeleteRewrite.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteRewriteRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteRewriteResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRewrite", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRewriteResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRule(self, request):
        """This API (DeleteRule) is used to delete a forwarding rule under a layer-7 CLB instance listener
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for DeleteRule.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteRuleRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteTargetGroups(self, request):
        """This API is used to delete a target group.

        :param request: Request instance for DeleteTargetGroups.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeleteTargetGroupsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeleteTargetGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTargetGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTargetGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeregisterTargetGroupInstances(self, request):
        """This API is used to unbind a server from a target group.
        This is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful.

        :param request: Request instance for DeregisterTargetGroupInstances.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetGroupInstancesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetGroupInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeregisterTargetGroupInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeregisterTargetGroupInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeregisterTargets(self, request):
        """This API (DeregisterTargets) is used to unbind one or more real servers from a CLB listener or forwarding rule. For layer-4 listeners, only the listener ID needs to be specified. For layer-7 listeners, the forwarding rule also needs to be specified through LocationId or Domain+Url.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for DeregisterTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeregisterTargets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeregisterTargetsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeregisterTargetsFromClassicalLB(self, request):
        """This API (DeregisterTargetsFromClassicalLB) is used to unbind real servers from a classic load balancer.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestId as an input parameter to check whether this task is successful.

        :param request: Request instance for DeregisterTargetsFromClassicalLB.
        :type request: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetsFromClassicalLBRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DeregisterTargetsFromClassicalLBResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeregisterTargetsFromClassicalLB", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeregisterTargetsFromClassicalLBResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClassicalLBByInstanceId(self, request):
        """This API (DescribeClassicalLBByInstanceId) is used to get the list of classic CLB IDs through the real server instance ID.

        :param request: Request instance for DescribeClassicalLBByInstanceId.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBByInstanceIdRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBByInstanceIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClassicalLBByInstanceId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClassicalLBByInstanceIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClassicalLBHealthStatus(self, request):
        """This API (DescribeClassicalLBHealthStatus) is used to get the real server health status of a classic CLB

        :param request: Request instance for DescribeClassicalLBHealthStatus.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBHealthStatusRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBHealthStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClassicalLBHealthStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClassicalLBHealthStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClassicalLBListeners(self, request):
        """This API (DescribeClassicalLBListeners) is used to get the listener information of a classic CLB.

        :param request: Request instance for DescribeClassicalLBListeners.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBListenersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClassicalLBListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClassicalLBListenersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClassicalLBTargets(self, request):
        """This API (DescribeClassicalLBTargets) is used to get the real servers bound to a classic CLB.

        :param request: Request instance for DescribeClassicalLBTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeClassicalLBTargetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClassicalLBTargets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClassicalLBTargetsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListeners(self, request):
        """This API is used to get the list of listeners by CLB instance ID, listener protocol, or port. If no filter is specified, all listeners under the CLB instance will be returned.

        :param request: Request instance for DescribeListeners.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeListenersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListenersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLoadBalancerListByCertId(self, request):
        """This API is used to query the list of CLB instances associated with a certificate in a region by certificate ID.

        :param request: Request instance for DescribeLoadBalancerListByCertId.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancerListByCertIdRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancerListByCertIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLoadBalancerListByCertId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLoadBalancerListByCertIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLoadBalancers(self, request):
        """This API is used to query the list of CLB instances in a region.

        :param request: Request instance for DescribeLoadBalancers.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLoadBalancers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLoadBalancersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRewrite(self, request):
        """This API (DescribeRewrite) is used to query the redirection relationship between the forwarding rules of a CLB instance by instance ID. If no listener ID or forwarding rule ID is specified, all redirection relationships in the instance will be returned.

        :param request: Request instance for DescribeRewrite.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeRewriteRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeRewriteResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRewrite", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRewriteResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTargetGroupInstances(self, request):
        """This API is used to get the information of servers bound to a target group.

        :param request: Request instance for DescribeTargetGroupInstances.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupInstancesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTargetGroupInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTargetGroupInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTargetGroupList(self, request):
        """This API is used to get the target group list.

        :param request: Request instance for DescribeTargetGroupList.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupListRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTargetGroupList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTargetGroupListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTargetGroups(self, request):
        """This API is used to query the target group information.

        :param request: Request instance for DescribeTargetGroups.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTargetGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTargetGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTargetGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTargetHealth(self, request):
        """This API (DescribeTargetHealth) is used to query the health check result of a real server of a CLB instance.

        :param request: Request instance for DescribeTargetHealth.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTargetHealthRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTargetHealthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTargetHealth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTargetHealthResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTargets(self, request):
        """This API (DescribeTargets) is used to query the list of real servers bound to some listeners of a CLB instance.

        :param request: Request instance for DescribeTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTargetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTargets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTargetsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskStatus(self, request):
        """This API is used to query the execution status of an async task. After non-query APIs (used to create/delete CLB instances, listeners, or rules or to bind/unbind real servers) are called successfully, this API needs to be used to query whether the task is successful.

        :param request: Request instance for DescribeTaskStatus.
        :type request: :class:`tencentcloud.clb.v20180317.models.DescribeTaskStatusRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DescribeTaskStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisassociateTargetGroups(self, request):
        """This API is used to unbind target groups from a rule.
        This is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful.

        :param request: Request instance for DisassociateTargetGroups.
        :type request: :class:`tencentcloud.clb.v20180317.models.DisassociateTargetGroupsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.DisassociateTargetGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateTargetGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateTargetGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ManualRewrite(self, request):
        """After the original access address and the address to be redirected are configured manually, the system will automatically redirect requests made to the original access address to the target address of the corresponding path. Multiple paths can be configured as a redirection policy under one domain name to achieve automatic redirection between HTTP and HTTPS. A redirection policy should meet the following rules: if A has already been redirected to B, then it cannot be redirected to C (unless the original redirection relationship is deleted and a new one is created), and B cannot be redirected to any other addresses.

        :param request: Request instance for ManualRewrite.
        :type request: :class:`tencentcloud.clb.v20180317.models.ManualRewriteRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ManualRewriteResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ManualRewrite", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ManualRewriteResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDomain(self, request):
        """This API (ModifyDomain) is used to modify a domain name under a layer-7 CLB listener.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for ModifyDomain.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyDomainRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDomainAttributes(self, request):
        """This API is used to modify the domain name-level attributes of a layer-7 listener's forwarding rule, such as modifying the domain name, changing the DefaultServer, enabling/disabling HTTP/2, and modifying certificates.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestId as an input parameter to check whether this task is successful.

        :param request: Request instance for ModifyDomainAttributes.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyDomainAttributesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyDomainAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDomainAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDomainAttributesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyListener(self, request):
        """This API (ModifyListener) is used to modify the attributes of a CLB listener, such as listener name, health check parameter, certificate information, and forwarding policy.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for ModifyListener.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyListenerRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyListenerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyListener", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyListenerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLoadBalancerAttributes(self, request):
        """This API is used to modify the attributes of a CLB instance such as name and cross-region attributes.

        :param request: Request instance for ModifyLoadBalancerAttributes.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyLoadBalancerAttributesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyLoadBalancerAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLoadBalancerAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLoadBalancerAttributesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRule(self, request):
        """This API (ModifyRule) is used to modify the attributes of a forwarding rule under a layer-7 CLB listener, such as forwarding path, health check attribute, and forwarding policy.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for ModifyRule.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyRuleRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTargetGroupAttribute(self, request):
        """This API is used to rename a target group or modify its default port attribute.

        :param request: Request instance for ModifyTargetGroupAttribute.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupAttributeRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTargetGroupAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTargetGroupAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTargetGroupInstancesPort(self, request):
        """This API is used to modify server ports of a target group in batches.
        This is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful.

        :param request: Request instance for ModifyTargetGroupInstancesPort.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupInstancesPortRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupInstancesPortResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTargetGroupInstancesPort", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTargetGroupInstancesPortResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTargetGroupInstancesWeight(self, request):
        """This API is used to modify server weights of a target group in batches.
        This is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful.

        :param request: Request instance for ModifyTargetGroupInstancesWeight.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupInstancesWeightRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyTargetGroupInstancesWeightResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTargetGroupInstancesWeight", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTargetGroupInstancesWeightResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTargetPort(self, request):
        """This API (ModifyTargetPort) is used to modify the port of a real server bound to a listener.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for ModifyTargetPort.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyTargetPortRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyTargetPortResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTargetPort", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTargetPortResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTargetWeight(self, request):
        """This API (ModifyTargetWeight) is used to modify the forwarding weight of a real server bound to a CLB instance.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for ModifyTargetWeight.
        :type request: :class:`tencentcloud.clb.v20180317.models.ModifyTargetWeightRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.ModifyTargetWeightResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTargetWeight", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTargetWeightResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RegisterTargetGroupInstances(self, request):
        """This API is used to register servers to a target group.
        This is an async API. After it is returned successfully, you can call the `DescribeTaskStatus` API with the returned `RequestID` as an input parameter to check whether this task is successful.

        :param request: Request instance for RegisterTargetGroupInstances.
        :type request: :class:`tencentcloud.clb.v20180317.models.RegisterTargetGroupInstancesRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.RegisterTargetGroupInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RegisterTargetGroupInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RegisterTargetGroupInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RegisterTargets(self, request):
        """This API (RegisterTargets) is used to bind one or more real servers to a CLB listener or layer-7 forwarding rule. Before using this API, you need to create relevant layer-4 listeners or layer-7 forwarding rules. For the former (TCP/UDP), only the listener ID needs to be specified, while for the latter (HTTP/HTTPS), the forwarding rule also needs to be specified through LocationId or Domain+Url.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for RegisterTargets.
        :type request: :class:`tencentcloud.clb.v20180317.models.RegisterTargetsRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.RegisterTargetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RegisterTargets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RegisterTargetsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RegisterTargetsWithClassicalLB(self, request):
        """This API (RegisterTargetsWithClassicalLB) is used to bind real servers to a classic CLB.
        This is an async API. After it is returned successfully, you can call the DescribeTaskStatus API with the returned RequestId as an input parameter to check whether this task is successful.

        :param request: Request instance for RegisterTargetsWithClassicalLB.
        :type request: :class:`tencentcloud.clb.v20180317.models.RegisterTargetsWithClassicalLBRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.RegisterTargetsWithClassicalLBResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RegisterTargetsWithClassicalLB", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RegisterTargetsWithClassicalLBResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("ReplaceCertForLoadBalancers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReplaceCertForLoadBalancersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetLoadBalancerClsLog(self, request):
        """This API is used to add, delete, and update the CLS topic of a CLB instance.

        :param request: Request instance for SetLoadBalancerClsLog.
        :type request: :class:`tencentcloud.clb.v20180317.models.SetLoadBalancerClsLogRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.SetLoadBalancerClsLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetLoadBalancerClsLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetLoadBalancerClsLogResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("SetLoadBalancerSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetLoadBalancerSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetSecurityGroupForLoadbalancers(self, request):
        """This API is used to bind or unbind a security group for multiple public network CLB instances. Note: Private network CLB do not support binding security groups.

        :param request: Request instance for SetSecurityGroupForLoadbalancers.
        :type request: :class:`tencentcloud.clb.v20180317.models.SetSecurityGroupForLoadbalancersRequest`
        :rtype: :class:`tencentcloud.clb.v20180317.models.SetSecurityGroupForLoadbalancersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetSecurityGroupForLoadbalancers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetSecurityGroupForLoadbalancersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)