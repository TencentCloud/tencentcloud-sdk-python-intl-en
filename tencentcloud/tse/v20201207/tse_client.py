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
from tencentcloud.tse.v20201207 import models


class TseClient(AbstractClient):
    _apiVersion = '2020-12-07'
    _endpoint = 'tse.intl.tencentcloudapi.com'
    _service = 'tse'


    def BindAutoScalerResourceStrategyToGroups(self, request):
        r"""Bind auto scaling policies to gateway groupings in batch

        :param request: Request instance for BindAutoScalerResourceStrategyToGroups.
        :type request: :class:`tencentcloud.tse.v20201207.models.BindAutoScalerResourceStrategyToGroupsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.BindAutoScalerResourceStrategyToGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindAutoScalerResourceStrategyToGroups", params, headers=headers)
            response = json.loads(body)
            model = models.BindAutoScalerResourceStrategyToGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseWafProtection(self, request):
        r"""Disables WAF protection

        :param request: Request instance for CloseWafProtection.
        :type request: :class:`tencentcloud.tse.v20201207.models.CloseWafProtectionRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CloseWafProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseWafProtection", params, headers=headers)
            response = json.loads(body)
            model = models.CloseWafProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAutoScalerResourceStrategy(self, request):
        r"""Create AS policy

        :param request: Request instance for CreateAutoScalerResourceStrategy.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateAutoScalerResourceStrategyRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateAutoScalerResourceStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAutoScalerResourceStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAutoScalerResourceStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGateway(self, request):
        r"""Create a cloud native API gateway instance

        :param request: Request instance for CreateCloudNativeAPIGateway.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGateway", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGatewayCanaryRule(self, request):
        r"""Create a grayscale rule for the cloud-native gateway

        :param request: Request instance for CreateCloudNativeAPIGatewayCanaryRule.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayCanaryRuleRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayCanaryRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewayCanaryRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayCanaryRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGatewayCertificate(self, request):
        r"""This API is used to create a cloud-native gateway certificate

        :param request: Request instance for CreateCloudNativeAPIGatewayCertificate.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayCertificateRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewayCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGatewayPublicNetwork(self, request):
        r"""Create a public network configuration

        :param request: Request instance for CreateCloudNativeAPIGatewayPublicNetwork.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayPublicNetworkRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayPublicNetworkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewayPublicNetwork", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayPublicNetworkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGatewayRoute(self, request):
        r"""This API is used to create a cloud-native gateway route.

        :param request: Request instance for CreateCloudNativeAPIGatewayRoute.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayRouteRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewayRoute", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGatewayRouteRateLimit(self, request):
        r"""This API is used to create a cloud-native gateway traffic throttling plugin.

        :param request: Request instance for CreateCloudNativeAPIGatewayRouteRateLimit.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayRouteRateLimitRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayRouteRateLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewayRouteRateLimit", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayRouteRateLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGatewayService(self, request):
        r"""Create a cloud-native gateway service

        :param request: Request instance for CreateCloudNativeAPIGatewayService.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayServiceRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewayService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudNativeAPIGatewayServiceRateLimit(self, request):
        r"""This API is used to create a traffic throttling plugin for a cloud-native gateway

        :param request: Request instance for CreateCloudNativeAPIGatewayServiceRateLimit.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayServiceRateLimitRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayServiceRateLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudNativeAPIGatewayServiceRateLimit", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudNativeAPIGatewayServiceRateLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGovernanceLaneGroups(self, request):
        r"""Create a lane group

        :param request: Request instance for CreateGovernanceLaneGroups.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateGovernanceLaneGroupsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateGovernanceLaneGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGovernanceLaneGroups", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGovernanceLaneGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNativeGatewayServerGroup(self, request):
        r"""Create a Cloud Native Gateway Engine group

        :param request: Request instance for CreateNativeGatewayServerGroup.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateNativeGatewayServerGroupRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateNativeGatewayServerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNativeGatewayServerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNativeGatewayServerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNativeGatewayServiceSource(self, request):
        r"""Create a gateway service source

        :param request: Request instance for CreateNativeGatewayServiceSource.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateNativeGatewayServiceSourceRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateNativeGatewayServiceSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNativeGatewayServiceSource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNativeGatewayServiceSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateOrModifyCloudNativeAPIGatewayCORS(self, request):
        r"""Create or edit a cloud-native gateway cross-domain configuration

        :param request: Request instance for CreateOrModifyCloudNativeAPIGatewayCORS.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateOrModifyCloudNativeAPIGatewayCORSRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateOrModifyCloudNativeAPIGatewayCORSResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrModifyCloudNativeAPIGatewayCORS", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrModifyCloudNativeAPIGatewayCORSResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWafDomains(self, request):
        r"""Create a WAF-protected domain name

        :param request: Request instance for CreateWafDomains.
        :type request: :class:`tencentcloud.tse.v20201207.models.CreateWafDomainsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.CreateWafDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWafDomains", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWafDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAutoScalerResourceStrategy(self, request):
        r"""Delete AS policy

        :param request: Request instance for DeleteAutoScalerResourceStrategy.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteAutoScalerResourceStrategyRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteAutoScalerResourceStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAutoScalerResourceStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAutoScalerResourceStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGateway(self, request):
        r"""Delete a cloud native API gateway instance

        :param request: Request instance for DeleteCloudNativeAPIGateway.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewayCORS(self, request):
        r"""This API is used to delete a cloud-native gateway cross-domain plug-in.

        :param request: Request instance for DeleteCloudNativeAPIGatewayCORS.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayCORSRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayCORSResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayCORS", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayCORSResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewayCanaryRule(self, request):
        r"""This API is used to delete the grayscale rule of the cloud-native gateway.

        :param request: Request instance for DeleteCloudNativeAPIGatewayCanaryRule.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayCanaryRuleRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayCanaryRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayCanaryRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayCanaryRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewayCertificate(self, request):
        r"""This API is used to delete a cloud-native gateway cert.

        :param request: Request instance for DeleteCloudNativeAPIGatewayCertificate.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayCertificateRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewayPublicNetwork(self, request):
        r"""Delete public network configuration

        :param request: Request instance for DeleteCloudNativeAPIGatewayPublicNetwork.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayPublicNetworkRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayPublicNetworkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayPublicNetwork", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayPublicNetworkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewayRoute(self, request):
        r"""Delete a cloud-native gateway route

        :param request: Request instance for DeleteCloudNativeAPIGatewayRoute.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayRouteRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayRoute", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewayRouteRateLimit(self, request):
        r"""This API is used to delete a traffic throttling plugin of a cloud-native gateway (Route).

        :param request: Request instance for DeleteCloudNativeAPIGatewayRouteRateLimit.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayRouteRateLimitRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayRouteRateLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayRouteRateLimit", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayRouteRateLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewayService(self, request):
        r"""This API is used to delete a cloud-native gateway service.

        :param request: Request instance for DeleteCloudNativeAPIGatewayService.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayServiceRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayService", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudNativeAPIGatewayServiceRateLimit(self, request):
        r"""This API is used to delete the traffic throttling plugin of a cloud-native gateway (Service).

        :param request: Request instance for DeleteCloudNativeAPIGatewayServiceRateLimit.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayServiceRateLimitRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayServiceRateLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudNativeAPIGatewayServiceRateLimit", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudNativeAPIGatewayServiceRateLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGovernanceLaneGroups(self, request):
        r"""Delete a lane group

        :param request: Request instance for DeleteGovernanceLaneGroups.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteGovernanceLaneGroupsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteGovernanceLaneGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGovernanceLaneGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGovernanceLaneGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNativeGatewayServerGroup(self, request):
        r"""Delete a Gateway Instance Group

        :param request: Request instance for DeleteNativeGatewayServerGroup.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteNativeGatewayServerGroupRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteNativeGatewayServerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNativeGatewayServerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNativeGatewayServerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNativeGatewayServiceSource(self, request):
        r"""Delete a gateway service source instance

        :param request: Request instance for DeleteNativeGatewayServiceSource.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteNativeGatewayServiceSourceRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteNativeGatewayServiceSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNativeGatewayServiceSource", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNativeGatewayServiceSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWafDomains(self, request):
        r"""Delete a WAF-protected domain name

        :param request: Request instance for DeleteWafDomains.
        :type request: :class:`tencentcloud.tse.v20201207.models.DeleteWafDomainsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DeleteWafDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWafDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWafDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoScalerResourceStrategies(self, request):
        r"""View AS policy list

        :param request: Request instance for DescribeAutoScalerResourceStrategies.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeAutoScalerResourceStrategiesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeAutoScalerResourceStrategiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoScalerResourceStrategies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoScalerResourceStrategiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoScalerResourceStrategyBindingGroups(self, request):
        r"""View gateway groupings bound to an auto scaling policy

        :param request: Request instance for DescribeAutoScalerResourceStrategyBindingGroups.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeAutoScalerResourceStrategyBindingGroupsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeAutoScalerResourceStrategyBindingGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoScalerResourceStrategyBindingGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoScalerResourceStrategyBindingGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGateway(self, request):
        r"""This API is used to obtain cloud native API gateway instance information.

        :param request: Request instance for DescribeCloudNativeAPIGateway.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayCORS(self, request):
        r"""Query cloud-native gateway cross-domain configuration

        :param request: Request instance for DescribeCloudNativeAPIGatewayCORS.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayCORSRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayCORSResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayCORS", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayCORSResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayCanaryRules(self, request):
        r"""Query the grayscale rule list of the cloud-native gateway

        :param request: Request instance for DescribeCloudNativeAPIGatewayCanaryRules.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayCanaryRulesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayCanaryRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayCanaryRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayCanaryRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayCertificateDetails(self, request):
        r"""Query the certificate detail of one cloud-native gateway

        :param request: Request instance for DescribeCloudNativeAPIGatewayCertificateDetails.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayCertificateDetailsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayCertificateDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayCertificateDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayCertificateDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayCertificates(self, request):
        r"""Query the certificate list of the cloud-native gateway

        :param request: Request instance for DescribeCloudNativeAPIGatewayCertificates.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayCertificatesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayCertificates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayCertificatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayConfig(self, request):
        r"""This API is used to obtain cloud native API gateway instance network configuration information

        :param request: Request instance for DescribeCloudNativeAPIGatewayConfig.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayConfigRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayInfoByIp(self, request):
        r"""Query cloud native gateway instance information based on public IP address

        :param request: Request instance for DescribeCloudNativeAPIGatewayInfoByIp.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayInfoByIpRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayInfoByIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayInfoByIp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayInfoByIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayNodes(self, request):
        r"""This API is used to get a cloud-native gateway node list

        :param request: Request instance for DescribeCloudNativeAPIGatewayNodes.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayNodesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayPorts(self, request):
        r"""Retrieve port information of a cloud native API gateway instance

        :param request: Request instance for DescribeCloudNativeAPIGatewayPorts.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayPortsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayPortsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayPorts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayPortsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayRouteRateLimit(self, request):
        r"""Query the traffic throttling plugin of a cloud-native gateway (Route).

        :param request: Request instance for DescribeCloudNativeAPIGatewayRouteRateLimit.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayRouteRateLimitRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayRouteRateLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayRouteRateLimit", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayRouteRateLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayRoutes(self, request):
        r"""Query the routing list of the cloud-native gateway

        :param request: Request instance for DescribeCloudNativeAPIGatewayRoutes.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayRoutesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayServiceRateLimit(self, request):
        r"""This API is used to query the traffic throttling plugin of a cloud-native gateway (Service).

        :param request: Request instance for DescribeCloudNativeAPIGatewayServiceRateLimit.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayServiceRateLimitRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayServiceRateLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayServiceRateLimit", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayServiceRateLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayServices(self, request):
        r"""Query the service list of the cloud-native gateway

        :param request: Request instance for DescribeCloudNativeAPIGatewayServices.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayServicesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayServicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayServices", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayServicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayServicesLight(self, request):
        r"""Lightweight query the service list of the cloud-native gateway

        :param request: Request instance for DescribeCloudNativeAPIGatewayServicesLight.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayServicesLightRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayServicesLightResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayServicesLight", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayServicesLightResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGatewayUpstream(self, request):
        r"""This API is used to query the Upstream list in the service detail of a cloud-native gateway.

        :param request: Request instance for DescribeCloudNativeAPIGatewayUpstream.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayUpstreamRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayUpstreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGatewayUpstream", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewayUpstreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudNativeAPIGateways(self, request):
        r"""This API is used to obtain the cloud native API gateway instance list.

        :param request: Request instance for DescribeCloudNativeAPIGateways.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewaysRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudNativeAPIGateways", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudNativeAPIGatewaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGovernanceLaneGroups(self, request):
        r"""Query lane group list

        :param request: Request instance for DescribeGovernanceLaneGroups.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeGovernanceLaneGroupsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeGovernanceLaneGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGovernanceLaneGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGovernanceLaneGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNativeGatewayServerGroups(self, request):
        r"""Query cloud native gateway group information

        :param request: Request instance for DescribeNativeGatewayServerGroups.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeNativeGatewayServerGroupsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeNativeGatewayServerGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNativeGatewayServerGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNativeGatewayServerGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNativeGatewayServiceSources(self, request):
        r"""Query the instance list of the gateway service source

        :param request: Request instance for DescribeNativeGatewayServiceSources.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeNativeGatewayServiceSourcesRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeNativeGatewayServiceSourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNativeGatewayServiceSources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNativeGatewayServiceSourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOneCloudNativeAPIGatewayService(self, request):
        r"""This API is used to obtain the service detail of the cloud-native gateway.

        :param request: Request instance for DescribeOneCloudNativeAPIGatewayService.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeOneCloudNativeAPIGatewayServiceRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeOneCloudNativeAPIGatewayServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOneCloudNativeAPIGatewayService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOneCloudNativeAPIGatewayServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublicAddressConfig(self, request):
        r"""Query public IP address info

        :param request: Request instance for DescribePublicAddressConfig.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribePublicAddressConfigRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribePublicAddressConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicAddressConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicAddressConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublicNetwork(self, request):
        r"""Query the public network details of a cloud native API gateway instance

        :param request: Request instance for DescribePublicNetwork.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribePublicNetworkRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribePublicNetworkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublicNetwork", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublicNetworkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUpstreamHealthCheckConfig(self, request):
        r"""This API is used to obtain the health check configuration of the cloud-native gateway service.

        :param request: Request instance for DescribeUpstreamHealthCheckConfig.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeUpstreamHealthCheckConfigRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeUpstreamHealthCheckConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUpstreamHealthCheckConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUpstreamHealthCheckConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWafDomains(self, request):
        r"""Query a WAF-protected domain name

        :param request: Request instance for DescribeWafDomains.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeWafDomainsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeWafDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWafDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWafDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWafProtection(self, request):
        r"""Query WAF protection status

        :param request: Request instance for DescribeWafProtection.
        :type request: :class:`tencentcloud.tse.v20201207.models.DescribeWafProtectionRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.DescribeWafProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWafProtection", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWafProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAutoScalerResourceStrategy(self, request):
        r"""Update AS policy

        :param request: Request instance for ModifyAutoScalerResourceStrategy.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyAutoScalerResourceStrategyRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyAutoScalerResourceStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAutoScalerResourceStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAutoScalerResourceStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGateway(self, request):
        r"""This API is used to modify the basic information of a cloud native API gateway instance.

        :param request: Request instance for ModifyCloudNativeAPIGateway.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGateway", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayCanaryRule(self, request):
        r"""Modify the grayscale rule of the cloud-native gateway

        :param request: Request instance for ModifyCloudNativeAPIGatewayCanaryRule.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayCanaryRuleRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayCanaryRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayCanaryRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayCanaryRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayCertificate(self, request):
        r"""Update the cloud-native gateway certificate

        :param request: Request instance for ModifyCloudNativeAPIGatewayCertificate.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayCertificateRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayRoute(self, request):
        r"""This API is used to modify a cloud-native gateway route.

        :param request: Request instance for ModifyCloudNativeAPIGatewayRoute.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayRouteRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayRoute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayRouteRateLimit(self, request):
        r"""This API is used to modify the traffic throttling plugin of a cloud-native gateway (Route).

        :param request: Request instance for ModifyCloudNativeAPIGatewayRouteRateLimit.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayRouteRateLimitRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayRouteRateLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayRouteRateLimit", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayRouteRateLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayService(self, request):
        r"""Modify a cloud-native gateway service

        :param request: Request instance for ModifyCloudNativeAPIGatewayService.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayServiceRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayService", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudNativeAPIGatewayServiceRateLimit(self, request):
        r"""This API is used to modify the traffic throttling plugin of a cloud-native gateway (Service).

        :param request: Request instance for ModifyCloudNativeAPIGatewayServiceRateLimit.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayServiceRateLimitRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyCloudNativeAPIGatewayServiceRateLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudNativeAPIGatewayServiceRateLimit", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudNativeAPIGatewayServiceRateLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyConsoleNetwork(self, request):
        r"""Modify the network configuration of the Konga gateway instance

        :param request: Request instance for ModifyConsoleNetwork.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyConsoleNetworkRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyConsoleNetworkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConsoleNetwork", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConsoleNetworkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGovernanceLaneGroups(self, request):
        r"""Create a lane group

        :param request: Request instance for ModifyGovernanceLaneGroups.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyGovernanceLaneGroupsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyGovernanceLaneGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGovernanceLaneGroups", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGovernanceLaneGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNativeGatewayServerGroup(self, request):
        r"""Modify the basic information of a cloud native API gateway instance group

        :param request: Request instance for ModifyNativeGatewayServerGroup.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyNativeGatewayServerGroupRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyNativeGatewayServerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNativeGatewayServerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNativeGatewayServerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNativeGatewayServiceSource(self, request):
        r"""Modify the gateway service source

        :param request: Request instance for ModifyNativeGatewayServiceSource.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyNativeGatewayServiceSourceRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyNativeGatewayServiceSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNativeGatewayServiceSource", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNativeGatewayServiceSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetworkAccessStrategy(self, request):
        r"""Modify the access policy of the Kong cloud native API gateway instance to support allowlist or blocklist.

        :param request: Request instance for ModifyNetworkAccessStrategy.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyNetworkAccessStrategyRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyNetworkAccessStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetworkAccessStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetworkAccessStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetworkBasicInfo(self, request):
        r"""This API is used to modify the basic information of a cloud native API gateway instance network, such as bandwidth and description, as well as specification upgrade. Only modification of client public network or private network information is supported.

        :param request: Request instance for ModifyNetworkBasicInfo.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyNetworkBasicInfoRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyNetworkBasicInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetworkBasicInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetworkBasicInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUpstreamNodeStatus(self, request):
        r"""Modify the node health status of the upstream instance for the cloud-native gateway

        :param request: Request instance for ModifyUpstreamNodeStatus.
        :type request: :class:`tencentcloud.tse.v20201207.models.ModifyUpstreamNodeStatusRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.ModifyUpstreamNodeStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUpstreamNodeStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUpstreamNodeStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenWafProtection(self, request):
        r"""Enable WAF protection

        :param request: Request instance for OpenWafProtection.
        :type request: :class:`tencentcloud.tse.v20201207.models.OpenWafProtectionRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.OpenWafProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenWafProtection", params, headers=headers)
            response = json.loads(body)
            model = models.OpenWafProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindAutoScalerResourceStrategyFromGroups(self, request):
        r"""Unbind gateway groupings in batch with auto scaling policy

        :param request: Request instance for UnbindAutoScalerResourceStrategyFromGroups.
        :type request: :class:`tencentcloud.tse.v20201207.models.UnbindAutoScalerResourceStrategyFromGroupsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.UnbindAutoScalerResourceStrategyFromGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindAutoScalerResourceStrategyFromGroups", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindAutoScalerResourceStrategyFromGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCloudNativeAPIGatewayCertificateInfo(self, request):
        r"""Modify the certificate information of a cloud-native gateway

        :param request: Request instance for UpdateCloudNativeAPIGatewayCertificateInfo.
        :type request: :class:`tencentcloud.tse.v20201207.models.UpdateCloudNativeAPIGatewayCertificateInfoRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.UpdateCloudNativeAPIGatewayCertificateInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCloudNativeAPIGatewayCertificateInfo", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCloudNativeAPIGatewayCertificateInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCloudNativeAPIGatewaySpec(self, request):
        r"""Modify the node specification information of a cloud native API gateway instance, such as node scaling or specification adjustment

        :param request: Request instance for UpdateCloudNativeAPIGatewaySpec.
        :type request: :class:`tencentcloud.tse.v20201207.models.UpdateCloudNativeAPIGatewaySpecRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.UpdateCloudNativeAPIGatewaySpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCloudNativeAPIGatewaySpec", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCloudNativeAPIGatewaySpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateUpstreamHealthCheckConfig(self, request):
        r"""This API is used to update the health check configuration of the cloud-native gateway.

        :param request: Request instance for UpdateUpstreamHealthCheckConfig.
        :type request: :class:`tencentcloud.tse.v20201207.models.UpdateUpstreamHealthCheckConfigRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.UpdateUpstreamHealthCheckConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateUpstreamHealthCheckConfig", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateUpstreamHealthCheckConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateUpstreamTargets(self, request):
        r"""Refresh the upstream instance list of the gateway, only supported for the IPList service type

        :param request: Request instance for UpdateUpstreamTargets.
        :type request: :class:`tencentcloud.tse.v20201207.models.UpdateUpstreamTargetsRequest`
        :rtype: :class:`tencentcloud.tse.v20201207.models.UpdateUpstreamTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateUpstreamTargets", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateUpstreamTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))