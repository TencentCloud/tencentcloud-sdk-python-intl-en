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
from tencentcloud.teo.v20220901 import models
from typing import Dict


class TeoClient(AbstractClient):
    _apiVersion = '2022-09-01'
    _endpoint = 'teo.intl.tencentcloudapi.com'
    _service = 'teo'

    async def ApplyFreeCertificate(
            self,
            request: models.ApplyFreeCertificateRequest,
            opts: Dict = None,
    ) -> models.ApplyFreeCertificateResponse:
        """
        This API is used to apply for a free certificate. If you need to proceed with DNS delegated verification or file verification, you can call this API to initiate the certificate application and obtain the corresponding verification content based on the application method. The order for API calls is as follows:.
        Step 1: Call ApplyFreeCertificate, specify the verification method for free certificate application, and obtain the verification content.
        Step 2: Configure the corresponding domain as verification content.
        Step 3: Call CheckFreeCertificateVerification to verify. After verification passes, the free certificate application is completed.
        Step 4: Call ModifyHostsCertificate to issue a domain certificate configured to use the EdgeOne free certificate.

        The application method introduction in the document: [Free Certificate Application Description](https://www.tencentcloud.comom/document/product/1552/90437?from_cn_redirect=1).
        description:.
        - Only CNAME access mode can call this API to specify the free certificate application method. NS/DNSPod hosting access modes use automatic validation to apply for free certificates with no need to call this API.
        - If you need to switch the free certificate authentication method, you can call this API again by changing the VerificationMethod field to update it.
        - A domain name can only apply for one free certificate. After calling this API, the backend will trigger the free certificate application task. You need to complete the domain name verification info configuration within 2 days, then finish certificate authentication.
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyFreeCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyFreeCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindSecurityTemplateToEntity(
            self,
            request: models.BindSecurityTemplateToEntityRequest,
            opts: Dict = None,
    ) -> models.BindSecurityTemplateToEntityResponse:
        """
        This API is used to bind/unbind a domain name to/from a specific policy template.
        """
        
        kwargs = {}
        kwargs["action"] = "BindSecurityTemplateToEntity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindSecurityTemplateToEntityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindSharedCNAME(
            self,
            request: models.BindSharedCNAMERequest,
            opts: Dict = None,
    ) -> models.BindSharedCNAMEResponse:
        """
        This API is used to bind/unbind a domain name to/from a shared CNAME. It is now only available to beta users.
        """
        
        kwargs = {}
        kwargs["action"] = "BindSharedCNAME"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindSharedCNAMEResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindZoneToPlan(
            self,
            request: models.BindZoneToPlanRequest,
            opts: Dict = None,
    ) -> models.BindZoneToPlanResponse:
        """
        This API is used to bind a site to a plan.
        """
        
        kwargs = {}
        kwargs["action"] = "BindZoneToPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindZoneToPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckCnameStatus(
            self,
            request: models.CheckCnameStatusRequest,
            opts: Dict = None,
    ) -> models.CheckCnameStatusResponse:
        """
        This API is used to query the CNAME status of a domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckCnameStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckCnameStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckFreeCertificateVerification(
            self,
            request: models.CheckFreeCertificateVerificationRequest,
            opts: Dict = None,
    ) -> models.CheckFreeCertificateVerificationResponse:
        """
        This API is used to verify a free certificate and obtain the application result. If verified, you can query the free certificate information for the corresponding domain name application through this API. If failed to apply, this API will return the corresponding verification failure message.
        This API is used to check the free certificate application result after triggering the [ApplyFreeCertificate](https://www.tencentcloud.comom/document/product/1552/124807?from_cn_redirect=1) . Once the application is successful, you need to configure through the [ModifyHostsCertificate](https://www.tencentcloud.comom/document/product/1552/80764?from_cn_redirect=1) to deploy the free certificate to the acceleration domain.
        """
        
        kwargs = {}
        kwargs["action"] = "CheckFreeCertificateVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckFreeCertificateVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ConfirmMultiPathGatewayOriginACL(
            self,
            request: models.ConfirmMultiPathGatewayOriginACLRequest,
            opts: Dict = None,
    ) -> models.ConfirmMultiPathGatewayOriginACLResponse:
        """
        This API is used to confirm the latest origin IP range is updated to the origin server firewall when the multi-channel security acceleration gateway's origin IP range changes.
        """
        
        kwargs = {}
        kwargs["action"] = "ConfirmMultiPathGatewayOriginACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConfirmMultiPathGatewayOriginACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ConfirmOriginACLUpdate(
            self,
            request: models.ConfirmOriginACLUpdateRequest,
            opts: Dict = None,
    ) -> models.ConfirmOriginACLUpdateResponse:
        """
        This API is used to confirm that the latest origin ACLs have been updated to the origin server firewall when the origin ACLs change. After confirming the update to the latest version, related change notifications will stop pushing.
        """
        
        kwargs = {}
        kwargs["action"] = "ConfirmOriginACLUpdate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConfirmOriginACLUpdateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccelerationDomain(
            self,
            request: models.CreateAccelerationDomainRequest,
            opts: Dict = None,
    ) -> models.CreateAccelerationDomainResponse:
        """
        This API is used to create an acceleration domain name.

        For sites connected via the CNAME, if you have not verified the ownership of the domain name, the ownership verification information of the domain name is returned. To verify your ownership of the domain name, see [Ownership Verification](https://intl.cloud.tencent.com/document/product/1552/70789?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccelerationDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccelerationDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAliasDomain(
            self,
            request: models.CreateAliasDomainRequest,
            opts: Dict = None,
    ) -> models.CreateAliasDomainResponse:
        """
        This API is used to create an alias domain name.
        The feature is only supported by the enterprise plan and is currently in closed beta testing. If you need to use it, please [contact us](https://www.tencentcloud.com/contact-us).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAliasDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAliasDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplicationProxy(
            self,
            request: models.CreateApplicationProxyRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationProxyResponse:
        """
        This API is on an earlier version. If you want to call it, please switch to the latest version [CreateL4Proxy] (https://intl.cloud.tencent.com/document/product/1552/103417?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplicationProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateApplicationProxyRule(
            self,
            request: models.CreateApplicationProxyRuleRequest,
            opts: Dict = None,
    ) -> models.CreateApplicationProxyRuleResponse:
        """
        This API is on an earlier version. If you want to call it, please switch to the latest version. For details, see [CreateL4ProxyRules] (https://intl.cloud.tencent.com/document/product/1552/103416?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateApplicationProxyRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateApplicationProxyRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCLSIndex(
            self,
            request: models.CreateCLSIndexRequest,
            opts: Dict = None,
    ) -> models.CreateCLSIndexResponse:
        """
        This API is used to create key-value indexes for relevant delivered log fields in the corresponding Tencent Cloud CLS log topic for a specified real-time log delivery task (task-id). If such indexes have been created in CLS, this API will append indexes through merging.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCLSIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCLSIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConfigGroupVersion(
            self,
            request: models.CreateConfigGroupVersionRequest,
            opts: Dict = None,
    ) -> models.CreateConfigGroupVersionResponse:
        """
        This API is used to create a new version for the specified configuration group in version management mode. The version management feature is currently undergoing beta testing and is accessible only to users on the whitelist.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConfigGroupVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConfigGroupVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateContentIdentifier(
            self,
            request: models.CreateContentIdentifierRequest,
            opts: Dict = None,
    ) -> models.CreateContentIdentifierResponse:
        """
        This API is used to create content identifiers, where you can set descriptions, tags, and other information. It is also necessary to bind an enterprise edition package for billing data statistics. A content identifier can only bind one billing package, while a billing package can bind multiple content identifiers. This feature is only available to the allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateContentIdentifier"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateContentIdentifierResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCustomizeErrorPage(
            self,
            request: models.CreateCustomizeErrorPageRequest,
            opts: Dict = None,
    ) -> models.CreateCustomizeErrorPageResponse:
        """
        This API is used to create a custom response page.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCustomizeErrorPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCustomizeErrorPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDnsRecord(
            self,
            request: models.CreateDnsRecordRequest,
            opts: Dict = None,
    ) -> models.CreateDnsRecordResponse:
        """
        After creating a site and the site is accessed in NS mode, you can create DNS records through this API.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDnsRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDnsRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFunction(
            self,
            request: models.CreateFunctionRequest,
            opts: Dict = None,
    ) -> models.CreateFunctionResponse:
        """
        This API is used to create and deploy an edge function to EdgeOne edge nodes.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFunctionRule(
            self,
            request: models.CreateFunctionRuleRequest,
            opts: Dict = None,
    ) -> models.CreateFunctionRuleResponse:
        """
        This API is used to create a trigger rule for an edge function.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFunctionRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFunctionRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateJustInTimeTranscodeTemplate(
            self,
            request: models.CreateJustInTimeTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateJustInTimeTranscodeTemplateResponse:
        """
        JIT transcoding already provides preset transcoding templates to meet most needs. If there are personalized transcoding requirements, you can create custom transcoding templates through this API, with up to 100 custom transcoding templates allowed.
        This API is used to ensure the consistency of JIT transcoding effect, avoid video output exceptions caused by EO cache or M3U8 sharding template changes during the process, and templates cannot be modified after creation.
        This API is used to learn about the detailed capacity of JIT transcoding. EdgeOne video instant processing function introduction (https://www.tencentcloud.comom/document/product/1552/111927?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateJustInTimeTranscodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateJustInTimeTranscodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL4Proxy(
            self,
            request: models.CreateL4ProxyRequest,
            opts: Dict = None,
    ) -> models.CreateL4ProxyResponse:
        """
        This API is used to create Layer 4 proxy instances.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL4Proxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL4ProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL4ProxyRules(
            self,
            request: models.CreateL4ProxyRulesRequest,
            opts: Dict = None,
    ) -> models.CreateL4ProxyRulesResponse:
        """
        This API is used to create Layer 4 proxy instance rules, supporting both individual and batch creation.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL4ProxyRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL4ProxyRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL7AccRules(
            self,
            request: models.CreateL7AccRulesRequest,
            opts: Dict = None,
    ) -> models.CreateL7AccRulesResponse:
        """
        This API is used to create rules in the [rule engine](https://intl.cloud.tencent.com/document/product/1552/70901?from_cn_redirect=1). Batch creation is supported.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL7AccRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL7AccRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLoadBalancer(
            self,
            request: models.CreateLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.CreateLoadBalancerResponse:
        """
        This API is used to create a LoadBalancer. For details, see [Quickly Create Load Balancers](https://intl.cloud.tencent.com/document/product/1552/104223?from_cn_redirect=1). The load balancing feature is in beta test. If you need to use it, [contact us](https://www.tencentcloud.com/contact-us).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMultiPathGateway(
            self,
            request: models.CreateMultiPathGatewayRequest,
            opts: Dict = None,
    ) -> models.CreateMultiPathGatewayResponse:
        """
        Create a multi-channel security acceleration gateway via this API, including Cloud Gateway (gateway created and managed by Tencent Cloud) and private gateway (gateway deployed by users). Query the status using DescribeMultiPathGateway, and creation is successful if the status is online.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMultiPathGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMultiPathGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMultiPathGatewayLine(
            self,
            request: models.CreateMultiPathGatewayLineRequest,
            opts: Dict = None,
    ) -> models.CreateMultiPathGatewayLineResponse:
        """
        This API is used to create lines integrated with the multi-channel security acceleration gateway, including EdgeOne Layer-4 proxy and custom lines.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMultiPathGatewayLine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMultiPathGatewayLineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMultiPathGatewaySecretKey(
            self,
            request: models.CreateMultiPathGatewaySecretKeyRequest,
            opts: Dict = None,
    ) -> models.CreateMultiPathGatewaySecretKeyResponse:
        """
        This API creates an access key for the multi-channel security acceleration gateway. Customers use the access key to sign requests for accessing the gateway. Each site can have only one key, which is applicable to all gateways under that site. Query the key via the DescribeMultiPathGatewaySecretKey API.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMultiPathGatewaySecretKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMultiPathGatewaySecretKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOriginGroup(
            self,
            request: models.CreateOriginGroupRequest,
            opts: Dict = None,
    ) -> models.CreateOriginGroupResponse:
        """
        This API is used to create an origin group for easy management. The created origin server group can be used for **adding acceleration domain names** and **layer-4 proxy configuration**.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOriginGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOriginGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePlan(
            self,
            request: models.CreatePlanRequest,
            opts: Dict = None,
    ) -> models.CreatePlanResponse:
        """
        If you need to use the EdgeOne product, you must create a billing plan through this interface.
        > After creating a plan, you need to complete the process of creating a site and binding the plan through [CreateZone](https://intl.cloud.tencent.com/document/product/1552/80719?from_cn_redirect=1), so that the EdgeOne can provide services properly.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePlanForZone(
            self,
            request: models.CreatePlanForZoneRequest,
            opts: Dict = None,
    ) -> models.CreatePlanForZoneResponse:
        """
        This API is used to purchase a plan for a new site.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePlanForZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePlanForZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrefetchTask(
            self,
            request: models.CreatePrefetchTaskRequest,
            opts: Dict = None,
    ) -> models.CreatePrefetchTaskResponse:
        """
        This API is used to create a pre-warming task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrefetchTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrefetchTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePurgeTask(
            self,
            request: models.CreatePurgeTaskRequest,
            opts: Dict = None,
    ) -> models.CreatePurgeTaskResponse:
        """
        When there are resources updated on the origin with the TTL remaining valid, users cannot access the latest resources. In this case, you can purge the cache using this API. There are two methods: <li>Delete: This method deletes the node cache without verification and retrieves the latest resources from the origin when receiving a request.</li><li>Invalidate: This method marks the node cache as invalid and sends a request with the If-None-Match and If-Modified-Since headers to the origin. If the origin responses with 200, the latest resources are retrieved to be cached on the node. If a 304 response is returned, the latest resources are not cached on the node.

        </li>For more details, see [Cache Purge](https://intl.cloud.tencent.com/document/product/1552/70759?from_cn_redirect=1). </li>
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePurgeTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePurgeTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRealtimeLogDeliveryTask(
            self,
            request: models.CreateRealtimeLogDeliveryTaskRequest,
            opts: Dict = None,
    ) -> models.CreateRealtimeLogDeliveryTaskResponse:
        """
        This API is used to create a real-time log delivery task.
        The following restrictions apply:

        - When the log type (`LogType`) is site acceleration log (L7 access log) (`domain`), L4 proxy log (`application`), or Edge Function execution log (`function`), the same entity (L7 domain, L4 proxy instance, or Edge Function instance) can be added to only one of the following `TaskType` combinations within the same `LogType`-`Area` pair:
            - One task delivering to Tencent Cloud CLS plus one task delivering to a custom HTTP(S) endpoint;
            - One task delivering to Tencent Cloud CLS plus one task delivering to an AWS S3-compatible bucket.
        - When the log type (`LogType`) is rate-limiting & CC attack protection log (`web-rateLiming`), managed rule log (`web-attack`), custom rule log (`web-rule`), or bot management log (`web-bot`), the same entity can be added to only one real-time log delivery task within the same `LogType`-`Area` pair.

        Before creating a task, we recommend that you first call [DescribeRealtimeLogDeliveryTasks](https://intl.cloud.tencent.com/document/product/1552/104110?from_cn_redirect=1) to list existing tasks for the entity and verify whether it has already been added to another task.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRealtimeLogDeliveryTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRealtimeLogDeliveryTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRule(
            self,
            request: models.CreateRuleRequest,
            opts: Dict = None,
    ) -> models.CreateRuleResponse:
        """
        This interface is the old version of the rule engine creation interface. EdgeOne has fully upgraded the rule engine related interfaces on January 21, 2025. For details on the new version of the seven-layer acceleration rule creation interface, please refer to [CreateL7AccRules](https://intl.cloud.tencent.com/document/product/1552/115822?from_cn_redirect=1).<p style="color: red;">Note: Starting from January 21, 2025, the old version of the interface will stop updating and iteration. Subsequent new features will only be provided in the new version of the interface, and the original capabilities supported by the old version of the interface will not be affected. To avoid data field conflicts when using the old version of the interface, it is recommended that you migrate to the new version of the rule engine interface as soon as possible. </p>
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityAPIResource(
            self,
            request: models.CreateSecurityAPIResourceRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityAPIResourceResponse:
        """
        This API is used to create an API resource.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityAPIResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityAPIResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityAPIService(
            self,
            request: models.CreateSecurityAPIServiceRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityAPIServiceResponse:
        """
        This API is used to create an API service.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityAPIService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityAPIServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityClientAttester(
            self,
            request: models.CreateSecurityClientAttesterRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityClientAttesterResponse:
        """
        This API is used to create client authentication options.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityClientAttester"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityClientAttesterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityIPGroup(
            self,
            request: models.CreateSecurityIPGroupRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityIPGroupResponse:
        """
        This API is used to create a security IP group.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityIPGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityIPGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityJSInjectionRule(
            self,
            request: models.CreateSecurityJSInjectionRuleRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityJSInjectionRuleResponse:
        """
        This API is used to create a JavaScript injection rule.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityJSInjectionRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityJSInjectionRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSharedCNAME(
            self,
            request: models.CreateSharedCNAMERequest,
            opts: Dict = None,
    ) -> models.CreateSharedCNAMEResponse:
        """
        This API is used to create a shared CNAME. It is now only available to beta users.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSharedCNAME"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSharedCNAMEResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWebSecurityTemplate(
            self,
            request: models.CreateWebSecurityTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateWebSecurityTemplateResponse:
        """
        This API is used to create a security policy configuration template.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWebSecurityTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWebSecurityTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateZone(
            self,
            request: models.CreateZoneRequest,
            opts: Dict = None,
    ) -> models.CreateZoneResponse:
        """
        This API is used to create a site. After you create the site, you can connect it to EdgeOne via the CNAME or NS (see [Quick Start](https://intl.cloud.tencent.com/document/product/1552/87601?from_cn_redirect=1)), or connect it without a domain name (see [Quick Access to L4 Proxy Service](https://intl.cloud.tencent.com/document/product/1552/96051?from_cn_redirect=1)).

        If there are already EdgeOne plans under the current account, it is recommended to pass in the `PlanId` to bind the site with the plan directly. If `PlanId` is not passed in, the created site is not activated. You need to call [BindZoneToPlan](https://intl.cloud.tencent.com/document/product/1552/83042?from_cn_redirect=1) to bind the site with a plan. To purchase a plan, please go to the EdgeOne console.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccelerationDomains(
            self,
            request: models.DeleteAccelerationDomainsRequest,
            opts: Dict = None,
    ) -> models.DeleteAccelerationDomainsResponse:
        """
        This API is used to batch remove accelerated domain names.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccelerationDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccelerationDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAliasDomain(
            self,
            request: models.DeleteAliasDomainRequest,
            opts: Dict = None,
    ) -> models.DeleteAliasDomainResponse:
        """
        This API is used to delete an alias domain name.
        The feature is only supported by the enterprise plan and is currently in closed beta testing. If you need to use it, [Contact Us](https://www.tencentcloud.com/contact-us).
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAliasDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAliasDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApplicationProxy(
            self,
            request: models.DeleteApplicationProxyRequest,
            opts: Dict = None,
    ) -> models.DeleteApplicationProxyResponse:
        """
        This API is on an earlier version. If you want to call it, please switch to the latest version. For details, see [DeleteL4Proxy] (https://intl.cloud.tencent.com/document/product/1552/103415?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApplicationProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApplicationProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteApplicationProxyRule(
            self,
            request: models.DeleteApplicationProxyRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteApplicationProxyRuleResponse:
        """
        This API is on an earlier version. If you want to call it, please switch to the latest version. For details, see [DeleteL4ProxyRules] (https://intl.cloud.tencent.com/document/product/1552/103414?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteApplicationProxyRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteApplicationProxyRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteContentIdentifier(
            self,
            request: models.DeleteContentIdentifierRequest,
            opts: Dict = None,
    ) -> models.DeleteContentIdentifierResponse:
        """
        Delete the specified content identifier. This feature is only available to the allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteContentIdentifier"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteContentIdentifierResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCustomErrorPage(
            self,
            request: models.DeleteCustomErrorPageRequest,
            opts: Dict = None,
    ) -> models.DeleteCustomErrorPageResponse:
        """
        This API is used to delete a custom response page.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCustomErrorPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCustomErrorPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDnsRecords(
            self,
            request: models.DeleteDnsRecordsRequest,
            opts: Dict = None,
    ) -> models.DeleteDnsRecordsResponse:
        """
        You can use this API to batch delete DNS records.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDnsRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDnsRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFunction(
            self,
            request: models.DeleteFunctionRequest,
            opts: Dict = None,
    ) -> models.DeleteFunctionResponse:
        """
        This API is used to delete an edge function. Once deleted, the function cannot be recovered, and associated trigger rules are also deleted.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFunctionRules(
            self,
            request: models.DeleteFunctionRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteFunctionRulesResponse:
        """
        This API is used to delete a trigger rule for an edge function.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFunctionRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFunctionRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteJustInTimeTranscodeTemplates(
            self,
            request: models.DeleteJustInTimeTranscodeTemplatesRequest,
            opts: Dict = None,
    ) -> models.DeleteJustInTimeTranscodeTemplatesResponse:
        """
        This API is used to delete the appropriate just in time transcoding template based on the unique template identifier under the site ID.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteJustInTimeTranscodeTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteJustInTimeTranscodeTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteL4Proxy(
            self,
            request: models.DeleteL4ProxyRequest,
            opts: Dict = None,
    ) -> models.DeleteL4ProxyResponse:
        """
        This API is used to delete a Layer 4 proxy instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteL4Proxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteL4ProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteL4ProxyRules(
            self,
            request: models.DeleteL4ProxyRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteL4ProxyRulesResponse:
        """
        This API is used to delete Layer 4 proxy forwarding rules, supporting both individual and batch operation.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteL4ProxyRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteL4ProxyRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteL7AccRules(
            self,
            request: models.DeleteL7AccRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteL7AccRulesResponse:
        """
        This API is used to delete rules of the [rule engine](https://intl.cloud.tencent.com/document/product/1552/70901?from_cn_redirect=1), supporting batch deletion.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteL7AccRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteL7AccRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLoadBalancer(
            self,
            request: models.DeleteLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.DeleteLoadBalancerResponse:
        """
        This API is used to delete a LoadBalancer. If the LoadBalancer is referenced by other services (for example, Layer-4 proxy), the LoadBalancer cannot be deleted until the reference relationship is removed. The load balancing feature is in beta test. If you need to use it, [contact us](https://www.tencentcloud.com/contact-us).
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMultiPathGateway(
            self,
            request: models.DeleteMultiPathGatewayRequest,
            opts: Dict = None,
    ) -> models.DeleteMultiPathGatewayResponse:
        """
        This API is used to delete a multi-channel security acceleration gateway, including private gateways and Cloud Gateways.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMultiPathGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMultiPathGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMultiPathGatewayLine(
            self,
            request: models.DeleteMultiPathGatewayLineRequest,
            opts: Dict = None,
    ) -> models.DeleteMultiPathGatewayLineResponse:
        """
        This API is used to delete lines integrated with the multi-channel security acceleration gateway. Only custom lines support deletion.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMultiPathGatewayLine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMultiPathGatewayLineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOriginGroup(
            self,
            request: models.DeleteOriginGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteOriginGroupResponse:
        """
        This API is used to delete an origin group. Note that an origin group can not be deleted if it is referenced by services (e.g. L4 Proxy, domain name service, load balancing, rule engines).
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOriginGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOriginGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRealtimeLogDeliveryTask(
            self,
            request: models.DeleteRealtimeLogDeliveryTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteRealtimeLogDeliveryTaskResponse:
        """
        This API is used to delete a real-time log delivery task.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRealtimeLogDeliveryTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRealtimeLogDeliveryTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRules(
            self,
            request: models.DeleteRulesRequest,
            opts: Dict = None,
    ) -> models.DeleteRulesResponse:
        """
        This interface is the old version of the rule engine deletion interface. EdgeOne has fully upgraded the rule engine related interfaces on January 21, 2025. For details on the new version of the seven-layer acceleration rule deletion interface, please refer to [DeleteL7AccRules](https://intl.cloud.tencent.com/document/product/1552/115821?from_cn_redirect=1).<0>Note: Starting from January 21, 2025, the earlier version API will no longer be updated. Subsequent new features will only be provided in the latest version interface. The original capabilities supported by the earlier version API will not be affected. To avoid field conflicts when using the earlier version API, it is recommended that you migrate to the new version rule engine API as soon as possible.</0>.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityAPIResource(
            self,
            request: models.DeleteSecurityAPIResourceRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityAPIResourceResponse:
        """
        This API is used to delete API resources.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityAPIResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityAPIResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityAPIService(
            self,
            request: models.DeleteSecurityAPIServiceRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityAPIServiceResponse:
        """
        This API is used to delete the API service.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityAPIService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityAPIServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityClientAttester(
            self,
            request: models.DeleteSecurityClientAttesterRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityClientAttesterResponse:
        """
        This API is used to delete client authentication options.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityClientAttester"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityClientAttesterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityIPGroup(
            self,
            request: models.DeleteSecurityIPGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityIPGroupResponse:
        """
        This API is used to delete a specified security IP group. Note that the security IP group cannot be deleted if it is referenced in a rule.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityIPGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityIPGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityJSInjectionRule(
            self,
            request: models.DeleteSecurityJSInjectionRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityJSInjectionRuleResponse:
        """
        This API is used to delete JavaScript injection rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityJSInjectionRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityJSInjectionRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSharedCNAME(
            self,
            request: models.DeleteSharedCNAMERequest,
            opts: Dict = None,
    ) -> models.DeleteSharedCNAMEResponse:
        """
        This API is used to delete a shared CNAME. It is now only available to beta users.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSharedCNAME"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSharedCNAMEResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWebSecurityTemplate(
            self,
            request: models.DeleteWebSecurityTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteWebSecurityTemplateResponse:
        """
        This API is used to delete a security policy configuration template.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWebSecurityTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWebSecurityTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteZone(
            self,
            request: models.DeleteZoneRequest,
            opts: Dict = None,
    ) -> models.DeleteZoneResponse:
        """
        This API is used to delete a site.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeployConfigGroupVersion(
            self,
            request: models.DeployConfigGroupVersionRequest,
            opts: Dict = None,
    ) -> models.DeployConfigGroupVersionResponse:
        """
        This API is used to release versions in version management mode. Users can deploy the version to either the testing environment or the production environment by specifying the EnvId parameter. The version management feature is currently undergoing beta testing and is accessible only to users on the whitelist.
        """
        
        kwargs = {}
        kwargs["action"] = "DeployConfigGroupVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeployConfigGroupVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccelerationDomains(
            self,
            request: models.DescribeAccelerationDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccelerationDomainsResponse:
        """
        This API is used to query domain name information of a site, including the acceleration domain name, origin, and domain name status. You can query the information of all domain names, or specific domain names by specifying filters information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccelerationDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccelerationDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAliasDomains(
            self,
            request: models.DescribeAliasDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeAliasDomainsResponse:
        """
        This API is used to query the alias domain name information list.
        The feature is only supported in the enterprise plan and is currently in closed beta testing. If you need to use it, [Contact Us](https://www.tencentcloud.com/contact-us).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAliasDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAliasDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplicationProxies(
            self,
            request: models.DescribeApplicationProxiesRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationProxiesResponse:
        """
        This API is on an earlier version. If you want to call it, please switch to the latest version. In the latest version, this API has been split into two APIs: one for querying the Layer 4 proxy instance list and the other for querying Layer 4 forwarding rules. For details, see [DescribeL4Proxy] (https://intl.cloud.tencent.com/document/product/1552/103413?from_cn_redirect=1) and [DescribeL4ProxyRules] (https://intl.cloud.tencent.com/document/product/1552/103412?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationProxies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationProxiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAvailablePlans(
            self,
            request: models.DescribeAvailablePlansRequest,
            opts: Dict = None,
    ) -> models.DescribeAvailablePlansResponse:
        """
        This API is used to query plan options available for purchase.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAvailablePlans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAvailablePlansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillingData(
            self,
            request: models.DescribeBillingDataRequest,
            opts: Dict = None,
    ) -> models.DescribeBillingDataResponse:
        """
        This API is used to query billing data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillingData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillingDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigGroupVersionDetail(
            self,
            request: models.DescribeConfigGroupVersionDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigGroupVersionDetailResponse:
        """
        This API is used to obtain detailed information about a version in version management mode. The response includes the version ID, description, status, creation time, configuration group information, and the content of the version configuration file. The version management feature is currently undergoing beta testing and is accessible only to users on the whitelist.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigGroupVersionDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigGroupVersionDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfigGroupVersions(
            self,
            request: models.DescribeConfigGroupVersionsRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigGroupVersionsResponse:
        """
        This API is used to query the version list for the specified configuration group in version management mode. The version management feature is currently undergoing beta testing and is accessible only to users on the whitelist.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfigGroupVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigGroupVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeContentIdentifiers(
            self,
            request: models.DescribeContentIdentifiersRequest,
            opts: Dict = None,
    ) -> models.DescribeContentIdentifiersResponse:
        """
        Batch query content identifiers, which can be filtered by ID, description, status, or Tag. Deleted content identifiers queried by status are retained for only three months. This feature is only open to the allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeContentIdentifiers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeContentIdentifiersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeContentQuota(
            self,
            request: models.DescribeContentQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeContentQuotaResponse:
        """
        This API is used to query content management quotas.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeContentQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeContentQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomErrorPages(
            self,
            request: models.DescribeCustomErrorPagesRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomErrorPagesResponse:
        """
        This API is used to query the custom response page list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomErrorPages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomErrorPagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSAttackData(
            self,
            request: models.DescribeDDoSAttackDataRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSAttackDataResponse:
        """
        This API is used to query the time-series data of DDoS attacks.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSAttackData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSAttackDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSAttackEvent(
            self,
            request: models.DescribeDDoSAttackEventRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSAttackEventResponse:
        """
        This API is used to query DDoS attack events.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSAttackEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSAttackEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSAttackTopData(
            self,
            request: models.DescribeDDoSAttackTopDataRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSAttackTopDataResponse:
        """
        This API is used to query the top-ranked DDoS attack data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSAttackTopData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSAttackTopDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSProtection(
            self,
            request: models.DescribeDDoSProtectionRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSProtectionResponse:
        """
        This API is used to search for site exclusive Anti-DDoS information.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDefaultCertificates(
            self,
            request: models.DescribeDefaultCertificatesRequest,
            opts: Dict = None,
    ) -> models.DescribeDefaultCertificatesResponse:
        """
        This API is used to query a list of default certificates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDefaultCertificates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDefaultCertificatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeployHistory(
            self,
            request: models.DescribeDeployHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeDeployHistoryResponse:
        """
        This API is used to query the release history of versions in the production or test environment in version management mode. The version management feature is currently undergoing beta testing and is accessible only to users on the whitelist.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeployHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeployHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDnsRecords(
            self,
            request: models.DescribeDnsRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeDnsRecordsResponse:
        """
        This API is used to view DNS record information under a site, including DNS record name, record type, and record content. It supports querying specific DNS record information by specifying filter conditions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDnsRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDnsRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvironments(
            self,
            request: models.DescribeEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvironmentsResponse:
        """
        This API is used to query environment information in version management mode. The response includes the environment ID, type, and current effective version. The version management feature is currently undergoing beta testing and is accessible only to users on the whitelist.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFunctionRules(
            self,
            request: models.DescribeFunctionRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeFunctionRulesResponse:
        """
        This API is used to query the list of trigger rules for an edge function. It supports filtering by rule ID, function ID, rule description, and so on.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFunctionRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFunctionRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFunctionRuntimeEnvironment(
            self,
            request: models.DescribeFunctionRuntimeEnvironmentRequest,
            opts: Dict = None,
    ) -> models.DescribeFunctionRuntimeEnvironmentResponse:
        """
        This API is used to query the runtime environment of an edge function, including environment variables.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFunctionRuntimeEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFunctionRuntimeEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFunctions(
            self,
            request: models.DescribeFunctionsRequest,
            opts: Dict = None,
    ) -> models.DescribeFunctionsResponse:
        """
        This API is used to query the list of edge functions. It supports filtering by function ID, name, description, and so on.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFunctions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFunctionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostsSetting(
            self,
            request: models.DescribeHostsSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeHostsSettingResponse:
        """
        This API is an old version. EdgeOne has fully upgraded the APIs related to the rule engine. You can obtain detailed configurations of domain names through [DescribeL7AccSetting](https://intl.cloud.tencent.com/document/product/1552/115819?from_cn_redirect=1) and [DescribeL7AccRules](https://intl.cloud.tencent.com/document/product/1552/115820?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostsSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostsSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIPRegion(
            self,
            request: models.DescribeIPRegionRequest,
            opts: Dict = None,
    ) -> models.DescribeIPRegionResponse:
        """
        This API is used to check if the IP is an EdgeOne IP.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIPRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIPRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIdentifications(
            self,
            request: models.DescribeIdentificationsRequest,
            opts: Dict = None,
    ) -> models.DescribeIdentificationsResponse:
        """
        This API is used to query the verification information of a site.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIdentifications"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIdentificationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJustInTimeTranscodeTemplates(
            self,
            request: models.DescribeJustInTimeTranscodeTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeJustInTimeTranscodeTemplatesResponse:
        """
        This API is used to search the transcoding template detail list according to the name, template type, or unique identifier of the just-in-time transcoding template. The returned results include all eligible custom templates and preset templates.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJustInTimeTranscodeTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJustInTimeTranscodeTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL4Proxy(
            self,
            request: models.DescribeL4ProxyRequest,
            opts: Dict = None,
    ) -> models.DescribeL4ProxyResponse:
        """
        This API is used to query a Layer 4 proxy instance list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL4Proxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL4ProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL4ProxyRules(
            self,
            request: models.DescribeL4ProxyRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeL4ProxyRulesResponse:
        """
        This API is used to query the forwarding rule list under a Layer 4 proxy instance.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL4ProxyRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL4ProxyRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL7AccRules(
            self,
            request: models.DescribeL7AccRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeL7AccRulesResponse:
        """
        This API is used to query the rule list of the rule engine (https://intl.cloud.tencent.com/document/product/1552/70901?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL7AccRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL7AccRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL7AccSetting(
            self,
            request: models.DescribeL7AccSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeL7AccSettingResponse:
        """
        This API is used to query the global configuration of [Site Acceleration](https://intl.cloud.tencent.com/document/product/1552/96193?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL7AccSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL7AccSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoadBalancerList(
            self,
            request: models.DescribeLoadBalancerListRequest,
            opts: Dict = None,
    ) -> models.DescribeLoadBalancerListResponse:
        """
        This API is used to query the LoadBalancer list. The load balancing feature is in beta test. If you need to use it, [contact us](https://www.tencentcloud.com/contact-us).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoadBalancerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoadBalancerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMultiPathGateway(
            self,
            request: models.DescribeMultiPathGatewayRequest,
            opts: Dict = None,
    ) -> models.DescribeMultiPathGatewayResponse:
        """
        This API is used to query multi-channel security acceleration gateway details such as name, Gateway ID, IP, port and type.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMultiPathGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMultiPathGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMultiPathGatewayLine(
            self,
            request: models.DescribeMultiPathGatewayLineRequest,
            opts: Dict = None,
    ) -> models.DescribeMultiPathGatewayLineResponse:
        """
        Use this API to query the lines integrated with the multi-channel security acceleration gateway, including direct connection lines, EdgeOne Layer-4 proxy lines, and custom lines.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMultiPathGatewayLine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMultiPathGatewayLineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMultiPathGatewayOriginACL(
            self,
            request: models.DescribeMultiPathGatewayOriginACLRequest,
            opts: Dict = None,
    ) -> models.DescribeMultiPathGatewayOriginACLResponse:
        """
        This API is used to query the binding relationship between a multi-channel security acceleration gateway instance and the origin server IP range, as well as the IP range details. If the MultiPathGatewayNextOriginACL field has a return value, the latest origin server IP range must be synchronized to the origin server firewall configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMultiPathGatewayOriginACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMultiPathGatewayOriginACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMultiPathGatewayRegions(
            self,
            request: models.DescribeMultiPathGatewayRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeMultiPathGatewayRegionsResponse:
        """
        This API is used to query the list of available regions for user-created multi-channel security acceleration gateways (Cloud Gateway).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMultiPathGatewayRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMultiPathGatewayRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMultiPathGatewaySecretKey(
            self,
            request: models.DescribeMultiPathGatewaySecretKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeMultiPathGatewaySecretKeyResponse:
        """
        This API is used to query keys for integrating multi-channel security acceleration gateways. Customers access multi-channel security acceleration gateways based on key signature.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMultiPathGatewaySecretKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMultiPathGatewaySecretKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMultiPathGateways(
            self,
            request: models.DescribeMultiPathGatewaysRequest,
            opts: Dict = None,
    ) -> models.DescribeMultiPathGatewaysResponse:
        """
        Query the multi-channel security acceleration gateway list created by the user through this interface. Supports pagination.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMultiPathGateways"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMultiPathGatewaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOriginACL(
            self,
            request: models.DescribeOriginACLRequest,
            opts: Dict = None,
    ) -> models.DescribeOriginACLResponse:
        """
        This API is used to query the binding relationship between L7 acceleration domains/L4 proxy instances and origin ACLs under a site, as well as IP range details. If you want to periodically obtain the latest version of origin IP ranges through an automation script, you can poll this API at a low-frequency (recommended every three days). If the NextOriginACL field has a return value, synchronize the latest origin IP ranges to the origin server firewall configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOriginACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOriginACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOriginGroup(
            self,
            request: models.DescribeOriginGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeOriginGroupResponse:
        """
        This API is used to obtain a list of origin groups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOriginGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOriginGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOriginGroupHealthStatus(
            self,
            request: models.DescribeOriginGroupHealthStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeOriginGroupHealthStatusResponse:
        """
        This API is used to query the health status of origin server groups under a LoadBalancer. The load balancing feature is in beta test. If you need to use it, [contact us](https://www.tencentcloud.com/contact-us).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOriginGroupHealthStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOriginGroupHealthStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOriginProtection(
            self,
            request: models.DescribeOriginProtectionRequest,
            opts: Dict = None,
    ) -> models.DescribeOriginProtectionResponse:
        """
        This API is used to query origin protection on an earlier version. EdgeOne comprehensively upgraded relevant APIs for origin protection on June 27, 2025. For details on the new version, see [DescribeOriginACL](https://intl.cloud.tencent.com/document/product/1552/120408?from_cn_redirect=1).

        Note: Starting from June 27, 2025, the legacy version APIs will stop updating. New features will only be provided in the latest version APIs. To avoid data field conflicts when using legacy version APIs, it is recommended to migrate to the new version origin protection APIs as soon as possible.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOriginProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOriginProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOverviewL7Data(
            self,
            request: models.DescribeOverviewL7DataRequest,
            opts: Dict = None,
    ) -> models.DescribeOverviewL7DataResponse:
        """
        This API is used to query the time sequence traffic data of the monitoring category in L7. This API is to be discarded. Please use the API <a href="https://intl.cloud.tencent.com/document/product/1552/80648?from_cn_redirect=1">DescribeTimingL7AnalysisData</a>.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOverviewL7Data"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOverviewL7DataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePlans(
            self,
            request: models.DescribePlansRequest,
            opts: Dict = None,
    ) -> models.DescribePlansResponse:
        """
        This API is used to query package information list with pagination support.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePlans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePlansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrefetchTasks(
            self,
            request: models.DescribePrefetchTasksRequest,
            opts: Dict = None,
    ) -> models.DescribePrefetchTasksResponse:
        """
        DescribePrefetchTasks is used to query the submission history and execution progress of preheating tasks. This interface can be used to query the tasks submitted by the CreatePrefetchTasks interface.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrefetchTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrefetchTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePurgeTasks(
            self,
            request: models.DescribePurgeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribePurgeTasksResponse:
        """
        DescribePurgeTasks is used to query the submitted URL refreshing and directory refreshing records and execution progress. This interface can be used to query the tasks submitted by the CreatePurgeTasks API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePurgeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePurgeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRealtimeLogDeliveryTasks(
            self,
            request: models.DescribeRealtimeLogDeliveryTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeRealtimeLogDeliveryTasksResponse:
        """
        This API is used to query the real-time log delivery task list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRealtimeLogDeliveryTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRealtimeLogDeliveryTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRules(
            self,
            request: models.DescribeRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeRulesResponse:
        """
        This API is on an earlier version to query engine rules. EdgeOne has comprehensively upgraded relevant APIs of the rule engine on January 21, 2025. For details about the new version API to query layer-7 acceleration rules, see DescribeL7AccRules(https://intl.cloud.tencent.com/document/product/1552/115820?from_cn_redirect=1).
        <p style="color: red;">Note: Starting from January 21, 2025, the old version of the interface will stop updating and iteration. Subsequent new features will only be provided in the new version of the interface, and the original capabilities supported by the old version of the interface will not be affected. To avoid data field conflicts when using the old version of the interface, it is recommended that you migrate to the new version of the rule engine interface as soon as possible. </p>
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRulesSetting(
            self,
            request: models.DescribeRulesSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeRulesSettingResponse:
        """
        This API is an older version. EdgeOne has fully upgraded the APIs related to the rule engine. For details, please refer to [RuleEngineAction](https://intl.cloud.tencent.com/document/product/1552/80721?from_cn_redirect=1#RuleEngineAction).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRulesSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRulesSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityAPIResource(
            self,
            request: models.DescribeSecurityAPIResourceRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityAPIResourceResponse:
        """
        This API is used to query API resources under a site.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityAPIResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityAPIResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityAPIService(
            self,
            request: models.DescribeSecurityAPIServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityAPIServiceResponse:
        """
        This API is used to query API services under a site.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityAPIService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityAPIServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityClientAttester(
            self,
            request: models.DescribeSecurityClientAttesterRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityClientAttesterResponse:
        """
        This API is used to query client authentication option configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityClientAttester"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityClientAttesterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityIPGroup(
            self,
            request: models.DescribeSecurityIPGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityIPGroupResponse:
        """
        This API is used to query the configuration information of a security IP group, including the ID, name and content of the security IP group. The query result of this API only returns up to 2000 IPs or CIDR blocks for each IP group. If there is a very large IP group exceeding 2000 IPs or CIDR blocks, call DescribeSecurityIPGroupContent to perform a paging query.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityIPGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityIPGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityIPGroupContent(
            self,
            request: models.DescribeSecurityIPGroupContentRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityIPGroupContentResponse:
        """
        This API is used to perform a paging query for the IP address list in a designated IP group. When the number of IP addresses in the group exceeds 2000, you can use this API to perform a paging query to obtain the complete IP address list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityIPGroupContent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityIPGroupContentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityIPGroupInfo(
            self,
            request: models.DescribeSecurityIPGroupInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityIPGroupInfoResponse:
        """
        The API is deprecated and will be discontinued on June 30, 2024. Please use the API [DescribeSecurityIPGroup
        ](https://intl.cloud.tencent.com/document/product/1552/105866?from_cn_redirect=1).

        This API is used to query the configuration information of an IP group, including the IP group name, IP group content, and the site the IP group belongs to.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityIPGroupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityIPGroupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityJSInjectionRule(
            self,
            request: models.DescribeSecurityJSInjectionRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityJSInjectionRuleResponse:
        """
        This API is used to query JavaScript injection rules.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityJSInjectionRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityJSInjectionRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityPolicy(
            self,
            request: models.DescribeSecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityPolicyResponse:
        """
        This API is used to query the web and security protection configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityTemplateBindings(
            self,
            request: models.DescribeSecurityTemplateBindingsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityTemplateBindingsResponse:
        """
        This API is used to query bindings of a policy template.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityTemplateBindings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityTemplateBindingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTimingL4Data(
            self,
            request: models.DescribeTimingL4DataRequest,
            opts: Dict = None,
    ) -> models.DescribeTimingL4DataResponse:
        """
        This API is used to query the list of L4 traffic data recorded over time.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTimingL4Data"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTimingL4DataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTimingL7AnalysisData(
            self,
            request: models.DescribeTimingL7AnalysisDataRequest,
            opts: Dict = None,
    ) -> models.DescribeTimingL7AnalysisDataResponse:
        """
        This API is used to query time series data for L7 domain name business.
        Create and bind policy Query instance Reset instance access password.
        This API is used to query data with a delay of about 10 minutes. It is recommended to pull data from at least 10 minutes before the current time.
        This API is used to return post-protection traffic request data by default. Users can query defended data in `Filters.mitigatedByWebSecurity`.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTimingL7AnalysisData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTimingL7AnalysisDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTimingL7CacheData(
            self,
            request: models.DescribeTimingL7CacheDataRequest,
            opts: Dict = None,
    ) -> models.DescribeTimingL7CacheDataResponse:
        """
        This API is used to query the time series traffic data of the L7 cache analysis. It will be deprecated. Use the <a href="https://intl.cloud.tencent.com/document/product/1552/80648?from_cn_redirect=1">DescribeTimingL7AnalysisData</a> API instead.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTimingL7CacheData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTimingL7CacheDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTimingL7OriginPullData(
            self,
            request: models.DescribeTimingL7OriginPullDataRequest,
            opts: Dict = None,
    ) -> models.DescribeTimingL7OriginPullDataResponse:
        """
        This API is used to query time series data for layer-7 domain services' origin-pull data.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTimingL7OriginPullData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTimingL7OriginPullDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopL7AnalysisData(
            self,
            request: models.DescribeTopL7AnalysisDataRequest,
            opts: Dict = None,
    ) -> models.DescribeTopL7AnalysisDataResponse:
        """
        This API is used to query the top N data of the L7 domain name business by specified dimension.
        Create and bind policy Query instance Reset instance access password.
        This API is used to query data with a delay of about 10 minutes. It is recommended to pull data from at least 10 minutes before the current time.
        This API is used to return post-protection traffic request data by default. Users can query defended data in `Filters.mitigatedByWebSecurity`.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopL7AnalysisData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopL7AnalysisDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopL7CacheData(
            self,
            request: models.DescribeTopL7CacheDataRequest,
            opts: Dict = None,
    ) -> models.DescribeTopL7CacheDataResponse:
        """
        This API is used to query the top N data of the L7 cache analysis. It will be deprecated. Use the <a href="https://intl.cloud.tencent.com/document/product/1552/80646?from_cn_redirect=1"> DescribeTopL7AnalysisData</a> API instead.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopL7CacheData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopL7CacheDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebSecurityTemplate(
            self,
            request: models.DescribeWebSecurityTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeWebSecurityTemplateResponse:
        """
        This API is used to query security policy configuration template details.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebSecurityTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebSecurityTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWebSecurityTemplates(
            self,
            request: models.DescribeWebSecurityTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeWebSecurityTemplatesResponse:
        """
        This API is used to query the security policy configuration template list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWebSecurityTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWebSecurityTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZoneConfigImportResult(
            self,
            request: models.DescribeZoneConfigImportResultRequest,
            opts: Dict = None,
    ) -> models.DescribeZoneConfigImportResultResponse:
        """
        This API is used to query the results of site configuration import via API (ImportZoneConfig). This feature only supports the sites in the plans of the Standard Edition and the Enterprise Edition.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZoneConfigImportResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZoneConfigImportResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZoneSetting(
            self,
            request: models.DescribeZoneSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeZoneSettingResponse:
        """
        This API is an old version. EdgeOne has fully upgraded the APIs related to the rule engine. For details, please refer to [DescribeL7AccSetting](https://intl.cloud.tencent.com/document/product/1552/115819?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZoneSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZoneSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZones(
            self,
            request: models.DescribeZonesRequest,
            opts: Dict = None,
    ) -> models.DescribeZonesResponse:
        """
        This API is used to query the information of sites that you have access to. You can filter sites based on different query criteria.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyPlan(
            self,
            request: models.DestroyPlanRequest,
            opts: Dict = None,
    ) -> models.DestroyPlanResponse:
        """
        To stop billing for your EdgeOne plan, you can use this interface to terminate the billing plan.
        > Terminating a billing plan requires the following conditions:
            1. The plan has expired (except for the Enterprise Edition Plan);
            2. All sites under the plan have been either shut down or deleted.

        > The site status can be queried through the [Query Site List](https://www.tencentcloud.com/zh/document/product/1145/50481) interface.
        A site can be deactivated by switching the site to a closed status through the [Switch Site Status](https://intl.cloud.tencent.com/document/product/1552/80707?from_cn_redirect=1) interface.
        A site can be deleted by using the [Delete Site](https://intl.cloud.tencent.com/document/product/1552/80717?from_cn_redirect=1) interface.
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableOriginACL(
            self,
            request: models.DisableOriginACLRequest,
            opts: Dict = None,
    ) -> models.DisableOriginACLResponse:
        """
        This API is used to disable 'Origin Protection' of a site. Once disabled, resources related to it will no longer use only the origin ACLs provided by "origin protection" to request your origin, and stops sending update notifications on the origin ACLs.
        """
        
        kwargs = {}
        kwargs["action"] = "DisableOriginACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableOriginACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadL4Logs(
            self,
            request: models.DownloadL4LogsRequest,
            opts: Dict = None,
    ) -> models.DownloadL4LogsResponse:
        """
        This API is used to download L4 logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadL4Logs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadL4LogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadL7Logs(
            self,
            request: models.DownloadL7LogsRequest,
            opts: Dict = None,
    ) -> models.DownloadL7LogsResponse:
        """
        This API is used to download L7 logs.
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadL7Logs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadL7LogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableOriginACL(
            self,
            request: models.EnableOriginACLRequest,
            opts: Dict = None,
    ) -> models.EnableOriginACLResponse:
        """
        This API is used to enable origin protection for a site for the first time. Enabled, EdgeOne will use specific origin IP ranges to backhaul traffic for L7 acceleration domains/L4 proxy instances. The maximum allowed number of L7 acceleration domains per submission is 200, and the maximum allowed number of L4 proxy instances is 100. Mixing L7 acceleration domains and L4 proxy instances in a single submission is supported, with a total maximum of 200 instances. To enable more than 200 resources, first enable the maximum quantity via specified resources, then enable the remaining resources via the ModifyOriginACL API. Subsequent addition of L7 acceleration domains/L4 proxy instances should be configured via the ModifyOriginACL API.

        Create and bind policy Query instance Reset instance access password.
        -Call this API to deem as consent to the origin protection enablement special agreement (https://intl.cloud.tencent.com/document/product/1552/120141?from_cn_redirect=1);.
        -The origin IP range may change irregularly. tencent cloud EdgeOne (EdgeOne) will trigger notifications via message Center, SMS, or email 14 days, 7 days, 3 days, and 1 day before the change. To ensure you receive the change notification for the origin IP range, please ensure you have selected EdgeOne product services in the [tencent cloud message Center console](https://console.cloud.tencent.com/message) and configured the correct message recipient. For the setting method, refer to [message Subscription Management](https://intl.cloud.tencent.com/document/product/567/43476?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "EnableOriginACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableOriginACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExportZoneConfig(
            self,
            request: models.ExportZoneConfigRequest,
            opts: Dict = None,
    ) -> models.ExportZoneConfigResponse:
        """
        This API is used to export site configuration . The exported configuration is used for import via the API (ImportZoneConfig). This feature only supports the sites in the plans of the Standard Edition and the Enterprise Edition.
        """
        
        kwargs = {}
        kwargs["action"] = "ExportZoneConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExportZoneConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def HandleFunctionRuntimeEnvironment(
            self,
            request: models.HandleFunctionRuntimeEnvironmentRequest,
            opts: Dict = None,
    ) -> models.HandleFunctionRuntimeEnvironmentResponse:
        """
        This API is used to operate the runtime environment of an edge function. It supports related settings for environment variables.
        After the environment variables are set, they can be used in the function code. For details, see [Edge Functions Referencing Environment Variables](https://intl.cloud.tencent.com/document/product/1552/109151?from_cn_redirect=1#0151fd9a-8b0e-407b-ae37-54553a60ded6).
        """
        
        kwargs = {}
        kwargs["action"] = "HandleFunctionRuntimeEnvironment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.HandleFunctionRuntimeEnvironmentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IdentifyZone(
            self,
            request: models.IdentifyZoneRequest,
            opts: Dict = None,
    ) -> models.IdentifyZoneResponse:
        """
        This API is used to verify ownership of the site.
        """
        
        kwargs = {}
        kwargs["action"] = "IdentifyZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IdentifyZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportZoneConfig(
            self,
            request: models.ImportZoneConfigRequest,
            opts: Dict = None,
    ) -> models.ImportZoneConfigResponse:
        """
        This API is used to quickly import site configuration files. After the import is initiated, the API will return the corresponding task ID (TaskId). Users need to use the site configuration import result query API (DescribeZoneConfigImportResult) to obtain the results of this import task. This feature only supports the sites in the plans of the Standard Edition and the Enterprise Edition.
        """
        
        kwargs = {}
        kwargs["action"] = "ImportZoneConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportZoneConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IncreasePlanQuota(
            self,
            request: models.IncreasePlanQuotaRequest,
            opts: Dict = None,
    ) -> models.IncreasePlanQuotaResponse:
        """
        When the number of sites bound to your plan, the number of rules under "Web Protection - Custom Rules - Precision Matching Policy", or the number of rules under "Web Protection - Rate Limiting - Precision Rate Limiting Module" reaches the plan's quota, you can use this interface to purchase additional quotas.
        > This interface only supports the Enterprise Edition Plan.
        """
        
        kwargs = {}
        kwargs["action"] = "IncreasePlanQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IncreasePlanQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccelerationDomain(
            self,
            request: models.ModifyAccelerationDomainRequest,
            opts: Dict = None,
    ) -> models.ModifyAccelerationDomainResponse:
        """
        This API is used to modify an accelerated domain name.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccelerationDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccelerationDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccelerationDomainStatuses(
            self,
            request: models.ModifyAccelerationDomainStatusesRequest,
            opts: Dict = None,
    ) -> models.ModifyAccelerationDomainStatusesResponse:
        """
        This API is used to batch modify the status of accelerated domains.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccelerationDomainStatuses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccelerationDomainStatusesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAliasDomain(
            self,
            request: models.ModifyAliasDomainRequest,
            opts: Dict = None,
    ) -> models.ModifyAliasDomainResponse:
        """
        This API is used to modify an alias domain name.
        The feature is only supported in the enterprise plan and is currently in closed beta testing. If you need to use it, [contact us](https://www.tencentcloud.com/contact-us).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAliasDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAliasDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAliasDomainStatus(
            self,
            request: models.ModifyAliasDomainStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyAliasDomainStatusResponse:
        """
        This API is used to modify the status of an alias domain name.
        The feature is only supported in the enterprise plan and is currently in closed beta testing. If you need to use it, [Contact Us](https://www.tencentcloud.com/contact-us).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAliasDomainStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAliasDomainStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationProxy(
            self,
            request: models.ModifyApplicationProxyRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationProxyResponse:
        """
        This API is on an earlier version. If you want to call it, please switch to the latest version. For details, see [ModifyL4Proxy
        ] (https://intl.cloud.tencent.com/document/product/1552/103411?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationProxyRule(
            self,
            request: models.ModifyApplicationProxyRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationProxyRuleResponse:
        """
        This API is on an earlier version. If you want to call it, please switch to the latest version. For details, see [ModifyL4ProxyRules] (https://intl.cloud.tencent.com/document/product/1552/103410?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationProxyRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationProxyRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationProxyRuleStatus(
            self,
            request: models.ModifyApplicationProxyRuleStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationProxyRuleStatusResponse:
        """
        This API is on an earlier version. If you want to call it, please switch to the latest version. For details, see [ModifyL4ProxyRulesStatus
        ] (https://intl.cloud.tencent.com/document/product/1552/103409?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationProxyRuleStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationProxyRuleStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApplicationProxyStatus(
            self,
            request: models.ModifyApplicationProxyStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyApplicationProxyStatusResponse:
        """
        This API is on an earlier version. If you want to call it, please switch to the latest version. For details, see [ModifyL4ProxyStatus] (https://intl.cloud.tencent.com/document/product/1552/103408?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApplicationProxyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApplicationProxyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyContentIdentifier(
            self,
            request: models.ModifyContentIdentifierRequest,
            opts: Dict = None,
    ) -> models.ModifyContentIdentifierResponse:
        """
        Modify content identifier, only description modification is supported. This feature is only open to the allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyContentIdentifier"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyContentIdentifierResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCustomErrorPage(
            self,
            request: models.ModifyCustomErrorPageRequest,
            opts: Dict = None,
    ) -> models.ModifyCustomErrorPageResponse:
        """
        This API is used to modify a custom response page.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCustomErrorPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCustomErrorPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSProtection(
            self,
            request: models.ModifyDDoSProtectionRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSProtectionResponse:
        """
        This API is used to modify site exclusive Anti-DDoS protection.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDDoSProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDDoSProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDnsRecords(
            self,
            request: models.ModifyDnsRecordsRequest,
            opts: Dict = None,
    ) -> models.ModifyDnsRecordsResponse:
        """
        This API is used to bulk modify DNS records.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDnsRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDnsRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDnsRecordsStatus(
            self,
            request: models.ModifyDnsRecordsStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyDnsRecordsStatusResponse:
        """
        You can batch modify the status of DNS records through this API, enabling and disabling records in bulk.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDnsRecordsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDnsRecordsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFunction(
            self,
            request: models.ModifyFunctionRequest,
            opts: Dict = None,
    ) -> models.ModifyFunctionResponse:
        """
        This API is used to modify an edge function. It supports modifying the function content and description. The function will take effect immediately after modification and redeployment.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFunctionRule(
            self,
            request: models.ModifyFunctionRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyFunctionRuleResponse:
        """
        This API is used to modify a trigger rule for an edge function. It supports modifying rule conditions, execution functions, and description.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFunctionRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFunctionRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFunctionRulePriority(
            self,
            request: models.ModifyFunctionRulePriorityRequest,
            opts: Dict = None,
    ) -> models.ModifyFunctionRulePriorityResponse:
        """
        This API is used to modify the priority of trigger rules for an edge function.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFunctionRulePriority"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFunctionRulePriorityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHostsCertificate(
            self,
            request: models.ModifyHostsCertificateRequest,
            opts: Dict = None,
    ) -> models.ModifyHostsCertificateResponse:
        """
        This API is used to configure the certificate of a site. You can use your own certificate or [apply for a free certificate](https://intl.cloud.tencent.com/document/product/1552/90437?from_cn_redirect=1).
        To use an external certificate, upload the certificate to [SSL Certificates Console](https://console.cloud.tencent.com/certoview) first, and then input the certificate ID in this API. For details, see [Deploying Own Certificates to EdgeOne Domains](https://intl.cloud.tencent.com/document/product/1552/88874?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHostsCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHostsCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL4Proxy(
            self,
            request: models.ModifyL4ProxyRequest,
            opts: Dict = None,
    ) -> models.ModifyL4ProxyResponse:
        """
        This API is used to modify the configuration of a Layer 4 proxy instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL4Proxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL4ProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL4ProxyRules(
            self,
            request: models.ModifyL4ProxyRulesRequest,
            opts: Dict = None,
    ) -> models.ModifyL4ProxyRulesResponse:
        """
        This API is used to modify Layer 4 proxy forwarding rules, supporting both individual and batch modification.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL4ProxyRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL4ProxyRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL4ProxyRulesStatus(
            self,
            request: models.ModifyL4ProxyRulesStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyL4ProxyRulesStatusResponse:
        """
        This API is used to start or stop Layer 4 proxy forwarding rules, supporting both individual and batch operation.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL4ProxyRulesStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL4ProxyRulesStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL4ProxyStatus(
            self,
            request: models.ModifyL4ProxyStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyL4ProxyStatusResponse:
        """
        This API is used to enable or disable a Layer 4 proxy instance.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL4ProxyStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL4ProxyStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL7AccRule(
            self,
            request: models.ModifyL7AccRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyL7AccRuleResponse:
        """
        This API is used to modify rules in the [rule engine](https://intl.cloud.tencent.com/document/product/1552/70901?from_cn_redirect=1), supporting only one rule modification per request.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL7AccRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL7AccRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL7AccRulePriority(
            self,
            request: models.ModifyL7AccRulePriorityRequest,
            opts: Dict = None,
    ) -> models.ModifyL7AccRulePriorityResponse:
        """
        This interface is used to modify the priority of the rule list in the [Rule Engine](https://intl.cloud.tencent.com/document/product/1552/70901?from_cn_redirect=1). This interface requires the complete rule ID list under the site ID to be passed in. The rule ID list can be obtained through the [Query Seven-Layer Acceleration Rules](https://intl.cloud.tencent.com/document/product/1552/115820?from_cn_redirect=1) interface. The final priority order will be adjusted to the order of the rule ID list, and will be executed from front to back.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL7AccRulePriority"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL7AccRulePriorityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL7AccSetting(
            self,
            request: models.ModifyL7AccSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyL7AccSettingResponse:
        """
        This API is used to modify the global configuration of [Site Acceleration](https://intl.cloud.tencent.com/document/product/1552/96193?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL7AccSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL7AccSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoadBalancer(
            self,
            request: models.ModifyLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.ModifyLoadBalancerResponse:
        """
        This API is used to modify LoadBalancer configuration. The load balancing feature is in beta test. If you need to use it, [contact us](https://www.tencentcloud.com/contact-us).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMultiPathGateway(
            self,
            request: models.ModifyMultiPathGatewayRequest,
            opts: Dict = None,
    ) -> models.ModifyMultiPathGatewayResponse:
        """
        This API is used to modify multi-channel security acceleration gateway information, such as name, gateway ID, IP and port.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMultiPathGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMultiPathGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMultiPathGatewayLine(
            self,
            request: models.ModifyMultiPathGatewayLineRequest,
            opts: Dict = None,
    ) -> models.ModifyMultiPathGatewayLineResponse:
        """
        This API is used to modify the access lines of the multi-channel security acceleration gateway, including EdgeOne Layer-4 proxy lines and custom lines.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMultiPathGatewayLine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMultiPathGatewayLineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMultiPathGatewaySecretKey(
            self,
            request: models.ModifyMultiPathGatewaySecretKeyRequest,
            opts: Dict = None,
    ) -> models.ModifyMultiPathGatewaySecretKeyResponse:
        """
        This API is used to modify the access key for the multi-channel security acceleration gateway.The access key is used by customers to sign requests for gateway access. The original key becomes invalid after modification.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMultiPathGatewaySecretKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMultiPathGatewaySecretKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMultiPathGatewayStatus(
            self,
            request: models.ModifyMultiPathGatewayStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyMultiPathGatewayStatusResponse:
        """
        This API is used to update the status of a multi-channel security gateway.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMultiPathGatewayStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMultiPathGatewayStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOriginACL(
            self,
            request: models.ModifyOriginACLRequest,
            opts: Dict = None,
    ) -> models.ModifyOriginACLResponse:
        """
        This API is used to enable or disable specific origin ACLs for L7 acceleration domain names or L4 proxy instances. A single submission supports up to 200 L7 acceleration domain names or 100 L4 proxy instances. Hybrid submissions of L7 acceleration domain names and L4 proxy instances are supported, with a maximum total number of instances of 200. If changes are needed for exceeding 200 instances, submit them in batches via this API.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOriginACL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOriginACLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyOriginGroup(
            self,
            request: models.ModifyOriginGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyOriginGroupResponse:
        """
        This API is used to modify the configuration of an origin group. The original configuration will be overwritten.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyOriginGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyOriginGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPlan(
            self,
            request: models.ModifyPlanRequest,
            opts: Dict = None,
    ) -> models.ModifyPlanResponse:
        """
        Modify the plan settings. Currently, only the auto-renewal switch of prepaid plans can be modified.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRealtimeLogDeliveryTask(
            self,
            request: models.ModifyRealtimeLogDeliveryTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyRealtimeLogDeliveryTaskResponse:
        """
        This API is used to modify the real-time log delivery task configuration. This API has the following restrictions:<li>Does not support modifying the destination type of the real-time log delivery task (TaskType);</li><li>Does not support modifying the data delivery type (LogType);</li><li>Does not support modifying the data delivery area (Area);</li><li>Does not support modifying the detailed destination configuration, such as log set and log topic, when the destination of the original real-time log delivery task is Tencent Cloud CLS.</li>
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRealtimeLogDeliveryTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRealtimeLogDeliveryTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRule(
            self,
            request: models.ModifyRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyRuleResponse:
        """
        This API is on an earlier version. EdgeOne has comprehensively upgraded the relevant APIs of the rule engine on January 21, 2025. For details about the new version of the API for modifying layer-7 acceleration rules, see ModifyL7AccRule(https://intl.cloud.tencent.com/document/product/1552/115818?from_cn_redirect=1).
        <p style="color: red;">Note: Starting from January 21, 2025, the old version of the interface will stop updating and iteration. Subsequent new features will only be provided in the new version of the interface, and the original capabilities supported by the old version of the interface will not be affected. To avoid data field conflicts when using the old version of the interface, it is recommended that you migrate to the new version of the rule engine interface as soon as possible. </p>
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityAPIResource(
            self,
            request: models.ModifySecurityAPIResourceRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityAPIResourceResponse:
        """
        This API is used to modify an API resource.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityAPIResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityAPIResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityAPIService(
            self,
            request: models.ModifySecurityAPIServiceRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityAPIServiceResponse:
        """
        This API is used to modify an API service.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityAPIService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityAPIServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityClientAttester(
            self,
            request: models.ModifySecurityClientAttesterRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityClientAttesterResponse:
        """
        This API is used to modify client authentication options.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityClientAttester"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityClientAttesterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityIPGroup(
            self,
            request: models.ModifySecurityIPGroupRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityIPGroupResponse:
        """
        This API is used to modify a security IP group.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityIPGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityIPGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityJSInjectionRule(
            self,
            request: models.ModifySecurityJSInjectionRuleRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityJSInjectionRuleResponse:
        """
        This API is used to modify JavaScript injection rules.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityJSInjectionRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityJSInjectionRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityPolicy(
            self,
            request: models.ModifySecurityPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityPolicyResponse:
        """
        This API is used to modify the web and bot security configurations.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebSecurityTemplate(
            self,
            request: models.ModifyWebSecurityTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyWebSecurityTemplateResponse:
        """
        This API is used to modify the security policy configuration template.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWebSecurityTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWebSecurityTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyZone(
            self,
            request: models.ModifyZoneRequest,
            opts: Dict = None,
    ) -> models.ModifyZoneResponse:
        """
        This API is used to modify a site.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyZoneSetting(
            self,
            request: models.ModifyZoneSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyZoneSettingResponse:
        """
        This API is an older version. EdgeOne has fully upgraded the APIs related to the rule engine. For details, please refer to [ModifyL7AccSetting](https://intl.cloud.tencent.com/document/product/1552/115817?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyZoneSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyZoneSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyZoneStatus(
            self,
            request: models.ModifyZoneStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyZoneStatusResponse:
        """
        This API is used to change the site status.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyZoneStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyZoneStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RefreshMultiPathGatewaySecretKey(
            self,
            request: models.RefreshMultiPathGatewaySecretKeyRequest,
            opts: Dict = None,
    ) -> models.RefreshMultiPathGatewaySecretKeyResponse:
        """
        This API is used to refresh keys for multi-channel security acceleration gateways. Customers access multi-channel security acceleration gateways based on integration key signatures. Each site has only one access key, which applies to all gateways under that site. After refreshing the key, the original key becomes invalid.
        """
        
        kwargs = {}
        kwargs["action"] = "RefreshMultiPathGatewaySecretKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RefreshMultiPathGatewaySecretKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewPlan(
            self,
            request: models.RenewPlanRequest,
            opts: Dict = None,
    ) -> models.RenewPlanResponse:
        """
        When your plan needs to be extended, you can use this interface to renew it. Plan renewal is only supported for the Personal, Basic, and Standard Editions.
        > For cost details, refer to [Plan Fees](https://intl.cloud.tencent.com/document/product/1552/94158?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "RenewPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradePlan(
            self,
            request: models.UpgradePlanRequest,
            opts: Dict = None,
    ) -> models.UpgradePlanResponse:
        """
        When you need features available only in higher-tier plans, you can upgrade your plan through this interface. Upgrades are only supported for Personal and Basic Edition Plans.
        > For differences between EdgeOne billing plans, refer to [Comparison of EdgeOne Plans](https://intl.cloud.tencent.com/document/product/1552/94165?from_cn_redirect=1).
        For EdgeOne plan upgrade rules and pricing details, refer to [EdgeOne Plan Upgrade Guide](https://intl.cloud.tencent.com/document/product/1552/95291?from_cn_redirect=1).
        If your plan needs to upgrade to the Enterprise Edition, [Contact Us](https://www.tencentcloud.com/contact-us).
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyOwnership(
            self,
            request: models.VerifyOwnershipRequest,
            opts: Dict = None,
    ) -> models.VerifyOwnershipResponse:
        """
        This API is used to verify your ownership of a site or domain name. It's required in the CNAME access mode. After a site is verified, you don't need to verify the ownership again for domain names added to it in the future. For details, see [Ownership Verification](https://intl.cloud.tencent.com/document/product/1552/70789?from_cn_redirect=1).

        For sites connected via the NS, you can query whether the NS is successfully switched through this API. For details, see [Modifying DNS Servers](https://intl.cloud.tencent.com/document/product/1552/90452?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyOwnership"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyOwnershipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)