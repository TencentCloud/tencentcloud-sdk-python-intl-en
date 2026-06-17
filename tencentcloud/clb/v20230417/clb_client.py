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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.clb.v20230417 import models


class ClbClient(AbstractClient):
    _apiVersion = '2023-04-17'
    _endpoint = 'clb.intl.tencentcloudapi.com'
    _service = 'clb'


    def BatchModifyTargetWeight(self, request):
        r"""The BatchModifyTargetWeight API is used to modify the forwarding weight of backend machines bound to a Cloud Load Balancer listener in batch. The resource limit is 500. This is an async API. After it returns a successful result, call DescribeTaskStatus API with the returned RequestID as input parameter to check whether this task is successful.<br/>This API is supported by layer-4 and layer-7 CLB listeners but not by classic CLB.

        :param request: Request instance for BatchModifyTargetWeight.
        :type request: :class:`tencentcloud.clb.v20230417.models.BatchModifyTargetWeightRequest`
        :rtype: :class:`tencentcloud.clb.v20230417.models.BatchModifyTargetWeightResponse`

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


    def CloneLoadBalancer(self, request):
        r"""This API is used to clone a Cloud Load Balancer instance. Based on the designated CLB instance, it creates a new instance with identical rules and binding relationships. The cloning operation is asynchronous. The cloned data is based on the call to CloneLoadBalancer. If the cloned CLB changes after calling CloneLoadBalancer, the change rules will not be cloned.

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

        :param request: Request instance for CloneLoadBalancer.
        :type request: :class:`tencentcloud.clb.v20230417.models.CloneLoadBalancerRequest`
        :rtype: :class:`tencentcloud.clb.v20230417.models.CloneLoadBalancerResponse`

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


    def CreateLoadBalancer(self, request):
        r"""This API is used to create a Cloud Load Balancer instance (this interface supports only pay-as-you-go CLB instances. For annual/monthly subscription, proceed to purchase through the console). To use the CLB service, you must purchase one or more CLB instances. After successfully calling the API, the unique ID of the CLB instance will be returned. CLB instances are divided into public network and private network types. For details, refer to the product type in the product description.
        Note: (1) To apply for Cloud Load Balancer (CLB) in a specified availability zone or cross-zone disaster recovery (only supported in Hong Kong (China)), [submit a request](https://console.cloud.tencent.com/workorder/category) if you need to experience the feature. (2) Currently only Beijing, Shanghai, and Guangzhou support IPv6. (3) The default purchase quota for an account in each region is 100 for public network and 100 for private network.
        This is an async API. After the API returns successfully, you can use the DescribeLoadBalancers API to query the status of the Cloud Load Balancer instance (such as creating and normal) to confirm whether the creation is successful.

        :param request: Request instance for CreateLoadBalancer.
        :type request: :class:`tencentcloud.clb.v20230417.models.CreateLoadBalancerRequest`
        :rtype: :class:`tencentcloud.clb.v20230417.models.CreateLoadBalancerResponse`

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


    def DescribeClassicalLBListeners(self, request):
        r"""This API is used to obtain listener information of classic CLB.

        :param request: Request instance for DescribeClassicalLBListeners.
        :type request: :class:`tencentcloud.clb.v20230417.models.DescribeClassicalLBListenersRequest`
        :rtype: :class:`tencentcloud.clb.v20230417.models.DescribeClassicalLBListenersResponse`

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


    def DescribeCustomizedConfigAssociateList(self, request):
        r"""This API is used to query the locations, servers, or CLB instances bound to a configuration. If there are domains, the result will be filtered by domain.

        :param request: Request instance for DescribeCustomizedConfigAssociateList.
        :type request: :class:`tencentcloud.clb.v20230417.models.DescribeCustomizedConfigAssociateListRequest`
        :rtype: :class:`tencentcloud.clb.v20230417.models.DescribeCustomizedConfigAssociateListResponse`

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
        r"""Pull the list of custom configurations. The configurations of the specified type under the user's AppId will be returned.

        :param request: Request instance for DescribeCustomizedConfigList.
        :type request: :class:`tencentcloud.clb.v20230417.models.DescribeCustomizedConfigListRequest`
        :rtype: :class:`tencentcloud.clb.v20230417.models.DescribeCustomizedConfigListResponse`

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


    def DescribeLoadBalancerListByCertId(self, request):
        r"""This API is used to query the list of CLB instances associated with a certificate in a region by certificate ID.

        :param request: Request instance for DescribeLoadBalancerListByCertId.
        :type request: :class:`tencentcloud.clb.v20230417.models.DescribeLoadBalancerListByCertIdRequest`
        :rtype: :class:`tencentcloud.clb.v20230417.models.DescribeLoadBalancerListByCertIdResponse`

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


    def DescribeLoadBalancers(self, request):
        r"""This API is used to query the list of CLB instances in a region.

        :param request: Request instance for DescribeLoadBalancers.
        :type request: :class:`tencentcloud.clb.v20230417.models.DescribeLoadBalancersRequest`
        :rtype: :class:`tencentcloud.clb.v20230417.models.DescribeLoadBalancersResponse`

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
        r"""Query the detailed information of Cloud Load Balancer, including listeners, rules, and backend targets.

        :param request: Request instance for DescribeLoadBalancersDetail.
        :type request: :class:`tencentcloud.clb.v20230417.models.DescribeLoadBalancersDetailRequest`
        :rtype: :class:`tencentcloud.clb.v20230417.models.DescribeLoadBalancersDetailResponse`

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


    def DescribeTargetHealth(self, request):
        r"""This API (DescribeTargetHealth) is used to query the health check result of a real server of a CLB instance. It is not supported by Classic CLB.

        :param request: Request instance for DescribeTargetHealth.
        :type request: :class:`tencentcloud.clb.v20230417.models.DescribeTargetHealthRequest`
        :rtype: :class:`tencentcloud.clb.v20230417.models.DescribeTargetHealthResponse`

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


    def SetCustomizedConfigForLoadBalancer(self, request):
        r"""This API is used to create, delete, modify, bind, and unbind custom CLB configurations.

        :param request: Request instance for SetCustomizedConfigForLoadBalancer.
        :type request: :class:`tencentcloud.clb.v20230417.models.SetCustomizedConfigForLoadBalancerRequest`
        :rtype: :class:`tencentcloud.clb.v20230417.models.SetCustomizedConfigForLoadBalancerResponse`

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