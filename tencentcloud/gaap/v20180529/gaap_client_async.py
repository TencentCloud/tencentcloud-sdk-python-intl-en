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
from tencentcloud.gaap.v20180529 import models
from typing import Dict


class GaapClient(AbstractClient):
    _apiVersion = '2018-05-29'
    _endpoint = 'gaap.intl.tencentcloudapi.com'
    _service = 'gaap'

    async def AddRealServers(
            self,
            request: models.AddRealServersRequest,
            opts: Dict = None,
    ) -> models.AddRealServersResponse:
        """
        This API is used to add the information of the origin server (server), which supports IP or the domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "AddRealServers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddRealServersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindListenerRealServers(
            self,
            request: models.BindListenerRealServersRequest,
            opts: Dict = None,
    ) -> models.BindListenerRealServersResponse:
        """
        This API (BindListenerRealServers) is used for the TCP/UDP listener to bind/unbind the origin server.
        Note: This API unbinds the previously bound origin servers, and binds the origin servers selected for this call. For example, the previously bound origin servers are A, B and C, and the origin servers selected for this call are C, D and E, then the origin servers bound after this call will be C, D and E.
        """
        
        kwargs = {}
        kwargs["action"] = "BindListenerRealServers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindListenerRealServersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindRuleRealServers(
            self,
            request: models.BindRuleRealServersRequest,
            opts: Dict = None,
    ) -> models.BindRuleRealServersResponse:
        """
        This API is used to bind an origin server to the forwarding rules of layer-7 listeners. Note: This API unbinds all previously bound origin servers before binding those selected.
        """
        
        kwargs = {}
        kwargs["action"] = "BindRuleRealServers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindRuleRealServersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckProxyCreate(
            self,
            request: models.CheckProxyCreateRequest,
            opts: Dict = None,
    ) -> models.CheckProxyCreateResponse:
        """
        This API (CheckProxyCreate) is used to query whether an acceleration connection with the specified configuration can be created.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckProxyCreate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckProxyCreateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseProxies(
            self,
            request: models.CloseProxiesRequest,
            opts: Dict = None,
    ) -> models.CloseProxiesResponse:
        """
        This API (CloseProxies) is used to disable connections. If disabled, no traffic will be generated, but the basic configuration fee will still be incurred.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseProxies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseProxiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseProxyGroup(
            self,
            request: models.CloseProxyGroupRequest,
            opts: Dict = None,
    ) -> models.CloseProxyGroupResponse:
        """
        This API is used to disable a connection group. Once disabled, the connection group will no longer generate traffic, but the basic connection configuration fees will still be incurred every day.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseProxyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseProxyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloseSecurityPolicy(
            self,
            request: models.CloseSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.CloseSecurityPolicyResponse:
        """
        This API is used to disable a security policy.
        """
        
        kwargs = {}
        kwargs["action"] = "CloseSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloseSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCertificate(
            self,
            request: models.CreateCertificateRequest,
            opts: Dict = None,
    ) -> models.CreateCertificateResponse:
        """
        This API (CreateCertificate) is used to create the GAAP certificates and configuration files, including basic authentication configuration files, client CA certificates, server SSL certificates, GAAP SSL certificates, and origin server CA certificates.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCustomHeader(
            self,
            request: models.CreateCustomHeaderRequest,
            opts: Dict = None,
    ) -> models.CreateCustomHeaderResponse:
        """
        This API is used to create a custom header of the HTTP/HTTPS listener. When client requests reach the listener, they will be forwarded to the origin with this custom hearer.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCustomHeader"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCustomHeaderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDomain(
            self,
            request: models.CreateDomainRequest,
            opts: Dict = None,
    ) -> models.CreateDomainResponse:
        """
        This API (CreateDomain) is used to create the access domain name for the HTTP/HTTPS listener. Clients request the backend data by accessing this domain.
        This API only supports connections of version 3.0.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDomainErrorPageInfo(
            self,
            request: models.CreateDomainErrorPageInfoRequest,
            opts: Dict = None,
    ) -> models.CreateDomainErrorPageInfoResponse:
        """
        This API is used to customize the error code of an error response to the specified domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDomainErrorPageInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDomainErrorPageInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHTTPListener(
            self,
            request: models.CreateHTTPListenerRequest,
            opts: Dict = None,
    ) -> models.CreateHTTPListenerResponse:
        """
        This API (CreateHTTPListener) is used to create an HTTP listener in the connection instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHTTPListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHTTPListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHTTPSListener(
            self,
            request: models.CreateHTTPSListenerRequest,
            opts: Dict = None,
    ) -> models.CreateHTTPSListenerResponse:
        """
        This API (CreateHTTPListener) is used to create an HTTPS listener in the connection instance.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHTTPSListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHTTPSListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProxy(
            self,
            request: models.CreateProxyRequest,
            opts: Dict = None,
    ) -> models.CreateProxyResponse:
        """
        This API is used to create/replicate an acceleration connection with the specified configuration. To replicate a connection, the basic configuration parameters need to be set for the new connection, and `ClonedProxyId` is needed to identify the replicated connection.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProxyGroup(
            self,
            request: models.CreateProxyGroupRequest,
            opts: Dict = None,
    ) -> models.CreateProxyGroupResponse:
        """
        This API (CreateProxyGroup) is used to create a connection group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProxyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProxyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProxyGroupDomain(
            self,
            request: models.CreateProxyGroupDomainRequest,
            opts: Dict = None,
    ) -> models.CreateProxyGroupDomainResponse:
        """
        This API (CreateProxyGroupDomain) is used to create the connection group domain name, and enable the domain name resolution.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProxyGroupDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProxyGroupDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRule(
            self,
            request: models.CreateRuleRequest,
            opts: Dict = None,
    ) -> models.CreateRuleResponse:
        """
        This API (CreateRule) is used to create the forwarding rules of HTTP/HTTPS listeners.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityPolicy(
            self,
            request: models.CreateSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityPolicyResponse:
        """
        This API is used to create security policies.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityRules(
            self,
            request: models.CreateSecurityRulesRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityRulesResponse:
        """
        This API is used to add security policy rules.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTCPListeners(
            self,
            request: models.CreateTCPListenersRequest,
            opts: Dict = None,
    ) -> models.CreateTCPListenersResponse:
        """
        This API (CreateTCPListeners) is used to batch create TCP listeners of single connections or connection groups.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTCPListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTCPListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUDPListeners(
            self,
            request: models.CreateUDPListenersRequest,
            opts: Dict = None,
    ) -> models.CreateUDPListenersResponse:
        """
        This API (CreateTCPListeners) is used to batch create UDP listeners of single connections or connection groups.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUDPListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUDPListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCertificate(
            self,
            request: models.DeleteCertificateRequest,
            opts: Dict = None,
    ) -> models.DeleteCertificateResponse:
        """
        This API is used to delete a certificate.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDomain(
            self,
            request: models.DeleteDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteDomainResponse:
        """
        This API (DeleteDomain) is only applicable to layer-7 listeners. It is used to delete the domain names of this listener, and all the rules under the domain name. All rules bound to the origin server are unbound automatically.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDomainErrorPageInfo(
            self,
            request: models.DeleteDomainErrorPageInfoRequest,
            opts: Dict = None,
    ) -> models.DeleteDomainErrorPageInfoResponse:
        """
        This API is used to delete a custom error code for a domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDomainErrorPageInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDomainErrorPageInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteListeners(
            self,
            request: models.DeleteListenersRequest,
            opts: Dict = None,
    ) -> models.DeleteListenersResponse:
        """
        This API (DeleteListeners) is used to batch delete the listeners of a connection or connection group, including layer-4/7 listeners.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProxyGroup(
            self,
            request: models.DeleteProxyGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteProxyGroupResponse:
        """
        This API (DeleteProxyGroup) is used to delete a connection group.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProxyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProxyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRule(
            self,
            request: models.DeleteRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteRuleResponse:
        """
        This API (DeleteRule) is used to delete the forwarding rules of HTTP/HTTPS listeners.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityPolicy(
            self,
            request: models.DeleteSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityPolicyResponse:
        """
        This API is used to delete a security policy.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityRules(
            self,
            request: models.DeleteSecurityRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityRulesResponse:
        """
        This API is used to delete security policy rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessRegions(
            self,
            request: models.DescribeAccessRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessRegionsResponse:
        """
        This API (DescribeAccessRegions) is used to query acceleration region (client access region).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccessRegionsByDestRegion(
            self,
            request: models.DescribeAccessRegionsByDestRegionRequest,
            opts: Dict = None,
    ) -> models.DescribeAccessRegionsByDestRegionResponse:
        """
        This API is used to query the available accelerator region based on the origin server region.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccessRegionsByDestRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccessRegionsByDestRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAuthSignature(
            self,
            request: models.DescribeAuthSignatureRequest,
            opts: Dict = None,
    ) -> models.DescribeAuthSignatureResponse:
        """
        This API is used to get a request signature that can prevent parameter tampering in the process of triggering orders, getting quotes, or activating subscription services.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAuthSignature"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAuthSignatureResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBlackHeader(
            self,
            request: models.DescribeBlackHeaderRequest,
            opts: Dict = None,
    ) -> models.DescribeBlackHeaderResponse:
        """
        This API is used to query names of blocked custom headers.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBlackHeader"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBlackHeaderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCertificateDetail(
            self,
            request: models.DescribeCertificateDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCertificateDetailResponse:
        """
        This API (DescribeCertificateDetail) is used to query certificate details, including the certificate ID, name, type, content, key, and other information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCertificateDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCertificateDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCertificates(
            self,
            request: models.DescribeCertificatesRequest,
            opts: Dict = None,
    ) -> models.DescribeCertificatesResponse:
        """
        This API (DescribeCertificates) is used to query the list of available certificates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCertificates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCertificatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCountryAreaMapping(
            self,
            request: models.DescribeCountryAreaMappingRequest,
            opts: Dict = None,
    ) -> models.DescribeCountryAreaMappingResponse:
        """
        This API (DescribeCountryAreaMapping) is used to obtain the country/region code mapping table.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCountryAreaMapping"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCountryAreaMappingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomHeader(
            self,
            request: models.DescribeCustomHeaderRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomHeaderResponse:
        """
        This API is used to query the list of custom headers.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomHeader"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomHeaderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDestRegions(
            self,
            request: models.DescribeDestRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeDestRegionsResponse:
        """
        This API (DescribeDestRegions) is used to query an origin server region (i.e., the region in which the origin server locates).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDestRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDestRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainErrorPageInfo(
            self,
            request: models.DescribeDomainErrorPageInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainErrorPageInfoResponse:
        """
        This API is used to query the custom error response to a domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainErrorPageInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainErrorPageInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDomainErrorPageInfoByIds(
            self,
            request: models.DescribeDomainErrorPageInfoByIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeDomainErrorPageInfoByIdsResponse:
        """
        This API is used to query the corresponding error response by a custom error ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDomainErrorPageInfoByIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDomainErrorPageInfoByIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupAndStatisticsProxy(
            self,
            request: models.DescribeGroupAndStatisticsProxyRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupAndStatisticsProxyResponse:
        """
        This is an internal API. It is used to query the information of connections and connection groups from which the statistics can be derived.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupAndStatisticsProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupAndStatisticsProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupDomainConfig(
            self,
            request: models.DescribeGroupDomainConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupDomainConfigResponse:
        """
        This API (DescribeGroupDomainConfig) is used to obtain the domain name resolution configuration details of a connection group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupDomainConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupDomainConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHTTPListeners(
            self,
            request: models.DescribeHTTPListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeHTTPListenersResponse:
        """
        This API (DescribeHTTPListeners) is used to query HTTP listener information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHTTPListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHTTPListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHTTPSListeners(
            self,
            request: models.DescribeHTTPSListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeHTTPSListenersResponse:
        """
        This API (DescribeHTTPSListeners) is used to query HTTPS listener information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHTTPSListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHTTPSListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListenerRealServers(
            self,
            request: models.DescribeListenerRealServersRequest,
            opts: Dict = None,
    ) -> models.DescribeListenerRealServersResponse:
        """
        This API (DescribeListenerRealServers) is used to query the origin server list of TCP/UDP listeners, including the list of bound origin servers and origin servers that can be bound.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListenerRealServers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListenerRealServersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListenerStatistics(
            self,
            request: models.DescribeListenerStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeListenerStatisticsResponse:
        """
        This API is used to query listener statistics, including inbound/outbound bandwidth, inbound/outbound packets, and concurrence data. It supports granularities of 300, 3,600, and 86,400. Default value is the highest within the granularity range.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListenerStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListenerStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxies(
            self,
            request: models.DescribeProxiesRequest,
            opts: Dict = None,
    ) -> models.DescribeProxiesResponse:
        """
        This API (DescribeProxies) is used to query the connection instance list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxiesStatus(
            self,
            request: models.DescribeProxiesStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeProxiesStatusResponse:
        """
        This API (DescribeProxiesStatus) is used to query the connection status list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxiesStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxiesStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxyAndStatisticsListeners(
            self,
            request: models.DescribeProxyAndStatisticsListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeProxyAndStatisticsListenersResponse:
        """
        This is an internal API. It is used to query the information of connections and listeners from which the statistics can be derived.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxyAndStatisticsListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxyAndStatisticsListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxyDetail(
            self,
            request: models.DescribeProxyDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeProxyDetailResponse:
        """
        This API (DescribeProxyDetail) is used to query connection details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxyGroupDetails(
            self,
            request: models.DescribeProxyGroupDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeProxyGroupDetailsResponse:
        """
        This API (DescribeProxyGroupDetails) is used to query connection group details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxyGroupDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxyGroupDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxyGroupList(
            self,
            request: models.DescribeProxyGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeProxyGroupListResponse:
        """
        This API (DescribeProxyGroupList) is used to pull the list of connection groups and the basic information of each connection group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxyGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxyGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxyGroupStatistics(
            self,
            request: models.DescribeProxyGroupStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeProxyGroupStatisticsResponse:
        """
        This API is used to query listener statistics, including inbound/outbound bandwidth, inbound/outbound packets, and concurrence data. It supports granularities of 300, 3,600, and 86,400. Default value is the highest within the granularity range.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxyGroupStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxyGroupStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxyStatistics(
            self,
            request: models.DescribeProxyStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeProxyStatisticsResponse:
        """
        This API is used to query listener statistics, including inbound/outbound bandwidth, inbound/outbound packets, concurrence, packet loss, and latency data. It supports granularities of 300, 3,600, and 86,400. Default value is the highest within the granularity range.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxyStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxyStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRealServerStatistics(
            self,
            request: models.DescribeRealServerStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeRealServerStatisticsResponse:
        """
        This API is used to query the statistics of an origin server's health check results. Origin server status is displayed as 1 (normal) or 0 (exceptional). The queried origin server must be bound to a listener or rule, and the ID of the bound listener or rule must be specified for the query. This API supports displaying origin server status statistics at a 1-minute granularity.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRealServerStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRealServerStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRealServers(
            self,
            request: models.DescribeRealServersRequest,
            opts: Dict = None,
    ) -> models.DescribeRealServersResponse:
        """
        This API is used to query origin server information. It can query all origin servers under the specified project name, and supports fuzzy query by specified IPs or domain names.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRealServers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRealServersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRealServersStatus(
            self,
            request: models.DescribeRealServersStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeRealServersStatusResponse:
        """
        This API (DescribeRealServersStatus) is used to query whether an origin server has been bound to a rule or listener.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRealServersStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRealServersStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegionAndPrice(
            self,
            request: models.DescribeRegionAndPriceRequest,
            opts: Dict = None,
    ) -> models.DescribeRegionAndPriceResponse:
        """
        This API (DescribeRegionAndPrice) is used to obtain the origin server regions and the bandwidth price gradient.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegionAndPrice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegionAndPriceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourcesByTag(
            self,
            request: models.DescribeResourcesByTagRequest,
            opts: Dict = None,
    ) -> models.DescribeResourcesByTagResponse:
        """
        This API (DescribeResourcesByTag) is used to query corresponding resource information by tags, including connection, connection group, and origin server.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourcesByTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourcesByTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleRealServers(
            self,
            request: models.DescribeRuleRealServersRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleRealServersResponse:
        """
        This API (DescribeRuleRealServers) is used to query forwarding rules-related origin server information, including information of origin servers that can be bound and have been bound.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleRealServers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleRealServersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRules(
            self,
            request: models.DescribeRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeRulesResponse:
        """
        This API (DescribeRules) is used to query all rule information of a listener, including the domain names, paths, and list of bound origin servers. For version 3.0 connections, this API returns the advanced authentication configuration information of the domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRulesByRuleIds(
            self,
            request: models.DescribeRulesByRuleIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeRulesByRuleIdsResponse:
        """
        This API is used to pull the list of rules based on rule ID. It supports pulling 1 to 10 rules at a time.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRulesByRuleIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRulesByRuleIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityPolicyDetail(
            self,
            request: models.DescribeSecurityPolicyDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityPolicyDetailResponse:
        """
        This API is used to obtain security policy details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityPolicyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityPolicyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityRules(
            self,
            request: models.DescribeSecurityRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityRulesResponse:
        """
        This API is used to query the list of security rules based on security rule ID. It supports querying 1 to 20 security rules at a time.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTCPListeners(
            self,
            request: models.DescribeTCPListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeTCPListenersResponse:
        """
        This API (DescribeTCPListeners) is used to query the TCP listener information of a single connection or connection group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTCPListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTCPListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUDPListeners(
            self,
            request: models.DescribeUDPListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeUDPListenersResponse:
        """
        This API (DescribeUDPListeners) is used to query the UDP listener information of a single connection or connection group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUDPListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUDPListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyProxies(
            self,
            request: models.DestroyProxiesRequest,
            opts: Dict = None,
    ) -> models.DestroyProxiesResponse:
        """
        This API (DestroyProxies) is used to terminate a connection. If terminated, no fees will be incurred.
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyProxies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyProxiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceCreateProxy(
            self,
            request: models.InquiryPriceCreateProxyRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceCreateProxyResponse:
        """
        This API (InquiryPriceCreateProxy) is used to create the price inquiries of acceleration connections.
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceCreateProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceCreateProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCertificate(
            self,
            request: models.ModifyCertificateRequest,
            opts: Dict = None,
    ) -> models.ModifyCertificateResponse:
        """
        This API (ModifyCertificate) is used to modify a domain name certificate of a listener. domain name certificate. This API is only applicable to connections of version 3.0.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCertificateAttributes(
            self,
            request: models.ModifyCertificateAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyCertificateAttributesResponse:
        """
        This API is used to modify certificate name and content.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCertificateAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCertificateAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDomain(
            self,
            request: models.ModifyDomainRequest,
            opts: Dict = None,
    ) -> models.ModifyDomainResponse:
        """
        This API (ModifyDomain) is used to modify domain names of listeners. For connections of version 3.0, it supports modifying certificates of the domain names.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGroupDomainConfig(
            self,
            request: models.ModifyGroupDomainConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyGroupDomainConfigResponse:
        """
        This API (ModifyGroupDomainConfig) is used to configure the nearest access domain name of a connection group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGroupDomainConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGroupDomainConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHTTPListenerAttribute(
            self,
            request: models.ModifyHTTPListenerAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyHTTPListenerAttributeResponse:
        """
        This API (ModifyHTTPListenerAttribute) is used to modify the HTTP listener configuration information of a connection. Currently only supports modifying listener name.
        Note: Grouped connections currently do not support HTTP/HTTPS listeners.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHTTPListenerAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHTTPListenerAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHTTPSListenerAttribute(
            self,
            request: models.ModifyHTTPSListenerAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyHTTPSListenerAttributeResponse:
        """
        This API (ModifyHTTPSListenerAttribute) is used to modify HTTPS listener configurations. It currently do not support connection groups and connections of version 1.0.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHTTPSListenerAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHTTPSListenerAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProxiesAttribute(
            self,
            request: models.ModifyProxiesAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyProxiesAttributeResponse:
        """
        This API (ModifyProxiesAttribute) is used to modify instance attributes (currently only supports modifying connection name).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProxiesAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProxiesAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProxiesProject(
            self,
            request: models.ModifyProxiesProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyProxiesProjectResponse:
        """
        This API (ModifyProxiesProject) is used to modify the project to which a connection belongs.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProxiesProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProxiesProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProxyConfiguration(
            self,
            request: models.ModifyProxyConfigurationRequest,
            opts: Dict = None,
    ) -> models.ModifyProxyConfigurationResponse:
        """
        This API (ModifyProxyConfiguration) is used to modify connection configurations. You can expand or reduce the capacity based on current business requirements. It only supports connections with a Scalarable of 1. Scalarable can be obtained via DescribeProxies API.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProxyConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProxyConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProxyGroupAttribute(
            self,
            request: models.ModifyProxyGroupAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyProxyGroupAttributeResponse:
        """
        This API (ModifyProxyGroupAttribute) is used to modify connection group attributes. It currently only supports modifying connection group name.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProxyGroupAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProxyGroupAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRealServerName(
            self,
            request: models.ModifyRealServerNameRequest,
            opts: Dict = None,
    ) -> models.ModifyRealServerNameResponse:
        """
        This API (ModifyRealServerName) is used to modify origin server names.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRealServerName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRealServerNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRuleAttribute(
            self,
            request: models.ModifyRuleAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyRuleAttributeResponse:
        """
        This API (ModifyRuleAttribute) is used to modify forwarding rule information, including health check configuration and forwarding policies.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRuleAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRuleAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityRule(
            self,
            request: models.ModifySecurityRuleRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityRuleResponse:
        """
        This API is used to modify security policy rule names.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTCPListenerAttribute(
            self,
            request: models.ModifyTCPListenerAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyTCPListenerAttributeResponse:
        """
        This API (ModifyTCPListenerAttribute) is used to modify the TCP listener configuration of a connection instance, including health check configuration and scheduling policies.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTCPListenerAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTCPListenerAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUDPListenerAttribute(
            self,
            request: models.ModifyUDPListenerAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyUDPListenerAttributeResponse:
        """
        This API (ModifyUDPListenerAttribute) is used to modify the UDP listener configuration of a connection instance, including modification of listener names and scheduling policies.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUDPListenerAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUDPListenerAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenProxies(
            self,
            request: models.OpenProxiesRequest,
            opts: Dict = None,
    ) -> models.OpenProxiesResponse:
        """
        This API (OpenProxies) is used to enable one or more connections.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenProxies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenProxiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenProxyGroup(
            self,
            request: models.OpenProxyGroupRequest,
            opts: Dict = None,
    ) -> models.OpenProxyGroupResponse:
        """
        This API is used to enable all connections in a connection group.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenProxyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenProxyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenSecurityPolicy(
            self,
            request: models.OpenSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.OpenSecurityPolicyResponse:
        """
        This API is used to enable a security policy.
        """
        
        kwargs = {}
        kwargs["action"] = "OpenSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveRealServers(
            self,
            request: models.RemoveRealServersRequest,
            opts: Dict = None,
    ) -> models.RemoveRealServersResponse:
        """
        This API is used to delete the added origin server (server) IP or domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveRealServers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveRealServersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetAuthentication(
            self,
            request: models.SetAuthenticationRequest,
            opts: Dict = None,
    ) -> models.SetAuthenticationResponse:
        """
        This API (SetAuthentication) is used for the advanced authentication configuration of connections, including authentication methods and their certificates. If only supports connections of version 3.0.
        """
        
        kwargs = {}
        kwargs["action"] = "SetAuthentication"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetAuthenticationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)