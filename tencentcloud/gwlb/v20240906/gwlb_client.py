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
from tencentcloud.gwlb.v20240906 import models


class GwlbClient(AbstractClient):
    _apiVersion = '2024-09-06'
    _endpoint = 'gwlb.intl.tencentcloudapi.com'
    _service = 'gwlb'


    def AssociateTargetGroups(self, request):
        """This API is used to bind target groups to a CLB.This is an async API. After the API return succeeds, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for AssociateTargetGroups.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.AssociateTargetGroupsRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.AssociateTargetGroupsResponse`

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


    def CreateGatewayLoadBalancer(self, request):
        """This API is used to create a GWLB instance. To use the GWLB service, you must purchase one or more GWLB instances. After this API is called successfully, a unique ID for the GWLB instance will be returned.Note: The default purchase quota for each account in each region is 10.This is an async API. After the API is called successfully, you can use the DescribeGatewayLoadBalancers API to query the status of the GWLB instance (such as creating and normal) to determine whether the creation is successful.

        :param request: Request instance for CreateGatewayLoadBalancer.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.CreateGatewayLoadBalancerRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.CreateGatewayLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGatewayLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGatewayLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTargetGroup(self, request):
        """This API is used to create a target group. This feature is in beta testing. If you need to use it, please [submit a ticket](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=163&source=0&data_title=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB&step=1).

        :param request: Request instance for CreateTargetGroup.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.CreateTargetGroupRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.CreateTargetGroupResponse`

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


    def DeleteGatewayLoadBalancer(self, request):
        """This API is used to delete one or more specified GWLB instances. After successful deletion, the GWLB instances will be unbound from the backend service.This is an async API. After the API return succeeds, you can call the DescribeTaskStatus API with the returned RequestId as an input parameter to check whether this task is successful.

        :param request: Request instance for DeleteGatewayLoadBalancer.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.DeleteGatewayLoadBalancerRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.DeleteGatewayLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGatewayLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGatewayLoadBalancerResponse()
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
        :type request: :class:`tencentcloud.gwlb.v20240906.models.DeleteTargetGroupsRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.DeleteTargetGroupsResponse`

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


    def DeregisterTargetGroupInstances(self, request):
        """This API is used to unbind a server from a target group.
        This is an async API. After the API return succeeds, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for DeregisterTargetGroupInstances.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.DeregisterTargetGroupInstancesRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.DeregisterTargetGroupInstancesResponse`

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


    def DescribeGatewayLoadBalancers(self, request):
        """This API is used to query the list of GWLB instances in a region.

        :param request: Request instance for DescribeGatewayLoadBalancers.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.DescribeGatewayLoadBalancersRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.DescribeGatewayLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatewayLoadBalancers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatewayLoadBalancersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargetGroupInstanceStatus(self, request):
        """This API is used to query the backend service status of a target group. Currently, only GWLB type target groups support querying backend service status.

        :param request: Request instance for DescribeTargetGroupInstanceStatus.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.DescribeTargetGroupInstanceStatusRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.DescribeTargetGroupInstanceStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargetGroupInstanceStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetGroupInstanceStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargetGroupInstances(self, request):
        """This API is used to obtain information on servers bound to a target group.

        :param request: Request instance for DescribeTargetGroupInstances.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.DescribeTargetGroupInstancesRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.DescribeTargetGroupInstancesResponse`

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
        """This API is used to obtain a target group list.

        :param request: Request instance for DescribeTargetGroupList.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.DescribeTargetGroupListRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.DescribeTargetGroupListResponse`

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
        """This API is used to query target group information.

        :param request: Request instance for DescribeTargetGroups.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.DescribeTargetGroupsRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.DescribeTargetGroupsResponse`

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


    def DescribeTaskStatus(self, request):
        """This API is used to query the execution status of an async task. After non-query APIs (for example, used to create/delete CLB instances) are called successfully, this API needs to be used to query whether the task is successful.

        :param request: Request instance for DescribeTaskStatus.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.DescribeTaskStatusRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.DescribeTaskStatusResponse`

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
        """This API is used to disassociate a CLB from a target group.This is an async API. After the API return succeeds, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for DisassociateTargetGroups.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.DisassociateTargetGroupsRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.DisassociateTargetGroupsResponse`

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


    def InquirePriceCreateGatewayLoadBalancer(self, request):
        """This API is used to query the price for creating a GWLB.

        :param request: Request instance for InquirePriceCreateGatewayLoadBalancer.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.InquirePriceCreateGatewayLoadBalancerRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.InquirePriceCreateGatewayLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceCreateGatewayLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceCreateGatewayLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGatewayLoadBalancerAttribute(self, request):
        """This API is used to modify the attributes of a CLB instance. It supports modifying the name and bandwidth cap of the CLB instance.

        :param request: Request instance for ModifyGatewayLoadBalancerAttribute.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.ModifyGatewayLoadBalancerAttributeRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.ModifyGatewayLoadBalancerAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGatewayLoadBalancerAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGatewayLoadBalancerAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTargetGroupAttribute(self, request):
        """This API is used to modify the name, health check, and other attributes of the target group.

        :param request: Request instance for ModifyTargetGroupAttribute.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.ModifyTargetGroupAttributeRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.ModifyTargetGroupAttributeResponse`

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


    def ModifyTargetGroupInstancesWeight(self, request):
        """This API is used to modify the server weight of a target group.This is an async API. After the API return succeeds, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for ModifyTargetGroupInstancesWeight.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.ModifyTargetGroupInstancesWeightRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.ModifyTargetGroupInstancesWeightResponse`

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


    def RegisterTargetGroupInstances(self, request):
        """This API is used to register servers to a target group.This is an async API. After the API return succeeds, you can call the DescribeTaskStatus API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for RegisterTargetGroupInstances.
        :type request: :class:`tencentcloud.gwlb.v20240906.models.RegisterTargetGroupInstancesRequest`
        :rtype: :class:`tencentcloud.gwlb.v20240906.models.RegisterTargetGroupInstancesResponse`

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