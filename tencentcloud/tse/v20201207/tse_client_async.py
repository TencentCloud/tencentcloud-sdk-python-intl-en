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
from tencentcloud.tse.v20201207 import models
from typing import Dict


class TseClient(AbstractClient):
    _apiVersion = '2020-12-07'
    _endpoint = 'tse.intl.tencentcloudapi.com'
    _service = 'tse'

    async def BindAutoScalerResourceStrategyToGroups(
            self,
            request: models.BindAutoScalerResourceStrategyToGroupsRequest,
            opts: Dict = None,
    ) -> models.BindAutoScalerResourceStrategyToGroupsResponse:
        """
        Bind auto scaling policies to gateway groupings in batch
        """
        
        kwargs = {}
        kwargs["action"] = "BindAutoScalerResourceStrategyToGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindAutoScalerResourceStrategyToGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseWafProtection(
            self,
            request: models.CloseWafProtectionRequest,
            opts: Dict = None,
    ) -> models.CloseWafProtectionResponse:
        """
        Disables WAF protection
        """
        
        kwargs = {}
        kwargs["action"] = "CloseWafProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseWafProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAutoScalerResourceStrategy(
            self,
            request: models.CreateAutoScalerResourceStrategyRequest,
            opts: Dict = None,
    ) -> models.CreateAutoScalerResourceStrategyResponse:
        """
        Create AS policy
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAutoScalerResourceStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAutoScalerResourceStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGateway(
            self,
            request: models.CreateCloudNativeAPIGatewayRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayResponse:
        """
        Create a cloud native API gateway instance
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewayCanaryRule(
            self,
            request: models.CreateCloudNativeAPIGatewayCanaryRuleRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayCanaryRuleResponse:
        """
        Create a grayscale rule for the cloud-native gateway
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewayCanaryRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayCanaryRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewayCertificate(
            self,
            request: models.CreateCloudNativeAPIGatewayCertificateRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayCertificateResponse:
        """
        This API is used to create a cloud-native gateway certificate
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewayCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewayPublicNetwork(
            self,
            request: models.CreateCloudNativeAPIGatewayPublicNetworkRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayPublicNetworkResponse:
        """
        Create a public network configuration
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewayPublicNetwork"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayPublicNetworkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewayRoute(
            self,
            request: models.CreateCloudNativeAPIGatewayRouteRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayRouteResponse:
        """
        This API is used to create a cloud-native gateway route.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewayRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewayRouteRateLimit(
            self,
            request: models.CreateCloudNativeAPIGatewayRouteRateLimitRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayRouteRateLimitResponse:
        """
        This API is used to create a cloud-native gateway traffic throttling plugin.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewayRouteRateLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayRouteRateLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewayService(
            self,
            request: models.CreateCloudNativeAPIGatewayServiceRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayServiceResponse:
        """
        Create a cloud-native gateway service
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewayService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudNativeAPIGatewayServiceRateLimit(
            self,
            request: models.CreateCloudNativeAPIGatewayServiceRateLimitRequest,
            opts: Dict = None,
    ) -> models.CreateCloudNativeAPIGatewayServiceRateLimitResponse:
        """
        This API is used to create a traffic throttling plugin for a cloud-native gateway
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudNativeAPIGatewayServiceRateLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudNativeAPIGatewayServiceRateLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGovernanceLaneGroups(
            self,
            request: models.CreateGovernanceLaneGroupsRequest,
            opts: Dict = None,
    ) -> models.CreateGovernanceLaneGroupsResponse:
        """
        Create a lane group
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGovernanceLaneGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGovernanceLaneGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNativeGatewayServerGroup(
            self,
            request: models.CreateNativeGatewayServerGroupRequest,
            opts: Dict = None,
    ) -> models.CreateNativeGatewayServerGroupResponse:
        """
        Create a Cloud Native Gateway Engine group
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNativeGatewayServerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNativeGatewayServerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNativeGatewayServiceSource(
            self,
            request: models.CreateNativeGatewayServiceSourceRequest,
            opts: Dict = None,
    ) -> models.CreateNativeGatewayServiceSourceResponse:
        """
        Create a gateway service source
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNativeGatewayServiceSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNativeGatewayServiceSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOrModifyCloudNativeAPIGatewayCORS(
            self,
            request: models.CreateOrModifyCloudNativeAPIGatewayCORSRequest,
            opts: Dict = None,
    ) -> models.CreateOrModifyCloudNativeAPIGatewayCORSResponse:
        """
        Create or edit a cloud-native gateway cross-domain configuration
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOrModifyCloudNativeAPIGatewayCORS"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOrModifyCloudNativeAPIGatewayCORSResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWafDomains(
            self,
            request: models.CreateWafDomainsRequest,
            opts: Dict = None,
    ) -> models.CreateWafDomainsResponse:
        """
        Create a WAF-protected domain name
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWafDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWafDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAutoScalerResourceStrategy(
            self,
            request: models.DeleteAutoScalerResourceStrategyRequest,
            opts: Dict = None,
    ) -> models.DeleteAutoScalerResourceStrategyResponse:
        """
        Delete AS policy
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAutoScalerResourceStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAutoScalerResourceStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGateway(
            self,
            request: models.DeleteCloudNativeAPIGatewayRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayResponse:
        """
        Delete a cloud native API gateway instance
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayCORS(
            self,
            request: models.DeleteCloudNativeAPIGatewayCORSRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayCORSResponse:
        """
        This API is used to delete a cloud-native gateway cross-domain plug-in.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayCORS"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayCORSResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayCanaryRule(
            self,
            request: models.DeleteCloudNativeAPIGatewayCanaryRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayCanaryRuleResponse:
        """
        This API is used to delete the grayscale rule of the cloud-native gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayCanaryRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayCanaryRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayCertificate(
            self,
            request: models.DeleteCloudNativeAPIGatewayCertificateRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayCertificateResponse:
        """
        This API is used to delete a cloud-native gateway cert.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayPublicNetwork(
            self,
            request: models.DeleteCloudNativeAPIGatewayPublicNetworkRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayPublicNetworkResponse:
        """
        Delete public network configuration
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayPublicNetwork"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayPublicNetworkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayRoute(
            self,
            request: models.DeleteCloudNativeAPIGatewayRouteRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayRouteResponse:
        """
        Delete a cloud-native gateway route
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayRouteRateLimit(
            self,
            request: models.DeleteCloudNativeAPIGatewayRouteRateLimitRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayRouteRateLimitResponse:
        """
        This API is used to delete a traffic throttling plugin of a cloud-native gateway (Route).
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayRouteRateLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayRouteRateLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayService(
            self,
            request: models.DeleteCloudNativeAPIGatewayServiceRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayServiceResponse:
        """
        This API is used to delete a cloud-native gateway service.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCloudNativeAPIGatewayServiceRateLimit(
            self,
            request: models.DeleteCloudNativeAPIGatewayServiceRateLimitRequest,
            opts: Dict = None,
    ) -> models.DeleteCloudNativeAPIGatewayServiceRateLimitResponse:
        """
        This API is used to delete the traffic throttling plugin of a cloud-native gateway (Service).
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCloudNativeAPIGatewayServiceRateLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCloudNativeAPIGatewayServiceRateLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGovernanceLaneGroups(
            self,
            request: models.DeleteGovernanceLaneGroupsRequest,
            opts: Dict = None,
    ) -> models.DeleteGovernanceLaneGroupsResponse:
        """
        Delete a lane group
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGovernanceLaneGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGovernanceLaneGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNativeGatewayServerGroup(
            self,
            request: models.DeleteNativeGatewayServerGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteNativeGatewayServerGroupResponse:
        """
        Delete a Gateway Instance Group
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNativeGatewayServerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNativeGatewayServerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNativeGatewayServiceSource(
            self,
            request: models.DeleteNativeGatewayServiceSourceRequest,
            opts: Dict = None,
    ) -> models.DeleteNativeGatewayServiceSourceResponse:
        """
        Delete a gateway service source instance
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNativeGatewayServiceSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNativeGatewayServiceSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWafDomains(
            self,
            request: models.DeleteWafDomainsRequest,
            opts: Dict = None,
    ) -> models.DeleteWafDomainsResponse:
        """
        Delete a WAF-protected domain name
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWafDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWafDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoScalerResourceStrategies(
            self,
            request: models.DescribeAutoScalerResourceStrategiesRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoScalerResourceStrategiesResponse:
        """
        View AS policy list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoScalerResourceStrategies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoScalerResourceStrategiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoScalerResourceStrategyBindingGroups(
            self,
            request: models.DescribeAutoScalerResourceStrategyBindingGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoScalerResourceStrategyBindingGroupsResponse:
        """
        View gateway groupings bound to an auto scaling policy
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoScalerResourceStrategyBindingGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoScalerResourceStrategyBindingGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGateway(
            self,
            request: models.DescribeCloudNativeAPIGatewayRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayResponse:
        """
        This API is used to obtain cloud native API gateway instance information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayCORS(
            self,
            request: models.DescribeCloudNativeAPIGatewayCORSRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayCORSResponse:
        """
        Query cloud-native gateway cross-domain configuration
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayCORS"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayCORSResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayCanaryRules(
            self,
            request: models.DescribeCloudNativeAPIGatewayCanaryRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayCanaryRulesResponse:
        """
        Query the grayscale rule list of the cloud-native gateway
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayCanaryRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayCanaryRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayCertificateDetails(
            self,
            request: models.DescribeCloudNativeAPIGatewayCertificateDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayCertificateDetailsResponse:
        """
        Query the certificate detail of one cloud-native gateway
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayCertificateDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayCertificateDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayCertificates(
            self,
            request: models.DescribeCloudNativeAPIGatewayCertificatesRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayCertificatesResponse:
        """
        Query the certificate list of the cloud-native gateway
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayCertificates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayCertificatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayConfig(
            self,
            request: models.DescribeCloudNativeAPIGatewayConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayConfigResponse:
        """
        This API is used to obtain cloud native API gateway instance network configuration information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayInfoByIp(
            self,
            request: models.DescribeCloudNativeAPIGatewayInfoByIpRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayInfoByIpResponse:
        """
        Query cloud native gateway instance information based on public IP address
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayInfoByIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayInfoByIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayNodes(
            self,
            request: models.DescribeCloudNativeAPIGatewayNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayNodesResponse:
        """
        This API is used to get a cloud-native gateway node list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayPorts(
            self,
            request: models.DescribeCloudNativeAPIGatewayPortsRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayPortsResponse:
        """
        Retrieve port information of a cloud native API gateway instance
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayPorts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayPortsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayRouteRateLimit(
            self,
            request: models.DescribeCloudNativeAPIGatewayRouteRateLimitRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayRouteRateLimitResponse:
        """
        Query the traffic throttling plugin of a cloud-native gateway (Route).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayRouteRateLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayRouteRateLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayRoutes(
            self,
            request: models.DescribeCloudNativeAPIGatewayRoutesRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayRoutesResponse:
        """
        Query the routing list of the cloud-native gateway
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayServiceRateLimit(
            self,
            request: models.DescribeCloudNativeAPIGatewayServiceRateLimitRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayServiceRateLimitResponse:
        """
        This API is used to query the traffic throttling plugin of a cloud-native gateway (Service).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayServiceRateLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayServiceRateLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayServices(
            self,
            request: models.DescribeCloudNativeAPIGatewayServicesRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayServicesResponse:
        """
        Query the service list of the cloud-native gateway
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayServices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayServicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayServicesLight(
            self,
            request: models.DescribeCloudNativeAPIGatewayServicesLightRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayServicesLightResponse:
        """
        Lightweight query the service list of the cloud-native gateway
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayServicesLight"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayServicesLightResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGatewayUpstream(
            self,
            request: models.DescribeCloudNativeAPIGatewayUpstreamRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewayUpstreamResponse:
        """
        This API is used to query the Upstream list in the service detail of a cloud-native gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGatewayUpstream"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewayUpstreamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCloudNativeAPIGateways(
            self,
            request: models.DescribeCloudNativeAPIGatewaysRequest,
            opts: Dict = None,
    ) -> models.DescribeCloudNativeAPIGatewaysResponse:
        """
        This API is used to obtain the cloud native API gateway instance list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCloudNativeAPIGateways"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCloudNativeAPIGatewaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGovernanceLaneGroups(
            self,
            request: models.DescribeGovernanceLaneGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeGovernanceLaneGroupsResponse:
        """
        Query lane group list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGovernanceLaneGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGovernanceLaneGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNativeGatewayServerGroups(
            self,
            request: models.DescribeNativeGatewayServerGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeNativeGatewayServerGroupsResponse:
        """
        Query cloud native gateway group information
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNativeGatewayServerGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNativeGatewayServerGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNativeGatewayServiceSources(
            self,
            request: models.DescribeNativeGatewayServiceSourcesRequest,
            opts: Dict = None,
    ) -> models.DescribeNativeGatewayServiceSourcesResponse:
        """
        Query the instance list of the gateway service source
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNativeGatewayServiceSources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNativeGatewayServiceSourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOneCloudNativeAPIGatewayService(
            self,
            request: models.DescribeOneCloudNativeAPIGatewayServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeOneCloudNativeAPIGatewayServiceResponse:
        """
        This API is used to obtain the service detail of the cloud-native gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOneCloudNativeAPIGatewayService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOneCloudNativeAPIGatewayServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicAddressConfig(
            self,
            request: models.DescribePublicAddressConfigRequest,
            opts: Dict = None,
    ) -> models.DescribePublicAddressConfigResponse:
        """
        Query public IP address info
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicAddressConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicAddressConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePublicNetwork(
            self,
            request: models.DescribePublicNetworkRequest,
            opts: Dict = None,
    ) -> models.DescribePublicNetworkResponse:
        """
        Query the public network details of a cloud native API gateway instance
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePublicNetwork"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePublicNetworkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUpstreamHealthCheckConfig(
            self,
            request: models.DescribeUpstreamHealthCheckConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeUpstreamHealthCheckConfigResponse:
        """
        This API is used to obtain the health check configuration of the cloud-native gateway service.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUpstreamHealthCheckConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUpstreamHealthCheckConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWafDomains(
            self,
            request: models.DescribeWafDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeWafDomainsResponse:
        """
        Query a WAF-protected domain name
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWafDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWafDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWafProtection(
            self,
            request: models.DescribeWafProtectionRequest,
            opts: Dict = None,
    ) -> models.DescribeWafProtectionResponse:
        """
        Query WAF protection status
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWafProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWafProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoScalerResourceStrategy(
            self,
            request: models.ModifyAutoScalerResourceStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoScalerResourceStrategyResponse:
        """
        Update AS policy
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoScalerResourceStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoScalerResourceStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGateway(
            self,
            request: models.ModifyCloudNativeAPIGatewayRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayResponse:
        """
        This API is used to modify the basic information of a cloud native API gateway instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayCanaryRule(
            self,
            request: models.ModifyCloudNativeAPIGatewayCanaryRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayCanaryRuleResponse:
        """
        Modify the grayscale rule of the cloud-native gateway
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayCanaryRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayCanaryRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayCertificate(
            self,
            request: models.ModifyCloudNativeAPIGatewayCertificateRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayCertificateResponse:
        """
        Update the cloud-native gateway certificate
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayRoute(
            self,
            request: models.ModifyCloudNativeAPIGatewayRouteRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayRouteResponse:
        """
        This API is used to modify a cloud-native gateway route.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayRouteRateLimit(
            self,
            request: models.ModifyCloudNativeAPIGatewayRouteRateLimitRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayRouteRateLimitResponse:
        """
        This API is used to modify the traffic throttling plugin of a cloud-native gateway (Route).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayRouteRateLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayRouteRateLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayService(
            self,
            request: models.ModifyCloudNativeAPIGatewayServiceRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayServiceResponse:
        """
        Modify a cloud-native gateway service
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCloudNativeAPIGatewayServiceRateLimit(
            self,
            request: models.ModifyCloudNativeAPIGatewayServiceRateLimitRequest,
            opts: Dict = None,
    ) -> models.ModifyCloudNativeAPIGatewayServiceRateLimitResponse:
        """
        This API is used to modify the traffic throttling plugin of a cloud-native gateway (Service).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCloudNativeAPIGatewayServiceRateLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCloudNativeAPIGatewayServiceRateLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConsoleNetwork(
            self,
            request: models.ModifyConsoleNetworkRequest,
            opts: Dict = None,
    ) -> models.ModifyConsoleNetworkResponse:
        """
        Modify the network configuration of the Konga gateway instance
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConsoleNetwork"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConsoleNetworkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGovernanceLaneGroups(
            self,
            request: models.ModifyGovernanceLaneGroupsRequest,
            opts: Dict = None,
    ) -> models.ModifyGovernanceLaneGroupsResponse:
        """
        Create a lane group
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGovernanceLaneGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGovernanceLaneGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNativeGatewayServerGroup(
            self,
            request: models.ModifyNativeGatewayServerGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyNativeGatewayServerGroupResponse:
        """
        Modify the basic information of a cloud native API gateway instance group
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNativeGatewayServerGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNativeGatewayServerGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNativeGatewayServiceSource(
            self,
            request: models.ModifyNativeGatewayServiceSourceRequest,
            opts: Dict = None,
    ) -> models.ModifyNativeGatewayServiceSourceResponse:
        """
        Modify the gateway service source
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNativeGatewayServiceSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNativeGatewayServiceSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetworkAccessStrategy(
            self,
            request: models.ModifyNetworkAccessStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyNetworkAccessStrategyResponse:
        """
        Modify the access policy of the Kong cloud native API gateway instance to support allowlist or blocklist.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetworkAccessStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetworkAccessStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetworkBasicInfo(
            self,
            request: models.ModifyNetworkBasicInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyNetworkBasicInfoResponse:
        """
        This API is used to modify the basic information of a cloud native API gateway instance network, such as bandwidth and description, as well as specification upgrade. Only modification of client public network or private network information is supported.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetworkBasicInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetworkBasicInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUpstreamNodeStatus(
            self,
            request: models.ModifyUpstreamNodeStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyUpstreamNodeStatusResponse:
        """
        Modify the node health status of the upstream instance for the cloud-native gateway
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUpstreamNodeStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUpstreamNodeStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenWafProtection(
            self,
            request: models.OpenWafProtectionRequest,
            opts: Dict = None,
    ) -> models.OpenWafProtectionResponse:
        """
        Enable WAF protection
        """
        
        kwargs = {}
        kwargs["action"] = "OpenWafProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenWafProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindAutoScalerResourceStrategyFromGroups(
            self,
            request: models.UnbindAutoScalerResourceStrategyFromGroupsRequest,
            opts: Dict = None,
    ) -> models.UnbindAutoScalerResourceStrategyFromGroupsResponse:
        """
        Unbind gateway groupings in batch with auto scaling policy
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindAutoScalerResourceStrategyFromGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindAutoScalerResourceStrategyFromGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCloudNativeAPIGatewayCertificateInfo(
            self,
            request: models.UpdateCloudNativeAPIGatewayCertificateInfoRequest,
            opts: Dict = None,
    ) -> models.UpdateCloudNativeAPIGatewayCertificateInfoResponse:
        """
        Modify the certificate information of a cloud-native gateway
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCloudNativeAPIGatewayCertificateInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCloudNativeAPIGatewayCertificateInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCloudNativeAPIGatewaySpec(
            self,
            request: models.UpdateCloudNativeAPIGatewaySpecRequest,
            opts: Dict = None,
    ) -> models.UpdateCloudNativeAPIGatewaySpecResponse:
        """
        Modify the node specification information of a cloud native API gateway instance, such as node scaling or specification adjustment
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCloudNativeAPIGatewaySpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCloudNativeAPIGatewaySpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUpstreamHealthCheckConfig(
            self,
            request: models.UpdateUpstreamHealthCheckConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateUpstreamHealthCheckConfigResponse:
        """
        This API is used to update the health check configuration of the cloud-native gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUpstreamHealthCheckConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUpstreamHealthCheckConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUpstreamTargets(
            self,
            request: models.UpdateUpstreamTargetsRequest,
            opts: Dict = None,
    ) -> models.UpdateUpstreamTargetsResponse:
        """
        Refresh the upstream instance list of the gateway, only supported for the IPList service type
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUpstreamTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUpstreamTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)