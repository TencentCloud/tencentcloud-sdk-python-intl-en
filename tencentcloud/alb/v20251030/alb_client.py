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
from tencentcloud.alb.v20251030 import models


class AlbClient(AbstractClient):
    _apiVersion = '2025-10-30'
    _endpoint = 'alb.intl.tencentcloudapi.com'
    _service = 'alb'


    def AddTargetsToTargetGroup(self, request):
        r"""Add a backend service in the target group.

        :param request: Request instance for AddTargetsToTargetGroup.
        :type request: :class:`tencentcloud.alb.v20251030.models.AddTargetsToTargetGroupRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.AddTargetsToTargetGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddTargetsToTargetGroup", params, headers=headers)
            response = json.loads(body)
            model = models.AddTargetsToTargetGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateBandwidthPackageWithLoadBalancer(self, request):
        r"""Bind a Bandwidth Package to an application CLB instance.

        :param request: Request instance for AssociateBandwidthPackageWithLoadBalancer.
        :type request: :class:`tencentcloud.alb.v20251030.models.AssociateBandwidthPackageWithLoadBalancerRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.AssociateBandwidthPackageWithLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateBandwidthPackageWithLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateBandwidthPackageWithLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateListenerAdditionalCertificates(self, request):
        r"""AssociateListenerAdditionalCertificates is an async API. The system returns a request ID, but the additional cert is not yet successfully added. The add task is still in progress in the system backend. You can call the DescribeListenerCertificates API to query the add status of the additional cert.
        When HTTPS and QUIC listeners are in Associating status, it means certificate expansion is ongoing.
        When HTTPS and QUIC listeners are in the Associated status, the extension cert is successfully added.

        :param request: Request instance for AssociateListenerAdditionalCertificates.
        :type request: :class:`tencentcloud.alb.v20251030.models.AssociateListenerAdditionalCertificatesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.AssociateListenerAdditionalCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateListenerAdditionalCertificates", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateListenerAdditionalCertificatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHealthCheckTemplate(self, request):
        r"""This API is used to create a health check Template.

        :param request: Request instance for CreateHealthCheckTemplate.
        :type request: :class:`tencentcloud.alb.v20251030.models.CreateHealthCheckTemplateRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.CreateHealthCheckTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHealthCheckTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHealthCheckTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateListener(self, request):
        r"""This API is used to create a listener.

        :param request: Request instance for CreateListener.
        :type request: :class:`tencentcloud.alb.v20251030.models.CreateListenerRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.CreateListenerResponse`

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
        r"""**CreateLoadBalancer** is an async API. The system returns an instance ID, but the application CLB instance is not created successfully yet, and the creation task is still in progress in the system backend. You can call [DescribeLoadBalancerDetail](https://www.tencentcloud.com/document/api/1822/133711) to query the creation status of the application CLB instance.
        - When an application CLB instance is in the **Provisioning** status, it means the application CLB instance is being created.
        -When an application CLB instance is in the **Active** status, the application CLB instance is successfully created.

        :param request: Request instance for CreateLoadBalancer.
        :type request: :class:`tencentcloud.alb.v20251030.models.CreateLoadBalancerRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.CreateLoadBalancerResponse`

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


    def CreateRules(self, request):
        r"""This API is used to create forwarding rules. It is an async API. After returning successfully, call the DescribeAsyncJobs API with the returned RequestID as an input parameter to check whether this task is successful.
        A rule supports up to 10 forward Conditions and 5 forward Actions.

        :param request: Request instance for CreateRules.
        :type request: :class:`tencentcloud.alb.v20251030.models.CreateRulesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.CreateRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRules", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityPolicy(self, request):
        r"""Create a custom security policy for configuring the TLS protocol version and encryption suite of an HTTPS listener. With a security policy, you can flexibly control the security level of HTTPS communication between clients and load balancing.

        :param request: Request instance for CreateSecurityPolicy.
        :type request: :class:`tencentcloud.alb.v20251030.models.CreateSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.CreateSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTargetGroup(self, request):
        r"""Target Group APIs

        :param request: Request instance for CreateTargetGroup.
        :type request: :class:`tencentcloud.alb.v20251030.models.CreateTargetGroupRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.CreateTargetGroupResponse`

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


    def DeleteHealthCheckTemplates(self, request):
        r"""Deletes a health check Template

        :param request: Request instance for DeleteHealthCheckTemplates.
        :type request: :class:`tencentcloud.alb.v20251030.models.DeleteHealthCheckTemplatesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DeleteHealthCheckTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteHealthCheckTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteHealthCheckTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteListener(self, request):
        r"""Delete a listener

        :param request: Request instance for DeleteListener.
        :type request: :class:`tencentcloud.alb.v20251030.models.DeleteListenerRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DeleteListenerResponse`

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


    def DeleteLoadBalancers(self, request):
        r"""The **DeleteLoadBalancers** API is an async API. The system returns a request ID, but the application CLB instance is not yet deleted successfully. The deletion task is still in progress in the system backend. You can call [DescribeLoadBalancerDetail](https://www.tencentcloud.com/document/api/1822/133711) to query the deletion status of the application CLB instance.
        - When an application CLB instance is in the **Deleting** status, it means the application CLB instance is being deleted.
        -If the specified application CLB instance cannot be queried, the application CLB instance has been deleted successfully.

        :param request: Request instance for DeleteLoadBalancers.
        :type request: :class:`tencentcloud.alb.v20251030.models.DeleteLoadBalancersRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DeleteLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoadBalancers", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoadBalancersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRules(self, request):
        r"""DeleteRules deletes forwarding rules. This is an async API. After returning successfully, call the DescribeAsyncJobs API with the returned RequestID as an input parameter to check whether this task is successful.

        :param request: Request instance for DeleteRules.
        :type request: :class:`tencentcloud.alb.v20251030.models.DeleteRulesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DeleteRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityPolicy(self, request):
        r"""Delete one or more custom security policies. Before deletion, please ensure the policy hasn't been referenced by any HTTPS listener, otherwise the deletion will fail.

        :param request: Request instance for DeleteSecurityPolicy.
        :type request: :class:`tencentcloud.alb.v20251030.models.DeleteSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DeleteSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTargetGroups(self, request):
        r"""Delete a target group.

        :param request: Request instance for DeleteTargetGroups.
        :type request: :class:`tencentcloud.alb.v20251030.models.DeleteTargetGroupsRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DeleteTargetGroupsResponse`

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


    def DescribeAsyncJobs(self, request):
        r"""Query API for async tasks

        :param request: Request instance for DescribeAsyncJobs.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeAsyncJobsRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeAsyncJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAsyncJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAsyncJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHealthCheckTemplates(self, request):
        r"""This API is used to query the health check template list.

        :param request: Request instance for DescribeHealthCheckTemplates.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeHealthCheckTemplatesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeHealthCheckTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHealthCheckTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHealthCheckTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListenerCertificates(self, request):
        r"""This API is used to query the list of certificates bound to a specified listener by instance id and listener id.
        If `CertificateType` is set to `SVR`, the information of the extended server certificate and the default server certificate is returned.
        If CertificateType is set to CA, the default CA certificate info is returned.

        :param request: Request instance for DescribeListenerCertificates.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeListenerCertificatesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeListenerCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListenerCertificates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListenerCertificatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListenerDetail(self, request):
        r"""Queries details of one listener.

        :param request: Request instance for DescribeListenerDetail.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeListenerDetailRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeListenerDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListenerDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListenerDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListenerHealthStatus(self, request):
        r"""Queries the health status of a listener.

        :param request: Request instance for DescribeListenerHealthStatus.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeListenerHealthStatusRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeListenerHealthStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListenerHealthStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListenerHealthStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListeners(self, request):
        r"""Queries the listener list

        :param request: Request instance for DescribeListeners.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeListenersRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeListenersResponse`

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


    def DescribeLoadBalancerDetail(self, request):
        r"""Queries detailed information of a specified load balancing instance.

        :param request: Request instance for DescribeLoadBalancerDetail.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeLoadBalancerDetailRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeLoadBalancerDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalancerDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoadBalancerDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoadBalancers(self, request):
        r"""Query instance configuration.

        :param request: Request instance for DescribeLoadBalancers.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeLoadBalancersRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeLoadBalancersResponse`

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


    def DescribeQuota(self, request):
        r"""Queries the ALB quota configuration of the current account. It supports querying by quota type and allows you to pass a resource ID to query resource-level quotas. You can use DisplayFields to return the used amount and remaining available quantity as needed.

        :param request: Request instance for DescribeQuota.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeQuotaRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeQuotaResponse`

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


    def DescribeRules(self, request):
        r"""This API is used to query forwarding rules.

        :param request: Request instance for DescribeRules.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeRulesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityPolicies(self, request):
        r"""Queries the custom security policy list, supports filtering by security policy ID, name, or tag, and supports paging query.

        :param request: Request instance for DescribeSecurityPolicies.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeSecurityPoliciesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeSecurityPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityPolicyCapabilities(self, request):
        r"""Query the security policy configuration capacity supported in the current region, including optional TLS protocol versions and the encryption suite list for each version. Before creating or modifying a custom security policy, call this API to get available configuration options.

        :param request: Request instance for DescribeSecurityPolicyCapabilities.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeSecurityPolicyCapabilitiesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeSecurityPolicyCapabilitiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPolicyCapabilities", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityPolicyCapabilitiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityPolicyRelations(self, request):
        r"""Query the relationship between a security policy and the HTTPS listeners that refer to it. Before deleting or modifying a security policy, it is advisable to call this API to confirm the impact.

        :param request: Request instance for DescribeSecurityPolicyRelations.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeSecurityPolicyRelationsRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeSecurityPolicyRelationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityPolicyRelations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityPolicyRelationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSystemSecurityPolicies(self, request):
        r"""Queries system security policies.

        :param request: Request instance for DescribeSystemSecurityPolicies.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeSystemSecurityPoliciesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeSystemSecurityPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSystemSecurityPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSystemSecurityPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargetGroupTargets(self, request):
        r"""Queries backend services in the target group.

        :param request: Request instance for DescribeTargetGroupTargets.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeTargetGroupTargetsRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeTargetGroupTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargetGroupTargets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetGroupTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTargetGroups(self, request):
        r"""Query the target group list.

        :param request: Request instance for DescribeTargetGroups.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeTargetGroupsRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeTargetGroupsResponse`

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


    def DescribeTargetGroupsByTarget(self, request):
        r"""Query bound target groups based on the slave machine.

        :param request: Request instance for DescribeTargetGroupsByTarget.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeTargetGroupsByTargetRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeTargetGroupsByTargetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargetGroupsByTarget", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetGroupsByTargetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZones(self, request):
        r"""Querying Availability Zones

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.alb.v20251030.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZones", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZonesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateBandwidthPackageFromLoadBalancer(self, request):
        r"""Unbind a Bandwidth Package from an application CLB instance.

        :param request: Request instance for DisassociateBandwidthPackageFromLoadBalancer.
        :type request: :class:`tencentcloud.alb.v20251030.models.DisassociateBandwidthPackageFromLoadBalancerRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DisassociateBandwidthPackageFromLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateBandwidthPackageFromLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateBandwidthPackageFromLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateListenerAdditionalCertificates(self, request):
        r"""DisassociateListenerAdditionalCertificates is an async API. The system returns a request ID, but the additional cert is not yet unbound. The unbinding task is still in progress in the system backend. You can call the DescribeListenerCertificates API to query the cert unbinding status. If the cert is in Disassociating status, it is being unbound.

        :param request: Request instance for DisassociateListenerAdditionalCertificates.
        :type request: :class:`tencentcloud.alb.v20251030.models.DisassociateListenerAdditionalCertificatesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.DisassociateListenerAdditionalCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateListenerAdditionalCertificates", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateListenerAdditionalCertificatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceCreateLoadBalancer(self, request):
        r"""This API is used to query the price for creating a load balancer.

        :param request: Request instance for InquirePriceCreateLoadBalancer.
        :type request: :class:`tencentcloud.alb.v20251030.models.InquirePriceCreateLoadBalancerRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.InquirePriceCreateLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceCreateLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceCreateLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHealthCheckTemplate(self, request):
        r"""Modify a health check template

        :param request: Request instance for ModifyHealthCheckTemplate.
        :type request: :class:`tencentcloud.alb.v20251030.models.ModifyHealthCheckTemplateRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.ModifyHealthCheckTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHealthCheckTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHealthCheckTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyListenerAttributes(self, request):
        r"""Modifies listener properties.

        :param request: Request instance for ModifyListenerAttributes.
        :type request: :class:`tencentcloud.alb.v20251030.models.ModifyListenerAttributesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.ModifyListenerAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyListenerAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyListenerAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoadBalancerAddressType(self, request):
        r"""**Prerequisite:**
        You have created an application CLB instance. For detailed operations, please see CreateLoadBalancer.
        When you need to change the network type of an application CLB instance from private network to public network through this API, you need to create an Elastic IP first.
        **Instructions:**
        The ModifyLoadBalancerAddressType API is an async API. The system returns a request ID, but the network type of the application CLB instance has not been changed yet. The change task is still in progress in the system backend. You can call DescribeLoadBalancerDetail to query the change status of the network type of the application CLB instance.
        When an application CLB instance is in the Configuring status, it means the network type of the instance is changing.
        When an application CLB instance is in the Active status, the network type change of the instance is successful.

        :param request: Request instance for ModifyLoadBalancerAddressType.
        :type request: :class:`tencentcloud.alb.v20251030.models.ModifyLoadBalancerAddressTypeRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.ModifyLoadBalancerAddressTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoadBalancerAddressType", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoadBalancerAddressTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLoadBalancerAttributes(self, request):
        r"""The **ModifyLoadBalancerAttributes** API is an async API. It returns a request ID, but the application CLB instance attribute has not been modified yet. The modifying task is still in progress in the system backend. You can call [DescribeLoadBalancerDetail](https://www.tencentcloud.com/document/api/1822/133711) to query the modification status of the application CLB instance attribute.
        -When the application CLB instance attribute is in the **Configuring** status, it means the application CLB instance attribute is being modified.
        - When the application CLB instance attribute is in the **Active** status, it means the application CLB instance attribute was modified successfully.

        :param request: Request instance for ModifyLoadBalancerAttributes.
        :type request: :class:`tencentcloud.alb.v20251030.models.ModifyLoadBalancerAttributesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.ModifyLoadBalancerAttributesResponse`

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


    def ModifyLoadBalancerModificationProtection(self, request):
        r"""Set load balancing instance modification protection.

        :param request: Request instance for ModifyLoadBalancerModificationProtection.
        :type request: :class:`tencentcloud.alb.v20251030.models.ModifyLoadBalancerModificationProtectionRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.ModifyLoadBalancerModificationProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoadBalancerModificationProtection", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoadBalancerModificationProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRulesAttributes(self, request):
        r"""This API is used to modify forwarding rule attributes. This is an async API. After the API return succeeds, you can call the DescribeAsyncJobs API with the returned RequestID as an input parameter to check whether this task is successful.
        A rule supports up to 10 forward Conditions and 5 forward Actions.

        :param request: Request instance for ModifyRulesAttributes.
        :type request: :class:`tencentcloud.alb.v20251030.models.ModifyRulesAttributesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.ModifyRulesAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRulesAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRulesAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityPolicyAttributes(self, request):
        r"""Modify the properties of a custom security policy, including the policy name, TLS protocol version, and encryption suite. The modified configuration will be applied to all HTTPS listeners associated with this policy immediately.

        :param request: Request instance for ModifySecurityPolicyAttributes.
        :type request: :class:`tencentcloud.alb.v20251030.models.ModifySecurityPolicyAttributesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.ModifySecurityPolicyAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityPolicyAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityPolicyAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTargetGroupAttributes(self, request):
        r"""Modify the target group.

        :param request: Request instance for ModifyTargetGroupAttributes.
        :type request: :class:`tencentcloud.alb.v20251030.models.ModifyTargetGroupAttributesRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.ModifyTargetGroupAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTargetGroupAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTargetGroupAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTargetsInTargetGroup(self, request):
        r"""Modifies backend service information in the target group.

        :param request: Request instance for ModifyTargetsInTargetGroup.
        :type request: :class:`tencentcloud.alb.v20251030.models.ModifyTargetsInTargetGroupRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.ModifyTargetsInTargetGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTargetsInTargetGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTargetsInTargetGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def NotifyUnbindTarget(self, request):
        r"""Notify load balancing to unbind real servers

        :param request: Request instance for NotifyUnbindTarget.
        :type request: :class:`tencentcloud.alb.v20251030.models.NotifyUnbindTargetRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.NotifyUnbindTargetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("NotifyUnbindTarget", params, headers=headers)
            response = json.loads(body)
            model = models.NotifyUnbindTargetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveTargetsFromTargetGroup(self, request):
        r"""Removes a backend service from the target group

        :param request: Request instance for RemoveTargetsFromTargetGroup.
        :type request: :class:`tencentcloud.alb.v20251030.models.RemoveTargetsFromTargetGroupRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.RemoveTargetsFromTargetGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveTargetsFromTargetGroup", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveTargetsFromTargetGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetLoadBalancerSecurityGroups(self, request):
        r"""The SetLoadBalancerSecurityGroups API supports setting (binding and unbinding) security groups for a public network load balancing instance. To query the security groups currently bound to a load balancing instance, use the DescribeLoadBalancerDetail API (https://www.tencentcloud.com/document/api/1822/133711?from_cn_redirect=1). This API uses SET semantics.
        For the binding operation, input parameters need to be passed in for all security groups that should be bound to the load balancing instance (bound + new binding).
        During unbinding, input parameters need to pass in all security groups bound to a CLB instance after unbinding. To unbind all security groups, omit this parameter or specify an empty array.

        :param request: Request instance for SetLoadBalancerSecurityGroups.
        :type request: :class:`tencentcloud.alb.v20251030.models.SetLoadBalancerSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.alb.v20251030.models.SetLoadBalancerSecurityGroupsResponse`

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