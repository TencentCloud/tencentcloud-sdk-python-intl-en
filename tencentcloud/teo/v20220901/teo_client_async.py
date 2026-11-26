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
        When applying for a free certificate, if you need to apply through DNS delegation verification or file verification, you can call this API to initiate the certificate application and get the corresponding verification content based on the application method. The order in which to call the API is as follows:
        Step 1: Call ApplyFreeCertificate to specify the verification method for the free certificate application and obtain the verification content.
        Step 2: Configure the content for the corresponding domain as required for verification.
        Step 3: Call CheckFreeCertificateVerification for verification. The free certificate application is completed after verification passes.
        Step 4: Call ModifyHostsCertificate to configure the domain name certificate with an EdgeOne free certificate.

        For the introduction to application methods, see the referenced document: Free Certificate Application Description (https://www.tencentcloud.com/document/product/1552/90437?from_cn_redirect=1)
        Description:
        -Only the CNAME access mode can call this API to specify the free certificate application method. The NS/DNSPod hosting access mode uses automatic validation to apply for a free certificate, with no need to call this API.
        -If you need to switch the verification method for a free certificate, you can call this API again to update it by changing the VerificationMethod field.
        -A domain name can only apply for one free certificate. After calling this API, the backend will trigger the free certificate application task. You need to complete the domain name verification info configuration within 2 days, and then complete certificate authentication.
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
        Operate a security policy template. This API is used to bind or rebind a domain name to a designated policy template, or unbind it from a designated policy template.
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
        Used to bind or unbind a shared CNAME for an acceleration domain name. This feature is in beta test.
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
        Bind the selected site not bound to a package to an existing package.
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
        When the site access type is CNAME, all domain names under the site must complete CNAME record configuration as specified by the CNAME domain assigned by EdgeOne.
        This API is used to obtain the CNAME domain name assigned by EdgeOne for the integrated domain name, and to validate the CNAME configuration status of the integrated domain name.
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
        This API is used to verify a free certificate and obtain the application result. If verification is passed, you can query the free certificate information for the corresponding domain through this API. If the application failed, this API will return the corresponding failure description.
        After triggering the free certificate application API (https://www.tencentcloud.com/document/product/1552/90437?from_cn_redirect=1), you can check the free certificate application result through this API. Once the free certificate application is successful, you need to configure it through the domain certificate configuration API (https://www.tencentcloud.com/document/product/1552/80764?from_cn_redirect=1) to deploy the free certificate to the acceleration domain.
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
        This API is used to confirm that the latest origin-pull IP ranges have been updated to the origin server firewall when the origin-pull IP ranges of the multi-channel security acceleration gateway change.
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
        This API is used to confirm that the latest origin-pull IP ranges have been updated to the origin server firewall when the origin-pull IP ranges change. After confirming the update to the latest origin-pull IP ranges, related change notifications will stop being pushed.
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
        After creating a site, you can create an acceleration domain name through this API.

        In CNAME mode, if site ownership verification is ongoing, this API will return domain ownership verification info. You can verify domain ownership separately. For details, see [Site/Domain Name Ownership Verification](https://www.tencentcloud.com/document/product/1552/70789?from_cn_redirect=1).
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
        This feature is only supported in the enterprise plan and is currently in beta test. To use it, please [contact us](https://www.tencentcloud.com/contact-us).
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
        This API is on an earlier version. If you want to call it, switch to the latest version to create layer 4 proxy instances (https://www.tencentcloud.com/document/product/1552/103417?from_cn_redirect=1).
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
        This API is on an earlier version. If you want to call it, switch to the latest version. For details, see [Create Layer 4 Proxy Forwarding Rule].
        ](https://www.tencentcloud.com/document/product/1552/103416?from_cn_redirect=1) .
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
        This API is used to create key-value indexes for delivered log fields in the corresponding Tencent Cloud CLS log topic for a specified real-time log delivery task (task-id). If indexes have been created in CLS, this API will append indexes through merging.
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
        In version management mode, this API is used to create a new version of a specified configuration group.
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
        This API is used to create a content identifier. You can set the description, tag, and other information. At the same time, you need to bind an enterprise package for billing data statistics. A content identifier can only be bound to one billing package, while a billing package can bind multiple content identifiers. This functionality is only available to allowlisted users.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateContentIdentifier"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateContentIdentifierResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCustomGroup(
            self,
            request: models.CreateCustomGroupRequest,
            opts: Dict = None,
    ) -> models.CreateCustomGroupResponse:
        """
        This API is used to create a custom group. A custom group is used to centrally manage a set of reusable matching entries. For example, you can save multiple JA3/JA4 TLS fingerprints as a TLS fingerprint group and directly reference the group in security rules, avoiding the need to maintain the same fingerprint list in multiple rules.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCustomGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCustomGroupResponse
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
        After a site is created and accessed in NS mode, you can create DNS records through this API.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDnsRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDnsRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEdgeKVNamespace(
            self,
            request: models.CreateEdgeKVNamespaceRequest,
            opts: Dict = None,
    ) -> models.CreateEdgeKVNamespaceResponse:
        """
        This API is used to create a KV namespace at a specified site.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEdgeKVNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEdgeKVNamespaceResponse
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
        
    async def CreateFunctionReplica(
            self,
            request: models.CreateFunctionReplicaRequest,
            opts: Dict = None,
    ) -> models.CreateFunctionReplicaResponse:
        """
        This API is used to create copies of a specified edge function. After creating copies, when client requests match the configured trigger rules or default domain name, you can access a specific function copy by adding EO-Function-Replica-Name:[copy name] to the request header. Each function supports creating two copies by default.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFunctionReplica"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFunctionReplicaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFunctionRule(
            self,
            request: models.CreateFunctionRuleRequest,
            opts: Dict = None,
    ) -> models.CreateFunctionRuleResponse:
        """
        Creates a trigger rule for an edge function. It supports customized filter conditions to determine whether to execute a function. When a function needs to be executed, multiple ways are provided to select the target function, including directly specifying, selecting based on the client's associated region, and weight-based selection.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFunctionRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFunctionRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInferenceAPIToken(
            self,
            request: models.CreateInferenceAPITokenRequest,
            opts: Dict = None,
    ) -> models.CreateInferenceAPITokenResponse:
        """
        Create an inference API Token for authentication when accessing the inference service. The Token content is returned only once when creating, and each site can create up to 100 tokens.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInferenceAPIToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInferenceAPITokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInferenceDomain(
            self,
            request: models.CreateInferenceDomainRequest,
            opts: Dict = None,
    ) -> models.CreateInferenceDomainResponse:
        """
        Create an inference service domain name for accessing the inference service through a custom domain name. An inference service supports creating a maximum of 5 custom domain names.
        After successful creation, complete the following steps to make the domain name function normally for external access:
        1. To validate the CNAME configuration status of a domain, see the CheckCnameStatus api.
        2. To verify ownership, refer to the VerifyOwnership API (https://www.tencentcloud.com/document/api/1552/98879?from_cn_redirect=1);
        3. To configure domain name certificates, refer to the ModifyHostsCertificate api.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInferenceDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInferenceDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInferenceService(
            self,
            request: models.CreateInferenceServiceRequest,
            opts: Dict = None,
    ) -> models.CreateInferenceServiceResponse:
        """
        This API is used to create an inference service. You can set the service name, listening port, container image configuration, and resource configuration. An access address is provided after successful creation.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInferenceService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInferenceServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateJustInTimeTranscodeTemplate(
            self,
            request: models.CreateJustInTimeTranscodeTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateJustInTimeTranscodeTemplateResponse:
        """
        JIT transcoding already provides preset transcoding templates to meet most needs. For personalized transcoding requirements, you can create custom transcoding templates through this API, with up to 100 custom templates.
        To ensure consistency of JIT transcoding effects and avoid video output exceptions caused by template changes during EO cache or M3U8 sharding, the template cannot be modified after creation.
        To learn about JIT transcoding capacity, see EdgeOne Video Instant Processing Function Introduction (https://www.tencentcloud.com/document/product/1552/111927?from_cn_redirect=1).
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
        This API is used to create a layer 4 proxy instance.
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
        This API is used to create Layer 4 proxy instance rules and supports individual and batch creation.
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
        This API is used to create rules in the [rule engine](https://www.tencentcloud.com/document/product/1552/70901?from_cn_redirect=1), with support for batch creation.
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
        This API is used to create a LoadBalancer. For details, see [Quickly Create Load Balancers](https://www.tencentcloud.com/document/product/1552/104223?from_cn_redirect=1). The load balancing feature is in beta test. If you need to use it, [contact us](https://www.tencentcloud.com/contact-us).
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLogAnalysisDownloadTask(
            self,
            request: models.CreateLogAnalysisDownloadTaskRequest,
            opts: Dict = None,
    ) -> models.CreateLogAnalysisDownloadTaskResponse:
        """
        This API is used to create a log analysis download task. After creation, you can query the download task through the DescribeLogAnalysisDownloadTasks API.
        Note:
        1. Supports up to 50 million log entries per download.
        2. Log files will be retained for 3 days.
        3. If multiple tasks exist at the same time, they will be processed sequentially based on task creation time.
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLogAnalysisDownloadTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLogAnalysisDownloadTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMultiPathGateway(
            self,
            request: models.CreateMultiPathGatewayRequest,
            opts: Dict = None,
    ) -> models.CreateMultiPathGatewayResponse:
        """
        This API is used to create a multi-channel security acceleration gateway, including Cloud Gateway and Private Gateway. Use the DescribeMultiPathGateway interface to query the status. If the status is online, the creation succeeded.
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
        This API is used to create lines for integrating with the multi-channel security acceleration gateway, including EdgeOne Layer 4 proxy lines and custom lines.
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
        This API is used to create a key for integrating with a multi-channel security acceleration gateway. Customers integrate with the multi-channel security acceleration gateway based on key signatures. Each site contains only one key, which can be used to integrate all gateways under the site. The key can be queried through the DescribeMultiPathGatewaySecretKey API.
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
        Create an origin server group to manage origin servers by group. The origin server group configured here can be referenced in features such as **adding an acceleration domain name** and **Layer 4 proxy**.
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
        If you need to use the Edgeone product, you need to create a billing plan through this interface.
        > After creating a package, you need to complete creating a site and binding the plan through [CreateZone](https://www.tencentcloud.com/document/product/1552/80719?from_cn_redirect=1) before Edgeone can provide services properly.
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
        Purchase a package for the selected site not bound to a package.
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
        This API is used to create a preheating task.
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
        When origin server resources update but the node cache TTL has not expired, users still access old resources. At this point, use this API to update node resources. The following two methods can trigger updates: <li>Direct deletion: Delete the node cache without any validation. User requests trigger origin-pull.</li><li>Mark expiration: Mark node resources as expired. User requests trigger back-to-origin validation, which sends HTTP conditional requests with If-None-Match and If-Modified-Since headers. If the origin server responds with 200, the node fetches new resources from the origin and updates the cache. If the origin server responds with 304, the cache will not be updated.</li>

        For details on purging cache tasks, see [Purge Cache](https://www.tencentcloud.com/document/product/1552/70759?from_cn_redirect=1).
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

        **Restrictions**

        An entity (a Layer 7 domain name, a Layer 4 proxy instance, or an Edge Function instance) under the same combination of `LogType` and `Area` can only have one task created for each `TaskType`. The mutual exclusion rules for different `LogType` values are as follows:

        | LogType | Conflicting TaskType |
        |---|---|
        | Layer 4 proxy logs, Edge Function execution logs | Choose one of `custom_endpoint`, `s3`, and `aws_s3` |

        When `TaskType` is `log_analysis`:

        <ul>
        <li>Only `LogType` = `l7-access-logs` or `web-attack` is supported.</li>
        <li>Under the same combination of `ZoneId` and `Area`, only one task can be created for each `LogType`.</li>
        </ul>

        **Recommendation**: Before creating a task, call the [DescribeRealtimeLogDeliveryTasks](https://www.tencentcloud.com/document/product/1145/59503) API to query existing tasks and avoid duplicate additions.
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
        This API is on an earlier version for creating rule engine APIs. EdgeOne comprehensively upgraded the rule engine APIs on January 21, 2025. For details on the new API for creating layer-7 acceleration rules, refer to [CreateL7AccRules](https://www.tencentcloud.com/document/product/1552/115822?from_cn_redirect=1).
        <p style="color: red;">Note: Starting from January 21, 2025, the old version APIs will stop update and iteration. New features will only be provided by the latest version interface. The existing capacity supported by the old version APIs will not be affected. To avoid data field conflicts when using the old version APIs, migrate to the new version rule engine APIs as soon as possible.</p>
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
        Used to create API resources.
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
        Used to create an API service.
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
        Create client authentication options.
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
        Create a security IP group
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
        This API is used to create JavaScript injection rules.
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
        Used to create a shared CNAME. This feature is in beta test.
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
        Create a security policy configuration template
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
        EdgeOne offers three access methods: CNAME, NS, and domainless access. You need to finalize site creation through this API first. For CNAME and NS connected site scenarios, see [Quickly access EdgeOne from scratch](https://www.tencentcloud.com/document/product/1552/87601?from_cn_redirect=1). For domainless access scenarios, see [Quickly enable layer 4 proxy service](https://www.tencentcloud.com/document/product/1552/96051?from_cn_redirect=1).

        > It is recommended to call this API to create a site when a package already exists under the account. Please input `PlanId` in the parameter to directly bind the site to the package. If `PlanId` is not input, the created site will be inactive and unable to provide normal services. You need to complete package binding through [BindZoneToPlan](https://www.tencentcloud.com/document/product/1552/83042?from_cn_redirect=1) before the site can provide services normally. If you currently have no bindable package, go to the console to purchase a package to finalize site creation.
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
        Delete acceleration domain names in batches.
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
        Delete an alias domain name.
        This feature is only supported in the enterprise plan and is currently in beta test. To use it, please [contact us](https://www.tencentcloud.com/contact-us).
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
        This API is on an earlier version. If you want to call it, switch to the latest version. For details, see Deleting a Layer 4 Proxy Instance.
        ](https://www.tencentcloud.com/document/product/1552/103415?from_cn_redirect=1) .
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
        This API is on an earlier version. If you want to call it, switch to the latest version. For details, see Deleting L4 Proxy Rules (https://www.tencentcloud.com/document/product/1552/103414?from_cn_redirect=1).
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
        Delete the specified content identifier. The feature is open only in the allowlist.
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
        
    async def DeleteCustomGroup(
            self,
            request: models.DeleteCustomGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteCustomGroupResponse:
        """
        This API is used to delete a specified custom group. If the group is referenced by a rule, deletion is not allowed. Remove the reference first.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCustomGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCustomGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDnsRecords(
            self,
            request: models.DeleteDnsRecordsRequest,
            opts: Dict = None,
    ) -> models.DeleteDnsRecordsResponse:
        """
        You can use this API to delete DNS records in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDnsRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDnsRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteEdgeKVNamespace(
            self,
            request: models.DeleteEdgeKVNamespaceRequest,
            opts: Dict = None,
    ) -> models.DeleteEdgeKVNamespaceResponse:
        """
        This API is used to delete a specified KV namespace. After deletion, all key-value pair data in the namespace will be cleared and cannot be recovered. If the namespace is referenced by an edge function, unbind the relationship before deletion.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteEdgeKVNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteEdgeKVNamespaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFunction(
            self,
            request: models.DeleteFunctionRequest,
            opts: Dict = None,
    ) -> models.DeleteFunctionResponse:
        """
        This API is used to delete an edge function. Once deleted, the function cannot be recovered, and associated trigger rules, environment variables, and replicas are also deleted.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFunctionReplica(
            self,
            request: models.DeleteFunctionReplicaRequest,
            opts: Dict = None,
    ) -> models.DeleteFunctionReplicaResponse:
        """
        This API is used to delete a specified edge function replica.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFunctionReplica"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFunctionReplicaResponse
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
        
    async def DeleteInferenceAPIToken(
            self,
            request: models.DeleteInferenceAPITokenRequest,
            opts: Dict = None,
    ) -> models.DeleteInferenceAPITokenResponse:
        """
        Delete an inference API Token. Once deleted, the Token expires immediately, and requests using it to access the inference service will not pass authentication.
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInferenceAPIToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInferenceAPITokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteJustInTimeTranscodeTemplates(
            self,
            request: models.DeleteJustInTimeTranscodeTemplatesRequest,
            opts: Dict = None,
    ) -> models.DeleteJustInTimeTranscodeTemplatesResponse:
        """
        Delete a just in time transcoding template based on the unique template identifier under the site ID.
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
        This API is used to delete a layer 4 proxy instance.
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
        This API is used to delete l4 proxy rules and supports both individual and batch operation.
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
        This API is used to delete rules from the rule engine (https://www.tencentcloud.com/document/product/1552/70901?from_cn_redirect=1). Batch deletion supported.
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
        This API is used to delete a load balancing instance. If the load balancing instance is referenced by other services, such as a Layer 4 proxy, it cannot be deleted. Remove the reference relationship first. The load balancer feature is in beta test. If you need to use it, contact us (https://www.tencentcloud.com/online?from_cn_redirect=1-service).
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
        This API is used to delete multi-channel security acceleration gateways, including private gateways and Cloud Gateways.
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
        This API is used to delete lines integrated with multi-channel security acceleration gateways. Only custom lines support deletion.
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
        Delete an origin group. If the origin group is still referenced by a service (for example, Layer 4 proxy, DNS, load balancing, or a rule), deletion is not allowed.
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
        This API is on an earlier version for deleting rule engine APIs. EdgeOne completed a comprehensive upgrade of rule engine APIs on January 21, 2025. For details on the new API for deleting L7 acceleration rules, see [DeleteL7AccRules](https://www.tencentcloud.com/document/product/1552/115821?from_cn_redirect=1).
        <p style="color: red;">Note: Starting from January 21, 2025, the old version API will stop update and iteration. New features will only be provided in the new version API, and the existing capabilities supported by the old version API will not be affected. To avoid data field conflicts when using the old version API, migrate to the new version rule engine API as soon as possible.</p>
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
        Used to delete API resources.
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
        Used to delete an API service.
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
        Delete client authentication options.
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
        Delete a specified IP group. If a rule references the IP group, deletion is not allowed.
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
        Used to delete a shared CNAME. This feature is in beta test.
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
        Delete a security policy configuration template
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
        Delete a site.
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
        In version management mode, this API is used for version release. You can release a version to the testing environment or production environment by EnvId. The version management feature is in beta test and currently only available to the allowlist.
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
        This API is used to view domain information under a site, including acceleration domain names, origin servers, and domain name status. You can view information of all domains under a site, or specify filter conditions to query specific domain information.
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
        Query the list of alias domain names.
        This feature is only supported in the enterprise plan and is currently in beta test. To use it, please [contact us](https://www.tencentcloud.com/contact-us).
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
        This API is on an earlier version. If you want to call it, switch to the latest version. The latest version splits into two APIs: one for querying the Layer 4 proxy instance list and the other for querying Layer 4 forwarding rules. For details, see [Query Layer 4 Proxy Instance List](https://www.tencentcloud.com/document/product/1552/103413?from_cn_redirect=1) and [Query Layer 4 Proxy Forwarding Rule List](https://www.tencentcloud.com/document/product/1552/103412?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplicationProxies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationProxiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAvailableCustomActionsForRuleEngine(
            self,
            request: models.DescribeAvailableCustomActionsForRuleEngineRequest,
            opts: Dict = None,
    ) -> models.DescribeAvailableCustomActionsForRuleEngineResponse:
        """
        Queries the list of available custom configurations for site rule engine operations.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAvailableCustomActionsForRuleEngine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAvailableCustomActionsForRuleEngineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAvailableOriginACLFamily(
            self,
            request: models.DescribeAvailableOriginACLFamilyRequest,
            opts: Dict = None,
    ) -> models.DescribeAvailableOriginACLFamilyResponse:
        """
        This API is used to query detailed information about the origin protection IP range control domain, including the version number and specific IP range information.
        The main difference between standard control domain and streamlined control domain is the number of IP ranges provided. The latter has fewer IP ranges, but has some usage restrictions. For specific restrictions, consult the product. The format description is as follows:
        Standard control domain:
        <li>gaz: standard global control domain;</li>
        <li>mlc: Standard China control domain;</li>
        <li>emc: standard overseas (worldwide excluding China) control domain;</li>
        Streamline the control domain.
        <li>plat-gaz: simplified global control domain;</li>
        <li>plat-mlc: Simplified China control domain;</li>
        <li>plat-emc: Simplified overseas (global excluding China) control domain;</li>
        <li>plat-specific-gaz: custom edition global availability zone control domain;</li>
        <li>plat-specific-mlc: custom edition for controlling the Chinese mainland availability zone control domain;</li>
        <li>plat-specific-emc: custom edition control domain for availability zones worldwide (excluding Chinese mainland);</li>
        Abbreviation description:
        <li>gaz:Global AZ Availability Zone;</li>
        <li>mlc:mainlandChina;</li>
        <li>emc:Exclude mainlandChina.</li>
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAvailableOriginACLFamily"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAvailableOriginACLFamilyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAvailablePlans(
            self,
            request: models.DescribeAvailablePlansRequest,
            opts: Dict = None,
    ) -> models.DescribeAvailablePlansResponse:
        """
        Query the list of available package information for the current account.
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
        Query billing data via this API.
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
        In version management mode, this API is used to obtain detailed version information, including version ID, description, status, creation time, associated configuration group information, and the content of the version configuration file. The version management feature is in beta test and currently only available to the allowlist.
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
        In version management mode, this API is used to query the version list of a specified configuration group. The version management feature is in beta test and currently only available to the allowlist.
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
        This API is used to query content identifiers in batches. They can be filtered by ID, description, status, or tags. Deleted content identifiers queried by status are only retained for three months. This feature is only open in the allowlist.
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
        Query the content management API quota
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
        This API is used to query the custom error page list.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomErrorPages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomErrorPagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomGroup(
            self,
            request: models.DescribeCustomGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomGroupResponse:
        """
        This API is used to query the detailed information of a custom group, including all entries in the group (returned with pagination via Limit/Offset). The DescribeCustomGroups list API returns up to the first 500 entries for each group. To obtain all entries, use this API. The GroupId can be obtained from the response of CreateCustomGroup or by querying DescribeCustomGroups.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomGroupReferences(
            self,
            request: models.DescribeCustomGroupReferencesRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomGroupReferencesResponse:
        """
        This API is used to obtain the security policy configuration that uses a custom group.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomGroupReferences"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomGroupReferencesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomGroups(
            self,
            request: models.DescribeCustomGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomGroupsResponse:
        """
        This API is used to query the list of custom groups under a specified site. This API returns only the first 500 entries of each custom group. To query all entries in a group, use the DescribeSecurityCustomGroup API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDDoSAttackData(
            self,
            request: models.DescribeDDoSAttackDataRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSAttackDataResponse:
        """
        This API is used to query DDoS attack time-series data.
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
        This API is used to query the list of DDoS attack events.
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
        This API is used to query Top-ranked data of DDoS attacks.
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
        This API is used to query exclusive DDoS protection info of a site.
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
        Query the default certificate list
        <p style="color: red;">Note: This earlier version interface is no longer updated. New features will only be provided in the latest version interface. Existing capacities supported by the earlier version interface will not be affected. To query the cert configured for a domain name, please use DescribeAccelerationDomains.</p>
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
        In version management mode, this API is used to query the version release history of production/test environments. The version management feature is in beta test and currently only available to the allowlist.
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
        This API is used to view DNS records under a site, including DNS record names, record types, and record content. It supports specifying filter conditions to query specific DNS records.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDnsRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDnsRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEdgeKVNamespaces(
            self,
            request: models.DescribeEdgeKVNamespacesRequest,
            opts: Dict = None,
    ) -> models.DescribeEdgeKVNamespacesResponse:
        """
        Queries the KV namespace list under a specified site. Supports pagination, sorting, and conditional filtering. Returns basic namespace info, storage capacity utilization, and reference relationships. If no data is found, an empty array is returned.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEdgeKVNamespaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEdgeKVNamespacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEnvironments(
            self,
            request: models.DescribeEnvironmentsRequest,
            opts: Dict = None,
    ) -> models.DescribeEnvironmentsResponse:
        """
        In version management mode, this API is used to query environment information, including the environment ID, type, and current effective version. The version management feature is in beta test and currently only available to the allowlist.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEnvironments"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEnvironmentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFunctionComponentBindings(
            self,
            request: models.DescribeFunctionComponentBindingsRequest,
            opts: Dict = None,
    ) -> models.DescribeFunctionComponentBindingsResponse:
        """
        This API is used to query the component binding list of a specified edge function. It supports pagination and conditional filtering, and returns detailed information such as the bound component type, variable name, and configuration parameters. The currently supported binding component type is KV namespace (kv_namespace).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFunctionComponentBindings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFunctionComponentBindingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFunctionReplicas(
            self,
            request: models.DescribeFunctionReplicasRequest,
            opts: Dict = None,
    ) -> models.DescribeFunctionReplicasResponse:
        """
        This API is used to query the replica list of edge functions.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFunctionReplicas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFunctionReplicasResponse
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
        This API is on an earlier version. EdgeOne has completed a comprehensive upgrade of rule engine APIs. You can use [DescribeL7AccSetting](https://www.tencentcloud.com/document/product/1552/115819?from_cn_redirect=1) and [DescribeL7AccRules](https://www.tencentcloud.com/document/product/1552/115820?from_cn_redirect=1) to obtain detailed configuration of a domain.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostsSetting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostsSettingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIPGroupReferences(
            self,
            request: models.DescribeIPGroupReferencesRequest,
            opts: Dict = None,
    ) -> models.DescribeIPGroupReferencesResponse:
        """
        This API is used to obtain policy settings that use IP grouping.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIPGroupReferences"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIPGroupReferencesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIPRegion(
            self,
            request: models.DescribeIPRegionRequest,
            opts: Dict = None,
    ) -> models.DescribeIPRegionResponse:
        """
        This API is used to query if the IP is an EdgeOne IP.
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
        Queries verification information of a site.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIdentifications"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIdentificationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInferenceAPITokens(
            self,
            request: models.DescribeInferenceAPITokensRequest,
            opts: Dict = None,
    ) -> models.DescribeInferenceAPITokensResponse:
        """
        Queries the list of reasoning API tokens and returns the Token ID, name, content, and creation time. Paging query is supported.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInferenceAPITokens"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInferenceAPITokensResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInferenceDomains(
            self,
            request: models.DescribeInferenceDomainsRequest,
            opts: Dict = None,
    ) -> models.DescribeInferenceDomainsResponse:
        """
        This API is used to query the inference service domain name list and return the Cname address, ownership verification, and certificate information of the domain.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInferenceDomains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInferenceDomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInferenceHardwareSpecifications(
            self,
            request: models.DescribeInferenceHardwareSpecificationsRequest,
            opts: Dict = None,
    ) -> models.DescribeInferenceHardwareSpecificationsResponse:
        """
        This API is used to query the inference hardware specification list and return the CPU, memory, GPU, and video memory configurations of each specification. You can select the required specification from the list when creating a service.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInferenceHardwareSpecifications"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInferenceHardwareSpecificationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInferenceServiceDeploymentLogs(
            self,
            request: models.DescribeInferenceServiceDeploymentLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeInferenceServiceDeploymentLogsResponse:
        """
        This API is used to query the logs of a specified deployment of an inference service, return log content and generation time, and support time range search, pagination, and sorting.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInferenceServiceDeploymentLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInferenceServiceDeploymentLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInferenceServiceDeploymentRecords(
            self,
            request: models.DescribeInferenceServiceDeploymentRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeInferenceServiceDeploymentRecordsResponse:
        """
        This API is used to query the deployment history list of an inference service. It returns the operation type, status, duration, configuration snapshot, and whether it is the currently effective configuration for each deployment. Pagination and sorting are supported.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInferenceServiceDeploymentRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInferenceServiceDeploymentRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInferenceServiceMonitorData(
            self,
            request: models.DescribeInferenceServiceMonitorDataRequest,
            opts: Dict = None,
    ) -> models.DescribeInferenceServiceMonitorDataResponse:
        """
        This API is used to query the monitoring data of inference services, supporting indicators such as CPU, memory, GPU, video memory utilization, and instance count. You can specify the time range and aggregation granularity, and query data from the most recent 30 days.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInferenceServiceMonitorData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInferenceServiceMonitorDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInferenceServices(
            self,
            request: models.DescribeInferenceServicesRequest,
            opts: Dict = None,
    ) -> models.DescribeInferenceServicesResponse:
        """
        This API is used to query the inference service list, support filtering by service name, service ID, and status, and return the service configuration, running state, number of instances, and inference access address.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInferenceServices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInferenceServicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJustInTimeTranscodeTemplates(
            self,
            request: models.DescribeJustInTimeTranscodeTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeJustInTimeTranscodeTemplatesResponse:
        """
        This API is used to retrieve the transcoding template detail list based on the just in time transcoding template name, template type, or unique ID. The returned results include all eligible custom templates and preset templates.
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
        This API is used to query the layer 4 proxy instance list.
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
        This API is used to query the rule list of the [rule engine](https://www.tencentcloud.com/document/product/1552/70901?from_cn_redirect=1).
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
        This API is used to query the global configuration of site acceleration.
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
        This API is used to query the load balancing instance list. The load balancer feature is in beta test. If you need to use it, [contact us](https://www.tencentcloud.com/contact-us).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoadBalancerList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoadBalancerListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogAnalysisDetail(
            self,
            request: models.DescribeLogAnalysisDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeLogAnalysisDetailResponse:
        """
        This API is used to query log analysis details. The data comes from the log data pushed by real-time log push tasks under the site with the destination "log-analysis".
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogAnalysisDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogAnalysisDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogAnalysisDownloadTasks(
            self,
            request: models.DescribeLogAnalysisDownloadTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeLogAnalysisDownloadTasksResponse:
        """
        This API is used to query the log download task list for log analysis. Note: Only download task records from the last three days are retained.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogAnalysisDownloadTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogAnalysisDownloadTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLogAnalysisStatistics(
            self,
            request: models.DescribeLogAnalysisStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeLogAnalysisStatisticsResponse:
        """
        This API is used to query log analysis statistics results. Users append an SQL aggregation statement after the query statement ([retrieval condition] | [SQL statement]). The backend executes the aggregation and returns columnar statistics results (column definition + data row).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLogAnalysisStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLogAnalysisStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMultiPathGateway(
            self,
            request: models.DescribeMultiPathGatewayRequest,
            opts: Dict = None,
    ) -> models.DescribeMultiPathGatewayResponse:
        """
        This API is used to query details of a multi-channel security acceleration gateway, such as name, Gateway ID, IP, port, and type.
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
        This API is used to query lines connected to the multi-channel security acceleration gateway, including direct connections, EdgeOne Layer 4 proxy lines, and custom lines.
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
        This API is used to query the binding relationship between a multi-channel security acceleration gateway instance and origin IP ranges, as well as origin IP range details. If the MultiPathGatewayNextOriginACL field has a return value, synchronize the latest origin IP ranges to the origin server firewall settings.
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
        This API is used to query the available region list of user-created multi-channel security acceleration gateways.
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
        This API is used to query the key for integrating a multi-channel security acceleration gateway. Customers sign with the integration key to access the multi-channel security acceleration gateway.
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
        This API is used to query the list of user-created multi-channel security acceleration gateways. Pagination is supported.
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
        This API is used to query the binding relationship between L7 acceleration domains/L4 proxy instances and origin IP ranges under a site, as well as origin IP range details. If you want to periodically get the latest version of origin IP ranges through an automation script, you can poll this API at a low frequency (once every three days is recommended). If the NextOriginACL field has a return value, synchronize the latest origin IP ranges to the origin server firewall configuration.
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
        This API is used to query the origin server group list.
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
        This API is used to query the health status of origin server groups under a load balancing instance. The load balancer feature is in beta test. If you need to use it, [contact us](https://www.tencentcloud.com/contact-us).
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
        This API is on an earlier version for origin protection queries. EdgeOne comprehensively upgraded the origin protection APIs on June 27, 2025. For details on the new version of the origin protection query API, refer to [DescribeOriginACL](https://www.tencentcloud.com/document/product/1552/120408?from_cn_redirect=1).

        <p style="color: red;">Note: Starting from June 27, 2025, earlier version APIs will stop update and iteration, and new features will only be provided in the new version of APIs. To avoid data field conflicts when using earlier version APIs, migrate to the new version of origin protection APIs as soon as possible.</p>
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
        This API is used to query layer-7 monitoring time series traffic Data. This API is to be deprecated. Please use the <a href="https://www.tencentcloud.com/document/product/1552/80648?from_cn_redirect=1">DescribeTimingL7AnalysisData</a> API.
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
        Query the package information list with pagination.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePlans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePlansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrefetchOriginLimit(
            self,
            request: models.DescribePrefetchOriginLimitRequest,
            opts: Dict = None,
    ) -> models.DescribePrefetchOriginLimitResponse:
        """
        This API is used to query origin-pull rate limits. This feature is in beta test for allowlisted users.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrefetchOriginLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrefetchOriginLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrefetchTasks(
            self,
            request: models.DescribePrefetchTasksRequest,
            opts: Dict = None,
    ) -> models.DescribePrefetchTasksResponse:
        """
        This API is used to query the commit history and execution progress of preheating tasks. Tasks submitted via the CreatePrefetchTasks API can be queried through this API.
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
        This API is used to query submitted URL refresh and directory refresh records and task progress. All tasks submitted via the CreatePurgeTasks API can be queried through this API.
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
        This API is used to query real-time log delivery task list.
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
        This API is on an earlier version for querying rule engine rules. EdgeOne comprehensively upgraded the rule engine APIs on January 21, 2025. For details on the new version API for querying L7 acceleration rules, see [DescribeL7AccRules](https://www.tencentcloud.com/document/product/1552/115820?from_cn_redirect=1).
        <p style="color: red;">Note: Starting from January 21, 2025, the legacy version API will stop update and iteration. New features will only be provided in the new version API. The existing capacity supported by the legacy version API will not be affected. To avoid data field conflicts when using the legacy version API, migrate to the new version rule engine API as soon as possible.</p>
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
        This API is on an earlier version. EdgeOne has completed a comprehensive upgrade of rule engine APIs. For details, see [RuleEngineAction](https://www.tencentcloud.com/document/product/1552/80721?from_cn_redirect=1#RuleEngineAction).
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
        Query API resources under a site.
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
        Query API services under a site.
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
        Query client authentication option configurations.
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
        This API is used to query the configuration information of a security IP group, including its ID, name, and content. In the query result of this API, each IP group returns up to 2,000 IPs or CIDR blocks. If an ultra-large IP group exceeds 2,000 IPs or CIDR blocks, call DescribeSecurityIPGroupContent for paging query.
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
        This API is used to query the IP address list in a specified IP group by page. When the number of IP addresses in an IP group exceeds 2000, you can use this API to perform a paging query to obtain the complete IP address list.
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
        This API is deprecated and will be discontinued on June 30, 2024. Please use the API for querying security IP groups.
        ](https://www.tencentcloud.com/document/product/1552/105866?from_cn_redirect=1).

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
        Query security protection configuration details.
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
        This API is used to query the binding relationship list of a specified policy template.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityTemplateBindings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityTemplateBindingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSharedCNAME(
            self,
            request: models.DescribeSharedCNAMERequest,
            opts: Dict = None,
    ) -> models.DescribeSharedCNAMEResponse:
        """
        This API is used to query the shared CNAME list, supporting fuzzy search, pagination, and sorting.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSharedCNAME"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSharedCNAMEResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTimingFunctionAnalysisData(
            self,
            request: models.DescribeTimingFunctionAnalysisDataRequest,
            opts: Dict = None,
    ) -> models.DescribeTimingFunctionAnalysisDataResponse:
        """
        This API is used to query the time series data of edge function analysis. Note that the data queried by this API has a delay of about 10 minutes. It is recommended to pull data from at least 10 minutes before the current time.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTimingFunctionAnalysisData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTimingFunctionAnalysisDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTimingL4Data(
            self,
            request: models.DescribeTimingL4DataRequest,
            opts: Dict = None,
    ) -> models.DescribeTimingL4DataResponse:
        """
        <p>This API is used to query the L4 time series Data list.</p>
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
        This API is used to query time series data of the L7 domain name business.
        Note:
        1. This API queries data with a delay of about 10 minutes. It is advisable to pull data from 10 minutes before the current time.
        2. This interface returns post-protection traffic request data by default. Users can use `Filters.mitigatedByWebSecurity` to custom query defended data.
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
        This API is used to query L7 cache analysis time series traffic data. This API is to be deprecated. Please use the <a href="https://www.tencentcloud.com/document/product/1552/80648?from_cn_redirect=1">DescribeTimingL7AnalysisData</a> API.
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
        This API is used to query the origin-pull time series data of an L7 domain.
        You can choose to group queries by specifying the query dimension <code>DimensionName</code>, which returns multiple groups of time series data. For detailed directions and usage limits, see [How to Use APIs to Implement Group Query in a Single Call](https://www.tencentcloud.com/document/product/1552/127501?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTimingL7OriginPullData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTimingL7OriginPullDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopFunctionAnalysisData(
            self,
            request: models.DescribeTopFunctionAnalysisDataRequest,
            opts: Dict = None,
    ) -> models.DescribeTopFunctionAnalysisDataResponse:
        """
        This API is used to query the topN data of Edge Functions by a specified dimension. Note that the data returned by this API has a delay of about 10 minutes. We recommend that you query the data generated at least 10 minutes before the current time.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopFunctionAnalysisData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopFunctionAnalysisDataResponse
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
        Note:
        1. This API queries data with a delay of about 10 minutes. It is recommended to pull data from 10 minutes before the current time.
        2. This interface returns post-protection traffic request data by default. Users can use `Filters.mitigatedByWebSecurity` to custom query defended data.
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
        This API is used to query L7 cache analysis topN data. This API is to be deprecated. Please use the <a href="https://www.tencentcloud.com/document/product/1552/80646?from_cn_redirect=1"> DescribeTopL7AnalysisData</a> API.
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
        Queries security policy configuration template details
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
        Queries the security policy configuration template list.
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
        This API is used to query the results of site configuration item import via the site configuration import API.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZoneConfigImportResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZoneConfigImportResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZoneCustomVariables(
            self,
            request: models.DescribeZoneCustomVariablesRequest,
            opts: Dict = None,
    ) -> models.DescribeZoneCustomVariablesResponse:
        """
        This API is used to query site-level custom variable configurations, including variable definitions and variable operations. If not configured, both variable definitions and variable operations return empty lists.

        If needed, call the DescribeL7AccRules API to query rule-level custom variables.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZoneCustomVariables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZoneCustomVariablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZoneSetting(
            self,
            request: models.DescribeZoneSettingRequest,
            opts: Dict = None,
    ) -> models.DescribeZoneSettingResponse:
        """
        This API is on an earlier version. EdgeOne has completed a comprehensive upgrade of rule engine APIs. For details, see [DescribeL7AccSetting](https://www.tencentcloud.com/document/product/1552/115819?from_cn_redirect=1).
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
        This API is used to query site information you have permission to access. You can filter sites based on different query conditions.
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
        This API is used to terminate a billing plan when you need to stop billing for an Edgeone plan.
        > The following conditions must be met to terminate a billing plan:
        1. The plan has expired (except for the Enterprise Edition Plan);
        2. All sites under the package have been shut down or deleted.

        > The site status can be queried through the [Query Site List](https://www.tencentcloud.com/document/product/1552/80713?from_cn_redirect=1) interface.
        A site can be deactivated by switching the site to a closed status through the [Switch Site Status](https://www.tencentcloud.com/document/product/1552/80707?from_cn_redirect=1) interface.
        A site can be deleted by using the Delete Site API.
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
        This API is used to disable origin protection for a site. Once disabled, resources related to the origin will no longer use only the origin IP range provided by origin protection to request your origin, and update notifications on origin IP ranges will stop simultaneously.
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
        This API is used to obtain the offline log download link for a Layer 4 proxy business.
        **Note:** EO stores offline logs and provides a download service only when the offline log feature is enabled. For specific features, see the [document](https://www.tencentcloud.com/document/product/1552/73660?from_cn_redirect=1).
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
        This API is used to obtain the offline log download link for an L7 domain.
        **Note:** EO stores offline logs and provides a download service only when the offline log feature is enabled. For specific features, see the [document](https://www.tencentcloud.com/document/product/1552/73660?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadL7Logs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadL7LogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DummyParseZoneFullConfig(
            self,
            request: models.DummyParseZoneFullConfigRequest,
            opts: Dict = None,
    ) -> models.DummyParseZoneFullConfigResponse:
        """
        This API is used to define the structure of a complete site configuration for reference only. Note: This API does not return actual data.
        """
        
        kwargs = {}
        kwargs["action"] = "DummyParseZoneFullConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DummyParseZoneFullConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EdgeKVDelete(
            self,
            request: models.EdgeKVDeleteRequest,
            opts: Dict = None,
    ) -> models.EdgeKVDeleteResponse:
        """
        This API is used to delete one or more key-value pair data in a specified namespace. Batch deletion supported. Data cannot be recovered after deletion.
        """
        
        kwargs = {}
        kwargs["action"] = "EdgeKVDelete"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EdgeKVDeleteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EdgeKVGet(
            self,
            request: models.EdgeKVGetRequest,
            opts: Dict = None,
    ) -> models.EdgeKVGetResponse:
        """
        This API is used to batch read key values from a specified namespace. It supports querying up to 20 keys in a single query.
        """
        
        kwargs = {}
        kwargs["action"] = "EdgeKVGet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EdgeKVGetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EdgeKVList(
            self,
            request: models.EdgeKVListRequest,
            opts: Dict = None,
    ) -> models.EdgeKVListResponse:
        """
        This API is used to list all keys in the specified namespace, with prefix filtering supported. Cursor-based traversal is implemented, and the next cursor is returned for continued querying. It is suitable for traversing all keys in a namespace.
        """
        
        kwargs = {}
        kwargs["action"] = "EdgeKVList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EdgeKVListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EdgeKVPut(
            self,
            request: models.EdgeKVPutRequest,
            opts: Dict = None,
    ) -> models.EdgeKVPutResponse:
        """
        This API is used to write key-value pair data to a specified namespace, with support for setting expiration time. If the key already exists, the original value is overwritten. If not, a new key-value pair is created.
        """
        
        kwargs = {}
        kwargs["action"] = "EdgeKVPut"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EdgeKVPutResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableOriginACL(
            self,
            request: models.EnableOriginACLRequest,
            opts: Dict = None,
    ) -> models.EnableOriginACLResponse:
        """
        This API is used to enable origin protection for a site for the first time. After it is enabled, EdgeOne will use specific origin-pull IP ranges to pull from the origin for layer-7 acceleration domains/layer-4 proxy instances.
        This API supports two modes: **Automatic Protection Mode** and **Specified Protection Mode**. <li>When **Automatic Protection Mode** is used (L7EnableMode/L4EnableMode is set to all), the acceleration domain list and layer-4 proxy instances under the site will be automatically added to the origin protection list in real time without manual intervention;</li><li>When **Specified Protection Mode** is used (L7EnableMode/L4EnableMode is set to specific), you need to manually specify the resources to be added to origin protection. Unspecified resources will not be added to the origin protection list. If resource adjustment is required, you need to actively call the ModifyOriginACL API to make adjustments.</li>

        Instructions for using the Specified Protection Mode:
        <li>The maximum number of layer-7 acceleration domains that can be submitted at a time is 200, and the maximum number of layer-4 proxy instances is 100. Mixed submission of layer-7 acceleration domains/layer-4 proxy instances is supported, with a maximum total of 200 instances;</li>
        <li>When more than 200 resources need to be enabled, you need to first configure the resources of the first shard through this API, and then configure the remaining shards through the ModifyOriginACL API. For example, if 500 layer-7 acceleration domains need to be added, first use this API to set 200 domains, and then use the ModifyOriginACL API to configure the remaining 300 domains in two batches, with no more than 200 domains per batch.</li>

        Note:
        - When enabling, accounts on the allowlist can select other origin-pull IP range versions, such as the simplified version, to achieve the effect of pulling from the origin with fewer IP ranges.
        - Calling this API is deemed as your agreement to the [Special Agreement on Enabling Origin Protection](https://www.tencentcloud.com/document/product/1552/120141?from_cn_redirect=1);
        - Origin-pull IP ranges are subject to change from time to time. EdgeOne will send notifications 14 days, 7 days, 3 days, and 1 day before the change through one or more methods such as in-site messages, SMS, and emails. To ensure that you can receive notifications of origin-pull IP range changes, make sure that you have selected message notifications related to the EdgeOne product in the [Tencent Cloud Message Center Console](https://console.cloud.tencent.com/message) and configured the correct message recipients. For configuration methods, refer to [Message Subscription Management](https://www.tencentcloud.com/document/product/567/43476?from_cn_redirect=1).
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
        This API is used to export site configuration by users based on desired configuration items. The exported configuration is used for import via the site configuration import API.
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
        After the environment variables are set, they can be used in the function code and function replica code. For details, see [Edge Functions Referencing Environment Variables](https://www.tencentcloud.com/document/product/1552/109151?from_cn_redirect=1#0151fd9a-8b0e-407b-ae37-54553a60ded6).
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
        Used to verify site ownership.
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
        This API is used to quickly import site configuration files. After the import is initiated, the API will return the corresponding task ID (TaskId). Users need to use the site configuration import result query API to obtain the results of this import task.
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
        This API is used to purchase additional quotas when the number of sites bound to your plan, the number of rules under "Web Protection - Custom Rules - Precision Matching Policy", or the rules under "Web Protection - Rate Limiting - Precision Rate Limiting Module" reach the plan's quota limit.
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
        Modify acceleration domain name information
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
        Batch modify accelerated domain status
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
        Modify an alias domain name.
        This feature is only supported in the enterprise plan and is currently in beta test. To use it, please [contact us](https://www.tencentcloud.com/contact-us).
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
        Modify the status of an alias domain name.
        This feature is only supported in the enterprise plan and is currently in beta test. To use it, please [contact us](https://www.tencentcloud.com/contact-us).
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
        This API is on an earlier version. If you want to call it, switch to the latest version. For details, refer to [Modify Layer 4 Proxy Instance].
        ](https://www.tencentcloud.com/document/product/1552/103411?from_cn_redirect=1) .
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
        This API is on an earlier version. If you want to call it, switch to the latest version. For details, see Modifying Layer 4 Proxy Forwarding Rules.
        ](https://www.tencentcloud.com/document/product/1552/103410?from_cn_redirect=1) .
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
        This API is on an earlier version. If you want to call it, switch to the latest version. For details, see Modifying Layer 4 Proxy Forwarding Rule Status.
        ](https://www.tencentcloud.com/document/product/1552/103409?from_cn_redirect=1) .
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
        This API is on an earlier version. If you want to call it, switch to the latest version. For details, see [modify layer 4 proxy instance status](https://www.tencentcloud.com/document/product/1552/103408?from_cn_redirect=1).
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
        Modification content identifier. Only description modification is supported. The feature is open in the allowlist only.
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
        
    async def ModifyCustomGroup(
            self,
            request: models.ModifyCustomGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyCustomGroupResponse:
        """
        This API is used to modify the content of a custom group. GroupType cannot be modified after creation. When modifying entries in the group, you can specify replacement, append, or removal operations through GroupItemOperation.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCustomGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCustomGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDDoSProtection(
            self,
            request: models.ModifyDDoSProtectionRequest,
            opts: Dict = None,
    ) -> models.ModifyDDoSProtectionResponse:
        """
        Modify exclusive DDoS protection for a site.
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
        You can use this API to batch modify DNS records.
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
        You can use this API to batch modify the status of DNS records and enable or disable records in batches.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDnsRecordsStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDnsRecordsStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyEdgeKVNamespace(
            self,
            request: models.ModifyEdgeKVNamespaceRequest,
            opts: Dict = None,
    ) -> models.ModifyEdgeKVNamespaceResponse:
        """
        This API is used to modify the attribute information of a specified KV namespace. Currently, only namespace description modification is supported.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyEdgeKVNamespace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyEdgeKVNamespaceResponse
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
        
    async def ModifyFunctionComponentBindings(
            self,
            request: models.ModifyFunctionComponentBindingsRequest,
            opts: Dict = None,
    ) -> models.ModifyFunctionComponentBindingsResponse:
        """
        Modify the binding relationship between edge functions and components. Four operation modes are supported: bind, bind-override, unbind, and rebind. Manage function component binding relationships by specifying the operation type and component list.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFunctionComponentBindings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFunctionComponentBindingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFunctionReplica(
            self,
            request: models.ModifyFunctionReplicaRequest,
            opts: Dict = None,
    ) -> models.ModifyFunctionReplicaResponse:
        """
        This API is used to modify the content and description of a specified edge function replica.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFunctionReplica"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFunctionReplicaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFunctionRule(
            self,
            request: models.ModifyFunctionRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyFunctionRuleResponse:
        """
        This API is used to modify a trigger rule for an edge function. It supports modifying rule conditions, execution functions, and description. You can first use the DescribeFunctionRules API to get the RuleId of the rule to be modified, then input the modified rule content. The original rule content will be overwritten.
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
        After domain name creation is completed, you can configure a self-owned certificate for the domain name, or alternatively use the free certificate (https://www.tencentcloud.com/document/product/1552/90437?from_cn_redirect=1) offered by EdgeOne.
        If you need to configure a self-owned certificate, upload the certificate to the [SSL certificate console](https://console.cloud.tencent.com/certoverview) first, then import the corresponding certificate ID in this API. For details, see [Deploy self-owned certificates to EdgeOne domain names].
        ](https://www.tencentcloud.com/document/product/1552/88874?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHostsCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHostsCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInferenceService(
            self,
            request: models.ModifyInferenceServiceRequest,
            opts: Dict = None,
    ) -> models.ModifyInferenceServiceResponse:
        """
        Modify an inference service to support updates to the listening port, request path, container image, resource configuration, and description. Only passed parameters will be modified, while unpassed parameters remain unchanged.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInferenceService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInferenceServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL4Proxy(
            self,
            request: models.ModifyL4ProxyRequest,
            opts: Dict = None,
    ) -> models.ModifyL4ProxyResponse:
        """
        This API is used to modify the configuration of a layer 4 proxy instance.
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
        This API is used to enable or disable the status of layer-4 proxy rules, supporting both individual and batch operation.
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
        This API is used to enable or disable an L4 proxy instance.
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
        This API is used to modify a rule in the [rule engine](https://www.tencentcloud.com/document/product/1552/70901?from_cn_redirect=1). Only one rule can be modified at a time.
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
        This API is used to modify the priority of the rule list in the rule engine (https://www.tencentcloud.com/document/product/1552/70901?from_cn_redirect=1). It requires the input of the complete rule ID list under the site ID. The rule ID list can be obtained through the API for querying layer-7 acceleration rules (https://www.tencentcloud.com/document/product/1552/115820?from_cn_redirect=1). The final priority order will be adjusted to the order of the rule ID list, executed from front to back.
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
        This API is used to modify the global configuration of site acceleration.
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
        This API is used to modify multi-channel security acceleration gateway information, such as name, gateway ID, IP, and port.
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
        This API is used to modify the configuration for connecting lines to the multi-channel security acceleration gateway, including EdgeOne Layer 4 proxy lines and custom lines.
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
        This API is used to modify the key for integrating a multi-channel security acceleration gateway. Customers sign with the integration key to access the multi-channel security acceleration gateway. After modification, the original key becomes invalid.
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
        This API is used to update the multi-channel security gateway status.
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
        This API is used to modify the origin protection configuration of a site. The following operations are supported: <li>**Resource addition and deletion**: enable or disable origin-pull from specific origin IP ranges for layer-7 accelerated domains/layer-4 proxy instances. This applies to resource adjustment in **specified protection mode**, and unspecified resources will not change;</li><li>**Mode switching**: adjust the origin protection mode of layer-7 accelerated domains/layer-4 proxy instances. After switching to all, the list of accelerated domains or layer-4 proxy instances under the site will be automatically added to the origin protection list in real time, and subsequent resource changes will also be automatically adjusted without manual intervention; after switching to specific, only the mode is changed, and resources already included in protection remain unchanged;</li><li>**IP range version switching**: for whitelisted customers, it supports switching to other available origin protection IP range versions, such as the simplified version, to reduce origin-pull IP ranges.</li>

        Instructions for specified protection mode:
        <li>The maximum number of layer-7 accelerated domains that can be submitted at a time is 200, and the maximum number of layer-4 proxy instances is 100. Mixed submission of layer-7 accelerated domains/layer-4 proxy instances is supported, with a maximum total of 200 instances;</li>
        <li>When more than 200 resources need to be changed, submit them in batches through this API. For example, to add 500 layer-7 accelerated domains, first submit 200 domains through this API, and then submit the remaining 300 domains in two batches, with no more than 200 domains each time.</li>
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
        Modify origin group configuration. Newly submitted origin records will overwrite the original origin records in the origin group.
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
        
    async def ModifyPrefetchOriginLimit(
            self,
            request: models.ModifyPrefetchOriginLimitRequest,
            opts: Dict = None,
    ) -> models.ModifyPrefetchOriginLimitResponse:
        """
        This API is used to configure origin-pull rate limiting. This feature is in allowlist beta test.
        This API is used to create, modify, and delete preheated origin-pull rate limits. Each account supports up to 100 limits.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrefetchOriginLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrefetchOriginLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRealtimeLogDeliveryTask(
            self,
            request: models.ModifyRealtimeLogDeliveryTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyRealtimeLogDeliveryTaskResponse:
        """
        This API is used to modify the configuration of a real-time log delivery task. It has the following limits:
        <ul>
        <li>The destination type (`TaskType`) of a real-time log delivery task cannot be modified;</li>
        <li>The data delivery type (`LogType`) cannot be modified;</li>
        <li>The data delivery region (`Area`) cannot be modified;</li>
        <li>When the destination of the original real-time log delivery task is Tencent Cloud CLS, the destination details such as the log set and log topic cannot be modified.</li>
        </ul>
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
        This API is on an earlier version for modifying rule engine APIs. EdgeOne comprehensively upgraded rule engine-related APIs on January 21, 2025. For details on the new version API for modifying layer-7 acceleration rules, refer to [ModifyL7AccRule](https://www.tencentcloud.com/document/product/1552/115818?from_cn_redirect=1).
        <p style="color: red;">Note: Starting from January 21, 2025, the legacy version API will stop update and iteration. New features will only be provided in the latest version API. The existing capacity supported by the legacy version API will not be affected. To avoid data field conflict when using the legacy version API, migrate to the latest version rule engine API as soon as possible.</p>
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
        This API is used to modify API resources.
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
        This API is used to modify API services.
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
        Modify client authentication options.
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
        Modifies a security IP group.
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
        Modify Web & Bot security configuration.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySharedCNAME(
            self,
            request: models.ModifySharedCNAMERequest,
            opts: Dict = None,
    ) -> models.ModifySharedCNAMEResponse:
        """
        This API is used to modify a shared CNAME. Currently, it only supports modifying the description and settings of a shared CNAME, and associating an IP SSL domain name with an IP SSL shared CNAME. Once created, a shared CNAME itself cannot be modified. This feature is in beta test.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySharedCNAME"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySharedCNAMEResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWebSecurityTemplate(
            self,
            request: models.ModifyWebSecurityTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyWebSecurityTemplateResponse:
        """
        Modifies a security policy configuration template
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
        Modifies site information.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyZone"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyZoneResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyZoneCustomVariables(
            self,
            request: models.ModifyZoneCustomVariablesRequest,
            opts: Dict = None,
    ) -> models.ModifyZoneCustomVariablesResponse:
        """
        This API is used to manage site-level custom variables, supporting the creation, modification, and deletion of variable definitions and variable operations. The submitted list will override the corresponding existing configuration. To clear the configuration, pass in an empty list. Configuration items not passed in remain unchanged. The default values for variable definitions and variable operations are both empty.

        For rule-level custom variable related operations, call the CreateL7AccRules or ModifyL7AccRule API.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyZoneCustomVariables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyZoneCustomVariablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyZoneSetting(
            self,
            request: models.ModifyZoneSettingRequest,
            opts: Dict = None,
    ) -> models.ModifyZoneSettingResponse:
        """
        This API is on an earlier version. EdgeOne has completed a comprehensive upgrade of rule engine APIs. For details, see [ModifyL7AccSetting](https://www.tencentcloud.com/document/product/1552/115817?from_cn_redirect=1).
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
        Used to enable or disable a site.
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyZoneStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyZoneStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyZoneWorkMode(
            self,
            request: models.ModifyZoneWorkModeRequest,
            opts: Dict = None,
    ) -> models.ModifyZoneWorkModeResponse:
        """
        This API is used to modify the working mode of each configuration module under a site. Each configuration module of a site can enable version management mode or immediate effect mode by configuration group dimension. For details, see Version Management (https://www.tencentcloud.com/document/product/1552/113690?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyZoneWorkMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyZoneWorkModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OperateInferenceDomain(
            self,
            request: models.OperateInferenceDomainRequest,
            opts: Dict = None,
    ) -> models.OperateInferenceDomainResponse:
        """
        Operate an inference service domain name. You can stop, enable, and delete it. Resources cannot be recovered after deletion.
        """
        
        kwargs = {}
        kwargs["action"] = "OperateInferenceDomain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OperateInferenceDomainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OperateInferenceService(
            self,
            request: models.OperateInferenceServiceRequest,
            opts: Dict = None,
    ) -> models.OperateInferenceServiceResponse:
        """
        Operate an inference service. You can stop, start, and delete it. Resources cannot be recovered after deletion.
        """
        
        kwargs = {}
        kwargs["action"] = "OperateInferenceService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OperateInferenceServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RefreshMultiPathGatewaySecretKey(
            self,
            request: models.RefreshMultiPathGatewaySecretKeyRequest,
            opts: Dict = None,
    ) -> models.RefreshMultiPathGatewaySecretKeyResponse:
        """
        This API is used to refresh the key of a multi-channel security acceleration gateway. Customers integrate with the multi-channel security acceleration gateway based on key signatures. Each site contains only one key, which can be used to integrate all gateways under the site. After the key is refreshed, the original key becomes invalid.
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
        When your plan needs to be extended, you can use this API to renew it. Plan renewal is only supported for the Personal, Basic, and Standard Editions.
        > For cost details, refer to [Plan Cost](https://www.tencentcloud.com/document/product/1552/94158?from_cn_redirect=1).
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
        > For differences between different types of Edgeone billing plans, see Edgeone billing plan comparison (https://www.tencentcloud.com/document/product/1552/94165?from_cn_redirect=1)
        For billing package upgrade rules and pricing details, see Edgeone billing package upgrade instructions (https://www.tencentcloud.com/document/product/1552/95291?from_cn_redirect=1)
        If your plan needs to upgrade to the Enterprise Edition, please [contact us](https://www.tencentcloud.com/contact-us).
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
        In CNAME access mode, you need to verify the ownership of the site or domain name. This API is used to trigger the verification. If the site passes ownership verification, no need to verify again when adding domains subsequently. For details, see [Site/Domain Name Ownership Verification](https://www.tencentcloud.com/document/product/1552/70789?from_cn_redirect=1).

        In NS access mode, you can also query through this API whether the NS server switch is successful. For details, see [Modify DNS Server](https://www.tencentcloud.com/document/product/1552/90452?from_cn_redirect=1).
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyOwnership"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyOwnershipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)