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
from tencentcloud.ga2.v20250115 import models


class Ga2Client(AbstractClient):
    _apiVersion = '2025-01-15'
    _endpoint = 'ga2.intl.tencentcloudapi.com'
    _service = 'ga2'


    def CreateAccelerateAreas(self, request):
        r"""This API is used to create an acceleration region.

        :param request: Request instance for CreateAccelerateAreas.
        :type request: :class:`tencentcloud.ga2.v20250115.models.CreateAccelerateAreasRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.CreateAccelerateAreasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccelerateAreas", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccelerateAreasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEndpointGroup(self, request):
        r"""This API is used to create a terminal node group.

        :param request: Request instance for CreateEndpointGroup.
        :type request: :class:`tencentcloud.ga2.v20250115.models.CreateEndpointGroupRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.CreateEndpointGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEndpointGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEndpointGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateForwardingPolicy(self, request):
        r"""Create a layer-7 forwarding policy.

        :param request: Request instance for CreateForwardingPolicy.
        :type request: :class:`tencentcloud.ga2.v20250115.models.CreateForwardingPolicyRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.CreateForwardingPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateForwardingPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateForwardingPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateForwardingRule(self, request):
        r"""Create a Layer 7 forwarding rule

        :param request: Request instance for CreateForwardingRule.
        :type request: :class:`tencentcloud.ga2.v20250115.models.CreateForwardingRuleRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.CreateForwardingRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateForwardingRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateForwardingRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGlobalAccelerator(self, request):
        r"""This API is used to create a global acceleration instance.

        :param request: Request instance for CreateGlobalAccelerator.
        :type request: :class:`tencentcloud.ga2.v20250115.models.CreateGlobalAcceleratorRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.CreateGlobalAcceleratorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGlobalAccelerator", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGlobalAcceleratorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGlobalAcceleratorAccessLog(self, request):
        r"""Create a GA access log

        :param request: Request instance for CreateGlobalAcceleratorAccessLog.
        :type request: :class:`tencentcloud.ga2.v20250115.models.CreateGlobalAcceleratorAccessLogRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.CreateGlobalAcceleratorAccessLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGlobalAcceleratorAccessLog", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGlobalAcceleratorAccessLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGlobalAcceleratorAclPolicy(self, request):
        r"""Create access control policy

        :param request: Request instance for CreateGlobalAcceleratorAclPolicy.
        :type request: :class:`tencentcloud.ga2.v20250115.models.CreateGlobalAcceleratorAclPolicyRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.CreateGlobalAcceleratorAclPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGlobalAcceleratorAclPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGlobalAcceleratorAclPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGlobalAcceleratorAclRule(self, request):
        r"""Create an ACL rule

        :param request: Request instance for CreateGlobalAcceleratorAclRule.
        :type request: :class:`tencentcloud.ga2.v20250115.models.CreateGlobalAcceleratorAclRuleRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.CreateGlobalAcceleratorAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGlobalAcceleratorAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGlobalAcceleratorAclRuleResponse()
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
        :type request: :class:`tencentcloud.ga2.v20250115.models.CreateListenerRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.CreateListenerResponse`

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


    def CreateListenerAdditionalCert(self, request):
        r"""Add an extension certificate.

        :param request: Request instance for CreateListenerAdditionalCert.
        :type request: :class:`tencentcloud.ga2.v20250115.models.CreateListenerAdditionalCertRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.CreateListenerAdditionalCertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateListenerAdditionalCert", params, headers=headers)
            response = json.loads(body)
            model = models.CreateListenerAdditionalCertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccelerateAreas(self, request):
        r"""Delete an acceleration region

        :param request: Request instance for DeleteAccelerateAreas.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DeleteAccelerateAreasRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DeleteAccelerateAreasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAccelerateAreas", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAccelerateAreasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEndpointGroups(self, request):
        r"""Delete a terminal node group.

        :param request: Request instance for DeleteEndpointGroups.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DeleteEndpointGroupsRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DeleteEndpointGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEndpointGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEndpointGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteForwardingPolicy(self, request):
        r"""Delete a layer-7 forwarding policy.

        :param request: Request instance for DeleteForwardingPolicy.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DeleteForwardingPolicyRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DeleteForwardingPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteForwardingPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteForwardingPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteForwardingRule(self, request):
        r"""Delete a Layer 7 forwarding rule

        :param request: Request instance for DeleteForwardingRule.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DeleteForwardingRuleRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DeleteForwardingRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteForwardingRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteForwardingRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGlobalAccelerator(self, request):
        r"""Deletes a global acceleration instance

        :param request: Request instance for DeleteGlobalAccelerator.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DeleteGlobalAcceleratorRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DeleteGlobalAcceleratorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGlobalAccelerator", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGlobalAcceleratorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGlobalAcceleratorAccessLog(self, request):
        r"""This API is used to delete a GA log task.

        :param request: Request instance for DeleteGlobalAcceleratorAccessLog.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DeleteGlobalAcceleratorAccessLogRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DeleteGlobalAcceleratorAccessLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGlobalAcceleratorAccessLog", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGlobalAcceleratorAccessLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGlobalAcceleratorAclPolicy(self, request):
        r"""Delete access control policy

        :param request: Request instance for DeleteGlobalAcceleratorAclPolicy.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DeleteGlobalAcceleratorAclPolicyRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DeleteGlobalAcceleratorAclPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGlobalAcceleratorAclPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGlobalAcceleratorAclPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGlobalAcceleratorAclRule(self, request):
        r"""Delete ACL rule

        :param request: Request instance for DeleteGlobalAcceleratorAclRule.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DeleteGlobalAcceleratorAclRuleRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DeleteGlobalAcceleratorAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGlobalAcceleratorAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGlobalAcceleratorAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteListener(self, request):
        r"""This API is used to delete a listener.

        :param request: Request instance for DeleteListener.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DeleteListenerRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DeleteListenerResponse`

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


    def DeleteListenerAdditionalCert(self, request):
        r"""Delete the extension certificate.

        :param request: Request instance for DeleteListenerAdditionalCert.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DeleteListenerAdditionalCertRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DeleteListenerAdditionalCertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteListenerAdditionalCert", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteListenerAdditionalCertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccelerateAreas(self, request):
        r"""Queries acceleration regions

        :param request: Request instance for DescribeAccelerateAreas.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DescribeAccelerateAreasRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DescribeAccelerateAreasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccelerateAreas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccelerateAreasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccelerateRegions(self, request):
        r"""Queries selectable acceleration regions.

        :param request: Request instance for DescribeAccelerateRegions.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DescribeAccelerateRegionsRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DescribeAccelerateRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccelerateRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccelerateRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccessLogParam(self, request):
        r"""View access log reporting parameters

        :param request: Request instance for DescribeAccessLogParam.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DescribeAccessLogParamRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DescribeAccessLogParamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccessLogParam", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccessLogParamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCrossBorderSettlement(self, request):
        r"""Querying Cross-Border Bills

        :param request: Request instance for DescribeCrossBorderSettlement.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DescribeCrossBorderSettlementRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DescribeCrossBorderSettlementResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCrossBorderSettlement", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCrossBorderSettlementResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEndpointGroups(self, request):
        r"""Query a terminal node group.

        :param request: Request instance for DescribeEndpointGroups.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DescribeEndpointGroupsRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DescribeEndpointGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEndpointGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEndpointGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeForwardingPolicy(self, request):
        r"""View a layer-7 forwarding policy

        :param request: Request instance for DescribeForwardingPolicy.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DescribeForwardingPolicyRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DescribeForwardingPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeForwardingPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeForwardingPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeForwardingRule(self, request):
        r"""View a Layer 7 forwarding rule

        :param request: Request instance for DescribeForwardingRule.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DescribeForwardingRuleRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DescribeForwardingRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeForwardingRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeForwardingRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGlobalAcceleratorAccessLog(self, request):
        r"""Query log tasks

        :param request: Request instance for DescribeGlobalAcceleratorAccessLog.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DescribeGlobalAcceleratorAccessLogRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DescribeGlobalAcceleratorAccessLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGlobalAcceleratorAccessLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGlobalAcceleratorAccessLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGlobalAcceleratorAclPolicies(self, request):
        r"""View the access control policy

        :param request: Request instance for DescribeGlobalAcceleratorAclPolicies.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DescribeGlobalAcceleratorAclPoliciesRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DescribeGlobalAcceleratorAclPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGlobalAcceleratorAclPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGlobalAcceleratorAclPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGlobalAcceleratorAclRules(self, request):
        r"""View ACL rules

        :param request: Request instance for DescribeGlobalAcceleratorAclRules.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DescribeGlobalAcceleratorAclRulesRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DescribeGlobalAcceleratorAclRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGlobalAcceleratorAclRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGlobalAcceleratorAclRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGlobalAccelerators(self, request):
        r"""Modify a global acceleration instance

        :param request: Request instance for DescribeGlobalAccelerators.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DescribeGlobalAcceleratorsRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DescribeGlobalAcceleratorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGlobalAccelerators", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGlobalAcceleratorsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeListeners(self, request):
        r"""This API is used to query listeners.

        :param request: Request instance for DescribeListeners.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DescribeListenersRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DescribeListenersResponse`

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


    def DescribeTaskResult(self, request):
        r"""Query asynchronous task result

        :param request: Request instance for DescribeTaskResult.
        :type request: :class:`tencentcloud.ga2.v20250115.models.DescribeTaskResultRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.DescribeTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccelerateAreas(self, request):
        r"""Modify acceleration region

        :param request: Request instance for ModifyAccelerateAreas.
        :type request: :class:`tencentcloud.ga2.v20250115.models.ModifyAccelerateAreasRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.ModifyAccelerateAreasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccelerateAreas", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccelerateAreasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccessLogStatus(self, request):
        r"""Modify the status of a log task

        :param request: Request instance for ModifyAccessLogStatus.
        :type request: :class:`tencentcloud.ga2.v20250115.models.ModifyAccessLogStatusRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.ModifyAccessLogStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccessLogStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccessLogStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEndpointGroup(self, request):
        r"""This API is used to modify a terminal node group.

        :param request: Request instance for ModifyEndpointGroup.
        :type request: :class:`tencentcloud.ga2.v20250115.models.ModifyEndpointGroupRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.ModifyEndpointGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEndpointGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEndpointGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyForwardingPolicy(self, request):
        r"""Modify a layer-7 forwarding policy

        :param request: Request instance for ModifyForwardingPolicy.
        :type request: :class:`tencentcloud.ga2.v20250115.models.ModifyForwardingPolicyRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.ModifyForwardingPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyForwardingPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyForwardingPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyForwardingRule(self, request):
        r"""This API is used to modify a Layer 7 forwarding rule.

        :param request: Request instance for ModifyForwardingRule.
        :type request: :class:`tencentcloud.ga2.v20250115.models.ModifyForwardingRuleRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.ModifyForwardingRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyForwardingRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyForwardingRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGlobalAccelerator(self, request):
        r"""Modify a global acceleration instance

        :param request: Request instance for ModifyGlobalAccelerator.
        :type request: :class:`tencentcloud.ga2.v20250115.models.ModifyGlobalAcceleratorRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.ModifyGlobalAcceleratorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGlobalAccelerator", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGlobalAcceleratorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGlobalAcceleratorAccessLog(self, request):
        r"""Modify GA access logs

        :param request: Request instance for ModifyGlobalAcceleratorAccessLog.
        :type request: :class:`tencentcloud.ga2.v20250115.models.ModifyGlobalAcceleratorAccessLogRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.ModifyGlobalAcceleratorAccessLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGlobalAcceleratorAccessLog", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGlobalAcceleratorAccessLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGlobalAcceleratorAclPolicy(self, request):
        r"""Modify the status of an access control policy

        :param request: Request instance for ModifyGlobalAcceleratorAclPolicy.
        :type request: :class:`tencentcloud.ga2.v20250115.models.ModifyGlobalAcceleratorAclPolicyRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.ModifyGlobalAcceleratorAclPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGlobalAcceleratorAclPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGlobalAcceleratorAclPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGlobalAcceleratorAclRule(self, request):
        r"""Modify ACL rules

        :param request: Request instance for ModifyGlobalAcceleratorAclRule.
        :type request: :class:`tencentcloud.ga2.v20250115.models.ModifyGlobalAcceleratorAclRuleRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.ModifyGlobalAcceleratorAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGlobalAcceleratorAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGlobalAcceleratorAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyListener(self, request):
        r"""Modify a listener

        :param request: Request instance for ModifyListener.
        :type request: :class:`tencentcloud.ga2.v20250115.models.ModifyListenerRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.ModifyListenerResponse`

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


    def ReplaceListenerAdditionalCert(self, request):
        r"""Replace the extension certificate.

        :param request: Request instance for ReplaceListenerAdditionalCert.
        :type request: :class:`tencentcloud.ga2.v20250115.models.ReplaceListenerAdditionalCertRequest`
        :rtype: :class:`tencentcloud.ga2.v20250115.models.ReplaceListenerAdditionalCertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceListenerAdditionalCert", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceListenerAdditionalCertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))